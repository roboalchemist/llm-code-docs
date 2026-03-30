# Source: https://firebase.google.com/docs/auth/android/start.md.txt

## Connect your app to Firebase

[Video](https://www.youtube.com/watch?v=wm626abfMM8)

If you haven't already,
[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

## Add Firebase Authentication to your app

1.


   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the Firebase Authentication library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.


   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the Firebase Authentication library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth")
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
   }
   ```

   <br />

2. To use an authentication provider, you need to enable it in the
   [Firebase console](https://console.firebase.google.com/). Go to the Sign-in Method page in the Firebase Authentication
   section to enable Email/Password sign-in and any other identity providers
   you want for your app.

## (Optional) Prototype and test with Firebase Local Emulator Suite

Before talking about how your app authenticates users, let's introduce a set of
tools you can use to prototype and test Authentication functionality:
Firebase Local Emulator Suite. If you're deciding among authentication techniques
and providers, trying out different data models with public and private data
using Authentication and Firebase Security Rules, or prototyping sign-in UI designs, being able to
work locally without deploying live services can be a great idea.

An Authentication emulator is part of the Local Emulator Suite, which
enables your app to interact with emulated database content and config, as
well as optionally your emulated project resources (functions, other databases,
and security rules).

Using the Authentication emulator involves just a few steps:

1. Adding a line of code to your app's test config to connect to the emulator.
2. From the root of your local project directory, running `firebase emulators:start`.
3. Using the Local Emulator Suite UI for interactive prototyping, or the Authentication emulator REST API for non-interactive testing.

A detailed guide is available at [Connect your app to the Authentication emulator](https://firebase.google.com/docs/emulator-suite/connect_auth).
For more information, see the [Local Emulator Suite introduction](https://firebase.google.com/docs/emulator-suite).

Now let's continue with how to authenticate users.

## Check current auth state

1. Declare an instance of `FirebaseAuth`.

   ### Kotlin

   ```kotlin
   private lateinit var auth: FirebaseAuthhttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/EmailPasswordActivity.kt#L15-L15
   ```

   ### Java

   ```java
   private FirebaseAuth mAuth;
   ```
2. In the `onCreate()` method, initialize the `FirebaseAuth` instance.

   ### Kotlin

   ```kotlin
   // Initialize Firebase Auth
   auth = Firebase.authhttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/EmailPasswordActivity.kt#L22-L23
   ```

   ### Java

   ```java
   // Initialize Firebase Auth
   mAuth = FirebaseAuth.getInstance();
   ```
3. When initializing your Activity, check to see if the user is currently signed
   in.

   ### Kotlin

   ```kotlin
   public override fun onStart() {
       super.onStart()
       // Check if user is signed in (non-null) and update UI accordingly.
       val currentUser = auth.currentUser
       if (currentUser != null) {
           reload()
       }
   }
   ```

   ### Java

   ```java
   @Override
   public void onStart() {
       super.onStart();
       // Check if user is signed in (non-null) and update UI accordingly.
       FirebaseUser currentUser = mAuth.getCurrentUser();
       if(currentUser != null){
           reload();
       }
   }
   ```

## Sign up new users

Create a new `createAccount` method that takes in an email address and password,
validates them, and then creates a new user with the
[`createUserWithEmailAndPassword`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,%20java.lang.String))
method.

### Kotlin

```kotlin
auth.createUserWithEmailAndPassword(email, password)
    .addOnCompleteListener(this) { task ->
        if (task.isSuccessful) {
            // Sign in success, update UI with the signed-in user's information
            Log.d(TAG, "createUserWithEmail:success")
            val user = auth.currentUser
            updateUI(user)
        } else {
            // If sign in fails, display a message to the user.
            Log.w(TAG, "createUserWithEmail:failure", task.exception)
            Toast.makeText(
                baseContext,
                "Authentication failed.",
                Toast.LENGTH_SHORT,
            ).show()
            updateUI(null)
        }
    }
```

### Java

```java
mAuth.createUserWithEmailAndPassword(email, password)
        .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    // Sign in success, update UI with the signed-in user's information
                    Log.d(TAG, "createUserWithEmail:success");
                    FirebaseUser user = mAuth.getCurrentUser();
                    updateUI(user);
                } else {
                    // If sign in fails, display a message to the user.
                    Log.w(TAG, "createUserWithEmail:failure", task.getException());
                    Toast.makeText(EmailPasswordActivity.this, "Authentication failed.",
                            Toast.LENGTH_SHORT).show();
                    updateUI(null);
                }
            }
        });
```

Add a form to register new users with their email and password and call this new
method when it is submitted. You can see an example in our
[quickstart sample](https://github.com/firebase/quickstart-android/tree/master/auth/app/src/main).

## Sign in existing users

Create a new `signIn` method which takes in an email address and password,
validates them, and then signs a user in with the
[`signInWithEmailAndPassword`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,%20java.lang.String)) method.

### Kotlin

```kotlin
auth.signInWithEmailAndPassword(email, password)
    .addOnCompleteListener(this) { task ->
        if (task.isSuccessful) {
            // Sign in success, update UI with the signed-in user's information
            Log.d(TAG, "signInWithEmail:success")
            val user = auth.currentUser
            updateUI(user)
        } else {
            // If sign in fails, display a message to the user.
            Log.w(TAG, "signInWithEmail:failure", task.exception)
            Toast.makeText(
                baseContext,
                "Authentication failed.",
                Toast.LENGTH_SHORT,
            ).show()
            updateUI(null)
        }
    }
```

### Java

```java
mAuth.signInWithEmailAndPassword(email, password)
        .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    // Sign in success, update UI with the signed-in user's information
                    Log.d(TAG, "signInWithEmail:success");
                    FirebaseUser user = mAuth.getCurrentUser();
                    updateUI(user);
                } else {
                    // If sign in fails, display a message to the user.
                    Log.w(TAG, "signInWithEmail:failure", task.getException());
                    Toast.makeText(EmailPasswordActivity.this, "Authentication failed.",
                            Toast.LENGTH_SHORT).show();
                    updateUI(null);
                }
            }
        });
```

Add a form to sign in users with their email and password and call this new
method when it is submitted. You can see an example in our
[quickstart sample](https://github.com/firebase/quickstart-android/tree/master/auth/app/src/main).

## Access user information

If a user has signed in successfully you can get their account data at
any point with the `getCurrentUser` method.

### Kotlin

```kotlin
val user = Firebase.auth.currentUser
user?.let {
    // Name, email address, and profile photo Url
    val name = it.displayName
    val email = it.email
    val photoUrl = it.photoUrl

    // Check if user's email is verified
    val emailVerified = it.isEmailVerified

    // The user's ID, unique to the Firebase project. Do NOT use this value to
    // authenticate with your backend server, if you have one. Use
    // FirebaseUser.getIdToken() instead.
    val uid = it.uid
}
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
if (user != null) {
    // Name, email address, and profile photo Url
    String name = user.getDisplayName();
    String email = user.getEmail();
    Uri photoUrl = user.getPhotoUrl();

    // Check if user's email is verified
    boolean emailVerified = user.isEmailVerified();

    // The user's ID, unique to the Firebase project. Do NOT use this value to
    // authenticate with your backend server, if you have one. Use
    // FirebaseUser.getIdToken() instead.
    String uid = user.getUid();
}
```

## Next Steps

Explore the guides on adding other identity and authentication services:

- [Google Sign-in](https://firebase.google.com/docs/auth/android/google-signin)
- [Facebook Login](https://firebase.google.com/docs/auth/android/facebook-login)
- [Anonymous Authentication](https://firebase.google.com/docs/auth/android/anonymous-auth)