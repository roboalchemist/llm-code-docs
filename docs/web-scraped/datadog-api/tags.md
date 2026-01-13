# Source: https://docs.datadoghq.com/api/latest/tags/

# Tags
The tag endpoint allows you to assign tags to hosts, for example: `role:database`. Those tags are applied to all metrics sent by the host. Refer to hosts by name (`yourhost.example.com`) when fetching and applying tags to a particular host.
The component of your infrastructure responsible for a tag is identified by a source. For example, some valid sources include nagios, hudson, jenkins, users, feed, chef, puppet, git, bitbucket, fabric, capistrano, etc.
Read more about tags on [Getting Started with Tags](https://docs.datadoghq.com/getting_started/tagging/).
## [Get Tags](https://docs.datadoghq.com/api/latest/tags/#get-tags)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/tags/#get-tags-v1)


GET https://api.ap1.datadoghq.com/api/v1/tags/hostshttps://api.ap2.datadoghq.com/api/v1/tags/hostshttps://api.datadoghq.eu/api/v1/tags/hostshttps://api.ddog-gov.com/api/v1/tags/hostshttps://api.datadoghq.com/api/v1/tags/hostshttps://api.us3.datadoghq.com/api/v1/tags/hostshttps://api.us5.datadoghq.com/api/v1/tags/hosts
### Overview
Return a mapping of tags to hosts for your whole infrastructure.
### Arguments
#### Query Strings
Name
Type
Description
source
string
When specified, filters host list to those tags with the specified source.
### Response
  * [200](https://docs.datadoghq.com/api/latest/tags/#ListHostTags-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/tags/#ListHostTags-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/tags/#ListHostTags-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/tags/#ListHostTags-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


In this object, the key is the tag, the value is a list of host names that are reporting that tag.
Field
Type
Description
tags
object
A list of tags to apply to the host.
<any-key>
[string]
A list of additional properties for tags.
```
{
  "tags": {
    "<any-key>": [
      "test.metric.host"
    ]
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/tags/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/tags/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/tags/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/tags/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/tags/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/tags/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/tags/?code-lang=typescript)


#####  Get Tags
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Tags
```
"""
Get Tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.list_host_tags()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get Tags
```
# Get Tags returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new
p api_instance.list_host_tags()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get Tags
```
// Get Tags returns "OK" response

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
	api := datadogV1.NewTagsApi(apiClient)
	resp, r, err := api.ListHostTags(ctx, *datadogV1.NewListHostTagsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.ListHostTags`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `TagsApi.ListHostTags`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get Tags
```
// Get Tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.TagToHosts;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    try {
      TagToHosts result = apiInstance.listHostTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#listHostTags");
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

#####  Get Tags
```
// Get Tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::ListHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .list_host_tags(ListHostTagsOptionalParams::default())
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

#####  Get Tags
```
/**
 * Get Tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

apiInstance
  .listHostTags()
  .then((data: v1.TagToHosts) => {
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
## [Get host tags](https://docs.datadoghq.com/api/latest/tags/#get-host-tags)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/tags/#get-host-tags-v1)


GET https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name}
### Overview
Return the list of tags that apply to a given host.
### Arguments
#### Path Parameters
Name
Type
Description
host_name [_required_]
string
When specified, filters list of tags to those tags with the specified source.
#### Query Strings
Name
Type
Description
source
string
Source to filter.
### Response
  * [200](https://docs.datadoghq.com/api/latest/tags/#GetHostTags-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/tags/#GetHostTags-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/tags/#GetHostTags-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/tags/#GetHostTags-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


Set of tags to associate with your host.
Expand All
Field
Type
Description
host
string
Your host name.
tags
[string]
A list of tags to apply to the host.
```
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/tags/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/tags/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/tags/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/tags/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/tags/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/tags/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/tags/?code-lang=typescript)


#####  Get host tags
Copy
```
                  # Path parameters  
export host_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get host tags
```
"""
Get host tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.get_host_tags(
        host_name="host_name",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get host tags
```
# Get host tags returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new
p api_instance.get_host_tags("host_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get host tags
```
// Get host tags returns "OK" response

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
	api := datadogV1.NewTagsApi(apiClient)
	resp, r, err := api.GetHostTags(ctx, "host_name", *datadogV1.NewGetHostTagsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.GetHostTags`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `TagsApi.GetHostTags`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get host tags
```
// Get host tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.HostTags;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    try {
      HostTags result = apiInstance.getHostTags("host_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#getHostTags");
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

#####  Get host tags
```
// Get host tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::GetHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .get_host_tags(
            "host_name".to_string(),
            GetHostTagsOptionalParams::default(),
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

#####  Get host tags
```
/**
 * Get host tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiGetHostTagsRequest = {
  hostName: "host_name",
};

apiInstance
  .getHostTags(params)
  .then((data: v1.HostTags) => {
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
## [Add tags to a host](https://docs.datadoghq.com/api/latest/tags/#add-tags-to-a-host)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/tags/#add-tags-to-a-host-v1)


POST https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name}
### Overview
This endpoint allows you to add new tags to a host, optionally specifying where these tags come from.
### Arguments
#### Path Parameters
Name
Type
Description
host_name [_required_]
string
This endpoint allows you to add new tags to a host, optionally specifying where the tags came from.
#### Query Strings
Name
Type
Description
source
string
The source of the tags. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
### Request
#### Body Data (required)
Update host tags request body.
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


Expand All
Field
Type
Description
host
string
Your host name.
tags
[string]
A list of tags to apply to the host.
```
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/tags/#CreateHostTags-201-v1)
  * [403](https://docs.datadoghq.com/api/latest/tags/#CreateHostTags-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/tags/#CreateHostTags-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/tags/#CreateHostTags-429-v1)


Created
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


Set of tags to associate with your host.
Expand All
Field
Type
Description
host
string
Your host name.
tags
[string]
A list of tags to apply to the host.
```
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/tags/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/tags/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/tags/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/tags/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/tags/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/tags/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/tags/?code-lang=typescript)


#####  Add tags to a host
Copy
```
                  # Path parameters  
export host_name="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Add tags to a host
```
"""
Add tags to a host returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi
from datadog_api_client.v1.model.host_tags import HostTags

body = HostTags(
    host="test.host",
    tags=[
        "environment:production",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.create_host_tags(host_name="host_name", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add tags to a host
```
# Add tags to a host returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new

body = DatadogAPIClient::V1::HostTags.new({
  host: "test.host",
  tags: [
    "environment:production",
  ],
})
p api_instance.create_host_tags("host_name", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add tags to a host
```
// Add tags to a host returns "Created" response

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
	body := datadogV1.HostTags{
		Host: datadog.PtrString("test.host"),
		Tags: []string{
			"environment:production",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewTagsApi(apiClient)
	resp, r, err := api.CreateHostTags(ctx, "host_name", body, *datadogV1.NewCreateHostTagsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.CreateHostTags`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `TagsApi.CreateHostTags`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add tags to a host
```
// Add tags to a host returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.HostTags;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    HostTags body =
        new HostTags().host("test.host").tags(Collections.singletonList("environment:production"));

    try {
      HostTags result = apiInstance.createHostTags("host_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#createHostTags");
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

#####  Add tags to a host
```
// Add tags to a host returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::CreateHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;
use datadog_api_client::datadogV1::model::HostTags;

#[tokio::main]
async fn main() {
    let body = HostTags::new()
        .host("test.host".to_string())
        .tags(vec!["environment:production".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .create_host_tags(
            "host_name".to_string(),
            body,
            CreateHostTagsOptionalParams::default(),
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

#####  Add tags to a host
```
/**
 * Add tags to a host returns "Created" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiCreateHostTagsRequest = {
  body: {
    host: "test.host",
    tags: ["environment:production"],
  },
  hostName: "host_name",
};

apiInstance
  .createHostTags(params)
  .then((data: v1.HostTags) => {
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
## [Update host tags](https://docs.datadoghq.com/api/latest/tags/#update-host-tags)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/tags/#update-host-tags-v1)


PUT https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name}
### Overview
This endpoint allows you to update/replace all tags in an integration source with those supplied in the request.
### Arguments
#### Path Parameters
Name
Type
Description
host_name [_required_]
string
This endpoint allows you to update/replace all in an integration source with those supplied in the request.
#### Query Strings
Name
Type
Description
source
string
The source of the tags (for example chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value)
### Request
#### Body Data (required)
Add tags to host
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


Expand All
Field
Type
Description
host
string
Your host name.
tags
[string]
A list of tags to apply to the host.
```
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/tags/#UpdateHostTags-201-v1)
  * [403](https://docs.datadoghq.com/api/latest/tags/#UpdateHostTags-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/tags/#UpdateHostTags-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/tags/#UpdateHostTags-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


Set of tags to associate with your host.
Expand All
Field
Type
Description
host
string
Your host name.
tags
[string]
A list of tags to apply to the host.
```
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/tags/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/tags/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/tags/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/tags/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/tags/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/tags/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/tags/?code-lang=typescript)


#####  Update host tags
Copy
```
                  # Path parameters  
export host_name="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Update host tags
```
"""
Update host tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi
from datadog_api_client.v1.model.host_tags import HostTags

body = HostTags(
    host="test.host",
    tags=[
        "environment:production",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.update_host_tags(host_name="host_name", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update host tags
```
# Update host tags returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new

body = DatadogAPIClient::V1::HostTags.new({
  host: "test.host",
  tags: [
    "environment:production",
  ],
})
p api_instance.update_host_tags("host_name", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update host tags
```
// Update host tags returns "OK" response

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
	body := datadogV1.HostTags{
		Host: datadog.PtrString("test.host"),
		Tags: []string{
			"environment:production",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewTagsApi(apiClient)
	resp, r, err := api.UpdateHostTags(ctx, "host_name", body, *datadogV1.NewUpdateHostTagsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.UpdateHostTags`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `TagsApi.UpdateHostTags`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update host tags
```
// Update host tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.HostTags;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    HostTags body =
        new HostTags().host("test.host").tags(Collections.singletonList("environment:production"));

    try {
      HostTags result = apiInstance.updateHostTags("host_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#updateHostTags");
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

#####  Update host tags
```
// Update host tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::TagsAPI;
use datadog_api_client::datadogV1::api_tags::UpdateHostTagsOptionalParams;
use datadog_api_client::datadogV1::model::HostTags;

#[tokio::main]
async fn main() {
    let body = HostTags::new()
        .host("test.host".to_string())
        .tags(vec!["environment:production".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .update_host_tags(
            "host_name".to_string(),
            body,
            UpdateHostTagsOptionalParams::default(),
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

#####  Update host tags
```
/**
 * Update host tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiUpdateHostTagsRequest = {
  body: {
    host: "test.host",
    tags: ["environment:production"],
  },
  hostName: "host_name",
};

apiInstance
  .updateHostTags(params)
  .then((data: v1.HostTags) => {
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
## [Remove host tags](https://docs.datadoghq.com/api/latest/tags/#remove-host-tags)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/tags/#remove-host-tags-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}https://api.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name}https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name}
### Overview
This endpoint allows you to remove all user-assigned tags for a single host.
### Arguments
#### Path Parameters
Name
Type
Description
host_name [_required_]
string
This endpoint allows you to remove all user-assigned tags for a single host.
#### Query Strings
Name
Type
Description
source
string
The source of the tags (for example chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
### Response
  * [204](https://docs.datadoghq.com/api/latest/tags/#DeleteHostTags-204-v1)
  * [403](https://docs.datadoghq.com/api/latest/tags/#DeleteHostTags-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/tags/#DeleteHostTags-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/tags/#DeleteHostTags-429-v1)


OK
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Model](https://docs.datadoghq.com/api/latest/tags/)
  * [Example](https://docs.datadoghq.com/api/latest/tags/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/tags/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/tags/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/tags/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/tags/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/tags/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/tags/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/tags/?code-lang=typescript)


#####  Remove host tags
Copy
```
                  # Path parameters  
export host_name="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove host tags
```
"""
Remove host tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    api_instance.delete_host_tags(
        host_name="host_name",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Remove host tags
```
# Remove host tags returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new
api_instance.delete_host_tags("host_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Remove host tags
```
// Remove host tags returns "OK" response

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
	api := datadogV1.NewTagsApi(apiClient)
	r, err := api.DeleteHostTags(ctx, "host_name", *datadogV1.NewDeleteHostTagsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.DeleteHostTags`: %v\n", err)
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

#####  Remove host tags
```
// Remove host tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    try {
      apiInstance.deleteHostTags("host_name");
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#deleteHostTags");
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

#####  Remove host tags
```
// Remove host tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::DeleteHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .delete_host_tags(
            "host_name".to_string(),
            DeleteHostTagsOptionalParams::default(),
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

#####  Remove host tags
```
/**
 * Remove host tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiDeleteHostTagsRequest = {
  hostName: "host_name",
};

apiInstance
  .deleteHostTags(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=650750b7-42d4-4040-bdd0-fc2d10637412&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=49d6692c-c019-4cb9-9df2-4d3379cac334&pt=Tags&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ftags%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=650750b7-42d4-4040-bdd0-fc2d10637412&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=49d6692c-c019-4cb9-9df2-4d3379cac334&pt=Tags&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ftags%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=b8735af3-5db4-4602-b2a2-a67515a5a379&bo=2&sid=c4ba0d50f0bf11f09afde9c0412ba014&vid=c4ba67e0f0bf11f099fcdb9b6c7a6b3e&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Tags&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ftags%2F&r=&lt=988&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=183701)
