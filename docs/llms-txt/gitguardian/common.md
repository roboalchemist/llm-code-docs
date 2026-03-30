# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/messaging-integrations/common.md

# Common

> Step-by-step instructions for installing the GitGuardian app on Slack workspaces to monitor public and private channels for secret leaks.

You can install GitGuardian on multiple Slack workspaces to start monitoring for secret leaks.

1. Make sure you're logged in to the Slack workspace you want to install
2. On the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
3. Click **Install** next to **Slack** in the **Messaging** section 
   ![Slack install](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-install.png)
4. Click **Install** on the [Slack integration](https://dashboard.gitguardian.com/settings/integrations/slack) page
5. Select the Slack workspace you want to add
6. Click **Allow** to grant the permissions requested by GitGuardian 
   ![Slack permissions](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-permissions.png)

That's it! Our GitGuardian app is now automatically joining all your public channels and will monitor new messages in these channels. You can also invite the GitGuardian app to private channels to monitor these channels as well.
