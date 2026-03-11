# Source: https://docs.axonius.com/docs/send-to-google-bigquery-table.md

# Google BigQuery - Send to Table

**Google BigQuery - Send to Table** inserts the entities retrieved from the saved query or selected in the asset table to the supplied Google BigQuery table. When used with a saved query as a trigger, only the fields configured in the saved query are inserted to the supplied table.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Table name** - The table name.
  * If the table name already exists, new records will be added to that table. If the table schema does not match the query columns, the insertion will fail.
  * If the table name does not exist, a new table will be created and new records will be added to that table. The table schema will be determined based on the query columns.

* **Project ID** - Project ID where the specified table will created.

* **Dataset ID** - Dataset ID where the specified table will created.

* **JSON Key pair for the service account authentication** - A JSON-document containing service-account credentials to GCP, For details, see [Connect Axonius to Google Cloud Platform](/docs/google-cloud-platform-gcp#connect-axonius-to-google-cloud-platform).

* **Append or override the table** *(default: Override)* - Select whether to override the table data or to append the table, if already exists, and add new records to it.

* **Partitioning** *(default: No partitioning)* - Select whether to create a partitioned table for the inserted data:
  * If **No partitioning** is selected, the table won't be partitioned.
  * If **Partition by ingestion time** is selected:
    * The table will be partitioned by calendar days.
    * Select whether a partition filter is required. Requiring a partition filter means users must include a WHERE clause that specifies the partitions to query. Using a partition filter may reduce cost and improve performance.
    * The **Partition type** and **Partitioning filter** fields can be found after the **Map Axonius fields to Google BigQuery fields** field.
  * **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
* **Map Axonius fields to Google BigQuery fields** *(optional, default: empty)* - Use the **Field Mapping Wizard** to map Axonius fields to fields in Google BigQuery. In this way you can transfer data found in Axonius into Google BigQuery. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  NOTE

  For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).
</Callout>

## Required Permissions

The stored credentials must have permission to perform this Enforcement Action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).