# Source: https://resend.com/docs/dashboard/webhooks/body-parameters.md

# Body Parameters

> Complete reference for webhook body parameters, their types and meanings.

All webhook payloads follow a consistent top-level structure with event-specific data nested within the `data` object.

| Parameter    | Type     | Description                                                                      |
| ------------ | -------- | -------------------------------------------------------------------------------- |
| `type`       | `string` | The event type that triggered the webhook (e.g., `email.sent`, `domain.created`) |
| `created_at` | `string` | ISO 8601 timestamp when the webhook event was created                            |
| `data`       | `object` | Event-specific data containing detailed information about the event              |

## Email Event Payloads

Email events (`email.sent`, `email.delivered`, `email.opened`, `email.clicked`, `email.bounced`, `email.complained`, `email.failed`, `email.delivery_delayed`) share common parameters in the `data` object.

### Common Email Parameters

| Parameter      | Type     | Description                                                                                       |
| -------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `broadcast_id` | `string` | Unique identifier for the broadcast campaign (if applicable)                                      |
| `created_at`   | `string` | ISO 8601 timestamp when the email was created                                                     |
| `email_id`     | `string` | Unique identifier for the specific email                                                          |
| `from`         | `string` | Sender email address and name in the format "Name \<[email@domain.com](mailto:email@domain.com)>" |
| `to`           | `array`  | Array of impacted recipient email addresses                                                       |
| `subject`      | `string` | Email subject line                                                                                |
| `tags`         | `array`  | Array of tag objects associated with the email                                                    |

### Tag Object Structure

| Parameter | Type     | Description   |
| --------- | -------- | ------------- |
| `name`    | `string` | The tag key   |
| `value`   | `string` | The tag value |

### Event-Specific Parameters

#### Email Bounced (`email.bounced`)

Additional `bounce` object in the `data` payload:

| Parameter               | Type     | Description                                                                                                                                                                                 |
| ----------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bounce.diagnosticCode` | `array`  | Array of SMTP diagnostic responses from the receiving server, including the status code and reason for the bounce (e.g., `smtp; 550 5.5.0 Requested action not taken: mailbox unavailable`) |
| `bounce.message`        | `string` | Detailed bounce message from the receiving server                                                                                                                                           |
| `bounce.subType`        | `string` | Bounce sub-type (e.g., `Suppressed`, `MessageRejected`)                                                                                                                                     |
| `bounce.type`           | `string` | Bounce type (e.g., `Permanent`, `Temporary`)                                                                                                                                                |

#### Email Clicked (`email.clicked`)

Additional `click` object in the `data` payload:

| Parameter         | Type     | Description                                            |
| ----------------- | -------- | ------------------------------------------------------ |
| `click.ipAddress` | `string` | IP address of the user who clicked the link            |
| `click.link`      | `string` | The URL that was clicked                               |
| `click.timestamp` | `string` | ISO 8601 timestamp when the click occurred             |
| `click.userAgent` | `string` | User agent string of the browser that clicked the link |

#### Email Failed (`email.failed`)

Additional `failed` object in the `data` payload:

| Parameter       | Type     | Description                                                |
| --------------- | -------- | ---------------------------------------------------------- |
| `failed.reason` | `string` | Reason for the email failure (e.g., `reached_daily_quota`) |

## Domain Event Payloads

Domain events (`domain.created`, `domain.updated`, `domain.deleted`) contain domain configuration and DNS record information.

### Domain Parameters

| Parameter    | Type     | Description                                                                 |
| ------------ | -------- | --------------------------------------------------------------------------- |
| `id`         | `string` | Unique identifier for the domain                                            |
| `name`       | `string` | Domain name (e.g., `example.com`)                                           |
| `status`     | `string` | Current verification status of the domain (e.g., `not_started`, `verified`) |
| `created_at` | `string` | ISO 8601 timestamp when the domain was created                              |
| `region`     | `string` | AWS region where the domain is configured (e.g., `us-east-1`)               |
| `records`    | `array`  | Array of DNS record objects required for domain verification                |

### DNS Record Object Structure

| Parameter  | Type     | Description                                 |
| ---------- | -------- | ------------------------------------------- |
| `record`   | `string` | Record type purpose (e.g., `SPF`, `DKIM`)   |
| `name`     | `string` | DNS record name/subdomain                   |
| `type`     | `string` | DNS record type (e.g., `MX`, `TXT`)         |
| `value`    | `string` | DNS record value to be set                  |
| `ttl`      | `string` | Time to live for the DNS record             |
| `status`   | `string` | Verification status of this specific record |
| `priority` | `number` | Priority value for MX records (optional)    |

## Contact Event Payloads

Contact events (`contact.created`, `contact.updated`, `contact.deleted`) contain information about audience contacts.

### Contact Parameters

| Parameter      | Type      | Description                                                |
| -------------- | --------- | ---------------------------------------------------------- |
| `id`           | `string`  | Unique identifier for the contact                          |
| `audience_id`  | `string`  | Unique identifier for the audience this contact belongs to |
| `created_at`   | `string`  | ISO 8601 timestamp when the contact was created            |
| `updated_at`   | `string`  | ISO 8601 timestamp when the contact was last updated       |
| `email`        | `string`  | Contact's email address                                    |
| `first_name`   | `string`  | Contact's first name                                       |
| `last_name`    | `string`  | Contact's last name                                        |
| `unsubscribed` | `boolean` | Whether the contact has unsubscribed from the audience     |

## Best Practices

* Always validate the `type` field to determine how to process the payload
* Store `email_id` for tracking and correlation with your application data
* Use `created_at` timestamps for proper event ordering and deduplication
* Handle missing optional fields gracefully (not all events include all parameters)
* Check the `status` field in domain events to track verification progress
* Monitor bounce types and reasons to improve deliverability

Looking for request body examples? Check out the [Event Types](/dashboard/webhooks/event-types) page.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://resend.com/docs/llms.txt