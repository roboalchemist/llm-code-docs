# Source: https://docs.unstructured.io/ui/sources/confluence.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/confluence.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/confluence.md

# Source: https://docs.unstructured.io/ui/sources/confluence.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/confluence.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/confluence.md

# Source: https://docs.unstructured.io/ui/sources/confluence.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/confluence.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/confluence.md

# Confluence

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

Ingest your files into Unstructured from Confluence.

The requirements are as follows.

* A [Confluence Cloud account](https://www.atlassian.com/software/confluence/pricing) or
  [Confluence Data Center installation](https://confluence.atlassian.com/doc/installing-confluence-data-center-203603.html).

* The site URL for your [Confluence Cloud account](https://community.atlassian.com/t5/Confluence-questions/confluence-cloud-url/qaq-p/1157148) or
  [Confluence Data Center installation](https://confluence.atlassian.com/confkb/how-to-find-your-site-url-to-set-up-the-confluence-data-center-and-server-mobile-app-938025792.html).

* A user in your [Confluence Cloud account](https://confluence.atlassian.com/cloud/invite-edit-and-remove-users-744721624.html) or
  [Confluence Data Center installation](https://confluence.atlassian.com/doc/add-and-invite-users-138313.html).

* The user must have the correct permissions in your
  [Conflunce Cloud account](https://support.atlassian.com/confluence-cloud/docs/what-are-confluence-cloud-permissions-and-restrictions/) or
  [Confluence Data Center installation](https://confluence.atlassian.com/doc/permissions-and-restrictions-139557.html) to
  access the target spaces and pages.

* One of the following:

  * For Confluence Cloud or Confluence Data Center, the target user's name or email address, and password.
    [Change a Confluence Cloud user's password](https://support.atlassian.com/confluence-cloud/docs/change-your-confluence-password/).
    [Change a Confluence Data Center user's password](https://confluence.atlassian.com/doc/change-your-password-139416.html).
  * For Confluence Cloud only, the target user's name or email address, and API token.
    [Create an API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).
  * For Confluence Data Center only, the target user's personal access token (PAT).
    [Create a PAT](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html).

* Optionally, the keys (not display names) of the specific [spaces](https://support.atlassian.com/confluence-cloud/docs/navigate-spaces/) in the Confluence instance to access. To get a space's key,
  which is different from a space's display name, open the space in your web browser and look at the URL. The space's key is the part of the URL after `spaces/` but before the next `/` after that.

The following video provides related setup information for Confluence Cloud:

<iframe width="560" height="315" src="https://www.youtube.com/embed/3PsFJkcIotI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

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
                                "11111:11111111-1111-1111-1111-111111111111"
                            ],
                            "groups": [
                                "22222222-2222-2222-2222-22222222",
                                "33333333-3333-3333-3333-33333333"
                            ]
                        }
                    },
                    {
                        "update": {
                            "users": [
                                "44444:44444444-4444-4444-4444-44444444",
                                "55555:55555555-5555-5555-5555-55555555"
                            ],
                            "groups": [
                                "66666666-6666-6666-6666-66666666",
                            ]
                        }
                    },
                    {
                        "delete": {
                            "users": [
                                "77777:77777777-7777-7777-7777-77777777"
                            ],
                            "groups": [
                                "88888888-8888-8888-8888-88888888"
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

To look up information about a particular Confluence user, use the user's ID (also known as their *account ID*) from the preceding output to call the
[GET /wiki/rest/api/user](https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-get)
operation in the Confluence REST API.

To look up information about a particular Confluence group, use the group's ID from the preceding output to call the
[GET /wiki/rest/api/group/by-id](https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-by-id-get)
operation in the Confluence REST API.

To create a Confluence source connector, see the following examples.

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
                  type="confluence",
                  config={
                      "url": "<url>",
                      "max_num_of_spaces": <max-num-of-spaces>,
                      "max_num_of_docs_from_each_space": <max-num-of-docs-from-each-space>,
                      "spaces": ["<space-key>", "<space-key>"],
                      "extract_images": <True|False>,
                      "extract_files": <True|False>,

                      # For API token authentication:
                      # "username": "<username>",
                      # "token": "<api-token>",
                      # "cloud": <True|False>,

                      # For personal access token (PAT) authentication:
                      # "token": "<personal-access-token>",
                      # "cloud": False,

                      # For password authentication:
                      # "username": "<username>",
                      # "password": "<password>",
                      # "cloud": <True|False>
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
      "type": "confluence",
      "config": {
          "url": "<url>",
          "max_num_of_spaces": <max-num-of-spaces>,
          "max_num_of_docs_from_each_space": <max-num-of-docs-from-each-space>,
          "spaces": ["<space-key>", "<space-key>"],
          "extract_images": "<true|false>",
          "extract_files": "<true|false>",

          # For API token authentication:

          "username": "<username>",
          "token": "<api-token>",
          "cloud": "<true|false>"

          # For personal access token (PAT) authentication:

          "token": "<personal-access-token>",
          "cloud": "false"

          # For password authentication:

          "username": "<username>",
          "password": "<password>",
          "cloud": "<true|false>"        
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<url>` (*required*) - The URL to the target Confluence Cloud instance.
* `<max-num-of-spaces>` - The maximum number of Confluence spaces to access within the Confluence Cloud instance. The default is `500` unless otherwise specified.
* `<max-num-of-docs-from-each-space>` - The maximum number of documents to access within each space. The default is `150` unless otherwise specified.
* `spaces` is an array of strings, with each `<space-key>` specifying the key (not display name) of a space to access, for example: `["luke","paul"]`. By default, if no space keys are specified, and the `<max-num-of-spaces>` is exceeded for the instance, be aware that you might get unexpected results.
* `extract_images` - Set to `true` to download images and replace the HTML content with Base64-encoded images. The default is `false` if not otherwise specified.
* `extract_files` - Set to `true` to download any embedded files in pages. The default is `false` if not otherwise specified.

For username and API token authentication:

* `<username>` - The name or email address of the target user.
* `<api-token>` - The user's API token value.
* For `cloud`, `true` if you are using Confluence Cloud. The default is `false` if not otherwise specified.

For personal access token (PAT) authentication:

* `<personal-access-token>` - The target user's PAT value.
* `cloud` should always be `false`.

For username and password authentication:

* `<username>` - The name or email address of the target user.
* `<password>` - The user's password.
* For `cloud`, `true` if you are using Confluence Cloud. The default is `false` if not otherwise specified.
