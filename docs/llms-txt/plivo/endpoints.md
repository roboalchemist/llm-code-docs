# Source: https://plivo.com/docs/voice/api/endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Endpoints

> Create and manage SIP endpoints for Voice SDK and WebRTC applications

Endpoints represent SIP users that can register with Plivo and make/receive calls through Voice SDKs (Web, iOS, Android) or SIP softphones. Each endpoint has a unique username, password, and SIP URI.

## The Endpoint Object

| Attribute        | Type     | Description                                                                 |
| ---------------- | -------- | --------------------------------------------------------------------------- |
| `endpoint_id`    | `string` | Unique identifier for the endpoint. Used in all endpoint API operations.    |
| `username`       | `string` | Username for the endpoint. Only alphanumeric characters are accepted.       |
| `password`       | `string` | Password for the endpoint. Returned as MD5 hash in responses.               |
| `alias`          | `string` | Human-readable alias for the endpoint.                                      |
| `sip_uri`        | `string` | SIP URI of the endpoint. External users can call this endpoint on this URI. |
| `sip_registered` | `string` | `true` if the endpoint is registered on a SIP client. Default: `false`.     |
| `application`    | `string` | URI of the application attached to the endpoint.                            |
| `sub_account`    | `string` | Subaccount the endpoint is linked to. `null` if not linked.                 |
| `resource_uri`   | `string` | URI of the endpoint object.                                                 |

### Example Endpoint Object

```json  theme={null}
{
  "alias": "callme",
  "application": "/v1/Account/MA2025RK4E639VJFZAGV/Application/33406267401237901/",
  "endpoint_id": "32866729519064",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Endpoint/32866729519064/",
  "sip_contact": "sip:callme140703093224@122.172.71.207:57563;ob",
  "sip_expires": "2022-07-21 19:26:08",
  "sip_registered": "true",
  "sip_uri": "sip:callme140703093944@phone.plivo.com",
  "sip_user_agent": "Telephone 1.1.4",
  "sub_account": null,
  "username": "callme140703093944"
}
```

***

## Create an Endpoint

Create a new SIP endpoint.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Endpoint/
```

### Arguments

| Parameter  | Required | Description                                                                            |
| ---------- | -------- | -------------------------------------------------------------------------------------- |
| `username` | Yes      | Username for the endpoint. Alphanumeric only, must start with an alphabetic character. |
| `password` | Yes      | Password for the endpoint. Must be at least 5 characters long.                         |
| `alias`    | Yes      | Alias for the endpoint. Allows letters, numbers, hyphens, and underscores.             |
| `app_id`   | No       | ID of the application to attach to the endpoint.                                       |

### Returns

Returns the created endpoint with a 12-digit number appended to the username.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.endpoints.create(
      username='testusername',
      password='testpassword',
      alias='Test Account')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.endpoints.create(
      'testusername',
      'testpassword',
      'Test Account',
      'app id'
  )
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.endpoints.create(
      "testusername",
      "testpassword",
      "Test Account"
  ).then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->endpoints->create(
      'testusername',
      'testpassword',
      'Test Account'
  );
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.endpoint.Endpoint;

  Plivo.init("<auth_id>","<auth_token>");
  EndpointCreateResponse response = Endpoint.creator("testusername", "testpassword", "Test Account").create();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Endpoint.Create(
      username: "testusername",
      alias: "Test Account",
      password: "testpassword"
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Endpoints.Create(plivo.EndpointCreateParams{
          Username: "testusername",
          Password: "testpassword",
          Alias:    "Test Account",
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"username": "testuser", "password": "test123", "alias": "Test"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Endpoint/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "username": "zumba131031145958",
  "alias": "zumba",
  "message": "created",
  "endpoint_id": "37371860103666",
  "api_id": "1c13de4c-423d-11e3-9899-22000abfa5d5"
}
```

***

## Retrieve an Endpoint

Get details of a specific endpoint.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Endpoint/{endpoint_id}/
```

### Arguments

No arguments required.

<Note>
  The `password` returned is an MD5 hash of the actual password.
</Note>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.endpoints.get(endpoint_id='1465909595140')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.endpoints.get('39452475478853')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.endpoints.get("39452475478853").then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->endpoints->get('39452475478853');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.endpoint.Endpoint;

  Plivo.init("<auth_id>","<auth_token>");
  Endpoint response = Endpoint.getter("39452475478853").get();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Endpoint.Get(endpointId: "18385812687105");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Endpoints.Get("39452475478853")
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Endpoint/{endpoint_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "alias": "callme",
  "application": "/v1/Account/MA2025RK4E639VJFZAGV/Application/33406267401237901/",
  "endpoint_id": "32866729519064",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Endpoint/32866729519064/",
  "sip_contact": "sip:callme140703093224@122.172.71.207:57563;ob",
  "sip_expires": "2022-07-21 19:26:08",
  "sip_registered": "true",
  "sip_uri": "sip:callme140703093944@phone.plivo.com",
  "sip_user_agent": "Telephone 1.1.4",
  "sub_account": null,
  "username": "callme140703093944"
}
```

***

## List All Endpoints

Retrieve all endpoints in your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Endpoint/
```

### Arguments

No arguments required.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.endpoints.list()
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.endpoints.list
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.endpoints.list().then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->endpoints->list();
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.endpoint.Endpoint;

  Plivo.init("<auth_id>","<auth_token>");
  ListResponse<Endpoint> response = Endpoint.lister().list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Endpoint.List();
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Endpoints.List(plivo.EndpointListParams{})
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Endpoint/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "30a0c8c2-110c-11e4-bd8a-12313f016a39",
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 11
  },
  "objects": [
    {
      "alias": "callme",
      "application": "/v1/Account/MA2025RK4E639VJFZAGV/Application/33406267401237901/",
      "endpoint_id": "32866729519064",
      "sip_registered": "true",
      "sip_uri": "sip:callme140703093944@phone.plivo.com",
      "username": "callme140703093944"
    }
  ]
}
```

***

## Update an Endpoint

Update an endpoint's password, alias, or attached application.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Endpoint/{endpoint_id}/
```

### Arguments

| Parameter  | Description                                                   |
| ---------- | ------------------------------------------------------------- |
| `password` | New password. Must be at least 5 characters.                  |
| `alias`    | New alias. Allows letters, numbers, hyphens, and underscores. |
| `app_id`   | ID of the application to attach.                              |

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.endpoints.update(
      endpoint_id='14659095951490',
      alias='Double time.')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.endpoints.update('39452475478853', alias: 'New Alias')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.endpoints.update("39452475478853", { alias: "New Alias" })
      .then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->endpoints->update('39452475478853', ['alias' => 'New Alias']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.endpoint.Endpoint;

  Plivo.init("<auth_id>","<auth_token>");
  EndpointUpdateResponse response = Endpoint.updater("39452475478853")
      .alias("New Alias")
      .update();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Endpoint.Update(
      endpointId: "18385812687105",
      alias: "New Alias"
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Endpoints.Update("39452475478853", plivo.EndpointUpdateParams{
          Alias: "New Alias",
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"alias": "New Alias"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Endpoint/{endpoint_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "message": "changed",
  "api_id": "d8f9ea6c-58cc-11e1-86da-adf28403fe48"
}
```

***

## Delete an Endpoint

Permanently delete an endpoint.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Endpoint/{endpoint_id}/
```

### Arguments

No arguments required.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.endpoints.delete(endpoint_id='14659095951490')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.endpoints.delete('39452475478853')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.endpoints.delete("39452475478853").then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->endpoints->delete('39452475478853');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.endpoint.Endpoint;

  Plivo.init("<auth_id>","<auth_token>");
  Endpoint.deleter("39452475478853").delete();
  System.out.println("Deleted successfully.");
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Endpoint.Delete(endpointId: "18385812687105");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.Endpoints.Delete("39452475478853")
  }
  ```

  ```bash cURL theme={null}
  curl -X DELETE -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Endpoint/{endpoint_id}/
  ```
</CodeGroup>

### Response

```
HTTP Status Code: 204
```

***

## Related

* [Voice SDK Documentation](/voice/sdk/) - Build client apps with Voice SDKs
* [Web SDK](/voice/sdk/web/) - Make calls from browsers
* [iOS SDK](/voice/sdk/ios/) - Make calls from iOS apps
* [Android SDK](/voice/sdk/android/) - Make calls from Android apps
