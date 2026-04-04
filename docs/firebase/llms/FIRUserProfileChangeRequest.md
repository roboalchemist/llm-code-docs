# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserProfileChangeRequest.md.txt

# FirebaseAuth Framework Reference

# FIRUserProfileChangeRequest


    @interface FIRUserProfileChangeRequest : NSObject

Represents an object capable of updating a user's profile data.
Properties are marked as being part of a profile update when they are set. Setting a
property value to nil is not the same as leaving the property unassigned.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserProfileChangeRequest#/c:objc(cs)FIRUserProfileChangeRequest(im)init)

  `
  `  
  Please use `User.createProfileChangeRequest()` instead.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [displayName](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserProfileChangeRequest#/c:objc(cs)FIRUserProfileChangeRequest(py)displayName)

  `
  `  
  The user's display name.
  It is an error to set this property after calling
  `commitChanges()`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *displayName;

- `
  ``
  ``
  `

  ### [photoURL](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserProfileChangeRequest#/c:objc(cs)FIRUserProfileChangeRequest(py)photoURL)

  `
  `  
  The user's photo URL.
  It is an error to set this property after calling
  `commitChanges()`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSURL *photoURL;

- `
  ``
  ``
  `

  ### [-commitChangesWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserProfileChangeRequest#/c:objc(cs)FIRUserProfileChangeRequest(im)commitChangesWithCompletion:)

  `
  `  
  Commits any pending changes.
  This method should only be called once. Once called, property values should not be
  changed.  

  #### Declaration

  Objective-C  

      - (void)commitChangesWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the user profile change has been applied. Invoked asynchronously on the main thread in the future. |