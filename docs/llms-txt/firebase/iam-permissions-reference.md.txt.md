# Source: https://firebase.google.com/docs/test-lab/android/iam-permissions-reference.md.txt

# IAM permissions reference guide

This document provides reference information about configuring Test Lab IAM
permissions and roles. If you want to configure more granular roles, Test Lab
provides permissions for both executing tests and streaming devices using
Android Studio. Test execution has extra requirements to properly configure
permissions and roles for IAM and the streaming devices.

## Test Execution

To properly configure Test Lab so that you can execute and read the results
of tests, you have to configure access to Cloud Storage buckets. This
requires a specific configuration of permissions that aren't all included in the
standard [Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined). To
grant access to Test Lab, use one of the following options.

### Tests through the Firebase console

For tests started from Firebase console or through the [Firebase Test Lab Device Matrix in Android Studio](https://developer.android.com/studio/test/test-in-android-studio#run-with-firebase-test-lab):

1. Test your app in a dedicated separate Firebase project.
2. Add users that need Test Lab access and assign them legacy project roles using the [Firebase console](https://console.firebase.google.com/).
3. (Optional) Assign the **Editor** project role to allow a user to run tests with Test Lab.
4. (Optional) Assign the **Viewer** project role to allow a user to view test results with Test Lab.

### Tests through gcloud CLI

Tests started from the [gcloud CLI](https://firebase.google.com/docs/test-lab/android/command-line),
the [Testing API](https://firebase.google.com/docs/test-lab/reference/testing/rest), or [Gradle Managed
Devices](https://firebase.google.com/docs/test-lab/android/android-studio#gmd-testlab-plugin) use a
Cloud Storage bucket created by Firebase by default. This requires the
principal executing the test to have the "roles/editor" role for your firebase
project.

If you cannot grant that role, or you want to retain detailed test results for
longer than 90 days, you can send these test results to a Cloud Storage
bucket that you own using the
[**--results-bucket** gcloud command-line option](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run).

When using your own Cloud Storage bucket:

1. Assign a pair of predefined roles, which grants the required set of permissions together, using the [Google Cloud console](https://cloud.google.com/iam/docs/granting-changing-revoking-access).
2. To allow a user to run tests with Test Lab, assign both: Firebase Test Lab Admin (`roles/cloudtestservice.testAdmin`) and Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)
3. To allow a user to view test results in Test Lab, assign both: Firebase Test Lab Viewer (`roles/cloudtestservice.testViewer`) and Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)

> [!CAUTION]
> **Caution:** Users assigned these predefined roles can access *all* Cloud Storage buckets associated with the Firebase project, potentially including customer data.

## Enable permissions in Device Streaming

Device Streaming is a separate feature built on top of Test Lab devices. It
provides you with direct access to Test Lab devices. Firebase Editors and
Admins can use Device Streaming without any additional roles, however, you can
also provide more granular roles if necessary.

To allow a user to use device streaming, assign a predefined role which grants
the required set of permissions together, using the [Google Cloud console](https://cloud.google.com/iam/docs/granting-changing-revoking-access)
. The role to assign is Firebase Test Lab Direct Access
Admin (`roles/cloudtestservice.directAccessAdmin`).

For more information on Device Streaming in Android Studio, see [Device Streaming in Android Studio](https://developer.android.com/studio/preview/android-device-streaming).