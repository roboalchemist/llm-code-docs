# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserMetadata.md.txt

# FirebaseAuth Framework Reference

# FIRUserMetadata


    @interface FIRUserMetadata : NSObject

A data class representing the metadata corresponding to a Firebase user.
- `
  ``
  ``
  `

  ### [lastSignInDate](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserMetadata#/c:objc(cs)FIRUserMetadata(py)lastSignInDate)

  `
  `  
  Stores the last sign in date for the corresponding Firebase user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSDate *lastSignInDate;

- `
  ``
  ``
  `

  ### [creationDate](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserMetadata#/c:objc(cs)FIRUserMetadata(py)creationDate)

  `
  `  
  Stores the creation date for the corresponding Firebase user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSDate *creationDate;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserMetadata#/c:objc(cs)FIRUserMetadata(im)init)

  `
  `  
  This class should not be initialized manually, an instance of this class can be obtained
  from a Firebase user object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;