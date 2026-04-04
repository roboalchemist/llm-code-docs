# Source: https://docs.envzero.com/guides/cost-monitoring/gcp-costs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure GCP Costs

> Set up GCP cost monitoring in env zero using BigQuery billing export and a service account

Google Cloud currently allow you to programmatically inspect your costs by exporting your project's billing information to a dedicated [dataset](https://cloud.google.com/bigquery/docs/datasets-intro) configured in your project's BigQuery database.

## Create a new dataset on BigQuery

Follow [these steps](https://cloud.google.com/bigquery/docs/datasets) provided by GCP official documentation in order to create a new dataset.

## Export Billing Data into BigQuery

Follow [these steps](https://cloud.google.com/billing/docs/how-to/export-data-bigquery#enable-bq-export) provided by GCP official documentation to export your billing information into an existing dataset in your BigQuery database. The exported billing information covers all your GCP projects that are **under the same GCP billing account**.

After the export has been configured, GCP will automatically create a new table in the provided dataset. The new table name should be like `gcp_billing_export_v1_011D4F_BEC512_83EA95` (for e.g).

## Create GCP Service Account key

Follow [these steps](https://cloud.google.com/iam/docs/keys-create-delete) provided by GCP official documentation to export new keys for your service account.

This service account should have the following permissions:

1. `bigquery.jobs.create`
2. `bigquery.tables.getData`

You can either create a custom role that includes these permissions (the preferred, more secured approach) and attach it to the service account, or you can attach the following GCP predefined roles to the service account:

1. `BigQuery Job User`
2. `BigQuery Data Viewer`

After the credentials have been created, download them as a JSON file.

If you wish to create the service account key via Terraform then [our predefined template](https://github.com/env0/templates/tree/master/gcp/service-account-key) could be helpful.

## Add Credentials to your Organization

1. Under your **Organization Settings**, Select the **Credentials** tab
2. Click **Add Credential**
3. Select the `GCP Credentials` type.
4. Enter the BigQuery Table ID that you've created in the previous step.\
   Table ID should look like `<PROJECT_ID>.<DATASET_NAME>.<TABLE_NAME>` where:

* `PROJECT_ID` - the GCP project name.
* `DATASET_NAME` - the dataset name that you've created in the previous step.
* `TABLE_NAME` - the table name that you've created in the previous step.

1. Enter the `Service Account Key JSON` that you've created and downloaded in the previous step.
2. Click **Add**

## Enable cost monitoring

1. Go to the **Project Settings** of the desired project.
2. Select the **Credentials** tab.
3. Check the appropriate cloud provider checkbox, and select the credential you created in the steps above.
4. Click **Save**.

<Warning>
  Data visibility

  Please note that after the configuration of cost monitoring is complete, a redeploy to the environments is needed, and once redeployed it can take 24-48 hours for data to show, depending on the cloud provider's cost exploration capabilities.
</Warning>

Built with [Mintlify](https://mintlify.com).
