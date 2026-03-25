# Source: https://docs.logrocket.com/docs/google-cloud-storage-prerequisites.md

# Google Cloud Storage Prerequisites

Configure your Google Cloud Storage destination.

## Prerequisites

* [ ] By default, GCS authentication uses role-based access. You will need the data-syncing service's service account name available to grant access: `datasync-feiwxmng@logrocket-prequel.iam.gserviceaccount.com`

## Step 1: Create a service account

1. In the GCP console, navigate to the **IAM & Admin** menu, click into the **Service Accounts** tab, and click **Create service account** at the top of the menu.
2. In the first step, name the service account that will be used to transfer data into Cloud Storage and click **Create and Continue**. Click **Continue** in the following optional step without assigning any roles.
3. In the **Grant users access to this service account** step, within the **Service account users role** field, enter the provided **Service account** (see prerequisite) and click **Done**.
4. Once successfully created, search for the created service account in the service accounts list, click the **Service account** name to view the details, and make a note of the **email** (note: this is a different email than the service's service account).
5. Select the permissions tab, find the provided principal name (**Service account** from the prerequisite), click the **Edit principal** button (pencil icon), click **Add another role**, select the **Service Account Token Creator** role, and click **Save**.
   > ![](https://storage.googleapis.com/prequel_docs/images/gcp-grant-role.png)

## Step 2: Create destination GCS bucket

1. Navigate to the **Cloud Storage** page.
2. Click **Create**.
3. Enter a **bucket name**, choose a **region**. **Note**: at the **Choose how to control access to objects** step, we recommend selecting **Enforce public access prevention on this bucket**.

![](https://storage.googleapis.com/prequel_docs/images/gcs-prevent-public-access.png)

4. After choosing your preferences for the remaining steps, click **Create**.
5. On the **Bucket details** page for the bucket you created, select the **Permissions** tab, and click **Grant access**.
6. Grant access to the principal (Service Account) you created in **Step 1** (*Note: this is the service account you created, not the service account from the prerequisite*), and assign the Role: **Storage Legacy Bucket Writer**. Click **Save**.

![](https://storage.googleapis.com/prequel_docs/images/gcs-storage-object-creator.png)

## Step 3: Gather the required setup information

For the data export setup, you will need:

* **bucket name**
* Your chosen **bucket folder name**
* **Service account email**

Visit the [LogRocket Streaming Data Export settings page](https://app.logrocket.com/r/settings/streaming-data-export) to complete the setup.