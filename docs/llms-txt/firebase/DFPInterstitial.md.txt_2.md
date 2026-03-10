# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial.md.txt

# GoogleMobileAds Framework Reference

# DFPInterstitial

    @interface DFPInterstitial : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial.html

Google Ad Manager interstitial ad, a full-screen advertisement shown at natural
transition points in your application such as between game levels or news stories.
- `


  ### [-initWithAdUnitID:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(im)initWithAdUnitID:)


  ` Initializes an interstitial with an ad unit created on the Ad Manager website. Create a new ad
  unit for every unique placement of an ad in your application. Set this to the ID assigned for
  this placement. Ad units are important for targeting and statistics.

  Example Ad Manager ad unit ID: @/6499/example/interstitial

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithAdUnitID:(nonnull NSString *)adUnitID;

- `


  ### [correlator](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(py)correlator)


  ` Correlator object for correlating this object to other ad objects.

  #### Declaration

  Objective-C

      @property (readwrite, strong, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCorrelator.html *correlator;

- `


  ### [appEventDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(py)appEventDelegate)


  ` Optional delegate that is notified when creatives send app events.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAppEventDelegate.html>
          appEventDelegate;

- `


  ### [customRenderedInterstitialDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(py)customRenderedInterstitialDelegate)


  ` Optional delegate object for custom rendered ads.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable)
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate.html>
              customRenderedInterstitialDelegate;