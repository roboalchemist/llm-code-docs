# Source: https://plivo.com/docs/account/api/account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Account API

> Retrieve and update your Plivo account details

The `Account` object lets you perform actions on your Plivo account. You can retrieve and update account details using this API.

**API Endpoint**

```
https://api.plivo.com/v1/Account/{auth_id}/
```

***

## The Account Object

### Attributes

<ParamField body="account_type" type="string">
  Account type. Values: `standard` for paid accounts, `developer` for free trial.
</ParamField>

<ParamField body="address" type="string">
  Postal address of the account, displayed on invoices.
</ParamField>

<ParamField body="auth_id" type="string">
  Auth ID of the account.
</ParamField>

<ParamField body="auto_recharge" type="boolean">
  Whether automatic recharge is enabled when credits fall below threshold.
</ParamField>

<ParamField body="billing_mode" type="string">
  Billing mode. Values: `prepaid` or `postpaid`.
</ParamField>

<ParamField body="cash_credits" type="string">
  Account credits in USD.
</ParamField>

<ParamField body="city" type="string">
  City of the account holder.
</ParamField>

<ParamField body="name" type="string">
  Name of the account holder.
</ParamField>

<ParamField body="resource_uri" type="string">
  URI of the account resource.
</ParamField>

<ParamField body="state" type="string">
  State or region of the account.
</ParamField>

<ParamField body="timezone" type="string">
  Time zone used in the Plivo dashboard. See [IANA Time Zone Database](https://www.iana.org/time-zones).
</ParamField>

### Example Object

```json  theme={null}
{
  "account_type": "standard",
  "address": "Wayne Enterprises Inc.",
  "api_id": "150892a0-922a-11e7-b6f4-061564b78b75",
  "auth_id": "MA2025RK4E639VJFZAGV",
  "auto_recharge": false,
  "billing_mode": "prepaid",
  "cash_credits": "1.80900",
  "city": "Gotham",
  "name": "Bruce Wayne",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/",
  "state": "NY",
  "timezone": "America/New_York"
}
```

***

## Retrieve Account Details

Retrieves the details of your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/
```

### Arguments

<Note>No arguments required.</Note>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.account.get()
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.accounts.get()
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.account.details
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->accounts->get();
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.account.Account;

  Plivo.init("<auth_id>", "<auth_token>");

  Account response = Account.getter().get();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Account.Get();
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

      response, _ := client.Accounts.Get()
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "account_type": "standard",
  "address": "Wayne Enterprises Inc.",
  "api_id": "150892a0-922a-11e7-b6f4-061564b78b75",
  "auth_id": "MA2025RK4E639VJFZAGV",
  "auto_recharge": false,
  "billing_mode": "prepaid",
  "cash_credits": "1.80900",
  "city": "Gotham",
  "name": "Bruce Wayne",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/",
  "state": "NY",
  "timezone": "America/New_York"
}
```

***

## Update Account Details

Updates the `Account` object. Parameters not provided remain unchanged.

```
POST https://api.plivo.com/v1/Account/{auth_id}/
```

### Arguments

<ParamField body="address" type="string">
  Postal address of the account, displayed on invoices.
</ParamField>

<ParamField body="name" type="string">
  Name of the account holder.
</ParamField>

<ParamField body="city" type="string">
  City of the account holder.
</ParamField>

<ParamField body="state" type="string">
  State or region of the account.
</ParamField>

<ParamField body="timezone" type="string">
  Time zone for the Plivo dashboard. See [IANA Time Zone Database](https://www.iana.org/time-zones).
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.account.update(
      name='Lucius Fox',
      city='New York',
      address='Times Square')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.accounts.update({
      name: 'Lucius Fox',
      city: 'New York',
      address: 'Times Square'
  }).then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.account.update(
      city: 'New York',
      name: 'Lucius Fox',
      address: 'Times Square')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->accounts->update(
      'Lucius Fox',
      'New York',
      'Times Square');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.account.Account;

  Plivo.init("<auth_id>", "<auth_token>");

  AccountUpdateResponse response = Account.updater()
      .name("Lucius Fox")
      .city("New York")
      .address("Times Square")
      .update();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Account.Update(
      city: "New York",
      name: "Lucius Fox",
      address: "Times Square");
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

      response, _ := client.Accounts.Update(plivo.AccountUpdateParams{
          Name:    "Lucius Fox",
          City:    "New York",
          Address: "Times Square",
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"name": "Lucius Fox", "city": "New York", "address": "Times Square"}' \
      https://api.plivo.com/v1/Account/{auth_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "02bbdbaa-9303-11e7-8bc8-065f6a74a84a",
  "message": "changed"
}
```
