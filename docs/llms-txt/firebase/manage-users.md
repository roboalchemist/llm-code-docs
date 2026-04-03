# Source: https://firebase.google.com/docs/auth/web/manage-users.md.txt

# Source: https://firebase.google.com/docs/auth/unity/manage-users.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/manage-users.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/manage-users.md.txt

# Source: https://firebase.google.com/docs/auth/android/manage-users.md.txt

# Source: https://firebase.google.com/docs/auth/admin/manage-users.md.txt

# Source: https://firebase.google.com/docs/auth/ios/manage-users.md.txt

## Create a user

You create a new user in your Firebase project by calling the[`createUser`](https://firebase.google.com/docs/auth/ios/password-auth#create_a_password-based_account)method or by signing in a user for the first time using a federated identity provider, such as[Google Sign-In](https://firebase.google.com/docs/auth/ios/google-signin)or[Facebook Login](https://firebase.google.com/docs/auth/ios/facebook-login).

You can also create new password-authenticated users from the Authentication section of the[Firebaseconsole](https://console.firebase.google.com/), on the Users page.

## Get the currently signed-in user

The recommended way to get the current user is by setting a listener on the Auth object:  

### Swift

```swift
handle = Auth.auth().addStateDidChangeListener { auth, user in
  // ...
}
```

### Objective-C

```objective-c
self.handle = [[FIRAuth auth]
    addAuthStateDidChangeListener:^(FIRAuth *_Nonnull auth, FIRUser *_Nullable user) {
      // ...
    }];
```

By using a listener, you ensure that the Auth object isn't in an intermediate state---such as initialization---when you get the current user.

You can also get the currently signed-in user by using the`currentUser`property. If a user isn't signed in,`currentUser`is nil:  

### Swift

```swift
if Auth.auth().currentUser != nil {
  // User is signed in.
  // ...
} else {
  // No user is signed in.
  // ...
}
```

### Objective-C

```objective-c
if ([FIRAuth auth].currentUser) {
  // User is signed in.
  // ...
} else {
  // No user is signed in.
  // ...
}
```
| **Note:** `currentUser`might also be nil because the auth object has not finished initializing. If you use a listener to keep track of the user's sign-in status, you don't need to handle this case.

## Get a user's profile

To get a user's profile information, use the properties of an instance of`FIRUser`. For example:  

### Swift

```swift
let user = Auth.auth().currentUser
if let user = user {
  // The user's ID, unique to the Firebase project.
  // Do NOT use this value to authenticate with your backend server,
  // if you have one. Use getTokenWithCompletion:completion: instead.
  let uid = user.uid
  let email = user.email
  let photoURL = user.photoURL
  var multiFactorString = "MultiFactor: "
  for info in user.multiFactor.enrolledFactors {
    multiFactorString += info.displayName ?? "[DispayName]"
    multiFactorString += " "
  }
  // ...
}
```

### Objective-C

```objective-c
FIRUser *user = [FIRAuth auth].currentUser;
if (user) {
  // The user's ID, unique to the Firebase project.
  // Do NOT use this value to authenticate with your backend server,
  // if you have one. Use getTokenWithCompletion:completion: instead.
  NSString *email = user.email;
  NSString *uid = user.uid;
  NSMutableString *multiFactorString = [NSMutableString stringWithFormat:@"MultiFactor: "];
  for (FIRMultiFactorInfo *info in user.multiFactor.enrolledFactors) {
    [multiFactorString appendString:info.displayName];
    [multiFactorString appendString:@" "];
  }
  NSURL *photoURL = user.photoURL;
  // ...
}
```

## Get a user's provider-specific profile information

To get the profile information retrieved from the sign-in providers linked to a user, use the`providerData`property. For example:  

### Swift

```swift
let userInfo = Auth.auth().currentUser?.providerData[indexPath.row]
cell?.textLabel?.text = userInfo?.providerID
// Provider-specific UID
cell?.detailTextLabel?.text = userInfo?.uid
```

### Objective-C

```objective-c
id<FIRUserInfo> userInfo = [FIRAuth auth].currentUser.providerData[indexPath.row];
cell.textLabel.text = [userInfo providerID];
// Provider-specific UID
cell.detailTextLabel.text = [userInfo uid];
```

## Update a user's profile

You can update a user's basic profile information---the user's display name and profile photo URL---with the`UserProfileChangeRequest`class. For example:  

### Swift

```swift
let changeRequest = Auth.auth().currentUser?.createProfileChangeRequest()
changeRequest?.displayName = displayName
changeRequest?.commitChanges { error in
  // ...
}
```

### Objective-C

```objective-c
FIRUserProfileChangeRequest *changeRequest = [[FIRAuth auth].currentUser profileChangeRequest];
changeRequest.displayName = userInput;
[changeRequest commitChangesWithCompletion:^(NSError *_Nullable error) {
  // ...
}];
```

## Set a user's email address

You can set a user's email address with the`updateEmail`method. For example:  

### Swift

```swift
Auth.auth().currentUser?.updateEmail(to: email) { error in
  // ...
}
```

### Objective-C

```objective-c
[[FIRAuth auth].currentUser updateEmail:userInput completion:^(NSError *_Nullable error) {
  // ...
}];
```
| **Important:** To set a user's email address, the user must have signed in recently. See[Re-authenticate a user](https://firebase.google.com/docs/auth/ios/manage-users#re-authenticate_a_user).

## Send a user a verification email

You can send an address verification email to a user with the`sendEmailVerificationWithCompletion:`method. For example:  

### Swift

```swift
Auth.auth().currentUser?.sendEmailVerification { error in
  // ...
}
```

### Objective-C

```objective-c
[[FIRAuth auth].currentUser sendEmailVerificationWithCompletion:^(NSError *_Nullable error) {
  // ...
}];
```

You can customize the email template that is used in Authentication section of the[Firebaseconsole](https://console.firebase.google.com/), on the Email Templates page. See[Email Templates](https://support.google.com/firebase/answer/7000714)in Firebase Help Center.

It is also possible to pass state via a[continue URL](https://firebase.google.com/docs/auth/ios/passing-state-in-email-actions)to redirect back to the app when sending a verification email.

Additionally you can localize the verification email by updating the language code on the Auth instance before sending the email. For example:  

### Swift

```swift
Auth.auth().languageCode = "fr"
// To apply the default app language instead of explicitly setting it.
// Auth.auth().useAppLanguage()
```

### Objective-C

```objective-c
[FIRAuth auth].languageCode = @"fr";
// To apply the default app language instead of explicitly setting it.
// [[FIRAuth auth] useAppLanguage];
```

## Set a user's password

You can set a user's password with the`updatePassword`method. For example:  

### Swift

```swift
Auth.auth().currentUser?.updatePassword(to: password) { error in
  // ...
}
```

### Objective-C

```objective-c
[[FIRAuth auth].currentUser updatePassword:userInput completion:^(NSError *_Nullable error) {
  // ...
}];
```
| **Important:** To set a user's password, the user must have signed in recently. See[Re-authenticate a user](https://firebase.google.com/docs/auth/ios/manage-users#re-authenticate_a_user).

## Send a password reset email

You can send a password reset email to a user with the`sendPasswordReset`method. For example:  

### Swift

```swift
Auth.auth().sendPasswordReset(withEmail: email) { error in
  // ...
}
```

### Objective-C

```objective-c
[[FIRAuth auth] sendPasswordResetWithEmail:userInput completion:^(NSError *_Nullable error) {
  // ...
}];
```

You can customize the email template that is used in Authentication section of the[Firebaseconsole](https://console.firebase.google.com/), on the Email Templates page. See[Email Templates](https://support.google.com/firebase/answer/7000714)in Firebase Help Center.

It is also possible to pass state via a[continue URL](https://firebase.google.com/docs/auth/ios/passing-state-in-email-actions)to redirect back to the app when sending a password reset email.

Additionally you can localize the password reset email by updating the language code on the Auth instance before sending the email. For example:  

#### Swift

```swift
Auth.auth().languageCode = "fr"
// To apply the default app language instead of explicitly setting it.
// Auth.auth().useAppLanguage()
```

#### Objective-C

```objective-c
[FIRAuth auth].languageCode = @"fr";
// To apply the default app language instead of explicitly setting it.
// [[FIRAuth auth] useAppLanguage];
```

You can also send password reset emails from theFirebaseconsole.

## Delete a user

You can delete a user account with the`delete`method. For example:  

### Swift

    let user = Auth.auth().currentUser

    user?.delete { error in
      if let error = error {
        // An error happened.
      } else {
        // Account deleted.
      }
    }

### Objective-C

    FIRUser *user = [FIRAuth auth].currentUser;

    [user deleteWithCompletion:^(NSError *_Nullable error) {
      if (error) {
        // An error happened.
      } else {
        // Account deleted.
      }
    }];

You can also delete users from the Authentication section of the[Firebaseconsole](https://console.firebase.google.com/), on the Users page.
| **Important:** To delete a user, the user must have signed in recently. See[Re-authenticate a user](https://firebase.google.com/docs/auth/ios/manage-users#re-authenticate_a_user).

## Re-authenticate a user

Some security-sensitive actions---such as[deleting an account](https://firebase.google.com/docs/auth/ios/manage-users#delete_a_user),[setting a primary email address](https://firebase.google.com/docs/auth/ios/manage-users#set_a_users_email_address), and[changing a password](https://firebase.google.com/docs/auth/ios/manage-users#set_a_users_password)---require that the user has recently signed in. If you perform one of these actions, and the user signed in too long ago, the action fails with the`FIRAuthErrorCodeCredentialTooOld`error. When this happens, re-authenticate the user by getting new sign-in credentials from the user and passing the credentials to`reauthenticate`. For example:  

### Swift

    let user = Auth.auth().currentUser
    var credential: AuthCredential

    // Prompt the user to re-provide their sign-in credentials

    user?.reauthenticate(with: credential) { error in
      if let error = error {
        // An error happened.
      } else {
        // User re-authenticated.
      }
    }

### Objective-C

    FIRUser *user = [FIRAuth auth].currentUser;
    FIRAuthCredential *credential;

    // Prompt the user to re-provide their sign-in credentials

    [user reauthenticateWithCredential:credential completion:^(NSError *_Nullable error) {
      if (error) {
        // An error happened.
      } else {
        // User re-authenticated.
      }
    }];

## Import user accounts

You can import user accounts from a file into your Firebase project by using the Firebase CLI's[`auth:import`](https://firebase.google.com/docs/cli/auth-import)command. For example:  

    firebase auth:import users.json --hash-algo=scrypt --rounds=8 --mem-cost=14