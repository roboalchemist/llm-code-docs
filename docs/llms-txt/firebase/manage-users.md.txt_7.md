# Source: https://firebase.google.com/docs/auth/android/manage-users.md.txt

## Create a user

You create a new user in your Firebase project by calling the
[`createUserWithEmailAndPassword`](https://firebase.google.com/docs/auth/android/password-auth#create_a_password-based_account)
method or by signing in a user for the first time using a federated identity
provider, such as [Google Sign-In](https://firebase.google.com/docs/auth/android/google-signin) or
[Facebook Login](https://firebase.google.com/docs/auth/android/facebook-login).

You can also create new password-authenticated users from the Authentication
section of the [Firebase console](https://console.firebase.google.com/), on the Users page.

## Get the currently signed-in user

The recommended way to get the current user is by calling the `getCurrentUser` method.
If no user is signed in, `getCurrentUser` returns null:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser
if (user != null) {
    // User is signed in
} else {
    // No user is signed in
}
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
if (user != null) {
    // User is signed in
} else {
    // No user is signed in
}
```

There are some cases where `getCurrentUser` will return a non-null `FirebaseUser`
but the underlying token is not valid. This can happen, for example, if the user
was deleted on another device and the local token has not refreshed. In this case,
you may get a valid user `getCurrentUser` but subsequent calls to authenticated
resources will fail.

`getCurrentUser` might also return `null` because the auth object has not
finished initializing.

If you attach an [AuthStateListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener)
you will get a callback every time the underlying token state changes. This can
be useful to react to edge cases like those mentioned above.

## Get a user's profile

To get a user's profile information, use the accessor methods of an instance of
`FirebaseUser`. For example:

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

## Get a user's provider-specific profile information

To get the profile information retrieved from the sign-in providers linked to a
user, use the `getProviderData` method. For example:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser
user?.let {
    for (profile in it.providerData) {
        // Id of the provider (ex: google.com)
        val providerId = profile.providerId

        // UID specific to the provider
        val uid = profile.uid

        // Name, email address, and profile photo Url
        val name = profile.displayName
        val email = profile.email
        val photoUrl = profile.photoUrl
    }
}
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
if (user != null) {
    for (UserInfo profile : user.getProviderData()) {
        // Id of the provider (ex: google.com)
        String providerId = profile.getProviderId();

        // UID specific to the provider
        String uid = profile.getUid();

        // Name, email address, and profile photo Url
        String name = profile.getDisplayName();
        String email = profile.getEmail();
        Uri photoUrl = profile.getPhotoUrl();
    }
}
```

## Update a user's profile

You can update a user's basic profile information---the user's display name
and profile photo URL---with the `updateProfile` method. For example:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser

val profileUpdates = userProfileChangeRequest {
    displayName = "Jane Q. User"
    photoUri = Uri.parse("https://example.com/jane-q-user/profile.jpg")
}

user!!.updateProfile(profileUpdates)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "User profile updated.")
        }
    }
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();

UserProfileChangeRequest profileUpdates = new UserProfileChangeRequest.Builder()
        .setDisplayName("Jane Q. User")
        .setPhotoUri(Uri.parse("https://example.com/jane-q-user/profile.jpg"))
        .build();

user.updateProfile(profileUpdates)
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "User profile updated.");
                }
            }
        });
```

## Set a user's email address

You can set a user's email address with the `updateEmail` method. For example:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser

user!!.updateEmail("user@example.com")
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "User email address updated.")
        }
    }
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();

user.updateEmail("user@example.com")
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "User email address updated.");
                }
            }
        });
```

> [!IMPORTANT]
> **Important:** To set a user's email address, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/android/manage-users#re-authenticate_a_user).

## Send a user a verification email

You can send an address verification email to a user with the
`sendEmailVerification` method. For example:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser

user!!.sendEmailVerification()
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "Email sent.")
        }
    }
```

### Java

```java
FirebaseAuth auth = FirebaseAuth.getInstance();
FirebaseUser user = auth.getCurrentUser();

user.sendEmailVerification()
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "Email sent.");
                }
            }
        });
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

It is also possible to pass state via a
[continue URL](https://firebase.google.com/docs/auth/android/passing-state-in-email-actions) to redirect back
to the app when sending a verification email.

Additionally you can localize the verification email by updating the language
code on the Auth instance before sending the email. For example:

### Kotlin

```kotlin
auth.setLanguageCode("fr")
// To apply the default app language instead of explicitly setting it.
// auth.useAppLanguage()https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L173-L175
```

### Java

```java
auth.setLanguageCode("fr");
// To apply the default app language instead of explicitly setting it.
// auth.useAppLanguage();https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L211-L213
```

## Set a user's password

You can set a user's password with the `updatePassword` method. For example:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser
val newPassword = "SOME-SECURE-PASSWORD"

user!!.updatePassword(newPassword)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "User password updated.")
        }
    }
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
String newPassword = "SOME-SECURE-PASSWORD";

user.updatePassword(newPassword)
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "User password updated.");
                }
            }
        });
```

> [!IMPORTANT]
> **Important:** To set a user's password, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/android/manage-users#re-authenticate_a_user).

## Send a password reset email

You can send a password reset email to a user with the `sendPasswordResetEmail`
method. For example:

### Kotlin

```kotlin
val emailAddress = "user@example.com"

Firebase.auth.sendPasswordResetEmail(emailAddress)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "Email sent.")
        }
    }
```

### Java

```java
FirebaseAuth auth = FirebaseAuth.getInstance();
String emailAddress = "user@example.com";

auth.sendPasswordResetEmail(emailAddress)
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "Email sent.");
                }
            }
        });
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

It is also possible to pass state via a
[continue URL](https://firebase.google.com/docs/auth/android/passing-state-in-email-actions) to redirect back
to the app when sending a password reset email.

Additionally you can localize the password reset email by updating the language
code on the Auth instance before sending the email. For example:

### Kotlin

```kotlin
auth.setLanguageCode("fr")
// To apply the default app language instead of explicitly setting it.
// auth.useAppLanguage()https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L173-L175
```

### Java

```java
auth.setLanguageCode("fr");
// To apply the default app language instead of explicitly setting it.
// auth.useAppLanguage();https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L211-L213
```

You can also send password reset emails from the Firebase console.

## Delete a user

You can delete a user account with the `delete` method. For example:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser!!

user.delete()
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "User account deleted.")
        }
    }
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();

user.delete()
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "User account deleted.");
                }
            }
        });
```

> [!IMPORTANT]
> **Important:** To delete a user, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/android/manage-users#re-authenticate_a_user).

You can also delete users from the Authentication section of the
[Firebase console](https://console.firebase.google.com/), on the Users page.

## Re-authenticate a user

Some security-sensitive actions---such as
[deleting an account](https://firebase.google.com/docs/auth/android/manage-users#delete_a_user),
[setting a primary email address](https://firebase.google.com/docs/auth/android/manage-users#set_a_users_email_address), and
[changing a password](https://firebase.google.com/docs/auth/android/manage-users#set_a_users_password)---require that the user has
recently signed in. If you perform one of these actions, and the user signed in
too long ago, the action fails and throws [`FirebaseAuthRecentLoginRequiredException`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException).
When this happens, re-authenticate the user by getting new sign-in credentials
from the user and passing the credentials to `reauthenticate`. For example:

### Kotlin

```kotlin
val user = Firebase.auth.currentUser!!

// Get auth credentials from the user for re-authentication. The example below shows
// email and password credentials but there are multiple possible providers,
// such as GoogleAuthProvider or FacebookAuthProvider.
val credential = EmailAuthProvider
    .getCredential("user@example.com", "password1234")

// Prompt the user to re-provide their sign-in credentials
user.reauthenticate(credential)
    .addOnCompleteListener { Log.d(TAG, "User re-authenticated.") }
```

### Java

```java
FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();

// Get auth credentials from the user for re-authentication. The example below shows
// email and password credentials but there are multiple possible providers,
// such as GoogleAuthProvider or FacebookAuthProvider.
AuthCredential credential = EmailAuthProvider
        .getCredential("user@example.com", "password1234");

// Prompt the user to re-provide their sign-in credentials
user.reauthenticate(credential)
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                Log.d(TAG, "User re-authenticated.");
            }
        });
```

## Import user accounts

You can import user accounts from a file into your Firebase project by using the
Firebase CLI's [`auth:import`](https://firebase.google.com/docs/cli/auth-import) command. For example:

    firebase auth:import users.json --hash-algo=scrypt --rounds=8 --mem-cost=14