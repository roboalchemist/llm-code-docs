# Source: https://docs.datafold.com/integrations/databases/databricks.md

# Databricks

**Steps to complete:**

1. [Generate a Personal Access Token](/integrations/databases/databricks#generate-a-personal-access-token)
2. [Retrieve SQL warehouse settings](/integrations/databases/databricks#retrieve-sql-warehouse-settings)
3. [Create schema for Datafold](/integrations/databases/databricks#create-schema-for-datafold)
4. [Configure your data connection in Datafold](/integrations/databases/databricks#configure-in-datafold)

## Generate a Personal Access Token

Visit **Settings** → **User Settings**, and then switch to **Personal Access Tokens** tab.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=77790371e1ab9da75072541115e76ef3" data-og-width="2638" width="2638" data-og-height="1644" height="1644" data-path="images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c7b74e10b593263d0cc301624721bfb3 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=ae39c6e82f203dd6c3c5b1f9334b48d0 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83b3833dc6231cc68cd41e6ab3551d0b 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=6150f351a20c0d48f7fddeea8bdf2e91 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4db8795496564e463a41237244b5636c 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b1e324220abdd51fe0c8b8e2bb41c4c2 2500w" />
</Frame>

Then, click **Generate new token**. Save the generated token somewhere, you'll need it later on.

## Retrieve SQL warehouse settings

In **SQL** mode, navigate to **SQL Warehouses**.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b9b5121c2a90cc855b8c2a5b0ef447ef" data-og-width="724" width="724" data-og-height="455" height="455" data-path="images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4e71648f9866e2051eca35f6f4b1930b 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=41bc7c67a4c9ce7a7f4ac2f7d7db8765 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=15e096e254600bfb0de3bb96b30de6f3 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cca8159fd049d6198ae0f02809e134ed 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=5ab9363e2bdab2a0254bf7640e95b6dc 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c538938c20ac5236d8eda63c3de67072 2500w" />
</Frame>

Choose the preferred warehouse and copy the following fields values from its **Connection Details** tab:

* Server hostname
* HTTP path

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c08e73c1c329dfe0120cc7a6287dd4a7" data-og-width="2638" width="2638" data-og-height="1644" height="1644" data-path="images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a554bf925d1acb4c0d65f7c459ba901c 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9e38ad072bd7875aae1731d6f835bb76 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=04b92efdc808ad8ad63eb4b25c55d8ab 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c6b1832bae9efb023c665709eb1d72af 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=20a9617da84665fd3f8ffcf7bc7bacc9 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8fec93f2fc8b8b819c4304d93895260f 2500w" />
</Frame>

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                   | Description                                                                                                                                                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                         | A name given to the data connection within Datafold                                                                                                                                                                                              |
| Host                         | The hostname retrieved in the Connection Details tab                                                                                                                                                                                             |
| HTTP Path                    | The HTTP Path retrieved in the Connection Details tab                                                                                                                                                                                            |
| Access Token                 | The token retrieved in [Generate a Personal Access Token](/integrations/databases/databricks#generate-a-personal-access-token)                                                                                                                   |
| Catalog                      | The catalog and schema name of your Databricks account. Formatted as catalog\_name.schema\_name (In most cases, catalog\_name is hive\_metastore.)                                                                                               |
| Dataset for temporary tables | Certain operations require Datafold to materialize intermediate results, which are stored in a dedicated schema. The input for this field should be in the catalog\_name.schema\_name format. (In most cases, catalog\_name is hive\_metastore.) |

Click **Create**. Your data connection is ready!
