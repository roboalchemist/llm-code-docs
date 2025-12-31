# Source: https://firebase.google.com/docs/auth/extend-with-blocking-functions.md.txt

Blocking functions let you execute custom code that modifies the result of a user registering or signing in to your app. For example, you can prevent a user from authenticating if they don't meet certain criteria, or update a user's information before returning it to your client app.

## Before you begin

To use blocking functions you must upgrade your Firebase project to[Firebase Authenticationwith Identity Platform](https://firebase.google.com/docs/auth#identity-platform). If you haven't already upgraded, do so first.

## Understanding blocking functions

You can register blocking functions for these events:

- **Before the user is created** : Triggers before a new user is saved to theFirebase Authenticationdatabase, and before a token is returned to your client app.

- **Before the user is signed in** : Triggers after a user's credentials are verified, but beforeFirebase Authenticationreturns an ID token to your client app. If your app uses multi-factor authentication, the function triggers after the user verifies their second factor. Note that creating a new user also triggers both these events.

- **Before sending an email (Node.js only)**: Triggers before an email (for example, a sign-in or password reset email) is sent to a user.

- **Before sending an SMS message (Node.js only)**: Triggers before an SMS Message is sent to a user, for cases such as multifactor authentication.

Keep the following in mind when using blocking functions:

- Your function must respond within 7 seconds. After 7 seconds,Firebase Authenticationreturns an error, and the client operation fails.

- HTTP response codes other than`200`are passed to your client apps. Ensure your client code handles any errors your function can return.

- Functions apply to all users in your project, including any contained in a[tenant](https://cloud.google.com/identity-platform/docs/multi-tenancy).Firebase Authenticationprovides information about users to your function, including any tenants they belong to, so you can respond accordingly.

- Linking another identity provider to an account re-triggers any registered`beforeUserSignedIn`functions.

- Anonymous and custom authentication do not trigger blocking functions.

| **Warning:** If you delete a function, you must also unregister the triggers withFirebase Authentication. Failure to do so will prevent all users from authenticating with your app.

## Deploy a blocking function

To insert your custom code into the user authentication flows, deploy blocking functions. Once your blocking functions are deployed, your custom code must complete successfully for authentication and user creation to succeed.

You deploy a blocking function the same way as you deploy any function. (see theCloud Functions[Getting started](https://firebase.google.com/docs/functions/get-started?2nd-gen)page for details). In summary:

1. Write a function that handles the targeted event.

   For example, to get started, you can add a no-op function like the following to your source:  

   ### Node.js

       import {
         beforeUserCreated,
       } from "firebase-functions/v2/identity";

       export const beforecreated = beforeUserCreated((event) => {
         // TODO
         return;
       });

   ### Python

       @identity_fn.before_user_created()
       def created_noop(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
           return

   The above example has omitted the implementation of custom auth logic. See the following sections to learn how to implement your blocking functions and[Common scenarios](https://firebase.google.com/docs/auth/extend-with-blocking-functions#common-scenarios)for specific examples.
2. Deploy your functions using theFirebaseCLI:

       firebase deploy --only functions

   You must re-deploy your functions each time you update them.

## Getting user and context information

Blocking events provide an`AuthBlockingEvent`object that contains information about the user signing in. Use these values in your code to determine whether to allow an operation to proceed.

The object contains the following properties:

|         Name         |                                                                                Description                                                                                 |                                                           Example                                                           |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `locale`             | The application locale. You can set the locale using the client SDK, or by passing the locale header in the REST API.                                                      | `fr`or`sv-SE`                                                                                                               |
| `ipAddress`          | The IP address of the device the end user is registering or signing in from.                                                                                               | `114.14.200.1`                                                                                                              |
| `userAgent`          | The user agent triggering the blocking function.                                                                                                                           | `Mozilla/5.0 (X11; Linux x86_64)`                                                                                           |
| `eventId`            | The event's unique identifier.                                                                                                                                             | `rWsyPtolplG2TBFoOkkgyg`                                                                                                    |
| `eventType`          | The event type. This provides information on the event name, such as`beforeSignIn`or`beforeCreate`, and the associated sign-in method used, like Google or email/password. | `providers/cloud.auth/eventTypes/user.beforeSignIn:password`                                                                |
| `authType`           | Always`USER`.                                                                                                                                                              | `USER`                                                                                                                      |
| `resource`           | TheFirebase Authenticationproject or tenant.                                                                                                                               | `projects/`<var translate="no">project-id</var>`/tenants/`<var translate="no">tenant-id</var>                               |
| `timestamp`          | The time the event was triggered, formatted as an[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)string.                                                                   | `Tue, 23 Jul 2019 21:10:57 GMT`                                                                                             |
| `additionalUserInfo` | An object containing information about the user.                                                                                                                           | [`AdditionalUserInfo`](https://cloud.google.com/identity-platform/docs/reference/gcip-cloud-functions#additional-user-info) |
| `credential`         | An object containing information about the user's credential.                                                                                                              | [`AuthCredential`](https://cloud.google.com/identity-platform/docs/reference/gcip-cloud-functions#auth-credential)          |

## Blocking registration or sign-in

To block a registration or sign-in attempt, throw an`HttpsError`in your function. For example:  

### Node.js

    import { HttpsError } from "firebase-functions/v2/identity";

    throw new HttpsError('invalid-argument');

### Python

    raise https_fn.HttpsError(
        code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT)

You can also specify a custom error message:  

### Node.js

    throw new HttpsError('permission-denied', 'Unauthorized request origin!');

### Python

    raise https_fn.HttpsError(
        code=https_fn.FunctionsErrorCode.PERMISSION_DENIED,
        message="Unauthorized request origin!"
    )

The following example shows how to block users who are not within a specific domain from registering for your app:  

### Node.js

    export const beforecreated = beforeUserCreated((event) => {
      const user = event.data;
      // (If the user is authenticating within a tenant context, the tenant ID can be determined from
      // user.tenantId or from event.resource, e.g. 'projects/project-id/tenant/tenant-id-1')

      // Only users of a specific domain can sign up.
      if (!user?.email?.includes('@acme.com')) {
        throw new HttpsError('invalid-argument', "Unauthorized email");
      }
    });

### Python

    # Block account creation with any non-acme email address.
    @identity_fn.before_user_created()
    def validatenewuser(
            event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
        # User data passed in from the CloudEvent.
        user = event.data

        # Only users of a specific domain can sign up.
        if user.email is None or "@acme.com" not in user.email:
            # Return None so that Firebase Auth rejects the account creation.
            raise https_fn.HttpsError(code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
                                      message="Unauthorized email")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L38-L55

Regardless of whether you use a default or custom message,Cloud Functionswraps the error and returns it to the client as an internal error. For example:  

### Node.js

    throw new HttpsError('invalid-argument', "Unauthorized email");

### Python

    # Only users of a specific domain can sign up.
    if user.email is None or "@acme.com" not in user.email:
        # Return None so that Firebase Auth rejects the account creation.
        raise https_fn.HttpsError(code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
                                  message="Unauthorized email")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L50-L54

Your app should catch the error, and handle it accordingly. For example:  

### JavaScript

    import { getAuth, createUserWithEmailAndPassword } from 'firebase/auth';

    // Blocking functions can also be triggered in a multi-tenant context before user creation.
    // firebase.auth().tenantId = 'tenant-id-1';
    const auth = getAuth();
    try {
      const result = await createUserWithEmailAndPassword(auth)
      const idTokenResult = await result.user.getIdTokenResult();
      console.log(idTokenResult.claim.admin);
    } catch(error) {
      if (error.code !== 'auth/internal-error' && error.message.indexOf('Cloud Function') !== -1) {
          // Display error.
        } else {
          // Registration succeeds.
        }
    }

## Modifying a user

Instead of blocking a registration or sign-in attempt, you can allow the operation to continue, but modify the`User`object that is saved toFirebase Authentication's database and returned to the client.

To modify a user, return an object from your event handler containing the fields to modify. You can modify the following fields:

- `displayName`
- `disabled`
- `emailVerified`
- `photoUrl`
- `customClaims`
- `sessionClaims`(`beforeUserSignedIn`only)

With the exception of`sessionClaims`, all modified fields are saved toFirebase Authentication's database, which means they are included on the response token and persist between user sessions.

The following example shows how to set a default display name:  

### Node.js

    export const beforecreated = beforeUserCreated((event) => {
      return {
        // If no display name is provided, set it to "Guest".
        displayName: event.data.displayName || 'Guest'
      };
    });

### Python

    @identity_fn.before_user_created()
    def setdefaultname(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
        return identity_fn.BeforeCreateResponse(
            # If no display name is provided, set it to "Guest".
            display_name=event.data.display_name if event.data.display_name is not None else "Guest")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L60-L64

If you register an event handler for both`beforeUserCreated`and`beforeUserSignedIn`, note that`beforeUserSignedIn`executes after`beforeUserCreated`. User fields updated in`beforeUserCreated`are visible in`beforeUserSignedIn`. If you set a field other than`sessionClaims`in both event handlers, the value set in`beforeUserSignedIn`overwrites the value set in`beforeUserCreated`. For`sessionClaims`only, they are propagated to the current session's token claims, but are not persisted or stored in the database.

For example, if any`sessionClaims`are set,`beforeUserSignedIn`will return them with any`beforeUserCreated`claims, and they will be merged. When they're merged, if a`sessionClaims`key matches a key in`customClaims`, the matching`customClaims`will be overwritten in the token claims by the`sessionClaims`key. However, the overwitten`customClaims`key will still be persisted in the database for future requests.

## Supported OAuth credentials and data

You can pass OAuth credentials and data to blocking functions from various identity providers. The following table shows what credentials and data are supported for each identity provider:

| Identity Provider | ID Token | Access Token | Expiration Time | Token Secret | Refresh Token | Sign-in Claims |
|-------------------|----------|--------------|-----------------|--------------|---------------|----------------|
| Google            | Yes      | Yes          | Yes             | No           | Yes           | No             |
| Facebook          | No       | Yes          | Yes             | No           | No            | No             |
| Twitter           | No       | Yes          | No              | Yes          | No            | No             |
| GitHub            | No       | Yes          | No              | No           | No            | No             |
| Microsoft         | Yes      | Yes          | Yes             | No           | Yes           | No             |
| LinkedIn          | No       | Yes          | Yes             | No           | No            | No             |
| Yahoo             | Yes      | Yes          | Yes             | No           | Yes           | No             |
| Apple             | Yes      | Yes          | Yes             | No           | Yes           | No             |
| SAML              | No       | No           | No              | No           | No            | Yes            |
| OIDC              | Yes      | Yes          | Yes             | No           | Yes           | Yes            |

### OAuth tokens

To use an ID token, access token, or refresh token in a blocking function, you must first select the checkbox on the**Blocking functions** page of theFirebaseconsole.

Refresh tokens will not be returned by any identity providers when signing in directly with an OAuth credential, such as an ID token or access token. In this situation, the same client-side OAuth credential will be passed to the blocking function.

The following sections describe each identity provider types and their supported credentials and data.

#### Generic OIDC providers

When a user signs in with a generic OIDC provider, the following credentials will be passed:

- **ID token** : Provided if the`id_token`flow is selected.
- **Access token**: Provided if the code flow is selected. Note that the code flow is only currently supported via the REST API.
- **Refresh token** : Provided if the[`offline_access`scope](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess)is selected.

Example:  

    const provider = new firebase.auth.OAuthProvider('oidc.my-provider');
    provider.addScope('offline_access');
    firebase.auth().signInWithPopup(provider);

#### Google

When a user signs in with Google, the following credentials will be passed:

- **ID token**
- **Access token**
- **Refresh token** : Only provided if the following custom parameters are requested:
  - `access_type=offline`
  - `prompt=consent`, if the user previously consented and no new scope was requested

Example:  

    import { getAuth, signInWithPopup, GoogleAuthProvider } from 'firebase/auth';

    const auth = getAuth();
    const provider = new GoogleAuthProvider();
    provider.setCustomParameters({
      'access_type': 'offline',
      'prompt': 'consent'
    });
    signInWithPopup(auth, provider);

Learn more about[Google refresh tokens](https://developers.google.com/identity/protocols/oauth2/openid-connect#refresh-tokens).

#### Facebook

When a user signs in with Facebook, the following credential will be passed:

- **Access token** : An access token is returned that can be exchanged for another access token. Learn more about the different types of[access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/)supported by Facebook and how you can exchange them for[long-lived tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/expiration-and-extension).

#### GitHub

When a user signs in with GitHub, the following credential will be passed:

- **Access token**: Does not expire unless revoked.

#### Microsoft

When a user signs in with Microsoft, the following credentials will be passed:

- **ID token**
- **Access token**
- **Refresh token** : Passed to the blocking function if the[`offline_access`scope](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess)is selected.

Example:  

    import { getAuth, signInWithPopup, OAuthProvider } from 'firebase/auth';

    const auth = getAuth();
    const provider = new OAuthProvider('microsoft.com');
    provider.addScope('offline_access');
    signInWithPopup(auth, provider);

#### Yahoo

When a user signs in with Yahoo, the following credentials will be passed without any custom parameters or scopes:

- **ID token**
- **Access token**
- **Refresh token**

#### LinkedIn

When a user signs in with LinkedIn, the following credential will be passed:

- **Access token**

#### Apple

When a user signs in with Apple, the following credentials will be passed without any custom parameters or scopes:

- **ID token**
- **Access token**
- **Refresh token**

## Common scenarios

The following examples demonstrate some common use cases for blocking functions:

### Only allowing registration from a specific domain

The following example shows how to prevent users who aren't part of the`example.com`domain from registering with your app:  

### Node.js

    export const beforecreated = beforeUserCreated((event) => {
      const user = event.data;
      if (!user?.email?.includes('@example.com')) {
        throw new HttpsError(
          'invalid-argument', 'Unauthorized email');
      }
    });

### Python

     @identity_fn.before_user_created()
       def validatenewuser(
           event: identity_fn.AuthBlockingEvent,
       ) -> identity_fn.BeforeCreateResponse | None:
           # User data passed in from the CloudEvent.
           user = event.data

           # Only users of a specific domain can sign up.
           if user.email is None or "@example.com" not in user.email:
               # Return None so that Firebase Auth rejects the account creation.
               raise https_fn.HttpsError(
                   code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
                   message="Unauthorized email",
               )

### Blocking users with unverified emails from registering

The following example shows how to prevent users with unverified emails from registering with your app:  

### Node.js

    export const beforecreated = beforeUserCreated((event) => {
      const user = event.data;
      if (user.email && !user.emailVerified) {
        throw new HttpsError(
          'invalid-argument', 'Unverified email');
      }
    });

### Python

    @identity_fn.before_user_created()
    def requireverified(
            event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
        if event.data.email is not None and not event.data.email_verified:
            raise https_fn.HttpsError(code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
                                      message="You must register using a trusted provider.")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L69-L74

### Treating certain identity provider emails as verified

The following example shows how to treat user emails from certain identity providers as verified:  

### Node.js

    export const beforecreated = beforeUserCreated((event) => {
      const user = event.data;
      if (user.email && !user.emailVerified && event.eventType.includes(':facebook.com')) {
        return {
          emailVerified: true,
        };
      }
    });

### Python

    @identity_fn.before_user_created()
    def markverified(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
        if event.data.email is not None and "@facebook.com" in event.data.email:
            return identity_fn.BeforeSignInResponse(email_verified=True)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L104-L107

### Blocking sign-in from certain IP addresses

The following example shows how to block sign-in from certain IP address ranges:  

### Node.js

    export const beforesignedin = beforeUserSignedIn((event) => {
      if (isSuspiciousIpAddress(event.ipAddress)) {
        throw new HttpsError(
          'permission-denied', 'Unauthorized access!');
      }
    });

### Python

    @identity_fn.before_user_signed_in()
    def ipban(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeSignInResponse | None:
        if is_suspicious(event.ip_address):
            raise https_fn.HttpsError(code=https_fn.FunctionsErrorCode.PERMISSION_DENIED,
                                      message="IP banned.")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L116-L120

### Setting custom and session claims

The following example shows how to set custom and session claims:  

### Node.js

    export const beforecreated = beforeUserCreated((event) => {
        if (event.credential &&
            event.credential.claims &&
            event.credential.providerId === "saml.my-provider-id") {
            return {
                // Employee ID does not change so save in persistent claims (stored in
                // Auth DB).
                customClaims: {
                    eid: event.credential.claims.employeeid,
                },
            };
        }
    });

    export const beforesignin = beforeUserSignedIn((event) => {
        if (event.credential &&
            event.credential.claims &&
            event.credential.providerId === "saml.my-provider-id") {
            return {
                // Copy role and groups to token claims. These will not be persisted.
                sessionClaims: {
                    role: event.credential.claims.role,
                    groups: event.credential.claims.groups,
                },
            };
        }
    });

### Python

    @identity_fn.before_user_created()
    def setemployeeid(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
        if (event.credential is not None and event.credential.claims is not None and
                event.credential.provider_id == "saml.my-provider-id"):
            return identity_fn.BeforeCreateResponse(
                custom_claims={"eid": event.credential.claims["employeeid"]})


    @identity_fn.before_user_signed_in()
    def copyclaimstosession(
            event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeSignInResponse | None:
        if (event.credential is not None and event.credential.claims is not None and
                event.credential.provider_id == "saml.my-provider-id"):
            return identity_fn.BeforeSignInResponse(session_claims={
                "role": event.credential.claims["role"],
                "groups": event.credential.claims["groups"]
            })  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L125-L141

### Tracking IP addresses to monitor suspicious activity

You can prevent token theft by tracking the IP address a user signs in from, and comparing it to the IP address on subsequent requests. If the request appears suspicious --- for example, the IPs are from from different geographical regions --- you can ask the user to sign in again.

1. Use session claims to track the IP address the user signs in with:

   ### Node.js

       export const beforesignedin = beforeUserSignedIn((event) => {
         return {
           sessionClaims: {
             signInIpAddress: event.ipAddress,
           },
         };
       });

   ### Python

       @identity_fn.before_user_signed_in()
       def logip(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeSignInResponse | None:
           return identity_fn.BeforeSignInResponse(session_claims={"signInIpAddress": event.ip_address})  
       https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L146-L148

2. When a user attempts to access resources that require authentication withFirebase Authentication, compare the IP address in the request with the IP used to sign in:

   ### Node.js

       app.post('/getRestrictedData', (req, res) => {
         // Get the ID token passed.
         const idToken = req.body.idToken;
         // Verify the ID token, check if revoked and decode its payload.
         admin.auth().verifyIdToken(idToken, true).then((claims) => {
           // Get request IP address
           const requestIpAddress = req.connection.remoteAddress;
           // Get sign-in IP address.
           const signInIpAddress = claims.signInIpAddress;
           // Check if the request IP address origin is suspicious relative to
           // the session IP addresses. The current request timestamp and the
           // auth_time of the ID token can provide additional signals of abuse,
           // especially if the IP address suddenly changed. If there was a sudden
           // geographical change in a short period of time, then it will give
           // stronger signals of possible abuse.
           if (!isSuspiciousIpAddressChange(signInIpAddress, requestIpAddress)) {
             // Suspicious IP address change. Require re-authentication.
             // You can also revoke all user sessions by calling:
             // admin.auth().revokeRefreshTokens(claims.sub).
             res.status(401).send({error: 'Unauthorized access. Please login again!'});
           } else {
             // Access is valid. Try to return data.
             getData(claims).then(data => {
               res.end(JSON.stringify(data);
             }, error => {
               res.status(500).send({ error: 'Server error!' })
             });
           }
         });
       });

   ### Python

       from firebase_admin import auth, initialize_app
       import flask

       initialize_app()
       flask_app = flask.Flask(__name__)

       @flask_app.post()
       def get_restricted_data(req: flask.Request):
           # Get the ID token passed.
           id_token = req.json().get("idToken")

           # Verify the ID token, check if revoked, and decode its payload.
           try:
               claims = auth.verify_id_token(id_token, check_revoked=True)
           except:
               return flask.Response(status=500)

           # Get request IP address.
           request_ip = req.remote_addr

           # Get sign-in IP address.
           signin_ip = claims["signInIpAddress"]

           # Check if the request IP address origin is suspicious relative to
           # the session IP addresses. The current request timestamp and the
           # auth_time of the ID token can provide additional signals of abuse,
           # especially if the IP address suddenly changed. If there was a sudden
           # geographical change in a short period of time, then it will give
           # stronger signals of possible abuse.
           if is_suspicious_change(signin_ip, request_ip):
               # Suspicious IP address change. Require re-authentication.
               # You can also revoke all user sessions by calling:
               #   auth.revoke_refresh_tokens(claims["sub"])
               return flask.Response(status=401,
                                     response="Unauthorized access. Sign in again!")
           else:
               # Access is valid. Try to return data.
               return data_from_claims(claims)

### Screening user photos

The following example shows how to sanitize users' profile photos:  

### Node.js

    export const beforecreated = beforeUserCreated((event) => {
      const user = event.data;
      if (user.photoURL) {
        return isPhotoAppropriate(user.photoURL)
          .then((status) => {
            if (!status) {
              // Sanitize inappropriate photos by replacing them with guest photos.
              // Users could also be blocked from sign-up, disabled, etc.
              return {
                photoUrl: PLACEHOLDER_GUEST_PHOTO_URL,
              };
            }
          });
    });

### Python

    @identity_fn.before_user_created()
    def sanitizeprofilephoto(
            event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
        if event.data.photo_url is not None:
            score = analyze_photo_with_ml(event.data.photo_url)
            if score > THRESHOLD:
                return identity_fn.BeforeCreateResponse(photo_url=PLACEHOLDER_URL)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/auth-blocking-functions/functions/main.py#L161-L167

To learn more about how to detect and sanitize images, see the[Cloud Vision](https://cloud.google.com/vision)documentation.

### Accessing a user's identity provider OAuth credentials

The following example demonstrates how to obtain a refresh token for a user that signed in with Google, and use it to call the Google Calendar APIs. The refresh token is stored for offline access.  

### Node.js

    const {OAuth2Client} = require('google-auth-library');
    const {google} = require('googleapis');
    // ...
    // Initialize Google OAuth client.
    const keys = require('./oauth2.keys.json');
    const oAuth2Client = new OAuth2Client(
      keys.web.client_id,
      keys.web.client_secret
    );

    export const beforecreated = beforeUserCreated((event) => {
      const user = event.data;
      if (event.credential &&
          event.credential.providerId === 'google.com') {
        // Store the refresh token for later offline use.
        // These will only be returned if refresh tokens credentials are included
        // (enabled by Cloud console).
        return saveUserRefreshToken(
            user.uid,
            event.credential.refreshToken,
            'google.com'
          )
          .then(() => {
            // Blocking the function is not required. The function can resolve while
            // this operation continues to run in the background.
            return new Promise((resolve, reject) => {
              // For this operation to succeed, the appropriate OAuth scope should be requested
              // on sign in with Google, client-side. In this case:
              // https://www.googleapis.com/auth/calendar
              // You can check granted_scopes from within:
              // event.additionalUserInfo.profile.granted_scopes (space joined list of scopes).

              // Set access token/refresh token.
              oAuth2Client.setCredentials({
                access_token: event.credential.accessToken,
                refresh_token: event.credential.refreshToken,
              });
              const calendar = google.calendar('v3');
              // Setup Onboarding event on user's calendar.
              const event = {/** ... */};
              calendar.events.insert({
                auth: oauth2client,
                calendarId: 'primary',
                resource: event,
              }, (err, event) => {
                // Do not fail. This is a best effort approach.
                resolve();
              });
          });
        })
      }
    });

### Python

    @identity_fn.before_user_created()
    def savegoogletoken(
            event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
        """During sign-up, save the Google OAuth2 access token and queue up a task
        to schedule an onboarding session on the user's Google Calendar.

        You will only get an access token if you enabled it in your project's blocking
        functions settings in the Firebase console:

        https://console.firebase.google.com/project/_/authentication/settings
        """
        if event.credential is not None and event.credential.provider_id == "google.com":
            print(f"Signed in with {event.credential.provider_id}. Saving access token.")

            firestore_client: google.cloud.firestore.Client = firestore.client()
            doc_ref = firestore_client.collection("user_info").document(event.data.uid)
            doc_ref.set({"calendar_access_token": event.credential.access_token}, merge=True)

            tasks_client = google.cloud.tasks_v2.CloudTasksClient()
            task_queue = tasks_client.queue_path(params.PROJECT_ID.value,
                                                 options.SupportedRegion.US_CENTRAL1,
                                                 "scheduleonboarding")
            target_uri = get_function_url("scheduleonboarding")
            calendar_task = google.cloud.tasks_v2.Task(http_request={
                "http_method": google.cloud.tasks_v2.HttpMethod.POST,
                "url": target_uri,
                "headers": {
                    "Content-type": "application/json"
                },
                "body": json.dumps({
                    "data": {
                        "uid": event.data.uid
                    }
                }).encode()
            },
                                                       schedule_time=datetime.now() +
                                                       timedelta(minutes=1))
            tasks_client.create_task(parent=task_queue, task=calendar_task)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/post-signup-event/functions/main.py#L32-L69

### Overriding reCAPTCHA Enterprise verdict for user operation

The following example shows how to override a reCAPTCHA Enterprise verdict for supported user flows.

Refer to[Enable reCAPTCHA Enterprise](https://cloud.google.com/identity-platform/docs/recaptcha-enterprise)to learn more about integrating reCAPTCHA Enterprise with Firebase Authentication.

Blocking functions can be used to allow or block flows based on custom factors, thereby overriding the result provided by reCAPTCHA Enterprise.  

### Node.js

    const { beforeSmsSent } = require("firebase-functions/v2/identity");
    exports.beforesmssentv2 = beforeSmsSent((event) => {
     if (
       event.smsType === "SIGN_IN_OR_SIGN_UP" &&
       event.additionalUserInfo.phoneNumber.includes('+91')
     ) {
       return {
         recaptchaActionOverride: "ALLOW",
       };
     }

     // Allow users to sign in with recaptcha score greater than 0.5
     if (event.additionalUserInfo.recaptchaScore > 0.5) {
       return {
         recaptchaActionOverride: 'ALLOW',
       };
     }

     // Block all others.
     return  {
       recaptchaActionOverride: 'BLOCK',
     }
    });