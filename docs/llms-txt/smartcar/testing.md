# Source: https://smartcar.com/docs/integrations/webhooks/best-practices/testing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing

> Test your webhook integration before going to production

Thoroughly test your webhook integration to catch issues before they affect users.

## Test in Development

Use the Smartcar Dashboard to trigger test webhook deliveries.

<Steps>
  <Step title="Set up local tunnel">
    Use ngrok or similar to expose your local server:

    ```bash  theme={null}
    ngrok http 3000
    ```

    This creates a public HTTPS URL that forwards to your local development server.
  </Step>

  <Step title="Configure webhook">
    In the Smartcar Dashboard, set your ngrok URL as the callback URI (e.g., `https://abc123.ngrok.io/webhooks/smartcar`)
  </Step>

  <Step title="Verify webhook">
    Complete the VERIFY challenge to activate the webhook
  </Step>

  <Step title="Trigger test events">
    Use the Dashboard to send test `VEHICLE_STATE` and `VEHICLE_ERROR` events to your endpoint
  </Step>

  <Step title="Verify handling">
    Check logs to confirm:

    * Signature verification works
    * Payload is queued successfully
    * Processing logic executes correctly
    * Idempotency prevents duplicates
  </Step>
</Steps>

***

## Next Steps

Once testing is complete, prepare for production deployment:

<CardGroup cols={2}>
  <Card title="Monitoring" icon="chart-line" href="/integrations/webhooks/best-practices/monitoring">
    Set up production monitoring and alerts
  </Card>

  <Card title="Security" icon="shield-check" href="/integrations/webhooks/best-practices/security">
    Review security best practices for production
  </Card>

  <Card title="Webhook Receiver Recipe" icon="rocket" href="/getting-started/tutorials/webhook-receiver-recipe">
    Deploy production-ready AWS infrastructure
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Understand production retry and timeout policies
  </Card>
</CardGroup>
