# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedUnifiedNativeAd

    protocol GADMediatedUnifiedNativeAd : NSObjectProtocol

Provides methods used for constructing native ads. The adapter must return an object conforming
to this protocol for native ad requests.
- `
  ``
  ``
  `

  ### [headline](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)headline)

  `
  `  
  Headline.  

  #### Declaration

  Swift  

      var headline: String? { get }

- `
  ``
  ``
  `

  ### [images](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)images)

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

  ### [body](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)body)

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

  ### [icon](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)icon)

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

  ### [callToAction](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)callToAction)

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

  ### [starRating](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)starRating)

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

  ### [store](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)store)

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

  ### [price](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)price)

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

  ### [advertiser](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)advertiser)

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

  ### [extraAssets](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)extraAssets)

  `
  `  
  Returns a dictionary of asset names and object pairs for assets that are not handled by
  properties of the GADMediatedUnifiedNativeAd.  

  #### Declaration

  Swift  

      var extraAssets: [String : Any]? { get }

- `
  ``
  ``
  `

  ### [adChoicesView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)adChoicesView)

  `
  `  
  AdChoices view.  

  #### Declaration

  Swift  

      optional var adChoicesView: UIView? { get }

- `
  ``
  ``
  `

  ### [mediaView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)mediaView)

  `
  `  
  Media view.  

  #### Declaration

  Swift  

      optional var mediaView: UIView? { get }

- `
  ``
  ``
  `

  ### [hasVideoContent](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)hasVideoContent)

  `
  `  
  Indicates whether the ad has video content.  

  #### Declaration

  Swift  

      optional var hasVideoContent: Bool { get }

- `
  ``
  ``
  `

  ### [mediaContentAspectRatio](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)mediaContentAspectRatio)

  `
  `  
  Media content aspect ratio (width/height) or 0 if there's no media content.  

  #### Declaration

  Swift  

      optional var mediaContentAspectRatio: CGFloat { get }

- `
  ``
  ``
  `

  ### [didRender(in:clickableAssetViews:nonclickableAssetViews:viewController:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didRenderInView:clickableAssetViews:nonclickableAssetViews:viewController:)

  `
  `  
  Tells the receiver that it has been rendered in \|view\| with clickable asset views and
  nonclickable asset views. viewController should be used to present modal views for the ad.  

  #### Declaration

  Swift  

      optional func didRender(in view: UIView, clickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier : UIView], nonclickableAssetViews: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier : UIView], viewController: UIViewController)

- `
  ``
  ``
  `

  ### [didRecordImpression()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didRecordImpression)

  `
  `  
  Tells the receiver that an impression is recorded. This method is called only once per mediated
  native ad.  

  #### Declaration

  Swift  

      optional func didRecordImpression()

- `
  ``
  ``
  `

  ### [didRecordClickOnAsset(withName:view:viewController:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didRecordClickOnAssetWithName:view:viewController:)

  `
  `  
  Tells the receiver that a user click is recorded on the asset named \|assetName\|. Full screen
  actions should be presented from viewController. This method is called only if
  -\[GADMAdNetworkAdapter handlesUserClicks\] returns NO.  

  #### Declaration

  Swift  

      optional func didRecordClickOnAsset(withName assetName: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier, view: UIView, viewController: UIViewController)

- `
  ``
  ``
  `

  ### [didUntrackView(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didUntrackView:)

  `
  `  
  Tells the receiver that it has untracked \|view\|. This method is called when the mediated native
  ad is no longer rendered in the provided view and the delegate should stop tracking the view's
  impressions and clicks. The method may also be called with a nil view when the view in which the
  mediated native ad has rendered is deallocated.  

  #### Declaration

  Swift  

      optional func didUntrackView(_ view: UIView?)