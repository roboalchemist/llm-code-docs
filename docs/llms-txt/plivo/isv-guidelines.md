# Source: https://plivo.com/docs/faq/messaging/isv-guidelines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# A2P Guidelines for ISVs

> ISV guidelines for building and selling A2P messaging applications on Plivo

Frequently asked questions about Plivo's guidelines for Independent Software Vendors (ISVs) providing A2P messaging and voice services.

***

## What is an ISV?

Independent Software Vendors (ISVs) provide A2P messaging and voice services to businesses, helping with campaign planning, content creation, deployment, monitoring, and analytics. A2P content includes P2P-like messaging, marketing, notifications, OTP authentication, and more.

***

## What types of brands can ISVs onboard?

ISVs should only onboard traffic from **direct brands**—businesses that engage directly with end subscribers and collect opt-ins.

ISVs working with other ISVs need prior approval from Plivo.

***

## How should ISVs segregate traffic between brands?

ISVs must separate traffic for each end brand using sub-accounts:

* Create a sub-account for each end brand
* Use that sub-account for all messaging and calling API requests
* Maintain clear separation between brands

***

## How does geography access work for ISVs?

By default, access to all regions outside the US is disabled at the main account level.

ISVs should enable access to relevant geographies only after completing KYC for each end brand.

***

## Can ISVs use short codes in the US and Canada?

No. Plivo does not offer short codes for A2P messaging in the US or Canada to ISV/Reseller customers.

**Alternatives:**

* Use long codes or toll-free numbers for messaging traffic
* For OTP delivery, use [Plivo Verify](https://www.plivo.com/docs/verify/) for short code-based OTP at no additional cost

***

## Can I use the same sender ID for multiple brands?

No. All messaging and calling compliance flows must be completed for each end brand separately.

If a sender ID is approved for Brand B1, it cannot be used for Brand B2, even for legitimate use cases like 2FA.

***

## What content is prohibited for ISVs?

The following categories are strictly prohibited. No campaign or toll-free verification will be supported:

| Category    | Examples                                            |
| ----------- | --------------------------------------------------- |
| Financial   | Mortgage, loans, credit repair, debt collection     |
| Investment  | Stock alerts, cryptocurrency, high-risk investments |
| Marketing   | Lead generation, affiliate marketing, MLM           |
| Employment  | Deceptive work-from-home, job postings              |
| Real Estate | Sales, servicing                                    |
| Gambling    | Gambling, sweepstakes                               |
| Regulated   | Tobacco/vape, illegal drugs, SHAFT content          |

**SHAFT:** Sex, Hate, Alcohol, Firearms, and Tobacco

***

## Can I use URL shorteners?

| Type                                    | Allowed |
| --------------------------------------- | ------- |
| Public shorteners (bit.ly, tinyurl.com) | No      |
| ISV-owned shorteners                    | No      |
| Brand-owned shorteners                  | Yes     |

***

## What are the opt-out requirements for ISVs?

* If an end subscriber opts out, do not contact them again regardless of sender ID used
* Monitor incoming messages and remove opted-out customers from contact lists
* Subscribers on national do-not-call lists must be excluded
* Subscribe to available DNC lists

***

## How does keyword monitoring work?

Plivo blocks outbound messages containing specific keywords that may violate the AUP.

* ISVs can request to whitelist specific keywords on a case-by-case basis
* Decisions are at Plivo's compliance team discretion
* Two weeks notice given before enforcement of changes

***

## Can ISVs redact message content or phone numbers?

No. ISVs cannot redact message content or destination phone numbers. This allows Plivo's compliance team to effectively monitor for non-compliance.

***

## What happens if an ISV violates compliance rules?

| Violation Type      | Action                                                        |
| ------------------- | ------------------------------------------------------------- |
| Single violation    | SID or campaign suspension                                    |
| Serious violation   | All SIDs/campaigns under sub-account suspended without notice |
| Multiple violations | Account suspension                                            |

***

## How should ISVs report security compromises?

If an ISV detects a compromise affecting message or call traffic:

1. Report immediately via email to [security-report@plivo.com](mailto:security-report@plivo.com)
2. Include relevant supporting details

***

## Related Resources

* [Messaging Compliance](/docs/messaging/messaging-compliance)
* [Acceptable Use Policy](https://www.plivo.com/aup/)
* [Plivo Verify](https://www.plivo.com/docs/verify/)
* [Sub-account API](https://www.plivo.com/docs/account/api/subaccount/)
