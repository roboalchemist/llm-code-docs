# Source: https://docs.datadoghq.com/api/latest/logs-pipelines/

# Logs Pipelines
Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.
  * See the [pipelines configuration page](https://app.datadoghq.com/logs/pipelines) for a list of the pipelines and processors currently configured in web UI.
  * Additional API-related information about processors can be found in the [processors documentation](https://docs.datadoghq.com/logs/log_configuration/processors/?tab=api#lookup-processor).
  * For more information about Pipelines, see the [pipeline documentation](https://docs.datadoghq.com/logs/log_configuration/pipelines).


**Notes:**
**Grok parsing rules may effect JSON output and require returned data to be configured before using in a request.** For example, if you are using the data returned from a request for another request body, and have a parsing rule that uses a regex pattern like `\s` for spaces, you will need to configure all escaped spaces as `%{space}` to use in the body data.
## [Get pipeline order](https://docs.datadoghq.com/api/latest/logs-pipelines/#get-pipeline-order)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-pipelines/#get-pipeline-order-v1)


GET https://api.ap1.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.ap2.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.datadoghq.eu/api/v1/logs/config/pipeline-orderhttps://api.ddog-gov.com/api/v1/logs/config/pipeline-orderhttps://api.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.us3.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order
### Overview
Get the current order of your pipelines. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-pipelines/#GetLogsPipelineOrder-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-pipelines/#GetLogsPipelineOrder-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-pipelines/#GetLogsPipelineOrder-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Object containing the ordered list of pipeline IDs.
Expand All
Field
Type
Description
pipeline_ids [_required_]
[string]
Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog.
```
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=typescript)


#####  Get pipeline order
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get pipeline order
```
"""
Get pipeline order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.get_logs_pipeline_order()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get pipeline order
```
# Get pipeline order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.get_logs_pipeline_order()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get pipeline order
```
// Get pipeline order returns "OK" response

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
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.GetLogsPipelineOrder(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.GetLogsPipelineOrder`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.GetLogsPipelineOrder`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get pipeline order
```
// Get pipeline order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipelinesOrder;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      LogsPipelinesOrder result = apiInstance.getLogsPipelineOrder();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#getLogsPipelineOrder");
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

#####  Get pipeline order
```
// Get pipeline order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.get_logs_pipeline_order().await;
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

#####  Get pipeline order
```
/**
 * Get pipeline order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

apiInstance
  .getLogsPipelineOrder()
  .then((data: v1.LogsPipelinesOrder) => {
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
## [Update pipeline order](https://docs.datadoghq.com/api/latest/logs-pipelines/#update-pipeline-order)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-pipelines/#update-pipeline-order-v1)


PUT https://api.ap1.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.ap2.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.datadoghq.eu/api/v1/logs/config/pipeline-orderhttps://api.ddog-gov.com/api/v1/logs/config/pipeline-orderhttps://api.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.us3.datadoghq.com/api/v1/logs/config/pipeline-orderhttps://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order
### Overview
Update the order of your pipelines. Since logs are processed sequentially, reordering a pipeline may change the structure and content of the data processed by other pipelines and their processors.
**Note** : Using the `PUT` method updates your pipeline order by replacing your current order with the new one sent to your Datadog organization.
This endpoint requires the `logs_write_pipelines` permission.
### Request
#### Body Data (required)
Object containing the new ordered list of pipeline IDs.
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Expand All
Field
Type
Description
pipeline_ids [_required_]
[string]
Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog.
```
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipelineOrder-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipelineOrder-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipelineOrder-403-v1)
  * [422](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipelineOrder-422-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipelineOrder-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Object containing the ordered list of pipeline IDs.
Expand All
Field
Type
Description
pipeline_ids [_required_]
[string]
Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog.
```
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Response returned by the Logs API when errors occur.
Field
Type
Description
error
object
Error returned by the Logs API
code
string
Code identifying the error
details
[object]
Additional error details
message
string
Error message
```
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
Unprocessable Entity
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Response returned by the Logs API when errors occur.
Field
Type
Description
error
object
Error returned by the Logs API
code
string
Code identifying the error
details
[object]
Additional error details
message
string
Error message
```
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=typescript)


#####  Update pipeline order
Copy
```
                  # Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
EOF  

                
```

#####  Update pipeline order
```
"""
Update pipeline order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_pipelines_order import LogsPipelinesOrder

body = LogsPipelinesOrder(
    pipeline_ids=[
        "tags",
        "org_ids",
        "products",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.update_logs_pipeline_order(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update pipeline order
```
# Update pipeline order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipelinesOrder.new({
  pipeline_ids: [
    "tags",
    "org_ids",
    "products",
  ],
})
p api_instance.update_logs_pipeline_order(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update pipeline order
```
// Update pipeline order returns "OK" response

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
	body := datadogV1.LogsPipelinesOrder{
		PipelineIds: []string{
			"tags",
			"org_ids",
			"products",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.UpdateLogsPipelineOrder(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.UpdateLogsPipelineOrder`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.UpdateLogsPipelineOrder`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update pipeline order
```
// Update pipeline order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipelinesOrder;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipelinesOrder body =
        new LogsPipelinesOrder().pipelineIds(Arrays.asList("tags", "org_ids", "products"));

    try {
      LogsPipelinesOrder result = apiInstance.updateLogsPipelineOrder(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#updateLogsPipelineOrder");
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

#####  Update pipeline order
```
// Update pipeline order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsPipelinesOrder;

#[tokio::main]
async fn main() {
    let body = LogsPipelinesOrder::new(vec![
        "tags".to_string(),
        "org_ids".to_string(),
        "products".to_string(),
    ]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.update_logs_pipeline_order(body).await;
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

#####  Update pipeline order
```
/**
 * Update pipeline order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiUpdateLogsPipelineOrderRequest = {
  body: {
    pipelineIds: ["tags", "org_ids", "products"],
  },
};

apiInstance
  .updateLogsPipelineOrder(params)
  .then((data: v1.LogsPipelinesOrder) => {
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
## [Get all pipelines](https://docs.datadoghq.com/api/latest/logs-pipelines/#get-all-pipelines)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-pipelines/#get-all-pipelines-v1)


GET https://api.ap1.datadoghq.com/api/v1/logs/config/pipelineshttps://api.ap2.datadoghq.com/api/v1/logs/config/pipelineshttps://api.datadoghq.eu/api/v1/logs/config/pipelineshttps://api.ddog-gov.com/api/v1/logs/config/pipelineshttps://api.datadoghq.com/api/v1/logs/config/pipelineshttps://api.us3.datadoghq.com/api/v1/logs/config/pipelineshttps://api.us5.datadoghq.com/api/v1/logs/config/pipelines
### Overview
Get all pipelines from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-pipelines/#ListLogsPipelines-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-pipelines/#ListLogsPipelines-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-pipelines/#ListLogsPipelines-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Array of all log pipeline objects configured for the organization.
Field
Type
Description
description
string
A description of the pipeline.
filter
object
Filter for logs.
query
string
The filter query.
id
string
ID of the pipeline.
is_enabled
boolean
Whether or not the pipeline is enabled.
is_read_only
boolean
Whether or not the pipeline can be edited.
name
string
Name of the pipeline.
processors
[ <oneOf>]
Ordered list of processors in this pipeline.
Option 1
object
Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).
grok [_required_]
object
Set of rules for the grok parser.
match_rules [_required_]
string
List of match rules for the grok parser, separated by a new line.
support_rules
string
List of support rules for the grok parser, separated by a new line.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
samples
[string]
List of sample logs to test this grok parser.
source [_required_]
string
Name of the log attribute to parse.
default: `message`
type [_required_]
enum
Type of logs grok parser. Allowed enum values: `grok-parser`
default: `grok-parser`
Option 2
object
As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.
  * `timestamp`
  * `date`
  * `_timestamp`
  * `Timestamp`
  * `eventTime`
  * `published_date`
If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164.


**Note:** If your logs don’t contain any of the default attributes and you haven’t defined your own date attribute, Datadog timestamps the logs with the date it received them.
If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs date remapper. Allowed enum values: `date-remapper`
default: `date-remapper`
Option 3
object
Use this Processor if you want to assign some attributes as the official status.
Each incoming status value is mapped as follows.
  * Integers from 0 to 7 map to the Syslog severity standards
  * Strings beginning with `emerg` or f (case-insensitive) map to `emerg` (0)
  * Strings beginning with `a` (case-insensitive) map to `alert` (1)
  * Strings beginning with `c` (case-insensitive) map to `critical` (2)
  * Strings beginning with `err` (case-insensitive) map to `error` (3)
  * Strings beginning with `w` (case-insensitive) map to `warning` (4)
  * Strings beginning with `n` (case-insensitive) map to `notice` (5)
  * Strings beginning with `i` (case-insensitive) map to `info` (6)
  * Strings beginning with `d`, `trace` or `verbose` (case-insensitive) map to `debug` (7)
  * Strings beginning with `o` or matching `OK` or `Success` (case-insensitive) map to OK
  * All others map to `info` (6)


**Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs status remapper. Allowed enum values: `status-remapper`
default: `status-remapper`
Option 4
object
Use this processor if you want to assign one or more attributes as the official service.
**Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs service remapper. Allowed enum values: `service-remapper`
default: `service-remapper`
Option 5
object
The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.
**Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `msg`
type [_required_]
enum
Type of logs message remapper. Allowed enum values: `message-remapper`
default: `message-remapper`
Option 6
object
The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
override_on_conflict
boolean
Override or not the target element if already set,
preserve_source
boolean
Remove or preserve the remapped source element.
source_type
string
Defines if the sources are from log `attribute` or `tag`.
default: `attribute`
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Final attribute or tag name to remap the sources to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
target_type
string
Defines if the final attribute or tag name is from log `attribute` or `tag`.
default: `attribute`
type [_required_]
enum
Type of logs attribute remapper. Allowed enum values: `attribute-remapper`
default: `attribute-remapper`
Option 7
object
This processor extracts query parameters and other important parameters from a URL.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
normalize_ending_slashes
boolean
Normalize the ending slashes or not.
sources [_required_]
[string]
Array of source attributes.
default: `http.url`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.url_details`
type [_required_]
enum
Type of logs URL parser. Allowed enum values: `url-parser`
default: `url-parser`
Option 8
object
The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.
is_enabled
boolean
Whether or not the processor is enabled.
is_encoded
boolean
Define if the source attribute is URL encoded or not.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `http.useragent`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.useragent_details`
type [_required_]
enum
Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`
default: `user-agent-parser`
Option 9
object
Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Once the log has matched one of the Processor queries, it stops. Make sure they are properly ordered in case a log could match several queries.
  * The names of the categories must be unique.
  * Once defined in the Category Processor, you can map categories to log status using the Log Status Remapper.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter
object
Filter for logs.
query
string
The filter query.
name
string
Value to assign to the target attribute.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
target [_required_]
string
Name of the target attribute which value is defined by the matching category.
type [_required_]
enum
Type of logs category processor. Allowed enum values: `category-processor`
default: `category-processor`
Option 10
object
Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.
The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.
By default, the calculation is skipped if an attribute is missing. Select “Replace missing attribute by 0” to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number.
_Notes_ :
  * The operator `-` needs to be space split in the formula as it can also be contained in attribute names.
  * If the target attribute already exists, it is overwritten by the result of the formula.
  * Results are rounded up to the 9th decimal. For example, if the result of the formula is `0.1234567891`, the actual value stored for the attribute is `0.123456789`.
  * If you need to scale a unit of measure, see [Scale Filter](https://docs.datadoghq.com/logs/log_configuration/parsing/?tab=filter#matcher-and-filter).


expression [_required_]
string
Arithmetic operation between one or more log attributes.
is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.
name
string
Name of the processor.
target [_required_]
string
Name of the attribute that contains the result of the arithmetic operation.
type [_required_]
enum
Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`
default: `arithmetic-processor`
Option 11
object
Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.
The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.
**Notes** :
  * The processor only accepts attributes with values or an array of values in the blocks.
  * If an attribute cannot be used (object or array of object), it is replaced by an empty string or the entire operation is skipped depending on your selection.
  * If the target attribute already exists, it is overwritten by the result of the template.
  * Results of the template cannot exceed 256 characters.


is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.
name
string
Name of the processor.
target [_required_]
string
The name of the attribute that contains the result of the template.
template [_required_]
string
A formula with one or more attributes and raw text.
type [_required_]
enum
Type of logs string builder processor. Allowed enum values: `string-builder-processor`
default: `string-builder-processor`
Option 12
object
Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.
A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.
filter
object
Filter for logs.
query
string
The filter query.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
processors
[object]
Ordered list of processors in this pipeline.
type [_required_]
enum
Type of logs pipeline processor. Allowed enum values: `pipeline`
default: `pipeline`
Option 13
object
The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `network.client.ip`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `network.client.geoip`
type [_required_]
enum
Type of GeoIP parser. Allowed enum values: `geo-ip-parser`
default: `geo-ip-parser`
Option 14
object
Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
default_lookup
string
Value to set the target attribute if the source value is not found in the list.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_table [_required_]
[string]
Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 15
object
**Note** : Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_enrichment_table [_required_]
string
Name of the Reference Table for the source attribute and their associated target attribute values.
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 16
object
There are two ways to improve correlation between application traces and logs.
  1. Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.
  2. Use the Trace remapper processor to define a log attribute as its associated trace ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.trace_id`
type [_required_]
enum
Type of logs trace remapper. Allowed enum values: `trace-id-remapper`
default: `trace-id-remapper`
Option 17
object
There are two ways to define correlation between application spans and logs:
  1. Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default.
  2. Use the span remapper processor to define a log attribute as its associated span ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.span_id`
type [_required_]
enum
Type of logs span remapper. Allowed enum values: `span-id-remapper`
default: `span-id-remapper`
Option 18
object
A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:
  * Select value from matching element
  * Compute array length
  * Append a value to an array


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
operation [_required_]
<oneOf>
Configuration of the array processor operation to perform.
Option 1
object
Operation that appends a value to a target array attribute.
preserve_source
boolean
Remove or preserve the remapped source element.
default: `true`
source [_required_]
string
Attribute path containing the value to append.
target [_required_]
string
Attribute path of the array to append to.
type [_required_]
enum
Operation type. Allowed enum values: `append`
Option 2
object
Operation that computes the length of a `source` array and stores the result in the `target` attribute.
source [_required_]
string
Attribute path of the array to measure.
target [_required_]
string
Attribute that receives the computed length.
type [_required_]
enum
Operation type. Allowed enum values: `length`
Option 3
object
Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.
filter [_required_]
string
Filter condition expressed as `key:value` used to find the matching element.
source [_required_]
string
Attribute path of the array to search into.
target [_required_]
string
Attribute that receives the extracted value.
type [_required_]
enum
Operation type. Allowed enum values: `select`
value_to_extract [_required_]
string
Key of the value to extract from the matching element.
type [_required_]
enum
Type of logs array processor. Allowed enum values: `array-processor`
default: `array-processor`
Option 19
object
The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.
binary_to_text_encoding [_required_]
enum
The encoding used to represent the binary data. Allowed enum values: `base64,base16`
input_representation [_required_]
enum
The original representation of input string. Allowed enum values: `utf_8,integer`
is_enabled
boolean
Whether the processor is enabled.
name
string
Name of the processor.
source [_required_]
string
Name of the log attribute with the encoded data.
target [_required_]
string
Name of the log attribute that contains the decoded data.
type [_required_]
enum
Type of logs decoder processor. Allowed enum values: `decoder-processor`
default: `decoder-processor`
Option 20
object
A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.
is_enabled
boolean
Whether or not the processor is enabled.
mappers [_required_]
[ <oneOf>]
The `LogsSchemaProcessor` `mappers`.
Option 1
object
The schema remapper maps source log fields to their correct fields.
name [_required_]
string
Name of the logs schema remapper.
override_on_conflict
boolean
Override or not the target element if already set.
preserve_source
boolean
Remove or preserve the remapped source element.
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Target field to map log source field to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
type [_required_]
enum
Type of logs schema remapper. Allowed enum values: `schema-remapper`
Option 2
object
Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Categories are executed in order and processing stops at the first match. Make sure categories are properly ordered in case a log could match multiple queries.
  * Sibling fields always have a numerical ID field and a human-readable string name.
  * A fallback section handles cases where the name or ID value matches a specific value. If the name matches "Other" or the ID matches 99, the value of the sibling name field will be pulled from a source field from the original log.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
id [_required_]
int64
ID to inject into the category.
name [_required_]
string
Value to assign to target schema field.
fallback
object
Used to override hardcoded category values with a value pulled from a source attribute on the log.
sources
object
Fallback sources used to populate value of field.
<any-key>
[string]
values
object
Values that define when the fallback is used.
<any-key>
string
name [_required_]
string
Name of the logs schema category mapper.
targets [_required_]
object
Name of the target attributes which value is defined by the matching category.
id
string
ID of the field to map log attributes to.
name
string
Name of the field to map log attributes to.
type [_required_]
enum
Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`
name [_required_]
string
Name of the processor.
schema [_required_]
object
Configuration of the schema data to use.
class_name [_required_]
string
Class name of the schema to use.
class_uid [_required_]
int64
Class UID of the schema to use.
profiles
[string]
Optional list of profiles to modify the schema.
schema_type [_required_]
string
Type of schema to use.
version [_required_]
string
Version of the schema to use.
type [_required_]
enum
Type of logs schema processor. Allowed enum values: `schema-processor`
default: `schema-processor`
tags
[string]
A list of tags associated with the pipeline.
type
string
Type of pipeline.
```
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=typescript)


#####  Get all pipelines
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all pipelines
```
"""
Get all pipelines returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.list_logs_pipelines()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all pipelines
```
# Get all pipelines returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.list_logs_pipelines()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all pipelines
```
// Get all pipelines returns "OK" response

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
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.ListLogsPipelines(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.ListLogsPipelines`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.ListLogsPipelines`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all pipelines
```
// Get all pipelines returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipeline;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      List<LogsPipeline> result = apiInstance.listLogsPipelines();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#listLogsPipelines");
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

#####  Get all pipelines
```
// Get all pipelines returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.list_logs_pipelines().await;
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

#####  Get all pipelines
```
/**
 * Get all pipelines returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

apiInstance
  .listLogsPipelines()
  .then((data: v1.LogsPipeline[]) => {
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
## [Create a pipeline](https://docs.datadoghq.com/api/latest/logs-pipelines/#create-a-pipeline)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-pipelines/#create-a-pipeline-v1)


POST https://api.ap1.datadoghq.com/api/v1/logs/config/pipelineshttps://api.ap2.datadoghq.com/api/v1/logs/config/pipelineshttps://api.datadoghq.eu/api/v1/logs/config/pipelineshttps://api.ddog-gov.com/api/v1/logs/config/pipelineshttps://api.datadoghq.com/api/v1/logs/config/pipelineshttps://api.us3.datadoghq.com/api/v1/logs/config/pipelineshttps://api.us5.datadoghq.com/api/v1/logs/config/pipelines
### Overview
Create a pipeline in your organization. This endpoint requires the `logs_write_pipelines` permission.
### Request
#### Body Data (required)
Definition of the new pipeline.
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Field
Type
Description
description
string
A description of the pipeline.
filter
object
Filter for logs.
query
string
The filter query.
id
string
ID of the pipeline.
is_enabled
boolean
Whether or not the pipeline is enabled.
is_read_only
boolean
Whether or not the pipeline can be edited.
name [_required_]
string
Name of the pipeline.
processors
[ <oneOf>]
Ordered list of processors in this pipeline.
Option 1
object
Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).
grok [_required_]
object
Set of rules for the grok parser.
match_rules [_required_]
string
List of match rules for the grok parser, separated by a new line.
support_rules
string
List of support rules for the grok parser, separated by a new line.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
samples
[string]
List of sample logs to test this grok parser.
source [_required_]
string
Name of the log attribute to parse.
default: `message`
type [_required_]
enum
Type of logs grok parser. Allowed enum values: `grok-parser`
default: `grok-parser`
Option 2
object
As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.
  * `timestamp`
  * `date`
  * `_timestamp`
  * `Timestamp`
  * `eventTime`
  * `published_date`
If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164.


**Note:** If your logs don’t contain any of the default attributes and you haven’t defined your own date attribute, Datadog timestamps the logs with the date it received them.
If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs date remapper. Allowed enum values: `date-remapper`
default: `date-remapper`
Option 3
object
Use this Processor if you want to assign some attributes as the official status.
Each incoming status value is mapped as follows.
  * Integers from 0 to 7 map to the Syslog severity standards
  * Strings beginning with `emerg` or f (case-insensitive) map to `emerg` (0)
  * Strings beginning with `a` (case-insensitive) map to `alert` (1)
  * Strings beginning with `c` (case-insensitive) map to `critical` (2)
  * Strings beginning with `err` (case-insensitive) map to `error` (3)
  * Strings beginning with `w` (case-insensitive) map to `warning` (4)
  * Strings beginning with `n` (case-insensitive) map to `notice` (5)
  * Strings beginning with `i` (case-insensitive) map to `info` (6)
  * Strings beginning with `d`, `trace` or `verbose` (case-insensitive) map to `debug` (7)
  * Strings beginning with `o` or matching `OK` or `Success` (case-insensitive) map to OK
  * All others map to `info` (6)


**Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs status remapper. Allowed enum values: `status-remapper`
default: `status-remapper`
Option 4
object
Use this processor if you want to assign one or more attributes as the official service.
**Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs service remapper. Allowed enum values: `service-remapper`
default: `service-remapper`
Option 5
object
The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.
**Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `msg`
type [_required_]
enum
Type of logs message remapper. Allowed enum values: `message-remapper`
default: `message-remapper`
Option 6
object
The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
override_on_conflict
boolean
Override or not the target element if already set,
preserve_source
boolean
Remove or preserve the remapped source element.
source_type
string
Defines if the sources are from log `attribute` or `tag`.
default: `attribute`
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Final attribute or tag name to remap the sources to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
target_type
string
Defines if the final attribute or tag name is from log `attribute` or `tag`.
default: `attribute`
type [_required_]
enum
Type of logs attribute remapper. Allowed enum values: `attribute-remapper`
default: `attribute-remapper`
Option 7
object
This processor extracts query parameters and other important parameters from a URL.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
normalize_ending_slashes
boolean
Normalize the ending slashes or not.
sources [_required_]
[string]
Array of source attributes.
default: `http.url`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.url_details`
type [_required_]
enum
Type of logs URL parser. Allowed enum values: `url-parser`
default: `url-parser`
Option 8
object
The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.
is_enabled
boolean
Whether or not the processor is enabled.
is_encoded
boolean
Define if the source attribute is URL encoded or not.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `http.useragent`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.useragent_details`
type [_required_]
enum
Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`
default: `user-agent-parser`
Option 9
object
Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Once the log has matched one of the Processor queries, it stops. Make sure they are properly ordered in case a log could match several queries.
  * The names of the categories must be unique.
  * Once defined in the Category Processor, you can map categories to log status using the Log Status Remapper.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter
object
Filter for logs.
query
string
The filter query.
name
string
Value to assign to the target attribute.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
target [_required_]
string
Name of the target attribute which value is defined by the matching category.
type [_required_]
enum
Type of logs category processor. Allowed enum values: `category-processor`
default: `category-processor`
Option 10
object
Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.
The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.
By default, the calculation is skipped if an attribute is missing. Select “Replace missing attribute by 0” to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number.
_Notes_ :
  * The operator `-` needs to be space split in the formula as it can also be contained in attribute names.
  * If the target attribute already exists, it is overwritten by the result of the formula.
  * Results are rounded up to the 9th decimal. For example, if the result of the formula is `0.1234567891`, the actual value stored for the attribute is `0.123456789`.
  * If you need to scale a unit of measure, see [Scale Filter](https://docs.datadoghq.com/logs/log_configuration/parsing/?tab=filter#matcher-and-filter).


expression [_required_]
string
Arithmetic operation between one or more log attributes.
is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.
name
string
Name of the processor.
target [_required_]
string
Name of the attribute that contains the result of the arithmetic operation.
type [_required_]
enum
Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`
default: `arithmetic-processor`
Option 11
object
Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.
The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.
**Notes** :
  * The processor only accepts attributes with values or an array of values in the blocks.
  * If an attribute cannot be used (object or array of object), it is replaced by an empty string or the entire operation is skipped depending on your selection.
  * If the target attribute already exists, it is overwritten by the result of the template.
  * Results of the template cannot exceed 256 characters.


is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.
name
string
Name of the processor.
target [_required_]
string
The name of the attribute that contains the result of the template.
template [_required_]
string
A formula with one or more attributes and raw text.
type [_required_]
enum
Type of logs string builder processor. Allowed enum values: `string-builder-processor`
default: `string-builder-processor`
Option 12
object
Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.
A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.
filter
object
Filter for logs.
query
string
The filter query.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
processors
[object]
Ordered list of processors in this pipeline.
type [_required_]
enum
Type of logs pipeline processor. Allowed enum values: `pipeline`
default: `pipeline`
Option 13
object
The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `network.client.ip`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `network.client.geoip`
type [_required_]
enum
Type of GeoIP parser. Allowed enum values: `geo-ip-parser`
default: `geo-ip-parser`
Option 14
object
Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
default_lookup
string
Value to set the target attribute if the source value is not found in the list.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_table [_required_]
[string]
Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 15
object
**Note** : Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_enrichment_table [_required_]
string
Name of the Reference Table for the source attribute and their associated target attribute values.
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 16
object
There are two ways to improve correlation between application traces and logs.
  1. Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.
  2. Use the Trace remapper processor to define a log attribute as its associated trace ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.trace_id`
type [_required_]
enum
Type of logs trace remapper. Allowed enum values: `trace-id-remapper`
default: `trace-id-remapper`
Option 17
object
There are two ways to define correlation between application spans and logs:
  1. Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default.
  2. Use the span remapper processor to define a log attribute as its associated span ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.span_id`
type [_required_]
enum
Type of logs span remapper. Allowed enum values: `span-id-remapper`
default: `span-id-remapper`
Option 18
object
A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:
  * Select value from matching element
  * Compute array length
  * Append a value to an array


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
operation [_required_]
<oneOf>
Configuration of the array processor operation to perform.
Option 1
object
Operation that appends a value to a target array attribute.
preserve_source
boolean
Remove or preserve the remapped source element.
default: `true`
source [_required_]
string
Attribute path containing the value to append.
target [_required_]
string
Attribute path of the array to append to.
type [_required_]
enum
Operation type. Allowed enum values: `append`
Option 2
object
Operation that computes the length of a `source` array and stores the result in the `target` attribute.
source [_required_]
string
Attribute path of the array to measure.
target [_required_]
string
Attribute that receives the computed length.
type [_required_]
enum
Operation type. Allowed enum values: `length`
Option 3
object
Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.
filter [_required_]
string
Filter condition expressed as `key:value` used to find the matching element.
source [_required_]
string
Attribute path of the array to search into.
target [_required_]
string
Attribute that receives the extracted value.
type [_required_]
enum
Operation type. Allowed enum values: `select`
value_to_extract [_required_]
string
Key of the value to extract from the matching element.
type [_required_]
enum
Type of logs array processor. Allowed enum values: `array-processor`
default: `array-processor`
Option 19
object
The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.
binary_to_text_encoding [_required_]
enum
The encoding used to represent the binary data. Allowed enum values: `base64,base16`
input_representation [_required_]
enum
The original representation of input string. Allowed enum values: `utf_8,integer`
is_enabled
boolean
Whether the processor is enabled.
name
string
Name of the processor.
source [_required_]
string
Name of the log attribute with the encoded data.
target [_required_]
string
Name of the log attribute that contains the decoded data.
type [_required_]
enum
Type of logs decoder processor. Allowed enum values: `decoder-processor`
default: `decoder-processor`
Option 20
object
A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.
is_enabled
boolean
Whether or not the processor is enabled.
mappers [_required_]
[ <oneOf>]
The `LogsSchemaProcessor` `mappers`.
Option 1
object
The schema remapper maps source log fields to their correct fields.
name [_required_]
string
Name of the logs schema remapper.
override_on_conflict
boolean
Override or not the target element if already set.
preserve_source
boolean
Remove or preserve the remapped source element.
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Target field to map log source field to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
type [_required_]
enum
Type of logs schema remapper. Allowed enum values: `schema-remapper`
Option 2
object
Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Categories are executed in order and processing stops at the first match. Make sure categories are properly ordered in case a log could match multiple queries.
  * Sibling fields always have a numerical ID field and a human-readable string name.
  * A fallback section handles cases where the name or ID value matches a specific value. If the name matches "Other" or the ID matches 99, the value of the sibling name field will be pulled from a source field from the original log.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
id [_required_]
int64
ID to inject into the category.
name [_required_]
string
Value to assign to target schema field.
fallback
object
Used to override hardcoded category values with a value pulled from a source attribute on the log.
sources
object
Fallback sources used to populate value of field.
<any-key>
[string]
values
object
Values that define when the fallback is used.
<any-key>
string
name [_required_]
string
Name of the logs schema category mapper.
targets [_required_]
object
Name of the target attributes which value is defined by the matching category.
id
string
ID of the field to map log attributes to.
name
string
Name of the field to map log attributes to.
type [_required_]
enum
Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`
name [_required_]
string
Name of the processor.
schema [_required_]
object
Configuration of the schema data to use.
class_name [_required_]
string
Class name of the schema to use.
class_uid [_required_]
int64
Class UID of the schema to use.
profiles
[string]
Optional list of profiles to modify the schema.
schema_type [_required_]
string
Type of schema to use.
version [_required_]
string
Version of the schema to use.
type [_required_]
enum
Type of logs schema processor. Allowed enum values: `schema-processor`
default: `schema-processor`
tags
[string]
A list of tags associated with the pipeline.
type
string
Type of pipeline.
#####  Create a pipeline with Array Processor Append Operation returns "OK" response
```
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppend",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_to_array",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps"
      }
    }
  ],
  "tags": []
}
```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response
```
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendNoPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_remove_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": false
      }
    }
  ],
  "tags": []
}
```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response
```
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_keep_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": true
      }
    }
  ],
  "tags": []
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-pipelines/#CreateLogsPipeline-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-pipelines/#CreateLogsPipeline-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-pipelines/#CreateLogsPipeline-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-pipelines/#CreateLogsPipeline-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.
**Note** : These endpoints are only available for admin users. Make sure to use an application key created by an admin.
Field
Type
Description
description
string
A description of the pipeline.
filter
object
Filter for logs.
query
string
The filter query.
id
string
ID of the pipeline.
is_enabled
boolean
Whether or not the pipeline is enabled.
is_read_only
boolean
Whether or not the pipeline can be edited.
name [_required_]
string
Name of the pipeline.
processors
[ <oneOf>]
Ordered list of processors in this pipeline.
Option 1
object
Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).
grok [_required_]
object
Set of rules for the grok parser.
match_rules [_required_]
string
List of match rules for the grok parser, separated by a new line.
support_rules
string
List of support rules for the grok parser, separated by a new line.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
samples
[string]
List of sample logs to test this grok parser.
source [_required_]
string
Name of the log attribute to parse.
default: `message`
type [_required_]
enum
Type of logs grok parser. Allowed enum values: `grok-parser`
default: `grok-parser`
Option 2
object
As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.
  * `timestamp`
  * `date`
  * `_timestamp`
  * `Timestamp`
  * `eventTime`
  * `published_date`
If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164.


**Note:** If your logs don’t contain any of the default attributes and you haven’t defined your own date attribute, Datadog timestamps the logs with the date it received them.
If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs date remapper. Allowed enum values: `date-remapper`
default: `date-remapper`
Option 3
object
Use this Processor if you want to assign some attributes as the official status.
Each incoming status value is mapped as follows.
  * Integers from 0 to 7 map to the Syslog severity standards
  * Strings beginning with `emerg` or f (case-insensitive) map to `emerg` (0)
  * Strings beginning with `a` (case-insensitive) map to `alert` (1)
  * Strings beginning with `c` (case-insensitive) map to `critical` (2)
  * Strings beginning with `err` (case-insensitive) map to `error` (3)
  * Strings beginning with `w` (case-insensitive) map to `warning` (4)
  * Strings beginning with `n` (case-insensitive) map to `notice` (5)
  * Strings beginning with `i` (case-insensitive) map to `info` (6)
  * Strings beginning with `d`, `trace` or `verbose` (case-insensitive) map to `debug` (7)
  * Strings beginning with `o` or matching `OK` or `Success` (case-insensitive) map to OK
  * All others map to `info` (6)


**Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs status remapper. Allowed enum values: `status-remapper`
default: `status-remapper`
Option 4
object
Use this processor if you want to assign one or more attributes as the official service.
**Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs service remapper. Allowed enum values: `service-remapper`
default: `service-remapper`
Option 5
object
The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.
**Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `msg`
type [_required_]
enum
Type of logs message remapper. Allowed enum values: `message-remapper`
default: `message-remapper`
Option 6
object
The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
override_on_conflict
boolean
Override or not the target element if already set,
preserve_source
boolean
Remove or preserve the remapped source element.
source_type
string
Defines if the sources are from log `attribute` or `tag`.
default: `attribute`
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Final attribute or tag name to remap the sources to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
target_type
string
Defines if the final attribute or tag name is from log `attribute` or `tag`.
default: `attribute`
type [_required_]
enum
Type of logs attribute remapper. Allowed enum values: `attribute-remapper`
default: `attribute-remapper`
Option 7
object
This processor extracts query parameters and other important parameters from a URL.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
normalize_ending_slashes
boolean
Normalize the ending slashes or not.
sources [_required_]
[string]
Array of source attributes.
default: `http.url`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.url_details`
type [_required_]
enum
Type of logs URL parser. Allowed enum values: `url-parser`
default: `url-parser`
Option 8
object
The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.
is_enabled
boolean
Whether or not the processor is enabled.
is_encoded
boolean
Define if the source attribute is URL encoded or not.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `http.useragent`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.useragent_details`
type [_required_]
enum
Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`
default: `user-agent-parser`
Option 9
object
Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Once the log has matched one of the Processor queries, it stops. Make sure they are properly ordered in case a log could match several queries.
  * The names of the categories must be unique.
  * Once defined in the Category Processor, you can map categories to log status using the Log Status Remapper.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter
object
Filter for logs.
query
string
The filter query.
name
string
Value to assign to the target attribute.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
target [_required_]
string
Name of the target attribute which value is defined by the matching category.
type [_required_]
enum
Type of logs category processor. Allowed enum values: `category-processor`
default: `category-processor`
Option 10
object
Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.
The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.
By default, the calculation is skipped if an attribute is missing. Select “Replace missing attribute by 0” to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number.
_Notes_ :
  * The operator `-` needs to be space split in the formula as it can also be contained in attribute names.
  * If the target attribute already exists, it is overwritten by the result of the formula.
  * Results are rounded up to the 9th decimal. For example, if the result of the formula is `0.1234567891`, the actual value stored for the attribute is `0.123456789`.
  * If you need to scale a unit of measure, see [Scale Filter](https://docs.datadoghq.com/logs/log_configuration/parsing/?tab=filter#matcher-and-filter).


expression [_required_]
string
Arithmetic operation between one or more log attributes.
is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.
name
string
Name of the processor.
target [_required_]
string
Name of the attribute that contains the result of the arithmetic operation.
type [_required_]
enum
Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`
default: `arithmetic-processor`
Option 11
object
Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.
The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.
**Notes** :
  * The processor only accepts attributes with values or an array of values in the blocks.
  * If an attribute cannot be used (object or array of object), it is replaced by an empty string or the entire operation is skipped depending on your selection.
  * If the target attribute already exists, it is overwritten by the result of the template.
  * Results of the template cannot exceed 256 characters.


is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.
name
string
Name of the processor.
target [_required_]
string
The name of the attribute that contains the result of the template.
template [_required_]
string
A formula with one or more attributes and raw text.
type [_required_]
enum
Type of logs string builder processor. Allowed enum values: `string-builder-processor`
default: `string-builder-processor`
Option 12
object
Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.
A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.
filter
object
Filter for logs.
query
string
The filter query.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
processors
[object]
Ordered list of processors in this pipeline.
type [_required_]
enum
Type of logs pipeline processor. Allowed enum values: `pipeline`
default: `pipeline`
Option 13
object
The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `network.client.ip`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `network.client.geoip`
type [_required_]
enum
Type of GeoIP parser. Allowed enum values: `geo-ip-parser`
default: `geo-ip-parser`
Option 14
object
Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
default_lookup
string
Value to set the target attribute if the source value is not found in the list.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_table [_required_]
[string]
Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 15
object
**Note** : Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_enrichment_table [_required_]
string
Name of the Reference Table for the source attribute and their associated target attribute values.
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 16
object
There are two ways to improve correlation between application traces and logs.
  1. Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.
  2. Use the Trace remapper processor to define a log attribute as its associated trace ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.trace_id`
type [_required_]
enum
Type of logs trace remapper. Allowed enum values: `trace-id-remapper`
default: `trace-id-remapper`
Option 17
object
There are two ways to define correlation between application spans and logs:
  1. Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default.
  2. Use the span remapper processor to define a log attribute as its associated span ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.span_id`
type [_required_]
enum
Type of logs span remapper. Allowed enum values: `span-id-remapper`
default: `span-id-remapper`
Option 18
object
A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:
  * Select value from matching element
  * Compute array length
  * Append a value to an array


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
operation [_required_]
<oneOf>
Configuration of the array processor operation to perform.
Option 1
object
Operation that appends a value to a target array attribute.
preserve_source
boolean
Remove or preserve the remapped source element.
default: `true`
source [_required_]
string
Attribute path containing the value to append.
target [_required_]
string
Attribute path of the array to append to.
type [_required_]
enum
Operation type. Allowed enum values: `append`
Option 2
object
Operation that computes the length of a `source` array and stores the result in the `target` attribute.
source [_required_]
string
Attribute path of the array to measure.
target [_required_]
string
Attribute that receives the computed length.
type [_required_]
enum
Operation type. Allowed enum values: `length`
Option 3
object
Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.
filter [_required_]
string
Filter condition expressed as `key:value` used to find the matching element.
source [_required_]
string
Attribute path of the array to search into.
target [_required_]
string
Attribute that receives the extracted value.
type [_required_]
enum
Operation type. Allowed enum values: `select`
value_to_extract [_required_]
string
Key of the value to extract from the matching element.
type [_required_]
enum
Type of logs array processor. Allowed enum values: `array-processor`
default: `array-processor`
Option 19
object
The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.
binary_to_text_encoding [_required_]
enum
The encoding used to represent the binary data. Allowed enum values: `base64,base16`
input_representation [_required_]
enum
The original representation of input string. Allowed enum values: `utf_8,integer`
is_enabled
boolean
Whether the processor is enabled.
name
string
Name of the processor.
source [_required_]
string
Name of the log attribute with the encoded data.
target [_required_]
string
Name of the log attribute that contains the decoded data.
type [_required_]
enum
Type of logs decoder processor. Allowed enum values: `decoder-processor`
default: `decoder-processor`
Option 20
object
A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.
is_enabled
boolean
Whether or not the processor is enabled.
mappers [_required_]
[ <oneOf>]
The `LogsSchemaProcessor` `mappers`.
Option 1
object
The schema remapper maps source log fields to their correct fields.
name [_required_]
string
Name of the logs schema remapper.
override_on_conflict
boolean
Override or not the target element if already set.
preserve_source
boolean
Remove or preserve the remapped source element.
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Target field to map log source field to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
type [_required_]
enum
Type of logs schema remapper. Allowed enum values: `schema-remapper`
Option 2
object
Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Categories are executed in order and processing stops at the first match. Make sure categories are properly ordered in case a log could match multiple queries.
  * Sibling fields always have a numerical ID field and a human-readable string name.
  * A fallback section handles cases where the name or ID value matches a specific value. If the name matches "Other" or the ID matches 99, the value of the sibling name field will be pulled from a source field from the original log.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
id [_required_]
int64
ID to inject into the category.
name [_required_]
string
Value to assign to target schema field.
fallback
object
Used to override hardcoded category values with a value pulled from a source attribute on the log.
sources
object
Fallback sources used to populate value of field.
<any-key>
[string]
values
object
Values that define when the fallback is used.
<any-key>
string
name [_required_]
string
Name of the logs schema category mapper.
targets [_required_]
object
Name of the target attributes which value is defined by the matching category.
id
string
ID of the field to map log attributes to.
name
string
Name of the field to map log attributes to.
type [_required_]
enum
Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`
name [_required_]
string
Name of the processor.
schema [_required_]
object
Configuration of the schema data to use.
class_name [_required_]
string
Class name of the schema to use.
class_uid [_required_]
int64
Class UID of the schema to use.
profiles
[string]
Optional list of profiles to modify the schema.
schema_type [_required_]
string
Type of schema to use.
version [_required_]
string
Version of the schema to use.
type [_required_]
enum
Type of logs schema processor. Allowed enum values: `schema-processor`
default: `schema-processor`
tags
[string]
A list of tags associated with the pipeline.
type
string
Type of pipeline.
```
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Response returned by the Logs API when errors occur.
Field
Type
Description
error
object
Error returned by the Logs API
code
string
Code identifying the error
details
[object]
Additional error details
message
string
Error message
```
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=typescript)


#####  Create a pipeline with Array Processor Append Operation returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppend",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_to_array",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps"
      }
    }
  ],
  "tags": []
}
EOF  

                        
```

#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendNoPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_remove_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": false
      }
    }
  ],
  "tags": []
}
EOF  

                        
```

#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_keep_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": true
      }
    }
  ],
  "tags": []
}
EOF  

                        
```

#####  Create a pipeline with Array Processor Append Operation returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation returns "OK" response

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
	body := datadogV1.LogsPipeline{
		Filter: &datadogV1.LogsFilter{
			Query: datadog.PtrString("source:python"),
		},
		Name: "testPipelineArrayAppend",
		Processors: []datadogV1.LogsProcessor{
			datadogV1.LogsProcessor{
				LogsArrayProcessor: &datadogV1.LogsArrayProcessor{
					Type:      datadogV1.LOGSARRAYPROCESSORTYPE_ARRAY_PROCESSOR,
					IsEnabled: datadog.PtrBool(true),
					Name:      datadog.PtrString("append_ip_to_array"),
					Operation: datadogV1.LogsArrayProcessorOperation{
						LogsArrayProcessorOperationAppend: &datadogV1.LogsArrayProcessorOperationAppend{
							Type:   datadogV1.LOGSARRAYPROCESSOROPERATIONAPPENDTYPE_APPEND,
							Source: "network.client.ip",
							Target: "sourceIps",
						}},
				}},
		},
		Tags: []string{},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.CreateLogsPipeline(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.CreateLogsPipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.CreateLogsPipeline`:\n%s\n", responseContent)
}

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response

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
	body := datadogV1.LogsPipeline{
		Filter: &datadogV1.LogsFilter{
			Query: datadog.PtrString("source:python"),
		},
		Name: "testPipelineArrayAppendNoPreserve",
		Processors: []datadogV1.LogsProcessor{
			datadogV1.LogsProcessor{
				LogsArrayProcessor: &datadogV1.LogsArrayProcessor{
					Type:      datadogV1.LOGSARRAYPROCESSORTYPE_ARRAY_PROCESSOR,
					IsEnabled: datadog.PtrBool(true),
					Name:      datadog.PtrString("append_ip_and_remove_source"),
					Operation: datadogV1.LogsArrayProcessorOperation{
						LogsArrayProcessorOperationAppend: &datadogV1.LogsArrayProcessorOperationAppend{
							Type:           datadogV1.LOGSARRAYPROCESSOROPERATIONAPPENDTYPE_APPEND,
							Source:         "network.client.ip",
							Target:         "sourceIps",
							PreserveSource: datadog.PtrBool(false),
						}},
				}},
		},
		Tags: []string{},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.CreateLogsPipeline(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.CreateLogsPipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.CreateLogsPipeline`:\n%s\n", responseContent)
}

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response

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
	body := datadogV1.LogsPipeline{
		Filter: &datadogV1.LogsFilter{
			Query: datadog.PtrString("source:python"),
		},
		Name: "testPipelineArrayAppendPreserve",
		Processors: []datadogV1.LogsProcessor{
			datadogV1.LogsProcessor{
				LogsArrayProcessor: &datadogV1.LogsArrayProcessor{
					Type:      datadogV1.LOGSARRAYPROCESSORTYPE_ARRAY_PROCESSOR,
					IsEnabled: datadog.PtrBool(true),
					Name:      datadog.PtrString("append_ip_and_keep_source"),
					Operation: datadogV1.LogsArrayProcessorOperation{
						LogsArrayProcessorOperationAppend: &datadogV1.LogsArrayProcessorOperationAppend{
							Type:           datadogV1.LOGSARRAYPROCESSOROPERATIONAPPENDTYPE_APPEND,
							Source:         "network.client.ip",
							Target:         "sourceIps",
							PreserveSource: datadog.PtrBool(true),
						}},
				}},
		},
		Tags: []string{},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.CreateLogsPipeline(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.CreateLogsPipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.CreateLogsPipeline`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a pipeline with Array Processor Append Operation returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsArrayProcessor;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperation;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppend;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppendType;
import com.datadog.api.client.v1.model.LogsArrayProcessorType;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("testPipelineArrayAppend")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsArrayProcessor()
                            .type(LogsArrayProcessorType.ARRAY_PROCESSOR)
                            .isEnabled(true)
                            .name("append_ip_to_array")
                            .operation(
                                new LogsArrayProcessorOperation(
                                    new LogsArrayProcessorOperationAppend()
                                        .type(LogsArrayProcessorOperationAppendType.APPEND)
                                        .source("network.client.ip")
                                        .target("sourceIps"))))));

    try {
      LogsPipeline result = apiInstance.createLogsPipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#createLogsPipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK"
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsArrayProcessor;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperation;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppend;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppendType;
import com.datadog.api.client.v1.model.LogsArrayProcessorType;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("testPipelineArrayAppendNoPreserve")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsArrayProcessor()
                            .type(LogsArrayProcessorType.ARRAY_PROCESSOR)
                            .isEnabled(true)
                            .name("append_ip_and_remove_source")
                            .operation(
                                new LogsArrayProcessorOperation(
                                    new LogsArrayProcessorOperationAppend()
                                        .type(LogsArrayProcessorOperationAppendType.APPEND)
                                        .source("network.client.ip")
                                        .target("sourceIps")
                                        .preserveSource(false))))));

    try {
      LogsPipeline result = apiInstance.createLogsPipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#createLogsPipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK"
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsArrayProcessor;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperation;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppend;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppendType;
import com.datadog.api.client.v1.model.LogsArrayProcessorType;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("testPipelineArrayAppendPreserve")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsArrayProcessor()
                            .type(LogsArrayProcessorType.ARRAY_PROCESSOR)
                            .isEnabled(true)
                            .name("append_ip_and_keep_source")
                            .operation(
                                new LogsArrayProcessorOperation(
                                    new LogsArrayProcessorOperationAppend()
                                        .type(LogsArrayProcessorOperationAppendType.APPEND)
                                        .source("network.client.ip")
                                        .target("sourceIps")
                                        .preserveSource(true))))));

    try {
      LogsPipeline result = apiInstance.createLogsPipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#createLogsPipeline");
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

#####  Create a pipeline with Array Processor Append Operation returns "OK" response 
```
"""
Create a pipeline with Array Processor Append Operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
from datadog_api_client.v1.model.logs_array_processor_operation_append_type import LogsArrayProcessorOperationAppendType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayAppend",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="append_ip_to_array",
            operation=LogsArrayProcessorOperationAppend(
                type=LogsArrayProcessorOperationAppendType.APPEND,
                source="network.client.ip",
                target="sourceIps",
            ),
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response 
```
"""
Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
from datadog_api_client.v1.model.logs_array_processor_operation_append_type import LogsArrayProcessorOperationAppendType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayAppendNoPreserve",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="append_ip_and_remove_source",
            operation=LogsArrayProcessorOperationAppend(
                type=LogsArrayProcessorOperationAppendType.APPEND,
                source="network.client.ip",
                target="sourceIps",
                preserve_source=False,
            ),
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response 
```
"""
Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
from datadog_api_client.v1.model.logs_array_processor_operation_append_type import LogsArrayProcessorOperationAppendType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayAppendPreserve",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="append_ip_and_keep_source",
            operation=LogsArrayProcessorOperationAppend(
                type=LogsArrayProcessorOperationAppendType.APPEND,
                source="network.client.ip",
                target="sourceIps",
                preserve_source=True,
            ),
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a pipeline with Array Processor Append Operation returns "OK" response 
```
# Create a pipeline with Array Processor Append Operation returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "testPipelineArrayAppend",
  processors: [
    DatadogAPIClient::V1::LogsArrayProcessor.new({
      type: DatadogAPIClient::V1::LogsArrayProcessorType::ARRAY_PROCESSOR,
      is_enabled: true,
      name: "append_ip_to_array",
      operation: DatadogAPIClient::V1::LogsArrayProcessorOperationAppend.new({
        type: DatadogAPIClient::V1::LogsArrayProcessorOperationAppendType::APPEND,
        source: "network.client.ip",
        target: "sourceIps",
      }),
    }),
  ],
  tags: [],
})
p api_instance.create_logs_pipeline(body)

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response 
```
# Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "testPipelineArrayAppendNoPreserve",
  processors: [
    DatadogAPIClient::V1::LogsArrayProcessor.new({
      type: DatadogAPIClient::V1::LogsArrayProcessorType::ARRAY_PROCESSOR,
      is_enabled: true,
      name: "append_ip_and_remove_source",
      operation: DatadogAPIClient::V1::LogsArrayProcessorOperationAppend.new({
        type: DatadogAPIClient::V1::LogsArrayProcessorOperationAppendType::APPEND,
        source: "network.client.ip",
        target: "sourceIps",
        preserve_source: false,
      }),
    }),
  ],
  tags: [],
})
p api_instance.create_logs_pipeline(body)

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response 
```
# Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "testPipelineArrayAppendPreserve",
  processors: [
    DatadogAPIClient::V1::LogsArrayProcessor.new({
      type: DatadogAPIClient::V1::LogsArrayProcessorType::ARRAY_PROCESSOR,
      is_enabled: true,
      name: "append_ip_and_keep_source",
      operation: DatadogAPIClient::V1::LogsArrayProcessorOperationAppend.new({
        type: DatadogAPIClient::V1::LogsArrayProcessorOperationAppendType::APPEND,
        source: "network.client.ip",
        target: "sourceIps",
        preserve_source: true,
      }),
    }),
  ],
  tags: [],
})
p api_instance.create_logs_pipeline(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a pipeline with Array Processor Append Operation returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsArrayProcessor;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperation;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppend;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppendType;
use datadog_api_client::datadogV1::model::LogsArrayProcessorType;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("testPipelineArrayAppend".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsArrayProcessor(Box::new(
            LogsArrayProcessor::new(
                LogsArrayProcessorOperation::LogsArrayProcessorOperationAppend(Box::new(
                    LogsArrayProcessorOperationAppend::new(
                        "network.client.ip".to_string(),
                        "sourceIps".to_string(),
                        LogsArrayProcessorOperationAppendType::APPEND,
                    ),
                )),
                LogsArrayProcessorType::ARRAY_PROCESSOR,
            )
            .is_enabled(true)
            .name("append_ip_to_array".to_string()),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.create_logs_pipeline(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation with preserve_source
// false returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsArrayProcessor;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperation;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppend;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppendType;
use datadog_api_client::datadogV1::model::LogsArrayProcessorType;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("testPipelineArrayAppendNoPreserve".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsArrayProcessor(Box::new(
            LogsArrayProcessor::new(
                LogsArrayProcessorOperation::LogsArrayProcessorOperationAppend(Box::new(
                    LogsArrayProcessorOperationAppend::new(
                        "network.client.ip".to_string(),
                        "sourceIps".to_string(),
                        LogsArrayProcessorOperationAppendType::APPEND,
                    )
                    .preserve_source(false),
                )),
                LogsArrayProcessorType::ARRAY_PROCESSOR,
            )
            .is_enabled(true)
            .name("append_ip_and_remove_source".to_string()),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.create_logs_pipeline(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response 
```
// Create a pipeline with Array Processor Append Operation with preserve_source
// true returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsArrayProcessor;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperation;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppend;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppendType;
use datadog_api_client::datadogV1::model::LogsArrayProcessorType;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("testPipelineArrayAppendPreserve".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsArrayProcessor(Box::new(
            LogsArrayProcessor::new(
                LogsArrayProcessorOperation::LogsArrayProcessorOperationAppend(Box::new(
                    LogsArrayProcessorOperationAppend::new(
                        "network.client.ip".to_string(),
                        "sourceIps".to_string(),
                        LogsArrayProcessorOperationAppendType::APPEND,
                    )
                    .preserve_source(true),
                )),
                LogsArrayProcessorType::ARRAY_PROCESSOR,
            )
            .is_enabled(true)
            .name("append_ip_and_keep_source".to_string()),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.create_logs_pipeline(body).await;
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

#####  Create a pipeline with Array Processor Append Operation returns "OK" response 
```
/**
 * Create a pipeline with Array Processor Append Operation returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiCreateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "testPipelineArrayAppend",
    processors: [
      {
        type: "array-processor",
        isEnabled: true,
        name: "append_ip_to_array",
        operation: {
          type: "append",
          source: "network.client.ip",
          target: "sourceIps",
        },
      },
    ],
    tags: [],
  },
};

apiInstance
  .createLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response 
```
/**
 * Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiCreateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "testPipelineArrayAppendNoPreserve",
    processors: [
      {
        type: "array-processor",
        isEnabled: true,
        name: "append_ip_and_remove_source",
        operation: {
          type: "append",
          source: "network.client.ip",
          target: "sourceIps",
          preserveSource: false,
        },
      },
    ],
    tags: [],
  },
};

apiInstance
  .createLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response 
```
/**
 * Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiCreateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "testPipelineArrayAppendPreserve",
    processors: [
      {
        type: "array-processor",
        isEnabled: true,
        name: "append_ip_and_keep_source",
        operation: {
          type: "append",
          source: "network.client.ip",
          target: "sourceIps",
          preserveSource: true,
        },
      },
    ],
    tags: [],
  },
};

apiInstance
  .createLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
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
## [Get a pipeline](https://docs.datadoghq.com/api/latest/logs-pipelines/#get-a-pipeline)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-pipelines/#get-a-pipeline-v1)


GET https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.datadoghq.eu/api/v1/logs/config/pipelines/{pipeline_id}https://api.ddog-gov.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.us3.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}
### Overview
Get a specific pipeline from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
pipeline_id [_required_]
string
ID of the pipeline to get.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-pipelines/#GetLogsPipeline-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-pipelines/#GetLogsPipeline-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-pipelines/#GetLogsPipeline-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-pipelines/#GetLogsPipeline-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.
**Note** : These endpoints are only available for admin users. Make sure to use an application key created by an admin.
Field
Type
Description
description
string
A description of the pipeline.
filter
object
Filter for logs.
query
string
The filter query.
id
string
ID of the pipeline.
is_enabled
boolean
Whether or not the pipeline is enabled.
is_read_only
boolean
Whether or not the pipeline can be edited.
name [_required_]
string
Name of the pipeline.
processors
[ <oneOf>]
Ordered list of processors in this pipeline.
Option 1
object
Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).
grok [_required_]
object
Set of rules for the grok parser.
match_rules [_required_]
string
List of match rules for the grok parser, separated by a new line.
support_rules
string
List of support rules for the grok parser, separated by a new line.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
samples
[string]
List of sample logs to test this grok parser.
source [_required_]
string
Name of the log attribute to parse.
default: `message`
type [_required_]
enum
Type of logs grok parser. Allowed enum values: `grok-parser`
default: `grok-parser`
Option 2
object
As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.
  * `timestamp`
  * `date`
  * `_timestamp`
  * `Timestamp`
  * `eventTime`
  * `published_date`
If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164.


**Note:** If your logs don’t contain any of the default attributes and you haven’t defined your own date attribute, Datadog timestamps the logs with the date it received them.
If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs date remapper. Allowed enum values: `date-remapper`
default: `date-remapper`
Option 3
object
Use this Processor if you want to assign some attributes as the official status.
Each incoming status value is mapped as follows.
  * Integers from 0 to 7 map to the Syslog severity standards
  * Strings beginning with `emerg` or f (case-insensitive) map to `emerg` (0)
  * Strings beginning with `a` (case-insensitive) map to `alert` (1)
  * Strings beginning with `c` (case-insensitive) map to `critical` (2)
  * Strings beginning with `err` (case-insensitive) map to `error` (3)
  * Strings beginning with `w` (case-insensitive) map to `warning` (4)
  * Strings beginning with `n` (case-insensitive) map to `notice` (5)
  * Strings beginning with `i` (case-insensitive) map to `info` (6)
  * Strings beginning with `d`, `trace` or `verbose` (case-insensitive) map to `debug` (7)
  * Strings beginning with `o` or matching `OK` or `Success` (case-insensitive) map to OK
  * All others map to `info` (6)


**Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs status remapper. Allowed enum values: `status-remapper`
default: `status-remapper`
Option 4
object
Use this processor if you want to assign one or more attributes as the official service.
**Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs service remapper. Allowed enum values: `service-remapper`
default: `service-remapper`
Option 5
object
The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.
**Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `msg`
type [_required_]
enum
Type of logs message remapper. Allowed enum values: `message-remapper`
default: `message-remapper`
Option 6
object
The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
override_on_conflict
boolean
Override or not the target element if already set,
preserve_source
boolean
Remove or preserve the remapped source element.
source_type
string
Defines if the sources are from log `attribute` or `tag`.
default: `attribute`
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Final attribute or tag name to remap the sources to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
target_type
string
Defines if the final attribute or tag name is from log `attribute` or `tag`.
default: `attribute`
type [_required_]
enum
Type of logs attribute remapper. Allowed enum values: `attribute-remapper`
default: `attribute-remapper`
Option 7
object
This processor extracts query parameters and other important parameters from a URL.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
normalize_ending_slashes
boolean
Normalize the ending slashes or not.
sources [_required_]
[string]
Array of source attributes.
default: `http.url`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.url_details`
type [_required_]
enum
Type of logs URL parser. Allowed enum values: `url-parser`
default: `url-parser`
Option 8
object
The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.
is_enabled
boolean
Whether or not the processor is enabled.
is_encoded
boolean
Define if the source attribute is URL encoded or not.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `http.useragent`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.useragent_details`
type [_required_]
enum
Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`
default: `user-agent-parser`
Option 9
object
Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Once the log has matched one of the Processor queries, it stops. Make sure they are properly ordered in case a log could match several queries.
  * The names of the categories must be unique.
  * Once defined in the Category Processor, you can map categories to log status using the Log Status Remapper.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter
object
Filter for logs.
query
string
The filter query.
name
string
Value to assign to the target attribute.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
target [_required_]
string
Name of the target attribute which value is defined by the matching category.
type [_required_]
enum
Type of logs category processor. Allowed enum values: `category-processor`
default: `category-processor`
Option 10
object
Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.
The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.
By default, the calculation is skipped if an attribute is missing. Select “Replace missing attribute by 0” to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number.
_Notes_ :
  * The operator `-` needs to be space split in the formula as it can also be contained in attribute names.
  * If the target attribute already exists, it is overwritten by the result of the formula.
  * Results are rounded up to the 9th decimal. For example, if the result of the formula is `0.1234567891`, the actual value stored for the attribute is `0.123456789`.
  * If you need to scale a unit of measure, see [Scale Filter](https://docs.datadoghq.com/logs/log_configuration/parsing/?tab=filter#matcher-and-filter).


expression [_required_]
string
Arithmetic operation between one or more log attributes.
is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.
name
string
Name of the processor.
target [_required_]
string
Name of the attribute that contains the result of the arithmetic operation.
type [_required_]
enum
Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`
default: `arithmetic-processor`
Option 11
object
Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.
The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.
**Notes** :
  * The processor only accepts attributes with values or an array of values in the blocks.
  * If an attribute cannot be used (object or array of object), it is replaced by an empty string or the entire operation is skipped depending on your selection.
  * If the target attribute already exists, it is overwritten by the result of the template.
  * Results of the template cannot exceed 256 characters.


is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.
name
string
Name of the processor.
target [_required_]
string
The name of the attribute that contains the result of the template.
template [_required_]
string
A formula with one or more attributes and raw text.
type [_required_]
enum
Type of logs string builder processor. Allowed enum values: `string-builder-processor`
default: `string-builder-processor`
Option 12
object
Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.
A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.
filter
object
Filter for logs.
query
string
The filter query.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
processors
[object]
Ordered list of processors in this pipeline.
type [_required_]
enum
Type of logs pipeline processor. Allowed enum values: `pipeline`
default: `pipeline`
Option 13
object
The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `network.client.ip`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `network.client.geoip`
type [_required_]
enum
Type of GeoIP parser. Allowed enum values: `geo-ip-parser`
default: `geo-ip-parser`
Option 14
object
Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
default_lookup
string
Value to set the target attribute if the source value is not found in the list.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_table [_required_]
[string]
Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 15
object
**Note** : Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_enrichment_table [_required_]
string
Name of the Reference Table for the source attribute and their associated target attribute values.
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 16
object
There are two ways to improve correlation between application traces and logs.
  1. Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.
  2. Use the Trace remapper processor to define a log attribute as its associated trace ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.trace_id`
type [_required_]
enum
Type of logs trace remapper. Allowed enum values: `trace-id-remapper`
default: `trace-id-remapper`
Option 17
object
There are two ways to define correlation between application spans and logs:
  1. Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default.
  2. Use the span remapper processor to define a log attribute as its associated span ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.span_id`
type [_required_]
enum
Type of logs span remapper. Allowed enum values: `span-id-remapper`
default: `span-id-remapper`
Option 18
object
A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:
  * Select value from matching element
  * Compute array length
  * Append a value to an array


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
operation [_required_]
<oneOf>
Configuration of the array processor operation to perform.
Option 1
object
Operation that appends a value to a target array attribute.
preserve_source
boolean
Remove or preserve the remapped source element.
default: `true`
source [_required_]
string
Attribute path containing the value to append.
target [_required_]
string
Attribute path of the array to append to.
type [_required_]
enum
Operation type. Allowed enum values: `append`
Option 2
object
Operation that computes the length of a `source` array and stores the result in the `target` attribute.
source [_required_]
string
Attribute path of the array to measure.
target [_required_]
string
Attribute that receives the computed length.
type [_required_]
enum
Operation type. Allowed enum values: `length`
Option 3
object
Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.
filter [_required_]
string
Filter condition expressed as `key:value` used to find the matching element.
source [_required_]
string
Attribute path of the array to search into.
target [_required_]
string
Attribute that receives the extracted value.
type [_required_]
enum
Operation type. Allowed enum values: `select`
value_to_extract [_required_]
string
Key of the value to extract from the matching element.
type [_required_]
enum
Type of logs array processor. Allowed enum values: `array-processor`
default: `array-processor`
Option 19
object
The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.
binary_to_text_encoding [_required_]
enum
The encoding used to represent the binary data. Allowed enum values: `base64,base16`
input_representation [_required_]
enum
The original representation of input string. Allowed enum values: `utf_8,integer`
is_enabled
boolean
Whether the processor is enabled.
name
string
Name of the processor.
source [_required_]
string
Name of the log attribute with the encoded data.
target [_required_]
string
Name of the log attribute that contains the decoded data.
type [_required_]
enum
Type of logs decoder processor. Allowed enum values: `decoder-processor`
default: `decoder-processor`
Option 20
object
A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.
is_enabled
boolean
Whether or not the processor is enabled.
mappers [_required_]
[ <oneOf>]
The `LogsSchemaProcessor` `mappers`.
Option 1
object
The schema remapper maps source log fields to their correct fields.
name [_required_]
string
Name of the logs schema remapper.
override_on_conflict
boolean
Override or not the target element if already set.
preserve_source
boolean
Remove or preserve the remapped source element.
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Target field to map log source field to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
type [_required_]
enum
Type of logs schema remapper. Allowed enum values: `schema-remapper`
Option 2
object
Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Categories are executed in order and processing stops at the first match. Make sure categories are properly ordered in case a log could match multiple queries.
  * Sibling fields always have a numerical ID field and a human-readable string name.
  * A fallback section handles cases where the name or ID value matches a specific value. If the name matches "Other" or the ID matches 99, the value of the sibling name field will be pulled from a source field from the original log.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
id [_required_]
int64
ID to inject into the category.
name [_required_]
string
Value to assign to target schema field.
fallback
object
Used to override hardcoded category values with a value pulled from a source attribute on the log.
sources
object
Fallback sources used to populate value of field.
<any-key>
[string]
values
object
Values that define when the fallback is used.
<any-key>
string
name [_required_]
string
Name of the logs schema category mapper.
targets [_required_]
object
Name of the target attributes which value is defined by the matching category.
id
string
ID of the field to map log attributes to.
name
string
Name of the field to map log attributes to.
type [_required_]
enum
Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`
name [_required_]
string
Name of the processor.
schema [_required_]
object
Configuration of the schema data to use.
class_name [_required_]
string
Class name of the schema to use.
class_uid [_required_]
int64
Class UID of the schema to use.
profiles
[string]
Optional list of profiles to modify the schema.
schema_type [_required_]
string
Type of schema to use.
version [_required_]
string
Version of the schema to use.
type [_required_]
enum
Type of logs schema processor. Allowed enum values: `schema-processor`
default: `schema-processor`
tags
[string]
A list of tags associated with the pipeline.
type
string
Type of pipeline.
```
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Response returned by the Logs API when errors occur.
Field
Type
Description
error
object
Error returned by the Logs API
code
string
Code identifying the error
details
[object]
Additional error details
message
string
Error message
```
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=typescript)


#####  Get a pipeline
Copy
```
                  # Path parameters  
export pipeline_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a pipeline
```
"""
Get a pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.get_logs_pipeline(
        pipeline_id="pipeline_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a pipeline
```
# Get a pipeline returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.get_logs_pipeline("pipeline_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a pipeline
```
// Get a pipeline returns "OK" response

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
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.GetLogsPipeline(ctx, "pipeline_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.GetLogsPipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.GetLogsPipeline`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a pipeline
```
// Get a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipeline;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      LogsPipeline result = apiInstance.getLogsPipeline("pipeline_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#getLogsPipeline");
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

#####  Get a pipeline
```
// Get a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.get_logs_pipeline("pipeline_id".to_string()).await;
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

#####  Get a pipeline
```
/**
 * Get a pipeline returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiGetLogsPipelineRequest = {
  pipelineId: "pipeline_id",
};

apiInstance
  .getLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
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
## [Delete a pipeline](https://docs.datadoghq.com/api/latest/logs-pipelines/#delete-a-pipeline)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-pipelines/#delete-a-pipeline-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.datadoghq.eu/api/v1/logs/config/pipelines/{pipeline_id}https://api.ddog-gov.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.us3.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}
### Overview
Delete a given pipeline from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_write_pipelines` permission.
### Arguments
#### Path Parameters
Name
Type
Description
pipeline_id [_required_]
string
ID of the pipeline to delete.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-pipelines/#DeleteLogsPipeline-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-pipelines/#DeleteLogsPipeline-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-pipelines/#DeleteLogsPipeline-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-pipelines/#DeleteLogsPipeline-429-v1)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Response returned by the Logs API when errors occur.
Field
Type
Description
error
object
Error returned by the Logs API
code
string
Code identifying the error
details
[object]
Additional error details
message
string
Error message
```
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=typescript)


#####  Delete a pipeline
Copy
```
                  # Path parameters  
export pipeline_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a pipeline
```
"""
Delete a pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    api_instance.delete_logs_pipeline(
        pipeline_id="pipeline_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a pipeline
```
# Delete a pipeline returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.delete_logs_pipeline("pipeline_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a pipeline
```
// Delete a pipeline returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	r, err := api.DeleteLogsPipeline(ctx, "pipeline_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.DeleteLogsPipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a pipeline
```
// Delete a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      apiInstance.deleteLogsPipeline("pipeline_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#deleteLogsPipeline");
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

#####  Delete a pipeline
```
// Delete a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.delete_logs_pipeline("pipeline_id".to_string()).await;
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

#####  Delete a pipeline
```
/**
 * Delete a pipeline returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiDeleteLogsPipelineRequest = {
  pipelineId: "pipeline_id",
};

apiInstance
  .deleteLogsPipeline(params)
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
## [Update a pipeline](https://docs.datadoghq.com/api/latest/logs-pipelines/#update-a-pipeline)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-pipelines/#update-a-pipeline-v1)


PUT https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.datadoghq.eu/api/v1/logs/config/pipelines/{pipeline_id}https://api.ddog-gov.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.us3.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}
### Overview
Update a given pipeline configuration to change it’s processors or their order.
**Note** : Using this method updates your pipeline configuration by **replacing** your current configuration with the new one sent to your Datadog organization.
This endpoint requires the `logs_write_pipelines` permission.
### Arguments
#### Path Parameters
Name
Type
Description
pipeline_id [_required_]
string
ID of the pipeline to delete.
### Request
#### Body Data (required)
New definition of the pipeline.
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Field
Type
Description
description
string
A description of the pipeline.
filter
object
Filter for logs.
query
string
The filter query.
id
string
ID of the pipeline.
is_enabled
boolean
Whether or not the pipeline is enabled.
is_read_only
boolean
Whether or not the pipeline can be edited.
name [_required_]
string
Name of the pipeline.
processors
[ <oneOf>]
Ordered list of processors in this pipeline.
Option 1
object
Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).
grok [_required_]
object
Set of rules for the grok parser.
match_rules [_required_]
string
List of match rules for the grok parser, separated by a new line.
support_rules
string
List of support rules for the grok parser, separated by a new line.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
samples
[string]
List of sample logs to test this grok parser.
source [_required_]
string
Name of the log attribute to parse.
default: `message`
type [_required_]
enum
Type of logs grok parser. Allowed enum values: `grok-parser`
default: `grok-parser`
Option 2
object
As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.
  * `timestamp`
  * `date`
  * `_timestamp`
  * `Timestamp`
  * `eventTime`
  * `published_date`
If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164.


**Note:** If your logs don’t contain any of the default attributes and you haven’t defined your own date attribute, Datadog timestamps the logs with the date it received them.
If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs date remapper. Allowed enum values: `date-remapper`
default: `date-remapper`
Option 3
object
Use this Processor if you want to assign some attributes as the official status.
Each incoming status value is mapped as follows.
  * Integers from 0 to 7 map to the Syslog severity standards
  * Strings beginning with `emerg` or f (case-insensitive) map to `emerg` (0)
  * Strings beginning with `a` (case-insensitive) map to `alert` (1)
  * Strings beginning with `c` (case-insensitive) map to `critical` (2)
  * Strings beginning with `err` (case-insensitive) map to `error` (3)
  * Strings beginning with `w` (case-insensitive) map to `warning` (4)
  * Strings beginning with `n` (case-insensitive) map to `notice` (5)
  * Strings beginning with `i` (case-insensitive) map to `info` (6)
  * Strings beginning with `d`, `trace` or `verbose` (case-insensitive) map to `debug` (7)
  * Strings beginning with `o` or matching `OK` or `Success` (case-insensitive) map to OK
  * All others map to `info` (6)


**Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs status remapper. Allowed enum values: `status-remapper`
default: `status-remapper`
Option 4
object
Use this processor if you want to assign one or more attributes as the official service.
**Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs service remapper. Allowed enum values: `service-remapper`
default: `service-remapper`
Option 5
object
The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.
**Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `msg`
type [_required_]
enum
Type of logs message remapper. Allowed enum values: `message-remapper`
default: `message-remapper`
Option 6
object
The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
override_on_conflict
boolean
Override or not the target element if already set,
preserve_source
boolean
Remove or preserve the remapped source element.
source_type
string
Defines if the sources are from log `attribute` or `tag`.
default: `attribute`
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Final attribute or tag name to remap the sources to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
target_type
string
Defines if the final attribute or tag name is from log `attribute` or `tag`.
default: `attribute`
type [_required_]
enum
Type of logs attribute remapper. Allowed enum values: `attribute-remapper`
default: `attribute-remapper`
Option 7
object
This processor extracts query parameters and other important parameters from a URL.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
normalize_ending_slashes
boolean
Normalize the ending slashes or not.
sources [_required_]
[string]
Array of source attributes.
default: `http.url`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.url_details`
type [_required_]
enum
Type of logs URL parser. Allowed enum values: `url-parser`
default: `url-parser`
Option 8
object
The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.
is_enabled
boolean
Whether or not the processor is enabled.
is_encoded
boolean
Define if the source attribute is URL encoded or not.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `http.useragent`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.useragent_details`
type [_required_]
enum
Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`
default: `user-agent-parser`
Option 9
object
Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Once the log has matched one of the Processor queries, it stops. Make sure they are properly ordered in case a log could match several queries.
  * The names of the categories must be unique.
  * Once defined in the Category Processor, you can map categories to log status using the Log Status Remapper.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter
object
Filter for logs.
query
string
The filter query.
name
string
Value to assign to the target attribute.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
target [_required_]
string
Name of the target attribute which value is defined by the matching category.
type [_required_]
enum
Type of logs category processor. Allowed enum values: `category-processor`
default: `category-processor`
Option 10
object
Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.
The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.
By default, the calculation is skipped if an attribute is missing. Select “Replace missing attribute by 0” to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number.
_Notes_ :
  * The operator `-` needs to be space split in the formula as it can also be contained in attribute names.
  * If the target attribute already exists, it is overwritten by the result of the formula.
  * Results are rounded up to the 9th decimal. For example, if the result of the formula is `0.1234567891`, the actual value stored for the attribute is `0.123456789`.
  * If you need to scale a unit of measure, see [Scale Filter](https://docs.datadoghq.com/logs/log_configuration/parsing/?tab=filter#matcher-and-filter).


expression [_required_]
string
Arithmetic operation between one or more log attributes.
is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.
name
string
Name of the processor.
target [_required_]
string
Name of the attribute that contains the result of the arithmetic operation.
type [_required_]
enum
Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`
default: `arithmetic-processor`
Option 11
object
Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.
The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.
**Notes** :
  * The processor only accepts attributes with values or an array of values in the blocks.
  * If an attribute cannot be used (object or array of object), it is replaced by an empty string or the entire operation is skipped depending on your selection.
  * If the target attribute already exists, it is overwritten by the result of the template.
  * Results of the template cannot exceed 256 characters.


is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.
name
string
Name of the processor.
target [_required_]
string
The name of the attribute that contains the result of the template.
template [_required_]
string
A formula with one or more attributes and raw text.
type [_required_]
enum
Type of logs string builder processor. Allowed enum values: `string-builder-processor`
default: `string-builder-processor`
Option 12
object
Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.
A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.
filter
object
Filter for logs.
query
string
The filter query.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
processors
[object]
Ordered list of processors in this pipeline.
type [_required_]
enum
Type of logs pipeline processor. Allowed enum values: `pipeline`
default: `pipeline`
Option 13
object
The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `network.client.ip`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `network.client.geoip`
type [_required_]
enum
Type of GeoIP parser. Allowed enum values: `geo-ip-parser`
default: `geo-ip-parser`
Option 14
object
Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
default_lookup
string
Value to set the target attribute if the source value is not found in the list.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_table [_required_]
[string]
Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 15
object
**Note** : Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_enrichment_table [_required_]
string
Name of the Reference Table for the source attribute and their associated target attribute values.
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 16
object
There are two ways to improve correlation between application traces and logs.
  1. Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.
  2. Use the Trace remapper processor to define a log attribute as its associated trace ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.trace_id`
type [_required_]
enum
Type of logs trace remapper. Allowed enum values: `trace-id-remapper`
default: `trace-id-remapper`
Option 17
object
There are two ways to define correlation between application spans and logs:
  1. Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default.
  2. Use the span remapper processor to define a log attribute as its associated span ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.span_id`
type [_required_]
enum
Type of logs span remapper. Allowed enum values: `span-id-remapper`
default: `span-id-remapper`
Option 18
object
A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:
  * Select value from matching element
  * Compute array length
  * Append a value to an array


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
operation [_required_]
<oneOf>
Configuration of the array processor operation to perform.
Option 1
object
Operation that appends a value to a target array attribute.
preserve_source
boolean
Remove or preserve the remapped source element.
default: `true`
source [_required_]
string
Attribute path containing the value to append.
target [_required_]
string
Attribute path of the array to append to.
type [_required_]
enum
Operation type. Allowed enum values: `append`
Option 2
object
Operation that computes the length of a `source` array and stores the result in the `target` attribute.
source [_required_]
string
Attribute path of the array to measure.
target [_required_]
string
Attribute that receives the computed length.
type [_required_]
enum
Operation type. Allowed enum values: `length`
Option 3
object
Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.
filter [_required_]
string
Filter condition expressed as `key:value` used to find the matching element.
source [_required_]
string
Attribute path of the array to search into.
target [_required_]
string
Attribute that receives the extracted value.
type [_required_]
enum
Operation type. Allowed enum values: `select`
value_to_extract [_required_]
string
Key of the value to extract from the matching element.
type [_required_]
enum
Type of logs array processor. Allowed enum values: `array-processor`
default: `array-processor`
Option 19
object
The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.
binary_to_text_encoding [_required_]
enum
The encoding used to represent the binary data. Allowed enum values: `base64,base16`
input_representation [_required_]
enum
The original representation of input string. Allowed enum values: `utf_8,integer`
is_enabled
boolean
Whether the processor is enabled.
name
string
Name of the processor.
source [_required_]
string
Name of the log attribute with the encoded data.
target [_required_]
string
Name of the log attribute that contains the decoded data.
type [_required_]
enum
Type of logs decoder processor. Allowed enum values: `decoder-processor`
default: `decoder-processor`
Option 20
object
A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.
is_enabled
boolean
Whether or not the processor is enabled.
mappers [_required_]
[ <oneOf>]
The `LogsSchemaProcessor` `mappers`.
Option 1
object
The schema remapper maps source log fields to their correct fields.
name [_required_]
string
Name of the logs schema remapper.
override_on_conflict
boolean
Override or not the target element if already set.
preserve_source
boolean
Remove or preserve the remapped source element.
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Target field to map log source field to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
type [_required_]
enum
Type of logs schema remapper. Allowed enum values: `schema-remapper`
Option 2
object
Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Categories are executed in order and processing stops at the first match. Make sure categories are properly ordered in case a log could match multiple queries.
  * Sibling fields always have a numerical ID field and a human-readable string name.
  * A fallback section handles cases where the name or ID value matches a specific value. If the name matches "Other" or the ID matches 99, the value of the sibling name field will be pulled from a source field from the original log.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
id [_required_]
int64
ID to inject into the category.
name [_required_]
string
Value to assign to target schema field.
fallback
object
Used to override hardcoded category values with a value pulled from a source attribute on the log.
sources
object
Fallback sources used to populate value of field.
<any-key>
[string]
values
object
Values that define when the fallback is used.
<any-key>
string
name [_required_]
string
Name of the logs schema category mapper.
targets [_required_]
object
Name of the target attributes which value is defined by the matching category.
id
string
ID of the field to map log attributes to.
name
string
Name of the field to map log attributes to.
type [_required_]
enum
Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`
name [_required_]
string
Name of the processor.
schema [_required_]
object
Configuration of the schema data to use.
class_name [_required_]
string
Class name of the schema to use.
class_uid [_required_]
int64
Class UID of the schema to use.
profiles
[string]
Optional list of profiles to modify the schema.
schema_type [_required_]
string
Type of schema to use.
version [_required_]
string
Version of the schema to use.
type [_required_]
enum
Type of logs schema processor. Allowed enum values: `schema-processor`
default: `schema-processor`
tags
[string]
A list of tags associated with the pipeline.
type
string
Type of pipeline.
```
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "is_enabled": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": []
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipeline-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipeline-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipeline-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-pipelines/#UpdateLogsPipeline-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.
**Note** : These endpoints are only available for admin users. Make sure to use an application key created by an admin.
Field
Type
Description
description
string
A description of the pipeline.
filter
object
Filter for logs.
query
string
The filter query.
id
string
ID of the pipeline.
is_enabled
boolean
Whether or not the pipeline is enabled.
is_read_only
boolean
Whether or not the pipeline can be edited.
name [_required_]
string
Name of the pipeline.
processors
[ <oneOf>]
Ordered list of processors in this pipeline.
Option 1
object
Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).
grok [_required_]
object
Set of rules for the grok parser.
match_rules [_required_]
string
List of match rules for the grok parser, separated by a new line.
support_rules
string
List of support rules for the grok parser, separated by a new line.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
samples
[string]
List of sample logs to test this grok parser.
source [_required_]
string
Name of the log attribute to parse.
default: `message`
type [_required_]
enum
Type of logs grok parser. Allowed enum values: `grok-parser`
default: `grok-parser`
Option 2
object
As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.
  * `timestamp`
  * `date`
  * `_timestamp`
  * `Timestamp`
  * `eventTime`
  * `published_date`
If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164.


**Note:** If your logs don’t contain any of the default attributes and you haven’t defined your own date attribute, Datadog timestamps the logs with the date it received them.
If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs date remapper. Allowed enum values: `date-remapper`
default: `date-remapper`
Option 3
object
Use this Processor if you want to assign some attributes as the official status.
Each incoming status value is mapped as follows.
  * Integers from 0 to 7 map to the Syslog severity standards
  * Strings beginning with `emerg` or f (case-insensitive) map to `emerg` (0)
  * Strings beginning with `a` (case-insensitive) map to `alert` (1)
  * Strings beginning with `c` (case-insensitive) map to `critical` (2)
  * Strings beginning with `err` (case-insensitive) map to `error` (3)
  * Strings beginning with `w` (case-insensitive) map to `warning` (4)
  * Strings beginning with `n` (case-insensitive) map to `notice` (5)
  * Strings beginning with `i` (case-insensitive) map to `info` (6)
  * Strings beginning with `d`, `trace` or `verbose` (case-insensitive) map to `debug` (7)
  * Strings beginning with `o` or matching `OK` or `Success` (case-insensitive) map to OK
  * All others map to `info` (6)


**Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs status remapper. Allowed enum values: `status-remapper`
default: `status-remapper`
Option 4
object
Use this processor if you want to assign one or more attributes as the official service.
**Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
type [_required_]
enum
Type of logs service remapper. Allowed enum values: `service-remapper`
default: `service-remapper`
Option 5
object
The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.
**Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `msg`
type [_required_]
enum
Type of logs message remapper. Allowed enum values: `message-remapper`
default: `message-remapper`
Option 6
object
The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
override_on_conflict
boolean
Override or not the target element if already set,
preserve_source
boolean
Remove or preserve the remapped source element.
source_type
string
Defines if the sources are from log `attribute` or `tag`.
default: `attribute`
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Final attribute or tag name to remap the sources to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
target_type
string
Defines if the final attribute or tag name is from log `attribute` or `tag`.
default: `attribute`
type [_required_]
enum
Type of logs attribute remapper. Allowed enum values: `attribute-remapper`
default: `attribute-remapper`
Option 7
object
This processor extracts query parameters and other important parameters from a URL.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
normalize_ending_slashes
boolean
Normalize the ending slashes or not.
sources [_required_]
[string]
Array of source attributes.
default: `http.url`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.url_details`
type [_required_]
enum
Type of logs URL parser. Allowed enum values: `url-parser`
default: `url-parser`
Option 8
object
The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.
is_enabled
boolean
Whether or not the processor is enabled.
is_encoded
boolean
Define if the source attribute is URL encoded or not.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `http.useragent`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `http.useragent_details`
type [_required_]
enum
Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`
default: `user-agent-parser`
Option 9
object
Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Once the log has matched one of the Processor queries, it stops. Make sure they are properly ordered in case a log could match several queries.
  * The names of the categories must be unique.
  * Once defined in the Category Processor, you can map categories to log status using the Log Status Remapper.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter
object
Filter for logs.
query
string
The filter query.
name
string
Value to assign to the target attribute.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
target [_required_]
string
Name of the target attribute which value is defined by the matching category.
type [_required_]
enum
Type of logs category processor. Allowed enum values: `category-processor`
default: `category-processor`
Option 10
object
Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.
The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.
By default, the calculation is skipped if an attribute is missing. Select “Replace missing attribute by 0” to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number.
_Notes_ :
  * The operator `-` needs to be space split in the formula as it can also be contained in attribute names.
  * If the target attribute already exists, it is overwritten by the result of the formula.
  * Results are rounded up to the 9th decimal. For example, if the result of the formula is `0.1234567891`, the actual value stored for the attribute is `0.123456789`.
  * If you need to scale a unit of measure, see [Scale Filter](https://docs.datadoghq.com/logs/log_configuration/parsing/?tab=filter#matcher-and-filter).


expression [_required_]
string
Arithmetic operation between one or more log attributes.
is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.
name
string
Name of the processor.
target [_required_]
string
Name of the attribute that contains the result of the arithmetic operation.
type [_required_]
enum
Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`
default: `arithmetic-processor`
Option 11
object
Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.
The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.
**Notes** :
  * The processor only accepts attributes with values or an array of values in the blocks.
  * If an attribute cannot be used (object or array of object), it is replaced by an empty string or the entire operation is skipped depending on your selection.
  * If the target attribute already exists, it is overwritten by the result of the template.
  * Results of the template cannot exceed 256 characters.


is_enabled
boolean
Whether or not the processor is enabled.
is_replace_missing
boolean
If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.
name
string
Name of the processor.
target [_required_]
string
The name of the attribute that contains the result of the template.
template [_required_]
string
A formula with one or more attributes and raw text.
type [_required_]
enum
Type of logs string builder processor. Allowed enum values: `string-builder-processor`
default: `string-builder-processor`
Option 12
object
Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.
A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.
filter
object
Filter for logs.
query
string
The filter query.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
processors
[object]
Ordered list of processors in this pipeline.
type [_required_]
enum
Type of logs pipeline processor. Allowed enum values: `pipeline`
default: `pipeline`
Option 13
object
The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.
is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources [_required_]
[string]
Array of source attributes.
default: `network.client.ip`
target [_required_]
string
Name of the parent attribute that contains all the extracted details from the `sources`.
default: `network.client.geoip`
type [_required_]
enum
Type of GeoIP parser. Allowed enum values: `geo-ip-parser`
default: `geo-ip-parser`
Option 14
object
Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
default_lookup
string
Value to set the target attribute if the source value is not found in the list.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_table [_required_]
[string]
Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 15
object
**Note** : Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.
is_enabled
boolean
Whether or not the processor is enabled.
lookup_enrichment_table [_required_]
string
Name of the Reference Table for the source attribute and their associated target attribute values.
name
string
Name of the processor.
source [_required_]
string
Source attribute used to perform the lookup.
target [_required_]
string
Name of the attribute that contains the corresponding value in the mapping list.
type [_required_]
enum
Type of logs lookup processor. Allowed enum values: `lookup-processor`
default: `lookup-processor`
Option 16
object
There are two ways to improve correlation between application traces and logs.
  1. Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.
  2. Use the Trace remapper processor to define a log attribute as its associated trace ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.trace_id`
type [_required_]
enum
Type of logs trace remapper. Allowed enum values: `trace-id-remapper`
default: `trace-id-remapper`
Option 17
object
There are two ways to define correlation between application spans and logs:
  1. Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default.
  2. Use the span remapper processor to define a log attribute as its associated span ID.


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
sources
[string]
Array of source attributes.
default: `dd.span_id`
type [_required_]
enum
Type of logs span remapper. Allowed enum values: `span-id-remapper`
default: `span-id-remapper`
Option 18
object
A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:
  * Select value from matching element
  * Compute array length
  * Append a value to an array


is_enabled
boolean
Whether or not the processor is enabled.
name
string
Name of the processor.
operation [_required_]
<oneOf>
Configuration of the array processor operation to perform.
Option 1
object
Operation that appends a value to a target array attribute.
preserve_source
boolean
Remove or preserve the remapped source element.
default: `true`
source [_required_]
string
Attribute path containing the value to append.
target [_required_]
string
Attribute path of the array to append to.
type [_required_]
enum
Operation type. Allowed enum values: `append`
Option 2
object
Operation that computes the length of a `source` array and stores the result in the `target` attribute.
source [_required_]
string
Attribute path of the array to measure.
target [_required_]
string
Attribute that receives the computed length.
type [_required_]
enum
Operation type. Allowed enum values: `length`
Option 3
object
Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.
filter [_required_]
string
Filter condition expressed as `key:value` used to find the matching element.
source [_required_]
string
Attribute path of the array to search into.
target [_required_]
string
Attribute that receives the extracted value.
type [_required_]
enum
Operation type. Allowed enum values: `select`
value_to_extract [_required_]
string
Key of the value to extract from the matching element.
type [_required_]
enum
Type of logs array processor. Allowed enum values: `array-processor`
default: `array-processor`
Option 19
object
The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.
binary_to_text_encoding [_required_]
enum
The encoding used to represent the binary data. Allowed enum values: `base64,base16`
input_representation [_required_]
enum
The original representation of input string. Allowed enum values: `utf_8,integer`
is_enabled
boolean
Whether the processor is enabled.
name
string
Name of the processor.
source [_required_]
string
Name of the log attribute with the encoded data.
target [_required_]
string
Name of the log attribute that contains the decoded data.
type [_required_]
enum
Type of logs decoder processor. Allowed enum values: `decoder-processor`
default: `decoder-processor`
Option 20
object
A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.
is_enabled
boolean
Whether or not the processor is enabled.
mappers [_required_]
[ <oneOf>]
The `LogsSchemaProcessor` `mappers`.
Option 1
object
The schema remapper maps source log fields to their correct fields.
name [_required_]
string
Name of the logs schema remapper.
override_on_conflict
boolean
Override or not the target element if already set.
preserve_source
boolean
Remove or preserve the remapped source element.
sources [_required_]
[string]
Array of source attributes.
target [_required_]
string
Target field to map log source field to.
target_format
enum
If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`
type [_required_]
enum
Type of logs schema remapper. Allowed enum values: `schema-remapper`
Option 2
object
Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.
**Notes** :
  * The syntax of the query is the one of Logs Explorer search bar. The query can be done on any log attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
  * Categories are executed in order and processing stops at the first match. Make sure categories are properly ordered in case a log could match multiple queries.
  * Sibling fields always have a numerical ID field and a human-readable string name.
  * A fallback section handles cases where the name or ID value matches a specific value. If the name matches "Other" or the ID matches 99, the value of the sibling name field will be pulled from a source field from the original log.


categories [_required_]
[object]
Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
id [_required_]
int64
ID to inject into the category.
name [_required_]
string
Value to assign to target schema field.
fallback
object
Used to override hardcoded category values with a value pulled from a source attribute on the log.
sources
object
Fallback sources used to populate value of field.
<any-key>
[string]
values
object
Values that define when the fallback is used.
<any-key>
string
name [_required_]
string
Name of the logs schema category mapper.
targets [_required_]
object
Name of the target attributes which value is defined by the matching category.
id
string
ID of the field to map log attributes to.
name
string
Name of the field to map log attributes to.
type [_required_]
enum
Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`
name [_required_]
string
Name of the processor.
schema [_required_]
object
Configuration of the schema data to use.
class_name [_required_]
string
Class name of the schema to use.
class_uid [_required_]
int64
Class UID of the schema to use.
profiles
[string]
Optional list of profiles to modify the schema.
schema_type [_required_]
string
Type of schema to use.
version [_required_]
string
Version of the schema to use.
type [_required_]
enum
Type of logs schema processor. Allowed enum values: `schema-processor`
default: `schema-processor`
tags
[string]
A list of tags associated with the pipeline.
type
string
Type of pipeline.
```
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


Response returned by the Logs API when errors occur.
Field
Type
Description
error
object
Error returned by the Logs API
code
string
Code identifying the error
details
[object]
Additional error details
message
string
Error message
```
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-pipelines/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-pipelines/?code-lang=typescript)


#####  Update a pipeline
Copy
```
                  # Path parameters  
export pipeline_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar"
      }
    }
  ]
}
EOF  

                
```

#####  Update a pipeline
```
"""
Update a pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_grok_parser import LogsGrokParser
from datadog_api_client.v1.model.logs_grok_parser_rules import LogsGrokParserRules
from datadog_api_client.v1.model.logs_grok_parser_type import LogsGrokParserType
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="",
    processors=[
        LogsGrokParser(
            grok=LogsGrokParserRules(
                match_rules="rule_name_1 foo\nrule_name_2 bar",
                support_rules="rule_name_1 foo\nrule_name_2 bar",
            ),
            is_enabled=False,
            samples=[],
            source="message",
            type=LogsGrokParserType.GROK_PARSER,
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.update_logs_pipeline(pipeline_id="pipeline_id", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a pipeline
```
# Update a pipeline returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "",
  processors: [
    DatadogAPIClient::V1::LogsGrokParser.new({
      grok: DatadogAPIClient::V1::LogsGrokParserRules.new({
        match_rules: 'rule_name_1 foo\nrule_name_2 bar',
        support_rules: 'rule_name_1 foo\nrule_name_2 bar',
      }),
      is_enabled: false,
      samples: [],
      source: "message",
      type: DatadogAPIClient::V1::LogsGrokParserType::GROK_PARSER,
    }),
  ],
  tags: [],
})
p api_instance.update_logs_pipeline("pipeline_id", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a pipeline
```
// Update a pipeline returns "OK" response

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
	body := datadogV1.LogsPipeline{
		Filter: &datadogV1.LogsFilter{
			Query: datadog.PtrString("source:python"),
		},
		Name: "",
		Processors: []datadogV1.LogsProcessor{
			datadogV1.LogsProcessor{
				LogsGrokParser: &datadogV1.LogsGrokParser{
					Grok: datadogV1.LogsGrokParserRules{
						MatchRules: `rule_name_1 foo
rule_name_2 bar`,
						SupportRules: datadog.PtrString(`rule_name_1 foo
rule_name_2 bar`),
					},
					IsEnabled: datadog.PtrBool(false),
					Samples:   []string{},
					Source:    "message",
					Type:      datadogV1.LOGSGROKPARSERTYPE_GROK_PARSER,
				}},
		},
		Tags: []string{},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsPipelinesApi(apiClient)
	resp, r, err := api.UpdateLogsPipeline(ctx, "pipeline_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.UpdateLogsPipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.UpdateLogsPipeline`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a pipeline
```
// Update a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsGrokParser;
import com.datadog.api.client.v1.model.LogsGrokParserRules;
import com.datadog.api.client.v1.model.LogsGrokParserType;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsGrokParser()
                            .grok(
                                new LogsGrokParserRules()
                                    .matchRules("""
rule_name_1 foo
rule_name_2 bar
""")
                                    .supportRules("""
rule_name_1 foo
rule_name_2 bar
"""))
                            .isEnabled(false)
                            .source("message")
                            .type(LogsGrokParserType.GROK_PARSER))));

    try {
      LogsPipeline result = apiInstance.updateLogsPipeline("pipeline_id", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#updateLogsPipeline");
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

#####  Update a pipeline
```
// Update a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsGrokParser;
use datadog_api_client::datadogV1::model::LogsGrokParserRules;
use datadog_api_client::datadogV1::model::LogsGrokParserType;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsGrokParser(Box::new(
            LogsGrokParser::new(
                LogsGrokParserRules::new(
                    r#"rule_name_1 foo
rule_name_2 bar"#
                        .to_string(),
                )
                .support_rules(
                    r#"rule_name_1 foo
rule_name_2 bar"#
                        .to_string(),
                ),
                "message".to_string(),
                LogsGrokParserType::GROK_PARSER,
            )
            .is_enabled(false)
            .samples(vec![]),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api
        .update_logs_pipeline("pipeline_id".to_string(), body)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a pipeline
```
/**
 * Update a pipeline returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiUpdateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "",
    processors: [
      {
        grok: {
          matchRules: "rule_name_1 foo\nrule_name_2 bar",
          supportRules: "rule_name_1 foo\nrule_name_2 bar",
        },
        isEnabled: false,
        samples: [],
        source: "message",
        type: "grok-parser",
      },
    ],
    tags: [],
  },
  pipelineId: "pipeline_id",
};

apiInstance
  .updateLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ab6484ce-3d71-4972-8884-d04755f4ed8e&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=55e66d20-2363-41f7-8b7d-c0af9054772c&pt=Logs%20Pipelines&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-pipelines%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ab6484ce-3d71-4972-8884-d04755f4ed8e&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=55e66d20-2363-41f7-8b7d-c0af9054772c&pt=Logs%20Pipelines&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-pipelines%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=03e60368-05b4-42a5-b3c4-50e98f5d61d9&bo=2&sid=ca97aff0f0bf11f0b225ebe7018368cd&vid=ca980060f0bf11f09385b797b877861f&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Logs%20Pipelines&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-pipelines%2F&r=&lt=2659&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=348194)
