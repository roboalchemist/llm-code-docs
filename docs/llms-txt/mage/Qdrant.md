# Source: https://docs.mage.ai/integrations/databases/Qdrant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Qdrant

## Credentials

Open the file named `io_config.yaml` at the root of your Mage project and enter qdrant required fields:

```yaml  theme={"system"}
version: 0.1.1
default:
  QDRANT_COLLECTION: collection_name
  QDRANT_PATH: path of the qdrant persisitant storage
```

## Dependencies

The dependency libraries are not installed in the docker image by default. You'll need to add the libraries to
project `requirements.txt` file manually and install them.

```
qdrant-client==1.6.9
sentence-transformers==2.2.2
```

## Using Python block

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader or data exporter using the Qdrant template under the "Databases" category.
   Both the data loader and exporter use SentenceTransformer 'all-MiniLM-L6-v2' as the default embedding function.
3. Add your customized code into the loader, exporter or add extra transformer blocks.
4. Run the block.

## Available functions

* Qdrant data loader arguments:
  * limit\_results (int): Number of results to return.
  * query\_vector (List): vector lit used for query.
  * collection\_name (str): name of the collection. Default to use the name defined in io\_config.yaml.

* Qdrant data exporter arguments:
  * df (DataFrame): Data to export.
  * document\_column (str): Column name containing documents to export.
  * id\_column (str): Column name of the id. Default will use index in df.
  * vector\_column (str): Column name of the vector. Will use default encoder to auto generate query vector.
  * collection\_name (str): name of the collection. Default to use the name defined in io\_config.yaml.
  * vector\_size (int): dimension size of vector.
  * distance (models.Distance): distance metric to use.

At the same time there is `create_collection` function can be used in your block to create new collection.


Built with [Mintlify](https://mintlify.com).