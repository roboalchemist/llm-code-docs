# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode.md.txt

# GoogleMobileAds Framework Reference

# GADErrorCode

    enum GADErrorCode : Int

NSError codes for GAD error domain.
- `
  ``
  ``
  `

  ### [invalidRequest](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInvalidRequest)

  `
  `  
  The ad request is invalid. The localizedFailureReason error description will have more
  details. Typically this is because the ad did not have the ad unit ID or root view
  controller set.  

  #### Declaration

  Swift  

      case invalidRequest = 0

- `
  ``
  ``
  `

  ### [noFill](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorNoFill)

  `
  `  
  The ad request was successful, but no ad was returned.  

  #### Declaration

  Swift  

      case noFill = 1

- `
  ``
  ``
  `

  ### [networkError](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorNetworkError)

  `
  `  
  There was an error loading data from the network.  

  #### Declaration

  Swift  

      case networkError = 2

- `
  ``
  ``
  `

  ### [serverError](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorServerError)

  `
  `  
  The ad server experienced a failure processing the request.  

  #### Declaration

  Swift  

      case serverError = 3

- `
  ``
  ``
  `

  ### [osVersionTooLow](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorOSVersionTooLow)

  `
  `  
  The current device's OS is below the minimum required version.  

  #### Declaration

  Swift  

      case osVersionTooLow = 4

- `
  ``
  ``
  `

  ### [timeout](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorTimeout)

  `
  `  
  The request was unable to be loaded before being timed out.  

  #### Declaration

  Swift  

      case timeout = 5

- `
  ``
  ``
  `

  ### [interstitialAlreadyUsed](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInterstitialAlreadyUsed)

  `
  `  
  Will not send request because the interstitial object has already been used.  

  #### Declaration

  Swift  

      case interstitialAlreadyUsed = 6

- `
  ``
  ``
  `

  ### [mediationDataError](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationDataError)

  `
  `  
  The mediation response was invalid.  

  #### Declaration

  Swift  

      case mediationDataError = 7

- `
  ``
  ``
  `

  ### [mediationAdapterError](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationAdapterError)

  `
  `  
  Error finding or creating a mediation ad network adapter.  

  #### Declaration

  Swift  

      case mediationAdapterError = 8

- `
  ``
  ``
  `

  ### [mediationNoFill](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationNoFill)

  `
  `  
  The mediation request was successful, but no ad was returned from any ad networks.  

  #### Declaration

  Swift  

      case mediationNoFill = 9

- `
  ``
  ``
  `

  ### [mediationInvalidAdSize](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationInvalidAdSize)

  `
  `  
  Attempting to pass an invalid ad size to an adapter.  

  #### Declaration

  Swift  

      case mediationInvalidAdSize = 10

- `
  ``
  ``
  `

  ### [internalError](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInternalError)

  `
  `  
  Internal error.  

  #### Declaration

  Swift  

      case internalError = 11

- `
  ``
  ``
  `

  ### [invalidArgument](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInvalidArgument)

  `
  `  
  Invalid argument error.  

  #### Declaration

  Swift  

      case invalidArgument = 12

- `
  ``
  ``
  `

  ### [receivedInvalidResponse](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorReceivedInvalidResponse)

  `
  `  
  Received invalid response.  

  #### Declaration

  Swift  

      case receivedInvalidResponse = 13

- `
  ``
  ``
  `

  ### [rewardedAdAlreadyUsed](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorRewardedAdAlreadyUsed)

  `
  `  
  Will not send request because the rewarded ad object has already been used.  

  #### Declaration

  Swift  

      case rewardedAdAlreadyUsed = 14