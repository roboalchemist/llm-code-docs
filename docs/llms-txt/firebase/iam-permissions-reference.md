# Source: https://firebase.google.com/docs/test-lab/android/iam-permissions-reference.md.txt

<br />

This document provides reference information about configuringTest LabIAM permissions and roles. If you want to configure more granular roles,Test Labprovides permissions for both executing tests and streaming devices using Android Studio. Test execution has extra requirements to properly configure permissions and roles for IAM and the streaming devices.

## Test Execution

To properly configureTest Labso that you can execute and read the results of tests, you have to configure access toCloud Storagebuckets. This requires a specific configuration of permissions that aren't all included in the standard[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined). To grant access toTest Lab, use one of the following options.

### Tests through theFirebaseconsole

For tests started fromFirebaseconsole or through the[Firebase Test Lab Device Matrix in Android Studio](https://developer.android.com/studio/test/test-in-android-studio#run-with-firebase-test-lab):

1. Test your app in a dedicated separate Firebase project.
2. Add users that needTest Labaccess and assign them legacy project roles using the[Firebaseconsole](https://console.firebase.google.com/).
3. (Optional) Assign the**Editor** project role to allow a user to run tests withTest Lab.
4. (Optional) Assign the**Viewer** project role to allow a user to view test results withTest Lab.

### Tests through gcloud CLI

Tests started from the[gcloud CLI](https://firebase.google.com/docs/test-lab/android/command-line), the[Testing API](https://firebase.google.com/docs/test-lab/reference/testing/rest), or[Gradle Managed Devices](https://firebase.google.com/docs/test-lab/android/android-studio#gmd-testlab-plugin)use aCloud Storagebucket created by Firebase by default. This requires the principal executing the test to have the "roles/editor" role for your firebase project.

If you cannot grant that role, or you want to retain detailed test results for longer than 90 days, you can send these test results to aCloud Storagebucket that you own using the[**--results-bucket**gcloud command-line option](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run).

When using your ownCloud Storagebucket:

1. Assign a pair of predefined roles, which grants the required set of permissions together, using the[Google Cloudconsole](https://cloud.google.com/iam/docs/granting-changing-revoking-access).
2. To allow a user to run tests withTest Lab, assign both: Firebase Test Lab Admin (`roles/cloudtestservice.testAdmin`) and Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)
3. To allow a user to view test results inTest Lab, assign both: Firebase Test Lab Viewer (`roles/cloudtestservice.testViewer`) and Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)

| **Caution:** Users assigned these predefined roles can access*all* Cloud Storagebuckets associated with the Firebase project, potentially including customer data.

## Enable permissions in Device Streaming

Device Streaming is a separate feature built on top ofTest Labdevices. It provides you with direct access toTest Labdevices. Firebase Editors and Admins can use Device Streaming without any additional roles, however, you can also provide more granular roles if necessary.

To allow a user to use device streaming, assign a predefined role which grants the required set of permissions together, using the[Google Cloudconsole](https://cloud.google.com/iam/docs/granting-changing-revoking-access). The role to assign is Firebase Test Lab Direct Access Admin (`roles/cloudtestservice.directAccessAdmin`).

For more information on Device Streaming in Android Studio, see[Device Streaming in Android Studio](https://developer.android.com/studio/preview/android-device-streaming).