# Source: https://firebase.google.com/docs/auth/android/play-games.md.txt

# Source: https://firebase.google.com/docs/auth/unity/play-games.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/play-games.md.txt

# Source: https://firebase.google.com/docs/auth/unity/play-games.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/play-games.md.txt

You can use Google Play Games services to sign in players to an Android game built on Firebase and written in C++. To use Google Play Games services sign-in with Firebase, first sign in the player with Google Play Games, and request an OAuth 2.0 auth code when you do so. Then, pass the auth code to`PlayGamesAuthProvider`to generate a Firebase credential, which you can use to authenticate with Firebase.
| **Important:** You can use Google Play Games services sign-in only on Android.

## Before you begin

Before you can use[Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth), you need to:

- Register your C++ project and configure it to use Firebase.

  If your C++ project already uses Firebase, then it's already registered and configured for Firebase.
- Add the[FirebaseC++SDK](https://firebase.google.com/download/cpp)to your C++ project.

| **Find detailed instructions for these initial setup tasks in[Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup#note-select-platform).**

Note that adding Firebase to your C++ project involves tasks both in the[Firebaseconsole](https://console.firebase.google.com/)and in your open C++ project (for example, you download Firebase config files from the console, then move them into your C++ project).

### Set up your Firebase project

1. If you haven't already, set your game's SHA-1 fingerprint in the[Settings](https://console.firebase.google.com/project/_/settings/general/)page of theFirebaseconsole.

   You can get the SHA hash of your signing certificate with the gradle`signingReport`command:  

   ```
   ./gradlew signingReport
   ```

   <br />

2. EnableGoogle Play Gamesas a sign-in provider:

   1. In theFirebaseconsole, open the[**Authentication**section](https://console.firebase.google.com/project/_/authentication/providers).

   2. Generate and obtain your project's web server client ID and client secret:

      1. Within the**Sign in method** tab, enable the**Google**sign-in provider.

      2. Copy the web server client ID and secret from the**Google**sign-in provider.

   3. Within the**Sign in method** tab, enable the**Play Games**sign-in provider, and specify your project's web server client ID and client secret, which you got in the last step.

### ConfigurePlay Gamesserviceswith your Firebase app information

1. In the[Google PlayConsole](https://play.google.com/console/developers), open yourGoogle Playapp or create one.

2. In the*Grow* section, click**Play Gamesservices\> Setup \& Management \> Configuration**.

3. Click**Yes, my game already uses Google APIs** , select your Firebase project from the list, and then click**Use**.

4. On thePlay Gamesservicesconfiguration page, click**Add Credential**.

   1. Select the**Game server**type.
   2. In the**OAuth client** field, select your project's web client ID. Be sure this is the same client ID you specified when you enabledPlay Gamessign-in.
   3. Save your changes.
5. Still on thePlay Gamesservicesconfiguration page, click**Add Credential**again.

   1. Select the**Android**type.
   2. In the**OAuth client** field, select your project's Android client ID. (If you don't see your Android client ID, be sure you set your game's SHA-1 fingerprint in theFirebaseconsole.)
   3. Save your changes.
6. On the**Testers** page, add the email addresses of any users who need to be able to sign in to your game before you release it on thePlayStore.

## Integrate Play Games sign-in into your game

Before you can sign players in to your game, you must integrate Google Play Games sign-in.

The easiest and recommended way to add support for Play Games sign-in to a C++ Android project is to use the[Google Sign-in C++ SDK](https://github.com/googlesamples/google-signin-unity/tree/master/staging/native).

To add Play Games sign-in to your game using the Google Sign-in C++ SDK, do the following:

1. Clone or download the[Google Sign-in Unity plugin repository](https://github.com/googlesamples/google-signin-unity), which also contains the C++ SDK.

2. Build the project contained in the`staging/native/`directory, either using Android Studio or`gradlew build`.

   The build copies its output to a directory named`google-signin-cpp`.
3. Include the Google Sign-in C++ SDK in your game's native code make file:

   #### CMake

   In your top-level`CMakeLists.txt`file:  

   ```cmake
   set(GSI_PACKAGE_DIR "/path/to/google-signin-cpp")

   add_library(lib-google-signin-cpp STATIC IMPORTED)
   set_target_properties(lib-google-signin-cpp PROPERTIES IMPORTED_LOCATION
   Â Â Â Â ${GSI_PACKAGE_DIR}/lib/${ANDROID_ABI}/libgoogle-signin-cpp.a )

   ...

   target_link_libraries(
   Â Â Â Â ...
   Â Â Â Â lib-google-signin-cpp)
   ```

   #### ndk-build

   In your`Android.mk`file:  

   ```c++
   include $(CLEAR_VARS)
   LOCAL_MODULE := google-signin-cpp
   GSI_SDK_DIR := /path/to/google-signin-cpp
   LOCAL_SRC_FILES := $(GSI_SDK_DIR)/lib/$(TARGET_ARCH_ABI)/libgoogle-signin-cpp.a
   LOCAL_EXPORT_C_INCLUDES := $(GSI_SDK_DIR)/include
   include $(PREBUILT_STATIC_LIBRARY)
   ```

   <br />

4. Next, include the Java helper component, which is required by the C++ SDK.

   To do so, in your project-level`build.gradle`file, add the SDK build output directory as a local repository:  

       allprojects {
           repositories {
               // ...
               flatDir {
                   dirs 'path/to/google-signin-cpp'
               }
           }
       }

   And, in your module-level`build.gradle`file, declare the helper component as a dependency:  

       dependencies {
           implementation 'com.google.android.gms:play-services-auth:21.4.0'
           // Depend on the AAR built with the Google Sign-in SDK in order to add
           // the Java helper classes, which are used by the C++ library.
           compile(name:'google-signin-cpp-release', ext:'aar')
       }

5. Then, in your game, configure a`GoogleSignIn`object to use Play Games sign-in and to retrieve a server auth code:

       #include "google_signin.h"
       #include "future.h"

       using namespace google::signin;

       // ...

       GoogleSignIn::Configuration config = {};
       config.web_client_id = "YOUR_WEB_CLIENT_ID_HERE";
       config.request_id_token = false;
       config.use_game_signin = true;
       config.request_auth_code = true;

       GoogleSignIn gsi = GoogleSignIn(GetActivity(), GetJavaVM());
       gsi.Configure(config);

6. Finally, call`SignIn()`to sign the player in to Play Games:

       Future<GoogleSignIn::SignInResult> &future = gsi.SignIn();

   When the Future returned by`SignIn()`resolves, you can get the server auth code from the result:  

       if (!future.Pending()) {
           const GoogleSignIn::StatusCode status =
                   static_cast<GoogleSignIn::StatusCode>(future.Status());
           if (status == GoogleSignIn::kStatusCodeSuccess) {
               // Player successfully signed in to Google Play! Get auth code to
               //   pass to Firebase
               const GoogleSignIn::SignInResult result =
                       static_cast<GoogleSignIn::SignInResult>(future.Result());
               const char* server_auth_code = result.User.GetServerAuthCode();
           }
       }

## Authenticate with Firebase

After the player signs in with Play Games, you can use the auth code to authenticate with Firebase.

1. After the player has successfully signed in using Play Games, get an auth code for the player's account.

2. Then, exchange the auth code from Play Games services for a Firebase credential, and use the Firebase credential to authenticate the player:

       firebase::auth::Credential credential =
           firebase::auth::PlayGamesAuthProvider::GetCredential(server_auth_code);
       firebase::Future<firebase::auth::AuthResult> result =
           auth->SignInAndRetrieveDataWithCredential(credential);

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

   <br />

   Or, if your program is event driven, you may prefer to[register a callback on the Future](https://firebase.google.com/docs/auth/cpp/play-games#register_callback_on_future).

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

After a user signs in for the first time, a new user account is created and linked to their Play Games ID. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project.

In your game, you can get the user's Firebase UID from the`firebase::auth::User`object:  

    firebase::auth::User user = auth->current_user();
    if (user.is_valid()) {
      std::string playerName = user.displayName();

      // The user's ID, unique to the Firebase project.
      // Do NOT use this value to authenticate with your backend server,
      // if you have one. Use firebase::auth::User::Token() instead.
      std::string uid = user.uid();
    }

In your Firebase Realtime Database and Cloud Storage Security Rules, you can get the signed-in user's unique user ID from the`auth`variable, and use it to control what data a user can access.

To get a user's Play Games player information or to access Play Games services, use the APIs provided by the[Google Play Games services C++ SDK](https://developers.google.com/games/services/cpp/GettingStartedNativeClient).

To sign out a user, call`SignOut()`:  

    auth->SignOut();