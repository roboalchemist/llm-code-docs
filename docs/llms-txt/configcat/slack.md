# Source: https://configcat.com/docs/integrations/slack.md

# Slack - Get notified when a feature flag changes

## Overview[​](#overview "Direct link to Overview")

Receive notifications via a Slack Channel message when someone changes a feature flag using the [ConfigCat Feature Flags app for Slack](https://configcat.slack.com/apps/A011CN2QZJB-configcat-feature-flags).

![slack\_notification](/docs/assets/slack/notification.png)

## Installation[​](#installation "Direct link to Installation")

1. Open the [integrations tab](https://app.configcat.com/product/integrations) on the ConfigCat Dashboard.
2. Click on Slack's CONNECT button and connect ConfigCat Feature Flags with your Slack workspace.
3. You're all set. Go ahead and make some changes to your feature flags, then check your Slack Channel for notifications.

## Un-installation[​](#un-installation "Direct link to Un-installation")

1. Open the [integrations tab](https://app.configcat.com/product/integrations) on ConfigCat Dashboard.
2. Click on Slack's DISCONNECT button.

Disconnection from ConfigCat stops sending notifications to your selected Slack channel. To manage authorization or remove the integration completely, please follow the instructions below:

1. Open your Slack App Directory: `<YOUR-WORKSPACE>.slack.com/apps/manage`

2. Select the `ConfigCat Feature Flags` app.

3. Select the `Configuration` tab.

   <!-- -->

   * If you'd like to remove the integration from an individual channel, you can **Revoke** its access in the `Your authorization` section.
   * If you'd like to remove the integration from your workspace completely, click the **Remove app** button in the `Remove app` section.

## Usage[​](#usage "Direct link to Usage")

1. Make some changes to your feature flags.
2. Check your Slack Channel for notifications.
