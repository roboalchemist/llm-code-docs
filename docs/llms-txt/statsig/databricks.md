# Source: https://docs.statsig.com/statsig-warehouse-native/connecting-your-warehouse/databricks.md

# Source: https://docs.statsig.com/data-warehouse-ingestion/databricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Databricks

## Overview

To set up connection with Databricks, Statsig needs the following

* API Key
* Server Hostname
* HTTP Path

We can use any cluster in your project to connect to your data, but we recommend using a databricks [SQL warehouse/endpoint](https://docs.databricks.com/sql/admin/sql-endpoints.html) so that the cluster does not need to spin up for every pull.

### API Key

You can generate a new API key by going to "User Settings" in your Databricks console. There, you should be able to generate a new token as shown below.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/databricks/188731186-ecdc0872-de06-4576-b387-fa08bdca447d.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=78ab18d4cc7aba283123a58f5a2e624c" alt="databricks info" width="1033" height="733" data-path="images/statsig-warehouse-native/connecting-your-warehouse/databricks/188731186-ecdc0872-de06-4576-b387-fa08bdca447d.png" />
</Frame>

You can also use a personal access token for a service principal. Generate one by following the steps in the doc [here](https://docs.databricks.com/en/administration-guide/users-groups/service-principals.html#manage-personal-access-tokens-for-a-service-principal).

### Server Hostname & HTTP Path

You can find your Server Hostname and HTTP Path in your Databricks console by going to your specific cluster, navigating to the "Configuration" tab and expanding the "Advanced options."

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/databricks/242474157-e6329ea8-92ae-43af-95dc-7bce2a26a3e6.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=36a625648af66bd820636543696eeca2" alt="credentials" width="1378" height="1296" data-path="images/statsig-warehouse-native/connecting-your-warehouse/databricks/242474157-e6329ea8-92ae-43af-95dc-7bce2a26a3e6.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).