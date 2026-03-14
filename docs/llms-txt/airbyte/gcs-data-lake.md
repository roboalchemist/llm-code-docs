# Source: https://docs.airbyte.com/integrations/destinations/gcs-data-lake.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-gcs-data-lake/latest/icon.svg)

# GCS Data Lake

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.7](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-gcs-data-lake)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-gcs-data-lake)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `8c8a2d3e-1b4f-4a9c-9e7d-6f5a4b3c2d1e`

This page guides you through setting up the GCS Data Lake destination connector.

This connector is Airbyte's official support for the Iceberg protocol on Google Cloud Storage. It writes the Iceberg table format to GCS using a supported Iceberg catalog.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

The GCS Data Lake connector requires two things:

1. A Google Cloud Storage bucket

2. A supported Iceberg catalog. Currently, the connector supports these catalogs:

   <!-- -->

   * BigLake
   * Polaris

## Setup guide[​](#setup-guide "Direct link to Setup guide")

Follow these steps to set up your GCS storage and Iceberg catalog permissions.

### GCS setup and permissions[​](#gcs-setup-and-permissions "Direct link to GCS setup and permissions")

#### Create a GCS bucket[​](#create-a-gcs-bucket "Direct link to Create a GCS bucket")

1. Open the [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Cloud Storage** > **Buckets**
3. Click **CREATE BUCKET**
4. Choose a bucket name and location
5. Select a storage class and access control settings
6. Click **CREATE**

#### Create a service account[​](#create-a-service-account "Direct link to Create a service account")

1. In the Google Cloud Console, navigate to **IAM & Admin** > **Service Accounts**

2. Click **CREATE SERVICE ACCOUNT**

3. Give it a name (for example: `airbyte-gcs-data-lake`)

4. Grant the following roles:

   * **Storage Admin** - For full GCS bucket access
   * **BigQuery Data Editor** - For BigLake catalog operations
   * **BigQuery User** - For BigQuery operations
   * **Service Usage Consumer** - For using GCP services

5. Click **CREATE KEY** and choose the **JSON** format

6. Download the JSON key file

7. In Airbyte, paste the entire contents of this JSON file into the **Service Account JSON** field

### Iceberg catalog setup and permissions[​](#iceberg-catalog-setup-and-permissions "Direct link to Iceberg catalog setup and permissions")

The rest of the setup process differs depending on the catalog you're using.

#### BigLake[​](#biglake "Direct link to BigLake")

The BigLake catalog is Google Cloud's managed Iceberg catalog service. To use BigLake, you need to have created a BigLake catalog in your GCP project. The service account you created earlier should have the necessary permissions to access this catalog.

#### Polaris[​](#polaris "Direct link to Polaris")

To authenticate with Apache Polaris, follow these steps:

1. Set up your Polaris catalog and create a principal with the necessary permissions. Refer to the [Apache Polaris documentation](https://polaris.apache.org/) for detailed setup instructions.

2. When creating a principal in Polaris, you'll receive OAuth credentials (Client ID and Client Secret). Keep these credentials secure.

3. Grant the required privileges to your principal's catalog role. You can either:

   **Option A: grant the broad `CATALOG_MANAGE_CONTENT` privilege** (recommended for simplicity):

   * This single privilege allows the connector to manage tables and namespaces in the catalog

   **Option B: grant specific granular privileges**:

   * `TABLE_LIST` - List tables in a namespace
   * `TABLE_CREATE` - Create new tables
   * `TABLE_DROP` - Delete tables
   * `TABLE_READ_PROPERTIES` - Read table metadata
   * `TABLE_WRITE_PROPERTIES` - Update table metadata
   * `TABLE_WRITE_DATA` - Write data to tables
   * `NAMESPACE_LIST` - List namespaces
   * `NAMESPACE_CREATE` - Create new namespaces
   * `NAMESPACE_READ_PROPERTIES` - Read namespace metadata

4. Ensure that your Polaris catalog has been configured with the appropriate storage credentials to access your GCS bucket.

## Configuration[​](#configuration "Direct link to Configuration")

In Airbyte, configure the following fields:

### Common fields (all catalog types)[​](#common-fields-all-catalog-types "Direct link to Common fields (all catalog types)")

| Field                    | Required | Description                                                                 |
| ------------------------ | -------- | --------------------------------------------------------------------------- |
| **GCS Bucket Name**      | Yes      | The name of your GCS bucket (for example: `my-data-lake`)                   |
| **Service Account JSON** | Yes      | The complete JSON content from your service account key file                |
| **GCP Project ID**       | No       | The GCP project ID. If not specified, extracted from service account        |
| **GCP Location**         | Yes      | The GCP location/region (for example: `us`, `us-central1`, `eu`)            |
| **Warehouse Location**   | Yes      | Root path for Iceberg data in GCS (for example: `gs://my-bucket/warehouse`) |
| **Catalog Type**         | Yes      | Select the type of Iceberg catalog to use: `BigLake` or `Polaris`           |
| **Main Branch Name**     | No       | Iceberg branch name (default: `main`)                                       |
| **Default Namespace**    | No       | Default namespace for tables (for example: `default`, `airbyte_data`)       |

### BigLake-specific fields[​](#biglake-specific-fields "Direct link to BigLake-specific fields")

When **Catalog Type** is set to `BigLake`, configure these additional fields:

| Field                    | Required | Description                                        |
| ------------------------ | -------- | -------------------------------------------------- |
| **BigLake Catalog Name** | Yes      | Name of your BigLake catalog (from the setup step) |

### Polaris-specific fields[​](#polaris-specific-fields "Direct link to Polaris-specific fields")

When **Catalog Type** is set to `Polaris`, configure these additional fields:

| Field                  | Required | Description                                                                            |
| ---------------------- | -------- | -------------------------------------------------------------------------------------- |
| **Polaris Server URI** | Yes      | The base URL of your Polaris server (for example: `http://localhost:8181/api/catalog`) |
| **Catalog Name**       | Yes      | The name of the catalog in Polaris (for example: `quickstart_catalog`)                 |
| **Client ID**          | Yes      | The OAuth Client ID for authenticating with the Polaris server                         |
| **Client Secret**      | Yes      | The OAuth Client Secret for authenticating with the Polaris server                     |

## Supported sync modes[​](#supported-sync-modes "Direct link to Supported sync modes")

| Sync mode                                                                                                                                     | Supported? |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [Full Refresh - Overwrite](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite)                   | Yes        |
| [Full Refresh - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-append)                         | Yes        |
| [Full Refresh - Overwrite + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped) | Yes        |
| [Incremental Sync - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append)                      | Yes        |
| [Incremental Sync - Append + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped)    | Yes        |

## Output schema[​](#output-schema "Direct link to Output schema")

### How Airbyte generates the Iceberg schema[​](#how-airbyte-generates-the-iceberg-schema "Direct link to How Airbyte generates the Iceberg schema")

In each stream, Airbyte maps top-level fields to Iceberg fields. Airbyte maps nested fields (objects, arrays, and unions) to string columns and writes them as serialized JSON.

This is the full mapping between Airbyte types and Iceberg types.

| Airbyte type               | Iceberg type                   |
| -------------------------- | ------------------------------ |
| Boolean                    | Boolean                        |
| Date                       | Date                           |
| Integer                    | Long                           |
| Number                     | Double                         |
| String                     | String                         |
| Time with timezone\*       | Time                           |
| Time without timezone      | Time                           |
| Timestamp with timezone\*  | Timestamp with timezone        |
| Timestamp without timezone | Timestamp without timezone     |
| Object                     | String (JSON-serialized value) |
| Array                      | String (JSON-serialized value) |
| Union                      | String (JSON-serialized value) |

\*Airbyte converts the `time with timezone` and `timestamp with timezone` types to Coordinated Universal Time (UTC) before writing to the Iceberg file.

### Managing schema evolution[​](#managing-schema-evolution "Direct link to Managing schema evolution")

This connector never rewrites existing Iceberg data files. This means Airbyte can only handle specific source schema changes:

* Adding or removing a column
* Widening a column
* Changing the primary key

You have the following options to manage schema evolution:

* To handle unsupported schema changes automatically, use [Full Refresh - Overwrite](/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite.md) as your [sync mode](/platform/using-airbyte/core-concepts/sync-modes/.md).

* To handle unsupported schema changes as they occur, wait for a sync to fail, then take action to restore it. Either:

  <!-- -->

  * Manually edit your table schema in Iceberg directly.
  * [Refresh](/platform/operator-guides/refreshes.md) your connection in Airbyte.
  * [Clear](/platform/operator-guides/clear.md) your connection in Airbyte.

## Deduplication[​](#deduplication "Direct link to Deduplication")

This connector uses a merge-on-read strategy to support deduplication.

* Airbyte translates the stream's primary keys to Iceberg's [identifier columns](https://iceberg.apache.org/spec/#identifier-field-ids).
* An "upsert" is an [equality-based delete](https://iceberg.apache.org/spec/#equality-delete-files) on that row's primary key, followed by an insertion of the new data.

### Assumptions about primary keys[​](#assumptions-about-primary-keys "Direct link to Assumptions about primary keys")

The GCS Data Lake connector assumes that one of two things is true:

* The source never emits the same primary key twice in a single sync attempt.
* If the source emits the same primary key multiple times in a single attempt, it always emits those records in cursor order from oldest to newest.

If these conditions aren't met, you may see inaccurate data in Iceberg in the form of older records taking precedence over newer records. If this happens, use append or overwrite as your [sync modes](/platform/using-airbyte/core-concepts/sync-modes/.md).

An unknown number of API sources have streams that don't meet these conditions. Airbyte knows [Stripe](/integrations/sources/stripe.md) and [Monday](/integrations/sources/monday.md) don't, but there are probably others.

## Branching and data availability[​](#branching-and-data-availability "Direct link to Branching and data availability")

Iceberg supports [Git-like semantics](https://iceberg.apache.org/docs/latest/branching/) over your data. This connector leverages those semantics to provide resilient syncs.

* In each sync, each microbatch creates a new snapshot.
* During truncate syncs, the connector writes the refreshed data to the `airbyte_staging` branch and replaces the `main` branch with the `airbyte_staging` at the end of the sync. Since most query engines target the `main` branch, people can query your data until the end of a truncate sync, at which point it's atomically swapped to the new version.

### Branch replacement[​](#branch-replacement "Direct link to Branch replacement")

At the end of stream sync, the current `main` branch is replaced with the `airbyte_staging` branch. Fast-forwarding is intentionally avoided to better handle potential compaction issues.

**Important Warning**: any changes made to the `main` branch outside of Airbyte's operations after a sync begins is going to be lost during this process.

## Compaction[​](#compaction "Direct link to Compaction")

caution

**Do not run compaction during a truncate refresh sync to prevent data loss.** During a truncate refresh sync, the system deletes all files that don't belong to the latest generation. This includes:

* Files without generation IDs (compacted files)
* Files from previous generations

If compaction runs simultaneously with the sync, it would delete files from the current generation, causing data loss.

## Namespace support[​](#namespace-support "Direct link to Namespace support")

This destination supports [namespaces](https://docs.airbyte.com/platform/using-airbyte/core-concepts/namespaces).

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Catalog Type

required

object

catalog\_type

›

GCP Location

required

string

gcp\_location

›

GCS Bucket Name

required

string

gcs\_bucket\_name

›

Main Branch Name

required

string

main\_branch\_name

›

Default Namespace

required

string

namespace

›

Service Account JSON

required

string

service\_account\_json

›

Warehouse Location

required

string

warehouse\_location

›

GCP Project ID

string

gcp\_project\_id

›

GCS Endpoint (Optional)

string

gcs\_endpoint

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1.0.7   | 2026-02-04 | [72855](https://github.com/airbytehq/airbyte/pull/72855) | Upgrade CDK to 0.2.8                                                                  |
| 1.0.6   | 2026-01-23 | [72300](https://github.com/airbytehq/airbyte/pull/72300) | Upgrade CDK to 0.2.0                                                                  |
| 1.0.5   | 2026-01-14 | [71760](https://github.com/airbytehq/airbyte/pull/71760) | Restore integration tests in CI. Workaround DI error.                                 |
| 1.0.4   | 2026-01-12 | [71227](https://github.com/airbytehq/airbyte/pull/71227) | Add speed mode support with PROTOBUF serialization                                    |
| 1.0.3   | 2026-01-12 | [71258](https://github.com/airbytehq/airbyte/pull/71258) | Migrate to TableSchemaMapper from deprecated ColumnNameMapper pattern                 |
| 1.0.2   | 2025-11-13 | [69317](https://github.com/airbytehq/airbyte/pull/69317) | Connector generally available                                                         |
| 1.0.1   | 2025-11-13 | [69212](https://github.com/airbytehq/airbyte/pull/69212) | Initial release of GCS Data Lake destination with BigLake and Polaris catalog support |
