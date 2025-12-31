# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-from/copy-from-with-endpoint.md

# COPY FROM with Endpoint

## Overview

When running [COPY FROM](/sql-reference/sql-statements/copy-from/copy-from) queries, you should have the option to include the **endpoint URL**. This feature is especially useful for scenarios where you need to provide credentials and specific endpoints.

## Syntax

The syntax is as follows:

```sql  theme={null}
COPY table_name FROM 'file_path' (AWS_CRED(AWS_REGION 'aws_region', AWS_KEY_ID "
      "'key_id', AWS_PRIVATE_KEY 'access_key', ENDPOINT 'endpoint_url'));
```

<Info>Replace `AWS_CRED` with `AZURE_CRED` or `GCS_CRED` when copying from the Azure Blob Storage or Google Cloud Storage.</Info>

Here's the breakdown of syntax parameters:

* **Shared parameters**:
  * `table_name`: table that will receive data from the file
  * `file_path`: link to the file location accessible from the server

* **Parameters in `AWS_CRED`**:
  * `aws_region`: AWS region associated with the storage service (e.g. 'region1')
  * `key_id`: key identifier for authentication
  * `access_key`: access key for authentication
  * `endpoint_url`: URL endpoint for the storage service

* **Parameters in `GCS_CRED`**:
  * `<path_to_credentials>`: path to JSON credentials file
  * `<json_credentials_string>`: contents of the GCS's credentials file

* **Parameters in `AZURE_CRED`**:
  * `tenant_id`: tenant identifier representing your organization's identity in Azure
  * `client_id`: client identifier used for authentication
  * `client_secret`: secret identifier acting as a password for authentication.

## Examples

### COPY FROM with AWS S3 Bucket

In this example, we are using the COPY FROM statement to import data from a file named `students_file` and the endpoint is `s3.us-east-2.amazonaws.com`.

```sql  theme={null}
COPY students FROM 'students_file' (AWS_CRED(AWS_REGION 'region1', AWS_KEY_ID "
      "'key_id', AWS_PRIVATE_KEY 'access_key', ENDPOINT 's3.us-east-2.amazonaws.com'));
```

**Expected Output**: Data from `students_file` is copied into the `students` table

### COPY FROM with Google Cloud Storage

This example shows how to use the `COPY FROM` statement to import data, but this time, the data is stored on Google Cloud Storage;

```sql  theme={null}
COPY project FROM 'gs://your-bucket/project_file' (GCS_CRED('/path/to/credentials.json'));
```

If for any reason you cannot use a path to the `credentials.json` file, you can also pass its contents as a string in the following way:

```sql  theme={null}
COPY project FROM 'gs://your-bucket/project_file' (GCS_CRED('<contents of the credentials.json file>'));
```

<Info>Make sure that it is in JSON format</Info>

You can also copy the data using the `AWS_CRED` like below, with the following endpoint `https://storage.googleapis.com`.

```sql  theme={null}
COPY project FROM 'project_file' (AWS_CRED(AWS_REGION 'region1', AWS_KEY_ID "
      "'key_id', AWS_PRIVATE_KEY 'access_key', ENDPOINT 'https://storage.googleapis.com'));
```

**Expected Output**: Data from `project_file` is copied into the `project` table.

<Tip>For Google Cloud Storage, it's recommended to use HMAC keys for authentication. You can find more details about that on the [HMAC keys - Cloud Storage](https://cloud.google.com/storage/docs/authentication/hmackeys) page.</Tip>

### COPY FROM with Azure Blob Storage

It's a similar story for getting the data from Azure Blob Storage.

```sql  theme={null}
COPY taxi_data FROM 'wasbs://container-name/your_blob' (AZURE_CRED(TENANT_ID 'your_tenant_id' CLIENT_ID 'your_client_id', CLIENT_SECRET 'your_client_secret'));
```

**Expected Output**: Data from the `your_blob` is copied into the `taxi_data`.
