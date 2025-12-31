# Source: https://firebase.google.com/docs/auth/admin/verify-id-tokens.md.txt

<br />

If your Firebase client app communicates with a custom backend server, you might need to identify the currently signed-in user on that server. To do so securely, after a successful sign-in, send the user's ID token to your server using HTTPS. Then, on the server, verify the integrity and authenticity of the ID token and retrieve the`uid`from it. You can use the`uid`transmitted in this way to securely identify the currently signed-in user on your server.
| **Note:** Many use cases for verifying ID tokens on the server can be accomplished by using Security Rules for the[Firebase Realtime Database](https://firebase.google.com/docs/database/security)and[Cloud Storage](https://firebase.google.com/docs/storage/security). See if those solve your problem before verifying ID tokens yourself.
| **Warning:** The ID token verification methods included in the Firebase Admin SDKs are meant to verify ID tokens that come from the client SDKs, not the custom tokens that you create with the Admin SDKs. See[Auth tokens](https://firebase.google.com/docs/auth/users#auth_tokens)for more information.

## Before you begin

To verify ID tokens with the Firebase Admin SDK, you must have a service account. Follow the[Admin SDK setup instructions](https://firebase.google.com/docs/admin/setup)for more information on how to initialize the Admin SDK with a service account.

## Retrieve ID tokens on clients

When a user or device successfully signs in, Firebase creates a corresponding ID token that uniquely identifies them and grants them access to several resources, such asFirebase Realtime DatabaseandCloud Storage. You can re-use that ID token to identify the user or device on your custom backend server. To retrieve the ID token from the client, make sure the user is signed in and then get the ID token from the signed-in user:  

### iOS+

##### Objective-C

    FIRUser *currentUser = [FIRAuth auth].currentUser;
    [currentUser getIDTokenForcingRefresh:YES
                               completion:^(NSString *_Nullable idToken,
                                            NSError *_Nullable error) {
              if (error) {
                // Handle error
                return;
              }

              // Send token to your backend via HTTPS
              // ...
    }];

##### Swift

    let currentUser = FIRAuth.auth()?.currentUser
    currentUser?.getIDTokenForcingRefresh(true) { idToken, error in
      if let error = error {
        // Handle error
        return;
      }

      // Send token to your backend via HTTPS
      // ...
    }

### Android

    FirebaseUser mUser = FirebaseAuth.getInstance().getCurrentUser();
    mUser.getIdToken(true)
        .addOnCompleteListener(new OnCompleteListener<GetTokenResult>() {
            public void onComplete(@NonNull Task<GetTokenResult> task) {
                if (task.isSuccessful()) {
                    String idToken = task.getResult().getToken();
                    // Send token to your backend via HTTPS
                    // ...
                } else {
                    // Handle error -> task.getException();
                }
            }
        });

### Unity

    Firebase.Auth.FirebaseUser user = auth.CurrentUser;
    user.TokenAsync(true).ContinueWith(task => {
      if (task.IsCanceled) {
        Debug.LogError("TokenAsync was canceled.");
       return;
      }

      if (task.IsFaulted) {
        Debug.LogError("TokenAsync encountered an error: " + task.Exception);
        return;
      }

      string idToken = task.Result;

      // Send token to your backend via HTTPS
      // ...
    });

### C++

    firebase::auth::User user = auth->current_user();
    if (user.is_valid()) {
      firebase::Future<std::string> idToken = user.GetToken(true);

      // Send token to your backend via HTTPS
      // ...
    }

### Web

    firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
      // Send token to your backend via HTTPS
      // ...
    }).catch(function(error) {
      // Handle error
    });

Once you have an ID token, you can send that[JSON Web Token (JWT)](https://www.jwt.io/introduction)to your backend and validate it using the Firebase Admin SDK, or using a third-party JWT library if your server is written in a language which Firebase does not natively support.

## Verify ID tokens using the Firebase Admin SDK

The Firebase Admin SDK has a built-in method for verifying and decoding ID tokens. If the provided ID token has the correct format, is not expired, and is properly signed, the method returns the decoded ID token. You can grab the`uid`of the user or device from the decoded token.
| **Note:** This does not check whether or not the token has been revoked. See:[Detect ID token revocation](https://firebase.google.com/docs/auth/admin/manage-sessions#detect_id_token_revocation).

Follow the[Admin SDK setup instructions](https://firebase.google.com/docs/admin/setup)to initialize the Admin SDK with a service account. Then, use the`verifyIdToken()`method to verify an ID token:  

### Node.js

    // idToken comes from the client app
    getAuth()
      .verifyIdToken(idToken)
      .then((decodedToken) => {
        const uid = decodedToken.uid;
        // ...
      })
      .catch((error) => {
        // Handle error
      });

### Java

    // idToken comes from the client app (shown above)
    FirebaseToken decodedToken = FirebaseAuth.getInstance().verifyIdToken(idToken);
    String uid = decodedToken.getUid();

### Python

    # id_token comes from the client app (shown above)

    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']

### Go

    client, err := app.Auth(ctx)
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }

    token, err := client.VerifyIDToken(ctx, idToken)
    if err != nil {
    	log.Fatalf("error verifying ID token: %v\n", err)
    }

    log.Printf("Verified ID token: %v\n", token)  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L82-L92

### C#

    FirebaseToken decodedToken = await FirebaseAuth.DefaultInstance
        .VerifyIdTokenAsync(idToken);
    string uid = decodedToken.Uid;

ID token verification requires a project ID. The Firebase Admin SDK attempts to obtain a project ID via one of the following methods:

- If the SDK was initialized with an explicit`projectId`app option, the SDK uses the value of that option.
- If the SDK was initialized with service account credentials, the SDK uses the`project_id`field of the service account JSON object.
- If the`GOOGLE_CLOUD_PROJECT`environment variable is set, the SDK uses its value as the project ID. This environment variable is available for code running on Google infrastructure such asApp EngineandCompute Engine.

## Verify ID tokens using a third-party JWT library

If your backend is in a language not supported by the Firebase Admin SDK, you can still verify ID tokens. First,[find a third-party JWT library for your language](https://jwt.io/). Then, verify the header, payload, and signature of the ID token.

Verify the ID token's header conforms to the following constraints:

|                                                                     ID Token Header Claims                                                                      |||
|-------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `alg` | Algorithm | `"RS256"`                                                                                                                                     |
| `kid` | Key ID    | Must correspond to one of the public keys listed at`https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com` |

Verify the ID token's payload conforms to the following constraints:

|                                                                            ID Token Payload Claims                                                                            |||
|-------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `exp`       | Expiration time     | Must be in the future. The time is measured in seconds since the UNIX epoch.                                                                |
| `iat`       | Issued-at time      | Must be in the past. The time is measured in seconds since the UNIX epoch.                                                                  |
| `aud`       | Audience            | Must be your Firebase project ID, the unique identifier for your Firebase project, which can be found in the URL of that project's console. |
| `iss`       | Issuer              | Must be`"https://securetoken.google.com/<projectId>"`, where`<projectId>`is the same project ID used for`aud`above.                         |
| `sub`       | Subject             | Must be a non-empty string and must be the`uid`of the user or device.                                                                       |
| `auth_time` | Authentication time | Must be in the past. The time when the user authenticated.                                                                                  |

Finally, ensure that the ID token was signed by the private key corresponding to the token's`kid`claim. Grab the public key from`https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com`and use a JWT library to verify the signature. Use the value of`max-age`in the`Cache-Control`header of the response from that endpoint to know when to refresh the public keys.

If all the above verifications are successful, you can use the subject (`sub`) of the ID token as the`uid`of the corresponding user or device.