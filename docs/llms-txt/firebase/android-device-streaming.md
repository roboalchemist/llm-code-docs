# Source: https://firebase.google.com/docs/test-lab/android/android-device-streaming.md.txt

<br />

Android Device Streaming lets you interact with and test your apps across multiple API levels and form factors in Google's secure data centers within Android Studio. With device streaming, you can interact with your app on a real device, just like a user would, including rotating and folding the device. This lets you see how your app behaves in different situations and to identify any problems that might not be apparent in other testing environments.

## Get started with Android Device Streaming

If you haven't done so already, download and install the latest Stable build of[Android Studio](https://developer.android.com/studio/)and follow these steps:

1. In Android Studio, open an Android project and navigate to the**Device Manager**tool window and click the Firebase icon.
2. If you're not already signed in to your developer account, click**Log in to Google**and follow the prompts.
3. After providing Android Studio with the requested permissions, return to the IDE and select a Firebase project. If you don't have a Firebase project, you can create one at no cost in the[Firebaseconsole](https://console.firebase.google.com/). Note: To enable the proper permissions to use device streaming with your Firebase project, see[Test Labpermissions](https://firebase.google.com/docs/test-lab/android/android-device-streaming#enable-testlab-permissions).
4. After selecting a project, you can browse the list of devices and select the devices you want to use.
5. Click**OK**.

For more information on how to get started with device streaming, see[Device Streaming in Android Studio](https://developer.android.com/studio/run/android-device-streaming).

## Enable permissions for Android Device Streaming

To use Device Streaming, you need to use a Firebase project that you have either**Editor** or**Owner** permissions. If you want to provide more specific roles and permissions to your team, you can enable[Test Lab permissions](https://firebase.google.com/docs/test-lab/android/android-device-streaming#enable-testlab-permissions)for Device Streaming.

### Test Lab permissions

To configure Test Lab permissions so that you can execute and read your test results, you have to configure access to Cloud Storage buckets. You can grant access to Test Lab, using the Firebase console or gcloud CLI.

For a user to run tests or view test results from the Firebase console or the[Test Lab Device Matrix in Android Studio](https://developer.android.com/studio/test/test-in-android-studio#run-with-firebase-test-lab), you will need to assign them the Editor and Viewer project roles.

For a user to run tests or view test results from the gcloud CLI while using your own Cloud Storage bucket, you can assign a pair of predefined roles, that will grant the required set of permissions together, using the Google Cloud console.

- To run test, assign the Firebase Test Lab Admin and Firebase Analytics Viewer roles.
- To view test results, assign the Firebase Test Lab Viewer and Firebase Analytics Viewer roles.

For more information on how to configure these granular Test Lab permissions, see Test Lab's[IAM permissions reference guide](https://firebase.google.com/docs/test-lab/android/iam-permissions-reference).