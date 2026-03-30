# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants.md.txt

# GoogleMobileAds Framework Reference

# Constants

The following constants are available globally.
- `


  ### [kDFPSimulatorID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kDFPSimulatorID)


  ` Add this constant to the testDevices property's array to receive test ads on the simulator.

  #### Declaration

  Swift

      let kDFPSimulatorID: AnyObject

- `


  ### [nativeAppInstall](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeNativeAppInstall)


  ` Use with GADAdLoader to request native app install ads. To receive ads, the ad loader's delegate
  must conform to the GADNativeAppInstallAdLoaderDelegate protocol. See GADNativeAppInstallAd.h.

  See GADNativeAdImageAdLoaderOptions.h for ad loader image options.

  #### Declaration

  Swift

      static let nativeAppInstall: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType

- `


  ### [nativeContent](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeNativeContent)


  ` Use with GADAdLoader to request native content ads. To receive ads, the ad loader's delegate
  must conform to the GADNativeContentAdLoaderDelegate protocol. See GADNativeContentAd.h.

  See GADNativeAdImageAdLoaderOptions.h for ad loader image options.

  #### Declaration

  Swift

      static let nativeContent: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType

- `


  ### [nativeCustomTemplate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeNativeCustomTemplate)


  ` Use with GADAdLoader to request native custom template ads. To receive ads, the ad loader's
  delegate must conform to the GADNativeCustomTemplateAdLoaderDelegate protocol. See
  GADNativeCustomTemplateAd.h.

  #### Declaration

  Swift

      static let nativeCustomTemplate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType

- `


  ### [dfpBanner](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeDFPBanner)


  ` Use with GADAdLoader to request Google Ad Manager banner ads. To receive ads, the ad loader's
  delegate must conform to the DFPBannerAdLoaderDelegate protocol. See DFPBannerView.h.

  #### Declaration

  Swift

      static let dfpBanner: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType

- `


  ### [unifiedNative](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdLoaderAdTypeUnifiedNative)


  ` Use with GADAdLoader to request native ads. To receive ads, the ad loader's delegate must
  conform to the GADUnifiedNativeAdLoaderDelegate protocol. See GADUnifiedNativeAd.h.

  #### Declaration

  Swift

      static let unifiedNative: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType

[## Standard Sizes](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/Standard%20Sizes)

- `


  ### [kGADAdSizeBanner](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeBanner)


  ` iPhone and iPod Touch ad size. Typically 320x50.

  #### Declaration

  Swift

      let kGADAdSizeBanner: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeLargeBanner](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeLargeBanner)


  ` Taller version of kGADAdSizeBanner. Typically 320x100.

  #### Declaration

  Swift

      let kGADAdSizeLargeBanner: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeMediumRectangle](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeMediumRectangle)


  ` Medium Rectangle size for the iPad (especially in a UISplitView's left pane). Typically 300x250.

  #### Declaration

  Swift

      let kGADAdSizeMediumRectangle: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeFullBanner](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeFullBanner)


  ` Full Banner size for the iPad (especially in a UIPopoverController or in
  UIModalPresentationFormSheet). Typically 468x60.

  #### Declaration

  Swift

      let kGADAdSizeFullBanner: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeLeaderboard](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeLeaderboard)


  ` Leaderboard size for the iPad. Typically 728x90.

  #### Declaration

  Swift

      let kGADAdSizeLeaderboard: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeSkyscraper](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeSkyscraper)


  ` Skyscraper size for the iPad. Mediation only. AdMob/Google does not offer this size. Typically
  120x600.

  #### Declaration

  Swift

      let kGADAdSizeSkyscraper: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeSmartBannerPortrait](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeSmartBannerPortrait)


  ` An ad size that spans the full width of the application in portrait orientation. The height is
  typically 50 points on an iPhone/iPod UI, and 90 points tall on an iPad UI.

  #### Declaration

  Swift

      let kGADAdSizeSmartBannerPortrait: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeSmartBannerLandscape](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeSmartBannerLandscape)


  ` An ad size that spans the full width of the application in landscape orientation. The height is
  typically 32 points on an iPhone/iPod UI, and 90 points tall on an iPad UI.

  #### Declaration

  Swift

      let kGADAdSizeSmartBannerLandscape: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeFluid](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeFluid)


  ` An ad size that spans the full width of its container, with a height dynamically determined by
  the ad.

  #### Declaration

  Swift

      let kGADAdSizeFluid: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [kGADAdSizeInvalid](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADAdSizeInvalid)


  ` Invalid ad size marker.

  #### Declaration

  Swift

      let kGADAdSizeInvalid: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize

- `


  ### [GADCustomEventParametersServer](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADCustomEventParametersServer)


  ` Key for getting the server parameter configured in AdMob when mediating to a custom event
  adapter.
  Example: NSString \*serverParameter = connector.credentials\[GADCustomEventParametersServer\].

  #### Declaration

  Swift

      let GADCustomEventParametersServer: String

- `


  ### [headlineAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallHeadlineAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let headlineAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [callToActionAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallCallToActionAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let callToActionAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [iconAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallIconAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let iconAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [bodyAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallBodyAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let bodyAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [storeAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallStoreAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let storeAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [priceAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallPriceAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let priceAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [imageAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallImageAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let imageAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [starRatingAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallStarRatingAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let starRatingAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [attributionIconAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallAttributionIconAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let attributionIconAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [attributionTextAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallAttributionTextAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let attributionTextAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [mediaViewAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallMediaViewAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let mediaViewAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [adChoicesViewAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallAdChoicesViewAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let adChoicesViewAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [backgroundAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeAppInstallBackgroundAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let backgroundAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID

- `


  ### [headlineAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentHeadlineAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let headlineAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [bodyAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentBodyAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let bodyAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [callToActionAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentCallToActionAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let callToActionAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [advertiserAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentAdvertiserAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let advertiserAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [imageAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentImageAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let imageAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [logoAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentLogoAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let logoAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [attributionIconAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentAttributionIconAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let attributionIconAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [attributionTextAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentAttributionTextAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let attributionTextAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [mediaViewAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentMediaViewAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let mediaViewAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [choicesViewAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentAdChoicesViewAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let choicesViewAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [backgroundAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeContentBackgroundAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let backgroundAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID

- `


  ### [GADNativeCustomTemplateAdMediaViewKey](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADNativeCustomTemplateAdMediaViewKey)


  ` Asset key for the GADMediaView asset view.

  #### Declaration

  Swift

      let GADNativeCustomTemplateAdMediaViewKey: String

- `


  ### [kGADSimulatorID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADSimulatorID)


  ` Add this constant to the testDevices property's array to receive test ads on the simulator.

  #### Declaration

  Swift

      let kGADSimulatorID: AnyObject

- `


  ### [general](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingGeneral)


  ` Rating for content suitable for general audiences, including families.

  #### Declaration

  Swift

      static let general: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating

- `


  ### [parentalGuidance](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingParentalGuidance)


  ` Rating for content suitable for most audiences with parental guidance.

  #### Declaration

  Swift

      static let parentalGuidance: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating

- `


  ### [teen](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingTeen)


  ` Rating for content suitable for teen and older audiences.

  #### Declaration

  Swift

      static let teen: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating

- `


  ### [matureAudience](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADMaxAdContentRatingMatureAudience)


  ` Rating for content suitable only for mature audiences.

  #### Declaration

  Swift

      static let matureAudience: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating

- `


  ### [kGADErrorDomain](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@kGADErrorDomain)


  ` Google AdMob Ads error domain.

  #### Declaration

  Swift

      let kGADErrorDomain: String

- `


  ### [headlineAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeHeadlineAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let headlineAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [callToActionAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeCallToActionAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let callToActionAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [iconAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeIconAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let iconAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [bodyAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeBodyAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let bodyAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [storeAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeStoreAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let storeAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [priceAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativePriceAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let priceAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [imageAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeImageAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let imageAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [starRatingAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeStarRatingAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let starRatingAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [advertiserAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeAdvertiserAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let advertiserAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [mediaViewAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeMediaViewAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let mediaViewAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [adChoicesViewAsset](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GADUnifiedNativeAdChoicesViewAsset)


  ` Undocumented

  #### Declaration

  Swift

      static let adChoicesViewAsset: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier

- `


  ### [GoogleMobileAdsVersionString](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Constants#/c:@GoogleMobileAdsVersionString)


  ` Project version string for GoogleMobileAds.