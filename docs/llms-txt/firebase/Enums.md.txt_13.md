# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums.md.txt

# GoogleMobileAds Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [GADAdFormat](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADAdFormat)


  ` Requested ad format.

  #### Declaration

  Objective-C

      enum GADAdFormat {}

[## Custom Purchase Flow](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums#/Custom%20Purchase%20Flow)

- `


  ### [GADInAppPurchaseStatus](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus)


  ` Enum of the different statuses resulting from processing a purchase.

  #### Declaration

  Objective-C

      enum GADInAppPurchaseStatus {}

- `


  ### [GADAdapterInitializationState](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADAdapterInitializationState)


  ` Undocumented

  #### Declaration

  Objective-C

      NS_ENUM(NSInteger, GADAdapterInitializationState) {
        /// The mediation adapter is less likely to fill ad requests.
        GADAdapterInitializationStateNotReady = 0,
        /// The mediation adapter is ready to service ad requests.
        GADAdapterInitializationStateReady = 1
      }

- `


  ### [GADNativeAdImageAdLoaderOptionsOrientation](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADNativeAdImageAdLoaderOptionsOrientation)


  ` Native ad image orientation preference.

  #### Declaration

  Objective-C

      enum GADNativeAdImageAdLoaderOptionsOrientation {}

- `


  ### [GADAdChoicesPosition](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADAdChoicesPosition)


  ` Position of the AdChoices icon in the containing ad.

  #### Declaration

  Objective-C

      enum GADAdChoicesPosition {}

- `


  ### [GADGender](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADGender)


  ` Deprecated gender constants.

  #### Declaration

  Objective-C

      enum GADGender {}

- `


  ### [GADErrorCode](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode)


  ` NSError codes for GAD error domain.

  #### Declaration

  Objective-C

      enum GADErrorCode {}

- `


  ### [GADSearchBorderType](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADSearchBorderType)


  ` Search ad border types.

  #### Declaration

  Objective-C

      enum GADSearchBorderType {}

- `


  ### [GADSearchCallButtonColor](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADSearchCallButtonColor)


  ` Search ad call button color types.

  #### Declaration

  Objective-C

      enum GADSearchCallButtonColor {}

- `


  ### [GADMBannerAnimationType](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADMBannerAnimationType)


  ` These are the types of animation we employ for transitions between two mediated ads.

  #### Declaration

  Objective-C

      enum GADMBannerAnimationType {}