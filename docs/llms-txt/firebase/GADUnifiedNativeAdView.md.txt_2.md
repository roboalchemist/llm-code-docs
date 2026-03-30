# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAdView

    @interface GADUnifiedNativeAdView : UIView

Base class for native ad views. Your native ad view must be a subclass of this class and must
call superclass methods for all overridden methods.
- `


  ### [nativeAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)nativeAd)


  ` This property must point to the unified native ad object rendered by this ad view.

  #### Declaration

  Objective-C

      @property (readwrite, strong, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html *nativeAd;

- `


  ### [headlineView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)headlineView)


  ` Weak reference to your ad view's headline asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *headlineView;

- `


  ### [callToActionView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)callToActionView)


  ` Weak reference to your ad view's call to action asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *callToActionView;

- `


  ### [iconView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)iconView)


  ` Weak reference to your ad view's icon asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *iconView;

- `


  ### [bodyView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)bodyView)


  ` Weak reference to your ad view's body asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *bodyView;

- `


  ### [storeView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)storeView)


  ` Weak reference to your ad view's store asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *storeView;

- `


  ### [priceView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)priceView)


  ` Weak reference to your ad view's price asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *priceView;

- `


  ### [imageView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)imageView)


  ` Weak reference to your ad view's image asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *imageView;

- `


  ### [starRatingView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)starRatingView)


  ` Weak reference to your ad view's star rating asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *starRatingView;

- `


  ### [advertiserView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)advertiserView)


  ` Weak reference to your ad view's advertiser asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *advertiserView;

- `


  ### [mediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)mediaView)


  ` Weak reference to your ad view's media asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaView.html *mediaView;

- `


  ### [adChoicesView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)adChoicesView)


  ` Weak reference to your ad view's AdChoices view. Must set adChoicesView before setting
  nativeAd, otherwise AdChoices will be rendered according to the preferredAdChoicesPosition
  defined in GADNativeAdViewAdOptions.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdChoicesView *adChoicesView;