# Source: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions.md.txt

# FirebaseAnalytics Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [ConsentType](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType)


  ` The type of consent to set. Supported consent types are `ConsentType.adStorage`,
  `ConsentType.analyticsStorage`, `ConsentType.adUserData`, and `ConsentType.adPersonalization`.
  Omitting a type retains its previous status.

  #### Declaration

  Swift

      struct ConsentType : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable, @unchecked Sendable

- `


  ### [ConsentStatus](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentStatus)


  ` The status value of the consent type. Supported statuses are `ConsentStatus.granted` and
  `ConsentStatus.denied`.

  #### Declaration

  Swift

      struct ConsentStatus : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable, @unchecked Sendable