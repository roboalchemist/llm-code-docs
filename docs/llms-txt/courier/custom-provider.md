# Source: https://www.courier.com/docs/external-integrations/other/custom-provider.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Provider

> Set up a Custom Provider in Courier's Push channel to deliver rich push messages to your own webhook endpoint, with support for content blocks and full payload overrides.

## Setup

To install the Custom Provider, navigate to [Custom Provider integration](https://app.courier.com/integrations/catalog/custom). Input your webhook HTTP address and choose an authentication model.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/channels/custom-provider.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=02ea87ea23764cfc71710244f5df4bf3" alt="Custom Provider" width="1266" height="1226" data-path="assets/platform/channels/custom-provider.png" />
</Frame>

After installing the Custom Provider, you can add it to any Push Channel. After adding a "Push Channel", open up the Channel Settings Modal.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/channels/custom-provider-settings.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=44c8e40d2c02b12d9fd70cc2d5c913bc" alt="Custom Provider Settings" width="714" height="344" data-path="assets/platform/channels/custom-provider-settings.png" />
</Frame>

You will see "Custom" in the list of "Installed Providers".

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/channels/custom-installed-provider.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=147f9432ad2d2e1dcf0203f99e39588c" alt="Installed Custom Provider" width="1460" height="432" data-path="assets/platform/channels/custom-installed-provider.png" />
</Frame>

You can now add a Title and blocks to your designer. They will be sent as both "plain text" and an array of "blocks" to the configured webhook.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/channels/custom-provider-designer.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=0061cfee73d57db561382fb982a41d2b" alt="Custom Provider Designer" width="916" height="482" data-path="assets/platform/channels/custom-provider-designer.png" />
</Frame>

Upon sending the message, your webhook will receive a payload that looks like this:

```js  theme={null}
interface TextBlock {
  type: "text";
  text: string;
}

interface ActionBlock {
  type: "action";
  url: string;
  text: string;
}

interface PushMessage {
  type: "push";
  data: {
  	messageId: string;
    content: {
      title: string;
      body: string;
      blocks: Array<ActionBlock | TextBlock>
    }
  }
}
```

```json  theme={null}
{
  "type": "push",
  "data": {
    "messageId": "1-6140e057-2749378a31c6026f3dab823f",
    "content": {
      "blocks": [
        {
          "text": "My Body",
          "type": "text"
        },
        {
          "text": "Click Here",
          "url": "https://example.execute-api.us-east-1.amazonaws.com/dev/r/TRACKING_ID",
          "type": "action"
        }
      ],
      "body": "My Body\nClick Here: https://example.execute-api.us-east-1.amazonaws.com/dev/r/TRACKING_ID",
      "title": "My Title"
    }
  }
}
```

## Overrides

You can use an override to replace what Courier sends to your custom provider. The `body`, `headers`, `method`, and `url` fields are all overridable.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "custom": {
        "override": {
          "body": {},
          "headers": {},
          "method": "POST",
          "url": "https://your-endpoint.example.com/webhook"
        }
      }
    }
  }
}
```
