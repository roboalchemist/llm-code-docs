# Source: https://docs.axonius.com/docs/google-big-query.md

# Google BigQuery

BigQuery is a serverless, highly-scalable, and cost-effective cloud data warehouse with an in-memory BI Engine and machine learning built in.
This adapter is similar to the CSV adapter.
The format of the table must be simliar to that described for the [CSV adapter](/docs/csv#which-fields-are-required-for-each-import-type).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
  , Aggregated Security Findings
  , Software, SaaS Applications

## Parameters

1. **Project ID** *(required)* - The ID of the Google Cloud Project.

2. **Dataset ID** *(required)* - TheThe ID of the Google Big Query Dataset.

3. **Table ID** *(required)* - The ID of the Google Big Query Table.

4. **JSON Key pair for the service account** *(required)* - A JSON-document containing service-account credentials to GCP. For details, see [Connect Axonius to Google Cloud Platform](/docs/google-cloud-platform-gcp#connect-axonius-to-google-cloud-platform).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="GoogleBigQuery(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GoogleBigQuery(1).png" />

## APIs

Axonius uses the [Google BigQuery API](https://cloud.google.com/bigquery/docs/reference/rest)

## Required Permissions

The following permissions are required:

* Google BigQuery API must be enabled in the Google Cloud project

* Requires one of the following OAuth scopes:

  `https://www.googleapis.com/auth/bigquery`

  `https://www.googleapis.com/auth/cloud-platform`

  `https://www.googleapis.com/auth/bigquery.readonly`

  `https://www.googleapis.com/auth/cloud-platform.read-only`

* The following permissions are required to run a query job:

  `bigquery.jobs.create` on the project.

  `bigquery.tables.getData` on all tables and views that your query references. To query views, you also need this permission on all underlying tables and views. If you're using authorized views or authorized datasets, you don't need access to the underlying source data.

## Supported From Version

Supported from Axonius version 6.0