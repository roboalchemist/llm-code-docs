# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus.md.txt

# GoogleMobileAds Framework Reference

# GADInAppPurchaseStatus

    enum GADInAppPurchaseStatus {}

Enum of the different statuses resulting from processing a purchase.
- `


  ### [kGADInAppPurchaseStatusError](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusError)


  ` \< Error occurred while processing the purchase.

  #### Declaration

  Objective-C

      kGADInAppPurchaseStatusError = 0

- `


  ### [kGADInAppPurchaseStatusSuccessful](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusSuccessful)


  ` \< Purchase was completed successfully.

  #### Declaration

  Objective-C

      kGADInAppPurchaseStatusSuccessful = 1

- `


  ### [kGADInAppPurchaseStatusCancel](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusCancel)


  ` \< Purchase was cancelled by the user.

  #### Declaration

  Objective-C

      kGADInAppPurchaseStatusCancel = 2

- `


  ### [kGADInAppPurchaseStatusInvalidProduct](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusInvalidProduct)


  ` \< Error occurred while looking up the product.

  #### Declaration

  Objective-C

      kGADInAppPurchaseStatusInvalidProduct = 3