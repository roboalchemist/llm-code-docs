# Source: https://plivo.com/docs/numbers/phone-numbers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Phone Numbers API

> Search and buy phone numbers from Plivo's inventory

Search for and purchase phone numbers from Plivo. You can search for local, toll-free, national, mobile, and fixed phone numbers that match specific criteria.

**API Endpoint**

```
https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/
```

***

## The PhoneNumber Object

### Attributes

<ParamField body="number" type="string">
  Phone number that can be purchased.
</ParamField>

<ParamField body="prefix" type="string">
  Area code of the number.
</ParamField>

<ParamField body="city" type="string">
  City of the number. Returns `null` for national numbers.
</ParamField>

<ParamField body="country" type="string">
  Country of the number.
</ParamField>

<ParamField body="region" type="string">
  City and country of the number.
</ParamField>

<ParamField body="rate_center" type="string">
  Rate center. US and Canada only.
</ParamField>

<ParamField body="lata" type="string">
  Local access and transport area. US and Canada only.
</ParamField>

<ParamField body="type" type="string">
  Number type. Values: `fixed`, `mobile`, or `tollfree`.
</ParamField>

<ParamField body="sub_type" type="string">
  Number subtype. Values: `fixed`, `mobile`, `tollfree`, `national`, or `local`.
</ParamField>

<ParamField body="setup_rate" type="string">
  One-time setup fee in USD.
</ParamField>

<ParamField body="monthly_rental_rate" type="string">
  Monthly rental fee in USD.
</ParamField>

<ParamField body="sms_enabled" type="boolean">
  Whether the number can receive SMS.
</ParamField>

<ParamField body="sms_rate" type="string">
  Cost per SMS received in USD.
</ParamField>

<ParamField body="mms_enabled" type="boolean">
  Whether the number can receive MMS.
</ParamField>

<ParamField body="mms_rate" type="string">
  Cost per MMS received in USD.
</ParamField>

<ParamField body="voice_enabled" type="boolean">
  Whether the number can receive calls.
</ParamField>

<ParamField body="voice_rate" type="string">
  Cost per minute for calls in USD.
</ParamField>

<ParamField body="restriction" type="string">
  Verification requirement. Values: `city-address`, `country-address`, `terms-and-conditions`, or `null`.
</ParamField>

<ParamField body="restriction_text" type="string">
  Description of verification requirements.
</ParamField>

<ParamField body="resource_uri" type="string">
  URI to the phone number resource.
</ParamField>

### Example Object

```json  theme={null}
{
  "number": "14155559186",
  "prefix": "415",
  "city": "SAN FRANCISCO",
  "country": "UNITED STATES",
  "region": "United States",
  "rate_center": "SNFC CNTRL",
  "lata": 722,
  "type": "fixed",
  "sub_type": "local",
  "setup_rate": "0.00000",
  "monthly_rental_rate": "0.80000",
  "sms_enabled": true,
  "sms_rate": "0.00800",
  "voice_enabled": true,
  "voice_rate": "0.00500",
  "restriction": null,
  "restriction_text": null,
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/PhoneNumber/14155559186/"
}
```

***

## Search Phone Numbers

Returns available phone numbers matching your criteria.

```
GET https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/
```

### Arguments

<ParamField query="country_iso" type="string" required>
  [ISO 3166 alpha-2 country code](https://www.iban.com/country-codes) of the country.
</ParamField>

<ParamField query="type" type="string">
  Number type filter. Values: `tollfree`, `local`, `mobile`, `national`, or `fixed`.
</ParamField>

<ParamField query="pattern" type="string">
  Pattern to match. For example, `415` returns numbers starting with 1415.
</ParamField>

<ParamField query="npanxx" type="integer">
  Six-digit prefix filter. US and Canada only.
</ParamField>

<ParamField query="local_calling_area" type="boolean">
  Expand search to local calling area of `npanxx`.
</ParamField>

<ParamField query="region" type="string">
  Region name (e.g., `Frankfurt`). For `fixed` type only.
</ParamField>

<ParamField query="city" type="string">
  City name. For `local` type only.
</ParamField>

<ParamField query="services" type="string">
  Filter by capabilities. Values: `voice`, `sms`, `mms`, `voice,sms`, or `voice,sms,mms`.
</ParamField>

<ParamField query="lata" type="integer">
  LATA filter. US and Canada only.
</ParamField>

<ParamField query="rate_center" type="string">
  Rate center filter. US and Canada only.
</ParamField>

<ParamField query="limit" type="integer">
  Results per page. Maximum 20, default 20.
</ParamField>

<ParamField query="offset" type="integer">
  Pagination offset. Default 0.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.numbers.search(country_iso='US', type='local', pattern='415')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.numbers.search('US', { type: 'local', pattern: '415' })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.phone_numbers.search('US', type: 'local', pattern: '415')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->phonenumbers->list('US', ['type' => 'local', 'pattern' => '415']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.number.PhoneNumber;

  Plivo.init("<auth_id>", "<auth_token>");

  ListResponse<PhoneNumber> response = PhoneNumber.lister("US")
      .type("local")
      .pattern("415")
      .list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.PhoneNumber.List(countryIso: "US", type: "local", pattern: "415");
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

      response, _ := client.PhoneNumbers.List(plivo.PhoneNumberListParams{
          CountryISO: "US",
          Type:       "local",
          Pattern:    "415",
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/?country_iso=US&type=local&pattern=415" \
    -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "859428b0-1c88-11e4-a2d1-22000ac5040c",
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 9
  },
  "objects": [
    {
      "number": "14154009186",
      "prefix": "415",
      "city": "SAN FRANCISCO",
      "country": "UNITED STATES",
      "type": "fixed",
      "sub_type": "local",
      "monthly_rental_rate": "0.80000",
      "sms_enabled": true,
      "voice_enabled": true,
      "restriction": null,
      "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/PhoneNumber/14154009186/"
    }
  ]
}
```

***

## Buy a Phone Number

Purchase a phone number and add it to your account.

```
POST https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/{number}/
```

### Arguments

<ParamField body="app_id" type="string">
  Application to assign. Defaults to `default_number_app`.
</ParamField>

<ParamField body="cnam_lookup" type="string">
  Enable CNAM lookup. Values: `enabled` or `disabled`. US only.
</ParamField>

<Note>
  If the number requires verification documents, the number status will be `pending` until documents are approved.
</Note>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.numbers.buy(number='14155559186')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.numbers.buy('14155559186')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.phone_numbers.buy('14155559186')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->phonenumbers->buy('14155559186');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.number.PhoneNumber;

  Plivo.init("<auth_id>", "<auth_token>");

  PhoneNumberCreateResponse response = PhoneNumber.creator("14155559186").create();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.PhoneNumber.Buy(number: "14155559186");
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

      response, _ := client.PhoneNumbers.Create("14155559186", plivo.PhoneNumberCreateParams{})
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/14155559186/" \
    -u "{auth_id}:{auth_token}" \
    -H "Content-Type: application/json"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "aa52882c-1c88-11e4-bd8a-12313f016a39",
    "message": "created",
    "numbers": [
        {
            "number": "14155559186",
            "status": "Success"
        }
    ],
    "status": "fulfilled"
}
```

***

## Related

* [Account Phone Numbers](/numbers/account-phone-numbers) - Manage your rented numbers
* [Regulatory Compliance](/numbers/regulatory-compliance) - Verification requirements
* [Number Porting](/numbers/number-porting) - Port numbers to Plivo
