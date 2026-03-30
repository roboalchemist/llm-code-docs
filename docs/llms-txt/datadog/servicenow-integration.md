# Source: https://docs.datadoghq.com/api/latest/servicenow-integration.md

---
title: ServiceNow Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > ServiceNow Integration
---

Manage your ServiceNow Integration. ServiceNow is a cloud-based platform that helps organizations manage digital workflows for enterprise operations.

## Delete ServiceNow template{% #delete-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/servicenow/handles/{template_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/servicenow/handles/{template_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/servicenow/handles/{template_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |

### Overview

Delete a ServiceNow template by ID.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                 |
| ----------------------------- | ------ | ------------------------------------------- |
| template_id [*required*] | string | The ID of the ServiceNow template to delete |

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
                  \# Path parametersexport template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/${template_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete ServiceNow template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_service_now_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    api_instance.delete_service_now_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete ServiceNow template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_service_now_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new
p api_instance.delete_service_now_template("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete ServiceNow template returns "OK" response

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
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.DeleteServiceNowTemplate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    r, err := api.DeleteServiceNowTemplate(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.DeleteServiceNowTemplate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete ServiceNow template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteServiceNowTemplate", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    try {
      apiInstance.deleteServiceNowTemplate(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceNowIntegrationApi#deleteServiceNowTemplate");
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
// Delete ServiceNow template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteServiceNowTemplate", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_service_now_template(
            Uuid::parse_str("00000000-0000-0000-0000-000000000000").expect("invalid UUID"),
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
 * Delete ServiceNow template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteServiceNowTemplate"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

const params: v2.ServiceNowIntegrationApiDeleteServiceNowTemplateRequest = {
  templateId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .deleteServiceNowTemplate(params)
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

## Update ServiceNow template{% #update-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/integration/servicenow/handles/{template_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/integration/servicenow/handles/{template_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/integration/servicenow/handles/{template_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |

### Overview

Update a ServiceNow template by ID.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                 |
| ----------------------------- | ------ | ------------------------------------------- |
| template_id [*required*] | string | The ID of the ServiceNow template to update |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for updating a ServiceNow template                                                |
| data                 | attributes [*required*]           | object | Attributes for updating a ServiceNow template                                                 |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template-updated",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "type": "servicenow_templates"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single ServiceNow template

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for a ServiceNow template                                                         |
| data                 | attributes [*required*]           | object | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid   | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "type": "servicenow_templates"
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
                  \# Path parametersexport template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/${template_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "handle_name": "incident-template-updated",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident"
    },
    "type": "servicenow_templates"
  }
}
EOF

#####

```python
"""
Update ServiceNow template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType
from datadog_api_client.v2.model.service_now_template_update_request import ServiceNowTemplateUpdateRequest
from datadog_api_client.v2.model.service_now_template_update_request_attributes import (
    ServiceNowTemplateUpdateRequestAttributes,
)
from datadog_api_client.v2.model.service_now_template_update_request_data import ServiceNowTemplateUpdateRequestData
from uuid import UUID

body = ServiceNowTemplateUpdateRequest(
    data=ServiceNowTemplateUpdateRequestData(
        attributes=ServiceNowTemplateUpdateRequestAttributes(
            assignment_group_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            business_service_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            fields_mapping=dict(
                category="hardware",
                priority="2",
            ),
            handle_name="incident-template-updated",
            instance_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            servicenow_tablename="incident",
            user_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
        ),
        type=ServiceNowTemplateType.SERVICENOW_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_service_now_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.update_service_now_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update ServiceNow template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_service_now_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new

body = DatadogAPIClient::V2::ServiceNowTemplateUpdateRequest.new({
  data: DatadogAPIClient::V2::ServiceNowTemplateUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::ServiceNowTemplateUpdateRequestAttributes.new({
      assignment_group_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
      business_service_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
      fields_mapping: {
        category: "hardware", priority: "2",
      },
      handle_name: "incident-template-updated",
      instance_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
      servicenow_tablename: "incident",
      user_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
    }),
    type: DatadogAPIClient::V2::ServiceNowTemplateType::SERVICENOW_TEMPLATES,
  }),
})
p api_instance.update_service_now_template("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update ServiceNow template returns "OK" response

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
    body := datadogV2.ServiceNowTemplateUpdateRequest{
        Data: datadogV2.ServiceNowTemplateUpdateRequestData{
            Attributes: datadogV2.ServiceNowTemplateUpdateRequestAttributes{
                AssignmentGroupId: datadog.PtrUUID(uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e")),
                BusinessServiceId: datadog.PtrUUID(uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e")),
                FieldsMapping: map[string]string{
                    "category": "hardware",
                    "priority": "2",
                },
                HandleName:          "incident-template-updated",
                InstanceId:          uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e"),
                ServicenowTablename: "incident",
                UserId:              datadog.PtrUUID(uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e")),
            },
            Type: datadogV2.SERVICENOWTEMPLATETYPE_SERVICENOW_TEMPLATES,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.UpdateServiceNowTemplate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.UpdateServiceNowTemplate(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.UpdateServiceNowTemplate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.UpdateServiceNowTemplate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update ServiceNow template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowTemplateResponse;
import com.datadog.api.client.v2.model.ServiceNowTemplateType;
import com.datadog.api.client.v2.model.ServiceNowTemplateUpdateRequest;
import com.datadog.api.client.v2.model.ServiceNowTemplateUpdateRequestAttributes;
import com.datadog.api.client.v2.model.ServiceNowTemplateUpdateRequestData;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateServiceNowTemplate", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    ServiceNowTemplateUpdateRequest body =
        new ServiceNowTemplateUpdateRequest()
            .data(
                new ServiceNowTemplateUpdateRequestData()
                    .attributes(
                        new ServiceNowTemplateUpdateRequestAttributes()
                            .assignmentGroupId(
                                UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"))
                            .businessServiceId(
                                UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"))
                            .fieldsMapping(
                                Map.ofEntries(
                                    Map.entry("category", "hardware"), Map.entry("priority", "2")))
                            .handleName("incident-template-updated")
                            .instanceId(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"))
                            .servicenowTablename("incident")
                            .userId(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e")))
                    .type(ServiceNowTemplateType.SERVICENOW_TEMPLATES));

    try {
      ServiceNowTemplateResponse result =
          apiInstance.updateServiceNowTemplate(
              UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"), body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceNowIntegrationApi#updateServiceNowTemplate");
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
// Update ServiceNow template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;
use datadog_api_client::datadogV2::model::ServiceNowTemplateType;
use datadog_api_client::datadogV2::model::ServiceNowTemplateUpdateRequest;
use datadog_api_client::datadogV2::model::ServiceNowTemplateUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::ServiceNowTemplateUpdateRequestData;
use std::collections::BTreeMap;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let body = ServiceNowTemplateUpdateRequest::new(ServiceNowTemplateUpdateRequestData::new(
        ServiceNowTemplateUpdateRequestAttributes::new(
            "incident-template-updated".to_string(),
            Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID"),
            "incident".to_string(),
        )
        .assignment_group_id(
            Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID"),
        )
        .business_service_id(
            Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID"),
        )
        .fields_mapping(BTreeMap::from([
            ("category".to_string(), "hardware".to_string()),
            ("priority".to_string(), "2".to_string()),
        ]))
        .user_id(Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID")),
        ServiceNowTemplateType::SERVICENOW_TEMPLATES,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateServiceNowTemplate", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api
        .update_service_now_template(
            Uuid::parse_str("00000000-0000-0000-0000-000000000000").expect("invalid UUID"),
            body,
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
 * Update ServiceNow template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateServiceNowTemplate"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

const params: v2.ServiceNowIntegrationApiUpdateServiceNowTemplateRequest = {
  body: {
    data: {
      attributes: {
        assignmentGroupId: "65b3341b-0680-47f9-a6d4-134db45c603e",
        businessServiceId: "65b3341b-0680-47f9-a6d4-134db45c603e",
        fieldsMapping: {
          category: "hardware",
          priority: "2",
        },
        handleName: "incident-template-updated",
        instanceId: "65b3341b-0680-47f9-a6d4-134db45c603e",
        servicenowTablename: "incident",
        userId: "65b3341b-0680-47f9-a6d4-134db45c603e",
      },
      type: "servicenow_templates",
    },
  },
  templateId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .updateServiceNowTemplate(params)
  .then((data: v2.ServiceNowTemplateResponse) => {
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

## Get ServiceNow template{% #get-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/handles/{template_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/handles/{template_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/handles/{template_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |

### Overview

Get a ServiceNow template by ID.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                   |
| ----------------------------- | ------ | --------------------------------------------- |
| template_id [*required*] | string | The ID of the ServiceNow template to retrieve |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single ServiceNow template

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for a ServiceNow template                                                         |
| data                 | attributes [*required*]           | object | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid   | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "type": "servicenow_templates"
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
                  \# Path parametersexport template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/${template_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get ServiceNow template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_service_now_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.get_service_now_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get ServiceNow template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_service_now_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new
p api_instance.get_service_now_template("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get ServiceNow template returns "OK" response

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
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetServiceNowTemplate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.GetServiceNowTemplate(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.GetServiceNowTemplate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.GetServiceNowTemplate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get ServiceNow template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowTemplateResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getServiceNowTemplate", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    try {
      ServiceNowTemplateResponse result =
          apiInstance.getServiceNowTemplate(
              UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceNowIntegrationApi#getServiceNowTemplate");
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
// Get ServiceNow template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetServiceNowTemplate", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api
        .get_service_now_template(
            Uuid::parse_str("00000000-0000-0000-0000-000000000000").expect("invalid UUID"),
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
 * Get ServiceNow template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getServiceNowTemplate"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

const params: v2.ServiceNowIntegrationApiGetServiceNowTemplateRequest = {
  templateId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .getServiceNowTemplate(params)
  .then((data: v2.ServiceNowTemplateResponse) => {
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

## Create ServiceNow template{% #create-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/servicenow/handles      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/servicenow/handles      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/servicenow/handles     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles |

### Overview

Create a new ServiceNow template.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for creating a ServiceNow template                                                |
| data                 | attributes [*required*]           | object | Attributes for creating a ServiceNow template                                                 |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "type": "servicenow_templates"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response containing a single ServiceNow template

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for a ServiceNow template                                                         |
| data                 | attributes [*required*]           | object | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid   | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "type": "servicenow_templates"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident"
    },
    "type": "servicenow_templates"
  }
}
EOF

#####

```python
"""
Create ServiceNow template returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from datadog_api_client.v2.model.service_now_template_create_request import ServiceNowTemplateCreateRequest
from datadog_api_client.v2.model.service_now_template_create_request_attributes import (
    ServiceNowTemplateCreateRequestAttributes,
)
from datadog_api_client.v2.model.service_now_template_create_request_data import ServiceNowTemplateCreateRequestData
from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType
from uuid import UUID

body = ServiceNowTemplateCreateRequest(
    data=ServiceNowTemplateCreateRequestData(
        attributes=ServiceNowTemplateCreateRequestAttributes(
            assignment_group_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            business_service_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            fields_mapping=dict(
                category="software",
                priority="1",
            ),
            handle_name="incident-template",
            instance_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            servicenow_tablename="incident",
            user_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
        ),
        type=ServiceNowTemplateType.SERVICENOW_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_service_now_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.create_service_now_template(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create ServiceNow template returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_service_now_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new

body = DatadogAPIClient::V2::ServiceNowTemplateCreateRequest.new({
  data: DatadogAPIClient::V2::ServiceNowTemplateCreateRequestData.new({
    attributes: DatadogAPIClient::V2::ServiceNowTemplateCreateRequestAttributes.new({
      assignment_group_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
      business_service_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
      fields_mapping: {
        category: "software", priority: "1",
      },
      handle_name: "incident-template",
      instance_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
      servicenow_tablename: "incident",
      user_id: "65b3341b-0680-47f9-a6d4-134db45c603e",
    }),
    type: DatadogAPIClient::V2::ServiceNowTemplateType::SERVICENOW_TEMPLATES,
  }),
})
p api_instance.create_service_now_template(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Create ServiceNow template returns "Created" response

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
    body := datadogV2.ServiceNowTemplateCreateRequest{
        Data: datadogV2.ServiceNowTemplateCreateRequestData{
            Attributes: datadogV2.ServiceNowTemplateCreateRequestAttributes{
                AssignmentGroupId: datadog.PtrUUID(uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e")),
                BusinessServiceId: datadog.PtrUUID(uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e")),
                FieldsMapping: map[string]string{
                    "category": "software",
                    "priority": "1",
                },
                HandleName:          "incident-template",
                InstanceId:          uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e"),
                ServicenowTablename: "incident",
                UserId:              datadog.PtrUUID(uuid.MustParse("65b3341b-0680-47f9-a6d4-134db45c603e")),
            },
            Type: datadogV2.SERVICENOWTEMPLATETYPE_SERVICENOW_TEMPLATES,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateServiceNowTemplate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.CreateServiceNowTemplate(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.CreateServiceNowTemplate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.CreateServiceNowTemplate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create ServiceNow template returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowTemplateCreateRequest;
import com.datadog.api.client.v2.model.ServiceNowTemplateCreateRequestAttributes;
import com.datadog.api.client.v2.model.ServiceNowTemplateCreateRequestData;
import com.datadog.api.client.v2.model.ServiceNowTemplateResponse;
import com.datadog.api.client.v2.model.ServiceNowTemplateType;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createServiceNowTemplate", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    ServiceNowTemplateCreateRequest body =
        new ServiceNowTemplateCreateRequest()
            .data(
                new ServiceNowTemplateCreateRequestData()
                    .attributes(
                        new ServiceNowTemplateCreateRequestAttributes()
                            .assignmentGroupId(
                                UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"))
                            .businessServiceId(
                                UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"))
                            .fieldsMapping(
                                Map.ofEntries(
                                    Map.entry("category", "software"), Map.entry("priority", "1")))
                            .handleName("incident-template")
                            .instanceId(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"))
                            .servicenowTablename("incident")
                            .userId(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e")))
                    .type(ServiceNowTemplateType.SERVICENOW_TEMPLATES));

    try {
      ServiceNowTemplateResponse result = apiInstance.createServiceNowTemplate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceNowIntegrationApi#createServiceNowTemplate");
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
// Create ServiceNow template returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;
use datadog_api_client::datadogV2::model::ServiceNowTemplateCreateRequest;
use datadog_api_client::datadogV2::model::ServiceNowTemplateCreateRequestAttributes;
use datadog_api_client::datadogV2::model::ServiceNowTemplateCreateRequestData;
use datadog_api_client::datadogV2::model::ServiceNowTemplateType;
use std::collections::BTreeMap;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let body = ServiceNowTemplateCreateRequest::new(ServiceNowTemplateCreateRequestData::new(
        ServiceNowTemplateCreateRequestAttributes::new(
            "incident-template".to_string(),
            Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID"),
            "incident".to_string(),
        )
        .assignment_group_id(
            Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID"),
        )
        .business_service_id(
            Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID"),
        )
        .fields_mapping(BTreeMap::from([
            ("category".to_string(), "software".to_string()),
            ("priority".to_string(), "1".to_string()),
        ]))
        .user_id(Uuid::parse_str("65b3341b-0680-47f9-a6d4-134db45c603e").expect("invalid UUID")),
        ServiceNowTemplateType::SERVICENOW_TEMPLATES,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateServiceNowTemplate", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api.create_service_now_template(body).await;
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
 * Create ServiceNow template returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createServiceNowTemplate"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

const params: v2.ServiceNowIntegrationApiCreateServiceNowTemplateRequest = {
  body: {
    data: {
      attributes: {
        assignmentGroupId: "65b3341b-0680-47f9-a6d4-134db45c603e",
        businessServiceId: "65b3341b-0680-47f9-a6d4-134db45c603e",
        fieldsMapping: {
          category: "software",
          priority: "1",
        },
        handleName: "incident-template",
        instanceId: "65b3341b-0680-47f9-a6d4-134db45c603e",
        servicenowTablename: "incident",
        userId: "65b3341b-0680-47f9-a6d4-134db45c603e",
      },
      type: "servicenow_templates",
    },
  },
};

apiInstance
  .createServiceNowTemplate(params)
  .then((data: v2.ServiceNowTemplateResponse) => {
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

## List ServiceNow templates{% #list-servicenow-templates %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/handles      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/handles      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/handles     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles |

### Overview

Get all ServiceNow templates for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow templates

| Parent field         | Field                                  | Type     | Description                                                                                   |
| -------------------- | -------------------------------------- | -------- | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | [object] | Array of ServiceNow template data objects                                                     |
| data                 | attributes [*required*]           | object   | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid     | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid     | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object   | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string   |
| attributes           | handle_name [*required*]          | string   | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid     | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string   | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid     | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid     | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum     | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "fields_mapping": {
          "<any-key>": "string"
        },
        "handle_name": "incident-template",
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "servicenow_tablename": "incident",
        "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "servicenow_templates"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List ServiceNow templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_service_now_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.list_service_now_templates()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List ServiceNow templates returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_service_now_templates".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new
p api_instance.list_service_now_templates()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List ServiceNow templates returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.ListServiceNowTemplates", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.ListServiceNowTemplates(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.ListServiceNowTemplates`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.ListServiceNowTemplates`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List ServiceNow templates returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowTemplatesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listServiceNowTemplates", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    try {
      ServiceNowTemplatesResponse result = apiInstance.listServiceNowTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceNowIntegrationApi#listServiceNowTemplates");
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
// List ServiceNow templates returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListServiceNowTemplates", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api.list_service_now_templates().await;
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
 * List ServiceNow templates returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listServiceNowTemplates"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

apiInstance
  .listServiceNowTemplates()
  .then((data: v2.ServiceNowTemplatesResponse) => {
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

## List ServiceNow assignment groups{% #list-servicenow-assignment-groups %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/assignment_groups/{instance_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/assignment_groups/{instance_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |

### Overview

Get all assignment groups for a ServiceNow instance.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                       |
| ----------------------------- | ------ | --------------------------------- |
| instance_id [*required*] | string | The ID of the ServiceNow instance |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow assignment groups

| Parent field | Field                                     | Type     | Description                                                                                        |
| ------------ | ----------------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data [*required*]                    | [object] | Array of ServiceNow assignment group data objects                                                  |
| data         | attributes [*required*]              | object   | Attributes of a ServiceNow assignment group                                                        |
| attributes   | assignment_group_name [*required*]   | string   | The name of the assignment group                                                                   |
| attributes   | assignment_group_sys_id [*required*] | string   | The system ID of the assignment group in ServiceNow                                                |
| attributes   | instance_id [*required*]             | uuid     | The ID of the ServiceNow instance                                                                  |
| data         | id [*required*]                      | uuid     | Unique identifier for the ServiceNow assignment group                                              |
| data         | type [*required*]                    | enum     | Type identifier for ServiceNow assignment group resources Allowed enum values: `assignment_groups` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "assignment_group_name": "Network Team",
        "assignment_group_sys_id": "abc123def456",
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "assignment_groups"
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
                  \# Path parametersexport instance_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/assignment_groups/${instance_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List ServiceNow assignment groups returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["list_service_now_assignment_groups"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.list_service_now_assignment_groups(
        instance_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List ServiceNow assignment groups returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_service_now_assignment_groups".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new
p api_instance.list_service_now_assignment_groups("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List ServiceNow assignment groups returns "OK" response

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
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListServiceNowAssignmentGroups", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.ListServiceNowAssignmentGroups(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.ListServiceNowAssignmentGroups`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.ListServiceNowAssignmentGroups`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List ServiceNow assignment groups returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowAssignmentGroupsResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listServiceNowAssignmentGroups", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    try {
      ServiceNowAssignmentGroupsResponse result =
          apiInstance.listServiceNowAssignmentGroups(
              UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceNowIntegrationApi#listServiceNowAssignmentGroups");
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
// List ServiceNow assignment groups returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListServiceNowAssignmentGroups", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api
        .list_service_now_assignment_groups(
            Uuid::parse_str("00000000-0000-0000-0000-000000000000").expect("invalid UUID"),
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
 * List ServiceNow assignment groups returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listServiceNowAssignmentGroups"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

const params: v2.ServiceNowIntegrationApiListServiceNowAssignmentGroupsRequest =
  {
    instanceId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  };

apiInstance
  .listServiceNowAssignmentGroups(params)
  .then((data: v2.ServiceNowAssignmentGroupsResponse) => {
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

## List ServiceNow business services{% #list-servicenow-business-services %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/business_services/{instance_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/business_services/{instance_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |

### Overview

Get all business services for a ServiceNow instance.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                       |
| ----------------------------- | ------ | --------------------------------- |
| instance_id [*required*] | string | The ID of the ServiceNow instance |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow business services

| Parent field | Field                            | Type     | Description                                                                                        |
| ------------ | -------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data [*required*]           | [object] | Array of ServiceNow business service data objects                                                  |
| data         | attributes [*required*]     | object   | Attributes of a ServiceNow business service                                                        |
| attributes   | instance_id [*required*]    | uuid     | The ID of the ServiceNow instance                                                                  |
| attributes   | service_name [*required*]   | string   | The name of the business service                                                                   |
| attributes   | service_sys_id [*required*] | string   | The system ID of the business service in ServiceNow                                                |
| data         | id [*required*]             | uuid     | Unique identifier for the ServiceNow business service                                              |
| data         | type [*required*]           | enum     | Type identifier for ServiceNow business service resources Allowed enum values: `business_services` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "service_name": "IT Support",
        "service_sys_id": "abc123def456"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "business_services"
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
                  \# Path parametersexport instance_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/business_services/${instance_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List ServiceNow business services returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["list_service_now_business_services"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.list_service_now_business_services(
        instance_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List ServiceNow business services returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_service_now_business_services".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new
p api_instance.list_service_now_business_services("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List ServiceNow business services returns "OK" response

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
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListServiceNowBusinessServices", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.ListServiceNowBusinessServices(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.ListServiceNowBusinessServices`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.ListServiceNowBusinessServices`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List ServiceNow business services returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowBusinessServicesResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listServiceNowBusinessServices", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    try {
      ServiceNowBusinessServicesResponse result =
          apiInstance.listServiceNowBusinessServices(
              UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceNowIntegrationApi#listServiceNowBusinessServices");
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
// List ServiceNow business services returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListServiceNowBusinessServices", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api
        .list_service_now_business_services(
            Uuid::parse_str("00000000-0000-0000-0000-000000000000").expect("invalid UUID"),
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
 * List ServiceNow business services returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listServiceNowBusinessServices"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

const params: v2.ServiceNowIntegrationApiListServiceNowBusinessServicesRequest =
  {
    instanceId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  };

apiInstance
  .listServiceNowBusinessServices(params)
  .then((data: v2.ServiceNowBusinessServicesResponse) => {
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

## List ServiceNow users{% #list-servicenow-users %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/users/{instance_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/users/{instance_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/users/{instance_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |

### Overview

Get all users for a ServiceNow instance.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                       |
| ----------------------------- | ------ | --------------------------------- |
| instance_id [*required*] | string | The ID of the ServiceNow instance |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow users

| Parent field | Field                         | Type     | Description                                                                |
| ------------ | ----------------------------- | -------- | -------------------------------------------------------------------------- |
|              | data [*required*]        | [object] | Array of ServiceNow user data objects                                      |
| data         | attributes [*required*]  | object   | Attributes of a ServiceNow user                                            |
| attributes   | email [*required*]       | string   | The email address of the user                                              |
| attributes   | full_name                     | string   | The full name of the user                                                  |
| attributes   | instance_id [*required*] | uuid     | The ID of the ServiceNow instance                                          |
| attributes   | user_name [*required*]   | string   | The username of the ServiceNow user                                        |
| attributes   | user_sys_id [*required*] | string   | The system ID of the user in ServiceNow                                    |
| data         | id [*required*]          | uuid     | Unique identifier for the ServiceNow user                                  |
| data         | type [*required*]        | enum     | Type identifier for ServiceNow user resources Allowed enum values: `users` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "email": "john.doe@example.com",
        "full_name": "John Doe",
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "user_name": "john.doe",
        "user_sys_id": "abc123def456"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "users"
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
                  \# Path parametersexport instance_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/users/${instance_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List ServiceNow users returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["list_service_now_users"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.list_service_now_users(
        instance_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List ServiceNow users returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_service_now_users".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new
p api_instance.list_service_now_users("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List ServiceNow users returns "OK" response

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
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListServiceNowUsers", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.ListServiceNowUsers(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.ListServiceNowUsers`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.ListServiceNowUsers`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List ServiceNow users returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowUsersResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listServiceNowUsers", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    try {
      ServiceNowUsersResponse result =
          apiInstance.listServiceNowUsers(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceNowIntegrationApi#listServiceNowUsers");
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
// List ServiceNow users returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListServiceNowUsers", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api
        .list_service_now_users(
            Uuid::parse_str("00000000-0000-0000-0000-000000000000").expect("invalid UUID"),
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
 * List ServiceNow users returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listServiceNowUsers"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

const params: v2.ServiceNowIntegrationApiListServiceNowUsersRequest = {
  instanceId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .listServiceNowUsers(params)
  .then((data: v2.ServiceNowUsersResponse) => {
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

## List ServiceNow instances{% #list-servicenow-instances %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/instances |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/instances |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/instances      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/instances      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/instances     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/instances |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/instances |

### Overview

Get all ServiceNow instances for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow instances

| Parent field | Field                           | Type     | Description                                                                       |
| ------------ | ------------------------------- | -------- | --------------------------------------------------------------------------------- |
|              | data [*required*]          | [object] | Array of ServiceNow instance data objects                                         |
| data         | attributes [*required*]    | object   | Attributes of a ServiceNow instance                                               |
| attributes   | instance_name [*required*] | string   | The name of the ServiceNow instance                                               |
| data         | id [*required*]            | uuid     | Unique identifier for the ServiceNow instance                                     |
| data         | type [*required*]          | enum     | Type identifier for ServiceNow instance resources Allowed enum values: `instance` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "instance_name": "my-servicenow-instance"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "instance"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/instances" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List ServiceNow instances returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_service_now_instances"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.list_service_now_instances()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List ServiceNow instances returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_service_now_instances".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceNowIntegrationAPI.new
p api_instance.list_service_now_instances()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List ServiceNow instances returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.ListServiceNowInstances", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceNowIntegrationApi(apiClient)
    resp, r, err := api.ListServiceNowInstances(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceNowIntegrationApi.ListServiceNowInstances`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceNowIntegrationApi.ListServiceNowInstances`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List ServiceNow instances returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceNowIntegrationApi;
import com.datadog.api.client.v2.model.ServiceNowInstancesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listServiceNowInstances", true);
    ServiceNowIntegrationApi apiInstance = new ServiceNowIntegrationApi(defaultClient);

    try {
      ServiceNowInstancesResponse result = apiInstance.listServiceNowInstances();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceNowIntegrationApi#listServiceNowInstances");
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
// List ServiceNow instances returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_now_integration::ServiceNowIntegrationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListServiceNowInstances", true);
    let api = ServiceNowIntegrationAPI::with_config(configuration);
    let resp = api.list_service_now_instances().await;
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
 * List ServiceNow instances returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listServiceNowInstances"] = true;
const apiInstance = new v2.ServiceNowIntegrationApi(configuration);

apiInstance
  .listServiceNowInstances()
  .then((data: v2.ServiceNowInstancesResponse) => {
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
