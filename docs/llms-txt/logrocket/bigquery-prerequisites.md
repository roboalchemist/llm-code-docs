# Source: https://docs.logrocket.com/docs/bigquery-prerequisites.md

# BigQuery Prerequisites

Configuring your BigQuery destination.

## Prerequisites

* [ ] By default, BigQuery authentication uses role-based access. You will need the data-syncing service's service account name available to grant access: `datasync-feiwxmng@logrocket-prequel.iam.gserviceaccount.com`.

## Step 1: Create service account in BigQuery project

1. In the GCP console, navigate to the **IAM & Admin** menu.

![](https://storage.googleapis.com/prequel_docs/images/gcp-iam-admin-full.png "iam & admin full.png")

2. Click into the **Service Accounts** tab.

![](https://storage.googleapis.com/prequel_docs/images/gcp-service-accounts-full.png "service accounts full.png")

3. Click **Create service account** at the top of the menu.

![](https://storage.googleapis.com/prequel_docs/images/gcp-create-service-account-menu.png "create service account menu.png")

4. In the first step, name the user and click **Create and Continue**.

![](https://storage.googleapis.com/prequel_docs/images/gcp-service-account-name-options.png "service account name options.png")

5. In the second step, grant the user the role **BigQuery User**.

![](https://storage.googleapis.com/prequel_docs/images/gcp-bigquery-user.png)

> Loading data into a dataset that already exists
>
> By default, we will attempt to create a new dataset (with a name you provide) in the BigQuery project. If instead you create the dataset ahead of time, you will need to grant the BigQuery Data Owner role to this Service Account at the dataset level.
>
> * In BigQuery, click on the existing dataset. In the dataset tab, click **Sharing**, then **Permissions**. Click **Add Principals**. Enter the Service Account name, and add the Role: **BigQuery Data Owner**

6. In the third step (**Grant users access to this service account** step), within the **Service account users role** field, enter the provided **Service account** (see prerequisite) and click **Done**.
7. Once successfully created, search for the created service account in the service accounts list, click the **Service account** name to view the details, and make a note of the **email** (note: this is a different email than the service's service account).
8. Select the permissions tab, find the provided principal name (**Service account** from the prerequisite), click the **Edit principal** button (pencil icon), click **Add another role**, select the **Service Account Token Creator** role, and click **Save**.

> ![](https://storage.googleapis.com/prequel_docs/images/gcp-grant-role.png)

## Step 2: Create a staging bucket

1. Log into the Google Cloud Console and navigate to **Cloud Storage**. Click **Create** to create a new bucket.

![](https://storage.googleapis.com/prequel_docs/images/gcp-create-gcs-bucket.png)

1. Choose a **name** for the bucket. Click **Continue**. Select a **location** for the staging bucket. Make a note of both the **name** and the **location** (region).

> Choosing a `location` (region)
>
> The location you choose for your staging bucket must match the location of your destination dataset in BigQuery. When creating your bucket, be sure to choose a region in which BigQuery is supported [(see BigQuery regions)](https://cloud.google.com/bigquery/docs/locations)
>
> * If the dataset **does not** exist yet, the dataset will be created for you in the same region where you created your bucket.
> * If the dataset **does** exist, the dataset region must match the location you choose for your bucket.

2. Click **continue** and select the following options according to your preferences. Once the options have been filled out, click **Create**.
3. On the **Bucket details** page that appears, click the **Permissions** tab, and then click **Add**.

![](https://storage.googleapis.com/prequel_docs/images/gcp-add-permission-to-bucket.png)

4. In the **New principals** dropdown, add the Service Account created in **Step 1**, select the **Storage Admin** role, and click **Save**.

![](https://storage.googleapis.com/prequel_docs/images/gcp-storage-admin.png)

## Step 3: Find Project ID

1. Log into the Google Cloud Console and select the projects list dropdown.
2. Make note of the BigQuery **Project ID**.

![](https://storage.googleapis.com/prequel_docs/images/gcp-project-id.png "project id.png")

## Step 4: Gather the required setup information

For the data export setup, you will need:

* **Project ID**
* **Bucket Name**
* **Bucket Location**
* **Dataset name**
* **Service Account Name**

Visit the [LogRocket Streaming Data Export settings page](https://app.logrocket.com/r/settings/streaming-data-export) to complete the setup.