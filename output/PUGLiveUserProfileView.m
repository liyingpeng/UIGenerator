//
//  PUGLiveUserProfileView.m
//  putong
//  Created by liyingpeng on 2019/08/20.
//  Copyright © 2019 P1. All rights reserved.
//

#import "PUGLiveUserProfileView.h"
#import "UIColor+PUGHex.h"

@interface PUGLiveUserProfileView ()

@property (nonatomic, strong) UILabel *label1;

@property (nonatomic, strong) UIView *container;
@property (nonatomic, strong) UILabel *subLabel;
@property (nonatomic, strong) UIButton *subButton;

@property (nonatomic, strong) UIView *subContainer;
@property (nonatomic, strong) UILabel *subLabel2;
@property (nonatomic, strong) UIButton *subButton2;


@property (nonatomic, strong) UIView *view;
@property (nonatomic, strong) UIButton *button;
@property (nonatomic, strong) UIImageView *image;

@end

@implementation PUGLiveUserProfileView

- (instancetype)init
{
    self = [super init];
    if (self) {
        [self setupSubviews];
    }
    return self;
}

- (void)setupSubviews {
    [self addSubview:self.label1];
    
    [self addSubview:self.container];
    [self addSubview:self.subLabel];
    [self addSubview:self.subButton];
    
    [self addSubview:self.subContainer];
    [self addSubview:self.subLabel2];
    [self addSubview:self.subButton2];
    
    
    [self addSubview:self.view];
    [self addSubview:self.button];
    [self addSubview:self.image];
}

- (void)updateWithModel:(id)model {
}

#pragma mark - property getters

- (UILabel *)label1 {
    if (!_label1) {
        _label1 = [UILabel new];
        _label1.color = [UIColor colorWithHexString:@"ffffff"];
        _label1.font = mSystemFont(123);
        _label1.text = @"1234";
    }
    return _text;
}

- (UIView *)container {
    if (!_container) {
        _container = [UIView new];
        _container.color = mRGBAColor(123, 123, 123, 1.0);
        _container.layer.cornerRadius = 4.0;
        _container.layer.masksToBounds = NO;
    }
    return _layer.masksToBounds;
}

- (UILabel *)subLabel {
    if (!_subLabel) {
        _subLabel = [UILabel new];
        _subLabel.color = [UIColor colorWithHexString:@"ffffff"];
        _subLabel.font = mSystemFont(123);
        _subLabel.text = @"1234";
    }
    return _text;
}

- (UIButton *)subButton {
    if (!_subButton) {
        _subButton = [UIButton new];
        _subButton.color = [UIColor colorWithHexString:@"ffffff"];
    }
    return _color;
}

- (UIView *)subContainer {
    if (!_subContainer) {
        _subContainer = [UIView new];
        _subContainer.backgroundColor = [UIColor colorWithHexString:@"ffffff"];
    }
    return _backgroundColor;
}

- (UILabel *)subLabel2 {
    if (!_subLabel2) {
        _subLabel2 = [UILabel new];
        _subLabel2.color = [UIColor colorWithHexString:@"ffffff"];
        _subLabel2.font = mSystemFont(123);
        _subLabel2.text = @"1234";
    }
    return _text;
}

- (UIButton *)subButton2 {
    if (!_subButton2) {
        _subButton2 = [UIButton new];
        _subButton2.color = [UIColor colorWithHexString:@"ffffff"];
    }
    return _color;
}

- (UIView *)view {
    if (!_view) {
        _view = [UIView new];
        _view.color = mRGBAColor(123, 123, 123, 1.0);
        _view.layer.cornerRadius = 4.0;
        _view.layer.masksToBounds = NO;
    }
    return _layer.masksToBounds;
}

- (UIButton *)button {
    if (!_button) {
        _button = [UIButton new];
        _button.color = mRGBAColor(123, 123, 123, 1.0);
        _button.layer.cornerRadius = 4.0;
        _button.layer.masksToBounds = NO;
    }
    return _layer.masksToBounds;
}

- (UIImageView *)image {
    if (!_image) {
        _image = [UIImageView new];
        _image.color = mRGBAColor(123, 123, 123, 1.0);
        _image.layer.cornerRadius = 4.0;
        _image.layer.masksToBounds = NO;
    }
    return _layer.masksToBounds;
}

@end
