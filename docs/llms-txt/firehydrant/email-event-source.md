# Source: https://docs.firehydrant.com/docs/email-event-source.md

# Email Event Source

The Email Event Source generates dynamic addresses to receive emails from your systems and create alerts. You can find and configure your email destinations in **Signals> Event Sources > Emails**.

## Creating an Email Destination

<Image alt="Creating a new Email Destination" align="center" width="650px" src="https://files.readme.io/d9424eb-CleanShot_2024-05-30_at_19.36.34.png">
  Creating a new Email Destination
</Image>

1. Click "+ Add Email Destination" at the top right of the Emails tab in Signals Event Sources.
2. On the side drawer that pops out, you'll have several fields you can fill out for this target:
   1. **Name (required)**: A descriptive name for this email target
   2. **Slug (required)**: The slug for the email address of the destination. We'll automatically generate this based on the Name above, but you can modify the slug afterward. Only alphanumeric characters and dashes are supported here
   3. **Description (required)**: A longer description for this email target
   4. **Status CEL**: A [CEL](https://docs.firehydrant.com/docs/signals-using-cel) expression that determines the alert status based on the email's content
      1. For example, you may have an expression like `email.body.contains('has recovered') ? "CLOSED" : "OPEN"` to determine if an inbound email creates a new alert or resolves an existing, open alert
   5. **Level CEL**: A [CEL](https://docs.firehydrant.com/docs/signals-using-cel) expression that determines the alert's error level based on the email's content
      1. For example, you may have an expression like `email.body.contains('panic') ? "ERROR" : "INFO"` to determine if an inbound email creates an alert that is `INFO` or `ERROR` levels
   6. **Allowed Senders**: Comma-delimited list of email addresses FireHydrant should accept emails from. Emails from other senders will be ignored. This field supports allowing all senders from specific domains as well (e.g., `@mydomain.com`).
   7. **Select notification target**: This allows setting an explicit target for the alert generated from this email. Like targeted webhooks, emails can target Escalation Policies, On-Call Schedules, Teams (and their default EPs), and Users. If this is left empty, then the inbound email will evaluate against any configured team Rules, like a normal event.
   8. **Rules (only visible when notification target selected)**: Like with Alert Triggers, these are email source rules determining whether an inbound email should raise an Alert. If you configure no rules, all inbound emails from this source will create Alerts.
3. When finished configuring the fields, click "Save." This will insert an entry into the email destinations table.Yyou can click "Copy Email" in the **Address** column for the corresponding destination to get the email address. Insert this into your external event source that is sending emails.

<Image alt="Copying the email address from the table" align="center" width="650px" src="https://files.readme.io/e961757-CleanShot_2024-05-30_at_20.03.03.png">
  Copying the email address from the table
</Image>

## Available Email Parameters

When writing the CEL statements above, these are the available parameters you can access from the email:

| Parameter       | Type                                  | Description                                                    |
| :-------------- | :------------------------------------ | :------------------------------------------------------------- |
| `email.subject` | `String`                              | The subject of the email                                       |
| `email.body`    | `String`                              | The content of the email                                       |
| `email.headers` | `Map{ key (String): value (String) }` | An object containing key-value pairs of email headers          |
| `email.from`    | `String`                              | The sender's email address                                     |
| `email.to`      | `String[]`                            | An array of destination email addresses this email was sent to |

## Deduplication Keys

Emails are deduplicated according to the target email address/event source as well as the email's subject, which is used for the *idempotency\_key* according to the [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

So if two emails come in from multiple sources with the same Subject, they won't be deduped. But if multiple emails come in targeting the same email source with the same email subject, they will be deduped.