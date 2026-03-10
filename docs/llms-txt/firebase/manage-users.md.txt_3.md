# Source: https://firebase.google.com/docs/auth/unity/manage-users.md.txt

## Create a user

You create a new user in your Firebase project by calling the
[`CreateUserWithEmailAndPassword`](https://firebase.google.com/docs/auth/unity/password-auth#create_a_password-based_account)
method or by signing in a user for the first time using a federated identity
provider, such as [Google Sign-In](https://firebase.google.com/docs/auth/unity/google-signin) or
[Facebook Login](https://firebase.google.com/docs/auth/unity/facebook-login).

You can also create new password-authenticated users from the Authentication
section of the [Firebase console](https://console.firebase.google.com/), on the Users page.

## Get the currently signed-in user

The recommended way to get the current user is by setting a listener on the
Auth object:

```c#
Firebase.Auth.FirebaseAuth auth;
Firebase.Auth.FirebaseUser user;

// Handle initialization of the necessary firebase modules:
void InitializeFirebase() {
  Debug.Log("Setting up Firebase Auth");
  auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
  auth.StateChanged += AuthStateChanged;
  AuthStateChanged(this, null);
}

// Track state changes of the auth object.
void AuthStateChanged(object sender, System.EventArgs eventArgs) {
  if (auth.CurrentUser != user) {
    bool signedIn = user != auth.CurrentUser && auth.CurrentUser != null;
    if (!signedIn && user != null) {
      Debug.Log("Signed out " + user.UserId);
    }
    user = auth.CurrentUser;
    if (signedIn) {
      Debug.Log("Signed in " + user.UserId);
    }
  }
}

// Handle removing subscription and reference to the Auth instance.
// Automatically called by a Monobehaviour after Destroy is called on it.
void OnDestroy() {
  auth.StateChanged -= AuthStateChanged;
  auth = null;
}
```

By using a listener, you ensure that the Auth object isn't in an intermediate
state---such as initialization---when you get the current user.

You can also get the currently signed-in user by calling `CurrentUser`. If a
user isn't signed in, `CurrentUser` will return null. If a user is signed out,
the user's `IsValid()` will return false.

> [!NOTE]
> **Note:** `CurrentUser` might also return null because the auth object has not finished initializing. If you use a listener to keep track of the user's sign-in status, you don't need to handle this case.

### Persist a user's credential

The user's credentials will be stored in the local keystore after a user
is signed in. The local cache of user credentials can be deleted by signing
the user out. The keystore is platform specific:

- Apple platforms: [Keychain Services](https://developer.apple.com/documentation/security/keychain_services).
- Android: [Android Keystore](https://developer.android.com/training/articles/keystore).
- Windows: [Credential Management API](https://docs.microsoft.com/en-us/windows/desktop/secauthn/authentication-functions#low-level-credentials-management-functions).
- OS X: [Keychain Services](https://developer.apple.com/documentation/security/keychain_services).
- Linux: [libsecret](https://developer.gnome.org/libsecret/), which the user must have installed.

## Get a user's profile

To get a user's profile information, use the accessor methods of an instance of
`Firebase.Auth.FirebaseUser`. For example:

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

## Get a user's provider-specific profile information

To get the profile information retrieved from the sign-in providers linked to a
user, use the `ProviderData` method. For example:

```c#
Firebase.Auth.FirebaseUser user = auth.CurrentUser;
if (user != null) {
  foreach (var profile in user.ProviderData) {
    // Id of the provider (ex: google.com)
    string providerId = profile.ProviderId;

    // UID specific to the provider
    string uid = profile.UserId;

    // Name, email address, and profile photo Url
    string name = profile.DisplayName;
    string email = profile.Email;
    System.Uri photoUrl = profile.PhotoUrl;
  }
}
```

## Update a user's profile

You can update a user's basic profile information---the user's display name
and profile photo URL---with the `UpdateUserProfile` method. For example:

```c#
Firebase.Auth.FirebaseUser user = auth.CurrentUser;
if (user != null) {
  Firebase.Auth.UserProfile profile = new Firebase.Auth.UserProfile {
    DisplayName = "Jane Q. User",
    PhotoUrl = new System.Uri("https://example.com/jane-q-user/profile.jpg"),
  };
  user.UpdateUserProfileAsync(profile).ContinueWith(task => {
    if (task.IsCanceled) {
      Debug.LogError("UpdateUserProfileAsync was canceled.");
      return;
    }
    if (task.IsFaulted) {
      Debug.LogError("UpdateUserProfileAsync encountered an error: " + task.Exception);
      return;
    }

    Debug.Log("User profile updated successfully.");
  });
}
```

## Set a user's email address

You can set a user's email address with the `UpdateEmail` method. For example:

```c#
Firebase.Auth.FirebaseUser user = auth.CurrentUser;
if (user != null) {
  user.UpdateEmailAsync("user@example.com").ContinueWith(task => {
    if (task.IsCanceled) {
      Debug.LogError("UpdateEmailAsync was canceled.");
      return;
    }
    if (task.IsFaulted) {
      Debug.LogError("UpdateEmailAsync encountered an error: " + task.Exception);
      return;
    }

    Debug.Log("User email updated successfully.");
  });
}
```

> [!IMPORTANT]
> **Important:** To set a user's email address, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/unity/manage-users#re-authenticate_a_user).

## Send a user a verification email

You can send an address verification email to a user with the
`SendEmailVerification` method. For example:

```c#
Firebase.Auth.FirebaseUser user = auth.CurrentUser;
if (user != null) {
  user.SendEmailVerificationAsync().ContinueWith(task => {
    if (task.IsCanceled) {
      Debug.LogError("SendEmailVerificationAsync was canceled.");
      return;
    }
    if (task.IsFaulted) {
      Debug.LogError("SendEmailVerificationAsync encountered an error: " + task.Exception);
      return;
    }

    Debug.Log("Email sent successfully.");
  });
}
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

## Set a user's password

You can set a user's password with the `UpdatePassword` method. For example:

```c#
Firebase.Auth.FirebaseUser user = auth.CurrentUser;
string newPassword = "SOME-SECURE-PASSWORD";
if (user != null) {
  user.UpdatePasswordAsync(newPassword).ContinueWith(task => {
    if (task.IsCanceled) {
      Debug.LogError("UpdatePasswordAsync was canceled.");
      return;
    }
    if (task.IsFaulted) {
      Debug.LogError("UpdatePasswordAsync encountered an error: " + task.Exception);
      return;
    }

    Debug.Log("Password updated successfully.");
  });
}
```

> [!IMPORTANT]
> **Important:** To set a user's password, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/unity/manage-users#re-authenticate_a_user).

## Send a password reset email

You can send a password reset email to a user with the `SendPasswordResetEmail`
method. For example:

```c#
string emailAddress = "user@example.com";
if (user != null) {
  auth.SendPasswordResetEmailAsync(emailAddress).ContinueWith(task => {
    if (task.IsCanceled) {
      Debug.LogError("SendPasswordResetEmailAsync was canceled.");
      return;
    }
    if (task.IsFaulted) {
      Debug.LogError("SendPasswordResetEmailAsync encountered an error: " + task.Exception);
      return;
    }

    Debug.Log("Password reset email sent successfully.");
  });
}
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

You can also send password reset emails from the Firebase console.

## Delete a user

You can delete a user account with the `Delete` method. For example:

```c#
Firebase.Auth.FirebaseUser user = auth.CurrentUser;
if (user != null) {
  user.DeleteAsync().ContinueWith(task => {
    if (task.IsCanceled) {
      Debug.LogError("DeleteAsync was canceled.");
      return;
    }
    if (task.IsFaulted) {
      Debug.LogError("DeleteAsync encountered an error: " + task.Exception);
      return;
    }

    Debug.Log("User deleted successfully.");
  });
}
```

> [!IMPORTANT]
> **Important:** To delete a user, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/unity/manage-users#re-authenticate_a_user).

You can also delete users from the Authentication section of the
[Firebase console](https://console.firebase.google.com/), on the Users page.

## Re-authenticate a user

Some security-sensitive actions---such as
[deleting an account](https://firebase.google.com/docs/auth/unity/manage-users#delete_a_user),
[setting a primary email address](https://firebase.google.com/docs/auth/unity/manage-users#set_a_users_email_address), and
[changing a password](https://firebase.google.com/docs/auth/unity/manage-users#set_a_users_password)---require that the user has
recently signed in. If you perform one of these actions, and the user signed in
too long ago, the action fails.

When this happens, re-authenticate the user by getting new sign-in credentials
from the user and passing the credentials to `Reauthenticate`. For example:

```c#
Firebase.Auth.FirebaseUser user = auth.CurrentUser;

// Get auth credentials from the user for re-authentication. The example below shows
// email and password credentials but there are multiple possible providers,
// such as GoogleAuthProvider or FacebookAuthProvider.
Firebase.Auth.Credential credential =
    Firebase.Auth.EmailAuthProvider.GetCredential("user@example.com", "password1234");

if (user != null) {
  user.ReauthenticateAsync(credential).ContinueWith(task => {
    if (task.IsCanceled) {
      Debug.LogError("ReauthenticateAsync was canceled.");
      return;
    }
    if (task.IsFaulted) {
      Debug.LogError("ReauthenticateAsync encountered an error: " + task.Exception);
      return;
    }

    Debug.Log("User reauthenticated successfully.");
  });
}
```

## Import user accounts

You can import user accounts from a file into your Firebase project by using the
Firebase CLI's [`auth:import`](https://firebase.google.com/docs/cli/auth-import) command. For example:

    firebase auth:import users.json --hash-algo=scrypt --rounds=8 --mem-cost=14