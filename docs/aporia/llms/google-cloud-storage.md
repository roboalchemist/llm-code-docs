# Source: https://docs.aporia.com/data-sources/google-cloud-storage.md

# Google Cloud Storage

This guide describes how to connect Aporia to a Google Cloud Storage (GCS) data source in order to monitor your ML Model in production.&#x20;

We will assume that your model inputs, outputs, and optionally delayed actuals are stored in a file in GCS. Currently, the following file formats are supported:

* `parquet`
* `json`

This data source may also be used to connect to your model's training dataset to be used as a baseline for model monitoring.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FORsfj3dFtETcN5KqBihu%2Fimage.png?alt=media&#x26;token=ef14e117-1177-4d19-b066-5772a9471081" alt=""><figcaption></figcaption></figure>

### Grant bucket access to Aporia Dataproc Worker Service Account

In order to provide access to GCS, you'll need to update your Aporia Dataproc worker service account with the necessary API permissions.

Go to the [Cloud Storage buckets page](https://console.cloud.google.com/storage/browser).

1. Select the buckets where your data is stored.
2. Click on the permissions button:

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FyaKn6h8FDirnGLAuSCsX%2Fimage.png?alt=media&#x26;token=31103064-66b0-4670-874f-30d16255e0a0" alt="" width="563"><figcaption></figcaption></figure>

On the Permissions tab, click on the Add Principal button.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F4qhXVRIW82P0IKLtN5SY%2Fimage.png?alt=media&#x26;token=26b21af6-a173-499d-94ee-f3161efeb098" alt="" width="563"><figcaption></figcaption></figure>

On the Grant access page, do the following:

1. Add the Aporia Dataproc Worker Service Account as a principal.
2. Assign the Storage Object Viewer role
3. Click Save.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2Fs9A5jypZuLNOx3lYz2S0%2Fimage.png?alt=media&#x26;token=794ac5ef-8a0e-4345-b9c7-7b07b1ca221d" alt="" width="563"><figcaption></figcaption></figure>

Now Aporia has the read permission it needs to connect to the GSC buckets you have granted permissions.

### Create a GCS data source in Aporia

1. Go to the [Aporia platform](https://platform.aporia.com/) and log in to your account.
2. Go to the **Integrations** page and click on the **Data Connectors** tab
3. Scroll to **Connect New Data Source** section
4. Click **Connect** on the GCS card and follow the instructions

Bravo! :clap: now you can use the data source you've created across all your models in Aporia.
