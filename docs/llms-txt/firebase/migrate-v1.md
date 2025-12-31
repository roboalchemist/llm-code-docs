# Source: https://firebase.google.com/docs/cloud-messaging/migrate-v1.md.txt

<br />

Apps using the deprecated FCM legacy APIs for HTTP and XMPP should migrate to the HTTP v1 API at the earliest opportunity. Sending messages (including upstream messages) with those APIs was deprecated on June 20, 2023, and**[shutdown begins on July 22, 2024](https://firebase.google.com/support/faq#deprecated-api-shutdown)**.

Learn more about the specific[features that are affected](https://firebase.google.com/support/faq#fcm-depr-service).

In addition to ongoing support and new features, the HTTP v1 API has these advantages over the legacy APIs:

- **Better security via access tokens**The HTTP v1 API uses short-lived access tokens according to the OAuth2 security model. In the event that an access token becomes public, it can only be maliciously used for an hour or so before it expires. Refresh tokens are not transmitted as often as the security keys used in the legacy API, so they are much less likely to be captured.

- **More efficient customization of messages across platforms**For the message body, the HTTP v1 API has common keys that go to all targeted instances, plus platform-specific keys that let you customize the message across platforms. This allows you to create "overrides" that send slightly different payloads to different client platforms in a single message.

- **More extendable and future-proof for new client platform versions** The HTTP v1 API fully supports messaging options available on Apple platforms, Android and Web. Since each platform has its own defined block in the JSON payload,FCMcan extend the API to new versions and new platforms as needed.

## Update the server endpoint

The endpoint URL for the HTTP v1 API differs from the legacy endpoint in these ways:

- It is versioned, with`/v1`in the path.
- The path contains the project ID of the Firebase project for your app, in the format`/projects/myproject-ID/`. This ID is available in the[General project settings](https://console.cloud.google.com/project/_/settings/general/)tab of theFirebaseconsole.
- It explicitly specifies the specify the[`send`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send)method as`:send`.

To update the server endpoint for HTTP v1, add these elements to the endpoint in the header of your send requests.

#### HTTP requests before

    POST https://fcm.googleapis.com/fcm/send

#### XMPP requests before

Legacy XMPP messages are sent over a connection to the following endpoint:  

    fcm-xmpp.googleapis.com:5235

#### After

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send

| **Note:** In typical migration paths, theFCMv1 API should be enabled by default. If you experience errors contacting the endpoint, double check that the "Firebase Cloud MessagingAPI" is enabled in the list of APIs and services in the[Google Cloudconsole](https://console.developers.google.com/apis/dashboard?project=_).

## Update authorization of send requests

In place of the server key string used in legacy requests, HTTP v1 send requests require an OAuth 2.0 access token. If you are using the Admin SDK to send messages, the library handles the token for you. If you are using raw protocol, obtain the token as described in this section and add it to the header as`Authorization: Bearer <valid Oauth 2.0 token>`.
| **Caution:** As with the legacy APIs, HTTP v1 messages**must be sent through a trusted environment** such as your app server or[Cloud Functions for Firebase](https://firebase.google.com/docs/functions)using the HTTP protocol or the Admin SDK to build message requests. Sending directly from client app logic carries extreme security risk and is not supported.

#### Before

    Authorization: key=AIzaSyZ-1u...0GBYzPu7Udno5aA

#### After

    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA

Depending on the details of your server environment, use a combination of these strategies to authorize server requests to Firebase services:

- Google Application Default Credentials (ADC)
- A service account JSON file
- A short-lived OAuth 2.0 access token derived from a service account

**If your application is running onCompute Engine,Google Kubernetes Engine,App Engine, or Cloud Functions** (includingCloud Functions for Firebase), use Application Default Credentials (ADC). ADC uses your existing default service account to obtain credentials to authorize requests, and ADC enables flexible local testing via the environment variable<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>. For the fullest automation of the authorization flow, use ADC together with Admin SDK server libraries.

**If your application is running on a non-Google server environment** , you'll need to download a service account JSON file from your Firebase project. As long as you have access to a file system containing the private key file, you can use the environment variable<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>to authorize requests with these manually obtained credentials. If you lack such file access, you must reference the service account file in your code--- which should be done with extreme care due to the risk of exposing your credentials.

### Provide credentials using ADC

Google Application Default Credentials (ADC) checks for your credentials in the following order:

1. ADC checks whether the environment variable<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>is set. If the variable is set, ADC uses the service account file that the variable points to.

2. If the environment variable isn't set, ADC uses the default service account thatCompute Engine,Google Kubernetes Engine,App Engine, and Cloud Functions provide for applications that run on those services.

3. If ADC can't use either of the above credentials, the system throws an error.

The following Admin SDK code example illustrates this strategy. The example doesn't explicitly specify the application credentials. However, ADC is able to implicitly find the credentials as long as the environment variable is set, or as long as the application is running onCompute Engine,Google Kubernetes Engine,App Engine, or Cloud Functions.  

### Node.js

    admin.initializeApp({
      credential: admin.credential.applicationDefault(),
    });

### Java

    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.getApplicationDefault())
        .setDatabaseUrl("https://<DATABASE_NAME>.firebaseio.com/")
        .build();

    FirebaseApp.initializeApp(options);

### Python

    default_app = firebase_admin.initialize_app()

### Go

    app, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/init.go#L60-L63

### C#

    FirebaseApp.Create(new AppOptions()
    {
        Credential = GoogleCredential.GetApplicationDefault(),
    });

### Provide credentials manually

Firebase projects support Google[service accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk), which you can use to call Firebase server APIs from your app server or trusted environment. If you're developing code locally or deploying your application on-premises, you can use credentials obtained via this service account to authorize server requests.

To authenticate a service account and authorize it to access Firebase services, you must generate a private key file in JSON format.

**To generate a private key file for your service account:**

1. In theFirebaseconsole, open**Settings \>[Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)**.

2. Click**Generate New Private Key** , then confirm by clicking**Generate Key**.

3. Securely store the JSON file containing the key.

When authorizing via a service account, you have two choices for providing the credentials to your application. You can either set the<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>environment variable, or you can explicitly pass the path to the service account key in code. The first option is more secure and is strongly recommended.

**To set the environment variable:**

Set the environment variable<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>to the file path of the JSON file that contains your service account key. This variable only applies to your current shell session, so if you open a new session, set the variable again.  

### Linux or macOS

    export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

### Windows

With PowerShell:  

    $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

After you've completed the above steps, Application Default Credentials (ADC) is able to implicitly determine your credentials, allowing you to use service account credentials when testing or running in non-Google environments.

### Use credentials to mint access tokens

Use your Firebase credentials together with the[Google Auth Library](https://github.com/googleapis?q=auth)for your preferred language to retrieve a short-lived OAuth 2.0 access token:  

### node.js

     function getAccessToken() {
      return new Promise(function(resolve, reject) {
        const key = require('../placeholders/service-account.json');
        const jwtClient = new google.auth.JWT(
          key.client_email,
          null,
          key.private_key,
          SCOPES,
          null
        );
        jwtClient.authorize(function(err, tokens) {
          if (err) {
            reject(err);
            return;
          }
          resolve(tokens.access_token);
        });
      });
    }  
    https://github.com/firebase/quickstart-nodejs/blob/55f2ff5c17c730f7fc352f51a5264011de92fed0/messaging/index.js#L22-L40

In this example, the Google API client library authenticates the request with a JSON web token, or JWT. For more information, see[JSON web tokens](https://github.com/googleapis/google-auth-library-nodejs/blob/d8c70b9d858e1ef07cb8ef2b5d5d560ac2b2600a/README.md#json-web-tokens).

### Python

    def _get_access_token():
      """Retrieve a valid access token that can be used to authorize requests.

      :return: Access token.
      """
      credentials = service_account.Credentials.from_service_account_file(
        'service-account.json', scopes=SCOPES)
      request = google.auth.transport.requests.Request()
      credentials.refresh(request)
      return credentials.token  
    https://github.com/firebase/quickstart-python/blob/2c68e7c5020f4dbb072cca4da03dba389fbbe4ec/messaging/messaging.py#L26-L35

### Java

    private static String getAccessToken() throws IOException {
      GoogleCredentials googleCredentials = GoogleCredentials
              .fromStream(new FileInputStream("service-account.json"))
              .createScoped(Arrays.asList(SCOPES));
      googleCredentials.refresh();
      return googleCredentials.getAccessToken().getTokenValue();
    }  
    https://github.com/firebase/quickstart-java/blob/254dd24fbc89e6b49e6c84ecbbcc1ba31975392c/messaging/src/main/java/com/google/firebase/quickstart/Messaging.java#L56-L62

After your access token expires, the token refresh method is called automatically to retrieve an updated access token.

To authorize access toFCM, request the scope`https://www.googleapis.com/auth/firebase.messaging`.

**To add the access token to an HTTP request header:**

Add the token as the value of the`Authorization`header in the format`Authorization: Bearer <access_token>`:  

### node.js

    headers: {
      'Authorization': 'Bearer ' + accessToken
    }  
    https://github.com/firebase/quickstart-nodejs/blob/55f2ff5c17c730f7fc352f51a5264011de92fed0/messaging/index.js#L55-L57

### Python

    headers = {
      'Authorization': 'Bearer ' + _get_access_token(),
      'Content-Type': 'application/json; UTF-8',
    }  
    https://github.com/firebase/quickstart-python/blob/2c68e7c5020f4dbb072cca4da03dba389fbbe4ec/messaging/messaging.py#L45-L48

### Java

    URL url = new URL(BASE_URL + FCM_SEND_ENDPOINT);
    HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
    httpURLConnection.setRequestProperty("Authorization", "Bearer " + getServiceAccountAccessToken());
    httpURLConnection.setRequestProperty("Content-Type", "application/json; UTF-8");
    return httpURLConnection;  
    https://github.com/firebase/snippets-java/blob/7051da2745f8f95b176c9c6347e0bb0db3de1112/admin/src/main/java/com/google/firebase/example/FirebaseMessagingSnippets.java#L243-L247

## Update the payload of send requests

FCM HTTP v1 introduces a significant change in the structuring of the JSON message payload. Primarily, these changes ensure that messages are handled correctly when received on different client platforms; additionally, the changes give you extra flexibility to customize, or "override" message fields per platform.

In addition to inspecting the examples in this section, see[Customizing a message across platforms](https://firebase.google.com/docs/cloud-messaging/concept-options#customizing_a_message_across_platforms)and review the[API reference](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)to gain familiarity with HTTP v1.

### Example: simple notification message

Here is a comparison of a very simple notification payload--- containing`title`,`body`and`data`fields only--- demonstrating the fundamental differences in legacy and HTTP v1 payloads.

#### Before

    {
      "to": "/topics/news",
      "notification": {
        "title": "Breaking News",
        "body": "New news story available."
      },
      "data": {
        "story_id": "story_12345"
      }
    }

#### After

    {
      "message": {
        "topic": "news",
        "notification": {
          "title": "Breaking News",
          "body": "New news story available."
        },
        "data": {
          "story_id": "story_12345"
        }
      }
    }

### Example: nested JSON data

Unlike the legacy messaging API, the HTTP v1 API does not support nested JSON values in the`data`field. A conversion from JSON to string is required.

#### Before

    {
      ...
      "data": {
        "keysandvalues": {"key1": "value1", "key2": 123}
      }
    }

#### After

    {
      "message": {
       ...
        "data": {
          "keysandvalues": "{\"key1\": \"value1\", \"key2\": 123}"
        }
      }
    }

### Example: targeting multiple platforms

To enable multiple-platform targeting, the legacy API performed overrides in the backend. By contrast, HTTP v1 provides platform-specific blocks of keys that make any differences between platforms explicit and visible to the developer. This allows you to target multiple platforms always with a single request, as demonstrated in the following sample.

#### Before

    // Android
    {
      "to": "/topics/news",
      "notification": {
        "title": "Breaking News",
        "body": "New news story available.",
        "click_action": "TOP_STORY_ACTIVITY"
      },
      "data": {
        "story_id": "story_12345"
      }
    }
    // Apple
    {
      "to": "/topics/news",
      "notification": {
        "title": "Breaking News",
        "body": "New news story available.",
        "click_action": "HANDLE_BREAKING_NEWS"
      },
      "data": {
        "story_id": "story_12345"
      }
    }

#### After

    {
      "message": {
        "topic": "news",
        "notification": {
          "title": "Breaking News",
          "body": "New news story available."
        },
        "data": {
          "story_id": "story_12345"
        },
        "android": {
          "notification": {
            "click_action": "TOP_STORY_ACTIVITY"
          }
        },
        "apns": {
          "payload": {
            "aps": {
              "category" : "NEW_MESSAGE_CATEGORY"
            }
          }
        }
      }
    }

### Example: customizing with platform overrides

In addition to simplifying cross-platform targeting of messages, the HTTP v1 API provides flexibility to customize messages per platform.

#### Before

    // Android
    {
      "to": "/topics/news",
      "notification": {
        "title": "Breaking News",
        "body": "Check out the Top Story.",
        "click_action": "TOP_STORY_ACTIVITY"
      },
      "data": {
        "story_id": "story_12345"
      }
    }
    // Apple
    {
      "to": "/topics/news",
      "notification": {
        "title": "Breaking News",
        "body": "New news story available.",
        "click_action": "HANDLE_BREAKING_NEWS"
      },
      "data": {
        "story_id": "story_12345"
      }
    }

#### After

    {
      "message": {
        "topic": "news",
        "notification": {
          "title": "Breaking News",
          "body": "New news story available."
        },
        "data": {
          "story_id": "story_12345"
        },
        "android": {
          "notification": {
            "click_action": "TOP_STORY_ACTIVITY",
            "body": "Check out the Top Story"
          }
        },
        "apns": {
          "payload": {
            "aps": {
              "category" : "NEW_MESSAGE_CATEGORY"
            }
          }
        }
      }
    }

### Example: targeting specific devices

To target specific devices with the HTTP v1 API, provide the device's current registration token in the`token`key instead of the`to`key.

#### Before

      { "notification": {
          "body": "This is an FCM notification message!",
          "title": "FCM Message"
        },
        "to" : "bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1..."
      }

#### After

    {
       "message":{
          "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
          "notification":{
            "body":"This is an FCM notification message!",
            "title":"FCM Message"
          }
       }
    }

For more samples and information about theFCMHTTP v1 API, see the following:

- Guidance on how to[build app server send requests](https://firebase.google.com/docs/cloud-messaging/send-message#rest)with the HTTP v1 API. All "REST" snippets use the v1 API unless specifically noted.

- The[Firebase Blog](https://firebase.googleblog.com/2017/11/whats-new-with-fcm-customizing-messages.html).