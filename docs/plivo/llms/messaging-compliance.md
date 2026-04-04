# Source: https://plivo.com/docs/faq/messaging/messaging-compliance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Messaging Compliance

> 10DLC registration, A2P compliance, campaign approval, and rejection reasons

Frequently asked questions about sender IDs, country-specific regulations, DND/opt-out management, and delivery alerts.

***

## What is a Sender ID?

Sender ID is the name or number that appears as the message sender on the recipient's device.

### Sender ID Types

| Type             | Example        | Support           |
| ---------------- | -------------- | ----------------- |
| **Alphanumeric** | "MyBrand"      | Country-dependent |
| **Numeric**      | "+14151234567" | Most countries    |
| **Short Code**   | "12345"        | US, Canada, UK    |

***

## What are the Sender ID country categories?

| Category             | Description                          |
| -------------------- | ------------------------------------ |
| **Dynamic**          | Instant sender ID support            |
| **Pre-registration** | Requires carrier approval before use |
| **Not Supported**    | Must use numeric sender ID           |

***

## Which countries require Sender ID pre-registration?

| Country   | Registration Fee | Recurring Fee | ETA       |
| --------- | ---------------- | ------------- | --------- |
| Singapore | Yes              | Monthly       | Varies    |
| India     | DLT registration | —             | 2-4 weeks |
| UK        | Yes              | —             | 1-2 weeks |

Check [Plivo coverage](https://www.plivo.com/coverage/) for country-specific requirements.

***

## How do I register a Sender ID?

1. Navigate to **Messaging > Settings > Sender ID**
2. Select country
3. Submit registration with required documents
4. Wait for carrier approval

***

## What are the requirements for sending SMS to India?

| Business Location | Currency | Route         | Requirements                       |
| ----------------- | -------- | ------------- | ---------------------------------- |
| India             | INR      | Domestic      | GST registration, DLT registration |
| Outside India     | USD      | International | —                                  |

### DLT Registration

* Required for all domestic SMS
* Register templates and headers
* See [DLT documentation](https://www.plivo.com/docs/messaging/concepts/dlt/)

### PE-TM Binding Chain

* TRAI requirement for domestic traffic
* Principal Entity must bind with Telemarketer
* Complete binding before sending

***

## How to comply with TRAI's PE-TM Binding Chain requirement?

The Principal Entity (PE) must bind with Telemarketer (TM) before sending domestic SMS in India. This is a TRAI regulatory requirement.

Complete the binding process through the DLT portal before initiating messaging.

***

## What are the Singapore Sender ID requirements?

**Full SMS Sender ID Registry (SSIR):**

* All sender IDs must be registered with SGNIC
* Unregistered sender IDs are blocked
* Registration required for all organizations

***

## What are the UK SMS regulations?

**A2P SMS Filtering:**

* Carriers actively filter unregistered traffic
* Register sender IDs to avoid filtering
* Follow UK carrier guidelines

***

## Can I send messages from Canadian long codes to US?

**Cross-Border Restrictions:**

* Canadian long codes cannot send to US
* Use US numbers for US destinations
* Toll-free and short codes work cross-border

***

## What keywords trigger the "Do Not Disturb" (DND) feature?

Plivo automatically recognizes these opt-out keywords (case-insensitive):

| Keyword     | Action  |
| ----------- | ------- |
| STOP        | Opt out |
| END         | Opt out |
| QUIT        | Opt out |
| CANCEL      | Opt out |
| UNSUBSCRIBE | Opt out |
| UNSUB       | Opt out |
| STOP ALL    | Opt out |

***

## What happens when someone opts out?

1. Recipient sends STOP keyword
2. Plivo adds number to suppression list
3. Future messages to that number are blocked
4. Messages fail with DND error code

***

## Can my customers opt back in after opting out?

Yes. Opt-in keywords:

| Keyword | Action      |
| ------- | ----------- |
| UNSTOP  | Opt back in |
| START   | Opt back in |

***

## Can I reply to customers who have opted out?

No. Messages to opted-out users:

* Are blocked by Plivo
* Fail with appropriate error code
* Are not charged

***

## How can I ensure my messages adhere to DND regulations?

* Include opt-out instructions in every message
* Example: "Reply STOP to opt out"
* Monitor inbound messages for complaints
* Only message explicit opt-ins

***

## Can I receive email alerts for message delivery issues?

Yes. Plivo monitors delivery rates and alerts you to issues.

### Alert Types

| Alert        | Trigger                            |
| ------------ | ---------------------------------- |
| **Outbound** | Significant drop in delivery rate  |
| **Inbound**  | Issues delivering to your endpoint |

***

## I've received an outbound delivery email alert from Plivo. What should I do?

1. Review message content for spam triggers
2. Check number registration status
3. Verify destination numbers are valid

**Email includes:**

* Total messages sent in past hour
* Phone numbers with low delivery
* Suggested actions

**Frequency:** Maximum once per day per destination country

***

## I've received an inbound delivery email alert from Plivo. What should I do?

1. Check endpoint availability
2. Verify URL configuration
3. Review server logs for errors

**Evaluation:**

* Checks delivery rate every 15 minutes
* Looks at messages from past hour
* Alerts if delivery issues detected

**Frequency:** Maximum once per day

***

## Why did my outbound SMS delivery fail?

**Common causes:**

* Carrier filtering
* Invalid numbers
* Content violations

**Inbound issues:**

* Endpoint timeout
* Server errors (5xx)
* Invalid URL configuration

***

## What content is prohibited in messaging?

* Unsolicited messages (spam)
* Fraudulent or deceptive content
* Violence, hate speech, obscenity
* Illegal drugs or substances
* Marketing to children under 13 (requires extra carrier review)

***

## What is age gating and when is it required?

Messages with age-restricted content (SHAFT: Sex, Hate, Alcohol, Firearms, Tobacco) must include age verification before opt-in.

***

## What are the best practices for messaging compliance?

### Consent

* Obtain explicit opt-in before messaging
* Document consent method and timestamp
* Honor opt-outs immediately

### Content

* Avoid spam triggers
* Include sender identification
* Provide opt-out instructions

### Record Keeping

* Maintain opt-in records
* Log opt-out requests
* Document consent methods

***

## What are the penalties for messaging compliance violations?

Violations of messaging standards or [Acceptable Use Policy](https://www.plivo.com/aup/) result in penalties.

### Penalty Tiers

| Tier   | Violation Type                             | Fine        |
| ------ | ------------------------------------------ | ----------- |
| Tier 1 | Phishing, smishing, social engineering     | \$2,000 USD |
| Tier 2 | Illegal content                            | \$1,000 USD |
| Tier 3 | Other violations (including SHAFT content) | \$500 USD   |

Fines apply regardless of country. If a carrier imposes a fine, the amount is deducted from your account.

### Consequences

* Single violation: SID or campaign suspension
* Serious violation: All SIDs/campaigns suspended without notice
* Repeated violations: Account suspension

***

## Related Resources

* [Messaging API Overview](/docs/messaging/messaging-api)
* [US Messaging](/docs/messaging/us-messaging)
* [ISV Guidelines](/docs/messaging/isv-guidelines)
* [DLT Registration](https://www.plivo.com/docs/messaging/concepts/dlt/)
* [Acceptable Use Policy](https://www.plivo.com/aup/)
