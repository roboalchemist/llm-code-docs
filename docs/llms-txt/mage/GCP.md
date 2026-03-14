# Source: https://docs.mage.ai/production/deploying-to-cloud/secrets/GCP.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GCP Secret Management

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

## Creating secrets

1. Go to
   [Google Secret Manager UI](https://console.cloud.google.com/security/secret-manager?referrer=search\&authuser=1).
2. Click the button at the top labeled **`+ CREATE SECRET`**.
3. Fill in the name of your secret; e.g. `bigquery_credentials`.
4. Under **Secret value**, upload your service account credentials JSON file or
   paste the JSON into the text area labeled **Secret value**.
5. Scroll all the way down and click the button **`CREATE SECRET`**.

You can mount secrets from Google Secret Manager through Terraform configurations or through the Google Console UI.

## Using secrets locally

### Download credentials from GCP UI

1. Download the credentials JSON file from GCP.
2. Run Mage and mount the secrets as a volume in Docker.
   Follow these [instructions](/getting-started/setup#using-secret-credential-files-in-docker) to learn how to do this.
3. Here are example code snippets to read from that credentials JSON file:

   <CodeGroup>
     ```python Python theme={"system"}
     with open('/home/secrets/gcp_credentials.json', 'r') as f:
         print(f.read())
     ```

     ```yaml YAML theme={"system"}
     demo:
     target: prod
     outputs:
       prod_bigquery:
         dataset: mage_demo
         keyfile: /home/secrets/gcp_credentials.json
         method: service-account
         project: my_cool_gcp_project
         threads: 1
         type: bigquery
     ```
   </CodeGroup>

   > Note
   >
   > This code example assumes your credentials JSON file downloaded from GCP is named
   > `gcp_credentials.json` and that the mount path (e.g. `-v`) you used when running Docker
   > is `/home/secrets`.

***

### Download credentials using `gcloud` CLI

1. Authenticate locally by running this command in your local terminal:

   ```
   gcloud auth application-default login
   ```

2. Create a new `.env` file in your Mage project folder with the following values:

   ```
   GOOGLE_APPLICATION_CREDENTIALS="[PATH TO YOUR USER CREDENTIALS, MOST LIKELY: ~/.config/gcloud/application_default_credentials.json]"
   GCS_BUCKET=[YOUR DEV BUCKET]
   GCLOUD_PROJECT=[YOUR PROJECT]
   ```

3. Run Mage using Docker and set the environment variable `GOOGLE_APPLICATION_CREDENTIALS`.
   Follow these [instructions](/getting-started/setup#environment-variables) to learn how to do this.
   For example, set the environment variable to:

   ```
   -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/FILE_NAME.json
   ```

4. Run Mage and mount the secrets as a volume in Docker.
   Follow these [instructions](/getting-started/setup#using-secret-credential-files-in-docker) to learn how to do this.
   For example:

   ```
   -v ~/.config/gcloud/application_default_credentials.json:/tmp/keys/FILE_NAME.json
   ```

5. Here is an example code snippet:

   ```python  theme={"system"}
   from google.cloud import storage
   from pandas import DataFrame
   from datetime import datetime
   import pytz
   import os
   ​
   ​
   @data_exporter
   def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
   ​
       bucket_name = os.getenv('GCS_BUCKET')
   ​
       now = datetime.utcnow()
       pt = pytz.timezone("America/Los_Angeles")
       now_pst = pytz.utc.localize(now).astimezone(pt)
   ​
       object_key = f'test_file_{now_pst.strftime("%Y-%m-%d")}.csv'
   ​
       storage_client = storage.Client()
       bucket = storage_client.bucket(bucket_name)
       blob = bucket.blob(object_key)
   ​
       blob.upload_from_string(df.to_csv())
   ​
       print(f'df uploaded to {bucket}/{object_key}.')
   ```

## GCP Secret Manager Integration in Mage Pro

<ProOnly source="gcp-secret" />

Securely manage and inject sensitive credentials into your Mage Pro pipelines using **Google Cloud Secret Manager**. This Pro-only feature helps enterprises meet cloud security and compliance standards by keeping secrets like API keys, database passwords, and tokens outside of source code.

### Required Environment Variables

Before accessing secrets, configure your Mage Pro cluster with the following environment variables:

* `GOOGLE_APPLICATION_CREDENTIALS`:
  Full path to your **GCP service account credentials JSON file**.
  *You can upload the credentials file directly to the Mage Pro cluster using the file browser interface.*

* `GCP_PROJECT_ID`:
  The **Google Cloud Project ID** associated with your Secret Manager secrets.

These credentials must have `Secret Manager Secret Accessor` permissions for the secrets you intend to retrieve.

### How to Use the GCP Secret Variable

You can reference GCP secrets programmatically in Python blocks or declaratively in YAML configs.

#### Python code

Use this approach inside a block in your Mage pipeline:

```python  theme={"system"}
from mage_ai.services.gcp.secret_manager.secret_manager import get_secret

# Retrieve a secret by ID from GCP Secret Manager
secret_value = get_secret('secret_id')
```

#### YAML config

To inject a secret dynamically into a YAML config (e.g., for a data source, destination, or authentication setting):

```yaml  theme={"system"}
{{gcp_secret_var('secret_id')}}
```

Mage will automatically resolve and substitute the secret value at runtime.


Built with [Mintlify](https://mintlify.com).