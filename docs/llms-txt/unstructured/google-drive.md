# Source: https://docs.unstructured.io/ui/sources/google-drive.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/google-drive.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/google-drive.md

# Source: https://docs.unstructured.io/ui/sources/google-drive.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/google-drive.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/google-drive.md

# Source: https://docs.unstructured.io/ui/sources/google-drive.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/google-drive.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/google-drive.md

# Google Drive

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a source connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key, as follows:

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the source connector, add it along with a
  [destination connector](/api-reference/workflow/destinations/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  [hands-on Workflow Endpoint quickstart](/api-reference/workflow/overview#quickstart),
  go directly to the [quickstart notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_Platform_Workflow_Endpoint_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create source connectors with the Unstructured user interface (UI).
  [Learn how](/ui/sources/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a source connector! Keep reading to learn how.
</Note>

Ingest your files into Unstructured from Google Drive.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZiRD7hC-wh8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A [Google Cloud account](https://console.cloud.google.com).

* The **Google Drive API** enabled in the account.
  [Learn how](https://cloud.google.com/apis/docs/getting-started#enabling_apis).

* Within the account, a Google Cloud service account and its related `credentials.json` key file or its contents in JSON format.
  [Create a service account](https://developers.google.com/workspace/guides/create-credentials#create_a_service_account).
  [Create credentials for a service account](https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account).

  To ensure maximum compatibility across Unstructured service offerings, you should give the service account key information to Unstructured as
  a single-line string that contains the contents of the downloaded service account key file (and not the service account key file itself).
  To print this single-line string without line breaks, suitable for copying, you can run one of the following commands from your Terminal or Command Prompt.
  In this command, replace `<path-to-downloaded-key-file>` with the path to the `credentials.json` key file that you downloaded by following the preceding instructions.

  * For macOS or Linux:

    ```text  theme={null}
    tr -d '\n' < <path-to-downloaded-key-file>
    ```

  * For Windows:

    ```text  theme={null}
    (Get-Content -Path "<path-to-downloaded-key-file>" -Raw).Replace("`r`n", "").Replace("`n", "")
    ```

* A Google Drive [shared folder](https://support.google.com/drive/answer/2375091) or [shared drive](https://support.google.com/a/users/answer/7212025).

* Give the service account access to the shared folder or shared drive. To do this, share the folder or drive with the service account's email address.
  [Learn how](https://support.google.com/drive/answer/7166529).
  [Learn more](https://www.googlecloudcommunity.com/gc/Workspace-Q-A/Can-i-give-access-to-document-of-google-drive-to-service-account/m-p/530106).

* Get the shared folder's ID or shared drive's ID. This is a part of the URL for your Google Drive shared folder or shared drive, represented in the following URL as `{folder_id}`: `https://drive.google.com/drive/folders/{folder-id}`.

## Document permissions metadata

The source connector outputs any permissions information that it can find in the source location about the processed source documents and associates that information with each
corresponding element that is generated. This permissions information is output into the `permissions_data` field, which is within the
`data_source` field under the element's `metadata` field. This information lists the users or groups, if any, that have
permissions to read, update, or delete the element's associated source document.

The following example shows what the output looks like. Ellipses indicate content that has been omitted from this example for brevity.

```json  theme={null}
[
    {
        "...": "...",
        "metadata": {
            "...": "...",
            "data_source": {
                "...": "...",
                "permissions_data": [
                    {
                        "read": {
                            "users": [
                                "11111111111111111111"
                            ],
                            "groups": [
                                "22222222222222222222",
                                "33333333333333333333"
                            ]
                        }
                    },
                    {
                        "update": {
                            "users": [
                                "44444444444444444444",
                                "55555555555555555555"
                            ],
                            "groups": [
                                "66666666666666666666",
                            ]
                        }
                    },
                    {
                        "delete": {
                            "users": [
                                "77777777777777777777"
                            ],
                            "groups": [
                                "88888888888888888888"
                            ]
                        }
                    }
                ],
                "...": "..."
            }
        }
    }
]
```

To look up information about a particular Google Cloud user, use the user's ID along with the
[Admin SDK API](https://developers.google.com/workspace/admin/directory/reference/rest/v1/users/get) or the
[People API](https://developers.google.com/people/api/rest/v1/people/get) for Google Cloud.

To look up information about a particular Google Cloud group, use the group's ID along with the
[Admin SDK API](https://developers.google.com/workspace/admin/directory/reference/rest/v1/groups/get) or the
[Cloud Identity API](https://cloud.google.com/identity/docs/reference/rest/v1/groups/get) for Google Cloud.

To create a Google Drive source connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateSourceRequest
  from unstructured_client.models.shared import CreateSourceConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.sources.create_source(
          request=CreateSourceRequest(
              create_source_connector=CreateSourceConnector(
                  name="<name>",
                  type="google_drive",
                  config={
                      "drive_id": "<drive-id>",
                      "service_account_key": "<service-account-key>",
                      "extensions": [
                          "<extension>",
                          "<extension>"
                      ],
                      "recursive": <True|False>
                  }
              )
          )
      )

      print(response.source_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/sources" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "google_drive",
      "config": {
          "drive_id": "<drive-id>",
          "service_account_key": "<service-account-key>",
          "extensions": [
              "<extension>",
              "<extension>"
          ],
          "recursive": <true|false>
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.

* `<drive-id>` - The ID for the target Google Drive folder or drive.

* `<service-account-key>` - The contents of the `credentials.json` key file as a single-line string.

* For `extensions`, set one or more `<extension>` values (such as `pdf` or `docx`) to process files with only those extensions. The default is to include all extensions.

  <Note>
    Do not include the leading dot in the file extensions. For example, use `pdf` or `docx` instead of `.pdf` or `.docx`.
  </Note>

* Set `recursive` to `true` to recursively process data from subfolders within the target folder or drive. The default is `false` if not otherwise specified.
