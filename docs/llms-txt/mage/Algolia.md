# Source: https://docs.mage.ai/integrations/databases/Algolia.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Algolia Integration in Mage

## Credentials Configuration

Open the file named `io_config.yaml` at the root of your Mage project and enter required fields:

```yaml  theme={"system"}
version: 0.1.1
default:
  ALGOLIA_APP_ID: app_id
  ALGOLIA_API_KEY: api_key
  ALGOLIA_INDEX_NAME: index_name
```

## Required Algolia Libraries

Add `algoliasearch==3.0.0` into `requirements.txt` to install the required weaviate library.

## Integration using Python Blocks

Follow these steps to integrate Algolia into your workflow using Python blocks:

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader or data exporter with Template. Under "Databases" category you can
   find the "Algolia" template.

* Data loader arguments:
  Args:
  query\_texts (str): Texts to query.
  index\_name (str): Name of the index. Defaults to the name defined in `io_config.yaml`.
  column\_names (List): columns to fetch.
  Returns:
  DataFrame: Data frame loaded.

* Data exporter arguments:
  Write  data into Algolia.

  Args:
  df (DataFrame): dataframes to write.
  index\_name (str): Name of the index. Defaults to the name defined in io\_config.yaml.

3. Add your customized code into the loader, exporter or add extra transformer blocks.
4. Run the block.


Built with [Mintlify](https://mintlify.com).