# Source: https://firebase.google.com/docs/app-check/unity/custom-resource.md.txt

You can use App Check to protect non-Google custom backend resources for
your app, like your own self-hosted backend. To do so, you'll need to do both of
the following:

- Modify your app client to send an App Check token along with each request to your backend, as described on this page.
- Modify your backend to require a valid App Check token with every request, as described in [Verify App Check tokens from a custom backend](https://firebase.google.com/docs/app-check/custom-resource-backend).

## Before you begin

Add App Check to your app, using the [default providers](https://firebase.google.com/docs/app-check/unity/default-providers).

## Send App Check tokens with backend requests

To ensure your backend requests include a valid, unexpired, App Check token,
precede each request with a call to `FirebaseAppCheck.GetAppCheckTokenAsync()`.
The App Check library will refresh the token if necessary.

Once you have a valid token, send it along with the request to your backend. The
specifics of how you accomplish this are up to you, but *don't send
App Check tokens as part of URLs*, including in query parameters, as this
makes them vulnerable to accidental leakage and interception. The recommended
approach is to send the token in a custom HTTP header.

For example:

    void CallApiExample() {
        FirebaseAppCheck.DefaultInstance.GetAppCheckToken(false).
          ContinueWithOnMainThread(task => {
            if (!task.IsFaulted) {
                // Got a valid App Check token. Include it in your own http calls.
            }
        });
    }