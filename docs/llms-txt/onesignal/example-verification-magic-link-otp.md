# Source: https://documentation.onesignal.com/docs/en/example-verification-magic-link-otp.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send verification, magic link, OTP, and double opt-in messages

> Examples of email and SMS verification messages using OneSignal, including one-time passwords, magic links, and double opt-in flows with templates and API examples.

Whether you need account authentication, registering new users/passwords, or confirming a transaction, you sometimes just need to send a one-time password, magic link, or registration URL to someone. Email verification is a good example and a way to prevent fake or inactive email addresses. Following this guide will help make sure your users can actually receive the emails you send while also increasing your sender's reputation and deliverability.

## Requirements

* A server to generate and send the OTP or confirmation code.

## Sending `custom_data` through the API

Our [Create message API](/reference/create-message) has the `custom_data` property which you can use to pass data from your server into the message.

Depending on how you generate the confirmation code, magic link, or custom URL, once you do, you can pass it into the `custom_data` object when sending a message to your users. For example:

<CodeGroup>
  ```Text JSON theme={null}
  "custom_data": {
      "user": {
          "first_name": "George"
      },
      "verify": {
          "URL" : "https://yourdomain.com/users/confirm?confirmation_token=OS4EVA",
          "otp" : "OS4EVA"
      }
  }
  ```
</CodeGroup>

## Verification Email Template

This email template example will demonstrate how to display the user's name, a one-time passcode, and a button with a link to confirm their email address.

<Frame caption="Verification email example">
    <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e653d20-Screenshot_2023-08-28_at_3.07.09_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=8633ab043badb9bf58acb90ef326052c" alt="" width="649" height="729" data-path="images/docs/e653d20-Screenshot_2023-08-28_at_3.07.09_PM.png" />
</Frame>

### Email Template Setup

Navigate to **Messages > Templates > New Email Template** and use the **Drag & Drop Editor**.

Create 1 row and drag in the following blocks:

* **Title** block
* **Paragraph** block
* **Button** block

<Frame caption="Drag and Drop editor example">
    <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/eaf02d3-Screenshot_2023-08-28_at_2.46.21_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=bebf50444f6d7733961279be58712871" alt="" width="859" height="209" data-path="images/docs/eaf02d3-Screenshot_2023-08-28_at_2.46.21_PM.png" />
</Frame>

### Display user's name in email

This is optional, but you can make the message more personalized by adding the user's name. If you may not have the name, you can omit it or set a default.

Within our template **Title** block, set your copy as desired. Example:

```
Hey {{ message.custom_data.user.first_name | default: "there" }},
```

### Display one-time password in email

This example shows both the option to send a one-time password and a button with confirmation URL. Depending on how you want to setup, set your copy within the **Paragraph** block as desired. Example:

```
To join the squirrel crew, verify your email with the One Time Password:
{{message.custom_data.verify.otp}}

Or use the link below!
```

You can use more than one **Paragraph** or **Text** blocks if you want to make the password larger or distinct from the text. In this example, we made it bold:

<Frame caption="OTP styled in bold within the email content">
    <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f534afb-Screenshot_2023-08-28_at_3.05.35_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=9ebc5e94bdc7afad54e0a39ffd994f0f" alt="" width="566" height="199" data-path="images/docs/f534afb-Screenshot_2023-08-28_at_3.05.35_PM.png" />
</Frame>

### Add a custom URL in email

There are several ways to setup the verification URL. In this example we pass in the full URL with confirmation code to `custom_data`.

In the **Button** block > Content Properties > Action > Url, set:

* `{{message.custom_data.verify.URL}}`

<Frame caption="Custom URL setting in Button block">
    <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/075aacf-Screenshot_2023-08-28_at_3.06.14_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=34a80930c78a39d662dcf787677e565f" alt="" width="1185" height="624" data-path="images/docs/075aacf-Screenshot_2023-08-28_at_3.06.14_PM.png" />
</Frame>

## Update the email template and send the message

See [Design Emails with Drag and Drop](./design-emails-with-drag-and-drop) for more details on customizing the template.

Example API request JSON:

<CodeGroup>
  ```Text JSON theme={null}
  {
      "include_email_tokens": [
          "Email Address"
      ],
      "app_id": "YOUR_APP_ID",
      "template_id": "YOUR_TEMPLATE_ID",
      "custom_data": {
          "user": {
              "first_name": "George"
          },
          "verify": {
              "URL" : "https://yourdomain.com/users/confirm?confirmation_token=OS4EVA",
              "otp" : "OS4EVA"
          }
      }
  }
  ```
</CodeGroup>

<Check>
  When ready, you can use the `template_id` within your [Create notification](/reference/create-message) API requests with `custom_data` property.
</Check>

## Verification SMS Template

This SMS template example will demonstrate how to display a one-time passcode.

### SMS Template Setup

SMS should only be sent with a limited amount of data to reduce charges.

Navigate to **Messages > Templates > New SMS Template**.

Name the template something memorable like `OTP Template`.

### Display OTP in SMS template

In the template **Message** field, add the following copy:

* `{{message.custom_data.verify.otp}} is your OneSignal verification code.`

We recommend changing "OneSignal" to the name of your app.

### Update the SMS template and send the message

Once you have the template created, you can generate your one time passwords and pass them to OneSignal using the following example API request JSON:

<CodeGroup>
  ```Text JSON theme={null}
  {
      "include_phone_numbers": ["+19999999999"],
      "app_id": "YOUR_APP_ID",
      "template_id": "YOUR_TEMPLATE_ID",
      "custom_data": {
          "verify": {
              "otp" : "OS4EVA"
          }
      }
  }
  ```
</CodeGroup>

<Check>
  When ready, you can use the `template_id` within your [Create notification](/reference/create-message) API requests with `custom_data` property.
</Check>

## Setting Up Email Double Opt-In

Double opt-in is a process that requires users to confirm their email subscriptions to enhance email list quality and comply with regulations.

### 1. Adding Email Addresses to OneSignal

When adding email addresses to OneSignal, they are automatically subscribed by default. However, for double opt-in, refrain from [adding users via our Create user API](/reference/create-user) until they click the verification link sent via email.

### 2. Sending Verification Emails

OneSignal allows you to send verification emails to recipients using our [Create notification API](/reference/create-message). The endpoint will send the email and add the address to OneSignal as an email subscription if it doesnt already exist in the app.

#### API Endpoint: Sending a Verification Email

* Utilize the [Create notification endpoint](/reference/create-message) to create and send a [verification email](./example-verification-magic-link-otp) to the recipient.

### 3. Handling Verification Responses

Depending on the recipient's response to the verification link, follow these steps:

**For Non-Subscribers**

1. Target the email recipient with a custom data notification via our [Create notification API](/reference/create-message).
2. If the user clicks the verification link, use the API's "[Create user](/reference/create-user)" endpoint to add them as a subscription.

**For Existing Subscribers**

1. Target existing subscribers separately with a verification email.
2. Monitor the recipients' responses to the verification link over a predefined period.

**If They Don't Respond**

* [Update the subscription](/reference/update-subscription) to unsubscribe or [delete it altogether](/reference/delete-subscription) via the API.

**If They Click the Verification Link**

* Do nothing - they are already subscribed to OneSignal.

### In summary, setting up double opt-in with OneSignal involves the following steps

#### For Email Addresses Not Currently in Your Audience

1. Send a verification email to the recipient via the API.
2. If the recipient clicks the verification link, use the "create user" API endpoint to create the subscription.

#### For Email Addresses Already in OneSignal

1. Send a verification email to existing subscribers via the API.
2. Monitor their response to the verification link.
3. If they don't respond within a specified period, update their subscription to unsubscribe or delete it.
4. If they've clicked the verification link, take no action as they are already subscribed.

By following these steps, you can effectively implement double opt-in functionality in your email subscription process while ensuring compliance and maintaining a high-quality email list.

***

Built with [Mintlify](https://mintlify.com).
