//
//  PUGLiveUserProfileView.m
//  putong
//  Created by liyingpeng on 2019/08/19.
//  Copyright © 2019 P1. All rights reserved.
//

#import "PUGLiveUserProfileView.h"
#import "UIColor+PUGHex.h"

@interface PUGLiveUserProfileView ()

@property (nonatomic, strong) UILabel *titleLabel;
@property (nonatomic, strong) UILabel *subTitleLabel;
@property (nonatomic, strong) UIView *titleView;
@property (nonatomic, strong) UIButton *titleButton;
@property (nonatomic, strong) UIImageView *titleImage;

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
    [self addSubview:self.titleLabel];
    [self addSubview:self.subTitleLabel];
    [self addSubview:self.titleView];
    [self addSubview:self.titleButton];
    [self addSubview:self.titleImage];
}

- (void)updateWithModel:(id)model {
}

#pragma mark - property getters

- (UILabel *)titleLabel {
    if (!_titleLabel) {
        _titleLabel = [UILabel new];
        _titleLabel.color = [UIColor colorWithHexString:@"ffffff"];
        _titleLabel.font = mSystemFont(123);
        _titleLabel.text = @"1234";
    }
    return _titleLabel;
}

- (UILabel *)subTitleLabel {
    if (!_subTitleLabel) {
        _subTitleLabel = [UILabel new];
        _subTitleLabel.color = mRGBAColor(123, 123, 123, 1.0);
        _subTitleLabel.layer.cornerRadius = 4.0;
        _subTitleLabel.layer.masksToBounds = NO;
        _subTitleLabel.font = mSystemFont(2123);
        _subTitleLabel.text = @"1234";
    }
    return _subTitleLabel;
}

- (UIView *)titleView {
    if (!_titleView) {
        _titleView = [UIView new];
        _titleView.color = mRGBAColor(123, 123, 123, 1.0);
        _titleView.layer.cornerRadius = 4.0;
        _titleView.layer.masksToBounds = NO;
    }
    return _titleView;
}

- (UIButton *)titleButton {
    if (!_titleButton) {
        _titleButton = [UIButton new];
        _titleButton.color = mRGBAColor(123, 123, 123, 1.0);
        _titleButton.layer.cornerRadius = 4.0;
        _titleButton.layer.masksToBounds = NO;
    }
    return _titleButton;
}

- (UIImageView *)titleImage {
    if (!_titleImage) {
        _titleImage = [UIImageView new];
        _titleImage.color = mRGBAColor(123, 123, 123, 1.0);
        _titleImage.layer.cornerRadius = 4.0;
        _titleImage.layer.masksToBounds = NO;
    }
    return _titleImage;
}

@end
