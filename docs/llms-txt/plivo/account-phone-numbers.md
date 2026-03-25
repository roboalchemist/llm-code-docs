# Source: https://plivo.com/docs/numbers/account-phone-numbers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Account Phone Numbers API

> Manage phone numbers in your Plivo account

Manage phone numbers that you've rented from Plivo or added from your carrier. List, retrieve, update, and unrent numbers.

**API Endpoint**

```
https://api.plivo.com/v1/Account/{auth_id}/Number/
```

***

## The AccountPhoneNumber Object

### Attributes

<ParamField body="number" type="string">
  The phone number.
</ParamField>

<ParamField body="alias" type="string">
  Alias for the phone number.
</ParamField>

<ParamField body="subaccount" type="string">
  Associated subaccount (null if main account).
</ParamField>

<ParamField body="added_on" type="string">
  Date rented. Format: `YYYY-MM-DD`.
</ParamField>

<ParamField body="application" type="string">
  Linked application URI.
</ParamField>

<ParamField body="carrier" type="string">
  Plivo or incoming carrier name.
</ParamField>

<ParamField body="region" type="string">
  City and country.
</ParamField>

<ParamField body="number_type" type="string">
  Number type. Values: `local`, `fixed`, `tollfree`, `mobile`, `national`.
</ParamField>

<ParamField body="monthly_rental_rate" type="string">
  Monthly fee (USD).
</ParamField>

<ParamField body="renewal_date" type="string">
  Next billing date. Format: `YYYY-MM-DD`.
</ParamField>

<ParamField body="sms_enabled" type="boolean">
  Can receive SMS.
</ParamField>

<ParamField body="sms_rate" type="string">
  Cost per SMS (USD).
</ParamField>

<ParamField body="mms_enabled" type="boolean">
  Can receive MMS.
</ParamField>

<ParamField body="mms_rate" type="string">
  Cost per MMS (USD).
</ParamField>

<ParamField body="voice_enabled" type="boolean">
  Can receive calls.
</ParamField>

<ParamField body="voice_rate" type="string">
  Cost per minute (USD).
</ParamField>

<ParamField body="cnam_lookup" type="string">
  CNAM lookup status. Values: `enabled`, `disabled`, `null`.
</ParamField>

<ParamField body="cnam" type="string">
  Caller ID name for outbound calls.
</ParamField>

<ParamField body="tendlc_registration_status" type="string">
  10DLC status. Values: `UNREGISTERED`, `PROCESSING`, `COMPLETED`.
</ParamField>

<ParamField body="tendlc_campaign_id" type="string">
  Linked 10DLC campaign ID.
</ParamField>

<ParamField body="toll_free_sms_verification" type="string">
  TF SMS verification. Values: `UNVERIFIED`, `PENDING_VERIFICATION`, `VERIFIED`.
</ParamField>

<ParamField body="profile_uuid" type="string">
  UUID of the linked business profile. `null` if no profile is linked.
</ParamField>

<ParamField body="caller_reputation_status" type="string">
  Caller Reputation activation status. Values: `PENDING`, `ACTIVE`, `FAILED`, `NOT_ENROLLED`, `null`.
</ParamField>

<ParamField body="resource_uri" type="string">
  URI to the number resource.
</ParamField>

### Example Object

```json  theme={null}
{
  "number": "17609915566",
  "alias": null,
  "sub_account": null,
  "added_on": "2023-02-14",
  "application": "/v1/Account/MA2025RK4E639VJFZAGV/Application/29986316244302815/",
  "carrier": "Plivo",
  "region": "California, UNITED STATES",
  "number_type": "local",
  "monthly_rental_rate": "0.80000",
  "renewal_date": "2023-05-10",
  "sms_enabled": true,
  "sms_rate": "0.00000",
  "voice_enabled": true,
  "voice_rate": "0.00850",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Number/17609915566/",
  "tendlc_campaign_id": "2FA_campaign",
  "tendlc_registration_status": "COMPLETED",
  "toll_free_sms_verification": null,
  "profile_uuid": null,
  "caller_reputation_status": null
}
```

***

## List Account Phone Numbers

Returns all phone numbers in your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Number/
```

### Query Parameters

<ParamField query="type" type="string">
  Filter by type. Values: `local`, `mobile`, `fixed`, `national`, `tollfree`.
</ParamField>

<ParamField query="number_startswith" type="string">
  Filter by prefix.
</ParamField>

<ParamField query="subaccount" type="string">
  Filter by subaccount.
</ParamField>

<ParamField query="alias" type="string">
  Filter by exact alias.
</ParamField>

<ParamField query="services" type="string">
  Filter by services. Values: `voice`, `sms`, `mms`, or combinations.
</ParamField>

<ParamField query="cnam_lookup" type="string">
  Filter by CNAM status. Values: `enabled`, `disabled`.
</ParamField>

<ParamField query="renewal_date" type="string">
  Filter by renewal date. Format: `YYYY-MM-DD`. Supports variants: `renewal_date__gt`, `renewal_date__gte`, `renewal_date__lt`, `renewal_date__lte`.
</ParamField>

<ParamField query="tendlc_registration_status" type="string">
  Filter by 10DLC status. Values: `unregistered`, `in_progress`, `registered`.
</ParamField>

<ParamField query="tendlc_campaign_id" type="string">
  Filter by campaign ID.
</ParamField>

<ParamField query="toll_free_sms_verification" type="string">
  Filter by TF verification status. Values: `unverified`, `pending_verification`, `verified`.
</ParamField>

<ParamField query="limit" type="integer">
  Results per page. Max: 20. Default: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Pagination offset.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.numbers.list(limit=10, type='local')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.numbers.list({ limit: 10, type: 'local' })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.numbers.list(limit: 10, type: 'local')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->numbers->list(['limit' => 10, 'type' => 'local']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.number.Number;

  Plivo.init("<auth_id>", "<auth_token>");

  ListResponse<Number> response = Number.lister()
      .limit(10)
      .list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Number.List(limit: 10, type: "local");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import (
      "fmt"
      "github.com/plivo/plivo-go/v7"
  )

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      response, _ := client.Numbers.List(plivo.NumberListParams{Limit: 10})
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/Number/?limit=10&type=local" \
    -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

***

## Get an Account Phone Number

Retrieve details of a specific phone number.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Number/{number}/
```

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.numbers.get(number='17609915566')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.numbers.get('17609915566')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.numbers.get('17609915566')
  puts response
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/Number/17609915566/" \
    -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

***

## Update an Account Phone Number

Change the application, subaccount, or alias for a phone number.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Number/{number}/
```

### Arguments

<ParamField body="app_id" type="string">
  Application to assign (or Zentrunk inbound trunk\_id).
</ParamField>

<ParamField body="subaccount" type="string">
  Subaccount auth\_id to transfer number to.
</ParamField>

<ParamField body="alias" type="string">
  Alias for the number.
</ParamField>

<ParamField body="compliance_id" type="string">
  ID of an approved compliance record to link to this number. The compliance record must match the number's country and type. See [Compliance API](/numbers/compliance) for details.
</ParamField>

<ParamField body="cnam_lookup" type="string">
  CNAM lookup. Values: `enabled`, `disabled`. US only.
</ParamField>

<ParamField body="cnam" type="string">
  Caller ID name for outbound calls.
</ParamField>

<ParamField body="cnam_callback_url" type="string">
  URL for CNAM registration updates.
</ParamField>

<ParamField body="cnam_callback_method" type="string">
  HTTP method. Values: `GET`, `POST`. Default: `POST`.
</ParamField>

<ParamField body="caller_reputation" type="string">
  Enable or disable Caller Reputation for this number. Values: `enabled`, `disabled`. When set to `enabled`, `profile_uuid` is required. US local and toll-free numbers only. Early access beta. See [Caller Reputation](/voice/concepts/caller-reputation) for details.
</ParamField>

<ParamField body="profile_uuid" type="string">
  UUID of the business profile to associate with this number. Required when `caller_reputation` is set to `enabled`.
</ParamField>

<ParamField body="caller_reputation_callback_url" type="string">
  URL to receive Caller Reputation status update notifications.
</ParamField>

<ParamField body="caller_reputation_callback_method" type="string">
  HTTP method for the callback. Values: `GET`, `POST`. Default: `POST`.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.numbers.update(number='17609915566', alias='Main Line')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.numbers.update('17609915566', { alias: 'Main Line' })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.numbers.update('17609915566', alias: 'Main Line')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Number/17609915566/" \
    -u "{auth_id}:{auth_token}" \
    -H "Content-Type: application/json" \
    -d '{"alias": "Main Line"}'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "message": "changed",
  "api_id": "5a9fcb68-582d-11e1-86da-6ff39efcb949"
}
```

***

## Unrent a Number

Remove a phone number from your account. This operation cannot be undone.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Number/{number}/
```

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.numbers.delete(number='17609915566')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.numbers.unrent('17609915566')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.numbers.delete('17609915566')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X DELETE "https://api.plivo.com/v1/Account/{auth_id}/Number/17609915566/" \
    -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

### Response

```
HTTP Status Code: 204
```

***

## Related

* [Phone Numbers](/numbers/phone-numbers/) - Search and buy numbers
* [Incoming Carriers](/numbers/incoming-carriers/) - Add numbers from your carrier
* [Regulatory Compliance](/numbers/regulatory-compliance/) - Verification requirements
* [Caller Reputation](/voice/concepts/caller-reputation) - Register your business identity to reduce spam flagging
