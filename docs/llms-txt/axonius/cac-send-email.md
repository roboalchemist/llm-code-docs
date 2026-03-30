# Source: https://docs.axonius.com/docs/cac-send-email.md

# Cloud Asset Compliance - Send Email

The **Send Email** action sends the CSV with the filtered compliance results by email to a specified recipient list.

To configure the **Send Email** action, in the **Cloud Asset Compliance** page, click the **Enforce** menu, and select **Send Email**.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1041\).png)

## Connection Settings

To use this action, you must enable the **Send Emails** setting and configure the email host and port. For more details, see [Configuring email settings](/docs/configuring-email-settings).

## Action Settings

1. **Email subject** *(required, default: empty)* - Specify the email subject.
2. **Custom message (up to 200 characters)** *(optional, default: empty)* - Specify the body of the email message.
   * If supplied, the generated email body will be the specified custom message.
   * If not supplied, the email message will be generated with no body.

<Callout icon="📘" theme="info">
  NOTE

  * The following parameters can be used in the email subject and the message/body:

  * \{\{USERNAME}} - The username of the user.

  * \{\{FIRST\_NAME}} - The user's first name.

  * This field allows unsanitized HTML code.
</Callout>

3. **Send to AWS account admins** *(required, default: False)*
   * Adds to the list of recipients, emails of IAM users which have the Administrator Access role and that these users are part of the AWS Account.
   * Relevant only for CIS Amazon Web Services Foundations Benchmark
4. **Recipients** *(required, default: empty)* - Add list of recipients.
5. **Recipients CC** *(optional, default: empty)* - Add list of recipients CC.
   * If supplied, the email will be sent as CC to the specified email list.
   * If not supplied, the email will be sent only to the defined **Recipients** specified email list.