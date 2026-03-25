# Source: https://plivo.com/docs/aiagent/deploy/whatsapp/template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Template Management

> Create, update, delete, and sync WhatsApp templates to enable seamless WhatsApp messaging.

A **WhatsApp template** is a pre-approved message format used by businesses to send messages through the WhatsApp Business API. Templates are necessary for sending outbound messages and ensure compliance with [WhatsApp’s Business Policy](https://business.whatsapp.com/policy). These templates are reviewed by Meta (WhatsApp) and must be approved before they can be used for messaging.

### Components of a WhatsApp Template

1. **Body**: The main content of the template where the message is written, and dynamic variables like customer names or order details can be inserted.
2. **Header**: Optional and used to include media, such as images, videos, or documents, to enhance the message content.
3. **Footer**: Optional and can be used for additional information like disclaimers or links.
4. **Buttons**: Used for interactive quick replies or call-to-action buttons, allowing customers to engage immediately.

### WhatsApp Template Review Process

After submitting a template, Meta reviews it to ensure compliance with WhatsApp’s **Business and Commerce Policies**. Meta will categorize the template based on the content. Templates can be used for **Transactional**, **Marketing**, **Authentication**, or **Service** messages.

If rejected, the template can be appealed, but Meta’s decision is final.

For more details, refer to Meta’s [Template Guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/).

### Pricing & Usage Notes

* **WhatsApp re-categorizes template types** based on their review.
* **Pricing varies by template type**, with marketing templates typically incurring higher costs.
* **Marketing messaging** has **per-user volume restrictions**.

For more details on marketing template limits, see [Per-User Marketing Template Message Limits](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Creating WhatsApp Templates on Plivo

You can create WhatsApp templates directly from **Meta Business Manager**:\
[Create WhatsApp Templates on Meta](https://business.facebook.com/latest/whatsapp_manager/message_templates).

Plivo also provides a place to create and manage WhatsApp templates, making it easier to sync your templates across platforms. Here's how:

1. **Sync Templates with Plivo**\
   Once your WhatsApp Business Account (WABA) is connected, you can sync your templates. This will bring all approved templates from Meta to your Plivo account under the connected WABA.
2. **Create WhatsApp Templates**\
   You can create new templates directly from Plivo’s interface, choosing template components like body, header, and footer, along with optional buttons. The template will then be submitted for Meta’s approval.
3. **Template Management**\
   You can also **update** and **delete** templates from Plivo’s platform, making it easy to maintain and modify your messaging templates.
4. **Template Status Sync**\
   Plivo syncs the status of your templates with Meta, meaning you can only use WhatsApp templates that have been **approved by Meta**. This ensures that you’re compliant with WhatsApp's policies.
