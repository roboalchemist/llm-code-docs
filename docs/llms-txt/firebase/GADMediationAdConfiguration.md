# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration.md.txt

# GoogleMobileAds Framework Reference

# GADMediationAdConfiguration

    @interface GADMediationAdConfiguration : NSObject

Provided by the Google Mobile Ads SDK for the adapter to render the ad. Contains 3PAS and other
ad configuration information.
- `
  ``
  ``
  `

  ### [bidResponse](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)bidResponse)

  `
  `  
  The ad string returned from the 3PAS.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) NSString *bidResponse;

- `
  ``
  ``
  `

  ### [topViewController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)topViewController)

  `
  `  
  View controller to present from. This value must be read at presentation time to obtain the most
  recent value. Must be accessed on the main queue.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) UIViewController *topViewController;

- `
  ``
  ``
  `

  ### [credentials](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)credentials)

  `
  `  
  Mediation configuration set by the publisher on the AdMob frontend.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nonnull) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationCredentials.html *credentials;

- `
  ``
  ``
  `

  ### [watermark](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)watermark)

  `
  `  
  PNG data containing a watermark that identifies the ad's source.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) NSData *watermark;

- `
  ``
  ``
  `

  ### [extras](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)extras)

  `
  `  
  Extras the publisher registered with -\[GADRequest registerAdNetworkExtras:\].  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras> extras;

- `
  ``
  ``
  `

  ### [childDirectedTreatment](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)childDirectedTreatment)

  `
  `  
  The value of childDirectedTreatment supplied by the publisher. Is nil if the publisher hasn't
  specified child directed treatment. Is @YES if child directed treatment is enabled.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) NSNumber *childDirectedTreatment;

- `
  ``
  ``
  `

  ### [isTestRequest](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)isTestRequest)

  `
  `  
  Indicates whether the publisher is requesting test ads.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic) BOOL isTestRequest;

- `
  ``
  ``
  `

  ### [hasUserLocation](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)hasUserLocation)

  `
  `  
  Indicates whether the publisher has specified latitude and longitude location.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic) BOOL hasUserLocation;

- `
  ``
  ``
  `

  ### [userLatitude](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)userLatitude)

  `
  `  
  The user's latitude or 0 if location isn't specified.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic) CGFloat userLatitude;

- `
  ``
  ``
  `

  ### [userLongitude](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)userLongitude)

  `
  `  
  The user's longitude or 0 if location isn't specified.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic) CGFloat userLongitude;

- `
  ``
  ``
  `

  ### [userLocationAccuracyInMeters](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)userLocationAccuracyInMeters)

  `
  `  
  The user's location accuracy or 0 if location isn't specified.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic) CGFloat userLocationAccuracyInMeters;