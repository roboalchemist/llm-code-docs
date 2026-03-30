# Source: https://firebase.google.com/docs/auth/flutter/manage-users.md.txt

# Manage Users in Firebase

<br />

## Create a user

You create a new user in your Firebase project in four ways:

- Call the `createUserWithEmailAndPassword()` method.
- Sign in a user for the first time using a [federated identity provider](https://firebase.google.com/docs/auth/flutter/federated-auth), such as Google Sign-In, Facebook Login, or Apple.

You can also create new password-authenticated users from the Authentication
section of the [Firebase console](https://console.firebase.google.com/), on the Users page.

## Get a user's profile

To get a user's profile information, use the properties of `User`. There are
three ways to get a `User` object representing the current user:

- The `authStateChanges`, `idTokenChanges` and `userChanges` streams: your
  listeners will receive the current `User`, or `null` if no user is
  authenticated:

      FirebaseAuth.instance
        .authStateChanges()
        .listen((User? user) {
          if (user != null) {
            print(user.uid);
          }
        });

  When the app starts, an event fires after the user credentials (if any) from
  local storage have been restored, meaning that your listeners always get
  called when the user state is initialized. Then, whenever the authentication
  state changes, a new event will be raised with the updated user state.

  By listening to the authentication state, you can build a user interface that
  reacts to these changes in authentication state.
  Do not place `authStateChanges().listen(...)` directly inside a widget's build
  method, as it will create a new subscription on every rebuild. If you need to
  update the UI in response to auth state, use a `StreamBuilder`:

      StreamBuilder<User?>(
      stream: FirebaseAuth.instance.authStateChanges(),
      builder: (BuildContext context, AsyncSnapshot<User?> snapshot) {
        if (snapshot.hasError) {
          return const Text('Something went wrong');
        }

        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Text("Loading...");
        }

        if (!snapshot.hasData) {
          return const SignInScreen();
        }

        final user = snapshot.data!;
        return HomeScreen(userId: user.uid);
      },
      )

  This approach ensures the widget tree rebuilds automatically when the user's
  authentication state changes.
- The `UserCredential` object returned by the authentication (`signIn`-)
  methods: the `UserCredential` object has a `user` property with the current
  `User`:

      final userCredential =
          await FirebaseAuth.instance.signInWithCredential(credential);
      final user = userCredential.user;
      print(user?.uid);

- The `currentUser` property of the `FirebaseAuth` instance: if you are sure the
  user is currently signed-in, you can access the `User` from the `currentUser`
  property:

      if (FirebaseAuth.instance.currentUser != null) {
        print(FirebaseAuth.instance.currentUser?.uid);
      }

  The `currentUser` can be `null` for two reasons:
  - The user isn't signed in.
  - The auth object has not finished initializing. If you use a listener to keep track of the user's sign-in status, you don't need to handle this case.

## Get a user's provider-specific profile information

To get the profile information retrieved from the sign-in providers linked to a
user, use the `providerData` property. For example:

    if (user != null) {
        for (final providerProfile in user.providerData) {
            // ID of the provider (google.com, apple.com, etc.)
            final provider = providerProfile.providerId;

            // UID specific to the provider
            final uid = providerProfile.uid;

            // Name, email address, and profile photo URL
            final name = providerProfile.displayName;
            final emailAddress = providerProfile.email;
            final profilePhoto = providerProfile.photoURL;
        }
    }

## Update a user's profile

You can update a user's basic profile information---the user's display name
and profile photo URL---with the `update`- methods. For example:

    await user?.updateDisplayName("Jane Q. User");
    await user?.updatePhotoURL("https://example.com/jane-q-user/profile.jpg");

## Set a user's email address

You can set a user's email address with the `updateEmail()` method. For example:

    await user?.updateEmail("janeq@example.com");

> [!NOTE]
> **Note:** To set a user's email address, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/flutter/manage-users#re-authenticate_a_user).

## Send a user a verification email

You can send an address verification email to a user with the
`sendEmailVerification()` method. For example:

    await user?.sendEmailVerification();

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

It is also possible to pass state via a
[continue URL](https://firebase.google.com/docs/auth/flutter/passing-state-in-email-actions) to redirect back
to the app when sending a verification email.

Additionally you can localize the verification email by updating the language
code on the Auth instance before sending the email. For example:

    await FirebaseAuth.instance.setLanguageCode("fr");
    await user?.sendEmailVerification();

## Set a user's password

You can set a user's password with the `updatePassword()` method. For example:

    await user?.updatePassword(newPassword);

> [!IMPORTANT]
> **Important:** To set a user's email address, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/flutter/manage-users#re-authenticate_a_user).

## Send a password reset email

You can send a password reset email to a user with the `sendPasswordResetEmail()`
method. For example:

    await FirebaseAuth.instance
        .sendPasswordResetEmail(email: "user@example.com");

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

It is also possible to pass state via a
[continue URL](https://firebase.google.com/docs/auth/android/passing-state-in-email-actions) to redirect back
to the app when sending a password reset email.

Additionally you can localize the password reset email by updating the language
code on the Auth instance before sending the email. For example:

    await FirebaseAuth.instance.setLanguageCode("fr");

You can also send password reset emails from the Firebase console.

## Delete a user

You can delete a user account with the `delete()` method. For example:

    await user?.delete();

> [!IMPORTANT]
> **Important:** To set a user's email address, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/flutter/manage-users#re-authenticate_a_user).

You can also delete users from the Authentication section of the
[Firebase console](https://console.firebase.google.com/), on the Users page.

## Re-authenticate a user

Some security-sensitive actions---such as
[deleting an account](https://firebase.google.com/docs/auth/flutter/manage-users#delete_a_user),
[setting a primary email address](https://firebase.google.com/docs/auth/flutter/manage-users#set_a_users_email_address), and
[changing a password](https://firebase.google.com/docs/auth/flutter/manage-users#set_a_users_password)---require that the user has
recently signed in. If you perform one of these actions, and the user signed in
too long ago, the action fails and throws a `FirebaseAuthException` with the code
`requires-recent-login`.
When this happens, re-authenticate the user by getting new sign-in credentials
from the user and passing the credentials to `reauthenticate`. For example:

    // Prompt the user to re-provide their sign-in credentials.
    // Then, use the credentials to reauthenticate:
    await user?.reauthenticateWithCredential(credential);

## Import user accounts

You can import user accounts from a file into your Firebase project by using the
Firebase CLI's [`auth:import`](https://firebase.google.com/docs/cli/auth-import) command. For example:

    firebase auth:import users.json --hash-algo=scrypt --rounds=8 --mem-cost=14