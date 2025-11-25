# Source: https://docs.unstructured.io/ui/sources/slack.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/slack.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/slack.md

# Slack

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

Ingest your files into Unstructured from Slack.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/0F1MXMgk3kY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A Slack app. Create a Slack app by following [Step 1: Creating an app](https://api.slack.com/quickstart#creating).

* The app must have the the following OAuth scopes:

  * To read messages from public channels, add the scopes `channels:join` and `channels:history`.
  * To read messages from private channels, add the scope `groups:history`.

  Add these scopes to the app by following [Step 2: Requesting scopes](https://api.slack.com/quickstart#scopes).

* The app must be installed and authorized for the target Slack workspace. Install and authorize the app by following [Step 3: Installing and authorizing the app](https://api.slack.com/quickstart#installing).

* The app's access token. Get this token by following [Step 3: Installing and authorizing the app](https://api.slack.com/quickstart#installing).

* Add the app to the target channels in the Slack workspace. To do this from the channel, open the channel's details page, click the **Integrations** tab, click **Add apps**, and follow the on-screen directions to install the app.

* The channel ID for each target channel. To get this ID, open the channel's details page, and look for the **Channel ID** field on the **About** tab.

* The starting and ending date and time range for the channels to be processed. Supported formats include:

  * `YYYY-MM-DD`
  * `YYYY-MM-DDTHH:MM:SS`
  * `YYYY-MM-DDTHH:MM:SSZ`
  * `YYYY-MM-DD+HH:MM:SS`
  * `YYYY-MM-DD-HH:MM:SS`

<Info>
  Slack has established API rate limits that could restrict the number and frequency of messages that can be read. To
  explore possible workarounds for these cases, see your Slack representative.
</Info>

To create a Slack source connector, see the following examples.

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
                  type="slack",
                  config={
                      "channels": [
                          "<channel>",
                          "<channel>"
                      ],
                      "start_date": "<start-date>",
                      "end_date": "<end-date>",
                      "token": "<token>"
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
      "type": "slack",
      "config": {
          "channels": [
              "<channel>",
              "<channel>"
          ],
          "start-date": "<start-date>",
          "end-date": "<end-date>",
          "token": "<token>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<channel>` (*required*): The ID of the target Slack channel from which to read messages.
* `<start-date>`: The date and time, in ISO 8601 format (such as `YYYY-MM-DDTHH:MM:SSZ`), from which to begin reading messages. Messages created before this timestamp are ignored. By default, all messages are read unless an end date is specified.
* `<end-date>`: The date and time, in ISO 8601 format (such as `YYYY-MM-DDTHH:MM:SSZ`), at which to stop reading messages. Messages created after this timestamp are ignored. By default, all messages are read unless a start date is specified.
* `<token>` (*required*): The access token for the Slack app that has permission to read messages from the target Slack channels.
