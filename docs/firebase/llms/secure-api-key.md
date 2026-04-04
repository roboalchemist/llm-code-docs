# Source: https://firebase.google.com/docs/ml/ios/secure-api-key.md.txt

# Source: https://firebase.google.com/docs/ml/android/secure-api-key.md.txt

<br />

If your Android app uses one ofFirebase ML's cloud APIs, before you launch your app in production, you should take some additional steps to prevent unauthorized API access.

For your production apps, you will ensure that only authenticated clients can access cloud services. (Note that only non-rooted devices can authenticate using the method described.)

Then, you will create a debug-only API key that you can use for convenience during testing and development.

## 1. Register your production apps with Firebase

First, register your production apps with Firebase.

1. Make sure that you have your app's SHA-1 signatures. Refer to[Authenticating your client](https://developers.google.com/android/guides/client-auth)to learn how.

2. Go to yoursettings*Project settings* in theFirebaseconsole, then select the*Settings*tab.

3. Scroll down to the*Your apps*card, then select your Android app.

4. Add your app's SHA-1 signature to your app's information.

## 2. Restrict the scope of your API keys

Next, configure your existing API keys to disallow access to the Cloud Vision API:

1. Open the[Credentials](https://console.cloud.google.com/apis/credentials?project=_)page of theGoogle Cloudconsole. When prompted, select your project.

2. For each existing API key in the list, open the editing view.

3. In the*API restrictions* section, select**Restrict key** , then add to the list all of the APIs to which you want the API key to have access. Make sure to***not***include the Cloud Vision API.

   When you configure an API key's*API restrictions* , you are explicitly declaring the APIs to which the key has access.**By default, when the*API restrictions* section has*Don't restrict key*selected, an API key can be used to access any API that is enabled for the project.**

Now, your existing API keys will not grant access to cloud ML services, but each key will continue to work for any APIs that you added to its*API restrictions*list.

Note that if you enable any additional APIs in the future, you must add them to the*API restrictions*list for the applicable API key.

## 3. Create and use a debug-only API key

Finally, create a new API key to be used only for development.Firebase MLcan use this API key to accessGoogle Cloudservices in environments where app authentication isn't possible, such as when running on emulators.

1. Create a new API key to be used for development:

   1. Open the[Credentials](https://console.cloud.google.com/apis/credentials?project=_)page of theGoogle Cloudconsole. When prompted, select your project.

   2. Click**Create credentials \> API key** and take note of the new API key. This key allows API access from unauthenticated apps, so**keep this key confidential**.

2. To ensure the new debug API key is not leaked with your released app, specify the debug API key in an Android manifest file used only for debug builds:

   1. If you don't already have a debug manifest, create one by clicking**File \> New \> Other \> Android Manifest File** and selecting`debug`from the target source sets.

   2. In the debug manifest, add the following declaration:

      ```text
      <application>
      <meta-data
          android:name="com.firebase.ml.cloud.ApiKeyForDebug"
          android:value="your-debug-api-key" />
      </application>
      ```
3. In your app, configureFirebase MLto use certificate fingerprint matching to authenticate your client in production and to use API keys---the debug key---only in debug builds:

   ### Kotlin

   ```kotlin
   val optionsBuilder = FirebaseVisionCloudImageLabelerOptions.Builder()
   if (!BuildConfig.DEBUG) {
       // Requires physical, non-rooted device:
       optionsBuilder.enforceCertFingerprintMatch()
   }

   // Set other options. For example:
   optionsBuilder.setConfidenceThreshold(0.8f)
   // ...

   // And lastly:
   val options = optionsBuilder.build()
   FirebaseVision.getInstance().getCloudImageLabeler(options).processImage(myImage)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/MainActivity.kt#L30-L42
   ```

   ### Java

   ```java
   FirebaseVisionCloudImageLabelerOptions.Builder optionsBuilder =
           new FirebaseVisionCloudImageLabelerOptions.Builder();
   if (!BuildConfig.DEBUG) {
       // Requires physical, non-rooted device:
       optionsBuilder.enforceCertFingerprintMatch();
   }

   // Set other options. For example:
   optionsBuilder.setConfidenceThreshold(0.8f);
   // ...

   // And lastly:
   FirebaseVisionCloudImageLabelerOptions options = optionsBuilder.build();
   FirebaseVision.getInstance().getCloudImageLabeler(options).processImage(myImage);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/MainActivity.java#L30-L43
   ```

## Next steps

See the[launch checklist](https://firebase.google.com/support/guides/launch-checklist)for information on preparing your app to launch when using other Firebase features.