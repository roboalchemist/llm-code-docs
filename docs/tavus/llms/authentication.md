# Source: https://docs.tavus.io/api-reference/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> Learn how to generate and use your Tavus API key to authenticate requests.

To use the Tavus API, you need an API key to authenticate your requests. This key verifies that requests are coming from your Tavus account.

## Get the API key

1. Go to the <a href="https://platform.tavus.io/" target="_blank">Developer Portal</a> and select **API Key** from the sidebar menu.
2. Click **Create New Key** to begin generating your API key.
3. Enter a name for the key and (optional) specify allowed IP addresses, then click **Create API Key**.
4. Copy your newly created API key and store it securely.

<Warning>
  **Remember that your API key is a secret!**

  Never expose it in client-side code such as browsers or apps. Always load your API key securely from environment variables or a server-side configuration.
</Warning>

## Make Your First Call

Authentication to the API is performed via HTTP Basic Auth. To authenticate with Tavus's API endpoints, you must provide the API Key in the header, as shown below.

```curl Authentication Header theme={null}
'x-api-key: <api-key>'
```

For example, you are using the [POST - Create Conversation](/api-reference/conversations/create-conversation) endpoint to create a real-time video call session with a Tavus replica. In this scenario, you can send an API request and replace `<api_key>` with your actual API Key.

```shell cURL theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api_key>' \
  --data '{
  "replica_id": "r9d30b0e55ac",
  "persona_id": "pe13ed370726",
  "conversation_name": "Interview User"
}'
```
