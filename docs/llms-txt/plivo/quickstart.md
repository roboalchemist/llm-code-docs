# Source: https://plivo.com/docs/voice/quickstart/quickstart.md

# Source: https://plivo.com/docs/messaging/quickstart/quickstart.md

# Source: https://plivo.com/docs/messaging/a2p-10dlc/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 10DLC Overview

> Get started with 10DLC registration for US A2P messaging

10DLC (10-digit long code) is a service offered by the US mobile network operators to explicitly allow application-to-person (A2P) SMS traffic over long code phone numbers. 10DLC numbers are standard US local phone numbers that are 10 digits long, including the area code. 10DLC is designed specifically for commercial A2P messaging.

<Note>
  Plivo now requires customers to register long codes for 10DLC for messaging in the US. Messages sent from numbers that are not associated with registered campaigns will not be delivered.
</Note>

## Benefits

10DLC provides several benefits over alternatives such as unregistered long codes, toll-free numbers, and short codes for messaging campaigns (use cases).

* **Improved deliverability**: Because use cases are preapproved by mobile network operators, messages sent using 10DLC numbers are more likely to reach their intended recipients.
* **Cost savings**:
  * Short code numbers have higher monthly rates than 10DLC numbers. Businesses that can't afford a short code or don't send enough messages to warrant paying for one now have a more cost-effective alternative.
  * Businesses can use their current regular long codes for 10DLC campaigns. This means that businesses can send more messages from their existing phone numbers without having to pay for new ones.
* **High messaging throughput**: 10DLC numbers can deliver up to 4,500 transactions per minute per operator, depending on the characteristics of the brand and campaign use case for which a 10DLC number is approved.
* **Transparent ecosystem**: The registration process detects bad actors, resulting in higher response rates and a reduction in spam texts overall.
* **Lower surcharges, less filtering**: If you have multiple low-volume use cases, you can register a mixed campaign and get your traffic approved beforehand, which will help you pay lower surcharges. Because your sample messages are already approved, less filtering will be applied to your messages.

## Who should use 10DLC?

10DLC is the best phone number choice for most standard use cases, such as delivery notifications and two-factor authentication. They’re also best for businesses that want to have their messages come from familiar local numbers. 10DLC gives businesses the flexibility to create multiple campaigns (one for marketing, one for 2FA, for instance) — and if you have multiple use cases, you can create a mixed campaign.

By comparison, toll-free numbers have lower maximum throughput and take slightly longer to get approval for. And while short codes offer higher maximum throughput than 10DLC, they have higher monthly rental costs and one-time setup fees and take several weeks to provision.

**Can I use long codes without registering them as 10DLC numbers?**

You must register your long codes if you use them for A2P messaging.

Not registering long codes has repercussions that impact your costs and your effectiveness. Carriers can impose fines for using unregistered long codes for A2P traffic. Worse, unregistered traffic is subject to high carrier filtering, which can result in your messages not reaching their destination, wasting the per-message fee you pay for outgoing messages. Ultimately, continued use of unregistered long codes may result in your business losing access to SMS.

## 10DLC specifics: brands and campaigns

The options for brand and campaign registration impact messaging throughput and cost.

### 10DLC brands

A brand is a business entity that a 10DLC number represents. Standard brands have a limit of 3 campaigns and 49 long code numbers per campaign. Throughput varies depending on the brand and campaign’s score, up to a maximum of 4,500 TPM.

| Fee                              | Frequency | Old Pricing (until 31st July 2025)                         | New Pricing (from 1st Aug 2025)                                             |
| :------------------------------- | :-------- | :--------------------------------------------------------- | :-------------------------------------------------------------------------- |
| Brand registration               | One-time  | \$4                                                        | \$4.5                                                                       |
| Brand vetting (optional)         | One-time  | \$40                                                       | \$41.5                                                                      |
| Brand Appeal                     | One-time  | \$10                                                       | \$11                                                                        |
| Campaign Vetting                 | One-time  | \$15                                                       | \$15                                                                        |
| Campaign Recurring               | Monthly   | \$10, or \$1.50 for low-volume campaigns, billed quarterly | \$10, or \$1.50 for low-volume campaigns, billed quarterly<br />(no change) |
| Authentication Plus Verification | One-time  | -                                                          | \$12.5                                                                      |

### 10DLC campaign types

A campaign represents the type of messages the brand intends to send. The terms “campaign” and “use case” are often used interchangeably. Brands may run campaigns of several types.

| Type                        | Details                                                                     |
| --------------------------- | --------------------------------------------------------------------------- |
| 2FA                         | Any two-factor authentication with passcodes used to unlock accounts        |
| Account Notifications       | Notification sent to account holders about changes in accounts              |
| Customer Care               | Customer care interactions by the support and other customer-facing teams   |
| Delivery Notifications      | Updates about the delivery of products and services                         |
| Fraud Alert Messaging       | Notifications of suspicious behavior identified the business                |
| Higher Education            | Messages sent by colleges, universities, and other educational institutions |
| Marketing                   | Communications related to time-bound events and sales                       |
| Polling and Voting          | Surveys, polling, and voting campaigns used for non-political purposes      |
| Public Service Announcement | Messages aimed at creating awareness about important topics                 |
| Security Alert              | Notifications that alert users about a potential breach of systems          |

In addition, businesses can register mixed use cases — a combination of two to five standard use cases — and low-volume mixed use cases, for brands with low throughput requirements.

Standard and mixed-use cases usually require no additional review. There are also special use cases such as 501(c)(3) charity, emergency services, K–12 education, political campaigns, and sweepstakes that may require additional approval, warrant additional fees, or have differences in throughput compared to standard use cases. Plivo does not support registration for special use cases yet.

### A note about vetting

Standard brands can take advantage of an optional vetting process to get higher throughput. Carriers rely on an organization called [The Campaign Registry](https://www.campaignregistry.com/) (TCR) to evaluate each registration based on the information the registrant provides and assign a vetting score to each registration. Vetting scores are calculated by third-party vetting partners such as Aegis Mobile, Campaign Verify, and WMC Global to verify brands using an undisclosed algorithm that takes into account type of organization and other company details. The vetting score determines the maximum throughput the carrier allows for a brand and its campaigns. TCR charges a one-time fee for vetting a 10DLC brand and Plivo passes that cost on to customers. Plivo recommends brands pay for additional vetting if their messaging volume exceeds 6,000 per day.

### Messaging throughput

Message rate limits and throughputs are based on the vetting score the business receives from TCR. US operators define messaging throughput tiers in terms of transactions per minute (TPM) and transactions per day (TPD).

**US messaging throughput comparison by number type:**

| Number Type              | Max Throughput              | Notes                                |
| ------------------------ | --------------------------- | ------------------------------------ |
| 10DLC (low trust score)  | \~15 TPM per carrier        | Unvetted or low-score brands         |
| 10DLC (high trust score) | Up to 4,500 TPM per carrier | Vetted brands with high trust scores |
| Toll-free                | \~3 MPS (180 TPM)           | After toll-free verification         |
| Short code               | \~100 MPS (6,000 TPM)       | Highest throughput, highest cost     |

<Note>
  10DLC throughput depends on your brand's vetting score and campaign type. Plivo recommends paying for additional vetting if your messaging volume exceeds 6,000 per day. TPM limits are per carrier (AT\&T, T-Mobile, etc.), not aggregate.
</Note>

For the latest throughput tier details, see our [10DLC support page](https://support.plivo.com/hc/en-us/articles/360054871572-A2P-10DLC).

## 10DLC number linking

Once you’ve registered your brands and campaigns you must link phone numbers to the campaigns. Once you’ve done that, messages sent from those numbers are considered 10DLC-registered and all the benefits of 10DLC apply.

See our [documentation on the 10DLC registration process](/messaging/a2p-10dlc/registration-process/) for more information.
