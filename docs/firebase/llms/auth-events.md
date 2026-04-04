# Source: https://firebase.google.com/docs/functions/1st-gen/auth-events.md.txt

<br />

You can trigger functions in response to the creation and deletion ofFirebaseuser accounts. For example, you could send a welcome email to a user who has just created an account in your app. Examples on this page are based on a sample that does exactly this---sends welcome and farewell emails upon account creation and deletion.

For more examples of use cases, see[What can I do withCloud Functions?](https://firebase.google.com/docs/functions/use-cases).
| **Note:** Cloud Functions for Firebase(2nd gen) does not provide support for the events and triggers described in this guide. Because 1st gen and 2nd gen functions can coexist side-by-side in the same source file, you can still develop and deploy this functionality together with 2nd gen functions.

## Trigger a function on user creation

You can create a function that triggers when aFirebaseuser is created using the[`functions.auth.user().onCreate()`](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder#authuserbuilderoncreate)event handler:

<br />

```transact-sql
exports.sendWelcomeEmail = functions.runWith({secrets: [gmailPassword]}).auth.user().onCreate((user) => {
  // ...
});
```

<br />

Firebaseaccounts will trigger user creation events forCloud Functionswhen:

- A user creates an email account and password.
- A user signs in for the first time using a federated identity provider.
- The developer creates an account using the Admin SDK.
- A user signs in to a new anonymous auth session for the first time.

ACloud Functionsevent is*not*triggered when a user signs in for the first time using a custom token.

### Access user attributes

From the user data returned to your function, you can access the list of user attributes available in the newly created user's[`UserRecord`](https://firebase.google.com/docs/reference/functions/firebase-functions.auth#authuserrecord)object. For example, you can get the user's email and display name as shown:

<br />

```gdscript
const email = user.email; // The email of the user.
const displayName = user.displayName; // The display name of the user.https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/email-users/functions/index.js#L54-L55
```

<br />

## Trigger a function on user deletion

Just as you can trigger a function on user creation, you can respond to user deletion events. Use the[`functions.auth.user().onDelete()`](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder#authuserbuilderondelete)event handler as shown:

<br />

```transact-sql
exports.sendByeEmail = functions.runWith({secrets: [gmailPassword]}).auth.user().onDelete((user) => {
  // ...
});
```

<br />

| **Caution:** Deleting multiple users at once using the Firebase Admin SDK (for example,`admin.auth().deleteUsers([uid1, uid2])`in Node.js) does not fire user deletion events, so event handlers set up using`functions.auth.user().onDelete()`*will not be triggered*. Delete users one at a time if you want user deletion events to fire for each deleted user.

## Trigger blocking functions

If you've upgraded toFirebase Authenticationwith Identity Platform, you can extendFirebase Authenticationusing[blockingCloud Functions](https://firebase.google.com/docs/auth/extend-with-blocking-functions).

Blocking functions let you execute custom code that modifies the result of a user registering or signing in to your app. For example, you can prevent a user from authenticating if they don't meet certain criteria, or update a user's information before returning it to your client app.