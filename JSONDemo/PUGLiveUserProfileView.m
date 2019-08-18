//
//  PUGLiveUserProfileView.m
//  putong
//  Created by liyingpeng on 2019/08/18.
//  Copyright © 2019 P1. All rights reserved.
//

#import "PUGLiveUserProfileView.h"
#import "UIColor+PUGHex.h"

@interface PUGLiveUserProfileView ()

@property (nonatomic, strong) UILabel *titleLabel;
@property (nonatomic, strong) UILabel *subTitleLabel;

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
        _subTitleLabel.layer.cornerRadius = @(4.0);
        _subTitleLabel.layer.masksToBounds = @"false";
        _subTitleLabel.font = mSystemFont(2123);
        _subTitleLabel.text = @"1234";
    }
    return _subTitleLabel;
}

@end
