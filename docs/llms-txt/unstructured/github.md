# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/github.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub

Connect GitHub to your preprocessing pipeline, and use the Unstructured Ingest CLI or the Unstructured Ingest Python library to batch process all your documents and store structured outputs locally on your filesystem.

The requirements are as follows.

* The user or organization name, and the repository name, for the target GitHub repository, for example `Unstructured-IO/docs`.
* The name of a branch to access in the repository. By default, the repository's default branch is used.
* A GitHub [account](https://docs.github.com/get-started/start-your-journey/creating-an-account-on-github).
* A GitHub [personal access token](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for the account.
* If you are accessing a private GitHub repository, the repository must grant the appropriate access
  [permissions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
  to the GitHub account.

The GitHub connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[github]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `GITHUB_URL` - The user or organization name, and the repository name, for the target GitHub repository; for example `Unstructured-IO/docs`, represented by `--url` (CLI) or `url` (Python).
* `GITHUB_BRANCH` - The name of the target branch in the repository, for example `main`, represented by `--branch` (CLI) or `branch` (Python). By default, the repository's default branch is used.
* `GITHUB_ACCESS_TOKEN` - The value of your GitHub access token, represented by `--access-token` (CLI) or `access_token` (Python).

Now call the Unstructured Ingest CLI or the Unstructured Ingest Python library. The destination connector can be any of the ones supported. This example uses the local destination connector.

This example sends data to Unstructured for processing by default. To process data locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  unstructured-ingest \
    github \
      --access-token $GITHUB_ACCESS_TOKEN \
      --url $GITHUB_URL \
      --branch $GITHUB_BRANCH \
      --recursive \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --strategy hi_res \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}"
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.github import (
      GithubIndexerConfig,
      GithubDownloaderConfig,
      GithubConnectionConfig,
      GithubAccessConfig
  )

  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig

  from unstructured_ingest.processes.connectors.local import LocalUploaderConfig

  # Chunking and embedding are optional.

  if __name__ == "__main__":
      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=GithubIndexerConfig(
              branch=os.getenv("GITHUB_BRANCH"),
              recursive=True
          ),
          downloader_config=GithubDownloaderConfig(download_dir=os.getenv("LOCAL_FILE_DOWNLOAD_DIR")),
          source_connection_config=GithubConnectionConfig(
              access_config=GithubAccessConfig(access_token=os.getenv("GITHUB_ACCESS_TOKEN")),
              url=os.getenv("GITHUB_URL")
          ),
          partitioner_config=PartitionerConfig(
              partition_by_api=True,
              api_key=os.getenv("UNSTRUCTURED_API_KEY"),
              partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
              additional_partition_args={
                  "split_pdf_page": True,
                  "split_pdf_allow_failed": True,
                  "split_pdf_concurrency_level": 15
              }
          ),
          chunker_config=ChunkerConfig(chunking_strategy="by_title"),
          embedder_config=EmbedderConfig(embedding_provider="huggingface"),
          uploader_config=LocalUploaderConfig(output_dir=os.getenv("LOCAL_FILE_OUTPUT_DIR"))
      ).run()

  ```
</CodeGroup>

For the Unstructured Ingest CLI and the Unstructured Ingest Python library, you can use the `--partition-by-api` option (CLI) or `partition_by_api` (Python) parameter to specify where files are processed:

* To do local file processing, omit `--partition-by-api` (CLI) or `partition_by_api` (Python), or explicitly specify `partition_by_api=False` (Python).

  Local file processing does not use an Unstructured API key or API URL, so you can also omit the following, if they appear:

  * `--api-key $UNSTRUCTURED_API_KEY` (CLI) or `api_key=os.getenv("UNSTRUCTURED_API_KEY")` (Python)
  * `--partition-endpoint $UNSTRUCTURED_API_URL` (CLI) or `partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")` (Python)
  * The environment variables `UNSTRUCTURED_API_KEY` and `UNSTRUCTURED_API_URL`

* To send files to the legacy [Unstructured Partition Endpoint](/api-reference/legacy-api/partition/overview) for processing, specify `--partition-by-api` (CLI) or `partition_by_api=True` (Python).

  Unstructured also requires an Unstructured API key and API URL, by adding the following:

  * `--api-key $UNSTRUCTURED_API_KEY` (CLI) or `api_key=os.getenv("UNSTRUCTURED_API_KEY")` (Python)
  * `--partition-endpoint $UNSTRUCTURED_API_URL` (CLI) or `partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")` (Python)
  * The environment variables `UNSTRUCTURED_API_KEY` and `UNSTRUCTURED_API_URL`, representing your API key and API URL, respectively.

  <Note>
    You must specify the API URL only if you are not using the default API URL for Unstructured Ingest, which applies to **Let's Go**, **Pay-As-You-Go**, and **Business SaaS** accounts.

    The default API URL for Unstructured Ingest is `https://api.unstructuredapp.io/general/v0/general`, which is the API URL for the legacy[Unstructured Partition Endpoint](/api-reference/legacy-api/partition/overview). However, you should always use the URL that was provided to you when your Unstructured account was created. If you do not have this URL, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

    If you do not have an API key, [get one now](/api-reference/legacy-api/partition/overview).

    If you are using a **Business** account, the process
    for generating Unstructured API keys, and the Unstructured API URL that you use, are different.
    For instructions, see your Unstructured account administrator, or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
  </Note>
