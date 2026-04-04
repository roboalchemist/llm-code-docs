# Source: https://firebase.google.com/docs/auth/unity/anonymous-auth.md.txt

You can use Firebase Authentication to create and use temporary anonymous accounts
to authenticate with Firebase. These temporary anonymous accounts can be used to
allow users who haven't yet signed up to your app to work with data protected
by security rules. If an anonymous user decides to sign up to your app, you can
[link their sign-in credentials to the anonymous
account](https://firebase.google.com/docs/auth/unity/account-linking) so that they can continue to work with their protected data in
future sessions.

## Before you begin

1. Before you can use
   [Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth),
   you need to add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically,
   `FirebaseAuth.unitypackage`) to your Unity project.

   <br />

   <br />

   **Find detailed instructions for these initial setup steps in
   [Add Firebase to your
   Unity project](https://firebase.google.com/docs/unity/setup#set_up_environment).**
2. If you haven't yet connected your app to your Firebase project, do so from the [Firebase console](https://console.firebase.google.com/).
3. Enable anonymous auth:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
   2. On the **Sign-in Methods** page, enable the **Anonymous** sign-in method.
   3. **Optional** : If you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can enable automatic clean-up. When you enable this setting, anonymous accounts older than 30 days will be automatically deleted. In projects with automatic clean-up enabled, anonymous authentication will no longer count toward usage limits or billing quotas. See [Automatic clean-up](https://firebase.google.com/docs/auth/unity/anonymous-auth#auto-cleanup).

## Authenticate with Firebase anonymously

When a signed-out user uses an app feature that requires authentication with
Firebase, sign in the user anonymously by completing the following steps:
The `FirebaseAuth` class is the gateway for all API calls. It is accessible through [FirebaseAuth.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#defaultinstance).

```c#
Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
```
1. Call `Firebase.Auth.FirebaseAuth.SignInAnonymouslyAsync`.

```c#
auth.SignInAnonymouslyAsync().ContinueWith(task => {
  if (task.IsCanceled) {
    Debug.LogError("SignInAnonymouslyAsync was canceled.");
    return;
  }
  if (task.IsFaulted) {
    Debug.LogError("SignInAnonymouslyAsync encountered an error: " + task.Exception);
    return;
  }

  Firebase.Auth.AuthResult result = task.Result;
  Debug.LogFormat("User signed in successfully: {0} ({1})",
      result.User.DisplayName, result.User.UserId);
});
```

<br />

To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the [Firebase console](https://console.firebase.google.com/project/_/authentication/providers).

## Convert an anonymous account to a permanent account

When an anonymous user signs up to your app, you might want to allow them to
continue their work with their new account---for example, you might want to
make the items the user added to their shopping cart before they signed up
available in their new account's shopping cart. To do so, complete the following
steps:

1. When the user signs up, complete the sign-in flow for the user's authentication provider up to, but not including, calling one of the [`Firebase.Auth.FirebaseAuth.SignInAndRetrieveDataWithCredentialAsync`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#signinandretrievedatawithcredentialasync) methods. For example, get the user's Google ID token, Facebook access token, or email address and password.
2. Get an `Firebase.Auth.Credential` for the new authentication provider:

3. Pass the `Firebase.Auth.Credential` object to the sign-in user's
   `LinkWithCredentialAsync` method:

If the call to `LinkWithCredentialAsync` succeeds, the user's new account can
access the anonymous account's Firebase data.

> [!NOTE]
> This technique can also be used to [link any two accounts](https://firebase.google.com/docs/auth/unity/account-linking).

## Automatic clean-up

If you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can
enable automatic clean-up in the Firebase console. When you enable this feature you allow
Firebase to automatically delete anonymous accounts older than 30 days. In projects with automatic
clean-up enabled, anonymous authentication will not count toward usage limits or billing quotas.

- Any anonymous accounts created after enabling automatic clean-up might be automatically deleted any time after 30 days post-creation.
- Existing anonymous accounts will be eligible for automatic deletion 30 days after enabling automatic clean-up.
- If you turn automatic clean-up off, any anonymous accounts scheduled to be deleted will remain scheduled to be deleted.
- If you "upgrade" an anonymous account by linking it to any sign-in method, the account will not get automatically deleted.

If you want to see how many users will be affected before you enable this feature, and you've
upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can filter by
`is_anon` in [Cloud
Logging](https://cloud.google.com/logging/docs).

## Next steps

Now that users can authenticate with Firebase, you can control their access to
data in your Firebase database using
[Firebase rules](https://firebase.google.com/docs/database/security#section-authorization).