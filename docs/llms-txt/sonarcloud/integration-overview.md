# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/integration-overview.md

# About SonarQube Cloud integration with Slack

With the SonarQube Cloud integration with Slack, users can receive real-time notifications on analysis results directly in Slack. Currently, a notification is triggered when the quality gate status of a project’s main branch analysis transitions from Passed to Failed or from Failed to Passed.

The Slack messages contain context-rich notifications for immediate action, significantly cutting context-switching and improving code review feedback loop efficiency. Check out this [video](https://www.youtube.com/watch?v=oW-pp4LN9r0) on how to benefit from the Slack integration.

{% hint style="info" %}
Read our [privacy notice](https://www.sonarsource.com/company/privacy/) to learn how your personal data is collected, processed and stored.
{% endhint %}

### Integration overview

The SonarQube App for Slack, installed in your Slack workspace, allows the integration of SonarQube Cloud with Slack:

* SonarQube Cloud is connected at the global level to your Slack workspace.\
  A Slack workspace admin connects the Slack workspace to SonarQube Cloud. This process links their Slack account with their SonarQube Cloud account.
* Users log in to the SonarQube App for Slack by connecting their SonarQube Cloud and Slack accounts.
* Any Slack channel can be subscribed to notifications on one or several SonarQube Cloud projects distributed across different organizations:
  * The channel’s member who performs the subscription must have Browse access to the project in SonarQube Cloud.
  * All channel members receive the notifications.

<figure><img src="broken-reference" alt="The SonarQube App for Slack, installed in your Slack workspace, allows the integration of SonarQube Cloud with Slack"><figcaption></figcaption></figure>

### Integration security

SonarQube Cloud and Slack utilize OAuth 2.0 for their integration, ensuring secure data transfer. This is achieved through secure token handling, encryption, and robust access controls, all contributing to the highest security standards.

### Notification process

The notification process is as follows:

1. When an event to be notified occurs in SonarQube Cloud following the analysis of Project\_abc, SonarQube Cloud sends the event notification to the SonarQube App for Slack to be sent to each Slack channel subscribed to this project.
2. The SonarQube App for Slack forwards the messages to all subscribed channels. All channel members receive the message.

<figure><img src="broken-reference" alt="An event in SonarQube Cloud is notified in a Slack channel subscribed to the respective SonarQube Cloud project."><figcaption></figcaption></figure>

### Related pages

* [setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/setup "mention")
* [subscribing-to-slack-notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/subscribing-to-slack-notifications "mention")
