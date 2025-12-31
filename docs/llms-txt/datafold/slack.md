# Source: https://docs.datafold.com/integrations/notifications/slack.md

# Slack

> Receive notifications for monitors in Slack.

## Prerequisites

* Slack admin access or permissions to manage integrations
* A Datafold account with admin privileges

## Configure the Integration

1. In Datafold, go to Settings > Integrations > Notifications
2. Click "Add New Integration"
3. Select "Slack"
4. You'll be automatically redirected to Slack
5. If you're not already signed in, sign in to your Slack account
6. Click "Allow" to grant Datafold the necessary permissions
7. You'll be redirected back to Datafold

You're all set! When you configure a monitor in Datafold, you'll now have the option to send notifications to Slack.

## Monitors as Code Configuration

If you're using [monitors as code](/data-monitoring/monitors-as-code), you can configure Slack notifications by adding a `notifications` section to your monitor definition as follows:

```yaml  theme={null}
monitors:
  <monitor_name>:
    ...
    notifications:
      - type: slack
        integration: <integration_id>
        channel: <channel_name>
        mentions:
          - <user_name>
          - here
          - channel
          ...
```

* `<integration_id>` can be found in Datafold -> Settings -> Integrations -> Notifications -> \<your\_slack\_integration>

#### Full example

```yaml  theme={null}
monitors:
  uniqueness_test_example:
    type: test
    enabled: true
    connection_id: 1123
    test:
      type: unique
      tables:
        - path: DEV.DATA_DEV.USERS
          columns:
            - USERNAME
    schedule:
      interval:
        every: hour
    notifications:
      - type: slack
        integration: 13
        channel: dev-notifications
        mentions:
          - John Doe
          - channel
```

## Need help?

If you have any questions about integrating with Slack, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
