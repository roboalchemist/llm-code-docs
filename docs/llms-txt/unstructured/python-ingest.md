# Source: https://docs.unstructured.io/open-source/ingestion/python-ingest.md

# Process files in batches by using the Unstructured Ingest Python library

The Unstructured Ingest Python library enables you to use Python code to send files in batches to Unstructured for processing, and to tell Unstructured where to deliver the processed data.

<Note>
  The Unstructured Ingest Python library does not work with the Unstructured API.

  For information about the Unstructured API, see the [Unstructured API Overview](/api-reference/workflow/overview).
</Note>

The following 3-minute video shows how to use the Unstructured Ingest Python library to send multiple PDFs from a local directory in batches to be ingested by Unstructured for processing:

<iframe width="560" height="315" src="https://www.youtube.com/embed/tSKHFXsBQ-c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

## Getting started

You can use the Unstructured Ingest Python library to process files locally, or you can use the Ingest Python library to send files in batches to Unstructured for processing.

Local processing does not use an Unstructured API key or API URL.

Using the Ingest Python library to send files in batches to Unstructured for processing is more robust, and usage is billed to you on a pay-as-you-go basis. Usage requires an Unstructured API key and API URL, as follows:

1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
   After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
   </Note>

2. If you have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
     or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
   </Note>

3. Get your Unstructured API key:<br />

   a. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

   <Note>
     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).
   </Note>

   b. Click **Generate API Key**.<br />
   c. Follow the on-screen instructions to finish generating the key.<br />
   d. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

3) The Unstructured API URL for Unstructured Ingest was provided to you when your Unstructured account was created.
   If you do not have this URL, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

<Note>
  The default URL for Unstructured Ingest is the same as the default URL for the Unstructured Partition Endpoint: `https://api.unstructuredapp.io/general/v0/general`.
  However, you should always use the URL that was provided to you when your Unstructured account was created.
</Note>

## Installation

One approach to get started quickly with the Unstructured Ingest Python library is to install Python and then run the following command:

```bash  theme={null}
pip install unstructured-ingest
```

This default installation option enables the ingestion of plain text files, HTML, XML, JSON and emails that do not require any extra dependencies. This default option also enables you to specify local source and destination locations.

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

For additional installation options, see the [Unstructured Ingest Python library](/open-source/ingestion/python-ingest) in the [Ingest](/open-source/ingestion/overview) section.

<Info>To migrate from older, deprecated versions of the Ingest Python library that used `pip install unstructured`, see the [migration guide](/open-source/ingestion/overview#migration-guide).</Info>

## Usage

For example, to use the Unstructured Ingest Python library to ingest files from a local source (input) location and to deliver the processed data to an Azure Storage account destination (output) location:

<CodeGroup>
  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.fsspec.azure import (
      AzureConnectionConfig,
      AzureAccessConfig,
      AzureUploaderConfig
  )
  from unstructured_ingest.processes.connectors.local import (
      LocalIndexerConfig,
      LocalDownloaderConfig,
      LocalConnectionConfig
  )
  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig

  # Chunking and embedding are optional.

  if __name__ == "__main__":
      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=LocalIndexerConfig(input_path=os.getenv("LOCAL_FILE_INPUT_DIR")),
          downloader_config=LocalDownloaderConfig(),
          source_connection_config=LocalConnectionConfig(),
          partitioner_config=PartitionerConfig(
              partition_by_api=True,
              api_key=os.getenv("UNSTRUCTURED_API_KEY"),
              partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
              strategy="hi_res",
              additional_partition_args={
                  "split_pdf_page": True,
                  "split_pdf_allow_failed": True,
                  "split_pdf_concurrency_level": 15
              }
          ),
          chunker_config=ChunkerConfig(chunking_strategy="by_title"),
          embedder_config=EmbedderConfig(embedding_provider="huggingface"),
          destination_connection_config=AzureConnectionConfig(
              access_config=AzureAccessConfig(
                  account_name=os.getenv("AZURE_STORAGE_ACCOUNT_NAME"),
                  account_key=os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
              )
          ),
          uploader_config=AzureUploaderConfig(remote_url=os.getenv("AZURE_STORAGE_REMOTE_URL"))
      ).run()
  ```
</CodeGroup>

To learn how to use the Unstructured Ingest Python library to work with a specific source (input) and destination (output) location, see the Python code examples for the [source](/open-source/ingestion/source-connectors/overview) and [destination](/open-source/ingestion/destination-connectors/overview) connectors that are available for you to choose from.

See also the [ingest configuration](/open-source/ingestion/ingest-configuration/overview) settings that enable you to further control how batches are sent and processed.

## Migration guide

The Unstructured Ingest Python library introduced breaking changes in version 0.7.0 as follows:

* The library has moved the calling pattern (formerly commonly referred to as "v2") up one level in the package. If you are using this calling pattern
  in your existing code, beginning with version 0.7.0 you must remove `.v2` from your related `from...import` statements. For example, if you previously had statments
  such as these:

  ```python  theme={null}
  from unstructured_ingest.v2.pipeline.pipeline import Pipeline
  from unstructured_ingest.v2.interfaces import ProcessorConfig
  ```

  Beginning with version 0.7.0, you must change to these by removing `.v2`:

  ```python  theme={null}
  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig
  ```

  If you do not make these changes beginning with version 0.7.0, your existing code will no longer work. To run your existing code
  without making these changes, you must pin your installed library version to 0.6.4 or earlier.

* The earlier calling pattern (commonly referred to as "v1") has been deprecated and removed from the library and will no longer work beginning with version 0.7.0. If you are using this earlier "v1" calling pattern in your code, you must
  either manually migrate your code to the new calling pattern (formerly commonly referred to as "v2"), or pin your installed library version to 0.6.4 or earlier to keep using this earlier "v1" calling pattern.

  To learn how to use the new calling pattern (formerly commonly referred to as "v2"), see the code examples in the
  [source connectors](/open-source/ingestion/source-connectors/overview) and [destination connectors](/open-source/ingestion/destination-connectors/overview) documentation.
