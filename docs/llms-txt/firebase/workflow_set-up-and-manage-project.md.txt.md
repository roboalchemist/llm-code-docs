# Source: https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project.md.txt

The [Firebase Management REST API](https://firebase.google.com/docs/reference/firebase-management/rest) enables
programmatic setup and management of Firebase projects, including a project's
Firebase resources and Firebase Apps.

This overview describes the general workflow to add Firebase resources and
apps to an existing [Google Cloud
project](https://cloud.google.com/resource-manager/reference/rest/v1/projects)
that doesn't yet use Firebase services.

You can jump to specific sections of this page if you just want to:

- [Add Firebase services to your project](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#add-firebase)
- [Add Firebase Apps to your Firebase project](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#add-apps)
- [Link your Firebase project to a Google Analytics account](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#link-ga-account)

Before following any steps on this page, make sure that you
[enable the API](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#enable-api).

For information about access management for the Firebase Management API, visit
the [Cloud Identity Access Management (IAM) API
documentation](https://cloud.google.com/iam/reference/rest/).

> [!NOTE]
> **Note:** If you don't already have an existing Google Cloud project, you can create one using the [`projects.create`](https://cloud.google.com/resource-manager/reference/rest/v1/projects/create) method in the [Google Cloud Resource Manager API](https://cloud.google.com/resource-manager/reference/rest/v1/projects) or by using the [Google Cloud console](https://console.cloud.google.com/).  
>
> Visit [Understand Firebase projects](https://firebase.google.com/docs/projects/learn-more#general-limits-projects-apps-sites) for details about the number of projects allowed per account.

## Before you begin

Before you begin, you'll need to [enable the Management API](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#enable-api) for
your Google Cloud project and
[generate your access token](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#generate-access-token).

### Enable the Management REST API for your Google Cloud project

If you haven't already, you'll need to enable the
[Firebase Management API](https://console.cloud.google.com/apis/library/firebase.googleapis.com)
for use with your Google Cloud project.

1. Open the [Firebase Management API](https://console.cloud.google.com/apis/library/firebase.googleapis.com) page in the Google APIs console.
2. When prompted, select your Google Cloud project.
3. Click **Enable** on the Firebase Management API page.

### Generate your API access token

Here's an example for Node.js that retrieves your access token.

First, if you aren't in a Google Cloud environment, set the
`GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path to your
service account key.

### Linux or macOS

    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"

### Windows

With PowerShell:

    $env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\service-account-file.json"

Then, use the Firebase Admin SDK to get an access token from your service
account credentials:

    import { initializeApp, applicationDefault } from "firebase-admin/app";

    initializeApp();

    async function getAccessToken() {
      try {
        const accessToken = await applicationDefault().getAccessToken();
        return accessToken.access_token;
      } catch (err) {
        console.error('Unable to get access token');
        console.error(err);
      }
    }

### Find the resource name of your project

You can find the Google Cloud projects which are available for adding Firebase
services.

> [!NOTE]
> To call this endpoint:
>
> - You must have an existing Google Cloud project and an [API access token](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#generate-access-token).
> - A project member must be a [Viewer](https://firebase.google.com/docs/projects/iam/roles), at minimum, of the existing Google Cloud project.

#### REQUEST

Call
[`availableProjects.list`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/availableProjects/list).
The request body for this call must be empty.

Here's an example for Node.js to request a list of available Google Cloud
projects:

    const fetch = require('node-fetch');

    async function listProjects() {
      const accessToken = getAccessToken();
      const uri = 'https://firebase.googleapis.com/v1beta1/availableProjects';
      const options = {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + accessToken,
        },
      };

      try {
        const rawResponse = await fetch(uri, options);
        const resp = await rawResponse.json();
        const projects = resp['projectInfo'];
        console.log('Project total: ' + projects.length);
        console.log('');
        for (let i in projects) {
          const project = projects[i];
          console.log('Project ' + i);
          console.log('ID: ' + project['project']);
          console.log('Display Name: ' + project['displayName']);
          console.log('');
        }
      } catch(err) {
        console.error(err);
      }
    }

#### RESULT

The response body from a call to `availableProjects.list` contains a list of
[`ProjectInfo`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/availableProjects/list#ProjectInfo)
objects. If the list of projects is too long, the response body also contains a
`nextPageToken` that you can use as a query parameter to get the next page of
projects.

Here's an example response body of an `availableProjects.list` call:

    {
      "projectInfo": [
        {
          "project": "projects/first-cloud-project",
          "displayName": "First Cloud Project"
        },
        {
          "project": "projects/second-cloud-project",
          "displayName": "Second Cloud Project"
        }
      ]
    }

This example response has two Google Cloud projects that can have Firebase
services added to them. Note that the `project` field provides the globally
unique resource name for a project.

You can use any `project` value listed in the response from
`availableProjects.list` to [add Firebase services](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#add-firebase) or
[add apps](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#add-apps) to your project.

In the next section, we'll add Firebase services to `First Cloud Project` using
the `projects/first-gcp-project` resource name.

## Add Firebase services to your project

Google Cloud projects can take advantage of the services offered by Firebase. In
this section, you'll learn how to add Firebase services to your existing
Google Cloud project programmatically. Note that you can also add Firebase
services to your existing Google Cloud project in the [Firebase console](https://console.firebase.google.com/).

> [!NOTE]
> To call this endpoint:
>
> - You must have an existing Google Cloud project, an [API access token](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#generate-access-token), and the unique [resource name](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#find-resource-name) of your `project`.
> - A project member or service account must have the following permissions. If you are an [Editor or Owner](https://firebase.google.com/docs/projects/iam/roles) of the existing Google Cloud project, then you have these permissions.   
>   `firebase.projects.update`  
>   `resourcemanager.projects.get`  
>   `serviceusage.services.enable`  
>   `serviceusage.services.get`

#### REQUEST

Call
[`projects.addFirebase`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase).
The request body for this call must be empty.

Here's an example for Node.js to add Firebase services to your Google Cloud
project:

    const fetch = require('node-fetch');

    async function addFirebase(projectId) {
      const accessToken = getAccessToken();
      const uri = 'https://firebase.googleapis.com/v1beta1/projects/' + projectId + ':addFirebase';
      const options = {
        method: 'POST',
        // Use a manual access token here since explicit user access token is required.
        headers: {
          'Authorization': 'Bearer ' + accessToken,
        },
      };

      try {
        const rawResponse = await fetch(uri, options);
        const resp = await rawResponse.json();
        console.log(resp);
      } catch(err) {
        console.error(err['message']);
      }
    }

#### RESULT

The result of a call to `projects.addFirebase` is an
[`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations). Before you
can call other Firebase-related endpoints for your project, the operation must
be successful.

To check if the operation is successful, you can call
[`operations.get`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations/get)
on the operation until the value of `done` is `true` and its `response` is of
type `FirebaseProject`. If the operation fails, its `error` is set to
`google.rpc.Status`.

Here's the response body of an `operations.get` call:

    {
      "name": "operations/...",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.firebase.service.v1beta1.FirebaseProject",
        "projectId": "first-cloud-project",
        "projectNumber": "...",
        "displayName": "First Cloud Project",
        "name": "projects/first-cloud-project",
        "resources": {
          "hostingSite": "first-cloud-project",
          "realtimeDatabaseInstance": "first-cloud-project"
        }
      }
    }

Since `done` is `true` and the `response` type is a `FirebaseProject`, the
Google Cloud project now has Firebase services. The response also contains
other useful information about your newly created `FirebaseProject`, like its
`projectNumber` and its default `resources`. The `Operation` is automatically
deleted after completion.

## Add Firebase Apps to your project

Many different apps can use a `FirebaseProject`, including iOS, Android, and web
apps. In this section, you'll learn how to add Firebase Apps to your existing
`FirebaseProject` programmatically. Note that you can also add Firebase Apps to
your existing Firebase project in the [Firebase console](https://console.firebase.google.com/).

> [!NOTE]
> To call the endpoints in this section:
>
> - You must have an [API access token](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#generate-access-token) and an existing [`FirebaseProject`](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#add-firebase).
> - A project member must be an [Editor or Owner](https://firebase.google.com/docs/projects/iam/roles) of the existing Firebase project.

**Select a type of Firebase App to add to your Firebase project.**

### iOS+

You can add a **Firebase iOS App** to your existing Firebase project.

#### REQUEST

Call
[`projects.iosApps.create`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/create).
Here's how to construct your request body:

- Required:

  - `bundleId`: The canonical bundle ID of the iOS app as it would appear in the iOS App Store.
- Optional, but recommended:

  - `displayName`: The user-assigned display name of the app. This value is
    useful for finding the app later in the [Firebase console](https://console.firebase.google.com/).

  - `appStoreId`: The automatically generated Apple ID assigned to your app by
    Apple. Specify an `appStoreId` if it has already been assigned by Apple.

In the request body for our example, we'll only use a `displayName` and
`bundleId`:

    {
      "displayName": "My Firebase iOS App",
      "bundleId": "com.firebase.ios"
    }

Here's an example for Node.js to add a Firebase iOS App to your Firebase
project:

    const fetch = require('node-fetch');

    async function addIosApp(projectId, displayName, bundleId) {
      const accessToken = getAccessToken();
      const uri = 'https://firebase.googleapis.com/v1beta1/projects/' + projectId + '/iosApps';
      const options = {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer ' + accessToken,
        },
        body: JSON.stringify({
          'displayName': displayName,
          'bundleId': bundleId
        }),
      };

      try {
        const rawResponse = await fetch(uri, options);
        const resp = await rawResponse.json();
        console.log(resp);
      } catch(err) {
        console.error(err['message']);
      }
    }

#### RESULT

The result of a call to `projects.iosApps.create` is an
[`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations). Before you
can call other Firebase-related endpoints for your project, the operation must
be successful.

To check if the operation is successful you can call
[`operations.get`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations/get)
on the operation until the value of `done` is `true` and its `response` is of
type `IosApp`. If the operation fails, its `error` is set to
`google.rpc.Status`.

Here's the response body of an `operations.get` call:

    {
      "name": "operations/...",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.firebase.service.v1beta1.IosApp",
        "name": "projects/first-cloud-project/iosApps/...",
        "appId": "...",
        "displayName": "My Firebase iOS App",
        "projectId": "first-cloud-project",
        "bundleId": "com.firebase.ios"
      }
    }

Since `done` is `true` and the `response` type is an `IosApp`, the
`FirebaseProject` now has an `IosApp`. The response also contains other useful
information about your newly created Firebase iOS App, like the unique Firebase
`appId`. The `Operation` is automatically deleted after completion.

### Android

You can add a **Firebase Android App** to your existing Firebase project.

#### REQUEST

Call
[`projects.androidApps.create`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/create).
Here's how to construct your request body:

- Required:

  - `packageName`: The canonical package name of the Android app as it would appear in the Google Play Developer console.
- Optional, but recommended:

  - `displayName`: The user-assigned display name of the app. This value is useful for finding your app later in the [Firebase console](https://console.firebase.google.com/).

In the request body for our example, we'll use `packageName` and
`displayName`:

    {
      "displayName": "My Firebase Android App"
      "packageName": "com.firebase.android"
    }

Here's an example for Node.js to add a Firebase Android App to your Firebase
project:

    const fetch = require('node-fetch');

    async function addAndroidApp(projectId, displayName, packageName) {
      const accessToken = getAccessToken();
      const uri = 'https://firebase.googleapis.com/v1beta1/projects/' + projectId + '/androidApps';
      const options = {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer ' + accessToken,
        },
        body: JSON.stringify({
          'displayName': displayName,
          'packageName': packageName
        }),
      };

      try {
        const rawResponse = await fetch(uri, options);
        const resp = await rawResponse.json();
        console.log(resp);
      } catch(err) {
        console.error(err['message']);
      }
    }

#### RESULT

The result of a call to `projects.androidApps.create` is an
[`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations). Before you
can call other Firebase-related endpoints for your project, the operation must
be successful.

To check if the operation is successful, you can call
[`operations.get`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations/get)
on the operation until the value of `done` is `true` and its `response` is of
type `AndroidApp`. If the operation fails, its `error` is set to
`google.rpc.Status`.

Here's the response body of an `operations.get` call:

    {
      "name": "operations/...",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.firebase.service.v1beta1.AndroidApp",
        "name": "projects/first-cloud-project/androidApps/...",
        "appId": "...",
        "displayName": "My Firebase Android App",
        "projectId": "first-cloud-project",
        "packageName": "com.firebase.android"
      }
    }

Since `done` is `true` and the `response` type is an `AndroidApp`, the
`FirebaseProject` now has an `AndroidApp`. The response also contains other
useful information about your newly created Firebase Android App, like the
unique Firebase `appId`. The `Operation` is automatically deleted after
completion.

#### Add SHA certificates

You can add SHA certificates to any existing Firebase Android App by calling
[`projects.androidApps.sha.create`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/create).
The request body for this method call must have an empty `name` field.
The result of this call is a newly created instance of
[`ShaCertificate`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate).

When calling `projects.androidApps.sha.create`, you need to provide a valid
SHA-1 or SHA-256 certificate hash. You can get the SHA hash of your signing
certificate with the gradle `signingReport` command:

```
./gradlew signingReport
```

<br />

For more information, visit [Google APIs for
Android](https://developers.google.com/android/guides/client-auth).

### Web

You can add a **Firebase Web App** to your existing Firebase project.

#### REQUEST

Call
[`projects.webApps.create`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/create).
Here's how to construct your request body:

- Optional:

  - `displayName`: The user-assigned display name of app. This value is useful for finding your app later in the [Firebase console](https://console.firebase.google.com/).
- *Not* recommended:

  - `appUrls`: The fully qualified URLs where the app is hosted. When a Firebase Web App is associated with a Firebase Hosting site, Firebase automatically populates these fields, so leave these fields empty in your request body.

We'll only specify a `displayName` in the request body for our example:

    {
      "displayName": "My Firebase Web App"
    }

Here's an example for Node.js to add a Firebase Web App to your Firebase
project:

    const fetch = require('node-fetch');

    async function addWebApp(projectId, displayName) {
      const accessToken = getAccessToken();
      const uri = 'https://firebase.googleapis.com/v1beta1/projects/' + projectId + '/webApps';
      const options = {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer ' + accessToken,
        },
        body: JSON.stringify({
          'displayName': displayName
        }),
      };

      try {
        const rawResponse = await fetch(uri, options);
        const resp = await rawResponse.json();
        console.log(resp);
      } catch(err) {
        console.error(err['message']);
      }
    }

#### RESULT

The result of a call to `projects.webApps.create` is an
[`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations). Before you
can call other Firebase-related endpoints for your project, the operation must
be successful.

To check if the operation is successful you can call
[`operations.get`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations/get)
on the operation until the value of `done` is `true` and its `response` is of
type `WebApp`. If the operation fails, its `error` is set to
`google.rpc.Status`.

Here's the response body of an `operations.get` call:

    {
      "name": "operations/...",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.firebase.service.v1beta1.WebApp",
        "name": "projects/first-cloud-project/webApps/...",
        "appId": "...",
        "displayName": "My Firebase Web App",
        "projectId": "first-cloud-project"
      }
    }

Since `done` is `true` and the `response` type is a `WebApp`, the
`FirebaseProject` now has a `WebApp`. The response also contains other useful
information about your newly created Firebase Web App, like the unique Firebase
`appId`. The `Operation` is automatically deleted after completion.

## Link your Firebase project to a Google Analytics account (Optional)

You can link an existing
[Google Analytics account](http://www.google.com/analytics/) to your existing
`FirebaseProject` programmatically. Note that you can also link your existing
Firebase project to Google Analytics in the
[**Integrations**](https://console.firebase.google.com/project/_/settings/integrations)
tab of your **Project Settings**.

> [!NOTE]
> To call this endpoint:
>
> - You must have an [API access token](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#generate-access-token) and an existing [`FirebaseProject`](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#add-firebase).
> - A project member must be an [Owner](https://firebase.google.com/docs/projects/iam/roles) of the existing Firebase project.

The call to `projects.addGoogleAnalytics` requires an `analytics_resource`,
which can either be an `analyticsAccountId` or an `analyticsPropertyId`:

- Specify an existing `analyticsAccountId` to provision a new Google Analytics
  property within the specified account and associate the new property with your
  Firebase project.

- Specify an existing `analyticsPropertyId` to associate the Google Analytics
  property with your Firebase project.

You can find both your `analyticsAccountId` and any existing
`analyticsPropertyId` on the [Google Analytics
website](https://analytics.google.com/analytics/web/).

**When you call `projects.addGoogleAnalytics`:**

1. The first check determines if any existing data streams in the Google
   Analytics property correspond to any existing Firebase Apps in your
   `FirebaseProject` (based on the `packageName` or `bundleId` associated with
   the data stream). Then, as applicable, the data streams and apps are linked.
   Note that this auto-linking only applies to Android Apps and iOS Apps.

2. If no corresponding data streams are found for your Firebase Apps, new data
   streams are provisioned in the Google Analytics property for each of your
   Firebase Apps. Note that a new data stream is always provisioned for a Web
   App even if it was previously associated with a data stream in your
   Analytics property.

Learn more about the hierarchy and structure of Google Analytics accounts in the
[Analytics documentation](https://support.google.com/analytics/answer/9303323).

> [!NOTE]
> **Note:** If you have Firebase Web Apps in your Firebase project before linking your project with Google Analytics, the Firebase configuration objects for those apps will be updated with a new `measurementId` field. This updated config object is required for your Web App to use Analytics. Call [`projects.webApps.getConfig`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/getConfig) to obtain updated config objects.

#### REQUEST

Call
[`projects.addGoogleAnalytics`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addGoogleAnalytics).

In the request body for our example call to `project.addGoogleAnalytics`, we'll
specify our Google Analytics account `analyticsAccountId`. This call will
provision a new Google Analytics property and associate the new property with
the `FirebaseProject`.

    {
      "analyticsAccountId": "<your-google-analytics-account-id>"
    }

Here's an example for Node.js to link a Firebase project with a Google Analytics
account:

    const fetch = require('node-fetch');

    async function addGoogleAnalytics(projectId, analyticsAccountId) {
      const accessToken = getAccessToken();
      const uri = 'https://firebase.googleapis.com/v1beta1/projects/' + projectId + ':addGoogleAnalytics';
      const options = {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer ' + accessToken,
        },
        body: JSON.stringify({
          'analyticsAccountId': analyticsAccountId
        }),
      };

      try {
        const rawResponse = await fetch(uri, options);
        const resp = await rawResponse.json();
        console.log(resp);
      } catch(err) {
        console.error(err['message']);
      }
    }

#### RESULT

The result of a call to `projects.addGoogleAnalytics` is an
[`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations). Before you
can call other Firebase-related endpoints for your project, the operation must
be successful.

To check if the operation is successful, you can call `operations.get` on the
operation until the value of `done` is `true` and the `response` is of type
`analyticsDetails`. If the operation fails, its `error` is set to
`google.rpc.Status`.

Here's the response body of an `operations.get` call:

    {
      "name": "operations/...",
      "none": true,
      "response": {
        "@type": "type.googleapis.com/google.firebase.service.v1beta1.AnalyticsDetails",
        "analyticsProperty": [
          {
            "id": "...",
            "displayName": "..."
          }
        ],
        "streamMappings": [
          {
            "app": "...",
            "streamId": "...",
            "measurementId": "..."
          }
        ]
      }
    }

Since `done` is true and the `response` type is `analyticsDetails`, the
`FirebaseProject` is now linked to the specified Google Analytics account. The
`Operation` is automatically deleted after completion.