# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest.md.txt

# GoogleMobileAds Framework Reference

# GADMediationAdRequest

    @protocol GADMediationAdRequest <NSObject>

Provides information which can be used for making ad requests during mediation.
- `
  ``
  ``
  `

  ### [-publisherId](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)publisherId)

  `
  `  
  Publisher ID set by the publisher on the AdMob frontend.  

  #### Declaration

  Objective-C  

      - (nullable NSString *)publisherId;

- `
  ``
  ``
  `

  ### [-credentials](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)credentials)

  `
  `  
  Mediation configurations set by the publisher on the AdMob frontend.  

  #### Declaration

  Objective-C  

      - (nullable NSDictionary *)credentials;

- `
  ``
  ``
  `

  ### [-testMode](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)testMode)

  `
  `  
  Returns YES if the publisher is requesting test ads.  

  #### Declaration

  Objective-C  

      - (BOOL)testMode;

- `
  ``
  ``
  `

  ### [-networkExtras](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)networkExtras)

  `
  `  
  The adapter's ad network extras specified in GADRequest.  

  #### Declaration

  Objective-C  

      - (nullable id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras>)networkExtras;

- `
  ``
  ``
  `

  ### [-childDirectedTreatment](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)childDirectedTreatment)

  `
  `  
  Returns the value of childDirectedTreatment supplied by the publisher. Returns nil if the
  publisher hasn't specified child directed treatment. Returns @YES if child directed treatment is
  enabled.  

  #### Declaration

  Objective-C  

      - (nullable NSNumber *)childDirectedTreatment;

- `
  ``
  ``
  `

  ### [-maxAdContentRating](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)maxAdContentRating)

  `
  `  
  Returns the maximum ad content rating supplied by the publisher. Returns nil if the publisher
  hasn't specified a max ad content rating.  

  #### Declaration

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating)maxAdContentRating;

- `
  ``
  ``
  `

  ### [-underAgeOfConsent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)underAgeOfConsent)

  `
  `  
  Returns the value of underAgeOfConsent supplied by the publisher. Returns nil if the publisher
  hasn't specified the user is under the age of consent. Returns @YES if the user is under the age
  of consent.  

  #### Declaration

  Objective-C  

      - (nullable NSNumber *)underAgeOfConsent;

- `
  ``
  ``
  `

  ### [-userHasLocation](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userHasLocation)

  `
  `  
  Returns YES if the publisher has specified latitude and longitude location.  

  #### Declaration

  Objective-C  

      - (BOOL)userHasLocation;

- `
  ``
  ``
  `

  ### [-userLatitude](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLatitude)

  `
  `  
  Returns the user's latitude or 0 if location isn't specified.  

  #### Declaration

  Objective-C  

      - (CGFloat)userLatitude;

- `
  ``
  ``
  `

  ### [-userLongitude](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLongitude)

  `
  `  
  Returns the user's longitude or 0 if location isn't specified.  

  #### Declaration

  Objective-C  

      - (CGFloat)userLongitude;

- `
  ``
  ``
  `

  ### [-userLocationAccuracyInMeters](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLocationAccuracyInMeters)

  `
  `  
  Returns the user's location accuracy or 0 if location isn't specified.  

  #### Declaration

  Objective-C  

      - (CGFloat)userLocationAccuracyInMeters;

- `
  ``
  ``
  `

  ### [-userLocationDescription](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLocationDescription)

  `
  `  
  Returns user's location description. May return a value even if userHasLocation is NO.  

  #### Declaration

  Objective-C  

      - (nullable NSString *)userLocationDescription;

- `
  ``
  ``
  `

  ### [-userKeywords](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userKeywords)

  `
  `  
  Keywords describing the user's current activity. Example: @Sport Scores.  

  #### Declaration

  Objective-C  

      - (nullable NSArray *)userKeywords;

[## Deprecated](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/Deprecated)

- `
  ``
  ``
  `

  ### [-userGender](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userGender)

  `
  `  
  Deprecated. The end user's gender set by the publisher in GADRequest. Returns kGADGenderUnknown
  if it has not been specified.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADGender.html)userGender;

- `
  ``
  ``
  `

  ### [-userBirthday](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userBirthday)

  `
  `  
  Deprecated. The end user's birthday set by the publisher. Returns nil if it has not been
  specified.  

  #### Declaration

  Objective-C  

      - (nullable NSDate *)userBirthday;