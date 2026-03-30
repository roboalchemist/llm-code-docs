# Source: https://firebase.google.com/docs/auth/cpp/manage-users.md.txt

## Create a user

You create a new user in your Firebase project by calling the
[`CreateUserWithEmailAndPassword`](https://firebase.google.com/docs/auth/cpp/password-auth#create_a_password-based_account)
method or by signing in a user for the first time using a federated identity
provider, such as [Google Sign-In](https://firebase.google.com/docs/auth/cpp/google-signin) or
[Facebook Login](https://firebase.google.com/docs/auth/cpp/facebook-login).

You can also create new password-authenticated users from the Authentication
section of the [Firebase console](https://console.firebase.google.com/), on the Users page.

## Get the currently signed-in user

The recommended way to get the current user is by setting a listener on the
Auth object:

```c++
class MyAuthStateListener : public firebase::auth::AuthStateListener {
 public:
  void OnAuthStateChanged(firebase::auth::Auth* auth) override {
    firebase::auth::User user = auth->current_user();
    if (user.is_valid()) {
      // User is signed in
      printf("OnAuthStateChanged: signed_in %s\n", user.uid().c_str());
    } else {
      // User is signed out
      printf("OnAuthStateChanged: signed_out\n");
    }
    // ...
  }
};
// ... initialization code
// Test notification on registration.
MyAuthStateListener state_change_listener;
auth->AddAuthStateListener(&state_change_listener);
```

By using a listener, you ensure that the Auth object isn't in an intermediate
state---such as initialization---when you get the current user.

You can also get the currently signed-in user by calling `current_user`. If a
user isn't signed in, the user's `is_valid` method will return false.

> [!NOTE]
> **Note:** `current_user` might be invalid because the `Auth` object has not finished initializing. If you use a listener to keep track of the user's sign-in status, you don't need to handle this case.

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
`firebase::auth::User`. For example:

```c++
firebase::auth::User user = auth->current_user();
if (user.is_valid()) {
  std::string name = user.display_name();
  std::string email = user.email();
  std::string photo_url = user.photo_url();
  // The user's ID, unique to the Firebase project.
  // Do NOT use this value to authenticate with your backend server,
  // if you have one. Use firebase::auth::User::Token() instead.
  std::string uid = user.uid();
}
```

## Get a user's provider-specific profile information

To get the profile information retrieved from the sign-in providers linked to a
user, use the `ProviderData` method. For example:

```c++
firebase::auth::User user = auth->current_user();
if (user.is_valid()) {
  for (auto it = user.provider_data().begin();
       it != user.provider_data().end(); ++it) {
    firebase::auth::UserInfoInterface profile = *it;
    // Id of the provider (ex: google.com)
    std::string providerId = profile.provider_id();

    // UID specific to the provider
    std::string uid = profile.uid();

    // Name, email address, and profile photo Url
    std::string name = profile.display_name();
    std::string email = profile.email();
    std::string photoUrl = profile.photo_url();
  }
}
```

## Update a user's profile

You can update a user's basic profile information---the user's display name
and profile photo URL---with the `UpdateUserProfile` method. For example:

```c++
firebase::auth::User user = auth->current_user();
if (user.is_valid()) {
  firebase::auth::User::UserProfile profile;
  profile.display_name = "Jane Q. User";
  profile.photo_url = "https://example.com/jane-q-user/profile.jpg";
  user.UpdateUserProfile(profile).OnCompletion(
      [](const firebase::Future<void>& completed_future, void* user_data) {
        // We are probably in a different thread right now.
        if (completed_future.error() == 0) {
          printf("User profile updated.");
        }
      },
      nullptr);  // pass user_data here.
}
```

## Set a user's email address

You can set a user's email address with the `UpdateEmail` method. For example:

```c++
firebase::auth::User user = auth->current_user();
if (user.is_valid()) {
  user.UpdateEmail("user@example.com")
      .OnCompletion(
          [](const firebase::Future<void>& completed_future,
             void* user_data) {
            // We are probably in a different thread right now.
            if (completed_future.error() == 0) {
              printf("User email address updated.");
            }
          },
          nullptr);
}
```

> [!IMPORTANT]
> **Important:** To set a user's email address, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/cpp/manage-users#re-authenticate_a_user).

## Send a user a verification email

You can send an address verification email to a user with the
`SendEmailVerification` method. For example:

```c++
firebase::auth::User user = auth->current_user();
if (user.is_valid()) {
  user.SendEmailVerification().OnCompletion(
      [](const firebase::Future<void>& completed_future, void* user_data) {
        // We are probably in a different thread right now.
        if (completed_future.error() == 0) {
          printf("Email sent.");
        }
      },
      nullptr);
}
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

## Set a user's password

You can set a user's password with the `UpdatePassword` method. For example:

```c++
firebase::auth::User user = auth->current_user();
std::string newPassword = "SOME-SECURE-PASSWORD";

if (user.is_valid()) {
  user.UpdatePassword(newPassword.c_str())
      .OnCompletion(
          [](const firebase::Future<void>& completed_future,
             void* user_data) {
            // We are probably in a different thread right now.
            if (completed_future.error() == 0) {
              printf("password updated.");
            }
          },
          nullptr);
}
```

> [!IMPORTANT]
> **Important:** To set a user's password, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/cpp/manage-users#re-authenticate_a_user).

## Send a password reset email

You can send a password reset email to a user with the `SendPasswordResetEmail`
method. For example:

```c++
std::string emailAddress = "user@example.com";

auth->SendPasswordResetEmail(emailAddress.c_str())
    .OnCompletion(
        [](const firebase::Future<void>& completed_future,
           void* user_data) {
          // We are probably in a different thread right now.
          if (completed_future.error() == 0) {
            // Email sent.
          } else {
            // An error happened.
            printf("Error %d: %s", completed_future.error(),
                   completed_future.error_message());
          }
        },
        nullptr);
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

You can also send password reset emails from the Firebase console.

## Delete a user

You can delete a user account with the `Delete` method. For example:

```c++
firebase::auth::User user = auth->current_user();
if (user.is_valid()) {
  user.Delete().OnCompletion(
      [](const firebase::Future<void>& completed_future, void* user_data) {
        if (completed_future.error() == 0) {
          // User deleted.
        } else {
          // An error happened.
          printf("Error %d: %s", completed_future.error(),
                 completed_future.error_message());
        }
      },
      nullptr);
}
```

> [!IMPORTANT]
> **Important:** To delete a user, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/cpp/manage-users#re-authenticate_a_user).

You can also delete users from the Authentication section of the
[Firebase console](https://console.firebase.google.com/), on the Users page.

## Re-authenticate a user

Some security-sensitive actions---such as
[deleting an account](https://firebase.google.com/docs/auth/cpp/manage-users#delete_a_user),
[setting a primary email address](https://firebase.google.com/docs/auth/cpp/manage-users#set_a_users_email_address), and
[changing a password](https://firebase.google.com/docs/auth/cpp/manage-users#set_a_users_password)---require that the user has
recently signed in. If you perform one of these actions, and the user signed in
too long ago, the action fails.

When this happens, re-authenticate the user by getting new sign-in credentials
from the user and passing the credentials to `Reauthenticate`. For example:

```c++
firebase::auth::User user = auth->current_user();

// Get auth credentials from the user for re-authentication. The example
// below shows email and password credentials but there are multiple
// possible providers, such as GoogleAuthProvider or FacebookAuthProvider.
firebase::auth::Credential credential =
    firebase::auth::EmailAuthProvider::GetCredential("user@example.com",
                                                     "password1234");

if (user.is_valid()) {
  user.Reauthenticate(credential)
      .OnCompletion(
          [](const firebase::Future<void>& completed_future,
             void* user_data) {
            if (completed_future.error() == 0) {
              printf("User re-authenticated.");
            }
          },
          nullptr);
}
```

## Import user accounts

You can import user accounts from a file into your Firebase project by using the
Firebase CLI's [`auth:import`](https://firebase.google.com/docs/cli/auth-import) command. For example:

    firebase auth:import users.json --hash-algo=scrypt --rounds=8 --mem-cost=14