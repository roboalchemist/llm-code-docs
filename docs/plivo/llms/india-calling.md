# Source: https://plivo.com/docs/voice/concepts/india-calling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Voice Calling in India

> Requirements and setup for voice calling within India

Requirements, eligibility, and setup for voice calling within India.

***

## Requirements

| Requirement               | Details                                   |
| ------------------------- | ----------------------------------------- |
| **Business registration** | India-registered businesses only          |
| **KYC compliance**        | Required before renting Indian numbers    |
| **Caller ID**             | Must use Plivo-rented Indian phone number |
| **Media anchoring**       | Both call legs must stay within India     |

For number rental requirements, see [Rent India Numbers](/numbers/rent-india-numbers).

***

## Eligibility

Only businesses registered in India can:

* Rent Indian phone numbers
* Make domestic calls within India
* Use India domestic routes

Businesses outside India must use international routes at higher rates without domestic Caller ID.

***

## Media Anchoring Rule

Both legs of a call must originate and terminate within India. Violating this causes calls to fail with `violates_media_anchoring` hangup cause.

***

## Compliant Call Architecture

| Call Type      | Requirement                        |
| -------------- | ---------------------------------- |
| **Inbound**    | India to India                     |
| **Outbound**   | Indian number to India destination |
| **Conference** | All participants must be in India  |

***

## Account Setup for India

India-registered businesses needing both India and international calling:

1. Create two separate Plivo accounts with different email addresses
2. Request India trial account via [sales form](https://www.plivo.com/contact/sales/)
3. Use Indian credit card for INR account payments

***

## Related

* [Rent India Numbers](/numbers/rent-india-numbers) - KYC and number rental process
* [India Voice Compliance](india-compliance) - Audit process and consent requirements
* [160-Series Number Provisioning](160-series-provisioning) - Setup guide for BFSI transactional voice numbers
* [Payments](/faq/billing-and-invoices/payments) - Payment methods for India
