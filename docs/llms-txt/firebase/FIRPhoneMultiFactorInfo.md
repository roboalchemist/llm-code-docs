# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneMultiFactorInfo.md.txt

# FirebaseAuth Framework Reference

# FIRPhoneMultiFactorInfo


    @interface FIRPhoneMultiFactorInfo : https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo.html

Extends the MultiFactorInfo class for phone number second factors.
The identifier of this second factor is "phone".
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [phoneNumber](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneMultiFactorInfo#/c:objc(cs)FIRPhoneMultiFactorInfo(py)phoneNumber)

  `
  `  
  This is the phone number associated with the current second factor.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSString *phoneNumber;