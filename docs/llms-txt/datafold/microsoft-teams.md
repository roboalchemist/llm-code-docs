# Source: https://docs.datafold.com/integrations/notifications/microsoft-teams.md

# Microsoft Teams

> Receive notifications for monitors in Microsoft Teams.

## Prerequisites

* Microsoft Teams admin access or permissions to manage integrations
* A Datafold account with admin privileges

## Configure the Integration

1. In Datafold, go to Settings > Integrations > Notifications
2. Click "Add New Integration"
3. Select "Microsoft Teams"
4. You'll be automatically redirected to the Microsoft Office login page
5. Sign in using the Microsoft Office account with admin privileges
6. Click "Accept" to grant Datafold the necessary permissions
7. You'll be redirected back to Datafold
8. Open the Teams app in a separate browser tab
9. Next to the channel where you'd like to receive notifications, click "..." and select "Workflows"
10. Select the template called "Post to a channel when a webhook request is received"
11. Advance through the wizard (the defaults should be fine)
12. At the end of the wizard, copy the webhook URL
13. Return to Datafold and click "Add channel configuration"
14. Select the relevant Team and Channel, then paste the webhook URL
15. Repeat steps 8-14 for as many channels as you'd like
16. Save the integration settings in Datafold

You're all set! When you configure a monitor in Datafold, you'll now have the option to send notifications to the Teams channel(s) you configured.

## Monitors as Code Configuration

If you're using [monitors as code](/data-monitoring/monitors-as-code), you can configure Teams notifications by adding a `notifications` section to your monitor definition as follows:

```yaml  theme={null}
monitors:
  <monitor_name>:
    ...
    notifications:
      - type: teams
        integration: <integration_id>
        channel: <team_name>:<channel_name>
        mentions:
          - <tag_name>
          - <user_name>
          ...
```

* `<integration_id>` can be found in Datafold -> Settings -> Integrations -> Notifications -> \<your\_ms\_teams\_integration>

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
      - type: teams
        integration: 23
        channel: Dev Team:Notifications Channel
        mentions:
          - NotifyDevCustomTag
          - Dima Cherenkov
```

## Need help?

If you have any questions about integrating with Microsoft Teams, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
