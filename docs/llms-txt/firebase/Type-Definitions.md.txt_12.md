# Source: https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions.md.txt

# FirebaseAnalytics Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRConsentType](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType)


  ` The type of consent to set. Supported consent types are `ConsentType.adStorage`,
  `ConsentType.analyticsStorage`, `ConsentType.adUserData`, and `ConsentType.adPersonalization`.
  Omitting a type retains its previous status.

  #### Declaration

  Objective-C

      typedef NSString *FIRConsentType

- `


  ### [FIRConsentStatus](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentStatus)


  ` The status value of the consent type. Supported statuses are `ConsentStatus.granted` and
  `ConsentStatus.denied`.

  #### Declaration

  Objective-C

      typedef NSString *FIRConsentStatus