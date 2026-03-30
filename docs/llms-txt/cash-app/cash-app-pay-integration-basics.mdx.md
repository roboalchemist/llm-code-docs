# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/cash-app-pay-integration-basics.mdx

***

## stoplight-id: 6d8b6cc4aa41d

# Cash App Pay Integration Basics

## Overview

Cash App Pay integrations include both front-end and back-end components.

**Front end (client)**

The front end handles customer interactions and must be embedded in your app or website UI. This is done using the Pay Kit SDK, which provides the necessary UI elements and functionality for users to complete payments with Cash App.

**Back end (server)**

The back end handles your server-to-server communication with Cash App. It supports key operations like:

* Payment processing
* Merchant onboarding
* Credential rotation
* Settlements
* Dispute management

To support these, Cash App Pay provides the following APIs and tools:

* Network API
* Management API
* Batch Reporting
  * Settlements
  * Dispute Reporting

![Cash App Pay Integration Basics diagram](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/cap-build-basics.png)

## Front end

### Pay Kit

Pay Kit is a JavaScript SDK that lets you embed fully managed and branded UI elements into an app or website, allowing merchants to accept Cash App Pay online.

It adapts to the user's device:

* On desktop devices, it displays a QR code that customers can scan using Cash App (installed on their mobile device) to authenticate the payment request.

* On mobile devices (such as iOS and Android phones), customers are redirected from the merchant’s checkout experience to Cash App, where they authenticate the payment request. Then they're redirected back to the merchant’s site.

If a merchant’s integration needs more flexibility in how and when the customer request authorization flow is initiated, consider using Pay Kit’s [advanced controls](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started#advanced-controls) capabilities.

To learn more, see the [Pay Kit Developer Guide](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started).

## Back end

### Network API

The Network API is a server-side API that allows your back end to handle key Cash App Pay operations including:

* Payment processing
* Merchant registration
* Dispute handling

It's an entirely server-side API; it can't be called from a browser or point-of-sale (POS) device directly.

To learn more, see the [Network API documentation](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/network-api).

### Management API

The Management API provides tools to automate key aspects of your Cash App Pay integration, including:

* Secure credential rotation
* Managing webhook subscriptions
* Creating scoped API keys, which can be used in a microservices environment to give least-privileged access to services calling the Cash App Pay API

To learn more, see the [Management API documentation](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/management-api).

### Batch reporting

Cash App provides several different reports to help PSPs manage settlements and disputes with Cash App Pay. These reports are uploaded daily (regardless of payment activity) and should be processed on a regular basis.

#### Settlements

Cash App uploads several reconciliation reports daily to a PSP-hosted SFTP server. Process these files regularly to maintain correct settlement reporting.

To learn more, see [Settlements](/cash-app-pay-partner-api/guides/technical-guides/payment-processing/settlement).

<Note>
  Cash App Pay provides a net settlement process, where refunds and disputes amounts are deducted from settlement amounts.
</Note>

#### Disputes

Cash App uploads a dispute report daily to a PSP-hosted SFTP server. Process these files regularly and use them with the Network API to manage customer disputes.

To learn more, see [Disputes Reports](/cash-app-pay-partner-api/guides/technical-guides/payment-processing/disputes/introduction).
