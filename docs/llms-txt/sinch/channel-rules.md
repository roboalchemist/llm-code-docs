# Source: https://docs.sinch.com/whatsapp/instructions-and-good-practices/channel-rules.md

# Channel Rules

## **WhatsApp Number Status:**

WhatsApp splits a number’s status into 5 categories:

* **Offline:** The number is not connected to WhatsApp;
* **Pending:** The number has not yet been integrated and approved;
* **Connected:** The number is online and functioning normally;
* **Flagged:** This is a warning sign. When its quality reaches a low quality rating, the number is moved to a flagged status;

When the quality rating reaches a low state **(red)**, the phone number is moved to a Flagged status.

If the message rating improves to a high **(green)** or medium **(yellow)** state within 7 days, the phone number will return to a Connected status.

If the quality rating does not improve within 7 days, the number will return to a Connected status, but with a lower messaging limit imposed on it.

* **Restricted:** Phone numbers that reach their messaging limit are moved to a restricted status. While restricted, the number will be unable to send any notification messages until the 24-hour window for sending messages is reset. They can still respond to any messages initiated by users.

## **Block Rate & Quality Rating**

For companies that use WhatsApp as their communication channel, it is worth paying attention to two variables: the quality rating and messaging limit. These indicators represent the satisfaction level of end customers and may impact the deliverability of messages sent by the company.

**Block Rate**

WhatsApp allows for the end customer to decide if the company is relevant or not through the “**block**” or “**flag as spam**” features.

A Block Rate is when the end customer blocks your brand’s number on WhatsApp or reports your message as spam.

When interaction with the brand is negative and the customer manifests their dissatisfaction, the block rate impacts the **quality rating** of its messages, and may reduce the deliverability of future messages.

The main reasons for a block are:

* **Lack of opt-in** or consent to privacy policies.
* **Frequency**: Number of messages sent to the same person.
* **Response time**: Delay in service, whether human or bot.
* **Lack of service or resolution in the channel**: a customer wishes to resolve a certain issue in the channel and there is no service.

Some factors that can cause a negative experience are:

• Bad experience with the bot; • The end customer contacts the company regarding subject X and the company insists on talking about subject Y; • Lack of or delay in transferring the conversation to another channel or agent; • Unmet need.

## **Influence of Templates (HSM)**

A Template (**previously HSM**) needs to be submitted for prior approval by WhatsApp, and this does not prevent the account from being flagged for poor quality or having a high block rate.

Examples of HSMs that could cause a block rate (even if previously approved):

* Open Session / New way;
* Vague messages;
* Request for personal information;
* Poor customer base;

## **Quality Rating**

The quality rating shows how messages have been received by customers within the last 24 hours. Three different statuses are displayed:

* **High (green):** Positive engagements;
* **Medium (yellow):** Engagement on alert
* **Low (red):** Poor engagement (**must revise template/bot/base**).

A phone number can display two specific statuses related to messaging limits and quality: [**Flagged**](https://docs.wavy.global/whatsapp/instrucoes-e-boas-praticas/regras-do-canal#status-do-numero-do-whatsapp) and [**Restricted**](https://docs.wavy.global/whatsapp/instrucoes-e-boas-praticas/regras-do-canal#status-do-numero-do-whatsapp).
