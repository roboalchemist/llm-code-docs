# Source: https://docs.anyscale.com/storage/gcs.md

# Access Google Cloud Storage buckets

[View Markdown](/storage/gcs.md)

# Access Google Cloud Storage buckets

This page describes how to directly interact with a GCS bucket from your self-hosted Anyscale cloud deployed on Google Cloud.

## Determine the cluster's service account[​](#service-account "Direct link to Determine the cluster's service account")

By default, Anyscale clusters run with a cloud-specific service account. You can also configure your cluster to use a custom service account. See [Manage Google Cloud service accounts for Anyscale clusters](/iam/google-cloud.md).

To interact with a private Google Cloud Storage bucket you need both permissions and tooling.

## Grant permissions to your Google Cloud service account[​](#permissions "Direct link to Grant permissions to your Google Cloud service account")

To grant access to your service account, either the Anyscale default service account or your own, to a bucket, follow the [Google instructions](https://cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

1. Go the **Permissions** tab of the bucket.
2. Click **Grant access**.
3. Type the service account email as a **New principal**. If you are using the Anyscale default cloud-specific service account, you can find the service account email in the Clouds table on the **Configurations** page in a column called **Provider Identity**.
4. Select roles to grant to the service account. To give full R/W List access, grant your bucket **Storage Object Admin** and **Storage Object Viewer**.
5. Click **Save**.

## Interact with your bucket[​](#interact "Direct link to Interact with your bucket")

To interact with a bucket from the CLI, install `gsutil`. Running the following command installs `gsutil` on a node:

```
wget -qO- https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-359.0.0-linux-x86_64.tar.gz | tar xvz
```

Afterwards, you can interact with `gsutil`, for example, to copy a local file to the bucket, as follows:

```
./google-cloud-sdk/bin/gsutil cp <file> gs://<bucket>
```

caution

If you install `gsutil` with `pip`, as is the case with `runtime_environments`, you may need to add the following to `~/.boto`:

```
[GoogleCompute]
service_account = default
```

You can create this file by running `printf "[GoogleCompute]\nservice_account = default\n" > ~/.boto`

## Use direct credentials for development[​](#direct-credentials "Direct link to Use direct credentials for development")

warning

Storing credentials directly isn't secure. Use service account IAM for production workloads. Use direct credentials only for development and testing.

### Use service account file[​](#use-service-account-file "Direct link to Use service account file")

Store credentials in a service account JSON file:

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
gsutil cp your_file.txt gs://bucket/path/
```

### Pass credentials in code[​](#pass-credentials-in-code "Direct link to Pass credentials in code")

```
from google.cloud import storage

# Use service account credentials
storage_client = storage.Client.from_service_account_json(
    'path/to/credentials.json'
)

bucket_name = 'my-dataset-bucket'
blob_name = 'datasets/my_data.csv'
destination_file = 'my_data.csv'

bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.download_to_filename(destination_file)

print(f"Downloaded {blob_name} to {destination_file}")
```
