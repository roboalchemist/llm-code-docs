# Source: https://docs.datadoghq.com/api/latest/agentless-scanning

# Agentless Scanning
Datadog Agentless Scanning provides visibility into risks and vulnerabilities within your hosts, running containers, and serverless functions—all without requiring teams to install Agents on every host or where Agents cannot be installed. Agentless offers also Sensitive Data Scanning capabilities on your storage. Go to <https://www.datadoghq.com/blog/agentless-scanning/> to learn more.
## [List AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-scan-options-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.datadoghq.eu/api/v2/agentless_scanning/accounts/awshttps://api.ddog-gov.com/api/v2/agentless_scanning/accounts/awshttps://api.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws
### Overview
Fetches the scan options configured for AWS accounts.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAwsScanOptions-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAwsScanOptions-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAwsScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object that includes a list of AWS scan options.
Field
Type
Description
data
[object]
A list of AWS scan options.
attributes
object
Attributes for the AWS scan options.
lambda
boolean
Indicates if scanning of Lambda functions is enabled.
sensitive_data
boolean
Indicates if scanning for sensitive data is enabled.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id
string
The ID of the AWS account.
type
enum
The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options`
default: `aws_scan_options`
```
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

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  List AWS scan options
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List AWS scan options
```
# List AWS scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_aws_scan_options()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-scan-options-v2)


POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.datadoghq.eu/api/v2/agentless_scanning/accounts/awshttps://api.ddog-gov.com/api/v2/agentless_scanning/accounts/awshttps://api.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/awshttps://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws
### Overview
Activate Agentless scan options for an AWS account.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Request
#### Body Data (required)
The definition of the new scan options.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Field
Type
Description
data [_required_]
object
Object for the scan options of a single AWS account.
attributes [_required_]
object
Attributes for the AWS scan options to create.
lambda [_required_]
boolean
Indicates if scanning of Lambda functions is enabled.
sensitive_data [_required_]
boolean
Indicates if scanning for sensitive data is enabled.
vuln_containers_os [_required_]
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os [_required_]
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The ID of the AWS account.
type [_required_]
enum
The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options`
default: `aws_scan_options`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsScanOptions-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsScanOptions-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsScanOptions-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsScanOptions-429-v2)


Agentless scan options enabled successfully.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object that includes the scan options of an AWS account.
Field
Type
Description
data
object
Single AWS Scan Options entry.
attributes
object
Attributes for the AWS scan options.
lambda
boolean
Indicates if scanning of Lambda functions is enabled.
sensitive_data
boolean
Indicates if scanning for sensitive data is enabled.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id
string
The ID of the AWS account.
type
enum
The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options`
default: `aws_scan_options`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Create AWS scan options
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws" \
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

                
```

#####  Create AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-scan-options-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}
### Overview
Fetches the Agentless scan options for an activated account.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
The ID of an AWS account.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsScanOptions-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsScanOptions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsScanOptions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object that includes the scan options of an AWS account.
Field
Type
Description
data
object
Single AWS Scan Options entry.
attributes
object
Attributes for the AWS scan options.
lambda
boolean
Indicates if scanning of Lambda functions is enabled.
sensitive_data
boolean
Indicates if scanning for sensitive data is enabled.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id
string
The ID of the AWS account.
type
enum
The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options`
default: `aws_scan_options`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Get AWS scan options
Copy
```
                  # Path parameters  
export account_id="123456789012"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get AWS scan options
```
# Get AWS scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new

# there is a valid "aws_scan_options" in the system
AWS_SCAN_OPTIONS_ID = ENV["AWS_SCAN_OPTIONS_ID"]
p api_instance.get_aws_scan_options(AWS_SCAN_OPTIONS_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-aws-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-aws-scan-options-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}
### Overview
Update the Agentless scan options for an activated account.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
The ID of an AWS account.
### Request
#### Body Data (required)
New definition of the scan options.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Field
Type
Description
data [_required_]
object
Object for the scan options of a single AWS account.
attributes [_required_]
object
Attributes for the AWS scan options to update.
lambda
boolean
Indicates if scanning of Lambda functions is enabled.
sensitive_data
boolean
Indicates if scanning for sensitive data is enabled.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The ID of the AWS account.
type [_required_]
enum
The type of the resource. The value should always be `aws_scan_options`. Allowed enum values: `aws_scan_options`
default: `aws_scan_options`
```
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

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateAwsScanOptions-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateAwsScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateAwsScanOptions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateAwsScanOptions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateAwsScanOptions-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Update AWS scan options returns "No Content" response
Copy
```
                          # Path parameters  
export account_id="123456789012"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/${account_id}" \
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

                        
```

#####  Update AWS scan options returns "No Content" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update AWS scan options returns "No Content" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update AWS scan options returns "No Content" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update AWS scan options returns "No Content" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update AWS scan options returns "No Content" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update AWS scan options returns "No Content" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-aws-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-aws-scan-options-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/{account_id}
### Overview
Delete Agentless scan options for an AWS account.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
The ID of an AWS account.
### Response
  * [204](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteAwsScanOptions-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteAwsScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteAwsScanOptions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteAwsScanOptions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteAwsScanOptions-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Delete AWS scan options
Copy
```
                  # Path parameters  
export account_id="123456789012"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/aws/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete AWS scan options
```
# Delete AWS scan options returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
api_instance.delete_aws_scan_options("account_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete AWS scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-azure-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-azure-scan-options-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azurehttps://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azurehttps://api.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure
### Overview
Fetches the scan options configured for Azure accounts.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAzureScanOptions-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAzureScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing a list of Azure scan options.
Field
Type
Description
data [_required_]
[object]
A list of Azure scan options.
attributes
object
Attributes for Azure scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The Azure subscription ID.
type [_required_]
enum
The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options`
default: `azure_scan_options`
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  List Azure scan options
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List Azure scan options
```
# List Azure scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_azure_scan_options()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-azure-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-azure-scan-options-v2)


POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azurehttps://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azurehttps://api.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azurehttps://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure
### Overview
Activate Agentless scan options for an Azure subscription.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Field
Type
Description
data
object
Single Azure scan options entry.
attributes
object
Attributes for Azure scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The Azure subscription ID.
type [_required_]
enum
The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options`
default: `azure_scan_options`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAzureScanOptions-201-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAzureScanOptions-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing Azure scan options for a single subscription.
Field
Type
Description
data
object
Single Azure scan options entry.
attributes
object
Attributes for Azure scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The Azure subscription ID.
type [_required_]
enum
The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options`
default: `azure_scan_options`
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Create Azure scan options returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure" \
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

                        
```

#####  Create Azure scan options returns "Created" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create Azure scan options returns "Created" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create Azure scan options returns "Created" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create Azure scan options returns "Created" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create Azure scan options returns "Created" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create Azure scan options returns "Created" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-azure-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-azure-scan-options-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}
### Overview
Fetches the Agentless scan options for an activated subscription.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
subscription_id [_required_]
string
The Azure subscription ID.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAzureScanOptions-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAzureScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAzureScanOptions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAzureScanOptions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAzureScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing Azure scan options for a single subscription.
Field
Type
Description
data
object
Single Azure scan options entry.
attributes
object
Attributes for Azure scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The Azure subscription ID.
type [_required_]
enum
The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options`
default: `azure_scan_options`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Get Azure scan options
Copy
```
                  # Path parameters  
export subscription_id="12345678-90ab-cdef-1234-567890abcdef"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/${subscription_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get Azure scan options
```
# Get Azure scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.get_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-azure-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-azure-scan-options-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}
### Overview
Update the Agentless scan options for an activated subscription.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
subscription_id [_required_]
string
The Azure subscription ID.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Field
Type
Description
data
object
Data object for updating the scan options of a single Azure subscription.
attributes
object
Attributes for updating Azure scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The Azure subscription ID.
type [_required_]
enum
Azure scan options resource type. Allowed enum values: `azure_scan_options`
default: `azure_scan_options`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateAzureScanOptions-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateAzureScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing Azure scan options for a single subscription.
Field
Type
Description
data
object
Single Azure scan options entry.
attributes
object
Attributes for Azure scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The Azure subscription ID.
type [_required_]
enum
The type of the resource. The value should always be `azure_scan_options`. Allowed enum values: `azure_scan_options`
default: `azure_scan_options`
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Update Azure scan options
Copy
```
                  # Path parameters  
export subscription_id="12345678-90ab-cdef-1234-567890abcdef"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/${subscription_id}" \
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

                
```

#####  Update Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-azure-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-azure-scan-options-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/{subscription_id}
### Overview
Delete Agentless scan options for an Azure subscription.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
subscription_id [_required_]
string
The Azure subscription ID.
### Response
  * [204](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteAzureScanOptions-204-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteAzureScanOptions-429-v2)


No Content
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Delete Azure scan options
Copy
```
                  # Path parameters  
export subscription_id="12345678-90ab-cdef-1234-567890abcdef"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/azure/${subscription_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete Azure scan options
```
# Delete Azure scan options returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
api_instance.delete_azure_scan_options("12345678-90ab-cdef-1234-567890abcdef")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete Azure scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-gcp-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-gcp-scan-options-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcphttps://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcphttps://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp
### Overview
Fetches the scan options configured for all GCP projects.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListGcpScanOptions-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListGcpScanOptions-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListGcpScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing a list of GCP scan options.
Field
Type
Description
data [_required_]
[object]
A list of GCP scan options.
attributes
object
Attributes for GCP scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The GCP project ID.
type [_required_]
enum
GCP scan options resource type. Allowed enum values: `gcp_scan_options`
default: `gcp_scan_options`
```
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

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  List GCP scan options
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List GCP scan options
```
# List GCP scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_gcp_scan_options()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-gcp-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-gcp-scan-options-v2)


POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcphttps://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcphttps://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcphttps://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp
### Overview
Activate Agentless scan options for a GCP project.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Request
#### Body Data (required)
The definition of the new scan options.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Field
Type
Description
data
object
Single GCP scan options entry.
attributes
object
Attributes for GCP scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The GCP project ID.
type [_required_]
enum
GCP scan options resource type. Allowed enum values: `gcp_scan_options`
default: `gcp_scan_options`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateGcpScanOptions-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateGcpScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateGcpScanOptions-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateGcpScanOptions-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateGcpScanOptions-429-v2)


Agentless scan options enabled successfully.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing GCP scan options for a single project.
Field
Type
Description
data
object
Single GCP scan options entry.
attributes
object
Attributes for GCP scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The GCP project ID.
type [_required_]
enum
GCP scan options resource type. Allowed enum values: `gcp_scan_options`
default: `gcp_scan_options`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Create GCP scan options returns "Agentless scan options enabled successfully." response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp" \
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

                        
```

#####  Create GCP scan options returns "Agentless scan options enabled successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create GCP scan options returns "Agentless scan options enabled successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create GCP scan options returns "Agentless scan options enabled successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create GCP scan options returns "Agentless scan options enabled successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create GCP scan options returns "Agentless scan options enabled successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create GCP scan options returns "Agentless scan options enabled successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-gcp-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-gcp-scan-options-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}
### Overview
Fetches the Agentless scan options for an activated GCP project.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
project_id [_required_]
string
The GCP project ID.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetGcpScanOptions-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetGcpScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetGcpScanOptions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetGcpScanOptions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetGcpScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing GCP scan options for a single project.
Field
Type
Description
data
object
Single GCP scan options entry.
attributes
object
Attributes for GCP scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The GCP project ID.
type [_required_]
enum
GCP scan options resource type. Allowed enum values: `gcp_scan_options`
default: `gcp_scan_options`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Get GCP scan options
Copy
```
                  # Path parameters  
export project_id="company-project-id"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/${project_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get GCP scan options
```
# Get GCP scan options returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.get_gcp_scan_options("api-spec-test")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-gcp-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-gcp-scan-options-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}
### Overview
Update the Agentless scan options for an activated GCP project.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
project_id [_required_]
string
The GCP project ID.
### Request
#### Body Data (required)
New definition of the scan options.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Field
Type
Description
data
object
Data object for updating the scan options of a single GCP project.
attributes
object
Attributes for updating GCP scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The GCP project ID.
type [_required_]
enum
GCP scan options resource type. Allowed enum values: `gcp_scan_options`
default: `gcp_scan_options`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateGcpScanOptions-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateGcpScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateGcpScanOptions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateGcpScanOptions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#UpdateGcpScanOptions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object containing GCP scan options for a single project.
Field
Type
Description
data
object
Single GCP scan options entry.
attributes
object
Attributes for GCP scan options configuration.
vuln_containers_os
boolean
Indicates if scanning for vulnerabilities in containers is enabled.
vuln_host_os
boolean
Indicates if scanning for vulnerabilities in hosts is enabled.
id [_required_]
string
The GCP project ID.
type [_required_]
enum
GCP scan options resource type. Allowed enum values: `gcp_scan_options`
default: `gcp_scan_options`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Update GCP scan options returns "OK" response
Copy
```
                          # Path parameters  
export project_id="company-project-id"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/${project_id}" \
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

                        
```

#####  Update GCP scan options returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update GCP scan options returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update GCP scan options returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update GCP scan options returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update GCP scan options returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update GCP scan options returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-gcp-scan-options)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-gcp-scan-options-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.datadoghq.eu/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.ddog-gov.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/{project_id}
### Overview
Delete Agentless scan options for a GCP project.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
project_id [_required_]
string
The GCP project ID.
### Response
  * [204](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteGcpScanOptions-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteGcpScanOptions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteGcpScanOptions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteGcpScanOptions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#DeleteGcpScanOptions-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Delete GCP scan options
Copy
```
                  # Path parameters  
export project_id="company-project-id"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/accounts/gcp/${project_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete GCP scan options
```
# Delete GCP scan options returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
api_instance.delete_gcp_scan_options("company-project-id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete GCP scan options
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List AWS on demand tasks](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-on-demand-tasks)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-on-demand-tasks-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.datadoghq.eu/api/v2/agentless_scanning/ondemand/awshttps://api.ddog-gov.com/api/v2/agentless_scanning/ondemand/awshttps://api.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.us3.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws
### Overview
Fetches the most recent 1000 AWS on demand tasks. This endpoint requires the `security_monitoring_findings_read` permission.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAwsOnDemandTasks-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAwsOnDemandTasks-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#ListAwsOnDemandTasks-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object that includes a list of AWS on demand tasks.
Field
Type
Description
data
[object]
A list of on demand tasks.
attributes
object
Attributes for the AWS on demand task.
arn
string
The arn of the resource to scan.
assigned_at
string
Specifies the assignment timestamp if the task has been already assigned to a scanner.
created_at
string
The task submission timestamp.
status
string
Indicates the status of the task. QUEUED: the task has been submitted successfully and the resource has not been assigned to a scanner yet. ASSIGNED: the task has been assigned. ABORTED: the scan has been aborted after a period of time due to technical reasons, such as resource not found, insufficient permissions, or the absence of a configured scanner.
id
string
The UUID of the task.
type
enum
The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`
default: `aws_resource`
```
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

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  List AWS on demand tasks
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List AWS on demand tasks
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List AWS on demand tasks
```
# List AWS on demand tasks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.list_aws_on_demand_tasks()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List AWS on demand tasks
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List AWS on demand tasks
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List AWS on demand tasks
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List AWS on demand tasks
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task-v2)


POST https://api.ap1.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.ap2.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.datadoghq.eu/api/v2/agentless_scanning/ondemand/awshttps://api.ddog-gov.com/api/v2/agentless_scanning/ondemand/awshttps://api.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.us3.datadoghq.com/api/v2/agentless_scanning/ondemand/awshttps://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws
### Overview
Trigger the scan of an AWS resource with a high priority. Agentless scanning must be activated for the AWS account containing the resource to scan. This endpoint requires the `security_monitoring_findings_write` permission.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Request
#### Body Data (required)
The definition of the on demand task.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Field
Type
Description
data [_required_]
object
Object for a single AWS on demand task.
attributes [_required_]
object
Attributes for the AWS on demand task.
arn [_required_]
string
The arn of the resource to scan. Agentless supports the scan of EC2 instances, lambda functions, AMI, ECR, RDS and S3 buckets.
type [_required_]
enum
The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`
default: `aws_resource`
```
{
  "data": {
    "attributes": {
      "arn": "arn:aws:lambda:us-west-2:123456789012:function:my-function"
    },
    "type": "aws_resource"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsOnDemandTask-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsOnDemandTask-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsOnDemandTask-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#CreateAwsOnDemandTask-429-v2)


AWS on demand task created successfully.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object that includes an AWS on demand task.
Field
Type
Description
data
object
Single AWS on demand task.
attributes
object
Attributes for the AWS on demand task.
arn
string
The arn of the resource to scan.
assigned_at
string
Specifies the assignment timestamp if the task has been already assigned to a scanner.
created_at
string
The task submission timestamp.
status
string
Indicates the status of the task. QUEUED: the task has been submitted successfully and the resource has not been assigned to a scanner yet. ASSIGNED: the task has been assigned. ABORTED: the scan has been aborted after a period of time due to technical reasons, such as resource not found, insufficient permissions, or the absence of a configured scanner.
id
string
The UUID of the task.
type
enum
The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`
default: `aws_resource`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Create AWS on demand task returns "AWS on demand task created successfully." response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws" \
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

                        
```

#####  Create AWS on demand task returns "AWS on demand task created successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create AWS on demand task returns "AWS on demand task created successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create AWS on demand task returns "AWS on demand task created successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create AWS on demand task returns "AWS on demand task created successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create AWS on demand task returns "AWS on demand task created successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create AWS on demand task returns "AWS on demand task created successfully." response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-on-demand-task)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-on-demand-task-v2)


GET https://api.ap1.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id}https://api.ap2.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id}https://api.datadoghq.eu/api/v2/agentless_scanning/ondemand/aws/{task_id}https://api.ddog-gov.com/api/v2/agentless_scanning/ondemand/aws/{task_id}https://api.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id}https://api.us3.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id}https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/{task_id}
### Overview
Fetch the data of a specific on demand task. This endpoint requires the `security_monitoring_findings_read` permission.
OAuth apps require the `security_monitoring_findings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#agentless-scanning) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
task_id [_required_]
string
The UUID of the task.
### Response
  * [200](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsOnDemandTask-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsOnDemandTask-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsOnDemandTask-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsOnDemandTask-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/agentless-scanning/#GetAwsOnDemandTask-429-v2)


OK.
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


Response object that includes an AWS on demand task.
Field
Type
Description
data
object
Single AWS on demand task.
attributes
object
Attributes for the AWS on demand task.
arn
string
The arn of the resource to scan.
assigned_at
string
Specifies the assignment timestamp if the task has been already assigned to a scanner.
created_at
string
The task submission timestamp.
status
string
Indicates the status of the task. QUEUED: the task has been submitted successfully and the resource has not been assigned to a scanner yet. ASSIGNED: the task has been assigned. ABORTED: the scan has been aborted after a period of time due to technical reasons, such as resource not found, insufficient permissions, or the absence of a configured scanner.
id
string
The UUID of the task.
type
enum
The type of the on demand task. The value should always be `aws_resource`. Allowed enum values: `aws_resource`
default: `aws_resource`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/agentless-scanning/)
  * [Example](https://docs.datadoghq.com/api/latest/agentless-scanning/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/agentless-scanning/?code-lang=typescript)


#####  Get AWS on demand task
Copy
```
                  # Path parameters  
export task_id="6d09294c-9ad9-42fd-a759-a0c1599b4828"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/agentless_scanning/ondemand/aws/${task_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get AWS on demand task
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get AWS on demand task
```
# Get AWS on demand task returns "OK." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AgentlessScanningAPI.new
p api_instance.get_aws_on_demand_task("63d6b4f5-e5d0-4d90-824a-9580f05f026a")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get AWS on demand task
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get AWS on demand task
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get AWS on demand task
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get AWS on demand task
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=80e61ee6-b367-4f3e-a489-4c65923e6cd2&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=0e99874c-ac92-4e7a-a496-fd57eb0639b7&pt=Agentless%20Scanning&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fagentless-scanning%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=80e61ee6-b367-4f3e-a489-4c65923e6cd2&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=0e99874c-ac92-4e7a-a496-fd57eb0639b7&pt=Agentless%20Scanning&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fagentless-scanning%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=faa9edfb-15ef-4589-a1c8-fce51e9d1dd9&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Agentless%20Scanning&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fagentless-scanning%2F&r=&lt=10405&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=230169)
