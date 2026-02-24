# Source: https://docs.datadoghq.com/api/latest/authn-mappings.md

---
title: AuthN Mappings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > AuthN Mappings
---

# AuthN Mappings

[The AuthN Mappings API](https://docs.datadoghq.com/account_management/authn_mapping/?tab=example) is used to automatically map groups of users to roles in Datadog using attributes sent from Identity Providers. Use these endpoints to manage your AuthN Mappings.

## Get an AuthN Mapping by UUID{% #get-an-authn-mapping-by-uuid %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/authn_mappings/{authn_mapping_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/authn_mappings/{authn_mapping_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |

### Overview

Get an AuthN Mapping specified by the AuthN Mapping UUID. This endpoint requires the `user_access_read` permission.

### Arguments

#### Path Parameters

| Name                               | Type   | Description                    |
| ---------------------------------- | ------ | ------------------------------ |
| authn_mapping_id [*required*] | string | The UUID of the AuthN Mapping. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
AuthN Mapping response from the API.

| Parent field             | Field                       | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                          | data                        | object          | The AuthN Mapping object returned by API.                                                                                                                                                                                                                                                     |
| data                     | attributes                  | object          | Attributes of AuthN Mapping.                                                                                                                                                                                                                                                                  |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| attributes               | created_at                  | date-time       | Creation time of the AuthN Mapping.                                                                                                                                                                                                                                                           |
| attributes               | modified_at                 | date-time       | Time of last AuthN Mapping modification.                                                                                                                                                                                                                                                      |
| attributes               | saml_assertion_attribute_id | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | id [*required*]        | string          | ID of the AuthN Mapping.                                                                                                                                                                                                                                                                      |
| data                     | relationships               | object          | All relationships associated with AuthN Mapping.                                                                                                                                                                                                                                              |
| relationships            | role                        | object          | Relationship to role.                                                                                                                                                                                                                                                                         |
| role                     | data                        | object          | Relationship to role object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| relationships            | saml_assertion_attribute    | object          | AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                                       |
| saml_assertion_attribute | data [*required*]      | object          | Data of AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                               |
| data                     | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| relationships            | team                        | object          | Relationship to team.                                                                                                                                                                                                                                                                         |
| team                     | data                        | object          | Relationship to Team object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the team.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |
| data                     | type [*required*]      | enum            | AuthN Mappings resource type. Allowed enum values: `authn_mappings`                                                                                                                                                                                                                           |
|                          | included                    | [ <oneOf>] | Included data in the AuthN Mapping response.                                                                                                                                                                                                                                                  |
| included                 | Option 1                    | object          | SAML assertion attribute.                                                                                                                                                                                                                                                                     |
| Option 1                 | attributes                  | object          | Key/Value pair of attributes used in SAML assertion attributes.                                                                                                                                                                                                                               |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| Option 1                 | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| Option 1                 | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| included                 | Option 2                    | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2                 | attributes                  | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes               | created_at                  | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes               | modified_at                 | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes               | name                        | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes               | receives_permissions_from   | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes               | user_count                  | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2                 | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2                 | relationships               | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships            | permissions                 | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions              | data                        | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data                     | id                          | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data                     | type                        | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2                 | type [*required*]      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included                 | Option 3                    | object          | Team.                                                                                                                                                                                                                                                                                         |
| Option 3                 | attributes                  | object          | Team attributes.                                                                                                                                                                                                                                                                              |
| attributes               | avatar                      | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                                                                                               |
| attributes               | banner                      | int64           | Banner selection for the team                                                                                                                                                                                                                                                                 |
| attributes               | handle                      | string          | The team's identifier                                                                                                                                                                                                                                                                         |
| attributes               | link_count                  | int32           | The number of links belonging to the team                                                                                                                                                                                                                                                     |
| attributes               | name                        | string          | The name of the team                                                                                                                                                                                                                                                                          |
| attributes               | summary                     | string          | A brief summary of the team, derived from the `description`                                                                                                                                                                                                                                   |
| attributes               | user_count                  | int32           | The number of users belonging to the team                                                                                                                                                                                                                                                     |
| Option 3                 | id                          | string          | The ID of the Team.                                                                                                                                                                                                                                                                           |
| Option 3                 | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development",
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "saml_assertion_attribute_id": "0"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
          "type": "roles"
        }
      },
      "saml_assertion_attribute": {
        "data": {
          "id": "0",
          "type": "saml_assertion_attributes"
        }
      },
      "team": {
        "data": {
          "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      }
    },
    "type": "authn_mappings"
  },
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport authn_mapping_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings/${authn_mapping_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get an AuthN Mapping by UUID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.get_authn_mapping(
        authn_mapping_id=AUTHN_MAPPING_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get an AuthN Mapping by UUID returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = ENV["AUTHN_MAPPING_DATA_ID"]
p api_instance.get_authn_mapping(AUTHN_MAPPING_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get an AuthN Mapping by UUID returns "OK" response

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
	// there is a valid "authn_mapping" in the system
	AuthnMappingDataID := os.Getenv("AUTHN_MAPPING_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.GetAuthNMapping(ctx, AuthnMappingDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.GetAuthNMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.GetAuthNMapping`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get an AuthN Mapping by UUID returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "authn_mapping" in the system
    String AUTHN_MAPPING_DATA_ID = System.getenv("AUTHN_MAPPING_DATA_ID");

    try {
      AuthNMappingResponse result = apiInstance.getAuthNMapping(AUTHN_MAPPING_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#getAuthNMapping");
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
// Get an AuthN Mapping by UUID returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "authn_mapping" in the system
    let authn_mapping_data_id = std::env::var("AUTHN_MAPPING_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api.get_authn_mapping(authn_mapping_data_id.clone()).await;
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
 * Get an AuthN Mapping by UUID returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "authn_mapping" in the system
const AUTHN_MAPPING_DATA_ID = process.env.AUTHN_MAPPING_DATA_ID as string;

const params: v2.AuthNMappingsApiGetAuthNMappingRequest = {
  authnMappingId: AUTHN_MAPPING_DATA_ID,
};

apiInstance
  .getAuthNMapping(params)
  .then((data: v2.AuthNMappingResponse) => {
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

## Edit an AuthN Mapping{% #edit-an-authn-mapping %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/authn_mappings/{authn_mapping_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/authn_mappings/{authn_mapping_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |

### Overview

Edit an AuthN Mapping. This endpoint requires the `user_access_manage` permission.

### Arguments

#### Path Parameters

| Name                               | Type   | Description                    |
| ---------------------------------- | ------ | ------------------------------ |
| authn_mapping_id [*required*] | string | The UUID of the AuthN Mapping. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                  | Type          | Description                                                                         |
| ------------- | ---------------------- | ------------- | ----------------------------------------------------------------------------------- |
|               | data [*required*] | object        | Data for updating an AuthN Mapping.                                                 |
| data          | attributes             | object        | Key/Value pair of attributes used for update request.                               |
| attributes    | attribute_key          | string        | Key portion of a key/value pair of the attribute sent from the Identity Provider.   |
| attributes    | attribute_value        | string        | Value portion of a key/value pair of the attribute sent from the Identity Provider. |
| data          | id [*required*]   | string        | ID of the AuthN Mapping.                                                            |
| data          | relationships          |  <oneOf> | Relationship of AuthN Mapping update object to a Role or Team.                      |
| relationships | Option 1               | object        | Relationship of AuthN Mapping to a Role.                                            |
| Option 1      | role [*required*] | object        | Relationship to role.                                                               |
| role          | data                   | object        | Relationship to role object.                                                        |
| data          | id                     | string        | The unique identifier of the role.                                                  |
| data          | type                   | enum          | Roles type. Allowed enum values: `roles`                                            |
| relationships | Option 2               | object        | Relationship of AuthN Mapping to a Team.                                            |
| Option 2      | team [*required*] | object        | Relationship to team.                                                               |
| team          | data                   | object        | Relationship to Team object.                                                        |
| data          | id                     | string        | The unique identifier of the team.                                                  |
| data          | type                   | enum          | Team type Allowed enum values: `team`                                               |
| data          | type [*required*] | enum          | AuthN Mappings resource type. Allowed enum values: `authn_mappings`                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
AuthN Mapping response from the API.

| Parent field             | Field                       | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                          | data                        | object          | The AuthN Mapping object returned by API.                                                                                                                                                                                                                                                     |
| data                     | attributes                  | object          | Attributes of AuthN Mapping.                                                                                                                                                                                                                                                                  |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| attributes               | created_at                  | date-time       | Creation time of the AuthN Mapping.                                                                                                                                                                                                                                                           |
| attributes               | modified_at                 | date-time       | Time of last AuthN Mapping modification.                                                                                                                                                                                                                                                      |
| attributes               | saml_assertion_attribute_id | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | id [*required*]        | string          | ID of the AuthN Mapping.                                                                                                                                                                                                                                                                      |
| data                     | relationships               | object          | All relationships associated with AuthN Mapping.                                                                                                                                                                                                                                              |
| relationships            | role                        | object          | Relationship to role.                                                                                                                                                                                                                                                                         |
| role                     | data                        | object          | Relationship to role object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| relationships            | saml_assertion_attribute    | object          | AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                                       |
| saml_assertion_attribute | data [*required*]      | object          | Data of AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                               |
| data                     | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| relationships            | team                        | object          | Relationship to team.                                                                                                                                                                                                                                                                         |
| team                     | data                        | object          | Relationship to Team object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the team.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |
| data                     | type [*required*]      | enum            | AuthN Mappings resource type. Allowed enum values: `authn_mappings`                                                                                                                                                                                                                           |
|                          | included                    | [ <oneOf>] | Included data in the AuthN Mapping response.                                                                                                                                                                                                                                                  |
| included                 | Option 1                    | object          | SAML assertion attribute.                                                                                                                                                                                                                                                                     |
| Option 1                 | attributes                  | object          | Key/Value pair of attributes used in SAML assertion attributes.                                                                                                                                                                                                                               |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| Option 1                 | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| Option 1                 | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| included                 | Option 2                    | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2                 | attributes                  | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes               | created_at                  | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes               | modified_at                 | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes               | name                        | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes               | receives_permissions_from   | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes               | user_count                  | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2                 | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2                 | relationships               | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships            | permissions                 | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions              | data                        | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data                     | id                          | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data                     | type                        | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2                 | type [*required*]      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included                 | Option 3                    | object          | Team.                                                                                                                                                                                                                                                                                         |
| Option 3                 | attributes                  | object          | Team attributes.                                                                                                                                                                                                                                                                              |
| attributes               | avatar                      | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                                                                                               |
| attributes               | banner                      | int64           | Banner selection for the team                                                                                                                                                                                                                                                                 |
| attributes               | handle                      | string          | The team's identifier                                                                                                                                                                                                                                                                         |
| attributes               | link_count                  | int32           | The number of links belonging to the team                                                                                                                                                                                                                                                     |
| attributes               | name                        | string          | The name of the team                                                                                                                                                                                                                                                                          |
| attributes               | summary                     | string          | A brief summary of the team, derived from the `description`                                                                                                                                                                                                                                   |
| attributes               | user_count                  | int32           | The number of users belonging to the team                                                                                                                                                                                                                                                     |
| Option 3                 | id                          | string          | The ID of the Team.                                                                                                                                                                                                                                                                           |
| Option 3                 | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development",
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "saml_assertion_attribute_id": "0"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
          "type": "roles"
        }
      },
      "saml_assertion_attribute": {
        "data": {
          "id": "0",
          "type": "saml_assertion_attributes"
        }
      },
      "team": {
        "data": {
          "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      }
    },
    "type": "authn_mappings"
  },
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
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

{% tab title="403" %}
Authentication Error
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

{% tab title="404" %}
Not Found
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

{% tab title="409" %}
Conflict
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

{% tab title="422" %}
Unprocessable Entity
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
                          \# Path parametersexport authn_mapping_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings/${authn_mapping_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
EOF
                        
##### 

```go
// Edit an AuthN Mapping returns "OK" response

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
	// there is a valid "authn_mapping" in the system
	AuthnMappingDataID := os.Getenv("AUTHN_MAPPING_DATA_ID")

	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	body := datadogV2.AuthNMappingUpdateRequest{
		Data: datadogV2.AuthNMappingUpdateData{
			Attributes: &datadogV2.AuthNMappingUpdateAttributes{
				AttributeKey:   datadog.PtrString("member-of"),
				AttributeValue: datadog.PtrString("Development"),
			},
			Id: AuthnMappingDataID,
			Relationships: &datadogV2.AuthNMappingUpdateRelationships{
				AuthNMappingRelationshipToRole: &datadogV2.AuthNMappingRelationshipToRole{
					Role: datadogV2.RelationshipToRole{
						Data: &datadogV2.RelationshipToRoleData{
							Id:   datadog.PtrString(RoleDataID),
							Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
						},
					},
				}},
			Type: datadogV2.AUTHNMAPPINGSTYPE_AUTHN_MAPPINGS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.UpdateAuthNMapping(ctx, AuthnMappingDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.UpdateAuthNMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.UpdateAuthNMapping`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Edit an AuthN Mapping returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingRelationshipToRole;
import com.datadog.api.client.v2.model.AuthNMappingResponse;
import com.datadog.api.client.v2.model.AuthNMappingUpdateAttributes;
import com.datadog.api.client.v2.model.AuthNMappingUpdateData;
import com.datadog.api.client.v2.model.AuthNMappingUpdateRelationships;
import com.datadog.api.client.v2.model.AuthNMappingUpdateRequest;
import com.datadog.api.client.v2.model.AuthNMappingsType;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "authn_mapping" in the system
    String AUTHN_MAPPING_DATA_ID = System.getenv("AUTHN_MAPPING_DATA_ID");

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    AuthNMappingUpdateRequest body =
        new AuthNMappingUpdateRequest()
            .data(
                new AuthNMappingUpdateData()
                    .attributes(
                        new AuthNMappingUpdateAttributes()
                            .attributeKey("member-of")
                            .attributeValue("Development"))
                    .id(AUTHN_MAPPING_DATA_ID)
                    .relationships(
                        new AuthNMappingUpdateRelationships(
                            new AuthNMappingRelationshipToRole()
                                .role(
                                    new RelationshipToRole()
                                        .data(
                                            new RelationshipToRoleData()
                                                .id(ROLE_DATA_ID)
                                                .type(RolesType.ROLES)))))
                    .type(AuthNMappingsType.AUTHN_MAPPINGS));

    try {
      AuthNMappingResponse result = apiInstance.updateAuthNMapping(AUTHN_MAPPING_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#updateAuthNMapping");
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
Edit an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_relationship_to_role import AuthNMappingRelationshipToRole
from datadog_api_client.v2.model.authn_mapping_update_attributes import AuthNMappingUpdateAttributes
from datadog_api_client.v2.model.authn_mapping_update_data import AuthNMappingUpdateData
from datadog_api_client.v2.model.authn_mapping_update_request import AuthNMappingUpdateRequest
from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingUpdateRequest(
    data=AuthNMappingUpdateData(
        attributes=AuthNMappingUpdateAttributes(
            attribute_key="member-of",
            attribute_value="Development",
        ),
        id=AUTHN_MAPPING_DATA_ID,
        relationships=AuthNMappingRelationshipToRole(
            role=RelationshipToRole(
                data=RelationshipToRoleData(
                    id=ROLE_DATA_ID,
                    type=RolesType.ROLES,
                ),
            ),
        ),
        type=AuthNMappingsType.AUTHN_MAPPINGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.update_authn_mapping(authn_mapping_id=AUTHN_MAPPING_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Edit an AuthN Mapping returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = ENV["AUTHN_MAPPING_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::AuthNMappingUpdateRequest.new({
  data: DatadogAPIClient::V2::AuthNMappingUpdateData.new({
    attributes: DatadogAPIClient::V2::AuthNMappingUpdateAttributes.new({
      attribute_key: "member-of",
      attribute_value: "Development",
    }),
    id: AUTHN_MAPPING_DATA_ID,
    relationships: DatadogAPIClient::V2::AuthNMappingRelationshipToRole.new({
      role: DatadogAPIClient::V2::RelationshipToRole.new({
        data: DatadogAPIClient::V2::RelationshipToRoleData.new({
          id: ROLE_DATA_ID,
          type: DatadogAPIClient::V2::RolesType::ROLES,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::AuthNMappingsType::AUTHN_MAPPINGS,
  }),
})
p api_instance.update_authn_mapping(AUTHN_MAPPING_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Edit an AuthN Mapping returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;
use datadog_api_client::datadogV2::model::AuthNMappingRelationshipToRole;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateAttributes;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateData;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateRelationships;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateRequest;
use datadog_api_client::datadogV2::model::AuthNMappingsType;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "authn_mapping" in the system
    let authn_mapping_data_id = std::env::var("AUTHN_MAPPING_DATA_ID").unwrap();

    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = AuthNMappingUpdateRequest::new(
        AuthNMappingUpdateData::new(
            authn_mapping_data_id.clone(),
            AuthNMappingsType::AUTHN_MAPPINGS,
        )
        .attributes(
            AuthNMappingUpdateAttributes::new()
                .attribute_key("member-of".to_string())
                .attribute_value("Development".to_string()),
        )
        .relationships(
            AuthNMappingUpdateRelationships::AuthNMappingRelationshipToRole(Box::new(
                AuthNMappingRelationshipToRole::new(
                    RelationshipToRole::new().data(
                        RelationshipToRoleData::new()
                            .id(role_data_id.clone())
                            .type_(RolesType::ROLES),
                    ),
                ),
            )),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api
        .update_authn_mapping(authn_mapping_data_id.clone(), body)
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
 * Edit an AuthN Mapping returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "authn_mapping" in the system
const AUTHN_MAPPING_DATA_ID = process.env.AUTHN_MAPPING_DATA_ID as string;

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.AuthNMappingsApiUpdateAuthNMappingRequest = {
  body: {
    data: {
      attributes: {
        attributeKey: "member-of",
        attributeValue: "Development",
      },
      id: AUTHN_MAPPING_DATA_ID,
      relationships: {
        role: {
          data: {
            id: ROLE_DATA_ID,
            type: "roles",
          },
        },
      },
      type: "authn_mappings",
    },
  },
  authnMappingId: AUTHN_MAPPING_DATA_ID,
};

apiInstance
  .updateAuthNMapping(params)
  .then((data: v2.AuthNMappingResponse) => {
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

## Delete an AuthN Mapping{% #delete-an-authn-mapping %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/authn_mappings/{authn_mapping_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/authn_mappings/{authn_mapping_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id} |

### Overview

Delete an AuthN Mapping specified by AuthN Mapping UUID. This endpoint requires the `user_access_manage` permission.

### Arguments

#### Path Parameters

| Name                               | Type   | Description                    |
| ---------------------------------- | ------ | ------------------------------ |
| authn_mapping_id [*required*] | string | The UUID of the AuthN Mapping. |

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="403" %}
Authentication Error
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport authn_mapping_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings/${authn_mapping_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    api_instance.delete_authn_mapping(
        authn_mapping_id=AUTHN_MAPPING_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an AuthN Mapping returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = ENV["AUTHN_MAPPING_DATA_ID"]
api_instance.delete_authn_mapping(AUTHN_MAPPING_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete an AuthN Mapping returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "authn_mapping" in the system
	AuthnMappingDataID := os.Getenv("AUTHN_MAPPING_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	r, err := api.DeleteAuthNMapping(ctx, AuthnMappingDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.DeleteAuthNMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete an AuthN Mapping returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "authn_mapping" in the system
    String AUTHN_MAPPING_DATA_ID = System.getenv("AUTHN_MAPPING_DATA_ID");

    try {
      apiInstance.deleteAuthNMapping(AUTHN_MAPPING_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#deleteAuthNMapping");
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
// Delete an AuthN Mapping returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "authn_mapping" in the system
    let authn_mapping_data_id = std::env::var("AUTHN_MAPPING_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api
        .delete_authn_mapping(authn_mapping_data_id.clone())
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
 * Delete an AuthN Mapping returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "authn_mapping" in the system
const AUTHN_MAPPING_DATA_ID = process.env.AUTHN_MAPPING_DATA_ID as string;

const params: v2.AuthNMappingsApiDeleteAuthNMappingRequest = {
  authnMappingId: AUTHN_MAPPING_DATA_ID,
};

apiInstance
  .deleteAuthNMapping(params)
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

## List all AuthN Mappings{% #list-all-authn-mappings %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/authn_mappings |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/authn_mappings |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/authn_mappings      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/authn_mappings      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/authn_mappings     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/authn_mappings |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/authn_mappings |

### Overview

List all AuthN Mappings in the org. This endpoint requires the `user_access_read` permission.

### Arguments

#### Query Strings

| Name          | Type    | Description                                                                                                                                                                                                                                                                                                                                                                |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]    | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                                                                                                                                                                                   |
| page[number]  | integer | Specific page number to return.                                                                                                                                                                                                                                                                                                                                            |
| sort          | enum    | Sort AuthN Mappings depending on the given field.Allowed enum values: `created_at, -created_at, role_id, -role_id, saml_assertion_attribute_id, -saml_assertion_attribute_id, role.name, -role.name, saml_assertion_attribute.attribute_key, -saml_assertion_attribute.attribute_key, saml_assertion_attribute.attribute_value, -saml_assertion_attribute.attribute_value` |
| filter        | string  | Filter all mappings by the given string.                                                                                                                                                                                                                                                                                                                                   |
| resource_type | enum    | Filter by mapping resource type. Defaults to "role" if not specified.Allowed enum values: `role, team`                                                                                                                                                                                                                                                                     |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Array of AuthN Mappings response.

| Parent field             | Field                       | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                          | data                        | [object]        | Array of returned AuthN Mappings.                                                                                                                                                                                                                                                             |
| data                     | attributes                  | object          | Attributes of AuthN Mapping.                                                                                                                                                                                                                                                                  |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| attributes               | created_at                  | date-time       | Creation time of the AuthN Mapping.                                                                                                                                                                                                                                                           |
| attributes               | modified_at                 | date-time       | Time of last AuthN Mapping modification.                                                                                                                                                                                                                                                      |
| attributes               | saml_assertion_attribute_id | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | id [*required*]        | string          | ID of the AuthN Mapping.                                                                                                                                                                                                                                                                      |
| data                     | relationships               | object          | All relationships associated with AuthN Mapping.                                                                                                                                                                                                                                              |
| relationships            | role                        | object          | Relationship to role.                                                                                                                                                                                                                                                                         |
| role                     | data                        | object          | Relationship to role object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| relationships            | saml_assertion_attribute    | object          | AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                                       |
| saml_assertion_attribute | data [*required*]      | object          | Data of AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                               |
| data                     | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| relationships            | team                        | object          | Relationship to team.                                                                                                                                                                                                                                                                         |
| team                     | data                        | object          | Relationship to Team object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the team.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |
| data                     | type [*required*]      | enum            | AuthN Mappings resource type. Allowed enum values: `authn_mappings`                                                                                                                                                                                                                           |
|                          | included                    | [ <oneOf>] | Included data in the AuthN Mapping response.                                                                                                                                                                                                                                                  |
| included                 | Option 1                    | object          | SAML assertion attribute.                                                                                                                                                                                                                                                                     |
| Option 1                 | attributes                  | object          | Key/Value pair of attributes used in SAML assertion attributes.                                                                                                                                                                                                                               |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| Option 1                 | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| Option 1                 | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| included                 | Option 2                    | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2                 | attributes                  | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes               | created_at                  | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes               | modified_at                 | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes               | name                        | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes               | receives_permissions_from   | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes               | user_count                  | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2                 | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2                 | relationships               | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships            | permissions                 | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions              | data                        | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data                     | id                          | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data                     | type                        | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2                 | type [*required*]      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included                 | Option 3                    | object          | Team.                                                                                                                                                                                                                                                                                         |
| Option 3                 | attributes                  | object          | Team attributes.                                                                                                                                                                                                                                                                              |
| attributes               | avatar                      | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                                                                                               |
| attributes               | banner                      | int64           | Banner selection for the team                                                                                                                                                                                                                                                                 |
| attributes               | handle                      | string          | The team's identifier                                                                                                                                                                                                                                                                         |
| attributes               | link_count                  | int32           | The number of links belonging to the team                                                                                                                                                                                                                                                     |
| attributes               | name                        | string          | The name of the team                                                                                                                                                                                                                                                                          |
| attributes               | summary                     | string          | A brief summary of the team, derived from the `description`                                                                                                                                                                                                                                   |
| attributes               | user_count                  | int32           | The number of users belonging to the team                                                                                                                                                                                                                                                     |
| Option 3                 | id                          | string          | The ID of the Team.                                                                                                                                                                                                                                                                           |
| Option 3                 | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |
|                          | meta                        | object          | Object describing meta attributes of response.                                                                                                                                                                                                                                                |
| meta                     | page                        | object          | Pagination object.                                                                                                                                                                                                                                                                            |
| page                     | total_count                 | int64           | Total count.                                                                                                                                                                                                                                                                                  |
| page                     | total_filtered_count        | int64           | Total count of elements matched by the filter.                                                                                                                                                                                                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development",
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "saml_assertion_attribute_id": "0"
      },
      "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
      "relationships": {
        "role": {
          "data": {
            "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            "type": "roles"
          }
        },
        "saml_assertion_attribute": {
          "data": {
            "id": "0",
            "type": "saml_assertion_attributes"
          }
        },
        "team": {
          "data": {
            "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
            "type": "team"
          }
        }
      },
      "type": "authn_mappings"
    }
  ],
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
    }
  ],
  "meta": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List all AuthN Mappings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.list_authn_mappings()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List all AuthN Mappings returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new
p api_instance.list_authn_mappings()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List all AuthN Mappings returns "OK" response

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
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.ListAuthNMappings(ctx, *datadogV2.NewListAuthNMappingsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.ListAuthNMappings`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.ListAuthNMappings`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List all AuthN Mappings returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    try {
      AuthNMappingsResponse result = apiInstance.listAuthNMappings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#listAuthNMappings");
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
// List all AuthN Mappings returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;
use datadog_api_client::datadogV2::api_authn_mappings::ListAuthNMappingsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api
        .list_authn_mappings(ListAuthNMappingsOptionalParams::default())
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
 * List all AuthN Mappings returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

apiInstance
  .listAuthNMappings()
  .then((data: v2.AuthNMappingsResponse) => {
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

## Create an AuthN Mapping{% #create-an-authn-mapping %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/authn_mappings |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/authn_mappings |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/authn_mappings      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/authn_mappings      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/authn_mappings     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/authn_mappings |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/authn_mappings |

### Overview

Create an AuthN Mapping. This endpoint requires the `user_access_manage` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                  | Type          | Description                                                                         |
| ------------- | ---------------------- | ------------- | ----------------------------------------------------------------------------------- |
|               | data [*required*] | object        | Data for creating an AuthN Mapping.                                                 |
| data          | attributes             | object        | Key/Value pair of attributes used for create request.                               |
| attributes    | attribute_key          | string        | Key portion of a key/value pair of the attribute sent from the Identity Provider.   |
| attributes    | attribute_value        | string        | Value portion of a key/value pair of the attribute sent from the Identity Provider. |
| data          | relationships          |  <oneOf> | Relationship of AuthN Mapping create object to a Role or Team.                      |
| relationships | Option 1               | object        | Relationship of AuthN Mapping to a Role.                                            |
| Option 1      | role [*required*] | object        | Relationship to role.                                                               |
| role          | data                   | object        | Relationship to role object.                                                        |
| data          | id                     | string        | The unique identifier of the role.                                                  |
| data          | type                   | enum          | Roles type. Allowed enum values: `roles`                                            |
| relationships | Option 2               | object        | Relationship of AuthN Mapping to a Team.                                            |
| Option 2      | team [*required*] | object        | Relationship to team.                                                               |
| team          | data                   | object        | Relationship to Team object.                                                        |
| data          | id                     | string        | The unique identifier of the team.                                                  |
| data          | type                   | enum          | Team type Allowed enum values: `team`                                               |
| data          | type [*required*] | enum          | AuthN Mappings resource type. Allowed enum values: `authn_mappings`                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "attribute_key": "exampleauthnmapping",
      "attribute_value": "Example-AuthN-Mapping"
    },
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
AuthN Mapping response from the API.

| Parent field             | Field                       | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                          | data                        | object          | The AuthN Mapping object returned by API.                                                                                                                                                                                                                                                     |
| data                     | attributes                  | object          | Attributes of AuthN Mapping.                                                                                                                                                                                                                                                                  |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| attributes               | created_at                  | date-time       | Creation time of the AuthN Mapping.                                                                                                                                                                                                                                                           |
| attributes               | modified_at                 | date-time       | Time of last AuthN Mapping modification.                                                                                                                                                                                                                                                      |
| attributes               | saml_assertion_attribute_id | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | id [*required*]        | string          | ID of the AuthN Mapping.                                                                                                                                                                                                                                                                      |
| data                     | relationships               | object          | All relationships associated with AuthN Mapping.                                                                                                                                                                                                                                              |
| relationships            | role                        | object          | Relationship to role.                                                                                                                                                                                                                                                                         |
| role                     | data                        | object          | Relationship to role object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| relationships            | saml_assertion_attribute    | object          | AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                                       |
| saml_assertion_attribute | data [*required*]      | object          | Data of AuthN Mapping relationship to SAML Assertion Attribute.                                                                                                                                                                                                                               |
| data                     | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| data                     | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| relationships            | team                        | object          | Relationship to team.                                                                                                                                                                                                                                                                         |
| team                     | data                        | object          | Relationship to Team object.                                                                                                                                                                                                                                                                  |
| data                     | id                          | string          | The unique identifier of the team.                                                                                                                                                                                                                                                            |
| data                     | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |
| data                     | type [*required*]      | enum            | AuthN Mappings resource type. Allowed enum values: `authn_mappings`                                                                                                                                                                                                                           |
|                          | included                    | [ <oneOf>] | Included data in the AuthN Mapping response.                                                                                                                                                                                                                                                  |
| included                 | Option 1                    | object          | SAML assertion attribute.                                                                                                                                                                                                                                                                     |
| Option 1                 | attributes                  | object          | Key/Value pair of attributes used in SAML assertion attributes.                                                                                                                                                                                                                               |
| attributes               | attribute_key               | string          | Key portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                             |
| attributes               | attribute_value             | string          | Value portion of a key/value pair of the attribute sent from the Identity Provider.                                                                                                                                                                                                           |
| Option 1                 | id [*required*]        | string          | The ID of the SAML assertion attribute.                                                                                                                                                                                                                                                       |
| Option 1                 | type [*required*]      | enum            | SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`                                                                                                                                                                                                     |
| included                 | Option 2                    | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2                 | attributes                  | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes               | created_at                  | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes               | modified_at                 | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes               | name                        | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes               | receives_permissions_from   | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes               | user_count                  | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2                 | id                          | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2                 | relationships               | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships            | permissions                 | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions              | data                        | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data                     | id                          | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data                     | type                        | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2                 | type [*required*]      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included                 | Option 3                    | object          | Team.                                                                                                                                                                                                                                                                                         |
| Option 3                 | attributes                  | object          | Team attributes.                                                                                                                                                                                                                                                                              |
| attributes               | avatar                      | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                                                                                               |
| attributes               | banner                      | int64           | Banner selection for the team                                                                                                                                                                                                                                                                 |
| attributes               | handle                      | string          | The team's identifier                                                                                                                                                                                                                                                                         |
| attributes               | link_count                  | int32           | The number of links belonging to the team                                                                                                                                                                                                                                                     |
| attributes               | name                        | string          | The name of the team                                                                                                                                                                                                                                                                          |
| attributes               | summary                     | string          | A brief summary of the team, derived from the `description`                                                                                                                                                                                                                                   |
| attributes               | user_count                  | int32           | The number of users belonging to the team                                                                                                                                                                                                                                                     |
| Option 3                 | id                          | string          | The ID of the Team.                                                                                                                                                                                                                                                                           |
| Option 3                 | type                        | enum            | Team type Allowed enum values: `team`                                                                                                                                                                                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development",
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "saml_assertion_attribute_id": "0"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
          "type": "roles"
        }
      },
      "saml_assertion_attribute": {
        "data": {
          "id": "0",
          "type": "saml_assertion_attributes"
        }
      },
      "team": {
        "data": {
          "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      }
    },
    "type": "authn_mappings"
  },
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
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

{% tab title="403" %}
Authentication Error
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

{% tab title="404" %}
Not Found
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "attribute_key": "exampleauthnmapping",
      "attribute_value": "Example-AuthN-Mapping"
    },
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
EOF
                        
##### 

```go
// Create an AuthN Mapping returns "OK" response

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
	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	body := datadogV2.AuthNMappingCreateRequest{
		Data: datadogV2.AuthNMappingCreateData{
			Attributes: &datadogV2.AuthNMappingCreateAttributes{
				AttributeKey:   datadog.PtrString("exampleauthnmapping"),
				AttributeValue: datadog.PtrString("Example-AuthN-Mapping"),
			},
			Relationships: &datadogV2.AuthNMappingCreateRelationships{
				AuthNMappingRelationshipToRole: &datadogV2.AuthNMappingRelationshipToRole{
					Role: datadogV2.RelationshipToRole{
						Data: &datadogV2.RelationshipToRoleData{
							Id:   datadog.PtrString(RoleDataID),
							Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
						},
					},
				}},
			Type: datadogV2.AUTHNMAPPINGSTYPE_AUTHN_MAPPINGS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.CreateAuthNMapping(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.CreateAuthNMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.CreateAuthNMapping`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create an AuthN Mapping returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingCreateAttributes;
import com.datadog.api.client.v2.model.AuthNMappingCreateData;
import com.datadog.api.client.v2.model.AuthNMappingCreateRelationships;
import com.datadog.api.client.v2.model.AuthNMappingCreateRequest;
import com.datadog.api.client.v2.model.AuthNMappingRelationshipToRole;
import com.datadog.api.client.v2.model.AuthNMappingResponse;
import com.datadog.api.client.v2.model.AuthNMappingsType;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    AuthNMappingCreateRequest body =
        new AuthNMappingCreateRequest()
            .data(
                new AuthNMappingCreateData()
                    .attributes(
                        new AuthNMappingCreateAttributes()
                            .attributeKey("exampleauthnmapping")
                            .attributeValue("Example-AuthN-Mapping"))
                    .relationships(
                        new AuthNMappingCreateRelationships(
                            new AuthNMappingRelationshipToRole()
                                .role(
                                    new RelationshipToRole()
                                        .data(
                                            new RelationshipToRoleData()
                                                .id(ROLE_DATA_ID)
                                                .type(RolesType.ROLES)))))
                    .type(AuthNMappingsType.AUTHN_MAPPINGS));

    try {
      AuthNMappingResponse result = apiInstance.createAuthNMapping(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#createAuthNMapping");
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
Create an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_create_attributes import AuthNMappingCreateAttributes
from datadog_api_client.v2.model.authn_mapping_create_data import AuthNMappingCreateData
from datadog_api_client.v2.model.authn_mapping_create_request import AuthNMappingCreateRequest
from datadog_api_client.v2.model.authn_mapping_relationship_to_role import AuthNMappingRelationshipToRole
from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingCreateRequest(
    data=AuthNMappingCreateData(
        attributes=AuthNMappingCreateAttributes(
            attribute_key="exampleauthnmapping",
            attribute_value="Example-AuthN-Mapping",
        ),
        relationships=AuthNMappingRelationshipToRole(
            role=RelationshipToRole(
                data=RelationshipToRoleData(
                    id=ROLE_DATA_ID,
                    type=RolesType.ROLES,
                ),
            ),
        ),
        type=AuthNMappingsType.AUTHN_MAPPINGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.create_authn_mapping(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create an AuthN Mapping returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::AuthNMappingCreateRequest.new({
  data: DatadogAPIClient::V2::AuthNMappingCreateData.new({
    attributes: DatadogAPIClient::V2::AuthNMappingCreateAttributes.new({
      attribute_key: "exampleauthnmapping",
      attribute_value: "Example-AuthN-Mapping",
    }),
    relationships: DatadogAPIClient::V2::AuthNMappingRelationshipToRole.new({
      role: DatadogAPIClient::V2::RelationshipToRole.new({
        data: DatadogAPIClient::V2::RelationshipToRoleData.new({
          id: ROLE_DATA_ID,
          type: DatadogAPIClient::V2::RolesType::ROLES,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::AuthNMappingsType::AUTHN_MAPPINGS,
  }),
})
p api_instance.create_authn_mapping(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create an AuthN Mapping returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;
use datadog_api_client::datadogV2::model::AuthNMappingCreateAttributes;
use datadog_api_client::datadogV2::model::AuthNMappingCreateData;
use datadog_api_client::datadogV2::model::AuthNMappingCreateRelationships;
use datadog_api_client::datadogV2::model::AuthNMappingCreateRequest;
use datadog_api_client::datadogV2::model::AuthNMappingRelationshipToRole;
use datadog_api_client::datadogV2::model::AuthNMappingsType;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = AuthNMappingCreateRequest::new(
        AuthNMappingCreateData::new(AuthNMappingsType::AUTHN_MAPPINGS)
            .attributes(
                AuthNMappingCreateAttributes::new()
                    .attribute_key("exampleauthnmapping".to_string())
                    .attribute_value("Example-AuthN-Mapping".to_string()),
            )
            .relationships(
                AuthNMappingCreateRelationships::AuthNMappingRelationshipToRole(Box::new(
                    AuthNMappingRelationshipToRole::new(
                        RelationshipToRole::new().data(
                            RelationshipToRoleData::new()
                                .id(role_data_id.clone())
                                .type_(RolesType::ROLES),
                        ),
                    ),
                )),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api.create_authn_mapping(body).await;
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
 * Create an AuthN Mapping returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.AuthNMappingsApiCreateAuthNMappingRequest = {
  body: {
    data: {
      attributes: {
        attributeKey: "exampleauthnmapping",
        attributeValue: "Example-AuthN-Mapping",
      },
      relationships: {
        role: {
          data: {
            id: ROLE_DATA_ID,
            type: "roles",
          },
        },
      },
      type: "authn_mappings",
    },
  },
};

apiInstance
  .createAuthNMapping(params)
  .then((data: v2.AuthNMappingResponse) => {
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
