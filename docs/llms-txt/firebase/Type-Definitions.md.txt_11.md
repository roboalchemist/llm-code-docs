# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.md.txt

# GoogleMobileAds Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [GADAdLoaderAdType](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType)


  ` Undocumented

  #### Declaration

  Objective-C

      typedef NSString *GADAdLoaderAdType

- `


  ### [GADAdMetadataKey](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdMetadataKeys.h@T@GADAdMetadataKey)


  ` Undocumented

  #### Declaration

  Objective-C

      typedef NSString *GADAdMetadataKey

- `


  ### [GADAdSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdSize.h@T@GADAdSize)


  ` A valid GADAdSize is considered to be one of the predefined GADAdSize constants or a GADAdSize
  constructed by GADAdSizeFromCGSize, GADAdSizeFullWidthPortraitWithHeight,
  GADAdSizeFullWidthLandscapeWithHeight.

  Do not create a GADAdSize manually. Use one of the kGADAdSize constants. Treat GADAdSize as an
  opaque type. Do not access any fields directly. To obtain a concrete CGSize, use the function
  CGSizeFromGADAdSize().

  #### Declaration

  Objective-C

      typedef struct https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [GADInitializationCompletionHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADMobileAds.h@T@GADInitializationCompletionHandler)


  ` A block called with the initialization status when \[GADMobileAds startWithCompletionHandler:\]
  completes or times out.

  #### Declaration

  Objective-C

      typedef void (^GADInitializationCompletionHandler)(
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInitializationStatus *_Nonnull)

- `


  ### [GADNativeAppInstallAssetID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID)


  ` Undocumented

  #### Declaration

  Objective-C

      typedef NSString *GADNativeAppInstallAssetID

- `


  ### [GADNativeContentAdAssetID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID)


  ` Undocumented

  #### Declaration

  Objective-C

      typedef NSString *GADNativeContentAdAssetID

- `


  ### [GADNativeAdCustomClickHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeCustomTemplateAd.h@T@GADNativeAdCustomClickHandler)


  ` Native ad custom click handler block. \|assetID\| is the ID of asset that has received a click.

  #### Declaration

  Objective-C

      typedef void (^GADNativeAdCustomClickHandler)(NSString *_Nonnull)

- `


  ### [GADMaxAdContentRating](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating)


  ` Maximum ad content rating.

  #### Declaration

  Objective-C

      typedef NSString *GADMaxAdContentRating

- `


  ### [GADRewardedAdLoadCompletionHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADRewardedAd.h@T@GADRewardedAdLoadCompletionHandler)


  ` A block to be executed when the ad request operation completes. If the load failed, the error
  object is non-null and provides failure information. On success, \|error\| is nil.

  #### Declaration

  Objective-C

      typedef void (^GADRewardedAdLoadCompletionHandler)(https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADRequestError *_Nullable)

- `


  ### [GADUnifiedNativeAssetIdentifier](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier)


  ` Undocumented

  #### Declaration

  Objective-C

      typedef NSString *GADUnifiedNativeAssetIdentifier

- `


  ### [GADMediationBannerLoadCompletionHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationBannerLoadCompletionHandler)


  ` Called by the adapter after loading the banner ad or encountering an error. Returns an ad
  event object to send ad events to the Google Mobile Ads SDK. The block returns nil if a delegate
  couldn't be created or if the block has already been called.

  #### Declaration

  Objective-C

      typedef id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationBannerAdEventDelegate> _Nullable (
          ^GADMediationBannerLoadCompletionHandler)(
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationBannerAd> _Nullable, NSError *_Nullable)

- `


  ### [GADMediationInterstitialLoadCompletionHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationInterstitialLoadCompletionHandler)


  ` Called by the adapter after loading the interstitial ad or encountering an error. Returns an
  ad event delegate to send ad events to the Google Mobile Ads SDK. The block returns nil if a
  delegate couldn't be created or if the block has already been called.

  #### Declaration

  Objective-C

      typedef id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationInterstitialAdEventDelegate> _Nullable (
          ^GADMediationInterstitialLoadCompletionHandler)(
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationInterstitialAd> _Nullable, NSError *_Nullable)

- `


  ### [GADMediationNativeLoadCompletionHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationNativeLoadCompletionHandler)


  ` Called by the adapter after loading the native ad or encountering an error. Returns an ad
  event delegate to send ad events to the Google Mobile Ads SDK. The block returns nil if a
  delegate couldn't be created or if the block has already been called.

  #### Declaration

  Objective-C

      typedef id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate> _Nullable (
          ^GADMediationNativeLoadCompletionHandler)(
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAd> _Nullable, NSError *_Nullable)

- `


  ### [GADMediationRewardedLoadCompletionHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationRewardedLoadCompletionHandler)


  ` Called by the adapter after loading the rewarded ad or encountering an error. Returns an ad
  event delegate to send ad events to the Google Mobile Ads SDK. The block returns nil if a
  delegate couldn't be created or if the block has already been called.

  #### Declaration

  Objective-C

      typedef id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate> _Nullable (
          ^GADMediationRewardedLoadCompletionHandler)(
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationRewardedAd> _Nullable, NSError *_Nullable)

- `


  ### [GADMediationAdapterSetUpCompletionBlock](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADMediationAdapter.h@T@GADMediationAdapterSetUpCompletionBlock)


  ` Executes when adapter set up completes.

  #### Declaration

  Objective-C

      typedef void (^GADMediationAdapterSetUpCompletionBlock)(NSError *_Nullable)

- `


  ### [GADVersionNumber](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions/GADVersionNumber)


  ` Undocumented

  #### Declaration

  Objective-C

      typedef struct GADVersionNumber GADVersionNumber

- `


  ### [GADRTBSignalCompletionHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADRTBAdapter.h@T@GADRTBSignalCompletionHandler)


  ` Completion handler for signal generation. Returns either signals or an error object.

  #### Declaration

  Objective-C

      typedef void (^GADRTBSignalCompletionHandler)(NSString *_Nullable,
                                                    NSError *_Nullable)