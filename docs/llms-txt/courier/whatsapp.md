# Source: https://www.courier.com/docs/external-integrations/direct-message/whatsapp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# WhatsApp

> Send WhatsApp messages via Courier using Twilio by including the recipient’s phone_number in their profile, using Twilio-approved message templates, and ensuring the content adheres to WhatsApp’s non-promotional category and verification guidelines.

Courier uses the [Twilio API for WhatsApp](https://twilio.com/whatsapp) as the delivery partner.

## Setup

You will need a [Twilio account](https://www.twilio.com/) with WhatsApp enabled. In Courier, navigate to the [WhatsApp Integration](https://app.courier.com/integrations/catalog/twilio-whatsapp) page, enter your Twilio Account SID, Auth Token, and the WhatsApp-enabled "From" number, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Twilio Whatsapp, Courier must be provided the recipient's SMS-compatible telephone number. This value should be included in the recipient profile as `phone_number`.

```json  theme={null}
{
  "message": {
    "to": {
      "phone_number": "+1555-555-5555"
    }
  }
}
```

## Notification Categories

Whatsapp allows the following [notification categories](https://www.twilio.com/docs/whatsapp/tutorial/send-whatsapp-notification-messages-templates#whatsapp-notification-categories):

* Marketing
* Authentication
* Utility

Other types of categories will likely be rejected, including:

* Account Update
* Alert Update
* Appointment Update
* Auto-Reply
* Issue Resolution
* Payment Update
* Personal Finance Update
* Reservation Update
* Shipping Update
* Ticket Update
* Transportation Update

## WhatsApp Template Verification

When using WhatsApp templates with Twilio, it's essential to understand the verification process, as WhatsApp has stringent guidelines to ensure the quality and appropriateness of messages sent through their platform.

### Create the Template

**Template Structure:** WhatsApp [message templates](https://www.twilio.com/docs/whatsapp/tutorial/send-whatsapp-notification-messages-templates) are predefined messages that can include placeholders for dynamic content. Templates can be of various types such as text, media (images, documents), or interactive messages (buttons, list messages).

**Template Categories:** These are typically [categorized](#notification-categories) into use cases like transactional updates, customer service, or alerts.

### Submit the Template for Approval

**Access Twilio Console:** Navigate to the Twilio Console and go to the Messaging section.

**Create Template:** In the WhatsApp Templates section, create a new template. You'll need to provide details like the template name, category, language, and the message content. This content should be free of any promotional material as WhatsApp strictly disallows promotional content in templates.

**Submit for Review:** Once you've filled in the necessary details, [submit](https://www.twilio.com/docs/whatsapp/tutorial/message-template-approvals-statuses) the template for WhatsApp's review.

### WhatsApp Approval Process

**Review by WhatsApp:** After submission, the template goes through WhatsApp's review process. This usually takes a few minutes to up to 24 hours. WhatsApp reviews the template to ensure it complies with their policies.

Possible Outcomes:

* **Approved:** If the template meets WhatsApp's guidelines, it will be approved. You can now use this template to send messages via the Twilio API.

* **Rejected:** If the template does not meet the guidelines, it will be [rejected](https://www.twilio.com/docs/whatsapp/tutorial/message-template-approvals-statuses#common-rejection-reasons). Reasons for rejection could include promotional content, inappropriate language, or violating other WhatsApp policies. You will need to modify the template and resubmit it for approval.

## Approved Templates with Courier

**Integration with Courier:** Once your template is approved, you can use the [Send API](/api-reference/send/send-a-message) to send messages using the Twilio approved template. You'll need to specify the [Twilio content SID](https://www.twilio.com/docs/whatsapp/tutorial/send-whatsapp-notification-messages-templates#creating-message-templates-and-submitting-them-for-approval) and paste it to a WhatsApp channel in Courier.

<Frame caption="WhatsApp Template">
    <img src="https://mintcdn.com/courier-4f1f25dc/A5Xe4OlKFUkTRiqy/assets/external-integrations/sms/whatsapp.png?fit=max&auto=format&n=A5Xe4OlKFUkTRiqy&q=85&s=df1516085cd4b21358ddb2d91113e8bc" alt="WhatsApp Template" width="1268" height="649" data-path="assets/external-integrations/sms/whatsapp.png" />
</Frame>

**Sending Messages:** When sending a message using an approved template, you make an API call with the required details. Twilio handles the rest, ensuring the message is delivered to the recipient via WhatsApp.

<Tip>
  While Twilio defines the content of your notification as a `template`, the format of your notification is what's important for the verification process. Once it's approved, you can use [Courier Templates](/platform/content/template-designer/template-designer-overview) as long as they follow the approved format design.
</Tip>

### Key Considerations

**Template Content:** Ensure that the content of your templates is clear, concise, and non-promotional. Include all necessary placeholders and provide sample values to give context during the review process.

**Localization:** If you need to send messages in multiple languages, you'll need to create and get approval for each language version of the template.

**Monitoring and Updates:** Keep an eye on the [performance](https://help.twilio.com/articles/360039737753-Recommendations-and-best-practices-for-creating-WhatsApp-Message-Templates) of your templates. If users frequently report your messages as spam, it might affect your ability to send messages. You may need to periodically update your templates to remain compliant with any new WhatsApp guidelines.

## Overrides

### Body Overrides

You can override the request body fields sent to the Twilio WhatsApp API. The `ContentSid` field is particularly useful for specifying a Twilio-approved template at send time:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+15555555555"
    },
    "providers": {
      "twilio-whatsapp": {
        "override": {
          "body": {
            "ContentSid": "HXXXXXXXXXXXXXXXXXXXXXXXXXXX"
          }
        }
      }
    }
  }
}
```

### Config Overrides

You can swap Twilio credentials or the "From" number at send time:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+15555555555"
    },
    "providers": {
      "twilio-whatsapp": {
        "override": {
          "config": {
            "accountSid": "RUNTIME_ACCOUNT_SID",
            "authToken": "RUNTIME_AUTH_TOKEN",
            "from": "+14155551234"
          }
        }
      }
    }
  }
}
```
