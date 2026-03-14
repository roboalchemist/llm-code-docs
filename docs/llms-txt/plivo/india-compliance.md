# Source: https://plivo.com/docs/voice/concepts/india-compliance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# India Voice Compliance

> Audit process, consent requirements, and violation handling for India voice calls

Audit process, consent requirements, and handling violations for voice calling in India.

***

## Audit Process

When a recipient complains about an unwanted call:

1. Recipient complains to their telecom provider
2. Provider identifies Plivo as the originating carrier
3. Plivo compliance team identifies your account
4. Audit notice sent to your registered email
5. **Five business days** to respond with evidence

***

## Audit Notice Contents

Audit notices include:

| Field         | Description            |
| ------------- | ---------------------- |
| Caller number | Your Plivo number used |
| Callee number | Recipient's number     |
| Timestamp     | Call time in IST       |
| Call UUID     | Unique call identifier |

***

## Required Evidence

You must provide consent evidence showing:

* Company logo/name
* Recipient's name
* Phone number
* Date consent was given

**Acceptable formats:**

* CRM screenshots
* Signed consent forms
* Digital opt-in records
* Call recordings with verbal consent

***

## Audit Outcomes

| Scenario                     | Outcome                                           |
| ---------------------------- | ------------------------------------------------- |
| Valid evidence within 5 days | Audit closed                                      |
| Insufficient evidence        | Request for additional documentation              |
| No response in 5 days        | Number disconnection, possible account suspension |
| Multiple complaints          | Potential TRAI blacklisting                       |

<Warning>
  **TRAI Blacklisting:** Repeated violations can result in your business being blacklisted by the Telecom Regulatory Authority of India (TRAI), preventing you from using Indian telecom services.
</Warning>

***

## Best Practices to Avoid Audits

| Practice                     | Description                                   |
| ---------------------------- | --------------------------------------------- |
| **Call only opted-in users** | Never call without explicit consent           |
| **Honor rejections**         | Remove users who request to stop calls        |
| **Refresh consent**          | TRAI requires consent renewal every 6 months  |
| **Maintain records**         | Keep consent evidence for at least 1 year     |
| **Use DND scrubbing**        | Check numbers against Do Not Disturb registry |

***

## Consent Requirements (TRAI)

Per TRAI regulations:

* Consent must be explicit and documented
* Consent expires after 6 months — must be renewed
* Users can withdraw consent at any time
* Maintain audit trail of all consent records

***

## Related

* [Voice Calling in India](india-calling) - Requirements and setup
* [160-Series Number Provisioning](160-series-provisioning) - Setup guide for BFSI transactional voice numbers
* [Rent India Numbers](/numbers/rent-india-numbers) - KYC and number rental
* [DLT Registration for SMS](https://www.plivo.com/docs/messaging/concepts/dlt-registration-process) - SMS compliance requirements
