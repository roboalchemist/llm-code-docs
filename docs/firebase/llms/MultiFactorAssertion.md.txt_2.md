# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.md.txt

# FirebaseAuth Framework Reference

# MultiFactorAssertion

    @objc(FIRMultiFactorAssertion)
    open class MultiFactorAssertion : NSObject

The base class for asserting ownership of a second factor. This is equivalent to the
AuthCredential class.

This class is available on iOS and macOS.
- `


  ### [factorID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorAssertion(py)factorID)


  ` The second factor identifier for this opaque object asserting a second factor.

  #### Declaration

  Swift

      @objc
      open var factorID: String