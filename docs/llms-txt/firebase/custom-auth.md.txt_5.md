# Source: https://firebase.google.com/docs/auth/unity/custom-auth.md.txt

You can integrate Firebase Authentication with a custom authentication system by
modifying your authentication server to produce custom signed tokens when a user
successfully signs in. Your app receives this token and uses it to authenticate
with Firebase.

## Before you begin

1. Before you can use
   [Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth),
   you need to:

   <br />

   <br />

   - Register your Unity project with your Firebase project.
   - Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseAuth.unitypackage`) to your Unity project.

   <br />

   <br />

   **Find detailed instructions for these initial setup steps in
   [Add Firebase to your Unity
   project](https://firebase.google.com/docs/unity/setup#set_up_environment).**
2. Get your project's server keys:
   1. Go to the [Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk) page in your project's settings.
   2. Click *Generate New Private Key* at the bottom of the *Firebase Admin SDK* section of the *Service Accounts* page.
   3. The new service account's public/private key pair is automatically saved on your computer. Copy this file to your authentication server.

## Authenticate with Firebase

The `FirebaseAuth` class is the gateway for all API calls. It is accessible through [FirebaseAuth.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#defaultinstance).

```c#
Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
```

Call `Firebase.Auth.FirebaseAuth.SignInWithCustomTokenAsync` with the token from
your authentication server.

1. When users sign in to your app, send their sign-in credentials (for example, their username and password) to your authentication server. Your server checks the credentials and returns a [custom token](https://firebase.google.com/docs/auth/admin/create-custom-tokens) if they are valid.
2. After you receive the custom token from your authentication server, pass it to `Firebase.Auth.FirebaseAuth.SignInWithCustomTokenAsync` to sign in the user:

   ```c#
   auth.SignInWithCustomTokenAsync(custom_token).ContinueWith(task => {
     if (task.IsCanceled) {
       Debug.LogError("SignInWithCustomTokenAsync was canceled.");
       return;
     }
     if (task.IsFaulted) {
       Debug.LogError("SignInWithCustomTokenAsync encountered an error: " + task.Exception);
       return;
     }

     Firebase.Auth.AuthResult result = task.Result;
     Debug.LogFormat("User signed in successfully: {0} ({1})",
         result.User.DisplayName, result.User.UserId);
   });
   ```

## Next steps

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