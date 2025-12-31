# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd.md.txt

# GoogleMobileAds Framework Reference

# GADRewardedAd

    @interface GADRewardedAd : NSObject

The GADRewardedAd class is used for requesting and presenting a rewarded ad.
- `
  ``
  ``
  `

  ### [-initWithAdUnitID:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(im)initWithAdUnitID:)

  `
  `  
  Initializes a rewarded ad with the provided ad unit ID. Create ad unit IDs using the AdMob
  website for each unique ad placement in your app. Unique ad units improve targeting and
  statistics.

  Example AdMob ad unit ID: @ca-app-pub-3940256099942544/1712485313  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithAdUnitID:(nonnull NSString *)adUnitID;

- `
  ``
  ``
  `

  ### [-loadRequest:completionHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(im)loadRequest:completionHandler:)

  `
  `  
  Requests an rewarded ad and calls the provided completion handler when the request finishes.  

  #### Declaration

  Objective-C  

      - (void)loadRequest:(nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest.html *)request
          completionHandler:
              (nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADRewardedAd.h@T@GADRewardedAdLoadCompletionHandler)completionHandler;

- `
  ``
  ``
  `

  ### [adUnitID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adUnitID)

  `
  `  
  The ad unit ID.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nonnull) NSString *adUnitID;

- `
  ``
  ``
  `

  ### [ready](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)ready)

  `
  `  
  Indicates whether the rewarded ad is ready to be presented.  

  #### Declaration

  Objective-C  

      @property (readonly, getter=isReady, nonatomic) BOOL ready;

- `
  ``
  ``
  `

  ### [adNetworkClassName](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adNetworkClassName)

  `
  `  
  The ad network class name that fetched the current ad. Is nil while the ready property is NO.
  For both standard and mediated Google AdMob ads, this property is @GADMAdapterGoogleAdMobAds.
  For ads fetched via mediation custom events, this property is the mediated custom event adapter.  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nullable) NSString *adNetworkClassName;

- `
  ``
  ``
  `

  ### [reward](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)reward)

  `
  `  
  The reward earned by the user for interacting with a rewarded ad. Is nil until the ad has
  successfully loaded.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward.html *reward;

- `
  ``
  ``
  `

  ### [serverSideVerificationOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)serverSideVerificationOptions)

  `
  `  
  Options specified for server-to-server user reward verification.  

  #### Declaration

  Objective-C  

      @property (readwrite, copy, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions.html *serverSideVerificationOptions;

- `
  ``
  ``
  `

  ### [adMetadata](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adMetadata)

  `
  `  
  The loaded ad's metadata. Is nil if no ad is loaded or the loaded ad doesn't have metadata. Ad
  metadata may update after loading. Use the rewardedAdMetadataDidChange: delegate method on
  GADRewardedAdMetadataDelegate to listen for updates.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable)
          NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADAdMetadataKeys.h@T@GADAdMetadataKey, id> *adMetadata;

- `
  ``
  ``
  `

  ### [adMetadataDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adMetadataDelegate)

  `
  `  
  Delegate for ad metadata changes.  

  #### Declaration

  Objective-C  

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate.html>
          adMetadataDelegate;

- `
  ``
  ``
  `

  ### [-presentFromRootViewController:delegate:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(im)presentFromRootViewController:delegate:)

  `
  `  
  Presents the rewarded ad with the provided view controller and rewarded delegate to call back on
  various intermission events. The delegate is strongly retained by the receiver until a terminal
  delegate method is called. Terminal methods are -rewardedAd:didFailToPresentWithError: and
  -rewardedAdDidClose: of GADRewardedAdDelegate.  

  #### Declaration

  Objective-C  

      - (void)presentFromRootViewController:(nonnull UIViewController *)viewController
                                   delegate:
                                       (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate.html>)delegate;