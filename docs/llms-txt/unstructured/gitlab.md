# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/gitlab.md

# GitLab

Connect GitLab to your preprocessing pipeline, and use the Unstructured CLI or Python to batch process all your documents and store structured outputs locally on your filesystem.

The requirements are as follows.

* A [GitLab account](https://gitlab.com/users/sign_up).
* The URL for the target [GitLab repository](https://docs.gitlab.com/ee/user/project/repository/).
* A [GitLab access token](https://docs.gitlab.com/ee/security/tokens/) that allows access to the repository.
* Optionally, the name of a specific branch to access in the repository. The repository's default repository branch is used if not otherwise specified.
* Optionally, a list of file globs to limit which types of files are accepted, for example `*.html` or `*.txt`.

The GitLab connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[gitlab]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `GITLAB_REPO_URL` - The URL for the target GitLab repository, represented by `--url` (CLI) or `url` (Python).
* `GITLAB_TOKEN` - The GitLab access token that allows access to the repository, represented by `--git-access-token` (CLI) or `access_token` (Python).

Now call the Unstructured CLI or Python. The destination connector can be any of the ones supported. This example uses the local destination connector.

This example sends data to Unstructured for processing by default. To process data locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  unstructured-ingest \
    gitlab \
    --url $GITLAB_URL \
    --git-access-token $GITLAB_TOKEN \
    --git-branch v0.0.7 \
    --git-file-glob "*.html,*.txt" \
    --output-dir $LOCAL_FILE_OUTPUT_DIR \
    --partition-by-api \
    --api-key $UNSTRUCTURED_API_KEY \
    --partition-endpoint $UNSTRUCTURED_API_URL \
    --strategy hi_res \
    --chunking-strategy by_title \
    --embedding-provider huggingface \
    --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}"
  ```

  ```python Python Ingest theme={null}
  # pip install "unstructured-ingest[gitlab]"

  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.gitlab import (
      GitLabIndexerConfig,
      GitLabDownloaderConfig,
      GitLabConnectionConfig,
      GitLabAccessConfig
  )

  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig
  from unstructured_ingest.processes.connectors.local import LocalUploaderConfig

  # Chunking and embedding are optional.

  if __name__ == "__main__":
      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=GitLabIndexerConfig(
              path="/",
              recursive=True,
              git_branch="v0.0.7"
          ),
          downloader_config=GitLabDownloaderConfig(download_dir=os.getenv("LOCAL_FILE_DOWNLOAD_DIR")),
          source_connection_config=GitLabConnectionConfig(
              access_config=GitLabAccessConfig(access_token=os.getenv("GITLAB_TOKEN")),
              url=os.getenv("GITLAB_URL")
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

* To send files to the [Unstructured Partition Endpoint](/api-reference/partition/overview) for processing, specify `--partition-by-api` (CLI) or `partition_by_api=True` (Python).

  Unstructured also requires an Unstructured API key and API URL, by adding the following:

  * `--api-key $UNSTRUCTURED_API_KEY` (CLI) or `api_key=os.getenv("UNSTRUCTURED_API_KEY")` (Python)
  * `--partition-endpoint $UNSTRUCTURED_API_URL` (CLI) or `partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")` (Python)
  * The environment variables `UNSTRUCTURED_API_KEY` and `UNSTRUCTURED_API_URL`, representing your API key and API URL, respectively.

  <Note>
    You must specify the API URL only if you are not using the default API URL for Unstructured Ingest, which applies to **Let's Go**, **Pay-As-You-Go**, and **Business SaaS** accounts.

    The default API URL for Unstructured Ingest is `https://api.unstructuredapp.io/general/v0/general`, which is the API URL for the [Unstructured Partition Endpoint](/api-reference/partition/overview). However, you should always use the URL that was provided to you when your Unstructured account was created. If you do not have this URL, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

    If you do not have an API key, [get one now](/api-reference/partition/overview).

    If you are using a **Business** account, the process
    for generating Unstructured API keys, and the Unstructured API URL that you use, are different.
    For instructions, see your Unstructured account administrator, or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
  </Note>
