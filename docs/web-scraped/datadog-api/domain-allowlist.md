# Source: https://docs.datadoghq.com/api/latest/domain-allowlist

# Domain Allowlist
Configure your Datadog Email Domain Allowlist directly through the Datadog API. The Email Domain Allowlist controls the domains that certain datadog emails can be sent to. For more information, see the [Domain Allowlist docs page](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist)
## [Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist-v2)


GET https://api.ap1.datadoghq.com/api/v2/domain_allowlisthttps://api.ap2.datadoghq.com/api/v2/domain_allowlisthttps://api.datadoghq.eu/api/v2/domain_allowlisthttps://api.ddog-gov.com/api/v2/domain_allowlisthttps://api.datadoghq.com/api/v2/domain_allowlisthttps://api.us3.datadoghq.com/api/v2/domain_allowlisthttps://api.us5.datadoghq.com/api/v2/domain_allowlist
### Overview
Get the domain allowlist for an organization. This endpoint requires any of the following permissions:
* `org_management`
* `monitors_write`
* `generate_dashboard_reports`
* `generate_log_reports`
* `manage_log_reports`
  

OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#domain-allowlist) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/domain-allowlist/#GetDomainAllowlist-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/domain-allowlist/#GetDomainAllowlist-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/domain-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/domain-allowlist/)


Response containing information about the email domain allowlist.
Field
Type
Description
data
object
The email domain allowlist response for an org.
attributes
object
The details of the email domain allowlist.
domains
[string]
The list of domains in the email domain allowlist.
enabled
boolean
Whether the email domain allowlist is enabled for the org.
id
string
The unique identifier of the org.
type [_required_]
enum
Email domain allowlist allowlist type. Allowed enum values: `domain_allowlist`
default: `domain_allowlist`
```
{
  "data": {
    "attributes": {
      "domains": [],
      "enabled": false
    },
    "id": "string",
    "type": "domain_allowlist"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/domain-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/domain-allowlist/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=typescript)


#####  Get Domain Allowlist
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/domain_allowlist" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Domain Allowlist
```
"""
Get Domain Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.domain_allowlist_api import DomainAllowlistApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DomainAllowlistApi(api_client)
    response = api_instance.get_domain_allowlist()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get Domain Allowlist
```
# Get Domain Allowlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DomainAllowlistAPI.new
p api_instance.get_domain_allowlist()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get Domain Allowlist
```
// Get Domain Allowlist returns "OK" response

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
	api := datadogV2.NewDomainAllowlistApi(apiClient)
	resp, r, err := api.GetDomainAllowlist(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainAllowlistApi.GetDomainAllowlist`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DomainAllowlistApi.GetDomainAllowlist`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get Domain Allowlist
```
// Get Domain Allowlist returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DomainAllowlistApi;
import com.datadog.api.client.v2.model.DomainAllowlistResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DomainAllowlistApi apiInstance = new DomainAllowlistApi(defaultClient);

    try {
      DomainAllowlistResponse result = apiInstance.getDomainAllowlist();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainAllowlistApi#getDomainAllowlist");
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

#####  Get Domain Allowlist
```
// Get Domain Allowlist returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_domain_allowlist::DomainAllowlistAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DomainAllowlistAPI::with_config(configuration);
    let resp = api.get_domain_allowlist().await;
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

#####  Get Domain Allowlist
```
/**
 * Get Domain Allowlist returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DomainAllowlistApi(configuration);

apiInstance
  .getDomainAllowlist()
  .then((data: v2.DomainAllowlistResponse) => {
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
## [Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/domain_allowlisthttps://api.ap2.datadoghq.com/api/v2/domain_allowlisthttps://api.datadoghq.eu/api/v2/domain_allowlisthttps://api.ddog-gov.com/api/v2/domain_allowlisthttps://api.datadoghq.com/api/v2/domain_allowlisthttps://api.us3.datadoghq.com/api/v2/domain_allowlisthttps://api.us5.datadoghq.com/api/v2/domain_allowlist
### Overview
Update the domain allowlist for an organization. This endpoint requires any of the following permissions:
* `org_management`
* `monitors_write`
* `generate_dashboard_reports`
* `generate_log_reports`
* `manage_log_reports`
  

OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#domain-allowlist) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/domain-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/domain-allowlist/)


Field
Type
Description
data [_required_]
object
The email domain allowlist for an org.
attributes
object
The details of the email domain allowlist.
domains
[string]
The list of domains in the email domain allowlist.
enabled
boolean
Whether the email domain allowlist is enabled for the org.
id
string
The unique identifier of the org.
type [_required_]
enum
Email domain allowlist allowlist type. Allowed enum values: `domain_allowlist`
default: `domain_allowlist`
```
{
  "data": {
    "attributes": {
      "domains": [
        "@static-test-domain.test"
      ],
      "enabled": false
    },
    "type": "domain_allowlist"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/domain-allowlist/#PatchDomainAllowlist-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/domain-allowlist/#PatchDomainAllowlist-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/domain-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/domain-allowlist/)


Response containing information about the email domain allowlist.
Field
Type
Description
data
object
The email domain allowlist response for an org.
attributes
object
The details of the email domain allowlist.
domains
[string]
The list of domains in the email domain allowlist.
enabled
boolean
Whether the email domain allowlist is enabled for the org.
id
string
The unique identifier of the org.
type [_required_]
enum
Email domain allowlist allowlist type. Allowed enum values: `domain_allowlist`
default: `domain_allowlist`
```
{
  "data": {
    "attributes": {
      "domains": [],
      "enabled": false
    },
    "id": "string",
    "type": "domain_allowlist"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/domain-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/domain-allowlist/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/domain-allowlist/?code-lang=typescript)


#####  Sets Domain Allowlist returns "OK" response
Copy
```
                          # Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/domain_allowlist" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "domains": [
        "@static-test-domain.test"
      ],
      "enabled": false
    },
    "type": "domain_allowlist"
  }
}
EOF  

                        
```

#####  Sets Domain Allowlist returns "OK" response
```
// Sets Domain Allowlist returns "OK" response

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
	body := datadogV2.DomainAllowlistRequest{
		Data: datadogV2.DomainAllowlist{
			Attributes: &datadogV2.DomainAllowlistAttributes{
				Domains: []string{
					"@static-test-domain.test",
				},
				Enabled: datadog.PtrBool(false),
			},
			Type: datadogV2.DOMAINALLOWLISTTYPE_DOMAIN_ALLOWLIST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDomainAllowlistApi(apiClient)
	resp, r, err := api.PatchDomainAllowlist(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainAllowlistApi.PatchDomainAllowlist`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DomainAllowlistApi.PatchDomainAllowlist`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Sets Domain Allowlist returns "OK" response
```
// Sets Domain Allowlist returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DomainAllowlistApi;
import com.datadog.api.client.v2.model.DomainAllowlist;
import com.datadog.api.client.v2.model.DomainAllowlistAttributes;
import com.datadog.api.client.v2.model.DomainAllowlistRequest;
import com.datadog.api.client.v2.model.DomainAllowlistResponse;
import com.datadog.api.client.v2.model.DomainAllowlistType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DomainAllowlistApi apiInstance = new DomainAllowlistApi(defaultClient);

    DomainAllowlistRequest body =
        new DomainAllowlistRequest()
            .data(
                new DomainAllowlist()
                    .attributes(
                        new DomainAllowlistAttributes()
                            .domains(Collections.singletonList("@static-test-domain.test"))
                            .enabled(false))
                    .type(DomainAllowlistType.DOMAIN_ALLOWLIST));

    try {
      DomainAllowlistResponse result = apiInstance.patchDomainAllowlist(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainAllowlistApi#patchDomainAllowlist");
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

#####  Sets Domain Allowlist returns "OK" response
```
"""
Sets Domain Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.domain_allowlist_api import DomainAllowlistApi
from datadog_api_client.v2.model.domain_allowlist import DomainAllowlist
from datadog_api_client.v2.model.domain_allowlist_attributes import DomainAllowlistAttributes
from datadog_api_client.v2.model.domain_allowlist_request import DomainAllowlistRequest
from datadog_api_client.v2.model.domain_allowlist_type import DomainAllowlistType

body = DomainAllowlistRequest(
    data=DomainAllowlist(
        attributes=DomainAllowlistAttributes(
            domains=[
                "@static-test-domain.test",
            ],
            enabled=False,
        ),
        type=DomainAllowlistType.DOMAIN_ALLOWLIST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DomainAllowlistApi(api_client)
    response = api_instance.patch_domain_allowlist(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Sets Domain Allowlist returns "OK" response
```
# Sets Domain Allowlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DomainAllowlistAPI.new

body = DatadogAPIClient::V2::DomainAllowlistRequest.new({
  data: DatadogAPIClient::V2::DomainAllowlist.new({
    attributes: DatadogAPIClient::V2::DomainAllowlistAttributes.new({
      domains: [
        "@static-test-domain.test",
      ],
      enabled: false,
    }),
    type: DatadogAPIClient::V2::DomainAllowlistType::DOMAIN_ALLOWLIST,
  }),
})
p api_instance.patch_domain_allowlist(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Sets Domain Allowlist returns "OK" response
```
// Sets Domain Allowlist returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_domain_allowlist::DomainAllowlistAPI;
use datadog_api_client::datadogV2::model::DomainAllowlist;
use datadog_api_client::datadogV2::model::DomainAllowlistAttributes;
use datadog_api_client::datadogV2::model::DomainAllowlistRequest;
use datadog_api_client::datadogV2::model::DomainAllowlistType;

#[tokio::main]
async fn main() {
    let body = DomainAllowlistRequest::new(
        DomainAllowlist::new(DomainAllowlistType::DOMAIN_ALLOWLIST).attributes(
            DomainAllowlistAttributes::new()
                .domains(vec!["@static-test-domain.test".to_string()])
                .enabled(false),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = DomainAllowlistAPI::with_config(configuration);
    let resp = api.patch_domain_allowlist(body).await;
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

#####  Sets Domain Allowlist returns "OK" response
```
/**
 * Sets Domain Allowlist returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DomainAllowlistApi(configuration);

const params: v2.DomainAllowlistApiPatchDomainAllowlistRequest = {
  body: {
    data: {
      attributes: {
        domains: ["@static-test-domain.test"],
        enabled: false,
      },
      type: "domain_allowlist",
    },
  },
};

apiInstance
  .patchDomainAllowlist(params)
  .then((data: v2.DomainAllowlistResponse) => {
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
![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=3ba173a6-0943-4521-bcc0-4243e97c10ea&bo=1&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Domain%20Allowlist&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdomain-allowlist%2F&r=&evt=pageLoad&sv=2&cdb=AQAA&rn=181359)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0fd7b951-ad2e-465d-a338-ca253de7a4c0&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2cbed7a6-b412-4e83-88cb-e90c53ffa5bf&pt=Domain%20Allowlist&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdomain-allowlist%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0fd7b951-ad2e-465d-a338-ca253de7a4c0&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2cbed7a6-b412-4e83-88cb-e90c53ffa5bf&pt=Domain%20Allowlist&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdomain-allowlist%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
