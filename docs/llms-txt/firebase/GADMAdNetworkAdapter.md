# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.md.txt

# GoogleMobileAds Framework Reference

# GADMAdNetworkAdapter

    protocol GADMAdNetworkAdapter : NSObjectProtocol

Ad network adapter protocol.
- `
  ``
  ``
  `

  ### [adapterVersion()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(cm)adapterVersion)

  `
  `  
  Returns a version string for the adapter. It can be any string that uniquely identifies the
  adapter's version. For example, 1.0, or a date such as 20110915.  

  #### Declaration

  Swift  

      static func adapterVersion() -> String!

- `
  ``
  ``
  `

  ### [networkExtrasClass()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(cm)networkExtrasClass)

  `
  `  
  Returns the extras class that is used by publishers to provide additional parameters to this
  adapter. Returns Nil if the adapter doesn't have extra publisher provided settings.  

  #### Declaration

  Swift  

      static func networkExtrasClass() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras.Type!

- `
  ``
  ``
  `

  ### [init(gadmAdNetworkConnector:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)initWithGADMAdNetworkConnector:)

  `
  `  
  Designated initializer. Adapters can and should store a weak reference to the connector.
  However, adapters must not keep a strong reference to the connector, as doing so creates a
  reference cycle and abandoned memory.  

  #### Declaration

  Swift  

      init!(gadmAdNetworkConnector connector: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector.html!)

- `
  ``
  ``
  `

  ### [getBannerWith(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)getBannerWithSize:)

  `
  `  
  Asks the adapter to initiate an asynchronous banner ad request. The adapter may act as a
  delegate to your SDK to listen to callbacks. If your SDK doesn't support the given ad size, or
  doesn't support banner ads, call adapter:didFailAd: on the connector.  

  #### Declaration

  Swift  

      func getBannerWith(_ adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html)

- `
  ``
  ``
  `

  ### [getInterstitial()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)getInterstitial)

  `
  `  
  Asks the adapter to initiate an asynchronous interstitial ad request. The adapter may act as a
  delegate to your SDK to listen to callbacks. If your SDK doesn't support interstitials, call
  adapter:didFailInterstitial: on the connector.  

  #### Declaration

  Swift  

      func getInterstitial()

- `
  ``
  ``
  `

  ### [stopBeingDelegate()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)stopBeingDelegate)

  `
  `  
  When called, the adapter must remove strong references to itself (e.g., delegate properties and
  notification observers). You should also call this method in your adapter dealloc to prevent
  your SDK from interacting with the deallocated adapter. This function may be called multiple
  times.  

  #### Declaration

  Swift  

      func stopBeingDelegate()

- `
  ``
  ``
  `

  ### [presentInterstitial(fromRootViewController:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)presentInterstitialFromRootViewController:)

  `
  `  
  Presents an interstitial using the supplied UIViewController, by calling
  presentViewController:animated:completion:.

  Your interstitial should not immediately present itself when it is received. Instead, you should
  wait until this method is called on your adapter to present the interstitial.

  The adapter must call adapterWillPresentInterstitial: on the connector when the interstitial is
  about to be presented, and adapterWillDismissInterstitial: and adapterDidDismissInterstitial:
  when the interstitial is being dismissed.  

  #### Declaration

  Swift  

      func presentInterstitial(fromRootViewController rootViewController: UIViewController!)

- `
  ``
  ``
  `

  ### [getNativeAd(withAdTypes:options:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)getNativeAdWithAdTypes:options:)

  `
  `  
  Asks the adapter to initiate an asynchronous native ad request. \|adTypes\| contains the list of
  native ad types requested. See GADAdLoaderAdTypes.h for available ad types. \|options\| contains
  additional options configured by the publisher. See GADNativeAdImageAdLoaderOptions.h for
  available image options.

  On ad load success or failure, call adapter:didReceiveNativeAdDataSource:mediationDelegate or
  adapter:didFailAd: on the connector.  

  #### Declaration

  Swift  

      optional func getNativeAd(withAdTypes adTypes: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType]!, options: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions]!)

- `
  ``
  ``
  `

  ### [handlesUserClicks()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)handlesUserClicks)

  `
  `  
  Indicates if the adapter handles user clicks. If the adapter returns YES, it must handle user
  clicks and notify the Google Mobile Ads SDK of clicks using
  +\[GADMediatedNativeAdNotificationSource mediatedNativeAdDidRecordClick:\]. If the adapter returns
  NO, the Google Mobile Ads SDK handles user clicks and notifies the adapter of clicks using
  -\[GADMediatedNativeAdDelegate
  mediatedNativeAd:didRecordClickOnAssetWithName:view:viewController:\].  

  #### Declaration

  Swift  

      optional func handlesUserClicks() -> Bool

- `
  ``
  ``
  `

  ### [handlesUserImpressions()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)handlesUserImpressions)

  `
  `  
  Indicates if the adapter handles user impressions tracking. If the adapter returns YES, the
  Google Mobile Ads SDK will not track user impressions and the adapter must notify the
  Google Mobile Ads SDK of impressions using +\[GADMediatedNativeAdNotificationSource
  mediatedNativeAdDidRecordImpression:\]. If the adapter returns NO, the Google Mobile Ads SDK
  tracks user impressions and notifies the adapter of impressions using
  -\[GADMediatedNativeAdDelegate mediatedNativeAdDidRecordImpression:\].  

  #### Declaration

  Swift  

      optional func handlesUserImpressions() -> Bool

- `
  ``
  ``
  `

  ### [changeAdSize(to:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter#/c:objc(pl)GADMAdNetworkAdapter(im)changeAdSizeTo:)

  `
  `  
  If your ad network handles multiple ad sizes for the same banner ad, implement this method to be
  informed of banner size updates. Ad sizes typically change between kGADAdSizeSmartBannerPortrait
  and kGADAdSizeSmartBannerLandscape. If this method is not implemented, the ad is removed from
  the user interface when the size changes.  

  #### Declaration

  Swift  

      optional func changeAdSize(to adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html)