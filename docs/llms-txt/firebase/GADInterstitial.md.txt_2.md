# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial.md.txt

# GoogleMobileAds Framework Reference

# GADInterstitial

    @interface GADInterstitial : NSObject

An interstitial ad. This is a full-screen advertisement shown at natural transition points in
your application such as between game levels or news stories.
- `


  ### [-initWithAdUnitID:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(im)initWithAdUnitID:)


  ` Initializes an interstitial with an ad unit created on the AdMob website. Create a new ad unit
  for every unique placement of an ad in your application. Set this to the ID assigned for this
  placement. Ad units are important for targeting and statistics.

  Example AdMob ad unit ID: @ca-app-pub-0123456789012345/0123456789

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithAdUnitID:(nonnull NSString *)adUnitID;

[## Pre-Request](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/Pre-Request)

- `


  ### [adUnitID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(py)adUnitID)


  ` The interstitial's ad unit ID.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) NSString *adUnitID;

- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(py)delegate)


  ` Optional delegate object that receives state change notifications from this GADInterstitalAd.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADInterstitialDelegate.html> delegate;

[## Making an Ad Request](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/Making%20an%20Ad%20Request)

- `


  ### [-loadRequest:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(im)loadRequest:)


  ` Makes an interstitial ad request. Additional targeting options can be supplied with a request
  object. Only one interstitial request is allowed at a time.

  This is best to do several seconds before the interstitial is needed to preload its content.
  Then when transitioning between view controllers show the interstital with
  presentFromViewController.

  #### Declaration

  Objective-C

      - (void)loadRequest:(nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest.html *)request;

[## Post-Request](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/Post-Request)

- `


  ### [isReady](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(py)isReady)


  ` Returns YES if the interstitial is ready to be displayed. The delegate's
  interstitialAdDidReceiveAd: will be called after this property switches from NO to YES.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) BOOL isReady;

- `


  ### [hasBeenUsed](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(py)hasBeenUsed)


  ` Returns YES if this object has already been presented. Interstitial objects can only be used
  once even with different requests.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) BOOL hasBeenUsed;

- `


  ### [adNetworkClassName](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(py)adNetworkClassName)


  ` Returns the ad network class name that fetched the current ad. Returns nil while the latest ad
  request is in progress or if the latest ad request failed. For both standard and mediated Google
  AdMob ads, this property returns @GADMAdapterGoogleAdMobAds. For ads fetched via mediation
  custom events, this property returns @GADMAdapterCustomEvents.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) NSString *adNetworkClassName;

- `


  ### [-presentFromRootViewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(im)presentFromRootViewController:)


  ` Presents the interstitial ad which takes over the entire screen until the user dismisses it.
  This has no effect unless isReady returns YES and/or the delegate's interstitialDidReceiveAd:
  has been received.

  Set rootViewController to the current view controller at the time this method is called. If your
  application does not use view controllers pass in nil and your views will be removed from the
  window to show the interstitial and restored when done. After the interstitial has been removed,
  the delegate's interstitialDidDismissScreen: will be called.

  #### Declaration

  Objective-C

      - (void)presentFromRootViewController:
          (nonnull UIViewController *)rootViewController;

[## Deprecated](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/Deprecated)

- `


  ### [inAppPurchaseDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(py)inAppPurchaseDelegate)


  ` Deprecated delegate. GADInAppPurchase is deprecated.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADInAppPurchaseDelegate.html>
          inAppPurchaseDelegate;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial#/c:objc(cs)GADInterstitial(im)init)


  ` Deprecated intializer. Use initWithAdUnitID: instead.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;