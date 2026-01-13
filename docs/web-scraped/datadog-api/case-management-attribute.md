# Source: https://docs.datadoghq.com/api/latest/case-management-attribute/

# Case Management Attribute
View and configure custom attributes within Case Management. See the [Case Management page](https://docs.datadoghq.com/service_management/case_management/) for more information.
## [Get all custom attributes](https://docs.datadoghq.com/api/latest/case-management-attribute/#get-all-custom-attributes)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management-attribute/#get-all-custom-attributes-v2)


GET https://api.ap1.datadoghq.com/api/v2/cases/types/custom_attributeshttps://api.ap2.datadoghq.com/api/v2/cases/types/custom_attributeshttps://api.datadoghq.eu/api/v2/cases/types/custom_attributeshttps://api.ddog-gov.com/api/v2/cases/types/custom_attributeshttps://api.datadoghq.com/api/v2/cases/types/custom_attributeshttps://api.us3.datadoghq.com/api/v2/cases/types/custom_attributeshttps://api.us5.datadoghq.com/api/v2/cases/types/custom_attributes
### Overview
Get all custom attributes
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributes-200-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributes-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributes-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributes-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


Custom attribute configs response.
Field
Type
Description
data
[object]
List of custom attribute configs of case type
attributes
object
Custom attribute resource attributes
case_type_id [_required_]
string
Custom attribute config identifier.
description
string
Custom attribute description.
display_name [_required_]
string
Custom attribute name.
is_multi [_required_]
boolean
Whether multiple values can be set
key [_required_]
string
Custom attribute key. This will be the value use to search on this custom attribute
type [_required_]
enum
Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`
id
string
Custom attribute configs identifier
type
enum
Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute`
default: `custom_attribute`
```
{
  "data": [
    {
      "attributes": {
        "case_type_id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
        "description": "AWS Region, must be a valid region supported by AWS",
        "display_name": "AWS Region",
        "is_multi": true,
        "key": "aws_region",
        "type": "NUMBER"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "custom_attribute"
    }
  ]
}
```

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=typescript)


#####  Get all custom attributes
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/custom_attributes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all custom attributes
```
"""
Get all custom attributes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.get_all_custom_attributes()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all custom attributes
```
# Get all custom attributes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new
p api_instance.get_all_custom_attributes()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all custom attributes
```
// Get all custom attributes returns "OK" response

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
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	resp, r, err := api.GetAllCustomAttributes(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.GetAllCustomAttributes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementAttributeApi.GetAllCustomAttributes`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all custom attributes
```
// Get all custom attributes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;
import com.datadog.api.client.v2.model.CustomAttributeConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    try {
      CustomAttributeConfigsResponse result = apiInstance.getAllCustomAttributes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CaseManagementAttributeApi#getAllCustomAttributes");
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

#####  Get all custom attributes
```
// Get all custom attributes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api.get_all_custom_attributes().await;
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

#####  Get all custom attributes
```
/**
 * Get all custom attributes returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

apiInstance
  .getAllCustomAttributes()
  .then((data: v2.CustomAttributeConfigsResponse) => {
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
## [Get all custom attributes config of case type](https://docs.datadoghq.com/api/latest/case-management-attribute/#get-all-custom-attributes-config-of-case-type)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management-attribute/#get-all-custom-attributes-config-of-case-type-v2)


GET https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.datadoghq.eu/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.ddog-gov.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes
### Overview
Get all custom attribute config of case type
### Arguments
#### Path Parameters
Name
Type
Description
case_type_id [_required_]
string
Case type’s UUID
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributeConfigsByCaseType-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributeConfigsByCaseType-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributeConfigsByCaseType-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributeConfigsByCaseType-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management-attribute/#GetAllCustomAttributeConfigsByCaseType-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


Custom attribute configs response.
Field
Type
Description
data
[object]
List of custom attribute configs of case type
attributes
object
Custom attribute resource attributes
case_type_id [_required_]
string
Custom attribute config identifier.
description
string
Custom attribute description.
display_name [_required_]
string
Custom attribute name.
is_multi [_required_]
boolean
Whether multiple values can be set
key [_required_]
string
Custom attribute key. This will be the value use to search on this custom attribute
type [_required_]
enum
Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`
id
string
Custom attribute configs identifier
type
enum
Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute`
default: `custom_attribute`
```
{
  "data": [
    {
      "attributes": {
        "case_type_id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
        "description": "AWS Region, must be a valid region supported by AWS",
        "display_name": "AWS Region",
        "is_multi": true,
        "key": "aws_region",
        "type": "NUMBER"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "custom_attribute"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=typescript)


#####  Get all custom attributes config of case type
Copy
```
                  # Path parameters  
export case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}/custom_attributes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all custom attributes config of case type
```
"""
Get all custom attributes config of case type returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.get_all_custom_attribute_configs_by_case_type(
        case_type_id=CASE_TYPE_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all custom attributes config of case type
```
# Get all custom attributes config of case type returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new

# there is a valid "case_type" in the system
CASE_TYPE_ID = ENV["CASE_TYPE_ID"]
p api_instance.get_all_custom_attribute_configs_by_case_type(CASE_TYPE_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all custom attributes config of case type
```
// Get all custom attributes config of case type returns "OK" response

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
	// there is a valid "case_type" in the system
	CaseTypeID := os.Getenv("CASE_TYPE_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	resp, r, err := api.GetAllCustomAttributeConfigsByCaseType(ctx, CaseTypeID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.GetAllCustomAttributeConfigsByCaseType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementAttributeApi.GetAllCustomAttributeConfigsByCaseType`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all custom attributes config of case type
```
// Get all custom attributes config of case type returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;
import com.datadog.api.client.v2.model.CustomAttributeConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    // there is a valid "case_type" in the system
    String CASE_TYPE_ID = System.getenv("CASE_TYPE_ID");

    try {
      CustomAttributeConfigsResponse result =
          apiInstance.getAllCustomAttributeConfigsByCaseType(CASE_TYPE_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling"
              + " CaseManagementAttributeApi#getAllCustomAttributeConfigsByCaseType");
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

#####  Get all custom attributes config of case type
```
// Get all custom attributes config of case type returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;

#[tokio::main]
async fn main() {
    // there is a valid "case_type" in the system
    let case_type_id = std::env::var("CASE_TYPE_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api
        .get_all_custom_attribute_configs_by_case_type(case_type_id.clone())
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

#####  Get all custom attributes config of case type
```
/**
 * Get all custom attributes config of case type returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

// there is a valid "case_type" in the system
const CASE_TYPE_ID = process.env.CASE_TYPE_ID as string;

const params: v2.CaseManagementAttributeApiGetAllCustomAttributeConfigsByCaseTypeRequest =
  {
    caseTypeId: CASE_TYPE_ID,
  };

apiInstance
  .getAllCustomAttributeConfigsByCaseType(params)
  .then((data: v2.CustomAttributeConfigsResponse) => {
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
## [Create custom attribute config for a case type](https://docs.datadoghq.com/api/latest/case-management-attribute/#create-custom-attribute-config-for-a-case-type)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management-attribute/#create-custom-attribute-config-for-a-case-type-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.datadoghq.eu/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.ddog-gov.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributeshttps://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes
### Overview
Create custom attribute config for a case type
### Arguments
#### Path Parameters
Name
Type
Description
case_type_id [_required_]
string
Case type’s UUID
### Request
#### Body Data (required)
Custom attribute config payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


Field
Type
Description
data [_required_]
object
Custom attribute config
attributes [_required_]
object
Custom attribute config resource attributes
description
string
Custom attribute description.
display_name [_required_]
string
Custom attribute name.
is_multi [_required_]
boolean
Whether multiple values can be set
key [_required_]
string
Custom attribute key. This will be the value use to search on this custom attribute
type [_required_]
enum
Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`
type [_required_]
enum
Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute`
default: `custom_attribute`
```
{
  "data": {
    "attributes": {
      "display_name": "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
      "is_multi": true,
      "key": "region_d9fe56bc9274fbb6",
      "type": "NUMBER"
    },
    "type": "custom_attribute"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/case-management-attribute/#CreateCustomAttributeConfig-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management-attribute/#CreateCustomAttributeConfig-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management-attribute/#CreateCustomAttributeConfig-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management-attribute/#CreateCustomAttributeConfig-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management-attribute/#CreateCustomAttributeConfig-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management-attribute/#CreateCustomAttributeConfig-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


Custom attribute config response.
Field
Type
Description
data
object
The definition of `CustomAttributeConfig` object.
attributes
object
Custom attribute resource attributes
case_type_id [_required_]
string
Custom attribute config identifier.
description
string
Custom attribute description.
display_name [_required_]
string
Custom attribute name.
is_multi [_required_]
boolean
Whether multiple values can be set
key [_required_]
string
Custom attribute key. This will be the value use to search on this custom attribute
type [_required_]
enum
Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`
id
string
Custom attribute configs identifier
type
enum
Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute`
default: `custom_attribute`
```
{
  "data": {
    "attributes": {
      "case_type_id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "description": "AWS Region, must be a valid region supported by AWS",
      "display_name": "AWS Region",
      "is_multi": true,
      "key": "aws_region",
      "type": "NUMBER"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "custom_attribute"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=typescript)


#####  Create custom attribute config for a case type returns "CREATED" response
Copy
```
                          # Path parameters  
export case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}/custom_attributes" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "display_name": "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
      "is_multi": true,
      "key": "region_d9fe56bc9274fbb6",
      "type": "NUMBER"
    },
    "type": "custom_attribute"
  }
}
EOF  

                        
```

#####  Create custom attribute config for a case type returns "CREATED" response
```
// Create custom attribute config for a case type returns "CREATED" response

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
	// there is a valid "case_type" in the system
	CaseTypeID := os.Getenv("CASE_TYPE_ID")

	body := datadogV2.CustomAttributeConfigCreateRequest{
		Data: datadogV2.CustomAttributeConfigCreate{
			Attributes: datadogV2.CustomAttributeConfigAttributesCreate{
				DisplayName: "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
				IsMulti:     true,
				Key:         "region_d9fe56bc9274fbb6",
				Type:        datadogV2.CUSTOMATTRIBUTETYPE_NUMBER,
			},
			Type: datadogV2.CUSTOMATTRIBUTECONFIGRESOURCETYPE_CUSTOM_ATTRIBUTE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	resp, r, err := api.CreateCustomAttributeConfig(ctx, CaseTypeID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.CreateCustomAttributeConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementAttributeApi.CreateCustomAttributeConfig`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create custom attribute config for a case type returns "CREATED" response
```
// Create custom attribute config for a case type returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;
import com.datadog.api.client.v2.model.CustomAttributeConfigAttributesCreate;
import com.datadog.api.client.v2.model.CustomAttributeConfigCreate;
import com.datadog.api.client.v2.model.CustomAttributeConfigCreateRequest;
import com.datadog.api.client.v2.model.CustomAttributeConfigResourceType;
import com.datadog.api.client.v2.model.CustomAttributeConfigResponse;
import com.datadog.api.client.v2.model.CustomAttributeType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    // there is a valid "case_type" in the system
    String CASE_TYPE_ID = System.getenv("CASE_TYPE_ID");

    CustomAttributeConfigCreateRequest body =
        new CustomAttributeConfigCreateRequest()
            .data(
                new CustomAttributeConfigCreate()
                    .attributes(
                        new CustomAttributeConfigAttributesCreate()
                            .displayName("AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
                            .isMulti(true)
                            .key("region_d9fe56bc9274fbb6")
                            .type(CustomAttributeType.NUMBER))
                    .type(CustomAttributeConfigResourceType.CUSTOM_ATTRIBUTE));

    try {
      CustomAttributeConfigResponse result =
          apiInstance.createCustomAttributeConfig(CASE_TYPE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CaseManagementAttributeApi#createCustomAttributeConfig");
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

#####  Create custom attribute config for a case type returns "CREATED" response
```
"""
Create custom attribute config for a case type returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi
from datadog_api_client.v2.model.custom_attribute_config_attributes_create import CustomAttributeConfigAttributesCreate
from datadog_api_client.v2.model.custom_attribute_config_create import CustomAttributeConfigCreate
from datadog_api_client.v2.model.custom_attribute_config_create_request import CustomAttributeConfigCreateRequest
from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType
from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

body = CustomAttributeConfigCreateRequest(
    data=CustomAttributeConfigCreate(
        attributes=CustomAttributeConfigAttributesCreate(
            display_name="AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
            is_multi=True,
            key="region_d9fe56bc9274fbb6",
            type=CustomAttributeType.NUMBER,
        ),
        type=CustomAttributeConfigResourceType.CUSTOM_ATTRIBUTE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.create_custom_attribute_config(case_type_id=CASE_TYPE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create custom attribute config for a case type returns "CREATED" response
```
# Create custom attribute config for a case type returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new

# there is a valid "case_type" in the system
CASE_TYPE_ID = ENV["CASE_TYPE_ID"]

body = DatadogAPIClient::V2::CustomAttributeConfigCreateRequest.new({
  data: DatadogAPIClient::V2::CustomAttributeConfigCreate.new({
    attributes: DatadogAPIClient::V2::CustomAttributeConfigAttributesCreate.new({
      display_name: "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
      is_multi: true,
      key: "region_d9fe56bc9274fbb6",
      type: DatadogAPIClient::V2::CustomAttributeType::NUMBER,
    }),
    type: DatadogAPIClient::V2::CustomAttributeConfigResourceType::CUSTOM_ATTRIBUTE,
  }),
})
p api_instance.create_custom_attribute_config(CASE_TYPE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create custom attribute config for a case type returns "CREATED" response
```
// Create custom attribute config for a case type returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;
use datadog_api_client::datadogV2::model::CustomAttributeConfigAttributesCreate;
use datadog_api_client::datadogV2::model::CustomAttributeConfigCreate;
use datadog_api_client::datadogV2::model::CustomAttributeConfigCreateRequest;
use datadog_api_client::datadogV2::model::CustomAttributeConfigResourceType;
use datadog_api_client::datadogV2::model::CustomAttributeType;

#[tokio::main]
async fn main() {
    // there is a valid "case_type" in the system
    let case_type_id = std::env::var("CASE_TYPE_ID").unwrap();
    let body = CustomAttributeConfigCreateRequest::new(CustomAttributeConfigCreate::new(
        CustomAttributeConfigAttributesCreate::new(
            "AWS Region ".to_string(),
            true,
            "region_d9fe56bc9274fbb6".to_string(),
            CustomAttributeType::NUMBER,
        ),
        CustomAttributeConfigResourceType::CUSTOM_ATTRIBUTE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api
        .create_custom_attribute_config(case_type_id.clone(), body)
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

#####  Create custom attribute config for a case type returns "CREATED" response
```
/**
 * Create custom attribute config for a case type returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

// there is a valid "case_type" in the system
const CASE_TYPE_ID = process.env.CASE_TYPE_ID as string;

const params: v2.CaseManagementAttributeApiCreateCustomAttributeConfigRequest =
  {
    body: {
      data: {
        attributes: {
          displayName: "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
          isMulti: true,
          key: "region_d9fe56bc9274fbb6",
          type: "NUMBER",
        },
        type: "custom_attribute",
      },
    },
    caseTypeId: CASE_TYPE_ID,
  };

apiInstance
  .createCustomAttributeConfig(params)
  .then((data: v2.CustomAttributeConfigResponse) => {
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
## [Delete custom attributes config](https://docs.datadoghq.com/api/latest/case-management-attribute/#delete-custom-attributes-config)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management-attribute/#delete-custom-attributes-config-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}https://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}https://api.datadoghq.eu/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}https://api.ddog-gov.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}https://api.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}https://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}https://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}
### Overview
Delete custom attribute config
### Arguments
#### Path Parameters
Name
Type
Description
case_type_id [_required_]
string
Case type’s UUID
custom_attribute_id [_required_]
string
Case Custom attribute’s UUID
### Response
  * [204](https://docs.datadoghq.com/api/latest/case-management-attribute/#DeleteCustomAttributeConfig-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management-attribute/#DeleteCustomAttributeConfig-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management-attribute/#DeleteCustomAttributeConfig-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management-attribute/#DeleteCustomAttributeConfig-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management-attribute/#DeleteCustomAttributeConfig-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management-attribute/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management-attribute/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management-attribute/?code-lang=typescript)


#####  Delete custom attributes config
Copy
```
                  # Path parameters  
export case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"  
export custom_attribute_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}/custom_attributes/${custom_attribute_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete custom attributes config
```
"""
Delete custom attributes config returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ID = environ["CUSTOM_ATTRIBUTE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    api_instance.delete_custom_attribute_config(
        case_type_id=CASE_TYPE_ID,
        custom_attribute_id=CUSTOM_ATTRIBUTE_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete custom attributes config
```
# Delete custom attributes config returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new

# there is a valid "case_type" in the system
CASE_TYPE_ID = ENV["CASE_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ID = ENV["CUSTOM_ATTRIBUTE_ID"]
api_instance.delete_custom_attribute_config(CASE_TYPE_ID, CUSTOM_ATTRIBUTE_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete custom attributes config
```
// Delete custom attributes config returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "case_type" in the system
	CaseTypeID := os.Getenv("CASE_TYPE_ID")

	// there is a valid "custom_attribute" in the system
	CustomAttributeID := os.Getenv("CUSTOM_ATTRIBUTE_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	r, err := api.DeleteCustomAttributeConfig(ctx, CaseTypeID, CustomAttributeID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.DeleteCustomAttributeConfig`: %v\n", err)
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

#####  Delete custom attributes config
```
// Delete custom attributes config returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    // there is a valid "case_type" in the system
    String CASE_TYPE_ID = System.getenv("CASE_TYPE_ID");

    // there is a valid "custom_attribute" in the system
    String CUSTOM_ATTRIBUTE_ID = System.getenv("CUSTOM_ATTRIBUTE_ID");

    try {
      apiInstance.deleteCustomAttributeConfig(CASE_TYPE_ID, CUSTOM_ATTRIBUTE_ID);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CaseManagementAttributeApi#deleteCustomAttributeConfig");
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

#####  Delete custom attributes config
```
// Delete custom attributes config returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;

#[tokio::main]
async fn main() {
    // there is a valid "case_type" in the system
    let case_type_id = std::env::var("CASE_TYPE_ID").unwrap();

    // there is a valid "custom_attribute" in the system
    let custom_attribute_id = std::env::var("CUSTOM_ATTRIBUTE_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api
        .delete_custom_attribute_config(case_type_id.clone(), custom_attribute_id.clone())
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

#####  Delete custom attributes config
```
/**
 * Delete custom attributes config returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

// there is a valid "case_type" in the system
const CASE_TYPE_ID = process.env.CASE_TYPE_ID as string;

// there is a valid "custom_attribute" in the system
const CUSTOM_ATTRIBUTE_ID = process.env.CUSTOM_ATTRIBUTE_ID as string;

const params: v2.CaseManagementAttributeApiDeleteCustomAttributeConfigRequest =
  {
    caseTypeId: CASE_TYPE_ID,
    customAttributeId: CUSTOM_ATTRIBUTE_ID,
  };

apiInstance
  .deleteCustomAttributeConfig(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=505934d3-ff72-4344-a3e2-c163242747c2&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=bb4a8161-727c-4642-bf75-843a7beffcad&pt=Case%20Management%20Attribute&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management-attribute%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=505934d3-ff72-4344-a3e2-c163242747c2&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=bb4a8161-727c-4642-bf75-843a7beffcad&pt=Case%20Management%20Attribute&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management-attribute%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=2c3c1866-a6c8-40d7-999f-0baaeb8ae036&bo=2&sid=30dec820f0bf11f0b66d5dc00f465c99&vid=30defdd0f0bf11f0b6565f6e489a262d&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Case%20Management%20Attribute&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management-attribute%2F&r=&lt=1901&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=242203)
