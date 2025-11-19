# Source: https://docs.datafold.com/integrations/databases/google-cloud-storage.md

# Google Cloud Storage (GCS)

**Steps to complete:**

1. [Create a Service Account](/integrations/databases/google-cloud-storage#create-a-service-account)
2. [Give the Service Account Storage Object Admin access](/integrations/databases/google-cloud-storage#service-account-access-and-permissions)
3. [Generate a Service Account JSON key](/integrations/databases/google-cloud-storage#generate-a-service-account-key)
4. [Configure your data connection in Datafold](/integrations/databases/google-cloud-storage#configure-in-datafold)

## Create a Service Account

To connect Datafold to your Google Cloud Storage bucket, you will need to create a *service account* for Datafold to use.

* Navigate to the [Google Cloud Console](https://console.cloud.google.com/), click on the drop-down to the left of the search bar, and select the project you want to connect to.
  * *Note: If you do not see your project, you may need to switch accounts.*
* Click on the hamburger menu in the upper left, then select **IAM & Admin** followed by **Service Accounts**.
* Create a service account named `Datafold`.

## Service Account Access and Permissions

The Datafold service account requires the following roles and permissions:

* **Storage Object Admin** for read and write access on all the datasets in the project.

## Generate a Service Account Key

Next, go back to the **IAM & Admin** page to generate a key for Datafold.

* Click on the **Service Accounts** page.
* Click on the **Datafold** service account.
* Click on the **Keys** tab.
* Click on **Add Key** and select **Create new key**.
* Select **JSON** and click **Create**.

We recommend using the JSON formatted key. After creating the key, it will be saved on your local machine.

## Configure in Datafold

| Field Name                                                | Description                                                                                                                                           |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection name                                           | A name given to the data connection within Datafold                                                                                                   |
| Bucket Name                                               | The name of the bucket you want to connect to.                                                                                                        |
| Bucket region                                             | The region of the bucket you want to connect to.                                                                                                      |
| JSON Key File                                             | The key file generated in the [Generate a Service Account JSON key](/integrations/databases/google-cloud-storage#generate-a-service-account-key) step |
| Directory for writing diff results                        | Optional. The directory in the bucket where diff results will be written. Service account should have write access to this directory.                 |
| Default maximum number of rows to include in diff results | Optional. The maximum number of rows that a file with materialized results will contain.                                                              |

Click **Create**. Your data connection is ready!
