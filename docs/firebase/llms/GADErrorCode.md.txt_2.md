# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode.md.txt

# GoogleMobileAds Framework Reference

# GADErrorCode

    enum GADErrorCode {}

NSError codes for GAD error domain.
- `


  ### [kGADErrorInvalidRequest](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInvalidRequest)


  ` The ad request is invalid. The localizedFailureReason error description will have more
  details. Typically this is because the ad did not have the ad unit ID or root view
  controller set.

  #### Declaration

  Objective-C

      kGADErrorInvalidRequest

- `


  ### [kGADErrorNoFill](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorNoFill)


  ` The ad request was successful, but no ad was returned.

  #### Declaration

  Objective-C

      kGADErrorNoFill

- `


  ### [kGADErrorNetworkError](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorNetworkError)


  ` There was an error loading data from the network.

  #### Declaration

  Objective-C

      kGADErrorNetworkError

- `


  ### [kGADErrorServerError](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorServerError)


  ` The ad server experienced a failure processing the request.

  #### Declaration

  Objective-C

      kGADErrorServerError

- `


  ### [kGADErrorOSVersionTooLow](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorOSVersionTooLow)


  ` The current device's OS is below the minimum required version.

  #### Declaration

  Objective-C

      kGADErrorOSVersionTooLow

- `


  ### [kGADErrorTimeout](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorTimeout)


  ` The request was unable to be loaded before being timed out.

  #### Declaration

  Objective-C

      kGADErrorTimeout

- `


  ### [kGADErrorInterstitialAlreadyUsed](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInterstitialAlreadyUsed)


  ` Will not send request because the interstitial object has already been used.

  #### Declaration

  Objective-C

      kGADErrorInterstitialAlreadyUsed

- `


  ### [kGADErrorMediationDataError](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationDataError)


  ` The mediation response was invalid.

  #### Declaration

  Objective-C

      kGADErrorMediationDataError

- `


  ### [kGADErrorMediationAdapterError](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationAdapterError)


  ` Error finding or creating a mediation ad network adapter.

  #### Declaration

  Objective-C

      kGADErrorMediationAdapterError

- `


  ### [kGADErrorMediationNoFill](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationNoFill)


  ` The mediation request was successful, but no ad was returned from any ad networks.

  #### Declaration

  Objective-C

      kGADErrorMediationNoFill

- `


  ### [kGADErrorMediationInvalidAdSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorMediationInvalidAdSize)


  ` Attempting to pass an invalid ad size to an adapter.

  #### Declaration

  Objective-C

      kGADErrorMediationInvalidAdSize

- `


  ### [kGADErrorInternalError](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInternalError)


  ` Internal error.

  #### Declaration

  Objective-C

      kGADErrorInternalError

- `


  ### [kGADErrorInvalidArgument](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorInvalidArgument)


  ` Invalid argument error.

  #### Declaration

  Objective-C

      kGADErrorInvalidArgument

- `


  ### [kGADErrorReceivedInvalidResponse](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorReceivedInvalidResponse)


  ` Received invalid response.

  #### Declaration

  Objective-C

      kGADErrorReceivedInvalidResponse

- `


  ### [kGADErrorRewardedAdAlreadyUsed](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADErrorCode#/c:@E@GADErrorCode@kGADErrorRewardedAdAlreadyUsed)


  ` Will not send request because the rewarded ad object has already been used.

  #### Declaration

  Objective-C

      kGADErrorRewardedAdAlreadyUsed