# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest.md.txt

# GoogleMobileAds Framework Reference

# GADMediationAdRequest

    protocol GADMediationAdRequest : NSObjectProtocol

Provides information which can be used for making ad requests during mediation.
- `


  ### [publisherId()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)publisherId)


  ` Publisher ID set by the publisher on the AdMob frontend.

  #### Declaration

  Swift

      func publisherId() -> String?

- `


  ### [credentials()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)credentials)


  ` Mediation configurations set by the publisher on the AdMob frontend.

  #### Declaration

  Swift

      func credentials() -> [AnyHashable : Any]?

- `


  ### [testMode()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)testMode)


  ` Returns YES if the publisher is requesting test ads.

  #### Declaration

  Swift

      func testMode() -> Bool

- `


  ### [networkExtras()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)networkExtras)


  ` The adapter's ad network extras specified in GADRequest.

  #### Declaration

  Swift

      func networkExtras() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras?

- `


  ### [childDirectedTreatment()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)childDirectedTreatment)


  ` Returns the value of childDirectedTreatment supplied by the publisher. Returns nil if the
  publisher hasn't specified child directed treatment. Returns @YES if child directed treatment is
  enabled.

  #### Declaration

  Swift

      func childDirectedTreatment() -> NSNumber?

- `


  ### [maxAdContentRating()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)maxAdContentRating)


  ` Returns the maximum ad content rating supplied by the publisher. Returns nil if the publisher
  hasn't specified a max ad content rating.

  #### Declaration

  Swift

      func maxAdContentRating() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating?

- `


  ### [underAgeOfConsent()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)underAgeOfConsent)


  ` Returns the value of underAgeOfConsent supplied by the publisher. Returns nil if the publisher
  hasn't specified the user is under the age of consent. Returns @YES if the user is under the age
  of consent.

  #### Declaration

  Swift

      func underAgeOfConsent() -> NSNumber?

- `


  ### [userHasLocation()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userHasLocation)


  ` Returns YES if the publisher has specified latitude and longitude location.

  #### Declaration

  Swift

      func userHasLocation() -> Bool

- `


  ### [userLatitude()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLatitude)


  ` Returns the user's latitude or 0 if location isn't specified.

  #### Declaration

  Swift

      func userLatitude() -> CGFloat

- `


  ### [userLongitude()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLongitude)


  ` Returns the user's longitude or 0 if location isn't specified.

  #### Declaration

  Swift

      func userLongitude() -> CGFloat

- `


  ### [userLocationAccuracyInMeters()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLocationAccuracyInMeters)


  ` Returns the user's location accuracy or 0 if location isn't specified.

  #### Declaration

  Swift

      func userLocationAccuracyInMeters() -> CGFloat

- `


  ### [userLocationDescription()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userLocationDescription)


  ` Returns user's location description. May return a value even if userHasLocation is NO.

  #### Declaration

  Swift

      func userLocationDescription() -> String?

- `


  ### [userKeywords()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userKeywords)


  ` Keywords describing the user's current activity. Example: @Sport Scores.

  #### Declaration

  Swift

      func userKeywords() -> [Any]?

[## Deprecated](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/Deprecated)

- `


  ### [userGender()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userGender)


  ` Deprecated. The end user's gender set by the publisher in GADRequest. Returns kGADGenderUnknown
  if it has not been specified.

  #### Declaration

  Swift

      func userGender() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADGender.html

- `


  ### [userBirthday()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest#/c:objc(pl)GADMediationAdRequest(im)userBirthday)


  ` Deprecated. The end user's birthday set by the publisher. Returns nil if it has not been
  specified.

  #### Declaration

  Swift

      func userBirthday() -> Date?