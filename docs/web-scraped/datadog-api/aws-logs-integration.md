# Source: https://docs.datadoghq.com/api/latest/aws-logs-integration/

# AWS Logs Integration
Configure your Datadog-AWS-Logs integration directly through Datadog API. For more information, see the [AWS integration page](https://docs.datadoghq.com/integrations/amazon_web_services/#log-collection).
## [List all AWS Logs integrations](https://docs.datadoghq.com/api/latest/aws-logs-integration/#list-all-aws-logs-integrations)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/aws-logs-integration/#list-all-aws-logs-integrations-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/aws/logshttps://api.ap2.datadoghq.com/api/v1/integration/aws/logshttps://api.datadoghq.eu/api/v1/integration/aws/logshttps://api.ddog-gov.com/api/v1/integration/aws/logshttps://api.datadoghq.com/api/v1/integration/aws/logshttps://api.us3.datadoghq.com/api/v1/integration/aws/logshttps://api.us5.datadoghq.com/api/v1/integration/aws/logs
### Overview
List all Datadog-AWS Logs integrations configured in your Datadog account. This endpoint requires the `aws_configuration_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsIntegrations-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsIntegrations-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsIntegrations-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsIntegrations-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Field
Type
Description
account_id
string
Your AWS Account ID without dashes.
lambdas
[object]
List of ARNs configured in your Datadog account.
arn
string
Available ARN IDs.
services
[string]
Array of services IDs.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python-legacy)


#####  List all AWS Logs integrations
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all AWS Logs integrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List all AWS Logs integrations
```
# List all AWS Logs integrations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new
p api_instance.list_aws_logs_integrations()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all AWS Logs integrations
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.aws_logs_integrations_list

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all AWS Logs integrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List all AWS Logs integrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List all AWS Logs integrations
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AwsLogsIntegration.list()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  List all AWS Logs integrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List all AWS Logs integrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Add AWS Log Lambda ARN](https://docs.datadoghq.com/api/latest/aws-logs-integration/#add-aws-log-lambda-arn)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/aws-logs-integration/#add-aws-log-lambda-arn-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logshttps://api.ap2.datadoghq.com/api/v1/integration/aws/logshttps://api.datadoghq.eu/api/v1/integration/aws/logshttps://api.ddog-gov.com/api/v1/integration/aws/logshttps://api.datadoghq.com/api/v1/integration/aws/logshttps://api.us3.datadoghq.com/api/v1/integration/aws/logshttps://api.us5.datadoghq.com/api/v1/integration/aws/logs
### Overview
Attach the Lambda ARN of the Lambda created for the Datadog-AWS log collection to your AWS account ID to enable log collection. This endpoint requires the `aws_configuration_edit` permission.
### Request
#### Body Data (required)
AWS Log Lambda Async request body.
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
account_id [_required_]
string
Your AWS Account ID without dashes.
lambda_arn [_required_]
string
ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup.
```
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CreateAWSLambdaARN-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CreateAWSLambdaARN-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CreateAWSLambdaARN-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CreateAWSLambdaARN-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python-legacy)


#####  Add AWS Log Lambda ARN
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs" \
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

                
```

#####  Add AWS Log Lambda ARN
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add AWS Log Lambda ARN
```
# Add AWS Log Lambda ARN returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccountAndLambdaRequest.new({
  account_id: "1234567",
  lambda_arn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
})
p api_instance.create_aws_lambda_arn(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add AWS Log Lambda ARN
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add AWS Log Lambda ARN
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add AWS Log Lambda ARN
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Add AWS Log Lambda ARN
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Add AWS Log Lambda ARN
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Add AWS Log Lambda ARN
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete an AWS Logs integration](https://docs.datadoghq.com/api/latest/aws-logs-integration/#delete-an-aws-logs-integration)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/aws-logs-integration/#delete-an-aws-logs-integration-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/aws/logshttps://api.ap2.datadoghq.com/api/v1/integration/aws/logshttps://api.datadoghq.eu/api/v1/integration/aws/logshttps://api.ddog-gov.com/api/v1/integration/aws/logshttps://api.datadoghq.com/api/v1/integration/aws/logshttps://api.us3.datadoghq.com/api/v1/integration/aws/logshttps://api.us5.datadoghq.com/api/v1/integration/aws/logs
### Overview
Delete a Datadog-AWS logs configuration by removing the specific Lambda ARN associated with a given AWS account. This endpoint requires the `aws_configuration_edit` permission.
### Request
#### Body Data (required)
Delete AWS Lambda ARN request body.
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
account_id [_required_]
string
Your AWS Account ID without dashes.
lambda_arn [_required_]
string
ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup.
```
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#DeleteAWSLambdaARN-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/aws-logs-integration/#DeleteAWSLambdaARN-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#DeleteAWSLambdaARN-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#DeleteAWSLambdaARN-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python-legacy)


#####  Delete an AWS Logs integration
Copy
```
                  # Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs" \
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

                
```

#####  Delete an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an AWS Logs integration
```
# Delete an AWS Logs integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccountAndLambdaRequest.new({
  account_id: "1234567",
  lambda_arn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
})
p api_instance.delete_aws_lambda_arn(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Delete an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get list of AWS log ready services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services)
  * [v1](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services-v2)


GET https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.ap2.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.datadoghq.eu/api/v1/integration/aws/logs/serviceshttps://api.ddog-gov.com/api/v1/integration/aws/logs/serviceshttps://api.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.us3.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.us5.datadoghq.com/api/v1/integration/aws/logs/services
### Overview
**This endpoint is deprecated - use the V2 endpoint instead.** Get the list of current AWS services that Datadog offers automatic log collection. Use returned service IDs with the services parameter for the Enable an AWS service log collection API endpoint. This endpoint requires the `aws_configuration_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsServices-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsServices-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsServices-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
id
string
Key value in returned object.
label
string
Name of service available for configuration with Datadog logs.
```
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

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python-legacy)


#####  Get list of AWS log ready services
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get list of AWS log ready services
```
# Get list of AWS log ready services returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new
p api_instance.list_aws_logs_services()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get list of AWS log ready services
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.aws_logs_list_services

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get list of AWS log ready services
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AwsLogsIntegration.list_log_services()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

GET https://api.ap1.datadoghq.com/api/v2/integration/aws/logs/serviceshttps://api.ap2.datadoghq.com/api/v2/integration/aws/logs/serviceshttps://api.datadoghq.eu/api/v2/integration/aws/logs/serviceshttps://api.ddog-gov.com/api/v2/integration/aws/logs/serviceshttps://api.datadoghq.com/api/v2/integration/aws/logs/serviceshttps://api.us3.datadoghq.com/api/v2/integration/aws/logs/serviceshttps://api.us5.datadoghq.com/api/v2/integration/aws/logs/services
### Overview
Get a list of AWS services that can send logs to Datadog. This endpoint requires the `aws_configuration_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsServices-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsServices-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#ListAWSLogsServices-429-v2)


AWS Logs Services List object
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


AWS Logs Services response body
Field
Type
Description
data [_required_]
object
AWS Logs Services response body
attributes
object
AWS Logs Services response body
logs_services [_required_]
[string]
List of AWS services that can send logs to Datadog
id [_required_]
string
The `AWSLogsServicesResponseData` `id`.
default: `logs_services`
type [_required_]
enum
The `AWSLogsServicesResponseData` `type`. Allowed enum values: `logs_services`
default: `logs_services`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)


#####  Get list of AWS log ready services
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/logs/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get list of AWS log ready services
```
# Get list of AWS log ready services returns "AWS Logs Services List object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSLogsIntegrationAPI.new
p api_instance.list_aws_logs_services()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get list of AWS log ready services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Enable an AWS Logs integration](https://docs.datadoghq.com/api/latest/aws-logs-integration/#enable-an-aws-logs-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/aws-logs-integration/#enable-an-aws-logs-integration-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.ap2.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.datadoghq.eu/api/v1/integration/aws/logs/serviceshttps://api.ddog-gov.com/api/v1/integration/aws/logs/serviceshttps://api.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.us3.datadoghq.com/api/v1/integration/aws/logs/serviceshttps://api.us5.datadoghq.com/api/v1/integration/aws/logs/services
### Overview
Enable automatic log collection for a list of services. This should be run after running `CreateAWSLambdaARN` to save the configuration. This endpoint requires the `aws_configuration_edit` permission.
### Request
#### Body Data (required)
Enable AWS Log Services request body.
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
account_id [_required_]
string
Your AWS Account ID without dashes.
services [_required_]
[string]
Array of services IDs set to enable automatic log collection. Discover the list of available services with the get list of AWS log ready services API endpoint.
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#EnableAWSLogServices-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/aws-logs-integration/#EnableAWSLogServices-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#EnableAWSLogServices-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#EnableAWSLogServices-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python-legacy)


#####  Enable an AWS Logs integration
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services" \
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

                
```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Enable an AWS Logs integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Check permissions for log services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#check-permissions-for-log-services)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/aws-logs-integration/#check-permissions-for-log-services-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/services_asynchttps://api.ap2.datadoghq.com/api/v1/integration/aws/logs/services_asynchttps://api.datadoghq.eu/api/v1/integration/aws/logs/services_asynchttps://api.ddog-gov.com/api/v1/integration/aws/logs/services_asynchttps://api.datadoghq.com/api/v1/integration/aws/logs/services_asynchttps://api.us3.datadoghq.com/api/v1/integration/aws/logs/services_asynchttps://api.us5.datadoghq.com/api/v1/integration/aws/logs/services_async
### Overview
Test if permissions are present to add log-forwarding triggers for the given services and AWS account. Input is the same as for `EnableAWSLogServices`. Done async, so can be repeatedly polled in a non-blocking fashion until the async request completes.
  * Returns a status of `created` when it’s checking if the permissions exists in the AWS account.
  * Returns a status of `waiting` while checking.
  * Returns a status of `checked and ok` if the Lambda exists.
  * Returns a status of `error` if the Lambda does not exist.

This endpoint requires the `aws_configuration_read` permission.
### Request
#### Body Data (required)
Check AWS Logs Async Services request body.
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
account_id [_required_]
string
Your AWS Account ID without dashes.
services [_required_]
[string]
Array of services IDs set to enable automatic log collection. Discover the list of available services with the get list of AWS log ready services API endpoint.
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsServicesAsync-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsServicesAsync-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsServicesAsync-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsServicesAsync-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


A list of all Datadog-AWS logs integrations available in your Datadog organization.
Field
Type
Description
errors
[object]
List of errors.
code
string
Code properties
message
string
Message content.
status
string
Status of the properties.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python-legacy)


#####  Check permissions for log services
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/services_async" \
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

                
```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Check permissions for log services
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Check that an AWS Lambda Function exists](https://docs.datadoghq.com/api/latest/aws-logs-integration/#check-that-an-aws-lambda-function-exists)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/aws-logs-integration/#check-that-an-aws-lambda-function-exists-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/aws/logs/check_asynchttps://api.ap2.datadoghq.com/api/v1/integration/aws/logs/check_asynchttps://api.datadoghq.eu/api/v1/integration/aws/logs/check_asynchttps://api.ddog-gov.com/api/v1/integration/aws/logs/check_asynchttps://api.datadoghq.com/api/v1/integration/aws/logs/check_asynchttps://api.us3.datadoghq.com/api/v1/integration/aws/logs/check_asynchttps://api.us5.datadoghq.com/api/v1/integration/aws/logs/check_async
### Overview
Test if permissions are present to add a log-forwarding triggers for the given services and AWS account. The input is the same as for Enable an AWS service log collection. Subsequent requests will always repeat the above, so this endpoint can be polled intermittently instead of blocking.
  * Returns a status of ‘created’ when it’s checking if the Lambda exists in the account.
  * Returns a status of ‘waiting’ while checking.
  * Returns a status of ‘checked and ok’ if the Lambda exists.
  * Returns a status of ’error’ if the Lambda does not exist.

This endpoint requires the `aws_configuration_read` permission.
### Request
#### Body Data (required)
Check AWS Log Lambda Async request body.
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Expand All
Field
Type
Description
account_id [_required_]
string
Your AWS Account ID without dashes.
lambda_arn [_required_]
string
ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup.
```
{
  "account_id": "1234567",
  "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsLambdaAsync-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsLambdaAsync-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsLambdaAsync-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/aws-logs-integration/#CheckAWSLogsLambdaAsync-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


A list of all Datadog-AWS logs integrations available in your Datadog organization.
Field
Type
Description
errors
[object]
List of errors.
code
string
Code properties
message
string
Message content.
status
string
Status of the properties.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/aws-logs-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/aws-logs-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/aws-logs-integration/?code-lang=python-legacy)


#####  Check that an AWS Lambda Function exists
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/logs/check_async" \
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

                
```

#####  Check that an AWS Lambda Function exists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Check that an AWS Lambda Function exists
```
# Check that an AWS Lambda Function exists returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSLogsIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccountAndLambdaRequest.new({
  account_id: "1234567",
  lambda_arn: "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
})
p api_instance.check_aws_logs_lambda_async(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Check that an AWS Lambda Function exists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Check that an AWS Lambda Function exists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Check that an AWS Lambda Function exists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Check that an AWS Lambda Function exists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Check that an AWS Lambda Function exists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Check that an AWS Lambda Function exists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2e6c7612-5a28-4467-81ca-dfda27b00f08&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=85df3bf0-1e0b-48fc-94a4-36c19e056548&pt=AWS%20Logs%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faws-logs-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2e6c7612-5a28-4467-81ca-dfda27b00f08&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=85df3bf0-1e0b-48fc-94a4-36c19e056548&pt=AWS%20Logs%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faws-logs-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=1479f5fd-687b-41ea-b593-3fec27095780&bo=2&sid=26a3a930f0bf11f090a827a9ebc76acd&vid=26a47450f0bf11f09ce8df1ce1dab822&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=AWS%20Logs%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faws-logs-integration%2F&r=&lt=1467&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=546913)
