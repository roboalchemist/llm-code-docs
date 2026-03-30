# Source: https://firebase.google.com/docs/projects/bigquery-export.md.txt

Firebase provides tools in the Firebase console to explore and analyze
historical data about your apps that use Firebase products. These tools can help
you answer many questions about how your apps are being used. Sometimes, though,
you also want to set up your own queries to answer your own questions.

You can do this by exporting data from various Firebase products into
[BigQuery](https://bigquery.cloud.google.com). With
BigQuery, you can analyze your data with BigQuery SQL or
export the data to use with your own tools.

The following products support data export to BigQuery:

- [Google Analytics](https://firebase.google.com/docs/analytics#integrations_with_other_services)
- [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/understand-delivery#bigquery-data-export)
- [Crashlytics](https://firebase.google.com/docs/crashlytics/bigquery-export)
- [Performance Monitoring](https://firebase.google.com/docs/perf-mon/bigquery-export)
- [A/B Testing](https://firebase.google.com/docs/ab-testing/abtest-config#bigquery_data_export)
- [Remote Config personalization](https://firebase.google.com/docs/remote-config/personalization/bigquery)

## Required permissions and suggested roles

To view or manage settings for data export to BigQuery, you must have
the required level of access.

If you don't have the necessary Firebase access, you can ask a Firebase
project Owner to assign you the applicable role via the
[Firebase console IAM settings](https://console.firebase.google.com/project/_/settings/iam).
If you have questions about accessing your Firebase project,
including finding or assigning an Owner, review the
[Permissions and access to Firebase projects FAQs](https://firebase.google.com/support/faq#projects-permissions-and-access).

<br />

#### Project-level

<br />

The following table applies to the top-level linking of a Firebase project to
BigQuery.

| **Action in Firebase console** | **Required IAM permission** | **IAM role(s) that include required permissions by default** | **Additional required roles** |
|---|---|---|---|
| Link a Firebase project and BigQuery | `firebase.links.create` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) | none |
| Unlink a Firebase project and BigQuery | `firebase.links.delete` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) | none |
| View the existing links for BigQuery | `firebase.links.list` | - Any [basic role](https://firebase.google.com/docs/projects/iam/roles-basic) (Owner, Editor, or Viewer) - Any [Firebase-level role](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) - Any [Firebase product-category role](https://firebase.google.com/docs/projects/iam/roles-predefined-category) | none |

<br />

<br />

<br />

#### Google Analytics

<br />

The following table applies specifically to the export of
Google Analytics data to BigQuery.

| **Action in Firebase console** | **Required IAM permission** | **IAM role(s) that include required permissions by default** | **Additional required roles** |
|---|---|---|---|
| Enable export of Google Analytics data to BigQuery | `firebase.links.update` AND `serviceusage.services.enable` AND `resourcemanager.projects.getIamPolicy` AND `resourcemanager.projects.setIamPolicy` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) AND [Service Usage Admin](https://cloud.google.com/service-usage/docs/access-control#predefined_roles) AND [Project IAM Admin](https://cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectIamAdmin) | - [Google Analytics](https://support.google.com/analytics/answer/9289234#access): Equivalent of account Administrator or Editor for the linked Google Analytics property - [See note below](https://firebase.google.com/docs/projects/bigquery-export#note-enable-disable-export-in-ga-ui). |
| Enable export for specific Firebase apps | `firebase.links.update` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) | - [Google Analytics](https://support.google.com/analytics/answer/9289234#access): Equivalent of account Administrator or Editor for the linked Google Analytics property - [See note below](https://firebase.google.com/docs/projects/bigquery-export#note-enable-disable-export-in-ga-ui). |
| Disable export for specific Firebase apps | `firebase.links.update` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) | - [Google Analytics](https://support.google.com/analytics/answer/9289234#access): Equivalent of account Administrator or Editor for the linked Google Analytics property - [See note below](https://firebase.google.com/docs/projects/bigquery-export#note-enable-disable-export-in-ga-ui). |

> [!NOTE]
> **Note:** To enable or disable export in the Google Analytics UI, you need the [explicit Administrator or Editor role](https://support.google.com/analytics/answer/9305587#zippy=google-analytics) for the linked Google Analytics property. However, Firebase access is not required.

<br />

<br />

<br />

#### Firebase products

<br />

The following table applies to any of the Firebase products for which you can
export data to BigQuery, for example, Crashlytics or Performance Monitoring.

| **Action in Firebase console** | **Required IAM permission** | **IAM role(s) that include required permissions by default** | **Additional required roles** |
|---|---|---|---|
| Enable export of a product's data to BigQuery | `firebase.links.update` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) | none |
| Enable export for specific Firebase apps | `firebase.links.update` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) | none |
| Disable export for specific Firebase apps | `firebase.links.update` | - [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) - [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) | none |

<br />

<br />

<br />

*** ** * ** ***

## Set up export to BigQuery

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Integrations** tab](https://console.firebase.google.com/u/0/project/_/settings/integrations).

4. On the **BigQuery** integration card, click **Link**.

5. Follow the on-screen instructions to set up export to BigQuery.

### Unlink from BigQuery

Unlinking from BigQuery stops the corresponding dataset(s) in
BigQuery from being populated.

Be aware of the following:

- Any data already exported into BigQuery will persist for the allowed
  retention time, and storage and query charges may still apply. You can
  manually delete your dataset(s) to prevent any further billing.

- If you have BigQuery data stored in other services, that data might
  be governed by different terms for data persistence.

You can unlink from BigQuery at the Firebase project level, at the
product-level, or at the app-level for a specific product.

> [!CAUTION]
> **Caution:** Unlinking your Firebase project from BigQuery stops ***all*** data export from any Firebase product (and if applicable, Google Analytics) for which you've set up export to BigQuery.

**Here's how to unlink from BigQuery:**

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **BigQuery** card, click **Manage**.

3. Choose to unlink a specific product or to unlink specific apps for
   a specific product.

   To unlink your Firebase project entirely, find the button at the bottom of
   the page.
4. When prompted, confirm that you want to stop exports.

<br />

*** ** * ** ***

## What happens when you enable export?

- You select the dataset location. After the dataset is created, the location
  can't be changed, but you can copy the dataset to a different location
  or manually move (recreate) the dataset in a different location. To learn
  more, see
  [Change the location for existing exports](https://firebase.google.com/docs/projects/bigquery-export#change-dataset-location).

  This location is only applicable for the data exported into BigQuery,
  and it does not impact the location of data stored for use in the
  Firebase console.
- By default, all apps in your project are linked to BigQuery and
  any apps that you later add to the project are automatically linked to
  BigQuery. You can
  [manage which apps send data](https://support.google.com/firebase/answer/6318765#manage).

- Firebase exports a copy of your existing data to BigQuery. The
  initial propagation of data for export may take up to 48 hours.

- Firebase sets up daily syncs of your data to BigQuery.

  - After you link your project, you usually need to wait until the next day's
    sync for your first set of data to be exported to BigQuery.

  - The daily sync happens once per day, regardless of any scheduled export
    that you might have set up in BigQuery. Note that the timing and
    duration of the sync job can change, so we don't recommend scheduling
    downstream operations or jobs based on a specific timing of the export.

  > [!NOTE]
  > **Note:** Exports of Google Analytics data into BigQuery are limited to 1 million events per day. You can use event filtering to limit the number of events that are exported. To learn more, see [Data filtering](https://support.google.com/analytics/answer/9823238#datafiltering). There is no limit for Google Analytics 360 users.

<br />

*** ** * ** ***

## Change the location for existing exports

After you set up a product for export to BigQuery and create a dataset,
you can't change the location of that dataset. However, you can copy your
existing dataset to a new dataset that has a different location and reset your
data export to that new location. Learn about
[BigQuery dataset locations](https://cloud.google.com/bigquery/docs/locations).

> [!CAUTION]
> Make sure that you follow all of the instructions in these procedures; overlooking a step might result in data loss.

**Select the product for which you want to change the location for data
export**

### Google Analytics

<br />

To change the location of an existing Google Analytics export to
BigQuery,
follow these instructions:

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).
   Then do the following:

   1. In the BigQuery card, click **Manage**.
   2. Toggle off the Google Analytics slider to disable BigQuery.
2. In the Google Cloud console, go to the
   [BigQuery page](https://console.cloud.google.com/bigquery).
   Then do the following:

   1. Create a temporary dataset to store a copy of the existing data from your original dataset. Assign the temporary dataset a *different name* than the name of the original dataset.
   2. [Copy](https://cloud.google.com/bigquery/docs/copying-datasets) or [move](https://cloud.google.com/bigquery/docs/managing-datasets#moving_datasets) the data from your original dataset to the temporary dataset.
   3. Delete the original dataset.
   4. Create a new, permanent dataset with the *same name* as your original dataset (`analytics_ANALYTICS_PROPERTY_ID`), then select the new region.
   5. Copy or move the data from the temporary dataset to the new dataset, then delete the temporary dataset.
3. Go back to the Firebase console and the
   [BigQuery card](https://console.firebase.google.com/project/_/settings/integrations/bigquery).
   Then do the following:

   1. Toggle on the Google Analytics slider to re-enable the BigQuery integration.
   2. Select the apps for which you want to enable the export.

### Cloud Messaging

<br />

To change the location of an existing Cloud Messaging export to
BigQuery,
follow these instructions:

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).
   Then do the following:

   1. In the BigQuery card, click **Manage**.
   2. Toggle off the Cloud Messaging slider to disable BigQuery.
2. In the Google Cloud console, go to the
   [BigQuery page](https://console.cloud.google.com/bigquery).
   Then do the following:

   1. Create a temporary dataset to store a copy of the existing data from your original dataset. Assign the temporary dataset a *different name* than the name of the original dataset.
   2. [Copy](https://cloud.google.com/bigquery/docs/copying-datasets) or [move](https://cloud.google.com/bigquery/docs/managing-datasets#moving_datasets) the data from your original dataset to the temporary dataset.
   3. Delete the original dataset.
   4. Create a new, permanent dataset with the *same name* as your original dataset (`firebase_messaging`), then select the new region.
   5. Copy or move the data from the temporary dataset to the new dataset, then delete the temporary dataset.
3. Go back to the Firebase console and the
   [BigQuery card](https://console.firebase.google.com/project/_/settings/integrations/bigquery).
   Then do the following:

   1. Toggle on the Cloud Messaging slider to re-enable the BigQuery integration.
   2. Select the apps for which you want to enable the export.
4. Go back to the Google Cloud console and the
   [BigQuery page](https://console.cloud.google.com/bigquery/transfers)
   to verify that a transfer configuration is created for
   Cloud Messaging in the new region.

### Crashlytics

<br />

To change the location of an existing Crashlytics export to
BigQuery,
follow these instructions:

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).
   Then do the following:

   1. In the BigQuery card, click **Manage**.
   2. Toggle off the Crashlytics slider to disable BigQuery.
2. In the Google Cloud console, go to the
   [BigQuery page](https://console.cloud.google.com/bigquery).
   Then do the following:

   1. Create a temporary dataset to store a copy of the existing data from your original dataset. Assign the temporary dataset a *different name* than the name of the original dataset.
   2. [Copy](https://cloud.google.com/bigquery/docs/copying-datasets) or [move](https://cloud.google.com/bigquery/docs/managing-datasets#moving_datasets) the data from your original dataset to the temporary dataset.
   3. Delete the original dataset.
   4. Create a new, permanent dataset with the *same name* as your original dataset (`firebase_crashlytics`), then select the new region.
   5. Copy or move the data from the temporary dataset to the new dataset, then delete the temporary dataset.
3. Go back to the Firebase console and the
   [BigQuery card](https://console.firebase.google.com/project/_/settings/integrations/bigquery).
   Then do the following:

   1. Toggle on the Crashlytics slider to re-enable the BigQuery integration.
   2. Select the apps for which you want to enable the export.
4. Go back to the Google Cloud console and the
   [BigQuery page](https://console.cloud.google.com/bigquery/transfers)
   to verify that a transfer configuration is created for
   Crashlytics in the new region.

### Performance Monitoring

<br />

To change the location of an existing Performance Monitoring export to
BigQuery,
follow these instructions:

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).
   Then do the following:

   1. In the BigQuery card, click **Manage**.
   2. Toggle off the Performance Monitoring slider to disable BigQuery.
2. In the Google Cloud console, go to the
   [BigQuery page](https://console.cloud.google.com/bigquery).
   Then do the following:

   1. Create a temporary dataset to store a copy of the existing data from your original dataset. Assign the temporary dataset a *different name* than the name of the original dataset.
   2. [Copy](https://cloud.google.com/bigquery/docs/copying-datasets) or [move](https://cloud.google.com/bigquery/docs/managing-datasets#moving_datasets) the data from your original dataset to the temporary dataset.
   3. Delete the original dataset.
   4. Create a new, permanent dataset with the *same name* as your original dataset (`firebase_performance`), then select the new region.
   5. Copy or move the data from the temporary dataset to the new dataset, then delete the temporary dataset.
3. Go back to the Firebase console and the
   [BigQuery card](https://console.firebase.google.com/project/_/settings/integrations/bigquery).
   Then do the following:

   1. Toggle on the Performance Monitoring slider to re-enable the BigQuery integration.
   2. Select the apps for which you want to enable the export.
4. Go back to the Google Cloud console and the
   [BigQuery page](https://console.cloud.google.com/bigquery/transfers)
   to verify that a transfer configuration is created for
   Performance Monitoring in the new region.

<br />

*** ** * ** ***

## Pricing and the BigQuery sandbox

If your Firebase project is on the no-cost Spark pricing plan, you can use the
[BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox),
which provides no-cost access to BigQuery. For information about the
BigQuery sandbox and its capabilities, see
[Using the BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox#limits).

If your Firebase project is on the pay-as-you-go Blaze pricing plan, you can use all the
features of BigQuery. Your use of BigQuery is subject to
[BigQuery pricing](https://cloud.google.com/bigquery/pricing),
which includes limited no-cost use.