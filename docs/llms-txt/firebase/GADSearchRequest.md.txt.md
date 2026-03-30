# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest.md.txt

# GoogleMobileAds Framework Reference

# GADSearchRequest

    @interface GADSearchRequest : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest.html

Specifies parameters for search ads.
- `


  ### [query](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)query)


  ` The search ad query.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *query;

- `


  ### [backgroundColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)backgroundColor)


  ` The search ad background color.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) UIColor *backgroundColor;

- `


  ### [gradientFrom](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)gradientFrom)


  ` The search ad gradient from color.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) UIColor *gradientFrom;

- `


  ### [gradientTo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)gradientTo)


  ` The search ad gradient to color.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) UIColor *gradientTo;

- `


  ### [headerColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)headerColor)


  ` The search ad header color.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) UIColor *headerColor;

- `


  ### [descriptionTextColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)descriptionTextColor)


  ` The search ad description text color.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) UIColor *descriptionTextColor;

- `


  ### [anchorTextColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)anchorTextColor)


  ` The search ad anchor text color.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) UIColor *anchorTextColor;

- `


  ### [fontFamily](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)fontFamily)


  ` The search ad text font family.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *fontFamily;

- `


  ### [headerTextSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)headerTextSize)


  ` The search ad header text size.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) NSUInteger headerTextSize;

- `


  ### [borderColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)borderColor)


  ` The search ad border color.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) UIColor *borderColor;

- `


  ### [borderType](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)borderType)


  ` The search ad border type.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADSearchBorderType.html borderType;

- `


  ### [borderThickness](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)borderThickness)


  ` The search ad border thickness.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) NSUInteger borderThickness;

- `


  ### [customChannels](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)customChannels)


  ` The search ad custom channels.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *customChannels;

- `


  ### [callButtonColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)callButtonColor)


  ` The search ad call button color.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADSearchCallButtonColor.html callButtonColor;

- `


  ### [-setBackgroundSolid:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(im)setBackgroundSolid:)


  ` A solid background color for rendering the ad. The background of the ad
  can either be a solid color, or a gradient, which can be specified through
  setBackgroundGradientFrom:toColor: method. If both solid and gradient
  background is requested, only the latter is considered.

  #### Declaration

  Objective-C

      - (void)setBackgroundSolid:(nonnull UIColor *)color;

- `


  ### [-setBackgroundGradientFrom:toColor:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(im)setBackgroundGradientFrom:toColor:)


  ` A linear gradient background color for rendering the ad. The background of
  the ad can either be a linear gradient, or a solid color, which can be
  specified through setBackgroundSolid method. If both solid and gradient
  background is requested, only the latter is considered.

  #### Declaration

  Objective-C

      - (void)setBackgroundGradientFrom:(nonnull UIColor *)from
                                toColor:(nonnull UIColor *)toColor;