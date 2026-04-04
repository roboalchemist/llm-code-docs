# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/data-storage/databricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_path_host.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=864b6fa66cc52a17c16767d4be4a505f" alt="" data-og-width="1406" width="1406" data-og-height="1088" height="1088" data-path="images/dbx_path_host.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_path_host.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=8233581e1904ac20f015916c25d1d209 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_path_host.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=dd002d00da9583c147bcc06fce915d62 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_path_host.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=5b1bf72ba694258ff63d5004bb5e578a 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_path_host.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=5124d27b12001b31b84c99d4066142a5 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_path_host.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=066ebb3ec840b2d2917a8443f22a315d 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_path_host.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6a117d64dd6024b00b4c3444785815e7 2500w" />

Once your integration is set up, you should be able to export data to your Databricks Delta Lake. Enter a name for the cluster and table, and Galileo will export your data straight into your Databricks Unity Catalog.

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_export.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=5da43b0698d1f3d55d09c97fe5347f2f" alt="" data-og-width="1406" width="1406" data-og-height="1088" height="1088" data-path="images/dbx_export.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_export.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=5cd6a87cb5f789cbe14bcd166987fa76 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_export.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=9cdfa10959a940aa599a6d416b5866e1 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_export.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=1f5b722d8fa006581d52cda84e8d9966 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_export.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=265148ac21de383d1bfcd0faaa47d346 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_export.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=30859f7747e6d8d381e81c39b0163692 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dbx_export.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c7917d12996f0e38dd4d054cbd22e37a 2500w" />
