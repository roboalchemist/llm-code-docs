# Source: https://docs.airbyte.com/integrations/sources/nexus-datasets.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-nexus-datasets/latest/icon.svg)

# Nexus Datasets

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.1.3](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-nexus-datasets)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-nexus-datasets)(last updated 23 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `9e1fe63c-80ad-44fe-8927-10e66c9e209b`

Nexus datasets is a solution to sync up with the current nexus data sets API. Data can be extracted from the nexus API after providing the required data in the config. Data set name should be provided aliong with the other details to sync the data. [API Documentation](https://developer.gtnexus.com/)

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Nexus customer organization with Data Mesh rights
* Export data set created in the customer organization
* Data API Agent user configured in the customer organization

## Airbyte OSS and Airbyte Cloud[​](#airbyte-oss-and-airbyte-cloud "Direct link to Airbyte OSS and Airbyte Cloud")

* Name of the data set to be synced
* Data API Agent user name / Cliend access key ID / Secret key for the Data API Agent user
* Data Key (API Key) for the customer organization

## Setup guide[​](#setup-guide "Direct link to Setup guide")

### Step 1: Nexus Configuration[​](#step-1-nexus-configuration "Direct link to Step 1: Nexus Configuration")

#### Step 1.1: Create Nexus Customer Organization[​](#step-11-create-nexus-customer-organization "Direct link to Step 1.1: Create Nexus Customer Organization")

1. Create customer organization in the nexus platform

#### Step 1.2: Configure Data Mesh in the Customer Organization[​](#step-12-configure-data-mesh-in-the-customer-organization "Direct link to Step 1.2: Configure Data Mesh in the Customer Organization")

1. Log into the admin side of the nexus application
2. Set up the Data Mesh rule for the organization
3. Create users with the Data Mesh previledges
4. Make sure this user can be logged in to the nexus platfrom

#### Step 1.3: Configure export data pipeline in the Nexus[​](#step-13-configure-export-data-pipeline-in-the-nexus "Direct link to Step 1.3: Configure export data pipeline in the Nexus")

1. Log into the nexus platform using created user in the step 2
2. Go to **Analytics** » **Data Mesh Console**
3. Click on **Export** tab to go into the exportable data sets
4. Click **Create** to create new export pipeline using the existing models
5. Schedule the data set to run

#### Step 1.4: Summary[​](#step-14-summary "Direct link to Step 1.4: Summary")

* Base URL for the nexus platform
* Nexus customer organization with relevant user with rights
* Export data set
* Data API Agent user (DAPI user)
* DAPI user id / access key id / secret key
* Data key (API key)

### Step 2: Set up the source connector in Airbyte[​](#step-2-set-up-the-source-connector-in-airbyte "Direct link to Step 2: Set up the source connector in Airbyte")

#### For Airbyte Cloud:[​](#for-airbyte-cloud "Direct link to For Airbyte Cloud:")

1. [Log into your Airbyte Cloud](https://cloud.airbyte.com/workspaces) account.
2. In the left navigation bar, click **Sources**. In the top-right corner, click **+ new source**.
3. On the source setup page, select **Nexus Datasets** from the Source type dropdown and enter a name for this connector.
4. Add **Base URL**
5. Add **Dataset Name**
6. Add **Infor Streaming Mode (default Full)**
7. Add **User ID**
8. Add **Access Key ID**
9. Add **Secret Key**
10. Add **API Key**
11. Click `Set up source`

#### For Airbyte OSS:[​](#for-airbyte-oss "Direct link to For Airbyte OSS:")

1. [Log into your Airbyte Cloud](https://cloud.airbyte.com/workspaces) account.
2. In the left navigation bar, click **Sources**. In the top-right corner, click **+ new source**.
3. On the source setup page, select **Nexus Datasets** from the Source type dropdown and enter a name for this connector.
4. Add **Base URL**
5. Add **Dataset Name**
6. Add **Infor Streaming Mode (default Full)**
7. Add **User ID**
8. Add **Access Key ID**
9. Add **Secret Key**
10. Add **API Key**
11. Click `Set up source`.

### Configuration[​](#configuration "Direct link to Configuration")

| Input                  | Type     | Description                                                              | Default Value |
| ---------------------- | -------- | ------------------------------------------------------------------------ | ------------- |
| `base_url`             | `string` | Base URL. Enter base url for your data set                               |               |
| `dataset_name`         | `string` | Name of the dataset. Enter dataset name to be synced                     |               |
| `infor_streaming_mode` | `string` | Name of the dataset. Enter dataset name to be synced                     |               |
| `user_id`              | `string` | Data API agent user ID. Enter DAPI agent user id configured in the nexus |               |
| `access_key_id`        | `string` | Access key ID. Enter access key ID for the DAPI agent user               |               |
| `secret_key`           | `string` | Secret key. Enter secret key for the DAPI agent user                     |               |
| `api_key`              | `string` | Data API key. Enter data API key for the organization                    |               |

### Supported sync modes[​](#supported-sync-modes "Direct link to Supported sync modes")

The Nexus Datasets source connector supports the following [sync modes](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):

* Full Refresh
* Incremental

### Streams[​](#streams "Direct link to Streams")

| Stream Name | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ----------- | ----------- | ---------------- | ------------------ | -------------------- |
| datasets    | ❌          | DefaultPaginator | ✅                 | ✅                   |

### Custom Components[​](#custom-components "Direct link to Custom Components")

NexusCustomAuthenticator is a primary component which handles the HMAC authentication for nexus API.

HMAC stands for Hash-based Message Authentication Code. In HMAC authentication, every request is independently established using a cryptographic hash function. For each API request, the client computes a hashed "signature" using a secret key and submits it in the Authorization header.

Please refer <https://developer.infornexus.com/api/authentication-choices/hmac> for more details to get the data to calculate the HMAC signature.

### Error Codes[​](#error-codes "Direct link to Error Codes")

200 : Data set is ready to stream 202 : Data set is not ready but try again later. 304 : Data set is not ready, check the source again.

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Access Key ID

required

string

access\_key\_id

›

API Key

required

string

api\_key

›

Base URL

required

string

base\_url

›

Dataset Name

required

string

dataset\_name

›

Secret Key

required

string

secret\_key

›

User ID

required

string

user\_id

›

Infor Streaming Mode

string

mode

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                        |
| ------- | ---------- | -------------------------------------------------------- | ---------------------------------------------- |
| 0.1.3   | 2026-02-17 | [73548](https://github.com/airbytehq/airbyte/pull/73548) | Update dependencies                            |
| 0.1.2   | 2026-02-10 | [73030](https://github.com/airbytehq/airbyte/pull/73030) | Update dependencies                            |
| 0.1.1   | 2026-02-03 | [72789](https://github.com/airbytehq/airbyte/pull/72789) | Add missing registryOverrides to metadata.yaml |
| 0.1.0   | 2025-09-30 | [69349](https://github.com/airbytehq/airbyte/pull/69349) | Nexus datasets connector first version         |
