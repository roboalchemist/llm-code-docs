# Source: https://docs.datadoghq.com/api/latest/rum-audience-management/

# Rum Audience Management
Auto-generated tag Rum Audience Management
## [Query accounts](https://docs.datadoghq.com/api/latest/rum-audience-management/#query-accounts)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#query-accounts-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/product-analytics/accounts/queryhttps://api.ap2.datadoghq.com/api/v2/product-analytics/accounts/queryhttps://api.datadoghq.eu/api/v2/product-analytics/accounts/queryhttps://api.ddog-gov.com/api/v2/product-analytics/accounts/queryhttps://api.datadoghq.com/api/v2/product-analytics/accounts/queryhttps://api.us3.datadoghq.com/api/v2/product-analytics/accounts/queryhttps://api.us5.datadoghq.com/api/v2/product-analytics/accounts/query
### Overview
Query accounts with flexible filtering by account properties
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
limit
int64
query
string
select_columns
[string]
sort
object
field
string
order
string
wildcard_search_term
string
id
string
type [_required_]
enum
Query account request resource type. Allowed enum values: `query_account_request`
default: `query_account_request`
```
{
  "data": {
    "attributes": {
      "limit": "integer",
      "query": "string",
      "select_columns": [],
      "sort": {
        "field": "string",
        "order": "string"
      },
      "wildcard_search_term": "string"
    },
    "id": "string",
    "type": "query_account_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#QueryAccounts-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#QueryAccounts-429-v2)


Successful response with account data
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
hits
[]
total
int64
id
string
type [_required_]
enum
Query response resource type. Allowed enum values: `query_response`
default: `query_response`
```
{
  "data": {
    "attributes": {
      "hits": [
        {
          "first_browser_name": "Chrome",
          "first_city": "San Francisco",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T06:45:12.142Z",
          "session_count": 47,
          "user_created": "2024-12-15T08:42:33.287Z",
          "user_email": "john.smith@techcorp.com",
          "user_id": "150847",
          "user_name": "John Smith",
          "user_org_id": "5001"
        },
        {
          "first_browser_name": "Chrome",
          "first_city": "Austin",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T05:22:08.951Z",
          "session_count": 89,
          "user_created": "2024-11-28T14:17:45.634Z",
          "user_email": "john.williams@techcorp.com",
          "user_id": "150848",
          "user_name": "John Williams",
          "user_org_id": "5001"
        },
        {
          "first_browser_name": "Chrome",
          "first_city": "Seattle",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T04:18:34.726Z",
          "session_count": 23,
          "user_created": "2025-01-03T16:33:21.445Z",
          "user_email": "john.jones@techcorp.com",
          "user_id": "150849",
          "user_name": "John Jones",
          "user_org_id": "5001"
        }
      ],
      "total": 147
    },
    "id": "query_response",
    "type": "query_response"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Query accounts
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/accounts/query" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "query_account_request"
  }
}
EOF  

                
```

#####  Query accounts
```
"""
Query accounts returns "Successful response with account data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.query_account_request import QueryAccountRequest
from datadog_api_client.v2.model.query_account_request_data import QueryAccountRequestData
from datadog_api_client.v2.model.query_account_request_data_attributes import QueryAccountRequestDataAttributes
from datadog_api_client.v2.model.query_account_request_data_attributes_sort import QueryAccountRequestDataAttributesSort
from datadog_api_client.v2.model.query_account_request_data_type import QueryAccountRequestDataType

body = QueryAccountRequest(
    data=QueryAccountRequestData(
        attributes=QueryAccountRequestDataAttributes(
            limit=20,
            query="plan_type:enterprise AND user_count:>100 AND subscription_status:active",
            select_columns=[
                "account_id",
                "account_name",
                "user_count",
                "plan_type",
                "subscription_status",
                "created_at",
                "mrr",
                "industry",
            ],
            sort=QueryAccountRequestDataAttributesSort(
                field="user_count",
                order="DESC",
            ),
            wildcard_search_term="tech",
        ),
        id="query_account_request",
        type=QueryAccountRequestDataType.QUERY_ACCOUNT_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.query_accounts(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Query accounts
```
# Query accounts returns "Successful response with account data" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.query_accounts".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new

body = DatadogAPIClient::V2::QueryAccountRequest.new({
  data: DatadogAPIClient::V2::QueryAccountRequestData.new({
    attributes: DatadogAPIClient::V2::QueryAccountRequestDataAttributes.new({
      limit: 20,
      query: "plan_type:enterprise AND user_count:>100 AND subscription_status:active",
      select_columns: [
        "account_id",
        "account_name",
        "user_count",
        "plan_type",
        "subscription_status",
        "created_at",
        "mrr",
        "industry",
      ],
      sort: DatadogAPIClient::V2::QueryAccountRequestDataAttributesSort.new({
        field: "user_count",
        order: "DESC",
      }),
      wildcard_search_term: "tech",
    }),
    id: "query_account_request",
    type: DatadogAPIClient::V2::QueryAccountRequestDataType::QUERY_ACCOUNT_REQUEST,
  }),
})
p api_instance.query_accounts(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Query accounts
```
// Query accounts returns "Successful response with account data" response

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
	body := datadogV2.QueryAccountRequest{
		Data: &datadogV2.QueryAccountRequestData{
			Attributes: &datadogV2.QueryAccountRequestDataAttributes{
				Limit: datadog.PtrInt64(20),
				Query: datadog.PtrString("plan_type:enterprise AND user_count:>100 AND subscription_status:active"),
				SelectColumns: []string{
					"account_id",
					"account_name",
					"user_count",
					"plan_type",
					"subscription_status",
					"created_at",
					"mrr",
					"industry",
				},
				Sort: &datadogV2.QueryAccountRequestDataAttributesSort{
					Field: datadog.PtrString("user_count"),
					Order: datadog.PtrString("DESC"),
				},
				WildcardSearchTerm: datadog.PtrString("tech"),
			},
			Id:   datadog.PtrString("query_account_request"),
			Type: datadogV2.QUERYACCOUNTREQUESTDATATYPE_QUERY_ACCOUNT_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.QueryAccounts", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	resp, r, err := api.QueryAccounts(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.QueryAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumAudienceManagementApi.QueryAccounts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Query accounts
```
// Query accounts returns "Successful response with account data" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.QueryAccountRequest;
import com.datadog.api.client.v2.model.QueryAccountRequestData;
import com.datadog.api.client.v2.model.QueryAccountRequestDataAttributes;
import com.datadog.api.client.v2.model.QueryAccountRequestDataAttributesSort;
import com.datadog.api.client.v2.model.QueryAccountRequestDataType;
import com.datadog.api.client.v2.model.QueryResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.queryAccounts", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    QueryAccountRequest body =
        new QueryAccountRequest()
            .data(
                new QueryAccountRequestData()
                    .attributes(
                        new QueryAccountRequestDataAttributes()
                            .limit(20L)
                            .query(
                                "plan_type:enterprise AND user_count:>100 AND"
                                    + " subscription_status:active")
                            .selectColumns(
                                Arrays.asList(
                                    "account_id",
                                    "account_name",
                                    "user_count",
                                    "plan_type",
                                    "subscription_status",
                                    "created_at",
                                    "mrr",
                                    "industry"))
                            .sort(
                                new QueryAccountRequestDataAttributesSort()
                                    .field("user_count")
                                    .order("DESC"))
                            .wildcardSearchTerm("tech"))
                    .id("query_account_request")
                    .type(QueryAccountRequestDataType.QUERY_ACCOUNT_REQUEST));

    try {
      QueryResponse result = apiInstance.queryAccounts(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#queryAccounts");
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

#####  Query accounts
```
// Query accounts returns "Successful response with account data" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;
use datadog_api_client::datadogV2::model::QueryAccountRequest;
use datadog_api_client::datadogV2::model::QueryAccountRequestData;
use datadog_api_client::datadogV2::model::QueryAccountRequestDataAttributes;
use datadog_api_client::datadogV2::model::QueryAccountRequestDataAttributesSort;
use datadog_api_client::datadogV2::model::QueryAccountRequestDataType;

#[tokio::main]
async fn main() {
    let body = QueryAccountRequest::new().data(
        QueryAccountRequestData::new(QueryAccountRequestDataType::QUERY_ACCOUNT_REQUEST)
            .attributes(
                QueryAccountRequestDataAttributes::new()
                    .limit(20)
                    .query(
                        "plan_type:enterprise AND user_count:>100 AND subscription_status:active"
                            .to_string(),
                    )
                    .select_columns(vec![
                        "account_id".to_string(),
                        "account_name".to_string(),
                        "user_count".to_string(),
                        "plan_type".to_string(),
                        "subscription_status".to_string(),
                        "created_at".to_string(),
                        "mrr".to_string(),
                        "industry".to_string(),
                    ])
                    .sort(
                        QueryAccountRequestDataAttributesSort::new()
                            .field("user_count".to_string())
                            .order("DESC".to_string()),
                    )
                    .wildcard_search_term("tech".to_string()),
            )
            .id("query_account_request".to_string()),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.QueryAccounts", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.query_accounts(body).await;
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

#####  Query accounts
```
/**
 * Query accounts returns "Successful response with account data" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.queryAccounts"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiQueryAccountsRequest = {
  body: {
    data: {
      attributes: {
        limit: 20,
        query:
          "plan_type:enterprise AND user_count:>100 AND subscription_status:active",
        selectColumns: [
          "account_id",
          "account_name",
          "user_count",
          "plan_type",
          "subscription_status",
          "created_at",
          "mrr",
          "industry",
        ],
        sort: {
          field: "user_count",
          order: "DESC",
        },
        wildcardSearchTerm: "tech",
      },
      id: "query_account_request",
      type: "query_account_request",
    },
  },
};

apiInstance
  .queryAccounts(params)
  .then((data: v2.QueryResponse) => {
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
## [Create connection](https://docs.datadoghq.com/api/latest/rum-audience-management/#create-connection)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#create-connection-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.ap2.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.datadoghq.eu/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.ddog-gov.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.us3.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.us5.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connection
### Overview
Create a new data connection and its fields for an entity
### Arguments
#### Path Parameters
Name
Type
Description
entity [_required_]
string
The entity for which to create the connection
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
fields
[object]
description
string
display_name
string
groups
[string]
id [_required_]
string
source_name [_required_]
string
type [_required_]
string
join_attribute [_required_]
string
join_type [_required_]
string
metadata
object
<any-key>
string
type [_required_]
string
id
string
type [_required_]
enum
Connection id resource type. Allowed enum values: `connection_id`
default: `connection_id`
```
{
  "data": {
    "attributes": {
      "fields": [
        {
          "description": "string",
          "display_name": "string",
          "groups": [],
          "id": "",
          "source_name": "",
          "type": ""
        }
      ],
      "join_attribute": "",
      "join_type": "",
      "metadata": {
        "<any-key>": "string"
      },
      "type": ""
    },
    "id": "string",
    "type": "connection_id"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/rum-audience-management/#CreateConnection-201-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#CreateConnection-429-v2)


Connection created successfully
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Create connection
Copy
```
                  # Path parameters  
export entity="users"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/${entity}/mapping/connection" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "fields": [
        {
          "id": "",
          "source_name": "",
          "type": ""
        }
      ],
      "join_attribute": "",
      "join_type": "",
      "type": ""
    },
    "type": "connection_id"
  }
}
EOF  

                
```

#####  Create connection
```
"""
Create connection returns "Connection created successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.create_connection_request import CreateConnectionRequest
from datadog_api_client.v2.model.create_connection_request_data import CreateConnectionRequestData
from datadog_api_client.v2.model.create_connection_request_data_attributes import CreateConnectionRequestDataAttributes
from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
    CreateConnectionRequestDataAttributesFieldsItems,
)
from datadog_api_client.v2.model.update_connection_request_data_type import UpdateConnectionRequestDataType

body = CreateConnectionRequest(
    data=CreateConnectionRequestData(
        attributes=CreateConnectionRequestDataAttributes(
            fields=[
                CreateConnectionRequestDataAttributesFieldsItems(
                    description="Customer subscription tier from `CRM`",
                    display_name="Customer Tier",
                    id="customer_tier",
                    source_name="subscription_tier",
                    type="string",
                ),
                CreateConnectionRequestDataAttributesFieldsItems(
                    description="Customer lifetime value in `USD`",
                    display_name="Lifetime Value",
                    id="lifetime_value",
                    source_name="ltv",
                    type="number",
                ),
            ],
            join_attribute="user_email",
            join_type="email",
            type="ref_table",
        ),
        id="crm-integration",
        type=UpdateConnectionRequestDataType.CONNECTION_ID,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    api_instance.create_connection(entity="users", body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create connection
```
# Create connection returns "Connection created successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_connection".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new

body = DatadogAPIClient::V2::CreateConnectionRequest.new({
  data: DatadogAPIClient::V2::CreateConnectionRequestData.new({
    attributes: DatadogAPIClient::V2::CreateConnectionRequestDataAttributes.new({
      fields: [
        DatadogAPIClient::V2::CreateConnectionRequestDataAttributesFieldsItems.new({
          description: "Customer subscription tier from `CRM`",
          display_name: "Customer Tier",
          id: "customer_tier",
          source_name: "subscription_tier",
          type: "string",
        }),
        DatadogAPIClient::V2::CreateConnectionRequestDataAttributesFieldsItems.new({
          description: "Customer lifetime value in `USD`",
          display_name: "Lifetime Value",
          id: "lifetime_value",
          source_name: "ltv",
          type: "number",
        }),
      ],
      join_attribute: "user_email",
      join_type: "email",
      type: "ref_table",
    }),
    id: "crm-integration",
    type: DatadogAPIClient::V2::UpdateConnectionRequestDataType::CONNECTION_ID,
  }),
})
p api_instance.create_connection("users", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create connection
```
// Create connection returns "Connection created successfully" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CreateConnectionRequest{
		Data: &datadogV2.CreateConnectionRequestData{
			Attributes: &datadogV2.CreateConnectionRequestDataAttributes{
				Fields: []datadogV2.CreateConnectionRequestDataAttributesFieldsItems{
					{
						Description: datadog.PtrString(`Customer subscription tier from ` + "`" + `CRM` + "`"),
						DisplayName: datadog.PtrString("Customer Tier"),
						Id:          "customer_tier",
						SourceName:  "subscription_tier",
						Type:        "string",
					},
					{
						Description: datadog.PtrString(`Customer lifetime value in ` + "`" + `USD` + "`"),
						DisplayName: datadog.PtrString("Lifetime Value"),
						Id:          "lifetime_value",
						SourceName:  "ltv",
						Type:        "number",
					},
				},
				JoinAttribute: "user_email",
				JoinType:      "email",
				Type:          "ref_table",
			},
			Id:   datadog.PtrString("crm-integration"),
			Type: datadogV2.UPDATECONNECTIONREQUESTDATATYPE_CONNECTION_ID,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateConnection", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	r, err := api.CreateConnection(ctx, "users", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.CreateConnection`: %v\n", err)
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

#####  Create connection
```
// Create connection returns "Connection created successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.CreateConnectionRequest;
import com.datadog.api.client.v2.model.CreateConnectionRequestData;
import com.datadog.api.client.v2.model.CreateConnectionRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateConnectionRequestDataAttributesFieldsItems;
import com.datadog.api.client.v2.model.UpdateConnectionRequestDataType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createConnection", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    CreateConnectionRequest body =
        new CreateConnectionRequest()
            .data(
                new CreateConnectionRequestData()
                    .attributes(
                        new CreateConnectionRequestDataAttributes()
                            .fields(
                                Arrays.asList(
                                    new CreateConnectionRequestDataAttributesFieldsItems()
                                        .description("Customer subscription tier from `CRM`")
                                        .displayName("Customer Tier")
                                        .id("customer_tier")
                                        .sourceName("subscription_tier")
                                        .type("string"),
                                    new CreateConnectionRequestDataAttributesFieldsItems()
                                        .description("Customer lifetime value in `USD`")
                                        .displayName("Lifetime Value")
                                        .id("lifetime_value")
                                        .sourceName("ltv")
                                        .type("number")))
                            .joinAttribute("user_email")
                            .joinType("email")
                            .type("ref_table"))
                    .id("crm-integration")
                    .type(UpdateConnectionRequestDataType.CONNECTION_ID));

    try {
      apiInstance.createConnection("users", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#createConnection");
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

#####  Create connection
```
// Create connection returns "Connection created successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;
use datadog_api_client::datadogV2::model::CreateConnectionRequest;
use datadog_api_client::datadogV2::model::CreateConnectionRequestData;
use datadog_api_client::datadogV2::model::CreateConnectionRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreateConnectionRequestDataAttributesFieldsItems;
use datadog_api_client::datadogV2::model::UpdateConnectionRequestDataType;

#[tokio::main]
async fn main() {
    let body = CreateConnectionRequest::new().data(
        CreateConnectionRequestData::new(UpdateConnectionRequestDataType::CONNECTION_ID)
            .attributes(
                CreateConnectionRequestDataAttributes::new(
                    "user_email".to_string(),
                    "email".to_string(),
                    "ref_table".to_string(),
                )
                .fields(vec![
                    CreateConnectionRequestDataAttributesFieldsItems::new(
                        "customer_tier".to_string(),
                        "subscription_tier".to_string(),
                        "string".to_string(),
                    )
                    .description(r#"Customer subscription tier from `CRM`"#.to_string())
                    .display_name("Customer Tier".to_string()),
                    CreateConnectionRequestDataAttributesFieldsItems::new(
                        "lifetime_value".to_string(),
                        "ltv".to_string(),
                        "number".to_string(),
                    )
                    .description(r#"Customer lifetime value in `USD`"#.to_string())
                    .display_name("Lifetime Value".to_string()),
                ]),
            )
            .id("crm-integration".to_string()),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateConnection", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.create_connection("users".to_string(), body).await;
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

#####  Create connection
```
/**
 * Create connection returns "Connection created successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createConnection"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiCreateConnectionRequest = {
  body: {
    data: {
      attributes: {
        fields: [
          {
            description: `Customer subscription tier from ` + "`" + `CRM` + "`",
            displayName: "Customer Tier",
            id: "customer_tier",
            sourceName: "subscription_tier",
            type: "string",
          },
          {
            description: `Customer lifetime value in ` + "`" + `USD` + "`",
            displayName: "Lifetime Value",
            id: "lifetime_value",
            sourceName: "ltv",
            type: "number",
          },
        ],
        joinAttribute: "user_email",
        joinType: "email",
        type: "ref_table",
      },
      id: "crm-integration",
      type: "connection_id",
    },
  },
  entity: "users",
};

apiInstance
  .createConnection(params)
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
## [Update connection](https://docs.datadoghq.com/api/latest/rum-audience-management/#update-connection)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#update-connection-v2)


**Note** : This endpoint may be subject to changes.
PUT https://api.ap1.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.ap2.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.datadoghq.eu/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.ddog-gov.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.us3.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionhttps://api.us5.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connection
### Overview
Update an existing data connection by adding, updating, or deleting fields
### Arguments
#### Path Parameters
Name
Type
Description
entity [_required_]
string
The entity for which to update the connection
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
fields_to_add
[object]
description
string
display_name
string
groups
[string]
id [_required_]
string
source_name [_required_]
string
type [_required_]
string
fields_to_delete
[string]
fields_to_update
[object]
field_id [_required_]
string
updated_description
string
updated_display_name
string
updated_field_id
string
updated_groups
[string]
id [_required_]
string
type [_required_]
enum
Connection id resource type. Allowed enum values: `connection_id`
default: `connection_id`
```
{
  "data": {
    "attributes": {
      "fields_to_add": [
        {
          "description": "string",
          "display_name": "string",
          "groups": [],
          "id": "",
          "source_name": "",
          "type": ""
        }
      ],
      "fields_to_delete": [],
      "fields_to_update": [
        {
          "field_id": "",
          "updated_description": "string",
          "updated_display_name": "string",
          "updated_field_id": "string",
          "updated_groups": []
        }
      ]
    },
    "id": "",
    "type": "connection_id"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#UpdateConnection-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#UpdateConnection-429-v2)


Connection updated successfully
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Update connection
Copy
```
                  # Path parameters  
export entity="users"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/${entity}/mapping/connection" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "fields_to_add": [
        {
          "id": "",
          "source_name": "",
          "type": ""
        }
      ],
      "fields_to_update": [
        {
          "field_id": ""
        }
      ]
    },
    "id": "",
    "type": "connection_id"
  }
}
EOF  

                
```

#####  Update connection
```
"""
Update connection returns "Connection updated successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
    CreateConnectionRequestDataAttributesFieldsItems,
)
from datadog_api_client.v2.model.update_connection_request import UpdateConnectionRequest
from datadog_api_client.v2.model.update_connection_request_data import UpdateConnectionRequestData
from datadog_api_client.v2.model.update_connection_request_data_attributes import UpdateConnectionRequestDataAttributes
from datadog_api_client.v2.model.update_connection_request_data_attributes_fields_to_update_items import (
    UpdateConnectionRequestDataAttributesFieldsToUpdateItems,
)
from datadog_api_client.v2.model.update_connection_request_data_type import UpdateConnectionRequestDataType

body = UpdateConnectionRequest(
    data=UpdateConnectionRequestData(
        attributes=UpdateConnectionRequestDataAttributes(
            fields_to_add=[
                CreateConnectionRequestDataAttributesFieldsItems(
                    description="Net Promoter Score from customer surveys",
                    display_name="NPS Score",
                    groups=[
                        "Satisfaction",
                        "Metrics",
                    ],
                    id="nps_score",
                    source_name="net_promoter_score",
                    type="number",
                ),
            ],
            fields_to_delete=[
                "old_revenue_field",
            ],
            fields_to_update=[
                UpdateConnectionRequestDataAttributesFieldsToUpdateItems(
                    field_id="lifetime_value",
                    updated_display_name="Customer Lifetime Value (`USD`)",
                    updated_groups=[
                        "Financial",
                        "Metrics",
                    ],
                ),
            ],
        ),
        id="crm-integration",
        type=UpdateConnectionRequestDataType.CONNECTION_ID,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    api_instance.update_connection(entity="users", body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update connection
```
# Update connection returns "Connection updated successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_connection".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new

body = DatadogAPIClient::V2::UpdateConnectionRequest.new({
  data: DatadogAPIClient::V2::UpdateConnectionRequestData.new({
    attributes: DatadogAPIClient::V2::UpdateConnectionRequestDataAttributes.new({
      fields_to_add: [
        DatadogAPIClient::V2::CreateConnectionRequestDataAttributesFieldsItems.new({
          description: "Net Promoter Score from customer surveys",
          display_name: "NPS Score",
          groups: [
            "Satisfaction",
            "Metrics",
          ],
          id: "nps_score",
          source_name: "net_promoter_score",
          type: "number",
        }),
      ],
      fields_to_delete: [
        "old_revenue_field",
      ],
      fields_to_update: [
        DatadogAPIClient::V2::UpdateConnectionRequestDataAttributesFieldsToUpdateItems.new({
          field_id: "lifetime_value",
          updated_display_name: "Customer Lifetime Value (`USD`)",
          updated_groups: [
            "Financial",
            "Metrics",
          ],
        }),
      ],
    }),
    id: "crm-integration",
    type: DatadogAPIClient::V2::UpdateConnectionRequestDataType::CONNECTION_ID,
  }),
})
p api_instance.update_connection("users", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update connection
```
// Update connection returns "Connection updated successfully" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.UpdateConnectionRequest{
		Data: &datadogV2.UpdateConnectionRequestData{
			Attributes: &datadogV2.UpdateConnectionRequestDataAttributes{
				FieldsToAdd: []datadogV2.CreateConnectionRequestDataAttributesFieldsItems{
					{
						Description: datadog.PtrString("Net Promoter Score from customer surveys"),
						DisplayName: datadog.PtrString("NPS Score"),
						Groups: []string{
							"Satisfaction",
							"Metrics",
						},
						Id:         "nps_score",
						SourceName: "net_promoter_score",
						Type:       "number",
					},
				},
				FieldsToDelete: []string{
					"old_revenue_field",
				},
				FieldsToUpdate: []datadogV2.UpdateConnectionRequestDataAttributesFieldsToUpdateItems{
					{
						FieldId:            "lifetime_value",
						UpdatedDisplayName: datadog.PtrString(`Customer Lifetime Value (` + "`" + `USD` + "`" + `)`),
						UpdatedGroups: []string{
							"Financial",
							"Metrics",
						},
					},
				},
			},
			Id:   "crm-integration",
			Type: datadogV2.UPDATECONNECTIONREQUESTDATATYPE_CONNECTION_ID,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateConnection", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	r, err := api.UpdateConnection(ctx, "users", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.UpdateConnection`: %v\n", err)
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

#####  Update connection
```
// Update connection returns "Connection updated successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.CreateConnectionRequestDataAttributesFieldsItems;
import com.datadog.api.client.v2.model.UpdateConnectionRequest;
import com.datadog.api.client.v2.model.UpdateConnectionRequestData;
import com.datadog.api.client.v2.model.UpdateConnectionRequestDataAttributes;
import com.datadog.api.client.v2.model.UpdateConnectionRequestDataAttributesFieldsToUpdateItems;
import com.datadog.api.client.v2.model.UpdateConnectionRequestDataType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateConnection", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    UpdateConnectionRequest body =
        new UpdateConnectionRequest()
            .data(
                new UpdateConnectionRequestData()
                    .attributes(
                        new UpdateConnectionRequestDataAttributes()
                            .fieldsToAdd(
                                Collections.singletonList(
                                    new CreateConnectionRequestDataAttributesFieldsItems()
                                        .description("Net Promoter Score from customer surveys")
                                        .displayName("NPS Score")
                                        .groups(Arrays.asList("Satisfaction", "Metrics"))
                                        .id("nps_score")
                                        .sourceName("net_promoter_score")
                                        .type("number")))
                            .fieldsToDelete(Collections.singletonList("old_revenue_field"))
                            .fieldsToUpdate(
                                Collections.singletonList(
                                    new UpdateConnectionRequestDataAttributesFieldsToUpdateItems()
                                        .fieldId("lifetime_value")
                                        .updatedDisplayName("Customer Lifetime Value (`USD`)")
                                        .updatedGroups(Arrays.asList("Financial", "Metrics")))))
                    .id("crm-integration")
                    .type(UpdateConnectionRequestDataType.CONNECTION_ID));

    try {
      apiInstance.updateConnection("users", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#updateConnection");
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

#####  Update connection
```
// Update connection returns "Connection updated successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;
use datadog_api_client::datadogV2::model::CreateConnectionRequestDataAttributesFieldsItems;
use datadog_api_client::datadogV2::model::UpdateConnectionRequest;
use datadog_api_client::datadogV2::model::UpdateConnectionRequestData;
use datadog_api_client::datadogV2::model::UpdateConnectionRequestDataAttributes;
use datadog_api_client::datadogV2::model::UpdateConnectionRequestDataAttributesFieldsToUpdateItems;
use datadog_api_client::datadogV2::model::UpdateConnectionRequestDataType;

#[tokio::main]
async fn main() {
    let body = UpdateConnectionRequest::new().data(
        UpdateConnectionRequestData::new(
            "crm-integration".to_string(),
            UpdateConnectionRequestDataType::CONNECTION_ID,
        )
        .attributes(
            UpdateConnectionRequestDataAttributes::new()
                .fields_to_add(vec![CreateConnectionRequestDataAttributesFieldsItems::new(
                    "nps_score".to_string(),
                    "net_promoter_score".to_string(),
                    "number".to_string(),
                )
                .description("Net Promoter Score from customer surveys".to_string())
                .display_name("NPS Score".to_string())
                .groups(vec!["Satisfaction".to_string(), "Metrics".to_string()])])
                .fields_to_delete(vec!["old_revenue_field".to_string()])
                .fields_to_update(vec![
                    UpdateConnectionRequestDataAttributesFieldsToUpdateItems::new(
                        "lifetime_value".to_string(),
                    )
                    .updated_display_name(r#"Customer Lifetime Value (`USD`)"#.to_string())
                    .updated_groups(vec!["Financial".to_string(), "Metrics".to_string()]),
                ]),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateConnection", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.update_connection("users".to_string(), body).await;
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

#####  Update connection
```
/**
 * Update connection returns "Connection updated successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateConnection"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiUpdateConnectionRequest = {
  body: {
    data: {
      attributes: {
        fieldsToAdd: [
          {
            description: "Net Promoter Score from customer surveys",
            displayName: "NPS Score",
            groups: ["Satisfaction", "Metrics"],
            id: "nps_score",
            sourceName: "net_promoter_score",
            type: "number",
          },
        ],
        fieldsToDelete: ["old_revenue_field"],
        fieldsToUpdate: [
          {
            fieldId: "lifetime_value",
            updatedDisplayName:
              `Customer Lifetime Value (` + "`" + `USD` + "`" + `)`,
            updatedGroups: ["Financial", "Metrics"],
          },
        ],
      },
      id: "crm-integration",
      type: "connection_id",
    },
  },
  entity: "users",
};

apiInstance
  .updateConnection(params)
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
## [Query event filtered users](https://docs.datadoghq.com/api/latest/rum-audience-management/#query-event-filtered-users)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#query-event-filtered-users-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/product-analytics/users/event_filtered_queryhttps://api.ap2.datadoghq.com/api/v2/product-analytics/users/event_filtered_queryhttps://api.datadoghq.eu/api/v2/product-analytics/users/event_filtered_queryhttps://api.ddog-gov.com/api/v2/product-analytics/users/event_filtered_queryhttps://api.datadoghq.com/api/v2/product-analytics/users/event_filtered_queryhttps://api.us3.datadoghq.com/api/v2/product-analytics/users/event_filtered_queryhttps://api.us5.datadoghq.com/api/v2/product-analytics/users/event_filtered_query
### Overview
Query users filtered by both user properties and event platform data
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
event_query
object
query
string
time_frame
object
end
int64
start
int64
include_row_count
boolean
limit
int64
query
string
select_columns
[string]
id
string
type [_required_]
enum
Query event filtered users request resource type. Allowed enum values: `query_event_filtered_users_request`
default: `query_event_filtered_users_request`
```
{
  "data": {
    "attributes": {
      "event_query": {
        "query": "string",
        "time_frame": {
          "end": "integer",
          "start": "integer"
        }
      },
      "include_row_count": false,
      "limit": "integer",
      "query": "string",
      "select_columns": []
    },
    "id": "string",
    "type": "query_event_filtered_users_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#QueryEventFilteredUsers-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#QueryEventFilteredUsers-429-v2)


Successful response with filtered user data
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
hits
[]
total
int64
id
string
type [_required_]
enum
Query response resource type. Allowed enum values: `query_response`
default: `query_response`
```
{
  "data": {
    "attributes": {
      "hits": [
        {
          "first_browser_name": "Chrome",
          "first_city": "San Francisco",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T06:45:12.142Z",
          "session_count": 47,
          "user_created": "2024-12-15T08:42:33.287Z",
          "user_email": "john.smith@techcorp.com",
          "user_id": "150847",
          "user_name": "John Smith",
          "user_org_id": "5001"
        },
        {
          "first_browser_name": "Chrome",
          "first_city": "Austin",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T05:22:08.951Z",
          "session_count": 89,
          "user_created": "2024-11-28T14:17:45.634Z",
          "user_email": "john.williams@techcorp.com",
          "user_id": "150848",
          "user_name": "John Williams",
          "user_org_id": "5001"
        },
        {
          "first_browser_name": "Chrome",
          "first_city": "Seattle",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T04:18:34.726Z",
          "session_count": 23,
          "user_created": "2025-01-03T16:33:21.445Z",
          "user_email": "john.jones@techcorp.com",
          "user_id": "150849",
          "user_name": "John Jones",
          "user_org_id": "5001"
        }
      ],
      "total": 147
    },
    "id": "query_response",
    "type": "query_response"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Query event filtered users
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/users/event_filtered_query" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "query_event_filtered_users_request"
  }
}
EOF  

                
```

#####  Query event filtered users
```
"""
Query event filtered users returns "Successful response with filtered user data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.query_event_filtered_users_request import QueryEventFilteredUsersRequest
from datadog_api_client.v2.model.query_event_filtered_users_request_data import QueryEventFilteredUsersRequestData
from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes import (
    QueryEventFilteredUsersRequestDataAttributes,
)
from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query import (
    QueryEventFilteredUsersRequestDataAttributesEventQuery,
)
from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query_time_frame import (
    QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame,
)
from datadog_api_client.v2.model.query_event_filtered_users_request_data_type import (
    QueryEventFilteredUsersRequestDataType,
)

body = QueryEventFilteredUsersRequest(
    data=QueryEventFilteredUsersRequestData(
        attributes=QueryEventFilteredUsersRequestDataAttributes(
            event_query=QueryEventFilteredUsersRequestDataAttributesEventQuery(
                query="@type:view AND @view.loading_time:>3000 AND @application.name:ecommerce-platform",
                time_frame=QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame(
                    end=1761309676,
                    start=1760100076,
                ),
            ),
            include_row_count=True,
            limit=25,
            query="user_org_id:5001 AND first_country_code:US AND first_browser_name:Chrome",
            select_columns=[
                "user_id",
                "user_email",
                "first_country_code",
                "first_browser_name",
                "events_count",
                "session_count",
                "error_count",
                "avg_loading_time",
            ],
        ),
        id="query_event_filtered_users_request",
        type=QueryEventFilteredUsersRequestDataType.QUERY_EVENT_FILTERED_USERS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_event_filtered_users"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.query_event_filtered_users(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Query event filtered users
```
# Query event filtered users returns "Successful response with filtered user data" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.query_event_filtered_users".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new

body = DatadogAPIClient::V2::QueryEventFilteredUsersRequest.new({
  data: DatadogAPIClient::V2::QueryEventFilteredUsersRequestData.new({
    attributes: DatadogAPIClient::V2::QueryEventFilteredUsersRequestDataAttributes.new({
      event_query: DatadogAPIClient::V2::QueryEventFilteredUsersRequestDataAttributesEventQuery.new({
        query: "@type:view AND @view.loading_time:>3000 AND @application.name:ecommerce-platform",
        time_frame: DatadogAPIClient::V2::QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame.new({
          _end: 1761309676,
          start: 1760100076,
        }),
      }),
      include_row_count: true,
      limit: 25,
      query: "user_org_id:5001 AND first_country_code:US AND first_browser_name:Chrome",
      select_columns: [
        "user_id",
        "user_email",
        "first_country_code",
        "first_browser_name",
        "events_count",
        "session_count",
        "error_count",
        "avg_loading_time",
      ],
    }),
    id: "query_event_filtered_users_request",
    type: DatadogAPIClient::V2::QueryEventFilteredUsersRequestDataType::QUERY_EVENT_FILTERED_USERS_REQUEST,
  }),
})
p api_instance.query_event_filtered_users(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Query event filtered users
```
// Query event filtered users returns "Successful response with filtered user data" response

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
	body := datadogV2.QueryEventFilteredUsersRequest{
		Data: &datadogV2.QueryEventFilteredUsersRequestData{
			Attributes: &datadogV2.QueryEventFilteredUsersRequestDataAttributes{
				EventQuery: &datadogV2.QueryEventFilteredUsersRequestDataAttributesEventQuery{
					Query: datadog.PtrString("@type:view AND @view.loading_time:>3000 AND @application.name:ecommerce-platform"),
					TimeFrame: &datadogV2.QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame{
						End:   datadog.PtrInt64(1761309676),
						Start: datadog.PtrInt64(1760100076),
					},
				},
				IncludeRowCount: datadog.PtrBool(true),
				Limit:           datadog.PtrInt64(25),
				Query:           datadog.PtrString("user_org_id:5001 AND first_country_code:US AND first_browser_name:Chrome"),
				SelectColumns: []string{
					"user_id",
					"user_email",
					"first_country_code",
					"first_browser_name",
					"events_count",
					"session_count",
					"error_count",
					"avg_loading_time",
				},
			},
			Id:   datadog.PtrString("query_event_filtered_users_request"),
			Type: datadogV2.QUERYEVENTFILTEREDUSERSREQUESTDATATYPE_QUERY_EVENT_FILTERED_USERS_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.QueryEventFilteredUsers", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	resp, r, err := api.QueryEventFilteredUsers(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.QueryEventFilteredUsers`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumAudienceManagementApi.QueryEventFilteredUsers`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Query event filtered users
```
// Query event filtered users returns "Successful response with filtered user data" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.QueryEventFilteredUsersRequest;
import com.datadog.api.client.v2.model.QueryEventFilteredUsersRequestData;
import com.datadog.api.client.v2.model.QueryEventFilteredUsersRequestDataAttributes;
import com.datadog.api.client.v2.model.QueryEventFilteredUsersRequestDataAttributesEventQuery;
import com.datadog.api.client.v2.model.QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame;
import com.datadog.api.client.v2.model.QueryEventFilteredUsersRequestDataType;
import com.datadog.api.client.v2.model.QueryResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.queryEventFilteredUsers", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    QueryEventFilteredUsersRequest body =
        new QueryEventFilteredUsersRequest()
            .data(
                new QueryEventFilteredUsersRequestData()
                    .attributes(
                        new QueryEventFilteredUsersRequestDataAttributes()
                            .eventQuery(
                                new QueryEventFilteredUsersRequestDataAttributesEventQuery()
                                    .query(
                                        "@type:view AND @view.loading_time:>3000 AND"
                                            + " @application.name:ecommerce-platform")
                                    .timeFrame(
                                        new QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame()
                                            .end(1761309676L)
                                            .start(1760100076L)))
                            .includeRowCount(true)
                            .limit(25L)
                            .query(
                                "user_org_id:5001 AND first_country_code:US AND"
                                    + " first_browser_name:Chrome")
                            .selectColumns(
                                Arrays.asList(
                                    "user_id",
                                    "user_email",
                                    "first_country_code",
                                    "first_browser_name",
                                    "events_count",
                                    "session_count",
                                    "error_count",
                                    "avg_loading_time")))
                    .id("query_event_filtered_users_request")
                    .type(
                        QueryEventFilteredUsersRequestDataType.QUERY_EVENT_FILTERED_USERS_REQUEST));

    try {
      QueryResponse result = apiInstance.queryEventFilteredUsers(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#queryEventFilteredUsers");
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

#####  Query event filtered users
```
// Query event filtered users returns "Successful response with filtered user
// data" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;
use datadog_api_client::datadogV2::model::QueryEventFilteredUsersRequest;
use datadog_api_client::datadogV2::model::QueryEventFilteredUsersRequestData;
use datadog_api_client::datadogV2::model::QueryEventFilteredUsersRequestDataAttributes;
use datadog_api_client::datadogV2::model::QueryEventFilteredUsersRequestDataAttributesEventQuery;
use datadog_api_client::datadogV2::model::QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame;
use datadog_api_client::datadogV2::model::QueryEventFilteredUsersRequestDataType;

#[tokio::main]
async fn main() {
    let body =
        QueryEventFilteredUsersRequest
        ::new().data(
            QueryEventFilteredUsersRequestData::new(
                QueryEventFilteredUsersRequestDataType::QUERY_EVENT_FILTERED_USERS_REQUEST,
            )
                .attributes(
                    QueryEventFilteredUsersRequestDataAttributes::new()
                        .event_query(
                            QueryEventFilteredUsersRequestDataAttributesEventQuery::new()
                                .query(
                                    "@type:view AND @view.loading_time:>3000 AND @application.name:ecommerce-platform".to_string(),
                                )
                                .time_frame(
                                    QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame::new()
                                        .end(1761309676)
                                        .start(1760100076),
                                ),
                        )
                        .include_row_count(true)
                        .limit(25)
                        .query("user_org_id:5001 AND first_country_code:US AND first_browser_name:Chrome".to_string())
                        .select_columns(
                            vec![
                                "user_id".to_string(),
                                "user_email".to_string(),
                                "first_country_code".to_string(),
                                "first_browser_name".to_string(),
                                "events_count".to_string(),
                                "session_count".to_string(),
                                "error_count".to_string(),
                                "avg_loading_time".to_string()
                            ],
                        ),
                )
                .id("query_event_filtered_users_request".to_string()),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.QueryEventFilteredUsers", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.query_event_filtered_users(body).await;
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

#####  Query event filtered users
```
/**
 * Query event filtered users returns "Successful response with filtered user data" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.queryEventFilteredUsers"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiQueryEventFilteredUsersRequest = {
  body: {
    data: {
      attributes: {
        eventQuery: {
          query:
            "@type:view AND @view.loading_time:>3000 AND @application.name:ecommerce-platform",
          timeFrame: {
            end: 1761309676,
            start: 1760100076,
          },
        },
        includeRowCount: true,
        limit: 25,
        query:
          "user_org_id:5001 AND first_country_code:US AND first_browser_name:Chrome",
        selectColumns: [
          "user_id",
          "user_email",
          "first_country_code",
          "first_browser_name",
          "events_count",
          "session_count",
          "error_count",
          "avg_loading_time",
        ],
      },
      id: "query_event_filtered_users_request",
      type: "query_event_filtered_users_request",
    },
  },
};

apiInstance
  .queryEventFilteredUsers(params)
  .then((data: v2.QueryResponse) => {
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
## [Get account facet info](https://docs.datadoghq.com/api/latest/rum-audience-management/#get-account-facet-info)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#get-account-facet-info-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/product-analytics/accounts/facet_infohttps://api.ap2.datadoghq.com/api/v2/product-analytics/accounts/facet_infohttps://api.datadoghq.eu/api/v2/product-analytics/accounts/facet_infohttps://api.ddog-gov.com/api/v2/product-analytics/accounts/facet_infohttps://api.datadoghq.com/api/v2/product-analytics/accounts/facet_infohttps://api.us3.datadoghq.com/api/v2/product-analytics/accounts/facet_infohttps://api.us5.datadoghq.com/api/v2/product-analytics/accounts/facet_info
### Overview
Get facet information for account attributes including possible values and counts
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
facet_id [_required_]
string
limit [_required_]
int64
search
object
query
string
term_search
object
value
string
id
string
type [_required_]
enum
Users facet info request resource type. Allowed enum values: `users_facet_info_request`
default: `users_facet_info_request`
```
{
  "data": {
    "attributes": {
      "facet_id": "",
      "limit": 0,
      "search": {
        "query": "string"
      },
      "term_search": {
        "value": "string"
      }
    },
    "id": "string",
    "type": "users_facet_info_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#GetAccountFacetInfo-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#GetAccountFacetInfo-429-v2)


Successful response with facet information
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
result
object
range
object
max
object
min
object
values
[object]
count
int64
value
string
id
string
type [_required_]
enum
Users facet info resource type. Allowed enum values: `users_facet_info`
default: `users_facet_info`
```
{
  "data": {
    "attributes": {
      "result": {
        "values": [
          {
            "count": 4892,
            "value": "Chrome"
          },
          {
            "count": 2341,
            "value": "Safari"
          },
          {
            "count": 1567,
            "value": "Firefox"
          },
          {
            "count": 892,
            "value": "Edge"
          },
          {
            "count": 234,
            "value": "Opera"
          }
        ]
      }
    },
    "id": "facet_info_response",
    "type": "users_facet_info"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Get account facet info
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/accounts/facet_info" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "facet_id": "",
      "limit": 0
    },
    "type": "users_facet_info_request"
  }
}
EOF  

                
```

#####  Get account facet info
```
"""
Get account facet info returns "Successful response with facet information" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.facet_info_request import FacetInfoRequest
from datadog_api_client.v2.model.facet_info_request_data import FacetInfoRequestData
from datadog_api_client.v2.model.facet_info_request_data_attributes import FacetInfoRequestDataAttributes
from datadog_api_client.v2.model.facet_info_request_data_attributes_search import FacetInfoRequestDataAttributesSearch
from datadog_api_client.v2.model.facet_info_request_data_attributes_term_search import (
    FacetInfoRequestDataAttributesTermSearch,
)
from datadog_api_client.v2.model.facet_info_request_data_type import FacetInfoRequestDataType

body = FacetInfoRequest(
    data=FacetInfoRequestData(
        attributes=FacetInfoRequestDataAttributes(
            facet_id="first_browser_name",
            limit=10,
            search=FacetInfoRequestDataAttributesSearch(
                query="user_org_id:5001 AND first_country_code:US",
            ),
            term_search=FacetInfoRequestDataAttributesTermSearch(
                value="Chrome",
            ),
        ),
        id="facet_info_request",
        type=FacetInfoRequestDataType.USERS_FACET_INFO_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_account_facet_info"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.get_account_facet_info(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get account facet info
```
# Get account facet info returns "Successful response with facet information" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_account_facet_info".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new

body = DatadogAPIClient::V2::FacetInfoRequest.new({
  data: DatadogAPIClient::V2::FacetInfoRequestData.new({
    attributes: DatadogAPIClient::V2::FacetInfoRequestDataAttributes.new({
      facet_id: "first_browser_name",
      limit: 10,
      search: DatadogAPIClient::V2::FacetInfoRequestDataAttributesSearch.new({
        query: "user_org_id:5001 AND first_country_code:US",
      }),
      term_search: DatadogAPIClient::V2::FacetInfoRequestDataAttributesTermSearch.new({
        value: "Chrome",
      }),
    }),
    id: "facet_info_request",
    type: DatadogAPIClient::V2::FacetInfoRequestDataType::USERS_FACET_INFO_REQUEST,
  }),
})
p api_instance.get_account_facet_info(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get account facet info
```
// Get account facet info returns "Successful response with facet information" response

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
	body := datadogV2.FacetInfoRequest{
		Data: &datadogV2.FacetInfoRequestData{
			Attributes: &datadogV2.FacetInfoRequestDataAttributes{
				FacetId: "first_browser_name",
				Limit:   10,
				Search: &datadogV2.FacetInfoRequestDataAttributesSearch{
					Query: datadog.PtrString("user_org_id:5001 AND first_country_code:US"),
				},
				TermSearch: &datadogV2.FacetInfoRequestDataAttributesTermSearch{
					Value: datadog.PtrString("Chrome"),
				},
			},
			Id:   datadog.PtrString("facet_info_request"),
			Type: datadogV2.FACETINFOREQUESTDATATYPE_USERS_FACET_INFO_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetAccountFacetInfo", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	resp, r, err := api.GetAccountFacetInfo(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.GetAccountFacetInfo`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumAudienceManagementApi.GetAccountFacetInfo`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get account facet info
```
// Get account facet info returns "Successful response with facet information" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.FacetInfoRequest;
import com.datadog.api.client.v2.model.FacetInfoRequestData;
import com.datadog.api.client.v2.model.FacetInfoRequestDataAttributes;
import com.datadog.api.client.v2.model.FacetInfoRequestDataAttributesSearch;
import com.datadog.api.client.v2.model.FacetInfoRequestDataAttributesTermSearch;
import com.datadog.api.client.v2.model.FacetInfoRequestDataType;
import com.datadog.api.client.v2.model.FacetInfoResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getAccountFacetInfo", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    FacetInfoRequest body =
        new FacetInfoRequest()
            .data(
                new FacetInfoRequestData()
                    .attributes(
                        new FacetInfoRequestDataAttributes()
                            .facetId("first_browser_name")
                            .limit(10L)
                            .search(
                                new FacetInfoRequestDataAttributesSearch()
                                    .query("user_org_id:5001 AND first_country_code:US"))
                            .termSearch(
                                new FacetInfoRequestDataAttributesTermSearch().value("Chrome")))
                    .id("facet_info_request")
                    .type(FacetInfoRequestDataType.USERS_FACET_INFO_REQUEST));

    try {
      FacetInfoResponse result = apiInstance.getAccountFacetInfo(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#getAccountFacetInfo");
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

#####  Get account facet info
```
// Get account facet info returns "Successful response with facet information"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;
use datadog_api_client::datadogV2::model::FacetInfoRequest;
use datadog_api_client::datadogV2::model::FacetInfoRequestData;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataAttributes;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataAttributesSearch;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataAttributesTermSearch;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataType;

#[tokio::main]
async fn main() {
    let body = FacetInfoRequest::new().data(
        FacetInfoRequestData::new(FacetInfoRequestDataType::USERS_FACET_INFO_REQUEST)
            .attributes(
                FacetInfoRequestDataAttributes::new("first_browser_name".to_string(), 10)
                    .search(
                        FacetInfoRequestDataAttributesSearch::new()
                            .query("user_org_id:5001 AND first_country_code:US".to_string()),
                    )
                    .term_search(
                        FacetInfoRequestDataAttributesTermSearch::new().value("Chrome".to_string()),
                    ),
            )
            .id("facet_info_request".to_string()),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetAccountFacetInfo", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.get_account_facet_info(body).await;
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

#####  Get account facet info
```
/**
 * Get account facet info returns "Successful response with facet information" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getAccountFacetInfo"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiGetAccountFacetInfoRequest = {
  body: {
    data: {
      attributes: {
        facetId: "first_browser_name",
        limit: 10,
        search: {
          query: "user_org_id:5001 AND first_country_code:US",
        },
        termSearch: {
          value: "Chrome",
        },
      },
      id: "facet_info_request",
      type: "users_facet_info_request",
    },
  },
};

apiInstance
  .getAccountFacetInfo(params)
  .then((data: v2.FacetInfoResponse) => {
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
## [Delete connection](https://docs.datadoghq.com/api/latest/rum-audience-management/#delete-connection)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#delete-connection-v2)


**Note** : This endpoint may be subject to changes.
DELETE https://api.ap1.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connection/{id}https://api.ap2.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connection/{id}https://api.datadoghq.eu/api/v2/product-analytics/{entity}/mapping/connection/{id}https://api.ddog-gov.com/api/v2/product-analytics/{entity}/mapping/connection/{id}https://api.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connection/{id}https://api.us3.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connection/{id}https://api.us5.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connection/{id}
### Overview
Delete an existing data connection for an entity
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The connection ID to delete
entity [_required_]
string
The entity for which to delete the connection
### Response
  * [204](https://docs.datadoghq.com/api/latest/rum-audience-management/#DeleteConnection-204-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#DeleteConnection-429-v2)


Connection deleted successfully
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Delete connection
Copy
```
                  # Path parameters  
export id="connection-id-123"  
export entity="users"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/${entity}/mapping/connection/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete connection
```
"""
Delete connection returns "Connection deleted successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi

configuration = Configuration()
configuration.unstable_operations["delete_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    api_instance.delete_connection(
        id="connection-id-123",
        entity="users",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete connection
```
# Delete connection returns "Connection deleted successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_connection".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new
api_instance.delete_connection("connection-id-123", "users")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete connection
```
// Delete connection returns "Connection deleted successfully" response

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
	configuration.SetUnstableOperationEnabled("v2.DeleteConnection", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	r, err := api.DeleteConnection(ctx, "connection-id-123", "users")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.DeleteConnection`: %v\n", err)
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

#####  Delete connection
```
// Delete connection returns "Connection deleted successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteConnection", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    try {
      apiInstance.deleteConnection("connection-id-123", "users");
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#deleteConnection");
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

#####  Delete connection
```
// Delete connection returns "Connection deleted successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteConnection", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api
        .delete_connection("connection-id-123".to_string(), "users".to_string())
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

#####  Delete connection
```
/**
 * Delete connection returns "Connection deleted successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteConnection"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiDeleteConnectionRequest = {
  id: "connection-id-123",
  entity: "users",
};

apiInstance
  .deleteConnection(params)
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
## [List connections](https://docs.datadoghq.com/api/latest/rum-audience-management/#list-connections)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#list-connections-v2)


**Note** : This endpoint may be subject to changes.
GET https://api.ap1.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionshttps://api.ap2.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionshttps://api.datadoghq.eu/api/v2/product-analytics/{entity}/mapping/connectionshttps://api.ddog-gov.com/api/v2/product-analytics/{entity}/mapping/connectionshttps://api.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionshttps://api.us3.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connectionshttps://api.us5.datadoghq.com/api/v2/product-analytics/{entity}/mapping/connections
### Overview
List all data connections for an entity
### Arguments
#### Path Parameters
Name
Type
Description
entity [_required_]
string
The entity for which to list connections
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#ListConnections-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#ListConnections-429-v2)


Successful response with list of connections
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
connections
[object]
created_at
date-time
created_by
string
fields
[object]
description
string
display_name
string
groups
[string]
id [_required_]
string
source_name [_required_]
string
type [_required_]
string
id
string
join
object
attribute
string
type
string
metadata
object
<any-key>
string
type
string
updated_at
date-time
updated_by
string
id
string
type [_required_]
enum
List connections response resource type. Allowed enum values: `list_connections_response`
default: `list_connections_response`
```
{
  "data": {
    "attributes": {
      "connections": [
        {
          "created_at": "0001-01-01T00:00:00Z",
          "created_by": "00000000-0000-0000-0000-000000000000",
          "fields": [
            {
              "description": "Customer subscription tier",
              "display_name": "Customer Tier",
              "groups": [
                "Business",
                "Subscription"
              ],
              "id": "customer_tier",
              "source_name": "subscription_tier",
              "type": "string"
            },
            {
              "description": "Channel through which user signed up",
              "display_name": "Signup Source",
              "groups": [
                "Marketing",
                "Attribution"
              ],
              "id": "signup_source",
              "source_name": "acquisition_channel",
              "type": "string"
            }
          ],
          "id": "user-profiles-connection",
          "join": {
            "attribute": "user_email",
            "type": "email"
          },
          "type": "ref_table",
          "updated_at": "0001-01-01T00:00:00Z",
          "updated_by": "00000000-0000-0000-0000-000000000000"
        }
      ]
    },
    "id": "list_connections_response",
    "type": "list_connections_response"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  List connections
Copy
```
                  # Path parameters  
export entity="users"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/${entity}/mapping/connections" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List connections
```
"""
List connections returns "Successful response with list of connections" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi

configuration = Configuration()
configuration.unstable_operations["list_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.list_connections(
        entity="users",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List connections
```
# List connections returns "Successful response with list of connections" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_connections".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new
p api_instance.list_connections("users")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List connections
```
// List connections returns "Successful response with list of connections" response

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
	configuration.SetUnstableOperationEnabled("v2.ListConnections", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	resp, r, err := api.ListConnections(ctx, "users")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.ListConnections`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumAudienceManagementApi.ListConnections`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List connections
```
// List connections returns "Successful response with list of connections" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.ListConnectionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listConnections", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    try {
      ListConnectionsResponse result = apiInstance.listConnections("users");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#listConnections");
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

#####  List connections
```
// List connections returns "Successful response with list of connections" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListConnections", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.list_connections("users".to_string()).await;
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

#####  List connections
```
/**
 * List connections returns "Successful response with list of connections" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listConnections"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiListConnectionsRequest = {
  entity: "users",
};

apiInstance
  .listConnections(params)
  .then((data: v2.ListConnectionsResponse) => {
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
## [Query users](https://docs.datadoghq.com/api/latest/rum-audience-management/#query-users)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#query-users-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/product-analytics/users/queryhttps://api.ap2.datadoghq.com/api/v2/product-analytics/users/queryhttps://api.datadoghq.eu/api/v2/product-analytics/users/queryhttps://api.ddog-gov.com/api/v2/product-analytics/users/queryhttps://api.datadoghq.com/api/v2/product-analytics/users/queryhttps://api.us3.datadoghq.com/api/v2/product-analytics/users/queryhttps://api.us5.datadoghq.com/api/v2/product-analytics/users/query
### Overview
Query users with flexible filtering by user properties, with optional wildcard search
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
limit
int64
query
string
select_columns
[string]
sort
object
field
string
order
string
wildcard_search_term
string
id
string
type [_required_]
enum
Query users request resource type. Allowed enum values: `query_users_request`
default: `query_users_request`
```
{
  "data": {
    "attributes": {
      "limit": "integer",
      "query": "string",
      "select_columns": [],
      "sort": {
        "field": "string",
        "order": "string"
      },
      "wildcard_search_term": "string"
    },
    "id": "string",
    "type": "query_users_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#QueryUsers-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#QueryUsers-429-v2)


Successful response with user data
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
hits
[]
total
int64
id
string
type [_required_]
enum
Query response resource type. Allowed enum values: `query_response`
default: `query_response`
```
{
  "data": {
    "attributes": {
      "hits": [
        {
          "first_browser_name": "Chrome",
          "first_city": "San Francisco",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T06:45:12.142Z",
          "session_count": 47,
          "user_created": "2024-12-15T08:42:33.287Z",
          "user_email": "john.smith@techcorp.com",
          "user_id": "150847",
          "user_name": "John Smith",
          "user_org_id": "5001"
        },
        {
          "first_browser_name": "Chrome",
          "first_city": "Austin",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T05:22:08.951Z",
          "session_count": 89,
          "user_created": "2024-11-28T14:17:45.634Z",
          "user_email": "john.williams@techcorp.com",
          "user_id": "150848",
          "user_name": "John Williams",
          "user_org_id": "5001"
        },
        {
          "first_browser_name": "Chrome",
          "first_city": "Seattle",
          "first_country_code": "US",
          "first_device_type": "Desktop",
          "last_seen": "2025-08-14T04:18:34.726Z",
          "session_count": 23,
          "user_created": "2025-01-03T16:33:21.445Z",
          "user_email": "john.jones@techcorp.com",
          "user_id": "150849",
          "user_name": "John Jones",
          "user_org_id": "5001"
        }
      ],
      "total": 147
    },
    "id": "query_response",
    "type": "query_response"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Query users
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/users/query" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "query_users_request"
  }
}
EOF  

                
```

#####  Query users
```
"""
Query users returns "Successful response with user data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.query_users_request import QueryUsersRequest
from datadog_api_client.v2.model.query_users_request_data import QueryUsersRequestData
from datadog_api_client.v2.model.query_users_request_data_attributes import QueryUsersRequestDataAttributes
from datadog_api_client.v2.model.query_users_request_data_attributes_sort import QueryUsersRequestDataAttributesSort
from datadog_api_client.v2.model.query_users_request_data_type import QueryUsersRequestDataType

body = QueryUsersRequest(
    data=QueryUsersRequestData(
        attributes=QueryUsersRequestDataAttributes(
            limit=25,
            query="user_email:*@techcorp.com AND first_country_code:US AND first_browser_name:Chrome",
            select_columns=[
                "user_id",
                "user_email",
                "user_name",
                "user_org_id",
                "first_country_code",
                "first_browser_name",
                "first_device_type",
                "last_seen",
            ],
            sort=QueryUsersRequestDataAttributesSort(
                field="first_seen",
                order="DESC",
            ),
            wildcard_search_term="john",
        ),
        id="query_users_request",
        type=QueryUsersRequestDataType.QUERY_USERS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_users"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.query_users(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Query users
```
# Query users returns "Successful response with user data" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.query_users".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new

body = DatadogAPIClient::V2::QueryUsersRequest.new({
  data: DatadogAPIClient::V2::QueryUsersRequestData.new({
    attributes: DatadogAPIClient::V2::QueryUsersRequestDataAttributes.new({
      limit: 25,
      query: "user_email:*@techcorp.com AND first_country_code:US AND first_browser_name:Chrome",
      select_columns: [
        "user_id",
        "user_email",
        "user_name",
        "user_org_id",
        "first_country_code",
        "first_browser_name",
        "first_device_type",
        "last_seen",
      ],
      sort: DatadogAPIClient::V2::QueryUsersRequestDataAttributesSort.new({
        field: "first_seen",
        order: "DESC",
      }),
      wildcard_search_term: "john",
    }),
    id: "query_users_request",
    type: DatadogAPIClient::V2::QueryUsersRequestDataType::QUERY_USERS_REQUEST,
  }),
})
p api_instance.query_users(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Query users
```
// Query users returns "Successful response with user data" response

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
	body := datadogV2.QueryUsersRequest{
		Data: &datadogV2.QueryUsersRequestData{
			Attributes: &datadogV2.QueryUsersRequestDataAttributes{
				Limit: datadog.PtrInt64(25),
				Query: datadog.PtrString("user_email:*@techcorp.com AND first_country_code:US AND first_browser_name:Chrome"),
				SelectColumns: []string{
					"user_id",
					"user_email",
					"user_name",
					"user_org_id",
					"first_country_code",
					"first_browser_name",
					"first_device_type",
					"last_seen",
				},
				Sort: &datadogV2.QueryUsersRequestDataAttributesSort{
					Field: datadog.PtrString("first_seen"),
					Order: datadog.PtrString("DESC"),
				},
				WildcardSearchTerm: datadog.PtrString("john"),
			},
			Id:   datadog.PtrString("query_users_request"),
			Type: datadogV2.QUERYUSERSREQUESTDATATYPE_QUERY_USERS_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.QueryUsers", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	resp, r, err := api.QueryUsers(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.QueryUsers`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumAudienceManagementApi.QueryUsers`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Query users
```
// Query users returns "Successful response with user data" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.QueryResponse;
import com.datadog.api.client.v2.model.QueryUsersRequest;
import com.datadog.api.client.v2.model.QueryUsersRequestData;
import com.datadog.api.client.v2.model.QueryUsersRequestDataAttributes;
import com.datadog.api.client.v2.model.QueryUsersRequestDataAttributesSort;
import com.datadog.api.client.v2.model.QueryUsersRequestDataType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.queryUsers", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    QueryUsersRequest body =
        new QueryUsersRequest()
            .data(
                new QueryUsersRequestData()
                    .attributes(
                        new QueryUsersRequestDataAttributes()
                            .limit(25L)
                            .query(
                                "user_email:*@techcorp.com AND first_country_code:US AND"
                                    + " first_browser_name:Chrome")
                            .selectColumns(
                                Arrays.asList(
                                    "user_id",
                                    "user_email",
                                    "user_name",
                                    "user_org_id",
                                    "first_country_code",
                                    "first_browser_name",
                                    "first_device_type",
                                    "last_seen"))
                            .sort(
                                new QueryUsersRequestDataAttributesSort()
                                    .field("first_seen")
                                    .order("DESC"))
                            .wildcardSearchTerm("john"))
                    .id("query_users_request")
                    .type(QueryUsersRequestDataType.QUERY_USERS_REQUEST));

    try {
      QueryResponse result = apiInstance.queryUsers(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#queryUsers");
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

#####  Query users
```
// Query users returns "Successful response with user data" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;
use datadog_api_client::datadogV2::model::QueryUsersRequest;
use datadog_api_client::datadogV2::model::QueryUsersRequestData;
use datadog_api_client::datadogV2::model::QueryUsersRequestDataAttributes;
use datadog_api_client::datadogV2::model::QueryUsersRequestDataAttributesSort;
use datadog_api_client::datadogV2::model::QueryUsersRequestDataType;

#[tokio::main]
async fn main() {
    let body =
        QueryUsersRequest
        ::new().data(
            QueryUsersRequestData::new(QueryUsersRequestDataType::QUERY_USERS_REQUEST)
                .attributes(
                    QueryUsersRequestDataAttributes::new()
                        .limit(25)
                        .query(
                            "user_email:*@techcorp.com AND first_country_code:US AND first_browser_name:Chrome".to_string(),
                        )
                        .select_columns(
                            vec![
                                "user_id".to_string(),
                                "user_email".to_string(),
                                "user_name".to_string(),
                                "user_org_id".to_string(),
                                "first_country_code".to_string(),
                                "first_browser_name".to_string(),
                                "first_device_type".to_string(),
                                "last_seen".to_string()
                            ],
                        )
                        .sort(
                            QueryUsersRequestDataAttributesSort::new()
                                .field("first_seen".to_string())
                                .order("DESC".to_string()),
                        )
                        .wildcard_search_term("john".to_string()),
                )
                .id("query_users_request".to_string()),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.QueryUsers", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.query_users(body).await;
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

#####  Query users
```
/**
 * Query users returns "Successful response with user data" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.queryUsers"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiQueryUsersRequest = {
  body: {
    data: {
      attributes: {
        limit: 25,
        query:
          "user_email:*@techcorp.com AND first_country_code:US AND first_browser_name:Chrome",
        selectColumns: [
          "user_id",
          "user_email",
          "user_name",
          "user_org_id",
          "first_country_code",
          "first_browser_name",
          "first_device_type",
          "last_seen",
        ],
        sort: {
          field: "first_seen",
          order: "DESC",
        },
        wildcardSearchTerm: "john",
      },
      id: "query_users_request",
      type: "query_users_request",
    },
  },
};

apiInstance
  .queryUsers(params)
  .then((data: v2.QueryResponse) => {
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
## [Get user facet info](https://docs.datadoghq.com/api/latest/rum-audience-management/#get-user-facet-info)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#get-user-facet-info-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/product-analytics/users/facet_infohttps://api.ap2.datadoghq.com/api/v2/product-analytics/users/facet_infohttps://api.datadoghq.eu/api/v2/product-analytics/users/facet_infohttps://api.ddog-gov.com/api/v2/product-analytics/users/facet_infohttps://api.datadoghq.com/api/v2/product-analytics/users/facet_infohttps://api.us3.datadoghq.com/api/v2/product-analytics/users/facet_infohttps://api.us5.datadoghq.com/api/v2/product-analytics/users/facet_info
### Overview
Get facet information for user attributes including possible values and counts
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
facet_id [_required_]
string
limit [_required_]
int64
search
object
query
string
term_search
object
value
string
id
string
type [_required_]
enum
Users facet info request resource type. Allowed enum values: `users_facet_info_request`
default: `users_facet_info_request`
```
{
  "data": {
    "attributes": {
      "facet_id": "",
      "limit": 0,
      "search": {
        "query": "string"
      },
      "term_search": {
        "value": "string"
      }
    },
    "id": "string",
    "type": "users_facet_info_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#GetUserFacetInfo-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#GetUserFacetInfo-429-v2)


Successful response with facet information
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
result
object
range
object
max
object
min
object
values
[object]
count
int64
value
string
id
string
type [_required_]
enum
Users facet info resource type. Allowed enum values: `users_facet_info`
default: `users_facet_info`
```
{
  "data": {
    "attributes": {
      "result": {
        "values": [
          {
            "count": 4892,
            "value": "Chrome"
          },
          {
            "count": 2341,
            "value": "Safari"
          },
          {
            "count": 1567,
            "value": "Firefox"
          },
          {
            "count": 892,
            "value": "Edge"
          },
          {
            "count": 234,
            "value": "Opera"
          }
        ]
      }
    },
    "id": "facet_info_response",
    "type": "users_facet_info"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Get user facet info
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/users/facet_info" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "facet_id": "",
      "limit": 0
    },
    "type": "users_facet_info_request"
  }
}
EOF  

                
```

#####  Get user facet info
```
"""
Get user facet info returns "Successful response with facet information" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.facet_info_request import FacetInfoRequest
from datadog_api_client.v2.model.facet_info_request_data import FacetInfoRequestData
from datadog_api_client.v2.model.facet_info_request_data_attributes import FacetInfoRequestDataAttributes
from datadog_api_client.v2.model.facet_info_request_data_attributes_search import FacetInfoRequestDataAttributesSearch
from datadog_api_client.v2.model.facet_info_request_data_attributes_term_search import (
    FacetInfoRequestDataAttributesTermSearch,
)
from datadog_api_client.v2.model.facet_info_request_data_type import FacetInfoRequestDataType

body = FacetInfoRequest(
    data=FacetInfoRequestData(
        attributes=FacetInfoRequestDataAttributes(
            facet_id="first_browser_name",
            limit=10,
            search=FacetInfoRequestDataAttributesSearch(
                query="user_org_id:5001 AND first_country_code:US",
            ),
            term_search=FacetInfoRequestDataAttributesTermSearch(
                value="Chrome",
            ),
        ),
        id="facet_info_request",
        type=FacetInfoRequestDataType.USERS_FACET_INFO_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_user_facet_info"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.get_user_facet_info(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get user facet info
```
# Get user facet info returns "Successful response with facet information" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_user_facet_info".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new

body = DatadogAPIClient::V2::FacetInfoRequest.new({
  data: DatadogAPIClient::V2::FacetInfoRequestData.new({
    attributes: DatadogAPIClient::V2::FacetInfoRequestDataAttributes.new({
      facet_id: "first_browser_name",
      limit: 10,
      search: DatadogAPIClient::V2::FacetInfoRequestDataAttributesSearch.new({
        query: "user_org_id:5001 AND first_country_code:US",
      }),
      term_search: DatadogAPIClient::V2::FacetInfoRequestDataAttributesTermSearch.new({
        value: "Chrome",
      }),
    }),
    id: "facet_info_request",
    type: DatadogAPIClient::V2::FacetInfoRequestDataType::USERS_FACET_INFO_REQUEST,
  }),
})
p api_instance.get_user_facet_info(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get user facet info
```
// Get user facet info returns "Successful response with facet information" response

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
	body := datadogV2.FacetInfoRequest{
		Data: &datadogV2.FacetInfoRequestData{
			Attributes: &datadogV2.FacetInfoRequestDataAttributes{
				FacetId: "first_browser_name",
				Limit:   10,
				Search: &datadogV2.FacetInfoRequestDataAttributesSearch{
					Query: datadog.PtrString("user_org_id:5001 AND first_country_code:US"),
				},
				TermSearch: &datadogV2.FacetInfoRequestDataAttributesTermSearch{
					Value: datadog.PtrString("Chrome"),
				},
			},
			Id:   datadog.PtrString("facet_info_request"),
			Type: datadogV2.FACETINFOREQUESTDATATYPE_USERS_FACET_INFO_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetUserFacetInfo", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	resp, r, err := api.GetUserFacetInfo(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.GetUserFacetInfo`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumAudienceManagementApi.GetUserFacetInfo`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get user facet info
```
// Get user facet info returns "Successful response with facet information" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.FacetInfoRequest;
import com.datadog.api.client.v2.model.FacetInfoRequestData;
import com.datadog.api.client.v2.model.FacetInfoRequestDataAttributes;
import com.datadog.api.client.v2.model.FacetInfoRequestDataAttributesSearch;
import com.datadog.api.client.v2.model.FacetInfoRequestDataAttributesTermSearch;
import com.datadog.api.client.v2.model.FacetInfoRequestDataType;
import com.datadog.api.client.v2.model.FacetInfoResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getUserFacetInfo", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    FacetInfoRequest body =
        new FacetInfoRequest()
            .data(
                new FacetInfoRequestData()
                    .attributes(
                        new FacetInfoRequestDataAttributes()
                            .facetId("first_browser_name")
                            .limit(10L)
                            .search(
                                new FacetInfoRequestDataAttributesSearch()
                                    .query("user_org_id:5001 AND first_country_code:US"))
                            .termSearch(
                                new FacetInfoRequestDataAttributesTermSearch().value("Chrome")))
                    .id("facet_info_request")
                    .type(FacetInfoRequestDataType.USERS_FACET_INFO_REQUEST));

    try {
      FacetInfoResponse result = apiInstance.getUserFacetInfo(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#getUserFacetInfo");
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

#####  Get user facet info
```
// Get user facet info returns "Successful response with facet information"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;
use datadog_api_client::datadogV2::model::FacetInfoRequest;
use datadog_api_client::datadogV2::model::FacetInfoRequestData;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataAttributes;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataAttributesSearch;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataAttributesTermSearch;
use datadog_api_client::datadogV2::model::FacetInfoRequestDataType;

#[tokio::main]
async fn main() {
    let body = FacetInfoRequest::new().data(
        FacetInfoRequestData::new(FacetInfoRequestDataType::USERS_FACET_INFO_REQUEST)
            .attributes(
                FacetInfoRequestDataAttributes::new("first_browser_name".to_string(), 10)
                    .search(
                        FacetInfoRequestDataAttributesSearch::new()
                            .query("user_org_id:5001 AND first_country_code:US".to_string()),
                    )
                    .term_search(
                        FacetInfoRequestDataAttributesTermSearch::new().value("Chrome".to_string()),
                    ),
            )
            .id("facet_info_request".to_string()),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetUserFacetInfo", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.get_user_facet_info(body).await;
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

#####  Get user facet info
```
/**
 * Get user facet info returns "Successful response with facet information" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getUserFacetInfo"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiGetUserFacetInfoRequest = {
  body: {
    data: {
      attributes: {
        facetId: "first_browser_name",
        limit: 10,
        search: {
          query: "user_org_id:5001 AND first_country_code:US",
        },
        termSearch: {
          value: "Chrome",
        },
      },
      id: "facet_info_request",
      type: "users_facet_info_request",
    },
  },
};

apiInstance
  .getUserFacetInfo(params)
  .then((data: v2.FacetInfoResponse) => {
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
## [Get mapping](https://docs.datadoghq.com/api/latest/rum-audience-management/#get-mapping)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/rum-audience-management/#get-mapping-v2)


**Note** : This endpoint may be subject to changes.
GET https://api.ap1.datadoghq.com/api/v2/product-analytics/{entity}/mappinghttps://api.ap2.datadoghq.com/api/v2/product-analytics/{entity}/mappinghttps://api.datadoghq.eu/api/v2/product-analytics/{entity}/mappinghttps://api.ddog-gov.com/api/v2/product-analytics/{entity}/mappinghttps://api.datadoghq.com/api/v2/product-analytics/{entity}/mappinghttps://api.us3.datadoghq.com/api/v2/product-analytics/{entity}/mappinghttps://api.us5.datadoghq.com/api/v2/product-analytics/{entity}/mapping
### Overview
Get entity mapping configuration including all available attributes and their properties
### Arguments
#### Path Parameters
Name
Type
Description
entity [_required_]
string
The entity for which to get the mapping
### Response
  * [200](https://docs.datadoghq.com/api/latest/rum-audience-management/#GetMapping-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/rum-audience-management/#GetMapping-429-v2)


Successful response with entity mapping configuration
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


Field
Type
Description
data
object
attributes
object
attributes
[object]
attribute
string
description
string
display_name
string
groups
[string]
is_custom
boolean
type
string
id
string
type [_required_]
enum
Get mappings response resource type. Allowed enum values: `get_mappings_response`
default: `get_mappings_response`
```
{
  "data": {
    "attributes": {
      "attributes": [
        {
          "attribute": "user_id",
          "description": "Unique user identifier",
          "display_name": "User ID",
          "groups": [
            "Identity"
          ],
          "is_custom": false,
          "type": "string"
        },
        {
          "attribute": "user_email",
          "description": "User email address",
          "display_name": "Email Address",
          "groups": [
            "Identity",
            "Contact"
          ],
          "is_custom": false,
          "type": "string"
        },
        {
          "attribute": "first_country_code",
          "description": "The ISO code of the country for the user's first session",
          "display_name": "First Country Code",
          "groups": [
            "Geography"
          ],
          "is_custom": false,
          "type": "string"
        },
        {
          "attribute": "@customer_tier",
          "description": "Customer subscription tier",
          "display_name": "Customer Tier",
          "groups": [
            "Business"
          ],
          "is_custom": true,
          "type": "string"
        }
      ]
    },
    "id": "get_mappings_response",
    "type": "get_mappings_response"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/rum-audience-management/)
  * [Example](https://docs.datadoghq.com/api/latest/rum-audience-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/rum-audience-management/?code-lang=typescript)


#####  Get mapping
Copy
```
                  # Path parameters  
export entity="users"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/product-analytics/${entity}/mapping" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get mapping
```
"""
Get mapping returns "Successful response with entity mapping configuration" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi

configuration = Configuration()
configuration.unstable_operations["get_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.get_mapping(
        entity="users",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get mapping
```
# Get mapping returns "Successful response with entity mapping configuration" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_mapping".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RumAudienceManagementAPI.new
p api_instance.get_mapping("users")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get mapping
```
// Get mapping returns "Successful response with entity mapping configuration" response

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
	configuration.SetUnstableOperationEnabled("v2.GetMapping", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumAudienceManagementApi(apiClient)
	resp, r, err := api.GetMapping(ctx, "users")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumAudienceManagementApi.GetMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumAudienceManagementApi.GetMapping`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get mapping
```
// Get mapping returns "Successful response with entity mapping configuration" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumAudienceManagementApi;
import com.datadog.api.client.v2.model.GetMappingResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getMapping", true);
    RumAudienceManagementApi apiInstance = new RumAudienceManagementApi(defaultClient);

    try {
      GetMappingResponse result = apiInstance.getMapping("users");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumAudienceManagementApi#getMapping");
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

#####  Get mapping
```
// Get mapping returns "Successful response with entity mapping configuration"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_audience_management::RumAudienceManagementAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetMapping", true);
    let api = RumAudienceManagementAPI::with_config(configuration);
    let resp = api.get_mapping("users".to_string()).await;
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

#####  Get mapping
```
/**
 * Get mapping returns "Successful response with entity mapping configuration" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getMapping"] = true;
const apiInstance = new v2.RumAudienceManagementApi(configuration);

const params: v2.RumAudienceManagementApiGetMappingRequest = {
  entity: "users",
};

apiInstance
  .getMapping(params)
  .then((data: v2.GetMappingResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=113a9dda-d806-43f3-a88d-34921e01a4d8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=162a6464-53a5-4c26-bb7b-d5a157ce54ea&pt=Rum%20Audience%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frum-audience-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=113a9dda-d806-43f3-a88d-34921e01a4d8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=162a6464-53a5-4c26-bb7b-d5a157ce54ea&pt=Rum%20Audience%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frum-audience-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
Feedback
## Was this page helpful?
Yes 🎉
No 👎
Next
![](https://survey-images.hotjar.com/surveys/logo/90f40352a7464c849f5ce82ccd0e758d)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=5232cc43-b1b4-4c95-9614-9629e9d47498&bo=2&sid=f729f770f0bf11f0aa19994c0c4b86b5&vid=f72a14f0f0bf11f0b889879a61d8cd17&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Rum%20Audience%20Management&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frum-audience-management%2F&r=&lt=2023&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=832261)
