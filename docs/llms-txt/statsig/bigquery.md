# Source: https://docs.statsig.com/statsig-warehouse-native/connecting-your-warehouse/bigquery.md

# Source: https://docs.statsig.com/integrations/data-imports/bigquery.md

# Source: https://docs.statsig.com/data-warehouse-ingestion/bigquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# BigQuery

## Overview

To set up connection with BigQuery, we need the following:

* Granting Permissions to a Statsig-owned Service Account
* Your BigQuery Project ID

Start by enabling the BigQuery source under Metrics -> Ingestion -> Add Source.

## Grant Permissions to Statsig's Service Account

You need to grant some permissions for Statsig from your Google Cloud console in order for us to access your BigQuery data.

1. In your BigQuery's [IAM & Admin settings](https://console.cloud.google.com/iam-admin/), add the Statsig service account you copied in the Statsig Console as a new principal for your project, and give it the following roles:
   * `BigQuery User`

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/bigquery/198107543-b3bcc19a-3231-4128-be42-a5dd52fb168a.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=816d567992fa66c29f63a39c426aaf31" alt="BigQuery IAM permissions configuration" width="2178" height="1186" data-path="images/statsig-warehouse-native/connecting-your-warehouse/bigquery/198107543-b3bcc19a-3231-4128-be42-a5dd52fb168a.png" />
</Frame>

<br />

2. Navigate to your [BigQuery SQL Workspace](https://console.cloud.google.com/bigquery), choose the dataset, click on "+ Sharing" -> "Permissions" -> "Add Principal" to give the same Statsig service account "BigQuery Data Viewer" role on the dataset.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/data-imports/bigquery/175113611-90e618ad-f6e8-4005-933e-2a5660a14466.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=4d91003c29e3b87999518c6ee20a30f9" alt="BigQuery dataset permissions setup" width="1175" height="306" data-path="images/integrations/data-imports/bigquery/175113611-90e618ad-f6e8-4005-933e-2a5660a14466.png" />
   </Frame>

Now the service account should have the required permissions to export data from this dataset.

## BigQuery Project ID

Find your BigQuery Project ID below

1. Click on your Project Dropdown inside your Cloud Console.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/bigquery/187518062-7027f682-d1fd-445e-9947-897e44ea929e.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=3497bd283a95d0228559205c4d3ce464" alt="Frame 4" width="885" height="596" data-path="images/statsig-warehouse-native/connecting-your-warehouse/bigquery/187518062-7027f682-d1fd-445e-9947-897e44ea929e.png" />
</Frame>

2. Copy and paste relevant Project ID from the modal pop-up.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/bigquery/187517901-9e7fd237-8325-4254-a1bd-c75f0ea08497.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=ec878fc56db68dfbc92ff58a3a58d16d" alt="Frame 5" width="813" height="634" data-path="images/statsig-warehouse-native/connecting-your-warehouse/bigquery/187517901-9e7fd237-8325-4254-a1bd-c75f0ea08497.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).