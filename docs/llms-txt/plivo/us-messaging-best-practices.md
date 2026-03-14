# Source: https://plivo.com/docs/messaging/concepts/us-messaging-best-practices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices for A2P Messaging in the US

> High-quality, well-formatted content is more likely to be opened and less likely to be mistaken as spam by consumers, operators, and carriers. Follow these guidelines to make sure your SMS content meets the standards for great messaging.

All use of Plivo services is subject to our [acceptable use policy](/aup/); violations may lead to suspension of your services.

## SMS content best practices

These best practices for message content make messages more valuable to consumers and less likely to trigger real-time content analysis from messages flagged incorrectly as spam.

As a general rule, carriers don’t preapprove or whitelist messaging content. A carrier may review any message content as part of an account review. Message content flagged by automatic spam detection algorithms is reviewed by a human operator. If the message is reviewed by a third party, out of context, it should appear to be a transactional, application-to-person message, originating from a specific request by the end user. If the operator decides the message is inappropriate, it may block the sending number.

In general, message content should include:

* Your organization’s name
* A reference to the reason the message is being sent
* A STOP message

While a STOP message does not need to be included in every message sent, consider sending it with every fourth or fifth message.

Message content should avoid:

* The words “Free,” “Now,” “Offer,” “Winner,” or any other promotional-sounding language
* Requests for action without specifying context
* Generic URL shortener links

### Use of URLs in messages

If your message contains a link, use a URL in a domain that your business owns and that aligns with the brand or campaign from which you send the message.

Use full URLs in your messages when you can. Avoid public URL shorteners such as Bitly and TinyURL. US carrier policies discourage the use of public URL shorteners, which means a higher risk your message will be filtered with no recourse. If you use a URL shortener, we recommend getting one that’s specific to your business (such as swoo.sh, which is used by Nike). Bear in mind, though, that many recipients view shortened URLs warily and refuse to click on them because they can be used by spammers and in phishing attempts.

URLs included in your messages must avoid multiple redirects, which are generally perceived as suspicious. Operators or message recipients might flag a message with multiple redirects as a phishing attempt, which might result in the suspension of your campaign.

### Use natural language

Use natural language in your messages. Avoid nonstandard spellings (“H! h0w ar3 u do1ng?”).

### Set expectations for message frequency

If you plan to send five texts a month, disclosing “5 messages a month” on the first interaction leads to a better user experience.

## Things to avoid in content creation

Certain kinds of A2P content are prohibited and should be avoided.

### Deceptive marketing

Marketing messages must be truthful, not misleading, and, when appropriate, backed by scientific evidence in order to meet the standards set by the Federal Trade Commission’s (FTC) Truth In Advertising rules. The FTC prohibits unfair or deceptive advertising in any medium, including text messages.

### Fraud or scam

Any messages that constitute fraud or scam and involve wrongful or criminal deception intended to result in financial or personal gain are prohibited. These messages generally involve money and/or some sort of business transaction.

### SHAFT (sex, hate, alcohol, firearms, and tobacco)

Content related to SHAFT use cases such as the following is prohibited in the US by local or federal law.

* Pornographic and/or adult entertainment industry purpose, prostitution, human trafficking
* Violence, hate speech, or otherwise engaging in threatening, abusive, harassing, defamatory, libelous, deceptive, or fraudulent behavior
* Sale or promotion of substances that are classified as controlled substances as per federal law (e.g. cannabis)

### Other prohibited content

Messages that contain terms related to the following sensitive topics are considered spam and should not be used in A2P campaigns.

* Debt collection, debt relief/restructuring/refinancing, and credit repair offers
* High-risk financial services such as payday loan offers, education loan offers, third-party auto and mortgage loan offers, and cryptocurrency
* Unsolicited insurance quotes
* Work-from-home job offers, including pyramid schemes
* Third-party lead generation services
* Illegal prescriptions
* Gambling
* Real estate
* Other campaign types that are not in compliance with CTIA [messaging principles and best practices](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)

Contact your customer success manager or our support team if you suspect your use case falls under a prohibited content type.

### Promotional messages

Promotional messaging is not allowed on toll-free numbers and is subject to blocking.

## Sample messages

### Example: Good content

* Plivo — your one-time passcode is 12345
* DeliveryFoodsInc — your food order has been completed and is on its way. Look for it in 15 minutes. Track your order via our app: [https://realurl.com/?id=12345](https://realurl.com/?id=12345). Reply STOP to opt out of future notifications
* Hi, Name, and thank you for requesting more information from CompanyName. The content you requested is available at [https://realurl.com/?id=12345](https://realurl.com/?id=12345). Reply STOP to opt out

### Example: Bad content

* Get a FREE quote about your home! Lowest APR! [https://urlshortener.com/?id=12345](https://urlshortener.com/?id=12345)
* Bad credit? Still get approved for a home! Check out our free finance options [https://urlshortener.com/?id=12345](https://urlshortener.com/?id=12345)
* Download our app `{appname}` now to get \$20 in free credits [https://appstoreurl.com/myapp](https://appstoreurl.com/myapp)
* Accept your special offer before it expires [https://urlshortener.com/?id=12345](https://urlshortener.com/?id=12345)

## Prohibited messaging practices

All messages in the US must adhere to the [codes of conduct published by mobile network operators](https://www.10dlc.org/en/verizon-tmobile-att-sprint-carrier-code-of-conduct) (AT\&T, T-Mobile, Verizon). If a message sender is observed sending any of the kinds of disallowed content listed below, Plivo will perform an account review. This review can result in the suspension of sending rights for a provisioned phone number, restriction of high-throughput access, suspension of provisioning rights for new phone numbers, and/or suspension of all network services. Message senders are expected to enforce restrictions on their own networks to prevent these types of content at the intake source.

### Phishing

Phishing is the practice of sending messages that appear to come from reputable companies but in fact trick consumers into revealing personal information, such as passwords and credit card numbers.

### Snowshoeing

Snowshoeing is a technique that uses multiple source numbers for messaging with the intent to evade filters. All operators prohibit snowshoeing. Using the practice may result in poor deliverability and in some cases campaign or account suspension.

### Filter evasion assistance and number cycling

The practice of automatically providing a sender with new phone numbers to replace previously blocked phone numbers is prohibited. Similarly, number cycling is a technique in which messaging providers discard numbers upon seeing poor deliverability and provide replacement numbers. This results in a poor experience for customers and suggests to operators unwanted messaging or lack of customer consent. Instead of number cycling, work with Plivo to identify the root cause of poor deliverability and fix the issue.

## Managaging messaging campaigns for better deliverability

Here are some best practices that can help you improve your message deliverability scores.

### Customer consent

All Plivo subscribers must comply with the opt-in requirements outlined in the [CTIA guidelines](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). In short, businesses should send messages to customers only after receiving opt-in permission. Also, message senders should not use opt-in lists that have been rented, sold, or shared. You can read more about opt-in practices in [our detailed guide](https://support.plivo.com/hc/en-us/articles/23925508391065-How-can-users-opt-in-to-receive-messages-in-the-US).

When customers opt in, you should send them a confirmation message that includes details about the campaign, possible charges, whether they’ll get recurring messages, and how to opt out. Example: *Welcome to Plivo developer outreach. Message and data rates may apply. Reply HELP for help, STOP to cancel.*

You should collect the consumer consent yourself. Don’t use consent acquired from a third party. Consumers expect a relationship with the businesses with which they interact.

Plivo reserves the right to suspend or terminate your messaging services if we learn you’ve failed to comply with opt-in guidelines.

If your opt-in process involves a web form, you should ensure that it clearly conveys all of these details to the consumer.

* Brand/company name
* Program/campaign description
* Link to Terms and Conditions page and Privacy Policy pages
* Customer care information
* Message frequency information

Plivo recommends adding as much information as you can about your use case.

Here’s a sample web-based opt-in form for illustration purposes that captures all relevant information to meet carrier/network guidelines.

<Frame>
    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/consent2.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=70a501c417071b915d81f8f5e3f5c4f5" alt="" width="932" height="938" data-path="images/consent2.png" />
</Frame>

Using the recommended opt-in process reduces the risk of unsolicited messaging in the ecosystem and spam complaints on your messaging campaigns.

### Proof of opt-in

Plivo recommends maintaining an updated list with a record of every opted-in user. If we receive carrier or subscriber complaints about spam, Plivo and its partners may carry out an audit. In that event we will ask you for proof of opt-in consent. For each user, you must be able to produce this information as proof of opt-in.

* Timestamp of opt-in
* Opt-in medium (e.g. web forms, SMS, paper opt-in, physical signup, etc.)
* IP address used for opt-in process (if opted in via web form)
* The consumer phone number that has granted consent (if opted in via SMS)
* Name of the individual or other identifier (e.g. online username, session ID, etc.)

You should also offer an [opt-out mechanism](/messaging/concepts/dnd-service/) in every message to avoid violations. Plivo also recommends that you review inbound messages for messages like “I’m not interested,” ”Do not send messages,” ”Not required,” etc., and remove those subscribers from your target group.

### Allow customers to opt out

Ensure that users can opt out of your messages easily. A general best practice is to add opt-out instructions to your messages, particularly for informational, marketing, and promotional messages. Plivo recommends adding “Reply STOP to unsubscribe” or “reply STOP to cancel” to the end of your message. Your system must not send messages to customers that have opted out. A general best practice is to send recipients a confirmation that they have been opted out and add instructions on how to opt back in. Example: *\[Business/campaign name]: You replied with STOP, which blocks all the texts from this number. Text UNSTOP to receive messages again.*

Not providing an opt-out option or sending people messages after they have opted out is a violation that could result in the termination of your campaign. But providing a way for people to opt out doesn’t mean you can ignore the opt-in requirement.

Plivo provides an easy way to manage opt-outs with its [DND service](/messaging/concepts/dnd-service/).

A high rate of opt-outs from your numbers or campaigns may result in filtering or blocking your traffic.

### HELP keyword

Offer a HELP keyword that users can send to get information from the message sender. The reply message you return when users request help may contain information such as

* Business name and description
* Contact info
* Fee or charges
* Opt-out instructions

### Use one recognizable number

Spreading messages over multiple source numbers is considered snowshoeing and is prohibited. Plivo recommends using a single number for each messaging campaign. If your campaign requires multiple phone numbers, please discuss the use case with your customer success manager or reach out to Plivo support.

### Use one recognizable domain name

Each campaign should be associated with a single web domain.

## Carrier monitoring

Our carriers continuously monitor text messages sent over their networks. To ensure uninterrupted service, avoid incurring a high number of consumer complaints and a high opt-out rate.

### Consumer complaints

Major operators in North America support consumer-driven spam controls. Their mobile subscribers can forward unwanted or unconsented text messages to the short code 7726 (it spells “SPAM” on the dialpad).

Carriers actively monitor consumer complaints sent to this service. When multiple complaints are received for a sender, mobile network operators (MNO) send a notification to the message sender that includes the source phone number, destination phone number, timestamp, and original message ID. Upon receipt, the sender provider must provide proof of a TCPA-compliant opt-in for those specific messages, as well as an overview of the messaging campaign and the opt-in process that the unwanted message was a part of.

If a large number of unwanted or unconsented messages are reported on a source phone number, that number may have its sending rights suspended while opt-in is being confirmed.

### Opt-out rate

MNOs also track opt-out rates. The daily opt-out rate on a phone number is defined as the number of opted-out consumers that were sent messages divide by the unique consumer phone numbers contacted within a 24-hour period.

If the daily opt-out rate on a sending phone number is 5% or greater, the account is flagged for monitoring. An opt-out rate of 10% or greater on a sending phone number may result in immediate suspension of services.
