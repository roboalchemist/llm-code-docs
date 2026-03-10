# Source: https://firebase.google.com/docs/auth/unity/facebook-login.md.txt

You can let your users authenticate with Firebase using their Facebook accounts
by integrating Facebook Login into your app.

## Before you begin

Before you can use
[Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseAuth.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

## Access the `Firebase.Auth.FirebaseAuth` class

The `FirebaseAuth` class is the gateway for all API calls. It is accessible through [FirebaseAuth.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#defaultinstance).

```c#
Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
```

## Authenticate with Firebase

1. Follow instructions for [Android](https://firebase.google.com/docs/auth/android/facebook-login#authenticate_with_firebase) and [iOS+](https://firebase.google.com/docs/auth/ios/facebook-login#authenticate_with_firebase) to get an access token for the signed-in Facebook user.
2. After a user successfully signs in, exchange the access token for a Firebase credential, and authenticate with Firebase using the Firebase credential:

   ```c#
   Firebase.Auth.Credential credential =
       Firebase.Auth.FacebookAuthProvider.GetCredential(accessToken);
   auth.SignInAndRetrieveDataWithCredentialAsync(credential).ContinueWith(task => {
     if (task.IsCanceled) {
       Debug.LogError("SignInAndRetrieveDataWithCredentialAsync was canceled.");
       return;
     }
     if (task.IsFaulted) {
       Debug.LogError("SignInAndRetrieveDataWithCredentialAsync encountered an error: " + task.Exception);
       return;
     }

     Firebase.Auth.AuthResult result = task.Result;
     Debug.LogFormat("User signed in successfully: {0} ({1})",
         result.User.DisplayName, result.User.UserId);
   });
   ```

## Next Steps

After a user signs in for the first time, a new user account is created and
linked to the credentials---that is, the user name and password, phone
number, or auth provider information---the user signed in with. This new
account is stored as part of your Firebase project, and can be used to identify
a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the
  [`Firebase.Auth.FirebaseUser`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user) object:

  ```c#
  Firebase.Auth.FirebaseUser user = auth.CurrentUser;
  if (user != null) {
    string name = user.DisplayName;
    string email = user.Email;
    System.Uri photo_url = user.PhotoUrl;
    // The user's Id, unique to the Firebase project.
    // Do NOT use this value to authenticate with your backend server, if you
    // have one; use User.TokenAsync() instead.
    string uid = user.UserId;
  }
  ```
- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/unity/account-linking)

To sign out a user, call [`SignOut()`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#signout):

```c#
auth.SignOut();
```