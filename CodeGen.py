#!/usr/bin/python
# coding:utf-8
import os

import errno
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

class CodeGen:
	def __init__(self, output_file_name, output_directory_path, parse_tree):
		if not os.path.exists(output_directory_path):
			try:
				os.makedirs(output_directory_path)
			except OSError as exc:  # Python >2.5
				if exc.errno == errno.EEXIST and os.path.isdir(output_directory_path):
					pass
				else:
					raise
		self.parse_tree = parse_tree
		self.output_file_m = open(os.path.join(output_directory_path, output_file_name + '.m'), 'w')
		self.output_file_h = open(os.path.join(output_directory_path, output_file_name + '.h'), 'w')
		self.currentFile = self.output_file_h
		self.indent = 0

	def write_line(self, text):
		# 1 indent = 4 blank space
		indent = reduce(lambda so_far, so_good: so_far + '    ', range(0, self.indent), '')
		# print indent + text
		self.currentFile.write((indent + text) + '\n')

	def write_blank_lines(self, count):
		if count <= 0:
			return
		blank_lines = reduce(lambda so_far, so_good: so_far + '\n', range(0, count - 1), '')
		self.write_line(blank_lines)

	def push_indent(self):
		self.indent += 1

	def pop_indent(self):
		self.indent -= 1

	def generate_entry(self):
		self.generate_h_file()
		self.generate_m_file()

	def generate_h_file(self):
		filename = eval(self.parse_tree.filename().getText())
		self.currentFile = self.output_file_h
		self.write_line('//')
		self.write_line('//  ' + filename + '.h')
		self.write_line('//  putong')
		self.write_line('//  Created by liyingpeng on ' + time.strftime("%Y/%m/%d", time.localtime())  + '.')
		self.write_line('//  Copyright © ' + time.strftime("%Y", time.localtime()) + ' P1. All rights reserved.')
		self.write_line('//')
		self.write_blank_lines(1)
		self.write_line('#import <UIKit/UIKit.h>')
		self.write_blank_lines(1)
		self.write_line('NS_ASSUME_NONNULL_BEGIN')
		self.write_blank_lines(1)
		self.write_line('@interface ' + filename + ' : UIView')
		self.write_blank_lines(1)
		self.write_line('@end')
		self.write_blank_lines(1)
		self.write_line('NS_ASSUME_NONNULL_END')

	def generate_m_file(self):
		self.currentFile = self.output_file_m
		filename = eval(self.parse_tree.filename().getText())
		self.write_line('//')
		self.write_line('//  ' + filename + '.m')
		self.write_line('//  putong')
		self.write_line('//  Created by liyingpeng on ' + time.strftime("%Y/%m/%d", time.localtime())  + '.')
		self.write_line('//  Copyright © ' + time.strftime("%Y", time.localtime()) + ' P1. All rights reserved.')
		self.write_line('//')
		self.write_blank_lines(1)
		self.write_line('#import "' + filename + '.h"')
		self.generateBasicImport()
		self.write_blank_lines(1)
		self.write_line('@interface ' + filename + ' ()')
		self.write_blank_lines(1)
		self.generatePropertyList()
		self.write_blank_lines(1)
		self.write_line('@end')
		self.write_blank_lines(1)
		self.write_line('@implementation ' + filename)
		self.write_blank_lines(1)
		self.generateInit()
		self.write_blank_lines(1)
		self.generateSetupviews()
		self.write_blank_lines(1)
		self.generateUpdateModel()
		self.write_blank_lines(1)
		self.write_line('#pragma mark - property getters')
		self.write_blank_lines(1)
		self.generateLazilyLoadProperties()
		self.write_line('@end')
		pass

	def generateInit(self):
		self.write_line('- (instancetype)init')
		self.write_line('{')
		self.push_indent()
		self.write_line('self = [super init];')
		self.write_line('if (self) {')
		self.push_indent()
		self.write_line('[self setupSubviews];')
		self.pop_indent()
		self.write_line('}')
		self.write_line('return self;')
		self.pop_indent()
		self.write_line('}')
		pass

	def generateSetupviews(self):
		self.write_line('- (void)setupSubviews {')
		self.push_indent()
		for control in self.controlList():
			self.write_line('[self addSubview:self.' + eval(control.identifier().getText()) + '];')
		pass
		self.pop_indent()
		self.write_line('}')
		pass

	def controlList(self):
		return self.parse_tree.properties().oneControl()

	def generatePropertyList(self):
		for control in self.controlList():
			self.write_line('@property (nonatomic, strong) ' + self.parseControlTypeString(control) + ' *' + eval(control.identifier().getText()) + ';')
		pass

	def parseControlTypeString(self, control):
		controlType = eval(control.controlType().getText())
		if controlType == "label":
			return "UILabel"
		elif controlType == "button":
			return "UIButton"
		elif controlType == "image":
			return "UIImageView"
		elif controlType == "view":
			return "UIView"
		return "None"
		pass

	def generateLazilyLoadProperties(self):
		for control in self.controlList():
			propertyName = eval(control.identifier().getText())
			instanceName = '_' + propertyName
			self.write_line('- (' + self.parseControlTypeString(control) + ' *)' + propertyName + ' {')
			self.push_indent()
			self.write_line('if (!' + instanceName + ') {')
			self.push_indent()
			self.write_line(instanceName + ' = [' + self.parseControlTypeString(control) + ' new];')

			self.setPropertyFor(control, instanceName)

			self.pop_indent()
			self.write_line('}')
			self.write_line('return _' + propertyName + ';')
			self.pop_indent()
			self.write_line('}')
			self.write_blank_lines(1)
		pass

	def generateUpdateModel(self):
		self.write_line('- (void)updateWithModel:(id)model {')
		self.push_indent()
			
		self.pop_indent()
		self.write_line('}')
		pass

	def setPropertyFor(self, control, instanceName):
		properties = control.uiKitProperties().oneProperty()
		for property in properties:
			propertyName = eval(property.propertyName().getText())
			propertyValue = eval(property.value().getText())
			print type(propertyValue)
			if propertyName == "color" or propertyName == "backgroundColor" or propertyName == "textColor":
				self.setColorValueFor(instanceName, propertyName, propertyValue)
			elif propertyName == "font":
				self.write_line(instanceName + '.' + propertyName + ' = mSystemFont(' + str(propertyValue) + ');')
			elif isinstance(propertyValue, int) or isinstance(propertyValue, float):
				self.write_line(instanceName + '.' + propertyName + ' = @(' + str(propertyValue) + ');')
			elif isinstance(propertyValue, str):
				self.write_line(instanceName + '.' + propertyName + ' = @"' + propertyValue + '";')
		pass

	def setColorValueFor(self, instanceName, propertyName, propertyValue):
		if isinstance(propertyValue, list):
			if len(propertyValue) == 3:
				self.write_line(instanceName + '.' + propertyName + ' = mRGBColor(' + str(propertyValue[0]) + ', ' + str(propertyValue[1]) + ', ' + str(propertyValue[2]) + ');')
			elif len(propertyValue) == 4:
				self.write_line(instanceName + '.' + propertyName + ' = mRGBAColor(' + str(propertyValue[0]) + ', ' + str(propertyValue[1]) + ', ' + str(propertyValue[2]) + ', ' + str(propertyValue[3]) + ');')
			else:
				pass
		else:
			self.write_line(instanceName + '.' + propertyName + ' = [UIColor colorWithHexString:@"' + propertyValue + '"];')
		pass

	def setBoolValueFor(self, instanceName, propertyName, propertyValue):
		pass

	def generateBasicImport(self):
		self.write_line('#import "UIColor+PUGHex.h"')
		pass

