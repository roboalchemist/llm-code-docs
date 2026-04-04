# Source: https://firebase.google.com/docs/auth/android/password-auth.md.txt

You can use Firebase Authentication to let your users authenticate with
Firebase using their email addresses and passwords, and to manage your app's
password-based accounts.

## Before you begin

1. If you haven't already,
   [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. If you haven't yet connected your app to your Firebase project, do so from the [Firebase console](https://console.firebase.google.com/).
3. Enable Email/Password sign-in:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
   2. On the **Sign in method** tab, enable the **Email/password** sign-in method and click **Save**.
4.


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

## Create a password-based account

To create a new user account with a password, complete the following steps in
your app's sign-in activity:

1. In your sign-up activity's `onCreate` method, get the shared instance of the `FirebaseAuth` object:

   ### Kotlin

   ```kotlin
   private lateinit var auth: FirebaseAuth
   // ...
   // Initialize Firebase Auth
   auth = Firebase.authhttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/EmailPasswordActivity.kt#L22-L23
   ```

   ### Java

   ```java
   private FirebaseAuth mAuth;
   // ...
   // Initialize Firebase Auth
   mAuth = FirebaseAuth.getInstance();
   ```
2. When initializing your Activity, check to see if the user is currently signed in:

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
3. When a new user signs up using your app's sign-up form, complete any new account validation steps that your app requires, such as verifying that the new account's password was correctly typed and meets your complexity requirements.
4. Create a new account by passing the new user's email address and password to `createUserWithEmailAndPassword`:

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
   If the new account was created, the user is also signed in. In the callback, you can use the `getCurrentUser` method to get the user's account data.

To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the [Firebase console](https://console.firebase.google.com/project/_/authentication/providers).

## Sign in a user with an email address and password

The steps for signing in a user with a password are similar to the steps for
creating a new account. In your app's sign-in activity, do the following:

1. In your sign-in activity's `onCreate` method, get the shared instance of the `FirebaseAuth` object:

   ### Kotlin

   ```kotlin
   private lateinit var auth: FirebaseAuth
   // ...
   // Initialize Firebase Auth
   auth = Firebase.authhttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/EmailPasswordActivity.kt#L22-L23
   ```

   ### Java

   ```java
   private FirebaseAuth mAuth;
   // ...
   // Initialize Firebase Auth
   mAuth = FirebaseAuth.getInstance();
   ```
2. When initializing your Activity, check to see if the user is currently signed in:

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
3. When a user signs in to your app, pass the user's email address and password to `signInWithEmailAndPassword`:

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
   If sign-in succeeded, you can use the returned `FirebaseUser` to proceed.

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

## Next steps

After a user signs in for the first time, a new user account is created and
linked to the credentials---that is, the user name and password, phone
number, or auth provider information---the user signed in with. This new
account is stored as part of your Firebase project, and can be used to identify
a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the
  [`FirebaseUser`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser) object. See [Manage Users](https://firebase.google.com/docs/auth/android/manage-users).

- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/android/account-linking)

To sign out a user, call [`signOut`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signOut()):

### Kotlin

```kotlin
Firebase.auth.signOut()
```

### Java

```java
FirebaseAuth.getInstance().signOut();
```