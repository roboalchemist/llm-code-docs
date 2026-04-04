# Source: https://docs.getint.io/getintio-platform/notifications.md

# Notifications

Getint’s notification system bridges the gap between various applications, ensuring a smooth user experience by delivering alerts through a range of customizable channels. These channels include Custom SMTP (Email), Email (sent by Getint Cloud), Slack, and Webhook. Users can select their preferred notification method, which allows them to stay informed in a way that best suits their workflow.

Whether you want to be alerted about failed tasks, warnings, or missing configuration details, Getint's notification system ensures timely issue detection and prompt resolution, keeping your integrations running smoothly.

### How to Set Up Notifications for Your Getint Integration <a href="#how-to-set-up-notifications-for-your-getint-integration" id="how-to-set-up-notifications-for-your-getint-integration"></a>

Setting up notifications in Getint is a straightforward process. Follow these steps to create and customize alerts for your integrations:

#### 1. Access the Notifications Section <a href="#id-1.-access-the-notifications-section" id="id-1.-access-the-notifications-section"></a>

* Navigate to the **Notifications** section within **Workflows** and click on **+ Create Alert**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsRlgJ6d0eijxef33DCym%2FNotifications%20feature.png?alt=media&#x26;token=5e9cbc95-d4c8-482d-9567-58315a98a57c" alt=""><figcaption></figcaption></figure>

#### 2. Configure Your Alert Settings <a href="#id-2.-configure-your-alert-settings" id="id-2.-configure-your-alert-settings"></a>

* **Name Your Alert**: Give your alert a descriptive name to help you easily identify it later.
* **Select Notification Types**: Choose which events you want to receive alerts for. Available options include:
  * **Failed runs**
  * **Failed syncs**
  * **Warning logs**
  * **Missing options mappings**
  * **Integration configuration changes** **(possible only via mail or Slack)**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOZGk6qkrriGTOWiUacPL%2FCreating%20an%20alert%20for%20notifications.png?alt=media&#x26;token=400b3b66-a9de-4d8a-9ae9-9b28df4cab74" alt=""><figcaption></figcaption></figure>

#### 3. Choose Your Integrations <a href="#id-3.-choose-your-integrations" id="id-3.-choose-your-integrations"></a>

* Choose the integrations where notifications should be applied. If none are selected, they will automatically apply to all integrations.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbIXNFi2lKwcYfaUHMdJO%2FSelecting%20the%20integrations%20to%20receive%20notifications%20from%20them.png?alt=media&#x26;token=7a21da23-f1ec-407e-925e-27183200232e" alt=""><figcaption></figcaption></figure>

#### 4. Choose Your Notification Channel <a href="#id-3.-choose-your-notification-channel" id="id-3.-choose-your-notification-channel"></a>

* You can select from four notification channels: **Custom SMTP (Email), Email (sent by Getint Cloud), Slack, or Webhook**. Here’s a breakdown of each option:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0ck7aOHASws2hKaid4DD%2FChannels%20to%20receive%20notifications.png?alt=media&#x26;token=86508cc3-b105-4228-a0aa-9afea246204a" alt=""><figcaption><p>Here’s a breakdown of each option</p></figcaption></figure>

### Configuring Notification Channels <a href="#configuring-notification-channels" id="configuring-notification-channels"></a>

#### 1. Custom SMTP (Email) <a href="#id-1.-custom-smtp-email" id="id-1.-custom-smtp-email"></a>

Custom SMTP emails are emails sent using a specific SMTP (Simple Mail Transfer Protocol) server that you configure yourself. Unlike standard email services where the provider controls the server settings, custom SMTP allows you to use your own server to send emails. This can provide greater control over email delivery, improve security, and ensure compliance with your specific requirements.

To configure Custom SMTP, you need to provide the following details:

* **SMTP Host**
* **SMTP Port**
* **SMTP Username**
* **SMTP Password**
* **SSL and/or StartTLS**
* **From Address** (email address of the sender)
* **Recipients** (comma-separated email addresses)
* **Subject prefix**

Once these details are filled in, use the **Send test email** button to confirm that everything is set up correctly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlkIL8JInd3uO7hnzYhaC%2FCustom%20SMTP%20(EMAIL).png?alt=media&#x26;token=bc093951-13e1-4469-a414-639b965a089c" alt=""><figcaption></figcaption></figure>

#### 2. Email (Sent by Getint Cloud) <a href="#id-2.-email-sent-by-getint-cloud" id="id-2.-email-sent-by-getint-cloud"></a>

This simple option enables users to receive notifications directly from Getint’s internal servers with minimal setup required. Just provide the following:

* **Recipients** (comma-separated email addresses)
* **Subject prefix**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPJrSDWZazTrEyq5oWo0B%2FEmail%20sent%20by%20Getint%20Cloud.png?alt=media&#x26;token=29aad8a5-e169-4a2b-a4a0-90ce7602efcc" alt=""><figcaption></figcaption></figure>

This channel is ideal for users who want quick and efficient notifications without additional configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXek1BsSXQCIhIiRtX0mN%2FGmail%20notifications%20for%20errors%20with%20your%20Getint%20instance.png?alt=media&#x26;token=802e04f8-5863-4047-8400-2cef20f66b20" alt=""><figcaption><p>Here’s an example of how email alerts are sent from our servers</p></figcaption></figure>

{% hint style="info" %}
Note that this option is only available for Jira Cloud apps.
{% endhint %}

#### 3. Slack <a href="#id-3.-slack" id="id-3.-slack"></a>

Slack is an excellent choice for teams looking for instant communication. Notifications can be set up using **Slack webhooks**, sending alerts directly to designated channels. This keeps your team informed and responsive, without leaving the app. Incorporating Slack into your notification setup allows for efficient, instant alerts, keeping your team synchronized and responsive.

To configure Slack notifications:

* **Provide the Webhook URL**: Follow the in-app guide to create a Slack webhook. You can also access this guide directly [here](https://api.slack.com/messaging/webhooks).
* **Configure your Slack workspace** to ensure real-time alerts are sent to the right Slack channels.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtCV9AYhamgPISALkcX98%2FSlack%20notifications.png?alt=media&#x26;token=41f5dbe0-77ea-4e10-80c4-6fa875f764dd" alt=""><figcaption></figcaption></figure>

Alerts are delivered automatically, keeping all authorized Slack users informed of any errors and eliminating the need for manual monitoring. This enhances the workflow's efficiency and significantly improves turnaround times.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGfyNF5rOxTgnIaAbTiA4%2FSlack%20notifications%20example.png?alt=media&#x26;token=652b3ed8-5136-4c36-b08d-3b385fb50f4c" alt=""><figcaption><p>Example of how Slack notifications are delivered</p></figcaption></figure>

#### 4. Webhooks <a href="#id-4.-webhooks" id="id-4.-webhooks"></a>

Webhooks are a powerful and flexible way to send real-time notifications to external systems. They enable your application to communicate with other services by sending HTTP requests to a specified URL whenever an event occurs. Unlike traditional polling, where an external system would check for updates periodically, webhooks push data instantly to a designated endpoint, making them more efficient for real-time integration.

When setting up webhook alerts in Getint, you will need the following details:

* **Webhook URL**: This is the endpoint where the notifications will be sent. The receiving service must be configured to accept the incoming HTTP requests.
* **Webhook Body (JSON format)**: The payload sent with the HTTP request is typically in JSON format and contains relevant details about the triggered event. You can customize the structure of the JSON to include the data you need.

The Webhook JSON body could be structured as follows:

`{"failedSynces": "${failedSyncs}", "failedRuns": "${failedRuns}", "timestamp": "${timestamp}"}`

* **Header Name** and **Header Value**: Custom headers may be required for authentication or other purposes. You can configure these to ensure that the receiving service can identify and validate the requests.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxtyAUy06V54cGaR9iGlX%2FWebhook%20alerts.png?alt=media&#x26;token=d48473d4-67af-406d-abcc-295240e66d89" alt=""><figcaption><p>With the flexible configuration in Getint, webhooks are a versatile tool that can integrate seamlessly with your existing systems, ensuring that your workflows are efficient and your processes are connected</p></figcaption></figure>

For more information on Webhooks and their configuration, please reach out to our [Support Center](https://getint.io/help-center). At Getint, we're always happy to assist you!

### Finalizing Your Notification Setup <a href="#finalizing-your-notification-setup" id="finalizing-your-notification-setup"></a>

After configuring your alert and choosing a channel, click **Create** at the bottom right of the screen to save it. Your new alert will now appear in the **Notifications** menu, where you can manage its settings.

You can edit, disable, or delete an alert by clicking the three-dot menu under **Actions**. When editing an alert, you can modify all fields except the **notification channel**, allowing you to adjust your alert settings as needed. You can also update the integration list by adding more integrations or removing selected ones to apply notifications to all integrations.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhxhMedLPEeCy6vfVu6Ze%2FActions%20for%20the%20newly%20created%20alert.png?alt=media&#x26;token=7a27bc12-0ade-4e16-946c-704c736032f4" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This feature is designed exclusively to receive notifications about errors or configuration changes in your integration. As a result, it ensures your integration remains operational and free of issues.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

The notifications feature in Getint provides a robust solution for monitoring integrations, ensuring that users receive timely updates through their preferred channels. Whether you choose to receive alerts via email, Slack, or Webhooks, the system's flexibility allows for a tailored notification experience that helps maintain operational efficiency.

If you’re experiencing issues with your notifications or you have any other questions, feel free to reach out to us at our [Support Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FO3FVs0hhldDtI43NPHAq%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=8d4a4c63-7894-466e-b0c1-a7867df6c503" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
