# Source: https://docs.firehydrant.com/docs/runbook-step-send-an-email-notification.md

# Send an Email Notification

<Image alt="Send an email notification Runbook step" align="center" width="650px" src="https://files.readme.io/d34d948-image.png">
  Send an email notification Runbook step
</Image>

Communication during incidents is crucial, and organizations use a wide array of different mediums. FireHydrant offers a Runbook step so you can notify stakeholders with information about an incident over email.

## Configuration

To add this step, Create a Runbook or Edit an existing Runbook and click "+ Add step." Search for "email" and then click on this step.

This step has several fields you can configure:

* **Email Address** - Recipient email addresses you'd like to email. Delimit multiple values with commas.
* **Email Subject** - The email's subject line (supports [Template Variables](https://docs.firehydrant.com/docs/template-variables))
* **Message Template** - The body of the email (supports [Template Variables](https://docs.firehydrant.com/docs/template-variables) as well as [Markdown](https://docs.firehydrant.com/docs/markdown-support))\*\*
* **Sender Name** - You can customize the name of the email's sender, which impacts how it appears in people's inboxes (supports [Template Variables](https://docs.firehydrant.com/docs/template-variables))

Optionally, you can also configure execution rules and conditions for the step.

> 📘 \*\*Note
>
> At this time, the Message Template does not support direct HTML.

## Runbook execution

When the Runbook step executes, it will send the configured email and message to the recipients listed. The most common use cases include:

* Automatically at incident start, notifying an email distribution list such as support team members
* When severity is critical or SEV1, notifying technical and/or executive leadership
* If a specific service is impacted (e.g., `login`), emailing the `iam-team` email distribution