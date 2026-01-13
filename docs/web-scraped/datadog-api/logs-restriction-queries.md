# Source: https://docs.datadoghq.com/api/latest/logs-restriction-queries/

# Logs Restriction Queries
**Note: This endpoint is in public beta. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
A Restriction Query is a logs query that restricts which logs the `logs_read_data` permission grants read access to. For users whose roles have Restriction Queries, any log query they make only returns those log events that also match one of their Restriction Queries. This is true whether the user queries log events from any log-related feature, including the log explorer, Live Tail, re-hydration, or a dashboard widget.
Restriction Queries currently only support use of the following components of log events:
  * Reserved attributes
  * The log message
  * Tags


To restrict read access on log data, add a team tag to log events to indicate which teams own them, and then scope Restriction Queries to the relevant values of the team tag. Tags can be applied to log events in many ways, and a log event can have multiple tags with the same key (like team) and different values. This means the same log event can be visible to roles whose restriction queries are scoped to different team values.
See [How to Set Up RBAC for Logs](https://docs.datadoghq.com/logs/guide/logs-rbac/?tab=api#restrict-access-to-logs) for details on how to add restriction queries.
## [List restriction queries](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#list-restriction-queries)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#list-restriction-queries-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.ap2.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.datadoghq.eu/api/v2/logs/config/restriction_querieshttps://api.ddog-gov.com/api/v2/logs/config/restriction_querieshttps://api.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.us3.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries
### Overview
Returns all restriction queries, including their names and IDs. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[number]
integer
Specific page number to return.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueries-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueries-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueries-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about multiple restriction queries.
Field
Type
Description
data
[object]
Array of returned restriction queries.
attributes
object
Attributes of the restriction query.
created_at
date-time
Creation time of the restriction query.
last_modifier_email
string
Email of the user who last modified this restriction query.
last_modifier_name
string
Name of the user who last modified this restriction query.
modified_at
date-time
Time of last restriction query modification.
restriction_query
string
The query that defines the restriction. Only the content matching the query can be returned.
role_count
int64
Number of roles associated with this restriction query.
user_count
int64
Number of users associated with this restriction query.
id
string
ID of the restriction query.
type
string
Restriction queries type.
default: `logs_restriction_queries`
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2020-03-17T21:06:44.000Z",
        "last_modifier_email": "user@example.com",
        "last_modifier_name": "John Doe",
        "modified_at": "2020-03-17T21:15:15.000Z",
        "restriction_query": "env:sandbox",
        "role_count": 3,
        "user_count": 5
      },
      "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
      "type": "logs_restriction_queries"
    }
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  List restriction queries
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List restriction queries
```
"""
List restriction queries returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

configuration = Configuration()
configuration.unstable_operations["list_restriction_queries"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_restriction_queries()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List restriction queries
```
# List restriction queries returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_restriction_queries".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new
p api_instance.list_restriction_queries()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List restriction queries
```
// List restriction queries returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListRestrictionQueries", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.ListRestrictionQueries(ctx, *datadogV2.NewListRestrictionQueriesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ListRestrictionQueries`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ListRestrictionQueries`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List restriction queries
```
// List restriction queries returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listRestrictionQueries", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    try {
      RestrictionQueryListResponse result = apiInstance.listRestrictionQueries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#listRestrictionQueries");
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

#####  List restriction queries
```
// List restriction queries returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::ListRestrictionQueriesOptionalParams;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListRestrictionQueries", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .list_restriction_queries(ListRestrictionQueriesOptionalParams::default())
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

#####  List restriction queries
```
/**
 * List restriction queries returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listRestrictionQueries"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

apiInstance
  .listRestrictionQueries()
  .then((data: v2.RestrictionQueryListResponse) => {
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
## [Create a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#create-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#create-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.ap2.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.datadoghq.eu/api/v2/logs/config/restriction_querieshttps://api.ddog-gov.com/api/v2/logs/config/restriction_querieshttps://api.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.us3.datadoghq.com/api/v2/logs/config/restriction_querieshttps://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries
### Overview
Create a new restriction query for your organization. This endpoint requires the `user_access_manage` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Field
Type
Description
data
object
Data related to the creation of a restriction query.
attributes
object
Attributes of the created restriction query.
restriction_query [_required_]
string
The restriction query.
type
enum
Restriction query resource type. Allowed enum values: `logs_restriction_queries`
default: `logs_restriction_queries`
```
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#CreateRestrictionQuery-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#CreateRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#CreateRestrictionQuery-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#CreateRestrictionQuery-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about a single restriction query.
Field
Type
Description
data
object
Restriction query object returned by the API.
attributes
object
Attributes of the restriction query.
created_at
date-time
Creation time of the restriction query.
last_modifier_email
string
Email of the user who last modified this restriction query.
last_modifier_name
string
Name of the user who last modified this restriction query.
modified_at
date-time
Time of last restriction query modification.
restriction_query
string
The query that defines the restriction. Only the content matching the query can be returned.
role_count
int64
Number of roles associated with this restriction query.
user_count
int64
Number of users associated with this restriction query.
id
string
ID of the restriction query.
type
string
Restriction queries type.
default: `logs_restriction_queries`
```
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "type": "logs_restriction_queries"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Create a restriction query returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
EOF  

                        
```

#####  Create a restriction query returns "OK" response
```
// Create a restriction query returns "OK" response

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
	body := datadogV2.RestrictionQueryCreatePayload{
		Data: &datadogV2.RestrictionQueryCreateData{
			Attributes: &datadogV2.RestrictionQueryCreateAttributes{
				RestrictionQuery: "env:sandbox",
			},
			Type: datadogV2.LOGSRESTRICTIONQUERIESTYPE_LOGS_RESTRICTION_QUERIES.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.CreateRestrictionQuery(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.CreateRestrictionQuery`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.CreateRestrictionQuery`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a restriction query returns "OK" response
```
// Create a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.LogsRestrictionQueriesType;
import com.datadog.api.client.v2.model.RestrictionQueryCreateAttributes;
import com.datadog.api.client.v2.model.RestrictionQueryCreateData;
import com.datadog.api.client.v2.model.RestrictionQueryCreatePayload;
import com.datadog.api.client.v2.model.RestrictionQueryWithoutRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    RestrictionQueryCreatePayload body =
        new RestrictionQueryCreatePayload()
            .data(
                new RestrictionQueryCreateData()
                    .attributes(
                        new RestrictionQueryCreateAttributes().restrictionQuery("env:sandbox"))
                    .type(LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES));

    try {
      RestrictionQueryWithoutRelationshipsResponse result =
          apiInstance.createRestrictionQuery(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#createRestrictionQuery");
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

#####  Create a restriction query returns "OK" response
```
"""
Create a restriction query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_create_attributes import RestrictionQueryCreateAttributes
from datadog_api_client.v2.model.restriction_query_create_data import RestrictionQueryCreateData
from datadog_api_client.v2.model.restriction_query_create_payload import RestrictionQueryCreatePayload

body = RestrictionQueryCreatePayload(
    data=RestrictionQueryCreateData(
        attributes=RestrictionQueryCreateAttributes(
            restriction_query="env:sandbox",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.create_restriction_query(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a restriction query returns "OK" response
```
# Create a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

body = DatadogAPIClient::V2::RestrictionQueryCreatePayload.new({
  data: DatadogAPIClient::V2::RestrictionQueryCreateData.new({
    attributes: DatadogAPIClient::V2::RestrictionQueryCreateAttributes.new({
      restriction_query: "env:sandbox",
    }),
    type: DatadogAPIClient::V2::LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES,
  }),
})
p api_instance.create_restriction_query(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a restriction query returns "OK" response
```
// Create a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::LogsRestrictionQueriesType;
use datadog_api_client::datadogV2::model::RestrictionQueryCreateAttributes;
use datadog_api_client::datadogV2::model::RestrictionQueryCreateData;
use datadog_api_client::datadogV2::model::RestrictionQueryCreatePayload;

#[tokio::main]
async fn main() {
    let body = RestrictionQueryCreatePayload::new().data(
        RestrictionQueryCreateData::new()
            .attributes(RestrictionQueryCreateAttributes::new(
                "env:sandbox".to_string(),
            ))
            .type_(LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api.create_restriction_query(body).await;
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

#####  Create a restriction query returns "OK" response
```
/**
 * Create a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

const params: v2.LogsRestrictionQueriesApiCreateRestrictionQueryRequest = {
  body: {
    data: {
      attributes: {
        restrictionQuery: "env:sandbox",
      },
      type: "logs_restriction_queries",
    },
  },
};

apiInstance
  .createRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithoutRelationshipsResponse) => {
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
## [Get a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#get-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#get-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}
### Overview
Get a restriction query in the organization specified by the restriction query’s `restriction_query_id`. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
restriction_query_id [_required_]
string
The ID of the restriction query.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRestrictionQuery-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRestrictionQuery-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRestrictionQuery-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRestrictionQuery-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about a single restriction query.
Field
Type
Description
data
object
Restriction query object returned by the API.
attributes
object
Attributes of the restriction query.
created_at
date-time
Creation time of the restriction query.
last_modifier_email
string
Email of the user who last modified this restriction query.
last_modifier_name
string
Name of the user who last modified this restriction query.
modified_at
date-time
Time of last restriction query modification.
restriction_query
string
The query that defines the restriction. Only the content matching the query can be returned.
role_count
int64
Number of roles associated with this restriction query.
user_count
int64
Number of users associated with this restriction query.
id
string
ID of the restriction query.
relationships
object
Relationships of the user object.
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Restriction query resource type. Allowed enum values: `logs_restriction_queries`
default: `logs_restriction_queries`
included
[ <oneOf>]
Array of objects related to the restriction query.
Option 1
object
Partial role object.
attributes [_required_]
object
Attributes of the role for a restriction query.
name
string
The role name.
id [_required_]
string
ID of the role.
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "relationships": {
      "roles": {
        "data": [
          {
            "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            "type": "roles"
          }
        ]
      }
    },
    "type": "logs_restriction_queries"
  },
  "included": [
    {
      "attributes": {
        "name": "Datadog Admin Role"
      },
      "id": "<ROLE_ID>",
      "type": "roles"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Get a restriction query
Copy
```
                  # Path parameters  
export restriction_query_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a restriction query
```
"""
Get a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.get_restriction_query(
        restriction_query_id=RESTRICTION_QUERY_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a restriction query
```
# Get a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]
p api_instance.get_restriction_query(RESTRICTION_QUERY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a restriction query
```
// Get a restriction query returns "OK" response

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
	// there is a valid "restriction_query" in the system
	RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.GetRestrictionQuery(ctx, RestrictionQueryDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.GetRestrictionQuery`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.GetRestrictionQuery`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a restriction query
```
// Get a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryWithRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    try {
      RestrictionQueryWithRelationshipsResponse result =
          apiInstance.getRestrictionQuery(RESTRICTION_QUERY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#getRestrictionQuery");
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

#####  Get a restriction query
```
// Get a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .get_restriction_query(restriction_query_data_id.clone())
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

#####  Get a restriction query
```
/**
 * Get a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiGetRestrictionQueryRequest = {
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .getRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithRelationshipsResponse) => {
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
## [Replace a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#replace-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#replace-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PUT https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}
### Overview
Replace a restriction query. This endpoint requires the `user_access_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
restriction_query_id [_required_]
string
The ID of the restriction query.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Field
Type
Description
data
object
Data related to the update of a restriction query.
attributes
object
Attributes of the edited restriction query.
restriction_query [_required_]
string
The restriction query.
type
enum
Restriction query resource type. Allowed enum values: `logs_restriction_queries`
default: `logs_restriction_queries`
```
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ReplaceRestrictionQuery-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ReplaceRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ReplaceRestrictionQuery-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ReplaceRestrictionQuery-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ReplaceRestrictionQuery-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about a single restriction query.
Field
Type
Description
data
object
Restriction query object returned by the API.
attributes
object
Attributes of the restriction query.
created_at
date-time
Creation time of the restriction query.
last_modifier_email
string
Email of the user who last modified this restriction query.
last_modifier_name
string
Name of the user who last modified this restriction query.
modified_at
date-time
Time of last restriction query modification.
restriction_query
string
The query that defines the restriction. Only the content matching the query can be returned.
role_count
int64
Number of roles associated with this restriction query.
user_count
int64
Number of users associated with this restriction query.
id
string
ID of the restriction query.
type
string
Restriction queries type.
default: `logs_restriction_queries`
```
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "type": "logs_restriction_queries"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Replace a restriction query
Copy
```
                  # Path parameters  
export restriction_query_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    }
  }
}
EOF  

                
```

#####  Replace a restriction query
```
"""
Replace a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_update_attributes import RestrictionQueryUpdateAttributes
from datadog_api_client.v2.model.restriction_query_update_data import RestrictionQueryUpdateData
from datadog_api_client.v2.model.restriction_query_update_payload import RestrictionQueryUpdatePayload

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

body = RestrictionQueryUpdatePayload(
    data=RestrictionQueryUpdateData(
        attributes=RestrictionQueryUpdateAttributes(
            restriction_query="env:staging",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["replace_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.replace_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Replace a restriction query
```
# Replace a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.replace_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

body = DatadogAPIClient::V2::RestrictionQueryUpdatePayload.new({
  data: DatadogAPIClient::V2::RestrictionQueryUpdateData.new({
    attributes: DatadogAPIClient::V2::RestrictionQueryUpdateAttributes.new({
      restriction_query: "env:staging",
    }),
    type: DatadogAPIClient::V2::LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES,
  }),
})
p api_instance.replace_restriction_query(RESTRICTION_QUERY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Replace a restriction query
```
// Replace a restriction query returns "OK" response

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
	// there is a valid "restriction_query" in the system
	RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

	body := datadogV2.RestrictionQueryUpdatePayload{
		Data: &datadogV2.RestrictionQueryUpdateData{
			Attributes: &datadogV2.RestrictionQueryUpdateAttributes{
				RestrictionQuery: "env:staging",
			},
			Type: datadogV2.LOGSRESTRICTIONQUERIESTYPE_LOGS_RESTRICTION_QUERIES.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ReplaceRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.ReplaceRestrictionQuery(ctx, RestrictionQueryDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ReplaceRestrictionQuery`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ReplaceRestrictionQuery`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Replace a restriction query
```
// Replace a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.LogsRestrictionQueriesType;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateAttributes;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateData;
import com.datadog.api.client.v2.model.RestrictionQueryUpdatePayload;
import com.datadog.api.client.v2.model.RestrictionQueryWithoutRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.replaceRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    RestrictionQueryUpdatePayload body =
        new RestrictionQueryUpdatePayload()
            .data(
                new RestrictionQueryUpdateData()
                    .attributes(
                        new RestrictionQueryUpdateAttributes().restrictionQuery("env:staging"))
                    .type(LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES));

    try {
      RestrictionQueryWithoutRelationshipsResponse result =
          apiInstance.replaceRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#replaceRestrictionQuery");
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

#####  Replace a restriction query
```
// Replace a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::LogsRestrictionQueriesType;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateAttributes;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateData;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdatePayload;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let body = RestrictionQueryUpdatePayload::new().data(
        RestrictionQueryUpdateData::new()
            .attributes(RestrictionQueryUpdateAttributes::new(
                "env:staging".to_string(),
            ))
            .type_(LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ReplaceRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .replace_restriction_query(restriction_query_data_id.clone(), body)
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

#####  Replace a restriction query
```
/**
 * Replace a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.replaceRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiReplaceRestrictionQueryRequest = {
  body: {
    data: {
      attributes: {
        restrictionQuery: "env:staging",
      },
      type: "logs_restriction_queries",
    },
  },
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .replaceRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithoutRelationshipsResponse) => {
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
## [Update a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#update-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#update-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PATCH https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}
### Overview
Edit a restriction query. This endpoint requires the `user_access_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
restriction_query_id [_required_]
string
The ID of the restriction query.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Field
Type
Description
data
object
Data related to the update of a restriction query.
attributes
object
Attributes of the edited restriction query.
restriction_query [_required_]
string
The restriction query.
type
enum
Restriction query resource type. Allowed enum values: `logs_restriction_queries`
default: `logs_restriction_queries`
```
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#UpdateRestrictionQuery-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#UpdateRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#UpdateRestrictionQuery-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#UpdateRestrictionQuery-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#UpdateRestrictionQuery-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about a single restriction query.
Field
Type
Description
data
object
Restriction query object returned by the API.
attributes
object
Attributes of the restriction query.
created_at
date-time
Creation time of the restriction query.
last_modifier_email
string
Email of the user who last modified this restriction query.
last_modifier_name
string
Name of the user who last modified this restriction query.
modified_at
date-time
Time of last restriction query modification.
restriction_query
string
The query that defines the restriction. Only the content matching the query can be returned.
role_count
int64
Number of roles associated with this restriction query.
user_count
int64
Number of users associated with this restriction query.
id
string
ID of the restriction query.
type
string
Restriction queries type.
default: `logs_restriction_queries`
```
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "type": "logs_restriction_queries"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Update a restriction query
Copy
```
                  # Path parameters  
export restriction_query_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    }
  }
}
EOF  

                
```

#####  Update a restriction query
```
"""
Update a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_update_attributes import RestrictionQueryUpdateAttributes
from datadog_api_client.v2.model.restriction_query_update_data import RestrictionQueryUpdateData
from datadog_api_client.v2.model.restriction_query_update_payload import RestrictionQueryUpdatePayload

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

body = RestrictionQueryUpdatePayload(
    data=RestrictionQueryUpdateData(
        attributes=RestrictionQueryUpdateAttributes(
            restriction_query="env:production",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.update_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a restriction query
```
# Update a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

body = DatadogAPIClient::V2::RestrictionQueryUpdatePayload.new({
  data: DatadogAPIClient::V2::RestrictionQueryUpdateData.new({
    attributes: DatadogAPIClient::V2::RestrictionQueryUpdateAttributes.new({
      restriction_query: "env:production",
    }),
    type: DatadogAPIClient::V2::LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES,
  }),
})
p api_instance.update_restriction_query(RESTRICTION_QUERY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a restriction query
```
// Update a restriction query returns "OK" response

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
	// there is a valid "restriction_query" in the system
	RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

	body := datadogV2.RestrictionQueryUpdatePayload{
		Data: &datadogV2.RestrictionQueryUpdateData{
			Attributes: &datadogV2.RestrictionQueryUpdateAttributes{
				RestrictionQuery: "env:production",
			},
			Type: datadogV2.LOGSRESTRICTIONQUERIESTYPE_LOGS_RESTRICTION_QUERIES.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.UpdateRestrictionQuery(ctx, RestrictionQueryDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.UpdateRestrictionQuery`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.UpdateRestrictionQuery`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a restriction query
```
// Update a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.LogsRestrictionQueriesType;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateAttributes;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateData;
import com.datadog.api.client.v2.model.RestrictionQueryUpdatePayload;
import com.datadog.api.client.v2.model.RestrictionQueryWithoutRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    RestrictionQueryUpdatePayload body =
        new RestrictionQueryUpdatePayload()
            .data(
                new RestrictionQueryUpdateData()
                    .attributes(
                        new RestrictionQueryUpdateAttributes().restrictionQuery("env:production"))
                    .type(LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES));

    try {
      RestrictionQueryWithoutRelationshipsResponse result =
          apiInstance.updateRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#updateRestrictionQuery");
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

#####  Update a restriction query
```
// Update a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::LogsRestrictionQueriesType;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateAttributes;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateData;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdatePayload;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let body = RestrictionQueryUpdatePayload::new().data(
        RestrictionQueryUpdateData::new()
            .attributes(RestrictionQueryUpdateAttributes::new(
                "env:production".to_string(),
            ))
            .type_(LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .update_restriction_query(restriction_query_data_id.clone(), body)
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

#####  Update a restriction query
```
/**
 * Update a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiUpdateRestrictionQueryRequest = {
  body: {
    data: {
      attributes: {
        restrictionQuery: "env:production",
      },
      type: "logs_restriction_queries",
    },
  },
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .updateRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithoutRelationshipsResponse) => {
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
## [Delete a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#delete-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#delete-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}
### Overview
Deletes a restriction query. This endpoint requires the `user_access_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
restriction_query_id [_required_]
string
The ID of the restriction query.
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#DeleteRestrictionQuery-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#DeleteRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#DeleteRestrictionQuery-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#DeleteRestrictionQuery-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#DeleteRestrictionQuery-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Delete a restriction query
Copy
```
                  # Path parameters  
export restriction_query_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a restriction query
```
"""
Delete a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.delete_restriction_query(
        restriction_query_id=RESTRICTION_QUERY_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a restriction query
```
# Delete a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]
api_instance.delete_restriction_query(RESTRICTION_QUERY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a restriction query
```
// Delete a restriction query returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "restriction_query" in the system
	RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	r, err := api.DeleteRestrictionQuery(ctx, RestrictionQueryDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.DeleteRestrictionQuery`: %v\n", err)
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

#####  Delete a restriction query
```
// Delete a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    try {
      apiInstance.deleteRestrictionQuery(RESTRICTION_QUERY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#deleteRestrictionQuery");
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

#####  Delete a restriction query
```
// Delete a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .delete_restriction_query(restriction_query_data_id.clone())
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

#####  Delete a restriction query
```
/**
 * Delete a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiDeleteRestrictionQueryRequest = {
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .deleteRestrictionQuery(params)
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
## [List roles for a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#list-roles-for-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#list-roles-for-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles
### Overview
Returns all roles that have a given restriction query. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
restriction_query_id [_required_]
string
The ID of the restriction query.
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[number]
integer
Specific page number to return.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueryRoles-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueryRoles-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueryRoles-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueryRoles-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListRestrictionQueryRoles-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about roles attached to a restriction query.
Field
Type
Description
data
[object]
Array of roles.
attributes [_required_]
object
Attributes of the role for a restriction query.
name
string
The role name.
id [_required_]
string
ID of the role.
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
{
  "data": [
    {
      "attributes": {
        "name": "Datadog Admin Role"
      },
      "id": "<ROLE_ID>",
      "type": "roles"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  List roles for a restriction query
Copy
```
                  # Path parameters  
export restriction_query_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}/roles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List roles for a restriction query
```
"""
List roles for a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_restriction_query_roles"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_restriction_query_roles(
        restriction_query_id=RESTRICTION_QUERY_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List roles for a restriction query
```
# List roles for a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_restriction_query_roles".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]
p api_instance.list_restriction_query_roles(RESTRICTION_QUERY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List roles for a restriction query
```
// List roles for a restriction query returns "OK" response

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
	// there is a valid "restriction_query" in the system
	RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ListRestrictionQueryRoles", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.ListRestrictionQueryRoles(ctx, RestrictionQueryDataID, *datadogV2.NewListRestrictionQueryRolesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ListRestrictionQueryRoles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ListRestrictionQueryRoles`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List roles for a restriction query
```
// List roles for a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryRolesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listRestrictionQueryRoles", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    try {
      RestrictionQueryRolesResponse result =
          apiInstance.listRestrictionQueryRoles(RESTRICTION_QUERY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#listRestrictionQueryRoles");
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

#####  List roles for a restriction query
```
// List roles for a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::ListRestrictionQueryRolesOptionalParams;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListRestrictionQueryRoles", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .list_restriction_query_roles(
            restriction_query_data_id.clone(),
            ListRestrictionQueryRolesOptionalParams::default(),
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List roles for a restriction query
```
/**
 * List roles for a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listRestrictionQueryRoles"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiListRestrictionQueryRolesRequest = {
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .listRestrictionQueryRoles(params)
  .then((data: v2.RestrictionQueryRolesResponse) => {
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
## [Grant role to a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#grant-role-to-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#grant-role-to-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles
### Overview
Adds a role to a restriction query.
**Note** : This operation automatically grants the `logs_read_data` permission to the role if it doesn’t already have it.
This endpoint requires the `user_access_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
restriction_query_id [_required_]
string
The ID of the restriction query.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Field
Type
Description
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
{
  "data": {
    "id": "string",
    "type": "roles"
  }
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#AddRoleToRestrictionQuery-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#AddRoleToRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#AddRoleToRestrictionQuery-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#AddRoleToRestrictionQuery-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#AddRoleToRestrictionQuery-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Grant role to a restriction query returns "OK" response
Copy
```
                          # Path parameters  
export restriction_query_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}/roles" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "string",
    "type": "roles"
  }
}
EOF  

                        
```

#####  Grant role to a restriction query returns "OK" response
```
// Grant role to a restriction query returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "restriction_query" in the system
	RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	body := datadogV2.RelationshipToRole{
		Data: &datadogV2.RelationshipToRoleData{
			Id:   datadog.PtrString(RoleDataID),
			Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.AddRoleToRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	r, err := api.AddRoleToRestrictionQuery(ctx, RestrictionQueryDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.AddRoleToRestrictionQuery`: %v\n", err)
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

#####  Grant role to a restriction query returns "OK" response
```
// Grant role to a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.addRoleToRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    RelationshipToRole body =
        new RelationshipToRole()
            .data(new RelationshipToRoleData().id(ROLE_DATA_ID).type(RolesType.ROLES));

    try {
      apiInstance.addRoleToRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#addRoleToRestrictionQuery");
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

#####  Grant role to a restriction query returns "OK" response
```
"""
Grant role to a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id=ROLE_DATA_ID,
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["add_role_to_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.add_role_to_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Grant role to a restriction query returns "OK" response
```
# Grant role to a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.add_role_to_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::RelationshipToRole.new({
  data: DatadogAPIClient::V2::RelationshipToRoleData.new({
    id: ROLE_DATA_ID,
    type: DatadogAPIClient::V2::RolesType::ROLES,
  }),
})
api_instance.add_role_to_restriction_query(RESTRICTION_QUERY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Grant role to a restriction query returns "OK" response
```
// Grant role to a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();

    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = RelationshipToRole::new().data(
        RelationshipToRoleData::new()
            .id(role_data_id.clone())
            .type_(RolesType::ROLES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.AddRoleToRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .add_role_to_restriction_query(restriction_query_data_id.clone(), body)
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

#####  Grant role to a restriction query returns "OK" response
```
/**
 * Grant role to a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.addRoleToRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiAddRoleToRestrictionQueryRequest = {
  body: {
    data: {
      id: ROLE_DATA_ID,
      type: "roles",
    },
  },
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .addRoleToRestrictionQuery(params)
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
## [Revoke role from a restriction query](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#revoke-role-from-a-restriction-query)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#revoke-role-from-a-restriction-query-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roleshttps://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles
### Overview
Removes a role from a restriction query. This endpoint requires the `user_access_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
restriction_query_id [_required_]
string
The ID of the restriction query.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Field
Type
Description
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "type": "roles"
  }
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#RemoveRoleFromRestrictionQuery-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#RemoveRoleFromRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#RemoveRoleFromRestrictionQuery-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#RemoveRoleFromRestrictionQuery-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#RemoveRoleFromRestrictionQuery-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Revoke role from a restriction query
Copy
```
                  # Path parameters  
export restriction_query_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}/roles" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Revoke role from a restriction query
```
"""
Revoke role from a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id=ROLE_DATA_ID,
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["remove_role_from_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.remove_role_from_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Revoke role from a restriction query
```
# Revoke role from a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.remove_role_from_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::RelationshipToRole.new({
  data: DatadogAPIClient::V2::RelationshipToRoleData.new({
    id: ROLE_DATA_ID,
    type: DatadogAPIClient::V2::RolesType::ROLES,
  }),
})
api_instance.remove_role_from_restriction_query(RESTRICTION_QUERY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Revoke role from a restriction query
```
// Revoke role from a restriction query returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "restriction_query" in the system
	RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	body := datadogV2.RelationshipToRole{
		Data: &datadogV2.RelationshipToRoleData{
			Id:   datadog.PtrString(RoleDataID),
			Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.RemoveRoleFromRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	r, err := api.RemoveRoleFromRestrictionQuery(ctx, RestrictionQueryDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.RemoveRoleFromRestrictionQuery`: %v\n", err)
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

#####  Revoke role from a restriction query
```
// Revoke role from a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.removeRoleFromRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    RelationshipToRole body =
        new RelationshipToRole()
            .data(new RelationshipToRoleData().id(ROLE_DATA_ID).type(RolesType.ROLES));

    try {
      apiInstance.removeRoleFromRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#removeRoleFromRestrictionQuery");
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

#####  Revoke role from a restriction query
```
// Revoke role from a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();

    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = RelationshipToRole::new().data(
        RelationshipToRoleData::new()
            .id(role_data_id.clone())
            .type_(RolesType::ROLES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.RemoveRoleFromRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .remove_role_from_restriction_query(restriction_query_data_id.clone(), body)
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

#####  Revoke role from a restriction query
```
/**
 * Revoke role from a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.removeRoleFromRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiRemoveRoleFromRestrictionQueryRequest =
  {
    body: {
      data: {
        id: ROLE_DATA_ID,
        type: "roles",
      },
    },
    restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
  };

apiInstance
  .removeRoleFromRestrictionQuery(params)
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
## [Get all restriction queries for a given user](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#get-all-restriction-queries-for-a-given-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#get-all-restriction-queries-for-a-given-user-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id}https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id}https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/user/{user_id}https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/user/{user_id}https://api.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id}https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id}https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id}
### Overview
Get all restriction queries for a given user. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The ID of the user.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListUserRestrictionQueries-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListUserRestrictionQueries-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListUserRestrictionQueries-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListUserRestrictionQueries-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#ListUserRestrictionQueries-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about multiple restriction queries.
Field
Type
Description
data
[object]
Array of returned restriction queries.
attributes
object
Attributes of the restriction query.
created_at
date-time
Creation time of the restriction query.
last_modifier_email
string
Email of the user who last modified this restriction query.
last_modifier_name
string
Name of the user who last modified this restriction query.
modified_at
date-time
Time of last restriction query modification.
restriction_query
string
The query that defines the restriction. Only the content matching the query can be returned.
role_count
int64
Number of roles associated with this restriction query.
user_count
int64
Number of users associated with this restriction query.
id
string
ID of the restriction query.
type
string
Restriction queries type.
default: `logs_restriction_queries`
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2020-03-17T21:06:44.000Z",
        "last_modifier_email": "user@example.com",
        "last_modifier_name": "John Doe",
        "modified_at": "2020-03-17T21:15:15.000Z",
        "restriction_query": "env:sandbox",
        "role_count": 3,
        "user_count": 5
      },
      "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
      "type": "logs_restriction_queries"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Get all restriction queries for a given user
Copy
```
                  # Path parameters  
export user_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/user/${user_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all restriction queries for a given user
```
"""
Get all restriction queries for a given user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_user_restriction_queries"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_user_restriction_queries(
        user_id=USER_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all restriction queries for a given user
```
# Get all restriction queries for a given user returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_user_restriction_queries".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.list_user_restriction_queries(USER_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all restriction queries for a given user
```
// Get all restriction queries for a given user returns "OK" response

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
	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ListUserRestrictionQueries", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.ListUserRestrictionQueries(ctx, UserDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ListUserRestrictionQueries`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ListUserRestrictionQueries`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all restriction queries for a given user
```
// Get all restriction queries for a given user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listUserRestrictionQueries", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    try {
      RestrictionQueryListResponse result = apiInstance.listUserRestrictionQueries(USER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#listUserRestrictionQueries");
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

#####  Get all restriction queries for a given user
```
// Get all restriction queries for a given user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListUserRestrictionQueries", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .list_user_restriction_queries(user_data_id.clone())
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

#####  Get all restriction queries for a given user
```
/**
 * Get all restriction queries for a given user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listUserRestrictionQueries"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiListUserRestrictionQueriesRequest = {
  userId: USER_DATA_ID,
};

apiInstance
  .listUserRestrictionQueries(params)
  .then((data: v2.RestrictionQueryListResponse) => {
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
## [Get restriction query for a given role](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#get-restriction-query-for-a-given-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#get-restriction-query-for-a-given-role-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id}https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id}https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/role/{role_id}https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/role/{role_id}https://api.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id}https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id}https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id}
### Overview
Get restriction query for a given role. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The ID of the role.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRoleRestrictionQuery-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRoleRestrictionQuery-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRoleRestrictionQuery-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRoleRestrictionQuery-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-restriction-queries/#GetRoleRestrictionQuery-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


Response containing information about multiple restriction queries.
Field
Type
Description
data
[object]
Array of returned restriction queries.
attributes
object
Attributes of the restriction query.
created_at
date-time
Creation time of the restriction query.
last_modifier_email
string
Email of the user who last modified this restriction query.
last_modifier_name
string
Name of the user who last modified this restriction query.
modified_at
date-time
Time of last restriction query modification.
restriction_query
string
The query that defines the restriction. Only the content matching the query can be returned.
role_count
int64
Number of roles associated with this restriction query.
user_count
int64
Number of users associated with this restriction query.
id
string
ID of the restriction query.
type
string
Restriction queries type.
default: `logs_restriction_queries`
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2020-03-17T21:06:44.000Z",
        "last_modifier_email": "user@example.com",
        "last_modifier_name": "John Doe",
        "modified_at": "2020-03-17T21:15:15.000Z",
        "restriction_query": "env:sandbox",
        "role_count": 3,
        "user_count": 5
      },
      "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
      "type": "logs_restriction_queries"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-restriction-queries/?code-lang=typescript)


#####  Get restriction query for a given role
Copy
```
                  # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/role/${role_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get restriction query for a given role
```
"""
Get restriction query for a given role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_role_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.get_role_restriction_query(
        role_id=ROLE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get restriction query for a given role
```
# Get restriction query for a given role returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_role_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.get_role_restriction_query(ROLE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get restriction query for a given role
```
// Get restriction query for a given role returns "OK" response

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
	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetRoleRestrictionQuery", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
	resp, r, err := api.GetRoleRestrictionQuery(ctx, RoleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.GetRoleRestrictionQuery`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.GetRoleRestrictionQuery`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get restriction query for a given role
```
// Get restriction query for a given role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getRoleRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    try {
      RestrictionQueryListResponse result = apiInstance.getRoleRestrictionQuery(ROLE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#getRoleRestrictionQuery");
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

#####  Get restriction query for a given role
```
// Get restriction query for a given role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetRoleRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api.get_role_restriction_query(role_data_id.clone()).await;
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

#####  Get restriction query for a given role
```
/**
 * Get restriction query for a given role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getRoleRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiGetRoleRestrictionQueryRequest = {
  roleId: ROLE_DATA_ID,
};

apiInstance
  .getRoleRestrictionQuery(params)
  .then((data: v2.RestrictionQueryListResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=105f844d-15b3-40cf-93c4-f8814fc1475d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8b7b43e2-a176-4c0b-980e-6825fa15f936&pt=Logs%20Restriction%20Queries&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-restriction-queries%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=105f844d-15b3-40cf-93c4-f8814fc1475d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8b7b43e2-a176-4c0b-980e-6825fa15f936&pt=Logs%20Restriction%20Queries&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-restriction-queries%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=2835aed7-0f24-44a4-8504-9fc2a2aabe6c&bo=2&sid=c4ba0d50f0bf11f09afde9c0412ba014&vid=c4ba67e0f0bf11f099fcdb9b6c7a6b3e&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Logs%20Restriction%20Queries&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-restriction-queries%2F&r=&lt=2043&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=812273)
