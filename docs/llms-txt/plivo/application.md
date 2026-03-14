# Source: https://plivo.com/docs/account/api/application.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Application API

> Create and manage applications to control incoming calls and messages

An `Application` is a set of Answer, Hangup, and Message URLs that help you control your incoming calls and messages.

**API Endpoint**

```
https://api.plivo.com/v1/Account/{auth_id}/Application/
```

***

## The Application Object

### Attributes

<ParamField body="app_id" type="string">
  Unique identifier for the application.
</ParamField>

<ParamField body="app_name" type="string">
  A friendly name for your Plivo application.
</ParamField>

<ParamField body="answer_url" type="string">
  URL requested when an incoming call is received. Must return valid Plivo XML.
</ParamField>

<ParamField body="answer_method" type="string">
  HTTP method for the answer\_url. Values: `GET` or `POST`.
</ParamField>

<ParamField body="hangup_url" type="string">
  URL notified when the call hangs up.
</ParamField>

<ParamField body="hangup_method" type="string">
  HTTP method for the hangup\_url.
</ParamField>

<ParamField body="fallback_answer_url" type="string">
  URL requested when answer\_url fails or returns invalid XML.
</ParamField>

<ParamField body="fallback_method" type="string">
  HTTP method for the fallback\_answer\_url.
</ParamField>

<ParamField body="message_url" type="string">
  URL notified when an inbound SMS is received.
</ParamField>

<ParamField body="message_method" type="string">
  HTTP method for the message\_url.
</ParamField>

<ParamField body="default_app" type="boolean">
  Whether this is the default app.
</ParamField>

<ParamField body="enabled" type="boolean">
  Whether the application is enabled.
</ParamField>

<ParamField body="public_uri" type="boolean">
  Whether the app can be called from external SIP services.
</ParamField>

<ParamField body="sip_uri" type="string">
  SIP URI of the application.
</ParamField>

<ParamField body="sub_account" type="string">
  Subaccount associated with the application. Null if main account.
</ParamField>

<ParamField body="log_incoming_messages" type="boolean">
  Whether incoming message content is logged. Default: `true`.
</ParamField>

<ParamField body="resource_uri" type="string">
  URI of the application resource.
</ParamField>

### Example Object

```json  theme={null}
{
  "answer_method": "GET",
  "answer_url": "https://example.com/answer",
  "app_id": "20372631212782780",
  "app_name": "My Application",
  "default_app": false,
  "enabled": true,
  "fallback_answer_url": "",
  "fallback_method": "POST",
  "hangup_method": "POST",
  "hangup_url": "https://example.com/hangup",
  "message_method": "POST",
  "message_url": "",
  "public_uri": false,
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Application/20372631212782780/",
  "sip_uri": "sip:20372631212782780@app.plivo.com",
  "sub_account": null,
  "log_incoming_messages": true
}
```

### Answer URL Parameters

When a call is received, Plivo sends these parameters to your answer\_url:

| Parameter       | Description                                           |
| --------------- | ----------------------------------------------------- |
| CallUUID        | Unique identifier for this call                       |
| From            | Caller's phone number with country code               |
| To              | Called phone number with country code                 |
| CallStatus      | Call status: `ringing`, `in-progress`, or `completed` |
| Direction       | Call direction: `inbound` or `outbound`               |
| ForwardedFrom   | Present only for forwarded calls                      |
| ALegUUID        | First leg UUID for outbound calls                     |
| ALegRequestUUID | Request UUID for API-initiated outbound calls         |

### Hangup URL Parameters

| Parameter       | Description                     |
| --------------- | ------------------------------- |
| CallUUID        | Unique identifier for this call |
| From            | Caller's phone number           |
| To              | Called phone number             |
| CallStatus      | Final call status               |
| Direction       | Call direction                  |
| Duration        | Call duration in seconds        |
| BillDuration    | Billed duration in seconds      |
| HangupCauseName | Reason for hangup               |
| HangupCauseCode | Hangup cause code               |
| HangupSource    | Entity that triggered hangup    |

### Message URL Parameters

| Parameter   | Description                                 |
| ----------- | ------------------------------------------- |
| From        | Source number of incoming message           |
| To          | Your Plivo number that received the message |
| Type        | Always `sms`                                |
| Text        | Message content                             |
| MessageUUID | Unique message identifier                   |

***

## Create an Application

Creates a new application.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Application/
```

### Arguments

<ParamField body="app_name" type="string" required>
  Application name. Allowed: alphanumeric, hyphen (-), underscore (\_).
</ParamField>

<ParamField body="answer_url" type="string" required>
  URL fetched when a call executes this application.
</ParamField>

<ParamField body="answer_method" type="string">
  HTTP method for answer\_url. Default: `POST`.
</ParamField>

<ParamField body="hangup_url" type="string">
  URL notified when call hangs up. Default: answer\_url.
</ParamField>

<ParamField body="hangup_method" type="string">
  HTTP method for hangup\_url. Default: `POST`.
</ParamField>

<ParamField body="fallback_answer_url" type="string">
  Fallback URL if answer\_url fails.
</ParamField>

<ParamField body="fallback_method" type="string">
  HTTP method for fallback\_answer\_url. Default: `POST`.
</ParamField>

<ParamField body="message_url" type="string">
  URL notified for inbound messages.
</ParamField>

<ParamField body="message_method" type="string">
  HTTP method for message\_url. Default: `POST`.
</ParamField>

<ParamField body="default_number_app" type="boolean">
  Make this the default app for new numbers.
</ParamField>

<ParamField body="default_endpoint_app" type="boolean">
  Make this the default app for new endpoints.
</ParamField>

<ParamField body="subaccount" type="string">
  Subaccount ID to associate with this application.
</ParamField>

<ParamField body="log_incoming_messages" type="boolean">
  Log incoming message content. Default: `true`.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.applications.create(
      app_name='MyApp',
      answer_url='https://example.com/answer')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.applications.create('MyApp', { answerUrl: 'https://example.com/answer' })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.applications.create(
      'MyApp',
      answer_url: 'https://example.com/answer')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->applications->create(
      'MyApp',
      ['answer_url' => 'https://example.com/answer']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.application.Application;

  Plivo.init("<auth_id>", "<auth_token>");

  ApplicationCreateResponse response = Application.creator("MyApp", "https://example.com/answer")
      .create();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Application.Create(
      appName: "MyApp",
      answerUrl: "https://example.com/answer");
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

      response, _ := client.Applications.Create(plivo.ApplicationCreateParams{
          AppName:   "MyApp",
          AnswerURL: "https://example.com/answer",
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"answer_url": "https://example.com/answer", "app_name": "MyApp"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Application/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "message": "created",
  "app_id": "15784735442685051",
  "api_id": "5a9fcb68-582d-11e1-86da-6ff39efcb949"
}
```

***

## Retrieve an Application

Get details of a specific application.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Application/{app_id}/
```

### Arguments

<Note>No arguments required.</Note>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.applications.get(app_id='15784735442685051')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.applications.get('15784735442685051')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.applications.get('15784735442685051')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->applications->get('15784735442685051');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.application.Application;

  Plivo.init("<auth_id>", "<auth_token>");

  Application response = Application.getter("15784735442685051").get();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Application.Get(appId: "15784735442685051");
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

      response, _ := client.Applications.Get("15784735442685051")
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Application/15784735442685051/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "answer_method": "GET",
  "answer_url": "https://example.com/answer",
  "app_id": "20372631212782780",
  "app_name": "My Application",
  "default_app": false,
  "enabled": true,
  "fallback_answer_url": "",
  "fallback_method": "POST",
  "hangup_method": "POST",
  "hangup_url": "https://example.com/hangup",
  "message_method": "POST",
  "message_url": "",
  "public_uri": false,
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Application/20372631212782780/",
  "sip_uri": "sip:20372631212782780@app.plivo.com",
  "sub_account": null,
  "log_incoming_messages": true
}
```

***

## List All Applications

Returns all applications sorted by creation date.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Application/
```

### Arguments

<ParamField query="subaccount" type="string">
  Filter by subaccount ID.
</ParamField>

<ParamField query="app_name" type="string">
  Filter by app name prefix.
</ParamField>

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

  response = client.applications.list(offset=0, limit=5)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.applications.list({ offset: 0, limit: 5 })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.applications.list(limit: 5, offset: 0)
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->applications->list(['limit' => 5, 'offset' => 0]);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.application.Application;

  Plivo.init("<auth_id>", "<auth_token>");

  ListResponse<Application> response = Application.lister()
      .offset(0)
      .limit(5)
      .list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Application.List(limit: 5, offset: 0);
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

      response, _ := client.Applications.List(plivo.ApplicationListParams{
          Offset: 0,
          Limit:  5,
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Application/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "e5b05b26-10c4-11e4-a2d1-22000ac5040c",
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 2
  },
  "objects": [
    {
      "answer_method": "GET",
      "answer_url": "https://example.com/answer",
      "app_id": "20372631212782780",
      "app_name": "My Application",
      "default_app": false,
      "enabled": true,
      "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Application/20372631212782780/"
    }
  ]
}
```

***

## Update an Application

Modify an existing application.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Application/{app_id}/
```

### Arguments

<ParamField body="answer_url" type="string">
  URL fetched when a call executes this application.
</ParamField>

<ParamField body="answer_method" type="string">
  HTTP method for answer\_url.
</ParamField>

<ParamField body="hangup_url" type="string">
  URL notified when call hangs up.
</ParamField>

<ParamField body="hangup_method" type="string">
  HTTP method for hangup\_url.
</ParamField>

<ParamField body="fallback_answer_url" type="string">
  Fallback URL if answer\_url fails.
</ParamField>

<ParamField body="fallback_method" type="string">
  HTTP method for fallback\_answer\_url.
</ParamField>

<ParamField body="message_url" type="string">
  URL notified for inbound messages.
</ParamField>

<ParamField body="message_method" type="string">
  HTTP method for message\_url.
</ParamField>

<ParamField body="default_number_app" type="boolean">
  Make this the default app for new numbers.
</ParamField>

<ParamField body="default_endpoint_app" type="boolean">
  Make this the default app for new endpoints.
</ParamField>

<ParamField body="subaccount" type="string">
  Subaccount ID to associate.
</ParamField>

<ParamField body="log_incoming_messages" type="boolean">
  Log incoming message content.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.applications.update(
      app_id='21686794894743506',
      answer_url='https://updated.answer.url')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.applications.update('15784735442685051', { answerUrl: 'https://updated.answer.url' })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.applications.update(
      '15784735442685051',
      answer_url: 'https://updated.answer.url')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->applications->update(
      '15784735442685051',
      ['answer_url' => 'https://updated.answer.url']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.application.Application;

  Plivo.init("<auth_id>", "<auth_token>");

  ApplicationUpdateResponse response = Application.updater("15784735442685051")
      .answerUrl("https://updated.answer.url")
      .update();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Application.Update(
      appId: "15784735442685051",
      answerUrl: "https://updated.answer.url");
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

      response, _ := client.Applications.Update("15784735442685051", plivo.ApplicationUpdateParams{
          AnswerURL: "https://updated.answer.url",
      })
      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"answer_url": "https://updated.answer.url"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Application/{app_id}/
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

## Delete an Application

Permanently deletes an application.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Application/{app_id}/
```

### Arguments

<ParamField query="cascade" type="boolean">
  Delete associated endpoints. Default: `true`.
</ParamField>

<ParamField query="new_endpoint_application" type="string">
  App ID to reassign endpoints to when cascade is `false`.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.applications.delete(app_id='21686794894743506')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.applications.delete('15784735442685051')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.applications.delete('15784735442685051')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->applications->delete('15784735442685051');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.application.Application;

  Plivo.init("<auth_id>", "<auth_token>");

  Application.deleter("15784735442685051").delete();
  System.out.println("Deleted successfully.");
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Application.Delete(appId: "15784735442685051");
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

      err := client.Applications.Delete("15784735442685051")
      if err == nil {
          fmt.Println("Deleted successfully.")
      }
  }
  ```

  ```bash cURL theme={null}
  curl -X DELETE -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Application/{app_id}/
  ```
</CodeGroup>

### Response

```
HTTP Status Code: 204
```
