# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/data-storage/databricks.md

# Databricks

> Integrating into Databricks to seamlessly export your data to Delta Lake

Galileo supports integrating into *Databricks Unity Catalog*. This allows you to directly export data your Evaluate or Observe data to Databricks.

<Info>Before starting, make sure you've created a Databricks Unity [Catalog](https://docs.databricks.com/en/catalogs/create-catalog.html) and have a [Compute Instance](https://docs.databricks.com/en/compute/configure.html)</Info>

To set up your Databricks integration, go to 'Settings & Permissions', followed by 'Integrations'. Open "Databricks" from the Data Storage section.

You'll be prompted for:

* Hostname

* Path

* Catalog names

* API Token

You can get these under the 'Connection Details' of your 'SQL Warehouses'

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dbx_path_host.png)

Once your integration is set up, you should be able to export data to your Databricks Delta Lake. Enter a name for the cluster and table, and Galileo will export your data straight into your Databricks Unity Catalog.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dbx_export.png)
