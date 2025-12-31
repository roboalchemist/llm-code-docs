# Source: https://docs.lancedb.com/integrations/data/dlt.md

# dlt

export const PyPlatformsDltPipeline = "# Import necessary modules\nimport dlt\nfrom rest_api import rest_api_source\n\n# Configure the REST API source\nmovies_source = rest_api_source(\n    {\n        \"client\": {\n            \"base_url\": \"https://www.omdbapi.com/\",\n            \"auth\": {  # authentication strategy for the OMDb API\n                \"type\": \"api_key\",\n                \"name\": \"apikey\",\n                \"api_key\": dlt.secrets[\n                    \"sources.rest_api.api_token\"\n                ],  # read API credentials directly from secrets.toml\n                \"location\": \"query\",\n            },\n            \"paginator\": {  # pagination strategy for the OMDb API\n                \"type\": \"page_number\",\n                \"base_page\": 1,\n                \"total_path\": \"totalResults\",\n                \"maximum_page\": 5,\n            },\n        },\n        \"resources\": [  # list of API endpoints to request\n            {\n                \"name\": \"movie_search\",\n                \"endpoint\": {\n                    \"path\": \"/\",\n                    \"params\": {\n                        \"s\": \"godzilla\",\n                        \"type\": \"movie\",\n                    },\n                },\n            }\n        ],\n    }\n)\n\nif __name__ == \"__main__\":\n    # Create a pipeline object\n    pipeline = dlt.pipeline(\n        pipeline_name=\"movies_pipeline\",\n        destination=\"lancedb\",  # this tells dlt to load the data into LanceDB\n        dataset_name=\"movies_data_pipeline\",\n    )\n\n    # Run the pipeline\n    load_info = pipeline.run(movies_source)\n\n    # pretty print the information on data that was loaded\n    print(load_info)\n";

export const PyPlatformsDltAdapterUsage = "load_info = pipeline.run(\n    lancedb_adapter(\n        movies_source,\n        embed=\"Title\",\n    )\n)\n";

export const PyPlatformsDltAdapterImport = "from dlt.destinations.adapters import lancedb_adapter\n";

[dlt](https://dlthub.com/docs/intro) is an open-source library that you can add to your Python scripts to load data from various and often messy data sources into well-structured, live datasets. dlt's [integration with LanceDB](https://dlthub.com/docs/dlt-ecosystem/destinations/lancedb) lets you ingest data from any source (databases, APIs, CSVs, dataframes, JSONs, and more) into LanceDB with a few lines of simple python code. The integration enables automatic normalization of nested data, schema inference, incremental loading and embedding the data. dlt also has integrations with several other tools like dbt, airflow, dagster etc. that can be inserted into your LanceDB workflow.

## How to ingest data into LanceDB

In this example, we will be fetching movie information from the [Open Movie Database (OMDb) API](https://www.omdbapi.com/) and loading it into a local LanceDB instance. To implement it, you will need an API key for the OMDb API (which can be created freely [here](https://www.omdbapi.com/apikey.aspx)).

1. **Install `dlt` with LanceDB extras:**
   ```sh  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   pip install dlt[lancedb]
   ```

2. **Inside an empty directory, initialize a `dlt` project with:**

   ```sh  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   dlt init rest_api lancedb
   ```

   This will add all the files necessary to create a `dlt` pipeline that can ingest data from any REST API (ex: OMDb API) and load into LanceDB.

   ```text  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   ├── .dlt
   │   ├── config.toml
   │   └── secrets.toml
   ├── rest_api
   ├── rest_api_pipeline.py
   └── requirements.txt
   ```

   dlt has a list of pre-built [sources](https://dlthub.com/docs/dlt-ecosystem/verified-sources/) like [SQL databases](https://dlthub.com/docs/dlt-ecosystem/verified-sources/sql_database), [REST APIs](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api), [Google Sheets](https://dlthub.com/docs/dlt-ecosystem/verified-sources/google_sheets), [Notion](https://dlthub.com/docs/dlt-ecosystem/verified-sources/notion) etc., that can be used out-of-the-box by running `dlt init <source_name> lancedb`. Since dlt is a python library, it is also very easy to modify these pre-built sources or to write your own custom source from scratch.

3. **Specify necessary credentials and/or embedding model details:**

   In order to fetch data from the OMDb API, you will need to pass a valid API key into your pipeline. Depending on whether you're using LanceDB OSS or LanceDB cloud, you also may need to provide the necessary credentials to connect to the LanceDB instance. These can be pasted inside `.dlt/sercrets.toml`.

   dlt's LanceDB integration also allows you to automatically embed the data during ingestion. Depending on the embedding model chosen, you may need to paste the necessary credentials inside `.dlt/sercrets.toml`:

   ```toml  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   [sources.rest_api]
   api_key = "api_key" # Enter the API key for the OMDb API

   [destination.lancedb]
   embedding_model_provider = "sentence-transformers"
   embedding_model = "all-MiniLM-L6-v2"
   [destination.lancedb.credentials]
   uri = ".lancedb"
   api_key = "api_key" # API key to connect to LanceDB Cloud. Leave out if you are using LanceDB OSS.
   embedding_model_provider_api_key = "embedding_model_provider_api_key" # Not needed for providers that don't need authentication (ollama, sentence-transformers).
   ```

   See [here](https://dlthub.com/docs/dlt-ecosystem/destinations/lancedb#configure-the-destination) for more information and for a list of available models and model providers.

4. **Write the pipeline code inside `rest_api_pipeline.py`:**

   The following code shows how you can configure dlt's REST API source to connect to the [OMDb API](https://www.omdbapi.com/), fetch all movies with the word "godzilla" in the title, and load it into a LanceDB table. The REST API source allows you to pull data from any API with minimal code, to learn more read the [dlt docs](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api).

   <CodeBlock filename="Python" language="Python" icon="python">
     {PyPlatformsDltPipeline}
   </CodeBlock>

   The script above will ingest the data into LanceDB as it is, i.e. without creating any embeddings. If we want to embed one of the fields (for example, `"Title"` that contains the movie titles), then we will use dlt's `lancedb_adapter` and modify the script as follows:

   * Add the following import statement:
     <CodeBlock filename="Python" language="Python" icon="python">
       {PyPlatformsDltAdapterImport}
     </CodeBlock>
   * Modify the pipeline run like this:
     <CodeBlock filename="Python" language="Python" icon="python">
       {PyPlatformsDltAdapterUsage}
     </CodeBlock>

   This will use the embedding model specified inside `.dlt/secrets.toml` to embed the field `"Title"`.

5. **Install necessary dependencies:**

   ```sh  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   pip install -r requirements.txt
   ```

   Note: You may need to install the dependencies for your embedding models separately.

   ```sh  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   pip install sentence-transformers
   ```

6. **Run the pipeline:**
   Finally, running the following command will ingest the data into your LanceDB instance.
   ```sh  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   python custom_source.py
   ```

For more information and advanced usage of dlt's LanceDB integration, read [the dlt documentation](https://dlthub.com/docs/dlt-ecosystem/destinations/lancedb).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt