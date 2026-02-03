# Source: https://docs.datadoghq.com/cloudcraft/api/aws-accounts.md

---
title: AWS Accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Cloudcraft API Reference > AWS Accounts
---

# AWS Accounts
.openapi-spec-content img{max-width:100%}.openapi-spec-content h1 a:hover,.openapi-spec-content h2 a:hover{color:#000;border-bottom:1px solid #000}List AWS accountsGET  /aws/accountOverview
List all AWS accounts linked to your Cloudcraft account.

The response is an array of AWS accounts. Each entry includes the account ID and name, access control, and user information.

The provided account IDs are required to access the other AWS-related APIs.
Response200401
{% tab title="200" %}
OKModelExample
{% tab title="Model" %}
Expand AllFieldTypeDescriptionaccounts
array

An array of AWS accounts.
{% /tab %}

{% tab title="Example" %}

```json
{
  "accounts": [
    {
      "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
      "createdAt": "2022-01-01T21:18:59.057Z",
      "externalId": "ex53e827-a724-4a2a-9fec-b13761540785",
      "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22",
      "name": "Development",
      "roleArn": "arn:aws:iam::1234567890:role/cloudcraft",
      "updatedAt": "2022-01-01T21:19:03.487Z"
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
curl --location 'https://api.cloudcraft.co/aws/account'
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

	// List all AWS accounts in the Cloudcraft account.
	accounts, _, err := client.AWS.List(context.Background())
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
  .url("https://api.cloudcraft.co/aws/account")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

accounts = cloudcraft.list_aws_accounts()
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/aws/account")

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

fetch("https://api.cloudcraft.co/aws/account", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Add an AWS accountPOST  /aws/accountOverview
Register a new AWS account with Cloudcraft.

The body of the request should contain the account properties in JSON format. The response contains the created account object, including the newly assigned ID for use with other API endpoints.

### Properties{% #properties %}

- **name**: A human-readable name for the AWS account. For example, "Production" or "Staging".
- **roleArn**: The ARN of the read-only IAM role you've created in your AWS account for Cloudcraft. The IAM role must be created with the unique external ID value of the person who generated the API key being used.
- **region**: Optional property representing the AWS region to be used for account validation. By default, the account will be validated in the us-east-1 region.
Response201401403
{% tab title="201" %}
OKModelExample
{% tab title="Model" %}
Expand AllFieldTypeDescriptionCreatorId
string

The user ID of the creator of the AWS account.
createdAt
string

The date and time the AWS account was created.
externalId
string

The unique external ID of the Cloudcraft user who created the AWS account.
id
string

The unique identifier of the AWS account.
name
string

A human-readable name for the AWS account.
roleArn
string

The ARN of the IAM role created in AWS for Cloudcraft.
updatedAt
string

The date and time the AWS account was last updated.
{% /tab %}

{% tab title="Example" %}

```json
{
  "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
  "createdAt": "2022-01-01T01:37:55.709Z",
  "externalId": "ex53e827-a724-4a2a-9fec-b13761540785",
  "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22 ",
  "name": "AWS account name (for example prod or staging)",
  "roleArn": "arn:aws:iam::1234567890:role/cloudcraft",
  "updatedAt": "2022-01-01T01:37:55.709Z"
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
curl --location 'https://api.cloudcraft.co/aws/account' \
--header 'Content-Type: application/json' \
--data '{"name": "AWS account name (for example, prod or staging)",
"roleArn": "arn:aws:iam::1234567890:role/cloudcraft",
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
		log.Fatalf("usage: %s <account-name> <role-arn>", os.Args[0])
	}

	// Create new Config to initialize a Client.
	cfg := cloudcraft.NewConfig(key)

	// Create a new Client instance with the given Config.
	client, err := cloudcraft.NewClient(cfg)
	if err != nil {
		log.Fatal(err)
	}

	// Create a new AWS Account with the name and role ARN coming from command
	// line arguments.
	account, _, err := client.AWS.Create(
		context.Background(),
		&cloudcraft.AWSAccount{
			Name:    os.Args[1],
			RoleARN: os.Args[2],
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
  .url("https://api.cloudcraft.co/aws/account")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

data = {"name": "AWS Account.", "roleArn": 'your-role-arn'}
result = cloudcraft.create_aws_account(data)
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("https://api.cloudcraft.co/aws/account")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "AWS account name (for example, prod or staging)",
"roleArn": "arn:aws:iam::1234567890:role/cloudcraft",

})

response = https.request(request)
puts response.read_body
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  HERE"name": "AWS account name (for example, prod or staging)",
"roleArn": "arn:aws:iam::1234567890:role/cloudcraft",

});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.cloudcraft.co/aws/account", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Get AWS IAM role parametersGET  /aws/account/iamParametersOverview
List the parameters required for you to register a new IAM role in AWS for use with Cloudcraft.

Combined with the AWS CLI to generate IAM roles, this endpoint can facilitate fully automated role creation at scale for organizations with many AWS accounts.
Response200401
{% tab title="200" %}
OKModelExample
{% tab title="Model" %}
Expand AllFieldTypeDescriptionaccountId
string

The AWS account ID for Cloudcraft.
awsConsoleUrl
string

The URL to the AWS IAM console with pre-filled role creation parameters.
externalId
string

The unique external ID for the Cloudcraft user.
{% /tab %}

{% tab title="Example" %}

```json
{
  "accountId": "1234567890",
  "awsConsoleUrl": "https://console.aws.amazon.com/iam/home?#/roles...",
  "externalId": "ex53e827-a724-4a2a-9fec-b13761540785"
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/aws/account/iamParameters'
```

```golang
package main

import (
	"context"
	"encoding/json"
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

	// Get the IAM parameters required for registering a new IAM Role in AWS for
	// use with Cloudcraft.
	params, _, err := client.AWS.IAMParameters(context.Background())
	if err != nil {
		log.Fatal(err)
	}

	// Pretty print all IAM parameters returned by the API.
	pretty, _ := json.MarshalIndent(params, "", "  ")

	log.Println(string(pretty))
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.cloudcraft.co/aws/account/iamParameters")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

params = cloudcraft.read_aws_role_parameters()
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/aws/account/iamParameters")

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

fetch("https://api.cloudcraft.co/aws/account/iamParameters", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Delete AWS accountDELETE  /aws/account/{account_id}Overview
Delete a registered AWS account.

### Path Parameters{% #path-parameters %}

- **account\_id**: *UUID*. AWS account ID. Required.
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
AWS account not found
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location --request DELETE 'https://api.cloudcraft.co/aws/account/{account_id}'
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

	// Delete the AWS account with the ID taken from a command line argument.
	_, err = client.AWS.Delete(
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
  .url("https://api.cloudcraft.co/aws/account/{account_id}")
  .method("DELETE", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

account_id = 'your account id'
result = cloudcraft.delete_aws_account(account_id)
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/aws/account/{account_id}")

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

fetch("https://api.cloudcraft.co/aws/account/{account_id}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Update an AWS accountPUT  /aws/account/{account_id}Overview
Update an AWS account registered in Cloudcraft.

The body of the request should contain the account properties in JSON format. The response contains the updated account object.

### Properties{% #properties %}

- **name**: A human-readable name for the AWS account. For example, "Production" or "Staging".
- **roleArn**: The ARN of the read-only IAM role you've created in your AWS account for Cloudcraft. The IAM role must be created with the unique external ID value of the person who generated the API key being used.
Response200401403
{% tab title="200" %}
OK
{% /tab %}

{% tab title="401" %}
Unauthorized
{% /tab %}

{% tab title="403" %}
Forbidden, insufficient privileges
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location --request PUT 'https://api.cloudcraft.co/aws/account/{account_id}' \
--data '{"name": "My updated AWS Account",
"roleArn": "arn:aws:iam::1234567890:role/cloudcraft",
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
	if len(os.Args) != 4 {
		log.Fatalf("usage: %s <account-id> <account-name> <role-arn>", os.Args[0])
	}

	// Create new Config to initialize a Client.
	cfg := cloudcraft.NewConfig(key)

	// Create a new Client instance with the given Config.
	client, err := cloudcraft.NewClient(cfg)
	if err != nil {
		log.Fatal(err)
	}

	// Update the AWS Account with the ID, name and role ARN coming from command
	// line arguments.
	_, err = client.AWS.Update(
		context.Background(),
		&cloudcraft.AWSAccount{
			ID:      os.Args[1],
			Name:    os.Args[2],
			RoleARN: os.Args[3],
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
  .url("https://api.cloudcraft.co/aws/account/{account_id}")
  .method("PUT", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

account_id = 'your account id'
data = {"name": "Updated AWS Account.", "roleArn": 'your-role-arn'}
result = cloudcraft.update_aws_account(account_id, data)
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/aws/account/{account_id}")

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

fetch("https://api.cloudcraft.co/aws/account/{account_id}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Snapshot AWS accountGET  /aws/account/{account_id}/{region}/{format}Overview
Scan and render one region of an AWS account into a blueprint in JSON, SVG, PNG, PDF, or MxGraph format.

The time required to generate the snapshot depends on the number of resources in the AWS region.

The API behaves as a long poll, with a wait time of up to 120 seconds for the result. For mostenvironments, the API call will therefore directly return a blueprint. Ifthe wait time is exceeded, a `202 Accepted` response is returned with a`{code: STILL_PROCESSING, retry: true ...}` JSON body. The snapshot will continue processing in the background, and a retry will either immediately return the result or continue waiting.

### Path Parameters{% #path-parameters %}

- **account\_id**: *UUID*. The AWS account ID as registered with Cloudcraft.
- **region**: *String*. The AWS region, for example, "us-east-1".
- **format**: *String*. One of "json", "svg", "png", "pdf", "mxGraph".

### Optional query parameters{% #optional-query-parameters %}

- **filter**: *String*. Render a subset of the AWS account. Accepts a filter expression as used on the **Live** tab in the web application. The filter expression terms must be separated by spaces. The terms are substrings to be matched, key-value pairs, logical operators, or parentheses. For example, `env=dev OR env=test`.
- **exclude**: *List of Strings*. Exclude AWS services by name. For example, "ec2,sg" to exclude both EC2s and Security Groups. The service value is specified by the "type" field of Blueprint components.
- **label**: *Boolean*. Automatically label all components. Defaults to true.
- **autoconnect**: *Boolean*. Automatically connect all components. Defaults to true.
- **scale**: *Float*. Scale relative to original size (1.0). For example, 0.5 for half or 2.0 for double size.
- **width**: *Number*. Image width in pixels (for SVG, PNG, and PDF).
- **height**: *Number*. Image height in pixels (for SVG, PNG, and PDF).
- **grid**: *Boolean*. Enable or disable grid rendering.
- **transparent**: *Boolean*. Enable or disable transparent background rendering.
- **landscape**: *Boolean*. Enable or disable landscape paper format (PDF).
- **paperSize**: *String*. Applies when the format is PDF. One of "Letter", "Legal", "Tabloid", "Ledger", "A0", "A1", "A2", "A3", "A4", or "A5".
- **projection**: *String*. The visual style of the diagram. One of "isometric" or "2d".
- **theme**: *String*. The color theme of the diagram. One of "light" or "dark".
Response200202401403404
{% tab title="200" %}
OK
{% /tab %}

{% tab title="202" %}
Wait time exceededModelExample
{% tab title="Model" %}
Expand AllFieldTypeDescriptioncode
string

A code indicating the status of the snapshot generation.
message
string

A message explaining the reason for the 202 response.
retry
boolean

A flag indicating whether the client should retry the request.
{% /tab %}

{% tab title="Example" %}

```json
{
  "code": "STILL_PROCESSING",
  "message": "Result wait time exceeded. Processing continues in the background, retry to receive result.",
  "retry": true
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

{% tab title="404" %}
AWS account not found
{% /tab %}
Code Example.chroma{max-height:350px;overflow:hidden;overflow-y:scroll}
```bash
curl --location 'https://api.cloudcraft.co/aws/account/{account_id}/{region}/{format}'
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

	// Create a new snapshot of the us-east-1 region with the given account-id
	// coming from a command line argument.
	snapshot, _, err := client.AWS.Snapshot(
		context.Background(),
		os.Args[1],
		"us-east-1",
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
  .url("https://api.cloudcraft.co/aws/account/{account_id}/{region}/{format}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```python
from cloudcraftco import Cloudcraft

cloudcraft = Cloudcraft()

account_id = 1234
options = {"grid": True, "scale": 1.5}
region = "us-east-1"
file_format = "png"
snapshot = cloudcraft.snapshot_aws_account(account_id, region, file_format, options)
with open(f'snapshot.{file_format}', "wb") as binary_file:
    binary_file.write(snapshot)
```

```ruby
require "uri"
require "net/http"

url = URI("https://api.cloudcraft.co/aws/account/{account_id}/{region}/{format}")

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

fetch("https://api.cloudcraft.co/aws/account/{account_id}/{region}/{format}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
