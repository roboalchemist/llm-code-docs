# Source: https://firebase.google.com/docs/auth/ios/github-auth.md.txt

# Source: https://firebase.google.com/docs/auth/android/github-auth.md.txt

# Source: https://firebase.google.com/docs/auth/web/github-auth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/github-auth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/github-auth.md.txt

# Source: https://firebase.google.com/docs/auth/web/github-auth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/github-auth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/github-auth.md.txt

You can let your users authenticate with Firebase using their GitHub accounts by integrating GitHub authentication into your app.

## Before you begin

1. [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup#note_select_platform).
2. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
3. On the**Sign in method** tab, enable the**GitHub**provider.
4. Add the**Client ID** and**Client Secret** from that provider's developer console to the provider configuration:
   1. [Register your app](https://github.com/settings/applications/new)as a developer application on GitHub and get your app's OAuth 2.0**Client ID** and**Client Secret**.
   2. Make sure your Firebase**OAuth redirect URI** (e.g.`my-app-12345.firebaseapp.com/__/auth/handler`) is set as your**Authorization callback URL** in your app's settings page on your[GitHub app's config](https://github.com/settings/developers).
5. Click**Save**.

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

## Authenticate with Firebase

1. Follow instructions for[Android](https://firebase.google.com/docs/auth/android/github-auth#authenticate_with_firebase)and[iOS+](https://firebase.google.com/docs/auth/ios/github-auth#authenticate_with_firebase)to get a token for the signed-in GitHub user.
2. After a user successfully signs in, exchange the token for a Firebase credential, and authenticate with Firebase using the Firebase credential:  

   ```c++
   firebase::auth::Credential credential =
       firebase::auth::GitHubAuthProvider::GetCredential(token);
   firebase::Future<firebase::auth::AuthResult> result =
       auth->SignInAndRetrieveDataWithCredential(credential);
   ```
3. If your program has an update loop that runs regularly (say at 30 or 60 times per second), you can check the results once per update with`Auth::SignInAndRetrieveDataWithCredentialLastResult`:  

   ```c++
   firebase::Future<firebase::auth::AuthResult> result =
       auth->SignInAndRetrieveDataWithCredentialLastResult();
   if (result.status() == firebase::kFutureStatusComplete) {
     if (result.error() == firebase::auth::kAuthErrorNone) {
       firebase::auth::AuthResult auth_result = *result.result();
       printf("Sign in succeeded for `%s`\n",
              auth_result.user.display_name().c_str());
     } else {
       printf("Sign in failed with error '%s'\n", result.error_message());
     }
   }
   ```
   Or, if your program is event driven, you may prefer to[register a callback on the Future](https://firebase.google.com/docs/auth/cpp/github-auth#register_callback_on_future).

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