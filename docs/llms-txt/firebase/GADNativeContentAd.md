# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd.md.txt

# GoogleMobileAds Framework Reference

# GADNativeContentAd

    class GADNativeContentAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html

Native content ad. To request this ad type, you need to pass kGADAdLoaderAdTypeNativeContent
(see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If
you request this ad type, your delegate must conform to the GADNativeContentAdLoaderDelegate
protocol.
[## Must be displayed](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/Must%20be%20displayed)

- `
  ``
  ``
  `

  ### [headline](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)headline)

  `
  `  
  Primary text headline.  

  #### Declaration

  Swift  

      var headline: String? { get }

- `
  ``
  ``
  `

  ### [body](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)body)

  `
  `  
  Secondary text.  

  #### Declaration

  Swift  

      var body: String? { get }

[## Recommended to display](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/Recommended%20to%20display)

- `
  ``
  ``
  `

  ### [images](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)images)

  `
  `  
  Large images.  

  #### Declaration

  Swift  

      var images: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html]? { get }

- `
  ``
  ``
  `

  ### [logo](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)logo)

  `
  `  
  Small logo image.  

  #### Declaration

  Swift  

      var logo: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html? { get }

- `
  ``
  ``
  `

  ### [callToAction](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)callToAction)

  `
  `  
  Text that encourages user to take some action with the ad.  

  #### Declaration

  Swift  

      var callToAction: String? { get }

- `
  ``
  ``
  `

  ### [advertiser](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)advertiser)

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

  ### [videoController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)videoController)

  `
  `  
  Video controller for controlling video playback in GADNativeContentAdView's mediaView.  

  #### Declaration

  Swift  

      var videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html { get }

- `
  ``
  ``
  `

  ### [register(_:assetViews:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(im)registerAdView:assetViews:)

  `
  `  
  Registers ad view and asset views created with this native ad.  

  #### Declaration

  Swift  

      func register(_ adView: UIView, assetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID : UIView])

  #### Parameters

  |--------------------|-----------------------------------------------|
  | ` `*assetViews*` ` | Dictionary of asset views keyed by asset IDs. |

- `
  ``
  ``
  `

  ### [register(_:clickableAssetViews:nonclickableAssetViews:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(im)registerAdView:clickableAssetViews:nonclickableAssetViews:)

  `
  `  
  Registers ad view, clickable asset views, and nonclickable asset views with this native ad.
  Media view shouldn't be registered as clickable.  

  #### Declaration

  Swift  

      func register(_ adView: UIView, clickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type Definitions.html#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID : UIView], nonclickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID : UIView])

  #### Parameters

  |--------------------------------|-----------------------------------------------------------------------|
  | ` `*clickableAssetViews*` `    | Dictionary of asset views that are clickable, keyed by asset IDs.     |
  | ` `*nonclickableAssetViews*` ` | Dictionary of asset views that are not clickable, keyed by asset IDs. |

- `
  ``
  ``
  `

  ### [unregisterAdView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(im)unregisterAdView)

  `
  `  
  Unregisters ad view from this native ad. The corresponding asset views will also be
  unregistered.  

  #### Declaration

  Swift  

      func unregisterAdView()