# Source: https://firebase.google.com/docs/auth/cpp/start.md.txt

You can use Firebase Authentication to allow users to sign in to your app using one
or more sign-in methods, including email address and password sign-in, and
federated identity providers such as Google Sign-in and Facebook Login. This
tutorial gets you started with Firebase Authentication by showing you how to add
email address and password sign-in to your app.

## Connect your C++ project to Firebase

Before you can use
[Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth),
you need to:

- Register your C++ project and configure it to use Firebase.

  If your C++ project already uses Firebase, then it's already registered and
  configured for Firebase.
- Add the [Firebase C++ SDK](https://firebase.google.com/download/cpp) to your C++ project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your C++
> project](https://firebase.google.com/docs/cpp/setup#note-select-platform).**

Note that adding Firebase to your C++ project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open C++ project (for example, you download
Firebase config files from the console, then move them into your C++ project).

## Sign up new users

Create a form that allows new users to register with your app using their
email address and a password. When a user completes the form, validate the
email address and password provided by the user, then pass them to the
`CreateUserWithEmailAndPassword` method:

    firebase::Future<firebase::auth::AuthResult> result =
        auth->CreateUserWithEmailAndPassword(email, password);

You can check the status of the account creation operation either by registering
a callback on the `CreateUserWithEmailAndPasswordLastResult` Future object, or,
if you're writing a game or app with some kind of periodic update loop, by
polling the status in the update loop.

For example, using a Future:

    firebase::Future<firebase::auth::AuthResult> result =
        auth->CreateUserWithEmailAndPasswordLastResult();

    // The lambda has the same signature as the callback function.
    result.OnCompletion(
        [](const firebase::Future<firebase::auth::AuthResult>& result,
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

Or, to use polling, do something like the following example in your game's
update loop:

    firebase::Future<firebase::auth::AuthResult> result =
        auth->CreateUserWithEmailAndPasswordLastResult();
    if (result.status() == firebase::kFutureStatusComplete) {
      if (result.error() == firebase::auth::kAuthErrorNone) {
        firebase::auth::AuthResult* auth_result = *result.result();
        printf("Create user succeeded for email %s\n", auth_result.user.email().c_str());
      } else {
        printf("Created user failed with error '%s'\n", result.error_message());
      }
    }

## Sign in existing users

Create a form that allows existing users to sign in using their email address
and password. When a user completes the form, call the
`SignInWithEmailAndPassword` method:

    firebase::Future<firebase::auth::AuthResult> result =
        auth->SignInWithEmailAndPassword(email, password);

Get the result of the sign-in operation the same way you got the sign-up result.

## Set an authentication state listener and get account data

To respond to sign-in and sign-out events, attach a listener to the global
authentication object. This listener gets called whenever the user's sign-in
state changes. Because the listener runs only after the authentication object is
fully initialized and after any network calls have completed, it is the best
place to get information about the signed-in user.

Create the listener by implementing the `firebase::auth::AuthStateListener`
abstract class. For example, to create a listener that gets information about
the user when a user successfully signs in:

    class MyAuthStateListener : public firebase::auth::AuthStateListener {
     public:
      void OnAuthStateChanged(firebase::auth::Auth* auth) override {
        firebase::auth::User user = auth.current_user();
        if (user.is_valid()) {
          // User is signed in
          printf("OnAuthStateChanged: signed_in %s\n", user.uid().c_str());
          const std::string displayName = user.DisplayName();
          const std::string emailAddress = user.Email();
          const std::string photoUrl = user.PhotoUrl();
        } else {
          // User is signed out
          printf("OnAuthStateChanged: signed_out\n");
        }
        // ...
      }
    };

Attach the listener with the `firebase::auth::Auth` object's
`AddAuthStateListener` method:

    MyAuthStateListener state_change_listener;
    auth->AddAuthStateListener(&state_change_listener);

## Next steps

Learn how to add support for other identity providers and anonymous guest
accounts:

- [Google Sign-in](https://firebase.google.com/docs/auth/cpp/google-signin)
- [Facebook Login](https://firebase.google.com/docs/auth/cpp/facebook-login)
- [Apple Login](https://firebase.google.com/docs/auth/cpp/apple)
- [Twitter Login](https://firebase.google.com/docs/auth/cpp/twitter-login)
- [GitHub Login](https://firebase.google.com/docs/auth/cpp/github-auth)
- [Microsoft Login](https://firebase.google.com/docs/auth/cpp/microsoft-oauth)
- [Yahoo Login](https://firebase.google.com/docs/auth/cpp/yahoo-oauth)
- [Anonymous sign-in](https://firebase.google.com/docs/auth/cpp/anonymous-auth)
- [Phone Authentication](https://firebase.google.com/docs/auth/cpp/phone-auth)