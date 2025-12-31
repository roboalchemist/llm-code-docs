# Source: https://firebase.google.com/docs/auth/admin/manage-cookies.md.txt

<br />

Firebase Auth provides server-side session cookie management for traditional websites that rely on session cookies. This solution has several advantages over client-side short-lived ID tokens, which may require a redirect mechanism each time to update the session cookie on expiration:

- Improved security via JWT-based session tokens that can only be generated using authorized service accounts.
- Stateless session cookies that come with all the benefit of using JWTs for authentication. The session cookie has the same claims (including custom claims) as the ID token, making the same permissions checks enforceable on the session cookies.
- Ability to create session cookies with custom expiration times ranging from 5 minutes to 2 weeks.
- Flexibility to enforce cookie policies based on application requirements: domain, path, secure,`httpOnly`, etc.
- Ability to revoke session cookies when token theft is suspected using the existing refresh token revocation API.
- Ability to detect session revocation on major account changes.

## Sign in

Assuming an application is using`httpOnly`server side cookies, sign in a user on the login page using the client SDKs. A Firebase ID token is generated, and the ID token is then sent via HTTP POST to a session login endpoint where, using the Admin SDK, a session cookie is generated. On success, the state should be cleared from the client side storage.  

    firebase.initializeApp({
      apiKey: 'AIza...',
      authDomain: '<PROJECT_ID>.firebasepp.com'
    });

    // As httpOnly cookies are to be used, do not persist any state client side.
    firebase.auth().setPersistence(firebase.auth.Auth.Persistence.NONE);

    // When the user signs in with email and password.
    firebase.auth().signInWithEmailAndPassword('user@example.com', 'password').then(user => {
      // Get the user's ID token as it is needed to exchange for a session cookie.
      return user.getIdToken().then(idToken => {
        // Session login endpoint is queried and the session cookie is set.
        // CSRF protection should be taken into account.
        // ...
        const csrfToken = getCookie('csrfToken')
        return postIdTokenToSessionLogin('/sessionLogin', idToken, csrfToken);
      });
    }).then(() => {
      // A page redirect would suffice as the persistence is set to NONE.
      return firebase.auth().signOut();
    }).then(() => {
      window.location.assign('/profile');
    });

## Create session cookie

To generate a session cookie in exchange for the provided ID token, an HTTP endpoint is required. Send the token to the endpoint, setting a custom session duration time using the Firebase Admin SDK. Appropriate measures should be taken to prevent cross-site request forgery (CSRF) attacks.  

### Node.js

    app.post('/sessionLogin', (req, res) => {
      // Get the ID token passed and the CSRF token.
      const idToken = req.body.idToken.toString();
      const csrfToken = req.body.csrfToken.toString();
      // Guard against CSRF attacks.
      if (csrfToken !== req.cookies.csrfToken) {
        res.status(401).send('UNAUTHORIZED REQUEST!');
        return;
      }
      // Set session expiration to 5 days.
      const expiresIn = 60 * 60 * 24 * 5 * 1000;
      // Create the session cookie. This will also verify the ID token in the process.
      // The session cookie will have the same claims as the ID token.
      // To only allow session cookie setting on recent sign-in, auth_time in ID token
      // can be checked to ensure user was recently signed in before creating a session cookie.
      getAuth()
        .createSessionCookie(idToken, { expiresIn })
        .then(
          (sessionCookie) => {
            // Set cookie policy for session cookie.
            const options = { maxAge: expiresIn, httpOnly: true, secure: true };
            res.cookie('session', sessionCookie, options);
            res.end(JSON.stringify({ status: 'success' }));
          },
          (error) => {
            res.status(401).send('UNAUTHORIZED REQUEST!');
          }
        );
    });

### Java

    @POST
    @Path("/sessionLogin")
    @Consumes("application/json")
    public Response createSessionCookie(LoginRequest request) {
      // Get the ID token sent by the client
      String idToken = request.getIdToken();
      // Set session expiration to 5 days.
      long expiresIn = TimeUnit.DAYS.toMillis(5);
      SessionCookieOptions options = SessionCookieOptions.builder()
          .setExpiresIn(expiresIn)
          .build();
      try {
        // Create the session cookie. This will also verify the ID token in the process.
        // The session cookie will have the same claims as the ID token.
        String sessionCookie = FirebaseAuth.getInstance().createSessionCookie(idToken, options);
        // Set cookie policy parameters as required.
        NewCookie cookie = new NewCookie("session", sessionCookie /* ... other parameters */);
        return Response.ok().cookie(cookie).build();
      } catch (FirebaseAuthException e) {
        return Response.status(Status.UNAUTHORIZED).entity("Failed to create a session cookie")
            .build();
      }
    }

### Python

    @app.route('/sessionLogin', methods=['POST'])
    def session_login():
        # Get the ID token sent by the client
        id_token = flask.request.json['idToken']
        # Set session expiration to 5 days.
        expires_in = datetime.timedelta(days=5)
        try:
            # Create the session cookie. This will also verify the ID token in the process.
            # The session cookie will have the same claims as the ID token.
            session_cookie = auth.create_session_cookie(id_token, expires_in=expires_in)
            response = flask.jsonify({'status': 'success'})
            # Set cookie policy for session cookie.
            expires = datetime.datetime.now() + expires_in
            response.set_cookie(
                'session', session_cookie, expires=expires, httponly=True, secure=True)
            return response
        except exceptions.FirebaseError:
            return flask.abort(401, 'Failed to create a session cookie')

### Go

    return func(w http.ResponseWriter, r *http.Request) {
    	// Get the ID token sent by the client
    	defer r.Body.Close()
    	idToken, err := getIDTokenFromBody(r)
    	if err != nil {
    		http.Error(w, err.Error(), http.StatusBadRequest)
    		return
    	}

    	// Set session expiration to 5 days.
    	expiresIn := time.Hour * 24 * 5

    	// Create the session cookie. This will also verify the ID token in the process.
    	// The session cookie will have the same claims as the ID token.
    	// To only allow session cookie setting on recent sign-in, auth_time in ID token
    	// can be checked to ensure user was recently signed in before creating a session cookie.
    	cookie, err := client.SessionCookie(r.Context(), idToken, expiresIn)
    	if err != nil {
    		http.Error(w, "Failed to create a session cookie", http.StatusInternalServerError)
    		return
    	}

    	// Set cookie policy for session cookie.
    	http.SetCookie(w, &http.Cookie{
    		Name:     "session",
    		Value:    cookie,
    		MaxAge:   int(expiresIn.Seconds()),
    		HttpOnly: true,
    		Secure:   true,
    	})
    	w.Write([]byte(`{"status": "success"}`))
    }

### C#

    // POST: /sessionLogin
    [HttpPost]
    public async Task<ActionResult> Login([FromBody] LoginRequest request)
    {
        // Set session expiration to 5 days.
        var options = new SessionCookieOptions()
        {
            ExpiresIn = TimeSpan.FromDays(5),
        };

        try
        {
            // Create the session cookie. This will also verify the ID token in the process.
            // The session cookie will have the same claims as the ID token.
            var sessionCookie = await FirebaseAuth.DefaultInstance
                .CreateSessionCookieAsync(request.IdToken, options);

            // Set cookie policy parameters as required.
            var cookieOptions = new CookieOptions()
            {
                Expires = DateTimeOffset.UtcNow.Add(options.ExpiresIn),
                HttpOnly = true,
                Secure = true,
            };
            this.Response.Cookies.Append("session", sessionCookie, cookieOptions);
            return this.Ok();
        }
        catch (FirebaseAuthException)
        {
            return this.Unauthorized("Failed to create a session cookie");
        }
    }

For sensitive applications, the`auth_time`should be checked before issuing the session cookie, minimizing the window of attack in case an ID token is stolen:  

### Node.js

    getAuth()
      .verifyIdToken(idToken)
      .then((decodedIdToken) => {
        // Only process if the user just signed in in the last 5 minutes.
        if (new Date().getTime() / 1000 - decodedIdToken.auth_time < 5 * 60) {
          // Create session cookie and set it.
          return getAuth().createSessionCookie(idToken, { expiresIn });
        }
        // A user that was not recently signed in is trying to set a session cookie.
        // To guard against ID token theft, require re-authentication.
        res.status(401).send('Recent sign in required!');
      });

### Java

    // To ensure that cookies are set only on recently signed in users, check auth_time in
    // ID token before creating a cookie.
    FirebaseToken decodedToken = FirebaseAuth.getInstance().verifyIdToken(idToken);
    long authTimeMillis = TimeUnit.SECONDS.toMillis(
        (long) decodedToken.getClaims().get("auth_time"));

    // Only process if the user signed in within the last 5 minutes.
    if (System.currentTimeMillis() - authTimeMillis < TimeUnit.MINUTES.toMillis(5)) {
      long expiresIn = TimeUnit.DAYS.toMillis(5);
      SessionCookieOptions options = SessionCookieOptions.builder()
          .setExpiresIn(expiresIn)
          .build();
      String sessionCookie = FirebaseAuth.getInstance().createSessionCookie(idToken, options);
      // Set cookie policy parameters as required.
      NewCookie cookie = new NewCookie("session", sessionCookie);
      return Response.ok().cookie(cookie).build();
    }
    // User did not sign in recently. To guard against ID token theft, require
    // re-authentication.
    return Response.status(Status.UNAUTHORIZED).entity("Recent sign in required").build();

### Python

    # To ensure that cookies are set only on recently signed in users, check auth_time in
    # ID token before creating a cookie.
    try:
        decoded_claims = auth.verify_id_token(id_token)
        # Only process if the user signed in within the last 5 minutes.
        if time.time() - decoded_claims['auth_time'] < 5 * 60:
            expires_in = datetime.timedelta(days=5)
            expires = datetime.datetime.now() + expires_in
            session_cookie = auth.create_session_cookie(id_token, expires_in=expires_in)
            response = flask.jsonify({'status': 'success'})
            response.set_cookie(
                'session', session_cookie, expires=expires, httponly=True, secure=True)
            return response
        # User did not sign in recently. To guard against ID token theft, require
        # re-authentication.
        return flask.abort(401, 'Recent sign in required')
    except auth.InvalidIdTokenError:
        return flask.abort(401, 'Invalid ID token')
    except exceptions.FirebaseError:
        return flask.abort(401, 'Failed to create a session cookie')

### Go

    return func(w http.ResponseWriter, r *http.Request) {
    	// Get the ID token sent by the client
    	defer r.Body.Close()
    	idToken, err := getIDTokenFromBody(r)
    	if err != nil {
    		http.Error(w, err.Error(), http.StatusBadRequest)
    		return
    	}

    	decoded, err := client.VerifyIDToken(r.Context(), idToken)
    	if err != nil {
    		http.Error(w, "Invalid ID token", http.StatusUnauthorized)
    		return
    	}
    	// Return error if the sign-in is older than 5 minutes.
    	if time.Now().Unix()-decoded.Claims["auth_time"].(int64) > 5*60 {
    		http.Error(w, "Recent sign-in required", http.StatusUnauthorized)
    		return
    	}

    	expiresIn := time.Hour * 24 * 5
    	cookie, err := client.SessionCookie(r.Context(), idToken, expiresIn)
    	if err != nil {
    		http.Error(w, "Failed to create a session cookie", http.StatusInternalServerError)
    		return
    	}
    	http.SetCookie(w, &http.Cookie{
    		Name:     "session",
    		Value:    cookie,
    		MaxAge:   int(expiresIn.Seconds()),
    		HttpOnly: true,
    		Secure:   true,
    	})
    	w.Write([]byte(`{"status": "success"}`))
    }

### C#

    // To ensure that cookies are set only on recently signed in users, check auth_time in
    // ID token before creating a cookie.
    var decodedToken = await FirebaseAuth.DefaultInstance.VerifyIdTokenAsync(idToken);
    var authTime = new DateTime(1970, 1, 1).AddSeconds(
        (long)decodedToken.Claims["auth_time"]);

    // Only process if the user signed in within the last 5 minutes.
    if (DateTime.UtcNow - authTime < TimeSpan.FromMinutes(5))
    {
        var options = new SessionCookieOptions()
        {
            ExpiresIn = TimeSpan.FromDays(5),
        };
        var sessionCookie = await FirebaseAuth.DefaultInstance.CreateSessionCookieAsync(
            idToken, options);
        // Set cookie policy parameters as required.
        this.Response.Cookies.Append("session", sessionCookie);
        return this.Ok();
    }

    // User did not sign in recently. To guard against ID token theft, require
    // re-authentication.
    return this.Unauthorized("Recent sign in required");

## Verify session cookie and check permissions

After sign-in, all access-protected sections of the website should check the session cookie and verify it before serving restricted content based on some security rule.  

### Node.js

    // Whenever a user is accessing restricted content that requires authentication.
    app.post('/profile', (req, res) => {
      const sessionCookie = req.cookies.session || '';
      // Verify the session cookie. In this case an additional check is added to detect
      // if the user's Firebase session was revoked, user deleted/disabled, etc.
      getAuth()
        .verifySessionCookie(sessionCookie, true /** checkRevoked */)
        .then((decodedClaims) => {
          serveContentForUser('/profile', req, res, decodedClaims);
        })
        .catch((error) => {
          // Session cookie is unavailable or invalid. Force user to login.
          res.redirect('/login');
        });
    });

### Java

    @POST
    @Path("/profile")
    public Response verifySessionCookie(@CookieParam("session") Cookie cookie) {
      String sessionCookie = cookie.getValue();
      try {
        // Verify the session cookie. In this case an additional check is added to detect
        // if the user's Firebase session was revoked, user deleted/disabled, etc.
        final boolean checkRevoked = true;
        FirebaseToken decodedToken = FirebaseAuth.getInstance().verifySessionCookie(
            sessionCookie, checkRevoked);
        return serveContentForUser(decodedToken);
      } catch (FirebaseAuthException e) {
        // Session cookie is unavailable, invalid or revoked. Force user to login.
        return Response.temporaryRedirect(URI.create("/login")).build();
      }
    }

### Python

    @app.route('/profile', methods=['POST'])
    def access_restricted_content():
        session_cookie = flask.request.cookies.get('session')
        if not session_cookie:
            # Session cookie is unavailable. Force user to login.
            return flask.redirect('/login')

        # Verify the session cookie. In this case an additional check is added to detect
        # if the user's Firebase session was revoked, user deleted/disabled, etc.
        try:
            decoded_claims = auth.verify_session_cookie(session_cookie, check_revoked=True)
            return serve_content_for_user(decoded_claims)
        except auth.InvalidSessionCookieError:
            # Session cookie is invalid, expired or revoked. Force user to login.
            return flask.redirect('/login')

### Go

    return func(w http.ResponseWriter, r *http.Request) {
    	// Get the ID token sent by the client
    	cookie, err := r.Cookie("session")
    	if err != nil {
    		// Session cookie is unavailable. Force user to login.
    		http.Redirect(w, r, "/login", http.StatusFound)
    		return
    	}

    	// Verify the session cookie. In this case an additional check is added to detect
    	// if the user's Firebase session was revoked, user deleted/disabled, etc.
    	decoded, err := client.VerifySessionCookieAndCheckRevoked(r.Context(), cookie.Value)
    	if err != nil {
    		// Session cookie is invalid. Force user to login.
    		http.Redirect(w, r, "/login", http.StatusFound)
    		return
    	}

    	serveContentForUser(w, r, decoded)
    }

### C#

    // POST: /profile
    [HttpPost]
    public async Task<ActionResult> Profile()
    {
        var sessionCookie = this.Request.Cookies["session"];
        if (string.IsNullOrEmpty(sessionCookie))
        {
            // Session cookie is not available. Force user to login.
            return this.Redirect("/login");
        }

        try
        {
            // Verify the session cookie. In this case an additional check is added to detect
            // if the user's Firebase session was revoked, user deleted/disabled, etc.
            var checkRevoked = true;
            var decodedToken = await FirebaseAuth.DefaultInstance.VerifySessionCookieAsync(
                sessionCookie, checkRevoked);
            return ViewContentForUser(decodedToken);
        }
        catch (FirebaseAuthException)
        {
            // Session cookie is invalid or revoked. Force user to login.
            return this.Redirect("/login");
        }
    }

Verify session cookies using the Admin SDK*verifySessionCookie*API. This is a low overhead operation. The public certificates are initially queried and cached until they expire. Session cookie verification can be done with the cached public certificates without any additional network requests.

If the cookie is invalid, make sure it is cleared, and ask the user to sign in again. An additional option is available to check for session revocation. Note that this adds an additional network request each time a session cookie is verified.

For security reasons, Firebase session cookies cannot be used with other Firebase services due to their custom validity period, which can be set to the maximum duration of 2 weeks. All applications using server side cookies are expected to enforce permissions checks after verifying these cookies server side.  

### Node.js

    getAuth()
      .verifySessionCookie(sessionCookie, true)
      .then((decodedClaims) => {
        // Check custom claims to confirm user is an admin.
        if (decodedClaims.admin === true) {
          return serveContentForAdmin('/admin', req, res, decodedClaims);
        }
        res.status(401).send('UNAUTHORIZED REQUEST!');
      })
      .catch((error) => {
        // Session cookie is unavailable or invalid. Force user to login.
        res.redirect('/login');
      });

### Java

    try {
      final boolean checkRevoked = true;
      FirebaseToken decodedToken = FirebaseAuth.getInstance().verifySessionCookie(
          sessionCookie, checkRevoked);
      if (Boolean.TRUE.equals(decodedToken.getClaims().get("admin"))) {
        return serveContentForAdmin(decodedToken);
      }
      return Response.status(Status.UNAUTHORIZED).entity("Insufficient permissions").build();
    } catch (FirebaseAuthException e) {
      // Session cookie is unavailable, invalid or revoked. Force user to login.
      return Response.temporaryRedirect(URI.create("/login")).build();
    }

### Python

    try:
        decoded_claims = auth.verify_session_cookie(session_cookie, check_revoked=True)
        # Check custom claims to confirm user is an admin.
        if decoded_claims.get('admin') is True:
            return serve_content_for_admin(decoded_claims)

        return flask.abort(401, 'Insufficient permissions')
    except auth.InvalidSessionCookieError:
        # Session cookie is invalid, expired or revoked. Force user to login.
        return flask.redirect('/login')

### Go

    return func(w http.ResponseWriter, r *http.Request) {
    	cookie, err := r.Cookie("session")
    	if err != nil {
    		// Session cookie is unavailable. Force user to login.
    		http.Redirect(w, r, "/login", http.StatusFound)
    		return
    	}

    	decoded, err := client.VerifySessionCookieAndCheckRevoked(r.Context(), cookie.Value)
    	if err != nil {
    		// Session cookie is invalid. Force user to login.
    		http.Redirect(w, r, "/login", http.StatusFound)
    		return
    	}

    	// Check custom claims to confirm user is an admin.
    	if decoded.Claims["admin"] != true {
    		http.Error(w, "Insufficient permissions", http.StatusUnauthorized)
    		return
    	}

    	serveContentForAdmin(w, r, decoded)
    }

### C#

    try
    {
        var checkRevoked = true;
        var decodedToken = await FirebaseAuth.DefaultInstance.VerifySessionCookieAsync(
            sessionCookie, checkRevoked);
        object isAdmin;
        if (decodedToken.Claims.TryGetValue("admin", out isAdmin) && (bool)isAdmin)
        {
            return ViewContentForAdmin(decodedToken);
        }

        return this.Unauthorized("Insufficient permissions");
    }
    catch (FirebaseAuthException)
    {
        // Session cookie is invalid or revoked. Force user to login.
        return this.Redirect("/login");
    }

| Session cookie verification requires the Admin SDK to be initialized with a project ID. This happens automatically when you initialize the SDK with a service account credential. Alternatively, the project ID can be set as a Firebase app option or specified via the`GCLOUD_PROJECT`environment variable.

## Sign out

When a user signs out from the client side, handle it on the server side via an endpoint. A POST/GET request should result in the session cookie being cleared. Note that even though the cookie is cleared, it remains active until its natural expiration.  

### Node.js

    app.post('/sessionLogout', (req, res) => {
      res.clearCookie('session');
      res.redirect('/login');
    });

### Java

    @POST
    @Path("/sessionLogout")
    public Response clearSessionCookie(@CookieParam("session") Cookie cookie) {
      final int maxAge = 0;
      NewCookie newCookie = new NewCookie(cookie, null, maxAge, true);
      return Response.temporaryRedirect(URI.create("/login")).cookie(newCookie).build();
    }

### Python

    @app.route('/sessionLogout', methods=['POST'])
    def session_logout():
        response = flask.make_response(flask.redirect('/login'))
        response.set_cookie('session', expires=0)
        return response

### Go

    return func(w http.ResponseWriter, r *http.Request) {
    	http.SetCookie(w, &http.Cookie{
    		Name:   "session",
    		Value:  "",
    		MaxAge: 0,
    	})
    	http.Redirect(w, r, "/login", http.StatusFound)
    }

### C#

    // POST: /sessionLogout
    [HttpPost]
    public ActionResult ClearSessionCookie()
    {
        this.Response.Cookies.Delete("session");
        return this.Redirect("/login");
    }

Calling the revocation API revokes the session and also revokes all the user's other sessions, forcing new login. For sensitive applications, a shorter session duration is advised.  

### Node.js

    app.post('/sessionLogout', (req, res) => {
      const sessionCookie = req.cookies.session || '';
      res.clearCookie('session');
      getAuth()
        .verifySessionCookie(sessionCookie)
        .then((decodedClaims) => {
          return getAuth().revokeRefreshTokens(decodedClaims.sub);
        })
        .then(() => {
          res.redirect('/login');
        })
        .catch((error) => {
          res.redirect('/login');
        });
    });

### Java

    @POST
    @Path("/sessionLogout")
    public Response clearSessionCookieAndRevoke(@CookieParam("session") Cookie cookie) {
      String sessionCookie = cookie.getValue();
      try {
        FirebaseToken decodedToken = FirebaseAuth.getInstance().verifySessionCookie(sessionCookie);
        FirebaseAuth.getInstance().revokeRefreshTokens(decodedToken.getUid());
        final int maxAge = 0;
        NewCookie newCookie = new NewCookie(cookie, null, maxAge, true);
        return Response.temporaryRedirect(URI.create("/login")).cookie(newCookie).build();
      } catch (FirebaseAuthException e) {
        return Response.temporaryRedirect(URI.create("/login")).build();
      }
    }

### Python

    @app.route('/sessionLogout', methods=['POST'])
    def session_logout():
        session_cookie = flask.request.cookies.get('session')
        try:
            decoded_claims = auth.verify_session_cookie(session_cookie)
            auth.revoke_refresh_tokens(decoded_claims['sub'])
            response = flask.make_response(flask.redirect('/login'))
            response.set_cookie('session', expires=0)
            return response
        except auth.InvalidSessionCookieError:
            return flask.redirect('/login')

### Go

    return func(w http.ResponseWriter, r *http.Request) {
    	cookie, err := r.Cookie("session")
    	if err != nil {
    		// Session cookie is unavailable. Force user to login.
    		http.Redirect(w, r, "/login", http.StatusFound)
    		return
    	}

    	decoded, err := client.VerifySessionCookie(r.Context(), cookie.Value)
    	if err != nil {
    		// Session cookie is invalid. Force user to login.
    		http.Redirect(w, r, "/login", http.StatusFound)
    		return
    	}
    	if err := client.RevokeRefreshTokens(r.Context(), decoded.UID); err != nil {
    		http.Error(w, "Failed to revoke refresh token", http.StatusInternalServerError)
    		return
    	}

    	http.SetCookie(w, &http.Cookie{
    		Name:   "session",
    		Value:  "",
    		MaxAge: 0,
    	})
    	http.Redirect(w, r, "/login", http.StatusFound)
    }

### C#

    // POST: /sessionLogout
    [HttpPost]
    public async Task<ActionResult> ClearSessionCookieAndRevoke()
    {
        var sessionCookie = this.Request.Cookies["session"];
        try
        {
            var decodedToken = await FirebaseAuth.DefaultInstance
                .VerifySessionCookieAsync(sessionCookie);
            await FirebaseAuth.DefaultInstance.RevokeRefreshTokensAsync(decodedToken.Uid);
            this.Response.Cookies.Delete("session");
            return this.Redirect("/login");
        }
        catch (FirebaseAuthException)
        {
            return this.Redirect("/login");
        }
    }

## Verify session cookies using a third-party JWT library

If your backend is in a language not supported by the Firebase Admin SDK, you can still verify session cookies. First,[find a third-party JWT library for your language](https://jwt.io/). Then, verify the header, payload, and signature of the session cookie.

Verify that the session cookie's header conforms to the following constraints:

|                                                    Firebase Session Cookie Header Claims                                                     |||
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------|
| `alg` | Algorithm | `"RS256"`                                                                                                                  |
| `kid` | Key ID    | Must correspond to one of the public keys listed at`https://www.googleapis.com/identitytoolkit/v3/relyingparty/publicKeys` |

Verify the session cookie's payload conforms to the following constraints:

|                                                                                 Firebase Session Cookie Payload Claims                                                                                 |||
|-------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `exp`       | Expiration time     | Must be in the future. The time is measured in seconds since the UNIX epoch. The expiration is set based on the custom duration provided when the cookie is created. |
| `iat`       | Issued-at time      | Must be in the past. The time is measured in seconds since the UNIX epoch.                                                                                           |
| `aud`       | Audience            | Must be your Firebase project ID, the unique identifier for your Firebase project, which can be found in the URL of that project's console.                          |
| `iss`       | Issuer              | Must be`"https://session.firebase.google.com/<projectId>"`", where`<projectId>`is the same project ID used for`aud`above.                                            |
| `sub`       | Subject             | Must be a non-empty string and must be the`uid`of the user or device.                                                                                                |
| `auth_time` | Authentication time | Must be in the past. The time when the user authenticated. This matches the`auth_time`of the ID token used to create the session cookie.                             |

Finally, ensure that the session cookie was signed by the private key corresponding to the token's kid claim. Get the public key from`https://www.googleapis.com/identitytoolkit/v3/relyingparty/publicKeys`and use a JWT library to verify the signature. Use the value of max-age in the`Cache-Control`header of the response from that endpoint to determine when to refresh the public keys.

If all the above verifications are successful, you can use the subject (`sub`) of the session cookie as the uid of the corresponding user or device.