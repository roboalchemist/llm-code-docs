# Source: https://plivo.com/docs/messaging/concepts/whatsapp/prerequisites.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Prerequisites for integrating WhatsApp with Plivo for messaging

> Meet the requirements to integrate WhatsApp messaging with Plivo APIs

You must meet several prerequisites before you can integrate WhatsApp with Plivo and start using our Messaging API.

## Meta Business Suite

You must have an active [Meta Business Suite](https://www.facebook.com/business/tools/meta-business-suite?content_id=RSnQo4HygrPVv5N\&ref=sem_smb\&utm_term=meta%20business%20suite\&gclid=EAIaIQobChMIw62j85__gAMVC0J9Ch1IMwVMEAAYASAAEgIJj_D_BwE) account to engage with Meta’s products, including WhatsApp. If you don’t have one yet, set one up through Meta Business Suite \[Recommended method] or using the [embedded signup](https://developers.facebook.com/docs/whatsapp/embedded-signup/#the-new-embedded-signup-flow) in the [Plivo console](https://cx.plivo.com/whatsapp/numbers) — learn how in [our guide](/messaging/concepts/whatsapp/waba-onboarding/). We also strongly recommend that you [verify your business details with Meta](https://www.facebook.com/business/help/1095661473946872?id=180505742745347) to improve the chances that your WhatsApp Business Account (WABA) is approved and to get higher [messaging limits](https://developers.facebook.com/docs/whatsapp/messaging-limits/).

## Admin rights

You must have access to the credentials of a Meta account that’s also an admin user in your Meta Business Account.

## WhatsApp Business Account (WABA)

You need an active WABA that is mapped to Plivo to start sending messages. Use the embedded signup flow in the [Plivo Console](https://cx.plivo.com/whatsapp/numbers) to create a new WABA. You will need to register a business phone number under this WABA as a part of the embedded signup flow.

## **Business** Phone number

Register a business phone number to your WABA during the embedded signup flow in Plivo’s console. The phone number that you wish to register should be able to receive a one-time password (OTP) sent via text message or a voice call. If you have registered this number with a different WhatsApp solution provider, you can migrate that number under the new WABA you create with Plivo. Detailed requirements for this migration are listed [here](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/#requirements).

Your business phone number will be used to send messages to your customers and will be visible to them on WhatsApp. You can rent a phone number from Plivo (in the countries where Plivo offers this option) or you can bring your own number. For more information, visit [Meta’s guidelines](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) for business phone numbers.

## Templates

Outbound Application-to-peer (A2P) messages can only be initiated using specific templates. You will need to get your template approved before you can send your first outbound A2P message. Follow [our guide](/messaging/concepts/whatsapp/manage-templates/) to [draft templates](https://business.facebook.com/wa/manage/message-templates/?) and adhere to [WhatsApp’s messaging guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/).

## Compliance

[Review the terms](https://business.whatsapp.com/policy) of WhatsApp’s Business Policy, Commerce Policy, and other relevant guidelines. Review Plivo’s acceptable use policy (AUP).

Once you’ve completed these prerequisites, you can begin using Plivo’s Messaging API with WhatsApp.
