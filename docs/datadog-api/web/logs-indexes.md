# Source: https://docs.datadoghq.com/api/latest/logs-indexes/

# Logs Indexes
Manage configuration of [log indexes](https://docs.datadoghq.com/logs/indexes/).
## [Get all indexes](https://docs.datadoghq.com/api/latest/logs-indexes/#get-all-indexes)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-indexes/#get-all-indexes-v1)


GET https://api.ap1.datadoghq.com/api/v1/logs/config/indexeshttps://api.ap2.datadoghq.com/api/v1/logs/config/indexeshttps://api.datadoghq.eu/api/v1/logs/config/indexeshttps://api.ddog-gov.com/api/v1/logs/config/indexeshttps://api.datadoghq.com/api/v1/logs/config/indexeshttps://api.us3.datadoghq.com/api/v1/logs/config/indexeshttps://api.us5.datadoghq.com/api/v1/logs/config/indexes
### Overview
The Index object describes the configuration of a log index. This endpoint returns an array of the `LogIndex` objects of your organization. This endpoint requires the `logs_read_config` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-indexes/#ListLogIndexes-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-indexes/#ListLogIndexes-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-indexes/#ListLogIndexes-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Object with all Index configurations for a given organization.
Field
Type
Description
indexes
[object]
Array of Log index configurations.
daily_limit
int64
The number of log events you can send in this index per day before you are rate-limited.
daily_limit_reset
object
Object containing options to override the default daily limit reset time.
reset_time
string
String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).
reset_utc_offset
string
String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).
daily_limit_warning_threshold_percentage
double
A percentage threshold of the daily quota at which a Datadog warning event is generated.
exclusion_filters
[object]
An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.
filter
object
Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.
query
string
Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.
sample_rate [_required_]
double
Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.
is_enabled
boolean
Whether or not the exclusion filter is active.
name [_required_]
string
Name of the index exclusion filter.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
is_rate_limited
boolean
A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.
name [_required_]
string
The name of the index.
num_flex_logs_retention_days
int64
The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions.
num_retention_days
int64
The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.
```
{
  "indexes": [
    {
      "daily_limit": 300000000,
      "daily_limit_reset": {
        "reset_time": "14:00",
        "reset_utc_offset": "+02:00"
      },
      "daily_limit_warning_threshold_percentage": 70,
      "exclusion_filters": [
        {
          "filter": {
            "query": "*",
            "sample_rate": 1
          },
          "is_enabled": false,
          "name": "payment"
        }
      ],
      "filter": {
        "query": "source:python"
      },
      "is_rate_limited": false,
      "name": "main",
      "num_flex_logs_retention_days": 360,
      "num_retention_days": 15
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=typescript)


#####  Get all indexes
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all indexes
```
"""
Get all indexes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.list_log_indexes()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all indexes
```
# Get all indexes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.list_log_indexes()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all indexes
```
// Get all indexes returns "OK" response

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
	api := datadogV1.NewLogsIndexesApi(apiClient)
	resp, r, err := api.ListLogIndexes(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.ListLogIndexes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.ListLogIndexes`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all indexes
```
// Get all indexes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndexListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      LogsIndexListResponse result = apiInstance.listLogIndexes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#listLogIndexes");
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

#####  Get all indexes
```
// Get all indexes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.list_log_indexes().await;
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

#####  Get all indexes
```
/**
 * Get all indexes returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

apiInstance
  .listLogIndexes()
  .then((data: v1.LogsIndexListResponse) => {
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
## [Get an index](https://docs.datadoghq.com/api/latest/logs-indexes/#get-an-index)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-indexes/#get-an-index-v1)


GET https://api.ap1.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.ap2.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.datadoghq.eu/api/v1/logs/config/indexes/{name}https://api.ddog-gov.com/api/v1/logs/config/indexes/{name}https://api.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.us3.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.us5.datadoghq.com/api/v1/logs/config/indexes/{name}
### Overview
Get one log index from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
name [_required_]
string
Name of the log index.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-indexes/#GetLogsIndex-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-indexes/#GetLogsIndex-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/logs-indexes/#GetLogsIndex-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-indexes/#GetLogsIndex-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Object describing a Datadog Log index.
Field
Type
Description
daily_limit
int64
The number of log events you can send in this index per day before you are rate-limited.
daily_limit_reset
object
Object containing options to override the default daily limit reset time.
reset_time
string
String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).
reset_utc_offset
string
String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).
daily_limit_warning_threshold_percentage
double
A percentage threshold of the daily quota at which a Datadog warning event is generated.
exclusion_filters
[object]
An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.
filter
object
Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.
query
string
Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.
sample_rate [_required_]
double
Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.
is_enabled
boolean
Whether or not the exclusion filter is active.
name [_required_]
string
Name of the index exclusion filter.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
is_rate_limited
boolean
A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.
name [_required_]
string
The name of the index.
num_flex_logs_retention_days
int64
The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions.
num_retention_days
int64
The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.
```
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "is_rate_limited": false,
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=typescript)


#####  Get an index
Copy
```
                  # Path parameters  
export name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes/${name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an index
```
"""
Get an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.get_logs_index(
        name="name",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an index
```
# Get an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.get_logs_index("name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an index
```
// Get an index returns "OK" response

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
	api := datadogV1.NewLogsIndexesApi(apiClient)
	resp, r, err := api.GetLogsIndex(ctx, "name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.GetLogsIndex`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.GetLogsIndex`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an index
```
// Get an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndex;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      LogsIndex result = apiInstance.getLogsIndex("name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#getLogsIndex");
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

#####  Get an index
```
// Get an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.get_logs_index("name".to_string()).await;
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

#####  Get an index
```
/**
 * Get an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiGetLogsIndexRequest = {
  name: "name",
};

apiInstance
  .getLogsIndex(params)
  .then((data: v1.LogsIndex) => {
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
## [Create an index](https://docs.datadoghq.com/api/latest/logs-indexes/#create-an-index)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-indexes/#create-an-index-v1)


POST https://api.ap1.datadoghq.com/api/v1/logs/config/indexeshttps://api.ap2.datadoghq.com/api/v1/logs/config/indexeshttps://api.datadoghq.eu/api/v1/logs/config/indexeshttps://api.ddog-gov.com/api/v1/logs/config/indexeshttps://api.datadoghq.com/api/v1/logs/config/indexeshttps://api.us3.datadoghq.com/api/v1/logs/config/indexeshttps://api.us5.datadoghq.com/api/v1/logs/config/indexes
### Overview
Creates a new index. Returns the Index object passed in the request body when the request is successful. This endpoint requires the `logs_modify_indexes` permission.
### Request
#### Body Data (required)
Object containing the new index.
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Field
Type
Description
daily_limit
int64
The number of log events you can send in this index per day before you are rate-limited.
daily_limit_reset
object
Object containing options to override the default daily limit reset time.
reset_time
string
String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).
reset_utc_offset
string
String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).
daily_limit_warning_threshold_percentage
double
A percentage threshold of the daily quota at which a Datadog warning event is generated.
exclusion_filters
[object]
An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.
filter
object
Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.
query
string
Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.
sample_rate [_required_]
double
Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.
is_enabled
boolean
Whether or not the exclusion filter is active.
name [_required_]
string
Name of the index exclusion filter.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
is_rate_limited
boolean
A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.
name [_required_]
string
The name of the index.
num_flex_logs_retention_days
int64
The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions.
num_retention_days
int64
The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.
```
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-indexes/#CreateLogsIndex-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-indexes/#CreateLogsIndex-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-indexes/#CreateLogsIndex-403-v1)
  * [422](https://docs.datadoghq.com/api/latest/logs-indexes/#CreateLogsIndex-422-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-indexes/#CreateLogsIndex-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Object describing a Datadog Log index.
Field
Type
Description
daily_limit
int64
The number of log events you can send in this index per day before you are rate-limited.
daily_limit_reset
object
Object containing options to override the default daily limit reset time.
reset_time
string
String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).
reset_utc_offset
string
String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).
daily_limit_warning_threshold_percentage
double
A percentage threshold of the daily quota at which a Datadog warning event is generated.
exclusion_filters
[object]
An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.
filter
object
Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.
query
string
Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.
sample_rate [_required_]
double
Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.
is_enabled
boolean
Whether or not the exclusion filter is active.
name [_required_]
string
Name of the index exclusion filter.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
is_rate_limited
boolean
A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.
name [_required_]
string
The name of the index.
num_flex_logs_retention_days
int64
The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions.
num_retention_days
int64
The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.
```
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "is_rate_limited": false,
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15
}
```

Copy
Invalid Parameter Error
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Response returned by the Logs API when the max limit has been reached.
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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=typescript)


#####  Create an index
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "exclusion_filters": [
    {
      "filter": {
        "sample_rate": 1
      },
      "name": "payment"
    }
  ],
  "filter": {},
  "name": "main"
}
EOF  

                
```

#####  Create an index
```
"""
Create an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_daily_limit_reset import LogsDailyLimitReset
from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
from datadog_api_client.v1.model.logs_exclusion_filter import LogsExclusionFilter
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_index import LogsIndex

body = LogsIndex(
    daily_limit=300000000,
    daily_limit_reset=LogsDailyLimitReset(
        reset_time="14:00",
        reset_utc_offset="+02:00",
    ),
    daily_limit_warning_threshold_percentage=70.0,
    exclusion_filters=[
        LogsExclusion(
            filter=LogsExclusionFilter(
                query="*",
                sample_rate=1.0,
            ),
            name="payment",
        ),
    ],
    filter=LogsFilter(
        query="source:python",
    ),
    name="main",
    num_flex_logs_retention_days=360,
    num_retention_days=15,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.create_logs_index(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an index
```
# Create an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new

body = DatadogAPIClient::V1::LogsIndex.new({
  daily_limit: 300000000,
  daily_limit_reset: DatadogAPIClient::V1::LogsDailyLimitReset.new({
    reset_time: "14:00",
    reset_utc_offset: "+02:00",
  }),
  daily_limit_warning_threshold_percentage: 70,
  exclusion_filters: [
    DatadogAPIClient::V1::LogsExclusion.new({
      filter: DatadogAPIClient::V1::LogsExclusionFilter.new({
        query: "*",
        sample_rate: 1.0,
      }),
      name: "payment",
    }),
  ],
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "main",
  num_flex_logs_retention_days: 360,
  num_retention_days: 15,
})
p api_instance.create_logs_index(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an index
```
// Create an index returns "OK" response

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
	body := datadogV1.LogsIndex{
		DailyLimit: datadog.PtrInt64(300000000),
		DailyLimitReset: &datadogV1.LogsDailyLimitReset{
			ResetTime:      datadog.PtrString("14:00"),
			ResetUtcOffset: datadog.PtrString("+02:00"),
		},
		DailyLimitWarningThresholdPercentage: datadog.PtrFloat64(70),
		ExclusionFilters: []datadogV1.LogsExclusion{
			{
				Filter: &datadogV1.LogsExclusionFilter{
					Query:      datadog.PtrString("*"),
					SampleRate: 1.0,
				},
				Name: "payment",
			},
		},
		Filter: datadogV1.LogsFilter{
			Query: datadog.PtrString("source:python"),
		},
		Name:                     "main",
		NumFlexLogsRetentionDays: datadog.PtrInt64(360),
		NumRetentionDays:         datadog.PtrInt64(15),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsIndexesApi(apiClient)
	resp, r, err := api.CreateLogsIndex(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.CreateLogsIndex`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.CreateLogsIndex`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an index
```
// Create an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsDailyLimitReset;
import com.datadog.api.client.v1.model.LogsExclusion;
import com.datadog.api.client.v1.model.LogsExclusionFilter;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsIndex;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    LogsIndex body =
        new LogsIndex()
            .dailyLimit(300000000L)
            .dailyLimitReset(new LogsDailyLimitReset().resetTime("14:00").resetUtcOffset("+02:00"))
            .dailyLimitWarningThresholdPercentage(70.0)
            .exclusionFilters(
                Collections.singletonList(
                    new LogsExclusion()
                        .filter(new LogsExclusionFilter().query("*").sampleRate(1.0))
                        .name("payment")))
            .filter(new LogsFilter().query("source:python"))
            .name("main")
            .numFlexLogsRetentionDays(360L)
            .numRetentionDays(15L);

    try {
      LogsIndex result = apiInstance.createLogsIndex(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#createLogsIndex");
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

#####  Create an index
```
// Create an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;
use datadog_api_client::datadogV1::model::LogsDailyLimitReset;
use datadog_api_client::datadogV1::model::LogsExclusion;
use datadog_api_client::datadogV1::model::LogsExclusionFilter;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsIndex;

#[tokio::main]
async fn main() {
    let body = LogsIndex::new(
        LogsFilter::new().query("source:python".to_string()),
        "main".to_string(),
    )
    .daily_limit(300000000)
    .daily_limit_reset(
        LogsDailyLimitReset::new()
            .reset_time("14:00".to_string())
            .reset_utc_offset("+02:00".to_string()),
    )
    .daily_limit_warning_threshold_percentage(70.0 as f64)
    .exclusion_filters(vec![LogsExclusion::new("payment".to_string())
        .filter(LogsExclusionFilter::new(1.0).query("*".to_string()))])
    .num_flex_logs_retention_days(360)
    .num_retention_days(15);
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.create_logs_index(body).await;
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

#####  Create an index
```
/**
 * Create an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiCreateLogsIndexRequest = {
  body: {
    dailyLimit: 300000000,
    dailyLimitReset: {
      resetTime: "14:00",
      resetUtcOffset: "+02:00",
    },
    dailyLimitWarningThresholdPercentage: 70,
    exclusionFilters: [
      {
        filter: {
          query: "*",
          sampleRate: 1.0,
        },
        name: "payment",
      },
    ],
    filter: {
      query: "source:python",
    },
    name: "main",
    numFlexLogsRetentionDays: 360,
    numRetentionDays: 15,
  },
};

apiInstance
  .createLogsIndex(params)
  .then((data: v1.LogsIndex) => {
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
## [Update an index](https://docs.datadoghq.com/api/latest/logs-indexes/#update-an-index)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-indexes/#update-an-index-v1)


PUT https://api.ap1.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.ap2.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.datadoghq.eu/api/v1/logs/config/indexes/{name}https://api.ddog-gov.com/api/v1/logs/config/indexes/{name}https://api.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.us3.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.us5.datadoghq.com/api/v1/logs/config/indexes/{name}
### Overview
Update an index as identified by its name. Returns the Index object passed in the request body when the request is successful.
Using the `PUT` method updates your index’s configuration by **replacing** your current configuration with the new one sent to your Datadog organization.
### Arguments
#### Path Parameters
Name
Type
Description
name [_required_]
string
Name of the log index.
### Request
#### Body Data (required)
Object containing the new `LogsIndexUpdateRequest`.
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Field
Type
Description
daily_limit
int64
The number of log events you can send in this index per day before you are rate-limited.
daily_limit_reset
object
Object containing options to override the default daily limit reset time.
reset_time
string
String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).
reset_utc_offset
string
String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).
daily_limit_warning_threshold_percentage
double
A percentage threshold of the daily quota at which a Datadog warning event is generated.
disable_daily_limit
boolean
If true, sets the `daily_limit` value to null and the index is not limited on a daily basis (any specified `daily_limit` value in the request is ignored). If false or omitted, the index's current `daily_limit` is maintained.
exclusion_filters
[object]
An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.
filter
object
Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.
query
string
Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.
sample_rate [_required_]
double
Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.
is_enabled
boolean
Whether or not the exclusion filter is active.
name [_required_]
string
Name of the index exclusion filter.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
num_flex_logs_retention_days
int64
The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions.
**Note** : Changing this value affects all logs already in this index. It may also affect billing.
num_retention_days
int64
The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.
**Note** : Changing this value affects all logs already in this index. It may also affect billing.
```
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "disable_daily_limit": false,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndex-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndex-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndex-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndex-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Object describing a Datadog Log index.
Field
Type
Description
daily_limit
int64
The number of log events you can send in this index per day before you are rate-limited.
daily_limit_reset
object
Object containing options to override the default daily limit reset time.
reset_time
string
String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).
reset_utc_offset
string
String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).
daily_limit_warning_threshold_percentage
double
A percentage threshold of the daily quota at which a Datadog warning event is generated.
exclusion_filters
[object]
An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.
filter
object
Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.
query
string
Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.
sample_rate [_required_]
double
Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.
is_enabled
boolean
Whether or not the exclusion filter is active.
name [_required_]
string
Name of the index exclusion filter.
filter [_required_]
object
Filter for logs.
query
string
The filter query.
is_rate_limited
boolean
A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.
name [_required_]
string
The name of the index.
num_flex_logs_retention_days
int64
The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions.
num_retention_days
int64
The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.
```
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "is_rate_limited": false,
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15
}
```

Copy
Invalid Parameter Error
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=typescript)


#####  Update an index
Copy
```
                  # Path parameters  
export name="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes/${name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "exclusion_filters": [
    {
      "filter": {
        "sample_rate": 1
      },
      "name": "payment"
    }
  ],
  "filter": {}
}
EOF  

                
```

#####  Update an index
```
"""
Update an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_daily_limit_reset import LogsDailyLimitReset
from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
from datadog_api_client.v1.model.logs_exclusion_filter import LogsExclusionFilter
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_index_update_request import LogsIndexUpdateRequest

body = LogsIndexUpdateRequest(
    daily_limit=300000000,
    daily_limit_reset=LogsDailyLimitReset(
        reset_time="14:00",
        reset_utc_offset="+02:00",
    ),
    daily_limit_warning_threshold_percentage=70.0,
    disable_daily_limit=False,
    exclusion_filters=[
        LogsExclusion(
            filter=LogsExclusionFilter(
                query="*",
                sample_rate=1.0,
            ),
            name="payment",
        ),
    ],
    filter=LogsFilter(
        query="source:python",
    ),
    num_flex_logs_retention_days=360,
    num_retention_days=15,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.update_logs_index(name="name", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update an index
```
# Update an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new

body = DatadogAPIClient::V1::LogsIndexUpdateRequest.new({
  daily_limit: 300000000,
  daily_limit_reset: DatadogAPIClient::V1::LogsDailyLimitReset.new({
    reset_time: "14:00",
    reset_utc_offset: "+02:00",
  }),
  daily_limit_warning_threshold_percentage: 70,
  disable_daily_limit: false,
  exclusion_filters: [
    DatadogAPIClient::V1::LogsExclusion.new({
      filter: DatadogAPIClient::V1::LogsExclusionFilter.new({
        query: "*",
        sample_rate: 1.0,
      }),
      name: "payment",
    }),
  ],
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  num_flex_logs_retention_days: 360,
  num_retention_days: 15,
})
p api_instance.update_logs_index("name", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update an index
```
// Update an index returns "OK" response

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
	body := datadogV1.LogsIndexUpdateRequest{
		DailyLimit: datadog.PtrInt64(300000000),
		DailyLimitReset: &datadogV1.LogsDailyLimitReset{
			ResetTime:      datadog.PtrString("14:00"),
			ResetUtcOffset: datadog.PtrString("+02:00"),
		},
		DailyLimitWarningThresholdPercentage: datadog.PtrFloat64(70),
		DisableDailyLimit:                    datadog.PtrBool(false),
		ExclusionFilters: []datadogV1.LogsExclusion{
			{
				Filter: &datadogV1.LogsExclusionFilter{
					Query:      datadog.PtrString("*"),
					SampleRate: 1.0,
				},
				Name: "payment",
			},
		},
		Filter: datadogV1.LogsFilter{
			Query: datadog.PtrString("source:python"),
		},
		NumFlexLogsRetentionDays: datadog.PtrInt64(360),
		NumRetentionDays:         datadog.PtrInt64(15),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsIndexesApi(apiClient)
	resp, r, err := api.UpdateLogsIndex(ctx, "name", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.UpdateLogsIndex`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.UpdateLogsIndex`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update an index
```
// Update an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsDailyLimitReset;
import com.datadog.api.client.v1.model.LogsExclusion;
import com.datadog.api.client.v1.model.LogsExclusionFilter;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsIndex;
import com.datadog.api.client.v1.model.LogsIndexUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    LogsIndexUpdateRequest body =
        new LogsIndexUpdateRequest()
            .dailyLimit(300000000L)
            .dailyLimitReset(new LogsDailyLimitReset().resetTime("14:00").resetUtcOffset("+02:00"))
            .dailyLimitWarningThresholdPercentage(70.0)
            .disableDailyLimit(false)
            .exclusionFilters(
                Collections.singletonList(
                    new LogsExclusion()
                        .filter(new LogsExclusionFilter().query("*").sampleRate(1.0))
                        .name("payment")))
            .filter(new LogsFilter().query("source:python"))
            .numFlexLogsRetentionDays(360L)
            .numRetentionDays(15L);

    try {
      LogsIndex result = apiInstance.updateLogsIndex("name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#updateLogsIndex");
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

#####  Update an index
```
// Update an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;
use datadog_api_client::datadogV1::model::LogsDailyLimitReset;
use datadog_api_client::datadogV1::model::LogsExclusion;
use datadog_api_client::datadogV1::model::LogsExclusionFilter;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsIndexUpdateRequest;

#[tokio::main]
async fn main() {
    let body = LogsIndexUpdateRequest::new(LogsFilter::new().query("source:python".to_string()))
        .daily_limit(300000000)
        .daily_limit_reset(
            LogsDailyLimitReset::new()
                .reset_time("14:00".to_string())
                .reset_utc_offset("+02:00".to_string()),
        )
        .daily_limit_warning_threshold_percentage(70.0 as f64)
        .disable_daily_limit(false)
        .exclusion_filters(vec![LogsExclusion::new("payment".to_string())
            .filter(LogsExclusionFilter::new(1.0).query("*".to_string()))])
        .num_flex_logs_retention_days(360)
        .num_retention_days(15);
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.update_logs_index("name".to_string(), body).await;
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

#####  Update an index
```
/**
 * Update an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiUpdateLogsIndexRequest = {
  body: {
    dailyLimit: 300000000,
    dailyLimitReset: {
      resetTime: "14:00",
      resetUtcOffset: "+02:00",
    },
    dailyLimitWarningThresholdPercentage: 70,
    disableDailyLimit: false,
    exclusionFilters: [
      {
        filter: {
          query: "*",
          sampleRate: 1.0,
        },
        name: "payment",
      },
    ],
    filter: {
      query: "source:python",
    },
    numFlexLogsRetentionDays: 360,
    numRetentionDays: 15,
  },
  name: "name",
};

apiInstance
  .updateLogsIndex(params)
  .then((data: v1.LogsIndex) => {
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
## [Delete an index](https://docs.datadoghq.com/api/latest/logs-indexes/#delete-an-index)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-indexes/#delete-an-index-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.ap2.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.datadoghq.eu/api/v1/logs/config/indexes/{name}https://api.ddog-gov.com/api/v1/logs/config/indexes/{name}https://api.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.us3.datadoghq.com/api/v1/logs/config/indexes/{name}https://api.us5.datadoghq.com/api/v1/logs/config/indexes/{name}
### Overview
Delete an existing index from your organization. Index deletions are permanent and cannot be reverted. You cannot recreate an index with the same name as deleted ones. This endpoint requires the `logs_modify_indexes` permission.
### Arguments
#### Path Parameters
Name
Type
Description
name [_required_]
string
Name of the log index.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-indexes/#DeleteLogsIndex-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-indexes/#DeleteLogsIndex-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/logs-indexes/#DeleteLogsIndex-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-indexes/#DeleteLogsIndex-429-v1)


OK
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=typescript)


#####  Delete an index
Copy
```
                  # Path parameters  
export name="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes/${name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an index
```
"""
Delete an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    api_instance.delete_logs_index(
        name="name",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an index
```
# Delete an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.delete_logs_index("name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an index
```
// Delete an index returns "OK" response

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
	api := datadogV1.NewLogsIndexesApi(apiClient)
	r, err := api.DeleteLogsIndex(ctx, "name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.DeleteLogsIndex`: %v\n", err)
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

#####  Delete an index
```
// Delete an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      apiInstance.deleteLogsIndex("name");
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#deleteLogsIndex");
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

#####  Delete an index
```
// Delete an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.delete_logs_index("name".to_string()).await;
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

#####  Delete an index
```
/**
 * Delete an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiDeleteLogsIndexRequest = {
  name: "name",
};

apiInstance
  .deleteLogsIndex(params)
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
## [Get indexes order](https://docs.datadoghq.com/api/latest/logs-indexes/#get-indexes-order)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-indexes/#get-indexes-order-v1)


GET https://api.ap1.datadoghq.com/api/v1/logs/config/index-orderhttps://api.ap2.datadoghq.com/api/v1/logs/config/index-orderhttps://api.datadoghq.eu/api/v1/logs/config/index-orderhttps://api.ddog-gov.com/api/v1/logs/config/index-orderhttps://api.datadoghq.com/api/v1/logs/config/index-orderhttps://api.us3.datadoghq.com/api/v1/logs/config/index-orderhttps://api.us5.datadoghq.com/api/v1/logs/config/index-order
### Overview
Get the current order of your log indexes. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-indexes/#GetLogsIndexOrder-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-indexes/#GetLogsIndexOrder-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-indexes/#GetLogsIndexOrder-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Object containing the ordered list of log index names.
Expand All
Field
Type
Description
index_names [_required_]
[string]
Array of strings identifying by their name(s) the index(es) of your organization. Logs are tested against the query filter of each index one by one, following the order of the array. Logs are eventually stored in the first matching index.
```
{
  "index_names": [
    "main",
    "payments",
    "web"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=typescript)


#####  Get indexes order
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/index-order" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get indexes order
```
"""
Get indexes order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.get_logs_index_order()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get indexes order
```
# Get indexes order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.get_logs_index_order()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get indexes order
```
// Get indexes order returns "OK" response

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
	api := datadogV1.NewLogsIndexesApi(apiClient)
	resp, r, err := api.GetLogsIndexOrder(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.GetLogsIndexOrder`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.GetLogsIndexOrder`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get indexes order
```
// Get indexes order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndexesOrder;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      LogsIndexesOrder result = apiInstance.getLogsIndexOrder();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#getLogsIndexOrder");
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

#####  Get indexes order
```
// Get indexes order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.get_logs_index_order().await;
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

#####  Get indexes order
```
/**
 * Get indexes order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

apiInstance
  .getLogsIndexOrder()
  .then((data: v1.LogsIndexesOrder) => {
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
## [Update indexes order](https://docs.datadoghq.com/api/latest/logs-indexes/#update-indexes-order)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/logs-indexes/#update-indexes-order-v1)


PUT https://api.ap1.datadoghq.com/api/v1/logs/config/index-orderhttps://api.ap2.datadoghq.com/api/v1/logs/config/index-orderhttps://api.datadoghq.eu/api/v1/logs/config/index-orderhttps://api.ddog-gov.com/api/v1/logs/config/index-orderhttps://api.datadoghq.com/api/v1/logs/config/index-orderhttps://api.us3.datadoghq.com/api/v1/logs/config/index-orderhttps://api.us5.datadoghq.com/api/v1/logs/config/index-order
### Overview
This endpoint updates the index order of your organization. It returns the index order object passed in the request body when the request is successful. This endpoint requires the `logs_modify_indexes` permission.
### Request
#### Body Data (required)
Object containing the new ordered list of index names
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Expand All
Field
Type
Description
index_names [_required_]
[string]
Array of strings identifying by their name(s) the index(es) of your organization. Logs are tested against the query filter of each index one by one, following the order of the array. Logs are eventually stored in the first matching index.
```
{
  "index_names": [
    "main",
    "payments",
    "web"
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndexOrder-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndexOrder-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndexOrder-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/logs-indexes/#UpdateLogsIndexOrder-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


Object containing the ordered list of log index names.
Expand All
Field
Type
Description
index_names [_required_]
[string]
Array of strings identifying by their name(s) the index(es) of your organization. Logs are tested against the query filter of each index one by one, following the order of the array. Logs are eventually stored in the first matching index.
```
{
  "index_names": [
    "main",
    "payments",
    "web"
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-indexes/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-indexes/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-indexes/?code-lang=typescript)


#####  Update indexes order
Copy
```
                  # Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/index-order" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "index_names": [
    "main",
    "payments",
    "web"
  ]
}
EOF  

                
```

#####  Update indexes order
```
"""
Update indexes order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_indexes_order import LogsIndexesOrder

body = LogsIndexesOrder(
    index_names=[
        "main",
        "payments",
        "web",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.update_logs_index_order(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update indexes order
```
# Update indexes order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new

body = DatadogAPIClient::V1::LogsIndexesOrder.new({
  index_names: [
    "main",
    "payments",
    "web",
  ],
})
p api_instance.update_logs_index_order(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update indexes order
```
// Update indexes order returns "OK" response

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
	body := datadogV1.LogsIndexesOrder{
		IndexNames: []string{
			"main",
			"payments",
			"web",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsIndexesApi(apiClient)
	resp, r, err := api.UpdateLogsIndexOrder(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.UpdateLogsIndexOrder`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.UpdateLogsIndexOrder`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update indexes order
```
// Update indexes order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndexesOrder;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    LogsIndexesOrder body =
        new LogsIndexesOrder().indexNames(Arrays.asList("main", "payments", "web"));

    try {
      LogsIndexesOrder result = apiInstance.updateLogsIndexOrder(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#updateLogsIndexOrder");
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

#####  Update indexes order
```
// Update indexes order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;
use datadog_api_client::datadogV1::model::LogsIndexesOrder;

#[tokio::main]
async fn main() {
    let body = LogsIndexesOrder::new(vec![
        "main".to_string(),
        "payments".to_string(),
        "web".to_string(),
    ]);
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.update_logs_index_order(body).await;
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

#####  Update indexes order
```
/**
 * Update indexes order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiUpdateLogsIndexOrderRequest = {
  body: {
    indexNames: ["main", "payments", "web"],
  },
};

apiInstance
  .updateLogsIndexOrder(params)
  .then((data: v1.LogsIndexesOrder) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=daca7683-47b9-48b3-929c-9dafba0284e6&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=76f1c302-2c92-4dd9-a36e-0458bb937d18&pt=Logs%20Indexes&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-indexes%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=daca7683-47b9-48b3-929c-9dafba0284e6&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=76f1c302-2c92-4dd9-a36e-0458bb937d18&pt=Logs%20Indexes&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-indexes%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=b95ae522-08d7-4f2e-b551-f274a2fb570e&bo=2&sid=d2ef8500f0bf11f0a1f0c74ff5b75d7f&vid=d2ef9f00f0bf11f0a649af9ed78a93a9&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Logs%20Indexes&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-indexes%2F&r=&lt=1680&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=620727)
