# Source: https://novita.ai/docs/api-reference/basic-query-fixed-term-billing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Fixed-Term Billing

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="category" type="string" required={false}>
  Product type. default: `summary`, Options:

  * `summary` (Summary bill)
  * `gpu` (GPU instance)
  * `local_storage` (Storage resources)
  * `image` (Image dedicated endpoint)
</ParamField>

<ParamField query="productName" type="string" required={false}>
  Product name. Supports fuzzy matching.
</ParamField>

<ParamField query="startTime" type="string" required={false}>
  The start time of the bill to query, timestamp in seconds, default: 0.
</ParamField>

<ParamField query="endTime" type="string" required={false}>
  The end time of the bill to query, timestamp in seconds, default: 0.
</ParamField>

<ParamField query="ownerId" type="string" required={false}>
  Specify the instance ID to query.
</ParamField>

## Response Parameters

<ResponseField name="bills" type="object[]" required={true}>
  Billing information for fixed-term instances.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="userId" type="string" required={true}>
      User ID to which the instance belongs.
    </ResponseField>

    <ResponseField name="startTime" type="string" required={true}>
      The start time of the bill, timestamp in seconds.
    </ResponseField>

    <ResponseField name="endTime" type="string" required={true}>
      The end time of the bill, timestamp in seconds.
    </ResponseField>

    <ResponseField name="memberId" type="string" required={true}>
      Sub-user ID within the team.
    </ResponseField>

    <ResponseField name="productName" type="string" required={true}>
      Product name.
    </ResponseField>

    <ResponseField name="productCategory" type="string" required={true}>
      Product type.
    </ResponseField>

    <ResponseField name="ownerID" type="string" required={true}>
      Instance ID.
    </ResponseField>

    <ResponseField name="tradeMode" type="string" required={true}>
      Billing method. The value is `monthly`, indicating fixed-term.
    </ResponseField>

    <ResponseField name="tradeType" type="string" required={true}>
      Type of fixed-term. Possible values:

      * `monthly_new_buy` (New purchase).
      * `monthly_re_buy` (Renewal).
      * `monthly_re_config` (Expansion).
    </ResponseField>

    <ResponseField name="basePrice" type="string" required={true}>
      Monthly unit price.
    </ResponseField>

    <ResponseField name="billNum" type="string" required={true}>
      Usage.
    </ResponseField>

    <ResponseField name="amount" type="string" required={true}>
      Total price.
    </ResponseField>

    <ResponseField name="voucherAmount" type="string" required={true}>
      Voucher deduction amount.
    </ResponseField>

    <ResponseField name="payAmount" type="string" required={true}>
      Cash payment amount.
    </ResponseField>

    <ResponseField name="payAmountDisplay" type="string" required={true} />

    <ResponseField name="pricePrecision" type="string" required={true}>
      Price Precision.
    </ResponseField>

    <ResponseField name="createTime" type="string" required={true}>
      Bill creation time.
    </ResponseField>

    <ResponseField name="cycle" type="string" required={true}>
      Billing Cycle.
    </ResponseField>

    <ResponseField name="storageDays" type="string" required={true}>
      Storage service duration (days).
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).