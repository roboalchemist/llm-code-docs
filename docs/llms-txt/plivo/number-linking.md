# Source: https://plivo.com/docs/messaging/api/10dlc/number-linking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Number Linking

> Link and unlink phone numbers from 10DLC campaigns

Use the Number Linking API to associate phone numbers with your 10DLC campaigns. You must link a number to a campaign before using it to send messages. This API allows you to link numbers, retrieve linked numbers, check linking status, and unlink numbers from campaigns.

## API Endpoint

```text BaseURI theme={null}
https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/
```

***

## The Number Object

### Attributes

<ParamField body="campaign_id" type="string">
  Unique identifier for a campaign.
</ParamField>

<ParamField body="campaign_alias" type="string">
  Friendly name for the campaign.
</ParamField>

<ParamField body="usecase" type="string">
  Use case of the campaign.
</ParamField>

<ParamField body="phone_numbers" type="array">
  Array containing status of each number linked to the campaign. Each entry includes `number` and `status` fields.
</ParamField>

### Example Object

```json  theme={null}
{
  "campaign_alias": "ABC Campaign",
  "campaign_id": "CUOGHIN",
  "phone_numbers": [
    {
      "number": "12125557778",
      "status": "PROCESSING"
    }
  ],
  "usecase": "STARTER"
}
```

***

## Link Number to Campaign

Link one or more phone numbers to an existing campaign.

```
POST https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/
```

### Arguments

<ParamField body="numbers" type="array" required>
  The numbers you want to link to a campaign. Numbers should be in [E.164 format](https://en.wikipedia.org/wiki/E.164).
</ParamField>

<ParamField body="url" type="string">
  Fully qualified URL to which status update callbacks for the linking request should be sent.
</ParamField>

<ParamField body="method" type="string">
  The HTTP method to be used when calling the URL defined above. Allowed values: `GET`, `POST`. Defaults to `POST`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.number_link(
      campaign_id="<campaign_id>",
      url="https://example.com/callback",
      method="POST",
      numbers=["<phone_number>"],
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client('<auth_id>', '<auth_token>');
  var callback = {"url": "https://example.com/callback", "method": "POST"};

  client.campaign.linkNumber("<campaign_id>", ["<number>"], callback)
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{
          "numbers": ["12025551111"],
          "url": "https://example.com/callback",
          "method": "POST"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "0b2e010e-b4a1-11ec-a9f5-0242ac110003",
  "message": "Request to link 14156667778 to campaign CUOGHIN was received and is being processed"
}
```

***

## Retrieve All Numbers Linked to a Campaign

Fetch all numbers linked to a particular campaign.

```
GET https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/
```

<Note>
  No arguments need to be passed.
</Note>

The `status` field in the `phone_numbers` array can have the following values:

* `FAILED` - The linking request failed
* `PROCESSING` - The linking request is being processed
* `COMPLETED` - The number has been successfully linked

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.list_number(campaign_id="<campaign_id>")
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client('<auth_id>', '<auth_token>');

  client.campaign.listNumber("<campaign_id>")
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "8010803c-b4a1-11ec-8f25-0242ac110002",
  "campaign_alias": "ABC Campaign",
  "campaign_id": "CUOGHIN",
  "phone_numbers": [
    {
      "number": "12125557777",
      "status": "PROCESSING"
    },
    {
      "number": "12125557778",
      "status": "PROCESSING"
    },
    {
      "number": "12125557779",
      "status": "FAILED"
    }
  ],
  "usecase": "STARTER"
}
```

***

## Retrieve Number Status

Fetch the status of a specific number linked to a campaign.

```
GET https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/{number}/
```

<Note>
  No arguments need to be passed.
</Note>

The `status` field can have the values `FAILED`, `PROCESSING`, or `COMPLETED`.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.get_number(
      campaign_id="<campaign_id>",
      number="<phone_number>"
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client('<auth_id>', '<auth_token>');

  client.campaign.getNumber("<campaign_id>", "<number>")
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/12025551111/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "56df0724-b4a1-11ec-a357-0242ac110002",
  "campaign_alias": "ABC Campaign",
  "campaign_id": "CUOGHIN",
  "phone_numbers": [
    {
      "number": "12125557777",
      "status": "PROCESSING"
    }
  ],
  "usecase": "STARTER"
}
```

***

## Unlink Number from Campaign

Unlink a phone number from a campaign.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/{number}/
```

### Arguments

<ParamField body="url" type="string">
  Fully qualified URL to which status update callbacks for the unlinking request should be sent.
</ParamField>

<ParamField body="method" type="string">
  The HTTP method to be used when calling the URL defined above. Allowed values: `GET`, `POST`. Defaults to `POST`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.number_unlink(
      campaign_id="<campaign_id>",
      number="<phone_number>",
      url="https://example.com/callback",
      method="POST",
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client('<auth_id>', '<auth_token>');
  var callback = {"url": "https://example.com/callback", "method": "POST"};

  client.campaign.unlinkNumber("<campaign_id>", "<number>", callback)
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl -X DELETE -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{
          "url": "https://example.com/callback",
          "method": "POST"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/Number/12025551111/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "eba3f9aa-b4a1-11ec-85a1-0242ac110003",
  "message": "Request to unlink 12125557777 from campaign CUOGHIN was received and is being processed"
}
```
