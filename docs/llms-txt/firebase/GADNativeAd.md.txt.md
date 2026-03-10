# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAd

    @interface GADNativeAd : NSObject

Native ad base class. All native ad types are subclasses of this class.
- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd#/c:objc(cs)GADNativeAd(py)delegate)


  ` Optional delegate to receive state change notifications.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate.html> delegate;

- `


  ### [rootViewController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd#/c:objc(cs)GADNativeAd(py)rootViewController)


  ` Reference to a root view controller that is used by the ad to present full screen content after
  the user interacts with the ad. The root view controller is most commonly the view controller
  displaying the ad.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIViewController *rootViewController;

- `


  ### [extraAssets](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd#/c:objc(cs)GADNativeAd(py)extraAssets)


  ` Dictionary of assets which aren't processed by the receiver.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSDictionary *extraAssets;

- `


  ### [adNetworkClassName](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd#/c:objc(cs)GADNativeAd(py)adNetworkClassName)


  ` The ad network class name that fetched the current ad. For both standard and mediated Google
  AdMob ads, this method returns @GADMAdapterGoogleAdMobAds. For ads fetched via mediation
  custom events, this method returns @GADMAdapterCustomEvents.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *adNetworkClassName;