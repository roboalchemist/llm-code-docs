# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest.md.txt

# GoogleMobileAds Framework Reference

# GADDynamicHeightSearchRequest

    @interface GADDynamicHeightSearchRequest : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest.html

Use to configure Custom Search Ad (CSA) ad requests. A dynamic height search banner can contain
multiple ads and the height is set dynamically based on the ad contents. Please cross-reference
the property sections and properties with the official reference document:
<https://developers.google.com/custom-search-ads/docs/reference>
[## Required](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Required)

- `


  ### [query](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)query)


  ` The CSA query parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *query;

- `


  ### [adPage](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)adPage)


  ` The CSA adPage parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) NSInteger adPage;

[## Configuration Settings](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Configuration%20Settings)

- `


  ### [adTestEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)adTestEnabled)


  ` Indicates whether the CSA adTest parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL adTestEnabled;

- `


  ### [channel](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)channel)


  ` The CSA channel parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *channel;

- `


  ### [hostLanguage](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)hostLanguage)


  ` The CSA hl parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *hostLanguage;

[## Layout and Styling](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Layout%20and%20Styling)

- `


  ### [locationExtensionTextColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)locationExtensionTextColor)


  ` The CSA colorLocation parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable)
          NSString *locationExtensionTextColor;

- `


  ### [locationExtensionFontSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)locationExtensionFontSize)


  ` The CSA fontSizeLocation parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat locationExtensionFontSize;

[## Ad Extensions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Ad%20Extensions)

- `


  ### [clickToCallExtensionEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)clickToCallExtensionEnabled)


  ` Indicates whether the CSA clickToCall parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL clickToCallExtensionEnabled;

- `


  ### [locationExtensionEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)locationExtensionEnabled)


  ` Indicates whether the CSA location parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL locationExtensionEnabled;

- `


  ### [plusOnesExtensionEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)plusOnesExtensionEnabled)


  ` Indicates whether the CSA plusOnes parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL plusOnesExtensionEnabled;

- `


  ### [sellerRatingsExtensionEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)sellerRatingsExtensionEnabled)


  ` Indicates whether the CSA sellerRatings parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL sellerRatingsExtensionEnabled;

- `


  ### [siteLinksExtensionEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)siteLinksExtensionEnabled)


  ` Indicates whether the CSA siteLinks parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL siteLinksExtensionEnabled;

[## Required](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Required2)

- `


  ### [CSSWidth](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)CSSWidth)


  ` The CSA width parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *CSSWidth;

- `


  ### [numberOfAds](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)numberOfAds)


  ` The CSA number parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) NSInteger numberOfAds;

[## Font](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Font)

- `


  ### [fontFamily](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)fontFamily)


  ` The CSA fontFamily parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *fontFamily;

- `


  ### [attributionFontFamily](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)attributionFontFamily)


  ` The CSA fontFamilyAttribution parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *attributionFontFamily;

- `


  ### [annotationFontSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)annotationFontSize)


  ` The CSA fontSizeAnnotation parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat annotationFontSize;

- `


  ### [attributionFontSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)attributionFontSize)


  ` The CSA fontSizeAttribution parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat attributionFontSize;

- `


  ### [descriptionFontSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)descriptionFontSize)


  ` The CSA fontSizeDescription parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat descriptionFontSize;

- `


  ### [domainLinkFontSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)domainLinkFontSize)


  ` The CSA fontSizeDomainLink parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat domainLinkFontSize;

- `


  ### [titleFontSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)titleFontSize)


  ` The CSA fontSizeTitle parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat titleFontSize;

[## Color](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Color)

- `


  ### [adBorderColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)adBorderColor)


  ` The CSA colorAdBorder parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *adBorderColor;

- `


  ### [adSeparatorColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)adSeparatorColor)


  ` The CSA colorAdSeparator parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *adSeparatorColor;

- `


  ### [annotationTextColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)annotationTextColor)


  ` The CSA colorAnnotation parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *annotationTextColor;

- `


  ### [attributionTextColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)attributionTextColor)


  ` The CSA colorAttribution parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *attributionTextColor;

- `


  ### [backgroundColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)backgroundColor)


  ` The CSA colorBackground parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *backgroundColor;

- `


  ### [borderColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)borderColor)


  ` The CSA colorBorder parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *borderColor;

- `


  ### [domainLinkColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)domainLinkColor)


  ` The CSA colorDomainLink parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *domainLinkColor;

- `


  ### [textColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)textColor)


  ` The CSA colorText parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *textColor;

- `


  ### [titleLinkColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)titleLinkColor)


  ` The CSA colorTitleLink parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *titleLinkColor;

[## General Formatting](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/General%20Formatting)

- `


  ### [adBorderCSSSelections](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)adBorderCSSSelections)


  ` The CSA adBorderSelections parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *adBorderCSSSelections;

- `


  ### [adjustableLineHeight](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)adjustableLineHeight)


  ` The CSA adjustableLineHeight parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat adjustableLineHeight;

- `


  ### [attributionBottomSpacing](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)attributionBottomSpacing)


  ` The CSA attributionSpacingBelow parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat attributionBottomSpacing;

- `


  ### [borderCSSSelections](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)borderCSSSelections)


  ` The CSA borderSelections parameter.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *borderCSSSelections;

- `


  ### [titleUnderlineHidden](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)titleUnderlineHidden)


  ` Indicates whether the CSA noTitleUnderline parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL titleUnderlineHidden;

- `


  ### [boldTitleEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)boldTitleEnabled)


  ` Indicates whether the CSA titleBold parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL boldTitleEnabled;

- `


  ### [verticalSpacing](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)verticalSpacing)


  ` The CSA verticalSpacing parameter.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) CGFloat verticalSpacing;

[## Ad Extensions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/Ad%20Extensions2)

- `


  ### [detailedAttributionExtensionEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)detailedAttributionExtensionEnabled)


  ` Indicates whether the CSA detailedAttribution parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic)
          BOOL detailedAttributionExtensionEnabled;

- `


  ### [longerHeadlinesExtensionEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(py)longerHeadlinesExtensionEnabled)


  ` Indicates whether the CSA longerHeadlines parameter is enabled.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL longerHeadlinesExtensionEnabled;

- `


  ### [-setAdvancedOptionValue:forKey:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest#/c:objc(cs)GADDynamicHeightSearchRequest(im)setAdvancedOptionValue:forKey:)


  ` Sets an advanced option value for a specified key. The value must be an NSString or NSNumber.

  #### Declaration

  Objective-C

      - (void)setAdvancedOptionValue:(nonnull id)value forKey:(nonnull NSString *)key;