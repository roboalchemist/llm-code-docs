# Source: https://docs.datadoghq.com/api/latest/case-management-type/

# Case Management Type
View and configure case types within Case Management. See the [Case Management page](https://docs.datadoghq.com/service_management/case_management/) for more information.
## [Get all case types](https://docs.datadoghq.com/api/latest/case-management-type/#get-all-case-types)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management-type/#get-all-case-types-v2)


GET https://api.ap1.datadoghq.com/api/v2/cases/typeshttps://api.ap2.datadoghq.com/api/v2/cases/typeshttps://api.datadoghq.eu/api/v2/cases/typeshttps://api.ddog-gov.com/api/v2/cases/typeshttps://api.datadoghq.com/api/v2/cases/typeshttps://api.us3.datadoghq.com/api/v2/cases/typeshttps://api.us5.datadoghq.com/api/v2/cases/types
### Overview
Get all case types
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management-type/#GetAllCaseTypes-200-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management-type/#GetAllCaseTypes-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management-type/#GetAllCaseTypes-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management-type/#GetAllCaseTypes-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


Case types response.
Field
Type
Description
data
[object]
List of case types
attributes
object
Case Type resource attributes
deleted_at
date-time
Timestamp of when the case type was deleted
description
string
Case type description.
emoji
string
Case type emoji.
name [_required_]
string
Case type name.
id
string
Case type's identifier
type
enum
Case type resource type Allowed enum values: `case_type`
default: `case_type`
```
{
  "data": [
    {
      "attributes": {
        "deleted_at": "2019-09-19T10:00:00.000Z",
        "description": "Investigations done in case management",
        "emoji": "🕵🏻‍♂️",
        "name": "Investigation"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "case_type"
    }
  ]
}
```

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=typescript)


#####  Get all case types
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all case types
```
"""
Get all case types returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    response = api_instance.get_all_case_types()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all case types
```
# Get all case types returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementTypeAPI.new
p api_instance.get_all_case_types()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all case types
```
// Get all case types returns "OK" response

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
	api := datadogV2.NewCaseManagementTypeApi(apiClient)
	resp, r, err := api.GetAllCaseTypes(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementTypeApi.GetAllCaseTypes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementTypeApi.GetAllCaseTypes`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all case types
```
// Get all case types returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementTypeApi;
import com.datadog.api.client.v2.model.CaseTypesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementTypeApi apiInstance = new CaseManagementTypeApi(defaultClient);

    try {
      CaseTypesResponse result = apiInstance.getAllCaseTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementTypeApi#getAllCaseTypes");
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

#####  Get all case types
```
// Get all case types returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_type::CaseManagementTypeAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementTypeAPI::with_config(configuration);
    let resp = api.get_all_case_types().await;
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

#####  Get all case types
```
/**
 * Get all case types returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementTypeApi(configuration);

apiInstance
  .getAllCaseTypes()
  .then((data: v2.CaseTypesResponse) => {
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
## [Create a case type](https://docs.datadoghq.com/api/latest/case-management-type/#create-a-case-type)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management-type/#create-a-case-type-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/typeshttps://api.ap2.datadoghq.com/api/v2/cases/typeshttps://api.datadoghq.eu/api/v2/cases/typeshttps://api.ddog-gov.com/api/v2/cases/typeshttps://api.datadoghq.com/api/v2/cases/typeshttps://api.us3.datadoghq.com/api/v2/cases/typeshttps://api.us5.datadoghq.com/api/v2/cases/types
### Overview
Create a Case Type
### Request
#### Body Data (required)
Case type payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


Field
Type
Description
data [_required_]
object
Case type
attributes [_required_]
object
Case Type resource attributes
deleted_at
date-time
Timestamp of when the case type was deleted
description
string
Case type description.
emoji
string
Case type emoji.
name [_required_]
string
Case type name.
type [_required_]
enum
Case type resource type Allowed enum values: `case_type`
default: `case_type`
```
{
  "data": {
    "attributes": {
      "description": "Investigations done in case management",
      "emoji": "\ud83d\udc51",
      "name": "Investigation"
    },
    "type": "case_type"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/case-management-type/#CreateCaseType-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management-type/#CreateCaseType-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management-type/#CreateCaseType-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management-type/#CreateCaseType-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management-type/#CreateCaseType-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


Case type response
Field
Type
Description
data
object
The definition of `CaseType` object.
attributes
object
Case Type resource attributes
deleted_at
date-time
Timestamp of when the case type was deleted
description
string
Case type description.
emoji
string
Case type emoji.
name [_required_]
string
Case type name.
id
string
Case type's identifier
type
enum
Case type resource type Allowed enum values: `case_type`
default: `case_type`
```
{
  "data": {
    "attributes": {
      "deleted_at": "2019-09-19T10:00:00.000Z",
      "description": "Investigations done in case management",
      "emoji": "🕵🏻‍♂️",
      "name": "Investigation"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "case_type"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=typescript)


#####  Create a case type returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Investigations done in case management",
      "emoji": "\ud83d\udc51",
      "name": "Investigation"
    },
    "type": "case_type"
  }
}
EOF  

                        
```

#####  Create a case type returns "CREATED" response
```
// Create a case type returns "CREATED" response

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
	body := datadogV2.CaseTypeCreateRequest{
		Data: datadogV2.CaseTypeCreate{
			Attributes: datadogV2.CaseTypeResourceAttributes{
				Description: datadog.PtrString("Investigations done in case management"),
				Emoji:       datadog.PtrString("👑"),
				Name:        "Investigation",
			},
			Type: datadogV2.CASETYPERESOURCETYPE_CASE_TYPE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementTypeApi(apiClient)
	resp, r, err := api.CreateCaseType(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementTypeApi.CreateCaseType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementTypeApi.CreateCaseType`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a case type returns "CREATED" response
```
// Create a case type returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementTypeApi;
import com.datadog.api.client.v2.model.CaseTypeCreate;
import com.datadog.api.client.v2.model.CaseTypeCreateRequest;
import com.datadog.api.client.v2.model.CaseTypeResourceAttributes;
import com.datadog.api.client.v2.model.CaseTypeResourceType;
import com.datadog.api.client.v2.model.CaseTypeResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementTypeApi apiInstance = new CaseManagementTypeApi(defaultClient);

    CaseTypeCreateRequest body =
        new CaseTypeCreateRequest()
            .data(
                new CaseTypeCreate()
                    .attributes(
                        new CaseTypeResourceAttributes()
                            .description("Investigations done in case management")
                            .emoji("👑")
                            .name("Investigation"))
                    .type(CaseTypeResourceType.CASE_TYPE));

    try {
      CaseTypeResponse result = apiInstance.createCaseType(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementTypeApi#createCaseType");
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

#####  Create a case type returns "CREATED" response
```
"""
Create a case type returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi
from datadog_api_client.v2.model.case_type_create import CaseTypeCreate
from datadog_api_client.v2.model.case_type_create_request import CaseTypeCreateRequest
from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType

body = CaseTypeCreateRequest(
    data=CaseTypeCreate(
        attributes=CaseTypeResourceAttributes(
            description="Investigations done in case management",
            emoji="👑",
            name="Investigation",
        ),
        type=CaseTypeResourceType.CASE_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    response = api_instance.create_case_type(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a case type returns "CREATED" response
```
# Create a case type returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementTypeAPI.new

body = DatadogAPIClient::V2::CaseTypeCreateRequest.new({
  data: DatadogAPIClient::V2::CaseTypeCreate.new({
    attributes: DatadogAPIClient::V2::CaseTypeResourceAttributes.new({
      description: "Investigations done in case management",
      emoji: "👑",
      name: "Investigation",
    }),
    type: DatadogAPIClient::V2::CaseTypeResourceType::CASE_TYPE,
  }),
})
p api_instance.create_case_type(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a case type returns "CREATED" response
```
// Create a case type returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_type::CaseManagementTypeAPI;
use datadog_api_client::datadogV2::model::CaseTypeCreate;
use datadog_api_client::datadogV2::model::CaseTypeCreateRequest;
use datadog_api_client::datadogV2::model::CaseTypeResourceAttributes;
use datadog_api_client::datadogV2::model::CaseTypeResourceType;

#[tokio::main]
async fn main() {
    let body = CaseTypeCreateRequest::new(CaseTypeCreate::new(
        CaseTypeResourceAttributes::new("Investigation".to_string())
            .description("Investigations done in case management".to_string())
            .emoji("👑".to_string()),
        CaseTypeResourceType::CASE_TYPE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementTypeAPI::with_config(configuration);
    let resp = api.create_case_type(body).await;
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

#####  Create a case type returns "CREATED" response
```
/**
 * Create a case type returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementTypeApi(configuration);

const params: v2.CaseManagementTypeApiCreateCaseTypeRequest = {
  body: {
    data: {
      attributes: {
        description: "Investigations done in case management",
        emoji: "👑",
        name: "Investigation",
      },
      type: "case_type",
    },
  },
};

apiInstance
  .createCaseType(params)
  .then((data: v2.CaseTypeResponse) => {
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
## [Delete a case type](https://docs.datadoghq.com/api/latest/case-management-type/#delete-a-case-type)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management-type/#delete-a-case-type-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id}https://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id}https://api.datadoghq.eu/api/v2/cases/types/{case_type_id}https://api.ddog-gov.com/api/v2/cases/types/{case_type_id}https://api.datadoghq.com/api/v2/cases/types/{case_type_id}https://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id}https://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id}
### Overview
Delete a case type
### Arguments
#### Path Parameters
Name
Type
Description
case_type_id [_required_]
string
Case type’s UUID
### Response
  * [204](https://docs.datadoghq.com/api/latest/case-management-type/#DeleteCaseType-204-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management-type/#DeleteCaseType-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management-type/#DeleteCaseType-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management-type/#DeleteCaseType-429-v2)


No Content
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-type/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-type/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management-type/?code-lang=typescript)


#####  Delete a case type
Copy
```
                  # Path parameters  
export case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a case type
```
"""
Delete a case type returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    api_instance.delete_case_type(
        case_type_id="case_type_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a case type
```
# Delete a case type returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementTypeAPI.new
api_instance.delete_case_type("case_type_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a case type
```
// Delete a case type returns "No Content" response

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
	api := datadogV2.NewCaseManagementTypeApi(apiClient)
	r, err := api.DeleteCaseType(ctx, "case_type_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementTypeApi.DeleteCaseType`: %v\n", err)
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

#####  Delete a case type
```
// Delete a case type returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementTypeApi apiInstance = new CaseManagementTypeApi(defaultClient);

    try {
      apiInstance.deleteCaseType("f98a5a5b-e0ff-45d4-b2f5-afe6e74de505");
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementTypeApi#deleteCaseType");
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

#####  Delete a case type
```
// Delete a case type returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_type::CaseManagementTypeAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementTypeAPI::with_config(configuration);
    let resp = api.delete_case_type("case_type_id".to_string()).await;
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

#####  Delete a case type
```
/**
 * Delete a case type returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementTypeApi(configuration);

const params: v2.CaseManagementTypeApiDeleteCaseTypeRequest = {
  caseTypeId: "case_type_id",
};

apiInstance
  .deleteCaseType(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=82b7519d-7479-498f-bf09-860712bd275c&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2d09387d-35eb-48b7-aca2-bf0a6155b646&pt=Case%20Management%20Type&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management-type%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=82b7519d-7479-498f-bf09-860712bd275c&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2d09387d-35eb-48b7-aca2-bf0a6155b646&pt=Case%20Management%20Type&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management-type%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=36f770ab-677f-41fd-8f65-e09b365a14e6&bo=2&sid=35894590f0bf11f0b175dbb6df07ed75&vid=35897fc0f0bf11f0801963682effb9b0&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Case%20Management%20Type&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management-type%2F&r=&lt=1397&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=687241)
