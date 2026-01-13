# Source: https://docs.datadoghq.com/api/latest/app-builder/

# App Builder
Datadog App Builder provides a low-code solution to rapidly develop and integrate secure, customized applications into your monitoring stack that are built to accelerate remediation at scale. These API endpoints allow you to create, read, update, delete, and publish apps.
## [List Apps](https://docs.datadoghq.com/api/latest/app-builder/#list-apps)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#list-apps-v2)


GET https://api.ap1.datadoghq.com/api/v2/app-builder/appshttps://api.ap2.datadoghq.com/api/v2/app-builder/appshttps://api.datadoghq.eu/api/v2/app-builder/appshttps://api.ddog-gov.com/api/v2/app-builder/appshttps://api.datadoghq.com/api/v2/app-builder/appshttps://api.us3.datadoghq.com/api/v2/app-builder/appshttps://api.us5.datadoghq.com/api/v2/app-builder/apps
### Overview
List all apps, with optional filters and sorting. This endpoint is paginated. Only basic app information such as the app ID, name, and description is returned by this endpoint. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `apps_run` permission.
### Arguments
#### Query Strings
Name
Type
Description
limit
integer
The number of apps to return per page.
page
integer
The page number to return.
filter[user_name]
string
Filter apps by the app creator. Usually the user’s email.
filter[user_uuid]
string
Filter apps by the app creator’s UUID.
filter[name]
string
Filter by app name.
filter[query]
string
Filter apps by the app name or the app creator.
filter[deployed]
boolean
Filter apps by whether they are published.
filter[tags]
string
Filter apps by tags.
filter[favorite]
boolean
Filter apps by whether you have added them to your favorites.
filter[self_service]
boolean
Filter apps by whether they are enabled for self-service.
sort
array
The fields and direction to sort apps by.
### Response
  * [200](https://docs.datadoghq.com/api/latest/app-builder/#ListApps-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#ListApps-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#ListApps-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#ListApps-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


A paginated list of apps matching the specified filters and sorting.
Field
Type
Description
data
[object]
An array of app definitions.
attributes [_required_]
object
Basic information about the app such as name, description, and tags.
description
string
A human-readable description for the app.
favorite
boolean
Whether the app is marked as a favorite by the current user.
name
string
The name of the app.
selfService
boolean
Whether the app is enabled for use in the Datadog self-service hub.
tags
[string]
A list of tags for the app, which can be used to filter apps.
id [_required_]
uuid
The ID of the app.
meta
object
Metadata of an app.
created_at
date-time
Timestamp of when the app was created.
deleted_at
date-time
Timestamp of when the app was deleted.
org_id
int64
The Datadog organization ID that owns the app.
updated_at
date-time
Timestamp of when the app was last updated.
updated_since_deployment
boolean
Whether the app was updated since it was last published. Published apps are pinned to a specific version and do not automatically update when the app is updated.
user_id
int64
The ID of the user who created the app.
user_name
string
The name (or email address) of the user who created the app.
user_uuid
uuid
The UUID of the user who created the app.
version
int64
The version number of the app. This starts at 1 and increments with each update.
relationships
object
The app's publication information.
deployment
object
Information pointing to the app's publication status.
data
object
Data object containing the deployment ID.
id
uuid
The deployment ID.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
included
[object]
Data on the version of the app that was published.
attributes
object
The attributes object containing the version ID of the published app.
app_version_id
uuid
The version ID of the app that was published. For an unpublished app, this is always the nil UUID (`00000000-0000-0000-0000-000000000000`).
id
uuid
The deployment ID.
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
meta
object
Pagination metadata.
page
object
Information on the total number of apps, to be used for pagination.
totalCount
int64
The total number of apps under the Datadog organization, disregarding any filters applied.
totalFilteredCount
int64
The total number of apps that match the specified filters.
```
{
  "data": [
    {
      "attributes": {
        "description": "string",
        "favorite": false,
        "name": "string",
        "selfService": false,
        "tags": [
          "service:webshop-backend",
          "team:webshop"
        ]
      },
      "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
      "meta": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "deleted_at": "2019-09-19T10:00:00.000Z",
        "org_id": "integer",
        "updated_at": "2019-09-19T10:00:00.000Z",
        "updated_since_deployment": false,
        "user_id": "integer",
        "user_name": "string",
        "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
        "version": "integer"
      },
      "relationships": {
        "deployment": {
          "data": {
            "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
            "type": "deployment"
          },
          "meta": {
            "created_at": "2019-09-19T10:00:00.000Z",
            "user_id": "integer",
            "user_name": "string",
            "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
          }
        }
      },
      "type": "appDefinitions"
    }
  ],
  "included": [
    {
      "attributes": {
        "app_version_id": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      },
      "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
      "meta": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "user_id": "integer",
        "user_name": "string",
        "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      },
      "type": "deployment"
    }
  ],
  "meta": {
    "page": {
      "totalCount": "integer",
      "totalFilteredCount": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  List Apps
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Apps
```
"""
List Apps returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.list_apps()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Apps
```
# List Apps returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new
p api_instance.list_apps()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Apps
```
// List Apps returns "OK" response

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
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.ListApps(ctx, *datadogV2.NewListAppsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.ListApps`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.ListApps`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Apps
```
// List Apps returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.ListAppsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    try {
      ListAppsResponse result = apiInstance.listApps();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#listApps");
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

#####  List Apps
```
// List Apps returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;
use datadog_api_client::datadogV2::api_app_builder::ListAppsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api.list_apps(ListAppsOptionalParams::default()).await;
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

#####  List Apps
```
/**
 * List Apps returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

apiInstance
  .listApps()
  .then((data: v2.ListAppsResponse) => {
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
## [Create App](https://docs.datadoghq.com/api/latest/app-builder/#create-app)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#create-app-v2)


POST https://api.ap1.datadoghq.com/api/v2/app-builder/appshttps://api.ap2.datadoghq.com/api/v2/app-builder/appshttps://api.datadoghq.eu/api/v2/app-builder/appshttps://api.ddog-gov.com/api/v2/app-builder/appshttps://api.datadoghq.com/api/v2/app-builder/appshttps://api.us3.datadoghq.com/api/v2/app-builder/appshttps://api.us5.datadoghq.com/api/v2/app-builder/apps
### Overview
Create a new app, returning the app ID. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires all of the following permissions:
* `apps_write`
* `connections_resolve`
* `workflows_run`
  

### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


Field
Type
Description
data
object
The data object containing the app definition.
attributes
object
App definition attributes such as name, description, and components.
components
[object]
The UI components that make up the app.
events
[object]
Events to listen for on the grid component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the grid component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this grid component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a grid component.
backgroundColor
string
The background color of the grid.
default: `default`
children
[object]
The child components of the grid.
events
[object]
Events to listen for on the UI component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the UI component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this UI component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a UI component. Different component types can have their own additional unique properties. See the [components documentation](https://docs.datadoghq.com/service_management/app_builder/components/) for more detail on each component type and its properties.
children
[object]
The child components of the UI component.
isVisible
<oneOf>
Whether the UI component is visible. If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
type [_required_]
enum
The UI component type. Allowed enum values: `table,textInput,textArea,button,text,select,modal,schemaForm,checkbox,tabs,vegaChart,radioButtons,numberInput,fileInput,jsonInput,gridCell,dateRangePicker,search,container,calloutValue`
isVisible
<oneOf>
Whether the grid component and its children are visible. If a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
string
Option 2
boolean
default: `true`
type [_required_]
enum
The grid component type. Allowed enum values: `grid`
default: `grid`
description
string
A human-readable description for the app.
name
string
The name of the app.
queries
[ <oneOf>]
An array of queries, such as external actions and state variables, that the app uses.
Option 1
object
An action query. This query type is used to trigger an action, such as sending a HTTP request.
events
[object]
Events to listen for downstream of the action query.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id [_required_]
uuid
The ID of the action query.
name [_required_]
string
A unique identifier for this action query. This name is also used to access the query's result throughout the app.
properties [_required_]
object
The properties of the action query.
condition
<oneOf>
Whether to run this query. If specified, the query will only run if this condition evaluates to `true` in JavaScript and all other conditions are also met.
Option 1
boolean
Option 2
string
debounceInMs
<oneOf>
The minimum time in milliseconds that must pass before the query can be triggered again. This is useful for preventing accidental double-clicks from triggering the query multiple times.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
mockedOutputs
<oneOf>
The mocked outputs of the action query. This is useful for testing the app without actually running the action.
Option 1
string
Option 2
object
The mocked outputs of the action query.
enabled [_required_]
<oneOf>
Whether to enable the mocked outputs for testing.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The mocked outputs of the action query, serialized as JSON.
onlyTriggerManually
<oneOf>
Determines when this query is executed. If set to `false`, the query will run when the app loads and whenever any query arguments change. If set to `true`, the query will only run when manually triggered from elsewhere in the app.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The post-query transformation function, which is a JavaScript function that changes the query's `.outputs` property after the query's execution.
pollingIntervalInMs
<oneOf>
If specified, the app will poll the query at the specified interval in milliseconds. The minimum polling interval is 15 seconds. The query will only poll when the app's browser tab is active.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
requiresConfirmation
<oneOf>
Whether to prompt the user to confirm this query before it runs.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
showToastOnError
<oneOf>
Whether to display a toast to the user when the query returns an error.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
spec [_required_]
<oneOf>
The definition of the action query.
Option 1
string
Option 2
object
The action query spec object.
connectionGroup
object
The connection group to use for an action query.
id
uuid
The ID of the connection group.
tags
[string]
The tags of the connection group.
connectionId
string
The ID of the custom connection to use for this action query.
fqn [_required_]
string
The fully qualified name of the action type.
inputs
<oneOf>
The inputs to the action query. These are the values that are passed to the action when it is triggered.
Option 1
string
Option 2
object
The inputs to the action query. See the [Actions Catalog](https://docs.datadoghq.com/actions/actions_catalog/) for more detail on each action and its inputs.
type [_required_]
enum
The action query type. Allowed enum values: `action`
default: `action`
Option 2
object
A data transformer, which is custom JavaScript code that executes and transforms data when its inputs change.
id [_required_]
uuid
The ID of the data transformer.
name [_required_]
string
A unique identifier for this data transformer. This name is also used to access the transformer's result throughout the app.
properties [_required_]
object
The properties of the data transformer.
outputs
string
A JavaScript function that returns the transformed data.
type [_required_]
enum
The data transform type. Allowed enum values: `dataTransform`
default: `dataTransform`
Option 3
object
A variable, which can be set and read by other components in the app.
id [_required_]
uuid
The ID of the state variable.
name [_required_]
string
A unique identifier for this state variable. This name is also used to access the variable's value throughout the app.
properties [_required_]
object
The properties of the state variable.
defaultValue
The default value of the state variable.
type [_required_]
enum
The state variable type. Allowed enum values: `stateVariable`
default: `stateVariable`
rootInstanceName
string
The name of the root component of the app. This must be a `grid` component that contains all other components.
tags
[string]
A list of tags for the app, which can be used to filter apps.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
```
{
  "data": {
    "type": "appDefinitions",
    "attributes": {
      "rootInstanceName": "grid0",
      "components": [
        {
          "name": "grid0",
          "type": "grid",
          "properties": {
            "children": [
              {
                "type": "gridCell",
                "name": "gridCell0",
                "properties": {
                  "children": [
                    {
                      "name": "text0",
                      "type": "text",
                      "properties": {
                        "content": "# Cat Facts",
                        "contentType": "markdown",
                        "textAlign": "left",
                        "verticalAlign": "top",
                        "isVisible": true
                      },
                      "events": []
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 0,
                      "y": 0,
                      "width": 4,
                      "height": 5
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell2",
                "properties": {
                  "children": [
                    {
                      "name": "table0",
                      "type": "table",
                      "properties": {
                        "data": "${fetchFacts?.outputs?.body?.data}",
                        "columns": [
                          {
                            "dataPath": "fact",
                            "header": "fact",
                            "isHidden": false,
                            "id": "0ae2ae9e-0280-4389-83c6-1c5949f7e674"
                          },
                          {
                            "dataPath": "length",
                            "header": "length",
                            "isHidden": true,
                            "id": "c9048611-0196-4a00-9366-1ef9e3ec0408"
                          },
                          {
                            "id": "8fa9284b-7a58-4f13-9959-57b7d8a7fe8f",
                            "dataPath": "Due Date",
                            "header": "Unused Old Column",
                            "disableSortBy": false,
                            "formatter": {
                              "type": "formatted_time",
                              "format": "LARGE_WITHOUT_TIME"
                            },
                            "isDeleted": true
                          }
                        ],
                        "summary": true,
                        "pageSize": "${pageSize?.value}",
                        "paginationType": "server_side",
                        "isLoading": "${fetchFacts?.isLoading}",
                        "rowButtons": [],
                        "isWrappable": false,
                        "isScrollable": "vertical",
                        "isSubRowsEnabled": false,
                        "globalFilter": false,
                        "isVisible": true,
                        "totalCount": "${fetchFacts?.outputs?.body?.total}"
                      },
                      "events": []
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 0,
                      "y": 5,
                      "width": 12,
                      "height": 96
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell1",
                "properties": {
                  "children": [
                    {
                      "name": "text1",
                      "type": "text",
                      "properties": {
                        "content": "## Random Fact\n\n${randomFact?.outputs?.fact}",
                        "contentType": "markdown",
                        "textAlign": "left",
                        "verticalAlign": "top",
                        "isVisible": true
                      },
                      "events": []
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 0,
                      "y": 101,
                      "width": 12,
                      "height": 16
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell3",
                "properties": {
                  "children": [
                    {
                      "name": "button0",
                      "type": "button",
                      "properties": {
                        "label": "Increase Page Size",
                        "level": "default",
                        "isPrimary": true,
                        "isBorderless": false,
                        "isLoading": false,
                        "isDisabled": false,
                        "isVisible": true,
                        "iconLeft": "angleUp",
                        "iconRight": ""
                      },
                      "events": [
                        {
                          "variableName": "pageSize",
                          "value": "${pageSize?.value + 1}",
                          "name": "click",
                          "type": "setStateVariableValue"
                        }
                      ]
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 10,
                      "y": 134,
                      "width": 2,
                      "height": 4
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell4",
                "properties": {
                  "children": [
                    {
                      "name": "button1",
                      "type": "button",
                      "properties": {
                        "label": "Decrease Page Size",
                        "level": "default",
                        "isPrimary": true,
                        "isBorderless": false,
                        "isLoading": false,
                        "isDisabled": false,
                        "isVisible": true,
                        "iconLeft": "angleDown",
                        "iconRight": ""
                      },
                      "events": [
                        {
                          "variableName": "pageSize",
                          "value": "${pageSize?.value - 1}",
                          "name": "click",
                          "type": "setStateVariableValue"
                        }
                      ]
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 10,
                      "y": 138,
                      "width": 2,
                      "height": 4
                    }
                  }
                },
                "events": []
              }
            ],
            "backgroundColor": "default"
          },
          "events": []
        }
      ],
      "queries": [
        {
          "id": "92ff0bb8-553b-4f31-87c7-ef5bd16d47d5",
          "type": "action",
          "name": "fetchFacts",
          "events": [],
          "properties": {
            "spec": {
              "fqn": "com.datadoghq.http.request",
              "connectionId": "5e63f4a8-4ce6-47de-ba11-f6617c1d54f3",
              "inputs": {
                "verb": "GET",
                "url": "https://catfact.ninja/facts",
                "urlParams": [
                  {
                    "key": "limit",
                    "value": "${pageSize.value.toString()}"
                  },
                  {
                    "key": "page",
                    "value": "${(table0.pageIndex + 1).toString()}"
                  }
                ]
              }
            }
          }
        },
        {
          "type": "stateVariable",
          "name": "pageSize",
          "properties": {
            "defaultValue": "${20}"
          },
          "id": "afd03c81-4075-4432-8618-ba09d52d2f2d"
        },
        {
          "type": "dataTransform",
          "name": "randomFact",
          "properties": {
            "outputs": "${(() => {const facts = fetchFacts.outputs.body.data\nreturn facts[Math.floor(Math.random()*facts.length)]\n})()}"
          },
          "id": "0fb22859-47dc-4137-9e41-7b67d04c525c"
        }
      ],
      "name": "Example Cat Facts Viewer",
      "description": "This is a slightly complicated example app that fetches and displays cat facts"
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/app-builder/#CreateApp-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#CreateApp-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#CreateApp-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#CreateApp-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


The response object after a new app is successfully created, with the app ID.
Field
Type
Description
data
object
The data object containing the app ID.
id [_required_]
uuid
The ID of the created app.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
```
{
  "data": {
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "type": "appDefinitions"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  Create App returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "appDefinitions",
    "attributes": {
      "rootInstanceName": "grid0",
      "components": [
        {
          "name": "grid0",
          "type": "grid",
          "properties": {
            "children": [
              {
                "type": "gridCell",
                "name": "gridCell0",
                "properties": {
                  "children": [
                    {
                      "name": "text0",
                      "type": "text",
                      "properties": {
                        "content": "# Cat Facts",
                        "contentType": "markdown",
                        "textAlign": "left",
                        "verticalAlign": "top",
                        "isVisible": true
                      },
                      "events": []
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 0,
                      "y": 0,
                      "width": 4,
                      "height": 5
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell2",
                "properties": {
                  "children": [
                    {
                      "name": "table0",
                      "type": "table",
                      "properties": {
                        "data": "${fetchFacts?.outputs?.body?.data}",
                        "columns": [
                          {
                            "dataPath": "fact",
                            "header": "fact",
                            "isHidden": false,
                            "id": "0ae2ae9e-0280-4389-83c6-1c5949f7e674"
                          },
                          {
                            "dataPath": "length",
                            "header": "length",
                            "isHidden": true,
                            "id": "c9048611-0196-4a00-9366-1ef9e3ec0408"
                          },
                          {
                            "id": "8fa9284b-7a58-4f13-9959-57b7d8a7fe8f",
                            "dataPath": "Due Date",
                            "header": "Unused Old Column",
                            "disableSortBy": false,
                            "formatter": {
                              "type": "formatted_time",
                              "format": "LARGE_WITHOUT_TIME"
                            },
                            "isDeleted": true
                          }
                        ],
                        "summary": true,
                        "pageSize": "${pageSize?.value}",
                        "paginationType": "server_side",
                        "isLoading": "${fetchFacts?.isLoading}",
                        "rowButtons": [],
                        "isWrappable": false,
                        "isScrollable": "vertical",
                        "isSubRowsEnabled": false,
                        "globalFilter": false,
                        "isVisible": true,
                        "totalCount": "${fetchFacts?.outputs?.body?.total}"
                      },
                      "events": []
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 0,
                      "y": 5,
                      "width": 12,
                      "height": 96
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell1",
                "properties": {
                  "children": [
                    {
                      "name": "text1",
                      "type": "text",
                      "properties": {
                        "content": "## Random Fact\n\n${randomFact?.outputs?.fact}",
                        "contentType": "markdown",
                        "textAlign": "left",
                        "verticalAlign": "top",
                        "isVisible": true
                      },
                      "events": []
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 0,
                      "y": 101,
                      "width": 12,
                      "height": 16
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell3",
                "properties": {
                  "children": [
                    {
                      "name": "button0",
                      "type": "button",
                      "properties": {
                        "label": "Increase Page Size",
                        "level": "default",
                        "isPrimary": true,
                        "isBorderless": false,
                        "isLoading": false,
                        "isDisabled": false,
                        "isVisible": true,
                        "iconLeft": "angleUp",
                        "iconRight": ""
                      },
                      "events": [
                        {
                          "variableName": "pageSize",
                          "value": "${pageSize?.value + 1}",
                          "name": "click",
                          "type": "setStateVariableValue"
                        }
                      ]
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 10,
                      "y": 134,
                      "width": 2,
                      "height": 4
                    }
                  }
                },
                "events": []
              },
              {
                "type": "gridCell",
                "name": "gridCell4",
                "properties": {
                  "children": [
                    {
                      "name": "button1",
                      "type": "button",
                      "properties": {
                        "label": "Decrease Page Size",
                        "level": "default",
                        "isPrimary": true,
                        "isBorderless": false,
                        "isLoading": false,
                        "isDisabled": false,
                        "isVisible": true,
                        "iconLeft": "angleDown",
                        "iconRight": ""
                      },
                      "events": [
                        {
                          "variableName": "pageSize",
                          "value": "${pageSize?.value - 1}",
                          "name": "click",
                          "type": "setStateVariableValue"
                        }
                      ]
                    }
                  ],
                  "isVisible": "true",
                  "layout": {
                    "default": {
                      "x": 10,
                      "y": 138,
                      "width": 2,
                      "height": 4
                    }
                  }
                },
                "events": []
              }
            ],
            "backgroundColor": "default"
          },
          "events": []
        }
      ],
      "queries": [
        {
          "id": "92ff0bb8-553b-4f31-87c7-ef5bd16d47d5",
          "type": "action",
          "name": "fetchFacts",
          "events": [],
          "properties": {
            "spec": {
              "fqn": "com.datadoghq.http.request",
              "connectionId": "5e63f4a8-4ce6-47de-ba11-f6617c1d54f3",
              "inputs": {
                "verb": "GET",
                "url": "https://catfact.ninja/facts",
                "urlParams": [
                  {
                    "key": "limit",
                    "value": "${pageSize.value.toString()}"
                  },
                  {
                    "key": "page",
                    "value": "${(table0.pageIndex + 1).toString()}"
                  }
                ]
              }
            }
          }
        },
        {
          "type": "stateVariable",
          "name": "pageSize",
          "properties": {
            "defaultValue": "${20}"
          },
          "id": "afd03c81-4075-4432-8618-ba09d52d2f2d"
        },
        {
          "type": "dataTransform",
          "name": "randomFact",
          "properties": {
            "outputs": "${(() => {const facts = fetchFacts.outputs.body.data\nreturn facts[Math.floor(Math.random()*facts.length)]\n})()}"
          },
          "id": "0fb22859-47dc-4137-9e41-7b67d04c525c"
        }
      ],
      "name": "Example Cat Facts Viewer",
      "description": "This is a slightly complicated example app that fetches and displays cat facts"
    }
  }
}
EOF  

                        
```

#####  Create App returns "Created" response
```
// Create App returns "Created" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	body := datadogV2.CreateAppRequest{
		Data: &datadogV2.CreateAppRequestData{
			Type: datadogV2.APPDEFINITIONTYPE_APPDEFINITIONS,
			Attributes: &datadogV2.CreateAppRequestDataAttributes{
				RootInstanceName: datadog.PtrString("grid0"),
				Components: []datadogV2.ComponentGrid{
					{
						Name: "grid0",
						Type: datadogV2.COMPONENTGRIDTYPE_GRID,
						Properties: datadogV2.ComponentGridProperties{
							Children: []datadogV2.Component{
								{
									Type: datadogV2.COMPONENTTYPE_GRIDCELL,
									Name: "gridCell0",
									Properties: datadogV2.ComponentProperties{
										Children: []datadogV2.Component{
											{
												Name: "text0",
												Type: datadogV2.COMPONENTTYPE_TEXT,
												Properties: datadogV2.ComponentProperties{
													IsVisible: &datadogV2.ComponentPropertiesIsVisible{
														Bool: datadog.PtrBool(true)},
												},
												Events: []datadogV2.AppBuilderEvent{},
											},
										},
										IsVisible: &datadogV2.ComponentPropertiesIsVisible{
											String: datadog.PtrString("true")},
									},
									Events: []datadogV2.AppBuilderEvent{},
								},
								{
									Type: datadogV2.COMPONENTTYPE_GRIDCELL,
									Name: "gridCell2",
									Properties: datadogV2.ComponentProperties{
										Children: []datadogV2.Component{
											{
												Name: "table0",
												Type: datadogV2.COMPONENTTYPE_TABLE,
												Properties: datadogV2.ComponentProperties{
													IsVisible: &datadogV2.ComponentPropertiesIsVisible{
														Bool: datadog.PtrBool(true)},
												},
												Events: []datadogV2.AppBuilderEvent{},
											},
										},
										IsVisible: &datadogV2.ComponentPropertiesIsVisible{
											String: datadog.PtrString("true")},
									},
									Events: []datadogV2.AppBuilderEvent{},
								},
								{
									Type: datadogV2.COMPONENTTYPE_GRIDCELL,
									Name: "gridCell1",
									Properties: datadogV2.ComponentProperties{
										Children: []datadogV2.Component{
											{
												Name: "text1",
												Type: datadogV2.COMPONENTTYPE_TEXT,
												Properties: datadogV2.ComponentProperties{
													IsVisible: &datadogV2.ComponentPropertiesIsVisible{
														Bool: datadog.PtrBool(true)},
												},
												Events: []datadogV2.AppBuilderEvent{},
											},
										},
										IsVisible: &datadogV2.ComponentPropertiesIsVisible{
											String: datadog.PtrString("true")},
									},
									Events: []datadogV2.AppBuilderEvent{},
								},
								{
									Type: datadogV2.COMPONENTTYPE_GRIDCELL,
									Name: "gridCell3",
									Properties: datadogV2.ComponentProperties{
										Children: []datadogV2.Component{
											{
												Name: "button0",
												Type: datadogV2.COMPONENTTYPE_BUTTON,
												Properties: datadogV2.ComponentProperties{
													IsVisible: &datadogV2.ComponentPropertiesIsVisible{
														Bool: datadog.PtrBool(true)},
												},
												Events: []datadogV2.AppBuilderEvent{
													{
														Name: datadogV2.APPBUILDEREVENTNAME_CLICK.Ptr(),
														Type: datadogV2.APPBUILDEREVENTTYPE_SETSTATEVARIABLEVALUE.Ptr(),
													},
												},
											},
										},
										IsVisible: &datadogV2.ComponentPropertiesIsVisible{
											String: datadog.PtrString("true")},
									},
									Events: []datadogV2.AppBuilderEvent{},
								},
								{
									Type: datadogV2.COMPONENTTYPE_GRIDCELL,
									Name: "gridCell4",
									Properties: datadogV2.ComponentProperties{
										Children: []datadogV2.Component{
											{
												Name: "button1",
												Type: datadogV2.COMPONENTTYPE_BUTTON,
												Properties: datadogV2.ComponentProperties{
													IsVisible: &datadogV2.ComponentPropertiesIsVisible{
														Bool: datadog.PtrBool(true)},
												},
												Events: []datadogV2.AppBuilderEvent{
													{
														Name: datadogV2.APPBUILDEREVENTNAME_CLICK.Ptr(),
														Type: datadogV2.APPBUILDEREVENTTYPE_SETSTATEVARIABLEVALUE.Ptr(),
													},
												},
											},
										},
										IsVisible: &datadogV2.ComponentPropertiesIsVisible{
											String: datadog.PtrString("true")},
									},
									Events: []datadogV2.AppBuilderEvent{},
								},
							},
							BackgroundColor: datadog.PtrString("default"),
						},
						Events: []datadogV2.AppBuilderEvent{},
					},
				},
				Queries: []datadogV2.Query{
					datadogV2.Query{
						ActionQuery: &datadogV2.ActionQuery{
							Id:     uuid.MustParse("92ff0bb8-553b-4f31-87c7-ef5bd16d47d5"),
							Type:   datadogV2.ACTIONQUERYTYPE_ACTION,
							Name:   "fetchFacts",
							Events: []datadogV2.AppBuilderEvent{},
							Properties: datadogV2.ActionQueryProperties{
								Spec: datadogV2.ActionQuerySpec{
									ActionQuerySpecObject: &datadogV2.ActionQuerySpecObject{
										Fqn:          "com.datadoghq.http.request",
										ConnectionId: datadog.PtrString("5e63f4a8-4ce6-47de-ba11-f6617c1d54f3"),
										Inputs: &datadogV2.ActionQuerySpecInputs{
											ActionQuerySpecInput: map[string]interface{}{
												"verb":      "GET",
												"url":       "https://catfact.ninja/facts",
												"urlParams": "[{'key': 'limit', 'value': '${pageSize.value.toString()}'}, {'key': 'page', 'value': '${(table0.pageIndex + 1).toString()}'}]",
											}},
									}},
							},
						}},
					datadogV2.Query{
						StateVariable: &datadogV2.StateVariable{
							Type: datadogV2.STATEVARIABLETYPE_STATEVARIABLE,
							Name: "pageSize",
							Properties: datadogV2.StateVariableProperties{
								DefaultValue: "${20}",
							},
							Id: uuid.MustParse("afd03c81-4075-4432-8618-ba09d52d2f2d"),
						}},
					datadogV2.Query{
						DataTransform: &datadogV2.DataTransform{
							Type: datadogV2.DATATRANSFORMTYPE_DATATRANSFORM,
							Name: "randomFact",
							Properties: datadogV2.DataTransformProperties{
								Outputs: datadog.PtrString(`${(() => {const facts = fetchFacts.outputs.body.data
return facts[Math.floor(Math.random()*facts.length)]
})()}`),
							},
							Id: uuid.MustParse("0fb22859-47dc-4137-9e41-7b67d04c525c"),
						}},
				},
				Name:        datadog.PtrString("Example Cat Facts Viewer"),
				Description: datadog.PtrString("This is a slightly complicated example app that fetches and displays cat facts"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.CreateApp(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.CreateApp`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.CreateApp`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create App returns "Created" response
```
// Create App returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.ActionQuery;
import com.datadog.api.client.v2.model.ActionQueryProperties;
import com.datadog.api.client.v2.model.ActionQuerySpec;
import com.datadog.api.client.v2.model.ActionQuerySpecInputs;
import com.datadog.api.client.v2.model.ActionQuerySpecObject;
import com.datadog.api.client.v2.model.ActionQueryType;
import com.datadog.api.client.v2.model.AppBuilderEvent;
import com.datadog.api.client.v2.model.AppBuilderEventName;
import com.datadog.api.client.v2.model.AppBuilderEventType;
import com.datadog.api.client.v2.model.AppDefinitionType;
import com.datadog.api.client.v2.model.Component;
import com.datadog.api.client.v2.model.ComponentGrid;
import com.datadog.api.client.v2.model.ComponentGridProperties;
import com.datadog.api.client.v2.model.ComponentGridType;
import com.datadog.api.client.v2.model.ComponentProperties;
import com.datadog.api.client.v2.model.ComponentPropertiesIsVisible;
import com.datadog.api.client.v2.model.ComponentType;
import com.datadog.api.client.v2.model.CreateAppRequest;
import com.datadog.api.client.v2.model.CreateAppRequestData;
import com.datadog.api.client.v2.model.CreateAppRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateAppResponse;
import com.datadog.api.client.v2.model.DataTransform;
import com.datadog.api.client.v2.model.DataTransformProperties;
import com.datadog.api.client.v2.model.DataTransformType;
import com.datadog.api.client.v2.model.Query;
import com.datadog.api.client.v2.model.StateVariable;
import com.datadog.api.client.v2.model.StateVariableProperties;
import com.datadog.api.client.v2.model.StateVariableType;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    CreateAppRequest body =
        new CreateAppRequest()
            .data(
                new CreateAppRequestData()
                    .type(AppDefinitionType.APPDEFINITIONS)
                    .attributes(
                        new CreateAppRequestDataAttributes()
                            .rootInstanceName("grid0")
                            .components(
                                Collections.singletonList(
                                    new ComponentGrid()
                                        .name("grid0")
                                        .type(ComponentGridType.GRID)
                                        .properties(
                                            new ComponentGridProperties()
                                                .children(
                                                    Arrays.asList(
                                                        new Component()
                                                            .type(ComponentType.GRIDCELL)
                                                            .name("gridCell0")
                                                            .properties(
                                                                new ComponentProperties()
                                                                    .children(
                                                                        Collections.singletonList(
                                                                            new Component()
                                                                                .name("text0")
                                                                                .type(
                                                                                    ComponentType
                                                                                        .TEXT)
                                                                                .properties(
                                                                                    new ComponentProperties()
                                                                                        .isVisible(
                                                                                            new ComponentPropertiesIsVisible(
                                                                                                true)))))
                                                                    .isVisible(
                                                                        new ComponentPropertiesIsVisible(
                                                                            "true"))),
                                                        new Component()
                                                            .type(ComponentType.GRIDCELL)
                                                            .name("gridCell2")
                                                            .properties(
                                                                new ComponentProperties()
                                                                    .children(
                                                                        Collections.singletonList(
                                                                            new Component()
                                                                                .name("table0")
                                                                                .type(
                                                                                    ComponentType
                                                                                        .TABLE)
                                                                                .properties(
                                                                                    new ComponentProperties()
                                                                                        .isVisible(
                                                                                            new ComponentPropertiesIsVisible(
                                                                                                true)))))
                                                                    .isVisible(
                                                                        new ComponentPropertiesIsVisible(
                                                                            "true"))),
                                                        new Component()
                                                            .type(ComponentType.GRIDCELL)
                                                            .name("gridCell1")
                                                            .properties(
                                                                new ComponentProperties()
                                                                    .children(
                                                                        Collections.singletonList(
                                                                            new Component()
                                                                                .name("text1")
                                                                                .type(
                                                                                    ComponentType
                                                                                        .TEXT)
                                                                                .properties(
                                                                                    new ComponentProperties()
                                                                                        .isVisible(
                                                                                            new ComponentPropertiesIsVisible(
                                                                                                true)))))
                                                                    .isVisible(
                                                                        new ComponentPropertiesIsVisible(
                                                                            "true"))),
                                                        new Component()
                                                            .type(ComponentType.GRIDCELL)
                                                            .name("gridCell3")
                                                            .properties(
                                                                new ComponentProperties()
                                                                    .children(
                                                                        Collections.singletonList(
                                                                            new Component()
                                                                                .name("button0")
                                                                                .type(
                                                                                    ComponentType
                                                                                        .BUTTON)
                                                                                .properties(
                                                                                    new ComponentProperties()
                                                                                        .isVisible(
                                                                                            new ComponentPropertiesIsVisible(
                                                                                                true)))
                                                                                .events(
                                                                                    Collections
                                                                                        .singletonList(
                                                                                            new AppBuilderEvent()
                                                                                                .name(
                                                                                                    AppBuilderEventName
                                                                                                        .CLICK)
                                                                                                .type(
                                                                                                    AppBuilderEventType
                                                                                                        .SETSTATEVARIABLEVALUE)))))
                                                                    .isVisible(
                                                                        new ComponentPropertiesIsVisible(
                                                                            "true"))),
                                                        new Component()
                                                            .type(ComponentType.GRIDCELL)
                                                            .name("gridCell4")
                                                            .properties(
                                                                new ComponentProperties()
                                                                    .children(
                                                                        Collections.singletonList(
                                                                            new Component()
                                                                                .name("button1")
                                                                                .type(
                                                                                    ComponentType
                                                                                        .BUTTON)
                                                                                .properties(
                                                                                    new ComponentProperties()
                                                                                        .isVisible(
                                                                                            new ComponentPropertiesIsVisible(
                                                                                                true)))
                                                                                .events(
                                                                                    Collections
                                                                                        .singletonList(
                                                                                            new AppBuilderEvent()
                                                                                                .name(
                                                                                                    AppBuilderEventName
                                                                                                        .CLICK)
                                                                                                .type(
                                                                                                    AppBuilderEventType
                                                                                                        .SETSTATEVARIABLEVALUE)))))
                                                                    .isVisible(
                                                                        new ComponentPropertiesIsVisible(
                                                                            "true")))))
                                                .backgroundColor("default"))))
                            .queries(
                                Arrays.asList(
                                    new Query(
                                        new ActionQuery()
                                            .id(
                                                UUID.fromString(
                                                    "92ff0bb8-553b-4f31-87c7-ef5bd16d47d5"))
                                            .type(ActionQueryType.ACTION)
                                            .name("fetchFacts")
                                            .properties(
                                                new ActionQueryProperties()
                                                    .spec(
                                                        new ActionQuerySpec(
                                                            new ActionQuerySpecObject()
                                                                .fqn("com.datadoghq.http.request")
                                                                .connectionId(
                                                                    "5e63f4a8-4ce6-47de-ba11-f6617c1d54f3")
                                                                .inputs(
                                                                    new ActionQuerySpecInputs(
                                                                        Map.ofEntries(
                                                                            Map.entry(
                                                                                "verb", "GET"),
                                                                            Map.entry(
                                                                                "url",
                                                                                "https://catfact.ninja/facts"),
                                                                            Map.entry(
                                                                                "urlParams",
                                                                                "[{'key': 'limit',"
                                                                                    + " 'value':"
                                                                                    + " '${pageSize.value.toString()}'},"
                                                                                    + " {'key':"
                                                                                    + " 'page',"
                                                                                    + " 'value':"
                                                                                    + " '${(table0.pageIndex"
                                                                                    + " + 1).toString()}'}]")))))))),
                                    new Query(
                                        new StateVariable()
                                            .type(StateVariableType.STATEVARIABLE)
                                            .name("pageSize")
                                            .properties(
                                                new StateVariableProperties().defaultValue("${20}"))
                                            .id(
                                                UUID.fromString(
                                                    "afd03c81-4075-4432-8618-ba09d52d2f2d"))),
                                    new Query(
                                        new DataTransform()
                                            .type(DataTransformType.DATATRANSFORM)
                                            .name("randomFact")
                                            .properties(
                                                new DataTransformProperties()
                                                    .outputs(
                                                        """
${(() => {const facts = fetchFacts.outputs.body.data
return facts[Math.floor(Math.random()*facts.length)]
})()}
"""))
                                            .id(
                                                UUID.fromString(
                                                    "0fb22859-47dc-4137-9e41-7b67d04c525c")))))
                            .name("Example Cat Facts Viewer")
                            .description(
                                "This is a slightly complicated example app that fetches and"
                                    + " displays cat facts")));

    try {
      CreateAppResponse result = apiInstance.createApp(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#createApp");
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

#####  Create App returns "Created" response
```
"""
Create App returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.action_query import ActionQuery
from datadog_api_client.v2.model.action_query_properties import ActionQueryProperties
from datadog_api_client.v2.model.action_query_spec_input import ActionQuerySpecInput
from datadog_api_client.v2.model.action_query_spec_object import ActionQuerySpecObject
from datadog_api_client.v2.model.action_query_type import ActionQueryType
from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
from datadog_api_client.v2.model.app_builder_event_name import AppBuilderEventName
from datadog_api_client.v2.model.app_builder_event_type import AppBuilderEventType
from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
from datadog_api_client.v2.model.component import Component
from datadog_api_client.v2.model.component_grid import ComponentGrid
from datadog_api_client.v2.model.component_grid_properties import ComponentGridProperties
from datadog_api_client.v2.model.component_grid_type import ComponentGridType
from datadog_api_client.v2.model.component_properties import ComponentProperties
from datadog_api_client.v2.model.component_type import ComponentType
from datadog_api_client.v2.model.create_app_request import CreateAppRequest
from datadog_api_client.v2.model.create_app_request_data import CreateAppRequestData
from datadog_api_client.v2.model.create_app_request_data_attributes import CreateAppRequestDataAttributes
from datadog_api_client.v2.model.data_transform import DataTransform
from datadog_api_client.v2.model.data_transform_properties import DataTransformProperties
from datadog_api_client.v2.model.data_transform_type import DataTransformType
from datadog_api_client.v2.model.state_variable import StateVariable
from datadog_api_client.v2.model.state_variable_properties import StateVariableProperties
from datadog_api_client.v2.model.state_variable_type import StateVariableType
from uuid import UUID

body = CreateAppRequest(
    data=CreateAppRequestData(
        type=AppDefinitionType.APPDEFINITIONS,
        attributes=CreateAppRequestDataAttributes(
            root_instance_name="grid0",
            components=[
                ComponentGrid(
                    name="grid0",
                    type=ComponentGridType.GRID,
                    properties=ComponentGridProperties(
                        children=[
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell0",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="text0",
                                            type=ComponentType.TEXT,
                                            properties=ComponentProperties(
                                                content="# Cat Facts",
                                                content_type="markdown",
                                                text_align="left",
                                                vertical_align="top",
                                                is_visible=True,
                                            ),
                                            events=[],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 0, 'y': 0, 'width': 4, 'height': 5}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell2",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="table0",
                                            type=ComponentType.TABLE,
                                            properties=ComponentProperties(
                                                data="${fetchFacts?.outputs?.body?.data}",
                                                columns=[
                                                    dict(
                                                        [
                                                            ("dataPath", "fact"),
                                                            ("header", "fact"),
                                                            ("isHidden", "False"),
                                                            ("id", "0ae2ae9e-0280-4389-83c6-1c5949f7e674"),
                                                        ]
                                                    ),
                                                    dict(
                                                        [
                                                            ("dataPath", "length"),
                                                            ("header", "length"),
                                                            ("isHidden", "True"),
                                                            ("id", "c9048611-0196-4a00-9366-1ef9e3ec0408"),
                                                        ]
                                                    ),
                                                    dict(
                                                        [
                                                            ("id", "8fa9284b-7a58-4f13-9959-57b7d8a7fe8f"),
                                                            ("dataPath", "Due Date"),
                                                            ("header", "Unused Old Column"),
                                                            ("disableSortBy", "False"),
                                                            (
                                                                "formatter",
                                                                "{'type': 'formatted_time', 'format': 'LARGE_WITHOUT_TIME'}",
                                                            ),
                                                            ("isDeleted", "True"),
                                                        ]
                                                    ),
                                                ],
                                                summary=True,
                                                page_size="${pageSize?.value}",
                                                pagination_type="server_side",
                                                is_loading="${fetchFacts?.isLoading}",
                                                row_buttons=[],
                                                is_wrappable=False,
                                                is_scrollable="vertical",
                                                is_sub_rows_enabled=False,
                                                global_filter=False,
                                                is_visible=True,
                                                total_count="${fetchFacts?.outputs?.body?.total}",
                                            ),
                                            events=[],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 0, 'y': 5, 'width': 12, 'height': 96}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell1",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="text1",
                                            type=ComponentType.TEXT,
                                            properties=ComponentProperties(
                                                content="## Random Fact\n\n${randomFact?.outputs?.fact}",
                                                content_type="markdown",
                                                text_align="left",
                                                vertical_align="top",
                                                is_visible=True,
                                            ),
                                            events=[],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 0, 'y': 101, 'width': 12, 'height': 16}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell3",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="button0",
                                            type=ComponentType.BUTTON,
                                            properties=ComponentProperties(
                                                label="Increase Page Size",
                                                level="default",
                                                is_primary=True,
                                                is_borderless=False,
                                                is_loading=False,
                                                is_disabled=False,
                                                is_visible=True,
                                                icon_left="angleUp",
                                                icon_right="",
                                            ),
                                            events=[
                                                AppBuilderEvent(
                                                    variable_name="pageSize",
                                                    value="${pageSize?.value + 1}",
                                                    name=AppBuilderEventName.CLICK,
                                                    type=AppBuilderEventType.SETSTATEVARIABLEVALUE,
                                                ),
                                            ],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 10, 'y': 134, 'width': 2, 'height': 4}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell4",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="button1",
                                            type=ComponentType.BUTTON,
                                            properties=ComponentProperties(
                                                label="Decrease Page Size",
                                                level="default",
                                                is_primary=True,
                                                is_borderless=False,
                                                is_loading=False,
                                                is_disabled=False,
                                                is_visible=True,
                                                icon_left="angleDown",
                                                icon_right="",
                                            ),
                                            events=[
                                                AppBuilderEvent(
                                                    variable_name="pageSize",
                                                    value="${pageSize?.value - 1}",
                                                    name=AppBuilderEventName.CLICK,
                                                    type=AppBuilderEventType.SETSTATEVARIABLEVALUE,
                                                ),
                                            ],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 10, 'y': 138, 'width': 2, 'height': 4}")]),
                                ),
                                events=[],
                            ),
                        ],
                        background_color="default",
                    ),
                    events=[],
                ),
            ],
            queries=[
                ActionQuery(
                    id=UUID("92ff0bb8-553b-4f31-87c7-ef5bd16d47d5"),
                    type=ActionQueryType.ACTION,
                    name="fetchFacts",
                    events=[],
                    properties=ActionQueryProperties(
                        spec=ActionQuerySpecObject(
                            fqn="com.datadoghq.http.request",
                            connection_id="5e63f4a8-4ce6-47de-ba11-f6617c1d54f3",
                            inputs=ActionQuerySpecInput(
                                [
                                    ("verb", "GET"),
                                    ("url", "https://catfact.ninja/facts"),
                                    (
                                        "urlParams",
                                        "[{'key': 'limit', 'value': '${pageSize.value.toString()}'}, {'key': 'page', 'value': '${(table0.pageIndex + 1).toString()}'}]",
                                    ),
                                ]
                            ),
                        ),
                    ),
                ),
                StateVariable(
                    type=StateVariableType.STATEVARIABLE,
                    name="pageSize",
                    properties=StateVariableProperties(
                        default_value="${20}",
                    ),
                    id=UUID("afd03c81-4075-4432-8618-ba09d52d2f2d"),
                ),
                DataTransform(
                    type=DataTransformType.DATATRANSFORM,
                    name="randomFact",
                    properties=DataTransformProperties(
                        outputs="${(() => {const facts = fetchFacts.outputs.body.data\nreturn facts[Math.floor(Math.random()*facts.length)]\n})()}",
                    ),
                    id=UUID("0fb22859-47dc-4137-9e41-7b67d04c525c"),
                ),
            ],
            name="Example Cat Facts Viewer",
            description="This is a slightly complicated example app that fetches and displays cat facts",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.create_app(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create App returns "Created" response
```
# Create App returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new

body = DatadogAPIClient::V2::CreateAppRequest.new({
  data: DatadogAPIClient::V2::CreateAppRequestData.new({
    type: DatadogAPIClient::V2::AppDefinitionType::APPDEFINITIONS,
    attributes: DatadogAPIClient::V2::CreateAppRequestDataAttributes.new({
      root_instance_name: "grid0",
      components: [
        DatadogAPIClient::V2::ComponentGrid.new({
          name: "grid0",
          type: DatadogAPIClient::V2::ComponentGridType::GRID,
          properties: DatadogAPIClient::V2::ComponentGridProperties.new({
            children: [
              DatadogAPIClient::V2::Component.new({
                type: DatadogAPIClient::V2::ComponentType::GRIDCELL,
                name: "gridCell0",
                properties: DatadogAPIClient::V2::ComponentProperties.new({
                  children: [
                    DatadogAPIClient::V2::Component.new({
                      name: "text0",
                      type: DatadogAPIClient::V2::ComponentType::TEXT,
                      properties: DatadogAPIClient::V2::ComponentProperties.new({
                        is_visible: true,
                      }),
                      events: [],
                    }),
                  ],
                  is_visible: "true",
                }),
                events: [],
              }),
              DatadogAPIClient::V2::Component.new({
                type: DatadogAPIClient::V2::ComponentType::GRIDCELL,
                name: "gridCell2",
                properties: DatadogAPIClient::V2::ComponentProperties.new({
                  children: [
                    DatadogAPIClient::V2::Component.new({
                      name: "table0",
                      type: DatadogAPIClient::V2::ComponentType::TABLE,
                      properties: DatadogAPIClient::V2::ComponentProperties.new({
                        is_visible: true,
                      }),
                      events: [],
                    }),
                  ],
                  is_visible: "true",
                }),
                events: [],
              }),
              DatadogAPIClient::V2::Component.new({
                type: DatadogAPIClient::V2::ComponentType::GRIDCELL,
                name: "gridCell1",
                properties: DatadogAPIClient::V2::ComponentProperties.new({
                  children: [
                    DatadogAPIClient::V2::Component.new({
                      name: "text1",
                      type: DatadogAPIClient::V2::ComponentType::TEXT,
                      properties: DatadogAPIClient::V2::ComponentProperties.new({
                        is_visible: true,
                      }),
                      events: [],
                    }),
                  ],
                  is_visible: "true",
                }),
                events: [],
              }),
              DatadogAPIClient::V2::Component.new({
                type: DatadogAPIClient::V2::ComponentType::GRIDCELL,
                name: "gridCell3",
                properties: DatadogAPIClient::V2::ComponentProperties.new({
                  children: [
                    DatadogAPIClient::V2::Component.new({
                      name: "button0",
                      type: DatadogAPIClient::V2::ComponentType::BUTTON,
                      properties: DatadogAPIClient::V2::ComponentProperties.new({
                        is_visible: true,
                      }),
                      events: [
                        DatadogAPIClient::V2::AppBuilderEvent.new({
                          name: DatadogAPIClient::V2::AppBuilderEventName::CLICK,
                          type: DatadogAPIClient::V2::AppBuilderEventType::SETSTATEVARIABLEVALUE,
                        }),
                      ],
                    }),
                  ],
                  is_visible: "true",
                }),
                events: [],
              }),
              DatadogAPIClient::V2::Component.new({
                type: DatadogAPIClient::V2::ComponentType::GRIDCELL,
                name: "gridCell4",
                properties: DatadogAPIClient::V2::ComponentProperties.new({
                  children: [
                    DatadogAPIClient::V2::Component.new({
                      name: "button1",
                      type: DatadogAPIClient::V2::ComponentType::BUTTON,
                      properties: DatadogAPIClient::V2::ComponentProperties.new({
                        is_visible: true,
                      }),
                      events: [
                        DatadogAPIClient::V2::AppBuilderEvent.new({
                          name: DatadogAPIClient::V2::AppBuilderEventName::CLICK,
                          type: DatadogAPIClient::V2::AppBuilderEventType::SETSTATEVARIABLEVALUE,
                        }),
                      ],
                    }),
                  ],
                  is_visible: "true",
                }),
                events: [],
              }),
            ],
            background_color: "default",
          }),
          events: [],
        }),
      ],
      queries: [
        DatadogAPIClient::V2::ActionQuery.new({
          id: "92ff0bb8-553b-4f31-87c7-ef5bd16d47d5",
          type: DatadogAPIClient::V2::ActionQueryType::ACTION,
          name: "fetchFacts",
          events: [],
          properties: DatadogAPIClient::V2::ActionQueryProperties.new({
            spec: {
              "fqn": "com.datadoghq.http.request", "connectionId": "5e63f4a8-4ce6-47de-ba11-f6617c1d54f3", "inputs": "{'verb': 'GET', 'url': 'https://catfact.ninja/facts', 'urlParams': [{'key': 'limit', 'value': '${pageSize.value.toString()}'}, {'key': 'page', 'value': '${(table0.pageIndex + 1).toString()}'}]}",
            },
          }),
        }),
        DatadogAPIClient::V2::StateVariable.new({
          type: DatadogAPIClient::V2::StateVariableType::STATEVARIABLE,
          name: "pageSize",
          properties: DatadogAPIClient::V2::StateVariableProperties.new({
            default_value: "${20}",
          }),
          id: "afd03c81-4075-4432-8618-ba09d52d2f2d",
        }),
        DatadogAPIClient::V2::DataTransform.new({
          type: DatadogAPIClient::V2::DataTransformType::DATATRANSFORM,
          name: "randomFact",
          properties: DatadogAPIClient::V2::DataTransformProperties.new({
            outputs: '${(() => {const facts = fetchFacts.outputs.body.data\nreturn facts[Math.floor(Math.random()*facts.length)]\n})()}',
          }),
          id: "0fb22859-47dc-4137-9e41-7b67d04c525c",
        }),
      ],
      name: "Example Cat Facts Viewer",
      description: "This is a slightly complicated example app that fetches and displays cat facts",
    }),
  }),
})
p api_instance.create_app(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create App returns "Created" response
```
// Create App returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;
use datadog_api_client::datadogV2::model::ActionQuery;
use datadog_api_client::datadogV2::model::ActionQueryProperties;
use datadog_api_client::datadogV2::model::ActionQuerySpec;
use datadog_api_client::datadogV2::model::ActionQuerySpecInputs;
use datadog_api_client::datadogV2::model::ActionQuerySpecObject;
use datadog_api_client::datadogV2::model::ActionQueryType;
use datadog_api_client::datadogV2::model::AppBuilderEvent;
use datadog_api_client::datadogV2::model::AppBuilderEventName;
use datadog_api_client::datadogV2::model::AppBuilderEventType;
use datadog_api_client::datadogV2::model::AppDefinitionType;
use datadog_api_client::datadogV2::model::Component;
use datadog_api_client::datadogV2::model::ComponentGrid;
use datadog_api_client::datadogV2::model::ComponentGridProperties;
use datadog_api_client::datadogV2::model::ComponentGridType;
use datadog_api_client::datadogV2::model::ComponentProperties;
use datadog_api_client::datadogV2::model::ComponentPropertiesIsVisible;
use datadog_api_client::datadogV2::model::ComponentType;
use datadog_api_client::datadogV2::model::CreateAppRequest;
use datadog_api_client::datadogV2::model::CreateAppRequestData;
use datadog_api_client::datadogV2::model::CreateAppRequestDataAttributes;
use datadog_api_client::datadogV2::model::DataTransform;
use datadog_api_client::datadogV2::model::DataTransformProperties;
use datadog_api_client::datadogV2::model::DataTransformType;
use datadog_api_client::datadogV2::model::Query;
use datadog_api_client::datadogV2::model::StateVariable;
use datadog_api_client::datadogV2::model::StateVariableProperties;
use datadog_api_client::datadogV2::model::StateVariableType;
use serde_json::Value;
use std::collections::BTreeMap;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let body =
        CreateAppRequest
        ::new().data(
            CreateAppRequestData::new(
                AppDefinitionType::APPDEFINITIONS,
            ).attributes(
                CreateAppRequestDataAttributes::new()
                    .components(
                        vec![
                            ComponentGrid::new(
                                "grid0".to_string(),
                                ComponentGridProperties::new()
                                    .background_color("default".to_string())
                                    .children(
                                        vec![
                                            Component::new(
                                                "gridCell0".to_string(),
                                                ComponentProperties::new()
                                                    .children(
                                                        vec![
                                                            Component::new(
                                                                "text0".to_string(),
                                                                ComponentProperties
                                                                ::new().is_visible(
                                                                    ComponentPropertiesIsVisible::Bool(true),
                                                                ),
                                                                ComponentType::TEXT,
                                                            ).events(vec![])
                                                        ],
                                                    )
                                                    .is_visible(
                                                        ComponentPropertiesIsVisible::String("true".to_string()),
                                                    ),
                                                ComponentType::GRIDCELL,
                                            ).events(vec![]),
                                            Component::new(
                                                "gridCell2".to_string(),
                                                ComponentProperties::new()
                                                    .children(
                                                        vec![
                                                            Component::new(
                                                                "table0".to_string(),
                                                                ComponentProperties
                                                                ::new().is_visible(
                                                                    ComponentPropertiesIsVisible::Bool(true),
                                                                ),
                                                                ComponentType::TABLE,
                                                            ).events(vec![])
                                                        ],
                                                    )
                                                    .is_visible(
                                                        ComponentPropertiesIsVisible::String("true".to_string()),
                                                    ),
                                                ComponentType::GRIDCELL,
                                            ).events(vec![]),
                                            Component::new(
                                                "gridCell1".to_string(),
                                                ComponentProperties::new()
                                                    .children(
                                                        vec![
                                                            Component::new(
                                                                "text1".to_string(),
                                                                ComponentProperties
                                                                ::new().is_visible(
                                                                    ComponentPropertiesIsVisible::Bool(true),
                                                                ),
                                                                ComponentType::TEXT,
                                                            ).events(vec![])
                                                        ],
                                                    )
                                                    .is_visible(
                                                        ComponentPropertiesIsVisible::String("true".to_string()),
                                                    ),
                                                ComponentType::GRIDCELL,
                                            ).events(vec![]),
                                            Component::new(
                                                "gridCell3".to_string(),
                                                ComponentProperties::new()
                                                    .children(
                                                        vec![
                                                            Component::new(
                                                                "button0".to_string(),
                                                                ComponentProperties
                                                                ::new().is_visible(
                                                                    ComponentPropertiesIsVisible::Bool(true),
                                                                ),
                                                                ComponentType::BUTTON,
                                                            ).events(
                                                                vec![
                                                                    AppBuilderEvent::new()
                                                                        .name(AppBuilderEventName::CLICK)
                                                                        .type_(
                                                                            AppBuilderEventType::SETSTATEVARIABLEVALUE,
                                                                        )
                                                                ],
                                                            )
                                                        ],
                                                    )
                                                    .is_visible(
                                                        ComponentPropertiesIsVisible::String("true".to_string()),
                                                    ),
                                                ComponentType::GRIDCELL,
                                            ).events(vec![]),
                                            Component::new(
                                                "gridCell4".to_string(),
                                                ComponentProperties::new()
                                                    .children(
                                                        vec![
                                                            Component::new(
                                                                "button1".to_string(),
                                                                ComponentProperties
                                                                ::new().is_visible(
                                                                    ComponentPropertiesIsVisible::Bool(true),
                                                                ),
                                                                ComponentType::BUTTON,
                                                            ).events(
                                                                vec![
                                                                    AppBuilderEvent::new()
                                                                        .name(AppBuilderEventName::CLICK)
                                                                        .type_(
                                                                            AppBuilderEventType::SETSTATEVARIABLEVALUE,
                                                                        )
                                                                ],
                                                            )
                                                        ],
                                                    )
                                                    .is_visible(
                                                        ComponentPropertiesIsVisible::String("true".to_string()),
                                                    ),
                                                ComponentType::GRIDCELL,
                                            ).events(vec![])
                                        ],
                                    ),
                                ComponentGridType::GRID,
                            ).events(vec![])
                        ],
                    )
                    .description(
                        "This is a slightly complicated example app that fetches and displays cat facts".to_string(),
                    )
                    .name("Example Cat Facts Viewer".to_string())
                    .queries(
                        vec![
                            Query::ActionQuery(
                                Box::new(
                                    ActionQuery::new(
                                        Uuid::parse_str(
                                            "92ff0bb8-553b-4f31-87c7-ef5bd16d47d5",
                                        ).expect("invalid UUID"),
                                        "fetchFacts".to_string(),
                                        ActionQueryProperties::new(
                                            ActionQuerySpec::ActionQuerySpecObject(
                                                Box::new(
                                                    ActionQuerySpecObject::new(
                                                        "com.datadoghq.http.request".to_string(),
                                                    )
                                                        .connection_id(
                                                            "5e63f4a8-4ce6-47de-ba11-f6617c1d54f3".to_string(),
                                                        )
                                                        .inputs(
                                                            ActionQuerySpecInputs::ActionQuerySpecInput(
                                                                BTreeMap::from(
                                                                    [
                                                                        ("verb".to_string(), Value::from("GET")),
                                                                        (
                                                                            "url".to_string(),
                                                                            Value::from(
                                                                                "https://catfact.ninja/facts",
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ),
                                                ),
                                            ),
                                        ),
                                        ActionQueryType::ACTION,
                                    ).events(vec![]),
                                ),
                            ),
                            Query::StateVariable(
                                Box::new(
                                    StateVariable::new(
                                        Uuid::parse_str(
                                            "afd03c81-4075-4432-8618-ba09d52d2f2d",
                                        ).expect("invalid UUID"),
                                        "pageSize".to_string(),
                                        StateVariableProperties::new().default_value(Value::from("${20}")),
                                        StateVariableType::STATEVARIABLE,
                                    ),
                                ),
                            ),
                            Query::DataTransform(
                                Box::new(
                                    DataTransform::new(
                                        Uuid::parse_str(
                                            "0fb22859-47dc-4137-9e41-7b67d04c525c",
                                        ).expect("invalid UUID"),
                                        "randomFact".to_string(),
                                        DataTransformProperties
                                        ::new().outputs(
                                            r#"${(() => {const facts = fetchFacts.outputs.body.data
return facts[Math.floor(Math.random()*facts.length)]
})()}"#.to_string(),
                                        ),
                                        DataTransformType::DATATRANSFORM,
                                    ),
                                ),
                            )
                        ],
                    )
                    .root_instance_name("grid0".to_string()),
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api.create_app(body).await;
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

#####  Create App returns "Created" response
```
/**
 * Create App returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

const params: v2.AppBuilderApiCreateAppRequest = {
  body: {
    data: {
      type: "appDefinitions",
      attributes: {
        rootInstanceName: "grid0",
        components: [
          {
            name: "grid0",
            type: "grid",
            properties: {
              children: [
                {
                  type: "gridCell",
                  name: "gridCell0",
                  properties: {
                    children: [
                      {
                        name: "text0",
                        type: "text",
                        properties: {
                          isVisible: true,
                        },
                        events: [],
                      },
                    ],
                    isVisible: "true",
                  },
                  events: [],
                },
                {
                  type: "gridCell",
                  name: "gridCell2",
                  properties: {
                    children: [
                      {
                        name: "table0",
                        type: "table",
                        properties: {
                          isVisible: true,
                        },
                        events: [],
                      },
                    ],
                    isVisible: "true",
                  },
                  events: [],
                },
                {
                  type: "gridCell",
                  name: "gridCell1",
                  properties: {
                    children: [
                      {
                        name: "text1",
                        type: "text",
                        properties: {
                          isVisible: true,
                        },
                        events: [],
                      },
                    ],
                    isVisible: "true",
                  },
                  events: [],
                },
                {
                  type: "gridCell",
                  name: "gridCell3",
                  properties: {
                    children: [
                      {
                        name: "button0",
                        type: "button",
                        properties: {
                          isVisible: true,
                        },
                        events: [
                          {
                            name: "click",
                            type: "setStateVariableValue",
                          },
                        ],
                      },
                    ],
                    isVisible: "true",
                  },
                  events: [],
                },
                {
                  type: "gridCell",
                  name: "gridCell4",
                  properties: {
                    children: [
                      {
                        name: "button1",
                        type: "button",
                        properties: {
                          isVisible: true,
                        },
                        events: [
                          {
                            name: "click",
                            type: "setStateVariableValue",
                          },
                        ],
                      },
                    ],
                    isVisible: "true",
                  },
                  events: [],
                },
              ],
              backgroundColor: "default",
            },
            events: [],
          },
        ],
        queries: [
          {
            id: "92ff0bb8-553b-4f31-87c7-ef5bd16d47d5",
            type: "action",
            name: "fetchFacts",
            events: [],
            properties: {
              spec: {
                fqn: "com.datadoghq.http.request",
                connectionId: "5e63f4a8-4ce6-47de-ba11-f6617c1d54f3",
                inputs: {
                  verb: "GET",
                  url: "https://catfact.ninja/facts",
                  urlParams:
                    "[{'key': 'limit', 'value': '${pageSize.value.toString()}'}, {'key': 'page', 'value': '${(table0.pageIndex + 1).toString()}'}]",
                },
              },
            },
          },
          {
            type: "stateVariable",
            name: "pageSize",
            properties: {
              defaultValue: "${20}",
            },
            id: "afd03c81-4075-4432-8618-ba09d52d2f2d",
          },
          {
            type: "dataTransform",
            name: "randomFact",
            properties: {
              outputs:
                "${(() => {const facts = fetchFacts.outputs.body.data\nreturn facts[Math.floor(Math.random()*facts.length)]\n})()}",
            },
            id: "0fb22859-47dc-4137-9e41-7b67d04c525c",
          },
        ],
        name: "Example Cat Facts Viewer",
        description:
          "This is a slightly complicated example app that fetches and displays cat facts",
      },
    },
  },
};

apiInstance
  .createApp(params)
  .then((data: v2.CreateAppResponse) => {
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
## [Delete Multiple Apps](https://docs.datadoghq.com/api/latest/app-builder/#delete-multiple-apps)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#delete-multiple-apps-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/app-builder/appshttps://api.ap2.datadoghq.com/api/v2/app-builder/appshttps://api.datadoghq.eu/api/v2/app-builder/appshttps://api.ddog-gov.com/api/v2/app-builder/appshttps://api.datadoghq.com/api/v2/app-builder/appshttps://api.us3.datadoghq.com/api/v2/app-builder/appshttps://api.us5.datadoghq.com/api/v2/app-builder/apps
### Overview
Delete multiple apps in a single request from a list of app IDs. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `apps_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


Field
Type
Description
data
[object]
An array of objects containing the IDs of the apps to delete.
id [_required_]
uuid
The ID of the app to delete.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
```
{
  "data": [
    {
      "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
      "type": "appDefinitions"
    }
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApps-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApps-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApps-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApps-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApps-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


The response object after multiple apps are successfully deleted.
Field
Type
Description
data
[object]
An array of objects containing the IDs of the deleted apps.
id [_required_]
uuid
The ID of the deleted app.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
```
{
  "data": [
    {
      "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
      "type": "appDefinitions"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  Delete Multiple Apps returns "OK" response
Copy
```
                          # Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
      "type": "appDefinitions"
    }
  ]
}
EOF  

                        
```

#####  Delete Multiple Apps returns "OK" response
```
// Delete Multiple Apps returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "app" in the system
	AppDataID := uuid.MustParse(os.Getenv("APP_DATA_ID"))

	body := datadogV2.DeleteAppsRequest{
		Data: []datadogV2.DeleteAppsRequestDataItems{
			{
				Id:   AppDataID,
				Type: datadogV2.APPDEFINITIONTYPE_APPDEFINITIONS,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.DeleteApps(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.DeleteApps`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.DeleteApps`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete Multiple Apps returns "OK" response
```
// Delete Multiple Apps returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.AppDefinitionType;
import com.datadog.api.client.v2.model.DeleteAppsRequest;
import com.datadog.api.client.v2.model.DeleteAppsRequestDataItems;
import com.datadog.api.client.v2.model.DeleteAppsResponse;
import java.util.Collections;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    // there is a valid "app" in the system
    UUID APP_DATA_ID = null;
    try {
      APP_DATA_ID = UUID.fromString(System.getenv("APP_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    DeleteAppsRequest body =
        new DeleteAppsRequest()
            .data(
                Collections.singletonList(
                    new DeleteAppsRequestDataItems()
                        .id(APP_DATA_ID)
                        .type(AppDefinitionType.APPDEFINITIONS)));

    try {
      DeleteAppsResponse result = apiInstance.deleteApps(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#deleteApps");
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

#####  Delete Multiple Apps returns "OK" response
```
"""
Delete Multiple Apps returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
from datadog_api_client.v2.model.delete_apps_request import DeleteAppsRequest
from datadog_api_client.v2.model.delete_apps_request_data_items import DeleteAppsRequestDataItems

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

body = DeleteAppsRequest(
    data=[
        DeleteAppsRequestDataItems(
            id=APP_DATA_ID,
            type=AppDefinitionType.APPDEFINITIONS,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.delete_apps(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete Multiple Apps returns "OK" response
```
# Delete Multiple Apps returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new

# there is a valid "app" in the system
APP_DATA_ID = ENV["APP_DATA_ID"]

body = DatadogAPIClient::V2::DeleteAppsRequest.new({
  data: [
    DatadogAPIClient::V2::DeleteAppsRequestDataItems.new({
      id: APP_DATA_ID,
      type: DatadogAPIClient::V2::AppDefinitionType::APPDEFINITIONS,
    }),
  ],
})
p api_instance.delete_apps(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete Multiple Apps returns "OK" response
```
// Delete Multiple Apps returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;
use datadog_api_client::datadogV2::model::AppDefinitionType;
use datadog_api_client::datadogV2::model::DeleteAppsRequest;
use datadog_api_client::datadogV2::model::DeleteAppsRequestDataItems;

#[tokio::main]
async fn main() {
    // there is a valid "app" in the system
    let app_data_id =
        uuid::Uuid::parse_str(&std::env::var("APP_DATA_ID").unwrap()).expect("Invalid UUID");
    let body = DeleteAppsRequest::new().data(vec![DeleteAppsRequestDataItems::new(
        app_data_id.clone(),
        AppDefinitionType::APPDEFINITIONS,
    )]);
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api.delete_apps(body).await;
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

#####  Delete Multiple Apps returns "OK" response
```
/**
 * Delete Multiple Apps returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

// there is a valid "app" in the system
const APP_DATA_ID = process.env.APP_DATA_ID as string;

const params: v2.AppBuilderApiDeleteAppsRequest = {
  body: {
    data: [
      {
        id: APP_DATA_ID,
        type: "appDefinitions",
      },
    ],
  },
};

apiInstance
  .deleteApps(params)
  .then((data: v2.DeleteAppsResponse) => {
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
## [Get App](https://docs.datadoghq.com/api/latest/app-builder/#get-app)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#get-app-v2)


GET https://api.ap1.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.ap2.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.datadoghq.eu/api/v2/app-builder/apps/{app_id}https://api.ddog-gov.com/api/v2/app-builder/apps/{app_id}https://api.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.us3.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.us5.datadoghq.com/api/v2/app-builder/apps/{app_id}
### Overview
Get the full definition of an app. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires all of the following permissions:
* `apps_run`
* `connections_read`
  

### Arguments
#### Path Parameters
Name
Type
Description
app_id [_required_]
string
The ID of the app to retrieve.
#### Query Strings
Name
Type
Description
version
string
The version number of the app to retrieve. If not specified, the latest version is returned. Version numbers start at 1 and increment with each update. The special values `latest` and `deployed` can be used to retrieve the latest version or the published version, respectively.
### Response
  * [200](https://docs.datadoghq.com/api/latest/app-builder/#GetApp-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#GetApp-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#GetApp-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/app-builder/#GetApp-404-v2)
  * [410](https://docs.datadoghq.com/api/latest/app-builder/#GetApp-410-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#GetApp-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


The full app definition response object.
Field
Type
Description
data
object
The data object containing the app definition.
attributes [_required_]
object
The app definition attributes, such as name, description, and components.
components
[object]
The UI components that make up the app.
events
[object]
Events to listen for on the grid component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the grid component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this grid component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a grid component.
backgroundColor
string
The background color of the grid.
default: `default`
children
[object]
The child components of the grid.
events
[object]
Events to listen for on the UI component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the UI component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this UI component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a UI component. Different component types can have their own additional unique properties. See the [components documentation](https://docs.datadoghq.com/service_management/app_builder/components/) for more detail on each component type and its properties.
children
[object]
The child components of the UI component.
isVisible
<oneOf>
Whether the UI component is visible. If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
type [_required_]
enum
The UI component type. Allowed enum values: `table,textInput,textArea,button,text,select,modal,schemaForm,checkbox,tabs,vegaChart,radioButtons,numberInput,fileInput,jsonInput,gridCell,dateRangePicker,search,container,calloutValue`
isVisible
<oneOf>
Whether the grid component and its children are visible. If a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
string
Option 2
boolean
default: `true`
type [_required_]
enum
The grid component type. Allowed enum values: `grid`
default: `grid`
description
string
A human-readable description for the app.
favorite
boolean
Whether the app is marked as a favorite by the current user.
name
string
The name of the app.
queries
[ <oneOf>]
An array of queries, such as external actions and state variables, that the app uses.
Option 1
object
An action query. This query type is used to trigger an action, such as sending a HTTP request.
events
[object]
Events to listen for downstream of the action query.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id [_required_]
uuid
The ID of the action query.
name [_required_]
string
A unique identifier for this action query. This name is also used to access the query's result throughout the app.
properties [_required_]
object
The properties of the action query.
condition
<oneOf>
Whether to run this query. If specified, the query will only run if this condition evaluates to `true` in JavaScript and all other conditions are also met.
Option 1
boolean
Option 2
string
debounceInMs
<oneOf>
The minimum time in milliseconds that must pass before the query can be triggered again. This is useful for preventing accidental double-clicks from triggering the query multiple times.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
mockedOutputs
<oneOf>
The mocked outputs of the action query. This is useful for testing the app without actually running the action.
Option 1
string
Option 2
object
The mocked outputs of the action query.
enabled [_required_]
<oneOf>
Whether to enable the mocked outputs for testing.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The mocked outputs of the action query, serialized as JSON.
onlyTriggerManually
<oneOf>
Determines when this query is executed. If set to `false`, the query will run when the app loads and whenever any query arguments change. If set to `true`, the query will only run when manually triggered from elsewhere in the app.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The post-query transformation function, which is a JavaScript function that changes the query's `.outputs` property after the query's execution.
pollingIntervalInMs
<oneOf>
If specified, the app will poll the query at the specified interval in milliseconds. The minimum polling interval is 15 seconds. The query will only poll when the app's browser tab is active.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
requiresConfirmation
<oneOf>
Whether to prompt the user to confirm this query before it runs.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
showToastOnError
<oneOf>
Whether to display a toast to the user when the query returns an error.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
spec [_required_]
<oneOf>
The definition of the action query.
Option 1
string
Option 2
object
The action query spec object.
connectionGroup
object
The connection group to use for an action query.
id
uuid
The ID of the connection group.
tags
[string]
The tags of the connection group.
connectionId
string
The ID of the custom connection to use for this action query.
fqn [_required_]
string
The fully qualified name of the action type.
inputs
<oneOf>
The inputs to the action query. These are the values that are passed to the action when it is triggered.
Option 1
string
Option 2
object
The inputs to the action query. See the [Actions Catalog](https://docs.datadoghq.com/actions/actions_catalog/) for more detail on each action and its inputs.
type [_required_]
enum
The action query type. Allowed enum values: `action`
default: `action`
Option 2
object
A data transformer, which is custom JavaScript code that executes and transforms data when its inputs change.
id [_required_]
uuid
The ID of the data transformer.
name [_required_]
string
A unique identifier for this data transformer. This name is also used to access the transformer's result throughout the app.
properties [_required_]
object
The properties of the data transformer.
outputs
string
A JavaScript function that returns the transformed data.
type [_required_]
enum
The data transform type. Allowed enum values: `dataTransform`
default: `dataTransform`
Option 3
object
A variable, which can be set and read by other components in the app.
id [_required_]
uuid
The ID of the state variable.
name [_required_]
string
A unique identifier for this state variable. This name is also used to access the variable's value throughout the app.
properties [_required_]
object
The properties of the state variable.
defaultValue
The default value of the state variable.
type [_required_]
enum
The state variable type. Allowed enum values: `stateVariable`
default: `stateVariable`
rootInstanceName
string
The name of the root component of the app. This must be a `grid` component that contains all other components.
tags
[string]
A list of tags for the app, which can be used to filter apps.
id [_required_]
uuid
The ID of the app.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
included
[object]
Data on the version of the app that was published.
attributes
object
The attributes object containing the version ID of the published app.
app_version_id
uuid
The version ID of the app that was published. For an unpublished app, this is always the nil UUID (`00000000-0000-0000-0000-000000000000`).
id
uuid
The deployment ID.
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
meta
object
Metadata of an app.
created_at
date-time
Timestamp of when the app was created.
deleted_at
date-time
Timestamp of when the app was deleted.
org_id
int64
The Datadog organization ID that owns the app.
updated_at
date-time
Timestamp of when the app was last updated.
updated_since_deployment
boolean
Whether the app was updated since it was last published. Published apps are pinned to a specific version and do not automatically update when the app is updated.
user_id
int64
The ID of the user who created the app.
user_name
string
The name (or email address) of the user who created the app.
user_uuid
uuid
The UUID of the user who created the app.
version
int64
The version number of the app. This starts at 1 and increments with each update.
relationship
object
The app's publication relationship and custom connections.
connections
[object]
Array of custom connections used by the app.
attributes
object
The custom connection attributes.
name
string
The name of the custom connection.
onPremRunner
object
Information about the Private Action Runner used by the custom connection, if the custom connection is associated with a Private Action Runner.
id
string
The Private Action Runner ID.
url
string
The URL of the Private Action Runner.
id
uuid
The ID of the custom connection.
type
enum
The custom connection type. Allowed enum values: `custom_connections`
default: `custom_connections`
deployment
object
Information pointing to the app's publication status.
data
object
Data object containing the deployment ID.
id
uuid
The deployment ID.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
```
{
  "data": {
    "attributes": {
      "components": [
        {
          "events": [
            {
              "name": "click",
              "type": "triggerQuery"
            }
          ],
          "id": "string",
          "name": "",
          "properties": {
            "backgroundColor": "string",
            "children": [
              {
                "events": [
                  {
                    "name": "click",
                    "type": "triggerQuery"
                  }
                ],
                "id": "string",
                "name": "",
                "properties": {
                  "children": [],
                  "isVisible": {
                    "type": "undefined"
                  }
                },
                "type": "text"
              }
            ],
            "isVisible": {
              "type": "undefined"
            }
          },
          "type": "grid"
        }
      ],
      "description": "string",
      "favorite": false,
      "name": "string",
      "queries": [
        {
          "events": [
            {
              "name": "click",
              "type": "triggerQuery"
            }
          ],
          "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
          "name": "fetchPendingOrders",
          "properties": {
            "condition": {
              "type": "undefined"
            },
            "debounceInMs": {
              "example": "undefined",
              "format": "undefined",
              "type": "undefined"
            },
            "mockedOutputs": {
              "type": "undefined"
            },
            "onlyTriggerManually": {
              "type": "undefined"
            },
            "outputs": "${((outputs) => {return outputs.body.data})(self.rawOutputs)}",
            "pollingIntervalInMs": {
              "example": "undefined",
              "format": "undefined",
              "minimum": "undefined",
              "type": "undefined"
            },
            "requiresConfirmation": {
              "type": "undefined"
            },
            "showToastOnError": {
              "type": "undefined"
            },
            "spec": {
              "type": ""
            }
          },
          "type": "action"
        }
      ],
      "rootInstanceName": "string",
      "tags": [
        "service:webshop-backend",
        "team:webshop"
      ]
    },
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "type": "appDefinitions"
  },
  "included": [
    {
      "attributes": {
        "app_version_id": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      },
      "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
      "meta": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "user_id": "integer",
        "user_name": "string",
        "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      },
      "type": "deployment"
    }
  ],
  "meta": {
    "created_at": "2019-09-19T10:00:00.000Z",
    "deleted_at": "2019-09-19T10:00:00.000Z",
    "org_id": "integer",
    "updated_at": "2019-09-19T10:00:00.000Z",
    "updated_since_deployment": false,
    "user_id": "integer",
    "user_name": "string",
    "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "version": "integer"
  },
  "relationship": {
    "connections": [
      {
        "attributes": {
          "name": "string",
          "onPremRunner": {
            "id": "string",
            "url": "string"
          }
        },
        "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
        "type": "custom_connections"
      }
    ],
    "deployment": {
      "data": {
        "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
        "type": "deployment"
      },
      "meta": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "user_id": "integer",
        "user_name": "string",
        "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      }
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Gone
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  Get App
Copy
```
                  # Path parameters  
export app_id="65bb1f25-52e1-4510-9f8d-22d1516ed693"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps/${app_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get App
```
"""
Get App returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.get_app(
        app_id=APP_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get App
```
# Get App returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new

# there is a valid "app" in the system
APP_DATA_ID = ENV["APP_DATA_ID"]
p api_instance.get_app(APP_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get App
```
// Get App returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "app" in the system
	AppDataID := uuid.MustParse(os.Getenv("APP_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.GetApp(ctx, AppDataID, *datadogV2.NewGetAppOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.GetApp`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.GetApp`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get App
```
// Get App returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.GetAppResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    // there is a valid "app" in the system
    UUID APP_DATA_ID = null;
    try {
      APP_DATA_ID = UUID.fromString(System.getenv("APP_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      GetAppResponse result = apiInstance.getApp(APP_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#getApp");
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

#####  Get App
```
// Get App returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;
use datadog_api_client::datadogV2::api_app_builder::GetAppOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "app" in the system
    let app_data_id =
        uuid::Uuid::parse_str(&std::env::var("APP_DATA_ID").unwrap()).expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api
        .get_app(app_data_id.clone(), GetAppOptionalParams::default())
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

#####  Get App
```
/**
 * Get App returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

// there is a valid "app" in the system
const APP_DATA_ID = process.env.APP_DATA_ID as string;

const params: v2.AppBuilderApiGetAppRequest = {
  appId: APP_DATA_ID,
};

apiInstance
  .getApp(params)
  .then((data: v2.GetAppResponse) => {
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
## [Update App](https://docs.datadoghq.com/api/latest/app-builder/#update-app)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#update-app-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.ap2.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.datadoghq.eu/api/v2/app-builder/apps/{app_id}https://api.ddog-gov.com/api/v2/app-builder/apps/{app_id}https://api.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.us3.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.us5.datadoghq.com/api/v2/app-builder/apps/{app_id}
### Overview
Update an existing app. This creates a new version of the app. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires all of the following permissions:
* `apps_write`
* `connections_resolve`
* `workflows_run`
  

### Arguments
#### Path Parameters
Name
Type
Description
app_id [_required_]
string
The ID of the app to update.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


Field
Type
Description
data
object
The data object containing the new app definition. Any fields not included in the request remain unchanged.
attributes
object
App definition attributes to be updated, such as name, description, and components.
components
[object]
The new UI components that make up the app. If this field is set, all existing components are replaced with the new components under this field.
events
[object]
Events to listen for on the grid component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the grid component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this grid component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a grid component.
backgroundColor
string
The background color of the grid.
default: `default`
children
[object]
The child components of the grid.
events
[object]
Events to listen for on the UI component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the UI component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this UI component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a UI component. Different component types can have their own additional unique properties. See the [components documentation](https://docs.datadoghq.com/service_management/app_builder/components/) for more detail on each component type and its properties.
children
[object]
The child components of the UI component.
isVisible
<oneOf>
Whether the UI component is visible. If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
type [_required_]
enum
The UI component type. Allowed enum values: `table,textInput,textArea,button,text,select,modal,schemaForm,checkbox,tabs,vegaChart,radioButtons,numberInput,fileInput,jsonInput,gridCell,dateRangePicker,search,container,calloutValue`
isVisible
<oneOf>
Whether the grid component and its children are visible. If a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
string
Option 2
boolean
default: `true`
type [_required_]
enum
The grid component type. Allowed enum values: `grid`
default: `grid`
description
string
The new human-readable description for the app.
name
string
The new name of the app.
queries
[ <oneOf>]
The new array of queries, such as external actions and state variables, that the app uses. If this field is set, all existing queries are replaced with the new queries under this field.
Option 1
object
An action query. This query type is used to trigger an action, such as sending a HTTP request.
events
[object]
Events to listen for downstream of the action query.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id [_required_]
uuid
The ID of the action query.
name [_required_]
string
A unique identifier for this action query. This name is also used to access the query's result throughout the app.
properties [_required_]
object
The properties of the action query.
condition
<oneOf>
Whether to run this query. If specified, the query will only run if this condition evaluates to `true` in JavaScript and all other conditions are also met.
Option 1
boolean
Option 2
string
debounceInMs
<oneOf>
The minimum time in milliseconds that must pass before the query can be triggered again. This is useful for preventing accidental double-clicks from triggering the query multiple times.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
mockedOutputs
<oneOf>
The mocked outputs of the action query. This is useful for testing the app without actually running the action.
Option 1
string
Option 2
object
The mocked outputs of the action query.
enabled [_required_]
<oneOf>
Whether to enable the mocked outputs for testing.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The mocked outputs of the action query, serialized as JSON.
onlyTriggerManually
<oneOf>
Determines when this query is executed. If set to `false`, the query will run when the app loads and whenever any query arguments change. If set to `true`, the query will only run when manually triggered from elsewhere in the app.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The post-query transformation function, which is a JavaScript function that changes the query's `.outputs` property after the query's execution.
pollingIntervalInMs
<oneOf>
If specified, the app will poll the query at the specified interval in milliseconds. The minimum polling interval is 15 seconds. The query will only poll when the app's browser tab is active.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
requiresConfirmation
<oneOf>
Whether to prompt the user to confirm this query before it runs.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
showToastOnError
<oneOf>
Whether to display a toast to the user when the query returns an error.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
spec [_required_]
<oneOf>
The definition of the action query.
Option 1
string
Option 2
object
The action query spec object.
connectionGroup
object
The connection group to use for an action query.
id
uuid
The ID of the connection group.
tags
[string]
The tags of the connection group.
connectionId
string
The ID of the custom connection to use for this action query.
fqn [_required_]
string
The fully qualified name of the action type.
inputs
<oneOf>
The inputs to the action query. These are the values that are passed to the action when it is triggered.
Option 1
string
Option 2
object
The inputs to the action query. See the [Actions Catalog](https://docs.datadoghq.com/actions/actions_catalog/) for more detail on each action and its inputs.
type [_required_]
enum
The action query type. Allowed enum values: `action`
default: `action`
Option 2
object
A data transformer, which is custom JavaScript code that executes and transforms data when its inputs change.
id [_required_]
uuid
The ID of the data transformer.
name [_required_]
string
A unique identifier for this data transformer. This name is also used to access the transformer's result throughout the app.
properties [_required_]
object
The properties of the data transformer.
outputs
string
A JavaScript function that returns the transformed data.
type [_required_]
enum
The data transform type. Allowed enum values: `dataTransform`
default: `dataTransform`
Option 3
object
A variable, which can be set and read by other components in the app.
id [_required_]
uuid
The ID of the state variable.
name [_required_]
string
A unique identifier for this state variable. This name is also used to access the variable's value throughout the app.
properties [_required_]
object
The properties of the state variable.
defaultValue
The default value of the state variable.
type [_required_]
enum
The state variable type. Allowed enum values: `stateVariable`
default: `stateVariable`
rootInstanceName
string
The new name of the root component of the app. This must be a `grid` component that contains all other components.
tags
[string]
The new list of tags for the app, which can be used to filter apps. If this field is set, any existing tags not included in the request are removed.
id
uuid
The ID of the app to update. The app ID must match the ID in the URL path.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
```
{
  "data": {
    "attributes": {
      "name": "Updated Name",
      "rootInstanceName": "grid0"
    },
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "type": "appDefinitions"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/app-builder/#UpdateApp-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#UpdateApp-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#UpdateApp-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#UpdateApp-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


The response object after an app is successfully updated.
Field
Type
Description
data
object
The data object containing the updated app definition.
attributes [_required_]
object
The updated app definition attributes, such as name, description, and components.
components
[object]
The UI components that make up the app.
events
[object]
Events to listen for on the grid component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the grid component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this grid component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a grid component.
backgroundColor
string
The background color of the grid.
default: `default`
children
[object]
The child components of the grid.
events
[object]
Events to listen for on the UI component.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id
string
The ID of the UI component. This property is deprecated; use `name` to identify individual components instead.
name [_required_]
string
A unique identifier for this UI component. This name is also visible in the app editor.
properties [_required_]
object
Properties of a UI component. Different component types can have their own additional unique properties. See the [components documentation](https://docs.datadoghq.com/service_management/app_builder/components/) for more detail on each component type and its properties.
children
[object]
The child components of the UI component.
isVisible
<oneOf>
Whether the UI component is visible. If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
type [_required_]
enum
The UI component type. Allowed enum values: `table,textInput,textArea,button,text,select,modal,schemaForm,checkbox,tabs,vegaChart,radioButtons,numberInput,fileInput,jsonInput,gridCell,dateRangePicker,search,container,calloutValue`
isVisible
<oneOf>
Whether the grid component and its children are visible. If a string, it must be a valid JavaScript expression that evaluates to a boolean.
Option 1
string
Option 2
boolean
default: `true`
type [_required_]
enum
The grid component type. Allowed enum values: `grid`
default: `grid`
description
string
The human-readable description for the app.
favorite
boolean
Whether the app is marked as a favorite by the current user.
name
string
The name of the app.
queries
[ <oneOf>]
An array of queries, such as external actions and state variables, that the app uses.
Option 1
object
An action query. This query type is used to trigger an action, such as sending a HTTP request.
events
[object]
Events to listen for downstream of the action query.
name
enum
The triggering action for the event. Allowed enum values: `pageChange,tableRowClick,_tableRowButtonClick,change,submit,click,toggleOpen,close,open,executionFinished`
type
enum
The response to the event. Allowed enum values: `custom,setComponentState,triggerQuery,openModal,closeModal,openUrl,downloadFile,setStateVariableValue`
id [_required_]
uuid
The ID of the action query.
name [_required_]
string
A unique identifier for this action query. This name is also used to access the query's result throughout the app.
properties [_required_]
object
The properties of the action query.
condition
<oneOf>
Whether to run this query. If specified, the query will only run if this condition evaluates to `true` in JavaScript and all other conditions are also met.
Option 1
boolean
Option 2
string
debounceInMs
<oneOf>
The minimum time in milliseconds that must pass before the query can be triggered again. This is useful for preventing accidental double-clicks from triggering the query multiple times.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
mockedOutputs
<oneOf>
The mocked outputs of the action query. This is useful for testing the app without actually running the action.
Option 1
string
Option 2
object
The mocked outputs of the action query.
enabled [_required_]
<oneOf>
Whether to enable the mocked outputs for testing.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The mocked outputs of the action query, serialized as JSON.
onlyTriggerManually
<oneOf>
Determines when this query is executed. If set to `false`, the query will run when the app loads and whenever any query arguments change. If set to `true`, the query will only run when manually triggered from elsewhere in the app.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
outputs
string
The post-query transformation function, which is a JavaScript function that changes the query's `.outputs` property after the query's execution.
pollingIntervalInMs
<oneOf>
If specified, the app will poll the query at the specified interval in milliseconds. The minimum polling interval is 15 seconds. The query will only poll when the app's browser tab is active.
Option 1
double
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a number.
requiresConfirmation
<oneOf>
Whether to prompt the user to confirm this query before it runs.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
showToastOnError
<oneOf>
Whether to display a toast to the user when the query returns an error.
Option 1
boolean
Option 2
string
If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
spec [_required_]
<oneOf>
The definition of the action query.
Option 1
string
Option 2
object
The action query spec object.
connectionGroup
object
The connection group to use for an action query.
id
uuid
The ID of the connection group.
tags
[string]
The tags of the connection group.
connectionId
string
The ID of the custom connection to use for this action query.
fqn [_required_]
string
The fully qualified name of the action type.
inputs
<oneOf>
The inputs to the action query. These are the values that are passed to the action when it is triggered.
Option 1
string
Option 2
object
The inputs to the action query. See the [Actions Catalog](https://docs.datadoghq.com/actions/actions_catalog/) for more detail on each action and its inputs.
type [_required_]
enum
The action query type. Allowed enum values: `action`
default: `action`
Option 2
object
A data transformer, which is custom JavaScript code that executes and transforms data when its inputs change.
id [_required_]
uuid
The ID of the data transformer.
name [_required_]
string
A unique identifier for this data transformer. This name is also used to access the transformer's result throughout the app.
properties [_required_]
object
The properties of the data transformer.
outputs
string
A JavaScript function that returns the transformed data.
type [_required_]
enum
The data transform type. Allowed enum values: `dataTransform`
default: `dataTransform`
Option 3
object
A variable, which can be set and read by other components in the app.
id [_required_]
uuid
The ID of the state variable.
name [_required_]
string
A unique identifier for this state variable. This name is also used to access the variable's value throughout the app.
properties [_required_]
object
The properties of the state variable.
defaultValue
The default value of the state variable.
type [_required_]
enum
The state variable type. Allowed enum values: `stateVariable`
default: `stateVariable`
rootInstanceName
string
The name of the root component of the app. This must be a `grid` component that contains all other components.
tags
[string]
A list of tags for the app, which can be used to filter apps.
id [_required_]
uuid
The ID of the updated app.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
included
[object]
Data on the version of the app that was published.
attributes
object
The attributes object containing the version ID of the published app.
app_version_id
uuid
The version ID of the app that was published. For an unpublished app, this is always the nil UUID (`00000000-0000-0000-0000-000000000000`).
id
uuid
The deployment ID.
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
meta
object
Metadata of an app.
created_at
date-time
Timestamp of when the app was created.
deleted_at
date-time
Timestamp of when the app was deleted.
org_id
int64
The Datadog organization ID that owns the app.
updated_at
date-time
Timestamp of when the app was last updated.
updated_since_deployment
boolean
Whether the app was updated since it was last published. Published apps are pinned to a specific version and do not automatically update when the app is updated.
user_id
int64
The ID of the user who created the app.
user_name
string
The name (or email address) of the user who created the app.
user_uuid
uuid
The UUID of the user who created the app.
version
int64
The version number of the app. This starts at 1 and increments with each update.
relationship
object
The app's publication relationship and custom connections.
connections
[object]
Array of custom connections used by the app.
attributes
object
The custom connection attributes.
name
string
The name of the custom connection.
onPremRunner
object
Information about the Private Action Runner used by the custom connection, if the custom connection is associated with a Private Action Runner.
id
string
The Private Action Runner ID.
url
string
The URL of the Private Action Runner.
id
uuid
The ID of the custom connection.
type
enum
The custom connection type. Allowed enum values: `custom_connections`
default: `custom_connections`
deployment
object
Information pointing to the app's publication status.
data
object
Data object containing the deployment ID.
id
uuid
The deployment ID.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
```
{
  "data": {
    "attributes": {
      "components": [
        {
          "events": [
            {
              "name": "click",
              "type": "triggerQuery"
            }
          ],
          "id": "string",
          "name": "",
          "properties": {
            "backgroundColor": "string",
            "children": [
              {
                "events": [
                  {
                    "name": "click",
                    "type": "triggerQuery"
                  }
                ],
                "id": "string",
                "name": "",
                "properties": {
                  "children": [],
                  "isVisible": {
                    "type": "undefined"
                  }
                },
                "type": "text"
              }
            ],
            "isVisible": {
              "type": "undefined"
            }
          },
          "type": "grid"
        }
      ],
      "description": "string",
      "favorite": false,
      "name": "string",
      "queries": [
        {
          "events": [
            {
              "name": "click",
              "type": "triggerQuery"
            }
          ],
          "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
          "name": "fetchPendingOrders",
          "properties": {
            "condition": {
              "type": "undefined"
            },
            "debounceInMs": {
              "example": "undefined",
              "format": "undefined",
              "type": "undefined"
            },
            "mockedOutputs": {
              "type": "undefined"
            },
            "onlyTriggerManually": {
              "type": "undefined"
            },
            "outputs": "${((outputs) => {return outputs.body.data})(self.rawOutputs)}",
            "pollingIntervalInMs": {
              "example": "undefined",
              "format": "undefined",
              "minimum": "undefined",
              "type": "undefined"
            },
            "requiresConfirmation": {
              "type": "undefined"
            },
            "showToastOnError": {
              "type": "undefined"
            },
            "spec": {
              "type": ""
            }
          },
          "type": "action"
        }
      ],
      "rootInstanceName": "string",
      "tags": [
        "service:webshop-backend",
        "team:webshop"
      ]
    },
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "type": "appDefinitions"
  },
  "included": [
    {
      "attributes": {
        "app_version_id": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      },
      "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
      "meta": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "user_id": "integer",
        "user_name": "string",
        "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      },
      "type": "deployment"
    }
  ],
  "meta": {
    "created_at": "2019-09-19T10:00:00.000Z",
    "deleted_at": "2019-09-19T10:00:00.000Z",
    "org_id": "integer",
    "updated_at": "2019-09-19T10:00:00.000Z",
    "updated_since_deployment": false,
    "user_id": "integer",
    "user_name": "string",
    "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "version": "integer"
  },
  "relationship": {
    "connections": [
      {
        "attributes": {
          "name": "string",
          "onPremRunner": {
            "id": "string",
            "url": "string"
          }
        },
        "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
        "type": "custom_connections"
      }
    ],
    "deployment": {
      "data": {
        "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
        "type": "deployment"
      },
      "meta": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "user_id": "integer",
        "user_name": "string",
        "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
      }
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  Update App returns "OK" response
Copy
```
                          # Path parameters  
export app_id="65bb1f25-52e1-4510-9f8d-22d1516ed693"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps/${app_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Updated Name",
      "rootInstanceName": "grid0"
    },
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "type": "appDefinitions"
  }
}
EOF  

                        
```

#####  Update App returns "OK" response
```
// Update App returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "app" in the system
	AppDataID := uuid.MustParse(os.Getenv("APP_DATA_ID"))

	body := datadogV2.UpdateAppRequest{
		Data: &datadogV2.UpdateAppRequestData{
			Attributes: &datadogV2.UpdateAppRequestDataAttributes{
				Name:             datadog.PtrString("Updated Name"),
				RootInstanceName: datadog.PtrString("grid0"),
			},
			Id:   &AppDataID,
			Type: datadogV2.APPDEFINITIONTYPE_APPDEFINITIONS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.UpdateApp(ctx, AppDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.UpdateApp`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.UpdateApp`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update App returns "OK" response
```
// Update App returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.AppDefinitionType;
import com.datadog.api.client.v2.model.UpdateAppRequest;
import com.datadog.api.client.v2.model.UpdateAppRequestData;
import com.datadog.api.client.v2.model.UpdateAppRequestDataAttributes;
import com.datadog.api.client.v2.model.UpdateAppResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    // there is a valid "app" in the system
    UUID APP_DATA_ID = null;
    try {
      APP_DATA_ID = UUID.fromString(System.getenv("APP_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    UpdateAppRequest body =
        new UpdateAppRequest()
            .data(
                new UpdateAppRequestData()
                    .attributes(
                        new UpdateAppRequestDataAttributes()
                            .name("Updated Name")
                            .rootInstanceName("grid0"))
                    .id(APP_DATA_ID)
                    .type(AppDefinitionType.APPDEFINITIONS));

    try {
      UpdateAppResponse result = apiInstance.updateApp(APP_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#updateApp");
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

#####  Update App returns "OK" response
```
"""
Update App returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
from datadog_api_client.v2.model.update_app_request import UpdateAppRequest
from datadog_api_client.v2.model.update_app_request_data import UpdateAppRequestData
from datadog_api_client.v2.model.update_app_request_data_attributes import UpdateAppRequestDataAttributes

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

body = UpdateAppRequest(
    data=UpdateAppRequestData(
        attributes=UpdateAppRequestDataAttributes(
            name="Updated Name",
            root_instance_name="grid0",
        ),
        id=APP_DATA_ID,
        type=AppDefinitionType.APPDEFINITIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.update_app(app_id=APP_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update App returns "OK" response
```
# Update App returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new

# there is a valid "app" in the system
APP_DATA_ID = ENV["APP_DATA_ID"]

body = DatadogAPIClient::V2::UpdateAppRequest.new({
  data: DatadogAPIClient::V2::UpdateAppRequestData.new({
    attributes: DatadogAPIClient::V2::UpdateAppRequestDataAttributes.new({
      name: "Updated Name",
      root_instance_name: "grid0",
    }),
    id: APP_DATA_ID,
    type: DatadogAPIClient::V2::AppDefinitionType::APPDEFINITIONS,
  }),
})
p api_instance.update_app(APP_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update App returns "OK" response
```
// Update App returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;
use datadog_api_client::datadogV2::model::AppDefinitionType;
use datadog_api_client::datadogV2::model::UpdateAppRequest;
use datadog_api_client::datadogV2::model::UpdateAppRequestData;
use datadog_api_client::datadogV2::model::UpdateAppRequestDataAttributes;

#[tokio::main]
async fn main() {
    // there is a valid "app" in the system
    let app_data_id =
        uuid::Uuid::parse_str(&std::env::var("APP_DATA_ID").unwrap()).expect("Invalid UUID");
    let body = UpdateAppRequest::new().data(
        UpdateAppRequestData::new(AppDefinitionType::APPDEFINITIONS)
            .attributes(
                UpdateAppRequestDataAttributes::new()
                    .name("Updated Name".to_string())
                    .root_instance_name("grid0".to_string()),
            )
            .id(app_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api.update_app(app_data_id.clone(), body).await;
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

#####  Update App returns "OK" response
```
/**
 * Update App returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

// there is a valid "app" in the system
const APP_DATA_ID = process.env.APP_DATA_ID as string;

const params: v2.AppBuilderApiUpdateAppRequest = {
  body: {
    data: {
      attributes: {
        name: "Updated Name",
        rootInstanceName: "grid0",
      },
      id: APP_DATA_ID,
      type: "appDefinitions",
    },
  },
  appId: APP_DATA_ID,
};

apiInstance
  .updateApp(params)
  .then((data: v2.UpdateAppResponse) => {
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
## [Delete App](https://docs.datadoghq.com/api/latest/app-builder/#delete-app)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#delete-app-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.ap2.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.datadoghq.eu/api/v2/app-builder/apps/{app_id}https://api.ddog-gov.com/api/v2/app-builder/apps/{app_id}https://api.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.us3.datadoghq.com/api/v2/app-builder/apps/{app_id}https://api.us5.datadoghq.com/api/v2/app-builder/apps/{app_id}
### Overview
Delete a single app. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `apps_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_id [_required_]
string
The ID of the app to delete.
### Response
  * [200](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApp-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApp-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApp-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApp-404-v2)
  * [410](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApp-410-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#DeleteApp-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


The response object after an app is successfully deleted.
Field
Type
Description
data
object
The definition of `DeleteAppResponseData` object.
id [_required_]
uuid
The ID of the deleted app.
type [_required_]
enum
The app definition type. Allowed enum values: `appDefinitions`
default: `appDefinitions`
```
{
  "data": {
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "type": "appDefinitions"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Gone
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  Delete App
Copy
```
                  # Path parameters  
export app_id="65bb1f25-52e1-4510-9f8d-22d1516ed693"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps/${app_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete App
```
"""
Delete App returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.delete_app(
        app_id=APP_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete App
```
# Delete App returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new

# there is a valid "app" in the system
APP_DATA_ID = ENV["APP_DATA_ID"]
p api_instance.delete_app(APP_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete App
```
// Delete App returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "app" in the system
	AppDataID := uuid.MustParse(os.Getenv("APP_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.DeleteApp(ctx, AppDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.DeleteApp`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.DeleteApp`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete App
```
// Delete App returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.DeleteAppResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    // there is a valid "app" in the system
    UUID APP_DATA_ID = null;
    try {
      APP_DATA_ID = UUID.fromString(System.getenv("APP_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      DeleteAppResponse result = apiInstance.deleteApp(APP_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#deleteApp");
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

#####  Delete App
```
// Delete App returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;

#[tokio::main]
async fn main() {
    // there is a valid "app" in the system
    let app_data_id =
        uuid::Uuid::parse_str(&std::env::var("APP_DATA_ID").unwrap()).expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api.delete_app(app_data_id.clone()).await;
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

#####  Delete App
```
/**
 * Delete App returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

// there is a valid "app" in the system
const APP_DATA_ID = process.env.APP_DATA_ID as string;

const params: v2.AppBuilderApiDeleteAppRequest = {
  appId: APP_DATA_ID,
};

apiInstance
  .deleteApp(params)
  .then((data: v2.DeleteAppResponse) => {
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
## [Publish App](https://docs.datadoghq.com/api/latest/app-builder/#publish-app)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#publish-app-v2)


POST https://api.ap1.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.ap2.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.datadoghq.eu/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.ddog-gov.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.us3.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.us5.datadoghq.com/api/v2/app-builder/apps/{app_id}/deployment
### Overview
Publish an app for use by other users. To ensure the app is accessible to the correct users, you also need to set a [Restriction Policy](https://docs.datadoghq.com/api/latest/restriction-policies/) on the app if a policy does not yet exist. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `apps_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_id [_required_]
string
The ID of the app to publish.
### Response
  * [201](https://docs.datadoghq.com/api/latest/app-builder/#PublishApp-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#PublishApp-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#PublishApp-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/app-builder/#PublishApp-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#PublishApp-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


The response object after an app is successfully published.
Field
Type
Description
data
object
The version of the app that was published.
attributes
object
The attributes object containing the version ID of the published app.
app_version_id
uuid
The version ID of the app that was published. For an unpublished app, this is always the nil UUID (`00000000-0000-0000-0000-000000000000`).
id
uuid
The deployment ID.
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
```
{
  "data": {
    "attributes": {
      "app_version_id": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
    },
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "meta": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "user_id": "integer",
      "user_name": "string",
      "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
    },
    "type": "deployment"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  Publish App
Copy
```
                  # Path parameters  
export app_id="65bb1f25-52e1-4510-9f8d-22d1516ed693"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps/${app_id}/deployment" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Publish App
```
"""
Publish App returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.publish_app(
        app_id=APP_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Publish App
```
# Publish App returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new

# there is a valid "app" in the system
APP_DATA_ID = ENV["APP_DATA_ID"]
p api_instance.publish_app(APP_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Publish App
```
// Publish App returns "Created" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "app" in the system
	AppDataID := uuid.MustParse(os.Getenv("APP_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.PublishApp(ctx, AppDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.PublishApp`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.PublishApp`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Publish App
```
// Publish App returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.PublishAppResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    // there is a valid "app" in the system
    UUID APP_DATA_ID = null;
    try {
      APP_DATA_ID = UUID.fromString(System.getenv("APP_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      PublishAppResponse result = apiInstance.publishApp(APP_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#publishApp");
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

#####  Publish App
```
// Publish App returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;

#[tokio::main]
async fn main() {
    // there is a valid "app" in the system
    let app_data_id =
        uuid::Uuid::parse_str(&std::env::var("APP_DATA_ID").unwrap()).expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api.publish_app(app_data_id.clone()).await;
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

#####  Publish App
```
/**
 * Publish App returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

// there is a valid "app" in the system
const APP_DATA_ID = process.env.APP_DATA_ID as string;

const params: v2.AppBuilderApiPublishAppRequest = {
  appId: APP_DATA_ID,
};

apiInstance
  .publishApp(params)
  .then((data: v2.PublishAppResponse) => {
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
## [Unpublish App](https://docs.datadoghq.com/api/latest/app-builder/#unpublish-app)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/app-builder/#unpublish-app-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.ap2.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.datadoghq.eu/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.ddog-gov.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.us3.datadoghq.com/api/v2/app-builder/apps/{app_id}/deploymenthttps://api.us5.datadoghq.com/api/v2/app-builder/apps/{app_id}/deployment
### Overview
Unpublish an app, removing the live version of the app. Unpublishing creates a new instance of a `deployment` object on the app, with a nil `app_version_id` (`00000000-0000-0000-0000-000000000000`). The app can still be updated and published again in the future. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `apps_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_id [_required_]
string
The ID of the app to unpublish.
### Response
  * [200](https://docs.datadoghq.com/api/latest/app-builder/#UnpublishApp-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/app-builder/#UnpublishApp-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/app-builder/#UnpublishApp-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/app-builder/#UnpublishApp-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/app-builder/#UnpublishApp-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


The response object after an app is successfully unpublished.
Field
Type
Description
data
object
The version of the app that was published.
attributes
object
The attributes object containing the version ID of the published app.
app_version_id
uuid
The version ID of the app that was published. For an unpublished app, this is always the nil UUID (`00000000-0000-0000-0000-000000000000`).
id
uuid
The deployment ID.
meta
object
Metadata object containing the publication creation information.
created_at
date-time
Timestamp of when the app was published.
user_id
int64
The ID of the user who published the app.
user_name
string
The name (or email address) of the user who published the app.
user_uuid
uuid
The UUID of the user who published the app.
type
enum
The deployment type. Allowed enum values: `deployment`
default: `deployment`
```
{
  "data": {
    "attributes": {
      "app_version_id": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
    },
    "id": "65bb1f25-52e1-4510-9f8d-22d1516ed693",
    "meta": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "user_id": "integer",
      "user_name": "string",
      "user_uuid": "65bb1f25-52e1-4510-9f8d-22d1516ed693"
    },
    "type": "deployment"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Model](https://docs.datadoghq.com/api/latest/app-builder/)
  * [Example](https://docs.datadoghq.com/api/latest/app-builder/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/app-builder/?code-lang=typescript)


#####  Unpublish App
Copy
```
                  # Path parameters  
export app_id="65bb1f25-52e1-4510-9f8d-22d1516ed693"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/app-builder/apps/${app_id}/deployment" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Unpublish App
```
"""
Unpublish App returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.unpublish_app(
        app_id=APP_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Unpublish App
```
# Unpublish App returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AppBuilderAPI.new

# there is a valid "app" in the system
APP_DATA_ID = ENV["APP_DATA_ID"]
p api_instance.unpublish_app(APP_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Unpublish App
```
// Unpublish App returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "app" in the system
	AppDataID := uuid.MustParse(os.Getenv("APP_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAppBuilderApi(apiClient)
	resp, r, err := api.UnpublishApp(ctx, AppDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBuilderApi.UnpublishApp`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AppBuilderApi.UnpublishApp`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Unpublish App
```
// Unpublish App returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AppBuilderApi;
import com.datadog.api.client.v2.model.UnpublishAppResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AppBuilderApi apiInstance = new AppBuilderApi(defaultClient);

    // there is a valid "app" in the system
    UUID APP_DATA_ID = null;
    try {
      APP_DATA_ID = UUID.fromString(System.getenv("APP_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      UnpublishAppResponse result = apiInstance.unpublishApp(APP_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppBuilderApi#unpublishApp");
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

#####  Unpublish App
```
// Unpublish App returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_app_builder::AppBuilderAPI;

#[tokio::main]
async fn main() {
    // there is a valid "app" in the system
    let app_data_id =
        uuid::Uuid::parse_str(&std::env::var("APP_DATA_ID").unwrap()).expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = AppBuilderAPI::with_config(configuration);
    let resp = api.unpublish_app(app_data_id.clone()).await;
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

#####  Unpublish App
```
/**
 * Unpublish App returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AppBuilderApi(configuration);

// there is a valid "app" in the system
const APP_DATA_ID = process.env.APP_DATA_ID as string;

const params: v2.AppBuilderApiUnpublishAppRequest = {
  appId: APP_DATA_ID,
};

apiInstance
  .unpublishApp(params)
  .then((data: v2.UnpublishAppResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a5c14004-88a8-42cc-87a4-fa91d0c30cf4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4651b4f6-0905-49b3-a7e0-d12a390b8cd7&pt=App%20Builder&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapp-builder%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a5c14004-88a8-42cc-87a4-fa91d0c30cf4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4651b4f6-0905-49b3-a7e0-d12a390b8cd7&pt=App%20Builder&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapp-builder%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=5c797741-dc4e-48e2-be58-2f1d4b4a1015&bo=2&sid=cb8cfe40f0be11f099ffd3211cb87056&vid=cb8d3b40f0be11f0b13449d819231651&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=App%20Builder&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapp-builder%2F&r=&lt=2233&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=206788)
