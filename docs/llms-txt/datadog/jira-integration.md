# Source: https://docs.datadoghq.com/api/latest/jira-integration.md

---
title: Jira Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Jira Integration
---

# Jira Integration

Manage your Jira Integration. Atlassian Jira is a project management and issue tracking tool for teams to coordinate work and handle tasks efficiently.

## Delete Jira issue template{% #delete-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |

### Overview

Delete a Jira issue template by ID.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                 |
| ----------------------------------- | ------ | ------------------------------------------- |
| issue_template_id [*required*] | string | The ID of the Jira issue template to delete |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport issue_template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/${issue_template_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Jira issue template returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_jira_issue_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    api_instance.delete_jira_issue_template(
        issue_template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Jira issue template returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_jira_issue_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::JiraIntegrationAPI.new
api_instance.delete_jira_issue_template("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete Jira issue template returns "No Content" response

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
	configuration.SetUnstableOperationEnabled("v2.DeleteJiraIssueTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewJiraIntegrationApi(apiClient)
	r, err := api.DeleteJiraIssueTemplate(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JiraIntegrationApi.DeleteJiraIssueTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Jira issue template returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.JiraIntegrationApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteJiraIssueTemplate", true);
    JiraIntegrationApi apiInstance = new JiraIntegrationApi(defaultClient);

    try {
      apiInstance.deleteJiraIssueTemplate(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
    } catch (ApiException e) {
      System.err.println("Exception when calling JiraIntegrationApi#deleteJiraIssueTemplate");
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
// Delete Jira issue template returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_jira_integration::JiraIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteJiraIssueTemplate", true);
    let api = JiraIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_jira_issue_template(
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
 * Delete Jira issue template returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteJiraIssueTemplate"] = true;
const apiInstance = new v2.JiraIntegrationApi(configuration);

const params: v2.JiraIntegrationApiDeleteJiraIssueTemplateRequest = {
  issueTemplateId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .deleteJiraIssueTemplate(params)
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

## Update Jira issue template{% #update-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |

### Overview

Update a Jira issue template by ID.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                 |
| ----------------------------------- | ------ | ------------------------------------------- |
| issue_template_id [*required*] | string | The ID of the Jira issue template to update |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                  |
| ------------ | ---------------------------- | ------ | -------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Data object for updating a Jira issue template                                               |
| data         | attributes [*required*] | object | Attributes for updating a Jira issue template                                                |
| attributes   | fields                       | object | Custom fields for the Jira issue template                                                    |
| attributes   | name                         | string | The name of the issue template                                                               |
| data         | type [*required*]       | enum   | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Updated Description",
          "type": "json"
        }
      },
      "name": "test_template_updated"
    },
    "type": "jira-issue-template"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single Jira issue template

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | object    | Data object for a Jira issue template                                                        |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test Description",
          "type": "json"
        }
      },
      "issue_type_id": "456",
      "name": "Test Template",
      "project_id": "123"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "relationships": {
      "jira-account": {
        "data": {
          "attributes": {
            "consumer_key": "consumer-key-1",
            "instance_url": "https://example.atlassian.net",
            "last_webhook_timestamp": "2024-01-15T10:30:00Z"
          },
          "id": "account-1",
          "type": "jira-account"
        }
      }
    },
    "type": "jira-issue-template"
  },
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
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
                  \# Path parametersexport issue_template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/${issue_template_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {},
    "type": "jira-issue-template"
  }
}
EOF
                
##### 

```python
"""
Update Jira issue template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType
from datadog_api_client.v2.model.jira_issue_template_update_request import JiraIssueTemplateUpdateRequest
from datadog_api_client.v2.model.jira_issue_template_update_request_attributes import (
    JiraIssueTemplateUpdateRequestAttributes,
)
from datadog_api_client.v2.model.jira_issue_template_update_request_data import JiraIssueTemplateUpdateRequestData
from uuid import UUID

body = JiraIssueTemplateUpdateRequest(
    data=JiraIssueTemplateUpdateRequestData(
        attributes=JiraIssueTemplateUpdateRequestAttributes(
            fields=dict([("description", "{'payload': 'Updated Description', 'type': 'json'}")]),
            name="test_template_updated",
        ),
        type=JiraIssueTemplateType.JIRA_ISSUE_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_jira_issue_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.update_jira_issue_template(
        issue_template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update Jira issue template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_jira_issue_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::JiraIntegrationAPI.new

body = DatadogAPIClient::V2::JiraIssueTemplateUpdateRequest.new({
  data: DatadogAPIClient::V2::JiraIssueTemplateUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::JiraIssueTemplateUpdateRequestAttributes.new({
      fields: {
        "description": "{'payload': 'Updated Description', 'type': 'json'}",
      },
      name: "test_template_updated",
    }),
    type: DatadogAPIClient::V2::JiraIssueTemplateType::JIRA_ISSUE_TEMPLATE,
  }),
})
p api_instance.update_jira_issue_template("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Update Jira issue template returns "OK" response

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
	body := datadogV2.JiraIssueTemplateUpdateRequest{
		Data: datadogV2.JiraIssueTemplateUpdateRequestData{
			Attributes: datadogV2.JiraIssueTemplateUpdateRequestAttributes{
				Fields: map[string]interface{}{
					"description": "{'payload': 'Updated Description', 'type': 'json'}",
				},
				Name: datadog.PtrString("test_template_updated"),
			},
			Type: datadogV2.JIRAISSUETEMPLATETYPE_JIRA_ISSUE_TEMPLATE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateJiraIssueTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewJiraIntegrationApi(apiClient)
	resp, r, err := api.UpdateJiraIssueTemplate(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JiraIntegrationApi.UpdateJiraIssueTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `JiraIntegrationApi.UpdateJiraIssueTemplate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update Jira issue template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.JiraIntegrationApi;
import com.datadog.api.client.v2.model.JiraIssueTemplateResponse;
import com.datadog.api.client.v2.model.JiraIssueTemplateType;
import com.datadog.api.client.v2.model.JiraIssueTemplateUpdateRequest;
import com.datadog.api.client.v2.model.JiraIssueTemplateUpdateRequestAttributes;
import com.datadog.api.client.v2.model.JiraIssueTemplateUpdateRequestData;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateJiraIssueTemplate", true);
    JiraIntegrationApi apiInstance = new JiraIntegrationApi(defaultClient);

    JiraIssueTemplateUpdateRequest body =
        new JiraIssueTemplateUpdateRequest()
            .data(
                new JiraIssueTemplateUpdateRequestData()
                    .attributes(
                        new JiraIssueTemplateUpdateRequestAttributes()
                            .fields(
                                Map.ofEntries(
                                    Map.entry(
                                        "description",
                                        "{'payload': 'Updated Description', 'type': 'json'}")))
                            .name("test_template_updated"))
                    .type(JiraIssueTemplateType.JIRA_ISSUE_TEMPLATE));

    try {
      JiraIssueTemplateResponse result =
          apiInstance.updateJiraIssueTemplate(
              UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"), body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JiraIntegrationApi#updateJiraIssueTemplate");
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
// Update Jira issue template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_jira_integration::JiraIntegrationAPI;
use datadog_api_client::datadogV2::model::JiraIssueTemplateType;
use datadog_api_client::datadogV2::model::JiraIssueTemplateUpdateRequest;
use datadog_api_client::datadogV2::model::JiraIssueTemplateUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::JiraIssueTemplateUpdateRequestData;
use std::collections::BTreeMap;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let body = JiraIssueTemplateUpdateRequest::new(JiraIssueTemplateUpdateRequestData::new(
        JiraIssueTemplateUpdateRequestAttributes::new()
            .fields(BTreeMap::from([]))
            .name("test_template_updated".to_string()),
        JiraIssueTemplateType::JIRA_ISSUE_TEMPLATE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateJiraIssueTemplate", true);
    let api = JiraIntegrationAPI::with_config(configuration);
    let resp = api
        .update_jira_issue_template(
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
 * Update Jira issue template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateJiraIssueTemplate"] = true;
const apiInstance = new v2.JiraIntegrationApi(configuration);

const params: v2.JiraIntegrationApiUpdateJiraIssueTemplateRequest = {
  body: {
    data: {
      attributes: {
        fields: {
          description: "{'payload': 'Updated Description', 'type': 'json'}",
        },
        name: "test_template_updated",
      },
      type: "jira-issue-template",
    },
  },
  issueTemplateId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .updateJiraIssueTemplate(params)
  .then((data: v2.JiraIssueTemplateResponse) => {
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

## Get Jira issue template{% #get-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |

### Overview

Get a Jira issue template by ID.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                   |
| ----------------------------------- | ------ | --------------------------------------------- |
| issue_template_id [*required*] | string | The ID of the Jira issue template to retrieve |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single Jira issue template

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | object    | Data object for a Jira issue template                                                        |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test Description",
          "type": "json"
        }
      },
      "issue_type_id": "456",
      "name": "Test Template",
      "project_id": "123"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "relationships": {
      "jira-account": {
        "data": {
          "attributes": {
            "consumer_key": "consumer-key-1",
            "instance_url": "https://example.atlassian.net",
            "last_webhook_timestamp": "2024-01-15T10:30:00Z"
          },
          "id": "account-1",
          "type": "jira-account"
        }
      }
    },
    "type": "jira-issue-template"
  },
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
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
                  \# Path parametersexport issue_template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/${issue_template_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get Jira issue template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_jira_issue_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.get_jira_issue_template(
        issue_template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get Jira issue template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_jira_issue_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::JiraIntegrationAPI.new
p api_instance.get_jira_issue_template("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get Jira issue template returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.GetJiraIssueTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewJiraIntegrationApi(apiClient)
	resp, r, err := api.GetJiraIssueTemplate(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JiraIntegrationApi.GetJiraIssueTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `JiraIntegrationApi.GetJiraIssueTemplate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get Jira issue template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.JiraIntegrationApi;
import com.datadog.api.client.v2.model.JiraIssueTemplateResponse;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getJiraIssueTemplate", true);
    JiraIntegrationApi apiInstance = new JiraIntegrationApi(defaultClient);

    try {
      JiraIssueTemplateResponse result =
          apiInstance.getJiraIssueTemplate(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JiraIntegrationApi#getJiraIssueTemplate");
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
// Get Jira issue template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_jira_integration::JiraIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetJiraIssueTemplate", true);
    let api = JiraIntegrationAPI::with_config(configuration);
    let resp = api
        .get_jira_issue_template(
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
 * Get Jira issue template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getJiraIssueTemplate"] = true;
const apiInstance = new v2.JiraIntegrationApi(configuration);

const params: v2.JiraIntegrationApiGetJiraIssueTemplateRequest = {
  issueTemplateId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .getJiraIssueTemplate(params)
  .then((data: v2.JiraIssueTemplateResponse) => {
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

## Create Jira issue template{% #create-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/jira/issue-templates      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/jira/issue-templates      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/jira/issue-templates     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates |

### Overview

Create a new Jira issue template.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                | Type   | Description                                                                                  |
| ------------ | -------------------- | ------ | -------------------------------------------------------------------------------------------- |
|              | data                 | object | Data object for creating a Jira issue template                                               |
| data         | attributes           | object | Attributes for creating a Jira issue template                                                |
| attributes   | fields               | object | Custom fields for the Jira issue template                                                    |
| attributes   | issue_type_id        | string | The ID of the Jira issue type                                                                |
| attributes   | jira-account         | object | Reference to the Jira account                                                                |
| jira-account | id [*required*] | uuid   | The ID of the Jira account                                                                   |
| attributes   | name                 | string | The name of the issue template                                                               |
| attributes   | project_id           | string | The ID of the Jira project                                                                   |
| data         | type                 | enum   | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test",
          "type": "json"
        }
      },
      "issue_type_id": "12730",
      "jira-account": {
        "id": "80f16d40-1fba-486e-b1fc-983e6ca19bec"
      },
      "name": "test-template",
      "project_id": "10772"
    },
    "type": "jira-issue-template"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response containing a single Jira issue template

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | object    | Data object for a Jira issue template                                                        |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test Description",
          "type": "json"
        }
      },
      "issue_type_id": "456",
      "name": "Test Template",
      "project_id": "123"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "relationships": {
      "jira-account": {
        "data": {
          "attributes": {
            "consumer_key": "consumer-key-1",
            "instance_url": "https://example.atlassian.net",
            "last_webhook_timestamp": "2024-01-15T10:30:00Z"
          },
          "id": "account-1",
          "type": "jira-account"
        }
      }
    },
    "type": "jira-issue-template"
  },
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "jira-account": {
        "id": "80f16d40-1fba-486e-b1fc-983e6ca19bec"
      }
    }
  }
}
EOF
                
##### 

```python
"""
Create Jira issue template returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from datadog_api_client.v2.model.jira_issue_template_create_request import JiraIssueTemplateCreateRequest
from datadog_api_client.v2.model.jira_issue_template_create_request_attributes import (
    JiraIssueTemplateCreateRequestAttributes,
)
from datadog_api_client.v2.model.jira_issue_template_create_request_attributes_jira_account import (
    JiraIssueTemplateCreateRequestAttributesJiraAccount,
)
from datadog_api_client.v2.model.jira_issue_template_create_request_data import JiraIssueTemplateCreateRequestData
from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType
from uuid import UUID

body = JiraIssueTemplateCreateRequest(
    data=JiraIssueTemplateCreateRequestData(
        attributes=JiraIssueTemplateCreateRequestAttributes(
            fields=dict([("description", "{'payload': 'Test', 'type': 'json'}")]),
            issue_type_id="12730",
            jira_account=JiraIssueTemplateCreateRequestAttributesJiraAccount(
                id=UUID("80f16d40-1fba-486e-b1fc-983e6ca19bec"),
            ),
            name="test-template",
            project_id="10772",
        ),
        type=JiraIssueTemplateType.JIRA_ISSUE_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_jira_issue_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.create_jira_issue_template(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create Jira issue template returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_jira_issue_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::JiraIntegrationAPI.new

body = DatadogAPIClient::V2::JiraIssueTemplateCreateRequest.new({
  data: DatadogAPIClient::V2::JiraIssueTemplateCreateRequestData.new({
    attributes: DatadogAPIClient::V2::JiraIssueTemplateCreateRequestAttributes.new({
      fields: {
        "description": "{'payload': 'Test', 'type': 'json'}",
      },
      issue_type_id: "12730",
      jira_account: DatadogAPIClient::V2::JiraIssueTemplateCreateRequestAttributesJiraAccount.new({
        id: "80f16d40-1fba-486e-b1fc-983e6ca19bec",
      }),
      name: "test-template",
      project_id: "10772",
    }),
    type: DatadogAPIClient::V2::JiraIssueTemplateType::JIRA_ISSUE_TEMPLATE,
  }),
})
p api_instance.create_jira_issue_template(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Create Jira issue template returns "Created" response

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
	body := datadogV2.JiraIssueTemplateCreateRequest{
		Data: &datadogV2.JiraIssueTemplateCreateRequestData{
			Attributes: &datadogV2.JiraIssueTemplateCreateRequestAttributes{
				Fields: map[string]interface{}{
					"description": "{'payload': 'Test', 'type': 'json'}",
				},
				IssueTypeId: datadog.PtrString("12730"),
				JiraAccount: &datadogV2.JiraIssueTemplateCreateRequestAttributesJiraAccount{
					Id: uuid.MustParse("80f16d40-1fba-486e-b1fc-983e6ca19bec"),
				},
				Name:      datadog.PtrString("test-template"),
				ProjectId: datadog.PtrString("10772"),
			},
			Type: datadogV2.JIRAISSUETEMPLATETYPE_JIRA_ISSUE_TEMPLATE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateJiraIssueTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewJiraIntegrationApi(apiClient)
	resp, r, err := api.CreateJiraIssueTemplate(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JiraIntegrationApi.CreateJiraIssueTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `JiraIntegrationApi.CreateJiraIssueTemplate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create Jira issue template returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.JiraIntegrationApi;
import com.datadog.api.client.v2.model.JiraIssueTemplateCreateRequest;
import com.datadog.api.client.v2.model.JiraIssueTemplateCreateRequestAttributes;
import com.datadog.api.client.v2.model.JiraIssueTemplateCreateRequestAttributesJiraAccount;
import com.datadog.api.client.v2.model.JiraIssueTemplateCreateRequestData;
import com.datadog.api.client.v2.model.JiraIssueTemplateResponse;
import com.datadog.api.client.v2.model.JiraIssueTemplateType;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createJiraIssueTemplate", true);
    JiraIntegrationApi apiInstance = new JiraIntegrationApi(defaultClient);

    JiraIssueTemplateCreateRequest body =
        new JiraIssueTemplateCreateRequest()
            .data(
                new JiraIssueTemplateCreateRequestData()
                    .attributes(
                        new JiraIssueTemplateCreateRequestAttributes()
                            .fields(
                                Map.ofEntries(
                                    Map.entry(
                                        "description", "{'payload': 'Test', 'type': 'json'}")))
                            .issueTypeId("12730")
                            .jiraAccount(
                                new JiraIssueTemplateCreateRequestAttributesJiraAccount()
                                    .id(UUID.fromString("80f16d40-1fba-486e-b1fc-983e6ca19bec")))
                            .name("test-template")
                            .projectId("10772"))
                    .type(JiraIssueTemplateType.JIRA_ISSUE_TEMPLATE));

    try {
      JiraIssueTemplateResponse result = apiInstance.createJiraIssueTemplate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JiraIntegrationApi#createJiraIssueTemplate");
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
// Create Jira issue template returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_jira_integration::JiraIntegrationAPI;
use datadog_api_client::datadogV2::model::JiraIssueTemplateCreateRequest;
use datadog_api_client::datadogV2::model::JiraIssueTemplateCreateRequestAttributes;
use datadog_api_client::datadogV2::model::JiraIssueTemplateCreateRequestAttributesJiraAccount;
use datadog_api_client::datadogV2::model::JiraIssueTemplateCreateRequestData;
use datadog_api_client::datadogV2::model::JiraIssueTemplateType;
use std::collections::BTreeMap;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let body = JiraIssueTemplateCreateRequest::new().data(
        JiraIssueTemplateCreateRequestData::new()
            .attributes(
                JiraIssueTemplateCreateRequestAttributes::new()
                    .fields(BTreeMap::from([]))
                    .issue_type_id("12730".to_string())
                    .jira_account(JiraIssueTemplateCreateRequestAttributesJiraAccount::new(
                        Uuid::parse_str("80f16d40-1fba-486e-b1fc-983e6ca19bec")
                            .expect("invalid UUID"),
                    ))
                    .name("test-template".to_string())
                    .project_id("10772".to_string()),
            )
            .type_(JiraIssueTemplateType::JIRA_ISSUE_TEMPLATE),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateJiraIssueTemplate", true);
    let api = JiraIntegrationAPI::with_config(configuration);
    let resp = api.create_jira_issue_template(body).await;
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
 * Create Jira issue template returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createJiraIssueTemplate"] = true;
const apiInstance = new v2.JiraIntegrationApi(configuration);

const params: v2.JiraIntegrationApiCreateJiraIssueTemplateRequest = {
  body: {
    data: {
      attributes: {
        fields: {
          description: "{'payload': 'Test', 'type': 'json'}",
        },
        issueTypeId: "12730",
        jiraAccount: {
          id: "80f16d40-1fba-486e-b1fc-983e6ca19bec",
        },
        name: "test-template",
        projectId: "10772",
      },
      type: "jira-issue-template",
    },
  },
};

apiInstance
  .createJiraIssueTemplate(params)
  .then((data: v2.JiraIssueTemplateResponse) => {
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

## List Jira issue templates{% #list-jira-issue-templates %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/jira/issue-templates      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/jira/issue-templates      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/jira/issue-templates     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates |

### Overview

Get all Jira issue templates for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing Jira issue templates

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | [object]  | Array of Jira issue template data objects                                                    |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "fields": {
          "description": {
            "payload": "Test Description",
            "type": "json"
          }
        },
        "issue_type_id": "456",
        "name": "Test Template",
        "project_id": "123"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "relationships": {
        "jira-account": {
          "data": {
            "attributes": {
              "consumer_key": "consumer-key-1",
              "instance_url": "https://example.atlassian.net",
              "last_webhook_timestamp": "2024-01-15T10:30:00Z"
            },
            "id": "account-1",
            "type": "jira-account"
          }
        }
      },
      "type": "jira-issue-template"
    }
  ],
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Jira issue templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_jira_issue_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.list_jira_issue_templates()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Jira issue templates returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_jira_issue_templates".to_sym] = true
end
api_instance = DatadogAPIClient::V2::JiraIntegrationAPI.new
p api_instance.list_jira_issue_templates()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List Jira issue templates returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListJiraIssueTemplates", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewJiraIntegrationApi(apiClient)
	resp, r, err := api.ListJiraIssueTemplates(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JiraIntegrationApi.ListJiraIssueTemplates`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `JiraIntegrationApi.ListJiraIssueTemplates`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List Jira issue templates returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.JiraIntegrationApi;
import com.datadog.api.client.v2.model.JiraIssueTemplatesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listJiraIssueTemplates", true);
    JiraIntegrationApi apiInstance = new JiraIntegrationApi(defaultClient);

    try {
      JiraIssueTemplatesResponse result = apiInstance.listJiraIssueTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JiraIntegrationApi#listJiraIssueTemplates");
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
// List Jira issue templates returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_jira_integration::JiraIntegrationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListJiraIssueTemplates", true);
    let api = JiraIntegrationAPI::with_config(configuration);
    let resp = api.list_jira_issue_templates().await;
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
 * List Jira issue templates returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listJiraIssueTemplates"] = true;
const apiInstance = new v2.JiraIntegrationApi(configuration);

apiInstance
  .listJiraIssueTemplates()
  .then((data: v2.JiraIssueTemplatesResponse) => {
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

## Delete Jira account{% #delete-jira-account %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/jira/accounts/{account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/jira/accounts/{account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/jira/accounts/{account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |

### Overview

Delete a Jira account by ID.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                          |
| ---------------------------- | ------ | ------------------------------------ |
| account_id [*required*] | string | The ID of the Jira account to delete |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport account_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Jira account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_jira_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    api_instance.delete_jira_account(
        account_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Jira account returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_jira_account".to_sym] = true
end
api_instance = DatadogAPIClient::V2::JiraIntegrationAPI.new
api_instance.delete_jira_account("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete Jira account returns "No Content" response

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
	configuration.SetUnstableOperationEnabled("v2.DeleteJiraAccount", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewJiraIntegrationApi(apiClient)
	r, err := api.DeleteJiraAccount(ctx, uuid.MustParse("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JiraIntegrationApi.DeleteJiraAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Jira account returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.JiraIntegrationApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteJiraAccount", true);
    JiraIntegrationApi apiInstance = new JiraIntegrationApi(defaultClient);

    try {
      apiInstance.deleteJiraAccount(UUID.fromString("65b3341b-0680-47f9-a6d4-134db45c603e"));
    } catch (ApiException e) {
      System.err.println("Exception when calling JiraIntegrationApi#deleteJiraAccount");
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
// Delete Jira account returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_jira_integration::JiraIntegrationAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteJiraAccount", true);
    let api = JiraIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_jira_account(
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
 * Delete Jira account returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteJiraAccount"] = true;
const apiInstance = new v2.JiraIntegrationApi(configuration);

const params: v2.JiraIntegrationApiDeleteJiraAccountRequest = {
  accountId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
};

apiInstance
  .deleteJiraAccount(params)
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

## List Jira accounts{% #list-jira-accounts %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/jira/accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/jira/accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/jira/accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/jira/accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/jira/accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/jira/accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/jira/accounts |

### Overview

Get all Jira accounts for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing Jira accounts

| Parent field | Field                          | Type      | Description                                                                    |
| ------------ | ------------------------------ | --------- | ------------------------------------------------------------------------------ |
|              | data [*required*]         | [object]  | Array of Jira account data objects                                             |
| data         | attributes [*required*]   | object    | Attributes of a Jira account                                                   |
| attributes   | consumer_key [*required*] | string    | The consumer key for the Jira account                                          |
| attributes   | instance_url [*required*] | string    | The URL of the Jira instance                                                   |
| attributes   | last_webhook_timestamp         | date-time | Timestamp of the last webhook received                                         |
| data         | id [*required*]           | string    | Unique identifier for the Jira account                                         |
| data         | type [*required*]         | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account` |
|              | meta                           | object    | Metadata for Jira accounts response                                            |
| meta         | public_key                     | string    | Public key for the Jira integration                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
    }
  ],
  "meta": {
    "public_key": "c29tZSBkYXRhIHdpdGggACBhbmQg77u/"
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Jira accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_jira_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.list_jira_accounts()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Jira accounts returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_jira_accounts".to_sym] = true
end
api_instance = DatadogAPIClient::V2::JiraIntegrationAPI.new
p api_instance.list_jira_accounts()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List Jira accounts returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListJiraAccounts", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewJiraIntegrationApi(apiClient)
	resp, r, err := api.ListJiraAccounts(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JiraIntegrationApi.ListJiraAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `JiraIntegrationApi.ListJiraAccounts`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List Jira accounts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.JiraIntegrationApi;
import com.datadog.api.client.v2.model.JiraAccountsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listJiraAccounts", true);
    JiraIntegrationApi apiInstance = new JiraIntegrationApi(defaultClient);

    try {
      JiraAccountsResponse result = apiInstance.listJiraAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JiraIntegrationApi#listJiraAccounts");
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
// List Jira accounts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_jira_integration::JiraIntegrationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListJiraAccounts", true);
    let api = JiraIntegrationAPI::with_config(configuration);
    let resp = api.list_jira_accounts().await;
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
 * List Jira accounts returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listJiraAccounts"] = true;
const apiInstance = new v2.JiraIntegrationApi(configuration);

apiInstance
  .listJiraAccounts()
  .then((data: v2.JiraAccountsResponse) => {
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
