# Source: https://documentation.onesignal.com/docs/en/sms-consent-keyword-management.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS consent keyword management

> Manage SMS opt-in, opt-out, and help keywords for compliance.

<Frame caption="SMS consent keyword management interface">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7e42aa8-Screenshot_2024-07-24_at_11.03.55_AM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=f1aa6280eae198da9ae1fb52373d5b6c" width="1492" height="1060" data-path="images/docs/7e42aa8-Screenshot_2024-07-24_at_11.03.55_AM.png" />
</Frame>

SMS is a regulated channel that requires specific functionality for managing subscriptions. Handling opt-outs can either store the opt-out status as a suppression for that particular Sender number or sync the unsubscribe globally across all Senders.

Start by navigating to **Settings > Platforms > SMS Settings > Consent Management**.

# Double opt-in

Double Opt-In will default sms subscriptions into a pending state when added to OneSignal and automatically send an SMS prompt for the user to confirm they'd like to subscribe. Once confirmed, we'll mark the sms subscription as subscribed. Double Opt In ensures genuine user consent, enhances engagement, reduces spam complaints, and complies with regulations like TCPA and GDPR. See [SMS Regulatory Compliance](./sms-regulatory-compliance) for details.

Click **Edit** and toggle on **Send Message Prompt**. Then select or create the SMS Template you want to use to ask for opt-in.

<Frame caption="">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8a38d651e7775d20c60a70d691363cf2f3c935b515ad019b3b73b5a1f09554fa-Screenshot_2024-10-28_at_12.59.19_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=549176e2c07eb6e2f7506a040acd0fb5" width="1926" height="1336" data-path="images/docs/8a38d651e7775d20c60a70d691363cf2f3c935b515ad019b3b73b5a1f09554fa-Screenshot_2024-10-28_at_12.59.19_PM.png" />
</Frame>

Example message:

```
Hi {{first_name | default: "there"}} to OneSignal sms, reply SUBSCRIBE to start receiving messages.
```

In this example, we are using [Message Personalization](./message-personalization) to include the user's name if you collect this via tags. Otherwise, it defaults to say "Hi there...". We are also setting the specific opt-in keyword "SUBSCRIBE" to let the user know what to say to opt-in to SMS. *Keep an eye on the length and content of your prompt to keep your SMS costs low. See [SMS](/reference/sms) for details.*

## Text-To-Subscribe keywords

Create your opt-in keywords. This should be the same keyword you used in the message prompt.

After the user messages back this keyword, you can send a "thank you" message to let them know how to unsubscribe in the future if needed.

<Frame caption="Text-to-subscribe keyword configuration">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7588e271019c40099924dd5ff81a2adcf2f0f6518ffac8c183af7d84345a4187-Screenshot_2024-10-28_at_12.59.19_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=43249ca1d714389a59b0d8bf17d3e8b6" width="1926" height="1336" data-path="images/docs/7588e271019c40099924dd5ff81a2adcf2f0f6518ffac8c183af7d84345a4187-Screenshot_2024-10-28_at_12.59.19_PM.png" />
</Frame>

```
Thanks for subscribing to sms text messages! We will only inform you of important information. Reply STOP to opt-out at anytime.
```

In this example, we are informing the user that they can opt-out of further messages with the keyword "STOP". *Keep an eye on the length and content of your prompt to keep your SMS costs low. See [SMS](/reference/sms) for details.*

<Warning>
  Ensure each sender is set up to sync incoming message replies in order to process Keywords. Navigate to **SMS Settings > Senders** and click **Setup Replies** to sync your sender's replies to OneSignal.

  If you do not have message replies synced, we will still stop sending to that recipient, but you will not be able to update their subscription status.

  **Important:** Alphanumeric sender IDs (e.g., "MyBrand") do not support two-way messaging and cannot receive replies. If using alphanumeric senders, you must implement your own opt-out mechanism (such as a web link or dedicated phone number) and manually manage subscription preferences to ensure compliance with local regulations.
</Warning>

***

# Opt-out keywords

OneSignal provides default keywords for managing unsubscribes. These are expected keywords to support common actions like subscribing, unsubscribing, and requesting help. Some cannot be edited but you can add more if desired.

**Opt-Out Keywords**: Keywords like `STOP`, `UNSUBSCRIBE`, or `CANCEL` are used to manage opt-outs and ensure users are not sent unwanted messages.

<Frame caption="Opt-out keywords settings">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8ae062e-Opt-out_1.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=15bbb293733771d353025885b5712f08" width="1653" height="740" data-path="images/docs/8ae062e-Opt-out_1.png" />
</Frame>

### Additional Actions

* **Sync as Unsubscribe Across All Senders**:

  * **On**: When someone texts `STOP` or one of the keywords provided, their subscription status will be updated to `unsubscribed` on their subscription profile. Attempting to send messages to them from any Sender will no longer be possible.
  * **Off**: The `STOP` command, or any opt-out keyword, will only prevent the recipient from receiving messages from that specific sender messaging service or number. They will appear as suppressed if you attempt to send them from the same sender again, but messages from different numbers may go through. This approach is recommended if you use multiple numbers, such as one for marketing and another for transactional purposes.

<Warning>
  Ensure each sender is set up to sync incoming message replies in order to process Keywords. Navigate to **SMS Settings > Senders** and click **Setup Replies** to sync your sender's replies to OneSignal.

  If you do not have message replies synced, we will still stop sending to that recipient, but you will not be able to update their subscription status.

  **Important:** Alphanumeric sender IDs (e.g., "MyBrand") do not support two-way messaging and cannot receive replies. If using alphanumeric senders, you must implement your own opt-out mechanism (such as a web link or dedicated phone number) and manually manage subscription preferences to ensure compliance with local regulations.
</Warning>

***

# Re-Subscribe keywords

**Re-Subscribe Keywords**: Keywords like `START`, `UNSTOP`, or `YES` allow users to resubscribe to messages.

<Frame caption="Re-subscribe keywords configuration">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c94ce45-Re-Subscribe_1.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=046f044aa759b54cc538c7d98e7db61d" width="1653" height="677" data-path="images/docs/c94ce45-Re-Subscribe_1.png" />
</Frame>

**Resubscribing**: Once someone is added to a suppression list for a sender, there is no way to remove that number from the suppression list via the OneSignal dashboard. The only method is for the recipient to resubscribe by texting a re-subscribe keyword to the same number. This action will update their subscription status to subscribed (if not already) and remove them from the suppression list for that sender.

<Warning>
  Ensure each sender is set up to sync incoming message replies in order to process Keywords. Navigate to **SMS Settings > Senders** and click **Setup Replies** to sync your sender's replies to OneSignal.

  If you do not have message replies synced, we will still stop sending to that recipient, but you will not be able to update their subscription status.

  **Important:** Alphanumeric sender IDs (e.g., "MyBrand") do not support two-way messaging and cannot receive replies. If using alphanumeric senders, you must implement your own opt-out mechanism (such as a web link or dedicated phone number) and manually manage subscription preferences to ensure compliance with local regulations.
</Warning>

***

# Help keywords

**Help Keywords**: Keywords like `HELP` are used to provide users with additional information on how to manage their subscriptions.

<Frame caption="Help keywords settings">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e739d60-Help_1.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=7599b43bd7ffbe9afc3d11565861d6e1" width="1653" height="578" data-path="images/docs/e739d60-Help_1.png" />
</Frame>

## Additional Information

* **Re-Subscribe Keywords**: Ensure these keywords are intuitive for users to easily re-subscribe.
* **Opt-out Keywords**: Provide clear instructions in your messages to users about how they can unsubscribe.
* **Help Keywords**: Make sure your help response provides essential information and points users to further assistance if needed.

By configuring these settings, you can efficiently manage your SMS subscriptions, comply with regulations, and provide a seamless experience for your users.

For more information or assistance, please contact our support team at `support@onesignal.com`

<Warning>
  Ensure each sender is set up to sync incoming message replies in order to process Keywords. Navigate to **SMS Settings > Senders** and click **Setup Replies** to sync your sender's replies to OneSignal.

  If you do not have message replies synced, we will still stop sending to that recipient, but you will not be able to update their subscription status.

  **Important:** Alphanumeric sender IDs (e.g., "MyBrand") do not support two-way messaging and cannot receive replies. If using alphanumeric senders, you must implement your own opt-out mechanism (such as a web link or dedicated phone number) and manually manage subscription preferences to ensure compliance with local regulations.
</Warning>

***

Built with [Mintlify](https://mintlify.com).
