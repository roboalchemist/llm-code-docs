# Source: https://firebase.google.com/docs/auth/admin/custom-claims.md.txt

<br />

The Firebase Admin SDK supports defining custom attributes on user accounts. This provides the ability to implement various access control strategies, including role-based access control, in Firebase apps. These custom attributes can give users different levels of access (roles), which are enforced in an application's security rules.

User roles can be defined for the following common cases:

- Giving a user administrative privileges to access data and resources.
- Defining different groups that a user belongs to.
- Providing multi-level access:
  - Differentiating paid/unpaid subscribers.
  - Differentiating moderators from regular users.
  - Teacher/student application, etc.
- Add an additional identifier on a user. For example, a Firebase user could map to a different UID in another system.

Let's consider a case where you want to limit access to the database node "adminContent." You could do that with a database lookup on a list of admin users. However, you can achieve the same objective more efficiently using a custom user claim named`admin`with the followingRealtime Databaserule:  

    {
      "rules": {
        "adminContent": {
          ".read": "auth.token.admin === true",
          ".write": "auth.token.admin === true",
        }
      }
    }

Custom user claims are accessible via user's authentication tokens. In the above example, only users with`admin`set to true in their token claim would have read/write access to`adminContent`node. As the ID token already contains these assertions, no additional processing or lookup is needed to check for admin permissions. In addition, the ID token is a trusted mechanism for delivering these custom claims. All authenticated access must validate the ID token before processing the associated request.
| **Note:** Though they are related, do not confuse custom user claims with*custom authentication*. Custom authentication is generally used when using a different authentication system with Firebase services, or to augment Firebase Auth with providers that are not supported out of the box. Custom claims apply to users already signed in with supported providers (Email/Password, Google, Facebook, phone, etc). For example, a user signed in with Firebase Auth's Email/Password provider can have access control defined using custom claims.

The code examples and solutions described in this page draw from both the client-side Firebase Auth APIs and the server-side Auth APIs provided by the[Admin SDK](https://firebase.google.com/docs/reference/admin).

## Set and validate custom user claims via the Admin SDK

Custom claims can contain sensitive data, therefore they should only be set from a privileged server environment by the Firebase Admin SDK.  

### Node.js

    // Set admin privilege on the user corresponding to uid.

    getAuth()
      .setCustomUserClaims(uid, { admin: true })
      .then(() => {
        // The new custom claims will propagate to the user's ID token the
        // next time a new one is issued.
      });

### Java

    // Set admin privilege on the user corresponding to uid.
    Map<String, Object> claims = new HashMap<>();
    claims.put("admin", true);
    FirebaseAuth.getInstance().setCustomUserClaims(uid, claims);
    // The new custom claims will propagate to the user's ID token the
    // next time a new one is issued.

### Python

    # Set admin privilege on the user corresponding to uid.
    auth.set_custom_user_claims(uid, {'admin': True})
    # The new custom claims will propagate to the user's ID token the
    # next time a new one is issued.

### Go

    // Get an auth client from the firebase.App
    client, err := app.Auth(ctx)
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }

    // Set admin privilege on the user corresponding to uid.
    claims := map[string]interface{}{"admin": true}
    err = client.SetCustomUserClaims(ctx, uid, claims)
    if err != nil {
    	log.Fatalf("error setting custom claims %v\n", err)
    }
    // The new custom claims will propagate to the user's ID token the
    // next time a new one is issued.  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L295-L308

### C#

    // Set admin privileges on the user corresponding to uid.
    var claims = new Dictionary<string, object>()
    {
        { "admin", true },
    };
    await FirebaseAuth.DefaultInstance.SetCustomUserClaimsAsync(uid, claims);
    // The new custom claims will propagate to the user's ID token the
    // next time a new one is issued.

| **Note:** this operation always overwrites the user's existing custom claims. However, if the same custom user claims are defined on a user signed in via[custom authentication](https://firebase.google.com/docs/auth/admin/create-custom-tokens), the overlapping claims defined in the custom token have higher priority and always overwrite the custom user claims defined on a user via this API.  
| For example, calling`setCustomUserClaims(uid, {foo: 'bar', key1: 'value1'})`and signing in the user with the custom token`createCustomToken(uid, {foo: 'overwrite', key2: 'value2'})`results in the following claims on the user`{foo: 'overwrite', key2: 'value2', key1: 'value1'})`.

The custom claims object should not contain any[OIDC](http://openid.net/specs/openid-connect-core-1_0.html#IDToken)reserved key names or[Firebase reserved names](https://firebase.google.com/docs/auth/admin/create-custom-tokens#reserved_custom_token_names). The payload must not exceed 1000 bytes. Custom claims must be JSON-serializable. Supported types include strings, numbers, booleans, arrays, objects, and null. Unsupported types such as Date, undefined, functions, or other non-JSON values will cause errors.

An ID token sent to a backend server can confirm the user's identity and access level using the Admin SDK as follows:  

### Node.js

    // Verify the ID token first.
    getAuth()
      .verifyIdToken(idToken)
      .then((claims) => {
        if (claims.admin === true) {
          // Allow access to requested admin resource.
        }
      });

### Java

    // Verify the ID token first.
    FirebaseToken decoded = FirebaseAuth.getInstance().verifyIdToken(idToken);
    if (Boolean.TRUE.equals(decoded.getClaims().get("admin"))) {
      // Allow access to requested admin resource.
    }

### Python

    # Verify the ID token first.
    claims = auth.verify_id_token(id_token)
    if claims['admin'] is True:
        # Allow access to requested admin resource.
        pass

### Go

    // Verify the ID token first.
    token, err := client.VerifyIDToken(ctx, idToken)
    if err != nil {
    	log.Fatal(err)
    }

    claims := token.Claims
    if admin, ok := claims["admin"]; ok {
    	if admin.(bool) {
    		//Allow access to requested admin resource.
    	}
    }  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L316-L327

### C#

    // Verify the ID token first.
    FirebaseToken decoded = await FirebaseAuth.DefaultInstance.VerifyIdTokenAsync(idToken);
    object isAdmin;
    if (decoded.Claims.TryGetValue("admin", out isAdmin))
    {
        if ((bool)isAdmin)
        {
            // Allow access to requested admin resource.
        }
    }

You can also check a user's existing custom claims, which are available as a property on the user object:  

### Node.js

    // Lookup the user associated with the specified uid.
    getAuth()
      .getUser(uid)
      .then((userRecord) => {
        // The claims can be accessed on the user record.
        console.log(userRecord.customClaims['admin']);
      });

### Java

    // Lookup the user associated with the specified uid.
    UserRecord user = FirebaseAuth.getInstance().getUser(uid);
    System.out.println(user.getCustomClaims().get("admin"));

### Python

    # Lookup the user associated with the specified uid.
    user = auth.get_user(uid)
    # The claims can be accessed on the user record.
    print(user.custom_claims.get('admin'))

### Go

    // Lookup the user associated with the specified uid.
    user, err := client.GetUser(ctx, uid)
    if err != nil {
    	log.Fatal(err)
    }
    // The claims can be accessed on the user record.
    if admin, ok := user.CustomClaims["admin"]; ok {
    	if admin.(bool) {
    		log.Println(admin)
    	}
    }  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L334-L344

### C#

    // Lookup the user associated with the specified uid.
    UserRecord user = await FirebaseAuth.DefaultInstance.GetUserAsync(uid);
    Console.WriteLine(user.CustomClaims["admin"]);

You can delete a user's custom claims by passing null for`customClaims`.

## Propagate custom claims to the client

After new claims are modified on a user via the Admin SDK, they are propagated to an authenticated user on the client side via the ID token in the following ways:

- A user signs in or re-authenticates after the custom claims are modified. The ID token issued as a result will contain the latest claims.
- An existing user session gets its ID token refreshed after an older token expires.
- An ID token is force refreshed by calling`currentUser.getIdToken(true)`.

## Access custom claims on the client

Custom claims can only be retrieved through the user's ID token. Access to these claims may be necessary to modify the client UI based on the user's role or access level. However, backend access should always be enforced through the ID token after validating it and parsing its claims. Custom claims should not be sent directly to the backend, as they can't be trusted outside of the token.

Once the latest claims have propagated to a user's ID token, you can get them by retrieving the ID token:  

### JavaScript

    firebase.auth().currentUser.getIdTokenResult()
      .then((idTokenResult) => {
         // Confirm the user is an Admin.
         if (!!idTokenResult.claims.admin) {
           // Show admin UI.
           showAdminUI();
         } else {
           // Show regular user UI.
           showRegularUI();
         }
      })
      .catch((error) => {
        console.log(error);
      });

### Android

    user.getIdToken(false).addOnSuccessListener(new OnSuccessListener<GetTokenResult>() {
      @Override
      public void onSuccess(GetTokenResult result) {
        boolean isAdmin = result.getClaims().get("admin");
        if (isAdmin) {
          // Show admin UI.
          showAdminUI();
        } else {
          // Show regular user UI.
          showRegularUI();
        }
      }
    });

### Swift

    user.getIDTokenResult(completion: { (result, error) in
      guard let admin = result?.claims?["admin"] as? NSNumber else {
        // Show regular user UI.
        showRegularUI()
        return
      }
      if admin.boolValue {
        // Show admin UI.
        showAdminUI()
      } else {
        // Show regular user UI.
        showRegularUI()
      }
    })

### Objective-C

    user.getIDTokenResultWithCompletion:^(FIRAuthTokenResult *result,
                                          NSError *error) {
      if (error != nil) {
        BOOL *admin = [result.claims[@"admin"] boolValue];
        if (admin) {
          // Show admin UI.
          [self showAdminUI];
        } else {
          // Show regular user UI.
          [self showRegularUI];
        }
      }
    }];

## Best practices for custom claims

Custom claims are only used to provide access control. They are not designed to store additional data (such as profile and other custom data). While this may seem like a convenient mechanism to do so, it is strongly discouraged as these claims are stored in the ID token and could cause performance issues because all authenticated requests always contain a Firebase ID token corresponding to the signed in user.

- Use custom claims to store data for controlling user access only. All other data should be stored separately via the real-time database or other server side storage.
- Custom claims are limited in size. Passing a custom claims payload greater than 1000 bytes will throw an error.

## Examples and use cases

The following examples illustrate custom claims in context of specific Firebase use cases.

### Defining roles via Firebase Functions on user creation

In this example, custom claims are set on a user on creation usingCloud Functions.

Custom claims can be added usingCloud Functions, and propagated immediately withRealtime Database. The function is called only on signup using an`onCreate`trigger. Once the custom claims are set, they propagate to all existing and future sessions. The next time the user signs in with the user credential, the token contains the custom claims.

#### Client side implementation (JavaScript)

    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
    .catch(error => {
      console.log(error);
    });

    let callback = null;
    let metadataRef = null;
    firebase.auth().onAuthStateChanged(user => {
      // Remove previous listener.
      if (callback) {
        metadataRef.off('value', callback);
      }
      // On user login add new listener.
      if (user) {
        // Check if refresh is required.
        metadataRef = firebase.database().ref('metadata/' + user.uid + '/refreshTime');
        callback = (snapshot) => {
          // Force refresh to pick up the latest custom claims changes.
          // Note this is always triggered on first call. Further optimization could be
          // added to avoid the initial trigger when the token is issued and already contains
          // the latest claims.
          user.getIdToken(true);
        };
        // Subscribe new listener to changes on that node.
        metadataRef.on('value', callback);
      }
    });

#### Cloud Functionslogic

A new database node (metadata/($uid)} with read/write restricted to the authenticated user is added.  

    const functions = require('firebase-functions');
    const { initializeApp } = require('firebase-admin/app');
    const { getAuth } = require('firebase-admin/auth');
    const { getDatabase } = require('firebase-admin/database');

    initializeApp();

    // On sign up.
    exports.processSignUp = functions.auth.user().onCreate(async (user) => {
      // Check if user meets role criteria.
      if (
        user.email &&
        user.email.endsWith('@admin.example.com') &&
        user.emailVerified
      ) {
        const customClaims = {
          admin: true,
          accessLevel: 9
        };

        try {
          // Set custom user claims on this newly created user.
          await getAuth().setCustomUserClaims(user.uid, customClaims);

          // Update real-time database to notify client to force refresh.
          const metadataRef = getDatabase().ref('metadata/' + user.uid);

          // Set the refresh time to the current UTC timestamp.
          // This will be captured on the client to force a token refresh.
          await  metadataRef.set({refreshTime: new Date().getTime()});
        } catch (error) {
          console.log(error);
        }
      }
    });

#### Database rules

    {
      "rules": {
        "metadata": {
          "$user_id": {
            // Read access only granted to the authenticated user.
            ".read": "$user_id === auth.uid",
            // Write access only via Admin SDK.
            ".write": false
          }
        }
      }
    }

### Defining roles via an HTTP request

The following example sets custom user claims on a newly signed in user via an HTTP request.

#### Client side implementation (JavaScript)

    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
    .then((result) => {
      // User is signed in. Get the ID token.
      return result.user.getIdToken();
    })
    .then((idToken) => {
      // Pass the ID token to the server.
      $.post(
        '/setCustomClaims',
        {
          idToken: idToken
        },
        (data, status) => {
          // This is not required. You could just wait until the token is expired
          // and it proactively refreshes.
          if (status == 'success' && data) {
            const json = JSON.parse(data);
            if (json && json.status == 'success') {
              // Force token refresh. The token claims will contain the additional claims.
              firebase.auth().currentUser.getIdToken(true);
            }
          }
        });
    }).catch((error) => {
      console.log(error);
    });

#### Backend implementation (Admin SDK)

    app.post('/setCustomClaims', async (req, res) => {
      // Get the ID token passed.
      const idToken = req.body.idToken;

      // Verify the ID token and decode its payload.
      const claims = await getAuth().verifyIdToken(idToken);

      // Verify user is eligible for additional privileges.
      if (
        typeof claims.email !== 'undefined' &&
        typeof claims.email_verified !== 'undefined' &&
        claims.email_verified &&
        claims.email.endsWith('@admin.example.com')
      ) {
        // Add custom claims for additional privileges.
        await getAuth().setCustomUserClaims(claims.sub, {
          admin: true
        });

        // Tell client to refresh token on user.
        res.end(JSON.stringify({
          status: 'success'
        }));
      } else {
        // Return nothing.
        res.end(JSON.stringify({ status: 'ineligible' }));
      }
    });

The same flow can be used when upgrading an existing user's access level. Take for example a free user upgrading to a paid subscription. The user's ID token is sent with the payment information to the backend server via an HTTP request. When the payment is successfully processed, the user is set as a paid subscriber via the Admin SDK. A successful HTTP response is returned to the client to force token refresh.

### Defining roles via backend script

A recurring script (not initiated from the client) could be set to run to update user custom claims:  

### Node.js

    getAuth()
      .getUserByEmail('user@admin.example.com')
      .then((user) => {
        // Confirm user is verified.
        if (user.emailVerified) {
          // Add custom claims for additional privileges.
          // This will be picked up by the user on token refresh or next sign in on new device.
          return getAuth().setCustomUserClaims(user.uid, {
            admin: true,
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });

### Java

    UserRecord user = FirebaseAuth.getInstance()
        .getUserByEmail("user@admin.example.com");
    // Confirm user is verified.
    if (user.isEmailVerified()) {
      Map<String, Object> claims = new HashMap<>();
      claims.put("admin", true);
      FirebaseAuth.getInstance().setCustomUserClaims(user.getUid(), claims);
    }

### Python

    user = auth.get_user_by_email('user@admin.example.com')
    # Confirm user is verified
    if user.email_verified:
        # Add custom claims for additional privileges.
        # This will be picked up by the user on token refresh or next sign in on new device.
        auth.set_custom_user_claims(user.uid, {
            'admin': True
        })

### Go

    user, err := client.GetUserByEmail(ctx, "user@admin.example.com")
    if err != nil {
    	log.Fatal(err)
    }
    // Confirm user is verified
    if user.EmailVerified {
    	// Add custom claims for additional privileges.
    	// This will be picked up by the user on token refresh or next sign in on new device.
    	err := client.SetCustomUserClaims(ctx, user.UID, map[string]interface{}{"admin": true})
    	if err != nil {
    		log.Fatalf("error setting custom claims %v\n", err)
    	}

    }  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L350-L363

### C#

    UserRecord user = await FirebaseAuth.DefaultInstance
        .GetUserByEmailAsync("user@admin.example.com");
    // Confirm user is verified.
    if (user.EmailVerified)
    {
        var claims = new Dictionary<string, object>()
        {
            { "admin", true },
        };
        await FirebaseAuth.DefaultInstance.SetCustomUserClaimsAsync(user.Uid, claims);
    }

Custom claims can also be modified incrementally via the Admin SDK:  

### Node.js

    getAuth()
      .getUserByEmail('user@admin.example.com')
      .then((user) => {
        // Add incremental custom claim without overwriting existing claims.
        const currentCustomClaims = user.customClaims;
        if (currentCustomClaims['admin']) {
          // Add level.
          currentCustomClaims['accessLevel'] = 10;
          // Add custom claims for additional privileges.
          return getAuth().setCustomUserClaims(user.uid, currentCustomClaims);
        }
      })
      .catch((error) => {
        console.log(error);
      });

### Java

    UserRecord user = FirebaseAuth.getInstance()
        .getUserByEmail("user@admin.example.com");
    // Add incremental custom claim without overwriting the existing claims.
    Map<String, Object> currentClaims = user.getCustomClaims();
    if (Boolean.TRUE.equals(currentClaims.get("admin"))) {
      // Add level.
      currentClaims.put("level", 10);
      // Add custom claims for additional privileges.
      FirebaseAuth.getInstance().setCustomUserClaims(user.getUid(), currentClaims);
    }

### Python

    user = auth.get_user_by_email('user@admin.example.com')
    # Add incremental custom claim without overwriting existing claims.
    current_custom_claims = user.custom_claims
    if current_custom_claims.get('admin'):
        # Add level.
        current_custom_claims['accessLevel'] = 10
        # Add custom claims for additional privileges.
        auth.set_custom_user_claims(user.uid, current_custom_claims)

### Go

    user, err := client.GetUserByEmail(ctx, "user@admin.example.com")
    if err != nil {
    	log.Fatal(err)
    }
    // Add incremental custom claim without overwriting existing claims.
    currentCustomClaims := user.CustomClaims
    if currentCustomClaims == nil {
    	currentCustomClaims = map[string]interface{}{}
    }

    if _, found := currentCustomClaims["admin"]; found {
    	// Add level.
    	currentCustomClaims["accessLevel"] = 10
    	// Add custom claims for additional privileges.
    	err := client.SetCustomUserClaims(ctx, user.UID, currentCustomClaims)
    	if err != nil {
    		log.Fatalf("error setting custom claims %v\n", err)
    	}

    }  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L369-L388

### C#

    UserRecord user = await FirebaseAuth.DefaultInstance
        .GetUserByEmailAsync("user@admin.example.com");
    // Add incremental custom claims without overwriting the existing claims.
    object isAdmin;
    if (user.CustomClaims.TryGetValue("admin", out isAdmin) && (bool)isAdmin)
    {
        var claims = user.CustomClaims.ToDictionary(kvp => kvp.Key, kvp => kvp.Value);
        // Add level.
        var level = 10;
        claims["level"] = level;
        // Add custom claims for additional privileges.
        await FirebaseAuth.DefaultInstance.SetCustomUserClaimsAsync(user.Uid, claims);
    }