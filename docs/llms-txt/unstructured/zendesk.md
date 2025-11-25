# Source: https://docs.unstructured.io/ui/sources/zendesk.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/zendesk.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/zendesk.md

# Zendesk

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

Ingest your files into Unstructured from Zendesk.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/f2yeXwSvZtE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A [Zendesk account](https://www.zendesk.com/register/).
* Your [Zendesk subdomain](https://support.zendesk.com/hc/en-us/articles/4409381383578-Where-can-I-find-my-Zendesk-subdomain), for example, the `<organization>` part of `<organization>.zendesk.com`.
* The login email address for your Zendesk account.
* An [API token](https://support.zendesk.com/hc/en-us/articles/4408889192858-Managing-access-to-the-Zendesk-API#topic_tcb_fk1_2yb) (not an OAuth token) for your login email address.

To create a Zendesk source connector, see the following examples.

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
                  type="zendesk",
                  config={
                      "subdomain": "<subdomain>",
                      "email": "<email>",
                      "api_token": "<api-token>",
                      "item_type": "<item-type>",
                      "batch_size": <batch-size>
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
      "type": "zendesk",
      "config": {
          "subdomain": "<subdomain>",
          "email": "<email>",
          "api-token": "<api-token>",
          "item-type": "<item-type>",
          "batch-size": <batch-size>
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<subdomain>` (*required*): The subdomain of your Zendesk site, for example  the `<organization>` part of `<organization>.zendesk.com`.
* `<email>` (*required*): The email address of the user account that has access to the Zendesk subdomain.
* `<api-token>` (*required*): The API token (not an OAuth token) for the user account. For more information, see [Managing access to the Zendesk API](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token).
* `<item-type>`: The type of item to parse. Allowed values include `tickets` and `articles`. If no value is provided, the default is `tickets`.
* `<batch-size>`: The maximum number of items to structure per batch. The default is `2`.

## Learn more

* <Icon icon="blog" />  [Unlock Customer Support Knowledge: Unstructured Integrates with Zendesk](https://unstructured.io/blog/unlock-customer-support-knowledge-unstructured-integrates-with-zendesk)
