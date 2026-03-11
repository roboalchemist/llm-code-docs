# Source: https://docs.axonius.com/docs/send-email-to-entities.md

# Axonius - Send Email to Assets

**Axonius - Send Email to Assets**  sends an email with a predefined subject and body to all assets which have an email address, based on the following logic:

* Users query - Email will be sent to each User asset which has an email address.
* Devices query - Email will be sent to each User asset which has an email address that is determined as the **Latest Used User Email** for each device.

<Callout icon="📘" theme="info">
  Note

  The count returned from this action tells you the number of users emails were sent to for each device.
</Callout>

To use this action, you must enable the 'Send Emails' setting and configure the email host and port. For more details, see [Configuring Email Settings](/docs/configuring-email-settings).

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

1. **Email subject** *(default: empty)* - Specify the email subject.
   * If supplied, the generated email subject will be the specified subject.
   * If not supplied, the email subject will be \[Enforcement Set Name] + 'for Query:' + \[query name]
2. **Customize recipients for device entities** - Select one of these options:
   * 'Send to Owner Only' - Select whether to send an email to the device owner.   If enabled, an email will be sent to the email address of the device owner, if it exists. Otherwise an email will be sent to each User asset which has an email address that is determined as the **Latest Used User Email** for each device.
   * 'Custom' - Select custom recipients to send the mail to, checkboxes are displayed, and you can choose 'Add device owner to recipients', and/or  'Add device latest used user email to recipients'
   * 'Send to AWS account administrators' - Select the option to send an email to users that are an admin in the accounts where the devices exist, in this case it adds   `{{ASSETS_PER_ASSOCIATION}}` to the Cusom message field and lists there the AWS ARNs per account.
   * 'Send to GCE account administrators'  - Select this option to send an email to users that are owners in the projects where the devices exist. To add the names of the devices by projects to the email add the following `{{ASSETS_PER_ASSOCIATION}}`. Note that *Fetch IAM permissions for users*  must be enabled in the GCP adapter in order for this to work.
3. **Limit recipients to first X, not counting CC** - Limit the number of recipients to only send to the first X recipients, based on the default order of recipients. The default value is 2. For a Devices query, the default order of email recipients is:

* Device Owner (if  **Add device owner to recipients**  is selected)

* Latest Used User Email (if **Add latest used user email to recipients** is selected)

* device.mail

* device.custom\_email

* device.email

* all of device.last\_used\_users\_mail\_association (that one is a list)

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Additional Fields

These fields are optional.

* **From** - Fill in the sender email address, if you want this enforcement action to send an email from a sender other than the **Sender address** configured in [Email Settings](/docs/configuring-email-settings) or the default sender address.
* **Custom message** *(default: empty)* - Specify the body of the email message.
  * If supplied, the generated email body will be the specified custom message.
  * If not supplied, the email message will be generated with no body.
* **Reply-To** - Fill in the recipient email address to enable sending an email reply to an email address that is different than the sender email address (and can be a noreply email address). For example, when emailing employees about an action they need to take to secure their devices, can provide here an email address where they can open a support ticket.
* **Logo** - Upload the custom company logo so that it appears in the header of emails sent by the Enforcement Center. Make sure that the [**Custom company logo for reports and email** option](/docs/configuring-user-interface-settings) is enabled. The Axonius logo remains in the email footer.
* **Send as plain text** - (default: False) - Select this checkbox to send the email as plain text. All formatting will be removed.
  * When not selected, the email will be formatted with HTML.
* **Send only custom message** - Select this checkbox to include only the custom message's content in the email.
* **Confirm only send to device owner** (and cc list) - Send the email only to the owner of the device and not to the Latest Used User Email. When **Send to Owner Only** is selected as well as  **Confirm only send to device owner (and CC list)**, then the recipients list will ONLY include the device.owner (and any CC emails configured in the enforcement set).
* **Email CC list** ' - Specify a comma-separated list of email addresses.
* If supplied, each email will also be sent to the supplied email addresses in that list.
* If not supplied, each email will only be sent to each User asset which has an email address that is determined as the **Latest Used User Email** for each device.
* **Secondary Email** - Select an email address field in a specific adapter to which this Enforcement Action sends the email, instead of the primary email address, for each user that matches the query. For example, the Okta Profile secondEmail field in the Okta adapter.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).