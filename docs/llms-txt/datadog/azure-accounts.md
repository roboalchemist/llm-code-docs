# Source: https://docs.datadoghq.com/cloudcraft/api/azure-accounts.md

---
title: Azure Accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Cloudcraft API Reference > Azure Accounts
source_url: https://docs.datadoghq.com/api/azure-accounts/index.html
---

# Azure Accounts
.openapi-spec-content img{max-width:100%}.openapi-spec-content h1 a:hover,.openapi-spec-content h2 a:hover{color:#000;border-bottom:1px solid #000}List Azure accountsGET&nbsp; /azure/accountOverview
List all Azure accounts linked to your Cloudcraft account.

The response is an array of Azure accounts. Each entry includes the account ID and name, access control, and user information.

The provided account IDs are required to access the other Azure-related APIs.
Response200401OKUnauthorizedCode Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/azure/account'
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

	// List all Azure accounts in the Cloudcraft account.
	accounts, _, err := client.Azure.List(context.Background())
	if err != nil {
		log.Fatal(err)
	}

	// Print the name of each account.
	for _, account := range accounts {
		log.Println(account.Name)
	}
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/azure/account")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
import http.client

conn = http.client.HTTPSConnection("api.cloudcraft.co")
payload = ''
headers = {}
conn.request("GET", "/azure/account", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/azure/account")

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

fetch("https://api.cloudcraft.co/azure/account", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Add an Azure accountPOST&nbsp; /azure/accountOverview
Register a new Azure account with Cloudcraft.

The body of the request should contain the account properties in JSON format. The response contains the created account object, including the newly assigned ID for use with other API endpoints.

### Properties{% #properties %}

- **name**: A human-readable name for the Azure account. For example, "Production" or "Staging".
- **subscriptionId**: Subscription ID of your Azure account.
- **directoryId**: Azure Tenant or Directory ID.
- **applicationId**: Identifier of the application registered with Azure
- **clientSecret**: Client secret associated with the registered application.
Response201401403OKModelExampleExpand AllFieldTypeDescriptionCreatorId
string

The user ID of the creator of the Azure account.
applicationId
string

Identifier of the application registered with Azure.
createdAt
string

The date and time the Azure account was created.
directoryId
string

The Azure Tenant or Directory ID.
id
string

The unique identifier of the Azure account.
name
string

A human-readable name for the Azure account.
subscriptionId
string

Subscription ID of the Azure account.
updatedAt
string

The date and time the Azure account was last updated.

```json
{
  "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
  "applicationId": "azapp737-4763-4fc4-9d2b-c5f4d07d22df",
  "createdAt": "2022-01-01T21:18:59.057Z",
  "directoryId": "azdirc44-0230-4732-9e70-cc00736f0a97",
  "id": "azfda35c-82fe-4edf-b9e9-ffd48f041c22",
  "name": "Development",
  "subscriptionId": "azsub827-5f07-45ce-8f2b-6c5001db5c6f",
  "updatedAt": "2022-01-01T21:19:03.487Z"
}
```
UnauthorizedForbidden, insufficient privilegesCode Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/azure/account' \
--header 'Content-Type: application/json' \
--data '{"applicationId": "azapp737-4763-4fc4-9d2b-c5f4d07d22df",
"clientSecret": "secret~AIaxaBYlVBkbBhJIqhP9iXgh4c1jpdyaa9",
"directoryId": "azdirc44-0230-4732-9e70-cc00736f0a97",
"name": "Development",
"subscriptionId": "azsub827-5f07-45ce-8f2b-6c5001db5c6f",
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
	if len(os.Args) != 6 {
		log.Fatalf("usage: %s <account-name> <app-id> <dir-id> <sub-id> <secret>", os.Args[0])
	}

	// Create new Config to initialize a Client.
	cfg := cloudcraft.NewConfig(key)

	// Create a new Client instance with the given Config.
	client, err := cloudcraft.NewClient(cfg)
	if err != nil {
		log.Fatal(err)
	}

	// Create a new Azure Account with the details coming from command line
	// arguments.
	account, _, err := client.Azure.Create(
		context.Background(),
		&cloudcraft.AzureAccount{
			Name:           os.Args[1],
			ApplicationID:  os.Args[2],
			DirectoryID:    os.Args[3],
			SubscriptionID: os.Args[4],
			ClientSecret:   os.Args[5],
		})
	if err != nil {
		log.Fatal(err)
	}

	// Print the account ID.
	log.Println(account.ID)
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"AWS account name (for example prod or staging)\",\n    \"roleArn\": \"arn:aws:iam::1234567890:role/cloudcraft\"\n}\n");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/azure/account")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```python
import http.client
import json

conn = http.client.HTTPSConnection("api.cloudcraft.co")
payload = json.dumps({
  "applicationId": "azapp737-4763-4fc4-9d2b-c5f4d07d22df",
"clientSecret": "secret~AIaxaBYlVBkbBhJIqhP9iXgh4c1jpdyaa9",
"directoryId": "azdirc44-0230-4732-9e70-cc00736f0a97",
"name": "Development",
"subscriptionId": "azsub827-5f07-45ce-8f2b-6c5001db5c6f",

})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/azure/account", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("https://api.cloudcraft.co/azure/account")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "applicationId": "azapp737-4763-4fc4-9d2b-c5f4d07d22df",
"clientSecret": "secret~AIaxaBYlVBkbBhJIqhP9iXgh4c1jpdyaa9",
"directoryId": "azdirc44-0230-4732-9e70-cc00736f0a97",
"name": "Development",
"subscriptionId": "azsub827-5f07-45ce-8f2b-6c5001db5c6f",

})

response = https.request(request)
puts response.read_body
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  HERE"applicationId": "azapp737-4763-4fc4-9d2b-c5f4d07d22df",
"clientSecret": "secret~AIaxaBYlVBkbBhJIqhP9iXgh4c1jpdyaa9",
"directoryId": "azdirc44-0230-4732-9e70-cc00736f0a97",
"name": "Development",
"subscriptionId": "azsub827-5f07-45ce-8f2b-6c5001db5c6f",

});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/azure/account", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Delete an Azure accountDELETE&nbsp; /azure/account/{account_id}Overview
Delete a registered Azure account.

### Path Parameters{% #path-parameters %}

- **account\_id**: *UUID*. Azure account ID. Required.
Response204401403404No ContentUnauthorizedForbidden, insufficient privilegesAzure account not foundCode Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location --request DELETE 'https://api.cloudcraft.co/azure/account/{account_id}'
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
		log.Fatalf("usage: %s <account-id>", os.Args[0])
	}

	// Create new Config to initialize a Client.
	cfg := cloudcraft.NewConfig(key)

	// Create a new Client instance with the given Config.
	client, err := cloudcraft.NewClient(cfg)
	if err != nil {
		log.Fatal(err)
	}

	// Delete the Azure account with the ID taken from a command line argument.
	_, err = client.Azure.Delete(
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
  .url("https://api.cloudcraft.co/azure/account/{account_id}")
  .method("DELETE", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
import http.client

conn = http.client.HTTPSConnection("api.cloudcraft.co")
payload = ''
headers = {}
conn.request("DELETE", "/azure/account/{account_id}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/azure/account/{account_id}")

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

fetch("https://api.cloudcraft.co/azure/account/{account_id}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Update an Azure accountPUT&nbsp; /azure/account/{account_id}Overview
Update an Azure account registered in Cloudcraft.

The body of the request should contain the account properties in JSON format. The response contains the updated account object.

### Path Parameters{% #path-parameters %}

- **account\_id**: *UUID*. Azure account ID. Required.

### Properties{% #properties %}

- **name**: A human-readable name for the Azure account. For example, "Production" or "Staging".
- **subscriptionId**: Subscription ID of your Azure account.
- **directoryId**: Azure Tenant or Directory ID.
- **applicationId**: Identifier of the application registered with Azure.
- **clientSecret**: Client secret associated with the registered application.
Response200401403OKUnauthorizedForbidden, insufficient privilegesCode Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location --request PUT 'https://api.cloudcraft.co/azure/account/{account_id}' \
--data '{"applicationId": "azapp737-4763-4fc4-9d2b-c5f4d07d22df",
"clientSecret": "secret~AIaxaBYlVBkbBhJIqhP9iXgh4c1jpdyaa9",
"directoryId": "azdirc44-0230-4732-9e70-cc00736f0a97",
"name": "Development123",
"subscriptionId": "azsub827-5f07-45ce-8f2b-6c5001db5c6f",
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
	if len(os.Args) != 5 {
		log.Fatalf("usage: %s <account-name> <app-id> <dir-id> <sub-id>", os.Args[0])
	}

	// Create new Config to initialize a Client.
	cfg := cloudcraft.NewConfig(key)

	// Create a new Client instance with the given Config.
	client, err := cloudcraft.NewClient(cfg)
	if err != nil {
		log.Fatal(err)
	}

	// Create a new Azure Account with the details coming from command line
	// arguments.
	_, err = client.Azure.Update(
		context.Background(),
		&cloudcraft.AzureAccount{
			Name:           os.Args[1],
			ApplicationID:  os.Args[2],
			DirectoryID:    os.Args[3],
			SubscriptionID: os.Args[4],
		})
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
  .url("https://api.cloudcraft.co/azure/account/{account_id}")
  .method("PUT", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
import http.client

conn = http.client.HTTPSConnection("api.cloudcraft.co")
payload = "{\n    \"name\": \"My updated AWS Account\",\n    \"roleArn\": \"arn:aws:iam::1234567890:role/cloudcraft\"\n}\n"
headers = {}
conn.request("PUT", "/azure/account/{account_id}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/azure/account/{account_id}")

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

fetch("https://api.cloudcraft.co/azure/account/{account_id}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Snapshot an Azure accountGET&nbsp; /azure/account/{account_id}/{region}/{format}Overview
Scan and render one region of an Azure account into a blueprint in JSON, SVG, PNG, PDF, or MxGraph format.

The time required to generate the snapshot depends on the number of resources in the Azure region.

The API behaves as a long poll, with a wait time of up to 120 seconds for the result. For mostenvironments, the API call returns a blueprint. Ifthe wait time is exceeded, a `202 Accepted` response is returned with a`{code: STILL_PROCESSING, retry: true ...}` JSON body. The snapshot will continue processing in the background, and a retry will either immediately return the result or continue waiting.

### Path Parameters{% #path-parameters %}

- **account\_id**: *UUID*. Azure Account ID as registered with Cloudcraft.
- **region**: *String*. Azure region, for example, "eastus".
- **format**: *String*. One of "json", "svg", "png", "pdf", or "mxGraph".

### Optional query parameters{% #optional-query-parameters %}

- **filter**: *String*. Render a subset of the Azure account. Accepts a filter expression as used on the **Live** tab in the web application. The filter expression terms must be separated by spaces. The terms are substrings to be matched, key-value pairs, logical operators, or parentheses. For example, `env=dev OR env=test`.
- **exclude**: *List of Strings*. Exclude Azure services by name. For example, "azurevmss,azurensg" to exclude both Virtual Machine Scale Set and Network Security Groups. The service value is specified by the "type" field of Blueprint components.
- **label**: *Boolean*. Automatically label all components. Defaults to true.
- **autoconnect**: *Boolean*. Automatically connect all components. Defaults to true.
- **scale**: *Float*. Scale relative to original size (1.0), for example, 0.5 for half or 2.0 for double size.
- **width**: *Number*. Image width in pixels (for SVG, PNG, and PDF).
- **height**: *Number*. Image height in pixels (for SVG, PNG, and PDF).
- **grid**: *Boolean*. Enable or disable grid rendering.
- **transparent**: *Boolean*. Enable or disable transparent background rendering.
- **landscape**: *Boolean*. Enable or disable landscape paper format (PDF).
- **paperSize**: *String*. Applies when the format is PDF. One of "Letter", "Legal", "Tabloid", "Ledger", "A0", "A1", "A2", "A3", "A4", "A5".
- **projection**: *String*. The visual style of the diagram. One of "isometric" or "2d".
- **theme**: *String*. The color theme of the diagram. One of "light" or "dark".
Response200202401403404OKWait time exceededModelExampleExpand AllFieldTypeDescriptioncode
string

&nbsp;
message
string

&nbsp;
retry
boolean

&nbsp;

```json
{
  "code": "STILL_PROCESSING",
  "message": "Result wait time exceeded. Processing continues in the background, retry to receive result.",
  "retry": true
}
```
UnauthorizedForbidden, insufficient privilegesAzure account not foundCode Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/azure/account/{account_id}/{region}/{format}'
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
		log.Fatalf("usage: %s <account-id>", os.Args[0])
	}

	// Create new Config to initialize a Client.
	cfg := cloudcraft.NewConfig(key)

	// Create a new Client instance with the given Config.
	client, err := cloudcraft.NewClient(cfg)
	if err != nil {
		log.Fatal(err)
	}

	// Create a new snapshot of the centralus region with the given account-id
	// coming from a command line argument.
	snapshot, _, err := client.Azure.Snapshot(
		context.Background(),
		os.Args[1],
		"centralus",
		"png",
		&cloudcraft.SnapshotParams{
			Width:  1920,
			Height: 1080,
		},
	)
	if err != nil {
		log.Fatal(err)
	}

	// Save the snapshot to a file.
	if err := os.WriteFile("snapshot.png", snapshot, 0o600); err != nil {
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
  .url("https://api.cloudcraft.co/azure/account/{account_id}/{region}/{format}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
import http.client

conn = http.client.HTTPSConnection("api.cloudcraft.co")
payload = ''
headers = {}
conn.request("GET", "/azure/account/{account_id}/{region}/{format}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/azure/account/{account_id}/{region}/{format}")

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

fetch("https://api.cloudcraft.co/azure/account/{account_id}/{region}/{format}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
