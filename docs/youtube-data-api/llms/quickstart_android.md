# Source: https://developers.google.com/youtube/v3/quickstart/android.md.txt

This guide explains how to set up a simple Android application that makes
requests to the YouTube Data API.
| **Note:** This quickstart demonstrates use of the YouTube Data API in an Android application. Many applications that use the Data API also use the [YouTube Android
| Player API](https://developers.google.com/youtube/android/player), which lets you incorporate video playback functionality in an Android application.

## Prerequisites

To run this quickstart, you'll need:

- [Android Studio SDK 1.2 or later](https://developer.android.com/sdk/index.html).
- [Android SDK packages](https://developer.android.com/sdk/installing/adding-packages.html) for API 23 or later, including the latest versions of Google Repository, Android Support Library and Google Play Services.
- Access to the internet on your test device.
- A Google account.

This quickstart will assume you are using the
[Android Studio](https://developer.android.com/tools/studio/index.html)
IDE (as opposed to the stand-alone SDK Tools) and are comfortable finding,
creating and editing files within a Studio project.

## Step 1: Acquire a SHA1 fingerprint

In a terminal, run the folowing
[Keytool
utility](https://developer.android.com/guide/publishing/app-signing.html) command to get the SHA1 fingerprint you will use to enable the API.  

    keytool -exportcert -alias androiddebugkey -keystore ~/.android/debug.keystore -list -v

When asked for a keystore password, enter "android".

The Keytool prints the fingerprint to the shell. For example:  

```
$ keytool -exportcert -alias androiddebugkey -keystore ~/.android/debug.keystore -list -v
Enter keystore password: Type "android" if using debug.keystore
Alias name: androiddebugkey
Creation date: Dec 4, 2014
Entry type: PrivateKeyEntry
Certificate chain length: 1
Certificate[1]:
Owner: CN=Android Debug, O=Android, C=US
Issuer: CN=Android Debug, O=Android, C=US
Serial number: 503bd581
Valid from: Mon Aug 27 13:16:01 PDT 2012 until: Wed Aug 20 13:16:01 PDT 2042
Certificate fingerprints:
   MD5:  1B:2B:2D:37:E1:CE:06:8B:A0:F0:73:05:3C:A3:63:DD
   SHA1: D8:AA:43:97:59:EE:C5:95:26:6A:07:EE:1C:37:8E:F4:F0:C8:05:C8
   SHA256: F3:6F:98:51:9A:DF:C3:15:4E:48:4B:0F:91:E3:3C:6A:A0:97:DC:0A:3F:B2:D2:E1:FE:23:57:F5:EB:AC:13:30
   Signature algorithm name: SHA1withRSA
   Version: 3
```

Copy the SHA1 fingerprint, which is
**highlighted** in the example above.
| **Important:** When you create a production app, you should not use the debug keystore. For more information, see [Signing your applications](https://developer.android.com/tools/publishing/app-signing.html).

## Step 2: Turn on the YouTube Data API

1. Use
   [this wizard](https://console.developers.google.com/start/api?id=youtube)
   to create or select a project in the Google Developers Console and
   automatically turn on the API. Click **Continue** , then
   **Go to credentials**.

2. On the **Create credentials** page, click the
   **Cancel** button.

3. At the top of the page, select the **OAuth consent screen** tab.
   Select an **Email address** , enter a **Product name** if not
   already set, and click the **Save** button.

4. Select the **Credentials** tab, click the **Create credentials**
   button and select **OAuth client ID**.

5. Select the application type **Android**.
6. Copy the SHA1 fingerprint from Step 1 into the **Signing-certificate
   fingerprint** field.
7. In the [**Package name**](https://developer.android.com/guide/topics/manifest/manifest-element.html#package) field, enter `com.example.quickstart`.
8. Click the **Create** button.

## Step 3: Create a new Android project

1. Open [Android Studio](https://developer.android.com/tools/studio/index.html), and start a New Android Studio Project.
2. In the **New Project** screen, name the application "Quickstart".
3. Set **Company Domain** to "example.com" and verify that the package name automatically produced matches the one you entered into the [Developer Console](https://console.developers.google.com) in Step 2. Click **Next**.
4. In the **Target Android Devices** screen, check the **Phone and Tablet** checkbox and choose a **Minimum SDK** of "API 14: Android 4.0 (IceCreamSandwich)". Leave the other checkboxes unchecked. Click **Next**.
5. In the **Add an activity to Mobile** screen, click **Add No Activity**.
6. Click **Finish**.

At this point,
[Android Studio](https://developer.android.com/tools/studio/index.html)
creates and opens the project.

## Step 4: Prepare the project

The Project sidebar is an expandable list of the default project files that
[Android Studio](https://developer.android.com/tools/studio/index.html)
has created. In that list, expand the list of Gradle scripts and open the
`build.gradle` file that is associated with the "app" module
(not the project).
| **Warning:** Be sure to open the correct `build.gradle` file. The first line should read `apply
| plugin: 'com.android.application'`.

1. Open the app `build.gradle` file and replace its contents with the following:
2. In the toolbar, select **Tools \> Android \> Sync Project with Gradle Files**. This will acquire and make available the libraries your project needs.
3. Find and open the default `src/main/AndroidManifest.xml` file. In the Project sidebar, this file is nested under `app` and then under `manifests`. Replace the file's contents with the following code:  

   ```carbon
   <?xml version="1.0" encoding="utf-8"?>
   <manifest xmlns:android="http://schemas.android.com/apk/res/android"
       package="com.example.quickstart">

       <uses-permission android:name="android.permission.INTERNET" />
       <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
       <uses-permission android:name="android.permission.GET_ACCOUNTS" />

       <application
           android:allowBackup="true"
           android:icon="@mipmap/ic_launcher"
           android:label="YouTube Data API Android Quickstart"
           android:theme="@style/AppTheme" >
           <activity
               android:name=".MainActivity"
               android:label="YouTube Data API Android Quickstart" >
               <intent-filter>
                   <action android:name="android.intent.action.MAIN" />
                   <category android:name="android.intent.category.LAUNCHER" />
               </intent-filter>
           </activity>

       </application>
   </manifest>
   ```

## Step 5: Setup the sample

| **Note:** For simplicity, this quickstart builds its layout dynamically and uses hardcoded string constants. Most Android applications, however, benefit from defining layouts, strings and other resources in [XML resource files](https://developer.android.com/guide/topics/resources/overview.html).

Create a new Java class. To do so, first select the `java` folder in the
Project sidebar. This folder appears in the group of `app` files. After
clicking on the folder, you can select
**File** \> **New** \> **Java Class** from the menu bar, or you can
right-click on the folder and select **New** \> **Java Class**.
If prompted to select a directory, choose `.../app/src/main/java`.

Name the class "MainActivity" and click **OK**. Replace the contents of the
new file with the following code.  

```python
package com.example.quickstart;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GoogleApiAvailability;
import com.google.api.client.extensions.android.http.AndroidHttp;
import com.google.api.client.googleapis.extensions.android.gms.auth.GoogleAccountCredential;
import com.google.api.client.googleapis.extensions.android.gms.auth.GooglePlayServicesAvailabilityIOException;
import com.google.api.client.googleapis.extensions.android.gms.auth.UserRecoverableAuthIOException;

import com.google.api.client.http.HttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.client.util.ExponentialBackOff;

import com.google.api.services.youtube.YouTubeScopes;

import com.google.api.services.youtube.model.*;

import android.Manifest;
import android.accounts.AccountManager;
import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.text.TextUtils;
import android.text.method.ScrollingMovementMethod;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import pub.devrel.easypermissions.AfterPermissionGranted;
import pub.devrel.easypermissions.EasyPermissions;

public class MainActivity extends Activity
    implements EasyPermissions.PermissionCallbacks {
    GoogleAccountCredential mCredential;
    private TextView mOutputText;
    private Button mCallApiButton;
    ProgressDialog mProgress;

    static final int REQUEST_ACCOUNT_PICKER = 1000;
    static final int REQUEST_AUTHORIZATION = 1001;
    static final int REQUEST_GOOGLE_PLAY_SERVICES = 1002;
    static final int REQUEST_PERMISSION_GET_ACCOUNTS = 1003;

    private static final String BUTTON_TEXT = "Call YouTube Data API";
    private static final String PREF_ACCOUNT_NAME = "accountName";
    private static final String[] SCOPES = { YouTubeScopes.YOUTUBE_READONLY };

    /**
     * Create the main activity.
     * @param savedInstanceState previously saved instance data.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        LinearLayout activityLayout = new LinearLayout(this);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.MATCH_PARENT);
        activityLayout.setLayoutParams(lp);
        activityLayout.setOrientation(LinearLayout.VERTICAL);
        activityLayout.setPadding(16, 16, 16, 16);

        ViewGroup.LayoutParams tlp = new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT);

        mCallApiButton = new Button(this);
        mCallApiButton.setText(BUTTON_TEXT);
        mCallApiButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mCallApiButton.setEnabled(false);
                mOutputText.setText("");
                getResultsFromApi();
                mCallApiButton.setEnabled(true);
            }
        });
        activityLayout.addView(mCallApiButton);

        mOutputText = new TextView(this);
        mOutputText.setLayoutParams(tlp);
        mOutputText.setPadding(16, 16, 16, 16);
        mOutputText.setVerticalScrollBarEnabled(true);
        mOutputText.setMovementMethod(new ScrollingMovementMethod());
        mOutputText.setText(
                "Click the \'" + BUTTON_TEXT +"\' button to test the API.");
        activityLayout.addView(mOutputText);

        mProgress = new ProgressDialog(this);
        mProgress.setMessage("Calling YouTube Data API ...");

        setContentView(activityLayout);

        // Initialize credentials and service object.
        mCredential = GoogleAccountCredential.usingOAuth2(
                getApplicationContext(), Arrays.asList(SCOPES))
                .setBackOff(new ExponentialBackOff());
    }

    

    /**
     * Attempt to call the API, after verifying that all the preconditions are
     * satisfied. The preconditions are: Google Play Services installed, an
     * account was selected and the device currently has online access. If any
     * of the preconditions are not satisfied, the app will prompt the user as
     * appropriate.
     */
    private void getResultsFromApi() {
        if (! isGooglePlayServicesAvailable()) {
            acquireGooglePlayServices();
        } else if (mCredential.getSelectedAccountName() == null) {
            chooseAccount();
        } else if (! isDeviceOnline()) {
            mOutputText.setText("No network connection available.");
        } else {
            new MakeRequestTask(mCredential).execute();
        }
    }

    /**
     * Attempts to set the account used with the API credentials. If an account
     * name was previously saved it will use that one; otherwise an account
     * picker dialog will be shown to the user. Note that the setting the
     * account to use with the credentials object requires the app to have the
     * GET_ACCOUNTS permission, which is requested here if it is not already
     * present. The AfterPermissionGranted annotation indicates that this
     * function will be rerun automatically whenever the GET_ACCOUNTS permission
     * is granted.
     */
    @AfterPermissionGranted(REQUEST_PERMISSION_GET_ACCOUNTS)
    private void chooseAccount() {
        if (EasyPermissions.hasPermissions(
                this, Manifest.permission.GET_ACCOUNTS)) {
            String accountName = getPreferences(Context.MODE_PRIVATE)
                    .getString(PREF_ACCOUNT_NAME, null);
            if (accountName != null) {
                mCredential.setSelectedAccountName(accountName);
                getResultsFromApi();
            } else {
                // Start a dialog from which the user can choose an account
                startActivityForResult(
                        mCredential.newChooseAccountIntent(),
                        REQUEST_ACCOUNT_PICKER);
            }
        } else {
            // Request the GET_ACCOUNTS permission via a user dialog
            EasyPermissions.requestPermissions(
                    this,
                    "This app needs to access your Google account (via Contacts).",
                    REQUEST_PERMISSION_GET_ACCOUNTS,
                    Manifest.permission.GET_ACCOUNTS);
        }
    }

    /**
     * Called when an activity launched here (specifically, AccountPicker
     * and authorization) exits, giving you the requestCode you started it with,
     * the resultCode it returned, and any additional data from it.
     * @param requestCode code indicating which activity result is incoming.
     * @param resultCode code indicating the result of the incoming
     *     activity result.
     * @param data Intent (containing result data) returned by incoming
     *     activity result.
     */
    @Override
    protected void onActivityResult(
            int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch(requestCode) {
            case REQUEST_GOOGLE_PLAY_SERVICES:
                if (resultCode != RESULT_OK) {
                    mOutputText.setText(
                            "This app requires Google Play Services. Please install " +
                            "Google Play Services on your device and relaunch this app.");
                } else {
                    getResultsFromApi();
                }
                break;
            case REQUEST_ACCOUNT_PICKER:
                if (resultCode == RESULT_OK && data != null &&
                        data.getExtras() != null) {
                    String accountName =
                            data.getStringExtra(AccountManager.KEY_ACCOUNT_NAME);
                    if (accountName != null) {
                        SharedPreferences settings =
                                getPreferences(Context.MODE_PRIVATE);
                        SharedPreferences.Editor editor = settings.edit();
                        editor.putString(PREF_ACCOUNT_NAME, accountName);
                        editor.apply();
                        mCredential.setSelectedAccountName(accountName);
                        getResultsFromApi();
                    }
                }
                break;
            case REQUEST_AUTHORIZATION:
                if (resultCode == RESULT_OK) {
                    getResultsFromApi();
                }
                break;
        }
    }

    /**
     * Respond to requests for permissions at runtime for API 23 and above.
     * @param requestCode The request code passed in
     *     requestPermissions(android.app.Activity, String, int, String[])
     * @param permissions The requested permissions. Never null.
     * @param grantResults The grant results for the corresponding permissions
     *     which is either PERMISSION_GRANTED or PERMISSION_DENIED. Never null.
     */
    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        EasyPermissions.onRequestPermissionsResult(
                requestCode, permissions, grantResults, this);
    }

    /**
     * Callback for when a permission is granted using the EasyPermissions
     * library.
     * @param requestCode The request code associated with the requested
     *         permission
     * @param list The requested permission list. Never null.
     */
    @Override
    public void onPermissionsGranted(int requestCode, List<String> list) {
        // Do nothing.
    }

    /**
     * Callback for when a permission is denied using the EasyPermissions
     * library.
     * @param requestCode The request code associated with the requested
     *         permission
     * @param list The requested permission list. Never null.
     */
    @Override
    public void onPermissionsDenied(int requestCode, List<String> list) {
        // Do nothing.
    }

    /**
     * Checks whether the device currently has a network connection.
     * @return true if the device has a network connection, false otherwise.
     */
    private boolean isDeviceOnline() {
        ConnectivityManager connMgr =
                (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
        return (networkInfo != null && networkInfo.isConnected());
    }

    /**
     * Check that Google Play services APK is installed and up to date.
     * @return true if Google Play Services is available and up to
     *     date on this device; false otherwise.
     */
    private boolean isGooglePlayServicesAvailable() {
        GoogleApiAvailability apiAvailability =
                GoogleApiAvailability.getInstance();
        final int connectionStatusCode =
                apiAvailability.isGooglePlayServicesAvailable(this);
        return connectionStatusCode == ConnectionResult.SUCCESS;
    }

    /**
     * Attempt to resolve a missing, out-of-date, invalid or disabled Google
     * Play Services installation via a user dialog, if possible.
     */
    private void acquireGooglePlayServices() {
        GoogleApiAvailability apiAvailability =
                GoogleApiAvailability.getInstance();
        final int connectionStatusCode =
                apiAvailability.isGooglePlayServicesAvailable(this);
        if (apiAvailability.isUserResolvableError(connectionStatusCode)) {
            showGooglePlayServicesAvailabilityErrorDialog(connectionStatusCode);
        }
    }


    /**
     * Display an error dialog showing that Google Play Services is missing
     * or out of date.
     * @param connectionStatusCode code describing the presence (or lack of)
     *     Google Play Services on this device.
     */
    void showGooglePlayServicesAvailabilityErrorDialog(
            final int connectionStatusCode) {
        GoogleApiAvailability apiAvailability = GoogleApiAvailability.getInstance();
        Dialog dialog = apiAvailability.getErrorDialog(
                MainActivity.this,
                connectionStatusCode,
                REQUEST_GOOGLE_PLAY_SERVICES);
        dialog.show();
    }

    /**
     * An asynchronous task that handles the YouTube Data API call.
     * Placing the API calls in their own task ensures the UI stays responsive.
     */
    private class MakeRequestTask extends AsyncTask<Void, Void, List<String>> {
        private com.google.api.services.youtube.YouTube mService = null;
        private Exception mLastError = null;

        MakeRequestTask(GoogleAccountCredential credential) {
            HttpTransport transport = AndroidHttp.newCompatibleTransport();
            JsonFactory jsonFactory = JacksonFactory.getDefaultInstance();
            mService = new com.google.api.services.youtube.YouTube.Builder(
                    transport, jsonFactory, credential)
                    .setApplicationName("YouTube Data API Android Quickstart")
                    .build();
        }

        /**
         * Background task to call YouTube Data API.
         * @param params no parameters needed for this task.
         */
        @Override
        protected List<String> doInBackground(Void... params) {
            try {
                return getDataFromApi();
            } catch (Exception e) {
                mLastError = e;
                cancel(true);
                return null;
            }
        }

        /**
         * Fetch information about the "GoogleDevelopers" YouTube channel.
         * @return List of Strings containing information about the channel.
         * @throws IOException
         */
        private List<String> getDataFromApi() throws IOException {
            // Get a list of up to 10 files.
            List<String> channelInfo = new ArrayList<String>();
            ChannelListResponse result = mService.channels().list("snippet,contentDetails,statistics")
                 .setForUsername("GoogleDevelopers")
                 .execute();
            List<Channel> channels = result.getItems();
            if (channels != null) {
                Channel channel = channels.get(0);
                channelInfo.add("This channel's ID is " + channel.getId() + ". " +
                        "Its title is '" + channel.getSnippet().getTitle() + ", " +
                        "and it has " + channel.getStatistics().getViewCount() + " views.");
            }
            return channelInfo;
        }

        @Override
        protected void onPreExecute() {
            mOutputText.setText("");
            mProgress.show();
        }

        @Override
        protected void onPostExecute(List<String> output) {
            mProgress.hide();
            if (output == null || output.size() == 0) {
                mOutputText.setText("No results returned.");
            } else {
                output.add(0, "Data retrieved using the YouTube Data API:");
                mOutputText.setText(TextUtils.join("\n", output));
            }
        }

        @Override
        protected void onCancelled() {
            mProgress.hide();
            if (mLastError != null) {
                if (mLastError instanceof GooglePlayServicesAvailabilityIOException) {
                    showGooglePlayServicesAvailabilityErrorDialog(
                            ((GooglePlayServicesAvailabilityIOException) mLastError)
                                    .getConnectionStatusCode());
                } else if (mLastError instanceof UserRecoverableAuthIOException) {
                    startActivityForResult(
                            ((UserRecoverableAuthIOException) mLastError).getIntent(),
                            MainActivity.REQUEST_AUTHORIZATION);
                } else {
                    mOutputText.setText("The following error occurred:\n"
                            + mLastError.getMessage());
                }
            } else {
                mOutputText.setText("Request cancelled.");
            }
        }
    }
}
```

## Step 6: Run the app

1. To test the app, click the **Run \> Run app** menu item.
2. You will be prompted to select a connected device (recommended) or emulation to run the app on. If you run on an emulation, make sure it is configured to use one of the **with Google APIs** system images. If you attempt to run the quickstart on a device that does not currently have Google Play services installed, the quickstart produces a dialog from which you can install it.
3. If running on an emulator, allow it to fully start and establish its network connection.
4. If starting the emulator for the first time, you may need to unlock its screen. Regardless, the quickstart app should start automatically.
5. The first time that you run the app, it prompts you to specify an account. Complete the sign-in flow to choose an account to connect to.
6. After selecting an account, the app prompts you to authorize access. Click **OK** to authorize.

It worked! **Great!** Check out the further reading section below to learn more.
I got an error **Bummer.** Check out our [troubleshooting](https://developers.google.com/youtube/v3/quickstart/android#troubleshooting) section below for some common errors and solutions. Thanks for letting us know and we'll work to fix this quickstart.

## Notes

- Authorization information is stored with the app, so subsequent executions do not prompt for authorization.

## Further reading

- [Google Developers Console help documentation](https://developers.google.com/console/help/new)
- [Google APIs Client for Java documentation](https://developers.google.com/api-client-library/java)
- [Android API Guides](https://developer.android.com/guide/index.html)
- [Google Play Services](https://developer.android.com/google/play-services/index.html)
- [YouTube Data API reference documentation](https://developers.google.com/youtube/v3/docs)

## Troubleshooting

#### Unregistered Android application

When the OAuth dialog contains an entry that reads "Unregistered Android
application," it means that the OAuth2 client ID you created in Step 2 cannot
be found and Android is falling back to a default client. The default client
won't be configured to use this API, so requests fail with errors like
`accessNotConfigured.` These errors might also mention the default project
number `608941808256`.

To fix the issue, make sure the SHA1 fingerprint that you retrieved in Step 1
and the `applicationId` listed in your `build.gradle` file match exactly with
the values that you set in the Google Developers console.