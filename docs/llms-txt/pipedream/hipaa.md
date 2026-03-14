# Source: https://pipedream.com/docs/privacy-and-security/hipaa.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# HIPAA Compliance

Pipedream can [sign Business Associate Addendums (BAAs)](/privacy-and-security/hipaa/#signing-a-business-associate-addendum) for Business customers intending to pass PHI to Pipedream. We can also provide a third-party SOC 2 report detailing our HIPAA-related controls.

## HIPAA-eligible services

* [Workflows](/workflows/building-workflows/)
* [Event sources](/workflows/building-workflows/triggers/)
* [Data stores](/workflows/data-management/data-stores/)
* [Destinations](/workflows/data-management/destinations/)
* [Pipedream Connect](/connect/)

### Ineligible services

Any service not listed in the [HIPAA-eligible services](/privacy-and-security/hipaa/#hipaa-eligible-services) section is not eligible for use with PHI under HIPAA. Please reach out to [Pipedream support](https://pipedream.com/support) if you have questions about a specific service.

The following services are explicitly not eligible for use with PHI under HIPAA.

* [v1 workflows](/deprecated/migrate-from-v1/)
* [File stores](/workflows/data-management/file-stores/)

## Your obligations as a customer

If you are a covered entity or business associate under HIPAA, you must ensure that [you have a BAA in place with Pipedream](/privacy-and-security/hipaa/#signing-a-business-associate-addendum) before passing PHI to Pipedream.

You must also ensure that you are using Pipedream in a manner that complies with HIPAA. This includes:

* You may only use [HIPAA-eligible services](/privacy-and-security/hipaa/#hipaa-eligible-services) to process or store PHI
* You may not include PHI in Pipedream resource names, like the names of projects or workflows

## Signing a Business Associate Addendum

Pipedream is considered a Business Associate under HIPAA regulations. If you are a Covered Entity or Business Associate under HIPAA, you must have a Business Associate Agreement (BAA) in place with Pipedream before passing PHI to Pipedream. This agreement is an addendum to our standard terms, and outlines your obligations as a customer and Pipedream’s obligations as a Business Associate under HIPAA.

Please request a BAA by visiting [https://pipedream.com/support](https://pipedream.com/support).

## Requesting information on HIPAA controls

Please request compliance reports from [https://pipedream.com/support](https://pipedream.com/support). Pipedream can provide a SOC 2 Type II report covering Security controls, and a SOC 2 Type I report for Confidentiality and Availability. In 2025, Pipedream plans to include Confidentiality and Availability controls in our standard Type II audit.

Built with [Mintlify](https://mintlify.com).
