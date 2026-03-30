# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo.md.txt

# FirebaseAuth Framework Reference

# FIRAdditionalUserInfo


    @interface FIRAdditionalUserInfo : NSObject

Represents additional user data returned from an identity provider.
- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo#/c:objc(cs)FIRAdditionalUserInfo(im)init)


  ` This class should not be initialized manually. `AdditionalUserInfo` can be retrieved
  from from an instance of `AuthDataResult`.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [providerID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo#/c:objc(cs)FIRAdditionalUserInfo(py)providerID)


  ` The provider identifier.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly) NSString *_Nonnull providerID;

- `


  ### [profile](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo#/c:objc(cs)FIRAdditionalUserInfo(py)profile)


  ` Dictionary containing the additional IdP specific information.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly, nullable) NSDictionary<NSString *, NSObject *> *profile;

- `


  ### [username](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo#/c:objc(cs)FIRAdditionalUserInfo(py)username)


  ` username The name of the user.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly, nullable) NSString *username;

- `


  ### [newUser](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo#/c:objc(cs)FIRAdditionalUserInfo(py)newUser)


  ` Indicates whether or not the current user was signed in for the first time.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly, getter=isNewUser) BOOL newUser;