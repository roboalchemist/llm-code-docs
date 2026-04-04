# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRTBRequestParameters.md.txt

# GoogleMobileAds Framework Reference

# GADRTBRequestParameters

    @interface GADRTBRequestParameters : NSObject

Request parameters provided by the publisher and Google Mobile Ads SDK.
- `


  ### [credentials](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRTBRequestParameters#/c:objc(cs)GADRTBRequestParameters(py)credentials)


  ` Mediation configuration set by the publisher on the AdMob UI.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationCredentials.html *credentials;

- `


  ### [extras](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRTBRequestParameters#/c:objc(cs)GADRTBRequestParameters(py)extras)


  ` Extras the publisher registered with -\[GADRequest registerAdNetworkExtras:\].

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras> extras;

[## Banner parameters](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRTBRequestParameters#/Banner%20parameters)

- `


  ### [adSize](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRTBRequestParameters#/c:objc(cs)GADRTBRequestParameters(py)adSize)


  ` Requested banner ad size. The ad size is kGADAdSizeInvalid for non-banner requests. Use
  credentials.format to determine the request format.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize.html adSize;