# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthSettings.md.txt

# FirebaseAuth Framework Reference

# FIRAuthSettings


    @interface FIRAuthSettings : NSObject <NSCopying>

Determines settings related to an auth object.
- `
  ``
  ``
  `

  ### [appVerificationDisabledForTesting](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthSettings#/c:objc(cs)FIRAuthSettings(py)appVerificationDisabledForTesting)

  `
  `  
  Flag to determine whether app verification should be disabled for testing or not.  

  #### Declaration

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isAppVerificationDisabledForTesting)
          BOOL appVerificationDisabledForTesting;