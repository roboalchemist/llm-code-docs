# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.md.txt

# GoogleMobileAds Framework Reference

# GADRewardBasedVideoAd

    class GADRewardBasedVideoAd : NSObject

The GADRewardBasedVideoAd class is used for requesting and presenting a reward based video ad.
This class isn't thread safe.
- `


  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(py)delegate)


  ` Delegate for receiving video notifications.

  #### Declaration

  Swift

      weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate.html? { get set }

- `


  ### [isReady](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(py)ready)


  ` Indicates whether the receiver is ready to be presented full screen.

  #### Declaration

  Swift

      var isReady: Bool { get }

- `


  ### [adNetworkClassName](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(py)adNetworkClassName)


  ` The ad network class name that fetched the current ad. Returns nil while the latest ad request
  is in progress or if the latest ad request failed. For both standard and mediated Google AdMob
  ads, this property returns @GADMAdapterGoogleAdMobAds. For ads fetched via mediation custom
  events, this property returns the mediated custom event adapter.

  #### Declaration

  Swift

      var adNetworkClassName: String? { get }

- `


  ### [userIdentifier](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(py)userIdentifier)


  ` A unique identifier used to identify the user when making server-to-server reward callbacks.
  This value is used at both request time and during ad display. New values must only be set
  before ad requests.

  #### Declaration

  Swift

      var userIdentifier: String? { get set }

- `


  ### [customRewardString](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(py)customRewardString)


  ` Optional custom reward string to include in the server-to-server callback.

  #### Declaration

  Swift

      var customRewardString: String? { get set }

- `


  ### [adMetadata](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(py)adMetadata)


  ` The loaded ad's metadata. Is nil if no ad is loaded or the loaded ad doesn't have metadata. Ad
  metadata may update after loading. Use the rewardBasedVideoAdMetadataDidChange: delegate method
  on GADRewardBasedVideoAdDelegate to listen for updates.

  #### Declaration

  Swift

      var adMetadata: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADAdMetadataKeys.h@T@GADAdMetadataKey : Any]? { get }

- `


  ### [sharedInstance()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(cm)sharedInstance)


  ` Returns the shared GADRewardBasedVideoAd instance.

  #### Declaration

  Swift

      class func sharedInstance() -> GADRewardBasedVideoAd

- `


  ### [load(_:withAdUnitID:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(im)loadRequest:withAdUnitID:)


  ` Initiates the request to fetch the reward based video ad. The \|request\| object supplies ad
  targeting information and must not be nil. The adUnitID is the ad unit id used for fetching an
  ad and must not be nil.

  #### Declaration

  Swift

      func load(_ request: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.html, withAdUnitID adUnitID: String)

- `


  ### [present(fromRootViewController:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd#/c:objc(cs)GADRewardBasedVideoAd(im)presentFromRootViewController:)


  ` Presents the reward based video ad with the provided view controller.

  #### Declaration

  Swift

      func present(fromRootViewController viewController: UIViewController)