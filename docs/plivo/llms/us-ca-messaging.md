# Source: https://plivo.com/docs/messaging/concepts/us-ca-messaging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# US and Canada Messaging

> SMS messaging in the US is governed by the [CTIA](https://www.ctia.org/). Strict rules are in place to regulate US messaging, which makes the right SMS implementation a deceptively challenging experience. This guide outlines the best practices to ensure your messaging is in compliance with regulatory and industry standards.

Unlike SMS in other countries, SMS features and regulations in the US and Canada are directly dependent on the source number used for sending an SMS. In the US, there are three possible types of source numbers that one might use to send an SMS:

1. Local phone numbers (a.k.a. long codes)
2. Toll-free numbers (1-8xx)
3. Short codes

To ensure high deliverability, it’s important to use the right source number type for your specific use case and daily volume. If you use the wrong source number, it may lead to excessive carrier filtering and poor delivery rates.

At Plivo, we support all the available source number types in the US. We work closely with our customers to help them choose the right product for their business.

## 10-digit long codes

Long codes are regular 10-digit phone numbers capable of sending and receiving texts and voice calls.

Long codes have the following advantages over other source number types:

* They are relatable and personal and therefore more likely to garner a response from the recipient.
* They‘re easy to procure and set up. Plivo’s [Phone Number API](/numbers/quickstart/numbers/) lets you programmatically search for and purchase phone numbers by region or prefix.

Regular long codes are meant for person-to-person (P2P) communication, or conversational SMS. In Canada, they can be used for A2P messaging but they have low throughput per number. In the US, regular long codes don’t perform well for high-volume application-to-person (A2P) messaging use cases. For these, US mobile network operators have launched a service called 10DLC (10-digit long code) to explicitly allow A2P SMS traffic over long code phone numbers.

### Who should use 10DLC?

10DLC is the best phone number choice for most standard use cases, such as delivery notifications and two-factor authentication. They’re also best for businesses that want to have their messages come from familiar local numbers. By comparison, toll-free numbers have lower maximum throughput and take slightly longer to get approval for. And while short codes offer higher maximum throughput than 10DLC, they have higher monthly rental costs and one-time setup fees and take several weeks to provision.

### Benefits of 10DLC

* High messaging throughput — up to 4,500 transactions per minute per operator
* Enhanced deliverability, because 10DLC use cases are approved by operators
* Unlike short codes, long code numbers can be used to make and receive calls
* Cost savings compared to short codes

### Key 10DLC terminologies

A brand represents a business entity that is responsible for sending messages.

A campaign represents the type of messages the brand intends to send. The terms “campaign” and “use case” are often used interchangeably. Brands may run campaigns of several types.

Once you’ve registered your brands and campaigns you must link phone numbers to the campaigns. Once you’ve done that, messages sent from those numbers are considered 10DLC-registered and all the benefits of 10DLC apply.

### 10DLC registration process

Plivo’s customers can use the [console](/blog/10dlc-in-the-console/) or the [SDKs](/messaging/api/10dlc/) to complete registration for themselves and their customers. [Register your business as a Standard brand](/messaging/a2p-10dlc/registration-process/). Plivo strongly recommends taking advantage of optional vetting for your brand if your messaging volume exceeds 6,000 per day. Only vetted brands can take advantage of the highest possible throughput: 4,500 messages per minute.

* If your messaging volume is less than 6,000 messages per day, you can opt for a low-volume mixed campaign.
* If your messaging volume is higher, you can choose from a variety of campaign types for your messaging requirement.

Read more about [how to get started with Plivo’s updated server SDKs for 10DLC](/messaging/a2p-10dlc/quickstart/).

## Toll-free numbers

We’ve all come across toll-free numbers — the 1-8xx customer care phone numbers we’re accustomed to calling when we want to speak to a business representative.

Toll-free numbers are well-suited for business messaging since people already perceive toll-free numbers as business lines. They can be used to send text messages at up to 40 SMS messages per second at a relatively [low cost](https://www.plivo.com/sms/pricing/us/#phone-price-section).

You can acquire SMS-enabled toll-free numbers on the [Plivo console](https://cx.plivo.com/home) or by using [Plivo APIs](/numbers/api/overview/). Toll-free numbers must be verified before you can start reaching out to customers in the US and Canada.

### Toll-free verification requirements

North American carriers have mandated the verification of toll-free numbers to be used for messaging. It’s prohibited to send messages from unverified toll-free numbers in both the US and Canada.

Verification is part of the Know Your Customer (KYC) regulations that aim to increase consumer trust and reduce spam in A2P messaging. Verifying toll-free numbers serves the same purpose as registering long codes before they can be used as 10DLC numbers.

### Toll-free verification process

Follow the process outlined in [our support document](https://support.plivo.com/hc/en-us/articles/360049342151) to initiate a verification request for a Plivo toll-free number.

Once you submit a request, Plivo passes it on to our carrier for review and lists the number as “pending verification”. We will promptly inform you via email or Callbacks once your toll-free numbers are either verified or rejected. If the verification request is rejected by the carrier, the number will be marked “unverified” and all messages sent thereafter will be blocked. You may review the rejection reason, consult with our support team, make changes, and resubmit your request. When the carrier notifies us of the successful completion of the verification request, the status will be changed to “verified.”

***Plivo recommends that you begin sending messages only after a toll-free number has been verified.***

When the carrier notifies us of the successful completion of the verification request, the status will be changed to “verified.” At that stage, the number is subject to the minimum amount of filtering. Verified numbers have no daily, weekly, or monthly limits.

A number does not need to be re-verified for the same use case in the future. If you want to use the toll-free number for a different or an additional use case, you should submit a new verification request. Failure to do so can be considered noncompliant by the carriers and may result in your messaging services being suspended.

## Short codes

Have you ever noticed that the text messages you receive from your bank or from other large institutions generally come from four- to seven-digit numbers that don’t look anything like regular phone numbers?

These numbers are called short codes: special SMS only source numbers, typically provisioned by enterprises for their business-critical communications. This is because short codes offer the best possible reliability at the highest possible scale (100 SMS per second).

The good news is that we’ve made short codes an affordable option for small and medium-sized businesses. Check out our [short code pricing list](/sms/pricing/).

Short codes have the following advantages over other source number products:

* Very high deliverability at maximum throughput (up to 100 SMS per second). You can be sure of your delivery metrics thanks to handset delivery receipts that are generated when the text message is successfully received.
* Highly predictable delivery rates since your use case and SMS content shall be preapproved even before you start.

The drawback is that the provisioning cycle for short codes is the longest out of all the available options — typically eight to twelve weeks. Why is that? Short codes and their corresponding use cases need to be preapproved by all network operators (Verizon, AT\&T, T-Mobile, etc.) before you send one text out.

The good news is that once you’re preapproved, there will be no surprises once you actually go live.

## A side-by-side comparison

| **10-Digit Long Code**                                                                                   | **Toll-Free**                                                                                                                 | **Short Code**                                                                                         |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Regular phone numbers. Specific to locality.                                                             | 1-8xx business phone numbers.                                                                                                 | Four- to seven-digit specially provisioned and preapproved source numbers.                             |
| Best for business notifications and updates to customers.                                                | Best for business notifications and updates to customers.                                                                     | Best for business-critical notifications and updates to customers.                                     |
| Buy using Plivo APIs or console. Requires completion of 10DLC registration, which can take up to a week. | Ready to use. Buy using Plivo APIs or console. Requires verification beyond certain sending limits, which can take 4–6 weeks. | Manual process. Provisioning short codes may take eight to 12 weeks.                                   |
| Network delivery reports.                                                                                | Handset delivery reports.                                                                                                     | Handset delivery reports.                                                                              |
| Relaxed spam filters, as use cases have been pre-vetted.                                                 | Sensitive spam filters tuned to block unwanted bulk marketing campaigns.                                                      | Relatively relaxed spam filters given that the use case and content must be preapproved to begin with. |
| Low rental cost per number. Additional cost for completing the registration process.                     | Relatively low rental cost for available throughput. No cost for completing the verification process.                         | Higher rental cost. Worth it for the high reliability at scale, as per-message cost is lowest.         |
