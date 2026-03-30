# Source: https://novita.ai/docs/api-reference/basic-query-usage-based-billing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Usage-based Billing

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="cycleType" type="string" required={true}>
  Billing cycle granularity. Options: `Hour`, `Day`, `Week`, `Month`
</ParamField>

<ParamField query="productCategory" type="string" required={true}>
  Product type. Options:

  * `summary` (Summary bill)
  * `gpu` (GPU instance)
  * `llm` (llm api)
  * `serverless` (Serverless Endpoint)
  * `cloud_storage` (Storage resources)
  * `gen_api` (Image/Video/Audio generation)
</ParamField>

<ParamField query="productName" type="string" required={false}>
  Product name. Supports fuzzy matching.
</ParamField>

<ParamField query="startTime" type="string" required={false}>
  Start time of the billing period to query, timestamp in seconds, default: 0.
</ParamField>

<ParamField query="endTime" type="string" required={false}>
  End time of the billing period to query, timestamp in seconds, default: 0.
</ParamField>

<ParamField query="ownerId" type="string" required={false}>
  Specify instance ID to query.
</ParamField>

## Response Parameters

<ResponseField name="bills" type="object[]" required={true}>
  Pay-as-you-go instance billing information.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="userId" type="string" required={true}>
      User ID to which the instance belongs.
    </ResponseField>

    <ResponseField name="startTime" type="string" required={true}>
      Start time of the bill. Format is Unix timestamp.
    </ResponseField>

    <ResponseField name="endTime" type="string" required={true}>
      End time of the bill. Format is Unix timestamp.
    </ResponseField>

    <ResponseField name="billingMethod" type="string" required={true}>
      Billing method of the instance. A value of 1 indicates pay-as-you-go.
    </ResponseField>

    <ResponseField name="productName" type="string" required={true}>
      Product name.
    </ResponseField>

    <ResponseField name="category" type="string" required={true}>
      Product category.
    </ResponseField>

    <ResponseField name="ownerID" type="string" required={true}>
      Instance ID.
    </ResponseField>

    <ResponseField name="billNum0" type="string" required={true}>
      * llm: input token
      * gpu: number of cards \* billing time
      * storage: storage size \* billing time
    </ResponseField>

    <ResponseField name="billNum1" type="string" required={true}>
      * llm: output token
    </ResponseField>

    <ResponseField name="basePrice0" type="string" required={true}>
      Original Price
    </ResponseField>

    <ResponseField name="basePrice1" type="string" required={true}>
      No significance
    </ResponseField>

    <ResponseField name="discountPrice0" type="string" required={true}>
      * llm: input token unit price
      * others: unit price
    </ResponseField>

    <ResponseField name="discountPrice1" type="string" required={true}>
      * llm: output token unit price
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

    <ResponseField name="productId" type="string" required={true}>
      Product ID.
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).