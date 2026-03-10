# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd.md.txt

# GoogleMobileAds Framework Reference

# GADRewardedAd

    class GADRewardedAd : NSObject

The GADRewardedAd class is used for requesting and presenting a rewarded ad.
- `


  ### [init(adUnitID:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(im)initWithAdUnitID:)


  ` Initializes a rewarded ad with the provided ad unit ID. Create ad unit IDs using the AdMob
  website for each unique ad placement in your app. Unique ad units improve targeting and
  statistics.

  Example AdMob ad unit ID: @ca-app-pub-3940256099942544/1712485313

  #### Declaration

  Swift

      init(adUnitID: String)

- `


  ### [load(_:completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(im)loadRequest:completionHandler:)


  ` Requests an rewarded ad and calls the provided completion handler when the request finishes.

  #### Declaration

  Swift

      func load(_ request: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.html?, completionHandler: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADRewardedAd.h@T@GADRewardedAdLoadCompletionHandler? = nil)

- `


  ### [adUnitID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adUnitID)


  ` The ad unit ID.

  #### Declaration

  Swift

      var adUnitID: String { get }

- `


  ### [isReady](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)ready)


  ` Indicates whether the rewarded ad is ready to be presented.

  #### Declaration

  Swift

      var isReady: Bool { get }

- `


  ### [adNetworkClassName](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adNetworkClassName)


  ` The ad network class name that fetched the current ad. Is nil while the ready property is NO.
  For both standard and mediated Google AdMob ads, this property is @GADMAdapterGoogleAdMobAds.
  For ads fetched via mediation custom events, this property is the mediated custom event adapter.

  #### Declaration

  Swift

      var adNetworkClassName: String? { get }

- `


  ### [reward](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)reward)


  ` The reward earned by the user for interacting with a rewarded ad. Is nil until the ad has
  successfully loaded.

  #### Declaration

  Swift

      var reward: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward.html? { get }

- `


  ### [serverSideVerificationOptions](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)serverSideVerificationOptions)


  ` Options specified for server-to-server user reward verification.

  #### Declaration

  Swift

      @NSCopying var serverSideVerificationOptions: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions.html? { get set }

- `


  ### [adMetadata](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adMetadata)


  ` The loaded ad's metadata. Is nil if no ad is loaded or the loaded ad doesn't have metadata. Ad
  metadata may update after loading. Use the rewardedAdMetadataDidChange: delegate method on
  GADRewardedAdMetadataDelegate to listen for updates.

  #### Declaration

  Swift

      var adMetadata: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADAdMetadataKeys.h@T@GADAdMetadataKey : Any]? { get }

- `


  ### [adMetadataDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(py)adMetadataDelegate)


  ` Delegate for ad metadata changes.

  #### Declaration

  Swift

      weak var adMetadataDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate.html? { get set }

- `


  ### [present(fromRootViewController:delegate:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd#/c:objc(cs)GADRewardedAd(im)presentFromRootViewController:delegate:)


  ` Presents the rewarded ad with the provided view controller and rewarded delegate to call back on
  various intermission events. The delegate is strongly retained by the receiver until a terminal
  delegate method is called. Terminal methods are -rewardedAd:didFailToPresentWithError: and
  -rewardedAdDidClose: of GADRewardedAdDelegate.

  #### Declaration

  Swift

      func present(fromRootViewController viewController: UIViewController, delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate.html)