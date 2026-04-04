# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/one-drive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# OneDrive

Connect OneDrive to your preprocessing pipeline, and use the Unstructured Ingest CLI or the Unstructured Ingest Python library to batch process all your documents and store structured outputs locally on your filesystem.

The requirements are as follows.

* A OneDrive for business plan, or a Microsoft 365 or Office 365 Business or enterprise plan that includes OneDrive.
  [Learn more](https://www.microsoft.com/microsoft-365/onedrive/compare-onedrive-plans).
  [Shop for business plans](https://www.microsoft.com/microsoft-365/business/compare-all-microsoft-365-business-products).
  [Shop for enterprise plans](https://www.microsoft.com/microsoft-365/enterprise/microsoft365-plans-and-pricing).
  OneDrive personal accounts, and Microsoft 365 Free, Basic, Personal, and Family plans are not supported.

* A SharePoint Online plan, or a Microsoft 365 or Office 365 Business or enterprise plan that includes SharePoint Online.
  (Even if you only plan to use OneDrive, you still need a plan that includes SharePoint Online, because OneDrive is built on SharePoint technology.)
  [Learn more](https://www.microsoft.com/en-us/microsoft-365/SharePoint/compare-SharePoint-plans).
  [Shop for business plans](https://www.microsoft.com/microsoft-365/business/compare-all-microsoft-365-business-products).
  [Shop for enterprise plans](https://www.microsoft.com/microsoft-365/enterprise/microsoft365-plans-and-pricing).

* The OneDrive and SharePoint Online plans must share the same Microsoft Entra ID tenant.
  [Learn more](https://learn.microsoft.com/microsoft-365/enterprise/subscriptions-licenses-accounts-and-tenants-for-microsoft-cloud-offerings?view=o365-worldwide).

* The path to the target OneDrive folder, starting from the OneDrive account's root folder, for example `my-folder/my-subfolder`.

  The following video shows how to get a path:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/SfUA1IwtI5U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* Two types of authentication are supported: client credentials, and a username and password. Both authentication types require a Microsoft Entra ID app registration.

  <Note>
    The OneDrive connector does not support any other authentication methods, such as multifactor (MFA) or passwordless authentication.
  </Note>

  You will need to provide the **Application (client) ID**, **Directory (tenant) ID**, and **Client secret** for the Entra ID app registration that has access to the target OneDrive account, and
  the app registration must have the correct set of Microsoft Graph access permissions. These permissions include:

  * `Files.ReadWrite.All` (if both reading and writing are needed)

  * `Sites.ReadWrite.All` (if both reading and writing are needed)

  * `User.Read.All`

  * `Directory.Read.All`

  1. [Create an Entra ID app registration](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app?pivots=portal).
  2. [Add Graph access permissions to an app registration](https://learn.microsoft.com/entra/identity-platform/howto-update-permissions?pivots=portal#add-permissions-to-an-application).
  3. [Grant consent for the added Graph permissions](https://learn.microsoft.com/entra/identity-platform/howto-update-permissions?pivots=portal#grant-consent-for-the-added-permissions-for-the-enterprise-application).

  The following video shows how to create an Entra ID app registration:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/aBAY-LKLPSo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  The following video shows how to add the correct set of Graph access permissions to the Entra ID app registration:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/jBJsrSkpClo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* Both authentication types also require the User Principal Name (UPN) for the OneDrive account. This is typically the OneDrive account user's email address. To find a UPN:

  1. Depending on your plan, sign in to your Microsoft 365 admin center (typically [https://admin.microsoft.com](https://admin.microsoft.com)) using your administrator credentials,
     or sign in to your Office 365 portal (typically [https://portal.office.com](https://portal.office.com)) using your credentials.
  2. In the **Users** section, click **Active users**.
  3. Locate the user account in the list of active users.
  4. The UPN is displayed in the **Username** column.

  The following video shows how to get a UPN:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/H0yYfhfyCE0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For username and password authentication, you will also need the password for the target UPN.

The OneDrive connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[onedrive]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `ONEDRIVE_PATH` - The path to the target folder in the OneDrive account, starting with the account's root folder (for example `my-folder/my-subfolder`), represented by `--path` (CLI) or `path` (Python).
* `ONEDRIVE_CLIENT_ID` - The application (client) ID of the Microsoft Entra ID app registration that has access to the OneDrive account, represented by `--client-id` (CLI) or `client_id` (Python).
* `ONEDRIVE_CLIENT_CRED` - The client secret for the Entra ID app registration, represented by `--client-cred` (CLI) or `client_cred` (Python).
* `ONEDRIVE_TENANT` - The directory (tenant) ID of the Entra ID app registration, represented by `--tenant` (CLI) or `tenant` (Python).
* `ONEDRIVE_USER_PNAME` - The User Principal Name (UPN) for the OneDrive user account in Entra ID (typically the user's email address), represented by `--user-pname` (CLI) or `user_pname` (Python).
* `ONEDRIVE_USER_PASSWORD` - The password for the target UPN, represented by `--password` (CLI) or `password` (Python).
* `ONEDRIVE_AUTHORITY_URL` - The authentication token provider URL for the Entra ID app registration (the default is `https://login.microsoftonline.com` if not otherwise specified), represented by `--authority-url` (CLI) or `authority_url` (Python).

Now call the Unstructured Ingest CLI or the Unstructured Ingest Python library. The destination connector can be any of the ones supported. This example uses the local destination connector:

This example sends data to Unstructured for processing by default. To process data locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  unstructured-ingest \
    onedrive \
      --client-id $ONEDRIVE_CLIENT_ID \
      --client-cred $ONEDRIVE_CLIENT_CRED \
      --authority-url $ONEDRIVE_AUTHORITY_URL \
      --tenant $ONEDRIVE_TENANT \
      --user-pname $ONEDRIVE_USER_PNAME \
      --password $ONEDRIVE_USER_PASSWORD \ # For username and password authentication.
      --path $ONEDRIVE_PATH \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --num-processes 2 \
      --verbose \
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

  from unstructured_ingest.processes.connectors.onedrive import (
      OnedriveIndexerConfig,
      OnedriveDownloaderConfig,
      OnedriveConnectionConfig,
      OnedriveAccessConfig
  )

  from unstructured_ingest.processes.connectors.local import LocalConnectionConfig
  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig

  # Chunking and embedding are optional.

  if __name__ == "__main__":
      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=OnedriveIndexerConfig(path=os.getenv("ONEDRIVE_PATH")),
          downloader_config=OnedriveDownloaderConfig(
              download_dir=os.getenv("LOCAL_FILE_DOWNLOAD_DIR")
          ),
          source_connection_config=OnedriveConnectionConfig(
              access_config=OnedriveAccessConfig(
                  client_cred=os.getenv("ONEDRIVE_CLIENT_CRED"),
                  password=os.getenv("ONEDRIVE_USER_PASSWORD") # For username and password authentication.
              ),
              client_id=os.getenv("ONEDRIVE_CLIENT_ID"),
              tenant=os.getenv("ONEDRIVE_TENANT"),
              user_pname=os.getenv("ONEDRIVE_USER_PNAME"),
              authority_url=os.getenv("ONEDRIVE_AUTHORITY_URL")
          ),
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
          destination_connection_config=LocalConnectionConfig()
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
