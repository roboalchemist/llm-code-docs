# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/payment-processing/disputes/introduction.mdx

***

## stoplight-id: 2c2055f113360

# Disputes

## Dispute filing

Disputes can only be initiated by a Customer. Customers may file a Dispute in two ways:

* For Payments originating from a **linked instrument**, Customers may file Disputes directly with their issuing financial institution or with Block directly through Cash App.
* For Payments originating from a **Cash App stored balance**, Customers must file Disputes with Block directly through Cash App.

## Merchant expectations

Merchants are expected to make a good faith attempt to resolve any issues associated with a Transaction to minimize the number of Disputes filed by Customers. Merchants are expected to be a Customer’s first point of contact for issues, grievances, and other Customer support issues related to a Transaction.

## Dispute notification and types

PSPs will receive notifications about the following types of Disputes. Such notifications will be sent via the CAP Disputes Report, as detailed in the technical documentation available on the Developer Portal. The PSP is able to choose whether, when, and how to respond to Disputes as noted below.

<br />

<table>
  <thead>
    <tr>
      <th>
        Code
      </th>

      <th>
        Description
      </th>

      <th>
        PSP Requirements
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        FR10
      </td>

      <td>
        Customer has no knowledge of the Payment.
      </td>

      <td>
        PSPs will receive notification with no action required, and the disputed payment will be settled back to the PSP. No dispute fee will be charged.
      </td>
    </tr>

    <tr>
      <td>
        FR11
      </td>

      <td>
        Customer has no knowledge of the Payment and liability has shifted to the Merchant due to collusion, fraud monitoring program thresholds, or any other reason.
      </td>

      <td rowspan="8">
        PSPs will receive notification with a due date for response.Response and supporting materials are required for adjudication. 

        <br />

        <br />

        Supporting materials may be provided in one or more of the following formats: PDFs, JPEG / GIF / PNG / TIFF / HEIF / HEIC images, and plain text. PSP will be liable for any Dispute accepted, ignored, or decided in the Customer’s favor.
      </td>
    </tr>

    <tr>
      <td>PE10</td>\
      <td>Payment was processed twice.</td>
    </tr>

    <tr>
      <td>PE11</td>\
      <td>Payment amount differs from agreed amount.</td>
    </tr>

    <tr>
      <td>PE12</td>\
      <td>Customer paid by other means.</td>
    </tr>

    <tr>
      <td>CD10</td>\
      <td>Canceled services.</td>
    </tr>

    <tr>
      <td>CD11</td>\
      <td>Goods or services differ from what was agreed upon for the Payment.</td>
    </tr>

    <tr>
      <td>CD12</td>\
      <td>The goods or services were not received.</td>
    </tr>

    <tr>
      <td>CD13</td>\
      <td>The purchase was canceled or returned, but the Refund has not been processed.</td>
    </tr>
  </tbody>
</table>

<br />

## Dispute timelines

PSPs must provide responses to Disputes within the aforementioned timeframe. Failure to respond within that timeframe will result in the Dispute being decided in the Customer’s favor and liability assumed by the PSP for the disputed Payment(s).

<br />

| Reason Code            | Max days for Customer to open a Dispute                                                                     | Max days for PSP response  (post notification from Block) | Max days for resolution  (post PSP response) |
| :--------------------- | :---------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- | :------------------------------------------- |
| FR10, FR11             | Up to 120 days post Payment date                                                                            | 13                                                        | 45                                           |
| CD11, CD12             | Up to 120 days post Payment date or expected receipt of goods/services (max 540 days from transaction date) | 13                                                        | 45                                           |
| CD13                   | Up to 120 days post Payment date or date of cancellation                                                    | 13                                                        | 45                                           |
| PE10, PE11, PE12, CD10 | Up to 120 days post Payment date                                                                            | 13                                                        | 45                                           |

<br />

### Dispute holds and fees

The amount of any Dispute will be debited from settlement amounts owed to PSPs at the time of Dispute notification. The funds will be disbursed to the PSP at the end of the Dispute process if the outcome is in favor of the PSP.

PSPs will be charged a fee for each Dispute received, regardless of the outcome of any review and adjudication of that Dispute. Disputes resulting from unauthorized Payments for which Block will assume liability will not incur such a fee.
