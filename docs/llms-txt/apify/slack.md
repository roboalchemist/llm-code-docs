# Source: https://docs.apify.com/platform/integrations/slack.md

# Slack integration

**Learn how to integrate your Apify Actors with Slack. This article guides you from installation through to automating your whole workflow in Slack.**

A tutorial can be found on https://help.apify.com/en/articles/6454058-apify-integration-for-slack.

***

> Explore the https://help.apify.com/en/articles/6454058-apify-integration-for-slack.

https://slack.com/ allows you to install various services in your workspace in order to automate and centralize jobs. Apify is one of these services, and it allows you to run your Apify Actors, get notified about their run statuses, and receive your results, all without opening your browser.

## Get started

To use the Apify integration for Slack, you will need:

* An https://console.apify.com/.
* A Slack account (and workspace).

## Step 1: Set up the integration for Slack

You can find all integrations on an Actor's or task's **Integrations** tab. For example, you can try using the https://console.apify.com/actors/aLTexEuCetoJNL9bL.

Find the integration for Slack, then click the **Configure** button. You will be prompted to log in with your Slack account and select your workspace in the **Settings > Integrations** window.

![Integrations tab](/assets/images/integrations-tab-ccd1902979bfea9812a6de7046ec6f04.png)

Then, head back to your task to finish the setup. Select what type of events you would like to be notified of (e.g., when a run is created, when a run succeeds, when a run fails, etc.), your workspace, and the channel you want to receive the notifications in (you can set up an ad-hoc channel for this test). In the **Message** field, you can see how the notification will look, or you can craft a new custom one.

![Integration setup](/assets/images/slack-integration-setup-0b413d14c705608f5d6a73e0ee5b5e05.png)

Once you are done, click the **Save** button.

## Step 2: Give the Apify integration a trial run

Click the **Start** button and head to the Slack channel you selected to see your first Apify integration notifications.

## Step 3: Start your run directly from Slack

You can now run the same Actor or task directly from Slack by typing `/apify call [Actor or task ID]` into the Slack message box.

![Use Apify from Slack](/assets/images/slack-apify-message-6c772c8d007770c873bfdc0f4201e80e.png)

When an Actor doesn't require you to fill in any input fields, you can run it by simply typing `/apify call [Actor or task ID]`.

You're all set! If you have any questions or need help, feel free to reach out to us on our https://discord.com/invite/jyEM2PRvMU.
