# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.md.txt

# GoogleMobileAds Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [GADAdLoaderAdType](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType)


  ` Undocumented

  #### Declaration

  Swift

      struct GADAdLoaderAdType : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [GADAdMetadataKey](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdMetadataKeys.h@T@GADAdMetadataKey)


  ` Undocumented

  #### Declaration

  Swift

      struct GADAdMetadataKey : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [GADAdSize](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdSize.h@T@GADAdSize)


  ` A valid GADAdSize is considered to be one of the predefined GADAdSize constants or a GADAdSize
  constructed by GADAdSizeFromCGSize, GADAdSizeFullWidthPortraitWithHeight,
  GADAdSizeFullWidthLandscapeWithHeight.

  Do not create a GADAdSize manually. Use one of the kGADAdSize constants. Treat GADAdSize as an
  opaque type. Do not access any fields directly. To obtain a concrete CGSize, use the function
  CGSizeFromGADAdSize().
- `


  ### [GADInitializationCompletionHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADMobileAds.h@T@GADInitializationCompletionHandler)


  ` A block called with the initialization status when \[GADMobileAds startWithCompletionHandler:\]
  completes or times out.

  #### Declaration

  Swift

      typealias GADInitializationCompletionHandler = (https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInitializationStatus) -> Void

- `


  ### [GADNativeAppInstallAssetID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID)


  ` Undocumented

  #### Declaration

  Swift

      struct GADNativeAppInstallAssetID : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [GADNativeContentAdAssetID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID)


  ` Undocumented

  #### Declaration

  Swift

      struct GADNativeContentAdAssetID : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [GADNativeAdCustomClickHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeCustomTemplateAd.h@T@GADNativeAdCustomClickHandler)


  ` Native ad custom click handler block. \|assetID\| is the ID of asset that has received a click.

  #### Declaration

  Swift

      typealias GADNativeAdCustomClickHandler = (String) -> Void

- `


  ### [GADMaxAdContentRating](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating)


  ` Maximum ad content rating.

  #### Declaration

  Swift

      struct GADMaxAdContentRating : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [GADRewardedAdLoadCompletionHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADRewardedAd.h@T@GADRewardedAdLoadCompletionHandler)


  ` A block to be executed when the ad request operation completes. If the load failed, the error
  object is non-null and provides failure information. On success, \|error\| is nil.

  #### Declaration

  Swift

      typealias GADRewardedAdLoadCompletionHandler = (https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes#/c:objc(cs)GADRequestError?) -> Void

- `


  ### [GADUnifiedNativeAssetIdentifier](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier)


  ` Undocumented

  #### Declaration

  Swift

      struct GADUnifiedNativeAssetIdentifier : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [GADMediationBannerLoadCompletionHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationBannerLoadCompletionHandler)


  ` Called by the adapter after loading the banner ad or encountering an error. Returns an ad
  event object to send ad events to the Google Mobile Ads SDK. The block returns nil if a delegate
  couldn't be created or if the block has already been called.

  #### Declaration

  Swift

      typealias GADMediationBannerLoadCompletionHandler = (https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAd?, Error?) -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAdEventDelegate?

- `


  ### [GADMediationInterstitialLoadCompletionHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationInterstitialLoadCompletionHandler)


  ` Called by the adapter after loading the interstitial ad or encountering an error. Returns an
  ad event delegate to send ad events to the Google Mobile Ads SDK. The block returns nil if a
  delegate couldn't be created or if the block has already been called.

  #### Declaration

  Swift

      typealias GADMediationInterstitialLoadCompletionHandler = (https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationInterstitialAd?, Error?) -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationInterstitialAdEventDelegate?

- `


  ### [GADMediationNativeLoadCompletionHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationNativeLoadCompletionHandler)


  ` Called by the adapter after loading the native ad or encountering an error. Returns an ad
  event delegate to send ad events to the Google Mobile Ads SDK. The block returns nil if a
  delegate couldn't be created or if the block has already been called.

  #### Declaration

  Swift

      typealias GADMediationNativeLoadCompletionHandler = (https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationNativeAd?, Error?) -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate?

- `


  ### [GADMediationRewardedLoadCompletionHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationRewardedLoadCompletionHandler)


  ` Called by the adapter after loading the rewarded ad or encountering an error. Returns an ad
  event delegate to send ad events to the Google Mobile Ads SDK. The block returns nil if a
  delegate couldn't be created or if the block has already been called.

  #### Declaration

  Swift

      typealias GADMediationRewardedLoadCompletionHandler = (https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAd?, Error?) -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate?

- `


  ### [GADMediationAdapterSetUpCompletionBlock](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationAdapterSetUpCompletionBlock)


  ` Executes when adapter set up completes.

  #### Declaration

  Swift

      typealias GADMediationAdapterSetUpCompletionBlock = (Error?) -> Void

- `


  ### [GADVersionNumber](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions/GADVersionNumber)


  ` Undocumented
- `


  ### [GADRTBSignalCompletionHandler](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADRTBAdapter.h@T@GADRTBSignalCompletionHandler)


  ` Completion handler for signal generation. Returns either signals or an error object.

  #### Declaration

  Swift

      typealias GADRTBSignalCompletionHandler = (String?, Error?) -> Void