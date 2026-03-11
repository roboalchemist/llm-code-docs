# Source: https://docs.axonius.com/docs/email-send-per-asset.md

# Axonius - Send Email per Asset

The **Axonius - Send Email per Asset** action sends an email to each email address in the list of recipients for:

* Assets returned by the selected query or assets selected on the relevant asset page.

To use this action, you must enable **Send Emails** setting and configure the email host and port. For more details,  see **[Configuring Email Settings](/docs/configuring-email-settings)**.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Description of Email Content

Axonius email templates summarize a query's results:

* The Enforcement Set that triggered the email, and whether the enforcement was executed automatically or by a user.
* The triggered query name and the number of previous results found, added (since last execution), and subtracted (since last execution) results, all together sum up to the total number of current results.
* Summary of the top 10 results and link to view the entire query results. When the query is created  on Activity logs and Fetch History using filters the email does not include a summary of the top 10 results.
* CSVs of the all results and/or of changes in the query results attached
  If you set [**Compress email attachments**](/docs/configuring-email-settings#general-email-configuration) on the **[Email Settings](/docs/configuring-email-settings)** page, you can send the CSV files as one compressed file. The system will warn you if the compressed file reaches 10 Megabytes.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(443\).png)

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

**Recipients** - Add list of recipients.

## Additional Fields

These fields are optional.

* **From** - Fill in the sender email address, if you want this enforcement action to send an email from a sender other than the **Sender address** configured in [Email Settings](/docs/configuring-email-settings) or the default sender address.

* **Secondary Email** - Select an email address field in a specific adapter to which this Enforcement Action sends the email, instead of the primary email address, for each user that matches the query. For example, the Okta Profile secondEmail field in the Okta adapter.

* **Email subject** - Specify the email subject.
  * If supplied, the generated email subject will be the specified subject.
  * If not supplied, the generated  email subject will be \[Enforcement Set Name] + 'for Query:' + \[query name]

* **Custom message (up to 10000 characters)** - Specify the body of the email message.
  * If supplied, the generated email body will be the specified custom message.
  * If not supplied, the email message will be generated with no body.

* **Reply To** - Fill in the recipient email address to enable sending an email reply to an email address that is different than the sender email address (and can be a no-reply email address). For example, when emailing employees about an action they need to take to secure their devices, can provide here an email address where they can open a support ticket.

* **Logo** - Upload the custom company logo so that it appears in the header of emails sent by the Enforcement Center. Make sure that the [**Custom company logo for reports and email** option](/docs/configuring-user-interface-settings) is enabled. The Axonius logo remains in the email footer.

* **Send email as plain text** *(default: False)* - Select whether to send the email as plain text. All formatting will be removed.

* **Recipients CC** - Add list of recipients CC.
  * If supplied, the email is sent as CC to the specified email list.
  * If not supplied, the email is sent only to the defined **Recipients** specified email list.

* **Include report data** *(default: True)* - Select this option to include hardcoded report data in the custom message. When this option is cleared, only the custom message is sent.

* **Plain-text email to include custom message only** *(default: False)* - Select this option to send plain-text emails with only the custom message. The following extra information is removed:
  * Enforcement Triggered
  * Custom Message
  * This message was sent by Axonius

<Callout icon="📘" theme="info">
  Note

  This option is effective only when **Send email as plain text** is enabled.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).