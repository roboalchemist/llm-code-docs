# Source: https://clickhouse.ferndocs.com/integrations/azure-data-factory/http-interface.md

---
sidebar_label: Using the HTTP interface
slug: /integrations/azure-data-factory/http-interface
description: >-
  Using ClickHouse's HTTP interface to bring data from Azure Data Factory into
  ClickHouse
keywords:

- azure data factory
- azure
- microsoft
- data
- http interface
title: Using ClickHouse HTTP Interface to bring Azure data into ClickHouse
doc_type: guide

---

The [`azureBlobStorage` Table Function](https://clickhouse.com/docs/sql-reference/table-functions/azureBlobStorage)
is a fast and convenient way to ingest data from Azure Blob Storage into
ClickHouse. Using it may however not always be suitable for the following reasons:

- Your data might not be stored in Azure Blob Storage — for example, it could be in Azure SQL Database, Microsoft SQL Server, or Cosmos DB.
- Security policies might prevent external access to Blob Storage
  altogether — for example, if the storage account is locked down with no public endpoint.

In such scenarios, you can use Azure Data Factory together with the
[ClickHouse HTTP interface](https://clickhouse.com/docs/interfaces/http)
to send data from Azure services into ClickHouse.

This method reverses the flow: instead of having ClickHouse pull the data from
Azure, Azure Data Factory pushes the data to ClickHouse. This approach
typically requires your ClickHouse instance to be accessible from the public
internet.

<Info>
It is possible to avoid exposing your ClickHouse instance to the internet by
using Azure Data Factory's Self-hosted Integration Runtime. This setup allows
data to be sent over a private network. However, it's beyond the scope of this
article. You can find more information in the official guide:
[Create and configure a self-hosted integration
runtime](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime?tabs=data-factory)
</Info>

## Turning ClickHouse into a REST service [#turning-clickhouse-to-a-rest-service]

Azure Data Factory supports sending data to external systems over HTTP in JSON
format. We can use this capability to insert data directly into ClickHouse
using the [ClickHouse HTTP interface](https://clickhouse.com/docs/interfaces/http).
You can learn more in the [ClickHouse HTTP Interface
documentation](https://clickhouse.com/docs/interfaces/http).

For this example, we only need to specify the destination table, define the
input data format as JSON, and include options to allow more flexible timestamp
parsing.

```sql
INSERT INTO my_table
SETTINGS 
    date_time_input_format='best_effort',
    input_format_json_read_objects_as_strings=1
FORMAT JSONEachRow
```

To send this query as part of an HTTP request, you simply pass it as a
URL-encoded string to the query parameter in your ClickHouse endpoint:

```text
https://your-clickhouse-url.com?query=INSERT%20INTO%20my_table%20SETTINGS%20date_time_input_format%3D%27best_effort%27%2C%20input_format_json_read_objects_as_strings%3D1%20FORMAT%20JSONEachRow%0A
```

<Info>
Azure Data Factory can handle this encoding automatically using its built-in
`encodeUriComponent` function, so you don't have to do it manually.
</Info>

Now you can send JSON-formatted data to this URL. The data should match the
structure of the target table. Here's a simple example using curl, assuming a
table with three columns: `col_1`, `col_2`, and `col_3`.

```text
curl \
    -XPOST "https://your-clickhouse-url.com?query=<our_URL_encded_query>" \
    --data '{"col_1":9119,"col_2":50.994,"col_3":"2019-06-01 00:00:00"}'
```

You can also send a JSON array of objects, or JSON Lines (newline-delimited
JSON objects). Azure Data Factory uses the JSON array format, which works
perfectly with ClickHouse's `JSONEachRow` input.

As you can see, for this step you don't need to do anything special on the ClickHouse
side. The HTTP interface already provides everything needed to act as a
REST-like endpoint — no additional configuration required.

Now that we've made ClickHouse behave like a REST endpoint, it's time to
configure Azure Data Factory to use it.

In the next steps, we'll create an Azure Data Factory instance, set up a Linked
Service to your ClickHouse instance, define a Dataset for the
[REST sink](https://learn.microsoft.com/en-us/azure/data-factory/connector-rest),
and create a Copy Data activity to send data from Azure to ClickHouse.

## Creating an Azure data factory instance [#create-an-azure-data-factory-instance]

This guide assumes that you have access to Microsoft Azure account, and you
already have configured a subscription and a resource group. If you have
an Azure Data Factory already configured, then you can safely skip this step
and move to the next one using your existing service.

1. Log in to the [Microsoft Azure Portal](https://portal.azure.com/) and click
   **Create a resource**.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c498422d890fc422293b31a6dfd61c7d36fd13991196e62248775083bbef9834/images/integrations/data-ingestion/azure-data-factory/azure-home-page.png" alt="Azure Portal Home Page"/>

2. In the Categories pane on the left, select **Analytics**, then click on
   **Data Factory** in the list of popular services.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/29a9c002e61b9f9d8a3b1384b1c3886188afe29f6b61737e48fe925a55dccc41/images/integrations/data-ingestion/azure-data-factory/azure-new-resource-analytics.png" alt="Azure Portal New Resource"/>

3. Select your subscription and resource group, enter a name for the new Data
   Factory instance, choose the region and leave the version as V2.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/16e763a7e99e99007bc0ac1f3b004f46caa49c5a8fe7c3e9c0bf79e3ab0e5983/images/integrations/data-ingestion/azure-data-factory/azure-new-data-factory.png" alt="Azure Portal New Data Factory"/>

4. Click **Review + Create**, then click **Create** to launch the deployment.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9b5d84010f54285b09ba8c0071df7c78539bab8796153ea806cfe148a718505d/images/integrations/data-ingestion/azure-data-factory/azure-new-data-factory-confirm.png" alt="Azure Portal New Data Factory Confirm"/>

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c1d359046e268c504113c09655f2882b1d813d7ac5ac934e494114d8f1c377d7/images/integrations/data-ingestion/azure-data-factory/azure-new-data-factory-success.png" alt="Azure Portal New Data Factory Success"/>

Once the deployment completes successfully, you can start using your new Azure
Data Factory instance.

## Creating a new REST-Based linked service [#-creating-new-rest-based-linked-service]

1. Log in to the Microsoft Azure Portal and open your Data Factory instance.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/df6a43ef4ab809b458e782f3dd8577ed37db4a6f7100ea2f288d72757c8ea1c2/images/integrations/data-ingestion/azure-data-factory/azure-home-with-data-factory.png" alt="Azure Portal Home Page with Data Factory"/>

2. On the Data Factory overview page, click **Launch Studio**.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bc40443f5c27bfb93ca5f0bfe2343f9a89b93574bb5975ae40e23c13a001d6f3/images/integrations/data-ingestion/azure-data-factory/azure-data-factory-page.png" alt="Azure Portal Data Factory Page"/>

3. In the left-hand menu, select **Manage**, then go to **Linked services**,
   and click **+ New** to create a new linked service.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dbc9fe8942a8034ffe656ea41acd83c922cde59002d7dd71ecaa6b28b2ac4338/images/integrations/data-ingestion/azure-data-factory/adf-create-linked-service-button.png" alt="Azure Data Factory New Linked Service Button"/>

4. In the **New linked service search bar**, type **REST**, select **REST**, and click **Continue**
   to create [a REST connector](https://learn.microsoft.com/en-us/azure/data-factory/connector-rest)
   instance.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e5399812d4f6d83814933458afbcf49068eff7f80dc8092c9e1a68c32d9a64ad/images/integrations/data-ingestion/azure-data-factory/adf-new-linked-service-search.png" alt="Azure Data Factory New Linked Service Search"/>

5. In the linked service configuration pane enter a name for your new service,
   click the **Base URL** field, then click **Add dynamic content** (this link only
   appears when the field is selected).
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/998908cac470a1ceb04e5a5caeb9e3661c93ea6ccc178410b54a16be99f0ed91/images/integrations/data-ingestion/azure-data-factory/adf-new-lined-service-pane.png" alt="New Lined Service Pane"/>

6. In the dynamic content pane you can create a parameterized URL, which
   allows you to define the query later when creating datasets for different
   tables — this makes the linked service reusable.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/61ee3542fa7cc9f25b45f07afdb4a476f0d43c1061bf5c271423991a8631a579/images/integrations/data-ingestion/azure-data-factory/adf-new-linked-service-base-url-empty.png" alt="New Linked ServiceBase Url Empty"/>

7. Click the **"+"** next to the filter input and add a new parameter, name it
   `pQuery`, set the type to String, and set the default value to `SELECT 1`.
   Click **Save**.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/792d3708afa9c082d199c1f41f1a8fba377223cfe6b125440e30dd7fb9c54fad/images/integrations/data-ingestion/azure-data-factory/adf-new-linked-service-params.png" alt="New Linked Service Parameters"/>

8. In the expression field, enter the following and click **OK**. Replace
   `your-clickhouse-url.com` with the actual address of your ClickHouse
   instance.

   ```text
   @{concat('https://your-clickhouse-url.com:8443/?query=', encodeUriComponent(linkedService().pQuery))}
   ```

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e6964e9e731300623240c15b4863217396af69d0bca1e3376240352be40f225f/images/integrations/data-ingestion/azure-data-factory/adf-new-linked-service-expression-field-filled.png" alt="New Linked Service Expression Field Filled"/>

9. Back in the main form select Basic authentication, enter the username and
   password used to connect to your ClickHouse HTTP interface, click **Test
   connection**. If everything is configured correctly, you'll see a success
   message.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f91ee1a3f26192d1e1b860d2f507dca25c3d3c3d58f9739cec479cb20688dc88/images/integrations/data-ingestion/azure-data-factory/adf-new-linked-service-check-connection.png" alt="New Linked Service Check Connection"/>

10. Click **Create** to finalize the setup.
    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f1d502db952a65736e9fe3dad899e54cc1200d3c769eb254bb3561d8af36da6e/images/integrations/data-ingestion/azure-data-factory/adf-linked-services-list.png" alt="Linked Services List"/>

You should now see your newly registered REST-based linked service in the list.

## Creating a new dataset for the ClickHouse HTTP Interface [#creating-a-new-dataset-for-the-clickhouse-http-interface]

Now that we have a linked service configured for the ClickHouse HTTP interface,
we can create a dataset that Azure Data Factory will use to send data to
ClickHouse.

In this example, we'll insert a small portion of the [Environmental Sensors
Data](https://clickhouse.com/docs/getting-started/example-datasets/environmental-sensors).

1. Open the ClickHouse query console of your choice — this could be the
   ClickHouse Cloud web UI, the CLI client, or any other interface you use to
   run queries — and create the target table:

   ```sql
   CREATE TABLE sensors
   (
       sensor_id UInt16,
       lat Float32,
       lon Float32,
       timestamp DateTime,
       temperature Float32
   )
   ENGINE = MergeTree
   ORDER BY (timestamp, sensor_id);
   ```

2. In Azure Data Factory Studio, select Author in the left-hand pane. Hover
   over the Dataset item, click the three-dot icon, and choose New dataset.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a819d844a209b9726147f791995c8b67a45400623fccc275b155af7efe6a3614/images/integrations/data-ingestion/azure-data-factory/adf-new-dataset-item.png" alt="New Dataset Item"/>

3. In the search bar, type **REST**, select **REST**, and click **Continue**.
   Enter a name for your dataset and select the **linked service** you created
   in the previous step. Click **OK** to create the dataset.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d3a5ac94bc0f8ea6e9c98073ce5ec2eced561dc027a6ce1dd7e3d919674cf978/images/integrations/data-ingestion/azure-data-factory/adf-new-dataset-page.png" alt="New Dataset Page"/>

4. You should now see your newly created dataset listed under the Datasets
   section in the Factory Resources pane on the left. Select the dataset to
   open its properties. You'll see the `pQuery` parameter that was defined in the
   linked service. Click the **Value** text field. Then click **Add dynamic**
   content.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/55005424bd02ca4cd0b57b01b807093ff22737b31e5b45b9924ef6b31d518125/images/integrations/data-ingestion/azure-data-factory/adf-new-dataset-properties.png" alt="New Dataset Properties"/>

5. In the pane that opens, paste the following query:

   ```sql
   INSERT INTO sensors
   SETTINGS 
       date_time_input_format=''best_effort'', 
       input_format_json_read_objects_as_strings=1 
   FORMAT JSONEachRow
   ```

   :::danger
   All single quotes `'` in the query must be replaced with two single quotes
   `''`. This is required by Azure Data Factory's expression parser. If you
   don't escape them, you may not see an error immediately — but it will fail
   later when you try to use or save the dataset. For example, `'best_effort'`
   must be written as `''best_effort''`.
   :::

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/08e584b87282fa6b4a6814634e01f32f4492f8497ee540cf582fa44ded28619c/images/integrations/data-ingestion/azure-data-factory/adf-new-dataset-query.png" alt="New Dataset Query"/>

6. Click OK to save the expression. Click Test connection. If everything is
   configured correctly, you'll see a Connection successful message. Click Publish
   all at the top of the page to save your changes.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/af3bc4fd0a1036ec8f408c1db3b3537755c5bfd1a81322e884f3c372dd6d5d45/images/integrations/data-ingestion/azure-data-factory/adf-new-dataset-connection-successful.png" alt="New Dataset Connection Successful"/>

### Setting up an example dataset [#setting-up-an-example-dataset]

In this example, we will not use the full Environmental Sensors Dataset, but
just a small subset available at the
[Sensors Dataset Sample](https://datasets-documentation.s3.eu-west-3.amazonaws.com/environmental/sensors.csv).

<Info>
To keep this guide focused, we won't go into the exact steps for creating the
source dataset in Azure Data Factory. You can upload the sample data to any
storage service of your choice — for example, Azure Blob Storage, Microsoft SQL
Server, or even a different file format supported by Azure Data Factory.
</Info>

Upload the dataset to your Azure Blob Storage (or another preferred storage
service), Then, in Azure Data Factory Studio, go to the Factory Resources pane.
Create a new dataset that points to the uploaded data. Click Publish all to
save your changes.

## Creating a Copy Activity to transfer data to ClickHouse [#creating-the-copy-activity-to-transfer-data-to-clickhouse]

Now that we've configured both the input and output datasets, we can set up a
**Copy Data** activity to transfer data from our example dataset into the
`sensors` table in ClickHouse.

1. Open **Azure Data Factory Studio**, go to the **Author tab**. In the
   **Factory Resources** pane, hover over **Pipeline**, click the three-dot
   icon, and select **New pipeline**.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/800d08caf692e24c7a5076afd47b02ea0b1613f4c3f4cfa9ff20ae5e930c6d06/images/integrations/data-ingestion/azure-data-factory/adf-new-pipeline-item.png" alt="ADF New Pipeline Item"/>

2. In the **Activities** pane, expand the **Move and transform** section and
   drag the **Copy data** activity onto the canvas.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/986b77241bbf45251e26720de318e3828b12c5653d423faba3451dba96c15fe0/images/integrations/data-ingestion/azure-data-factory/adf-new-copy-data-item.png" alt="New Copy DataItem"/>

3. Select the **Source** tab, and choose the source dataset you created earlier.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ace2e1a21ff2b85463369914057205861680408975a22469e0d21b2566b1d386/images/integrations/data-ingestion/azure-data-factory/adf-copy-data-source.png" alt="Copy Data Source"/>

4. Go to the **Sink** tab and select the ClickHouse dataset created for your
   sensors table. Set **Request method** to POST. Ensure **HTTP compression
   type** is set to **None**.
   :::warning
   HTTP compression does not work correctly in Azure Data Factory's Copy Data
   activity. When enabled, Azure sends a payload consisting of zero bytes only
   — likely a bug in the service. Be sure to leave compression disabled.
   :::
   :::info
   We recommend keeping the default batch size of 10,000, or even increasing it
   further. For more details, see
   [Selecting an Insert Strategy / Batch inserts if synchronous](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy#batch-inserts-if-synchronous)
   for more details.
   :::
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7913a5228fb3ba1ec212ad9b2e5e5d4aea4bd948192aabaa2c0f6c40b3c989d3/images/integrations/data-ingestion/azure-data-factory/adf-copy-data-sink-select-post.png" alt="Copy Data Sink Select Post"/>

5. Click **Debug** at the top of the canvas to run the pipeline. After a short
   wait, the activity will be queued and executed. If everything is configured
   correctly, the task should finish with a **Success** status.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b773dbb94017e17d5820a5f54078a7a27d091c36c5ec91b0fd7c4c2b70ef84dd/images/integrations/data-ingestion/azure-data-factory/adf-copy-data-debug-success.png" alt="Copy Data Debug Success"/>

6. Once complete, click **Publish all** to save your pipeline and dataset changes.

## Additional resources [#additional-resources-1]

- [HTTP Interface](https://clickhouse.com/docs/interfaces/http)
- [Copy and transform data from and to a REST endpoint by using Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/connector-rest?tabs=data-factory)
- [Selecting an Insert Strategy](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy)
- [Create and configure a self-hosted integration runtime](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime?tabs=data-factory)
