# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/notifications/slack.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/managing-your-account/subscribing-to-notifications/slack.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/managing-your-account/subscribing-to-notifications/slack.md

# Subscribing to Slack notifications

Once your Slack workspace administrator [has connected the workspace to SonarQube Server](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack/setup), you can subscribe to Slack notifications for your project. Follow the steps below to subscribe to your project in the Slack channel of your choice.

{% hint style="info" %}
In the following sections, you will need to execute the required operation by entering a slash command starting with `/sonarqube-server`. **If your Slack workspace is connected to multiple SonarQube Server instances**, your administrator may have configured for your instance a custom slash command, like `/sonarqube-server-2`, which you will need to use instead. For more information, consult your administrator.
{% endhint %}

{% hint style="warning" %}
If your organization uses Slack Enterprise and the SonarQube Server app for Slack is already installed on a different workspace, you might see the app in your workspace even if it hasn't been installed there yet. \
If you install the app via a `@SonarQube Server` command or directly from the Slack app configuration page in this state, the app will install on your workspace but will not function correctly.\
The SonarQube Server app for Slack must be installed directly through SonarQube Server (see [setup](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack/setup "mention")). If you are unsure about your installation status, please consult your administrator.
{% endhint %}

### Step 1: Log in to the SonarQube Server app for Slack

Logging in to the SonarQube Server app for Slack connects your Slack account to your SonarQube Server account. You only need to do this once.

To log in to the SonarQube Server app for Slack:

1. In your Slack workspace, go to **Apps** and open the **SonarQube Server** app.

<figure><img src="broken-reference" alt="SonarQube Server app for Slack"><figcaption></figcaption></figure>

2. In the **Messages** tab, type `/sonarqube-server connect`. You will be prompted to connect your SonarQube Server account to Slack.

### Step 2: Prepare the channel to be used for subscription

You must select the Slack channel to be used to receive your project’s notifications. You can create a new one. Note that:

* All channel members will receive the SonarQube Server notifications.
* You can use the same channel to receive the notifications on different projects distributed across various organizations.
* You may need specific permissions to add the app to private channels.

If your Slack channel is private, you need to add the SonarQube Server app for Slack to your channel:

1. In your Slack workspace, navigate to your private channel.
2. In the private channel, type `/invite @SonarQube Server`.

### Step 3: Subscribe your channel to your project

Make sure that you have the Browse permission on the project in SonarQube Server.

{% hint style="warning" %}
All channel members will receive the SonarQube Server notifications on your project.
{% endhint %}

To subscribe your channel to your project:

1. In SonarQube Server, copy your project key. You'll find the project key in the **Project Information** page as illustrated below.

<figure><img src="broken-reference" alt="To copy your project key, select the copy icon in the Project Key section."><figcaption></figcaption></figure>

2. In your Slack workspace, navigate to the channel in which you want to enable the subscription.
3. In the channel, type `/sonarqube-server subscribe <project_key>` .

### Unsubscribing a channel from a project

To unsubscribe a channel from a project, you need the Browse permission on the project in SonarQube Server.

{% hint style="warning" %}
Unsubscribing a channel from a project disables the subscription for all members of the channel.
{% endhint %}

To unsubscribe a channel from a project:

1. In SonarQube Server, copy the project key. You'll find the project key in the **Project Information** page.
2. In your Slack workspace, navigate to the channel subscribed to your project.
3. In the channel, type `/sonarqube-server unsubscribe <project_key>`.

### Relates pages

[setup](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack/setup "mention")\
[about](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack/about "mention")
