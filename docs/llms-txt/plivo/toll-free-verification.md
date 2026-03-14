# Source: https://plivo.com/docs/messaging/api/toll-free-verification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Toll-free Verification

> Verify toll-free numbers for US A2P messaging

Before you can use a toll-free number to send application-to-person (A2P) messages in the US and Canada, you must complete the toll-free number verification process. This process identifies the sender, ensures compliance with toll-free messaging best practices, and helps eliminate bad actors from the A2P channel.

During verification, you provide information about your company and messaging use cases. If you're a reseller, you must also provide information about the customers on whose behalf you will send messages.

<Note>
  As of November 8, 2023, unverified toll-free numbers cannot send messages to users in the US and Canada. These messages will be rejected by carriers.
</Note>

## API Endpoint

```text Base URL theme={null}
https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/
```

***

## Use Cases

The following use cases are supported for toll-free verification:

| Use Case                      | Description                                                           |
| ----------------------------- | --------------------------------------------------------------------- |
| 2FA                           | Two-factor authentication with passcodes used to unlock accounts      |
| ACCOUNT\_NOTIFICATION         | Notifications sent to account holders about account changes           |
| CUSTOMER\_CARE                | Customer care interactions by support and customer-facing teams       |
| DELIVERY\_NOTIFICATION        | Updates about delivery of products and services                       |
| FRAUD\_ALERT                  | Notifications of suspicious behavior identified by the business       |
| HIGHER\_EDUCATION             | Messages sent by colleges, universities, and educational institutions |
| MARKETING                     | Communications related to time-bound events and sales                 |
| POLLING\_VOTING               | Surveys, polling, and voting campaigns for non-political purposes     |
| PUBLIC\_SERVICE\_ANNOUNCEMENT | Messages aimed at creating awareness about important topics           |
| SECURITY\_ALERT               | Notifications that alert users about potential security breaches      |

***

## Opt-in Types

You must specify how users consent to receive messages:

| Opt-in Type      | Requirements                                                                        |
| ---------------- | ----------------------------------------------------------------------------------- |
| VERBAL           | Include sample verbal consent collection in a document linked via `optin_image_url` |
| WEB\_FORM        | Include link to the web form in `optin_image_url`                                   |
| PAPER\_FORM      | Include link to the paper form (can be scanned image) in `optin_image_url`          |
| VIA\_TEXT        | Describe the keyword campaign in a document linked via `optin_image_url`            |
| MOBILE\_QR\_CODE | Include the QR code in a document linked via `optin_image_url`                      |

***

## Volume Tiers

Specify your expected monthly message volume using one of these values:

| Volume      |
| ----------- |
| 1,000       |
| 10,000      |
| 100,000     |
| 250,000     |
| 500,000     |
| 750,000     |
| 1,000,000   |
| 5,000,000   |
| 10,000,000+ |

<Note>
  Provide a value that accommodates projected growth for the next six to eight months.
</Note>

***

## The Verification Object

### Attributes

<ParamField body="uuid" type="string">
  The unique identifier for the verification request.
</ParamField>

<ParamField body="profile_uuid" type="string">
  The unique identifier of an existing Plivo profile.
</ParamField>

<ParamField body="number" type="string">
  The toll-free number for which verification is being initiated.
</ParamField>

<ParamField body="usecase" type="list">
  The messaging use case(s) for which the toll-free number will be used. One use case is mandatory; multiple use cases can be added as a list of strings.
</ParamField>

<ParamField body="usecase_summary" type="string">
  Explanation of how messaging will be used on this toll-free number by your business.
</ParamField>

<ParamField body="message_sample" type="string">
  Sample message(s) that your business will send to end users. Multiple samples are allowed.
</ParamField>

<ParamField body="optin_image_url" type="list">
  A valid URL where you submit images explaining the opt-in process. Multiple URLs are allowed as a list of strings.
</ParamField>

<ParamField body="optin_type" type="string">
  Describes how a user opts into receiving text messages.
</ParamField>

<ParamField body="volume" type="string">
  An estimate of the monthly volume of messages you will send from the toll-free number.
</ParamField>

<ParamField body="additional_information" type="string">
  Any additional information related to the website, such as terms of service or privacy policy links.
</ParamField>

<ParamField body="extra_data" type="string">
  Any additional information for your own internal reference.
</ParamField>

<ParamField body="status" type="string">
  The status of the toll-free verification request.
</ParamField>

<ParamField body="rejection_reason" type="string">
  The reason for toll-free verification rejection (if applicable).
</ParamField>

<ParamField body="callback_url" type="string">
  A valid URL where verification-related callbacks will be sent.
</ParamField>

<ParamField body="created" type="datetime">
  The date when the verification request was created.
</ParamField>

<ParamField body="last_modified" type="datetime">
  The date when the verification request was last modified.
</ParamField>

### Example Verification Object

```json  theme={null}
{
  "uuid": "7f4b4d49-8d3f-422c-4f3d-5b0166223a4b",
  "profile_uuid": "bd781875-24f8-4f51-8472-85e697db24dX",
  "number": "18664892XXX",
  "usecase": "2FA",
  "usecase_summary": "We send 2FA codes to customers when they sign up.",
  "message_sample": "Your Plivo verification code is xxxx.",
  "optin_image_url": "https://abc.com/test1",
  "optin_type": "WEB_FORM",
  "volume": "1,000",
  "additional_information": "Privacy policy: https://www.plivo.com/legal/privacy/",
  "extra_data": "Ticket 1",
  "status": "SUBMITTED",
  "callback_url": "https://abc.com/test2",
  "created": "2023-11-07T14:47:00.761439Z",
  "last_modified": "2023-11-07T14:47:00.761412Z"
}
```

***

## Verification Statuses

| Status           | Description                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SUBMITTED        | The carrier has accepted the submission and is reviewing the request.                                                                                                     |
| APPROVED         | The request has been verified by the carrier.                                                                                                                             |
| REJECTED         | The carrier has rejected the verification request. The use case cannot be submitted for verification anymore.                                                             |
| UPDATE\_REQUIRED | The carrier has requested additional data to validate the request. You must provide this information via the Update API within six days, or the request will be rejected. |

***

## Create a Verification Request

Create a new toll-free verification request. You must first create a [Plivo profile](/messaging/api/10dlc/profile/) before starting the verification process.

```
POST https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/
```

### Arguments

<ParamField body="profile_uuid" type="string" required>
  The unique identifier of an existing [Plivo profile](/messaging/api/10dlc/profile/).
</ParamField>

<ParamField body="number" type="string" required>
  The toll-free number in E.164 format for which verification is being initiated. Only US and Canadian toll-free numbers are accepted. Only one number per request.
</ParamField>

<ParamField body="usecase" type="string" required>
  The messaging use case(s). Multiple use cases can be added as a comma-separated string.
  Example: `"2FA, CUSTOMER_CARE"`
</ParamField>

<ParamField body="usecase_summary" type="string" required>
  Explanation of how messaging will be used (max 500 characters).
</ParamField>

<ParamField body="message_sample" type="string" required>
  Sample message(s) that you will send to end users (max 1000 characters).
</ParamField>

<ParamField body="optin_image_url" type="string" required>
  A valid URL where you submit images demonstrating the opt-in process. Multiple URLs allowed as comma-separated string.
</ParamField>

<ParamField body="optin_type" type="string" required>
  How users opt in to messages. Values: `VERBAL`, `WEB_FORM`, `PAPER_FORM`, `VIA_TEXT`, `MOBILE_QR_CODE`
</ParamField>

<ParamField body="volume" type="string" required>
  Expected monthly message volume. Must be one of the allowed volume tier values.
</ParamField>

<ParamField body="additional_information" type="string">
  Additional information such as terms of service or privacy policy links (max 500 characters).
</ParamField>

<ParamField body="extra_data" type="string">
  Information for your internal reference (max 100 characters).
</ParamField>

<ParamField body="callback_url" type="string">
  A valid URL where verification-related callbacks will be sent.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.tollfree_verification.create(
      profile_uuid="<profile_uuid>",
      number="<toll_free_number>",
      usecase="2FA",
      usecase_summary="We send 2FA codes to customers when they sign up.",
      message_sample="Your verification code is xxxx.",
      optin_image_url="https://example.com/optin",
      optin_type="WEB_FORM",
      volume="10,000"
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.tollfreeVerification.create({
      profile_uuid: '<profile_uuid>',
      number: '<toll_free_number>',
      usecase: '2FA',
      usecase_summary: 'We send 2FA codes to customers when they sign up.',
      message_sample: 'Your verification code is xxxx.',
      optin_image_url: 'https://example.com/optin',
      optin_type: 'WEB_FORM',
      volume: '10,000'
  }).then(console.log);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/" \
      -u AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
          "profile_uuid": "<profile_uuid>",
          "number": "<toll_free_number>",
          "usecase": "2FA",
          "usecase_summary": "We send 2FA codes to customers when they sign up.",
          "message_sample": "Your verification code is xxxx.",
          "optin_image_url": "https://example.com/optin",
          "optin_type": "WEB_FORM",
          "volume": "10,000"
      }'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "ffe33a14-81fc-11ee-b92a-0242ac110005",
  "message": "created",
  "uuid": "4a59de5e-204a-47e8-6973-e713f9a1e0ce"
}
```

***

## Retrieve a Verification Request

Get details of a specific toll-free verification request.

```
GET https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/{uuid}/
```

### Arguments

<ParamField path="uuid" type="string" required>
  The unique identifier of the verification request.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.tollfree_verification.get('<uuid>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.tollfreeVerification.get('<uuid>').then(console.log);
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/{uuid}/" \
      -u AUTH_ID:AUTH_TOKEN
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "aecbd496-81fd-11ee-b92a-0242ac110005",
  "uuid": "7f4b4d49-8d3f-422c-4f3d-5b0166223a4b",
  "profile_uuid": "bd781875-24f8-4f51-8472-85e697db24dX",
  "created": "2023-11-07T14:47:00.761439Z",
  "last_modified": "2023-11-07T14:47:00.761412Z",
  "message_sample": "Your Plivo verification code is xxxx.",
  "number": "18664892XXX",
  "optin_image_url": "https://abc.com/test1",
  "optin_type": "WEB_FORM",
  "status": "SUBMITTED",
  "usecase": "2FA",
  "usecase_summary": "We send 2FA codes to customers when they sign up.",
  "volume": "1,000",
  "additional_information": "Privacy policy: https://www.plivo.com/legal/privacy/",
  "extra_data": "Ticket 1",
  "callback_url": "https://abc.com/test2",
  "error_message": ""
}
```

***

## List All Verification Requests

Get the status of all toll-free verification requests for your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/
```

### Query Parameters

<ParamField query="number" type="string">
  Filter by a single toll-free number.
</ParamField>

<ParamField query="status" type="string">
  Filter by verification status.
</ParamField>

<ParamField query="profile_uuid" type="string">
  Filter by profile UUID.
</ParamField>

<ParamField query="usecase" type="string">
  Filter by use case(s) in comma-separated format. This is an exact match.
</ParamField>

<ParamField query="created" type="string">
  Filter by creation date (YYYY-MM-DD format). Supports `created__gt`, `created__gte`, `created__lt`, `created__lte` for range queries. Default window is 7 days; maximum is 30 days.
</ParamField>

<ParamField query="limit" type="integer">
  Number of results per page (1-20). Default: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Number of records to skip for pagination.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.tollfree_verification.list(limit=10, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.tollfreeVerification.list({ limit: 10, offset: 0 }).then(console.log);
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/?limit=10" \
      -u AUTH_ID:AUTH_TOKEN
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "c2b5a6ec-81ff-11ee-9447-0242ac110002",
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 2
  },
  "objects": [
    {
      "uuid": "4bfde431-5317-43cc-644a-2b41e2af4e16",
      "profile_uuid": "bd781875-24f8-4f51-8472-85e697db24d8",
      "number": "18884353XXX",
      "usecase": "ACCOUNT_NOTIFICATION",
      "usecase_summary": "We send account notifications to customers whenever they change the password.",
      "message_sample": "You have successfully updated the password for the Plivo account.",
      "optin_image_url": "https://abc.com/test4",
      "optin_type": "WEB_FORM",
      "volume": "10,000",
      "status": "SUBMITTED",
      "additional_information": "Privacy policy: https://www.plivo.com/legal/privacy/",
      "callback_url": "https://abc.com/test3",
      "created": "2023-11-13T08:35:46.024584Z",
      "last_modified": "2023-11-13T08:35:46.024543Z"
    }
  ]
}
```

***

## Update a Verification Request

Update an existing toll-free verification request. Only requests with status `SUBMITTED` or `UPDATE_REQUIRED` can be updated.

```
POST https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/{uuid}/
```

### Arguments

<ParamField path="uuid" type="string" required>
  The unique identifier of the verification request.
</ParamField>

<ParamField body="profile_uuid" type="string">
  The unique identifier of an existing Plivo profile.
</ParamField>

<ParamField body="usecase" type="string">
  The messaging use case(s) in comma-separated format.
</ParamField>

<ParamField body="usecase_summary" type="string">
  Explanation of how messaging will be used (max 500 characters).
</ParamField>

<ParamField body="message_sample" type="string">
  Sample message(s) that you will send (max 1000 characters).
</ParamField>

<ParamField body="optin_image_url" type="string">
  A valid URL demonstrating the opt-in process.
</ParamField>

<ParamField body="optin_type" type="string">
  How users opt in to messages. Values: `VERBAL`, `WEB_FORM`, `PAPER_FORM`, `VIA_TEXT`, `MOBILE_QR_CODE`
</ParamField>

<ParamField body="volume" type="string">
  Expected monthly message volume.
</ParamField>

<ParamField body="additional_information" type="string">
  Additional information (max 500 characters).
</ParamField>

<ParamField body="extra_data" type="string">
  Information for your internal reference.
</ParamField>

<ParamField body="callback_url" type="string">
  A valid URL for verification callbacks.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.tollfree_verification.update(
      '<uuid>',
      usecase_summary="Updated summary for our 2FA use case."
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.tollfreeVerification.update('<uuid>', {
      usecase_summary: 'Updated summary for our 2FA use case.'
  }).then(console.log);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/{uuid}/" \
      -u AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"usecase_summary": "Updated summary for our 2FA use case."}'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "c74aa53a-8200-11ee-b92a-0242ac110005",
  "message": "Tollfree verification request for uuid 4bfde431-5317-43cc-644a-2b41e2af4e16 updated successfully."
}
```

***

## Delete a Verification Request

Delete an existing verification request. Only requests with status `SUBMITTED`, `PROCESSING`, or `UPDATE_REQUIRED` can be deleted.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/{uuid}/
```

### Arguments

<ParamField path="uuid" type="string" required>
  The unique identifier of the verification request to delete.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.tollfree_verification.delete('<uuid>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.tollfreeVerification.delete('<uuid>').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -X DELETE "https://api.plivo.com/v1/Account/{auth_id}/TollfreeVerification/{uuid}/" \
      -u AUTH_ID:AUTH_TOKEN
  ```
</CodeGroup>

***

## Callbacks

A callback is sent to the `callback_url` (if specified) whenever the verification status changes:

* From `SUBMITTED` to `APPROVED`, `REJECTED`, or `UPDATE_REQUIRED`
* From `UPDATE_REQUIRED` to `APPROVED` or `REJECTED`

### Callback Parameters

<ParamField body="uuid" type="string">
  The unique identifier of the verification request.
</ParamField>

<ParamField body="number" type="string">
  The toll-free number associated with the verification request.
</ParamField>

<ParamField body="status" type="string">
  The current status of the verification request.
</ParamField>

<ParamField body="error_message" type="string">
  Error or rejection reason (if applicable).
</ParamField>

### Example Callback Payload

```json  theme={null}
{
  "uuid": "7f4b4d49-8d3f-422c-4f3d-5b0166223a4b",
  "number": "18664892XXX",
  "status": "APPROVED",
  "error_message": ""
}
```
