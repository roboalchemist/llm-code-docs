# Source: https://docs.unstructured.io/ui/sources/jira.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/jira.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/jira.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Jira

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

Ingest your files into Unstructured from Jira.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JR5mcukOSUQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A [Jira Cloud account](https://www.atlassian.com/try/cloud/signup?bundle=jira-software\&edition=free) or
  [Jira Data Center installation](https://confluence.atlassian.com/adminjiraserver/installing-jira-data-center-938846870.html).
* The site URL for your [Jira Data Center installation](https://confluence.atlassian.com/jirakb/find-your-site-url-to-set-up-the-jira-data-center-and-server-mobile-app-954244798.html) or Jira Cloud account.
  For Jira Cloud, open Jira in your web browser and copy the address from the browser's address bar.
  If you're unsure, check the dashboard URL, or if viewing an issue, project or board, the site URL is typically everything that comes before **but not including** `/jira`, such as
  `https://<organization>.atlassian.net`.
* To process Jira projects, provide the IDs for the target projects. To get a project's ID, sign in to your Jira Cloud account or Jira Data Center installation, and then go to the following URL: `https://<organization>.atlassian.net/rest/api/latest/project/<project-key>`,
  replacing `<organization>` with yours, and replacing `<project-key>` with the target project's key. In the
  response, look for the URL `https://<organization>.atlassian.net/rest/api/3/project/<project-id>`, where `<project-id>` is the target project's ID.
* To process Jira boards, the IDs for the target boards. To get a board's ID, sign in to your Jira Cloud account or Jira Data Center installation, and then go to the following URL: `https://<organization>.atlassian.net/rest/agile/1.0/board?projectKeyOrId=<project-key-or-id>`,
  replacing `<organization>` with yours, and `<project-key-or-id>` with the associated project's key or ID. In the
  response, look for the URL `https://<organization>.atlassian.net/rest/agile/1.0/board/<board-id>`, where `<board-id>` is the board's ID.
* To process Jira issues, the IDs for the target issues. To get an issue's ID, sign in to your Jia Cloud account or Jira Data Center installation, open the issue, and then look at the URL in your browser's address bar. The issue ID is the string of characters after the final slash in the URL.
* A user in your [Jira Cloud account](https://support.atlassian.com/jira-cloud-administration/docs/manage-users-groups-permissions-and-roles-in-jira-cloud/) or
  [Jira Data Center installation](https://confluence.atlassian.com/adminjiraserver/create-edit-or-remove-a-user-938847025.html).
* The user must have the correct permissions in your
  [Jira Cloud account](https://support.atlassian.com/jira-cloud-administration/docs/manage-users-groups-permissions-and-roles-in-jira-cloud/) or
  [Jira Data Center installation](https://confluence.atlassian.com/jirakb/permissions-made-simple-for-jira-server-717062767.html) to
  access the target projects, boards, and issues.
* One of the following:

  * For Jira Cloud or Jira Data Center, the target user's name or email address, and password.
    [Change a Jira Cloud user's password](https://support.atlassian.com/user-management/docs/change-password-for-portal-only-customers/).
    [Change a Jira Data Center user's password](https://confluence.atlassian.com/adminjiraserver/create-edit-or-remove-a-user-938847025.html).
  * For Jira Cloud only, the target user's name or email address, and API token.
    [Create an API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).
  * For Jira Data Center only, the target user's personal access token (PAT).
    [Create a PAT](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html).

To create a Jira source connector, see the following examples.

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
                  type="jira",
                  config={
                      "url": "<url>",

                      # For password or API token authentication:
                      # "username": "<username>",
                      # "password": "<password>",

                      # For personal access token authentication:
                      # "token": "<token>",

                      "projects": [
                          "<project-id>",
                          "<project-id>"
                      ],
                      "boards": [
                          "<board-id>",
                          "<board-id>"
                      ],
                      "issues": [
                          "<issue-id>",
                          "<issue-id>"
                      ],
                      "status_filters": [
                          "<status>",
                          "<status>"
                      ],
                      "download_attachments": <True|False>,
                      "cloud": <True|False>
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
      "type": "jira",
      "config": {
          "url": "<url>",

          # For password or API token authentication:
          "username": "<username>",
          "password": "<password">,

          # For personal access token authentication:
          "token": "<token>",
          
          "projects": [ 
              "<project-id>",
              "<project-id>"
          ],
          "boards": [ 
              "<board-id>",
              "<board-id>"
          ],
          "issues": [ 
              "<issue-id>",
              "<issue-id>"
          ],
          "status_filters": [
              "<status>",
              "<status>"
          ],
          "download_attachments": <true|false>,
          "cloud": <true|false>
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*): A unique name for this connector.
* `<url>` (*required*): The URL of the Jira instance.
* `<username>` (*required* for password or API token authentication): The username of the Jira user.
* `<password>` (*required* for password or API token authentication): For password authentication, the password of the Jira user.
  For API token authentication, the API token of the Jira user.
* `<token>` (*required* for personal access token authentication): The personal access token of the Jira user.
* `<project-id>`: The ID of a target project in Jira to access.
* `<board-id>`: The ID of a target board in Jira to access.
* `<issue-id>`: The ID of a target issue in Jira to access.
* `<status>`: The name of a status to filter Jira issues by.
* Set `download_attachments` to `true` to download attachments from Jira issues. The default is `false`.
* Set `cloud` to `true` to specify using Jira Cloud or `false` to specify using Jira Data Center. The default is to use Jira Data Center.

## Learn more

* <Icon icon="blog" />  [Jira Integration in Unstructured: Build RAG Systems with Project Management Data](https://unstructured.io/blog/jira-integration-in-unstructured-build-rag-systems-with-project-management-data)
