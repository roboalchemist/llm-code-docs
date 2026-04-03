# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorAssertion.md.txt

# FirebaseAuth Framework Reference

# FIRMultiFactorAssertion


    @interface FIRMultiFactorAssertion : NSObject

The base class for asserting ownership of a second factor. This is equivalent to the
AuthCredential class.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [factorID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorAssertion#/c:objc(cs)FIRMultiFactorAssertion(py)factorID)

  `
  `  
  The second factor identifier for this opaque object asserting a second factor.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSString *factorID;