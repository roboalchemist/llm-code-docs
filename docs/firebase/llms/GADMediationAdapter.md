# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter.md.txt

# GoogleMobileAds Framework Reference

# GADMediationAdapter

    protocol GADMediationAdapter : NSObjectProtocol

Receives messages and requests from the Google Mobile Ads SDK. Provides GMA to 3P SDK
communication.

Adapters are initialized on a background queue and should avoid using the main queue until
load time.
- `
  ``
  ``
  `

  ### [version()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)version)

  `
  `  
  Returns the adapter version.  

  #### Declaration

  Swift  

      static func version() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADVersionNumber.html

- `
  ``
  ``
  `

  ### [adSDKVersion()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)adSDKVersion)

  `
  `  
  Returns the ad SDK version.  

  #### Declaration

  Swift  

      static func adSDKVersion() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADVersionNumber.html

- `
  ``
  ``
  `

  ### [networkExtrasClass()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)networkExtrasClass)

  `
  `  
  The extras class that is used to specify additional parameters for a request to this ad network.
  Returns Nil if the network doesn't have publisher provided extras.  

  #### Declaration

  Swift  

      static func networkExtrasClass() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras.Type?

- `
  ``
  ``
  `

  ### [setUpWith(_:completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)setUpWithConfiguration:completionHandler:)

  `
  `  
  Tells the adapter to set up its underlying ad network SDK and perform any necessary prefetching
  or configuration work. The adapter must call completionHandler once the adapter can service ad
  requests, or if it encounters an error while setting up.  

  #### Declaration

  Swift  

      optional static func setUpWith(_ configuration: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationServerConfiguration.html, completionHandler: @escaping https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationAdapterSetUpCompletionBlock)

- `
  ``
  ``
  `

  ### [loadBanner(for:completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadBannerForAdConfiguration:completionHandler:)

  `
  `  
  Asks the adapter to load a banner ad with the provided ad configuration. The adapter must call
  back completionHandler with the loaded ad, or it may call back with an error. This method is
  called on the main thread, and completionHandler must be called back on the main thread.  

  #### Declaration

  Swift  

      optional func loadBanner(for adConfiguration: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationBannerAdConfiguration.html, completionHandler: @escaping https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationBannerLoadCompletionHandler)

- `
  ``
  ``
  `

  ### [loadInterstitial(for:completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadInterstitialForAdConfiguration:completionHandler:)

  `
  `  
  Asks the adapter to load an interstitial ad with the provided ad configuration. The adapter
  must call back completionHandler with the loaded ad, or it may call back with an error. This
  method is called on the main thread, and completionHandler must be called back on the main
  thread.  

  #### Declaration

  Swift  

      optional func loadInterstitial(for adConfiguration: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADMediationInterstitialAdConfiguration, completionHandler: @escaping https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationInterstitialLoadCompletionHandler)

- `
  ``
  ``
  `

  ### [loadNativeAd(for:completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadNativeAdForAdConfiguration:completionHandler:)

  `
  `  
  Asks the adapter to load a native ad with the provided ad configuration. The adapter must call
  back completionHandler with the loaded ad, or it may call back with an error. This method is
  called on the main thread, and completionHandler must be called back on the main thread.  

  #### Declaration

  Swift  

      optional func loadNativeAd(for adConfiguration: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationNativeAdConfiguration.html, completionHandler: @escaping https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationNativeLoadCompletionHandler)

- `
  ``
  ``
  `

  ### [loadRewardedAd(for:completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadRewardedAdForAdConfiguration:completionHandler:)

  `
  `  
  Asks the adapter to load a rewarded ad with the provided ad configuration. The adapter must
  call back completionHandler with the loaded ad, or it may call back with an error. This method
  is called on the main thread, and completionHandler must be called back on the main thread.  

  #### Declaration

  Swift  

      optional func loadRewardedAd(for adConfiguration: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADMediationRewardedAdConfiguration, completionHandler: @escaping https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationRewardedLoadCompletionHandler)

- `
  ``
  ``
  `

  ### [setUp()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)setUp)

  `
  `  
  Deprecated. To be removed before launch. Use setUpWithConfiguration:completionHandler:.  

  #### Declaration

  Swift  

      optional static func setUp()

- `
  ``
  ``
  `

  ### [update(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)updateConfiguration:)

  `
  `  
  Deprecated. To be removed before launch. Use setUpWithConfiguration:completionHandler:.  

  #### Declaration

  Swift  

      optional static func update(_ configuration: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationServerConfiguration.html)