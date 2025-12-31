# Source: https://firebase.google.com/docs/auth/web/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/android/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/password-auth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/password-auth.md.txt

You can useFirebase Authenticationto let your users authenticate with Firebase using their email addresses and passwords, and to manage your app's password-based accounts.

## Before you begin

1. [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup#note_select_platform).
2. If you haven't yet connected your app to your Firebase project, do so from the[Firebaseconsole](https://console.firebase.google.com/).
3. Enable Email/Password sign-in:
   1. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
   2. On the**Sign in method** tab, enable the**Email/password** sign-in method and click**Save**.

## Access the`firebase::auth::Auth`class

The`Auth`class is the gateway for all API calls.

1. Add the Auth and App header files:  

   ```c++
   #include "firebase/app.h"
   #include "firebase/auth.h"
   ```
2. In your initialization code, create a[`firebase::App`](https://firebase.google.com/docs/reference/cpp/class/firebase/app)class.  

   ```c++
   #if defined(__ANDROID__)
     firebase::App* app =
         firebase::App::Create(firebase::AppOptions(), my_jni_env, my_activity);
   #else
     firebase::App* app = firebase::App::Create(firebase::AppOptions());
   #endif  // defined(__ANDROID__)
   ```
3. Acquire the`firebase::auth::Auth`class for your`firebase::App`. There is a one-to-one mapping between`App`and`Auth`.  

   ```c++
   firebase::auth::Auth* auth = firebase::auth::Auth::GetAuth(app);
   ```

## Create a password-based account

To create a new user account with a password, complete the following steps in your app's sign-in code:

1. When a new user signs up using your app's sign-up form, complete any new account validation steps that your app requires, such as verifying that the new account's password was correctly typed and meets your complexity requirements.
2. Create a new account by passing the new user's email address and password to`Auth::CreateUserWithEmailAndPassword`:  

   ```c++
   firebase::Future<firebase::auth::AuthResult> result =
       auth->CreateUserWithEmailAndPassword(email, password);
   ```
3. If your program has an update loop that runs regularly (say at 30 or 60 times per second), you can check the results once per update with`Auth::CreateUserWithEmailAndPasswordLastResult`:  

   ```c++
   firebase::Future<firebase::auth::AuthResult> result =
       auth->CreateUserWithEmailAndPasswordLastResult();
   if (result.status() == firebase::kFutureStatusComplete) {
     if (result.error() == firebase::auth::kAuthErrorNone) {
       const firebase::auth::AuthResult auth_result = *result.result();
       printf("Create user succeeded for email %s\n",
              auth_result.user.email().c_str());
     } else {
       printf("Created user failed with error '%s'\n", result.error_message());
     }
   }
   ```
   Or, if your program is event driven, you may prefer to[register a callback on the Future](https://firebase.google.com/docs/auth/cpp/password-auth#register_callback_on_future).

| To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the[Firebaseconsole](https://console.firebase.google.com/project/_/authentication/providers).

## Sign in a user with an email address and password

The steps for signing in a user with a password are similar to the steps for creating a new account. In your app's sign-in function, do the following:

1. When a user signs in to your app, pass the user's email address and password to`firebase::auth::Auth::SignInWithEmailAndPassword`:  

   ```c++
   firebase::Future<firebase::auth::AuthResult> result =
       auth->SignInWithEmailAndPassword(email, password);
   ```
2. If your program has an update loop that runs regularly (say at 30 or 60 times per second), you can check the results once per update with`Auth::SignInWithEmailAndPasswordLastResult`:  

   ```c++
   firebase::Future<firebase::auth::AuthResult> result =
       auth->SignInWithEmailAndPasswordLastResult();
   if (result.status() == firebase::kFutureStatusComplete) {
     if (result.error() == firebase::auth::kAuthErrorNone) {
       const firebase::auth::AuthResult auth_result = *result.result();
       printf("Sign in succeeded for email %s\n",
              auth_result.user.email().c_str());
     } else {
       printf("Sign in failed with error '%s'\n", result.error_message());
     }
   }
   ```
   Or, if your program is event driven, you may prefer to[register a callback on the Future](https://firebase.google.com/docs/auth/cpp/password-auth#register_callback_on_future).

## Register a callback on a Future

Some programs have`Update`functions that are called 30 or 60 times per second. For example, many games follow this model. These programs can call the`LastResult`functions to poll asynchronous calls. However, if your program is event driven, you may prefer to register callback functions. A callback function is called upon completion of the Future.  

```c++
void OnCreateCallback(const firebase::Future<firebase::auth::User*>& result,
                      void* user_data) {
  // The callback is called when the Future enters the `complete` state.
  assert(result.status() == firebase::kFutureStatusComplete);

  // Use `user_data` to pass-in program context, if you like.
  MyProgramContext* program_context = static_cast<MyProgramContext*>(user_data);

  // Important to handle both success and failure situations.
  if (result.error() == firebase::auth::kAuthErrorNone) {
    firebase::auth::User* user = *result.result();
    printf("Create user succeeded for email %s\n", user->email().c_str());

    // Perform other actions on User, if you like.
    firebase::auth::User::UserProfile profile;
    profile.display_name = program_context->display_name;
    user->UpdateUserProfile(profile);

  } else {
    printf("Created user failed with error '%s'\n", result.error_message());
  }
}

void CreateUser(firebase::auth::Auth* auth) {
  // Callbacks work the same for any firebase::Future.
  firebase::Future<firebase::auth::AuthResult> result =
      auth->CreateUserWithEmailAndPasswordLastResult();

  // `&my_program_context` is passed verbatim to OnCreateCallback().
  result.OnCompletion(OnCreateCallback, &my_program_context);
}
```
The callback function can also be a lambda, if you prefer.  

```c++
void CreateUserUsingLambda(firebase::auth::Auth* auth) {
  // Callbacks work the same for any firebase::Future.
  firebase::Future<firebase::auth::AuthResult> result =
      auth->CreateUserWithEmailAndPasswordLastResult();

  // The lambda has the same signature as the callback function.
  result.OnCompletion(
      [](const firebase::Future<firebase::auth::User*>& result,
         void* user_data) {
        // `user_data` is the same as &my_program_context, below.
        // Note that we can't capture this value in the [] because std::function
        // is not supported by our minimum compiler spec (which is pre C++11).
        MyProgramContext* program_context =
            static_cast<MyProgramContext*>(user_data);

        // Process create user result...
        (void)program_context;
      },
      &my_program_context);
}
```

## Recommended: Set a password policy

You can improve account security by enforcing password complexity requirements.

To configure a password policy for your project, open the**Password policy** tab on the Authentication Settings page of theFirebaseconsole:

[Authentication Settings](https://console.firebase.google.com/project/_/authentication/settings)

Firebase Authenticationpassword policies support the following password requirements:

- Lowercase character required

- Uppercase character required

- Numeric character required

- Non-alphanumeric character required

  The following characters satisfy the non-alphanumeric character requirement:`^ $ * . [ ] { } ( ) ? " ! @ # % & / \ , > < ' : ; | _ ~`
- Minimum password length (ranges from 6 to 30 characters; defaults to 6)

- Maximum password length (maximum length of 4096 characters)

You can enable password policy enforcement in two modes:

- **Require**: Attempts to sign up fail until the user updates to a password that complies with your policy.

- **Notify**: Users are allowed to sign up with a non-compliant password. When using this mode, you should check if the user's password complies with the policy on the client side and prompt the user in some way to update their password if it does not comply.

New users are always required to choose a password that complies with your policy.

If you have active users, we recommend not enabling force upgrade on sign in unless you intend to block access to users whose passwords don't comply with your policy. Instead, use notify mode, which allows users to sign in with their current passwords, and inform them of the requirements their password lacks.

## Recommended: Enable email enumeration protection

SomeFirebase Authenticationmethods that take email addresses as parameters throw specific errors if the email address is unregistered when it must be registered (for example, when signing in with an email address and password), or registered when it must be unused (for example, when changing a user's email address). While this can be helpful for suggesting specific remedies to users, it can also be abused by malicious actors to discover the email addresses registered by your users.

To mitigate this risk, we recommend you[enable email enumeration protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)for your project using the Google Cloud`gcloud`tool. Note that enabling this feature changesFirebase Authentication's error reporting behavior: be sure your app doesn't rely on the more specific errors.

## Next steps

After a user signs in for the first time, a new user account is created and linked to the credentials---that is, the user name and password, phone number, or auth provider information---the user signed in with. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the[`firebase::auth::User`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user)object:

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
- In yourFirebase Realtime DatabaseandCloud Storage[Security Rules](https://firebase.google.com/docs/database/security/user-security), you can get the signed-in user's unique user ID from the`auth`variable, and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication providers by[linking auth provider credentials to an existing user account.](https://firebase.google.com/docs/auth/cpp/account-linking)

To sign out a user, call[`SignOut()`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#signout):  

```c++
auth->SignOut();
```