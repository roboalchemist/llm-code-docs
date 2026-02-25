# Source: https://docs.datadoghq.com/api/latest/agentless-scanning.md

---
title: Agentless Scanning
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Agentless Scanning
---

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

# Agentless Scanning

Datadog Agentless Scanning provides visibility into risks and vulnerabilities within your hosts, running containers, and serverless functionsâall without requiring teams to install Agents on every host or where Agents cannot be installed. Agentless offers also Sensitive Data Scanning capabilities on your storage. Go to [https://www.datadoghq.com/blog/agentless-scanning/](https://www.datadoghq.com/blog/agentless-scanning/) to learn more.

## List AWS scan options{% #list-aws-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws |

### Overview

Fetches the scan options configured for AWS accounts.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of AWS scan options.

| Parent field | Field              | Type     | Description                                                                                                      |
| ------------ | ------------------ | -------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data               | [object] | A list of AWS scan options.                                                                                      |
| data         | attributes         | object   | Attributes for the AWS scan options.                                                                             |
| attributes   | lambda             | boolean  | Indicates if scanning of Lambda functions is enabled.                                                            |
| attributes   | sensitive_data     | boolean  | Indicates if scanning for sensitive data is enabled.                                                             |
| attributes   | vuln_containers_os | boolean  | Indicates if scanning for vulnerabilities in containers is enabled.                                              |
| attributes   | vuln_host_os       | boolean  | Indicates if scanning for vulnerabilities in hosts is enabled.                                                   |
| data         | id                 | string   | The ID of the AWS account.                                                                                       |
| data         | type               | enum     | The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "lambda": true,
        "sensitive_data": false,
        "vuln_containers_os": true,
        "vuln_host_os": true
      },
      "id": "184366314700",
      "type": "aws_scan_options"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List AWS scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.list_aws_scan_options()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List AWS scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_aws_scan_options()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List AWS scan options returns "OK" response

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
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.ListAwsScanOptions(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.ListAwsScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.ListAwsScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List AWS scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AwsScanOptionsListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      AwsScanOptionsListResponse result = apiInstance.listAwsScanOptions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#listAwsScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List AWS scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.list_aws_scan_options().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List AWS scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

apiInstance
  .listAwsScanOptions()
  .then((data: v2.AwsScanOptionsListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create AWS scan options{% #create-aws-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws |

### Overview

Activate Agentless scan options for an AWS account.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Request

#### Body Data (required)

The definition of the new scan options.

{% tab title="Model" %}

| Parent field | Field                                | Type    | Description                                                                                                      |
| ------------ | ------------------------------------ | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]               | object  | Object for the scan options of a single AWS account.                                                             |
| data         | attributes [*required*]         | object  | Attributes for the AWS scan options to create.                                                                   |
| attributes   | lambda [*required*]             | boolean | Indicates if scanning of Lambda functions is enabled.                                                            |
| attributes   | sensitive_data [*required*]     | boolean | Indicates if scanning for sensitive data is enabled.                                                             |
| attributes   | vuln_containers_os [*required*] | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                              |
| attributes   | vuln_host_os [*required*]       | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                   |
| data         | id [*required*]                 | string  | The ID of the AWS account.                                                                                       |
| data         | type [*required*]               | enum    | The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "lambda": true,
      "sensitive_data": false,
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "123456789012",
    "type": "aws_scan_options"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Agentless scan options enabled successfully.
{% tab title="Model" %}
Response object that includes the scan options of an AWS account.

| Parent field | Field              | Type    | Description                                                                                                      |
| ------------ | ------------------ | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data               | object  | Single AWS Scan Options entry.                                                                                   |
| data         | attributes         | object  | Attributes for the AWS scan options.                                                                             |
| attributes   | lambda             | boolean | Indicates if scanning of Lambda functions is enabled.                                                            |
| attributes   | sensitive_data     | boolean | Indicates if scanning for sensitive data is enabled.                                                             |
| attributes   | vuln_containers_os | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                              |
| attributes   | vuln_host_os       | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                   |
| data         | id                 | string  | The ID of the AWS account.                                                                                       |
| data         | type               | enum    | The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "lambda": true,
      "sensitive_data": false,
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "184366314700",
    "type": "aws_scan_options"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="409" %}
Conflict
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "lambda": true,
      "sensitive_data": false,
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "123456789012",
    "type": "aws_scan_options"
  }
}
EOF

#####

```python
"""
Create AWS scan options returns "Agentless scan options enabled successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.aws_scan_options_create_attributes import AwsScanOptionsCreateAttributes
from datadog_api_client.v2.model.aws_scan_options_create_data import AwsScanOptionsCreateData
from datadog_api_client.v2.model.aws_scan_options_create_request import AwsScanOptionsCreateRequest
from datadog_api_client.v2.model.aws_scan_options_type import AwsScanOptionsType

body = AwsScanOptionsCreateRequest(
    data=AwsScanOptionsCreateData(
        id="000000000003",
        type=AwsScanOptionsType.AWS_SCAN_OPTIONS,
        attributes=AwsScanOptionsCreateAttributes(
            _lambda=True,
            sensitive_data=False,
            vuln_containers_os=True,
            vuln_host_os=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_aws_scan_options(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create AWS scan options returns "Agentless scan options enabled successfully." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

body = DatadogAPIClient::V2::AwsScanOptionsCreateRequest.new({
  data: DatadogAPIClient::V2::AwsScanOptionsCreateData.new({
    id: "000000000003",
    type: DatadogAPIClient::V2::AwsScanOptionsType::AWS_SCAN_OPTIONS,
    attributes: DatadogAPIClient::V2::AwsScanOptionsCreateAttributes.new({
      lambda: true,
      sensitive_data: false,
      vuln_containers_os: true,
      vuln_host_os: true,
    }),
  }),
})
p api_instance.create_aws_scan_options(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create AWS scan options returns "Agentless scan options enabled successfully." response

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
    body := datadogV2.AwsScanOptionsCreateRequest{
        Data: datadogV2.AwsScanOptionsCreateData{
            Id:   "000000000003",
            Type: datadogV2.AWSSCANOPTIONSTYPE_AWS_SCAN_OPTIONS,
            Attributes: datadogV2.AwsScanOptionsCreateAttributes{
                Lambda:           true,
                SensitiveData:    false,
                VulnContainersOs: true,
                VulnHostOs:       true,
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.CreateAwsScanOptions(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.CreateAwsScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.CreateAwsScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create AWS scan options returns "Agentless scan options enabled successfully." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AwsScanOptionsCreateAttributes;
import com.datadog.api.client.v2.model.AwsScanOptionsCreateData;
import com.datadog.api.client.v2.model.AwsScanOptionsCreateRequest;
import com.datadog.api.client.v2.model.AwsScanOptionsResponse;
import com.datadog.api.client.v2.model.AwsScanOptionsType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    AwsScanOptionsCreateRequest body =
        new AwsScanOptionsCreateRequest()
            .data(
                new AwsScanOptionsCreateData()
                    .id("000000000003")
                    .type(AwsScanOptionsType.AWS_SCAN_OPTIONS)
                    .attributes(
                        new AwsScanOptionsCreateAttributes()
                            .lambda(true)
                            .sensitiveData(false)
                            .vulnContainersOs(true)
                            .vulnHostOs(true)));

    try {
      AwsScanOptionsResponse result = apiInstance.createAwsScanOptions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#createAwsScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Create AWS scan options returns "Agentless scan options enabled successfully."
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;
use datadog_api_client::datadogV2::model::AwsScanOptionsCreateAttributes;
use datadog_api_client::datadogV2::model::AwsScanOptionsCreateData;
use datadog_api_client::datadogV2::model::AwsScanOptionsCreateRequest;
use datadog_api_client::datadogV2::model::AwsScanOptionsType;

#[tokio::main]
async fn main() {
    let body = AwsScanOptionsCreateRequest::new(AwsScanOptionsCreateData::new(
        AwsScanOptionsCreateAttributes::new(true, false, true, true),
        "000000000003".to_string(),
        AwsScanOptionsType::AWS_SCAN_OPTIONS,
    ));
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.create_aws_scan_options(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create AWS scan options returns "Agentless scan options enabled successfully." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiCreateAwsScanOptionsRequest = {
  body: {
    data: {
      id: "000000000003",
      type: "aws_scan_options",
      attributes: {
        lambda: true,
        sensitiveData: false,
        vulnContainersOs: true,
        vulnHostOs: true,
      },
    },
  },
};

apiInstance
  .createAwsScanOptions(params)
  .then((data: v2.AwsScanOptionsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get AWS scan options{% #get-aws-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws/{account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws/{account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |

### Overview

Fetches the Agentless scan options for an activated account.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description               |
| ---------------------------- | ------ | ------------------------- |
| account_id [*required*] | string | The ID of an AWS account. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes the scan options of an AWS account.

| Parent field | Field              | Type    | Description                                                                                                      |
| ------------ | ------------------ | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data               | object  | Single AWS Scan Options entry.                                                                                   |
| data         | attributes         | object  | Attributes for the AWS scan options.                                                                             |
| attributes   | lambda             | boolean | Indicates if scanning of Lambda functions is enabled.                                                            |
| attributes   | sensitive_data     | boolean | Indicates if scanning for sensitive data is enabled.                                                             |
| attributes   | vuln_containers_os | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                              |
| attributes   | vuln_host_os       | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                   |
| data         | id                 | string  | The ID of the AWS account.                                                                                       |
| data         | type               | enum    | The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "lambda": true,
      "sensitive_data": false,
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "184366314700",
    "type": "aws_scan_options"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport account_id="123456789012"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get AWS scan options returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

# there is a valid "aws_scan_options" in the system
AWS_SCAN_OPTIONS_ID = environ["AWS_SCAN_OPTIONS_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.get_aws_scan_options(
        account_id=AWS_SCAN_OPTIONS_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get AWS scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

# there is a valid "aws_scan_options" in the system
AWS_SCAN_OPTIONS_ID = ENV["AWS_SCAN_OPTIONS_ID"]
p api_instance.get_aws_scan_options(AWS_SCAN_OPTIONS_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get AWS scan options returns "OK" response

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
    // there is a valid "aws_scan_options" in the system
    AwsScanOptionsID := os.Getenv("AWS_SCAN_OPTIONS_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.GetAwsScanOptions(ctx, AwsScanOptionsID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.GetAwsScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.GetAwsScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get AWS scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AwsScanOptionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    // there is a valid "aws_scan_options" in the system
    String AWS_SCAN_OPTIONS_ID = System.getenv("AWS_SCAN_OPTIONS_ID");

    try {
      AwsScanOptionsResponse result = apiInstance.getAwsScanOptions(AWS_SCAN_OPTIONS_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#getAwsScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Get AWS scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    // there is a valid "aws_scan_options" in the system
    let aws_scan_options_id = std::env::var("AWS_SCAN_OPTIONS_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.get_aws_scan_options(aws_scan_options_id.clone()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get AWS scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

// there is a valid "aws_scan_options" in the system
const AWS_SCAN_OPTIONS_ID = process.env.AWS_SCAN_OPTIONS_ID as string;

const params: v2.AgentlessScanningApiGetAwsScanOptionsRequest = {
  accountId: AWS_SCAN_OPTIONS_ID,
};

apiInstance
  .getAwsScanOptions(params)
  .then((data: v2.AwsScanOptionsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update AWS scan options{% #update-aws-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws/{account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws/{account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |

### Overview

Update the Agentless scan options for an activated account.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description               |
| ---------------------------- | ------ | ------------------------- |
| account_id [*required*] | string | The ID of an AWS account. |

### Request

#### Body Data (required)

New definition of the scan options.

{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                                                      |
| ------------ | ---------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object  | Object for the scan options of a single AWS account.                                                             |
| data         | attributes [*required*] | object  | Attributes for the AWS scan options to update.                                                                   |
| attributes   | lambda                       | boolean | Indicates if scanning of Lambda functions is enabled.                                                            |
| attributes   | sensitive_data               | boolean | Indicates if scanning for sensitive data is enabled.                                                             |
| attributes   | vuln_containers_os           | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                              |
| attributes   | vuln_host_os                 | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                   |
| data         | id [*required*]         | string  | The ID of the AWS account.                                                                                       |
| data         | type [*required*]       | enum    | The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "aws_scan_options",
    "id": "000000000002",
    "attributes": {
      "vuln_host_os": true,
      "vuln_containers_os": true,
      "lambda": false
    }
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                          \# Path parametersexport account_id="123456789012"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/${account_id}" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "aws_scan_options",
    "id": "000000000002",
    "attributes": {
      "vuln_host_os": true,
      "vuln_containers_os": true,
      "lambda": false
    }
  }
}
EOF

#####

```go
// Update AWS scan options returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.AwsScanOptionsUpdateRequest{
        Data: datadogV2.AwsScanOptionsUpdateData{
            Type: datadogV2.AWSSCANOPTIONSTYPE_AWS_SCAN_OPTIONS,
            Id:   "000000000002",
            Attributes: datadogV2.AwsScanOptionsUpdateAttributes{
                VulnHostOs:       datadog.PtrBool(true),
                VulnContainersOs: datadog.PtrBool(true),
                Lambda:           datadog.PtrBool(false),
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    r, err := api.UpdateAwsScanOptions(ctx, "000000000002", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.UpdateAwsScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update AWS scan options returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AwsScanOptionsType;
import com.datadog.api.client.v2.model.AwsScanOptionsUpdateAttributes;
import com.datadog.api.client.v2.model.AwsScanOptionsUpdateData;
import com.datadog.api.client.v2.model.AwsScanOptionsUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    AwsScanOptionsUpdateRequest body =
        new AwsScanOptionsUpdateRequest()
            .data(
                new AwsScanOptionsUpdateData()
                    .type(AwsScanOptionsType.AWS_SCAN_OPTIONS)
                    .id("000000000002")
                    .attributes(
                        new AwsScanOptionsUpdateAttributes()
                            .vulnHostOs(true)
                            .vulnContainersOs(true)
                            .lambda(false)));

    try {
      apiInstance.updateAwsScanOptions("000000000002", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#updateAwsScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
"""
Update AWS scan options returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.aws_scan_options_type import AwsScanOptionsType
from datadog_api_client.v2.model.aws_scan_options_update_attributes import AwsScanOptionsUpdateAttributes
from datadog_api_client.v2.model.aws_scan_options_update_data import AwsScanOptionsUpdateData
from datadog_api_client.v2.model.aws_scan_options_update_request import AwsScanOptionsUpdateRequest

body = AwsScanOptionsUpdateRequest(
    data=AwsScanOptionsUpdateData(
        type=AwsScanOptionsType.AWS_SCAN_OPTIONS,
        id="000000000002",
        attributes=AwsScanOptionsUpdateAttributes(
            vuln_host_os=True,
            vuln_containers_os=True,
            _lambda=False,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    api_instance.update_aws_scan_options(account_id="000000000002", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update AWS scan options returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

body = DatadogAPIClient::V2::AwsScanOptionsUpdateRequest.new({
  data: DatadogAPIClient::V2::AwsScanOptionsUpdateData.new({
    type: DatadogAPIClient::V2::AwsScanOptionsType::AWS_SCAN_OPTIONS,
    id: "000000000002",
    attributes: DatadogAPIClient::V2::AwsScanOptionsUpdateAttributes.new({
      vuln_host_os: true,
      vuln_containers_os: true,
      lambda: false,
    }),
  }),
})
api_instance.update_aws_scan_options("000000000002", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update AWS scan options returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;
use datadog_api_client::datadogV2::model::AwsScanOptionsType;
use datadog_api_client::datadogV2::model::AwsScanOptionsUpdateAttributes;
use datadog_api_client::datadogV2::model::AwsScanOptionsUpdateData;
use datadog_api_client::datadogV2::model::AwsScanOptionsUpdateRequest;

#[tokio::main]
async fn main() {
    let body = AwsScanOptionsUpdateRequest::new(AwsScanOptionsUpdateData::new(
        AwsScanOptionsUpdateAttributes::new()
            .lambda(false)
            .vuln_containers_os(true)
            .vuln_host_os(true),
        "000000000002".to_string(),
        AwsScanOptionsType::AWS_SCAN_OPTIONS,
    ));
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api
        .update_aws_scan_options("000000000002".to_string(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Update AWS scan options returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiUpdateAwsScanOptionsRequest = {
  body: {
    data: {
      type: "aws_scan_options",
      id: "000000000002",
      attributes: {
        vulnHostOs: true,
        vulnContainersOs: true,
        lambda: false,
      },
    },
  },
  accountId: "000000000002",
};

apiInstance
  .updateAwsScanOptions(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete AWS scan options{% #delete-aws-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws/{account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws/{account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id} |

### Overview

Delete Agentless scan options for an AWS account.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description               |
| ---------------------------- | ------ | ------------------------- |
| account_id [*required*] | string | The ID of an AWS account. |

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport account_id="123456789012"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete AWS scan options returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    api_instance.delete_aws_scan_options(
        account_id="account_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete AWS scan options returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
api_instance.delete_aws_scan_options("account_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete AWS scan options returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    r, err := api.DeleteAwsScanOptions(ctx, "account_id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.DeleteAwsScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete AWS scan options returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      apiInstance.deleteAwsScanOptions("123456789012");
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#deleteAwsScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Delete AWS scan options returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.delete_aws_scan_options("account_id".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Delete AWS scan options returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiDeleteAwsScanOptionsRequest = {
  accountId: "account_id",
};

apiInstance
  .deleteAwsScanOptions(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List Azure scan options{% #list-azure-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure |

### Overview

Fetches the scan options configured for Azure accounts.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing a list of Azure scan options.

| Parent field | Field                  | Type     | Description                                                                                                          |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*] | [object] | A list of Azure scan options.                                                                                        |
| data         | attributes             | object   | Attributes for Azure scan options configuration.                                                                     |
| attributes   | vuln_containers_os     | boolean  | Indicates if scanning for vulnerabilities in containers is enabled.                                                  |
| attributes   | vuln_host_os           | boolean  | Indicates if scanning for vulnerabilities in hosts is enabled.                                                       |
| data         | id [*required*]   | string   | The Azure subscription ID.                                                                                           |
| data         | type [*required*] | enum     | The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "vuln_containers_os": true,
        "vuln_host_os": true
      },
      "id": "12345678-90ab-cdef-1234-567890abcdef",
      "type": "azure_scan_options"
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List Azure scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.list_azure_scan_options()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List Azure scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_azure_scan_options()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List Azure scan options returns "OK" response

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
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.ListAzureScanOptions(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.ListAzureScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.ListAzureScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List Azure scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AzureScanOptionsArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      AzureScanOptionsArray result = apiInstance.listAzureScanOptions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#listAzureScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List Azure scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.list_azure_scan_options().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List Azure scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

apiInstance
  .listAzureScanOptions()
  .then((data: v2.AzureScanOptionsArray) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create Azure scan options{% #create-azure-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure |

### Overview

Activate Agentless scan options for an Azure subscription.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type    | Description                                                                                                          |
| ------------ | ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
|              | data                   | object  | Single Azure scan options entry.                                                                                     |
| data         | attributes             | object  | Attributes for Azure scan options configuration.                                                                     |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                                  |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                       |
| data         | id [*required*]   | string  | The Azure subscription ID.                                                                                           |
| data         | type [*required*] | enum    | The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "type": "azure_scan_options"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response object containing Azure scan options for a single subscription.

| Parent field | Field                  | Type    | Description                                                                                                          |
| ------------ | ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
|              | data                   | object  | Single Azure scan options entry.                                                                                     |
| data         | attributes             | object  | Attributes for Azure scan options configuration.                                                                     |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                                  |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                       |
| data         | id [*required*]   | string  | The Azure subscription ID.                                                                                           |
| data         | type [*required*] | enum    | The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "type": "azure_scan_options"
  }
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "type": "azure_scan_options"
  }
}
EOF

#####

```go
// Create Azure scan options returns "Created" response

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
    body := datadogV2.AzureScanOptions{
        Data: &datadogV2.AzureScanOptionsData{
            Attributes: &datadogV2.AzureScanOptionsDataAttributes{
                VulnContainersOs: datadog.PtrBool(true),
                VulnHostOs:       datadog.PtrBool(true),
            },
            Id:   "12345678-90ab-cdef-1234-567890abcdef",
            Type: datadogV2.AZURESCANOPTIONSDATATYPE_AZURE_SCAN_OPTIONS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.CreateAzureScanOptions(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.CreateAzureScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.CreateAzureScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create Azure scan options returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AzureScanOptions;
import com.datadog.api.client.v2.model.AzureScanOptionsData;
import com.datadog.api.client.v2.model.AzureScanOptionsDataAttributes;
import com.datadog.api.client.v2.model.AzureScanOptionsDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    AzureScanOptions body =
        new AzureScanOptions()
            .data(
                new AzureScanOptionsData()
                    .attributes(
                        new AzureScanOptionsDataAttributes()
                            .vulnContainersOs(true)
                            .vulnHostOs(true))
                    .id("12345678-90ab-cdef-1234-567890abcdef")
                    .type(AzureScanOptionsDataType.AZURE_SCAN_OPTIONS));

    try {
      AzureScanOptions result = apiInstance.createAzureScanOptions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#createAzureScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
"""
Create Azure scan options returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.azure_scan_options import AzureScanOptions
from datadog_api_client.v2.model.azure_scan_options_data import AzureScanOptionsData
from datadog_api_client.v2.model.azure_scan_options_data_attributes import AzureScanOptionsDataAttributes
from datadog_api_client.v2.model.azure_scan_options_data_type import AzureScanOptionsDataType

body = AzureScanOptions(
    data=AzureScanOptionsData(
        attributes=AzureScanOptionsDataAttributes(
            vuln_containers_os=True,
            vuln_host_os=True,
        ),
        id="12345678-90ab-cdef-1234-567890abcdef",
        type=AzureScanOptionsDataType.AZURE_SCAN_OPTIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_azure_scan_options(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create Azure scan options returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

body = DatadogAPIClient::V2::AzureScanOptions.new({
  data: DatadogAPIClient::V2::AzureScanOptionsData.new({
    attributes: DatadogAPIClient::V2::AzureScanOptionsDataAttributes.new({
      vuln_containers_os: true,
      vuln_host_os: true,
    }),
    id: "12345678-90ab-cdef-1234-567890abcdef",
    type: DatadogAPIClient::V2::AzureScanOptionsDataType::AZURE_SCAN_OPTIONS,
  }),
})
p api_instance.create_azure_scan_options(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create Azure scan options returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;
use datadog_api_client::datadogV2::model::AzureScanOptions;
use datadog_api_client::datadogV2::model::AzureScanOptionsData;
use datadog_api_client::datadogV2::model::AzureScanOptionsDataAttributes;
use datadog_api_client::datadogV2::model::AzureScanOptionsDataType;

#[tokio::main]
async fn main() {
    let body = AzureScanOptions::new().data(
        AzureScanOptionsData::new(
            "12345678-90ab-cdef-1234-567890abcdef".to_string(),
            AzureScanOptionsDataType::AZURE_SCAN_OPTIONS,
        )
        .attributes(
            AzureScanOptionsDataAttributes::new()
                .vuln_containers_os(true)
                .vuln_host_os(true),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.create_azure_scan_options(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create Azure scan options returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiCreateAzureScanOptionsRequest = {
  body: {
    data: {
      attributes: {
        vulnContainersOs: true,
        vulnHostOs: true,
      },
      id: "12345678-90ab-cdef-1234-567890abcdef",
      type: "azure_scan_options",
    },
  },
};

apiInstance
  .createAzureScanOptions(params)
  .then((data: v2.AzureScanOptions) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get Azure scan options{% #get-azure-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure/{subscription_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |

### Overview

Fetches the Agentless scan options for an activated subscription.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                              | Type   | Description                |
| --------------------------------- | ------ | -------------------------- |
| subscription_id [*required*] | string | The Azure subscription ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing Azure scan options for a single subscription.

| Parent field | Field                  | Type    | Description                                                                                                          |
| ------------ | ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
|              | data                   | object  | Single Azure scan options entry.                                                                                     |
| data         | attributes             | object  | Attributes for Azure scan options configuration.                                                                     |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                                  |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                       |
| data         | id [*required*]   | string  | The Azure subscription ID.                                                                                           |
| data         | type [*required*] | enum    | The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "type": "azure_scan_options"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport subscription_id="12345678-90ab-cdef-1234-567890abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/${subscription_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get Azure scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.get_azure_scan_options(
        subscription_id="12345678-90ab-cdef-1234-567890abcdef",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get Azure scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.get_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get Azure scan options returns "OK" response

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
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.GetAzureScanOptions(ctx, "12345678-90ab-cdef-1234-567890abcdef")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.GetAzureScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.GetAzureScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get Azure scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AzureScanOptions;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      AzureScanOptions result =
          apiInstance.getAzureScanOptions("12345678-90ab-cdef-1234-567890abcdef");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#getAzureScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Get Azure scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api
        .get_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get Azure scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiGetAzureScanOptionsRequest = {
  subscriptionId: "12345678-90ab-cdef-1234-567890abcdef",
};

apiInstance
  .getAzureScanOptions(params)
  .then((data: v2.AzureScanOptions) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update Azure scan options{% #update-azure-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure/{subscription_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |

### Overview

Update the Agentless scan options for an activated subscription.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                              | Type   | Description                |
| --------------------------------- | ------ | -------------------------- |
| subscription_id [*required*] | string | The Azure subscription ID. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type    | Description                                                                 |
| ------------ | ---------------------- | ------- | --------------------------------------------------------------------------- |
|              | data                   | object  | Data object for updating the scan options of a single Azure subscription.   |
| data         | attributes             | object  | Attributes for updating Azure scan options configuration.                   |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.         |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.              |
| data         | id [*required*]   | string  | The Azure subscription ID.                                                  |
| data         | type [*required*] | enum    | Azure scan options resource type. Allowed enum values: `azure_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": false,
      "vuln_host_os": false
    },
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "type": "azure_scan_options"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing Azure scan options for a single subscription.

| Parent field | Field                  | Type    | Description                                                                                                          |
| ------------ | ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
|              | data                   | object  | Single Azure scan options entry.                                                                                     |
| data         | attributes             | object  | Attributes for Azure scan options configuration.                                                                     |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.                                                  |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.                                                       |
| data         | id [*required*]   | string  | The Azure subscription ID.                                                                                           |
| data         | type [*required*] | enum    | The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "type": "azure_scan_options"
  }
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
                  \# Path parametersexport subscription_id="12345678-90ab-cdef-1234-567890abcdef"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/${subscription_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "type": "azure_scan_options"
  }
}
EOF

#####

```python
"""
Update Azure scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.azure_scan_options_input_update import AzureScanOptionsInputUpdate
from datadog_api_client.v2.model.azure_scan_options_input_update_data import AzureScanOptionsInputUpdateData
from datadog_api_client.v2.model.azure_scan_options_input_update_data_type import AzureScanOptionsInputUpdateDataType

body = AzureScanOptionsInputUpdate(
    data=AzureScanOptionsInputUpdateData(
        id="12345678-90ab-cdef-1234-567890abcdef",
        type=AzureScanOptionsInputUpdateDataType.AZURE_SCAN_OPTIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.update_azure_scan_options(subscription_id="12345678-90ab-cdef-1234-567890abcdef", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update Azure scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

body = DatadogAPIClient::V2::AzureScanOptionsInputUpdate.new({
  data: DatadogAPIClient::V2::AzureScanOptionsInputUpdateData.new({
    id: "12345678-90ab-cdef-1234-567890abcdef",
    type: DatadogAPIClient::V2::AzureScanOptionsInputUpdateDataType::AZURE_SCAN_OPTIONS,
  }),
})
p api_instance.update_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Update Azure scan options returns "OK" response

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
    body := datadogV2.AzureScanOptionsInputUpdate{
        Data: &datadogV2.AzureScanOptionsInputUpdateData{
            Id:   "12345678-90ab-cdef-1234-567890abcdef",
            Type: datadogV2.AZURESCANOPTIONSINPUTUPDATEDATATYPE_AZURE_SCAN_OPTIONS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.UpdateAzureScanOptions(ctx, "12345678-90ab-cdef-1234-567890abcdef", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.UpdateAzureScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.UpdateAzureScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update Azure scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AzureScanOptions;
import com.datadog.api.client.v2.model.AzureScanOptionsInputUpdate;
import com.datadog.api.client.v2.model.AzureScanOptionsInputUpdateData;
import com.datadog.api.client.v2.model.AzureScanOptionsInputUpdateDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    AzureScanOptionsInputUpdate body =
        new AzureScanOptionsInputUpdate()
            .data(
                new AzureScanOptionsInputUpdateData()
                    .id("12345678-90ab-cdef-1234-567890abcdef")
                    .type(AzureScanOptionsInputUpdateDataType.AZURE_SCAN_OPTIONS));

    try {
      AzureScanOptions result =
          apiInstance.updateAzureScanOptions("12345678-90ab-cdef-1234-567890abcdef", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#updateAzureScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Update Azure scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;
use datadog_api_client::datadogV2::model::AzureScanOptionsInputUpdate;
use datadog_api_client::datadogV2::model::AzureScanOptionsInputUpdateData;
use datadog_api_client::datadogV2::model::AzureScanOptionsInputUpdateDataType;

#[tokio::main]
async fn main() {
    let body = AzureScanOptionsInputUpdate::new().data(AzureScanOptionsInputUpdateData::new(
        "12345678-90ab-cdef-1234-567890abcdef".to_string(),
        AzureScanOptionsInputUpdateDataType::AZURE_SCAN_OPTIONS,
    ));
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api
        .update_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef".to_string(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Update Azure scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiUpdateAzureScanOptionsRequest = {
  body: {
    data: {
      id: "12345678-90ab-cdef-1234-567890abcdef",
      type: "azure_scan_options",
    },
  },
  subscriptionId: "12345678-90ab-cdef-1234-567890abcdef",
};

apiInstance
  .updateAzureScanOptions(params)
  .then((data: v2.AzureScanOptions) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete Azure scan options{% #delete-azure-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure/{subscription_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id} |

### Overview

Delete Agentless scan options for an Azure subscription.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                              | Type   | Description                |
| --------------------------------- | ------ | -------------------------- |
| subscription_id [*required*] | string | The Azure subscription ID. |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport subscription_id="12345678-90ab-cdef-1234-567890abcdef"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/${subscription_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete Azure scan options returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    api_instance.delete_azure_scan_options(
        subscription_id="12345678-90ab-cdef-1234-567890abcdef",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete Azure scan options returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
api_instance.delete_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete Azure scan options returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    r, err := api.DeleteAzureScanOptions(ctx, "12345678-90ab-cdef-1234-567890abcdef")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.DeleteAzureScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete Azure scan options returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      apiInstance.deleteAzureScanOptions("12345678-90ab-cdef-1234-567890abcdef");
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#deleteAzureScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Delete Azure scan options returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api
        .delete_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Delete Azure scan options returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiDeleteAzureScanOptionsRequest = {
  subscriptionId: "12345678-90ab-cdef-1234-567890abcdef",
};

apiInstance
  .deleteAzureScanOptions(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List GCP scan options{% #list-gcp-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |

### Overview

Fetches the scan options configured for all GCP projects.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing a list of GCP scan options.

| Parent field | Field                  | Type     | Description                                                             |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------- |
|              | data [*required*] | [object] | A list of GCP scan options.                                             |
| data         | attributes             | object   | Attributes for GCP scan options configuration.                          |
| attributes   | vuln_containers_os     | boolean  | Indicates if scanning for vulnerabilities in containers is enabled.     |
| attributes   | vuln_host_os           | boolean  | Indicates if scanning for vulnerabilities in hosts is enabled.          |
| data         | id [*required*]   | string   | The GCP project ID.                                                     |
| data         | type [*required*] | enum     | GCP scan options resource type. Allowed enum values: `gcp_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "vuln_containers_os": true,
        "vuln_host_os": true
      },
      "id": "company-project-id",
      "type": "gcp_scan_options"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List GCP scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.list_gcp_scan_options()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List GCP scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_gcp_scan_options()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List GCP scan options returns "OK" response

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
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.ListGcpScanOptions(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.ListGcpScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.ListGcpScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List GCP scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.GcpScanOptionsArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      GcpScanOptionsArray result = apiInstance.listGcpScanOptions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#listGcpScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List GCP scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.list_gcp_scan_options().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List GCP scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

apiInstance
  .listGcpScanOptions()
  .then((data: v2.GcpScanOptionsArray) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create GCP scan options{% #create-gcp-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp |

### Overview

Activate Agentless scan options for a GCP project.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Request

#### Body Data (required)

The definition of the new scan options.

{% tab title="Model" %}

| Parent field | Field                  | Type    | Description                                                             |
| ------------ | ---------------------- | ------- | ----------------------------------------------------------------------- |
|              | data                   | object  | Single GCP scan options entry.                                          |
| data         | attributes             | object  | Attributes for GCP scan options configuration.                          |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.     |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.          |
| data         | id [*required*]   | string  | The GCP project ID.                                                     |
| data         | type [*required*] | enum    | GCP scan options resource type. Allowed enum values: `gcp_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "new-project",
    "type": "gcp_scan_options",
    "attributes": {
      "vuln_host_os": true,
      "vuln_containers_os": true
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Agentless scan options enabled successfully.
{% tab title="Model" %}
Response object containing GCP scan options for a single project.

| Parent field | Field                  | Type    | Description                                                             |
| ------------ | ---------------------- | ------- | ----------------------------------------------------------------------- |
|              | data                   | object  | Single GCP scan options entry.                                          |
| data         | attributes             | object  | Attributes for GCP scan options configuration.                          |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.     |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.          |
| data         | id [*required*]   | string  | The GCP project ID.                                                     |
| data         | type [*required*] | enum    | GCP scan options resource type. Allowed enum values: `gcp_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "company-project-id",
    "type": "gcp_scan_options"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="409" %}
Conflict
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "new-project",
    "type": "gcp_scan_options",
    "attributes": {
      "vuln_host_os": true,
      "vuln_containers_os": true
    }
  }
}
EOF

#####

```go
// Create GCP scan options returns "Agentless scan options enabled successfully." response

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
    body := datadogV2.GcpScanOptions{
        Data: &datadogV2.GcpScanOptionsData{
            Id:   "new-project",
            Type: datadogV2.GCPSCANOPTIONSDATATYPE_GCP_SCAN_OPTIONS,
            Attributes: &datadogV2.GcpScanOptionsDataAttributes{
                VulnHostOs:       datadog.PtrBool(true),
                VulnContainersOs: datadog.PtrBool(true),
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.CreateGcpScanOptions(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.CreateGcpScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.CreateGcpScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create GCP scan options returns "Agentless scan options enabled successfully." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.GcpScanOptions;
import com.datadog.api.client.v2.model.GcpScanOptionsData;
import com.datadog.api.client.v2.model.GcpScanOptionsDataAttributes;
import com.datadog.api.client.v2.model.GcpScanOptionsDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    GcpScanOptions body =
        new GcpScanOptions()
            .data(
                new GcpScanOptionsData()
                    .id("new-project")
                    .type(GcpScanOptionsDataType.GCP_SCAN_OPTIONS)
                    .attributes(
                        new GcpScanOptionsDataAttributes()
                            .vulnHostOs(true)
                            .vulnContainersOs(true)));

    try {
      GcpScanOptions result = apiInstance.createGcpScanOptions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#createGcpScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
"""
Create GCP scan options returns "Agentless scan options enabled successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.gcp_scan_options import GcpScanOptions
from datadog_api_client.v2.model.gcp_scan_options_data import GcpScanOptionsData
from datadog_api_client.v2.model.gcp_scan_options_data_attributes import GcpScanOptionsDataAttributes
from datadog_api_client.v2.model.gcp_scan_options_data_type import GcpScanOptionsDataType

body = GcpScanOptions(
    data=GcpScanOptionsData(
        id="new-project",
        type=GcpScanOptionsDataType.GCP_SCAN_OPTIONS,
        attributes=GcpScanOptionsDataAttributes(
            vuln_host_os=True,
            vuln_containers_os=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_gcp_scan_options(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create GCP scan options returns "Agentless scan options enabled successfully." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

body = DatadogAPIClient::V2::GcpScanOptions.new({
  data: DatadogAPIClient::V2::GcpScanOptionsData.new({
    id: "new-project",
    type: DatadogAPIClient::V2::GcpScanOptionsDataType::GCP_SCAN_OPTIONS,
    attributes: DatadogAPIClient::V2::GcpScanOptionsDataAttributes.new({
      vuln_host_os: true,
      vuln_containers_os: true,
    }),
  }),
})
p api_instance.create_gcp_scan_options(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create GCP scan options returns "Agentless scan options enabled successfully."
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;
use datadog_api_client::datadogV2::model::GcpScanOptions;
use datadog_api_client::datadogV2::model::GcpScanOptionsData;
use datadog_api_client::datadogV2::model::GcpScanOptionsDataAttributes;
use datadog_api_client::datadogV2::model::GcpScanOptionsDataType;

#[tokio::main]
async fn main() {
    let body = GcpScanOptions::new().data(
        GcpScanOptionsData::new(
            "new-project".to_string(),
            GcpScanOptionsDataType::GCP_SCAN_OPTIONS,
        )
        .attributes(
            GcpScanOptionsDataAttributes::new()
                .vuln_containers_os(true)
                .vuln_host_os(true),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.create_gcp_scan_options(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create GCP scan options returns "Agentless scan options enabled successfully." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiCreateGcpScanOptionsRequest = {
  body: {
    data: {
      id: "new-project",
      type: "gcp_scan_options",
      attributes: {
        vulnHostOs: true,
        vulnContainersOs: true,
      },
    },
  },
};

apiInstance
  .createGcpScanOptions(params)
  .then((data: v2.GcpScanOptions) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get GCP scan options{% #get-gcp-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp/{project_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp/{project_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |

### Overview

Fetches the Agentless scan options for an activated GCP project.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description         |
| ---------------------------- | ------ | ------------------- |
| project_id [*required*] | string | The GCP project ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing GCP scan options for a single project.

| Parent field | Field                  | Type    | Description                                                             |
| ------------ | ---------------------- | ------- | ----------------------------------------------------------------------- |
|              | data                   | object  | Single GCP scan options entry.                                          |
| data         | attributes             | object  | Attributes for GCP scan options configuration.                          |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.     |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.          |
| data         | id [*required*]   | string  | The GCP project ID.                                                     |
| data         | type [*required*] | enum    | GCP scan options resource type. Allowed enum values: `gcp_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "company-project-id",
    "type": "gcp_scan_options"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport project_id="company-project-id"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/${project_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get GCP scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.get_gcp_scan_options(
        project_id="api-spec-test",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get GCP scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.get_gcp_scan_options("api-spec-test")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get GCP scan options returns "OK" response

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
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.GetGcpScanOptions(ctx, "api-spec-test")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.GetGcpScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.GetGcpScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get GCP scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.GcpScanOptions;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      GcpScanOptions result = apiInstance.getGcpScanOptions("api-spec-test");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#getGcpScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Get GCP scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.get_gcp_scan_options("api-spec-test".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get GCP scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiGetGcpScanOptionsRequest = {
  projectId: "api-spec-test",
};

apiInstance
  .getGcpScanOptions(params)
  .then((data: v2.GcpScanOptions) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update GCP scan options{% #update-gcp-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp/{project_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp/{project_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |

### Overview

Update the Agentless scan options for an activated GCP project.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description         |
| ---------------------------- | ------ | ------------------- |
| project_id [*required*] | string | The GCP project ID. |

### Request

#### Body Data (required)

New definition of the scan options.

{% tab title="Model" %}

| Parent field | Field                  | Type    | Description                                                             |
| ------------ | ---------------------- | ------- | ----------------------------------------------------------------------- |
|              | data                   | object  | Data object for updating the scan options of a single GCP project.      |
| data         | attributes             | object  | Attributes for updating GCP scan options configuration.                 |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.     |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.          |
| data         | id [*required*]   | string  | The GCP project ID.                                                     |
| data         | type [*required*] | enum    | GCP scan options resource type. Allowed enum values: `gcp_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "api-spec-test",
    "type": "gcp_scan_options",
    "attributes": {
      "vuln_containers_os": false
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing GCP scan options for a single project.

| Parent field | Field                  | Type    | Description                                                             |
| ------------ | ---------------------- | ------- | ----------------------------------------------------------------------- |
|              | data                   | object  | Single GCP scan options entry.                                          |
| data         | attributes             | object  | Attributes for GCP scan options configuration.                          |
| attributes   | vuln_containers_os     | boolean | Indicates if scanning for vulnerabilities in containers is enabled.     |
| attributes   | vuln_host_os           | boolean | Indicates if scanning for vulnerabilities in hosts is enabled.          |
| data         | id [*required*]   | string  | The GCP project ID.                                                     |
| data         | type [*required*] | enum    | GCP scan options resource type. Allowed enum values: `gcp_scan_options` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "vuln_containers_os": true,
      "vuln_host_os": true
    },
    "id": "company-project-id",
    "type": "gcp_scan_options"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                          \# Path parametersexport project_id="company-project-id"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/${project_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "api-spec-test",
    "type": "gcp_scan_options",
    "attributes": {
      "vuln_containers_os": false
    }
  }
}
EOF

#####

```go
// Update GCP scan options returns "OK" response

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
    body := datadogV2.GcpScanOptionsInputUpdate{
        Data: &datadogV2.GcpScanOptionsInputUpdateData{
            Id:   "api-spec-test",
            Type: datadogV2.GCPSCANOPTIONSINPUTUPDATEDATATYPE_GCP_SCAN_OPTIONS,
            Attributes: &datadogV2.GcpScanOptionsInputUpdateDataAttributes{
                VulnContainersOs: datadog.PtrBool(false),
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.UpdateGcpScanOptions(ctx, "api-spec-test", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.UpdateGcpScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.UpdateGcpScanOptions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update GCP scan options returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.GcpScanOptions;
import com.datadog.api.client.v2.model.GcpScanOptionsInputUpdate;
import com.datadog.api.client.v2.model.GcpScanOptionsInputUpdateData;
import com.datadog.api.client.v2.model.GcpScanOptionsInputUpdateDataAttributes;
import com.datadog.api.client.v2.model.GcpScanOptionsInputUpdateDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    GcpScanOptionsInputUpdate body =
        new GcpScanOptionsInputUpdate()
            .data(
                new GcpScanOptionsInputUpdateData()
                    .id("api-spec-test")
                    .type(GcpScanOptionsInputUpdateDataType.GCP_SCAN_OPTIONS)
                    .attributes(
                        new GcpScanOptionsInputUpdateDataAttributes().vulnContainersOs(false)));

    try {
      GcpScanOptions result = apiInstance.updateGcpScanOptions("api-spec-test", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#updateGcpScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
"""
Update GCP scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.gcp_scan_options_input_update import GcpScanOptionsInputUpdate
from datadog_api_client.v2.model.gcp_scan_options_input_update_data import GcpScanOptionsInputUpdateData
from datadog_api_client.v2.model.gcp_scan_options_input_update_data_attributes import (
    GcpScanOptionsInputUpdateDataAttributes,
)
from datadog_api_client.v2.model.gcp_scan_options_input_update_data_type import GcpScanOptionsInputUpdateDataType

body = GcpScanOptionsInputUpdate(
    data=GcpScanOptionsInputUpdateData(
        id="api-spec-test",
        type=GcpScanOptionsInputUpdateDataType.GCP_SCAN_OPTIONS,
        attributes=GcpScanOptionsInputUpdateDataAttributes(
            vuln_containers_os=False,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.update_gcp_scan_options(project_id="api-spec-test", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update GCP scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

body = DatadogAPIClient::V2::GcpScanOptionsInputUpdate.new({
  data: DatadogAPIClient::V2::GcpScanOptionsInputUpdateData.new({
    id: "api-spec-test",
    type: DatadogAPIClient::V2::GcpScanOptionsInputUpdateDataType::GCP_SCAN_OPTIONS,
    attributes: DatadogAPIClient::V2::GcpScanOptionsInputUpdateDataAttributes.new({
      vuln_containers_os: false,
    }),
  }),
})
p api_instance.update_gcp_scan_options("api-spec-test", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update GCP scan options returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;
use datadog_api_client::datadogV2::model::GcpScanOptionsInputUpdate;
use datadog_api_client::datadogV2::model::GcpScanOptionsInputUpdateData;
use datadog_api_client::datadogV2::model::GcpScanOptionsInputUpdateDataAttributes;
use datadog_api_client::datadogV2::model::GcpScanOptionsInputUpdateDataType;

#[tokio::main]
async fn main() {
    let body = GcpScanOptionsInputUpdate::new().data(
        GcpScanOptionsInputUpdateData::new(
            "api-spec-test".to_string(),
            GcpScanOptionsInputUpdateDataType::GCP_SCAN_OPTIONS,
        )
        .attributes(GcpScanOptionsInputUpdateDataAttributes::new().vuln_containers_os(false)),
    );
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api
        .update_gcp_scan_options("api-spec-test".to_string(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Update GCP scan options returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiUpdateGcpScanOptionsRequest = {
  body: {
    data: {
      id: "api-spec-test",
      type: "gcp_scan_options",
      attributes: {
        vulnContainersOs: false,
      },
    },
  },
  projectId: "api-spec-test",
};

apiInstance
  .updateGcpScanOptions(params)
  .then((data: v2.GcpScanOptions) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete GCP scan options{% #delete-gcp-scan-options %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp/{project_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp/{project_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id} |

### Overview

Delete Agentless scan options for a GCP project.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description         |
| ---------------------------- | ------ | ------------------- |
| project_id [*required*] | string | The GCP project ID. |

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport project_id="company-project-id"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/${project_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete GCP scan options returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    api_instance.delete_gcp_scan_options(
        project_id="company-project-id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete GCP scan options returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
api_instance.delete_gcp_scan_options("company-project-id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete GCP scan options returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    r, err := api.DeleteGcpScanOptions(ctx, "company-project-id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.DeleteGcpScanOptions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete GCP scan options returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      apiInstance.deleteGcpScanOptions("company-project-id");
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#deleteGcpScanOptions");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Delete GCP scan options returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api
        .delete_gcp_scan_options("company-project-id".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Delete GCP scan options returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiDeleteGcpScanOptionsRequest = {
  projectId: "company-project-id",
};

apiInstance
  .deleteGcpScanOptions(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List AWS on demand tasks{% #list-aws-on-demand-tasks %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/ondemand/aws      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/ondemand/aws      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/ondemand/aws     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |

### Overview

Fetches the most recent 1000 AWS on demand tasks. This endpoint requires the `security_monitoring_findings_read` permission.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of AWS on demand tasks.

| Parent field | Field       | Type     | Description                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data        | [object] | A list of on demand tasks.                                                                                                                                                                                                                                                                                                                                          |
| data         | attributes  | object   | Attributes for the AWS on demand task.                                                                                                                                                                                                                                                                                                                              |
| attributes   | arn         | string   | The arn of the resource to scan.                                                                                                                                                                                                                                                                                                                                    |
| attributes   | assigned_at | string   | Specifies the assignment timestamp if the task has been already assigned to a scanner.                                                                                                                                                                                                                                                                              |
| attributes   | created_at  | string   | The task submission timestamp.                                                                                                                                                                                                                                                                                                                                      |
| attributes   | status      | string   | Indicates the status of the task. QUEUED: the task has been submitted successfully and the resource has not been assigned to a scanner yet. ASSIGNED: the task has been assigned. ABORTED: the scan has been aborted after a period of time due to technical reasons, such as resource not found, insufficient permissions, or the absence of a configured scanner. |
| data         | id          | string   | The UUID of the task.                                                                                                                                                                                                                                                                                                                                               |
| data         | type        | enum     | The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "arn": "arn:aws:ec2:us-east-1:727000456123:instance/i-0eabb50529b67a1ba",
        "assigned_at": "2025-02-11T18:25:04.550564Z",
        "created_at": "2025-02-11T18:13:24.576915Z",
        "status": "QUEUED"
      },
      "id": "6d09294c-9ad9-42fd-a759-a0c1599b4828",
      "type": "aws_resource"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List AWS on demand tasks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.list_aws_on_demand_tasks()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List AWS on demand tasks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_aws_on_demand_tasks()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List AWS on demand tasks returns "OK" response

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
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.ListAwsOnDemandTasks(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.ListAwsOnDemandTasks`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.ListAwsOnDemandTasks`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List AWS on demand tasks returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AwsOnDemandListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      AwsOnDemandListResponse result = apiInstance.listAwsOnDemandTasks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#listAwsOnDemandTasks");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List AWS on demand tasks returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.list_aws_on_demand_tasks().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List AWS on demand tasks returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

apiInstance
  .listAwsOnDemandTasks()
  .then((data: v2.AwsOnDemandListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create AWS on demand task{% #create-aws-on-demand-task %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/agentless_scanning/ondemand/aws      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/agentless_scanning/ondemand/aws      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/agentless_scanning/ondemand/aws     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws |

### Overview

Trigger the scan of an AWS resource with a high priority. Agentless scanning must be activated for the AWS account containing the resource to scan. This endpoint requires the `security_monitoring_findings_write` permission.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Request

#### Body Data (required)

The definition of the on demand task.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                    |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]       | object | Object for a single AWS on demand task.                                                                                        |
| data         | attributes [*required*] | object | Attributes for the AWS on demand task.                                                                                         |
| attributes   | arn [*required*]        | string | The arn of the resource to scan. Agentless supports the scan of EC2 instances, lambda functions, AMI, ECR, RDS and S3 buckets. |
| data         | type [*required*]       | enum   | The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "arn": "arn:aws:lambda:us-west-2:123456789012:function:my-function"
    },
    "type": "aws_resource"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
AWS on demand task created successfully.
{% tab title="Model" %}
Response object that includes an AWS on demand task.

| Parent field | Field       | Type   | Description                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data        | object | Single AWS on demand task.                                                                                                                                                                                                                                                                                                                                          |
| data         | attributes  | object | Attributes for the AWS on demand task.                                                                                                                                                                                                                                                                                                                              |
| attributes   | arn         | string | The arn of the resource to scan.                                                                                                                                                                                                                                                                                                                                    |
| attributes   | assigned_at | string | Specifies the assignment timestamp if the task has been already assigned to a scanner.                                                                                                                                                                                                                                                                              |
| attributes   | created_at  | string | The task submission timestamp.                                                                                                                                                                                                                                                                                                                                      |
| attributes   | status      | string | Indicates the status of the task. QUEUED: the task has been submitted successfully and the resource has not been assigned to a scanner yet. ASSIGNED: the task has been assigned. ABORTED: the scan has been aborted after a period of time due to technical reasons, such as resource not found, insufficient permissions, or the absence of a configured scanner. |
| data         | id          | string | The UUID of the task.                                                                                                                                                                                                                                                                                                                                               |
| data         | type        | enum   | The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "arn": "arn:aws:ec2:us-east-1:727000456123:instance/i-0eabb50529b67a1ba",
      "assigned_at": "2025-02-11T18:25:04.550564Z",
      "created_at": "2025-02-11T18:13:24.576915Z",
      "status": "QUEUED"
    },
    "id": "6d09294c-9ad9-42fd-a759-a0c1599b4828",
    "type": "aws_resource"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "arn": "arn:aws:lambda:us-west-2:123456789012:function:my-function"
    },
    "type": "aws_resource"
  }
}
EOF

#####

```go
// Create AWS on demand task returns "AWS on demand task created successfully." response

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
    body := datadogV2.AwsOnDemandCreateRequest{
        Data: datadogV2.AwsOnDemandCreateData{
            Attributes: datadogV2.AwsOnDemandCreateAttributes{
                Arn: "arn:aws:lambda:us-west-2:123456789012:function:my-function",
            },
            Type: datadogV2.AWSONDEMANDTYPE_AWS_RESOURCE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.CreateAwsOnDemandTask(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.CreateAwsOnDemandTask`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.CreateAwsOnDemandTask`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create AWS on demand task returns "AWS on demand task created successfully." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AwsOnDemandCreateAttributes;
import com.datadog.api.client.v2.model.AwsOnDemandCreateData;
import com.datadog.api.client.v2.model.AwsOnDemandCreateRequest;
import com.datadog.api.client.v2.model.AwsOnDemandResponse;
import com.datadog.api.client.v2.model.AwsOnDemandType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    AwsOnDemandCreateRequest body =
        new AwsOnDemandCreateRequest()
            .data(
                new AwsOnDemandCreateData()
                    .attributes(
                        new AwsOnDemandCreateAttributes()
                            .arn("arn:aws:lambda:us-west-2:123456789012:function:my-function"))
                    .type(AwsOnDemandType.AWS_RESOURCE));

    try {
      AwsOnDemandResponse result = apiInstance.createAwsOnDemandTask(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#createAwsOnDemandTask");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
"""
Create AWS on demand task returns "AWS on demand task created successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.aws_on_demand_create_attributes import AwsOnDemandCreateAttributes
from datadog_api_client.v2.model.aws_on_demand_create_data import AwsOnDemandCreateData
from datadog_api_client.v2.model.aws_on_demand_create_request import AwsOnDemandCreateRequest
from datadog_api_client.v2.model.aws_on_demand_type import AwsOnDemandType

body = AwsOnDemandCreateRequest(
    data=AwsOnDemandCreateData(
        attributes=AwsOnDemandCreateAttributes(
            arn="arn:aws:lambda:us-west-2:123456789012:function:my-function",
        ),
        type=AwsOnDemandType.AWS_RESOURCE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_aws_on_demand_task(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create AWS on demand task returns "AWS on demand task created successfully." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

body = DatadogAPIClient::V2::AwsOnDemandCreateRequest.new({
  data: DatadogAPIClient::V2::AwsOnDemandCreateData.new({
    attributes: DatadogAPIClient::V2::AwsOnDemandCreateAttributes.new({
      arn: "arn:aws:lambda:us-west-2:123456789012:function:my-function",
    }),
    type: DatadogAPIClient::V2::AwsOnDemandType::AWS_RESOURCE,
  }),
})
p api_instance.create_aws_on_demand_task(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create AWS on demand task returns "AWS on demand task created successfully."
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;
use datadog_api_client::datadogV2::model::AwsOnDemandCreateAttributes;
use datadog_api_client::datadogV2::model::AwsOnDemandCreateData;
use datadog_api_client::datadogV2::model::AwsOnDemandCreateRequest;
use datadog_api_client::datadogV2::model::AwsOnDemandType;

#[tokio::main]
async fn main() {
    let body = AwsOnDemandCreateRequest::new(AwsOnDemandCreateData::new(
        AwsOnDemandCreateAttributes::new(
            "arn:aws:lambda:us-west-2:123456789012:function:my-function".to_string(),
        ),
        AwsOnDemandType::AWS_RESOURCE,
    ));
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api.create_aws_on_demand_task(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create AWS on demand task returns "AWS on demand task created successfully." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiCreateAwsOnDemandTaskRequest = {
  body: {
    data: {
      attributes: {
        arn: "arn:aws:lambda:us-west-2:123456789012:function:my-function",
      },
      type: "aws_resource",
    },
  },
};

apiInstance
  .createAwsOnDemandTask(params)
  .then((data: v2.AwsOnDemandResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get AWS on demand task{% #get-aws-on-demand-task %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/agentless_scanning/ondemand/aws/{task_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/agentless_scanning/ondemand/aws/{task_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id} |

### Overview

Fetch the data of a specific on demand task. This endpoint requires the `security_monitoring_findings_read` permission.

OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description           |
| ------------------------- | ------ | --------------------- |
| task_id [*required*] | string | The UUID of the task. |

### Response

{% tab title="200" %}
OK.
{% tab title="Model" %}
Response object that includes an AWS on demand task.

| Parent field | Field       | Type   | Description                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data        | object | Single AWS on demand task.                                                                                                                                                                                                                                                                                                                                          |
| data         | attributes  | object | Attributes for the AWS on demand task.                                                                                                                                                                                                                                                                                                                              |
| attributes   | arn         | string | The arn of the resource to scan.                                                                                                                                                                                                                                                                                                                                    |
| attributes   | assigned_at | string | Specifies the assignment timestamp if the task has been already assigned to a scanner.                                                                                                                                                                                                                                                                              |
| attributes   | created_at  | string | The task submission timestamp.                                                                                                                                                                                                                                                                                                                                      |
| attributes   | status      | string | Indicates the status of the task. QUEUED: the task has been submitted successfully and the resource has not been assigned to a scanner yet. ASSIGNED: the task has been assigned. ABORTED: the scan has been aborted after a period of time due to technical reasons, such as resource not found, insufficient permissions, or the absence of a configured scanner. |
| data         | id          | string | The UUID of the task.                                                                                                                                                                                                                                                                                                                                               |
| data         | type        | enum   | The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "arn": "arn:aws:ec2:us-east-1:727000456123:instance/i-0eabb50529b67a1ba",
      "assigned_at": "2025-02-11T18:25:04.550564Z",
      "created_at": "2025-02-11T18:13:24.576915Z",
      "status": "QUEUED"
    },
    "id": "6d09294c-9ad9-42fd-a759-a0c1599b4828",
    "type": "aws_resource"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport task_id="6d09294c-9ad9-42fd-a759-a0c1599b4828"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/${task_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get AWS on demand task returns "OK." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.get_aws_on_demand_task(
        task_id="63d6b4f5-e5d0-4d90-824a-9580f05f026a",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get AWS on demand task returns "OK." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.get_aws_on_demand_task("63d6b4f5-e5d0-4d90-824a-9580f05f026a")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get AWS on demand task returns "OK." response

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
    api := datadogV2.NewAgentlessScanningApi(apiClient)
    resp, r, err := api.GetAwsOnDemandTask(ctx, "63d6b4f5-e5d0-4d90-824a-9580f05f026a")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AgentlessScanningApi.GetAwsOnDemandTask`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `AgentlessScanningApi.GetAwsOnDemandTask`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get AWS on demand task returns "OK." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AgentlessScanningApi;
import com.datadog.api.client.v2.model.AwsOnDemandResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AgentlessScanningApi apiInstance = new AgentlessScanningApi(defaultClient);

    try {
      AwsOnDemandResponse result =
          apiInstance.getAwsOnDemandTask("63d6b4f5-e5d0-4d90-824a-9580f05f026a");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentlessScanningApi#getAwsOnDemandTask");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Get AWS on demand task returns "OK." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_agentless_scanning::AgentlessScanningAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AgentlessScanningAPI::with_config(configuration);
    let resp = api
        .get_aws_on_demand_task("63d6b4f5-e5d0-4d90-824a-9580f05f026a".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get AWS on demand task returns "OK." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AgentlessScanningApi(configuration);

const params: v2.AgentlessScanningApiGetAwsOnDemandTaskRequest = {
  taskId: "63d6b4f5-e5d0-4d90-824a-9580f05f026a",
};

apiInstance
  .getAwsOnDemandTask(params)
  .then((data: v2.AwsOnDemandResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
