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
		self.output_file_name = output_file_name
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
		self.currentFile = self.output_file_h
		self.write_line('//')
		self.write_line('//  ' + self.output_file_name + '.h')
		self.write_line('//  putong')
		self.write_line('//  Created by liyingpeng on ' + time.strftime("%Y/%m/%d", time.localtime())  + '.')
		self.write_line('//  Copyright © ' + time.strftime("%Y", time.localtime()) + ' P1. All rights reserved.')
		self.write_line('//')
		self.write_blank_lines(1)
		self.write_line('#import <UIKit/UIKit.h>')
		self.write_blank_lines(1)
		self.write_line('NS_ASSUME_NONNULL_BEGIN')
		self.write_blank_lines(1)
		self.write_line('@interface ' + self.output_file_name + ' : UIView')
		self.write_blank_lines(1)
		self.write_line('@end')
		self.write_blank_lines(1)
		self.write_line('NS_ASSUME_NONNULL_END')

	def generate_m_file(self):
		self.currentFile = self.output_file_m
		self.write_line('//')
		self.write_line('//  ' + self.output_file_name + '.m')
		self.write_line('//  putong')
		self.write_line('//  Created by liyingpeng on ' + time.strftime("%Y/%m/%d", time.localtime())  + '.')
		self.write_line('//  Copyright © ' + time.strftime("%Y", time.localtime()) + ' P1. All rights reserved.')
		self.write_line('//')
		self.write_blank_lines(1)
		self.write_line('#import "' + self.output_file_name + '.h"')
		self.generateBasicImport()
		self.write_blank_lines(1)
		self.write_line('@interface ' + self.output_file_name + ' ()')
		self.write_blank_lines(1)
		self.generatePropertyListFor(self.parse_tree.pair())
		self.write_blank_lines(1)
		self.write_line('@end')
		self.write_blank_lines(1)
		self.write_line('@implementation ' + self.output_file_name)
		self.write_blank_lines(1)
		self.generateInit()
		self.write_blank_lines(1)
		self.generateSetupviewsFor(self.parse_tree.pair())
		self.write_blank_lines(1)
		self.generateUpdateModel()
		self.write_blank_lines(1)
		self.write_line('#pragma mark - property getters')
		self.write_blank_lines(1)
		self.generateLazilyLoadPropertiesFor(self.parse_tree.pair())
		self.write_line('@end')
		pass

	def generateBasicImport(self):
		self.write_line('#import "UIColor+PUGHex.h"')
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

	def generateSetupviewsFor(self, controlList):
		self.write_line('- (void)setupSubviews {')
		self.push_indent()
		self.writeAddSubviewsForControls(controlList)
		self.pop_indent()
		self.write_line('}')
		pass

	def writeAddSubviewsForControls(self, controlList):
		for control in controlList:
			subviews = self.subviewsForControl(control)
			if subviews is not None:
				self.write_blank_lines(1)
				self.write_line('[self addSubview:self.' + eval(control.key().getText()) + '];')
				self.writeAddSubviewsForControls(subviews)
				self.write_blank_lines(1)
			else:
				self.write_line('[self addSubview:self.' + eval(control.key().getText()) + '];')
		pass

	def generatePropertyListFor(self, controlList):
		for control in controlList:
			subviews = self.subviewsForControl(control)
			if subviews is not None:
				self.write_blank_lines(1)
				self.write_line('@property (nonatomic, strong) ' + self.parseControlTypeString(control) + ' *' + eval(control.key().getText()) + ';')
				self.generatePropertyListFor(subviews)
				self.write_blank_lines(1)
			else:
				self.write_line('@property (nonatomic, strong) ' + self.parseControlTypeString(control) + ' *' + eval(control.key().getText()) + ';')
		pass

	def generateLazilyLoadPropertiesFor(self, control_list):
		for control in control_list:
			propertyName = eval(control.key().getText())
			instanceName = '_' + propertyName

			self.write_line('- (' + self.parseControlTypeString(control) + ' *)' + propertyName + ' {')
			self.push_indent()
			self.write_line('if (!' + instanceName + ') {')
			self.push_indent()
			self.write_line(instanceName + ' = [' + self.parseControlTypeString(control) + ' new];')

			properties = self.propertiesForControl(control)
			for property in properties:
				propertyName = eval(property.key().getText())
				propertyValue = eval(property.value().getText())
				if propertyName == "subviews":
					subviews = property.value().obj().pair()
					continue
					
				if propertyName == "color" or propertyName == "backgroundColor" or propertyName == "textColor":
					self.setColorForControl(instanceName, propertyName, propertyValue)
				elif propertyName == "font":
					self.setFontForControl(instanceName, propertyName, propertyValue)
				elif propertyValue == "false" or propertyValue == "true":
					self.setBoolForControl(instanceName, propertyName, propertyValue)
				elif isinstance(propertyValue, int) or isinstance(propertyValue, float):
					self.write_line(instanceName + '.' + propertyName + ' = ' + str(propertyValue) + ';')
				elif isinstance(propertyValue, str):
					self.write_line(instanceName + '.' + propertyName + ' = @"' + propertyValue + '";')

			self.pop_indent()
			self.write_line('}')
			self.write_line('return _' + propertyName + ';')
			self.pop_indent()
			self.write_line('}')
			self.write_blank_lines(1)

			subviews = self.subviewsForControl(control)
			if subviews is not None:
				self.generateLazilyLoadPropertiesFor(subviews)
		pass

	def generateUpdateModel(self):
		self.write_line('- (void)updateWithModel:(id)model {')
		self.push_indent()
			
		self.pop_indent()
		self.write_line('}')
		pass

	def setColorForControl(self, instanceName, propertyName, propertyValue):
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

	def setFontForControl(self, instanceName, propertyName, propertyValue):
		self.write_line(instanceName + '.' + propertyName + ' = mSystemFont(' + str(propertyValue) + ');')
		pass

	def setBoolForControl(self, instanceName, propertyName, propertyValue):
		if propertyValue == "false":
			self.write_line(instanceName + '.' + propertyName + ' = NO;')
		elif propertyValue == "true":
			self.write_line(instanceName + '.' + propertyName + ' = YES;')
		pass

	def parseControlTypeString(self, control):
		controlType = self.typeForControl(control)
		if controlType == "label":
			return "UILabel"
		elif controlType == "button":
			return "UIButton"
		elif controlType == "image":
			return "UIImageView"
		elif controlType == "view":
			return "UIView"
		return None

	def typeForControl(self, control):
		for pairItem in control.value().obj().pair():
			if eval(pairItem.key().getText()) == "type":
				return eval(pairItem.value().getText())
		return None

	def propertiesForControl(self, control):
		for pairItem in control.value().obj().pair():
			if eval(pairItem.key().getText()) == "properties":
				return pairItem.value().obj().pair()
		return None
	
	def subviewsForControl(self, control):
		for pairItem in control.value().obj().pair():
			if eval(pairItem.key().getText()) == "subviews":
				return pairItem.value().obj().pair()
		return None


