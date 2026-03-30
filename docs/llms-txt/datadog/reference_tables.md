# Source: https://docs.datadoghq.com/reference_tables.md

---
title: Reference Tables
description: >-
  Combine custom metadata with Datadog data by uploading CSV files or connecting
  cloud storage to enrich logs, security data, and analytics.
breadcrumbs: Docs > Reference Tables
---

# Reference Tables

## Overview{% #overview %}

Reference Tables allow you to combine custom metadata with information already in Datadog. You can define new entities like customer details, service names and information, or IP addresses by uploading a CSV file containing a table of information. The entities are represented by a primary key in a Reference Table and the associated metadata.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/reference-table.0359451fd94d11f2508593dcaa742f5b.png?auto=format"
   alt="A reference table with data populated in the columns for org id, org name, parent org, account owner, and csm" /%}

For example, you can:

- **Enrich logs and security data for faster investigations:** Correlate logs, traces, and security events with up-to-date business contextâsuch as customer names, account owners, threat intelligence, or error code descriptionsâto accelerate troubleshooting and analysis.
- **Segment users and resources for targeted analytics and cost management:** Group users, customers, or cloud resources into meaningful segments (like user tiers, teams, or business units) for deeper product analytics and precise cost attribution using tools like Tag Pipelines.
- **Enhance data for advanced querying and reporting:** Join external data from Reference Tables in Sheets, DDSQL Editor, or Notebooks to perform complex queries, aggregations, and build custom reports without technical expertise.

## Create a Reference Table{% #create-a-reference-table %}

Datadog supports the following data sources, including integrations and manual CSV upload:

{% tab title="Cloud storage" %}

{% collapsible-section open=null %}
#### Manual upload

Click **New Reference Table +**, then upload a CSV file, name the appropriate columns, and define the primary key for lookups.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/enrichment-table-setup.86e918c0f0e15ac2f8cd4396e274e7aa.png?auto=format"
   alt="The Define the Schema section showing a table with org_id marked as the primary key and columns with data for org id, org name, parent org, account owner, and csm " /%}

**Note**: The manual CSV upload method supports files up to 4MB.
{% /collapsible-section %}

{% collapsible-section #amazon-s3 %}
#### Amazon S3

Reference Tables can automatically pull a CSV file from an Amazon S3 bucket to keep your data up to date. The integration looks for changes to the CSV file in S3, and when the file is updated it replaces the Reference Table with the new data. This also enables API updating with the S3 API once the initial Reference Table is configured. **Note**: Reference Tables are not replaced if the content of the CSV file is unchanged.

To update Reference Tables from S3, Datadog uses the IAM role in your AWS account that you configured for the [AWS integration](https://app.datadoghq.com/account/settings#integrations/amazon-web-services). If you have not yet created that role, [follow these steps](https://docs.datadoghq.com/integrations/amazon_web_services/?tab=automaticcloudformation#installation) to do so. To allow that role to update your Reference Tables, add the following permission statement to its IAM policies. Be sure to edit the bucket names to match your environment.

**Note**: If using server-side encryption, you can upload Reference Tables encrypted with Amazon S3-managed keys (SSE-S3) or AWS Key Management Service keys (SSE-KMS).

```json
{
    "Statement": [
        {
            "Sid": "EnrichmentTablesS3",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                // Grant KMS decrypt permissions if uploading KMS-encrypted object
                // "kms:Decrypt",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<MY_BUCKET_NAME_1/*>",
                "arn:aws:s3:::<MY_BUCKET_NAME_2>"
            ]
        }
    ],
    "Version": "2012-10-17"
}
```

#### Define the table{% #define-the-table %}

Click **New Reference Table +**, then add a name, select Amazon S3, fill out all fields, click import, and define the primary key for lookups.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/configure-s3-reference-table.39612e37e79a8a6bc0c7063cd8e5e427.png?auto=format"
   alt="The upload your data section with the Amazon S3 tile selected and data filled in for AWS Account, Bucket, and Path" /%}

**Note**: The upload from an S3 bucket method supports files up to 200MB.
{% /collapsible-section %}

{% collapsible-section #azure-storage %}
#### Azure storage

1. If you haven't already, set up the [Azure integration](https://app.datadoghq.com/integrations/azure) within the subscription that holds the storage account from which you want to import your Reference Table. This involves [creating an app registration that Datadog can](https://docs.datadoghq.com/integrations/azure/?tab=azurecliv20#integrating-through-the-azure-portal) integrate with.

1. In the Azure Portal, select the storage account that stores your Reference Table files.

1. Within your storage account, navigate to **Access Control (IAM)** and select **Add** > **Add Role Assignment**.

1. Input and select the **Storage Blob Data Reader** Role. The [Storage Blob Data Reader role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-reader) allows Datadog to read and list storage containers and blobs.

1. In the **Members** tab, click **+ Select members**. Select the app registration you created in Step 1.

   {% image
      source="https://datadog-docs.imgix.net/images/reference_tables/add_members.bbbaf670376f94f45cde38445df6bebd.png?auto=format"
      alt="The Members section in the Azure Portal where a member is selected and data filled in for the Name, Object ID, and Type" /%}

After reviewing and assigning the role, you can import into Reference Tables from Azure. It may take a few minutes for your Azure configuration to update in Datadog.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/azure_storage.3d8245d8d6148b8bed9fcbaa19a4a3b8.png?auto=format"
   alt="An Azure Storage tile in the Upload or import data section of a new reference table workflow" /%}

For more information, see the [Azure integration documentation](https://docs.datadoghq.com/integrations/azure/).

**Note**: The upload from cloud object storage supports files up to 200MB.
{% /collapsible-section %}

{% collapsible-section #google-cloud-storage %}
#### Google Cloud storage

### Google Cloud storage{% #google-cloud-storage %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Reference Tables are not available for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site) ()
{% /alert %}


{% /callout %}

1. If you have not set up a Google Cloud integration with Datadog or you are using legacy Google project ID files (legacy projects are indicated in your GCP integration tile), follow the instructions for setting up the [Google Cloud Platform integration](https://docs.datadoghq.com/integrations/google_cloud_platform/#setup). This involves creating a [Google Cloud service account](https://docs.datadoghq.com/integrations/google_cloud_platform/#1-create-your-google-cloud-service-account).

1. From the Google Cloud console, navigate to the **Cloud Storage** page.

1. Find the bucket you'd like to grant access to and click on it.

1. Click on the **Permissions** tab. Under "View By Principals", click the **Grant Access** button.

1. In the window that appears, under the "New principals" field, enter the service account email that you created and added to the GCP tile in Step 1. Under "Assign roles", select the **Storage Object Viewer** role. Click **Save**.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/grant_access.79d22ad46a495d9e94621cc603831b1a.png?auto=format"
   alt="Google Cloud console showing the configuration to grant access" /%}

After reviewing and assigning the role, you can import into Reference Tables from Google Cloud. It may take a few minutes for your configuration to update in Datadog.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/gcp_upload_import_ui.b6af4623e8dc3c51861dca9b2d89b0b4.png?auto=format"
   alt="Select GCP Storage in Upload or import data when creating a new reference table" /%}

**Note**: The upload from cloud object storage supports files up to 200MB.
{% /collapsible-section %}

{% collapsible-section #api-or-terraform %}
#### API or Terraform

Create reference tables programmatically using the [Datadog API](https://docs.datadoghq.com/api/latest/reference-tables/) or the [Datadog Terraform provider](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/reference_table).

**Note**: The API and Terraform provider support the same file size limits as cloud storage uploads. See Reference Table limits for details.

### API{% #api %}

Use the [Create Reference Table endpoint](https://docs.datadoghq.com/api/latest/reference-tables/#create-reference-table) to create reference tables from cloud storage or local files.

- For cloud storage sources (S3, Azure, GCS), provide `access_details` in `file_metadata` pointing to a CSV file in cloud storage.
- For local files, call `POST /api/latest/reference-tables/uploads` to get an upload ID and upload your CSV data. Then, call the Create Reference Table endpoint with the `upload_id` in `file_metadata`.

### Terraform{% #terraform %}

Use the `datadog_reference_table` resource to manage reference tables as infrastructure as code. Configure the resource with your table schema, primary keys, and cloud storage access details.
{% /collapsible-section %}

{% /tab %}

{% tab title="Integrations" %}

- [databricks](https://docs.datadoghq.com/integrations/databricks/#reference-table-configuration)
- [salesforce](https://docs.datadoghq.com/integrations/salesforce/#enabling-ingestion-of-reference-tables)
- [servicenow](https://docs.datadoghq.com/integrations/servicenow/#reference-tables)
- [snowflake](https://docs.datadoghq.com/integrations/snowflake_web/#reference-tables)

{% /tab %}

This Reference Table can be used to add additional attributes to logs with the [Lookup Processor](https://docs.datadoghq.com/logs/log_configuration/processors/#lookup-processor).

## Validation rules{% #validation-rules %}

Reference Table names and column headers are validated using the following naming conventions and automatically updated or normalized, if necessary.

| Rule                                                                              | Normalization                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Names and headers cannot be duplicated.                                           | Duplicated names are enumerated. For example, if `fileid` is used twice as a name, the first instance becomes `fileid1` and the second instance becomes `fileid2`. If a name or header is enumerated and it exceeds the 56 characters, it is rejected and needs to be renamed. |
| Names and headers cannot contain uppercase letters.                               | Names with uppercase letters are converted to lowercase. This conversion may result in duplicate names, which are then enumerated. For example, `Fileid` and `FileID` both become `fileid` and are enumerated to `fileid1` and `fileid2` respectively.                         |
| Names and headers cannot contain spaces.                                          | Spaces other than leading and trailing spaces are replaced with underscore `_` characters. Leading and trailing spaces are removed. For example, `customer names` is replaced with `customer_names`.                                                                           |
| Names and headers must start with a lowercase letter.                             | Uppercase characters are converted to lowercase. Non-letter leading characters are removed. For example, `23Two_three` becomes `two_three`.                                                                                                                                    |
| Names and headers support only lowercase letters, numbers, and the `_` character. | Unsupported characters are replaced with the underscore `_` character, unless it breaks one of the rules above. In that case, the unsupported characters are normalized by the respective rule.                                                                                |
| Names and headers must be 56 characters or less.                                  | No normalization is done. Names and headers that have more than 56 characters are rejected and need to be renamed.                                                                                                                                                             |

## Modify a Reference Table{% #modify-a-reference-table %}

To modify an existing Reference Table with new data, select a table and click **Update Config** on the top right corner. The selected CSV is upserted into the table, meaning that:

- All existing rows with the same primary key are updated
- All new rows are added
- All old rows that are not in the new file are deleted

Once the table is saved, the upserted rows are processed asynchronously and updated in the preview. It may take up to 10 minutes for the update to complete.

## Export a Reference Table{% #export-a-reference-table %}

To export a Reference Table, select a table and click **Query in DDSQL Editor**. From there, you can use the [DDSQL Editor](https://docs.datadoghq.com/ddsql_editor/#save-and-share-queries) to export to CSV, Dashboard, and more.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/query_ddsql_editor.f730afcd1f24e28e138436bd8d54553e.png?auto=format"
   alt="Table preview with a blue button labeled Query in DDSQL Editor positioned above the results" /%}

## Delete a Reference Table{% #delete-a-reference-table %}

To delete a Reference Table, select a table, click the gear icon in the top right corner, and then click **Delete Table**. The table and all associated rows is deleted.

If there is a Lookup Processor using a Reference Table for Log enrichment, then the enrichment stops. It may take up to 10 minutes for the enrichment to stop.

## Monitor Reference Table Activity{% #monitor-reference-table-activity %}

You can monitor reference table activity with [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/) or [Change Events](https://docs.datadoghq.com/events/). To view the audit trail and change events for a specific reference table, select the table and click the Settings icon next to **Update Config**. You need org management permissions to view the audit trail.

### Audit Trail{% #audit-trail %}

Use the audit trail for reference tables to track user-triggered actions. Audit trail events are sent when a user initially uploads or imports a CSV file, or when a user creates, modifies, or deletes a reference table.

The `reference_table_file` Asset Type displays import/upload events and the `reference_table` Asset Type displays reference table events. The audit trail provides observability into the content of a reference table.

### Change Events{% #change-events %}

Use change events for reference tables to track automated or user-triggered actions. They are sent when a cloud file is imported from a user or automatic refresh. (Uploading a local file does not generate a change event.) While events can track user-triggered actions, they are mainly used to track triggered imports when a reference table automatically pulls a new CSV file.

Events contain information about the success status, path, and table name of the import. If an error occurs, information about the error type is provided.

### Alerting{% #alerting %}

To be alerted on errors encountered during imports, use [Event Monitors](https://docs.datadoghq.com/monitors/types/event/) for reference table change events. Reference table change events are sent from the `reference_tables` source.

You can create monitors from the **Monitors** tab, or click on the Settings icon next to **New Reference Table +** to generate a pre-filled monitor.

## Reference Table limits{% #reference-table-limits %}

- A reference table can have up to 50 columns
- The size of a reference table file uploaded through the UI can be up to 4 MB
- The size of a reference table file uploaded through a cloud bucket file can be up to 200 MB
- The size of a reference table file uploaded through an integration can be up to 200 MB
- You can have up to 100 reference tables per organization

Reach out to [support](https://docs.datadoghq.com/help/) if you have a use case that exceeds these limits.

## Automatic update frequency{% #automatic-update-frequency %}

Reference Tables can be updated automatically, depending on the data source:

- **Cloud file storage** (Amazon S3, Azure Storage, Google Cloud Storage): Every 5 minutes
- **Integrations**: Every hour
- **CSV manual uploads**: Automatic updates are not supported

## Permissions{% #permissions %}

### Role based access{% #role-based-access %}

To view Reference Tables, users require the `reference_tables_read` permission. To create or modify Reference Tables, users require the `reference_tables_write` permission.

For more information on permissions, see the [RBAC documentation](https://docs.datadoghq.com/account_management/rbac/permissions/#reference-tables).

### Granular access controls{% #granular-access-controls %}

Restrict access to individual tables by specifying a list of teams, roles, or users that are allowed to view or edit them.

{% image
   source="https://datadog-docs.imgix.net/images/reference_tables/granular_access_permissions.efe507b9afd55a1cf75efe5d89f4e488.png?auto=format"
   alt="The Permissions cog option that supports setting granular access permissions on a table" /%}

1. Click on a table to open its detail page.
1. Click the cog icon in the upper-right corner.
1. Select **Permissions** from the menu.
1. Click **Restrict Access**.
1. Use the dropdown to select one or more teams, roles, or users.
1. Click **Add**.
1. Select either **Editor** or **Viewer**.
1. Click **Save** to apply changes.

## Further Reading{% #further-reading %}

- [Simplify log collection and aggregation for MSSPs with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-mssp)
- [Use the lookup processor to enrich logs from a Reference Table](https://docs.datadoghq.com/logs/log_configuration/processors)
- [Filter logs based on Reference Tables](https://docs.datadoghq.com/logs/explorer/advanced_search#filter-logs-based-on-reference-tables)
- [Sheets lookup](https://docs.datadoghq.com/sheets/#lookup)
- [Lookup processor for Events](https://docs.datadoghq.com/events/pipelines_and_processors/lookup_processor/)
- [Use Reference Tables to add multiple tags to cost data](https://docs.datadoghq.com/cloud_cost_management/tag_pipelines/#map-multiple-tags)
- [Learn about Reference Table joins with metrics](https://docs.datadoghq.com/metrics/reference_table_joins_with_metrics/)
- [Add more context to your logs with Reference Tables](https://www.datadoghq.com/blog/add-context-with-reference-tables/)
- [Enrich your existing Datadog telemetry with custom metadata using Reference Tables](https://www.datadoghq.com/blog/reference-tables/)
- [Add more context to Cloud SIEM detections and investigations with Datadog Reference Tables](https://www.datadoghq.com/blog/add-context-with-reference-tables-in-cloud-siem/)
