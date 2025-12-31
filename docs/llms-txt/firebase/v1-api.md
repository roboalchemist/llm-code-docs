# Source: https://firebase.google.com/docs/cloud-messaging/send/v1-api.md.txt

<br />

Using the[FCMHTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages), you can build message requests and send them to these types of targets:

- Topic name
- Condition
- Device registration token
- Device group name (protocol only)

You can send messages with a notification payload made up of predefined fields, a data payload of your own user-defined fields, or a message containing both types of payload. See[Message types](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type)for more information.
| **Tip:** Use this[codelab](https://firebase.google.com/codelabs/use-the-fcm-http-v1-api-with-oauth-2-access-tokens)to learn how to use the FCM HTTP v1 API with OAuth 2.0 access tokens

## Authorize HTTP v1 send requests

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

Unless you are using the[FirebaseAdmin SDK](https://firebase.google.com/docs/cloud-messaging/send/admin-sdk), which handles authorization automatically, you'll need to mint the access token and add it to send requests.

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

## Authorize with a Service Account from a Different Project

You can send messages for one project (the "target project") while using an OAuth 2.0 token generated from a service account in a different project (the "sender project"). This lets you centralize service account management in one project while sending messages on behalf of others. To learn how to do this, use the following steps:

1. **Enable API:** Ensure the Firebase Cloud Messaging API is[enabled](https://console.firebase.google.com/project/_/settings/cloudmessaging/?_gl=1*sjye00*_ga*NDU0NDM2OTk2LjE3NTYzMjgyOTQ.*_ga_CW55HF8NVT*czE3NTYzMjgyOTMkbzEkZzEkdDE3NTYzMjgzNzkkajQxJGwwJGgw)in the sender project.
2. **Create Service Account:** Create a[service account](https://cloud.google.com/iam/docs/service-accounts-create)in the sender project.
3. **Grant Permissions:** In the target project, grant the service account's email address the[Firebase Cloud Messaging API Admin](https://cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.admin)role on the IAM page. This allows the service account from the other project to send messages to the target project.
4. **Obtain Token:** [Generate](https://firebase.google.com/docs/cloud-messaging/send/v1-api#use-credentials-to-mint-access-tokens)an OAuth 2.0 access token for the service account in the sender project. You can do this by either:
   - Downloading and using the service account key JSON file.
   - Alternatively, using[Workload Identity](https://cloud.google.com/iam/docs/workload-identities)if your service is running on Google Cloud.
5. **Send Request:** Use the obtained access token in the`Authorization`header of your send request. The request must be made to the HTTP v1 endpoint for the**target project** :  

   ```scdoc
       POST https://fcm.googleapis.com/v1/TARGET_PROJECT_ID/messages:send
   ```

## Send messages to specific devices

To send to a single, specific device, pass the device's registration token as shown.  

### REST

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

    Content-Type: application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA

    {
       "message":{
          "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
          "notification":{
            "body":"This is an FCM notification message!",
            "title":"FCM Message"
          }
       }
    }

cURL command:  

    curl -X POST -H "Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA" -H "Content-Type: application/json" -d '{
    "message":{
       "notification":{
         "title":"FCM Message",
         "body":"This is an FCM Message"
       },
       "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1..."
    }}' https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send

On success, the HTTP v1 API response is a JSON object containing the message ID:  

        {
          "name":"projects/myproject-b5ae1/messages/0:1500415314455276%31bd1c9631bd1c96"
        }

## Send a test notification message using the FCM HTTP v1 API

This section describes how to send a test notification message using the FCM HTTP v1 API.

### HTTP request URL

The request consists of an HTTP POST to the specified target (a registration token, topic or condition) at the following URL:  

```text
POST https://fcm.googleapis.com/v1/projectId/messages:send
```

### Complete HTTP request JSON sample

Here is a complete example showing how to post a notification within an HTTP POST request:  

```scdoc
{
  "message": {
    "token": REGISTRATION_TOKEN,
    "notification": {
      "title": "FCM API test",
      "body": "This is the body of the notification.",
      "image": "https://cat.10515.net/1.jpg"
    }
  }
}
```

[Run](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send?apix=true&apix_params=%7B%22parent%22:%22projects/PROJECT_ID%22,%22resource%22:%7B%22message%22:%7B%22token%22:%22REGISTRATION_TOKEN%22,%22notification%22:%7B%22title%22:%22FCM+API+test%22,%22body%22:%22This+is+the+body+of+the+notification.%22,%22image%22:%22https://cat.10515.net/1.jpg%22%7D%7D%7D%7D)

Click**Run** to try the sample in the**API Explorer**.