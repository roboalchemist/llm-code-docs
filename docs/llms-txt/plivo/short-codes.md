# Source: https://plivo.com/docs/faq/messaging/short-codes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Short Codes

> Short code provisioning, approval process, and messaging limits

Frequently asked questions about short code messaging, application process, and country-specific requirements.

***

## What is a short code?

A short code is a 4-6 digit number designed for high-volume messaging. Short codes offer:

* Highest throughput (up to 100 MPS in US)
* Carrier-approved for A2P and promotional messaging
* Bypass carrier content filtering
* Easy to remember for customers

***

## Which countries support short codes?

| Country       | Digits | Types          | SMS | MMS |
| ------------- | ------ | -------------- | --- | --- |
| United States | 5-6    | Random, Vanity | Yes | Yes |
| Canada        | 5-6    | Random         | Yes | No  |
| Brazil        | 5      | Random         | Yes | No  |
| New Zealand   | 4      | FTEU, Standard | Yes | No  |

***

## What is the throughput for short codes?

| Country       | SMS Throughput |
| ------------- | -------------- |
| United States | 100 MPS        |
| Canada        | 10 MPS         |
| Brazil        | Varies         |
| New Zealand   | Varies         |

***

## How much do short codes cost?

| Country                | Setup Fee | Monthly Rental | Procurement Time |
| ---------------------- | --------- | -------------- | ---------------- |
| United States (Random) | \$1,500   | \$500          | 6-8 weeks        |
| United States (Vanity) | \$1,500   | \$1,000        | 6-8 weeks        |
| Canada                 | \$4,000   | \$700          | 6-8 weeks        |
| Brazil                 | \$0       | \$500          | 4 weeks          |
| New Zealand            | \$156     | \$156          | 3-4 weeks        |

Rental charges are deducted in advance on a quarterly basis.

***

## What is the difference between random and vanity short codes?

| Type   | Description                         | Cost                  |
| ------ | ----------------------------------- | --------------------- |
| Random | Assigned by CSCA                    | Lower monthly rental  |
| Vanity | Custom number (e.g., 75486 = PLIVO) | Higher monthly rental |

Vanity short codes are subject to availability and only available in the US.

***

## What are the requirements for US short codes?

1. Update Terms and Conditions page with carrier-required language
2. Ensure web opt-in forms contain mandated verbiage
3. Configure keyword responses (opt-in, opt-out, HELP)
4. Submit application with usage details

### Required Keywords

| Keyword  | Purpose | Required Response                    |
| -------- | ------- | ------------------------------------ |
| STOP     | Opt-out | Confirmation of opt-out              |
| HELP     | Help    | Program description and contact info |
| YES/JOIN | Opt-in  | Confirmation of subscription         |

***

## What are the requirements for Canada short codes?

* Carriers must review use case and campaign details
* Shared short codes not supported
* Specific language requirements for Terms and Conditions
* Same application steps as US

***

## What are the requirements for Brazil short codes?

* 5 digits, random only
* Messages are Free To End User (FTEU)
* Express consent required before sending
* 35 days notice required to give up a short code
* Unused short codes may be disconnected by regulators

### Content Restrictions (Brazil)

| Allowed                          | Prohibited                      |
| -------------------------------- | ------------------------------- |
| Alerts, Marketing, Notifications | Adult content                   |
| OTP, Promotions, Special offers  | Gambling/casinos                |
| Political, Religious             | Illegal products, Malware, Spam |

***

## What are the requirements for New Zealand short codes?

### Types

| Type                    | Description                     |
| ----------------------- | ------------------------------- |
| Free To End User (FTEU) | All charges to short code owner |
| Standard                | Recipient may be charged        |

### Messaging Requirements

For **Standard** short codes:

* If expecting a reply: include "standard charges apply"
* If message contains URL: include "data charges apply"
* If no response needed: add "No Text Reply"

***

## What triggers a short code audit?

Carriers in US and Canada conduct audits for:

* Deviation from registered use cases
* Non-compliant traffic (prohibited content, missing opt-in)
* Using same short code for multiple brands (shared short code)

Potential outcomes include short code suspension, use case disallowed, or fines.

***

## What qualifies as a shared short code?

When a short code registered for one purpose (e.g., account notifications) is used to send messages for another brand. This is prohibited by carriers.

***

## What are the US Short Code Registry updates?

Effective October 2024, the registry requires:

| Entity            | Required Information                                 |
| ----------------- | ---------------------------------------------------- |
| CSC Registrants   | Legal name, entity type, physical address, URL, FEIN |
| Content Providers | Point of contact (name, email, phone)                |
| Brand Clients     | Organization details and verification                |

Brand clients receive a verification email from Aegis Mobile with a link and PIN for completion.

***

## How do short codes renew?

* Short codes auto-renew by default
* To discontinue: contact Plivo support
* Decommissioned short codes cannot be reactivated
* Failure to notify results in continued rental charges

***

## Can ISVs use short codes?

No. Plivo does not offer short codes for A2P messaging in US or Canada to ISV/Reseller customers.

**Alternatives:**

* Long codes or toll-free numbers for messaging
* [Plivo Verify](https://www.plivo.com/docs/verify/) for short code-based OTP delivery

***

## Related Resources

* [US Messaging (10DLC, Toll-Free)](/docs/messaging/us-messaging)
* [Powerpack](/docs/messaging/powerpack)
* [Short Code API](https://www.plivo.com/docs/messaging/api/)
* [Acceptable Use Policy](https://www.plivo.com/aup/)
