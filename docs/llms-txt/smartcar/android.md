# Source: https://smartcar.com/docs/getting-started/tutorials/android.md

# Android Tutorial

> In this tutorial, we will use the Android SDK to integrate Connect into your application.

<Warning>
  Our frontend SDKs handle getting an authorization code representing a vehicle owner's consent for your application to interact with their vehicle
  for the requested permissions. In order to make requests to a vehicle, please use one of our [backend SDKs](/api-reference/api-sdks).

  For security, token exchanges and requests to vehicles **should not** be made client side.
</Warning>

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e55ce733a1529f22994defa49ca2ca8c" data-og-width="850" width="850" data-og-height="510" height="510" data-path="images/android/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8ded54ca1d073b539d48542e44032e6b 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7a3b55192cd87e42e5b5e0cc51ef81f0 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=050ddfb32ff8eafb4a907ee1601a653a 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1e8414af0bb59139f78d4ff54072a129 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=97d5a32bc895768e53ba94f9139c751a 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=202b2b7d1ff4c26cbc91677a30d692ea 2500w" />
</Frame>

<br />

1. The Mobile Application launches a `Chrome Custom Tab` with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with their vehicle credentials and grants the Application access to their vehicle.
2. The `Chrome Tab` is redirected to a specified `REDIRECT_URI` along with an authorization `code`.
   This will be the custom scheme set on the application. The Smartcar Android receives the authorization `code` in a view listening
   for the specified custom scheme URI, and passes it to the Mobile Application.
3. The Mobile Application sends the received authorization `code` to the Application’s backend service.
4. The Application sends a request to the Smartcar API. This request contains the authorization code along with the Application’s
   `CLIENT_ID` and `CLIENT_SECRET`.
5. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
6. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add a custom scheme redirect URI to your application configuration.
* Add the `app_server` redirect URI from [Setup step 2.](/getting-started/tutorials/android#setup) to your application configuration.

<Note>
  For Android, we require the custom URI scheme to be in the format of `sc` + `clientId` + `://` + `hostname`.
  For now, you can just set it to `sc` + `clientId` + `://exchange`.

  Please see our [Connect Docs](/connect/dashboard-config#redirect-uris) for more information.
</Note>

# Setup

1. Clone our repo and install the required dependencies:
   ```bash  theme={null}
   $git clone https://github.com/smartcar/getting-started-android-sdk.git
   ```
   <Note>
     Do not “checkout from version control” with the Getting Started repo in Android Studio, as it will not open the proper module.
   </Note>

2. Open `getting-started-android-sdk/tutorial` in Android Studio as an existing project and build from existing sources.
   Android Studio should automatically import the required dependencies and build gradle. We're setting `app_server` to `http://10.0.2.2:8000`
   to pass the authorization `code` from the [Handle the Response](/getting-started/tutorials/android#handle-the-response) step later on in the tutorial to our backend.
   ```xml strings.xml theme={null}
   <string name="smartcar_auth_scheme">sc[yourClientId]</string>
   <string name="client_id">[yourClientId]</string>
   <string name="app_server">http://10.0.2.2:8000</string>
   ```

# Build your Connect URL

1. Instantiate a `smartcarAuth` object in the `onCreate` function of the `MainActivity`.
   ```java MainActivity.java theme={null}
   // TODO: Authorization Step 1a: Initialize the Smartcar object
   private static String CLIENT_ID;
   private static String REDIRECT_URI;
   private static String[] SCOPE;
   private SmartcarAuth smartcarAuth;

   protected void onCreate(Bundle savedInstanceState) {
       ...
       
       // TODO: Authorization Step 1b: Initialize the Smartcar object
       CLIENT_ID = getString(R.string.client_id);
       REDIRECT_URI = getString(R.string.smartcar_auth_scheme) + "://" + getString(R.string.smartcar_auth_host);
       SCOPE = new String[]{"required:read_vehicle_info"};
       
       smartcarAuth = new SmartcarAuth(
           CLIENT_ID,
           REDIRECT_URI,
           SCOPE,
           true,
           new SmartcarCallback() {
               // TODO: Authorization Step 3b: Receive an authorization code
           }
       );
   }
   ```

<Info>
  The Android SDK does not support `simulated` mode at this time - only `test` and `live`.
  Feel free to set `testMode` to `false` where you instantiate your `SmartcarAuth` object to
  connect to a real vehicle.
</Info>

2. The Android application will launch a Chrome Tab with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with the username and password for their vehicle’s connected services account and grants the application access to their vehicle.

   To launch Connect, we can use the `addClickHandler` function that our `smartcarAuth` object has access to.

   ```java MainActivity.java theme={null}
   // TODO: Authorization Step 2: Launch Connect
   smartcarAuth.addClickHandler(appContext, connectButton);
   ```

# Registering your Custom Scheme

Once a user has authorized the application to access their vehicle, the user is redirected to the `REDIRECT_URI` with an authorization `code` as a query parameter.

Android applications use custom URI schemes to intercept calls and launch the relevant application. This is defined within the `AndroidManifest`.

```xml AndroidManifest.xml theme={null}
<!-- TODO: Authorization Step 3a: Receive an authorization code -->
<activity android:name="com.smartcar.sdk.SmartcarCodeReceiver">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:host="@string/smartcar_auth_host"
            android:scheme="@string/smartcar_auth_scheme" />
    </intent-filter>
</activity>
```

# Handle the response

Using the Android SDK, the application can receive the code in the `SmartcarCallback` object passed into the `SmartcarAuth` object.

```java MainActivity.java theme={null}
smartcarAuth = new SmartcarAuth(
    CLIENT_ID,
    REDIRECT_URI,
    SCOPE,
    true,
    new SmartcarCallback() {
        // TODO: Authorization Step 3b: Receive an authorization code
        @Override
        public void handleResponse(final SmartcarResponse smartcarResponse) {
            Log.i("MainActivity", smartcarResponse.getCode());

            // TODO: Request Step 1: Obtain an access token

            //TODO: Request Step 2: Get vehicle information
        }
    }
);
```

# Launching Connect

Build your application in Android Studio and click on the **Connect your vehicle** button.

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

# Getting your first access token

After receiving the authorization `code`, your iOS application must exchange it for an `ACCESS_TOKEN`. To do so, we can send
the code to a backend service. Let’s assume our backend service contains an endpoint `/exchange` that receives an authorization `code` as a query parameter and exchanges it for an `ACCESS_TOKEN`.

```swift ViewController.swift theme={null}
// TODO: Obtain an access token
public void handleResponse(final SmartcarResponse smartcarResponse) {
    Log.i("MainActivity", smartcarResponse.getCode());

    final OkHttpClient client = new OkHttpClient();

    // TODO: Request Step 1: Obtain and access token

    // Request can not run on the Main Thread
    // Main Thread is used for UI and therefore can not be blocked
    new Thread(new Runnable() {
        @Override
        public void run() {
    
            // send request to exchange the auth code for the access token
            Request exchangeRequest = new Request.Builder()
                .url(getString(R.string.app_server) + "/exchange?code=" + smartcarResponse.getCode())
                .build();
        
            try {
                client.newCall(exchangeRequest).execute();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }).start();
}
```

<Warning>
  Notice that our backend service **does not** return the `ACCESS_TOKEN`.
  This is by design. For security, our frontend should never have access
  to the `ACCESS_TOKEN` and should always be stored in the backend.
</Warning>

# Getting data from a vehicle

Once the backend has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API. The Android app will
have to send a request to the backend service which in turn sends a request to Smartcar. We have to do this because
our frontend **does not** have the `ACCESS_TOKEN`.

Assuming our backend has a `/vehicle` endpoint that returns the information of a user’s vehicle, we can make this query in
our `completion callback` and start another `activity` to show the returned vehicle attributes.

```java MainActivity.java theme={null}
public void handleResponse(final SmartcarResponse smartcarResponse) {
    ...
    
    // TODO: Request Step 2: Get vehicle information

    // send request to retrieve the vehicle info
    Request infoRequest = new Request.Builder()
        .url(getString(R.string.app_server) + "/vehicle")
        .build();
    
    try {
        Response response = client.newCall(infoRequest).execute();
    
        String jsonBody = response.body().string();
        JSONObject JObject = new JSONObject(jsonBody);
    
        String make = JObject.getString("make");
        String model = JObject.getString("model");
        String year = JObject.getString("year");
    
        Intent intent = new Intent(appContext, DisplayInfoActivity.class);
        intent.putExtra("INFO", make + " " + model + " " + year);
        startActivity(intent);
    } catch (IOException e) {
        e.printStackTrace();
    } catch (JSONException e) {
        e.printStackTrace();
    }
}
```

# Setting up your backend

Now that our frontend is complete, we will need to create a backend service that contains the logic for the `/exchange` and `/vehicle` endpoints.
You can use any of our backend SDKs below to set up the service starting from the **Obtaining an Access Token** step.

<Note>
  When setting up the environment variables for your  backend SDK, make sure to set `REDIRECT_URI` to the custom scheme
  used for this tutorial i.e. `sc + "clientId" + ://exchange`.
</Note>

<CardGroup cols={4}>
  <Card title="Java" icon="java" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Node.js" href="/getting-started/how-to/architecture-design" icon="node-js" icontype="duotone" />

  <Card title="Python" icon="python" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Ruby" href="/getting-started/how-to/architecture-design" icon="gem" icontype="duotone" />
</CardGroup>
