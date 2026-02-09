# Source: https://docs.unstructured.io/ui/sources/google-cloud.md

# Source: https://docs.unstructured.io/ui/destinations/google-cloud.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/google-cloud.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/google-cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Cloud Storage

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a destination connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key.

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the destination connector, add it along with a
  [source connector](/api-reference/workflow/sources/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  the notebook [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create destination connectors with the Unstructured user interface (UI).
  [Learn how](/ui/destinations/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a destination connector! Keep reading to learn how.
</Note>

Send processed data from Unstructured to Google Cloud Storage.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R57duYCxLi8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A Google Cloud service account. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create#console).

* A service account key for the service account. See [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating) in
  [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete).

  To ensure maximum compatibility across Unstructured service offerings, you should give the service account key information to Unstructured as
  a single-line string that contains the contents of the downloaded service account key file (and not the service account key file itself).
  To print this single-line string without line breaks, suitable for copying, you can run one of the following commands from your Terminal or Command Prompt.
  In this command, replace `<path-to-downloaded-key-file>` with the path to the service account key file that you downloaded by following the preceding instructions.

  * For macOS or Linux:
    ```text  theme={null}
    tr -d '\n' < <path-to-downloaded-key-file>
    ```
  * For Windows:
    ```text  theme={null}
    (Get-Content -Path "<path-to-downloaded-key-file>" -Raw).Replace("`r`n", "").Replace("`n", "")
    ```

* The URI for a Google Cloud Storage bucket. This URI consists of the target bucket name, plus any target folder within the bucket, expressed as `gs://<bucket-name>[/folder-name]`. [Create a bucket](https://cloud.google.com/storage/docs/creating-buckets#console).

  This bucket must have, at minimum, one of the following roles applied to the target Google Cloud service account:

  * `Storage Object Viewer` for bucket read access.
  * `Storage Object User` for bucket write access.
  * The `Storage Object Admin` role provides read and write access, plus access to additional bucket operations.

  To apply one of these roles to a service account for a bucket, see [Add a principal to a bucket-level policy](https://cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add)
  in [Set and manage IAM policies on buckets](https://cloud.google.com/storage/docs/access-control/using-iam-permissions).

To create a Google Cloud Storage destination connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateDestinationRequest
  from unstructured_client.models.shared import CreateDestinationConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.destinations.create_destination(
          request=CreateDestinationRequest(
              create_destination_connector=CreateDestinationConnector(
                  name="<name>",
                  type="gcs",
                  config={
                      "remote_url": "<remote-url>",
                      "service_account_key": "<service-account-key>"
                  }
              )
          )
      )

      print(response.destination_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/destinations" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "type": "gcs",
      "name": "<name>",
      "config": {
          "remote_url": "<remote-url>",
          "service_account_key": "<service-account-key>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<service-account-key>` (*required*) - The contents of a service account key file, expressed as a single string without line breaks, for a Google Cloud service account that has the required access permissions to the bucket.
* `<remote-url>` (*required*) - The URI for the Google Cloud Storage bucket and any target folder path within the bucket. This URI takes the format `gs://<bucket-name>[/folder-name]`.
* For `recursive` (source connector only), set to `true` to ingest data recursively from any subfolders, starting from the path specified by `<remote-url>`. The default is `false` if not otherwise specified.
