# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants.md.txt

# GoogleMobileAds Framework Reference

# Constants

The following constants are available globally.
- `


  ### [kDFPSimulatorID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kDFPSimulatorID)


  ` Add this constant to the testDevices property's array to receive test ads on the simulator.

  #### Declaration

  Objective-C

      extern id _Nonnull const kDFPSimulatorID

- `


  ### [kGADAdLoaderAdTypeNativeAppInstall](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeNativeAppInstall)


  ` Use with GADAdLoader to request native app install ads. To receive ads, the ad loader's delegate
  must conform to the GADNativeAppInstallAdLoaderDelegate protocol. See GADNativeAppInstallAd.h.

  See GADNativeAdImageAdLoaderOptions.h for ad loader image options.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType _Nonnull kGADAdLoaderAdTypeNativeAppInstall

- `


  ### [kGADAdLoaderAdTypeNativeContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeNativeContent)


  ` Use with GADAdLoader to request native content ads. To receive ads, the ad loader's delegate
  must conform to the GADNativeContentAdLoaderDelegate protocol. See GADNativeContentAd.h.

  See GADNativeAdImageAdLoaderOptions.h for ad loader image options.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType _Nonnull kGADAdLoaderAdTypeNativeContent

- `


  ### [kGADAdLoaderAdTypeNativeCustomTemplate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeNativeCustomTemplate)


  ` Use with GADAdLoader to request native custom template ads. To receive ads, the ad loader's
  delegate must conform to the GADNativeCustomTemplateAdLoaderDelegate protocol. See
  GADNativeCustomTemplateAd.h.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType _Nonnull kGADAdLoaderAdTypeNativeCustomTemplate

- `


  ### [kGADAdLoaderAdTypeDFPBanner](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeDFPBanner)


  ` Use with GADAdLoader to request Google Ad Manager banner ads. To receive ads, the ad loader's
  delegate must conform to the DFPBannerAdLoaderDelegate protocol. See DFPBannerView.h.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType _Nonnull kGADAdLoaderAdTypeDFPBanner

- `


  ### [kGADAdLoaderAdTypeUnifiedNative](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeUnifiedNative)


  ` Use with GADAdLoader to request native ads. To receive ads, the ad loader's delegate must
  conform to the GADUnifiedNativeAdLoaderDelegate protocol. See GADUnifiedNativeAd.h.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType _Nonnull kGADAdLoaderAdTypeUnifiedNative

[## Standard Sizes](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/Standard%20Sizes)

- `


  ### [kGADAdSizeBanner](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeBanner)


  ` iPhone and iPod Touch ad size. Typically 320x50.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeBanner

- `


  ### [kGADAdSizeLargeBanner](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeLargeBanner)


  ` Taller version of kGADAdSizeBanner. Typically 320x100.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeLargeBanner

- `


  ### [kGADAdSizeMediumRectangle](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeMediumRectangle)


  ` Medium Rectangle size for the iPad (especially in a UISplitView's left pane). Typically 300x250.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeMediumRectangle

- `


  ### [kGADAdSizeFullBanner](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeFullBanner)


  ` Full Banner size for the iPad (especially in a UIPopoverController or in
  UIModalPresentationFormSheet). Typically 468x60.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeFullBanner

- `


  ### [kGADAdSizeLeaderboard](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeLeaderboard)


  ` Leaderboard size for the iPad. Typically 728x90.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeLeaderboard

- `


  ### [kGADAdSizeSkyscraper](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeSkyscraper)


  ` Skyscraper size for the iPad. Mediation only. AdMob/Google does not offer this size. Typically
  120x600.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeSkyscraper

- `


  ### [kGADAdSizeSmartBannerPortrait](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeSmartBannerPortrait)


  ` An ad size that spans the full width of the application in portrait orientation. The height is
  typically 50 points on an iPhone/iPod UI, and 90 points tall on an iPad UI.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeSmartBannerPortrait

- `


  ### [kGADAdSizeSmartBannerLandscape](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeSmartBannerLandscape)


  ` An ad size that spans the full width of the application in landscape orientation. The height is
  typically 32 points on an iPhone/iPod UI, and 90 points tall on an iPad UI.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeSmartBannerLandscape

- `


  ### [kGADAdSizeFluid](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeFluid)


  ` An ad size that spans the full width of its container, with a height dynamically determined by
  the ad.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeFluid

- `


  ### [kGADAdSizeInvalid](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADAdSizeInvalid)


  ` Invalid ad size marker.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize kGADAdSizeInvalid

- `


  ### [GADCustomEventParametersServer](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADCustomEventParametersServer)


  ` Key for getting the server parameter configured in AdMob when mediating to a custom event
  adapter.
  Example: NSString \*serverParameter = connector.credentials\[GADCustomEventParametersServer\].

  #### Declaration

  Objective-C

      extern NSString *const _Nonnull GADCustomEventParametersServer

- `


  ### [GADNativeAppInstallHeadlineAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallHeadlineAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallHeadlineAsset

- `


  ### [GADNativeAppInstallCallToActionAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallCallToActionAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallCallToActionAsset

- `


  ### [GADNativeAppInstallIconAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallIconAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallIconAsset

- `


  ### [GADNativeAppInstallBodyAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallBodyAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallBodyAsset

- `


  ### [GADNativeAppInstallStoreAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallStoreAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallStoreAsset

- `


  ### [GADNativeAppInstallPriceAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallPriceAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallPriceAsset

- `


  ### [GADNativeAppInstallImageAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallImageAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallImageAsset

- `


  ### [GADNativeAppInstallStarRatingAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallStarRatingAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallStarRatingAsset

- `


  ### [GADNativeAppInstallAttributionIconAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallAttributionIconAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallAttributionIconAsset

- `


  ### [GADNativeAppInstallAttributionTextAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallAttributionTextAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallAttributionTextAsset

- `


  ### [GADNativeAppInstallMediaViewAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallMediaViewAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallMediaViewAsset

- `


  ### [GADNativeAppInstallAdChoicesViewAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallAdChoicesViewAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallAdChoicesViewAsset

- `


  ### [GADNativeAppInstallBackgroundAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallBackgroundAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID const GADNativeAppInstallBackgroundAsset

- `


  ### [GADNativeContentHeadlineAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentHeadlineAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentHeadlineAsset

- `


  ### [GADNativeContentBodyAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentBodyAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentBodyAsset

- `


  ### [GADNativeContentCallToActionAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentCallToActionAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentCallToActionAsset

- `


  ### [GADNativeContentAdvertiserAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentAdvertiserAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentAdvertiserAsset

- `


  ### [GADNativeContentImageAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentImageAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentImageAsset

- `


  ### [GADNativeContentLogoAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentLogoAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentLogoAsset

- `


  ### [GADNativeContentAttributionIconAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentAttributionIconAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentAttributionIconAsset

- `


  ### [GADNativeContentAttributionTextAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentAttributionTextAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentAttributionTextAsset

- `


  ### [GADNativeContentMediaViewAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentMediaViewAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentMediaViewAsset

- `


  ### [GADNativeContentAdChoicesViewAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentAdChoicesViewAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentAdChoicesViewAsset

- `


  ### [GADNativeContentBackgroundAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeContentBackgroundAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID const GADNativeContentBackgroundAsset

- `


  ### [GADNativeCustomTemplateAdMediaViewKey](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADNativeCustomTemplateAdMediaViewKey)


  ` Asset key for the GADMediaView asset view.

  #### Declaration

  Objective-C

      extern NSString *const _Nonnull GADNativeCustomTemplateAdMediaViewKey

- `


  ### [kGADSimulatorID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADSimulatorID)


  ` Add this constant to the testDevices property's array to receive test ads on the simulator.

  #### Declaration

  Objective-C

      extern const id _Nonnull kGADSimulatorID

- `


  ### [GADMaxAdContentRatingGeneral](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingGeneral)


  ` Rating for content suitable for general audiences, including families.

  #### Declaration

  Objective-C

      extern https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating _Nonnull const GADMaxAdContentRatingGeneral

- `


  ### [GADMaxAdContentRatingParentalGuidance](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingParentalGuidance)


  ` Rating for content suitable for most audiences with parental guidance.

  #### Declaration

  Objective-C

      extern https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating _Nonnull const GADMaxAdContentRatingParentalGuidance

- `


  ### [GADMaxAdContentRatingTeen](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingTeen)


  ` Rating for content suitable for teen and older audiences.

  #### Declaration

  Objective-C

      extern https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating _Nonnull const GADMaxAdContentRatingTeen

- `


  ### [GADMaxAdContentRatingMatureAudience](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingMatureAudience)


  ` Rating for content suitable only for mature audiences.

  #### Declaration

  Objective-C

      extern https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating _Nonnull const GADMaxAdContentRatingMatureAudience

- `


  ### [kGADErrorDomain](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@kGADErrorDomain)


  ` Google AdMob Ads error domain.

  #### Declaration

  Objective-C

      extern NSString *const _Nonnull kGADErrorDomain

- `


  ### [GADUnifiedNativeHeadlineAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeHeadlineAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeHeadlineAsset

- `


  ### [GADUnifiedNativeCallToActionAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeCallToActionAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeCallToActionAsset

- `


  ### [GADUnifiedNativeIconAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeIconAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeIconAsset

- `


  ### [GADUnifiedNativeBodyAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeBodyAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeBodyAsset

- `


  ### [GADUnifiedNativeStoreAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeStoreAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeStoreAsset

- `


  ### [GADUnifiedNativePriceAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativePriceAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativePriceAsset

- `


  ### [GADUnifiedNativeImageAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeImageAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeImageAsset

- `


  ### [GADUnifiedNativeStarRatingAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeStarRatingAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeStarRatingAsset

- `


  ### [GADUnifiedNativeAdvertiserAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeAdvertiserAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeAdvertiserAsset

- `


  ### [GADUnifiedNativeMediaViewAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeMediaViewAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeMediaViewAsset

- `


  ### [GADUnifiedNativeAdChoicesViewAsset](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeAdChoicesViewAsset)


  ` Undocumented

  #### Declaration

  Objective-C

      GAD_EXTERN https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier const GADUnifiedNativeAdChoicesViewAsset

- `


  ### [GoogleMobileAdsVersionString](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Constants#/c:@GoogleMobileAdsVersionString)


  ` Project version string for GoogleMobileAds.

  #### Declaration

  Objective-C

      extern const unsigned char GoogleMobileAdsVersionString[]