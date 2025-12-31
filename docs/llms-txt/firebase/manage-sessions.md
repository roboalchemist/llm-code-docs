# Source: https://firebase.google.com/docs/auth/admin/manage-sessions.md.txt

<br />

Firebase Authenticationsessions are long lived. Every time a user signs in, the user credentials are sent to theFirebase Authenticationbackend and exchanged for a Firebase ID token (a JWT) and refresh token. Firebase ID tokens are short lived and last for an hour; the refresh token can be used to retrieve new ID tokens. Refresh tokens expire only when one of the following occurs:

- The user is deleted
- The user is disabled
- A major account change is detected for the user. This includes events like password or email address updates.

The Firebase Admin SDK provides the ability to revoke refresh tokens for a specified user. In addition, an API to check for ID token revocation is also made available. With these capabilities, you have more control over user sessions. The SDK provides the ability to add restrictions to prevent sessions from being used in suspicious circumstances, as well as a mechanism for recovery from potential token theft.

## Revoke refresh tokens

You might revoke a user's existing refresh token when a user reports a lost or stolen device. Similarly, if you discover a general vulnerability or suspect a wide-scale leak of active tokens, you can use the[`listUsers`](https://firebase.google.com/docs/auth/admin/manage-users#list_all_users)API to look up all users and revoke their tokens for the specified project.

Password resets also revoke a user's existing tokens; however, theFirebase Authenticationbackend handles the revocation automatically in that case. On revocation, the user is signed out and prompted to reauthenticate.

Here is an example implementation that uses the Admin SDK to revoke the refresh token of a given user. To initialize the Admin SDK follow the instructions on the[setup page](https://firebase.google.com/docs/admin/setup#initialize-sdk).  

### Node.js

    // Revoke all refresh tokens for a specified user for whatever reason.
    // Retrieve the timestamp of the revocation, in seconds since the epoch.
    getAuth()
      .revokeRefreshTokens(uid)
      .then(() => {
        return getAuth().getUser(uid);
      })
      .then((userRecord) => {
        return new Date(userRecord.tokensValidAfterTime).getTime() / 1000;
      })
      .then((timestamp) => {
        console.log(`Tokens revoked at: ${timestamp}`);
      });

### Java

    FirebaseAuth.getInstance().revokeRefreshTokens(uid);
    UserRecord user = FirebaseAuth.getInstance().getUser(uid);
    // Convert to seconds as the auth_time in the token claims is in seconds too.
    long revocationSecond = user.getTokensValidAfterTimestamp() / 1000;
    System.out.println("Tokens revoked at: " + revocationSecond);

### Python

    # Revoke tokens on the backend.
    auth.revoke_refresh_tokens(uid)
    user = auth.get_user(uid)
    # Convert to seconds as the auth_time in the token claims is in seconds.
    revocation_second = user.tokens_valid_after_timestamp / 1000
    print(f'Tokens revoked at: {revocation_second}')

### Go

    client, err := app.Auth(ctx)
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }
    if err := client.RevokeRefreshTokens(ctx, uid); err != nil {
    	log.Fatalf("error revoking tokens for user: %v, %v\n", uid, err)
    }
    // accessing the user's TokenValidAfter
    u, err := client.GetUser(ctx, uid)
    if err != nil {
    	log.Fatalf("error getting user %s: %v\n", uid, err)
    }
    timestamp := u.TokensValidAfterMillis / 1000
    log.Printf("the refresh tokens were revoked at: %d (UTC seconds) ", timestamp)  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L104-L117

### C#

    await FirebaseAuth.DefaultInstance.RevokeRefreshTokensAsync(uid);
    var user = await FirebaseAuth.DefaultInstance.GetUserAsync(uid);
    Console.WriteLine("Tokens revoked at: " + user.TokensValidAfterTimestamp);  
    https://github.com/firebase/firebase-admin-dotnet/blob/6cf4da307eb3803aca69a053023696c111e51426/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L601-L603

## Detect ID token revocation

Because Firebase ID tokens are stateless JWTs, you can determine a token has been revoked only by requesting the token's status from theFirebase Authenticationbackend. For this reason, performing this check on your server is an expensive operation, requiring an extra network round trip. You can avoid making this network request by setting upFirebase Security Rulesthat check for revocation rather than using the Admin SDK to make the check.

### Detect ID token revocation inFirebase Security Rules

To be able to detect the ID token revocation using Security Rules, we must first store some user-specific metadata.

#### Update user-specific metadata inFirebase Realtime Database.

Save the refresh token revocation timestamp. This is needed to track ID token revocation viaFirebase Security Rules. This allows for efficient checks within the database. In the code samples below, use the uid and the revocation time obtained in the[previous section](https://firebase.google.com/docs/auth/admin/manage-sessions#revoke_refresh_tokens).  

### Node.js

    const metadataRef = getDatabase().ref('metadata/' + uid);
    metadataRef.set({ revokeTime: utcRevocationTimeSecs }).then(() => {
      console.log('Database updated successfully.');
    });

### Java

    DatabaseReference ref = FirebaseDatabase.getInstance().getReference("metadata/" + uid);
    Map<String, Object> userData = new HashMap<>();
    userData.put("revokeTime", revocationSecond);
    ref.setValueAsync(userData);

### Python

    metadata_ref = firebase_admin.db.reference("metadata/" + uid)
    metadata_ref.set({'revokeTime': revocation_second})

#### Add a check toFirebase Security Rules

To enforce this check, set up a rule with no client write access to store the revocation time per user. This can be updated with the UTC timestamp of the last revocation time as shown in the previous examples:  

    {
      "rules": {
        "metadata": {
          "$user_id": {
            // this could be false as it is only accessed from backend or rules.
            ".read": "$user_id === auth.uid",
            ".write": "false",
          }
        }
      }
    }

Any data that requires authenticated access must have the following rule configured. This logic only allows authenticated users with unrevoked ID tokens to access the protected data:  

    {
      "rules": {
        "users": {
          "$user_id": {
            ".read": "auth != null && $user_id === auth.uid && (
                !root.child('metadata').child(auth.uid).child('revokeTime').exists()
              || auth.token.auth_time > root.child('metadata').child(auth.uid).child('revokeTime').val()
            )",
            ".write": "auth != null && $user_id === auth.uid && (
                !root.child('metadata').child(auth.uid).child('revokeTime').exists()
              || auth.token.auth_time > root.child('metadata').child(auth.uid).child('revokeTime').val()
            )",
          }
        }
      }
    }

### Detect ID token revocation in the SDK.

In your server, implement the following logic for refresh token revocation and ID token validation:

When a user's ID token is to be verified, the additional`checkRevoked`boolean flag has to be passed to`verifyIdToken`. If the user's token is revoked, the user should be signed out on the client or asked to reauthenticate using reauthentication APIs provided by theFirebase Authenticationclient SDKs.

To initialize the Admin SDK for your platform, follow the instructions on the[setup page](https://firebase.google.com/docs/admin/setup#initialize-sdk). Examples of retrieving the ID token are in the[`verifyIdToken`](https://firebase.google.com/docs/auth/admin/verify-id-tokens#retrieve_id_tokens_on_clients)section.  

### Node.js

    // Verify the ID token while checking if the token is revoked by passing
    // checkRevoked true.
    let checkRevoked = true;
    getAuth()
      .verifyIdToken(idToken, checkRevoked)
      .then((payload) => {
        // Token is valid.
      })
      .catch((error) => {
        if (error.code == 'auth/id-token-revoked') {
          // Token has been revoked. Inform the user to reauthenticate or signOut() the user.
        } else {
          // Token is invalid.
        }
      });

### Java

    try {
      // Verify the ID token while checking if the token is revoked by passing checkRevoked
      // as true.
      boolean checkRevoked = true;
      FirebaseToken decodedToken = FirebaseAuth.getInstance()
          .verifyIdToken(idToken, checkRevoked);
      // Token is valid and not revoked.
      String uid = decodedToken.getUid();
    } catch (FirebaseAuthException e) {
      if (e.getAuthErrorCode() == AuthErrorCode.REVOKED_ID_TOKEN) {
        // Token has been revoked. Inform the user to re-authenticate or signOut() the user.
      } else {
        // Token is invalid.
      }
    }

### Python

    try:
        # Verify the ID token while checking if the token is revoked by
        # passing check_revoked=True.
        decoded_token = auth.verify_id_token(id_token, check_revoked=True)
        # Token is valid and not revoked.
        uid = decoded_token['uid']
    except auth.RevokedIdTokenError:
        # Token revoked, inform the user to reauthenticate or signOut().
        pass
    except auth.UserDisabledError:
        # Token belongs to a disabled user record.
        pass
    except auth.InvalidIdTokenError:
        # Token is invalid
        pass

### Go

    client, err := app.Auth(ctx)
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }
    token, err := client.VerifyIDTokenAndCheckRevoked(ctx, idToken)
    if err != nil {
    	if err.Error() == "ID token has been revoked" {
    		// Token is revoked. Inform the user to reauthenticate or signOut() the user.
    	} else {
    		// Token is invalid
    	}
    }
    log.Printf("Verified ID token: %v\n", token)  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/auth.go#L123-L135

### C#

    try
    {
        // Verify the ID token while checking if the token is revoked by passing checkRevoked
        // as true.
        bool checkRevoked = true;
        var decodedToken = await FirebaseAuth.DefaultInstance.VerifyIdTokenAsync(
            idToken, checkRevoked);
        // Token is valid and not revoked.
        string uid = decodedToken.Uid;
    }
    catch (FirebaseAuthException ex)
    {
        if (ex.AuthErrorCode == AuthErrorCode.RevokedIdToken)
        {
            // Token has been revoked. Inform the user to re-authenticate or signOut() the user.
        }
        else
        {
            // Token is invalid.
        }
    }  
    https://github.com/firebase/firebase-admin-dotnet/blob/6cf4da307eb3803aca69a053023696c111e51426/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L610-L631

## Respond to token revocation on the client

If the token is revoked via the Admin SDK, the client is informed of the revocation and the user is expected to reauthenticate or is signed out:  

    function onIdTokenRevocation() {
      // For an email/password user. Prompt the user for the password again.
      let password = prompt('Please provide your password for reauthentication');
      let credential = firebase.auth.EmailAuthProvider.credential(
          firebase.auth().currentUser.email, password);
      firebase.auth().currentUser.reauthenticateWithCredential(credential)
        .then(result => {
          // User successfully reauthenticated. New ID tokens should be valid.
        })
        .catch(error => {
          // An error occurred.
        });
    }

## Advanced Security: Enforce IP address restrictions

A common security mechanism for detecting token theft is to keep track of request IP address origins. For example, if requests are always coming from the same IP address (server making the call), single IP address sessions can be enforced. Or, you might revoke a user's token if you detect that the user's IP address suddenly changed geolocation or you receive a request from a suspicious origin.

To perform security checks based on IP address, for every authenticated request inspect the ID token and check if the request's IP address matches previous trusted IP addresses or is within a trusted range before allowing access to restricted data. For example:  

    app.post('/getRestrictedData', (req, res) => {
      // Get the ID token passed.
      const idToken = req.body.idToken;
      // Verify the ID token, check if revoked and decode its payload.
      admin.auth().verifyIdToken(idToken, true).then((claims) => {
        // Get the user's previous IP addresses, previously saved.
        return getPreviousUserIpAddresses(claims.sub);
      }).then(previousIpAddresses => {
        // Get the request IP address.
        const requestIpAddress = req.connection.remoteAddress;
        // Check if the request IP address origin is suspicious relative to previous
        // IP addresses. The current request timestamp and the auth_time of the ID
        // token can provide additional signals of abuse especially if the IP address
        // suddenly changed. If there was a sudden location change in a
        // short period of time, then it will give stronger signals of possible abuse.
        if (!isValidIpAddress(previousIpAddresses, requestIpAddress)) {
          // Invalid IP address, take action quickly and revoke all user's refresh tokens.
          revokeUserTokens(claims.uid).then(() => {
            res.status(401).send({error: 'Unauthorized access. Please login again!'});
          }, error => {
            res.status(401).send({error: 'Unauthorized access. Please login again!'});
          });
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