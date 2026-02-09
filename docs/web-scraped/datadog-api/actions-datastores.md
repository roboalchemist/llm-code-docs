# Source: https://docs.datadoghq.com/api/latest/actions-datastores/

# Actions Datastores
Leverage the Actions Datastore API to create, modify, and delete items in datastores owned by your organization.
## [List datastores](https://docs.datadoghq.com/api/latest/actions-datastores/#list-datastores)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#list-datastores-v2)


GET https://api.ap1.datadoghq.com/api/v2/actions-datastoreshttps://api.ap2.datadoghq.com/api/v2/actions-datastoreshttps://api.datadoghq.eu/api/v2/actions-datastoreshttps://api.ddog-gov.com/api/v2/actions-datastoreshttps://api.datadoghq.com/api/v2/actions-datastoreshttps://api.us3.datadoghq.com/api/v2/actions-datastoreshttps://api.us5.datadoghq.com/api/v2/actions-datastores
### Overview
Lists all datastores for the organization. This endpoint requires the `apps_datastore_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#ListDatastores-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#ListDatastores-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


A collection of datastores returned by list operations.
Field
Type
Description
data [_required_]
[object]
An array of datastore objects containing their configurations and metadata.
attributes
object
Detailed information about a datastore.
created_at
date-time
Timestamp when the datastore was created.
creator_user_id
int64
The numeric ID of the user who created the datastore.
creator_user_uuid
string
The UUID of the user who created the datastore.
description
string
A human-readable description about the datastore.
modified_at
date-time
Timestamp when the datastore was last modified.
name
string
The display name of the datastore.
org_id
int64
The ID of the organization that owns this datastore.
primary_column_name
string
The name of the primary key column for this datastore. Primary column names:
  * Must abide by both [PostgreSQL naming conventions](https://www.postgresql.org/docs/7.0/syntax525.htm)
  * Cannot exceed 63 characters


primary_key_generation_strategy
enum
Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid`
id
string
The unique identifier of the datastore.
type [_required_]
enum
The resource type for datastores. Allowed enum values: `datastores`
default: `datastores`
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "creator_user_id": "integer",
        "creator_user_uuid": "string",
        "description": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "org_id": "integer",
        "primary_column_name": "",
        "primary_key_generation_strategy": "string"
      },
      "id": "string",
      "type": "datastores"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  List datastores
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List datastores
```
"""
List datastores returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.list_datastores()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List datastores
```
# List datastores returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new
p api_instance.list_datastores()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List datastores
```
// List datastores returns "OK" response

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
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.ListDatastores(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.ListDatastores`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.ListDatastores`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List datastores
```
// List datastores returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.DatastoreArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    try {
      DatastoreArray result = apiInstance.listDatastores();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#listDatastores");
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

#####  List datastores
```
// List datastores returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api.list_datastores().await;
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

#####  List datastores
```
/**
 * List datastores returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

apiInstance
  .listDatastores()
  .then((data: v2.DatastoreArray) => {
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
## [Create datastore](https://docs.datadoghq.com/api/latest/actions-datastores/#create-datastore)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#create-datastore-v2)


POST https://api.ap1.datadoghq.com/api/v2/actions-datastoreshttps://api.ap2.datadoghq.com/api/v2/actions-datastoreshttps://api.datadoghq.eu/api/v2/actions-datastoreshttps://api.ddog-gov.com/api/v2/actions-datastoreshttps://api.datadoghq.com/api/v2/actions-datastoreshttps://api.us3.datadoghq.com/api/v2/actions-datastoreshttps://api.us5.datadoghq.com/api/v2/actions-datastores
### Overview
Creates a new datastore. This endpoint requires the `apps_datastore_manage` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Field
Type
Description
data
object
Data wrapper containing the configuration needed to create a new datastore.
attributes
object
Configuration and metadata to create a new datastore.
description
string
A human-readable description about the datastore.
name [_required_]
string
The display name for the new datastore.
org_access
enum
The organization access level for the datastore. For example, 'contributor'. Allowed enum values: `contributor,viewer,manager`
primary_column_name [_required_]
string
The name of the primary key column for this datastore. Primary column names:
  * Must abide by both [PostgreSQL naming conventions](https://www.postgresql.org/docs/7.0/syntax525.htm)
  * Cannot exceed 63 characters


primary_key_generation_strategy
enum
Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid`
id
string
Optional ID for the new datastore. If not provided, one will be generated automatically.
type [_required_]
enum
The resource type for datastores. Allowed enum values: `datastores`
default: `datastores`
```
{
  "data": {
    "attributes": {
      "name": "datastore-name",
      "primary_column_name": "primaryKey"
    },
    "type": "datastores"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#CreateDatastore-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#CreateDatastore-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#CreateDatastore-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Response after successfully creating a new datastore, containing the datastore’s assigned ID.
Field
Type
Description
data
object
The newly created datastore's data.
id
string
The unique identifier assigned to the newly created datastore.
type [_required_]
enum
The resource type for datastores. Allowed enum values: `datastores`
default: `datastores`
```
{
  "data": {
    "id": "string",
    "type": "datastores"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Create datastore returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "datastore-name",
      "primary_column_name": "primaryKey"
    },
    "type": "datastores"
  }
}
EOF  

                        
```

#####  Create datastore returns "OK" response
```
// Create datastore returns "OK" response

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
	body := datadogV2.CreateAppsDatastoreRequest{
		Data: &datadogV2.CreateAppsDatastoreRequestData{
			Attributes: &datadogV2.CreateAppsDatastoreRequestDataAttributes{
				Name:              "datastore-name",
				PrimaryColumnName: "primaryKey",
			},
			Type: datadogV2.DATASTOREDATATYPE_DATASTORES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.CreateDatastore(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.CreateDatastore`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.CreateDatastore`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create datastore returns "OK" response
```
// Create datastore returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.CreateAppsDatastoreRequest;
import com.datadog.api.client.v2.model.CreateAppsDatastoreRequestData;
import com.datadog.api.client.v2.model.CreateAppsDatastoreRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateAppsDatastoreResponse;
import com.datadog.api.client.v2.model.DatastoreDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    CreateAppsDatastoreRequest body =
        new CreateAppsDatastoreRequest()
            .data(
                new CreateAppsDatastoreRequestData()
                    .attributes(
                        new CreateAppsDatastoreRequestDataAttributes()
                            .name("datastore-name")
                            .primaryColumnName("primaryKey"))
                    .type(DatastoreDataType.DATASTORES));

    try {
      CreateAppsDatastoreResponse result = apiInstance.createDatastore(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#createDatastore");
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

#####  Create datastore returns "OK" response
```
"""
Create datastore returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.create_apps_datastore_request import CreateAppsDatastoreRequest
from datadog_api_client.v2.model.create_apps_datastore_request_data import CreateAppsDatastoreRequestData
from datadog_api_client.v2.model.create_apps_datastore_request_data_attributes import (
    CreateAppsDatastoreRequestDataAttributes,
)
from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType

body = CreateAppsDatastoreRequest(
    data=CreateAppsDatastoreRequestData(
        attributes=CreateAppsDatastoreRequestDataAttributes(
            name="datastore-name",
            primary_column_name="primaryKey",
        ),
        type=DatastoreDataType.DATASTORES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.create_datastore(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create datastore returns "OK" response
```
# Create datastore returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

body = DatadogAPIClient::V2::CreateAppsDatastoreRequest.new({
  data: DatadogAPIClient::V2::CreateAppsDatastoreRequestData.new({
    attributes: DatadogAPIClient::V2::CreateAppsDatastoreRequestDataAttributes.new({
      name: "datastore-name",
      primary_column_name: "primaryKey",
    }),
    type: DatadogAPIClient::V2::DatastoreDataType::DATASTORES,
  }),
})
p api_instance.create_datastore(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create datastore returns "OK" response
```
// Create datastore returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;
use datadog_api_client::datadogV2::model::CreateAppsDatastoreRequest;
use datadog_api_client::datadogV2::model::CreateAppsDatastoreRequestData;
use datadog_api_client::datadogV2::model::CreateAppsDatastoreRequestDataAttributes;
use datadog_api_client::datadogV2::model::DatastoreDataType;

#[tokio::main]
async fn main() {
    let body = CreateAppsDatastoreRequest::new().data(
        CreateAppsDatastoreRequestData::new(DatastoreDataType::DATASTORES).attributes(
            CreateAppsDatastoreRequestDataAttributes::new(
                "datastore-name".to_string(),
                "primaryKey".to_string(),
            ),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api.create_datastore(body).await;
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

#####  Create datastore returns "OK" response
```
/**
 * Create datastore returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

const params: v2.ActionsDatastoresApiCreateDatastoreRequest = {
  body: {
    data: {
      attributes: {
        name: "datastore-name",
        primaryColumnName: "primaryKey",
      },
      type: "datastores",
    },
  },
};

apiInstance
  .createDatastore(params)
  .then((data: v2.CreateAppsDatastoreResponse) => {
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
## [Get datastore](https://docs.datadoghq.com/api/latest/actions-datastores/#get-datastore)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#get-datastore-v2)


GET https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}
### Overview
Retrieves a specific datastore by its ID. This endpoint requires the `apps_datastore_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The unique identifier of the datastore to retrieve.
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#GetDatastore-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#GetDatastore-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/actions-datastores/#GetDatastore-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#GetDatastore-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


A datastore’s complete configuration and metadata.
Field
Type
Description
data
object
Core information about a datastore, including its unique identifier and attributes.
attributes
object
Detailed information about a datastore.
created_at
date-time
Timestamp when the datastore was created.
creator_user_id
int64
The numeric ID of the user who created the datastore.
creator_user_uuid
string
The UUID of the user who created the datastore.
description
string
A human-readable description about the datastore.
modified_at
date-time
Timestamp when the datastore was last modified.
name
string
The display name of the datastore.
org_id
int64
The ID of the organization that owns this datastore.
primary_column_name
string
The name of the primary key column for this datastore. Primary column names:
  * Must abide by both [PostgreSQL naming conventions](https://www.postgresql.org/docs/7.0/syntax525.htm)
  * Cannot exceed 63 characters


primary_key_generation_strategy
enum
Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid`
id
string
The unique identifier of the datastore.
type [_required_]
enum
The resource type for datastores. Allowed enum values: `datastores`
default: `datastores`
```
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "creator_user_id": "integer",
      "creator_user_uuid": "string",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "org_id": "integer",
      "primary_column_name": "",
      "primary_key_generation_strategy": "string"
    },
    "id": "string",
    "type": "datastores"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Get datastore
Copy
```
                  # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get datastore
```
"""
Get datastore returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.get_datastore(
        datastore_id=DATASTORE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get datastore
```
# Get datastore returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]
p api_instance.get_datastore(DATASTORE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get datastore
```
// Get datastore returns "OK" response

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
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.GetDatastore(ctx, DatastoreDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.GetDatastore`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.GetDatastore`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get datastore
```
// Get datastore returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.Datastore;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    try {
      Datastore result = apiInstance.getDatastore(DATASTORE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#getDatastore");
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

#####  Get datastore
```
// Get datastore returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api.get_datastore(datastore_data_id.clone()).await;
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

#####  Get datastore
```
/**
 * Get datastore returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiGetDatastoreRequest = {
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .getDatastore(params)
  .then((data: v2.Datastore) => {
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
## [Update datastore](https://docs.datadoghq.com/api/latest/actions-datastores/#update-datastore)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#update-datastore-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}
### Overview
Updates an existing datastore’s attributes. This endpoint requires the `apps_datastore_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The unique identifier of the datastore to retrieve.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Field
Type
Description
data
object
Data wrapper containing the datastore identifier and the attributes to update.
attributes
object
Attributes that can be updated on a datastore.
description
string
A human-readable description about the datastore.
name
string
The display name of the datastore.
id
string
The unique identifier of the datastore to update.
type [_required_]
enum
The resource type for datastores. Allowed enum values: `datastores`
default: `datastores`
```
{
  "data": {
    "attributes": {
      "name": "updated name"
    },
    "type": "datastores",
    "id": "string"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastore-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastore-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastore-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastore-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


A datastore’s complete configuration and metadata.
Field
Type
Description
data
object
Core information about a datastore, including its unique identifier and attributes.
attributes
object
Detailed information about a datastore.
created_at
date-time
Timestamp when the datastore was created.
creator_user_id
int64
The numeric ID of the user who created the datastore.
creator_user_uuid
string
The UUID of the user who created the datastore.
description
string
A human-readable description about the datastore.
modified_at
date-time
Timestamp when the datastore was last modified.
name
string
The display name of the datastore.
org_id
int64
The ID of the organization that owns this datastore.
primary_column_name
string
The name of the primary key column for this datastore. Primary column names:
  * Must abide by both [PostgreSQL naming conventions](https://www.postgresql.org/docs/7.0/syntax525.htm)
  * Cannot exceed 63 characters


primary_key_generation_strategy
enum
Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid`
id
string
The unique identifier of the datastore.
type [_required_]
enum
The resource type for datastores. Allowed enum values: `datastores`
default: `datastores`
```
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "creator_user_id": "integer",
      "creator_user_uuid": "string",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "org_id": "integer",
      "primary_column_name": "",
      "primary_key_generation_strategy": "string"
    },
    "id": "string",
    "type": "datastores"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Update datastore returns "OK" response
Copy
```
                          # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "updated name"
    },
    "type": "datastores",
    "id": "string"
  }
}
EOF  

                        
```

#####  Update datastore returns "OK" response
```
// Update datastore returns "OK" response

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
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	body := datadogV2.UpdateAppsDatastoreRequest{
		Data: &datadogV2.UpdateAppsDatastoreRequestData{
			Attributes: &datadogV2.UpdateAppsDatastoreRequestDataAttributes{
				Name: datadog.PtrString("updated name"),
			},
			Type: datadogV2.DATASTOREDATATYPE_DATASTORES,
			Id:   datadog.PtrString(DatastoreDataID),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.UpdateDatastore(ctx, DatastoreDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.UpdateDatastore`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.UpdateDatastore`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update datastore returns "OK" response
```
// Update datastore returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.Datastore;
import com.datadog.api.client.v2.model.DatastoreDataType;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreRequest;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreRequestData;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreRequestDataAttributes;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    UpdateAppsDatastoreRequest body =
        new UpdateAppsDatastoreRequest()
            .data(
                new UpdateAppsDatastoreRequestData()
                    .attributes(new UpdateAppsDatastoreRequestDataAttributes().name("updated name"))
                    .type(DatastoreDataType.DATASTORES)
                    .id(DATASTORE_DATA_ID));

    try {
      Datastore result = apiInstance.updateDatastore(DATASTORE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#updateDatastore");
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

#####  Update datastore returns "OK" response
```
"""
Update datastore returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType
from datadog_api_client.v2.model.update_apps_datastore_request import UpdateAppsDatastoreRequest
from datadog_api_client.v2.model.update_apps_datastore_request_data import UpdateAppsDatastoreRequestData
from datadog_api_client.v2.model.update_apps_datastore_request_data_attributes import (
    UpdateAppsDatastoreRequestDataAttributes,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = UpdateAppsDatastoreRequest(
    data=UpdateAppsDatastoreRequestData(
        attributes=UpdateAppsDatastoreRequestDataAttributes(
            name="updated name",
        ),
        type=DatastoreDataType.DATASTORES,
        id=DATASTORE_DATA_ID,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.update_datastore(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update datastore returns "OK" response
```
# Update datastore returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]

body = DatadogAPIClient::V2::UpdateAppsDatastoreRequest.new({
  data: DatadogAPIClient::V2::UpdateAppsDatastoreRequestData.new({
    attributes: DatadogAPIClient::V2::UpdateAppsDatastoreRequestDataAttributes.new({
      name: "updated name",
    }),
    type: DatadogAPIClient::V2::DatastoreDataType::DATASTORES,
    id: DATASTORE_DATA_ID,
  }),
})
p api_instance.update_datastore(DATASTORE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update datastore returns "OK" response
```
// Update datastore returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;
use datadog_api_client::datadogV2::model::DatastoreDataType;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreRequest;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreRequestData;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreRequestDataAttributes;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let body = UpdateAppsDatastoreRequest::new().data(
        UpdateAppsDatastoreRequestData::new(DatastoreDataType::DATASTORES)
            .attributes(
                UpdateAppsDatastoreRequestDataAttributes::new().name("updated name".to_string()),
            )
            .id(datastore_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api.update_datastore(datastore_data_id.clone(), body).await;
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

#####  Update datastore returns "OK" response
```
/**
 * Update datastore returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiUpdateDatastoreRequest = {
  body: {
    data: {
      attributes: {
        name: "updated name",
      },
      type: "datastores",
      id: DATASTORE_DATA_ID,
    },
  },
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .updateDatastore(params)
  .then((data: v2.Datastore) => {
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
## [Delete datastore](https://docs.datadoghq.com/api/latest/actions-datastores/#delete-datastore)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#delete-datastore-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}
### Overview
Deletes a datastore by its unique identifier. This endpoint requires the `apps_datastore_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The unique identifier of the datastore to retrieve.
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#DeleteDatastore-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#DeleteDatastore-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#DeleteDatastore-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Delete datastore
Copy
```
                  # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete datastore
```
"""
Delete datastore returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    api_instance.delete_datastore(
        datastore_id=DATASTORE_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete datastore
```
# Delete datastore returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]
p api_instance.delete_datastore(DATASTORE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete datastore
```
// Delete datastore returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	r, err := api.DeleteDatastore(ctx, DatastoreDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.DeleteDatastore`: %v\n", err)
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

#####  Delete datastore
```
// Delete datastore returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    try {
      apiInstance.deleteDatastore(DATASTORE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#deleteDatastore");
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

#####  Delete datastore
```
// Delete datastore returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api.delete_datastore(datastore_data_id.clone()).await;
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

#####  Delete datastore
```
/**
 * Delete datastore returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiDeleteDatastoreRequest = {
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .deleteDatastore(params)
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
## [List datastore items](https://docs.datadoghq.com/api/latest/actions-datastores/#list-datastore-items)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#list-datastore-items-v2)


GET https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/itemshttps://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items
### Overview
Lists items from a datastore. You can filter the results by specifying either an item key or a filter query parameter, but not both at the same time. Supports server-side pagination for large datasets. This endpoint requires the `apps_datastore_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The unique identifier of the datastore to retrieve.
#### Query Strings
Name
Type
Description
filter
string
Optional query filter to search items using the [logs search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).
item_key
string
Optional primary key value to retrieve a specific item. Cannot be used together with the filter parameter.
page[limit]
integer
Optional field to limit the number of items to return per page for pagination. Up to 100 items can be returned per page.
page[offset]
integer
Optional field to offset the number of items to skip from the beginning of the result set for pagination.
sort
string
Optional field to sort results by. Prefix with ‘-’ for descending order (e.g., ‘-created_at’).
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#ListDatastoreItems-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#ListDatastoreItems-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/actions-datastores/#ListDatastoreItems-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#ListDatastoreItems-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


A collection of datastore items with pagination and schema metadata.
Field
Type
Description
data [_required_]
[object]
An array of datastore items with their content and metadata.
attributes
object
Metadata and content of a datastore item.
created_at
date-time
Timestamp when the item was first created.
modified_at
date-time
Timestamp when the item was last modified.
org_id
int64
The ID of the organization that owns this item.
primary_column_name
string
The name of the primary key column for this datastore. Primary column names:
  * Must abide by both [PostgreSQL naming conventions](https://www.postgresql.org/docs/7.0/syntax525.htm)
  * Cannot exceed 63 characters


signature
string
A unique signature identifying this item version.
store_id
string
The unique identifier of the datastore containing this item.
value
object
The data content (as key-value pairs) of a datastore item.
id
string
The unique identifier of the datastore.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
meta
object
Metadata about the included items, including pagination info and datastore schema.
page
object
Pagination information for a collection of datastore items.
hasMore
boolean
Whether there are additional pages of items beyond the current page.
totalCount
int64
The total number of items in the datastore, ignoring any filters.
totalFilteredCount
int64
The total number of items that match the current filter criteria.
schema
object
Schema information about the datastore, including its primary key and field definitions.
fields
[object]
An array describing the columns available in this datastore.
name [_required_]
string
The name of this column in the datastore.
type [_required_]
string
The data type of this column. For example, 'string', 'number', or 'boolean'.
primary_key
string
The name of the primary key column for this datastore.
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "org_id": "integer",
        "primary_column_name": "",
        "signature": "string",
        "store_id": "string",
        "value": {}
      },
      "id": "string",
      "type": "items"
    }
  ],
  "meta": {
    "page": {
      "hasMore": false,
      "totalCount": "integer",
      "totalFilteredCount": "integer"
    },
    "schema": {
      "fields": [
        {
          "name": "",
          "type": ""
        }
      ],
      "primary_key": "string"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  List datastore items
Copy
```
                  # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List datastore items
```
"""
List datastore items returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.list_datastore_items(
        datastore_id=DATASTORE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List datastore items
```
# List datastore items returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]
p api_instance.list_datastore_items(DATASTORE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List datastore items
```
// List datastore items returns "OK" response

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
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.ListDatastoreItems(ctx, DatastoreDataID, *datadogV2.NewListDatastoreItemsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.ListDatastoreItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.ListDatastoreItems`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List datastore items
```
// List datastore items returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.ItemApiPayloadArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    try {
      ItemApiPayloadArray result = apiInstance.listDatastoreItems(DATASTORE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#listDatastoreItems");
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

#####  List datastore items
```
// List datastore items returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;
use datadog_api_client::datadogV2::api_actions_datastores::ListDatastoreItemsOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api
        .list_datastore_items(
            datastore_data_id.clone(),
            ListDatastoreItemsOptionalParams::default(),
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

#####  List datastore items
```
/**
 * List datastore items returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiListDatastoreItemsRequest = {
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .listDatastoreItems(params)
  .then((data: v2.ItemApiPayloadArray) => {
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
## [Delete datastore item](https://docs.datadoghq.com/api/latest/actions-datastores/#delete-datastore-item)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#delete-datastore-item-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/itemshttps://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items
### Overview
Deletes an item from a datastore by its key. This endpoint requires the `apps_datastore_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The unique identifier of the datastore to retrieve.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Field
Type
Description
data
object
Data wrapper containing the information needed to identify and delete a specific datastore item.
attributes
object
Attributes specifying which datastore item to delete by its primary key.
id
string
Optional unique identifier of the item to delete.
item_key [_required_]
string
The primary key value that identifies the item to delete. Cannot exceed 256 characters.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
```
{
  "data": {
    "attributes": {
      "item_key": "test-key"
    },
    "type": "items"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#DeleteDatastoreItem-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#DeleteDatastoreItem-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/actions-datastores/#DeleteDatastoreItem-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#DeleteDatastoreItem-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Response from successfully deleting a datastore item.
Field
Type
Description
data
object
Data containing the identifier of the datastore item that was successfully deleted.
id
string
The unique identifier of the item that was deleted.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
```
{
  "data": {
    "id": "string",
    "type": "items"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Delete datastore item returns "OK" response
Copy
```
                          # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "item_key": "test-key"
    },
    "type": "items"
  }
}
EOF  

                        
```

#####  Delete datastore item returns "OK" response
```
// Delete datastore item returns "OK" response

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
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	body := datadogV2.DeleteAppsDatastoreItemRequest{
		Data: &datadogV2.DeleteAppsDatastoreItemRequestData{
			Attributes: &datadogV2.DeleteAppsDatastoreItemRequestDataAttributes{
				ItemKey: "test-key",
			},
			Type: datadogV2.DATASTOREITEMSDATATYPE_ITEMS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.DeleteDatastoreItem(ctx, DatastoreDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.DeleteDatastoreItem`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.DeleteDatastoreItem`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete datastore item returns "OK" response
```
// Delete datastore item returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.DatastoreItemsDataType;
import com.datadog.api.client.v2.model.DeleteAppsDatastoreItemRequest;
import com.datadog.api.client.v2.model.DeleteAppsDatastoreItemRequestData;
import com.datadog.api.client.v2.model.DeleteAppsDatastoreItemRequestDataAttributes;
import com.datadog.api.client.v2.model.DeleteAppsDatastoreItemResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    DeleteAppsDatastoreItemRequest body =
        new DeleteAppsDatastoreItemRequest()
            .data(
                new DeleteAppsDatastoreItemRequestData()
                    .attributes(
                        new DeleteAppsDatastoreItemRequestDataAttributes().itemKey("test-key"))
                    .type(DatastoreItemsDataType.ITEMS));

    try {
      DeleteAppsDatastoreItemResponse result =
          apiInstance.deleteDatastoreItem(DATASTORE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#deleteDatastoreItem");
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

#####  Delete datastore item returns "OK" response
```
"""
Delete datastore item returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType
from datadog_api_client.v2.model.delete_apps_datastore_item_request import DeleteAppsDatastoreItemRequest
from datadog_api_client.v2.model.delete_apps_datastore_item_request_data import DeleteAppsDatastoreItemRequestData
from datadog_api_client.v2.model.delete_apps_datastore_item_request_data_attributes import (
    DeleteAppsDatastoreItemRequestDataAttributes,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = DeleteAppsDatastoreItemRequest(
    data=DeleteAppsDatastoreItemRequestData(
        attributes=DeleteAppsDatastoreItemRequestDataAttributes(
            item_key="test-key",
        ),
        type=DatastoreItemsDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.delete_datastore_item(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete datastore item returns "OK" response
```
# Delete datastore item returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]

body = DatadogAPIClient::V2::DeleteAppsDatastoreItemRequest.new({
  data: DatadogAPIClient::V2::DeleteAppsDatastoreItemRequestData.new({
    attributes: DatadogAPIClient::V2::DeleteAppsDatastoreItemRequestDataAttributes.new({
      item_key: "test-key",
    }),
    type: DatadogAPIClient::V2::DatastoreItemsDataType::ITEMS,
  }),
})
p api_instance.delete_datastore_item(DATASTORE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete datastore item returns "OK" response
```
// Delete datastore item returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;
use datadog_api_client::datadogV2::model::DatastoreItemsDataType;
use datadog_api_client::datadogV2::model::DeleteAppsDatastoreItemRequest;
use datadog_api_client::datadogV2::model::DeleteAppsDatastoreItemRequestData;
use datadog_api_client::datadogV2::model::DeleteAppsDatastoreItemRequestDataAttributes;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let body = DeleteAppsDatastoreItemRequest::new().data(
        DeleteAppsDatastoreItemRequestData::new(DatastoreItemsDataType::ITEMS).attributes(
            DeleteAppsDatastoreItemRequestDataAttributes::new("test-key".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api
        .delete_datastore_item(datastore_data_id.clone(), body)
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

#####  Delete datastore item returns "OK" response
```
/**
 * Delete datastore item returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiDeleteDatastoreItemRequest = {
  body: {
    data: {
      attributes: {
        itemKey: "test-key",
      },
      type: "items",
    },
  },
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .deleteDatastoreItem(params)
  .then((data: v2.DeleteAppsDatastoreItemResponse) => {
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
## [Update datastore item](https://docs.datadoghq.com/api/latest/actions-datastores/#update-datastore-item)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#update-datastore-item-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/itemshttps://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/itemshttps://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items
### Overview
Partially updates an item in a datastore by its key. This endpoint requires the `apps_datastore_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The unique identifier of the datastore to retrieve.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Field
Type
Description
data
object
Data wrapper containing the item identifier and the changes to apply during the update operation.
attributes
object
Attributes for updating a datastore item, including the item key and changes to apply.
id
string
The unique identifier of the item being updated.
item_changes [_required_]
object
Changes to apply to a datastore item using set operations.
ops_set
object
Set operation that contains key-value pairs to set on the datastore item.
item_key [_required_]
string
The primary key that identifies the item to update. Cannot exceed 256 characters.
id
string
The unique identifier of the datastore item.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
```
{
  "data": {
    "attributes": {
      "item_changes": {},
      "item_key": "test-key"
    },
    "type": "items"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastoreItem-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastoreItem-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastoreItem-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#UpdateDatastoreItem-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


A single datastore item with its content and metadata.
Field
Type
Description
data
object
Core data and metadata for a single datastore item.
attributes
object
Metadata and content of a datastore item.
created_at
date-time
Timestamp when the item was first created.
modified_at
date-time
Timestamp when the item was last modified.
org_id
int64
The ID of the organization that owns this item.
primary_column_name
string
The name of the primary key column for this datastore. Primary column names:
  * Must abide by both [PostgreSQL naming conventions](https://www.postgresql.org/docs/7.0/syntax525.htm)
  * Cannot exceed 63 characters


signature
string
A unique signature identifying this item version.
store_id
string
The unique identifier of the datastore containing this item.
value
object
The data content (as key-value pairs) of a datastore item.
id
string
The unique identifier of the datastore.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
```
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "org_id": "integer",
      "primary_column_name": "",
      "signature": "string",
      "store_id": "string",
      "value": {}
    },
    "id": "string",
    "type": "items"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Update datastore item returns "OK" response
Copy
```
                          # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "item_changes": {},
      "item_key": "test-key"
    },
    "type": "items"
  }
}
EOF  

                        
```

#####  Update datastore item returns "OK" response
```
// Update datastore item returns "OK" response

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
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	body := datadogV2.UpdateAppsDatastoreItemRequest{
		Data: &datadogV2.UpdateAppsDatastoreItemRequestData{
			Attributes: &datadogV2.UpdateAppsDatastoreItemRequestDataAttributes{
				ItemChanges: datadogV2.UpdateAppsDatastoreItemRequestDataAttributesItemChanges{},
				ItemKey:     "test-key",
			},
			Type: datadogV2.UPDATEAPPSDATASTOREITEMREQUESTDATATYPE_ITEMS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.UpdateDatastoreItem(ctx, DatastoreDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.UpdateDatastoreItem`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.UpdateDatastoreItem`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update datastore item returns "OK" response
```
// Update datastore item returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.ItemApiPayload;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreItemRequest;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreItemRequestData;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreItemRequestDataAttributes;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreItemRequestDataAttributesItemChanges;
import com.datadog.api.client.v2.model.UpdateAppsDatastoreItemRequestDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    UpdateAppsDatastoreItemRequest body =
        new UpdateAppsDatastoreItemRequest()
            .data(
                new UpdateAppsDatastoreItemRequestData()
                    .attributes(
                        new UpdateAppsDatastoreItemRequestDataAttributes()
                            .itemChanges(
                                new UpdateAppsDatastoreItemRequestDataAttributesItemChanges())
                            .itemKey("test-key"))
                    .type(UpdateAppsDatastoreItemRequestDataType.ITEMS));

    try {
      ItemApiPayload result = apiInstance.updateDatastoreItem(DATASTORE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#updateDatastoreItem");
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

#####  Update datastore item returns "OK" response
```
"""
Update datastore item returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.update_apps_datastore_item_request import UpdateAppsDatastoreItemRequest
from datadog_api_client.v2.model.update_apps_datastore_item_request_data import UpdateAppsDatastoreItemRequestData
from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes import (
    UpdateAppsDatastoreItemRequestDataAttributes,
)
from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes_item_changes import (
    UpdateAppsDatastoreItemRequestDataAttributesItemChanges,
)
from datadog_api_client.v2.model.update_apps_datastore_item_request_data_type import (
    UpdateAppsDatastoreItemRequestDataType,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = UpdateAppsDatastoreItemRequest(
    data=UpdateAppsDatastoreItemRequestData(
        attributes=UpdateAppsDatastoreItemRequestDataAttributes(
            item_changes=UpdateAppsDatastoreItemRequestDataAttributesItemChanges(),
            item_key="test-key",
        ),
        type=UpdateAppsDatastoreItemRequestDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.update_datastore_item(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update datastore item returns "OK" response
```
# Update datastore item returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]

body = DatadogAPIClient::V2::UpdateAppsDatastoreItemRequest.new({
  data: DatadogAPIClient::V2::UpdateAppsDatastoreItemRequestData.new({
    attributes: DatadogAPIClient::V2::UpdateAppsDatastoreItemRequestDataAttributes.new({
      item_changes: DatadogAPIClient::V2::UpdateAppsDatastoreItemRequestDataAttributesItemChanges.new({}),
      item_key: "test-key",
    }),
    type: DatadogAPIClient::V2::UpdateAppsDatastoreItemRequestDataType::ITEMS,
  }),
})
p api_instance.update_datastore_item(DATASTORE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update datastore item returns "OK" response
```
// Update datastore item returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreItemRequest;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreItemRequestData;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreItemRequestDataAttributes;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreItemRequestDataAttributesItemChanges;
use datadog_api_client::datadogV2::model::UpdateAppsDatastoreItemRequestDataType;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let body = UpdateAppsDatastoreItemRequest::new().data(
        UpdateAppsDatastoreItemRequestData::new(UpdateAppsDatastoreItemRequestDataType::ITEMS)
            .attributes(UpdateAppsDatastoreItemRequestDataAttributes::new(
                UpdateAppsDatastoreItemRequestDataAttributesItemChanges::new(),
                "test-key".to_string(),
            )),
    );
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api
        .update_datastore_item(datastore_data_id.clone(), body)
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

#####  Update datastore item returns "OK" response
```
/**
 * Update datastore item returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiUpdateDatastoreItemRequest = {
  body: {
    data: {
      attributes: {
        itemChanges: {},
        itemKey: "test-key",
      },
      type: "items",
    },
  },
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .updateDatastoreItem(params)
  .then((data: v2.ItemApiPayload) => {
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
## [Bulk write datastore items](https://docs.datadoghq.com/api/latest/actions-datastores/#bulk-write-datastore-items)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#bulk-write-datastore-items-v2)


POST https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk
### Overview
Creates or replaces multiple items in a datastore by their keys in a single operation. This endpoint requires the `apps_datastore_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The unique identifier of the datastore to retrieve.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Field
Type
Description
data
object
Data wrapper containing the items to insert and their configuration for the bulk insert operation.
attributes
object
Configuration for bulk inserting multiple items into a datastore.
conflict_mode
enum
How to handle conflicts when inserting items that already exist in the datastore. Allowed enum values: `fail_on_conflict,overwrite_on_conflict`
values [_required_]
[object]
An array of items to add to the datastore, where each item is a set of key-value pairs representing the item's data. Up to 100 items can be updated in a single request.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
```
{
  "data": {
    "attributes": {
      "values": [
        {
          "id": "cust_3141",
          "name": "Johnathan"
        },
        {
          "id": "cust_3142",
          "name": "Mary"
        }
      ]
    },
    "type": "items"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkWriteDatastoreItems-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkWriteDatastoreItems-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkWriteDatastoreItems-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkWriteDatastoreItems-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Response after successfully inserting multiple items into a datastore, containing the identifiers of the created items.
Field
Type
Description
data [_required_]
[object]
An array of data objects containing the identifiers of the successfully inserted items.
id
string
The unique identifier assigned to the inserted item.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
```
{
  "data": [
    {
      "id": "string",
      "type": "items"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Bulk write datastore items returns "OK" response
Copy
```
                          # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items/bulk" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "values": [
        {
          "id": "cust_3141",
          "name": "Johnathan"
        },
        {
          "id": "cust_3142",
          "name": "Mary"
        }
      ]
    },
    "type": "items"
  }
}
EOF  

                        
```

#####  Bulk write datastore items returns "OK" response
```
// Bulk write datastore items returns "OK" response

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
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	body := datadogV2.BulkPutAppsDatastoreItemsRequest{
		Data: &datadogV2.BulkPutAppsDatastoreItemsRequestData{
			Attributes: &datadogV2.BulkPutAppsDatastoreItemsRequestDataAttributes{
				Values: []map[string]interface{}{
					{
						"id":   "cust_3141",
						"name": "Johnathan",
					},
					{
						"id":   "cust_3142",
						"name": "Mary",
					},
				},
			},
			Type: datadogV2.DATASTOREITEMSDATATYPE_ITEMS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.BulkWriteDatastoreItems(ctx, DatastoreDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.BulkWriteDatastoreItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.BulkWriteDatastoreItems`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Bulk write datastore items returns "OK" response
```
// Bulk write datastore items returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.BulkPutAppsDatastoreItemsRequest;
import com.datadog.api.client.v2.model.BulkPutAppsDatastoreItemsRequestData;
import com.datadog.api.client.v2.model.BulkPutAppsDatastoreItemsRequestDataAttributes;
import com.datadog.api.client.v2.model.DatastoreItemsDataType;
import com.datadog.api.client.v2.model.PutAppsDatastoreItemResponseArray;
import java.util.Arrays;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    BulkPutAppsDatastoreItemsRequest body =
        new BulkPutAppsDatastoreItemsRequest()
            .data(
                new BulkPutAppsDatastoreItemsRequestData()
                    .attributes(
                        new BulkPutAppsDatastoreItemsRequestDataAttributes()
                            .values(
                                Arrays.asList(
                                    Map.ofEntries(
                                        Map.entry("id", "cust_3141"),
                                        Map.entry("name", "Johnathan")),
                                    Map.ofEntries(
                                        Map.entry("id", "cust_3142"), Map.entry("name", "Mary")))))
                    .type(DatastoreItemsDataType.ITEMS));

    try {
      PutAppsDatastoreItemResponseArray result =
          apiInstance.bulkWriteDatastoreItems(DATASTORE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#bulkWriteDatastoreItems");
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

#####  Bulk write datastore items returns "OK" response
```
"""
Bulk write datastore items returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request import BulkPutAppsDatastoreItemsRequest
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data import BulkPutAppsDatastoreItemsRequestData
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data_attributes import (
    BulkPutAppsDatastoreItemsRequestDataAttributes,
)
from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = BulkPutAppsDatastoreItemsRequest(
    data=BulkPutAppsDatastoreItemsRequestData(
        attributes=BulkPutAppsDatastoreItemsRequestDataAttributes(
            values=[
                dict([("id", "cust_3141"), ("name", "Johnathan")]),
                dict([("id", "cust_3142"), ("name", "Mary")]),
            ],
        ),
        type=DatastoreItemsDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.bulk_write_datastore_items(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Bulk write datastore items returns "OK" response
```
# Bulk write datastore items returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]

body = DatadogAPIClient::V2::BulkPutAppsDatastoreItemsRequest.new({
  data: DatadogAPIClient::V2::BulkPutAppsDatastoreItemsRequestData.new({
    attributes: DatadogAPIClient::V2::BulkPutAppsDatastoreItemsRequestDataAttributes.new({
      values: [
        {
          "id": "cust_3141", "name": "Johnathan",
        },
        {
          "id": "cust_3142", "name": "Mary",
        },
      ],
    }),
    type: DatadogAPIClient::V2::DatastoreItemsDataType::ITEMS,
  }),
})
p api_instance.bulk_write_datastore_items(DATASTORE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Bulk write datastore items returns "OK" response
```
// Bulk write datastore items returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;
use datadog_api_client::datadogV2::model::BulkPutAppsDatastoreItemsRequest;
use datadog_api_client::datadogV2::model::BulkPutAppsDatastoreItemsRequestData;
use datadog_api_client::datadogV2::model::BulkPutAppsDatastoreItemsRequestDataAttributes;
use datadog_api_client::datadogV2::model::DatastoreItemsDataType;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let body = BulkPutAppsDatastoreItemsRequest::new().data(
        BulkPutAppsDatastoreItemsRequestData::new(DatastoreItemsDataType::ITEMS).attributes(
            BulkPutAppsDatastoreItemsRequestDataAttributes::new(vec![
                BTreeMap::from([
                    ("id".to_string(), Value::from("cust_3141")),
                    ("name".to_string(), Value::from("Johnathan")),
                ]),
                BTreeMap::from([
                    ("id".to_string(), Value::from("cust_3142")),
                    ("name".to_string(), Value::from("Mary")),
                ]),
            ]),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api
        .bulk_write_datastore_items(datastore_data_id.clone(), body)
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

#####  Bulk write datastore items returns "OK" response
```
/**
 * Bulk write datastore items returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiBulkWriteDatastoreItemsRequest = {
  body: {
    data: {
      attributes: {
        values: [
          {
            id: "cust_3141",
            name: "Johnathan",
          },
          {
            id: "cust_3142",
            name: "Mary",
          },
        ],
      },
      type: "items",
    },
  },
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .bulkWriteDatastoreItems(params)
  .then((data: v2.PutAppsDatastoreItemResponseArray) => {
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
## [Bulk delete datastore items](https://docs.datadoghq.com/api/latest/actions-datastores/#bulk-delete-datastore-items)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/actions-datastores/#bulk-delete-datastore-items-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulkhttps://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk
### Overview
Deletes multiple items from a datastore by their keys in a single operation. This endpoint requires the `apps_datastore_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
datastore_id [_required_]
string
The ID of the datastore.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


Field
Type
Description
data
object
Data wrapper containing the data needed to delete items from a datastore.
attributes
object
Attributes of request data to delete items from a datastore.
item_keys
[string]
List of primary keys identifying items to delete from datastore. Up to 100 items can be deleted in a single request.
id
string
ID for the datastore of the items to delete.
type [_required_]
enum
Items resource type. Allowed enum values: `items`
default: `items`
```
{
  "data": {
    "attributes": {
      "item_keys": [
        "test-key"
      ]
    },
    "type": "items"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkDeleteDatastoreItems-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkDeleteDatastoreItems-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkDeleteDatastoreItems-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkDeleteDatastoreItems-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/actions-datastores/#BulkDeleteDatastoreItems-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


The definition of `DeleteAppsDatastoreItemResponseArray` object.
Field
Type
Description
data [_required_]
[object]
The `DeleteAppsDatastoreItemResponseArray` `data`.
id
string
The unique identifier of the item that was deleted.
type [_required_]
enum
The resource type for datastore items. Allowed enum values: `items`
default: `items`
```
{
  "data": [
    {
      "id": "string",
      "type": "items"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/actions-datastores/)
  * [Example](https://docs.datadoghq.com/api/latest/actions-datastores/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/actions-datastores/?code-lang=typescript)


#####  Bulk delete datastore items returns "OK" response
Copy
```
                          # Path parameters  
export datastore_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items/bulk" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "item_keys": [
        "test-key"
      ]
    },
    "type": "items"
  }
}
EOF  

                        
```

#####  Bulk delete datastore items returns "OK" response
```
// Bulk delete datastore items returns "OK" response

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
	// there is a valid "datastore" in the system
	DatastoreDataID := os.Getenv("DATASTORE_DATA_ID")

	body := datadogV2.BulkDeleteAppsDatastoreItemsRequest{
		Data: &datadogV2.BulkDeleteAppsDatastoreItemsRequestData{
			Attributes: &datadogV2.BulkDeleteAppsDatastoreItemsRequestDataAttributes{
				ItemKeys: []string{
					"test-key",
				},
			},
			Type: datadogV2.BULKDELETEAPPSDATASTOREITEMSREQUESTDATATYPE_ITEMS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewActionsDatastoresApi(apiClient)
	resp, r, err := api.BulkDeleteDatastoreItems(ctx, DatastoreDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ActionsDatastoresApi.BulkDeleteDatastoreItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ActionsDatastoresApi.BulkDeleteDatastoreItems`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Bulk delete datastore items returns "OK" response
```
// Bulk delete datastore items returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionsDatastoresApi;
import com.datadog.api.client.v2.model.BulkDeleteAppsDatastoreItemsRequest;
import com.datadog.api.client.v2.model.BulkDeleteAppsDatastoreItemsRequestData;
import com.datadog.api.client.v2.model.BulkDeleteAppsDatastoreItemsRequestDataAttributes;
import com.datadog.api.client.v2.model.BulkDeleteAppsDatastoreItemsRequestDataType;
import com.datadog.api.client.v2.model.DeleteAppsDatastoreItemResponseArray;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionsDatastoresApi apiInstance = new ActionsDatastoresApi(defaultClient);

    // there is a valid "datastore" in the system
    String DATASTORE_DATA_ID = System.getenv("DATASTORE_DATA_ID");

    BulkDeleteAppsDatastoreItemsRequest body =
        new BulkDeleteAppsDatastoreItemsRequest()
            .data(
                new BulkDeleteAppsDatastoreItemsRequestData()
                    .attributes(
                        new BulkDeleteAppsDatastoreItemsRequestDataAttributes()
                            .itemKeys(Collections.singletonList("test-key")))
                    .type(BulkDeleteAppsDatastoreItemsRequestDataType.ITEMS));

    try {
      DeleteAppsDatastoreItemResponseArray result =
          apiInstance.bulkDeleteDatastoreItems(DATASTORE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsDatastoresApi#bulkDeleteDatastoreItems");
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

#####  Bulk delete datastore items returns "OK" response
```
"""
Bulk delete datastore items returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request import BulkDeleteAppsDatastoreItemsRequest
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data import (
    BulkDeleteAppsDatastoreItemsRequestData,
)
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_attributes import (
    BulkDeleteAppsDatastoreItemsRequestDataAttributes,
)
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_type import (
    BulkDeleteAppsDatastoreItemsRequestDataType,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = BulkDeleteAppsDatastoreItemsRequest(
    data=BulkDeleteAppsDatastoreItemsRequestData(
        attributes=BulkDeleteAppsDatastoreItemsRequestDataAttributes(
            item_keys=[
                "test-key",
            ],
        ),
        type=BulkDeleteAppsDatastoreItemsRequestDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.bulk_delete_datastore_items(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Bulk delete datastore items returns "OK" response
```
# Bulk delete datastore items returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]

body = DatadogAPIClient::V2::BulkDeleteAppsDatastoreItemsRequest.new({
  data: DatadogAPIClient::V2::BulkDeleteAppsDatastoreItemsRequestData.new({
    attributes: DatadogAPIClient::V2::BulkDeleteAppsDatastoreItemsRequestDataAttributes.new({
      item_keys: [
        "test-key",
      ],
    }),
    type: DatadogAPIClient::V2::BulkDeleteAppsDatastoreItemsRequestDataType::ITEMS,
  }),
})
p api_instance.bulk_delete_datastore_items(DATASTORE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Bulk delete datastore items returns "OK" response
```
// Bulk delete datastore items returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_actions_datastores::ActionsDatastoresAPI;
use datadog_api_client::datadogV2::model::BulkDeleteAppsDatastoreItemsRequest;
use datadog_api_client::datadogV2::model::BulkDeleteAppsDatastoreItemsRequestData;
use datadog_api_client::datadogV2::model::BulkDeleteAppsDatastoreItemsRequestDataAttributes;
use datadog_api_client::datadogV2::model::BulkDeleteAppsDatastoreItemsRequestDataType;

#[tokio::main]
async fn main() {
    // there is a valid "datastore" in the system
    let datastore_data_id = std::env::var("DATASTORE_DATA_ID").unwrap();
    let body = BulkDeleteAppsDatastoreItemsRequest::new().data(
        BulkDeleteAppsDatastoreItemsRequestData::new(
            BulkDeleteAppsDatastoreItemsRequestDataType::ITEMS,
        )
        .attributes(
            BulkDeleteAppsDatastoreItemsRequestDataAttributes::new()
                .item_keys(vec!["test-key".to_string()]),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ActionsDatastoresAPI::with_config(configuration);
    let resp = api
        .bulk_delete_datastore_items(datastore_data_id.clone(), body)
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

#####  Bulk delete datastore items returns "OK" response
```
/**
 * Bulk delete datastore items returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionsDatastoresApi(configuration);

// there is a valid "datastore" in the system
const DATASTORE_DATA_ID = process.env.DATASTORE_DATA_ID as string;

const params: v2.ActionsDatastoresApiBulkDeleteDatastoreItemsRequest = {
  body: {
    data: {
      attributes: {
        itemKeys: ["test-key"],
      },
      type: "items",
    },
  },
  datastoreId: DATASTORE_DATA_ID,
};

apiInstance
  .bulkDeleteDatastoreItems(params)
  .then((data: v2.DeleteAppsDatastoreItemResponseArray) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2267ae36-4a94-47fe-a15d-f43c193f4c76&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=ed719aba-8d27-4a1b-88da-57c8241899fe&pt=Actions%20Datastores&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Factions-datastores%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2267ae36-4a94-47fe-a15d-f43c193f4c76&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=ed719aba-8d27-4a1b-88da-57c8241899fe&pt=Actions%20Datastores&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Factions-datastores%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=ed1ca886-31e3-460f-a068-d49795a8d454&bo=2&sid=c5e1b530f0be11f0ae1ff1e6f8e56999&vid=c5e22300f0be11f08910977dd913337a&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Actions%20Datastores&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Factions-datastores%2F&r=&lt=2049&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=910934)
