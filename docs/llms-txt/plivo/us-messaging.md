# Source: https://plivo.com/docs/faq/messaging/us-messaging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# US Messaging (10DLC, Toll-Free, Short Codes)

> FAQs about US A2P messaging compliance, 10DLC registration, and toll-free verification

Frequently asked questions about A2P messaging compliance in the US, including 10DLC registration and toll-free verification.

***

## What is required for A2P messaging in the US?

US carriers require registration or verification for A2P (Application-to-Person) messaging:

| Number Type    | Registration     | Throughput   | Best For          |
| -------------- | ---------------- | ------------ | ----------------- |
| **10DLC**      | Brand + Campaign | 3.75-15+ MPS | General A2P       |
| **Toll-Free**  | Verification     | 25 MPS       | High volume, 2FA  |
| **Short Code** | Application      | 100+ MPS     | Marketing, alerts |

***

## What is 10DLC?

10DLC (10-Digit Long Code) is the standard for A2P messaging on local US numbers.

***

## What is the 10DLC registration process?

1. **Register Brand** - Company information with TCR (The Campaign Registry)
2. **Register Campaign** - Use case and sample messages
3. **Link Numbers** - Associate phone numbers with campaign

***

## How to register a 10DLC brand on the Plivo console?

### Required Information

| Field               | Description                    |
| ------------------- | ------------------------------ |
| Legal business name | Official registered name       |
| EIN                 | Employer Identification Number |
| Business address    | Physical address               |
| Website             | Business website URL           |
| Vertical            | Industry category              |

***

## What is Authentication+ for 10DLC Public Brands?

Effective October 2024, public for-profit brands must complete Authentication+ verification through TCR.

***

## Why did my brand registration fail, and how can I fix it?

| Status   | Meaning                         | Action                    |
| -------- | ------------------------------- | ------------------------- |
| Approved | Ready for campaign registration | Proceed                   |
| Failed   | Issues with submitted info      | Review feedback, resubmit |

Review the feedback from TCR and correct the identified issues before resubmitting.

***

## How to register a 10DLC campaign on the Plivo console?

### Campaign Types

| Type           | Use Cases                         |
| -------------- | --------------------------------- |
| **Standard**   | Marketing, notifications, alerts  |
| **Special**    | Political, charity, emergency     |
| **Low Volume** | Mixed use, under 6,000 msgs/month |

### Required Information

* Use case description
* Sample messages
* Opt-in method
* Opt-out handling

***

## What is the 10DLC campaign vetting process?

Campaigns undergo third-party vetting. Declined campaigns receive feedback for resubmission.

***

## Why was my campaign registration declined, and how can I fix it?

Review the feedback from TCR/carrier, correct the identified issues, and resubmit with updated information.

***

## How do I set up 10DLC for multi-brand companies?

For companies with multiple brands (e.g., parent company with subsidiaries):

* Register each brand separately
* Link campaigns to appropriate brand
* Maintain consistent legal entity information

***

## How to set up email alerts for your 10DLC submissions?

1. Navigate to **Messaging > 10DLC**
2. Configure notification preferences
3. Receive updates on approvals/rejections

***

## How to link phone numbers with 10DLC campaigns?

Associate your phone numbers with registered campaigns through the Plivo console after campaign approval.

***

## How can users opt in to receive messages in the US?

### Supported Opt-In Methods

| Method            | Description                         |
| ----------------- | ----------------------------------- |
| **Web form**      | User enters phone number on website |
| **Keyword**       | User texts keyword to your number   |
| **Paper form**    | Physical sign-up sheet              |
| **Verbal**        | Phone call consent (recorded)       |
| **Point of sale** | In-person consent at checkout       |

***

## What is the Toll-Free Verification Process?

1. Purchase toll-free number
2. Submit verification request
3. Carrier reviews submission
4. Receive approval or rejection feedback

***

## How to submit Toll-free verification on the Plivo console?

1. Navigate to **Messaging > Toll-free Verification**
2. Click **Submit Toll-free Verification**
3. Select profile
4. Complete required fields
5. Submit

### Required Information

| Field           | Description                  |
| --------------- | ---------------------------- |
| Business name   | Legal business name          |
| Business type   | Direct brand or ISV/Reseller |
| Use case        | How you'll use messaging     |
| Sample messages | Example message content      |
| Opt-in method   | How users consent            |
| Website         | Business website             |

***

## Why was my Toll-free verification request rejected, and how can I fix it?

| Status   | Meaning           | Action                    |
| -------- | ----------------- | ------------------------- |
| Approved | Ready to send     | Begin messaging           |
| Rejected | Issues identified | Review feedback, resubmit |

Review the feedback, provide clear and accurate business information, and resubmit.

***

## What are the best practices for Toll-free verification?

* Provide clear, accurate business information
* Include realistic sample messages
* Document opt-in methods clearly
* Respond promptly to carrier inquiries

***

## What about Short Codes?

For high-volume messaging, see [Short Codes](/docs/messaging/short-codes) for complete details on:

* US, Canada, Brazil, and New Zealand short codes
* Application process and requirements
* Pricing and throughput
* Compliance and audits

***

## What is the throughput comparison for US numbers?

| Number Type | Registration Status | SMS Throughput         |
| ----------- | ------------------- | ---------------------- |
| Long Code   | Unregistered        | 1 MPS, 2,000/day limit |
| Long Code   | 10DLC Low Volume    | 0.2-0.75 MPS           |
| Long Code   | 10DLC Standard      | 3.75-15+ MPS           |
| Toll-Free   | Verified            | 25 MPS                 |
| Short Code  | Approved            | 100+ MPS               |

***

## What is the throughput for Canada numbers?

| Number Type | SMS Throughput |
| ----------- | -------------- |
| Long Code   | 15/minute      |
| Toll-Free   | 25/second      |
| Short Code  | 10/second      |

***

## Why are my messages being filtered?

* Verify registration is complete
* Check message content for spam triggers
* Ensure proper opt-in documentation

***

## Why is my throughput low?

* Complete 10DLC registration for higher limits
* Consider toll-free or short code for high volume

***

## Related Resources

* [Messaging API Overview](/docs/messaging/messaging-api)
* [SMS](/docs/messaging/sms)
* [Short Codes](/docs/messaging/short-codes)
* [10DLC Documentation](https://www.plivo.com/docs/messaging/concepts/10dlc/)
* [Toll-Free Verification](https://www.plivo.com/docs/messaging/concepts/toll-free-verification/)
