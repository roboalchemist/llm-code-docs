# Source: https://firebase.google.com/docs/auth/unity/password-auth.md.txt

You can use Firebase Authentication to let your users authenticate with
Firebase using their email addresses and passwords, and to manage your app's
password-based accounts.

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

## Create a password-based account

To create a new user account with a password, complete the following steps in
your app's sign-in code:

1. When a new user signs up using your app's sign-up form, complete any new account validation steps that your app requires, such as verifying that the new account's password was correctly typed and meets your complexity requirements.
2. Create a new account by passing the new user's email address and password to `FirebaseAuth.CreateUserWithEmailAndPassword`:

   ```c#
   auth.CreateUserWithEmailAndPasswordAsync(email, password).ContinueWith(task => {
     if (task.IsCanceled) {
       Debug.LogError("CreateUserWithEmailAndPasswordAsync was canceled.");
       return;
     }
     if (task.IsFaulted) {
       Debug.LogError("CreateUserWithEmailAndPasswordAsync encountered an error: " + task.Exception);
       return;
     }

     // Firebase user has been created.
     Firebase.Auth.AuthResult result = task.Result;
     Debug.LogFormat("Firebase user created successfully: {0} ({1})",
         result.User.DisplayName, result.User.UserId);
   });
   ```

To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the [Firebase console](https://console.firebase.google.com/project/_/authentication/providers).

## Sign in a user with an email address and password

The steps for signing in a user with a password are similar to the steps for
creating a new account. In your app's sign-in function, do the following:

1. When a user signs in to your app, pass the user's email address and password to `FirebaseAuth.SignInWithEmailAndPassword`:

   ```c#
   auth.SignInWithEmailAndPasswordAsync(email, password).ContinueWith(task => {
     if (task.IsCanceled) {
       Debug.LogError("SignInWithEmailAndPasswordAsync was canceled.");
       return;
     }
     if (task.IsFaulted) {
       Debug.LogError("SignInWithEmailAndPasswordAsync encountered an error: " + task.Exception);
       return;
     }

     Firebase.Auth.AuthResult result = task.Result;
     Debug.LogFormat("User signed in successfully: {0} ({1})",
         result.User.DisplayName, result.User.UserId);
   });
   ```
2. You can also create the credential and sign in like the other workflows:

   ```c#
   Firebase.Auth.Credential credential =
       Firebase.Auth.EmailAuthProvider.GetCredential(email, password);
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

## Recommended: Set a password policy

[Video](https://www.youtube.com/watch?v=smB-4UogJpQ)

You can improve account security by enforcing password complexity requirements.

To configure a password policy for your project, open the **Password policy**
tab on the Authentication Settings page of the Firebase console:

[Authentication Settings](https://console.firebase.google.com/project/_/authentication/settings)

Firebase Authentication password policies support the following password requirements:

- Lowercase character required

- Uppercase character required

- Numeric character required

- Non-alphanumeric character required

  The following characters satisfy the non-alphanumeric character requirement:
  `^ $ * . [ ] { } ( ) ? " ! @ # % & / \ , > < ' : ; | _ ~`
- Minimum password length (ranges from 6 to 30 characters; defaults to 6)

- Maximum password length (maximum length of 4096 characters)

You can enable password policy enforcement in two modes:

- **Require**: Attempts to sign up fail until the user updates to a password
  that complies with your policy.

- **Notify**: Users are allowed to sign up with a non-compliant password. When
  using this mode, you should check if the user's password complies with the
  policy on the client side and prompt the user in some way to update their
  password if it does not comply.

New users are always required to choose a password that complies with your
policy.

If you have active users, we recommend not enabling force upgrade on sign in
unless you intend to block access to users whose passwords don't comply with
your policy. Instead, use notify mode, which allows users to sign in with their
current passwords, and inform them of the requirements their password lacks.

## Recommended: Enable email enumeration protection

Some Firebase Authentication methods that take email addresses as parameters throw
specific errors if the email address is unregistered when it must be registered
(for example, when signing in with an email address and password), or registered
when it must be unused (for example, when changing a user's email address).
While this can be helpful for suggesting specific remedies to users, it can also
be abused by malicious actors to discover the email addresses registered by your
users.

To mitigate this risk, we recommend you [enable email enumeration protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
for your project using the Google Cloud `gcloud` tool. Note that enabling this
feature changes Firebase Authentication's error reporting behavior: be sure your app
doesn't rely on the more specific errors.

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