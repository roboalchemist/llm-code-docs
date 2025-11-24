# Source: https://flatfile.com/docs/plugins/webhook-event-forwarder.md

# Webhook Event Forwarder

> Forward all Flatfile events to a webhook URL for language-agnostic integration with external systems

The Webhook Event Forwarder plugin for Flatfile is designed to capture all events within a Flatfile listener and forward them to a specified webhook URL. This allows developers to process Flatfile events in external systems, regardless of the programming language used at the endpoint.

Its primary purpose is to enable language-agnostic integration with backend services. Common use cases include:

* Triggering custom workflows in services like Zapier or Make
* Storing event data in an external database or data warehouse for analytics
* Notifying external systems of user actions within Flatfile (e.g., data submission, file upload)
* Implementing custom validation or data processing logic on a separate server

The plugin listens for all events (`**`), packages the full event object as a JSON payload, and sends it via an HTTP POST request.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-webhook-event-forwarder
```

## Configuration & Parameters

### webhookEventForward(url, callback?, options?)

| Parameter       | Type       | Required | Description                                                                                                                                                                 |
| --------------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`           | `string`   | Yes      | The webhook endpoint URL where the plugin will send all Flatfile events via an HTTP POST request                                                                            |
| `callback`      | `function` | No       | An optional callback function that is executed after the webhook request is complete. Receives `data` (webhook response) and `event` (original Flatfile event) as arguments |
| `options`       | `object`   | No       | Additional configuration options                                                                                                                                            |
| `options.debug` | `boolean`  | No       | When set to `true`, logs any errors that occur during the webhook forwarding process to the console. Default: `false`                                                       |

### Default Behavior

By default, the plugin listens for every event (`**`) emitted by the Flatfile listener. For each event, it sends an HTTP POST request to the provided `url` with the event object serialized as a JSON string in the request body. If the webhook call fails, the error is suppressed unless `options.debug` is set to `true`. No action is taken on the webhook's response unless a `callback` function is provided.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';

  listener.use(webhookEventForward('https://webhook.site/your-unique-id'));
  ```

  ```typescript TypeScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';

  listener.use(webhookEventForward('https://webhook.site/your-unique-id'));
  ```
</CodeGroup>

### Configuration with Callback and Debug

<CodeGroup>
  ```javascript JavaScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';

  const myCallback = (response, event) => {
    console.log(`Received response for event: ${event.topic}`);
    console.log('Webhook response data:', response);
  };

  const options = {
    debug: true
  };

  listener.use(webhookEventForward('https://webhook.site/your-unique-id', myCallback, options));
  ```

  ```typescript TypeScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';
  import type { FlatfileEvent } from '@flatfile/listener';

  const myCallback = (response: any, event: FlatfileEvent) => {
    console.log(`Received response for event: ${event.topic}`);
    console.log('Webhook response data:', response);
  };

  const options = {
    debug: true
  };

  listener.use(webhookEventForward('https://webhook.site/your-unique-id', myCallback, options));
  ```
</CodeGroup>

### Advanced Usage with Async Callback

<CodeGroup>
  ```javascript JavaScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';

  const handleWebhookResponse = async (response, event) => {
    if (response?.error) {
      console.error(`Failed to process event ${event.id} at webhook. Error: ${response.message}`);
      // You could add logic here to retry the operation or send a notification
    } else {
      console.log(`Event ${event.id} successfully processed by webhook.`);
      // You could update a record in your own database with the response
    }
  };

  listener.use(webhookEventForward('https://api.my-service.com/flatfile-hook', handleWebhookResponse));
  ```

  ```typescript TypeScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';
  import type { FlatfileEvent } from '@flatfile/listener';

  const handleWebhookResponse = async (response: any, event: FlatfileEvent) => {
    if (response?.error) {
      console.error(`Failed to process event ${event.id} at webhook. Error: ${response.message}`);
      // You could add logic here to retry the operation or send a notification
    } else {
      console.log(`Event ${event.id} successfully processed by webhook.`);
      // You could update a record in your own database with the response
    }
  };

  listener.use(webhookEventForward('https://api.my-service.com/flatfile-hook', handleWebhookResponse));
  ```
</CodeGroup>

### Error Handling Example

<CodeGroup>
  ```javascript JavaScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';

  const myCallback = (response, event) => {
    // Check for the error object passed by the plugin on failure
    if (response && response.error === true) {
      console.error(`Webhook forwarding failed for event: ${event.topic}`);
      console.error(`Message: ${response.message}`);
      console.error(`Details: ${response.data}`);
    } else {
      console.log(`Webhook for event ${event.topic} succeeded.`);
    }
  };

  // Use a URL that is expected to fail to demonstrate error handling
  // and enable debug logging to see the error in the console.
  listener.use(webhookEventForward('https://httpstat.us/500', myCallback, { debug: true }));
  ```

  ```typescript TypeScript
  import { listener } from './listener'; // Your listener instance
  import { webhookEventForward } from '@flatfile/plugin-webhook-event-forwarder';
  import type { FlatfileEvent } from '@flatfile/listener';

  const myCallback = (response: any, event: FlatfileEvent) => {
    // Check for the error object passed by the plugin on failure
    if (response && response.error === true) {
      console.error(`Webhook forwarding failed for event: ${event.topic}`);
      console.error(`Message: ${response.message}`);
      console.error(`Details: ${response.data}`);
    } else {
      console.log(`Webhook for event ${event.topic} succeeded.`);
    }
  };

  // Use a URL that is expected to fail to demonstrate error handling
  // and enable debug logging to see the error in the console.
  listener.use(webhookEventForward('https://httpstat.us/500', myCallback, { debug: true }));
  ```
</CodeGroup>

## Troubleshooting

To troubleshoot issues:

1. **Enable debug mode**: Set `debug: true` in the options object to see detailed error messages in your console logs.

2. **Verify URL accessibility**: Ensure that the `url` provided is correct and is publicly accessible from the environment where your Flatfile listener is running.

3. **Check webhook endpoint logs**: Review the server logs of your webhook endpoint to see if it's receiving requests and if it's returning any errors.

4. **Test with webhook.site**: Use a service like `webhook.site` to test if events are being sent correctly from the plugin.

## Notes

### Important Considerations

* **Event Volume**: The plugin listens for `**` (all events), which can generate a high volume of HTTP requests to your endpoint. Ensure your webhook receiver can handle the potential load.

* **Synchronous vs. Asynchronous**: The plugin sends the webhook request and continues. While the callback function can be `async` and is `await`ed, the plugin does not block the Flatfile event lifecycle.

* **Security**: The plugin sends the full event payload, which may contain sensitive data. Ensure your webhook endpoint is secure (uses HTTPS) and properly authenticated if necessary. The plugin itself does not add any authentication headers; this would need to be handled by the receiving endpoint or by wrapping the fetch call.

### Error Handling Patterns

The plugin uses a `try...catch` block to handle errors during the `fetch` call. If an error occurs (including non-ok HTTP responses like 4xx or 5xx), it will not crash the listener process. Instead, it constructs a standardized error object:

```json
{
  "error": true,
  "message": "Error received, please try again",
  "data": "error details"
}
```

This object is then passed as the first argument to the `callback` function, if provided. If `options.debug` is `true`, the original error is also logged to the console.
