# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration.md.txt

# GoogleMobileAds Framework Reference

# GADMediationAdConfiguration

    class GADMediationAdConfiguration : NSObject

Provided by the Google Mobile Ads SDK for the adapter to render the ad. Contains 3PAS and other
ad configuration information.
- `


  ### [bidResponse](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)bidResponse)


  ` The ad string returned from the 3PAS.

  #### Declaration

  Swift

      var bidResponse: String? { get }

- `


  ### [topViewController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)topViewController)


  ` View controller to present from. This value must be read at presentation time to obtain the most
  recent value. Must be accessed on the main queue.

  #### Declaration

  Swift

      var topViewController: UIViewController? { get }

- `


  ### [credentials](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)credentials)


  ` Mediation configuration set by the publisher on the AdMob frontend.

  #### Declaration

  Swift

      var credentials: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationCredentials.html { get }

- `


  ### [watermark](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)watermark)


  ` PNG data containing a watermark that identifies the ad's source.

  #### Declaration

  Swift

      var watermark: Data? { get }

- `


  ### [extras](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)extras)


  ` Extras the publisher registered with -\[GADRequest registerAdNetworkExtras:\].

  #### Declaration

  Swift

      var extras: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras? { get }

- `


  ### [childDirectedTreatment](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)childDirectedTreatment)


  ` The value of childDirectedTreatment supplied by the publisher. Is nil if the publisher hasn't
  specified child directed treatment. Is @YES if child directed treatment is enabled.

  #### Declaration

  Swift

      var childDirectedTreatment: NSNumber? { get }

- `


  ### [isTestRequest](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)isTestRequest)


  ` Indicates whether the publisher is requesting test ads.

  #### Declaration

  Swift

      var isTestRequest: Bool { get }

- `


  ### [hasUserLocation](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)hasUserLocation)


  ` Indicates whether the publisher has specified latitude and longitude location.

  #### Declaration

  Swift

      var hasUserLocation: Bool { get }

- `


  ### [userLatitude](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)userLatitude)


  ` The user's latitude or 0 if location isn't specified.

  #### Declaration

  Swift

      var userLatitude: CGFloat { get }

- `


  ### [userLongitude](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)userLongitude)


  ` The user's longitude or 0 if location isn't specified.

  #### Declaration

  Swift

      var userLongitude: CGFloat { get }

- `


  ### [userLocationAccuracyInMeters](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationAdConfiguration#/c:objc(cs)GADMediationAdConfiguration(py)userLocationAccuracyInMeters)


  ` The user's location accuracy or 0 if location isn't specified.

  #### Declaration

  Swift

      var userLocationAccuracyInMeters: CGFloat { get }