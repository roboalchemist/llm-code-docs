# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAppInstallAdView


    @interface GADNativeAppInstallAdView : UIView

Base class for app install ad views. Your app install ad view must be a subclass of this class
and must call superclass methods for all overriden methods.
- `


  ### [nativeAppInstallAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)nativeAppInstallAd)


  ` This property must point to the native app install ad object rendered by this ad view.

  #### Declaration

  Objective-C

      @property (readwrite, strong, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd.html *nativeAppInstallAd;

- `


  ### [headlineView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)headlineView)


  ` Weak reference to your ad view's headline asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *headlineView;

- `


  ### [callToActionView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)callToActionView)


  ` Weak reference to your ad view's call to action asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *callToActionView;

- `


  ### [iconView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)iconView)


  ` Weak reference to your ad view's icon asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *iconView;

- `


  ### [bodyView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)bodyView)


  ` Weak reference to your ad view's body asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *bodyView;

- `


  ### [storeView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)storeView)


  ` Weak reference to your ad view's store asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *storeView;

- `


  ### [priceView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)priceView)


  ` Weak reference to your ad view's price asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *priceView;

- `


  ### [imageView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)imageView)


  ` Weak reference to your ad view's image asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *imageView;

- `


  ### [starRatingView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)starRatingView)


  ` Weak reference to your ad view's star rating asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *starRatingView;

- `


  ### [mediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)mediaView)


  ` Weak reference to your ad view's media asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaView.html *mediaView;

- `


  ### [adChoicesView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)adChoicesView)


  ` Weak reference to your ad view's AdChoices view. Must set adChoicesView before setting
  nativeAppInstallAd, otherwise AdChoices will be rendered in the publisher's
  preferredAdChoicesPosition as defined in GADNativeAdViewAdOptions.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdChoicesView *adChoicesView;