# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeInfo.md.txt

# FirebaseAuth Framework Reference

# FIRActionCodeInfo


    @interface FIRActionCodeInfo : NSObject

Manages information regarding action codes.
- `
  ``
  ``
  `

  ### [operation](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeInfo#/c:objc(cs)FIRActionCodeInfo(py)operation)

  `
  `  
  The operation being performed.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRActionCodeOperation.html operation;

- `
  ``
  ``
  `

  ### [email](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeInfo#/c:objc(cs)FIRActionCodeInfo(py)email)

  `
  `  
  The email address to which the code was sent. The new email address in the case of
  `ActionCodeOperationRecoverEmail`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *email;

- `
  ``
  ``
  `

  ### [previousEmail](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeInfo#/c:objc(cs)FIRActionCodeInfo(py)previousEmail)

  `
  `  
  The email that is being recovered in the case of `ActionCodeOperationRecoverEmail`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *previousEmail;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeInfo#/c:objc(cs)FIRActionCodeInfo(im)init)

  `
  `  
  please use initWithOperation: instead.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;