# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAppInstallAd

    class GADNativeAppInstallAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html

Native app install ad. To request this ad type, you need to pass
kGADAdLoaderAdTypeNativeAppInstall (see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in
GADAdLoader's initializer method. If you request this ad type, your delegate must conform to
the GADNativeAppInstallAdLoaderDelegate protocol.
[## Must be displayed](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/Must%20be%20displayed)

- `


  ### [headline](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)headline)


  ` App title.

  #### Declaration

  Swift

      var headline: String? { get }

- `


  ### [callToAction](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)callToAction)


  ` Text that encourages user to take some action with the ad. For example Install.

  #### Declaration

  Swift

      var callToAction: String? { get }

- `


  ### [icon](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)icon)


  ` Application icon.

  #### Declaration

  Swift

      var icon: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html? { get }

[## Recommended to display](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/Recommended%20to%20display)

- `


  ### [body](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)body)


  ` App description.

  #### Declaration

  Swift

      var body: String? { get }

- `


  ### [store](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)store)


  ` The app store name. For example, App Store.

  #### Declaration

  Swift

      var store: String? { get }

- `


  ### [price](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)price)


  ` String representation of the app's price.

  #### Declaration

  Swift

      var price: String? { get }

- `


  ### [images](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)images)


  ` Array of GADNativeAdImage objects related to the advertised application.

  #### Declaration

  Swift

      var images: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html]? { get }

- `


  ### [starRating](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)starRating)


  ` App store rating (0 to 5).

  #### Declaration

  Swift

      @NSCopying var starRating: NSDecimalNumber? { get }

- `


  ### [videoController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)videoController)


  ` Video controller for controlling video playback in GADNativeAppInstallAdView's mediaView.

  #### Declaration

  Swift

      var videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html { get }

- `


  ### [register(_:assetViews:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(im)registerAdView:assetViews:)


  ` Registers ad view and asset views with this native ad.

  #### Declaration

  Swift

      func register(_ adView: UIView, assetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID : UIView])

  #### Parameters

  |---|---|
  | ` assetViews ` | Dictionary of asset views keyed by asset IDs. |

- `


  ### [register(_:clickableAssetViews:nonclickableAssetViews:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(im)registerAdView:clickableAssetViews:nonclickableAssetViews:)


  ` Registers ad view, clickable asset views, and nonclickable asset views with this native ad.
  Media view shouldn't be registered as clickable.

  #### Declaration

  Swift

      func register(_ adView: UIView, clickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type Definitions.html#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID : UIView], nonclickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID : UIView])

  #### Parameters

  |---|---|
  | ` clickableAssetViews ` | Dictionary of asset views that are clickable, keyed by asset IDs. |
  | ` nonclickableAssetViews ` | Dictionary of asset views that are not clickable, keyed by asset IDs. |

- `


  ### [unregisterAdView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(im)unregisterAdView)


  ` Unregisters ad view from this native ad. The corresponding asset views will also be
  unregistered.

  #### Declaration

  Swift

      func unregisterAdView()