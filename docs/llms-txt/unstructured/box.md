# Source: https://docs.unstructured.io/ui/sources/box.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/box.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/box.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/box.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Box

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
  the notebook [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create source connectors with the Unstructured user interface (UI).
  [Learn how](/ui/sources/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a source connector! Keep reading to learn how.
</Note>

Ingest your files into Unstructured from Box.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Gkniu1sfz1o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

1. Access to the [Developer Console](https://app.box.com/developers/console) from your [Box enterprise account](https://account.box.com/signup/enterprise-plan) or [Box developer account](https://account.box.com/signup/developer).

2. A Box Custom App in your Box account, set up to use **Server Authentication (with JWT)**. See [Setup with JWT](https://developer.box.com/guides/authentication/jwt/jwt-setup/).

3. The appropriate application scopes and advanced features set up for the Box Custom App, as follows:

   * In the Box Custom App, on the **Configuration** tab, under **Application Scopes**, check the box titled **Write all files and folders stored in Box**.
   * In the Box Custom App, on the **Configuration** tab, under **Advanced Features**, check the box titled **Make API calls using the as-user header**.
   * Click **Save Changes** before continuing.

4. Authorization by a Box Admin in your Box account for the Box Custom App. See [App Authorization](https://developer.box.com/guides/authentication/jwt/jwt-setup/#app-authorization).

5. Access by your Box account's source or target [folder](https://app.box.com/folder/0) to your Box Custom App, as follows:

   * In the Box Custom App, on the **General Settings** tab, copy the **Service Account ID** (which takes the form `AutomationUser_<your-app-service-id>_<a-random-string@boxdevedition.com`).
   * **Share** your Box account's target folder with the copied service account's email address as a **Co-owner** or **Editor**.
   * Note the remote URL to the target folder, which takes the format `box://<path/to/folder/in/account>`.

6. The private key configuration JSON file for the Box Custom App, or a string that contains this file's contents.

   * To download this file, in the Box Custom App, on the **Configuration** tab, under **Add and Manage Public Keys**, click **Generate a Public/Private Keypair**. Store the downloaded private key configuration JSON file in a secure location.
   * To ensure maximum compatibility across Unstructured service offerings, you should give the private key configuration JSON file information to Unstructured as
     a single-line string that contains the contents of the downloaded private key configuration JSON file (and not the file itself).
     To print this single-line string, suitable for copying, you can run one of the following commands from your Terminal or Command Prompt.
     In this command, replace `<path-to-downloaded-key-file>` with the path to the private key configuration JSON file that you downloaded by following the preceding instructions.

     * For macOS or Linux:

       ```text  theme={null}
       tr -d '\n' < <path-to-downloaded-key-file>
       ```

     * For Windows:

       ```text  theme={null}
       (Get-Content -Path "<path-to-downloaded-key-file>" -Raw).Replace("`r`n", "").Replace("`n", "")
       ```

To create an Box source connector, see the following examples.

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
                  type="box",
                  config={
                      "remote_url": "<remote-url>",
                      "recursive": <True|False>,
                      "box_app_config": "<box-app-config>"
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
      "type": "box",
      "config": {
          "remote_url": "<remote-url>",
          "recursive": <true|false>,
          "box_app_config": "<box-app-config>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*): A unique name for this connector.
* `<remote-url>` (*required*): The URL to the target Box folder. This URL must take the format `box://<path/to/folder/in/account>`.
* For `recursive`, set to `true` to recursively access files from subfolders within the taget Box folder. The default is `false` if not otherwise specified.
* `<box-app-config>` (*required*): The contents of the private key configuration JSON file for the Box Custom App with access to the target Box folder. This file's contents must be provided as a single string.

## Learn more

* <Icon icon="blog" />  [Finding Needles in a Haystack: PII Detection at Scale with Unstructured, Box, and Elasticsearch](https://unstructured.io/blog/finding-needles-in-a-haystack-pii-detection-at-scale-with-unstructured-box-and-elasticsearch)
