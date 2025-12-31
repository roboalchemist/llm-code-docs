# Source: https://firebase.google.com/docs/auth/unity/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/web/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/android/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/web/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/anonymous-auth.md.txt

# Source: https://firebase.google.com/docs/auth/android/anonymous-auth.md.txt

You can useFirebase Authenticationto create and use temporary anonymous accounts to authenticate with Firebase. These temporary anonymous accounts can be used to allow users who haven't yet signed up to your app to work with data protected by security rules. If an anonymous user decides to sign up to your app, you can[link their sign-in credentials to the anonymous account](https://firebase.google.com/docs/auth/android/account-linking)so that they can continue to work with their protected data in future sessions.

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theFirebase Authenticationlibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.  

   ```carbon
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Firebase Authentication library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth")
   }
   ```

   By using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)* Add Firebase library dependencies*without* using theBoM

   If you choose not to use theFirebase BoM, you must specify each Firebase library version in its dependency line.

   **Note that if you use*multiple* Firebase libraries in your app, we strongly recommend using theBoMto manage library versions, which ensures that all versions are compatible.**  

   ```groovy
   dependencies {
       // Add the dependency for the Firebase Authentication library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth:24.0.1")
   }
   ```
3. If you haven't yet connected your app to your Firebase project, do so from the[Firebaseconsole](https://console.firebase.google.com/).
4. Enable anonymous auth:
   1. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
   2. On the**Sign-in Methods** page, enable the**Anonymous**sign-in method.
   3. **Optional** : If you've upgraded your project to[Firebase Authenticationwith Identity Platform](https://firebase.google.com/auth#identity-platform), you can enable automatic clean-up. When you enable this setting, anonymous accounts older than 30 days will be automatically deleted. In projects with automatic clean-up enabled, anonymous authentication will no longer count toward usage limits or billing quotas. See[Automatic clean-up](https://firebase.google.com/docs/auth/android/anonymous-auth#auto-cleanup).

## Authenticate with Firebase anonymously

When a signed-out user uses an app feature that requires authentication with Firebase, sign in the user anonymously by completing the following steps:

1. In your activity's`onCreate`method, get the shared instance of the`FirebaseAuth`object:  

   ### Kotlin

   ```kotlin
   private lateinit var auth: FirebaseAuth
   // ...
   // Initialize Firebase Auth
   auth = Firebase.auth  
   https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/AnonymousAuthActivity.kt#L25-L26
   ```

   ### Java

   ```java
   private FirebaseAuth mAuth;
   // ...
   // Initialize Firebase Auth
   mAuth = FirebaseAuth.getInstance();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/AnonymousAuthActivity.java#L49-L50
   ```
2. When initializing your Activity, check to see if the user is currently signed in:  

   ### Kotlin

   ```kotlin
   public override fun onStart() {
       super.onStart()
       // Check if user is signed in (non-null) and update UI accordingly.
       val currentUser = auth.currentUser
       updateUI(currentUser)
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/AnonymousAuthActivity.kt#L31-L36
   ```

   ### Java

   ```java
   @Override
   public void onStart() {
       super.onStart();
       // Check if user is signed in (non-null) and update UI accordingly.
       FirebaseUser currentUser = mAuth.getCurrentUser();
       updateUI(currentUser);
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/AnonymousAuthActivity.java#L55-L61
   ```
3. Finally, call`signInAnonymously`to sign in as an anonymous user:  

   ### Kotlin

   ```kotlin
   auth.signInAnonymously()
       .addOnCompleteListener(this) { task ->
           if (task.isSuccessful) {
               // Sign in success, update UI with the signed-in user's information
               Log.d(TAG, "signInAnonymously:success")
               val user = auth.currentUser
               updateUI(user)
           } else {
               // If sign in fails, display a message to the user.
               Log.w(TAG, "signInAnonymously:failure", task.exception)
               Toast.makeText(
                   baseContext,
                   "Authentication failed.",
                   Toast.LENGTH_SHORT,
               ).show()
               updateUI(null)
           }
       }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/AnonymousAuthActivity.kt#L41-L58
   ```

   ### Java

   ```java
   mAuth.signInAnonymously()
           .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
               @Override
               public void onComplete(@NonNull Task<AuthResult> task) {
                   if (task.isSuccessful()) {
                       // Sign in success, update UI with the signed-in user's information
                       Log.d(TAG, "signInAnonymously:success");
                       FirebaseUser user = mAuth.getCurrentUser();
                       updateUI(user);
                   } else {
                       // If sign in fails, display a message to the user.
                       Log.w(TAG, "signInAnonymously:failure", task.getException());
                       Toast.makeText(AnonymousAuthActivity.this, "Authentication failed.",
                               Toast.LENGTH_SHORT).show();
                       updateUI(null);
                   }
               }
           });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/AnonymousAuthActivity.java#L66-L83
   ```
   If sign-in succeeds you can use the`getCurrentUser`method to get the user's account data.

| To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the[Firebaseconsole](https://console.firebase.google.com/project/_/authentication/providers).

## Convert an anonymous account to a permanent account

When an anonymous user signs up to your app, you might want to allow them to continue their work with their new account---for example, you might want to make the items the user added to their shopping cart before they signed up available in their new account's shopping cart. To do so, complete the following steps:

1. When the user signs up, complete the sign-in flow for the user's authentication provider up to, but not including, calling one of the`FirebaseAuth.signInWith`methods. For example, get the user's Google ID token, Facebook access token, or email address and password.
2. Get an`AuthCredential`for the new authentication provider:

   ##### Google Sign-In

   ### Kotlin

   ```kotlin
   val credential = GoogleAuthProvider.getCredential(googleIdToken, null)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L394-L394
   ```

   ### Java

   ```java
   AuthCredential credential = GoogleAuthProvider.getCredential(googleIdToken, null);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L479-L479
   ```

   ##### Facebook Login

   ### Kotlin

   ```kotlin
   val credential = FacebookAuthProvider.getCredential(token.token)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L401-L401
   ```

   ### Java

   ```java
   AuthCredential credential = FacebookAuthProvider.getCredential(token.getToken());https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L487-L487
   ```

   ##### Email-password sign-in

   ### Kotlin

   ```kotlin
   val credential = EmailAuthProvider.getCredential(email, password)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L409-L409
   ```

   ### Java

   ```java
   AuthCredential credential = EmailAuthProvider.getCredential(email, password);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L495-L495
   ```
3. Pass the`AuthCredential`object to the sign-in user's`linkWithCredential`method:

   ### Kotlin

   ```kotlin
   auth.currentUser!!.linkWithCredential(credential)
       .addOnCompleteListener(this) { task ->
           if (task.isSuccessful) {
               Log.d(TAG, "linkWithCredential:success")
               val user = task.result?.user
               updateUI(user)
           } else {
               Log.w(TAG, "linkWithCredential:failure", task.exception)
               Toast.makeText(
                   baseContext,
                   "Authentication failed.",
                   Toast.LENGTH_SHORT,
               ).show()
               updateUI(null)
           }
       }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/AnonymousAuthActivity.kt#L66-L81
   ```

   ### Java

   ```java
   mAuth.getCurrentUser().linkWithCredential(credential)
           .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
               @Override
               public void onComplete(@NonNull Task<AuthResult> task) {
                   if (task.isSuccessful()) {
                       Log.d(TAG, "linkWithCredential:success");
                       FirebaseUser user = task.getResult().getUser();
                       updateUI(user);
                   } else {
                       Log.w(TAG, "linkWithCredential:failure", task.getException());
                       Toast.makeText(AnonymousAuthActivity.this, "Authentication failed.",
                               Toast.LENGTH_SHORT).show();
                       updateUI(null);
                   }
               }
           });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/AnonymousAuthActivity.java#L91-L106
   ```

If the call to`linkWithCredential`succeeds, the user's new account can access the anonymous account's Firebase data.
| This technique can also be used to[link any two accounts](https://firebase.google.com/docs/auth/android/account-linking).

## Automatic clean-up

If you've upgraded your project to[Firebase Authenticationwith Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can enable automatic clean-up in theFirebaseconsole. When you enable this feature you allow Firebase to automatically delete anonymous accounts older than 30 days. In projects with automatic clean-up enabled, anonymous authentication will not count toward usage limits or billing quotas.

- Any anonymous accounts created after enabling automatic clean-up might be automatically deleted any time after 30 days post-creation.
- Existing anonymous accounts will be eligible for automatic deletion 30 days after enabling automatic clean-up.
- If you turn automatic clean-up off, any anonymous accounts scheduled to be deleted will remain scheduled to be deleted.
- If you "upgrade" an anonymous account by linking it to any sign-in method, the account will not get automatically deleted.

If you want to see how many users will be affected before you enable this feature, and you've upgraded your project to[Firebase Authenticationwith Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can filter by`is_anon`in[Cloud Logging](https://cloud.google.com/logging/docs).

## Next steps

Now that users can authenticate with Firebase, you can control their access to data in your Firebase database using[Firebase rules](https://firebase.google.com/docs/database/security#section-authorization).