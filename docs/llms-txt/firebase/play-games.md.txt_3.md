# Source: https://firebase.google.com/docs/auth/android/play-games.md.txt

You can use Google Play Games services to sign players in to an Android game
built on Firebase. To use Google Play Games services sign-in with Firebase,
first sign the player in with Google Play Games, and request an OAuth 2.0 auth
code when you do so. Then, pass the auth code to `PlayGamesAuthProvider` to
generate a Firebase credential, which you can use to authenticate with Firebase.

## Before you begin

### Set up your Android project

1. If you haven't already,
   [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2.


   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the Firebase Authentication library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.

   Also, as part of setting up Firebase Authentication, you need to add the
   Google Play services SDK to your app.


   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the Firebase Authentication library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth")

       // Also add the dependency for the Google Play services library and specify its version
       implementation("com.google.android.gms:play-services-auth:21.5.1")
   }
   ```

   By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)*
   Add Firebase library dependencies *without* using the BoM

   If you choose not to use the Firebase BoM, you must specify each Firebase library version
   in its dependency line.

   **Note that if you use *multiple* Firebase libraries in your app, we strongly
   recommend using the BoM to manage library versions, which ensures that all versions are
   compatible.**

   ```groovy
   dependencies {
       // Add the dependency for the Firebase Authentication library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth:24.0.1")

       // Also add the dependency for the Google Play services library and specify its version
       implementation("com.google.android.gms:play-services-auth:21.5.1")
   }
   ```

   <br />

### Set up your Firebase project

1. Set your game's SHA-1 fingerprint from the
   [Settings](https://console.firebase.google.com/project/_/settings/general/) page
   of the Firebase console.

   You can get the SHA hash of your signing certificate with the gradle
   `signingReport` command:

   ```
   ./gradlew signingReport
   ```

   <br />

2. Enable Google Play Games as a sign-in provider:

   1. Find your project's web server client ID and client secret. The web
      server client ID identifies your Firebase project to the Google Play
      auth servers.

      To find these values:
      1. Open your Firebase project in the [Google APIs console](https://console.developers.google.com/apis/credentials?project=_) credentials page.
      2. In the **OAuth 2.0 client IDs** section, open the **Web client (auto
         created by Google Service)** details page. This page lists your web server client ID and secret.
   2. Then, in the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section.

   3. On the **Sign in method** tab, enable the **Play Games** sign-in
      provider. You will need to specify your project's web server
      client ID and client secret, which you got from the APIs console.

### Configure Play Games services with your Firebase app information

1. In the
   [Google Play Console](https://play.google.com/console/developers),
   open your Google Play app or create one.

2. In the *Grow* section, click
   **Play Games services \> Setup \& Management \> Configuration**.

3. Click **Yes, my game already uses Google APIs** , select your Firebase
   project from the list, and then click **Use**.

4. On the Play Games services configuration page, click
   **Add Credential**.

   1. Select the **Game server** type.
   2. In the **OAuth client** field, select your project's web client ID. Be sure this is the same client ID you specified when you enabled Play Games sign-in.
   3. Save your changes.
5. Still on the Play Games services configuration page, click
   **Add Credential** again.

   1. Select the **Android** type.
   2. In the **OAuth client** field, select your project's Android client ID. (If you don't see your Android client ID, be sure you set your game's SHA-1 fingerprint in the Firebase console.)
   3. Save your changes.
6. On the **Testers** page, add the email addresses of any users who need
   to be able to sign in to your game before you release it on the
   Play Store.

## Integrate Play Games sign-in into your game

First, integrate Play Games sign-in into your app. See
[Sign in to Android Games](https://developers.google.com/games/services/android/signin)
for complete instructions.

In your integration, when you build the `GoogleSignInOptions` object, use the
`DEFAULT_GAMES_SIGN_IN` configuration and call `requestServerAuthCode`:

### Kotlin

```kotlin
val gso = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN)
    .requestServerAuthCode(getString(R.string.default_web_client_id))
    .build()
```

### Java

```java
GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN)
        .requestServerAuthCode(getString(R.string.default_web_client_id))
        .build();
```

You must pass your web server client ID to the `requestServerAuthCode` method.
This is the ID that you provided when you enabled Play Games sign-in in the
Firebase console.

## Authenticate with Firebase

After you add Play Games sign-in to your app, you need to set up Firebase to use
the Google account credentials that you get when a player signs in successfully
with Play Games.

1. First, in your sign-in activity's `onCreate` method, get the shared instance of the `FirebaseAuth` object:

### Kotlin

```kotlin
private lateinit var auth: FirebaseAuth
// ...
// Initialize Firebase Auth
auth = Firebase.authhttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GoogleSignInActivity.kt#L42-L43
```

### Java

```java
private FirebaseAuth mAuth;
// ...
// Initialize Firebase Auth
mAuth = FirebaseAuth.getInstance();
```

1. When initializing your Activity, check to see if the player is already signed in with Firebase:

### Kotlin

```kotlin
override fun onStart() {
    super.onStart()
    // Check if user is signed in (non-null) and update UI accordingly.
    val currentUser = auth.currentUser
    updateUI(currentUser)
}
```

### Java

```java
@Override
public void onStart() {
    super.onStart();
    // Check if user is signed in (non-null) and update UI accordingly.
    FirebaseUser currentUser = mAuth.getCurrentUser();
    updateUI(currentUser);
}
```

    If the player isn't signed in, present the player with your game's
    signed-out experience, including the option to sign in.

1. After a player signs in with Play Games either silently or interactively, get the auth code from the `GoogleSignInAccount` object, exchange it for a Firebase credential, and authenticate with Firebase using the Firebase credential:

### Kotlin

```kotlin
// Call this both in the silent sign-in task's OnCompleteListener and in the
// Activity's onActivityResult handler.
private fun firebaseAuthWithPlayGames(acct: GoogleSignInAccount) {
    Log.d(TAG, "firebaseAuthWithPlayGames:" + acct.id!!)

    val auth = Firebase.auth
    val credential = PlayGamesAuthProvider.getCredential(acct.serverAuthCode!!)
    auth.signInWithCredential(credential)
        .addOnCompleteListener(this) { task ->
            if (task.isSuccessful) {
                // Sign in success, update UI with the signed-in user's information
                Log.d(TAG, "signInWithCredential:success")
                val user = auth.currentUser
                updateUI(user)
            } else {
                // If sign in fails, display a message to the user.
                Log.w(TAG, "signInWithCredential:failure", task.exception)
                Toast.makeText(
                    baseContext,
                    "Authentication failed.",
                    Toast.LENGTH_SHORT,
                ).show()
                updateUI(null)
            }

            // ...
        }
}
```

### Java

```java
// Call this both in the silent sign-in task's OnCompleteListener and in the
// Activity's onActivityResult handler.
private void firebaseAuthWithPlayGames(GoogleSignInAccount acct) {
    Log.d(TAG, "firebaseAuthWithPlayGames:" + acct.getId());

    final FirebaseAuth auth = FirebaseAuth.getInstance();
    AuthCredential credential = PlayGamesAuthProvider.getCredential(acct.getServerAuthCode());
    auth.signInWithCredential(credential)
            .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if (task.isSuccessful()) {
                        // Sign in success, update UI with the signed-in user's information
                        Log.d(TAG, "signInWithCredential:success");
                        FirebaseUser user = auth.getCurrentUser();
                        updateUI(user);
                    } else {
                        // If sign in fails, display a message to the user.
                        Log.w(TAG, "signInWithCredential:failure", task.getException());
                        Toast.makeText(MainActivity.this, "Authentication failed.",
                                Toast.LENGTH_SHORT).show();
                        updateUI(null);
                    }

                    // ...
                }
            });
}
```

If the call to `signInWithCredential` succeeds you can use the `getCurrentUser` method to get the user's account data.

## Next steps

After a user signs in for the first time, a new user account is created and
linked to their Play Games ID. This new account is stored as part of your
Firebase project, and can be used to identify a user across every app in your
project.

In your game, you can get the user's Firebase UID from the `FirebaseUser`
object:

### Kotlin

```kotlin
val user = auth.currentUser
user?.let {
    val playerName = it.displayName

    // The user's Id, unique to the Firebase project.
    // Do NOT use this value to authenticate with your backend server, if you
    // have one; use FirebaseUser.getIdToken() instead.
    val uid = it.uid
}
```

### Java

```java
FirebaseUser user = mAuth.getCurrentUser();
String playerName = user.getDisplayName();

// The user's Id, unique to the Firebase project.
// Do NOT use this value to authenticate with your backend server, if you
// have one; use FirebaseUser.getIdToken() instead.
String uid = user.getUid();
```

In your Firebase Realtime Database and Cloud Storage Security Rules, you can get
the signed-in user's unique user ID from the `auth` variable, and use it to
control what data a user can access.

To get a user's Play Games player information or to access Play Games services,
use the APIs provided by the [Google Play Games SDK](https://developers.google.com/games/services/android/quickstart).

To sign out a user, call `FirebaseAuth.signOut()`:

### Kotlin

```kotlin
Firebase.auth.signOut()
```

### Java

```java
FirebaseAuth.getInstance().signOut();
```