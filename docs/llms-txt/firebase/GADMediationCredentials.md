# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediationCredentials.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationCredentials.md.txt

# GoogleMobileAds Framework Reference

# GADMediationCredentials

    @interface GADMediationCredentials : NSObject

Mediation configuration set by the publisher on the AdMob UI.
- `
  ``
  ``
  `

  ### [settings](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationCredentials#/c:objc(cs)GADMediationCredentials(py)settings)

  `
  `  
  The AdMob UI settings.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nonnull) NSDictionary<NSString *, id> *settings;

- `
  ``
  ``
  `

  ### [format](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationCredentials#/c:objc(cs)GADMediationCredentials(py)format)

  `
  `  
  The ad format associated with the credentials.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADAdFormat.html format;