# Source: https://documentation.onesignal.com/docs/en/transactional-messages.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transactional messages

> Learn how to send transactional messages like OTPs, billing updates, and reminders using OneSignal’s API with personalized data via push, email, or SMS.

Sending timely and personalized messages to individuals or small groups is critical to delivering a strong customer experience and maintaining engagement. Transactional messages—such as One-Time Passcodes (OTPs), billing updates, or activity confirmations—allow you to share meaningful, real-time updates from your server.

This guide explains how to send transactional messages (push, email, or SMS) with OneSignal's API using custom data and user identifiers.

***

## Common use cases

Use transactional messages to:

* Send login and verification codes (OTP)
* Confirm orders, receipts, or subscription changes
* Deliver billing status or renewal alerts
* Remind users about appointments or deadlines
* Acknowledge key actions (e.g. signups or purchases)

***

## Requirements

Before sending transactional messages, we suggest reviewing the following guides:

* Understand OneSignal [Users](./users), [Subscriptions](./subscriptions), and [Aliases](./aliases).
* Setup your [Database, DMP, or CRM to communicate with OneSignal](./database-dmp-crm-integration) or use one of our [Integrations](./integrations).
* Create [Templates](./templates) to personalize your messages.
* Use [Liquid Syntax](./using-liquid-syntax) to personalize your messages.

***

## Identifying users

To target individual users, you must identify them within OneSignal. The recommended approach is to set an **External ID**, which should map to the user identifier used in your database or CRM.

OneSignal also supports up to **20 aliases per user**, enabling you to associate multiple identifiers (e.g., `other_user_id`, `facebook_id`, etc.) across your systems. For email and SMS, you can also send messages directly using the email address or phone number respectively.

***

## Targeting users

Use the [Create Message API](/reference/create-message) to send transactional messages across push, email, and SMS channels by targeting users via aliases, email addresses, phone numbers, or subscription IDs.

### Send to aliases (recommended)

Use `include_aliases` to target the recommended `external_id` or other aliases like so:

<CodeGroup>
  ```json external_id theme={null}
  {
    "app_id": "YOUR_APP_ID",
    "include_aliases": {"external_id": ["userA", "userB"]},
    "contents": {"en": "English Message"},
    "target_channel": "push"
  }
  ```

  ```json custom_alias theme={null}
  {
    "app_id": "YOUR_APP_ID",
    "include_aliases": { "alias_label": ["alias_id_1", "alias_id_2"] },
    "contents": { "en": "English Message" },
    "target_channel": "email"
  }
  ```

</CodeGroup>

### Send to subscriptions

If you want to send to specific Subscriptions, you can use the `include_subscription_ids` property. This option is not recommended because Users can have multiple Subscriptions.

```json  theme={null}
{
  "app_id": "YOUR_APP_ID",
  "include_subscription_ids": ["1dd608f2-c6a1-11e3-851d-000c2940e62c"],
  "contents": { "en": "English Message" }
}
```

### Send to email addresses

If you have the user's email address, you can send emails to them using the `include_email_tokens` property.

Any emails included that do not exist within your OneSignal app will automatically create a new email subscription.

```json  theme={null}
{
  "app_id": "YOUR_APP_ID",
  "include_email_tokens": ["user1@email.com", "user2@email.com"],
  "email_subject": "Welcome to Cat Facts!",
  "email_body": "<html><head>Welcome to Cat Facts</head><body><h1>Welcome to Cat Facts</h1><h4>Learn more about everyone's favorite furry companions!</h4><hr/><p>Hi Nick,</p><p>Thanks for subscribing to Cat Facts! We can't wait to surprise you with funny details about your favorite animal.</p><h5>Today's Cat Fact (March 27)</h5><p>In tigers and tabbies, the middle of the tongue is covered in backward-pointing spines, used for breaking off and gripping meat.</p><a href='https://catfac.ts/welcome'>Show me more Cat Facts</a><hr/><p><small>(c) 2018 Cat Facts, inc</small></p><p><small><a href='[unsubscribe_url]'>Unsubscribe</a></small></p></body></html>"
}
```

### Send to phone numbers

If you have the user's phone number, you can send them SMS and MMS using the `include_phone_numbers` property.

Any phone numbers included that do not exist within your OneSignal app will automatically create a new SMS subscription.

```json  theme={null}
{
  "app_id": "YOUR_APP_ID",
  "include_phone_numbers": ["+15555555555"],
  "contents": { "en": "English Message" }
}
```

***

## Adding custom data

For personalized content, pass user-specific `custom_data` to the message using Templates and Liquid syntax.

Steps to add custom data:

1. Create a [Template](./templates) via the dashboard or [Create template API](/reference/create-template).
2. Add [Liquid Variables](./using-liquid-syntax) (e.g., `{{ message.custom_data.order_id }}`) to your template.
3. Reference the `template_id` and `custom_data` within your Create Message API call.

```json  theme={null}
{
  "app_id": "YOUR_APP_ID",
  "include_aliases": { "external_id": ["userA"] },
  "template_id": "8458af75-4da2-4ecf-afb5-f242a8926cc3",
  "custom_data": { "order_id": 123, "currency": "USD", "amount": 25 }
}
```

### Example: One-Time Passcode (OTP)

1. Identify the user using an alias, email, or phone number.
2. Create a Template that includes a verification code:

```
Your verification code is {{ message.custom_data.verification_code }}
```

1. Generate the `verification_code` on your server when the user requests access.
2. Input the `verification_code` value into the API request.

```json  theme={null}
{
  "app_id": "YOUR_APP_ID",
  "include_aliases": { "external_id": ["userA"] },
  "template_id": "8458af75-4da2-4ecf-afb5-f242a8926cc3",
  "custom_data": { "verification_code": "123456" }
}
```

**Alternative:** If you don't want to use templates and `custom_data` you can input the variable value directly into the message with string concatenation. For example:

```json  theme={null}
{
  "app_id": "YOUR_APP_ID",
  "include_aliases": {"external_id": ["userA"]},
  "contents": {"en": "Your verification code is " + verification_code}
}
```

***

## Troubleshooting

* For `include_aliases`, the alias must be registered on the user beforehand.
* For email/SMS, ensure correct formatting.

***

## Additional Resources

* [Create message guide](/reference/create-message)
* [Users](./users) and [Aliases](./aliases)
* [Templates](./templates) and [Liquid Syntax](./using-liquid-syntax)
* [Rate Limits](/reference/rate-limits)

***

Built with [Mintlify](https://mintlify.com).
