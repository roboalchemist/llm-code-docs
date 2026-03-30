# Source: https://firebase.google.com/docs/projects/locations.md.txt

> [!CAUTION]
> **There's not a global project-level or app-level
> setting for location.**   
> Locations are set per product or per resource, and in some cases, per group of products. Usually, though, you set the location for each product and each resource independently from the others.
>
> Note that
> [some
> Firebase products and resources don't support location selection](https://firebase.google.com/support/privacy#data_storage_and_processing_locations).
> Also, you can optionally set an
> [organization-level location restriction](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)
> for products and resources that support location selection.

## Products or resources that require a location setting

Several products or resources require a location setting.

| **Product** | **Default location** | **Additional information** |
|---|---|---|
| **Firebase AI Logic** | - For Gemini Developer API: No location selection possible; always global. - For Vertex AI Gemini API: If location not set, the default region is `us-central1`. | This location is where you access the model. |
| **Google Analytics** | No default location. You must set this location. | This location is the Analytics reporting location^2^, which represents the country or region of your organization. Your Analytics reporting location, in turn, sets the currency for revenue reporting. |
| **Firebase App Hosting** | No default location. You must set this location for each backend. | This location is where App Hosting deployment creates each of your backend resources. Each backend can be in a different location. |
| **Firebase Data Connect** | No default location. You must set the location for each instance. | Each instance can be in a different location. |
| **Cloud Firestore** ^1^ | No default location. You must set the location for each instance. | Each instance can be in a different location. |
| **Firebase Realtime Database** | No default location. You must set the location for each instance. | Each instance can be in a different location. |
| **Cloud Storage for Firebase** ^1^ | No default location. You must set the location for each bucket. | Each bucket can be in a different location. |
| **Cloud Functions for Firebase** ^1^ | If location not set, the default region is `us-central1`. | Each function can be in a different location. |

^1^ Depending on when you initially started using these products in
your project, there can be location dependencies between these products. You
might see this dependency referred to as the
"location for default Google Cloud resources". Learn more about this
[location dependency](https://firebase.google.com/docs/projects/locations#default-cloud-location).

^2^ Your Analytics reporting location does *not* affect where
Google may process and store [customer data for Firebase](https://firebase.google.com/support/privacy).

## Set a location for a product or its resources

For a few products, you set the location at the product level. However, for most
products, you set the location at the resource level (for example, for each
Cloud Storage bucket or each function).

| **Product** | **When and how to set the location** | **Available locations** |
|---|---|---|
| **Firebase AI Logic** | - For Gemini Developer API: No location selection possible; always global. - For Vertex AI Gemini API: When you initialize the Vertex AI backend service in your codebase, you can optionally specify a location for where to access the model. If you don't specify a location, the default region is `us-central1`. | [Firebase AI Logic locations](https://firebase.google.com/docs/ai-logic/locations) |
| **Google Analytics** | When you enable Google Analytics in your Firebase project in the [Firebase console](https://console.firebase.google.com/), you're prompted to select an Analytics reporting location. You should select a country or region that represents the location of your organization. If you're a project Owner or Editor, you can later edit the time zone and the currency for your Analytics reporting location; go to your [Google Analytics settings](https://console.firebase.google.com/project/_/settings/integrations/analytics), then go to the *Reporting* pane. | See list in the [Google Analytics settings](https://console.firebase.google.com/project/_/settings/integrations/analytics) \> *Reporting* pane. |
| **Firebase App Hosting** | When you create an App Hosting backend, you're prompted to select a location. You can use the Firebase console, REST API, or Firebase CLI to create a backend. | [App Hosting locations](https://firebase.google.com/docs/app-hosting/about-app-hosting#locations) |
| **Firebase Data Connect** | When you provision a Data Connect service instance, you set its locations. You also set the location of the associated Google Cloud SQL instance. You can use the Firebase console or Firebase CLI to provision an instance. | [Data Connect service and Cloud SQL instance locations](https://firebase.google.com/docs/data-connect/manage-services-and-databases#configure-regions) |
| **Cloud Firestore ^1^** | When you provision a Cloud Firestore database instance, you set its location. You can use the Firebase console, REST API, Firebase CLI, or Terraform to provision an instance. | [Cloud Firestore locations](https://firebase.google.com/docs/firestore/locations) |
| **Firebase Realtime Database** | When you provision the Realtime Database instance, you set its location. You can use the Firebase console, REST API, Firebase CLI, or Terraform to provision an instance. | [Realtime Database locations](https://firebase.google.com/docs/database/locations) |
| **Cloud Storage for Firebase ^1^** | When you provision the Cloud Storage bucket, you set its location. You can use the Firebase console, REST API, or Terraform to provision a bucket. | [Cloud Storage for Firebase locations](https://firebase.google.com/docs/storage/locations) |
| **Cloud Functions for Firebase ^1^** | When you write a function, you can optionally set its region. If you don't specify a location, the default region is `us-central1`. | [Cloud Functions for Firebase locations](https://firebase.google.com/docs/functions/locations) |

^1^ Depending on when you initially started using these products in
your project, there can be location dependencies between these products. You
might see this dependency referred to as the
"location for default Google Cloud resources". Learn more about this
[location dependency](https://firebase.google.com/docs/projects/locations#default-cloud-location).

## View location settings

| **Product** | **Where to view the location setting** |
|---|---|
| **Firebase AI Logic** | - For Gemini Developer API: No location selection possible; always global. - For Vertex AI Gemini API: In your codebase, look for the initialization of the Vertex AI backend service. If a location isn't specified, then the default location is `us-central1`. |
| **Google Analytics** | In the Firebase console, go to settings *Project settings* \> *Integrations* \> [*Google Analytics*](https://console.firebase.google.com/project/_/settings/integrations/analytics). Click the account number to open your Google Analytics account, and then go to the **Admin** panel to find your account's location information. |
| **Firebase App Hosting** | - In the Firebase console, go to the [App Hosting page](https://console.firebase.google.com/project/_/apphosting) to view the list of your backends and their locations. - To view the location for a specific backend, you can use the Firebase CLI command `firebase apphosting:backends:get --project PROJECT_ID BACKEND_ID` |
| **Firebase Data Connect** | In the Firebase console, go to the [Data Connect page](https://console.firebase.google.com/project/_/dataconnect) to view the list of your database instances and their locations. |
| **Cloud Firestore** | In the Firebase console, go to the [Cloud Firestore *Data* tab](https://console.firebase.google.com/project/_/firestore/databases/_/data) to view the list of your database instances and their locations. |
| **Firebase Realtime Database** | In the Firebase console, go to the [Realtime Database *Data* tab](https://console.firebase.google.com/project/_/database/_/data) to view the list of your database instances and their locations. |
| **Cloud Storage for Firebase** | In the Firebase console, go to the [Cloud Storage *Files* tab](https://console.firebase.google.com/project/_/firestore/database) to view the list of your buckets and their locations. |
| **Cloud Functions for Firebase** | - Scheduled functions: In the Google Cloud console, go to [Cloud Scheduler](https://console.cloud.google.com/project/_/cloudscheduler) to view the list of topics for each job and function. The location is the last segment in the name of the topic. - Non-scheduled functions: In your function's source code, look for a `region` parameter. If a region isn't specified, then the default location is `us-central1`. |

## Possible location dependencies due to "location for default Google Cloud resources"

The "location for default Google Cloud resources" is the location setting
for any project resources associated with Google App Engine, including the
following:

- default Cloud Firestore database instance
- default Cloud Storage for Firebase bucket with the name format of `*.appspot.com`
- Google Cloud Scheduler used specifically with 1st gen scheduled functions

> [!NOTE]
> **Note:** None of the other resources in your project share this location dependency, including the following: Realtime Database instances, non-default Cloud Firestore instances, non-default Cloud Storage buckets, default Cloud Storage buckets with the name format of `*.firebasestorage.app`, non-scheduled functions, and 2nd gen scheduled functions.

This "location for default Google Cloud resources" is an immutable
setting. Also, when you set the location for one of the associated resources,
you indirectly set the location for all of them due to their common association
with App Engine.

However, with many changes to the Firebase and Google Cloud ecosystem over
the years, the associations of resources to App Engine have been
changing. Most notably, starting
October 30, 2024, all newly provisioned
default Cloud Storage for Firebase buckets have the name format
`*.firebasestorage.app`, and they are *not* associated
with App Engine.

> [!IMPORTANT]
> **Key Point:** Starting October 30, 2024, provisioning the default Cloud Storage for Firebase bucket does not set the "location for default Google Cloud resources" (like the location for the project's default Cloud Firestore instance). Also, provisioning the default Cloud Firestore instance no longer sets the location for a new default Cloud Storage for Firebase bucket (with name format of `*.firebasestorage.app`).

Here are the details of what changed in the possible **location dependencies**:

- Starting October 30, 2024, **if the
  default Cloud Firestore instance and the
  default Cloud Storage for Firebase bucket are *not* yet provisioned:**

  - Provisioning the default Cloud Firestore instance sets the location
    for any future App Engine app provisioned in the project.
    However, it does *not* dictate the location of the future
    default Cloud Storage bucket.

  - Provisioning the default Cloud Storage bucket *no longer* provisions
    an App Engine app. Thus, the location of the
    default Cloud Storage bucket does *not* dictate the location of the
    future default Cloud Firestore instance.

- Starting October 30, 2024, **if the default
  Cloud Firestore instance has *already* been provisioned, but the
  default Cloud Storage for Firebase bucket has *not* been provisioned:**

  - The existing default Cloud Firestore instance does *not* dictate the location of the future default Cloud Storage bucket (`*.firebasestorage.app`).
- Starting October 30, 2024, **if the
  default Cloud Storage for Firebase bucket has *already* been
  provisioned** (specifically, the
  `*.appspot.com` bucket)**, but the
  default Cloud Firestore instance has *not* been provisioned:**

  - Back when the default Cloud Storage bucket (`*.appspot.com`) was provisioned, an App Engine app was *also* provisioned, and thus the location of the future default Cloud Firestore instance was set at that time. Even if you delete the `*.appspot.com` bucket, you can't delete the App Engine app, so the location setting of the future default Cloud Firestore instance is already set.

If you used ***1st gen scheduled* functions** , then their location is set to the
location for default Google Cloud resources. This is because
Cloud Scheduler and App Engine previously had an association with
each other. Also, if you set up 1st gen scheduled functions *before*
provisioning other resources that shared this location setting, then you set
their location, too.


## Next steps

- For more information about building applications to meet your latency, availability, and durability requirements, refer to [Geography and Regions](https://cloud.google.com/docs/geography-and-regions#multi-regional_resources).