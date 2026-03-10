# Source: https://firebase.google.com/docs/app-check/custom-provider.md.txt

App Check has built-in support for several providers: DeviceCheck and App
Attest on Apple platforms, Play Integrity on Android, and reCAPTCHA Enterprise
in web apps ([overview](https://firebase.google.com/docs/app-check)). These are well-understood providers
that should meet the needs of most developers. You can, however, also implement
your own custom App Check providers. Using a custom provider is necessary
when:

- You want to use a provider other than the built-in ones.

- You want to use the built-in providers in unsupported ways.

- You want to verify devices using platforms other than Apple, Android, and the
  web. For example, you could create App Check providers for desktop OSes or
  Internet-of-Things devices.

- You want to implement your own verification techniques on any platform.

## Overview

To implement a custom App Check provider, you need a secure backend
environment that can run the Node.js [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup).
This can be Cloud Functions, a container platform such as
[Cloud Run](https://cloud.google.com/run), or your own server.

From this environment, you will provide a network-accessible service that
receives proof of authenticity from your app clients, and---if the proof of
authenticity passes your authenticity assessment---returns an App Check
token. The specific indicators you use as proof of authenticity will depend on
either the third-party provider you're using, or the indicators of your own
invention, if you're implementing custom logic.

Usually, you expose this service as a REST or gRPC endpoint, but this detail is
up to you.

## Create the token acquisition endpoint

1. [Install and initialize the Admin SDK](https://firebase.google.com/docs/admin/setup).

2. Create a network-accessible endpoint that can receive authenticity data from
   your clients. For example, using Cloud Functions:

       // Create endpoint at https://example-app.cloudfunctions.net/fetchAppCheckToken
       exports.fetchAppCheckToken = functions.https.onRequest((request, response) => {
         // ...
       });

3. Add to the endpoint logic that assesses the authenticity data. This is the
   core logic of your custom App Check provider, which you will need to
   write yourself.

4. If you determine the client to be authentic, use the Admin SDK to mint
   an App Check token and return it and its expiration time to the client:

       const admin = require('firebase-admin');
       admin.initializeApp();

       // ...

       admin.appCheck().createToken(appId)
           .then(function (appCheckToken) {
             // Token expires in an hour.
             const expiresAt = Math.floor(Date.now() / 1000) + 60 * 60;

             // Return appCheckToken and expiresAt to the client.
           })
          .catch(function (err) {
            console.error('Unable to create App Check token.');
            console.error(err);
          });

   > [!NOTE]
   > **Note:** If you encounter a token signing error while creating a new token, make sure your service account has the required permissions. See the [Admin SDK troubleshooting guide](https://firebase.google.com/docs/auth/admin/create-custom-tokens#troubleshooting).

   If you can't verify the client's authenticity, return an error (for example,
   return an HTTP 403 error).
5. **Optional** : Set the time-to-live (TTL) for App Check tokens issued by
   your custom provider by passing an `AppCheckTokenOptions` object to
   `createToken()`. You can set the TTL to any value between 30 minutes and 7
   days. When setting this value, be aware of the following tradeoffs:

   - Security: Shorter TTLs provide stronger security, because it reduces the window in which a leaked or intercepted token can be abused by an attacker.
   - Performance: Shorter TTLs mean your app will perform attestation more frequently. Because the app attestation process adds latency to network requests every time it's performed, a short TTL can impact the performance of your app.

   The default TTL of 1 hour is reasonable for most apps.

## Next steps

Now that you've implemented your custom provider's server-side logic, learn how
to use it from your [Apple](https://firebase.google.com/docs/app-check/ios/custom-provider),
[Android](https://firebase.google.com/docs/app-check/android/custom-provider), and [web](https://firebase.google.com/docs/app-check/web/custom-provider) clients.