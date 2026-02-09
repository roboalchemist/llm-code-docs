# Source: https://docs.datadoghq.com/api/latest/actions-datastores.md

---
title: Actions Datastores
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Actions Datastores
---

# Actions Datastores

Leverage the Actions Datastore API to create, modify, and delete items in datastores owned by your organization.

## List datastores{% #list-datastores %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/actions-datastores |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/actions-datastores |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/actions-datastores      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/actions-datastores      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/actions-datastores     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/actions-datastores |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/actions-datastores |

### Overview

Lists all datastores for the organization. This endpoint requires the `apps_datastore_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A collection of datastores returned by list operations.

| Parent field | Field                           | Type      | Description                                                                                                                                                                                                   |
| ------------ | ------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]          | [object]  | An array of datastore objects containing their configurations and metadata.                                                                                                                                   |
| data         | attributes                      | object    | Detailed information about a datastore.                                                                                                                                                                       |
| attributes   | created_at                      | date-time | Timestamp when the datastore was created.                                                                                                                                                                     |
| attributes   | creator_user_id                 | int64     | The numeric ID of the user who created the datastore.                                                                                                                                                         |
| attributes   | creator_user_uuid               | string    | The UUID of the user who created the datastore.                                                                                                                                                               |
| attributes   | description                     | string    | A human-readable description about the datastore.                                                                                                                                                             |
| attributes   | modified_at                     | date-time | Timestamp when the datastore was last modified.                                                                                                                                                               |
| attributes   | name                            | string    | The display name of the datastore.                                                                                                                                                                            |
| attributes   | org_id                          | int64     | The ID of the organization that owns this datastore.                                                                                                                                                          |
| attributes   | primary_column_name             | string    | The name of the primary key column for this datastore. Primary column names:                                                                                                                                  |
| attributes   | primary_key_generation_strategy | enum      | Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid` |
| data         | id                              | string    | The unique identifier of the datastore.                                                                                                                                                                       |
| data         | type [*required*]          | enum      | The resource type for datastores. Allowed enum values: `datastores`                                                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List datastores returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new
p api_instance.list_datastores()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create datastore{% #create-datastore %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/actions-datastores |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/actions-datastores |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/actions-datastores      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/actions-datastores      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/actions-datastores     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/actions-datastores |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/actions-datastores |

### Overview

Creates a new datastore. This endpoint requires the `apps_datastore_manage` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                                 | Type   | Description                                                                                                                                                                                                   |
| ------------ | ------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                                  | object | Data wrapper containing the configuration needed to create a new datastore.                                                                                                                                   |
| data         | attributes                            | object | Configuration and metadata to create a new datastore.                                                                                                                                                         |
| attributes   | description                           | string | A human-readable description about the datastore.                                                                                                                                                             |
| attributes   | name [*required*]                | string | The display name for the new datastore.                                                                                                                                                                       |
| attributes   | org_access                            | enum   | The organization access level for the datastore. For example, 'contributor'. Allowed enum values: `contributor,viewer,manager`                                                                                |
| attributes   | primary_column_name [*required*] | string | The name of the primary key column for this datastore. Primary column names:                                                                                                                                  |
| attributes   | primary_key_generation_strategy       | enum   | Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid` |
| data         | id                                    | string | Optional ID for the new datastore. If not provided, one will be generated automatically.                                                                                                                      |
| data         | type [*required*]                | enum   | The resource type for datastores. Allowed enum values: `datastores`                                                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response after successfully creating a new datastore, containing the datastore's assigned ID.

| Parent field | Field                  | Type   | Description                                                         |
| ------------ | ---------------------- | ------ | ------------------------------------------------------------------- |
|              | data                   | object | The newly created datastore's data.                                 |
| data         | id                     | string | The unique identifier assigned to the newly created datastore.      |
| data         | type [*required*] | enum   | The resource type for datastores. Allowed enum values: `datastores` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "string",
    "type": "datastores"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get datastore{% #get-datastore %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id} |

### Overview

Retrieves a specific datastore by its ID. This endpoint requires the `apps_datastore_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                         |
| ------------------------------ | ------ | --------------------------------------------------- |
| datastore_id [*required*] | string | The unique identifier of the datastore to retrieve. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A datastore's complete configuration and metadata.

| Parent field | Field                           | Type      | Description                                                                                                                                                                                                   |
| ------------ | ------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                            | object    | Core information about a datastore, including its unique identifier and attributes.                                                                                                                           |
| data         | attributes                      | object    | Detailed information about a datastore.                                                                                                                                                                       |
| attributes   | created_at                      | date-time | Timestamp when the datastore was created.                                                                                                                                                                     |
| attributes   | creator_user_id                 | int64     | The numeric ID of the user who created the datastore.                                                                                                                                                         |
| attributes   | creator_user_uuid               | string    | The UUID of the user who created the datastore.                                                                                                                                                               |
| attributes   | description                     | string    | A human-readable description about the datastore.                                                                                                                                                             |
| attributes   | modified_at                     | date-time | Timestamp when the datastore was last modified.                                                                                                                                                               |
| attributes   | name                            | string    | The display name of the datastore.                                                                                                                                                                            |
| attributes   | org_id                          | int64     | The ID of the organization that owns this datastore.                                                                                                                                                          |
| attributes   | primary_column_name             | string    | The name of the primary key column for this datastore. Primary column names:                                                                                                                                  |
| attributes   | primary_key_generation_strategy | enum      | Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid` |
| data         | id                              | string    | The unique identifier of the datastore.                                                                                                                                                                       |
| data         | type [*required*]          | enum      | The resource type for datastores. Allowed enum values: `datastores`                                                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get datastore returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]
p api_instance.get_datastore(DATASTORE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update datastore{% #update-datastore %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id} |

### Overview

Updates an existing datastore's attributes. This endpoint requires the `apps_datastore_manage` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                         |
| ------------------------------ | ------ | --------------------------------------------------- |
| datastore_id [*required*] | string | The unique identifier of the datastore to retrieve. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                                    |
| ------------ | ---------------------- | ------ | ------------------------------------------------------------------------------ |
|              | data                   | object | Data wrapper containing the datastore identifier and the attributes to update. |
| data         | attributes             | object | Attributes that can be updated on a datastore.                                 |
| attributes   | description            | string | A human-readable description about the datastore.                              |
| attributes   | name                   | string | The display name of the datastore.                                             |
| data         | id                     | string | The unique identifier of the datastore to update.                              |
| data         | type [*required*] | enum   | The resource type for datastores. Allowed enum values: `datastores`            |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A datastore's complete configuration and metadata.

| Parent field | Field                           | Type      | Description                                                                                                                                                                                                   |
| ------------ | ------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                            | object    | Core information about a datastore, including its unique identifier and attributes.                                                                                                                           |
| data         | attributes                      | object    | Detailed information about a datastore.                                                                                                                                                                       |
| attributes   | created_at                      | date-time | Timestamp when the datastore was created.                                                                                                                                                                     |
| attributes   | creator_user_id                 | int64     | The numeric ID of the user who created the datastore.                                                                                                                                                         |
| attributes   | creator_user_uuid               | string    | The UUID of the user who created the datastore.                                                                                                                                                               |
| attributes   | description                     | string    | A human-readable description about the datastore.                                                                                                                                                             |
| attributes   | modified_at                     | date-time | Timestamp when the datastore was last modified.                                                                                                                                                               |
| attributes   | name                            | string    | The display name of the datastore.                                                                                                                                                                            |
| attributes   | org_id                          | int64     | The ID of the organization that owns this datastore.                                                                                                                                                          |
| attributes   | primary_column_name             | string    | The name of the primary key column for this datastore. Primary column names:                                                                                                                                  |
| attributes   | primary_key_generation_strategy | enum      | Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item. Allowed enum values: `none,uuid` |
| data         | id                              | string    | The unique identifier of the datastore.                                                                                                                                                                       |
| data         | type [*required*]          | enum      | The resource type for datastores. Allowed enum values: `datastores`                                                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete datastore{% #delete-datastore %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id} |

### Overview

Deletes a datastore by its unique identifier. This endpoint requires the `apps_datastore_manage` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                         |
| ------------------------------ | ------ | --------------------------------------------------- |
| datastore_id [*required*] | string | The unique identifier of the datastore to retrieve. |

### Response

{% tab title="200" %}
OK
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete datastore returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]
p api_instance.delete_datastore(DATASTORE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## List datastore items{% #list-datastore-items %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/items      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/items      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |

### Overview

Lists items from a datastore. You can filter the results by specifying either an item key or a filter query parameter, but not both at the same time. Supports server-side pagination for large datasets. This endpoint requires the `apps_datastore_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                         |
| ------------------------------ | ------ | --------------------------------------------------- |
| datastore_id [*required*] | string | The unique identifier of the datastore to retrieve. |

#### Query Strings

| Name         | Type    | Description                                                                                                                    |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| filter       | string  | Optional query filter to search items using the [logs search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/). |
| item_key     | string  | Optional primary key value to retrieve a specific item. Cannot be used together with the filter parameter.                     |
| page[limit]  | integer | Optional field to limit the number of items to return per page for pagination. Up to 100 items can be returned per page.       |
| page[offset] | integer | Optional field to offset the number of items to skip from the beginning of the result set for pagination.                      |
| sort         | string  | Optional field to sort results by. Prefix with '-' for descending order (e.g., '-created_at').                                 |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A collection of datastore items with pagination and schema metadata.

| Parent field | Field                  | Type      | Description                                                                              |
| ------------ | ---------------------- | --------- | ---------------------------------------------------------------------------------------- |
|              | data [*required*] | [object]  | An array of datastore items with their content and metadata.                             |
| data         | attributes             | object    | Metadata and content of a datastore item.                                                |
| attributes   | created_at             | date-time | Timestamp when the item was first created.                                               |
| attributes   | modified_at            | date-time | Timestamp when the item was last modified.                                               |
| attributes   | org_id                 | int64     | The ID of the organization that owns this item.                                          |
| attributes   | primary_column_name    | string    | The name of the primary key column for this datastore. Primary column names:             |
| attributes   | signature              | string    | A unique signature identifying this item version.                                        |
| attributes   | store_id               | string    | The unique identifier of the datastore containing this item.                             |
| attributes   | value                  | object    | The data content (as key-value pairs) of a datastore item.                               |
| data         | id                     | string    | The unique identifier of the datastore.                                                  |
| data         | type [*required*] | enum      | The resource type for datastore items. Allowed enum values: `items`                      |
|              | meta                   | object    | Metadata about the included items, including pagination info and datastore schema.       |
| meta         | page                   | object    | Pagination information for a collection of datastore items.                              |
| page         | hasMore                | boolean   | Whether there are additional pages of items beyond the current page.                     |
| page         | totalCount             | int64     | The total number of items in the datastore, ignoring any filters.                        |
| page         | totalFilteredCount     | int64     | The total number of items that match the current filter criteria.                        |
| meta         | schema                 | object    | Schema information about the datastore, including its primary key and field definitions. |
| schema       | fields                 | [object]  | An array describing the columns available in this datastore.                             |
| fields       | name [*required*] | string    | The name of this column in the datastore.                                                |
| fields       | type [*required*] | string    | The data type of this column. For example, 'string', 'number', or 'boolean'.             |
| schema       | primary_key            | string    | The name of the primary key column for this datastore.                                   |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List datastore items returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionsDatastoresAPI.new

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = ENV["DATASTORE_DATA_ID"]
p api_instance.list_datastore_items(DATASTORE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete datastore item{% #delete-datastore-item %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/items      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/items      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |

### Overview

Deletes an item from a datastore by its key. This endpoint requires the `apps_datastore_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                         |
| ------------------------------ | ------ | --------------------------------------------------- |
| datastore_id [*required*] | string | The unique identifier of the datastore to retrieve. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                      | Type   | Description                                                                                      |
| ------------ | -------------------------- | ------ | ------------------------------------------------------------------------------------------------ |
|              | data                       | object | Data wrapper containing the information needed to identify and delete a specific datastore item. |
| data         | attributes                 | object | Attributes specifying which datastore item to delete by its primary key.                         |
| attributes   | id                         | string | Optional unique identifier of the item to delete.                                                |
| attributes   | item_key [*required*] | string | The primary key value that identifies the item to delete. Cannot exceed 256 characters.          |
| data         | type [*required*]     | enum   | The resource type for datastore items. Allowed enum values: `items`                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "item_key": "test-key"
    },
    "type": "items"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response from successfully deleting a datastore item.

| Parent field | Field                  | Type   | Description                                                                         |
| ------------ | ---------------------- | ------ | ----------------------------------------------------------------------------------- |
|              | data                   | object | Data containing the identifier of the datastore item that was successfully deleted. |
| data         | id                     | string | The unique identifier of the item that was deleted.                                 |
| data         | type [*required*] | enum   | The resource type for datastore items. Allowed enum values: `items`                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "string",
    "type": "items"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update datastore item{% #update-datastore-item %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/items      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/items      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items |

### Overview

Partially updates an item in a datastore by its key. This endpoint requires the `apps_datastore_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                         |
| ------------------------------ | ------ | --------------------------------------------------- |
| datastore_id [*required*] | string | The unique identifier of the datastore to retrieve. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                          | Type   | Description                                                                                       |
| ------------ | ------------------------------ | ------ | ------------------------------------------------------------------------------------------------- |
|              | data                           | object | Data wrapper containing the item identifier and the changes to apply during the update operation. |
| data         | attributes                     | object | Attributes for updating a datastore item, including the item key and changes to apply.            |
| attributes   | id                             | string | The unique identifier of the item being updated.                                                  |
| attributes   | item_changes [*required*] | object | Changes to apply to a datastore item using set operations.                                        |
| item_changes | ops_set                        | object | Set operation that contains key-value pairs to set on the datastore item.                         |
| attributes   | item_key [*required*]     | string | The primary key that identifies the item to update. Cannot exceed 256 characters.                 |
| data         | id                             | string | The unique identifier of the datastore item.                                                      |
| data         | type [*required*]         | enum   | The resource type for datastore items. Allowed enum values: `items`                               |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A single datastore item with its content and metadata.

| Parent field | Field                  | Type      | Description                                                                  |
| ------------ | ---------------------- | --------- | ---------------------------------------------------------------------------- |
|              | data                   | object    | Core data and metadata for a single datastore item.                          |
| data         | attributes             | object    | Metadata and content of a datastore item.                                    |
| attributes   | created_at             | date-time | Timestamp when the item was first created.                                   |
| attributes   | modified_at            | date-time | Timestamp when the item was last modified.                                   |
| attributes   | org_id                 | int64     | The ID of the organization that owns this item.                              |
| attributes   | primary_column_name    | string    | The name of the primary key column for this datastore. Primary column names: |
| attributes   | signature              | string    | A unique signature identifying this item version.                            |
| attributes   | store_id               | string    | The unique identifier of the datastore containing this item.                 |
| attributes   | value                  | object    | The data content (as key-value pairs) of a datastore item.                   |
| data         | id                     | string    | The unique identifier of the datastore.                                      |
| data         | type [*required*] | enum      | The resource type for datastore items. Allowed enum values: `items`          |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Bulk write datastore items{% #bulk-write-datastore-items %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                           |
| ----------------- | -------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/items/bulk      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/items/bulk      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |

### Overview

Creates or replaces multiple items in a datastore by their keys in a single operation. This endpoint requires the `apps_datastore_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                         |
| ------------------------------ | ------ | --------------------------------------------------- |
| datastore_id [*required*] | string | The unique identifier of the datastore to retrieve. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                    | Type     | Description                                                                                                                                                              |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                     | object   | Data wrapper containing the items to insert and their configuration for the bulk insert operation.                                                                       |
| data         | attributes               | object   | Configuration for bulk inserting multiple items into a datastore.                                                                                                        |
| attributes   | conflict_mode            | enum     | How to handle conflicts when inserting items that already exist in the datastore. Allowed enum values: `fail_on_conflict,overwrite_on_conflict`                          |
| attributes   | values [*required*] | [object] | An array of items to add to the datastore, where each item is a set of key-value pairs representing the item's data. Up to 100 items can be updated in a single request. |
| data         | type [*required*]   | enum     | The resource type for datastore items. Allowed enum values: `items`                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response after successfully inserting multiple items into a datastore, containing the identifiers of the created items.

| Parent field | Field                  | Type     | Description                                                                             |
| ------------ | ---------------------- | -------- | --------------------------------------------------------------------------------------- |
|              | data [*required*] | [object] | An array of data objects containing the identifiers of the successfully inserted items. |
| data         | id                     | string   | The unique identifier assigned to the inserted item.                                    |
| data         | type [*required*] | enum     | The resource type for datastore items. Allowed enum values: `items`                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "string",
      "type": "items"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items/bulk" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Bulk delete datastore items{% #bulk-delete-datastore-items %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/actions-datastores/{datastore_id}/items/bulk      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/actions-datastores/{datastore_id}/items/bulk      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/actions-datastores/{datastore_id}/items/bulk |

### Overview

Deletes multiple items from a datastore by their keys in a single operation. This endpoint requires the `apps_datastore_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| datastore_id [*required*] | string | The ID of the datastore. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                          |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
|              | data                   | object   | Data wrapper containing the data needed to delete items from a datastore.                                            |
| data         | attributes             | object   | Attributes of request data to delete items from a datastore.                                                         |
| attributes   | item_keys              | [string] | List of primary keys identifying items to delete from datastore. Up to 100 items can be deleted in a single request. |
| data         | id                     | string   | ID for the datastore of the items to delete.                                                                         |
| data         | type [*required*] | enum     | Items resource type. Allowed enum values: `items`                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `DeleteAppsDatastoreItemResponseArray` object.

| Parent field | Field                  | Type     | Description                                                         |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------- |
|              | data [*required*] | [object] | The `DeleteAppsDatastoreItemResponseArray` `data`.                  |
| data         | id                     | string   | The unique identifier of the item that was deleted.                 |
| data         | type [*required*] | enum     | The resource type for datastore items. Allowed enum values: `items` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "string",
      "type": "items"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

### Code Example

##### 
                          \# Path parametersexport datastore_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions-datastores/${datastore_id}/items/bulk" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
