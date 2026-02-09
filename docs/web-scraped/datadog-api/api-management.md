# Source: https://docs.datadoghq.com/api/latest/api-management

# API Management
Configure your API endpoints through the Datadog API.
## [Create a new API](https://docs.datadoghq.com/api/latest/api-management/#create-a-new-api)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/api-management/#create-a-new-api-v2)


**Note** : This endpoint is deprecated.
POST https://api.ap1.datadoghq.com/api/v2/apicatalog/openapihttps://api.ap2.datadoghq.com/api/v2/apicatalog/openapihttps://api.datadoghq.eu/api/v2/apicatalog/openapihttps://api.ddog-gov.com/api/v2/apicatalog/openapihttps://api.datadoghq.com/api/v2/apicatalog/openapihttps://api.us3.datadoghq.com/api/v2/apicatalog/openapihttps://api.us5.datadoghq.com/api/v2/apicatalog/openapi
### Overview
Create a new API from the [OpenAPI](https://spec.openapis.org/oas/latest.html) specification given. See the [API Catalog documentation](https://docs.datadoghq.com/api_catalog/add_metadata/) for additional information about the possible metadata. It returns the created API ID. This endpoint requires the `apm_api_catalog_write` permission.
OAuth apps require the `apm_api_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


Expand All
Field
Type
Description
openapi_spec_file
binary
Binary `OpenAPI` spec file
```
{
  "openapi_spec_file": "string"
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/api-management/#CreateOpenAPI-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/api-management/#CreateOpenAPI-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/api-management/#CreateOpenAPI-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/api-management/#CreateOpenAPI-429-v2)


API created successfully
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


Response for `CreateOpenAPI` operation.
Field
Type
Description
data
object
Data envelope for `CreateOpenAPIResponse`.
attributes
object
Attributes for `CreateOpenAPI`.
failed_endpoints
[object]
List of endpoints which couldn't be parsed.
method
string
The endpoint method.
path
string
The endpoint path.
id
uuid
API identifier.
```
{
  "data": {
    "attributes": {
      "failed_endpoints": [
        {
          "method": "string",
          "path": "string"
        }
      ]
    },
    "id": "90646597-5fdb-4a17-a240-647003f8c028"
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/api-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/api-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/api-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/api-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/api-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/api-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/api-management/?code-lang=typescript)


#####  Create a new API
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/openapi" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F openapi_spec_file=@string  

                
```

#####  Create a new API
```
"""
Create a new API returns "API created successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

configuration = Configuration()
configuration.unstable_operations["create_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.create_open_api(
        openapi_spec_file=open("openapi-spec.yaml", "rb"),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a new API
```
# Create a new API returns "API created successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new
opts = {
  openapi_spec_file: File.open("openapi-spec.yaml", "r"),
}
p api_instance.create_open_api(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a new API
```
// Create a new API returns "API created successfully" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.CreateOpenAPI(ctx, *datadogV2.NewCreateOpenAPIOptionalParameters().WithOpenapiSpecFile(func() io.Reader { fp, _ := os.Open("openapi-spec.yaml"); return fp }()))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.CreateOpenAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.CreateOpenAPI`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a new API
```
// Create a new API returns "API created successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import com.datadog.api.client.v2.api.ApiManagementApi.CreateOpenAPIOptionalParameters;
import com.datadog.api.client.v2.model.CreateOpenAPIResponse;
import java.io.File;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    try {
      CreateOpenAPIResponse result =
          apiInstance.createOpenAPI(
              new CreateOpenAPIOptionalParameters().openapiSpecFile(new File("openapi-spec.yaml")));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#createOpenAPI");
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

#####  Create a new API
```
// Create a new API returns "API created successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;
use datadog_api_client::datadogV2::api_api_management::CreateOpenAPIOptionalParams;
use std::fs;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api
        .create_open_api(
            CreateOpenAPIOptionalParams::default()
                .openapi_spec_file(fs::read("openapi-spec.yaml").unwrap()),
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

#####  Create a new API
```
/**
 * Create a new API returns "API created successfully" response
 */

import * as fs from "fs";
import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

const params: v2.APIManagementApiCreateOpenAPIRequest = {
  openapiSpecFile: {
    data: Buffer.from(fs.readFileSync("openapi-spec.yaml", "utf8")),
    name: "openapi-spec.yaml",
  },
};

apiInstance
  .createOpenAPI(params)
  .then((data: v2.CreateOpenAPIResponse) => {
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
## [Update an API](https://docs.datadoghq.com/api/latest/api-management/#update-an-api)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/api-management/#update-an-api-v2)


**Note** : This endpoint is deprecated.
PUT https://api.ap1.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.ap2.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.datadoghq.eu/api/v2/apicatalog/api/{id}/openapihttps://api.ddog-gov.com/api/v2/apicatalog/api/{id}/openapihttps://api.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.us3.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.us5.datadoghq.com/api/v2/apicatalog/api/{id}/openapi
### Overview
Update information about a specific API. The given content will replace all API content of the given ID. The ID is returned by the create API, or can be found in the URL in the API catalog UI. This endpoint requires the `apm_api_catalog_write` permission.
OAuth apps require the `apm_api_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
ID of the API to modify
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


Expand All
Field
Type
Description
openapi_spec_file
binary
Binary `OpenAPI` spec file
```
{
  "openapi_spec_file": "string"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/api-management/#UpdateOpenAPI-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/api-management/#UpdateOpenAPI-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/api-management/#UpdateOpenAPI-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/api-management/#UpdateOpenAPI-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/api-management/#UpdateOpenAPI-429-v2)


API updated successfully
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


Response for `UpdateOpenAPI`.
Field
Type
Description
data
object
Data envelope for `UpdateOpenAPIResponse`.
attributes
object
Attributes for `UpdateOpenAPI`.
failed_endpoints
[object]
List of endpoints which couldn't be parsed.
method
string
The endpoint method.
path
string
The endpoint path.
id
uuid
API identifier.
```
{
  "data": {
    "attributes": {
      "failed_endpoints": [
        {
          "method": "string",
          "path": "string"
        }
      ]
    },
    "id": "90646597-5fdb-4a17-a240-647003f8c028"
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
API not found error
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/api-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/api-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/api-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/api-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/api-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/api-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/api-management/?code-lang=typescript)


#####  Update an API
Copy
```
                  # Path parameters  
export id="90646597-5fdb-4a17-a240-647003f8c028"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api/${id}/openapi" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F openapi_spec_file=@string  

                
```

#####  Update an API
```
"""
Update an API returns "API updated successfully" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = environ["MANAGED_API_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["update_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.update_open_api(
        id=MANAGED_API_DATA_ID,
        openapi_spec_file=open("openapi-spec.yaml", "rb"),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update an API
```
# Update an API returns "API updated successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = ENV["MANAGED_API_DATA_ID"]
opts = {
  openapi_spec_file: File.open("openapi-spec.yaml", "r"),
}
p api_instance.update_open_api(MANAGED_API_DATA_ID, opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update an API
```
// Update an API returns "API updated successfully" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "managed_api" in the system
	ManagedAPIDataID := uuid.MustParse(os.Getenv("MANAGED_API_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.UpdateOpenAPI(ctx, ManagedAPIDataID, *datadogV2.NewUpdateOpenAPIOptionalParameters().WithOpenapiSpecFile(func() io.Reader { fp, _ := os.Open("openapi-spec.yaml"); return fp }()))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.UpdateOpenAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.UpdateOpenAPI`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update an API
```
// Update an API returns "API updated successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import com.datadog.api.client.v2.api.ApiManagementApi.UpdateOpenAPIOptionalParameters;
import com.datadog.api.client.v2.model.UpdateOpenAPIResponse;
import java.io.File;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    // there is a valid "managed_api" in the system
    UUID MANAGED_API_DATA_ID = null;
    try {
      MANAGED_API_DATA_ID = UUID.fromString(System.getenv("MANAGED_API_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      UpdateOpenAPIResponse result =
          apiInstance.updateOpenAPI(
              MANAGED_API_DATA_ID,
              new UpdateOpenAPIOptionalParameters().openapiSpecFile(new File("openapi-spec.yaml")));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#updateOpenAPI");
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

#####  Update an API
```
// Update an API returns "API updated successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;
use datadog_api_client::datadogV2::api_api_management::UpdateOpenAPIOptionalParams;
use std::fs;

#[tokio::main]
async fn main() {
    // there is a valid "managed_api" in the system
    let managed_api_data_id = uuid::Uuid::parse_str(&std::env::var("MANAGED_API_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api
        .update_open_api(
            managed_api_data_id.clone(),
            UpdateOpenAPIOptionalParams::default()
                .openapi_spec_file(fs::read("openapi-spec.yaml").unwrap()),
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

#####  Update an API
```
/**
 * Update an API returns "API updated successfully" response
 */

import * as fs from "fs";
import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

// there is a valid "managed_api" in the system
const MANAGED_API_DATA_ID = process.env.MANAGED_API_DATA_ID as string;

const params: v2.APIManagementApiUpdateOpenAPIRequest = {
  id: MANAGED_API_DATA_ID,
  openapiSpecFile: {
    data: Buffer.from(fs.readFileSync("openapi-spec.yaml", "utf8")),
    name: "openapi-spec.yaml",
  },
};

apiInstance
  .updateOpenAPI(params)
  .then((data: v2.UpdateOpenAPIResponse) => {
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
## [Get an API](https://docs.datadoghq.com/api/latest/api-management/#get-an-api)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/api-management/#get-an-api-v2)


**Note** : This endpoint is deprecated.
GET https://api.ap1.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.ap2.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.datadoghq.eu/api/v2/apicatalog/api/{id}/openapihttps://api.ddog-gov.com/api/v2/apicatalog/api/{id}/openapihttps://api.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.us3.datadoghq.com/api/v2/apicatalog/api/{id}/openapihttps://api.us5.datadoghq.com/api/v2/apicatalog/api/{id}/openapi
### Overview
Retrieve information about a specific API in [OpenAPI](https://spec.openapis.org/oas/latest.html) format file. This endpoint requires the `apm_api_catalog_read` permission.
OAuth apps require the `apm_api_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
ID of the API to retrieve
### Response
  * [200](https://docs.datadoghq.com/api/latest/api-management/#GetOpenAPI-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/api-management/#GetOpenAPI-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/api-management/#GetOpenAPI-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/api-management/#GetOpenAPI-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/api-management/#GetOpenAPI-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
API not found error
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/api-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/api-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/api-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/api-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/api-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/api-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/api-management/?code-lang=typescript)


#####  Get an API
Copy
```
                  # Path parameters  
export id="90646597-5fdb-4a17-a240-647003f8c028"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api/${id}/openapi" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an API
```
"""
Get an API returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = environ["MANAGED_API_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.get_open_api(
        id=MANAGED_API_DATA_ID,
    )

    print(response.read())

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get an API
```
# Get an API returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = ENV["MANAGED_API_DATA_ID"]
p api_instance.get_open_api(MANAGED_API_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get an API
```
// Get an API returns "OK" response

package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "managed_api" in the system
	ManagedAPIDataID := uuid.MustParse(os.Getenv("MANAGED_API_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.GetOpenAPI(ctx, ManagedAPIDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.GetOpenAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := ioutil.ReadAll(resp)
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.GetOpenAPI`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get an API
```
// Get an API returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import java.io.File;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    // there is a valid "managed_api" in the system
    UUID MANAGED_API_DATA_ID = null;
    try {
      MANAGED_API_DATA_ID = UUID.fromString(System.getenv("MANAGED_API_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      File result = apiInstance.getOpenAPI(MANAGED_API_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#getOpenAPI");
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

#####  Get an API
```
// Get an API returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "managed_api" in the system
    let managed_api_data_id = uuid::Uuid::parse_str(&std::env::var("MANAGED_API_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api.get_open_api(managed_api_data_id.clone()).await;
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

#####  Get an API
```
/**
 * Get an API returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

// there is a valid "managed_api" in the system
const MANAGED_API_DATA_ID = process.env.MANAGED_API_DATA_ID as string;

const params: v2.APIManagementApiGetOpenAPIRequest = {
  id: MANAGED_API_DATA_ID,
};

apiInstance
  .getOpenAPI(params)
  .then((data: client.HttpFile) => {
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
## [List APIs](https://docs.datadoghq.com/api/latest/api-management/#list-apis)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/api-management/#list-apis-v2)


**Note** : This endpoint is deprecated.
GET https://api.ap1.datadoghq.com/api/v2/apicatalog/apihttps://api.ap2.datadoghq.com/api/v2/apicatalog/apihttps://api.datadoghq.eu/api/v2/apicatalog/apihttps://api.ddog-gov.com/api/v2/apicatalog/apihttps://api.datadoghq.com/api/v2/apicatalog/apihttps://api.us3.datadoghq.com/api/v2/apicatalog/apihttps://api.us5.datadoghq.com/api/v2/apicatalog/api
### Overview
List APIs and their IDs. This endpoint requires the `apm_api_catalog_read` permission.
OAuth apps require the `apm_api_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
query
string
Filter APIs by name
page[limit]
integer
Number of items per page.
page[offset]
integer
Offset for pagination.
### Response
  * [200](https://docs.datadoghq.com/api/latest/api-management/#ListAPIs-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/api-management/#ListAPIs-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/api-management/#ListAPIs-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/api-management/#ListAPIs-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


Response for `ListAPIs`.
Field
Type
Description
data
[object]
List of API items.
attributes
object
Attributes for `ListAPIsResponseData`.
name
string
API name.
id
uuid
API identifier.
meta
object
Metadata for `ListAPIsResponse`.
pagination
object
Pagination metadata information for `ListAPIsResponse`.
limit
int64
Number of items in the current page.
offset
int64
Offset for pagination.
total_count
int64
Total number of items.
```
{
  "data": [
    {
      "attributes": {
        "name": "Payments API"
      },
      "id": "90646597-5fdb-4a17-a240-647003f8c028"
    }
  ],
  "meta": {
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total_count": 35
    }
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/api-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/api-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/api-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/api-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/api-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/api-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/api-management/?code-lang=typescript)


#####  List APIs
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List APIs
```
"""
List APIs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

configuration = Configuration()
configuration.unstable_operations["list_apis"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.list_apis()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List APIs
```
# List APIs returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_apis".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new
p api_instance.list_apis()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List APIs
```
// List APIs returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListAPIs", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.ListAPIs(ctx, *datadogV2.NewListAPIsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.ListAPIs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.ListAPIs`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List APIs
```
// List APIs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import com.datadog.api.client.v2.model.ListAPIsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listAPIs", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    try {
      ListAPIsResponse result = apiInstance.listAPIs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#listAPIs");
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

#####  List APIs
```
// List APIs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;
use datadog_api_client::datadogV2::api_api_management::ListAPIsOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListAPIs", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api.list_apis(ListAPIsOptionalParams::default()).await;
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

#####  List APIs
```
/**
 * List APIs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listAPIs"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

apiInstance
  .listAPIs()
  .then((data: v2.ListAPIsResponse) => {
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
## [Delete an API](https://docs.datadoghq.com/api/latest/api-management/#delete-an-api)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/api-management/#delete-an-api-v2)


**Note** : This endpoint is deprecated.
DELETE https://api.ap1.datadoghq.com/api/v2/apicatalog/api/{id}https://api.ap2.datadoghq.com/api/v2/apicatalog/api/{id}https://api.datadoghq.eu/api/v2/apicatalog/api/{id}https://api.ddog-gov.com/api/v2/apicatalog/api/{id}https://api.datadoghq.com/api/v2/apicatalog/api/{id}https://api.us3.datadoghq.com/api/v2/apicatalog/api/{id}https://api.us5.datadoghq.com/api/v2/apicatalog/api/{id}
### Overview
Delete a specific API by ID. This endpoint requires the `apm_api_catalog_write` permission.
OAuth apps require the `apm_api_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
ID of the API to delete
### Response
  * [204](https://docs.datadoghq.com/api/latest/api-management/#DeleteOpenAPI-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/api-management/#DeleteOpenAPI-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/api-management/#DeleteOpenAPI-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/api-management/#DeleteOpenAPI-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/api-management/#DeleteOpenAPI-429-v2)


API deleted successfully
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
API not found error
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/api-management/)
  * [Example](https://docs.datadoghq.com/api/latest/api-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/api-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/api-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/api-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/api-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/api-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/api-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/api-management/?code-lang=typescript)


#####  Delete an API
Copy
```
                  # Path parameters  
export id="90646597-5fdb-4a17-a240-647003f8c028"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an API
```
"""
Delete an API returns "API deleted successfully" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = environ["MANAGED_API_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    api_instance.delete_open_api(
        id=MANAGED_API_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an API
```
# Delete an API returns "API deleted successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = ENV["MANAGED_API_DATA_ID"]
api_instance.delete_open_api(MANAGED_API_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an API
```
// Delete an API returns "API deleted successfully" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "managed_api" in the system
	ManagedAPIDataID := uuid.MustParse(os.Getenv("MANAGED_API_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	r, err := api.DeleteOpenAPI(ctx, ManagedAPIDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.DeleteOpenAPI`: %v\n", err)
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

#####  Delete an API
```
// Delete an API returns "API deleted successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    // there is a valid "managed_api" in the system
    UUID MANAGED_API_DATA_ID = null;
    try {
      MANAGED_API_DATA_ID = UUID.fromString(System.getenv("MANAGED_API_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      apiInstance.deleteOpenAPI(MANAGED_API_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#deleteOpenAPI");
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

#####  Delete an API
```
// Delete an API returns "API deleted successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "managed_api" in the system
    let managed_api_data_id = uuid::Uuid::parse_str(&std::env::var("MANAGED_API_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api.delete_open_api(managed_api_data_id.clone()).await;
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

#####  Delete an API
```
/**
 * Delete an API returns "API deleted successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

// there is a valid "managed_api" in the system
const MANAGED_API_DATA_ID = process.env.MANAGED_API_DATA_ID as string;

const params: v2.APIManagementApiDeleteOpenAPIRequest = {
  id: MANAGED_API_DATA_ID,
};

apiInstance
  .deleteOpenAPI(params)
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4bae82c7-cbcb-45c6-80df-2d17389f4dca&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4e2f3191-aad5-4ec4-a825-57506f835088&pt=API%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapi-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4bae82c7-cbcb-45c6-80df-2d17389f4dca&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4e2f3191-aad5-4ec4-a825-57506f835088&pt=API%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapi-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=965e7936-3e7d-410e-898c-bfb0d9329fdf&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=API%20Management&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapi-management%2F&r=&lt=13756&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=15729)
