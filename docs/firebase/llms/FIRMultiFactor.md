# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor.md.txt

# FirebaseAuth Framework Reference

# FIRMultiFactor


    @interface FIRMultiFactor : NSObject

The interface defining the multi factor related properties and operations pertaining to a
user.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [enrolledFactors](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor#/c:objc(cs)FIRMultiFactor(py)enrolledFactors)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      @property(nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo.html *> *enrolledFactors

- `
  ``
  ``
  `

  ### [-getSessionWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor#/c:objc(cs)FIRMultiFactor(im)getSessionWithCompletion:)

  `
  `  
  Get a session for a second factor enrollment operation.  

  #### Declaration

  Objective-C  

      - (void)getSessionWithCompletion:
          (nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRMultiFactorSession *_Nullable,
                             NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A block with the session identifier for a second factor enrollment operation. This is used to identify the current user trying to enroll a second factor. |

- `
  ``
  ``
  `

  ### [-enrollWithAssertion:displayName:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor#/c:objc(cs)FIRMultiFactor(im)enrollWithAssertion:displayName:completion:)

  `
  `  
  Enrolls a second factor as identified by the `MultiFactorAssertion` parameter for the
  current user.  

  #### Declaration

  Objective-C  

      - (void)enrollWithAssertion:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorAssertion.html *)assertion
                      displayName:(nullable NSString *)displayName
                       completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |---------------------|----------------------------------------------------------------------|
  | ` `*displayName*` ` | An optional display name associated with the multi factor to enroll. |
  | ` `*completion*` `  | The block invoked when the request is complete, or fails.            |

- `
  ``
  ``
  `

  ### [-unenrollWithInfo:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor#/c:objc(cs)FIRMultiFactor(im)unenrollWithInfo:completion:)

  `
  `  
  Unenroll the given multi factor.  

  #### Declaration

  Objective-C  

      - (void)unenrollWithInfo:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo.html *)factorInfo
                    completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The block invoked when the request to send the verification email is complete, or fails. |

- `
  ``
  ``
  `

  ### [-unenrollWithFactorUID:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor#/c:objc(cs)FIRMultiFactor(im)unenrollWithFactorUID:completion:)

  `
  `  
  Unenroll the given multi factor.  

  #### Declaration

  Objective-C  

      - (void)unenrollWithFactorUID:(nonnull NSString *)factorUID
                         completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The block invoked when the request to send the verification email is complete, or fails. |