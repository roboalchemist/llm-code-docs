# Source: https://docs.acceldata.io/documentation/global-storage.md

# Global Storage

## What Is Global Storage?

Acceldata Data Plane processes a huge amount of data, from profiling and quality checks to advanced analytics and monitoring. All of that data needs to go somewhere, whether it's logs, results, temporary files, or models.

That “somewhere” is what we call **Global Storage**, a central storage location used by Data Plane services to read and write data.

Depending on your environment, this storage could be:

- Google Cloud Storage (GCS) – If you're running in GCP
- Amazon S3 – If you're on AWS
- Azure Data Lake (ADLS) – If you're on Microsoft Azure
- HDFS or MAPRFS – For on-prem or Hadoop-based setups
- Local disk – For quick tests or minimal deployments (not recommended for production)

## Where Is This Configured?

All global storage settings live in a JSON configuration file at:

```bash
/opt/acceldata/globalstorage.json
```



This file tells Data Plane:

- What type of storage you’re using (gcs, s3, adls, etc.)
- Where to find the storage (bucket name, project ID, etc.)
- How to securely connect to it (credentials, roles, or keys)

## Sample Configuration (GCS Example)

Here’s what this JSON file might look like if you're using Google Cloud Storage:

```json
{
  "MEASURE_RESULT_FS_TYPE": "gcs",
  "MEASURE_RESULT_FS_GCS_BUCKET": "your-bucket-name",
  "MEASURE_RESULT_FS_GCS_PROJECT_ID": "your-gcp-project-id",
  "MEASURE_RESULT_FS_GCS_MODE": "SERVICE_ACCOUNT_INLINE",
  "MEASURE_RESULT_FS_GCS_CLIENT_EMAIL": "example@project.iam.gserviceaccount.com",
  "MEASURE_RESULT_FS_GCS_PRIVATE_KEY": "-----BEGIN PRIVATE KEY-----\nMIIEv....\n-----END PRIVATE KEY-----",
  "MEASURE_RESULT_FS_GCS_PRIVATE_KEY_ID": "1234567890abcdef"
}
```



Note If you're using GCS, you’ll also need to securely provide the service account credentials (gcp_cred.json) to the system. This is explained in the [Secret Management](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/secret-management).

AWS S3
Here’s what this JSON file might look like if you're using AWS S3:

```json
{
  "MEASURE_RESULT_FS_TYPE": "s3",
  "MEASURE_RESULT_FS_S3A_BUCKET": "<Container name to store the result>",
  "MEASURE_RESULT_FS_S3A_ACCESS_KEY": "AWS Access key",
  "MEASURE_RESULT_FS_S3A_SECRET_KEY": "AWS Secret key",
  "MEASURE_RESULT_FS_S3A_REGION": "AWS Region",
  "MEASURE_RESULT_FS_S3A_MODE": "KEY_BASED"
}
```



Azure ALDS
Here’s what this JSON file might look like if you're using Azure ALDS:

```json
{
	"MEASURE_RESULT_FS_TYPE"  :  "adls"
  "MEASURE_RESULT_FS_ADLS_STORAGE_CONTAINER_NAME" :  "Container name to store the result"
	"MEASURE_RESULT_FS_ADLS_STORAGE_ACCOUNT_NAME" : "ADLS storage account name"
 	"MEASURE_RESULT_FS_ADLS_MODE" : "STORAGE_KEY"
	"MEASURE_RESULT_FS_ADLS_STORAGE_ACCESS_KEY" : "ADLS storage access key to connect with storage"
  (or)
  "MEASURE_RESULT_FS_ADLS_MODE" : "SERVICE_PRINCIPAL"
	"MEASURE_RESULT_FS_ADLS_STORAGE_CLIENT_ID" : "ADLS Storage client id"
	(or)
	"MEASURE_RESULT_FS_ADLS_STORAGE_CLIENT_SECRET" : "ADLS Storage client secret"
	"MEASURE_RESULT_FS_ADLS_STORAGE_TENANT_ID" : "ADLS Tenant id"
	(or)
	"MEASURE_RESULT_FS_ADLS_MODE" : "MANAGED_IDENTITY"
	"MEASURE_RESULT_FS_ADLS_GENERATION" : "GEN_1 or GEN_2"
}
```



HDFS/MAPRFS
Here’s what this JSON file might look like if you're using HDFS/MAPRFS:

```json
{
  "MEASURE_RESULT_FS_TYPE" :  "hdfs"
  "MEASURE_RESULT_FS_HDFS_DIRECTORY" : "hdfs or maprfs driven complete path to store the result"
}
```



Local Storage to Pod
Here’s what this JSON file might look like if you're using Local Storage to Pod:

```json
"MEASURE_RESULT_FS_TYPE" : "local"
```





---

## How to Provide Credentials (If Using Cloud Storage)

For cloud-based storage (like GCS or S3), the system needs credentials to authenticate and access the storage bucket.

Rather than putting raw credentials in the file or environment, Data Plane reads them from Kubernetes Secrets for security.

Here’s how that works:

**Step 1: Create or update /opt/acceldata/globalstorage.json**

Define your storage type (e.g., gcs, s3) and connection settings.

**Step 2: Base64-encode the file**

Kubernetes requires secrets to be stored in base64-encoded form.

**Step 3: Inject the config into the cluster**

Run:

```bash
kubectl edit secret global-storage -n <your-namespace>
```



In the data: section, add:

```yaml
globalstorage.json: <your-base64-encoded-content>
```



**Step 4 (GCP Only): Provide GCP credentials**

If using GCS, you'll also need to base64-encode your gcp_cred.json file (your service account credentials) and add it to the gcp-cred Kubernetes Secret:

```bash
kubectl edit secret gcp-cred -n <your-namespace>
```



Inside the data: section, add or update:

```yaml
gcp_cred.json: <base64-encoded-credentials>
```



Note For full instructions on setting up secrets securely — including how to create and inject gcp_cred.json — refer to the [Secret Management](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/secret-management).

## Deploying the Configuration

After updating the JSON file with the encoded secret, restart the data plane services by running the following command:

```bash
kubectl rollout restart deploy -n <your-namespace>
```



Once completed, navigate to the Data Plane's Application Configuration page in the UI to verify that the Global Storage is properly set up.

---

## Specifying Custom Folder Paths for Good/Bad Records

ADOC stores policy execution results—such as **good records, bad records, and metadata**—in the object storage bucket configured for the data plane.

The storage location is determined using two levels of configuration:

1. **Data plane Storage Configuration**: defines the object storage location where results are written.
2. **Persistence Configuration**: defines how the execution results are organized within that storage location.

### Data Plane Storage Configuration

The object storage **bucket or container** used to store policy execution results is configured in the **Data Plane Global Storage configuration**.

| Key | Description | 
| ---- | ---- | 
| `MEASURE_RESULT_SAVE_PATH` | Specifies an optional base folder (prefix) inside the configured storage location where policy execution results will be written. | 


Example configuration:

```bash
MEASURE_RESULT_SAVE_PATH=user/
```



In this example, all policy execution results are written under the configured storage location using the specified base folder:

```bash
<configured-storage-location>/user/
```



Note This configuration is **data plane-specific**. Each data plane can have its own storage bucket and base path depending on the deployment configuration.

For more details on configuring data plane storage settings, see [Data Plane Installation - Application Config](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation#5-application-config).

## Persistence Configuration (ADOC v26.3.0 and Later)

Starting with **ADOC v26.3.0**, the internal folder structure used to organize policy execution results is configured using **Persistence Configuration**.

Persistence Configuration uses **suffix templates** to dynamically generate storage paths based on variables such as:

- Policy name
- Policy type
- Execution time
- Request ID or execution ID
- Datasource name
- Asset name
- Record type (good, bad, metadata)

For example, a suffix template such as:

```bash
{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}
```



can generate paths similar to:

```bash
data-quality/orders_policy/2026-03-11/abc123/bad-records
```



The final storage path is created by combining:

```bash
<Dataplane base path> + <Persistence configuration suffix template>
```



Example:

```bash
s3://educ-global-storage-queue/user/data-quality/orders_policy/2026-03-11/abc123/bad-records
```



This approach enables organizations to organize execution results more effectively by **policy, execution date, datasource, or team-specific structures**.

For detailed instructions on configuring persistence templates and managing persistence configurations, see [Persistence Configuration](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/persistence-configuration).