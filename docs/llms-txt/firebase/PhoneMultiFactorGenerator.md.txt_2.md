# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorGenerator.md.txt

# FirebaseAuth Framework Reference

# PhoneMultiFactorGenerator

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRPhoneMultiFactorGenerator)
    open class PhoneMultiFactorGenerator : NSObject

The data structure used to help initialize an assertion for a second factor entity to the
Firebase Auth/CICP server.

Depending on the type of second factor, this will help generate the assertion.

This class is available on iOS and macOS.
- `


  ### [assertion(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorGenerator#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorGenerator(cm)assertionWithCredential:)


  ` Initializes the MFA assertion to confirm ownership of the phone second factor.

  Note that this API is used for both enrolling and signing in with a phone second factor.

  #### Declaration

  Swift

      @objc(assertionWithCredential:)
      open class func assertion(with phoneAuthCredential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthCredential.html)
        -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorAssertion

  #### Parameters

  |---|---|
  | ` phoneAuthCredential ` | The phone auth credential used for multi factor flows. |