# Source: https://docs.datadoghq.com/cloudcraft/api/blueprints.md

---
title: Blueprints
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Cloudcraft API Reference > Blueprints
---

# Blueprints
.openapi-spec-content img{max-width:100%}.openapi-spec-content h1 a:hover,.openapi-spec-content h2 a:hover{color:#000;border-bottom:1px solid #000}List blueprintsGET  /blueprintOverview
List all of your saved blueprints.

Each entry includes the blueprint ID and name, access control, and user information.

The provided blueprint IDs are required to access the other blueprint-related APIs.
Response200401
{% tab title="200" %}
OKModelExample
{% tab title="Model" %}
Expand AllFieldTypeDescriptionblueprints
array

An array of blueprint metadata.
{% /tab %}

{% tab title="Example" %}

```json
{
  "blueprints": [
    {
      "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
      "LastUserId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
      "createdAt": "2022-01-01T20:54:47.302Z",
      "id": "bp37712a-c507-4c62-ad8b-7d981cacb3be",
      "name": "Web App Reference Architecture",
      "updatedAt": "2022-01-01T20:55:52.876Z"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/blueprint'
```

```golang
package main

import (
    "context"
    "log"
    "os"

    "github.com/DataDog/cloudcraft-go"
)

func main() {
    // Get the API key from the environment.
    key, ok := os.LookupEnv("CLOUDCRAFT_API_KEY")
    if !ok {
        log.Fatal("missing env var: CLOUDCRAFT_API_KEY")
    }

    // Create new Config to initialize a Client.
    cfg := cloudcraft.NewConfig(key)

    // Create a new Client instance with the given Config.
    client, err := cloudcraft.NewClient(cfg)
    if err != nil {
        log.Fatal(err)
    }

    // List all blueprints in the Cloudcraft account.
    blueprints, _, err := client.Blueprint.List(context.Background())
    if err != nil {
        log.Fatal(err)
    }

    // Print the name of each blueprint.
    for _, blueprint := range blueprints {
        log.Println(blueprint.Name)
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/blueprint")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

blueprints = cloudcraft.list_blueprints()
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/blueprint")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)

response = https.request(request)
puts response.read_body
```

```javascript
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/blueprint", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Create a blueprintPOST  /blueprintOverview
Create a new blueprint.

The body of the request should contain the blueprint document in JSON format. The response contains the created blueprint, including the newly assigned ID.
Response201401403
{% tab title="201" %}
OKModelExample
{% tab title="Model" %}
Expand AllFieldTypeDescriptionCreatorId
string

The user ID of the creator of the blueprint.
LastUserId
string

The user ID of the last user to modify the blueprint.
createdAt
string

The date and time the blueprint was created.
data
object

The definition of the blueprint.
id
string

The unique identifier of the blueprint.
updatedAt
string

The date and time the blueprint was last updated.
{% /tab %}

{% tab title="Example" %}

```json
{
  "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
  "LastUserId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
  "createdAt": "2022-01-01T20:59:57.340Z",
  "data": {
    "grid": "standard",
    "name": "My new blueprint",
    "version": 1
  },
  "id": "bp37712a-c507-4c62-ad8b-7d981cacb3be",
  "updatedAt": "2022-01-01T20:59:57.340Z"
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}

{% tab title="403" %}
Forbidden, insufficient privileges
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/blueprint' \
--header 'Content-Type: application/json' \
--data '{"data": "%!s(<nil>)",
}'
```

```golang
package main

import (
    "context"
    "log"
    "os"

    "github.com/DataDog/cloudcraft-go"
)

func main() {
    // Get the API key from the environment.
    key, ok := os.LookupEnv("CLOUDCRAFT_API_KEY")
    if !ok {
        log.Fatal("missing env var: CLOUDCRAFT_API_KEY")
    }

    // Check if the command line arguments are correct.
    if len(os.Args) != 2 {
        log.Fatalf("usage: %s <blueprint-name>", os.Args[0])
    }

    // Create new Config to initialize a Client.
    cfg := cloudcraft.NewConfig(key)

    // Create a new Client instance with the given Config.
    client, err := cloudcraft.NewClient(cfg)
    if err != nil {
        log.Fatal(err)
    }

    // Create a simple blueprint with the name coming from a command line argument.
    blueprint, _, err := client.Blueprint.Create(
        context.Background(),
        &cloudcraft.Blueprint{
            Data: &cloudcraft.BlueprintData{
                Name: os.Args[1],
            },
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    // Print the blueprint ID.
    log.Println(blueprint.ID)
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"AWS account name (for example prod or staging)\",\n    \"roleArn\": \"arn:aws:iam::1234567890:role/cloudcraft\"\n}\n");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/blueprint")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

data = {"data": {"grid": "standard", "name": "New blueprint"}}
result = cloudcraft.create_blueprint(data)
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("https://api.cloudcraft.co/blueprint")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "data": "%!s(<nil>)",

})

response = https.request(request)
puts response.read_body
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  HERE"data": "%!s(<nil>)",

});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/blueprint", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Delete a blueprintDELETE  /blueprint/{blueprint_id}Overview
Delete a blueprint.

When the deletion succeeds, *204 No Content* is returned.

### Path Parameters{% #path-parameters %}

- **blueprint\_id**: *UUID*. Blueprint ID. Required.
Response204401403404
{% tab title="204" %}
OK
{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}

{% tab title="403" %}
Forbidden, insufficient privileges
{% /tab %}

{% tab title="404" %}
Blueprint not found
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location --request DELETE 'https://api.cloudcraft.co/blueprint/{blueprint_id}'
```

```golang
package main

import (
    "context"
    "log"
    "os"

    "github.com/DataDog/cloudcraft-go"
)

func main() {
    // Get the API key from the environment.
    key, ok := os.LookupEnv("CLOUDCRAFT_API_KEY")
    if !ok {
        log.Fatal("missing env var: CLOUDCRAFT_API_KEY")
    }

    // Show usage if the number of command line arguments is not correct.
    if len(os.Args) != 2 {
        log.Fatalf("usage: %s <blueprint-id>", os.Args[0])
    }

    // Create new Config to initialize a Client.
    cfg := cloudcraft.NewConfig(key)

    // Create a new Client instance with the given Config.
    client, err := cloudcraft.NewClient(cfg)
    if err != nil {
        log.Fatal(err)
    }

    // Delete the blueprint with the ID taken from a command line argument.
    _, err = client.Blueprint.Delete(
        context.Background(),
        os.Args[1],
    )
    if err != nil {
        log.Fatal(err)
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/blueprint/{blueprint_id}")
  .method("DELETE", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

blueprint_id = 1234
result = cloudcraft.delete_blueprint(blueprint_id)
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/blueprint/{blueprint_id}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = https.request(request)
puts response.read_body
```

```javascript
var requestOptions = {
  method: 'DELETE',
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/blueprint/{blueprint_id}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Retrieve a blueprintGET  /blueprint/{blueprint_id}Overview
Retrieve a blueprint in JSON format.

### Path Parameters{% #path-parameters %}

- **blueprint\_id**: *UUID*. Blueprint ID. Required.
Response200401403404
{% tab title="200" %}
Retrieve blueprint
{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}

{% tab title="403" %}
Forbidden, insufficient privileges
{% /tab %}

{% tab title="404" %}
Blueprint not found
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/blueprint/{blueprint_id}'
```

```golang
package main

import (
    "context"
    "log"
    "os"

    "github.com/DataDog/cloudcraft-go"
)

func main() {
    // Get the API key from the environment.
    key, ok := os.LookupEnv("CLOUDCRAFT_API_KEY")
    if !ok {
        log.Fatal("missing env var: CLOUDCRAFT_API_KEY")
    }

    // Show usage if the number of command line arguments is not correct.
    if len(os.Args) != 2 {
        log.Fatalf("usage: %s <blueprint-id>", os.Args[0])
    }

    // Create new Config to initialize a Client.
    cfg := cloudcraft.NewConfig(key)

    // Create a new Client instance with the given Config.
    client, err := cloudcraft.NewClient(cfg)
    if err != nil {
        log.Fatal(err)
    }

    // Get the blueprint with the ID taken from a command line argument.
    blueprint, _, err := client.Blueprint.Get(
        context.Background(),
        os.Args[1],
    )
    if err != nil {
        log.Fatal(err)
    }

    // Print the blueprint ID.
    log.Println(blueprint.ID)
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/blueprint/{blueprint_id}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

blueprint_id = 1234
blueprint = cloudcraft.read_blueprint(blueprint_id)
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/blueprint/{blueprint_id}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)

response = https.request(request)
puts response.read_body
```

```javascript
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/blueprint/{blueprint_id}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Update a blueprintPUT  /blueprint/{blueprint_id}Overview
Update an existing blueprint.

The body of the request should contain the updated blueprint document in JSON format.

Optionally, a conditional update of the blueprint can be perfomed by including the *If-Match* HTTP header with the same ETag value as provided by the "Retrieve blueprint" API. If the blueprint has been modified since the retrieval, the update is rejected with a *412 Resource out of date* response. If the update succeeds, the new ETag is returned.
Response204401403404412
{% tab title="204" %}
OK
{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}

{% tab title="403" %}
Forbidden, insufficient privileges
{% /tab %}

{% tab title="404" %}
Blueprint not found
{% /tab %}

{% tab title="412" %}
Resource out of date
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location --request PUT 'https://api.cloudcraft.co/blueprint/{blueprint_id}' \
--data '{"data": "%!s(<nil>)",
}'
```

```golang
package main

import (
    "context"
    "log"
    "os"

    "github.com/DataDog/cloudcraft-go"
)

func main() {
    // Get the API key from the environment.
    key, ok := os.LookupEnv("CLOUDCRAFT_API_KEY")
    if !ok {
        log.Fatal("missing env var: CLOUDCRAFT_API_KEY")
    }

    // Check if the command line arguments are correct.
    if len(os.Args) != 3 {
        log.Fatalf("usage: %s <blueprint-id> <blueprint-name>", os.Args[0])
    }

    // Create new Config to initialize a Client.
    cfg := cloudcraft.NewConfig(key)

    // Create a new Client instance with the given Config.
    client, err := cloudcraft.NewClient(cfg)
    if err != nil {
        log.Fatal(err)
    }

    // Update the blueprint with the ID and name coming from command line
    // arguments. Add a new EC2 node to the blueprint.
    _, err = client.Blueprint.Update(
        context.Background(),
        &cloudcraft.Blueprint{
            ID:   os.Args[1],
            Name: os.Args[2],
            Data: &cloudcraft.BlueprintData{
                Name: os.Args[2],
                Nodes: []map[string]any{
                    {
                        "id":           "98172baa-a059-4b04-832d-8a7f5d14b595",
                        "type":         "ec2",
                        "region":       "us-east-1",
                        "platform":     "linux",
                        "instanceType": "m5",
                        "instanceSize": "large",
                    },
                },
            },
        },
        "",
    )
    if err != nil {
        log.Fatal(err)
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"My updated AWS Account\",\n    \"roleArn\": \"arn:aws:iam::1234567890:role/cloudcraft\"\n}\n");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/blueprint/{blueprint_id}")
  .method("PUT", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

blueprint_id = 1234
data = {
    "data": {
        "grid": "standard",
        "name": "Updated blueprint",
        "text": [
            {
                "id": "label1",
                "text": "Hello\nWorld!",
                "type": "isotext",
                "color": "#f5b720",
                "mapPos": [0, 0],
                "textSize": 15,
            }
        ],
    }
}
result = cloudcraft.update_blueprint(blueprint_id, data)
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/blueprint/{blueprint_id}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request.body = "{\n    \"name\": \"My updated AWS Account\",\n    \"roleArn\": \"arn:aws:iam::1234567890:role/cloudcraft\"\n}\n"

response = https.request(request)
puts response.read_body
```

```javascript
var raw = "{\n    \"name\": \"My updated AWS Account\",\n    \"roleArn\": \"arn:aws:iam::1234567890:role/cloudcraft\"\n}\n";

var requestOptions = {
  method: 'PUT',
  body: raw,
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/blueprint/{blueprint_id}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Export a blueprint as an imageGET  /blueprint/{blueprint_id}/{format}Overview
Render blueprint for export in SVG, PNG, PDF, or MxGraph format.

### Path Parameters{% #path-parameters %}

- **blueprint\_id**: *UUID*. Blueprint ID.
- **format**: *String*. One of "svg", "png", "pdf", or "mxGraph".

### Optional query parameters{% #optional-query-parameters %}

- **scale**: *Float*. Scale relative to original size (1.0), for example, 0.5 for half or 2.0 for double size.
- **width**: *Number*. Image width in pixels (for SVG, PNG, and PDF).
- **height**: *Number*. Image height in pixels (for SVG, PNG, and PDF).
- **grid**: *Boolean*. Enable or disable grid rendering.
- **transparent**: *Boolean*. Enable or disable transparent background rendering.
- **landscape**: *Boolean*. Enable or disable landscape paper format (PDF).
- **paperSize**: *String*. One of "Letter", "Legal", "Tabloid", "Ledger", "A0", "A1", "A2", "A3", "A4", "A5".
Response200401403404
{% tab title="200" %}
OK
{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}

{% tab title="403" %}
Forbidden, insufficient privileges
{% /tab %}

{% tab title="404" %}
Blueprint not found
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/blueprint/{blueprint_id}/{format}'
```

```golang
package main

import (
    "context"
    "log"
    "os"

    "github.com/DataDog/cloudcraft-go"
)

func main() {
    // Get the API key from the environment.
    key, ok := os.LookupEnv("CLOUDCRAFT_API_KEY")
    if !ok {
        log.Fatal("missing env var: CLOUDCRAFT_API_KEY")
    }

    // Check if the command line arguments are correct.
    if len(os.Args) != 2 {
        log.Fatalf("usage: %s <blueprint-id>", os.Args[0])
    }

    // Create new Config to initialize a Client.
    cfg := cloudcraft.NewConfig(key)

    // Create a new Client instance with the given Config.
    client, err := cloudcraft.NewClient(cfg)
    if err != nil {
        log.Fatal(err)
    }

    // Export the blueprint as an image with the given blueprint-id coming from
    // a command line argument.
    image, _, err := client.Blueprint.ExportImage(
        context.Background(),
        os.Args[1],
        "png",
        &cloudcraft.ImageExportParams{
            Width:  1920,
            Height: 1080,
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    // Save the blueprint export to a file.
    if err := os.WriteFile("blueprint.png", image, 0o600); err != nil {
        log.Fatal(err)
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/blueprint/{blueprint_id}/{format}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

blueprints = cloudcraft.list_blueprints()

blueprint_id = 1234
bp_format = "png"
export = cloudcraft.export_blueprint(blueprint_id, bp_format)
with open(f'export.{bp_format}', "wb") as binary_file:
    binary_file.write(export)
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/blueprint/{blueprint_id}/{format}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)

response = https.request(request)
puts response.read_body
```

```javascript
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/blueprint/{blueprint_id}/{format}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
