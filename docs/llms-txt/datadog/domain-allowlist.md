# Source: https://docs.datadoghq.com/api/latest/domain-allowlist.md

---
title: Domain Allowlist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Domain Allowlist
---

# Domain Allowlist

Configure your Datadog Email Domain Allowlist directly through the Datadog API. The Email Domain Allowlist controls the domains that certain datadog emails can be sent to. For more information, see the [Domain Allowlist docs page](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist)

## Get Domain Allowlist{% #get-domain-allowlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/domain_allowlist |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/domain_allowlist |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/domain_allowlist      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/domain_allowlist      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/domain_allowlist     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/domain_allowlist |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/domain_allowlist |

### Overview

Get the domain allowlist for an organization. This endpoint requires any of the following permissions:
`org_management``monitors_write``generate_dashboard_reports``generate_log_reports``manage_log_reports`


OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#domain-allowlist) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about the email domain allowlist.

| Parent field | Field                  | Type     | Description                                                                    |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------------------ |
|              | data                   | object   | The email domain allowlist response for an org.                                |
| data         | attributes             | object   | The details of the email domain allowlist.                                     |
| attributes   | domains                | [string] | The list of domains in the email domain allowlist.                             |
| attributes   | enabled                | boolean  | Whether the email domain allowlist is enabled for the org.                     |
| data         | id                     | string   | The unique identifier of the org.                                              |
| data         | type [*required*] | enum     | Email domain allowlist allowlist type. Allowed enum values: `domain_allowlist` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/domain_allowlist" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get Domain Allowlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DomainAllowlistAPI.new
p api_instance.get_domain_allowlist()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Sets Domain Allowlist{% #sets-domain-allowlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/domain_allowlist |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/domain_allowlist |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/domain_allowlist      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/domain_allowlist      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/domain_allowlist     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/domain_allowlist |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/domain_allowlist |

### Overview

Update the domain allowlist for an organization. This endpoint requires any of the following permissions:
`org_management``monitors_write``generate_dashboard_reports``generate_log_reports``manage_log_reports`


OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#domain-allowlist) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                    |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------------------ |
|              | data [*required*] | object   | The email domain allowlist for an org.                                         |
| data         | attributes             | object   | The details of the email domain allowlist.                                     |
| attributes   | domains                | [string] | The list of domains in the email domain allowlist.                             |
| attributes   | enabled                | boolean  | Whether the email domain allowlist is enabled for the org.                     |
| data         | id                     | string   | The unique identifier of the org.                                              |
| data         | type [*required*] | enum     | Email domain allowlist allowlist type. Allowed enum values: `domain_allowlist` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about the email domain allowlist.

| Parent field | Field                  | Type     | Description                                                                    |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------------------ |
|              | data                   | object   | The email domain allowlist response for an org.                                |
| data         | attributes             | object   | The details of the email domain allowlist.                                     |
| attributes   | domains                | [string] | The list of domains in the email domain allowlist.                             |
| attributes   | enabled                | boolean  | Whether the email domain allowlist is enabled for the org.                     |
| data         | id                     | string   | The unique identifier of the org.                                              |
| data         | type [*required*] | enum     | Email domain allowlist allowlist type. Allowed enum values: `domain_allowlist` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/domain_allowlist" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
