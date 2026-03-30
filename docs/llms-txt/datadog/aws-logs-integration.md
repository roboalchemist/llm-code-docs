# Source: https://docs.datadoghq.com/api/latest/aws-logs-integration.md

---
title: AWS Logs Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > AWS Logs Integration
---

# AWS Logs Integration

Configure your Datadog-AWS-Logs integration directly through Datadog API. For more information, see the [AWS integration page](https://docs.datadoghq.com/integrations/amazon_web_services/#log-collection).

## List all AWS Logs integrations{% #list-all-aws-logs-integrations %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/aws/logs |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/aws/logs |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/aws/logs      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/aws/logs      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/aws/logs     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/aws/logs |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/aws/logs |

### Overview

List all Datadog-AWS Logs integrations configured in your Datadog account. This endpoint requires the `aws_configuration_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field      | Type     | Description                                      |
| ------------ | ---------- | -------- | ------------------------------------------------ |
|              | account_id | string   | Your AWS Account ID without dashes.              |
|              | lambdas    | [object] | List of ARNs configured in your Datadog account. |
| lambdas      | arn        | string   | Available ARN IDs.                               |
|              | services   | [string] | Array of services IDs.                           |

{% /tab %}

{% tab title="Example" %}

```json
[
  {
    "account_id": "123456789101",
    "lambdas": [],
    "services": [
      "s3",
      "elb",
      "elbv2",
      "cloudfront",
      "redshift",
      "lambda"
    ]
  }
]
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List all AWS Logs integrations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.list_aws_logs_integrations()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List all AWS Logs integrations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new
p api_instance.list_aws_logs_integrations()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.aws_logs_integrations_list
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List all AWS Logs integrations returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.ListAWSLogsIntegrations(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.ListAWSLogsIntegrations`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.ListAWSLogsIntegrations`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List all AWS Logs integrations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v1.model.AWSLogsListResponse;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    try {
      List<AWSLogsListResponse> result = apiInstance.listAWSLogsIntegrations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#listAWSLogsIntegrations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AwsLogsIntegration.list()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
#####

```rust
// List all AWS Logs integrations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_logs_integration::AWSLogsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.list_aws_logs_integrations().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * List all AWS Logs integrations returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSLogsIntegrationApi(configuration);

apiInstance
  .listAWSLogsIntegrations()
  .then((data: v1.AWSLogsListResponse[]) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
## Add AWS Log Lambda ARN{% #add-aws-log-lambda-arn %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logs |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/aws/logs |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/aws/logs      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/aws/logs      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/aws/logs     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/aws/logs |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/aws/logs |

### Overview

Attach the Lambda ARN of the Lambda created for the Datadog-AWS log collection to your AWS account ID to enable log collection. This endpoint requires the `aws_configuration_edit` permission.

### Request

#### Body Data (required)

AWS Log Lambda Async request body.

{% tab title="Model" %}

| Field                        | Type   | Description                                                                                    |
| ---------------------------- | ------ | ---------------------------------------------------------------------------------------------- |
| account_id [*required*] | string | Your AWS Account ID without dashes.                                                            |
| lambda_arn [*required*] | string | ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
EOF

#####

```python
"""
Add AWS Log Lambda ARN returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi
from datadog_api_client.v1.model.aws_account_and_lambda_request import AWSAccountAndLambdaRequest

body = AWSAccountAndLambdaRequest(
    account_id="1234567",
    lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.create_aws_lambda_arn(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Add AWS Log Lambda ARN returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccountAndLambdaRequest.new({
  account_id: "1234567",
  lambda_arn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
})
p api_instance.create_aws_lambda_arn(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
    "account_id": '<AWS_ACCOUNT_ID>',
    "lambda_arn": 'arn:aws:lambda:<REGION>:<AWS_ACCOUNT_ID>:function:<LAMBDA_FUNCTION_NAME>'
  }

dog.aws_logs_add_lambda(config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Add AWS Log Lambda ARN returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.AWSAccountAndLambdaRequest{
        AccountId: "1234567",
        LambdaArn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.CreateAWSLambdaARN(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.CreateAWSLambdaARN`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.CreateAWSLambdaARN`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Add AWS Log Lambda ARN returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v1.model.AWSAccountAndLambdaRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    AWSAccountAndLambdaRequest body =
        new AWSAccountAndLambdaRequest()
            .accountId("1234567")
            .lambdaArn("arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest");

    try {
      apiInstance.createAWSLambdaARN(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#createAWSLambdaARN");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

account_id = "<AWS_ACCOUNT_ID>"
lambda_arn = "arn:aws:lambda:<REGION>:<AWS_ACCOUNT_ID>:function:<LAMBDA_FUNCTION_NAME>"

api.AwsLogsIntegration.add_log_lambda_arn(account_id=account_id, lambda_arn=lambda_arn)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
#####

```rust
// Add AWS Log Lambda ARN returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_logs_integration::AWSLogsIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSAccountAndLambdaRequest;

#[tokio::main]
async fn main() {
    let body = AWSAccountAndLambdaRequest::new(
        "1234567".to_string(),
        "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest".to_string(),
    );
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.create_aws_lambda_arn(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Add AWS Log Lambda ARN returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSLogsIntegrationApi(configuration);

const params: v1.AWSLogsIntegrationApiCreateAWSLambdaARNRequest = {
  body: {
    accountId: "1234567",
    lambdaArn:
      "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
  },
};

apiInstance
  .createAWSLambdaARN(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete an AWS Logs integration{% #delete-an-aws-logs-integration %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/aws/logs |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/aws/logs |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/aws/logs      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/aws/logs      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/aws/logs     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/aws/logs |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/aws/logs |

### Overview

Delete a Datadog-AWS logs configuration by removing the specific Lambda ARN associated with a given AWS account. This endpoint requires the `aws_configuration_edit` permission.

### Request

#### Body Data (required)

Delete AWS Lambda ARN request body.

{% tab title="Model" %}

| Field                        | Type   | Description                                                                                    |
| ---------------------------- | ------ | ---------------------------------------------------------------------------------------------- |
| account_id [*required*] | string | Your AWS Account ID without dashes.                                                            |
| lambda_arn [*required*] | string | ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
EOF

#####

```python
"""
Delete an AWS Logs integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi
from datadog_api_client.v1.model.aws_account_and_lambda_request import AWSAccountAndLambdaRequest

body = AWSAccountAndLambdaRequest(
    account_id="1234567",
    lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.delete_aws_lambda_arn(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete an AWS Logs integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccountAndLambdaRequest.new({
  account_id: "1234567",
  lambda_arn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
})
p api_instance.delete_aws_lambda_arn(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
    "account_id": '<AWS_ACCOUNT_ID>',
    "lambda_arn": 'arn:aws:lambda:<REGION>:<AWS_ACCOUNT_ID>:function:<LAMBDA_FUNCTION_NAME>'
  }

dog.aws_logs_integration_delete(config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete an AWS Logs integration returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.AWSAccountAndLambdaRequest{
        AccountId: "1234567",
        LambdaArn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.DeleteAWSLambdaARN(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.DeleteAWSLambdaARN`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.DeleteAWSLambdaARN`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete an AWS Logs integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v1.model.AWSAccountAndLambdaRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    AWSAccountAndLambdaRequest body =
        new AWSAccountAndLambdaRequest()
            .accountId("1234567")
            .lambdaArn("arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest");

    try {
      apiInstance.deleteAWSLambdaARN(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#deleteAWSLambdaARN");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

account_id = "<AWS_ACCOUNT_ID>"
lambda_arn = "arn:aws:lambda:<REGION>:<AWS_ACCOUNT_ID>:function:<LAMBDA_FUNCTION_NAME>"

api.AwsLogsIntegration.delete_config(account_id=account_id, lambda_arn=lambda_arn)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
#####

```rust
// Delete an AWS Logs integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_logs_integration::AWSLogsIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSAccountAndLambdaRequest;

#[tokio::main]
async fn main() {
    let body = AWSAccountAndLambdaRequest::new(
        "1234567".to_string(),
        "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest".to_string(),
    );
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.delete_aws_lambda_arn(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Delete an AWS Logs integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSLogsIntegrationApi(configuration);

const params: v1.AWSLogsIntegrationApiDeleteAWSLambdaARNRequest = {
  body: {
    accountId: "1234567",
    lambdaArn:
      "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
  },
};

apiInstance
  .deleteAWSLambdaARN(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get list of AWS log ready services{% #get-list-of-aws-log-ready-services %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/services |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/aws/logs/services |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/aws/logs/services      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/aws/logs/services      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/aws/logs/services     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/aws/logs/services |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services |

### Overview

**This endpoint is deprecated - use the V2 endpoint instead.** Get the list of current AWS services that Datadog offers automatic log collection. Use returned service IDs with the services parameter for the Enable an AWS service log collection API endpoint. This endpoint requires the `aws_configuration_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type   | Description                                                    |
| ----- | ------ | -------------------------------------------------------------- |
| id    | string | Key value in returned object.                                  |
| label | string | Name of service available for configuration with Datadog logs. |

{% /tab %}

{% tab title="Example" %}

```json
[
  {
    "id": "s3",
    "label": "S3 Access Logs"
  },
  {
    "id": "elb",
    "label": "Classic ELB Access Logs"
  },
  {
    "id": "elbv2",
    "label": "Application ELB Access Logs"
  },
  {
    "id": "cloudfront",
    "label": "CloudFront Access Logs"
  },
  {
    "id": "redshift",
    "label": "Redshift Logs"
  },
  {
    "id": "lambda",
    "label": "Lambda Cloudwatch Logs"
  }
]
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get list of AWS log ready services returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.list_aws_logs_services()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get list of AWS log ready services returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new
p api_instance.list_aws_logs_services()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.aws_logs_list_services
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get list of AWS log ready services returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.ListAWSLogsServices(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.ListAWSLogsServices`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.ListAWSLogsServices`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get list of AWS log ready services returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v1.model.AWSLogsListServicesResponse;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    try {
      List<AWSLogsListServicesResponse> result = apiInstance.listAWSLogsServices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#listAWSLogsServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AwsLogsIntegration.list_log_services()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
#####

```rust
// Get list of AWS log ready services returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_logs_integration::AWSLogsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.list_aws_logs_services().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get list of AWS log ready services returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSLogsIntegrationApi(configuration);

apiInstance
  .listAWSLogsServices()
  .then((data: v1.AWSLogsListServicesResponse[]) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/logs/services |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/logs/services |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/logs/services      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/logs/services      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/logs/services     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/logs/services |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/logs/services |

### Overview

Get a list of AWS services that can send logs to Datadog. This endpoint requires the `aws_configuration_read` permission.

### Response

{% tab title="200" %}
AWS Logs Services List object
{% tab title="Model" %}
AWS Logs Services response body

| Parent field | Field                           | Type     | Description                                                                    |
| ------------ | ------------------------------- | -------- | ------------------------------------------------------------------------------ |
|              | data [*required*]          | object   | AWS Logs Services response body                                                |
| data         | attributes                      | object   | AWS Logs Services response body                                                |
| attributes   | logs_services [*required*] | [string] | List of AWS services that can send logs to Datadog                             |
| data         | id [*required*]            | string   | The `AWSLogsServicesResponseData` `id`.                                        |
| data         | type [*required*]          | enum     | The `AWSLogsServicesResponseData` `type`. Allowed enum values: `logs_services` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "logs_services": [
        "s3"
      ]
    },
    "id": "logs_services",
    "type": "logs_services"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/logs/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get list of AWS log ready services returns "AWS Logs Services List object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_logs_integration_api import AWSLogsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.list_aws_logs_services()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get list of AWS log ready services returns "AWS Logs Services List object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSLogsIntegrationAPI.new
p api_instance.list_aws_logs_services()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get list of AWS log ready services returns "AWS Logs Services List object" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.ListAWSLogsServices(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.ListAWSLogsServices`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.ListAWSLogsServices`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get list of AWS log ready services returns "AWS Logs Services List object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v2.model.AWSLogsServicesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    try {
      AWSLogsServicesResponse result = apiInstance.listAWSLogsServices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#listAWSLogsServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get list of AWS log ready services returns "AWS Logs Services List object"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_logs_integration::AWSLogsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.list_aws_logs_services().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get list of AWS log ready services returns "AWS Logs Services List object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSLogsIntegrationApi(configuration);

apiInstance
  .listAWSLogsServices()
  .then((data: v2.AWSLogsServicesResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Enable an AWS Logs integration{% #enable-an-aws-logs-integration %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/services |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/aws/logs/services |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/aws/logs/services      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/aws/logs/services      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/aws/logs/services     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/aws/logs/services |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services |

### Overview

Enable automatic log collection for a list of services. This should be run after running `CreateAWSLambdaARN` to save the configuration. This endpoint requires the `aws_configuration_edit` permission.

### Request

#### Body Data (required)

Enable AWS Log Services request body.

{% tab title="Model" %}

| Field                        | Type     | Description                                                                                                                                                     |
| ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id [*required*] | string   | Your AWS Account ID without dashes.                                                                                                                             |
| services [*required*]   | [string] | Array of services IDs set to enable automatic log collection. Discover the list of available services with the get list of AWS log ready services API endpoint. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "1234567",
  "services": [
    "s3",
    "elb",
    "elbv2",
    "cloudfront",
    "redshift",
    "lambda"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "1234567",
  "services": [
    "s3",
    "elb",
    "elbv2",
    "cloudfront",
    "redshift",
    "lambda"
  ]
}
EOF

#####

```python
"""
Enable an AWS Logs integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi
from datadog_api_client.v1.model.aws_logs_services_request import AWSLogsServicesRequest

body = AWSLogsServicesRequest(
    account_id="1234567",
    services=[
        "s3",
        "elb",
        "elbv2",
        "cloudfront",
        "redshift",
        "lambda",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.enable_aws_log_services(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Enable an AWS Logs integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSLogsServicesRequest.new({
  account_id: "1234567",
  services: [
    "s3",
    "elb",
    "elbv2",
    "cloudfront",
    "redshift",
    "lambda",
  ],
})
p api_instance.enable_aws_log_services(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
    "account_id": '<AWS_ACCOUNT_ID>',
    "services": ['s3', 'elb', 'elbv2', 'cloudfront', 'redshift', 'lambda']
  }

dog.aws_logs_save_services(config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Enable an AWS Logs integration returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.AWSLogsServicesRequest{
        AccountId: "1234567",
        Services: []string{
            "s3",
            "elb",
            "elbv2",
            "cloudfront",
            "redshift",
            "lambda",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.EnableAWSLogServices(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.EnableAWSLogServices`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.EnableAWSLogServices`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Enable an AWS Logs integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v1.model.AWSLogsServicesRequest;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    AWSLogsServicesRequest body =
        new AWSLogsServicesRequest()
            .accountId("1234567")
            .services(Arrays.asList("s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"));

    try {
      apiInstance.enableAWSLogServices(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#enableAWSLogServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

account_id = "<AWS_ACCOUNT_ID"
services = ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"]

api.AwsLogsIntegration.save_services(account_id=account_id, services=services)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
#####

```rust
// Enable an AWS Logs integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_logs_integration::AWSLogsIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSLogsServicesRequest;

#[tokio::main]
async fn main() {
    let body = AWSLogsServicesRequest::new(
        "1234567".to_string(),
        vec![
            "s3".to_string(),
            "elb".to_string(),
            "elbv2".to_string(),
            "cloudfront".to_string(),
            "redshift".to_string(),
            "lambda".to_string(),
        ],
    );
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.enable_aws_log_services(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Enable an AWS Logs integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSLogsIntegrationApi(configuration);

const params: v1.AWSLogsIntegrationApiEnableAWSLogServicesRequest = {
  body: {
    accountId: "1234567",
    services: ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"],
  },
};

apiInstance
  .enableAWSLogServices(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
## Check permissions for log services{% #check-permissions-for-log-services %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/services_async |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/aws/logs/services_async |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/aws/logs/services_async      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/aws/logs/services_async      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/aws/logs/services_async     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/aws/logs/services_async |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services_async |

### Overview



Test if permissions are present to add log-forwarding triggers for the given services and AWS account. Input is the same as for `EnableAWSLogServices`. Done async, so can be repeatedly polled in a non-blocking fashion until the async request completes.

- Returns a status of `created` when it's checking if the permissions exists in the AWS account.
- Returns a status of `waiting` while checking.
- Returns a status of `checked and ok` if the Lambda exists.
- Returns a status of `error` if the Lambda does not exist.
This endpoint requires the `aws_configuration_read` permission.


### Request

#### Body Data (required)

Check AWS Logs Async Services request body.

{% tab title="Model" %}

| Field                        | Type     | Description                                                                                                                                                     |
| ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id [*required*] | string   | Your AWS Account ID without dashes.                                                                                                                             |
| services [*required*]   | [string] | Array of services IDs set to enable automatic log collection. Discover the list of available services with the get list of AWS log ready services API endpoint. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "1234567",
  "services": [
    "s3",
    "elb",
    "elbv2",
    "cloudfront",
    "redshift",
    "lambda"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A list of all Datadog-AWS logs integrations available in your Datadog organization.

| Parent field | Field   | Type     | Description               |
| ------------ | ------- | -------- | ------------------------- |
|              | errors  | [object] | List of errors.           |
| errors       | code    | string   | Code properties           |
| errors       | message | string   | Message content.          |
|              | status  | string   | Status of the properties. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "code": "no_such_config",
      "message": "AWS account 12345 has no Lambda config to update"
    }
  ],
  "status": "created"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services_async" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "1234567",
  "services": [
    "s3",
    "elb",
    "elbv2",
    "cloudfront",
    "redshift",
    "lambda"
  ]
}
EOF

#####

```python
"""
Check permissions for log services returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi
from datadog_api_client.v1.model.aws_logs_services_request import AWSLogsServicesRequest

body = AWSLogsServicesRequest(
    account_id="1234567",
    services=[
        "s3",
        "elb",
        "elbv2",
        "cloudfront",
        "redshift",
        "lambda",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.check_aws_logs_services_async(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Check permissions for log services returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSLogsServicesRequest.new({
  account_id: "1234567",
  services: [
    "s3",
    "elb",
    "elbv2",
    "cloudfront",
    "redshift",
    "lambda",
  ],
})
p api_instance.check_aws_logs_services_async(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
    "account_id": '<AWS_ACCOUNT_ID>',
    "services": ['s3', 'elb', 'elbv2', 'cloudfront', 'redshift', 'lambda']
  }

dog.aws_logs_check_services(config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Check permissions for log services returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.AWSLogsServicesRequest{
        AccountId: "1234567",
        Services: []string{
            "s3",
            "elb",
            "elbv2",
            "cloudfront",
            "redshift",
            "lambda",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.CheckAWSLogsServicesAsync(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.CheckAWSLogsServicesAsync`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.CheckAWSLogsServicesAsync`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Check permissions for log services returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v1.model.AWSLogsAsyncResponse;
import com.datadog.api.client.v1.model.AWSLogsServicesRequest;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    AWSLogsServicesRequest body =
        new AWSLogsServicesRequest()
            .accountId("1234567")
            .services(Arrays.asList("s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"));

    try {
      AWSLogsAsyncResponse result = apiInstance.checkAWSLogsServicesAsync(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#checkAWSLogsServicesAsync");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

account_id = "<AWS_ACCOUNT_ID"
services = ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"]

api.AwsLogsIntegration.check_services(account_id=account_id, services=services)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
#####

```rust
// Check permissions for log services returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_logs_integration::AWSLogsIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSLogsServicesRequest;

#[tokio::main]
async fn main() {
    let body = AWSLogsServicesRequest::new(
        "1234567".to_string(),
        vec![
            "s3".to_string(),
            "elb".to_string(),
            "elbv2".to_string(),
            "cloudfront".to_string(),
            "redshift".to_string(),
            "lambda".to_string(),
        ],
    );
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.check_aws_logs_services_async(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Check permissions for log services returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSLogsIntegrationApi(configuration);

const params: v1.AWSLogsIntegrationApiCheckAWSLogsServicesAsyncRequest = {
  body: {
    accountId: "1234567",
    services: ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"],
  },
};

apiInstance
  .checkAWSLogsServicesAsync(params)
  .then((data: v1.AWSLogsAsyncResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Check that an AWS Lambda Function exists{% #check-that-an-aws-lambda-function-exists %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/check_async |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/aws/logs/check_async |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/aws/logs/check_async      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/aws/logs/check_async      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/aws/logs/check_async     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/aws/logs/check_async |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/aws/logs/check_async |

### Overview



Test if permissions are present to add a log-forwarding triggers for the given services and AWS account. The input is the same as for Enable an AWS service log collection. Subsequent requests will always repeat the above, so this endpoint can be polled intermittently instead of blocking.

- Returns a status of 'created' when it's checking if the Lambda exists in the account.
- Returns a status of 'waiting' while checking.
- Returns a status of 'checked and ok' if the Lambda exists.
- Returns a status of 'error' if the Lambda does not exist.
This endpoint requires the `aws_configuration_read` permission.


### Request

#### Body Data (required)

Check AWS Log Lambda Async request body.

{% tab title="Model" %}

| Field                        | Type   | Description                                                                                    |
| ---------------------------- | ------ | ---------------------------------------------------------------------------------------------- |
| account_id [*required*] | string | Your AWS Account ID without dashes.                                                            |
| lambda_arn [*required*] | string | ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A list of all Datadog-AWS logs integrations available in your Datadog organization.

| Parent field | Field   | Type     | Description               |
| ------------ | ------- | -------- | ------------------------- |
|              | errors  | [object] | List of errors.           |
| errors       | code    | string   | Code properties           |
| errors       | message | string   | Message content.          |
|              | status  | string   | Status of the properties. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "code": "no_such_config",
      "message": "AWS account 12345 has no Lambda config to update"
    }
  ],
  "status": "created"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/check_async" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
EOF

#####

```python
"""
Check that an AWS Lambda Function exists returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi
from datadog_api_client.v1.model.aws_account_and_lambda_request import AWSAccountAndLambdaRequest

body = AWSAccountAndLambdaRequest(
    account_id="1234567",
    lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.check_aws_logs_lambda_async(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Check that an AWS Lambda Function exists returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccountAndLambdaRequest.new({
  account_id: "1234567",
  lambda_arn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
})
p api_instance.check_aws_logs_lambda_async(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
    "account_id": '<AWS_ACCOUNT_ID>',
    "lambda_arn": 'arn:aws:lambda:<REGION>:<AWS_ACCOUNT_ID>:function:<LAMBDA_FUNCTION_NAME>'
  }

dog.aws_logs_check_lambda(config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Check that an AWS Lambda Function exists returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.AWSAccountAndLambdaRequest{
        AccountId: "1234567",
        LambdaArn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewAWSLogsIntegrationApi(apiClient)
    resp, r, err := api.CheckAWSLogsLambdaAsync(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AWSLogsIntegrationApi.CheckAWSLogsLambdaAsync`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AWSLogsIntegrationApi.CheckAWSLogsLambdaAsync`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Check that an AWS Lambda Function exists returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsLogsIntegrationApi;
import com.datadog.api.client.v1.model.AWSAccountAndLambdaRequest;
import com.datadog.api.client.v1.model.AWSLogsAsyncResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsLogsIntegrationApi apiInstance = new AwsLogsIntegrationApi(defaultClient);

    AWSAccountAndLambdaRequest body =
        new AWSAccountAndLambdaRequest()
            .accountId("1234567")
            .lambdaArn("arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest");

    try {
      AWSLogsAsyncResponse result = apiInstance.checkAWSLogsLambdaAsync(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsLogsIntegrationApi#checkAWSLogsLambdaAsync");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

account_id = "<AWS_ACCOUNT_ID>"
lambda_arn = "arn:aws:lambda:<REGION>:<AWS_ACCOUNT_ID>:function:<FUNCTION_NAME>"

api.AwsLogsIntegration.check_lambda(account_id=account_id, lambda_arn=lambda_arn)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
#####

```rust
// Check that an AWS Lambda Function exists returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_logs_integration::AWSLogsIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSAccountAndLambdaRequest;

#[tokio::main]
async fn main() {
    let body = AWSAccountAndLambdaRequest::new(
        "1234567".to_string(),
        "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest".to_string(),
    );
    let configuration = datadog::Configuration::new();
    let api = AWSLogsIntegrationAPI::with_config(configuration);
    let resp = api.check_aws_logs_lambda_async(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Check that an AWS Lambda Function exists returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSLogsIntegrationApi(configuration);

const params: v1.AWSLogsIntegrationApiCheckAWSLogsLambdaAsyncRequest = {
  body: {
    accountId: "1234567",
    lambdaArn:
      "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
  },
};

apiInstance
  .checkAWSLogsLambdaAsync(params)
  .then((data: v1.AWSLogsAsyncResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
