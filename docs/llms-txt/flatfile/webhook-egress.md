# Source: https://flatfile.com/docs/plugins/webhook-egress.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhook Egress

> Send workbook data from Flatfile to external webhook endpoints for seamless integration with your systems

The Webhook Egress plugin acts as a bridge between Flatfile and external systems by sending workbook data to webhook endpoints. When a user triggers a specific action in the Flatfile UI (like a "Submit" button), this plugin gathers all data from all sheets within the current workbook, packages it into a single JSON payload, and sends it via an HTTP POST request to a pre-configured webhook URL.

This plugin is ideal for integrating Flatfile with custom backends, serverless functions, or third-party services that accept data via webhooks. Common use cases include triggering data processing pipelines, updating databases, or pushing data into CRM systems once users have finished cleaning and preparing their data in Flatfile.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-webhook-egress
```

## Configuration & Parameters

### Parameters

<ParamField path="job" type="string" required>
  The name of the job or event that will trigger the egress process. This must correspond to an `operation` name defined in an action in your workbook configuration (e.g., 'workbook:submitActionFg').
</ParamField>

<ParamField path="webhookUrl" type="string" optional>
  The URL of the webhook endpoint where the workbook data will be sent. If not provided, the plugin will use the value from the `WEBHOOK_SITE_URL` environment variable.
</ParamField>

### Default Behavior

When the `webhookUrl` parameter is not provided during initialization, the plugin will look for an environment variable named `WEBHOOK_SITE_URL` and use its value as the destination for the data. If neither the parameter nor the environment variable is set, the request will fail. The plugin sends data as a JSON payload in an HTTP POST request with `Content-Type: application/json`.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  // listener.js
  import { listener } from '@flatfile/listener';
  import { webhookEgress } from '@flatfile/plugin-webhook-egress';

  listener.use(webhookEgress('workbook:submitActionFg'));

  // You also need to define the action in your workbook config
  // workbook.config.js
  const workbookConfig = {
    name: 'My Workbook',
    sheets: { /* ... */ },
    actions: [
      {
        operation: 'submitActionFg',
        mode: 'foreground',
        label: 'Submit Data',
        description: 'Send data to our system.',
        primary: true,
      },
    ],
  };
  ```

  ```typescript TypeScript theme={null}
  // listener.ts
  import { listener } from '@flatfile/listener';
  import { webhookEgress } from '@flatfile/plugin-webhook-egress';

  listener.use(webhookEgress('workbook:submitActionFg'));

  // You also need to define the action in your workbook config
  // workbook.config.ts
  const workbookConfig = {
    name: 'My Workbook',
    sheets: { /* ... */ },
    actions: [
      {
        operation: 'submitActionFg',
        mode: 'foreground',
        label: 'Submit Data',
        description: 'Send data to our system.',
        primary: true,
      },
    ],
  };
  ```
</CodeGroup>

### Explicit Webhook URL Configuration

<CodeGroup>
  ```javascript JavaScript theme={null}
  // listener.js
  import { listener } from '@flatfile/listener';
  import { webhookEgress } from '@flatfile/plugin-webhook-egress';

  const MY_WEBHOOK_URL = 'https://api.myapp.com/data-ingest';

  listener.use(webhookEgress('workbook:submitActionFg', MY_WEBHOOK_URL));
  ```

  ```typescript TypeScript theme={null}
  // listener.ts
  import { listener } from '@flatfile/listener';
  import { webhookEgress } from '@flatfile/plugin-webhook-egress';

  const MY_WEBHOOK_URL: string = 'https://api.myapp.com/data-ingest';

  listener.use(webhookEgress('workbook:submitActionFg', MY_WEBHOOK_URL));
  ```
</CodeGroup>

### Webhook Response with Rejections

The plugin can process responses from your webhook that contain data rejections. If your webhook performs validation and finds errors, it can return them in a specific JSON format, and the plugin will display these errors in the Flatfile UI.

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Example webhook endpoint response format
  // POST https://api.myapp.com/data-ingest
  /*
  {
    "rejections": {
      "id": "wb_abc123", // The workbook ID
      "sheets": [
        {
          "sheetId": "us_sh_xyz456", // The sheet ID
          "rejectedRecords": [
            {
              "id": "dev_rc_123", // The record ID
              "values": [
                {
                  "field": "email",
                  "message": "This email address is already in use."
                }
              ]
            }
          ]
        }
      ]
    }
  }
  */

  // No special client-side configuration needed for rejections
  import { listener } from '@flatfile/listener';
  import { webhookEgress } from '@flatfile/plugin-webhook-egress';

  listener.use(webhookEgress('workbook:submit', 'https://webhook.site/your-unique-url'));
  ```

  ```typescript TypeScript theme={null}
  // Example webhook endpoint response format
  // POST https://api.myapp.com/data-ingest
  /*
  {
    "rejections": {
      "id": "wb_abc123", // The workbook ID
      "sheets": [
        {
          "sheetId": "us_sh_xyz456", // The sheet ID
          "rejectedRecords": [
            {
              "id": "dev_rc_123", // The record ID
              "values": [
                {
                  "field": "email",
                  "message": "This email address is already in use."
                }
              ]
            }
          ]
        }
      ]
    }
  }
  */

  // No special client-side configuration needed for rejections
  import { listener } from '@flatfile/listener';
  import { webhookEgress } from '@flatfile/plugin-webhook-egress';

  listener.use(webhookEgress('workbook:submit', 'https://webhook.site/your-unique-url'));
  ```
</CodeGroup>

## Troubleshooting

### Common Error Messages

**"Failed to submit data to \[webhook]"**

* Check that the webhook URL is correct
* Verify the server is running and accessible
* Ensure the webhook is not returning error status codes (4xx or 5xx)

**"Error posting data to webhook"**

* Check for network connectivity issues
* Verify DNS resolution for the webhook URL
* Confirm the webhook URL is properly formatted

**"Request succeeded but failed to parse response from webhook"**

* Your webhook returns a 200 OK status but the response body is not valid JSON
* Ensure your endpoint returns `Content-Type: application/json`
* Return at least an empty JSON object `{}` if no specific response is needed

### Error Handling Patterns

The plugin handles errors internally and reports them as job outcomes:

* **Non-200 HTTP status codes**: The job completes with a failure message showing the status code
* **Network errors**: The job fails with a generic "Error posting data to webhook" message
* **Invalid JSON responses**: The job completes with a success status but warns about parsing issues

## Notes

### Requirements and Limitations

* An action must be configured in the workbook with an `operation` that matches the `job` string passed to the plugin
* The webhook endpoint must accept POST requests with `Content-Type: application/json`
* The entire workbook's data (all sheets and all records) is sent in a single request, which may result in large payloads for extensive workbooks

### Dependencies

* The plugin depends on `@flatfile/plugin-job-handler` for job lifecycle management (bundled with the plugin)
* Uses `@flatfile/util-response-rejection` for processing webhook rejection responses
* Utilizes `@flatfile/util-common` for error logging

### Validation Flow

The plugin supports a two-way validation flow where your webhook can return validation errors in the `rejections` format. These errors are automatically processed and displayed in the Flatfile UI, allowing users to see and correct data issues identified by your backend systems.
