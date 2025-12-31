# Source: https://docs.unstructured.io/ui/sources/outlook.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/outlook.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/outlook.md

# Source: https://docs.unstructured.io/ui/sources/outlook.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/outlook.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/outlook.md

# Source: https://docs.unstructured.io/ui/sources/outlook.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/outlook.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/outlook.md

# Outlook

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

Ingest your files into Unstructured from Outlook.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9yESRp9pzv0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The Outlook user's email address.
* A Microsoft Entra ID app registration in the same Azure account as the Outlook account. You will need
  this app registration's application (client) ID, client secret, and directory (tenant) ID. [Learn how](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app).
* The Entra ID app registration must have the following Graph API permission levels of the application (not delegated) type:

  * `Mail.Read`
  * `Mail.ReadBasic`
  * `User.Read.All`

  [Learn how](https://learn.microsoft.com/entra/identity-platform/howto-update-permissions).

To create an Outlook source connector, see the following examples.

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
                  type="outlook",
                  config={
                      "client_id": "<client-id>",
                      "authority_url": "<authority-url>",
                      "tenant": "<tenant>",
                      "client_cred": "<client-cred>",
                      "user_email": "<user-email>",
                      "outlook_folders": ["<folder-name>", "<folder-name>"],
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
      "type": "outlook",
      "name": "<name>",
      "config": {
          "client_id": "<client-id>",
          "authority_url": "<authority-url>",
          "tenant": "<tenant>",
          "client_cred": "<client-cred>",
          "user_email": "<user-email>",
          "outlook_folders": ["<folder-name>","<folder-name>"],
          "recursive": <true|false>
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<client-id>` (*required*) - The application (client) ID of the Microsoft Entra ID app registration that has access to the Outlook account.
* `<authority-url>` - The authentication token provider URL for the Entra ID app registration. The default is `https://login.microsoftonline.com` if not otherwise specified.
* `<tenant>` (*required*) - The directory (tenant) ID of the Entra ID app registration.
* `<client-cred>` (*required*) - The client secret for the Entra ID app registration.
* `<user-email>` (*required*) - The user's email address for the target Outlook account.
* `outlook_folders` is a *required* array of strings, with each `<folder-name>` specifying the name of a folder to access, for example: `["Inbox","Sent"]`. Do not specify any subfolder names.
* For `recursive` (source connector only), set to `true` to access any and all subfolders within each of the specified top-level folders. The default is `false` if not otherwise specified.
