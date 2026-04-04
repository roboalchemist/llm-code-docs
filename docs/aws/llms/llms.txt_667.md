# Source: https://docs.aws.amazon.com/pinpoint/latest/userguide/llms.txt

# Amazon Pinpoint User Guide

> This is the official Amazon Web Services (AWS) user guide for Amazon Pinpoint. This documentation shows you how to use the features of Amazon Pinpoint by using the web-based AWS Management Console. Amazon Pinpoint is a customer engagement service that you can use to engage with your customers. When you use Amazon Pinpoint, you create segments that define targeted groups of customers. Next, you create campaigns that target your segments. Campaigns contain content that Amazon Pinpoint delivers to your customers using their preferred channels (such as email, SMS, or push notifications). Finally, Amazon Pinpoint provides engagement metrics that help you to track the success of your campaigns, as well as usage metrics that help you understand how customers use your apps. This documentation is offered here as a free Kindle book. You can also read it online or in PDF format at https://aws.amazon.com/documentation/pinpoint/.

- [What is Amazon Pinpoint?](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html)
- [Amazon Pinpoint end of support](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html)
- [Settings](https://docs.aws.amazon.com/pinpoint/latest/userguide/settings.html)
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/pinpoint/latest/userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/pinpoint/latest/userguide/gettingstarted.html)

- [Create a project](https://docs.aws.amazon.com/pinpoint/latest/userguide/gettingstarted-create-project.html): Get started using Amazon Pinpoint and learn how to create and configure a project.
- [Import data and create a segment](https://docs.aws.amazon.com/pinpoint/latest/userguide/gettingstarted-import-customer-data.html): Import customer information into Amazon Pinpoint and then create a targeted segment.
- [Create a campaign](https://docs.aws.amazon.com/pinpoint/latest/userguide/gettingstarted-create-campaign.html): Create an email campaign in the Amazon Pinpoint console, and schedule it to be sent at a certain time.
- [View campaign analytics](https://docs.aws.amazon.com/pinpoint/latest/userguide/gettingstarted-analytics.html): Learn how you can view campaign analytics in Amazon Pinpoint.
- [Next steps](https://docs.aws.amazon.com/pinpoint/latest/userguide/gettingstarted-next-steps.html): Learn about the next steps after you have created a project, imported the data, and viewed campaign analytics.


## [Tutorials](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials.html)

### [Using Postman with Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-using-postman.html)

Use Postman with the Amazon Pinpoint API.

- [Prerequisites](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-using-postman-prerequisites.html): Before you begin this tutorial, complete the following prerequisites:
- [Create IAM policies and roles](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-using-postman-iam-user.html): When you use Postman to test the Amazon Pinpoint API, the first step is to create a user.
- [Set up Postman](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-using-postman-configuration.html): Now that you've created a user that's able to access the Amazon Pinpoint API, you can set up Postman.
- [Send requests](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-using-postman-sample-requests.html): When you finish configuring and testing Postman, you can start sending additional requests to the Amazon Pinpoint API.

### [Set up an SMS registration system](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms.html)

SMS messages (text messages) are a great way to send time-sensitive messages to your customers using Amazon Pinpoint.

- [Prerequisites](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms-prereqs.html): Before you begin this tutorial, you have to complete the following prerequisites:
- [Set up SMS in Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms-part-1.html): Before you can set up SMS messages, you need an Amazon Pinpoint project.
- [Create IAM policies and roles](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms-part-2.html): Create IAM policies and roles for use with Amazon Pinpoint SMS
- [Create Lambda functions](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms-part-3.html): Create Lambda functions to use for Amazon Pinpoint SMS messaging.
- [Set up Amazon API Gateway](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms-part-4.html): Create a new API by using Amazon API Gateway as part of the SMS registration for Amazon Pinpoint
- [Create and deploy the web form](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms-part-5.html): Finish setting up Amazon Pinpoint for SMS messaging.
- [Next steps](https://docs.aws.amazon.com/pinpoint/latest/userguide/tutorials-two-way-sms-next-steps.html): Finish setting up Amazon Pinpoint for SMS messaging.


## [Projects](https://docs.aws.amazon.com/pinpoint/latest/userguide/projects.html)

### [Managing projects](https://docs.aws.amazon.com/pinpoint/latest/userguide/projects-manage.html)

Create, edit, and delete projects in Amazon Pinpoint.

- [Creating a project](https://docs.aws.amazon.com/pinpoint/latest/userguide/projects-manage-create.html): The procedure for creating a new project differs depending on whether your account already contains projects in the current AWS Region.
- [Editing a project](https://docs.aws.amazon.com/pinpoint/latest/userguide/projects-manage-edit.html): On the General settings page, you can configure default settings and quotas that you want to apply to campaigns and journeys in a project.
- [Deleting a project](https://docs.aws.amazon.com/pinpoint/latest/userguide/projects-manage-delete.html): If you want to remove a project from Amazon Pinpoint completely, you can delete the project by using the Amazon Pinpoint console.


## [Channels](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels.html)

### [Push notifications](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-push.html)

Learn about push notification channels in Amazon Pinpoint.

- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-push-troubleshooting.html): Learn about troubleshooting the push channel in Amazon Pinpoint.

### [Email](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email.html)

Learn about the email channel in Amazon Pinpoint.

- [Email sandbox](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-setup-production-access.html): Request email production access by opening a service quota increase with Support.

### [Setting up](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-setup.html)

Set up the email channel for Amazon Pinpoint.

- [Creating an email project](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-setup-create.html): Create an Amazon Pinpoint project that you can use to send email.
- [Verifying email identities](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html): Verify your email address or domain to enable the email channel in Amazon Pinpoint.
- [Creating an email orchestration sending role](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-orchestration-sending-role.html): Set up sending email through Amazon SES and learn how to create and delete an email orchestration sending role.
- [Monitoring](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-monitor.html): Monitor your email activity with Amazon Pinpoint.

### [Managing](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage.html)

Manage email settings with Amazon Pinpoint.

- [Updating email settings](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-update.html): In the Amazon Pinpoint console, you can enable the email channel for an existing project, or you can update the email address or domain for the email channel.
- [Managing your sending quotas](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-limits.html): Manage your email sending quota and rate by opening a request with Support.
- [Managing configuration sets](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-configuration-sets.html): Learn how to manage configuration sets, and view and apply configuration sets to an email identity.
- [Enabling and disabling the email channel](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-enable.html): Learn how to enable and disable the email channel.
- [Sending email](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-send.html): Use Amazon Pinpoint to send campaign-based and transactional emails.

### [Using dedicated IP addresses](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-dedicated-ips.html)

Describes how to use dedicated IP addresses with Amazon Pinpoint.

- [Requesting and relinquishing dedicated IPs](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-dedicated-ips-case.html): Describes how to request and release dedicated IP addresses with Amazon Pinpoint.
- [Viewing your dedicated IPs](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-dedicated-ips-viewing.html): Contains information about viewing a list of the dedicated IP addresses that are associated with your Amazon Pinpoint account.
- [Warming up dedicated IPs](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-dedicated-ips-warming.html): Describes how to warm up dedicated IP addresses with Amazon Pinpoint.
- [Creating dedicated IP pools](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-dedicated-ips-pools.html): Describes how to create dedicated IP pools.

### [Deliverability dashboard](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard.html)

Learn how to use the Amazon Pinpoint Deliverability dashboard.

- [Domain reputation](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard-domain.html): Learn about the Domain reputation page and how to use it.
- [IP reputation](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard-ip-address.html): Learn about the IP address reputation page and how to use it.
- [Bounce and complaint rates](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard-bounce-complaint.html): Learn about bounce and complaint rates and how to view metrics.
- [Campaign delivery metrics](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard-campaign-delivery.html): Learn about what kind of information is shown in the campaign delivery metrics.
- [Inbox placement tests](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard-pipt.html): Learn about the inbox placement tests page and how to create a new test.
- [Deliverability dashboard settings](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard-settings.html): Learn about the deliverability dashboard settings and how to change them.
- [Email best practices](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-best-practices.html): Learn about the best practices for sending email communications to your intended audience.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-troubleshooting.html): Learn about troubleshooting the Email channel in Amazon Pinpoint.

### [SMS](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms.html)

Learn about the SMS channel in Amazon Pinpoint.

- [Setting up](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-setup.html): Learn how to set up the SMS channel for Amazon Pinpoint.
- [Managing](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-manage.html): Manage the SMS channel in Amazon Pinpoint.
- [Message routes](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-limitations-routes.html): Learn how message routes are set when sending SMS messages using Amazon Pinpoint.
- [Message fallback](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-limitations-fallback.html): Discusses how message fallback is used when sending SMS messages using Amazon Pinpoint.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-troubleshooting.html): Learn about troubleshooting the SMS channel in Amazon Pinpoint.

### [Voice](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-voice.html)

Send voice messages to your customers over the phone by using Amazon Pinpoint.

- [Setting up](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-voice-setup.html): Set up the voice channel for Amazon Pinpoint.
- [Managing](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-voice-manage.html): Learn how you can manage the Amazon Pinpoint voice console.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-voice-troubleshooting.html): Learn about troubleshooting the Voice channel in Amazon Pinpoint.
- [In-app messages](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-inapp.html): Learn about the in-app messaging channel in Amazon Pinpoint.
- [Custom channels](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-custom.html): Use custom channels to send messages to your customers using third-party APIs.


## [Segments](https://docs.aws.amazon.com/pinpoint/latest/userguide/segments.html)

- [Building segments](https://docs.aws.amazon.com/pinpoint/latest/userguide/segments-building.html): Define and manage user segments in Amazon Pinpoint.
- [Managing segments](https://docs.aws.amazon.com/pinpoint/latest/userguide/segments-managing.html): Manage user segments in Amazon Pinpoint.
- [Importing segments](https://docs.aws.amazon.com/pinpoint/latest/userguide/segments-importing.html): Import user segments in Amazon Pinpoint.
- [Exporting segments](https://docs.aws.amazon.com/pinpoint/latest/userguide/segments-exporting.html): Export a list of segment members from Amazon Pinpoint to a file on your computer.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/segments-troubleshooting.html): This section describes how to troubleshoot importing and exporting segments.


## [Campaigns](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns.html)

- [Create a campaign](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-begin.html): Create an Amazon Pinpoint campaign.
- [Specify the segment](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-segment.html): Specify which users to reach with an Amazon Pinpoint campaign by choosing a segment.
- [Configure the message](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-message.html): Write the message for your campaign by using the Amazon Pinpoint console.
- [Schedule the campaign](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-schedule.html): Schedule when to send your Amazon Pinpoint campaign.
- [Launch the campaign](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-review.html): Review and launch your Amazon Pinpoint campaign.
- [Managing campaigns](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-managing.html): Manage your Amazon Pinpoint campaign.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-troubleshooting.html): This section describes how to troubleshoot campaigns.


## [Journeys](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys.html)

- [Take a tour of journeys](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-tour.html): Journeys includes some new concepts and terminology that you might not be familiar with.
- [Create a journey](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-create.html): Learn how to create and configure a journey.
- [Set up the journey entry activity](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-entry-activity.html): Learn how to set up the journey entry activity.
- [Add activities to the journey](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-add-activities.html): Learn how to add activities to your journey.
- [Review and test a journey](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-review-test.html): Review issues with your journey and perform a test before you publish it.
- [Publish a journey](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-publish.html): When you've tested your journey and you're ready for customers to enter it, you can publish the journey.
- [Pause, resume, or stop a journey](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-pause-stop.html): After a journey is published you can pause, resume, and stop that journey.
- [View journey metrics](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-metrics.html): Amazon Pinpoint captures metrics about journey participants and their behaviors.
- [Tips and best practices](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-best-practices.html): Consider the following tips and best practices for planning, designing, and managing a successful journey in Amazon Pinpoint.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-troubleshooting.html): This section describes how to troubleshoot journeys.


## [Test messages](https://docs.aws.amazon.com/pinpoint/latest/userguide/messages.html)

- [Sending an email message](https://docs.aws.amazon.com/pinpoint/latest/userguide/messages-email.html): Learn how to send a test email message using Amazon Pinpoint.
- [Sending a push notification](https://docs.aws.amazon.com/pinpoint/latest/userguide/messages-mobile.html): Learn how to send a test push notification using Amazon Pinpoint.
- [Sending an SMS message](https://docs.aws.amazon.com/pinpoint/latest/userguide/messages-sms.html): Learn how to send a test SMS message using Amazon Pinpoint.


## [Analytics](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics.html)

### [Chart reference](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-charts.html)

Describes the charts and metrics in Amazon Pinpoint Analytics.

- [Overview charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-overview.html): Learn about the overview charts in Amazon Pinpoint.
- [Usage charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-usage.html): Learn how to view the usage charts and metrics using Amazon Pinpoint.
- [Revenue charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-revenue.html): Learn how to view revenue charts in Amazon Pinpoint.
- [Events charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-events.html): Learn how to view the event charts in Amazon Pinpoint.
- [Demographics charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-demographics.html): Learn how to view the demographics charts in Amazon Pinpoint.
- [Campaign charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-campaigns.html): Learn how to view the campaign charts in Amazon Pinpoint.
- [Transactional messaging charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-transactional-messages.html): Learn how to view transactional messaging charts in Amazon Pinpoint.
- [Creating funnel charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-funnels.html): Use Amazon Pinpoint to create funnels, which are charts that show how many users complete each of a series of steps.
- [Streaming event data](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-streaming.html): Configure Amazon Pinpoint to stream application usage and engagement data to Amazon Kinesis.


## [Message templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/messages-templates.html)

- [Creating email templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-email.html): Create an email template for messages that you send through the email channel for Amazon Pinpoint projects.
- [Creating in-app templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html): Learn to create message templates for in-app messages that you send using Amazon Pinpoint.
- [Creating push templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-push.html): Create a template for push notifications that you send through a push notification channel for Amazon Pinpoint projects.
- [Creating SMS templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-sms.html): Create an SMS template for text messages that you send through the SMS channel for Amazon Pinpoint projects.
- [Creating voice templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-voice.html): Create a voice template for messages that you send through the voice channel for Amazon Pinpoint projects.
- [Adding personalized content](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-personalizing.html): Deliver dynamic, personalized content to message recipients by using message variables in Amazon Pinpoint message templates.
- [Using message template helpers](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-template-helpers.html): Describes the template helpers used to customize message templates in Amazon Pinpoint.

### [Managing templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing.html)

View, edit, copy, and delete message templates by using the Amazon Pinpoint console.

- [Viewing message templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-view-all.html): The Message templates page displays a list of all the message templates for your Amazon Pinpoint account in the current AWS Region.
- [Opening a message template](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-open.html): By using the Message templates page, you can quickly find and open a specific message template to view the contents of the template and information about the template.
- [Editing a message template](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-edit.html): You can open a message template for editing in two ways: while you're authoring a message that uses the template, and by using the Message templates page.
- [Copying a message template](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-copy.html): To quickly create a new message template that's similar to an existing template, you can create a copy of the template.
- [Deleting a message template](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-delete.html): If you want to remove a message template from Amazon Pinpoint completely, you can delete the template.
- [Adding a tag to a template](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-add-tag.html): A tag is a label that you can define and associate with AWS resources, including certain types of Amazon Pinpoint resources.
- [Removing a tag from a template](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-remove-tag.html): If you no longer need a tag to apply to a template, you can remove it through the console.
- [Managing template versions](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-versioning.html): View, edit, and manage versions of message templates by using the Amazon Pinpoint console.


## [Machine learning models](https://docs.aws.amazon.com/pinpoint/latest/userguide/ml-models.html)

- [How recommendations work](https://docs.aws.amazon.com/pinpoint/latest/userguide/ml-models-rm-how-it-works.html): Learn how Amazon Pinpoint works with recommender models to add personalized recommendations to messages.
- [Preparing to use recommendations](https://docs.aws.amazon.com/pinpoint/latest/userguide/ml-models-rm-prerequisites.html): Learn what steps to take before you configure Amazon Pinpoint to connect to and use recommendations from a recommender model.
- [Setting up recommendations](https://docs.aws.amazon.com/pinpoint/latest/userguide/ml-models-rm-setup.html): Learn how to configure Amazon Pinpoint to retrieve recommendations from a recommender model.
- [Using recommendations in messages](https://docs.aws.amazon.com/pinpoint/latest/userguide/ml-models-rm-using.html): Learn how to add dynamic, personalized recommendations to messages by using message variables in Amazon Pinpoint message templates.
- [Managing machine learning models](https://docs.aws.amazon.com/pinpoint/latest/userguide/ml-models-managing.html): View, edit, copy, and delete settings for integrating machine learning models with Amazon Pinpoint.


## [Monitoring](https://docs.aws.amazon.com/pinpoint/latest/userguide/monitoring.html)

- [Exported metrics](https://docs.aws.amazon.com/pinpoint/latest/userguide/monitoring-metrics.html): Learn about Amazon Pinpoint metrics that are exported to CloudWatch.
- [View Amazon Pinpoint metrics](https://docs.aws.amazon.com/pinpoint/latest/userguide/monitoring-view-metrics.html): Learn how to view Amazon Pinpoint metrics in CloudWatch.
- [Create CloudWatch alarms](https://docs.aws.amazon.com/pinpoint/latest/userguide/monitoring-create-alarms.html): TBD
