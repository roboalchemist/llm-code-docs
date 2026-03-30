# Source: https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Enums.md.txt

# FirebasePerformance Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FIRHTTPMethod](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Enums/FIRHTTPMethod)


  ` Undocumented

  #### Declaration

  Objective-C

      NS_ENUM(NSInteger, FIRHTTPMethod) {
        /** HTTP Method GET */
        FIRHTTPMethodGET NS_SWIFT_NAME(get),
        /** HTTP Method PUT */
        FIRHTTPMethodPUT NS_SWIFT_NAME(put),
        /** HTTP Method POST */
        FIRHTTPMethodPOST NS_SWIFT_NAME(post),
        /** HTTP Method DELETE */
        FIRHTTPMethodDELETE NS_SWIFT_NAME(delete),
        /** HTTP Method HEAD */
        FIRHTTPMethodHEAD NS_SWIFT_NAME(head),
        /** HTTP Method PATCH */
        FIRHTTPMethodPATCH NS_SWIFT_NAME(patch),
        /** HTTP Method OPTIONS */
        FIRHTTPMethodOPTIONS NS_SWIFT_NAME(options),
        /** HTTP Method TRACE */
        FIRHTTPMethodTRACE NS_SWIFT_NAME(trace),
        /** HTTP Method CONNECT */
        FIRHTTPMethodCONNECT NS_SWIFT_NAME(connect)
      }