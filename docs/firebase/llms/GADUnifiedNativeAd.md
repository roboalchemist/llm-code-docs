# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAd

    class GADUnifiedNativeAd : NSObject

Unified native ad. To request this ad type, pass kGADAdLoaderAdTypeUnifiedNative
(see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If
you request this ad type, your delegate must conform to the GADUnifiedNativeAdLoaderDelegate
protocol.
[## Must be displayed if available](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/Must%20be%20displayed%20if%20available)

- `
  ``
  ``
  `

  ### [headline](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)headline)

  `
  `  
  Headline  

  #### Declaration

  Swift  

      var headline: String? { get }

[## Recommended to display](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/Recommended%20to%20display)

- `
  ``
  ``
  `

  ### [callToAction](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)callToAction)

  `
  `  
  Text that encourages user to take some action with the ad. For example Install.  

  #### Declaration

  Swift  

      var callToAction: String? { get }

- `
  ``
  ``
  `

  ### [icon](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)icon)

  `
  `  
  Icon image.  

  #### Declaration

  Swift  

      var icon: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html? { get }

- `
  ``
  ``
  `

  ### [body](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)body)

  `
  `  
  Description.  

  #### Declaration

  Swift  

      var body: String? { get }

- `
  ``
  ``
  `

  ### [images](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)images)

  `
  `  
  Array of GADNativeAdImage objects.  

  #### Declaration

  Swift  

      var images: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html]? { get }

- `
  ``
  ``
  `

  ### [starRating](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)starRating)

  `
  `  
  App store rating (0 to 5).  

  #### Declaration

  Swift  

      @NSCopying var starRating: NSDecimalNumber? { get }

- `
  ``
  ``
  `

  ### [store](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)store)

  `
  `  
  The app store name. For example, App Store.  

  #### Declaration

  Swift  

      var store: String? { get }

- `
  ``
  ``
  `

  ### [price](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)price)

  `
  `  
  String representation of the app's price.  

  #### Declaration

  Swift  

      var price: String? { get }

- `
  ``
  ``
  `

  ### [advertiser](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)advertiser)

  `
  `  
  Identifies the advertiser. For example, the advertiser's name or visible URL.  

  #### Declaration

  Swift  

      var advertiser: String? { get }

- `
  ``
  ``
  `

  ### [videoController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)videoController)

  `
  `  
  Video controller for controlling video playback in GADUnifiedNativeAdView's mediaView.  

  #### Declaration

  Swift  

      var videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html? { get }

- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)delegate)

  `
  `  
  Optional delegate to receive state change notifications.  

  #### Declaration

  Swift  

      weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [rootViewController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)rootViewController)

  `
  `  
  Reference to a root view controller that is used by the ad to present full screen content after
  the user interacts with the ad. The root view controller is most commonly the view controller
  displaying the ad.  

  #### Declaration

  Swift  

      weak var rootViewController: UIViewController? { get set }

- `
  ``
  ``
  `

  ### [extraAssets](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)extraAssets)

  `
  `  
  Dictionary of assets which aren't processed by the receiver.  

  #### Declaration

  Swift  

      var extraAssets: [String : Any]? { get }

- `
  ``
  ``
  `

  ### [adNetworkClassName](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)adNetworkClassName)

  `
  `  
  The ad network class name that fetched the current ad. For both standard and mediated Google
  AdMob ads, this method returns @GADMAdapterGoogleAdMobAds. For ads fetched via mediation
  custom events, this method returns @GADMAdapterCustomEvents.  

  #### Declaration

  Swift  

      var adNetworkClassName: String? { get }

- `
  ``
  ``
  `

  ### [isCustomMuteThisAdAvailable](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)customMuteThisAdAvailable)

  `
  `  
  Indicates whether custom Mute This Ad is available for the native ad.  

  #### Declaration

  Swift  

      var isCustomMuteThisAdAvailable: Bool { get }

- `
  ``
  ``
  `

  ### [muteThisAdReasons](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)muteThisAdReasons)

  `
  `  
  An array of Mute This Ad reasons used to render customized mute ad survey. Use this array to
  implement your own Mute This Ad feature only when customMuteThisAdAvailable is YES.  

  #### Declaration

  Swift  

      var muteThisAdReasons: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMuteThisAdReason.html]? { get }

- `
  ``
  ``
  `

  ### [mediaContent](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)mediaContent)

  `
  `  
  Media content. Set the associated media view's mediaContent property to this object to display
  this content.  

  #### Declaration

  Swift  

      var mediaContent: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediaContent.html { get }

- `
  ``
  ``
  `

  ### [register(_:clickableAssetViews:nonclickableAssetViews:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)registerAdView:clickableAssetViews:nonclickableAssetViews:)

  `
  `  
  Registers ad view, clickable asset views, and nonclickable asset views with this native ad.
  Media view shouldn't be registered as clickable.  

  #### Declaration

  Swift  

      func register(_ adView: UIView, clickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier : UIView], nonclickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier : UIView])

  #### Parameters

  |--------------------------------|-----------------------------------------------------------------------|
  | ` `*clickableAssetViews*` `    | Dictionary of asset views that are clickable, keyed by asset IDs.     |
  | ` `*nonclickableAssetViews*` ` | Dictionary of asset views that are not clickable, keyed by asset IDs. |

- `
  ``
  ``
  `

  ### [unregisterAdView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)unregisterAdView)

  `
  `  
  Unregisters ad view from this native ad. The corresponding asset views will also be
  unregistered.  

  #### Declaration

  Swift  

      func unregisterAdView()

- `
  ``
  ``
  `

  ### [muteThisAd(with:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)muteThisAdWithReason:)

  `
  `  
  Reports the mute event with the mute reason selected by user. Use nil if no reason was selected.
  Call this method only if customMuteThisAdAvailable is YES.  

  #### Declaration

  Swift  

      func muteThisAd(with reason: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMuteThisAdReason.html?)

[## ConfirmedClick](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/ConfirmedClick)

- `
  ``
  ``
  `

  ### [unconfirmedClickDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)unconfirmedClickDelegate)

  `
  `  
  Unconfirmed click delegate.  

  #### Declaration

  Swift  

      weak var unconfirmedClickDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdUnconfirmedClickDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [registerClickConfirmingView(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)registerClickConfirmingView:)

  `
  `  
  Registers a view that will confirm the click.  

  #### Declaration

  Swift  

      func registerClickConfirmingView(_ view: UIView?)

- `
  ``
  ``
  `

  ### [cancelUnconfirmedClick()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)cancelUnconfirmedClick)

  `
  `  
  Cancels the unconfirmed click. Call this method when the user fails to confirm the click.
  Calling this method causes the SDK to stop tracking clicks on the registered click confirming
  view and invokes the -nativeAdDidCancelUnconfirmedClick: delegate method. If no unconfirmed
  click is in progress, this method has no effect.  

  #### Declaration

  Swift  

      func cancelUnconfirmedClick()

[## CustomClickGesture](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/CustomClickGesture)

- `
  ``
  ``
  `

  ### [isCustomClickGestureEnabled](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)customClickGestureEnabled)

  `
  `  
  Indicates whether the custom click gestures feature can be used.  

  #### Declaration

  Swift  

      var isCustomClickGestureEnabled: Bool { get }

- `
  ``
  ``
  `

  ### [enableCustomClickGestures()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)enableCustomClickGestures)

  `
  `  
  Enables custom click gestures. Must be called before the ad is associated with an ad view.
  Available for whitelisted accounts only.  

  #### Declaration

  Swift  

      func enableCustomClickGestures()

- `
  ``
  ``
  `

  ### [recordCustomClickGesture()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)recordCustomClickGesture)

  `
  `  
  Records a click triggered by a custom click gesture.  

  #### Declaration

  Swift  

      func recordCustomClickGesture()