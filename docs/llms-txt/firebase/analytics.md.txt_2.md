# Source: https://firebase.google.com/docs/reference/dynamic-links/analytics.md.txt

You can use this REST API to get analytics data for each of your short Dynamic Links,
whether [created in the console or programmatically](https://firebase.google.com/docs/dynamic-links/create-links).

## API Authorization

When you make requests to the Dynamic Link Analytics APIs, you must include an OAuth
2.0 access token that authorizes access to your Firebase project.

You can get access tokens using a Google API client library:

1. [Add Firebase to your app](https://firebase.google.com/docs/admin/setup#prerequisites) as described in the Admin SDK setup guide. That is, create a service account and generate a private key.
2. Use a Google API client library to get an access token from your service account credentials:

   #### Java

   Using the
   [Google API Client Library for Java](https://developers.google.com/api-client-library/java/):

   ```java
   // Load the service account key JSON file
   FileInputStream serviceAccount = new FileInputStream("path/to/serviceAccountKey.json");

   // Authenticate a Google credential with the service account
   GoogleCredential googleCred = GoogleCredential.fromStream(serviceAccount);

   // Add the required scope to the Google credential
   GoogleCredential scoped = googleCred.createScoped(
       Arrays.asList(
         "https://www.googleapis.com/auth/firebase"
       )
   );

   // Use the Google credential to generate an access token
   scoped.refreshToken();
   String token = scoped.getAccessToken();

   // Include the access token in the Authorization header.
   ```

   #### Node.js

   Using the
   [Google API Client Library for Node.js](https://github.com/google/google-api-nodejs-client/):

   ```javascript
   var { google } = require("googleapis");

   // Load the service account key JSON file.
   var serviceAccount = require("path/to/serviceAccountKey.json");

   // Specify the required scope.
   var scopes = [
     "https://www.googleapis.com/auth/firebase"
   ];

   // Authenticate a JWT client with the service account.
   var jwtClient = new google.auth.JWT(
     serviceAccount.client_email,
     null,
     serviceAccount.private_key,
     scopes
   );

   // Use the JWT client to generate an access token.
   jwtClient.authorize(function(error, tokens) {
     if (error) {
       console.log("Error making request to generate access token:", error);
     } else if (tokens.access_token === null) {
       console.log("Provided service account does not have permission to generate access tokens");
     } else {
       var accessToken = tokens.access_token;

       // Include the access token in the Authorization header.
     }
   });
   ```

   #### Python

   Using the [Google Auth](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth) library for Python:

   ```python
   from google.oauth2 import service_account
   from google.auth.transport.requests import AuthorizedSession

   # Specify the required scope
   scopes = [
     "https://www.googleapis.com/auth/firebase"
   ]

   # Authenticate a credential with the service account
   credentials = service_account.Credentials.from_service_account_file(
       "path/to/serviceAccountKey.json", scopes=scopes)

   # Use the credentials object to authenticate a Requests session.
   authed_session = AuthorizedSession(credentials)
   response = authed_session.get(
       "https://firebasedynamiclinks.googleapis.com/v1/SHORT_DYNAMIC_LINK/linkStats?durationDays=DURATION")

   # Or, use the token directly, as described below.
   request = google.auth.transport.requests.Request()
   credentials.refresh(request)
   access_token = credentials.token
   ```

> [!WARNING]
> **Warning:** Use extra caution when handling service account credentials in your code. Do not commit them to a public repository, deploy them in a client app, or expose them in any way that could compromise the security of your Firebase project.

## Get statistics for a single Dynamic Link

Use the `linkStats` endpoint to get event statistics for a single Dynamic Link.

### HTTP request

A `linkStats` request has the following format:

```
GET https://firebasedynamiclinks.googleapis.com/v1/SHORT_DYNAMIC_LINK/linkStats?durationDays=DURATION

Authorization: Bearer ACCESS_TOKEN
```

For example, to retrieve statistics from the last 7 days for the short link
`https://example.page.link/wXYz`:

```
GET https://firebasedynamiclinks.googleapis.com/v1/https%3A%2F%2Fexample.page.link%2FwXYz/linkStats?durationDays=7

Authorization: Bearer ya29.Abc123...
```

| Parameters ||
|---|---|
| <var translate="no">SHORT_DYNAMIC_LINK</var> | The [URL-encoded](https://developer.mozilla.org/docs/Glossary/percent-encoding) short Dynamic Link for which you want to get event data. |
| <var translate="no">DURATION</var> | The number of days for which to get event data. For example, if you specify `30`, the request retrieves data for the past 30 days. Note that some events logged in the last 36 hours might not be included. |
| <var translate="no">ACCESS_TOKEN</var> | An unexpired access token. See [API Authorization](https://firebase.google.com/docs/reference/dynamic-links/analytics#api_authorization). |

### Response body

The response to a request is a JSON object like the following:

    {
      "linkEventStats": [
        {
          "platform": "ANDROID",
          "count": "123",
          "event": "CLICK"
        },
        {
          "platform": "IOS",
          "count": "123",
          "event": "CLICK"
        },
        {
          "platform": "DESKTOP",
          "count": "456",
          "event": "CLICK"
        },
        {
          "platform": "ANDROID",
          "count": "99",
          "event": "APP_INSTALL"
        },
        {
          "platform": "ANDROID",
          "count": "42",
          "event": "APP_FIRST_OPEN"
        },

        ...

      ]
    }

Each item in the `linkEventStats` list contains a platform-specific count of
some Dynamic Link related event (such as the number of clicks on Android). Note that
these statistics might not include events that have been logged within the last
36 hours.

| Event | Description | Firebase console | REST API |
|---|---|---|---|
| CLICK | Count of any click on a Dynamic Link, irrespective to how it is handled and its destinations | Yes | Yes |
| REDIRECT | Count of attempts to redirect users, either to the App Store or Play Store to install or update the app, or to some other destination |   | Yes |
| APP_INSTALL | Count of actual installs (only supported by the Play Store) |   | Yes |
| APP_FIRST_OPEN | Count of first-opens after an install | Yes | Yes |
| APP_RE_OPEN | Number of times the Dynamic Link caused an app to be re-opened | Yes | Yes |