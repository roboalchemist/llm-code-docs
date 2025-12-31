# Source: https://firebase.google.com/docs/app-check/custom-resource-backend.md.txt

You can useApp Checkto protect non-Google custom backend resources for your app, like your own self-hosted backend. To do so, you'll need to do both of the following:

- Modify your app client to send anApp Checktoken along with each request to your backend, as described on the pages for[iOS+](https://firebase.google.com/docs/app-check/ios/custom-resource),[Android](https://firebase.google.com/docs/app-check/android/custom-resource),[web](https://firebase.google.com/docs/app-check/web/custom-resource),[Flutter](https://firebase.google.com/docs/app-check/flutter/custom-resource),[Unity](https://firebase.google.com/docs/app-check/unity/custom-resource), or[C++](https://firebase.google.com/docs/app-check/cpp/custom-resource).
- Modify your backend to require a validApp Checktoken with every request, as described on this page.

## Token verification

To verifyApp Checktokens on your backend, add logic to your API endpoints that does the following:

- Check that each request include anApp Checktoken.

- Verify theApp Checktoken using the Admin SDK.

  If verification succeeds, the Admin SDK returns the decodedApp Checktoken. Successful verification indicates the token originated from an app belonging to your Firebase project.

Reject any request that fails either check. For example:  

### Node.js

If you haven't already installed the[Node.js Admin SDK](https://firebase.google.com/docs/admin/setup), do so.

Then, using Express.js middleware as an example:  

    import express from "express";
    import { initializeApp } from "firebase-admin/app";
    import { getAppCheck } from "firebase-admin/app-check";

    const expressApp = express();
    const firebaseApp = initializeApp();

    const appCheckVerification = async (req, res, next) => {
        const appCheckToken = req.header("X-Firebase-AppCheck");

        if (!appCheckToken) {
            res.status(401);
            return next("Unauthorized");
        }

        try {
            const appCheckClaims = await getAppCheck().verifyToken(appCheckToken);

            // If verifyToken() succeeds, continue with the next middleware
            // function in the stack.
            return next();
        } catch (err) {
            res.status(401);
            return next("Unauthorized");
        }
    }

    expressApp.get("/yourApiEndpoint", [appCheckVerification], (req, res) => {
        // Handle request.
    });

### Python

If you haven't already installed the[Python Admin SDK](https://firebase.google.com/docs/admin/setup), do so.

Then, in your API endpoint handlers, call`app_check.verify_token()`and reject the request if it fails. In the following example, a function decorated with`@before_request`performs this task for all requests:  

    import firebase_admin
    from firebase_admin import app_check
    import flask
    import jwt

    firebase_app = firebase_admin.initialize_app()
    flask_app = flask.Flask(__name__)

    @flask_app.before_request
    def verify_app_check() -> None:
        app_check_token = flask.request.headers.get("X-Firebase-AppCheck", default="")
        try:
            app_check_claims = app_check.verify_token(app_check_token)
            # If verify_token() succeeds, okay to continue to route handler.
        except (ValueError, jwt.exceptions.DecodeError):
            flask.abort(401)

    @flask_app.route("/yourApiEndpoint")
    def your_api_endpoint(request: flask.Request):
        # Handle request.
        ...

### Go

If you haven't already installed the[Admin SDK for Go](https://firebase.google.com/docs/admin/setup), do so.

Then, in your API endpoint handlers, call`appcheck.Client.VerifyToken()`and reject the request if it fails. In the following example, a wrapper function adds this logic to the endpoint handlers:  

    package main

    import (
        "context"
        "log"
        "net/http"

        firebaseAdmin "firebase.google.com/go/v4"
        "firebase.google.com/go/v4/appcheck"
    )

    var (
        appCheck *appcheck.Client
    )

    func main() {
        app, err := firebaseAdmin.NewApp(context.Background(), nil)
        if err != nil {
            log.Fatalf("error initializing app: %v\n", err)
        }

        appCheck, err = app.AppCheck(context.Background())
        if err != nil {
            log.Fatalf("error initializing app: %v\n", err)
        }

        http.HandleFunc("/yourApiEndpoint", requireAppCheck(yourApiEndpointHandler))
        log.Fatal(http.ListenAndServe(":8080", nil))
    }

    func requireAppCheck(handler func(http.ResponseWriter, *http.Request)) func(http.ResponseWriter, *http.Request) {
        wrappedHandler := func(w http.ResponseWriter, r *http.Request) {
            appCheckToken, ok := r.Header[http.CanonicalHeaderKey("X-Firebase-AppCheck")]
            if !ok {
                w.WriteHeader(http.StatusUnauthorized)
                w.Write([]byte("Unauthorized."))
                return
            }

            _, err := appCheck.VerifyToken(appCheckToken[0])
            if err != nil {
                w.WriteHeader(http.StatusUnauthorized)
                w.Write([]byte("Unauthorized."))
                return
            }

            // If VerifyToken() succeeds, continue with the provided handler.
            handler(w, r)
        }
        return wrappedHandler
    }

    func yourApiEndpointHandler(w http.ResponseWriter, r *http.Request) {
        // Handle request.
    }

### Other

If your backend is written in another language, you can use a general-purpose JWT library, such as one found at[jwt.io](https://jwt.io/libraries), to verify App Check tokens.

Your token verification logic must complete the following steps:

1. Obtain the Firebase App Check public JSON Web Key (JWK) Set from the App Check JWKS endpoint:`https://firebaseappcheck.googleapis.com/v1/jwks`
2. Verify the App Check token's signature to ensure it is legitimate.
3. Ensure that the token's header uses the algorithm RS256.
4. Ensure that the token's header has type JWT.
5. Ensure that the token is issued by Firebase App Check under your project.
6. Ensure that the token has not expired.
7. Ensure that the token's audience matches your project.
8. **Optional**: Check that the token's subject matches your app's App ID.

The capabilities of JWT libraries can differ; be sure to manually complete any steps not handled by the library you choose.

The following example performs the necessary steps in Ruby using the`jwt`gem as a Rack middleware layer.  

    require 'json'
    require 'jwt'
    require 'net/http'
    require 'uri'

    class AppCheckVerification
    def initialize(app, options = {})
        @app = app
        @project_number = options[:project_number]
    end

    def call(env)
        app_id = verify(env['HTTP_X_FIREBASE_APPCHECK'])
        return [401, { 'Content-Type' => 'text/plain' }, ['Unauthenticated']] unless app_id
        env['firebase.app'] = app_id
        @app.call(env)
    end

    def verify(token)
        return unless token

        # 1. Obtain the Firebase App Check Public Keys
        # Note: It is not recommended to hard code these keys as they rotate,
        # but you should cache them for up to 6 hours.
        uri = URI('https://firebaseappcheck.googleapis.com/v1/jwks')
        jwks = JSON(Net::HTTP.get(uri))

        # 2. Verify the signature on the App Check token
        payload, header = JWT.decode(token, nil, true, jwks: jwks, algorithms: 'RS256')

        # 3. Ensure the token's header uses the algorithm RS256
        return unless header['alg'] == 'RS256'

        # 4. Ensure the token's header has type JWT
        return unless header['typ'] == 'JWT'

        # 5. Ensure the token is issued by App Check
        return unless payload['iss'] == "https://firebaseappcheck.googleapis.com/#{@project_number}"

        # 6. Ensure the token is not expired
        return unless payload['exp'] > Time.new.to_i

        # 7. Ensure the token's audience matches your project
        return unless payload['aud'].include? "projects/#{@project_number}"

        # 8. The token's subject will be the app ID, you may optionally filter against
        # an allow list
        payload['sub']
    rescue
    end
    end

    class Application
    def call(env)
        [200, { 'Content-Type' => 'text/plain' }, ["Hello app #{env['firebase.app']}"]]
    end
    end

    use AppCheckVerification, project_number: 1234567890
    run Application.new

## Replay protection (beta)

To protect an endpoint from replay attacks, you can consume the App Check token after verifying it so that it can be used only once.
| **Note:** The replay protection beta supports only the Node.js SDK.

Using replay protection adds a network round trip to the`verifyToken()`call, and therefore adds latency to any endpoint that uses it. For this reason, we recommend that you enable replay protection only on particularly sensitive endpoints.

To use replay protection, do the following:

1. In the[Cloud console](https://console.cloud.google.com/iam-admin/iam?project=_), grant the "Firebase App Check Token Verifier" role to the service account used to verify tokens.

   - If you initialized the Admin SDK with the Admin SDK service account credentials you downloaded from the Firebase console, the required role is already granted.
   - If you're using 1st generation Cloud Functions with the default Admin SDK configuration, grant the role to the**App Engine default service account** . See[Changing service account permissions](https://cloud.google.com/appengine/docs/legacy/standard/python/service-account#modifying_the_default_service_account).
   - If you're using 2nd generation Cloud Functions with the default Admin SDK configuration, grant the role to the**Default compute service account**.
2. Then, to consume a token, pass`{ consume: true }`to the`verifyToken()`method and examine the result object; if the`alreadyConsumed`property is`true`, reject the request or take some kind of corrective action, such as requiring the caller to pass other checks.

   For example:  

       const appCheckClaims = await getAppCheck().verifyToken(appCheckToken, { consume: true });

       if (appCheckClaims.alreadyConsumed) {
           res.status(401);
           return next('Unauthorized');
       }

       // If verifyToken() succeeds and alreadyConsumed is not set, okay to continue.

   This verifies the token and then flags it as consumed. Future invocations of`verifyToken(appCheckToken, { consume: true })`on the same token will set`alreadyConsumed`to`true`. (Note that`verifyToken()`does not reject a consumed token or even check if it's consumed if`consume`is not set.)

When you enable this feature for a particular endpoint, you must also update your app client code to acquire consumable limited-use tokens for use with the endpoint. See the client-side docs for[Apple platforms](https://firebase.google.com/docs/app-check/ios/custom-resource#replay-protection),[Android](https://firebase.google.com/docs/app-check/android/custom-resource#replay-protection), and[web](https://firebase.google.com/docs/app-check/web/custom-resource#replay-protection).