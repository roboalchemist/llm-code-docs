# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView.md.txt

# GoogleMobileAds Framework Reference

# GADNativeContentAdView


    @interface GADNativeContentAdView : UIView

Base class for content ad views. Your content ad view must be a subclass of this class and must
call superclass methods for all overriden methods.
- `


  ### [nativeContentAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)nativeContentAd)


  ` This property must point to the native content ad object rendered by this ad view.

  #### Declaration

  Objective-C

      @property (readwrite, strong, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd.html *nativeContentAd;

- `


  ### [headlineView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)headlineView)


  ` Weak reference to your ad view's headline asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *headlineView;

- `


  ### [bodyView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)bodyView)


  ` Weak reference to your ad view's body asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *bodyView;

- `


  ### [imageView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)imageView)


  ` Weak reference to your ad view's image asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *imageView;

- `


  ### [logoView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)logoView)


  ` Weak reference to your ad view's logo asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *logoView;

- `


  ### [callToActionView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)callToActionView)


  ` Weak reference to your ad view's call to action asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *callToActionView;

- `


  ### [advertiserView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)advertiserView)


  ` Weak reference to your ad view's advertiser asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIView *advertiserView;

- `


  ### [mediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)mediaView)


  ` Weak reference to your ad view's media asset view.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaView.html *mediaView;

- `


  ### [adChoicesView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)adChoicesView)


  ` Weak reference to your ad view's AdChoices view. Must set adChoicesView before setting
  nativeContentAd, otherwise AdChoices will be rendered in the publisher's
  preferredAdChoicesPosition as defined in GADNativeAdViewAdOptions.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdChoicesView *adChoicesView;