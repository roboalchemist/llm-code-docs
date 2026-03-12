# Source: https://documentation.onesignal.com/docs/en/email-compliance.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email regulatory compliance

> Learn how to comply with global privacy and communication regulations when sending marketing emails using OneSignal. This guide covers consent requirements, opt-out rules, and email content regulations across major regions, including the EU, US, Canada, and more.

Most countries have legislation in place to protect individuals’ privacy and regulate how organizations can send email communications. As the sender, it is your legal responsibility to:

* Ensure your messages comply with your own country’s privacy legislation.
* Ensure your messages comply with the privacy laws of each recipient’s country.

OneSignal provides tools to help you manage compliance, but you must implement them appropriately based on your target audience and applicable laws.

***

## Consent requirements for marketing emails

Many countries mandate **explicit consent** (opt-in) before sending marketing emails. These include:

* European Union (under the GDPR)
* United Kingdom
* Canada (under CASL)
* Australia
* New Zealand
* Singapore
* Hong Kong

The United States differs by allowing either opt-in or opt-out, depending on the context and applicable state or federal law. The **CAN-SPAM Act** permits sending marketing emails without prior consent, as long as recipients are allowed to unsubscribe.

### Double opt-in requirements

Some countries, like Germany, recommend or require a double opt-in process. This involves:

1. The user submitting a form requesting marketing emails.
2. A follow-up confirmation email with a link the user must click to complete the subscription.

This additional step provides proof of consent and helps reduce spam complaints.

***

## How to get opt-in consent

At minimum, you should collect clear opt-in consent before sending marketing messages. This can be done using:

* A checkbox on your signup form (unchecked by default) labeled clearly for marketing consent.
* A pop-up or banner that explains what communications users will receive.

If it has been a long time since you've emailed your list, consider sending a **re-consent email campaign** to revalidate their interest and compliance.

***

## Unsubscribe and opt-out requirements

Every marketing email you send must include a **visible and functional "unsubscribe" link**. This allows recipients to opt out of future communications.

Timelines for honoring unsubscribe requests vary:

* **United States (CAN-SPAM)**: Opt-out requests must be honored within 10 business days.
* **GDPR and similar laws**: Opt-out must be honored immediately or without undue delay.

### Best practices for opt-out links

* Place the link in a visible location, typically at the bottom of the email.
* Clearly label it as an unsubscribe or subscription management option.
* Do not require users to log in or take additional steps to opt out.

***

## Email content compliance

Certain regulations also govern the content of your marketing emails:

* **Header and sender info**: You must use accurate "From," "Reply-To," and routing information.
* **Subject line**: Must not be misleading or deceptive.
* **Physical address**: Include your organization's physical mailing address in every message.

These rules are strictly enforced under the **CAN-SPAM Act**, and similar guidelines exist in other jurisdictions.

***

## Managing subscription preferences in OneSignal

OneSignal supports tools to help you comply with email legislation:

* [Unsubscribe Links & Email Subscriptions](./unsubscribe-links-email-subscriptions): Easily manage user opt-outs and preferences.
* [Email Best Practices](./email-setup): Guidance to ensure high deliverability and compliance.
* [Email Acceptable Use Policy & Code of Conduct](https://onesignal.com/aup): Outlines what types of content are allowed.

## We recommend all senders follow these tools and policies to ensure your marketing campaigns are respectful, legally compliant, and effective

Built with [Mintlify](https://mintlify.com).
