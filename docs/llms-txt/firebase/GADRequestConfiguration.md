# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequestConfiguration.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequestConfiguration.md.txt

# GoogleMobileAds Framework Reference

# GADRequestConfiguration

    @interface GADRequestConfiguration : NSObject

Request configuration. The settings in this class will apply to all ad requests.
- `
  ``
  ``
  `

  ### [maxAdContentRating](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequestConfiguration#/c:objc(cs)GADRequestConfiguration(py)maxAdContentRating)

  `
  `  
  The maximum ad content rating. All Google ads will have this content rating or lower.  

  #### Declaration

  Objective-C  

      @property (readwrite, copy, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADRequestConfiguration.h@T@GADMaxAdContentRating maxAdContentRating;

- `
  ``
  ``
  `

  ### [-tagForUnderAgeOfConsent:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequestConfiguration#/c:objc(cs)GADRequestConfiguration(im)tagForUnderAgeOfConsent:)

  `
  `  
  This method allows you to specify whether the user is under the age of consent.
  <https://developers.google.com/admob/ios/targeting#users_under_the_age_of_consent>.

  If you call this method with YES, a TFUA parameter will be included in all ad requests. This
  parameter disables personalized advertising, including remarketing, for all ad requests. It also
  disables requests to third-party ad vendors, such as ad measurement pixels and third-party ad
  servers.  

  #### Declaration

  Objective-C  

      - (void)tagForUnderAgeOfConsent:(BOOL)underAgeOfConsent;

- `
  ``
  ``
  `

  ### [-tagForChildDirectedTreatment:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequestConfiguration#/c:objc(cs)GADRequestConfiguration(im)tagForChildDirectedTreatment:)

  `
  `  
  \[Optional\] This method allows you to specify whether you would like your app to be treated as
  child-directed for purposes of the Children's Online Privacy Protection Act (COPPA),
  <http://business.ftc.gov/privacy-and-security/childrens-privacy>.

  If you call this method with YES, you are indicating that your app should be treated as
  child-directed for purposes of the Children's Online Privacy Protection Act (COPPA). If you call
  this method with NO, you are indicating that your app should not be treated as child-directed
  for purposes of the Children's Online Privacy Protection Act (COPPA). If you do not call this
  method, ad requests will include no indication of how you would like your app treated with
  respect to COPPA.

  By setting this method, you certify that this notification is accurate and you are authorized to
  act on behalf of the owner of the app. You understand that abuse of this setting may result in
  termination of your Google account.  

  #### Declaration

  Objective-C  

      - (void)tagForChildDirectedTreatment:(BOOL)childDirectedTreatment;