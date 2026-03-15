# Source: https://docs.jit.io/docs/integrating-with-slack.md

# Slack Integration

Integrating with Slack

## Overview

Slack integration enables you to view security-related notifications in your team's native environment for day-to-day communications. Furthermore, you can assign specific notification types (e.g., whenever a developer ignores a security finding) to different channels in your Slack workspace.

## Steps for integrating with Slack

**To integrate with a Slack workspace—**

1. From the [Integrations page](https://docs.jit.io/docs/integrations-page), locate the Slack tile and select **Connect**. Your browser navigates to the Slack permissions page.
2. If you have multiple Slack workspaces, select the one you intend to integrate with from the dropdown in the top right corner of the page.
3. From the dropdown at the bottom of the page, select a channel for the Jit Bot to post on.
4. Select **Allow**. Your browser navigates back to the Jit platform.

![](https://files.readme.io/8de58f2-Screenshot_2022-08-31_6.58.53_AM.png)

> 👍 Success!
>
> Successful integration is indicated by a green check mark on the Slack tile. A welcome message from the Jit Bot displays in the Slack channel you previously selected.

## Configuring Slack channels

Jit enables you to assign channels in your Slack workspace for specific notification types. Use this option to stay organized and eliminate unnecessary noise.

### Notification types:

* *New high-severity findings*: This channel displays a notification for every high-severity (or greater) finding that is displayed in the Backlog page and was not found in the initial scan.
* *Ignored findings*: This channel displays a notification for each ignored finding.
* *Deployment on staging with findings*: (Coming soon!)
* *Findings on saved views*: Any new security finding that displays in a custom view defined in the Backlog page displays on this channel. For further information on custom views, visit the Backlog page.
* *New action created*: This channel displays a notification for every Action created in the Actions page.
* <br />

### Private Channels

Jit will detect public channels automatically. In order for Jit to post on **private** channels, you first need to add Jit app to that specific channel.

1. From Slack go to the channel you want Jit to post to.
2. Go to the channel settings (click the channel name).
3. Go to `Integrations` and click `Add an App`.\
   ![](https://files.readme.io/271b762-image.png)
4. Search for `Jit bot` and add it to the channel.

### Configure Slack channels in Jit platform

1. From the [Integrations page](https://docs.jit.io/docs/integrations-page), locate the Slack tile and select **Configure**.
2. Use the dropdowns located in the *Slack Notification Channels* section of the dialog to make your selections.
3. Select **Done**.

![](https://files.readme.io/127d416-small-image.png)

## Configuring users for action sharing

Jit enables you to alert other users to newly created Actions via a notification in Slack. To ensure that Jit sends the notification to the correct user, you may need to manually match Jit users with their identities in Slack. See below for instructions.

**To manually configure Slack users—**

1. From the [Integrations page](https://docs.jit.io/docs/integrations-page), locate the Slack tile and select **Configure**.
2. Use the dropdowns located in the *Configure Users for Sharing Actions* section to match Jit users with their identities in Slack.
3. Select **Done**.

![](https://files.readme.io/1f5fc6d-small-image_1.png)

## Disconnecting from Slack

**To disconnect from Slack—**

1. Navigate to the  [Integrations page](https://docs.jit.io/docs/integrations-page), locate the Slack tile, and select **Disconnect**. The disconnect dialog opens.
2. Select **Disconnect** to confirm the disconnection of Slack integration.