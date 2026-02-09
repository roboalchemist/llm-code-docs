# Source: https://docs.aporia.com/integrations/slack-integration.md

# Source: https://docs.aporia.com/v1/integrations/slack-integration.md

# Slack

You can integrate Aporia with Slack to receive alerts and notifications directly to your Slack workspace.

Integrations can be found in the "Integrations" page, accessible through the sidebar:

![All Integrations](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FogmjRuZ5XbmPSJwXoBPm%2Fall_integrations.png?alt=media)

### Setting up the Slack Integration

After clicking the Slack integration, you will be redirected to Slack, where you will need to allow Aporia to post to a channel in your Slack workspace:

![Authorize Slack Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2Fzx5CRTQtyBcanZJUIcMs%2Fslack_authorize.png?alt=media)

Choosing a channel will redirect you back to Aporia:

![Slack Success](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FRD2AQUqguIwF3vUqMGBE%2Fslack_success.png?alt=media)

You can then send a test message, or remove the integration, through the Slack integration page:

![Slack Manage](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FL7k5qz2g3sr6BtsvkLE5%2Fslack_manage.png?alt=media)

### Sending Alerts to Slack

After setting up the Slack integration, you can configure monitors to send a message to your chosen slack channel when an anomaly is detected:

![Slack in Monitor Config](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2Fr5q60CsDDUN3sUXqTJWM%2Fslack_monitor.png?alt=media)

### Tagging Users in Slack

You can easily tag users in the Slack notifications using an alert's custom description.

Get the user id from Slack:

![Get Slack User ID](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F2qvAvDpDRdLipyQ21rPS%2F1.png?alt=media)

Insert it in the custom description:&#x20;

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FnSePxLFXK2YfcDSdcmGY%2F2.png?alt=media" alt=""><figcaption></figcaption></figure>

The user tag should be in the form of `<@user_id>`

Save the monitor.

Now, whenever you receive a Slack alert, the user will be tagged in the message:

![Alert Custom Description](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FKqZab93b61LqhA0NtobO%2F3.png?alt=media)
