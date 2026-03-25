# Source: https://plivo.com/docs/messaging/concepts/dnd-service.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DND Service

> Manage Do Not Disturb opt-out handling for US/Canada messaging

Plivo offers a "Do Not Disturb" (DND) feature by default for long codes and toll-free numbers in the U.S. and Canada. This feature is now available for short codes as well. To enable DND for short codes, please reach out to [Plivo support](https://support.plivo.com/hc/en-us/requests/new?ticket_form_id=360000156292) for assistance.

## Keywords for HELP and INFO

Plivo automatically responds to users who text "HELP" or "INFO" to a Plivo long code or toll-free number. If a user no longer wishes to receive messages from a specific Plivo number, they can simply text "STOP." Standard message and data rates may apply.

```text  theme={null}
Text STOP to stop receiving messages from this number. Message and data rates may apply.
```

## Opt-Out Functionality

Plivo’s DND feature halts outbound messages from a Plivo number to a specific destination when the destination replies with certain opt-out keywords. For instance, if a recipient (Number A) sends an inbound message containing any of the keywords below to a Plivo number (Number B), outbound messages from Number B to Number A will be blocked and flagged with [error code 200](/messaging/troubleshooting/error-codes/).

### Supported Keywords for Opting Out

* STOP
* END
* QUIT
* CANCEL
* UNSUBSCRIBE
* UNSUB
* STOP ALL

<Note>
  <strong>Note:</strong> Variations of "STOP" with trailing spaces or newline characters will also trigger the DND block.
</Note>

### Examples of Valid Opt-Outs

The DND feature is case-insensitive, so variations like "STOP," "Stop," "STop," or "stop" are all recognized as valid.

### Examples of Invalid Opt-Outs

* “Hey, can you stop texting me?”
* “Stop it!”

### Opt-out confirmation message

After a customer opts out, they will receive a confirmation message, indicating that they've been unsubscribed and will no longer receive messages from that particular number:

```text  theme={null}
You have been unsubscribed and will not receive any more messages from this number.
```

### Best Practices for Opt-Out Messages

* Refer to our [best practices guide](/messaging/concepts/us-messaging-best-practices/) for recommendations on message content.
* Always include opt-out instructions in your messages, such as, "Reply STOP to opt out."
* In addition to standard keywords, some customers may reply with text messages like 'Can you stop texting me?' and other similar messages. Plivo recommends establishing monitoring for inbound messages. If you receive angry or complaining messages, review the opt-in list to ensure you are reaching out to valid opted-in users.
* If a customer opts out of messages from one Plivo number, you should not try to reach out to the customer with another number. This is likely to enrage the customer and increases the likelihood of 7726 (spam) complaints, which can lead to the suspension of your messaging campaign.

### 10DLC Campaign Guidelines

In the case of US 10 DLC, If a customer opts out of messages from one Plivo number linked to a campaign, they will be opted out from all numbers associated with that campaign. This means if a customer opts out from number A within campaign C, all other numbers (such as B, C, and D) associated with campaign X will also be opted out, and no further messages will be allowed from any Plivo numbers in that campaign. Attempting to reach out with another number after opt-out can lead to customer dissatisfaction and an increased risk of 7726 (spam) complaints, potentially resulting in the suspension of your messaging campaign.

## Opting in

To opt back in to receive messages from a blocked number, the number that replied with STOP must send one of these keywords:

* START
* YES
* RESUME
* UNSTOP
* GO

After a number replies with any of these keywords, it will again be able to receive messages from the Plivo number that was blocked. The keyword triggers opt-in only when sent as a single word with no punctuation or leading spaces (any trailing spaces are trimmed).

### Valid opt-in examples

All the keywords are case-insensitive, so variations like UNSTOP, UNStop, UnSTop, and unstop are all valid.

### Invalid opt-in examples

* “Hey can you enable me again”
* “Unstop me!”

### Opt-in confirmation message

An opt-in confirmation message informs the consumer they can start two-way texting with the message sender’s phone number again:

```text  theme={null}
You have been resubscribed to receiving messages from this number. Reply HELP for help or STOP to stop receiving messages. Message and data rates may apply.
```

If a sender’s phone number was not blocked earlier, sending these keywords will not trigger any confirmation message.
