# Source: https://plivo.com/docs/numbers/regulatory-compliance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Regulatory Compliance

> Phone number verification requirements and compliance applications

Many phone numbers have compliance requirements set by regional regulatory bodies. This guide explains the verification process and how to use Compliance Applications.

<Note>
  **For India numbers:** See [India Calling Guidelines](/faq/voice-api-and-SIP-trunking/india-calling) for specific compliance requirements.
</Note>

***

## Overview

Plivo provides virtual phone numbers across [multiple countries](https://www.plivo.com/virtual-phone-numbers/coverage/us/). Ownership and usage of these numbers may require approval from regulatory bodies, involving submission of information and documents for review.

### Requirements Vary By

* **Country** of the phone number
* **Number type:** local, toll-free, or mobile
* **User type:** business or individual

### Example Requirement

For a business to own a toll-free number in a country, the applicant might need:

* An address proof within that country
* Company representative identification

***

## Compliance Review Process

1. **Search** for a number on the [Plivo console](https://cx.plivo.com/phone-numbers)
2. **View regulations** associated with that number
3. **Submit** required compliance information and documentation
4. **Wait for review** by Plivo and carrier partners
5. **Activation** upon successful verification

***

## Compliance Applications

A [Compliance Application](https://cx.plivo.com/phone-numbers?tab=compliance) bundles the documents required for a unique combination of:

* Phone number country
* Number type
* User type

### Benefits

* **Clear visibility** into required documents before purchase
* **Reuse documents** across multiple countries
* **Multiple collections** for different end users
* **Easy association** with phone numbers

***

## Creating a Compliance Application

1. Go to **Phone Numbers > Compliance Application** in the [Plivo console](https://cx.plivo.com/phone-numbers?tab=compliance)
2. Select the **country**, **number type**, and **end user type**
3. Fill in the required information fields
4. Upload required documents
5. Submit for review

### Required Information (varies by country)

* Business name and registration details
* End user address
* Authorized representative details
* Proof of address
* Identity documents

***

## Linking to Phone Numbers

After your Compliance Application is approved:

1. Go to **Phone Numbers > Search**
2. Find a number in the same country/type as your application
3. Select your Compliance Application when purchasing
4. The number will be activated once linked

***

## Application Status

| Status                 | Description                                |
| ---------------------- | ------------------------------------------ |
| **Draft**              | Application started but not submitted      |
| **Pending**            | Submitted and awaiting review              |
| **Approved**           | Documents verified, can link to numbers    |
| **Rejected**           | Documents not accepted, needs resubmission |
| **More Info Required** | Additional documents or corrections needed |

***

## Document Guidelines

### Address Proof

* Utility bill (within 3 months)
* Bank statement (within 3 months)
* Government-issued document showing address

### Identity Documents

* Passport
* National ID card
* Driver's license

### Business Documents

* Certificate of incorporation
* Business registration certificate
* Tax registration document

<Note>
  Document requirements vary by country. Check the specific requirements when creating your Compliance Application.
</Note>

***

## Frequently Asked Questions

### How long does approval take?

Review times vary by country and carrier, typically ranging from 1-10 business days.

### Can I use one application for multiple numbers?

Yes, an approved Compliance Application can be linked to multiple phone numbers of the same country and type.

### What happens if my application is rejected?

You'll receive feedback on why the application was rejected. You can correct the issues and resubmit. See **Troubleshooting Rejected Applications** below for common reasons.

### Are documents stored securely?

Yes, all documents are encrypted and stored securely in compliance with data protection regulations.

***

## Troubleshooting Rejected Applications

<AccordionGroup>
  <Accordion title="Document quality issues">
    **Common problems:**

    * Document is blurry or unreadable
    * Document is cropped or cut off
    * Document is expired
    * Wrong document type submitted

    **Solutions:**

    * Upload high-resolution scans (at least 300 DPI)
    * Ensure all corners and text are visible
    * Check expiration dates before submitting
    * Verify document matches the requested type
  </Accordion>

  <Accordion title="Information mismatch">
    **Common problems:**

    * Name on documents doesn't match application
    * Address on proof doesn't match entered address
    * Business name differs between documents

    **Solutions:**

    * Use exact legal name as shown on official documents
    * Copy address exactly as it appears on proof
    * Ensure consistency across all submitted documents
  </Accordion>

  <Accordion title="Missing required documents">
    **Common problems:**

    * Not all required documents uploaded
    * Document doesn't meet country-specific requirements
    * Additional authorization needed

    **Solutions:**

    * Review all requirements before submitting
    * Check country-specific rules in the application form
    * Contact support if unsure which documents are needed
  </Accordion>

  <Accordion title="Account verification issues">
    **Common problems:**

    * Plivo account not fully verified
    * Account suspended or restricted
    * Enterprise account required for certain countries

    **Solutions:**

    * Complete account verification in Console → Account
    * Resolve any outstanding account issues
    * Contact support to upgrade if Enterprise is required
  </Accordion>

  <Accordion title="Country-specific rejections">
    **India numbers:**

    * Only India-registered businesses can rent Indian numbers
    * KYC documents must be from Indian authorities
    * GST registration may be required

    **UK/EU numbers:**

    * Local address proof often required
    * Business must be registered in region

    **US toll-free:**

    * Toll-Free Verification (TFV) may be required
    * Business use case must be clearly described
  </Accordion>
</AccordionGroup>

### Cannot Purchase Number (Account Disabled)

If you see "account disabled" when trying to purchase:

1. **Check account status** in Console → Account
2. **Verify your account** if verification is pending
3. **Check for violations** - review any emails from Plivo about policy issues
4. **Contact support** if you believe this is an error

### How to Resubmit a Rejected Application

1. Go to **Phone Numbers → Compliance Application**
2. Find your rejected application
3. Click **View Details** to see rejection reason
4. Click **Edit** to update documents/information
5. Address the specific feedback provided
6. Resubmit for review

***

## Related

* [Compliance Applications API](/numbers/compliance-applications) - API reference for managing compliance programmatically
* [Phone Numbers](/numbers/phone-numbers) - Search and buy numbers
* [Account Phone Numbers](/numbers/account-phone-numbers) - Manage your numbers
* [Number Porting](/numbers/number-porting) - Port existing numbers to Plivo
