# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/subscribing-to-slack-notifications.md

# Subscribing to Slack notifications

Once your Slack workspace admin [has connected the workspace to SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/setup), you can subscribe to Slack notifications for your project. To do so, you subscribe to your project in the Slack channel of your choice.

For more information about the Slack integration in SonarQube Cloud, see [integration-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/integration-overview "mention"), or check out this [video](https://www.youtube.com/watch?v=oW-pp4LN9r0) on how to benefit from the Slack integration.

### Step 1: Connect your Slack and SonarQube Cloud accounts

You only need to perform this step once.

Proceed as follows:

1. In your Slack workspace, navigate to any channel.
2. In the channel, type `/sonarqube connect`. You will be prompted to connect your account.

### Step 2: Prepare the channel to be used for subscription

You must select the Slack channel to be used to receive your project’s notifications. You can create a new one. Note that:

* All channel members will receive the SonarQube Cloud notifications.
* You can use the same channel to receive the notifications on different projects distributed across various organizations.
* You may need specific permissions to add the app to private channels.

If your Slack channel is private, you need to add the SonarQube App for Slack to your channel:

1. In your Slack workspace, navigate to your private channel.
2. In the private channel, type `/invite @SonarQube`.

### Step 3: Subscribe your channel to your project

Make sure that you have the Browse permission on the project in SonarQube Cloud.

{% hint style="warning" %}
All channel members will receive the SonarQube Cloud notifications on your project.
{% endhint %}

To subscribe your channel to your project:

1. In SonarQube Cloud, copy your project key. See [#viewing-project-information](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects#viewing-project-information "mention").
2. In your Slack workspace, navigate to the channel in which you want to enable the subscription.
3. In the channel, type `/sonarqube subscribe <project_key>` .

### Unsubscribing a channel from a project

To unsubscribe a channel from a project, you need the Browse permission on the project in SonarQube Cloud.

{% hint style="warning" %}
Unsubscribing a channel from a project disables the subscription for all members of the channel.
{% endhint %}

To unsubscribe a channel from a project:

1. In SonarQube Cloud, copy the project key. See [#viewing-project-information](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects#viewing-project-information "mention").
2. In your Slack workspace, navigate to the channel subscribed to your project.
3. In the channel, type `/sonarqube unsubscribe <project_key>`.

### Related pages

* [integration-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/integration-overview "mention")
* [setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/setup "mention")
