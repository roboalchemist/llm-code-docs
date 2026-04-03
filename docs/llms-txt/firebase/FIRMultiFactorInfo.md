# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo.md.txt

# FirebaseAuth Framework Reference

# FIRMultiFactorInfo


    @interface FIRMultiFactorInfo : NSObject

Safe public structure used to represent a second factor entity from a client perspective.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [UID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo#/c:objc(cs)FIRMultiFactorInfo(py)UID)

  `
  `  
  The multi-factor enrollment ID.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull UID;

- `
  ``
  ``
  `

  ### [displayName](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo#/c:objc(cs)FIRMultiFactorInfo(py)displayName)

  `
  `  
  The user friendly name of the current second factor.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *displayName;

- `
  ``
  ``
  `

  ### [enrollmentDate](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo#/c:objc(cs)FIRMultiFactorInfo(py)enrollmentDate)

  `
  `  
  The second factor enrollment date.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDate *_Nonnull enrollmentDate;

- `
  ``
  ``
  `

  ### [factorID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo#/c:objc(cs)FIRMultiFactorInfo(py)factorID)

  `
  `  
  The identifier of the second factor.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull factorID;