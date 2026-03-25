# Source: https://docs.firehydrant.com/docs/google-cloud-stackdriver-event-source.md

# Google Cloud Stackdriver Event Source

The StackDriver Integration for Signals allows users to create events in FireHydrant from webhooks configured in StackDriver. Anytime that StackDriver sends an event to FireHydrant, we’ll evaluate the signal to see if if matches a rule setup by one of your teams. If it matches that rule, we’ll alert the team. Learn more about [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) here.

### Configuring StackDriver Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find two webhook URLs that you can use when creating a webhook in StackDriver. One webhook is designed to support batch alerts while the other will handle single alerts.

   <Image align="center" src="https://files.readme.io/f96b873-stackdriver-webhooks.jpg" />
2. Follow the steps in the Google Cloud documentation provided below. Add the URL from step 1 as your webhook's Endpoint URL.

You can learn more about StackDriver webhook alerts by reading[ their documentation](https://cloud.google.com/blog/products/gcp/how-to-connect-stackdriver-to-external-monitoring).

### Testing your StackDriver Webhook

1. When editing your webhook, click the "Test Connection" button to send a test to FireHydrant.
2. Confirm that FireHydrant received your webhook by visiting Alerting > Webhook Logs in the web app. You should see a new event created. You can open the drawer to see the transposed Signal from Stackdriver.

<Image align="center" src="https://files.readme.io/8c8ea27-logs.jpg" />