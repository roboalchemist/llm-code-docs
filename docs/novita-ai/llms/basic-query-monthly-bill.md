# Source: https://novita.ai/docs/api-reference/basic-query-monthly-bill.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Monthly Bill

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response Parameters

<ResponseField name="data" type="object[]" required={true}>
  Monthly billing information.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="billId" type="string" required={true}>
      Unique identifier for the bill.
    </ResponseField>

    <ResponseField name="userId" type="string" required={true}>
      User ID to which the bill belongs.
    </ResponseField>

    <ResponseField name="billingMonth" type="string" required={true}>
      The billing month in YYYY-MM format (e.g., "2025-11").
    </ResponseField>

    <ResponseField name="totalAmount" type="string" required={true}>
      Total amount for the billing month, unit is 0.0001 USD.
    </ResponseField>

    <ResponseField name="originTotalAmount" type="string" required={true}>
      Original total amount before any discounts or adjustments, unit is 0.0001 USD.
    </ResponseField>

    <ResponseField name="voucherPayAmount" type="string" required={true}>
      Amount paid using vouchers, unit is 0.0001 USD.
    </ResponseField>

    <ResponseField name="cashPayAmount" type="string" required={true}>
      Amount paid in cash, unit is 0.0001 USD.
    </ResponseField>

    <ResponseField name="debtAmount" type="string" required={true}>
      Outstanding debt amount, unit is 0.0001 USD.
    </ResponseField>

    <ResponseField name="status" type="string" required={true}>
      Bill status. Possible values:

      * `pending` (Upcoming)
      * `outed` (Payment Due)
      * `paid` (Paid)
      * `overdue` (Overdue)
    </ResponseField>

    <ResponseField name="invoiceUrl" type="string" required={true}>
      URL to download the invoice. Empty string if invoice is not yet available.
    </ResponseField>

    <ResponseField name="startTime" type="string" required={true}>
      Start time of the billing period, Unix timestamp in seconds.
    </ResponseField>

    <ResponseField name="endTime" type="string" required={true}>
      End time of the billing period, Unix timestamp in seconds.
    </ResponseField>

    <ResponseField name="repaidAmount" type="string" required={true}>
      Amount that has been paid, unit is 0.0001 USD.
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).