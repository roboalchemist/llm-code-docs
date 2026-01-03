# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/tracking-unsubscribes.md

# Tracking Unsubscribes

### Auto-Handling

Mailgun will automatically prevent future emails from being sent to recipients who have unsubscribed when you enable the Unsubscribe functionality by going to the settings in your domain area on the Control Panel. You can also edit the unsubscribed address list from the Control Panel or through the API.

Note:
Before enabling the Unsubscribe feature, you will need to configure the required DNS entries provided in your Control Panel.

### Unsubscribe Variables

Mailgun provides you with several unsubscribe variables:

| **Variable** | **Description** |
|  --- | --- |
| `%unsubscribe_url%` | Link to unsubscribe recipient from all messages sent by given domain. |
| `%tag_unsubscribe_url%` | Link to unsubscribe from all tags provided in the message. |
| `%mailing_list_unsubscribe_url%` | Link to unsubscribe from future messages sent to a mailing list. |


When these variables are included in your emails, any recipient who clicks on the URL will be automatically unsubscribed, and those email addresses will be blocked from receiving future emails from that domain or message tag.

Mailgun can automatically provide a customizable unsubscribe footer in each email you send. You can edit the unsubscribe footer by editing the settings in your control panel.

To enable/disable unsubscribes programmatically, you can do the following:

- Enable the Unsubscription feature for your domain.
- Remove text in the HTML and text footer so they won't be appended automatically.
- Insert a variable in the HTML and text bodies of your email when you need unsubscribe links.
  - This variable will be replaced by the corresponding unsubscribe link.


When you go to the **Suppressions** tab of the Control Panel or through the API, you can also:

- View/get a list of unsubscribed addresses
- Remove an unsubscribed address from the list
- Add a new unsubscribed address


Learn how to programmatically manage lists of unsubscribed users by visiting the Unsubscribes section of the API reference.

**Unsubscribe Webhook**

You can specify webhook URLs programmatically using Webhooks API. When a recipient unsubscribes, Mailgun will invoke the unsubscribed webhook with the following webhooks payload.