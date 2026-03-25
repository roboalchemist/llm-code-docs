# Source: https://docs.port.io/build-your-software-catalog/custom-integration/S3-integrations.md

# S3 Bucket

Port allows you to ingest any data source by using [Airbyte](https://airbyte.com/), storing the data temporarily in [S3 bucket](https://aws.amazon.com/s3/), and then triggering ingestion via a [Webhook](https://docs.port.io/build-your-software-catalog/custom-integration/webhook/).

This flow is useful for syncing external data sources where no direct integration exists yet or where you need to have control over the ingestion process.

![](/img/build-your-software-catalog/custom-integration/s3integrations/s3IntegrationsAirbyte.png)

<br />

<br />

Disclaimer

S3 integrations lack some of the features (such as reconciliation) found in Ocean or other Port integration solutions.

As a result, if a record ingested during the initial sync is later deleted in the data source, thereâs no automatic mechanism to remove it from Port. The record simply wonât appear in future syncs, but it will remain in Port indefinitely.

If the data includes a flag for deleted records (e.g., is\_deleted: "true"), you can configure a webhook delete operation in your [webhookâs mapping configuration](/build-your-software-catalog/custom-integration/webhook/.md#configuration-structure) to remove these records from Port automatically.

## Detailed examples[â](#detailed-examples "Direct link to Detailed examples")

The following guides walk you through ingesting specific data sources into Port using Airbyte, S3 and webhook:

* [Ingest Slack data into Port](https://docs.port.io/guides/all/ingest-slack-data-via-airbyte-s3-and-webhook)
* [Ingest Okta data into Port](https://docs.port.io/guides/all/ingest-okta-data-via-airbyte-s3-and-webhook)
* [Ingest Hibob data into Port](https://docs.port.io/guides/all/ingest-hibob-data-via-airbyte-s3-and-webhook)

It is also available to ingest data sources into Port using Fivetran, S3 and webhook:

* [Ingest Slack data into Port with Fivetran](https://docs.port.io/guides/all/ingest-slack-data-via-fivetran-s3-and-webhook)

## How it works[â](#how-it-works "Direct link to How it works")

Airbyte connects to your data source, which can be any of Airbyteâs supported connectors.<br /><!-- -->The extracted data is then written to an Amazon S3 bucket, and is ready to be picked up for ingestion.

Once the data is in S3, Portâs webhook integration can be triggered, either manually or automatically, to fetch it.

Finally, the webhook fetches the data from S3, transforms it based on your blueprint and mapping, and ingests it into Port.

## Airbyte setup[â](#airbyte-setup "Direct link to Airbyte setup")

To integrate Airbyte-supported data source into Port, you will need to:

1. Set up the S3 destination (only once).

2. Set up the Data Source - once per data source you wish to integrate. Airbyte provides detailed [documentation](https://docs.airbyte.com/integrations/sources/) on how to generate/receive the appropriate credentials to set each data source.

3. Set up the Connection between the source and destination - in this step you will be able to define what data will be ingested, to which webhook integration in Port (see below "Set up the Connection"), how often will the sync will be executed, and in what mode (full refresh / incremental).

### Set up S3 Destination[â](#set-up-s3-destination "Direct link to Set up S3 Destination")

* UI
* Terraform

1. Login to your Airbyte application (cloud or self-hosted).

2. In the left-side pane, click on `Destinations`.

3. Click on `+ New Destination`.

4. Input the S3 Credentials provided to you by Port:

   * Under **S3 Key ID** enter your S3 Access Key ID.
   * Under **S3 Access Key** enter your S3 Access Key Secret.
   * Under **S3 Bucket Name** enter the bucket name (example: "org-xxx").
   * Under **S3 Bucket Path** enter "data/".
   * Under **S3 Bucket Region** enter the appropriate region.
   * For **output format**, choose "JSON Lines: Newline-delimited JSON".
   * For **compression**, choose "GZIP".
   * Under **Optional Fields**, enter the following in **S3 Path Format**: `${NAMESPACE}/${STREAM_NAME}/year=${YEAR}/month=${MONTH}/${DAY}_${EPOCH}_`

5. Click `Test and save` and wait for Airbyte to confirm the Destination is set up correctly.

![](/img/build-your-software-catalog/custom-integration/s3integrations/airbyteDestinationSetupExample.png)

```
terraform {
  required_providers {
    airbyte = {
      source = "airbytehq/airbyte"
      version = "0.6.5"
    }
  }
}

provider "airbyte" {
  username = "<AIRBYTE_USERNAME>"
  password = "<AIRBYTE_PASSWORD>"
  server_url = "<AIRBYTE_API_URL>"
}

resource "airbyte_destination_s3" "port-s3-destination" {
  configuration = {
    access_key_id     = "<S3_ACCESS_KEY>"
    secret_access_key = "<S3_SECRET_KEY>"
    s3_bucket_region  = "<S3_REGION>"
    s3_bucket_name    = "<S3_BUCKET>"
    s3_bucket_path    = "data/"
    format = {
      json_lines_newline_delimited_json = {
        compression = { gzip = {} }
        format_type = "JSONL"
      }
    }
    s3_path_format    = `$${NAMESPACE}/$${STREAM_NAME}/year=$${YEAR}/month=$${MONTH}/$${DAY}_$${EPOCH}_`
    destination_type = "s3"
  }
  name          = "port-s3-destination"
  workspace_id  = var.workspace_id
}

variable "workspace_id" {
  default     = "<AIRBYTE_WORKSPACE_ID>"
}
```

### Set up data source[â](#set-up-data-source "Direct link to Set up data source")

### Find the connector in Airbyte

Airbyte supports a wide range of [connectors](https://airbyte.com/connectors?connector-type=Sources).

Setup is often straightforward (such as generating an API key), and some connectors may require extra steps (like creating a Slack app).

If a connector doesnât exist yet, you can [request it](https://airbyte.com/connector-requests) from the Airbyte community or build your own.

![](/img/build-your-software-catalog/custom-integration/s3integrations/airbyteConnectorSearchExample.png)

### Configure the source connector

Follow the guides provided by Airbyte, visible on the right side of the application, see below:

![](/img/build-your-software-catalog/custom-integration/s3integrations/airbyteSourceSetupExample.png)

### Set up the connection[â](#set-up-the-connection "Direct link to Set up the connection")

1. In the Airbyte "Connections" page, create a "+ New Connection".

2. For **Source**, choose your desired data source.

3. For **Destination**, choose the S3 Destination you have set up.

4. In the **Select Streams** step, check the streams you are interested in synchronizing into Port.

5. In the **Configuration** step, under "Destination Namespace", choose "Custom Format" and enter the webhook URL you copied when setting up the webhook, for example: "wSLvwtI1LFwQzXXX".

![](/img/build-your-software-catalog/custom-integration/s3integrations/airbyteConnectionSetupExample.png)

6. **Click on Finish & Sync** to apply and start the Integration process!

## Data model setup[â](#data-model-setup "Direct link to Data model setup")

### Figure out the target schema and mapping[â](#figure-out-the-target-schema-and-mapping "Direct link to Figure out the target schema and mapping")

To define the data model, you will need to know the schema of the data you want to ingest.<br /><!-- -->If you are unsure about the schema that the connector extracts, you can always set up the Airbyte connection to S3 first, and during the **Select Streams** step in the connection setup, review the expected schema for each stream and construct the appropriate blueprints and mappings:

![](/img/build-your-software-catalog/custom-integration/s3integrations/airbyteSelectStreamsScreenshot.png)

<br />

Alternatively, you can set up the connection and start the sync, then download the extracted files from S3, review them, and construct the appropriate blueprints and mappings.

Resync Airbyte After Port Setup

If you set up a connection to S3 before setting the target blueprints and mappings, you will have to execute a "resync" in airbyte after the resources in Port have been properly set up.

**To download the extracted S3 files:**

* AWS CLI
* Python (Boto3)

1. Install AWS CLI: Download and install the AWS CLI from [AWSâs official page](https://aws.amazon.com/cli/).

2. Configure Your Credentials: Run the command below and input your `ACCESS_KEY`, `SECRET_KEY`, and `region`:

```
aws configure
```

Alternatively, you can set the environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`.

3. Download Files from S3: Use the following command, replacing the placeholders with your bucket name and file prefix:

```
aws s3 cp s3://<bucket-name>/<file-prefix> ./local-folder --recursive
```

for example:

```
aws s3 cp s3://org-XXX/data/abc123/ ./my_extracted_data --recursive
```

This command copies all files that start with your specified prefix into the local folder (create it if needed).

Run the following command to install boto3 if you havenât already:

```
pip install boto3
```

Copy and paste this code into a file (e.g., download\_s3.py), replacing the placeholders with your actual details:

```
import boto3

# Initialize the S3 client with your credentials and region
s3 = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
    region_name='YOUR_REGION'
)

bucket_name = 'your-bucket-name'
prefix = 'your/file/prefix/'  # Ensure this ends with '/' if you want a folder-like behavior

# List objects within the specified prefix
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

# Download each file found
for obj in response.get('Contents', []):
    key = obj['Key']
    # Define a local filename (you might want to recreate the directory structure)
    local_filename = key.split('/')[-1]
    print(f"Downloading {key} to {local_filename}...")
    s3.download_file(bucket_name, key, local_filename)
```

Execute your script from the terminal:

```
python download_s3.py
```

Once the files are in your local device you can use your preferred text editor to review it's content and construct the appropriate blueprints and mappings for your data.

### Create blueprints[â](#create-blueprints "Direct link to Create blueprints")

Once you have decided on the desired blueprints you wish to set up, you can refer to the [blueprint creation docs](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/?definition=ui) to set them up in your account.

### Create webhook integration[â](#create-webhook-integration "Direct link to Create webhook integration")

Once you have decided on the mappings you wish to set up, you can refer to the [webhook creation docs](https://docs.port.io/build-your-software-catalog/custom-integration/webhook/) to set them up in your portal.

Using the generated webhook URL

It is important that you use the generated webhook URL when setting up the Connection in Airbyte, otherwise the data will not be automatically ingested into Port from S3.

## Troubleshooting[â](#troubleshooting "Direct link to Troubleshooting")

### Issues with Airbyte->S3 integration[â](#issues-with-airbyte-s3-integration "Direct link to Issues with Airbyte->S3 integration")

Airbyte provides detailed logs available through the web application on currently running sync processes as well as historical ones.<br /><!-- -->After a successful sync has completed, you will be able to see how long ago it was executed, and how many records were loaded to S3 in every stream.

### Issues with S3->Port ingestion[â](#issues-with-s3-port-ingestion "Direct link to Issues with S3->Port ingestion")

If everything in Airbyte is working properly, and you don't see the data in your Port account, you can follow these steps to diagnose the root cause:

### Issues with the webhook

1. Navigate to [Data Sources page](https://app.getport.io/settings/data-sources) in your port account.

2. Locate the Webhook integration you have set for the ingestion, and click on it.

3. In the pop-up interface, under "Add test Event" click on "Load latest event".

4. You should now see an example event that was received from the ingestion pipeline (in case you don't - scroll down to the below section in this guide: Data in S3 is not propagating to Port).

5. Scroll down to the section "Test Mapping" and click on the "Test Mapping" button at the bottom of the pop-up interface.<br /><!-- -->You should see the result of the mapping applied on the latest event that was received by the webhook URL in the text box above the "Test Mapping" button.<br /><!-- -->If you encounter a jq error - it means you have a syntax error or the source's schema does not match the mapping you have set and you will need to adjust the mapping properly.<br /><!-- -->If you encounter a JSON document list, it means the mapping is working properly, but it could be that the filters you have set in it all result in "false" (which means no entity will be created).<br /><!-- -->In this case you will need to look over the appropriate element in the document (with the relevant blueprint for the loaded event) and adjust the mapping so that the "filter" field will result to "true".

### Issues with the blueprint definition

1. Navigate to the [Data Sources page](https://app.getport.io/settings/data-sources) of your port account.

2. Locate the webhook integration you have set for the ingestion, and click on it.

3. In the pop-up interface, in the top pane menu click on "Audit Log".

4. You can now browse for issues in ingestion of specific entities in the audit log, or apply a filter where **Status != "Success"**.<br /><!-- -->If any entities were created but failed to ingest, you will see an indicative error that may lead you to the issue in the blueprint definition.

### Data is not propagating from S3 to Port

If you're sure the Airbyte integration is working properly, there are no records in the Audit Log, and the "Load latest event" button does not produce an event in the corresponding box, there might be an issue with the pipeline set up by Port.

<br />

<!-- -->

In this case, contact us using chat/Slack/support site to [support.port.io](http://support.port.io/) and our support team will assist in diagnosing and solving the issue.
