# Source: https://documentation.onesignal.com/docs/en/templates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Templates

> Create, personalize, send, and track reusable templates for Push Notifications, SMS, and Email in OneSignal. Save time, maintain consistency, and optimize performance.

Templates are reusable blueprints for Push Notifications, Emails, and SMS messages. They save time, ensure consistent messaging, and make personalization at scale easy. Templates are especially useful for **frequently sent**, **event-driven**, or **transactional** messages, since performance metrics are stored in one place for ongoing optimization.

<Note>
  This guide covers how to create and use templates. For details on performance tracking, see [Template Analytics](./template-analytics).
</Note>

***

## Create templates

Templates can be created in multiple ways:

<Columns cols={2}>
  <Card title="Dashboard">
    Go to **Messages > Templates** and click **New Template**.
  </Card>

  <Card title="API" href="/reference/create-template" arrow={true}>
    Create templates programmatically using the Create Template API.
  </Card>

  <Card title="Email Template Forwarding" href="./email-template-forwarding" arrow={true}>
    Migrate email templates from another email platform.
  </Card>

  <Card title="Copy Between Apps API" href="/reference/copy-template-to-another-app" arrow={true}>
    Move templates between OneSignal apps. Helpful if you have someone create the templates in another app before moving to your production app.
    **Note:** This is a one-time copy, not a live sync.
  </Card>
</Columns>

### Design guidelines

Templates support [Liquid syntax](./using-liquid-syntax) for [advanced personalization](./message-personalization), letting you insert dynamic, user-specific content.

<Note>
  Template data can be overwritten. You can use a template as a starting point and update the content on a per-message basis before sending.
</Note>

For channel-specific best practices, see:

<Columns cols={2}>
  <Card title="Push Notification Design" href="./push" arrow={true}>
    Details on push notification design, features, and creation.
  </Card>

  <Card title="SMS Messaging" href="./sms-messaging" arrow={true}>
    SMS design, features, and creation.
  </Card>

  <Card title="Email HTML Design" href="./design-emails-with-html" arrow={true}>
    Create emails with HTML.
  </Card>

  <Card title="Email Drag and Drop Design" href="./design-emails-with-drag-and-drop" arrow={true}>
    Create emails with our drag and drop editor.
  </Card>
</Columns>

***

## Send messages using templates

You can send a template in multiple ways:

* **From the Compose Screen:** When creating a new message in the Dashboard, choose to start from a template.
* **From the Templates Page:** Go to **Messages > Templates**, select **Options (3 dots) > New Message**.
* **API:** Include the `template_id` in your [send request](/reference/create-message).

### Template ID

Each template has a unique OneSignal-generated `template_id` (UUID v4). You can find it:

* Using the [View Templates API](/reference/view-templates)
* In the OneSignal Dashboard under **Messages > Templates > Options > Copy Template ID**

<Frame caption="Copy Template ID">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/templates/copy-template-id.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=b1b94df3f7ad6cdc5dc985e5c2f7ffeb" alt="Copy Template ID in OneSignal Dashboard" width="2208" height="1038" data-path="images/dashboard/templates/copy-template-id.png" />
</Frame>

***

## Track performance

The **Templates** page shows aggregate performance across all sends using the template. The data on this page is for the lifetime of the template.

For individual template performance, see [Template Analytics](./template-analytics).

| Column        | Description                                                                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**      | The template's name.                                                                                                                                                                        |
| **Labels**    | Unique [Labels](./labels) you can use to group and filter templates.                                                                                                                        |
| **Type**      | Push, Email, or SMS.                                                                                                                                                                        |
| **Last Sent** | The last date and time the template was used in a sent message.                                                                                                                             |
| **Delivered** | Push: Total of successful sends to the push services (FCM, APNs, etc.) <br />Email: Total delivered to the recipient's inbox.<br />SMS: Total of successful sends to the SMS carriers.      |
| **Opened**    | Push: Not applicable.<br />Email: Total number of times the email was opened (not unique).<br />SMS: Not applicable.                                                                        |
| **Clicked**   | Push: Total number of times the push was clicked.<br />Email: Total number of times a link within the email was clicked.<br />SMS: Total number of times a link within the SMS was clicked. |
| **CTR**       | `(Clicked ÷ Delivered) × 100%`.                                                                                                                                                             |

***

## Update templates

You can update templates via:

* **Dashboard:** Go to **Messages > Templates > Options > Edit**.
* **API:** Use the [Update Template API](/reference/update-template).

Updating templates does not affect the performance stats. New links will continue to be tracked and aggregated.

Template data can be overwritten. You can use a template as a starting point and update the content on a per-message basis before sending.

For example, if your push template has a set message and you use the [Create push API](/reference/push-notification) with new `content`, it will override the template message.

***

## Delete templates

You can delete templates via:

* **Dashboard:** Go to **Messages > Templates > Options > Delete**.
* **API:** Use the [Delete Template API](/reference/delete-template).

<Warning>
  Once the template is deleted, all data associated with it is deleted and cannot be recovered.

  You cannot delete templates used within a Journey. Either delete the Journey or remove the template from the Journey.
</Warning>

***

## FAQ

### How long is template data stored?

* Template content data is stored for the lifetime of the template until it is deleted.
* Template overview analytics found on the **Templates** page are for the lifetime of the template.
* Individual template analytics subject to your [plan type](https://onesignal.com/pricing). See [Template analytics](./template-analytics) for details.

### Can I duplicate templates across apps?

Yes:

* Use the [Copy Template to Another App API](/reference/copy-template-to-another-app) for any template type.
* For Email specifically, use [Email Template Forwarding](./email-template-forwarding).

***

Built with [Mintlify](https://mintlify.com).
