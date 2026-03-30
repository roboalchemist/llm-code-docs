# Source: https://developers.webflow.com/browser/data-exports/destinations/google-cloud-storage.mdx

***

title: Google Cloud Storage
slug: data-exports/destinations/google-cloud-storage
description: Configure Google Cloud Storage as a destination for Data Exports
-----------------------------------------------------------------------------

This guide walks you through configuring Google Cloud Storage as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* By default, GCS authentication uses role-based access. You will need to use the Webflow Data Sync Service Account email to grant access: `datasync-webflow@prql-prod.iam.gserviceaccount.com`.

## Configuration steps

<Steps>
  ### Create a service account

  1. In the GCP console, navigate to the **IAM & Admin** menu, click into the **Service Accounts** tab, and click **Create service account** at the top of the menu.
  2. In the first step, name the service account that will be used to transfer data into Cloud Storage and click **Create and Continue**. Click **Continue** in the following optional step without assigning any roles.
  3. In the **Grant users access to this service account** step, within the **Service account users role** field, enter the provided **Service account** (see prerequisite) and click **Done**.
  4. Once successfully created, search for the created service account in the service accounts list, click the **Service account** name to view the details, and make a note of the **email** (note: this is a different email the Webflow Data Sync Service Account).
  5. Select the permissions tab, find the provided principal name (**Service account** from the prerequisite), click the **Edit principal** button (pencil icon), click **Add another role**, select the **Service Account Token Creator** role, and click **Save**.

     ![Grant role](https://storage.googleapis.com/prequel_docs/images/gcp-grant-role.png)

     <Warning>
       **Alternative authentication method: HMAC Access Key & Secret**

       Role-based authentication is the preferred authentication mode for Google Cloud Storage based on GCP recommendations. However, HMAC Access Key ID & Secret Access Key is an alternative authentication method that can be used if preferred. An HMAC key is a type of credential and can be associated with a service account or a user account to access Google Cloud Storage.

       1. Navigate to the **Cloud Storage** page.

       2. Click into the **Settings** tab on the left side menu.

          ![GCS bucket settings](https://storage.googleapis.com/prequel_docs/images/gcs-bucket-settings.png)

       3. Navigate to the **Interoperability** tab and click the **Create a key for a Service Account** button.

       4. Select the **Service Account** created in **Step 1**, and click **Create key**.

          ![Select service account for HMAC](https://storage.googleapis.com/prequel_docs/images/gcs-select-service-account-hmac.png)

       5. Make a note of the **Access key** and **Secret**.
     </Warning>

  ### Create destination GCS bucket

  1. Navigate to the **Cloud Storage** page.

  2. Click **Create**.

  3. Enter a **bucket name**, choose a **region**. **Note**: at the **Choose how to control access to objects** step, we recommend selecting **Enforce public access prevention on this bucket**.

     ![Prevent public access](https://storage.googleapis.com/prequel_docs/images/gcs-prevent-public-access.png)

  4. After choosing your preferences for the remaining steps, click **Create**.

     <Note>
       **Recommendation: dedicated bucket for data transfers**

       Use a unique bucket for these transfers. This:

       * Prevents resource contention with other workloads
       * Avoids accidental data loss from mixed lifecycle or cleanup rules
       * Improves security by reducing surface area and enabling tighter, destination-scoped policies
     </Note>

  5. On the **Bucket details** page for the bucket you created, select the **Permissions** tab, and click **Grant access**.

  6. Grant access to the principal (Service Account) you created in **Step 1** (*Note: this is the service account you created, not the service account from the prerequisite*), and assign the Role: **Storage Legacy Bucket Writer**. Click **Save**.

     ![Storage Legacy Bucket Writer](https://storage.googleapis.com/prequel_docs/images/gcp-storage-legacy-bucket-writer.png)

  ### Add your destination

  Use the following details to complete the connection setup: **bucket name**, your chosen **folder name** for the data, and your **Service account email**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49269230875027)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271447307539)
</Steps>

## Permissions checklist

* Service account has write access to the bucket (e.g., Storage Legacy Bucket Writer), or an equivalent custom role including:
  * `storage.buckets.get`
  * `storage.objects.list`, `storage.objects.get`, `storage.objects.create`, `storage.objects.delete`
* If using service account impersonation, the token creator role is granted to the impersonating principal

## FAQ

<Accordion title="How is the GCS connection secured?">
  Recommended: use a service account with role-based access (no long-lived user credentials). Optionally, HMAC keys can be used when policy requires, but short-lived tokens and least-privilege roles are preferred.
</Accordion>

<Accordion title="How is data organized in the bucket?">
  Data lands in Hive-style partitions per model: `<folder>/<model_name>/dt=<transfer_date>/<file_part>_<transfer_timestamp>.<ext>`. To write to the bucket root, enter `.` as the folder name.
</Accordion>

<Accordion title="What file formats are supported?">
  Parquet (default/recommended), CSV, and JSON/JSONL.
</Accordion>

<Accordion title="How are large datasets written?">
  Files are automatically split; multiple files may be written per model per transfer.
</Accordion>

<Accordion title="How do I know when a transfer completed?">
  Each transfer writes a manifest file per model under `_manifests`. Files are written per model per transfer in the format: `_manifests/<model_name>/dt=<transfer_date>/manifest_{transfer_id}.json`.
</Accordion>

<Accordion title="Why do I sometimes see duplicates?">
  Object storage is append-only. The change detection process uses a lookback window to ensure no data is missed, which can create duplicates. Downstream pipelines should deduplicate on primary keys prioritizing the most recent transfer window; manifest files can help bound the set of files to read.
</Accordion>

<Accordion title="What if I change the bucket or folder?">
  New files are appended to the new location. Existing data remains in the old location.
</Accordion>

<Accordion title="Are there file size limits?">
  No explicit size/row limits for GCS; files are split automatically based on volume and performance heuristics.
</Accordion>
