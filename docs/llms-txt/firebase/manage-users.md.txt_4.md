# Source: https://firebase.google.com/docs/auth/web/manage-users.md.txt

## Create a user

You create a new user in your Firebase project by calling the
[`createUserWithEmailAndPassword`](https://firebase.google.com/docs/auth/web/password-auth#create_a_password-based_account)
method or by signing in a user for the first time using a federated identity
provider, such as [Google Sign-In](https://firebase.google.com/docs/auth/web/google-signin) or
[Facebook Login](https://firebase.google.com/docs/auth/web/facebook-login).

You can also create new password-authenticated users from the Authentication
section of the [Firebase console](https://console.firebase.google.com/), on the Users page, or by using the
[Admin SDK](https://firebase.google.com/docs/auth/admin/manage-users#create_a_user).

## Get the currently signed-in user

The recommended way to get the current user is by setting an observer on the
Auth object:

### Web

```javascript
import { getAuth, onAuthStateChanged } from "firebase/auth";

const auth = getAuth();
onAuthStateChanged(auth, (user) => {
  if (user) {
    // User is signed in, see docs for a list of available properties
    // https://firebase.google.com/docs/reference/js/auth.user
    const uid = user.uid;
    // ...
  } else {
    // User is signed out
    // ...
  }
});
```

### Web

```javascript
firebase.auth().onAuthStateChanged((user) => {
  if (user) {
    // User is signed in, see docs for a list of available properties
    // https://firebase.google.com/docs/reference/js/v8/firebase.User
    var uid = user.uid;
    // ...
  } else {
    // User is signed out
    // ...
  }
});
```

By using an observer, you ensure that the Auth object isn't in an intermediate
state---such as initialization---when you get the current user. When you
use `signInWithRedirect`, the `onAuthStateChanged` observer waits until
`getRedirectResult` resolves before triggering.

You can also get the currently signed-in user by using the `currentUser`
property. If a user isn't signed in, `currentUser` is null:

### Web

```javascript
import { getAuth } from "firebase/auth";

const auth = getAuth();
const user = auth.currentUser;

if (user) {
  // User is signed in, see docs for a list of available properties
  // https://firebase.google.com/docs/reference/js/auth.user
  // ...
} else {
  // No user is signed in.
}
```

### Web

```javascript
const user = firebase.auth().currentUser;

if (user) {
  // User is signed in, see docs for a list of available properties
  // https://firebase.google.com/docs/reference/js/v8/firebase.User
  // ...
} else {
  // No user is signed in.
}
```

> [!NOTE]
> **Note:** `currentUser` might also be null because the auth object has not finished initializing. If you use an observer to keep track of the user's sign-in status, you don't need to handle this case.

## Get a user's profile

To get a user's profile information, use the properties of an instance of
`User`. For example:

### Web

```javascript
import { getAuth } from "firebase/auth";

const auth = getAuth();
const user = auth.currentUser;
if (user !== null) {
  // The user object has basic properties such as display name, email, etc.
  const displayName = user.displayName;
  const email = user.email;
  const photoURL = user.photoURL;
  const emailVerified = user.emailVerified;

  // The user's ID, unique to the Firebase project. Do NOT use
  // this value to authenticate with your backend server, if
  // you have one. Use User.getToken() instead.
  const uid = user.uid;
}
```

### Web

```javascript
const user = firebase.auth().currentUser;
if (user !== null) {
  // The user object has basic properties such as display name, email, etc.
  const displayName = user.displayName;
  const email = user.email;
  const photoURL = user.photoURL;
  const emailVerified = user.emailVerified;

  // The user's ID, unique to the Firebase project. Do NOT use
  // this value to authenticate with your backend server, if
  // you have one. Use User.getIdToken() instead.
  const uid = user.uid;
}
```

> [!IMPORTANT]
> **Important:** Be careful when setting (and later displaying) potentially user-facing UI values like `displayName` and `photoURL`. The API does not filter the values to prevent potential XSS-type attacks.

## Get a user's provider-specific profile information

To get the profile information retrieved from the sign-in providers linked to a
user, use the `providerData` property. For example:

### Web

```javascript
import { getAuth } from "firebase/auth";

const auth = getAuth();
const user = auth.currentUser;

if (user !== null) {
  user.providerData.forEach((profile) => {
    console.log("Sign-in provider: " + profile.providerId);
    console.log("  Provider-specific UID: " + profile.uid);
    console.log("  Name: " + profile.displayName);
    console.log("  Email: " + profile.email);
    console.log("  Photo URL: " + profile.photoURL);
  });
}
```

### Web

```javascript
const user = firebase.auth().currentUser;

if (user !== null) {
  user.providerData.forEach((profile) => {
    console.log("Sign-in provider: " + profile.providerId);
    console.log("  Provider-specific UID: " + profile.uid);
    console.log("  Name: " + profile.displayName);
    console.log("  Email: " + profile.email);
    console.log("  Photo URL: " + profile.photoURL);
  });
}
```

## Update a user's profile

You can update a user's basic profile information---the user's display name
and profile photo URL---with the `updateProfile` method. For example:

### Web

```javascript
import { getAuth, updateProfile } from "firebase/auth";
const auth = getAuth();
updateProfile(auth.currentUser, {
  displayName: "Jane Q. User", photoURL: "https://example.com/jane-q-user/profile.jpg"
}).then(() => {
  // Profile updated!
  // ...
}).catch((error) => {
  // An error occurred
  // ...
});
```

### Web

```javascript
const user = firebase.auth().currentUser;

user.updateProfile({
  displayName: "Jane Q. User",
  photoURL: "https://example.com/jane-q-user/profile.jpg"
}).then(() => {
  // Update successful
  // ...
}).catch((error) => {
  // An error occurred
  // ...
});  
```

## Set a user's email address

You can set a user's email address with the `updateEmail` method. For example:

### Web

```javascript
import { getAuth, updateEmail } from "firebase/auth";
const auth = getAuth();
updateEmail(auth.currentUser, "user@example.com").then(() => {
  // Email updated!
  // ...
}).catch((error) => {
  // An error occurred
  // ...
});
```

### Web

```javascript
const user = firebase.auth().currentUser;

user.updateEmail("user@example.com").then(() => {
  // Update successful
  // ...
}).catch((error) => {
  // An error occurred
  // ...
});
```

> [!IMPORTANT]
> **Important:** To set a user's email address, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/web/manage-users#re-authenticate_a_user).

## Send a user a verification email

You can send an address verification email to a user with the
`sendEmailVerification` method. For example:

### Web

```javascript
import { getAuth, sendEmailVerification } from "firebase/auth";

const auth = getAuth();
sendEmailVerification(auth.currentUser)
  .then(() => {
    // Email verification sent!
    // ...
  });
```

### Web

```javascript
firebase.auth().currentUser.sendEmailVerification()
  .then(() => {
    // Email verification sent!
    // ...
  });
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

It is also possible to pass state via a
[continue URL](https://firebase.google.com/docs/auth/web/passing-state-in-email-actions) to redirect back
to the app when sending a verification email.

Additionally you can localize the verification email by updating the language
code on the Auth instance before sending the email. For example:

### Web

```javascript
import { getAuth } from "firebase/auth";

const auth = getAuth();
auth.languageCode = 'it';
// To apply the default browser preference instead of explicitly setting it.
// auth.useDeviceLanguage();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/index/auth_set_language_code.js#L8-L13
```

### Web

```javascript
firebase.auth().languageCode = 'it';
// To apply the default browser preference instead of explicitly setting it.
// firebase.auth().useDeviceLanguage();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/index.js#L73-L75
```

## Set a user's password

You can set a user's password with the `updatePassword` method. For example:

### Web

```javascript
import { getAuth, updatePassword } from "firebase/auth";

const auth = getAuth();

const user = auth.currentUser;
const newPassword = getASecureRandomPassword();

updatePassword(user, newPassword).then(() => {
  // Update successful.
}).catch((error) => {
  // An error ocurred
  // ...
});
```

### Web

```javascript
const user = firebase.auth().currentUser;
const newPassword = getASecureRandomPassword();

user.updatePassword(newPassword).then(() => {
  // Update successful.
}).catch((error) => {
  // An error ocurred
  // ...
});
```

> [!IMPORTANT]
> **Important:** To set a user's password, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/web/manage-users#re-authenticate_a_user).

## Send a password reset email

You can send a password reset email to a user with the `sendPasswordResetEmail`
method. For example:

### Web

```javascript
import { getAuth, sendPasswordResetEmail } from "firebase/auth";

const auth = getAuth();
sendPasswordResetEmail(auth, email)
  .then(() => {
    // Password reset email sent!
    // ..
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    // ..
  });
```

### Web

```javascript
firebase.auth().sendPasswordResetEmail(email)
  .then(() => {
    // Password reset email sent!
    // ..
  })
  .catch((error) => {
    var errorCode = error.code;
    var errorMessage = error.message;
    // ..
  });
```

You can customize the email template that is used in Authentication section of
the [Firebase console](https://console.firebase.google.com/), on the Email Templates page.
See [Email Templates](https://support.google.com/firebase/answer/7000714) in
Firebase Help Center.

It is also possible to pass state via a
[continue URL](https://firebase.google.com/docs/auth/web/passing-state-in-email-actions) to redirect back
to the app when sending a password reset email.

Additionally you can localize the password reset email by updating the language
code on the Auth instance before sending the email. For example:

### Web

```javascript
import { getAuth } from "firebase/auth";

const auth = getAuth();
auth.languageCode = 'it';
// To apply the default browser preference instead of explicitly setting it.
// auth.useDeviceLanguage();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/index/auth_set_language_code.js#L8-L13
```

### Web

```javascript
firebase.auth().languageCode = 'it';
// To apply the default browser preference instead of explicitly setting it.
// firebase.auth().useDeviceLanguage();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/index.js#L73-L75
```

You can also send password reset emails from the Firebase console.

## Delete a user

You can delete a user account with the `delete` method. For example:

### Web

```javascript
import { getAuth, deleteUser } from "firebase/auth";

const auth = getAuth();
const user = auth.currentUser;

deleteUser(user).then(() => {
  // User deleted.
}).catch((error) => {
  // An error ocurred
  // ...
});
```

### Web

```javascript
const user = firebase.auth().currentUser;

user.delete().then(() => {
  // User deleted.
}).catch((error) => {
  // An error ocurred
  // ...
});
```

> [!IMPORTANT]
> **Important:** To delete a user, the user must have signed in recently. See [Re-authenticate a user](https://firebase.google.com/docs/auth/web/manage-users#re-authenticate_a_user).

You can also delete users from the Authentication section of the
[Firebase console](https://console.firebase.google.com/), on the Users page.

## Re-authenticate a user

Some security-sensitive actions---such as
[deleting an account](https://firebase.google.com/docs/auth/web/manage-users#delete_a_user),
[setting a primary email address](https://firebase.google.com/docs/auth/web/manage-users#set_a_users_email_address), and
[changing a password](https://firebase.google.com/docs/auth/web/manage-users#set_a_users_password)---require that the user has
recently signed in. If you perform one of these actions, and the user signed in
too long ago, the action fails with an error.
When this happens, re-authenticate the user by getting new sign-in credentials
from the user and passing the credentials to `reauthenticateWithCredential`.
For example:

### Web

```javascript
import { getAuth, reauthenticateWithCredential } from "firebase/auth";

const auth = getAuth();
const user = auth.currentUser;

// TODO(you): prompt the user to re-provide their sign-in credentials
const credential = promptForCredentials();

reauthenticateWithCredential(user, credential).then(() => {
  // User re-authenticated.
}).catch((error) => {
  // An error ocurred
  // ...
});
```

### Web

```javascript
const user = firebase.auth().currentUser;

// TODO(you): prompt the user to re-provide their sign-in credentials
const credential = promptForCredentials();

user.reauthenticateWithCredential(credential).then(() => {
  // User re-authenticated.
}).catch((error) => {
  // An error occurred
  // ...
});
```

## Import user accounts

You can import user accounts from a file into your Firebase project by using the
Firebase CLI's [`auth:import`](https://firebase.google.com/docs/cli/auth-import) command. For example:

    firebase auth:import users.json --hash-algo=scrypt --rounds=8 --mem-cost=14