# Source: https://plivo.com/docs/account/api/subaccount.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subaccount API

> Create and manage subaccounts to segment usage and isolate traffic

Subaccounts let you manage multiple customer accounts under your main account. Each subaccount has its own Auth ID and Token, while charges deduct from the main account.

**API Endpoint**

```
https://api.plivo.com/v1/Account/{auth_id}/Subaccount/
```

***

## The Subaccount Object

### Attributes

<ParamField body="auth_id" type="string">
  Auth ID of the subaccount.
</ParamField>

<ParamField body="auth_token" type="string">
  Auth Token of the subaccount.
</ParamField>

<ParamField body="name" type="string">
  Name of the subaccount.
</ParamField>

<ParamField body="enabled" type="boolean">
  Whether the subaccount is enabled.
</ParamField>

<ParamField body="account" type="string">
  URI to the parent account.
</ParamField>

<ParamField body="created" type="string">
  Date the subaccount was created.
</ParamField>

<ParamField body="modified" type="string">
  Date the subaccount was last modified.
</ParamField>

<ParamField body="resource_uri" type="string">
  URI to the subaccount resource.
</ParamField>

### Example Object

```json  theme={null}
{
  "account": "/v1/Account/MA2025RK4E639VJFZAGV/",
  "api_id": "968f0a22-9237-11e7-a51d-0245fa790d9e",
  "auth_id": "SA2025RK4E639VJFZAMM",
  "auth_token": "NWM3YjliMjk0ZGYxMGM2YjJiYWE0MjEwZDM5YWU5",
  "created": "2022-09-05",
  "enabled": true,
  "modified": null,
  "name": "Subaccount Test",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Subaccount/SA2025RK4E639VJFZAMM/"
}
```

***

## Create a Subaccount

Creates a new subaccount.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Subaccount/
```

### Arguments

<ParamField body="name" type="string" required>
  A human-readable name for the subaccount.
</ParamField>

<ParamField body="enabled" type="boolean">
  Whether the subaccount should be enabled. Default: `false`.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.subaccounts.create(
      name='Wayne Enterprises Subaccount',
      enabled=True)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.subAccounts.create('Test Subaccount', true)
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.subaccounts.create('Test Subaccount', true)
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->subaccounts->create('Test Subaccount', true);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.account.Subaccount;

  Plivo.init("<auth_id>", "<auth_token>");

  SubaccountCreateResponse response = Subaccount.creator("Test Subaccount")
      .enabled(true)
      .create();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Subaccount.Create(
      enabled: true,
      name: "Test Subaccount");
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

      response, _ := client.Subaccounts.Create(plivo.SubaccountCreateParams{
          Name:    "Test Subaccount",
          Enabled: true,
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"name": "Test Subaccount", "enabled": true}' \
      https://api.plivo.com/v1/Account/{auth_id}/Subaccount/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "324a7dd8-0db2-11e4-8a4a-123140008edf",
  "auth_id": "SA2025RK4E639VJFZAMM",
  "auth_token": "MTZjYWM0YzVjNjMwZmVmODFiNWJjNPJmOGJjZjgw",
  "message": "created"
}
```

***

## Retrieve a Subaccount

Get details of a specific subaccount.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Subaccount/{subauth_id}/
```

### Arguments

<Note>No arguments required.</Note>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.subaccounts.get(auth_id='SA2025RK4E639VJFZAMM')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.subaccounts.get('SA2025RK4E639VJFZAMM')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.subaccounts.get('SA2025RK4E639VJFZAMM')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->subaccounts->get('SA2025RK4E639VJFZAMM');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.account.Subaccount;

  Plivo.init("<auth_id>", "<auth_token>");

  Subaccount response = Subaccount.getter("SA2025RK4E639VJFZAMM").get();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Subaccount.Get(id: "SA2025RK4E639VJFZAMM");
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

      response, _ := client.Subaccounts.Get("SA2025RK4E639VJFZAMM")
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Subaccount/{subauth_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "account": "/v1/Account/MA2025RK4E639VJFZAGV/",
  "api_id": "323972b2-0db3-11e4-a2d1-22000ac5040c",
  "auth_id": "SA2025RK4E639VJFZAMM",
  "auth_token": "MTZjYWM0YzVjNjMwZmVmODFiNWJjNWJmOGJjZjgw",
  "created": "2022-07-17",
  "enabled": false,
  "modified": null,
  "name": "Han Solo",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Subaccount/SA2025RK4E639VJFZAMM/"
}
```

***

## List All Subaccounts

Returns all subaccounts sorted by creation date, newest first.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Subaccount/
```

### Arguments

<ParamField query="limit" type="integer">
  Results per page. Maximum 20.
</ParamField>

<ParamField query="offset" type="integer">
  Pagination offset.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.subaccounts.list(offset=0, limit=5)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.subaccounts.list({ offset: 0, limit: 5 })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.subaccounts.list(limit: 5, offset: 0)
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->subaccounts->list(3, 2);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.account.Subaccount;

  Plivo.init("<auth_id>", "<auth_token>");

  ListResponse<Subaccount> response = Subaccount.lister()
      .offset(0)
      .limit(5)
      .list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Subaccount.List(limit: 5, offset: 0);
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

      response, _ := client.Subaccounts.List(plivo.SubaccountListParams{
          Offset: 0,
          Limit:  5,
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Subaccount/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "b38bf42e-0db4-11e4-8a4a-123140008edf",
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 2
  },
  "objects": [
    {
      "account": "/v1/Account/MA2025RK4E639VJFZAGV/",
      "auth_id": "SA2025RK4E639VJFZAMM",
      "auth_token": "MTZjYWM0YzVjNjMwZmVmODFiNWJjNWJmOGJjZjgw",
      "created": "2022-07-17",
      "enabled": false,
      "modified": null,
      "name": "Chewbacca",
      "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Subaccount/SA2025RK4E639VJFZAMM/"
    }
  ]
}
```

***

## Update a Subaccount

Updates a subaccount. Parameters not provided remain unchanged.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Subaccount/{subauth_id}/
```

### Arguments

<ParamField body="name" type="string" required>
  Name of the subaccount.
</ParamField>

<ParamField body="enabled" type="boolean">
  Whether the subaccount should be enabled.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.subaccounts.update(
      auth_id='SA2025RK4E639VJFZAMM',
      name='Updated Subaccount Name')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.subaccounts.update('SA2025RK4E639VJFZAMM', 'Updated Subaccount Name')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.subaccounts.update(
      'SA2025RK4E639VJFZAMM',
      'Updated Subaccount Name',
      false)
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->subaccounts->update(
      'SA2025RK4E639VJFZAMM',
      'Updated Subaccount Name');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.account.Subaccount;

  Plivo.init("<auth_id>", "<auth_token>");

  SubaccountUpdateResponse response = Subaccount.updater("SA2025RK4E639VJFZAMM", "Updated Subaccount Name")
      .update();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Subaccount.Update(
      id: "SA2025RK4E639VJFZAMM",
      name: "Updated Subaccount Name");
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

      response, _ := client.Subaccounts.Update("SA2025RK4E639VJFZAMM", plivo.SubaccountUpdateParams{
          Name: "Updated Subaccount Name",
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"name": "Updated Subaccount Name"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Subaccount/{subauth_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "message": "changed",
  "api_id": "5a9fcb68-523d-11e1-86da-6ff39efcb949"
}
```

***

## Delete a Subaccount

Permanently deletes a subaccount.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Subaccount/{subauth_id}/
```

### Arguments

<ParamField query="cascade" type="boolean">
  If `true`, deletes associated Applications, Endpoints, and Numbers. If `false`, maps them to the main account. Default: `false`.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.subaccounts.delete(
      auth_id='SA2025RK4E639VJFZAMM',
      cascade=True)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.subaccounts.delete('SA2025RK4E639VJFZAMM', true)
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.subaccounts.delete('SA2025RK4E639VJFZAMM', true)
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->subaccounts->delete('SA2025RK4E639VJFZAMM', true);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.account.Subaccount;

  Plivo.init("<auth_id>", "<auth_token>");

  Subaccount.deleter("SA2025RK4E639VJFZAMM").cascade(true).delete();
  System.out.println("Deleted successfully.");
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Subaccount.Delete(
      id: "SA2025RK4E639VJFZAMM",
      cascade: true);
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

      err := client.Subaccounts.Delete("SA2025RK4E639VJFZAMM", plivo.SubaccountDeleteParams{Cascade: true})
      if err == nil {
          fmt.Println("Deleted successfully.")
      }
  }
  ```

  ```bash cURL theme={null}
  curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Subaccount/{subauth_id}/
  ```
</CodeGroup>

### Response

```
HTTP Status Code: 204
```
