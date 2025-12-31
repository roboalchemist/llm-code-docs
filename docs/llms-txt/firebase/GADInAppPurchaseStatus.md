# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus.md.txt

# GoogleMobileAds Framework Reference

# GADInAppPurchaseStatus

    enum GADInAppPurchaseStatus : Int

Enum of the different statuses resulting from processing a purchase.
- `
  ``
  ``
  `

  ### [error](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusError)

  `
  `  
  \< Error occurred while processing the purchase.  

  #### Declaration

  Swift  

      case error = 0

- `
  ``
  ``
  `

  ### [successful](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusSuccessful)

  `
  `  
  \< Purchase was completed successfully.  

  #### Declaration

  Swift  

      case successful = 1

- `
  ``
  ``
  `

  ### [cancel](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusCancel)

  `
  `  
  \< Purchase was cancelled by the user.  

  #### Declaration

  Swift  

      case cancel = 2

- `
  ``
  ``
  `

  ### [invalidProduct](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus#/c:@E@GADInAppPurchaseStatus@kGADInAppPurchaseStatusInvalidProduct)

  `
  `  
  \< Error occurred while looking up the product.  

  #### Declaration

  Swift  

      case invalidProduct = 3