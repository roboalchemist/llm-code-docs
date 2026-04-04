# Source: https://docs.datadoghq.com/api/latest/processes/

# Processes
The processes API allows you to query processes data for your organization. See the [Live Processes page](https://docs.datadoghq.com/infrastructure/process/) for more information.
## [Get all processes](https://docs.datadoghq.com/api/latest/processes/#get-all-processes)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/processes/#get-all-processes-v2)


GET https://api.ap1.datadoghq.com/api/v2/processeshttps://api.ap2.datadoghq.com/api/v2/processeshttps://api.datadoghq.eu/api/v2/processeshttps://api.ddog-gov.com/api/v2/processeshttps://api.datadoghq.com/api/v2/processeshttps://api.us3.datadoghq.com/api/v2/processeshttps://api.us5.datadoghq.com/api/v2/processes
### Overview
Get all processes for your organization.
### Arguments
#### Query Strings
Name
Type
Description
search
string
String to search processes by.
tags
string
Comma-separated list of tags to filter processes by.
from
integer
Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window will be 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`.
to
integer
Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window will be 15 minutes after the `from` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`.
page[limit]
integer
Maximum number of results returned.
page[cursor]
string
String to query the next page of results. This key is provided with each valid response from the API in `meta.page.after`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/processes/#ListProcesses-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/processes/#ListProcesses-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/processes/#ListProcesses-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/processes/#ListProcesses-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/processes/)
  * [Example](https://docs.datadoghq.com/api/latest/processes/)


List of process summaries.
Field
Type
Description
data
[object]
Array of process summary objects.
attributes
object
Attributes for a process summary.
cmdline
string
Process command line.
host
string
Host running the process.
pid
int64
Process ID.
ppid
int64
Parent process ID.
start
string
Time the process was started.
tags
[string]
List of tags associated with the process.
timestamp
string
Time the process was seen.
user
string
Process owner.
id
string
Process ID.
type
enum
Type of process summary. Allowed enum values: `process`
default: `process`
meta
object
Response metadata object.
page
object
Paging attributes.
after
string
The cursor used to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.
size
int32
Number of results returned.
```
{
  "data": [
    {
      "attributes": {
        "cmdline": "string",
        "host": "string",
        "pid": "integer",
        "ppid": "integer",
        "start": "string",
        "tags": [],
        "timestamp": "string",
        "user": "string"
      },
      "id": "string",
      "type": "process"
    }
  ],
  "meta": {
    "page": {
      "after": "911abf1204838d9cdfcb9a96d0b6a1bd03e1b514074f1ce1737c4cbd",
      "size": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/processes/)
  * [Example](https://docs.datadoghq.com/api/latest/processes/)


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
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/processes/)
  * [Example](https://docs.datadoghq.com/api/latest/processes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/processes/)
  * [Example](https://docs.datadoghq.com/api/latest/processes/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/processes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/processes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/processes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/processes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/processes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/processes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/processes/?code-lang=typescript)


#####  Get all processes
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/processes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all processes
```
"""
Get all processes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.processes_api import ProcessesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProcessesApi(api_client)
    response = api_instance.list_processes(
        search="process-agent",
        tags="testing:true",
        page_limit=2,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all processes
```
# Get all processes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ProcessesAPI.new
opts = {
  search: "process-agent",
  tags: "testing:true",
  page_limit: 2,
}
p api_instance.list_processes(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all processes
```
// Get all processes returns "OK" response

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
	api := datadogV2.NewProcessesApi(apiClient)
	resp, r, err := api.ListProcesses(ctx, *datadogV2.NewListProcessesOptionalParameters().WithSearch("process-agent").WithTags("testing:true").WithPageLimit(2))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProcessesApi.ListProcesses`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ProcessesApi.ListProcesses`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all processes
```
// Get all processes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ProcessesApi;
import com.datadog.api.client.v2.api.ProcessesApi.ListProcessesOptionalParameters;
import com.datadog.api.client.v2.model.ProcessSummariesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ProcessesApi apiInstance = new ProcessesApi(defaultClient);

    try {
      ProcessSummariesResponse result =
          apiInstance.listProcesses(
              new ListProcessesOptionalParameters()
                  .search("process-agent")
                  .tags("testing:true")
                  .pageLimit(2));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessesApi#listProcesses");
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

#####  Get all processes
```
// Get all processes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_processes::ListProcessesOptionalParams;
use datadog_api_client::datadogV2::api_processes::ProcessesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ProcessesAPI::with_config(configuration);
    let resp = api
        .list_processes(
            ListProcessesOptionalParams::default()
                .search("process-agent".to_string())
                .tags("testing:true".to_string())
                .page_limit(2),
        )
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

#####  Get all processes
```
/**
 * Get all processes returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ProcessesApi(configuration);

const params: v2.ProcessesApiListProcessesRequest = {
  search: "process-agent",
  tags: "testing:true",
  pageLimit: 2,
};

apiInstance
  .listProcesses(params)
  .then((data: v2.ProcessSummariesResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=962d7f9b-9bbd-44b9-8333-d229f395a4ae&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=47203e82-0f90-4661-893e-9ec06e20fc4a&pt=Processes&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fprocesses%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=962d7f9b-9bbd-44b9-8333-d229f395a4ae&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=47203e82-0f90-4661-893e-9ec06e20fc4a&pt=Processes&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fprocesses%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=84667f64-130d-4b52-ba90-303d62662c97&bo=2&sid=b77a5fe0f0bf11f0bab0291dd4b5f9fd&vid=b77a7130f0bf11f0b69eb7008fe8e23b&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Processes&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fprocesses%2F&r=&lt=834&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=141152)
