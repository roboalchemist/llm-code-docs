# Source: https://docs.mage.ai/guides/streaming/destinations/azure_data_lake.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Data Lake

## Basic config

```yaml  theme={"system"}
connector_type: azure_data_lake
table_uri: abfs://container@storagename.dfs.core.windows.net/
account_name: account_name
access_key: access_key
mode: append
file_type: delta
```

* `table_uri`: Azure Data Lake container location, or local path, where the Delta Table will be written.
* `account_name`: Azure Storage Account name
* `access_key`: Azure Storage Access key
* `mode`: write mode. 'append' or 'overwrite' are accepted. default is 'append'
* `file_type`: File type to insert in Azure Data Lake. Only 'delta' is supported.


Built with [Mintlify](https://mintlify.com).