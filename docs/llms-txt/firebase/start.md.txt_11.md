# Source: https://firebase.google.com/docs/auth/unity/start.md.txt

[Video](https://www.youtube.com/watch?v=52yUcKLMKX0)

You can use Firebase Authentication to allow users to sign in to your game using one
or more sign-in methods, including email address and password sign-in, and
federated identity providers such as Google Sign-in and Facebook Login. This
tutorial gets you started with Firebase Authentication by showing you how to add
email address and password sign-in to your game.

## Before you begin

Before you can use
[Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseAuth.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

## Sign up new users

Create a form that allows new users to register with your game using their email
address and a password. When a user completes the form, validate the email
address and password provided by the user, then pass them to the
`CreateUserWithEmailAndPasswordAsync` method:

    auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
    auth.CreateUserWithEmailAndPasswordAsync(email, password).ContinueWith(task => {
      if (task.IsCanceled) {
        Debug.LogError("CreateUserWithEmailAndPasswordAsync was canceled.");
        return;
      }
      if (task.IsFaulted) {
        Debug.LogError("CreateUserWithEmailAndPasswordAsync encountered an error: " + task.Exception);
        return;
      }

      // Firebase user has been created.
      Firebase.Auth.AuthResult result = task.Result;
      Debug.LogFormat("Firebase user created successfully: {0} ({1})",
          result.User.DisplayName, result.User.UserId);
    });

## Sign in existing users

Create a form that allows existing users to sign in using their email address
and password. When a user completes the form, call the
`SignInWithEmailAndPasswordAsync` method:

    auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
    auth.SignInWithEmailAndPasswordAsync(email, password).ContinueWith(task => {
      if (task.IsCanceled) {
        Debug.LogError("SignInWithEmailAndPasswordAsync was canceled.");
        return;
      }
      if (task.IsFaulted) {
        Debug.LogError("SignInWithEmailAndPasswordAsync encountered an error: " + task.Exception);
        return;
      }

      Firebase.Auth.AuthResult result = task.Result;
      Debug.LogFormat("User signed in successfully: {0} ({1})",
          result.User.DisplayName, result.User.UserId);
    });

## Set an authentication state change event handler and get user data

To respond to sign-in and sign-out events, attach an event handler to the global
authentication object. This handler gets called whenever the user's sign-in
state changes. Because the handler runs only after the authentication object is
fully initialized and after any network calls have completed, it is the best
place to get information about the signed-in user.

Register the event handler using the `FirebaseAuth` object's `StateChanged`
field. When a user successfully signs in, you can get information about the user
in the event handler.

Finally, when this object has `Destroy` called on it, it will automatically call
`OnDestroy`. Clean up the Auth object's references in `OnDestroy`.

    void InitializeFirebase() {
      auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
      auth.StateChanged += AuthStateChanged;
      AuthStateChanged(this, null);
    }

    void AuthStateChanged(object sender, System.EventArgs eventArgs) {
      if (auth.CurrentUser != user) {
        bool signedIn = user != auth.CurrentUser && auth.CurrentUser != null
            && auth.CurrentUser.IsValid();
        if (!signedIn && user != null) {
          Debug.Log("Signed out " + user.UserId);
        }
        user = auth.CurrentUser;
        if (signedIn) {
          Debug.Log("Signed in " + user.UserId);
          displayName = user.DisplayName ?? "";
          emailAddress = user.Email ?? "";
          photoUrl = user.PhotoUrl ?? "";
        }
      }
    }

    void OnDestroy() {
      auth.StateChanged -= AuthStateChanged;
      auth = null;
    }

## Next steps

Learn how to add support for other identity providers and anonymous guest
accounts:

- [Google Sign-in](https://firebase.google.com/docs/auth/unity/google-signin)
- [Facebook Login](https://firebase.google.com/docs/auth/unity/facebook-login)
- [Twitter Login](https://firebase.google.com/docs/auth/unity/twitter-login)
- [GitHub Login](https://firebase.google.com/docs/auth/unity/github-auth)
- [Microsoft Login](https://firebase.google.com/docs/auth/cpp/microsoft-oauth)
- [Yahoo Login](https://firebase.google.com/docs/auth/cpp/yahoo-oauth)
- [Anonymous sign-in](https://firebase.google.com/docs/auth/unity/anonymous-auth)
- [Phone Authentication](https://firebase.google.com/docs/auth/unity/phone-auth)