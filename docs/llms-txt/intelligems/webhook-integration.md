# Source: https://docs.intelligems.io/integrations/webhook-integration.md

# Webhook Integration

## Introduction

Intelligems provides a powerful webhook system that allows you to send real-time data about experiments, user actions, and store events to external services. This enables you to build custom integrations, automate workflows, and connect Intelligems data with your existing tools and platforms.

## Overview

Webhooks are HTTP POST requests that Intelligems sends to your specified endpoints when certain events occur. This allows you to:

* Receive real-time notifications about experiment events
* Integrate Intelligems data with external analytics platforms
* Automate workflows based on A/B test results
* Send alerts to team communication tools like Slack
* Trigger custom business logic in your applications

## Available Webhook Events

Intelligems supports webhooks for the following experience event types:

#### Experience Events

* **Create Experience**: Triggered when a new A/B test or experiment is created
* **Start Experience**: Triggered when an experiment goes live
* **Pause Experience**: Triggered when an experiment is paused
* **End Experience**: Triggered when an experiment is stopped or completed
* **Update Experience**: Triggered when experiment settings are modified
* **Delete Experience**: Triggered when an experiment is deleted

## Setting Up Webhooks

#### 1. Configure Webhook Endpoints

To set up webhooks in Intelligems:

1. Navigate to **Settings** in your Intelligems dashboard
2. Enter your webhook endpoint URL
3. Select the events you want to receive
4. Click Add Webhook in the Webhooks section
5. Configure any authentication headers within your consuming application, if required
6. Test the webhook connection

#### 2. Webhook Security (Optional)

Intelligems signs all webhook payloads with a secret key to ensure authenticity:

```javascript
// Verify webhook signature (Node.js example)
const crypto = require('crypto');

function verifyWebhookSignature(payload, signature, secret) {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

#### 3. Handling Webhook Retries

Intelligems will retry failed webhook deliveries:

* **Success Criteria**: HTTP status codes 200-299
* **Timeout**: 10 seconds per request
* **Maximum Retries**: 5 attempts

## Example: Zapier to Slack Integration

This step-by-step example shows how to use Zapier to send Slack alerts when experiments launch.&#x20;

#### Step 1: Create a Zapier Webhook

1. Log into your [Zapier account](https://zapier.com)
2. Click **Create Zap**
3. Search for and select **Webhooks by Zapier** as the trigger app
4. Choose **Catch Hook** as the trigger event
5. Copy the webhook URL provided by Zapier

#### Step 2: Configure Intelligems Webhook

1. In your Intelligems dashboard, go to **Settings** > **Integrations**
2. Click **Add Webhook**
3. Paste the Zapier webhook URL
4. Select the **Start Experience** event (or any other experience event you want to track)
5. Save the configuration

#### Step 3: Set Up Slack Action in Zapier

1. In your Zapier workflow, click **Continue** after setting up the webhook trigger
2. Search for and select **Slack** as the action app
3. Choose **Send Channel Message** as the action event
4. Connect your Slack account if not already connected
5. Configure the Slack message:
   * **Channel**: Select your desired Slack channel (e.g., #marketing-alerts)
   * **Message Text**: Use dynamic fields from the webhook payload:

#### Step 4: Test the Integration

1. In Zapier, click **Test & Continue** to test the Slack message
2. Create a test experiment in Intelligems or trigger a test webhook
3. Verify that the Slack message appears in your chosen channel
4. Turn on your Zap to make it live

## Additional Integration Examples

### Google Sheets Integration

Track experiment results in a Google Sheet:

1. Use **Google Sheets** as the Zapier action app
2. Choose **Create Spreadsheet Row** as the action
3. Map webhook fields to spreadsheet columns:
   * Column A: Experience Name
   * Column B: Action Type
   * Column C: Experience Type
   * Column D: Timestamp
   * Column E: Experience ID
   * Column F: Triggered By Email

### Email Notifications

Send email alerts to your team:

1. Use **Email by Zapier** as the action app
2. Configure recipient email addresses
3. Create email templates with experience data
4. Set up different email templates for different action types

### Custom API Integration

Send data to your own API endpoint:

1. Use **Webhooks by Zapier** as the action app
2. Choose **POST** as the action event
3. Configure your API endpoint URL
4. Map webhook payload data to your API format
5. Add authentication headers if required

## Best Practices

#### 1. Webhook Endpoint Design

* **Respond Quickly**: Return HTTP 200 status within 10 seconds
* **Validate Signatures**: Always verify webhook authenticity
* **Log Events**: Keep records of received webhooks for debugging

#### 2. Error Handling

```javascript
// Example webhook handler with proper error handling
app.post('/webhook/intelligems', (req, res) => {
  try {
    // Verify signature
    if (!verifyWebhookSignature(req.body, req.headers['X-Intelligems-Signature'], secret)) {
      return res.status(401).send('Invalid signature');
    }

    // Process webhook
    processWebhookEvent(req.body);

    // Respond quickly
    res.status(200).send('OK');
  } catch (error) {
    console.error('Webhook processing error:', error);
    res.status(500).send('Internal server error');
  }
});
```

#### 3. Monitoring and Debugging

* Test webhooks thoroughly before going live

## Troubleshooting

### Common Issues

#### **Webhook Not Receiving Data**

* Verify the endpoint URL is correct and accessible
* Check that your server responds with HTTP 200
* Ensure firewall settings allow incoming requests
* Verify the webhook is enabled for the correct events

#### **Authentication Failures**

* Confirm webhook signature verification is implemented correctly
* Check that the secret key matches your configuration
* Verify timestamp tolerance in signature validation

#### **Zapier Integration Issues**

* Ensure the Zapier webhook URL is correctly configured in Intelligems
* Check that your Zap is turned on and active
* Verify field mappings in your Zapier action steps
* Test the integration with sample data
