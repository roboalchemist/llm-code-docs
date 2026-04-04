# Source: https://firebase.google.com/docs/auth/admin/create-custom-tokens.md.txt

<br />

Firebase gives you complete control over authentication by allowing you to authenticate users or devices using secure JSON Web Tokens (JWTs). You generate these tokens on your server, pass them back to a client device, and then use them to authenticate via the`signInWithCustomToken()`method.

To achieve this, you must create a server endpoint that accepts sign-in credentials---such as a username and password---and, if the credentials are valid, returns a custom JWT. The custom JWT returned from your server can then be used by a client device to authenticate with Firebase ([iOS+](https://firebase.google.com/docs/auth/ios/custom-auth),[Android](https://firebase.google.com/docs/auth/android/custom-auth),[web](https://firebase.google.com/docs/auth/web/custom-auth)). Once authenticated, this identity will be used when accessing other Firebase services, such as theFirebase Realtime DatabaseandCloud Storage. Furthermore, the contents of the JWT will be available in the`auth`object in your[Realtime DatabaseSecurity Rules](https://firebase.google.com/docs/database/security)and the`request.auth`object in your[Cloud StorageSecurity Rules](https://firebase.google.com/docs/storage/security).

You can create a custom token with the Firebase Admin SDK, or you can use a third-party JWT library if your server is written in a language which Firebase does not natively support.

## Before you begin

Custom tokens are signed JWTs where the private key used for signing belongs to a Google service account. There are several ways to specify the Google service account that should be used by the Firebase Admin SDK for signing custom tokens:

- [Using a service account JSON file](https://firebase.google.com/docs/auth/admin/create-custom-tokens#using_a_service_account_json_file)-- This method can be used in any environment, but requires you to package a service account JSON file along with your code. Special care must be taken to ensure that the service account JSON file is not exposed to external parties.
- [Letting the Admin SDK discover a service account](https://firebase.google.com/docs/auth/admin/create-custom-tokens#letting_the_admin_sdk_discover_a_service_account)-- This method can be used in environments managed by Google such as Google Cloud Functions andApp Engine. You may have to configure some additional permissions via theGoogle Cloudconsole.
- [Using a service account ID](https://firebase.google.com/docs/auth/admin/create-custom-tokens#using_a_service_account_id)-- When used in a Google-managed environment this method will sign tokens using the specified service account's key. However, it uses a remote web service, and you may have to configure additional permissions for this service account via theGoogle Cloudconsole.

### Using a service account JSON file

Service account JSON files contain all the information corresponding to service accounts (including the RSA private key). They can be downloaded from theFirebaseconsole. Follow the[Admin SDK set up instructions](https://firebase.google.com/docs/admin/setup#initialize-sdk)for more information on how to initialize the Admin SDK with a service account JSON file.

This method of initialization is suitable for a wide range of Admin SDK deployments. Also it enables the Admin SDK to create and sign custom tokens locally, without making any remote API calls. The main drawback of this approach is that it requires you to package a service account JSON file along with your code. Also note that the private key in a service account JSON file is sensitive information, and special care must be taken to keep it confidential. Specifically, refrain from adding service account JSON files to public version control.

### Letting the Admin SDK discover a service account

If your code is deployed in an environment managed by Google, the Admin SDK can attempt to auto-discover a means to sign custom tokens:

- If your code is deployed in theApp Enginestandard environment for Java, Python or Go, the Admin SDK can use the[App Identity service](https://cloud.google.com/appengine/docs/standard/java/appidentity/)present in that environment to sign custom tokens. The App Identity service signs data using a service account provisioned for your app by Google App Engine.

- If your code is deployed in some other managed environment (e.g. Google Cloud Functions, Google Compute Engine), the Firebase Admin SDK can auto-discover a service account ID string from the local[metadata server](https://cloud.google.com/compute/docs/storing-retrieving-metadata). The discovered service account ID is then used in conjunction with the IAM service to sign tokens remotely.

To make use of these signing methods, initialize the SDK with Google Application Default credentials and do not specify a service account ID string:  

### Node.js

    initializeApp();

### Java

    FirebaseApp.initializeApp();

### Python

    default_app = firebase_admin.initialize_app()

### Go

    app, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/init.go#L60-L63

### C#

    FirebaseApp.Create();

To test the same code locally, download a service account JSON file and set the`GOOGLE_APPLICATION_CREDENTIALS`environment variable to point to it.

If the Firebase Admin SDK has to discover a service account ID string, it does so when your code creates a custom token for the first time. The result is cached and reused for subsequent token signing operations. The auto-discovered service account ID is usually one of the default service accounts provided by theGoogle Cloud:

- [DefaultCompute Engineservice account](https://cloud.google.com/compute/docs/access/service-accounts#google-managed_service_accounts)
- [Default Cloud Functions service account](https://cloud.google.com/functions/docs/concepts/iam#runtime_service_account)

Just like with explicitly specified service account IDs, auto-discoverd service account IDs must have the`iam.serviceAccounts.signBlob`permission for the custom token creation to work. You may have to use the[IAM and admin](https://console.cloud.google.com/project/_/iam-admin)section of theGoogle Cloudconsole to grant the default service accounts the necessary permissions. See the troubleshooting section below for more details.

### Using a service account ID

To maintain consistency between various parts of your application, you can specify a service account ID whose keys will be used to sign tokens when running in a Google-managed environment. This can make IAM policies simpler and more secure, and avoid having to include the service account JSON file in your code.

The service account ID can be found in the[Google Cloudconsole](https://console.cloud.google.com/iam-admin/serviceaccounts?consoleUI=FIREBASE), or in the`client_email`field of a downloaded service account JSON file. Service account IDs are email addresses that have the following format:`<client-id>@<project-id>.iam.gserviceaccount.com`. They uniquely identify service accounts in Firebase andGoogle Cloudprojects.

To create custom tokens using a separate service account ID, initialize the SDK as shown below:  

### Node.js

    initializeApp({
      serviceAccountId: 'my-client-id@my-project-id.iam.gserviceaccount.com',
    });

### Java

    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.getApplicationDefault())
        .setServiceAccountId("my-client-id@my-project-id.iam.gserviceaccount.com")
        .build();
    FirebaseApp.initializeApp(options);

### Python

    options = {
        'serviceAccountId': 'my-client-id@my-project-id.iam.gserviceaccount.com',
    }
    firebase_admin.initialize_app(options=options)

### Go

    conf := &firebase.Config{
    	ServiceAccountID: "my-client-id@my-project-id.iam.gserviceaccount.com",
    }
    app, err := firebase.NewApp(context.Background(), conf)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }  
    https://github.com/firebase/firebase-admin-go/blob/da7068d6d46f07b69052c691949a7e65049df7a0/snippets/init.go#L71-L77

### C#

    FirebaseApp.Create(new AppOptions()
    {
        Credential = GoogleCredential.GetApplicationDefault(),
        ServiceAccountId = "my-client-id@my-project-id.iam.gserviceaccount.com",
    });

| **Note:** This setting will have no effect if you are[using a service account JSON file](https://firebase.google.com/docs/auth/admin/create-custom-tokens#using_a_service_account_json_file).

Service account IDs are not sensitive information and therefore their exposure is inconsequential. However, to sign custom tokens with the specified service account, the Firebase Admin SDK must invoke a remote service. Moreover, you must also make sure that the service account the Admin SDK is using to make this call ---usually`{project-name}@appspot.gserviceaccount.com`--- has the`iam.serviceAccounts.signBlob`[permission](https://cloud.google.com/iam/docs/overview#permissions). See the troubleshooting section below for more details.

## Create custom tokens using the Firebase Admin SDK

The Firebase Admin SDK has a built-in method for creating custom tokens. At a minimum, you need to provide a`uid`, which can be any string but should uniquely identify the user or device you are authenticating. These tokens expire after one hour.  

### Node.js

    const uid = 'some-uid';

    getAuth()
      .createCustomToken(uid)
      .then((customToken) => {
        // Send token back to client
      })
      .catch((error) => {
        console.log('Error creating custom token:', error);
      });

### Java

    String uid = "some-uid";

    String customToken = FirebaseAuth.getInstance().createCustomToken(uid);
    // Send token back to client

### Python

    uid = 'some-uid'

    custom_token = auth.create_custom_token(uid)  
    https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/auth/index.py#L107-L109

### Go

    client, err := app.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }

    token, err := client.CustomToken(ctx, "some-uid")
    if err != nil {
    	log.Fatalf("error minting custom token: %v\n", err)
    }

    log.Printf("Got custom token: %v\n", token)  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L38-L48

### C#

    var uid = "some-uid";

    string customToken = await FirebaseAuth.DefaultInstance.CreateCustomTokenAsync(uid);
    // Send token back to client

You can also optionally specify additional claims to be included in the custom token. For example, below, a`premiumAccount`field has been added to the custom token, which will be available in the`auth`/`request.auth`objects in your Security Rules:  

### Node.js

    const userId = 'some-uid';
    const additionalClaims = {
      premiumAccount: true,
    };

    getAuth()
      .createCustomToken(userId, additionalClaims)
      .then((customToken) => {
        // Send token back to client
      })
      .catch((error) => {
        console.log('Error creating custom token:', error);
      });

### Java

    String uid = "some-uid";
    Map<String, Object> additionalClaims = new HashMap<String, Object>();
    additionalClaims.put("premiumAccount", true);

    String customToken = FirebaseAuth.getInstance()
        .createCustomToken(uid, additionalClaims);
    // Send token back to client

### Python

    uid = 'some-uid'
    additional_claims = {
        'premiumAccount': True
    }

    custom_token = auth.create_custom_token(uid, additional_claims)  
    https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/auth/index.py#L118-L123

### Go

    client, err := app.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }

    claims := map[string]interface{}{
    	"premiumAccount": true,
    }

    token, err := client.CustomTokenWithClaims(ctx, "some-uid", claims)
    if err != nil {
    	log.Fatalf("error minting custom token: %v\n", err)
    }

    log.Printf("Got custom token: %v\n", token)  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L56-L70

### C#

    var uid = "some-uid";
    var additionalClaims = new Dictionary<string, object>()
    {
        { "premiumAccount", true },
    };

    string customToken = await FirebaseAuth.DefaultInstance
        .CreateCustomTokenAsync(uid, additionalClaims);
    // Send token back to client

### Reserved custom token names

| Firebase tokens comply with the OpenID Connect JWT spec, which means the following claims are reserved and cannot be specified within the additional claims:
|
| |-----------------------------|----------------------------------|-------------------------|---------------------|
| | `acr` `amr` `at_hash` `aud` | `auth_time` `azp` `cnf` `c_hash` | `exp` `iat` `iss` `jti` | `nbf` `nonce` `sub` |
|
| In addition, Firebase reserves the following claims:
|
| |------------|-----------|
| | `firebase` | `user_id` |
|
## Sign in using custom tokens on clients

After you create a custom token, you should send it to your client app. The client app authenticates with the custom token by calling`signInWithCustomToken()`:  

### iOS+

##### Objective-C

    [[FIRAuth auth] signInWithCustomToken:customToken
                               completion:^(FIRAuthDataResult * _Nullable authResult,
                                            NSError * _Nullable error) {
      // ...
    }];

##### Swift

    Auth.auth().signIn(withCustomToken: customToken ?? "") { user, error in
      // ...
    }

### Android

    mAuth.signInWithCustomToken(mCustomToken)
            .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if (task.isSuccessful()) {
                        // Sign in success, update UI with the signed-in user's information
                        Log.d(TAG, "signInWithCustomToken:success");
                        FirebaseUser user = mAuth.getCurrentUser();
                        updateUI(user);
                    } else {
                        // If sign in fails, display a message to the user.
                        Log.w(TAG, "signInWithCustomToken:failure", task.getException());
                        Toast.makeText(CustomAuthActivity.this, "Authentication failed.",
                                Toast.LENGTH_SHORT).show();
                        updateUI(null);
                    }
                }
            });

### Unity

    auth.SignInWithCustomTokenAsync(custom_token).ContinueWith(task => {
      if (task.IsCanceled) {
        Debug.LogError("SignInWithCustomTokenAsync was canceled.");
        return;
      }
      if (task.IsFaulted) {
        Debug.LogError("SignInWithCustomTokenAsync encountered an error: " + task.Exception);
        return;
      }

      Firebase.Auth.AuthResult result = task.Result;
      Debug.LogFormat("User signed in successfully: {0} ({1})",
          result.User.DisplayName, result.User.UserId);
    });

### C++

    firebase::Future<firebase::auth::AuthResult> result =
        auth->SignInWithCustomToken(custom_token);

### Web

    firebase.auth().signInWithCustomToken(token)
      .then((userCredential) => {
        // Signed in
        var user = userCredential.user;
        // ...
      })
      .catch((error) => {
        var errorCode = error.code;
        var errorMessage = error.message;
        // ...
      });  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/custom.js#L10-L20

### Web

    import { getAuth, signInWithCustomToken } from "firebase/auth";

    const auth = getAuth();
    signInWithCustomToken(auth, token)
      .then((userCredential) => {
        // Signed in
        const user = userCredential.user;
        // ...
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        // ...
      });  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/custom/auth_sign_in_custom.js#L8-L21

| **Note:** You can read more about this process on[iOS+](https://firebase.google.com/docs/auth/ios/custom-auth),[Android](https://firebase.google.com/docs/auth/android/custom-auth),[Unity](https://firebase.google.com/docs/auth/unity/custom-auth),[C++](https://firebase.google.com/docs/auth/cpp/custom-auth), and[web](https://firebase.google.com/docs/auth/web/custom-auth).

If the authentication succeeds, your user will be now signed in into your client app with the account specified by the`uid`included in the custom token. If that account did not previously exist, a record for that user will be created.

In the same way as with other sign-in methods (such as`signInWithEmailAndPassword()`and`signInWithCredential()`) the`auth`object in your[Realtime DatabaseSecurity Rules](https://firebase.google.com/docs/database/security)and the`request.auth`object in your[Cloud StorageSecurity Rules](https://firebase.google.com/docs/storage/security)will be populated with the user's`uid`. In this case, the`uid`will be the one that you specified when generating the custom token.  

### Database Rules

    {
      "rules": {
        "adminContent": {
          ".read": "auth.uid === 'some-uid'"
        }
      }
    }

### Storage Rules

    service firebase.storage {
      match /b/<your-firebase-storage-bucket>/o {
        match /adminContent/{filename} {
          allow read, write: if request.auth != null && request.auth.uid == "some-uid";
        }
      }
    }

If the custom token contains additional claims, they can be referenced off of the`auth.token`(Firebase Realtime Database) or`request.auth.token`(Cloud Storage) object in your rules:  

### Database Rules

    {
      "rules": {
        "premiumContent": {
          ".read": "auth.token.premiumAccount === true"
        }
      }
    }

### Storage Rules

    service firebase.storage {
      match /b/<your-firebase-storage-bucket>/o {
        match /premiumContent/{filename} {
          allow read, write: if request.auth.token.premiumAccount == true;
        }
      }
    }

## Create custom tokens using a third-party JWT library

If your backend is in a language that doesn't have an official Firebase Admin SDK, you can still manually create custom tokens. First,[find a third-party JWT library](https://jwt.io/)for your language. Then, use that JWT library to mint a JWT which includes the following claims:

|                                                                                                                                                                                                Custom Token Claims                                                                                                                                                                                                |||
|--------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `alg`              | Algorithm       | `"RS256"`                                                                                                                                                                                                                                                                                                                                                                    |
| `iss`              | Issuer          | Your project's service account email address                                                                                                                                                                                                                                                                                                                                 |
| `sub`              | Subject         | Your project's service account email address                                                                                                                                                                                                                                                                                                                                 |
| `aud`              | Audience        | `"https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit"`                                                                                                                                                                                                                                                                                |
| `iat`              | Issued-at time  | The current time, in seconds since the UNIX epoch                                                                                                                                                                                                                                                                                                                            |
| `exp`              | Expiration time | The time, in seconds since the UNIX epoch, at which the token expires. It can be a**maximum of 3600 seconds later** than the`iat`. Note: this only controls the time when the*custom token* itself expires. But once you sign a user in using`signInWithCustomToken()`, they will remain signed in into the device until their session is invalidated or the user signs out. |
| `uid`              |                 | The unique identifier of the signed-in user must be a string, between 1-128 characters long, inclusive. Shorter`uid`s offer better performance.                                                                                                                                                                                                                              |
| `claims`(optional) |                 | Optional custom claims to include in the Security Rules`auth`/`request.auth`variables                                                                                                                                                                                                                                                                                        |

Here are some example implementations of how to create custom tokens in a variety of languages that the Firebase Admin SDK does not support:  

### PHP

Using[`php-jwt`](https://github.com/firebase/php-jwt):  

    // Requires: composer require firebase/php-jwt
    use Firebase\JWT\JWT;

    // Get your service account's email address and private key from the JSON key file
    $service_account_email = "abc-123@a-b-c-123.iam.gserviceaccount.com";
    $private_key = "-----BEGIN PRIVATE KEY-----...";

    function create_custom_token($uid, $is_premium_account) {
      global $service_account_email, $private_key;

      $now_seconds = time();
      $payload = array(
        "iss" => $service_account_email,
        "sub" => $service_account_email,
        "aud" => "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
        "iat" => $now_seconds,
        "exp" => $now_seconds+(60*60),  // Maximum expiration time is one hour
        "uid" => $uid,
        "claims" => array(
          "premium_account" => $is_premium_account
        )
      );
      return JWT::encode($payload, $private_key, "RS256");
    }

### Ruby

Using[`ruby-jwt`](https://github.com/jwt/ruby-jwt):  

    require "jwt"

    # Get your service account's email address and private key from the JSON key file
    $service_account_email = "service-account@my-project-abc123.iam.gserviceaccount.com"
    $private_key = OpenSSL::PKey::RSA.new "-----BEGIN PRIVATE KEY-----\n..."

    def create_custom_token(uid, is_premium_account)
      now_seconds = Time.now.to_i
      payload = {:iss => $service_account_email,
                 :sub => $service_account_email,
                 :aud => "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
                 :iat => now_seconds,
                 :exp => now_seconds+(60*60), # Maximum expiration time is one hour
                 :uid => uid,
                 :claims => {:premium_account => is_premium_account}}
      JWT.encode payload, $private_key, "RS256"
    end

After you create the custom token, send it to your client app to use to authenticate with Firebase. See the code samples above for how to do this.

## Troubleshooting

This section outlines some common problems developers may encounter when creating custom tokens, and how to resolve them.

### IAM API not enabled

If you are specifying a service account ID for signing tokens you may get an error similar to the following:  

```
Identity and Access Management (IAM) API has not been used in project
1234567890 before or it is disabled. Enable it by visiting
https://console.developers.google.com/apis/api/iam.googleapis.com/overview?project=1234567890
then retry. If you enabled this API recently, wait a few minutes for the action
to propagate to our systems and retry.
```

The Firebase Admin SDK uses the[IAM API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/signBlob)to sign tokens. This error indicates that the IAM API is not currently enabled for your Firebase project. Open the link in the error message in a web browser, and click the "Enable API" button to enable it for your project.

### Service account does not have required permissions

If the service account the Firebase Admin SDK is running as does not have the`iam.serviceAccounts.signBlob`permission, you may get an error message like the following:  

```
Permission iam.serviceAccounts.signBlob is required to perform this operation
on service account projects/-/serviceAccounts/{your-service-account-id}.
```

The easiest way to resolve this is to grant the "Service Account Token Creator" IAM role to the service account in question, usually`{project-name}@appspot.gserviceaccount.com`:

1. Open the[IAM and admin](https://console.cloud.google.com/project/_/iam-admin)page in theGoogle Cloudconsole.
2. Select your project and click "Continue".
3. Click the edit icon corresponding to the service account you wish to update.
4. Click on "Add Another Role".
5. Type "Service Account Token Creator" into the search filter, and select it from the results.
6. Click "Save" to confirm the role grant.

Refer to[IAM documentation](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts)for more details on this process, or learn how to do update roles using the gcloud command-line tools.

### Failed to determine service account

If you get an error message similar to the following, the Firebase Admin SDK has not been properly initialized.  

```
Failed to determine service account ID. Initialize the SDK with service account
credentials or specify a service account ID with iam.serviceAccounts.signBlob
permission.
```

If you are relying on the SDK to auto-discover a service account ID, make sure the code is deployed in a managed Google environment with a metadata server. Otherwise, be sure to specify service account JSON file or service account ID at the SDK initialization.