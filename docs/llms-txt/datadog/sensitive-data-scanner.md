# Source: https://docs.datadoghq.com/api/latest/sensitive-data-scanner.md

---
title: Sensitive Data Scanner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Sensitive Data Scanner
---

# Sensitive Data Scanner

Create, update, delete, and retrieve sensitive data scanner groups and rules. See the [Sensitive Data Scanner page](https://docs.datadoghq.com/sensitive_data_scanner/) for more information.

## List Scanning Groups{% #list-scanning-groups %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/sensitive-data-scanner/config     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config |

### Overview

List all the Scanning groups in your organization. This endpoint requires the `data_scanner_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Get all groups response.

| Parent field                   | Field                             | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------ | --------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                | data                              | object          | Response data related to the scanning groups.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| data                           | attributes                        | object          | Attributes of the Sensitive Data configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| data                           | id                                | string          | ID of the configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| data                           | relationships                     | object          | Relationships of the configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| relationships                  | groups                            | object          | List of groups, ordered.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| groups                         | data                              | [object]        | List of groups. The order is important.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| data                           | id                                | string          | ID of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| data                           | type                              | enum            | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                                                                                                                                                                                                                                                                                                                                                                                                |
| data                           | type                              | enum            | Sensitive Data Scanner configuration type. Allowed enum values: `sensitive_data_scanner_configuration`                                                                                                                                                                                                                                                                                                                                                                                |
|                                | included                          | [ <oneOf>] | Included objects from relationships.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| included                       | Option 1                          | object          | A Scanning Rule included item.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Option 1                       | attributes                        | object          | Attributes of the Sensitive Data Scanner rule.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | description                       | string          | Description of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes                     | excluded_namespaces               | [string]        | Attributes excluded from the scan. If namespaces is provided, it has to be a sub-path of the namespaces array.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | included_keyword_configuration    | object          | Object defining a set of keywords and a number of characters that help reduce noise. You can provide a list of keywords you would like to check within a defined proximity of the matching pattern. If any of the keywords are found within the proximity check, the match is kept. If none are found, the match is discarded.                                                                                                                                                        |
| included_keyword_configuration | character_count [*required*] | int64           | The number of characters behind a match detected by Sensitive Data Scanner to look for the keywords defined. `character_count` should be greater than the maximum length of a keyword defined for a rule.                                                                                                                                                                                                                                                                             |
| included_keyword_configuration | keywords [*required*]        | [string]        | Keyword list that will be checked during scanning in order to validate a match. The number of keywords in the list must be less than or equal to 30.                                                                                                                                                                                                                                                                                                                                  |
| included_keyword_configuration | use_recommended_keywords          | boolean         | Should the rule use the underlying standard pattern keyword configuration. If set to `true`, the rule must be tied to a standard pattern. If set to `false`, the specified keywords and `character_count` are applied.                                                                                                                                                                                                                                                                |
| attributes                     | is_enabled                        | boolean         | Whether or not the rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes                     | name                              | string          | Name of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| attributes                     | namespaces                        | [string]        | Attributes included in the scan. If namespaces is empty or missing, all attributes except excluded_namespaces are scanned. If both are missing the whole event is scanned.                                                                                                                                                                                                                                                                                                            |
| attributes                     | pattern                           | string          | Not included if there is a relationship to a standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | priority                          | int64           | Integer from 1 (high) to 5 (low) indicating rule issue severity.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| attributes                     | suppressions                      | object          | Object describing the suppressions for a rule. There are three types of suppressions, `starts_with`, `ends_with`, and `exact_match`. Suppressed matches are not obfuscated, counted in metrics, or displayed in the Findings page.                                                                                                                                                                                                                                                    |
| suppressions                   | ends_with                         | [string]        | List of strings to use for suppression of matches ending with these strings.                                                                                                                                                                                                                                                                                                                                                                                                          |
| suppressions                   | exact_match                       | [string]        | List of strings to use for suppression of matches exactly matching these strings.                                                                                                                                                                                                                                                                                                                                                                                                     |
| suppressions                   | starts_with                       | [string]        | List of strings to use for suppression of matches starting with these strings.                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | tags                              | [string]        | List of tags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| attributes                     | text_replacement                  | object          | Object describing how the scanned event will be replaced.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | number_of_chars                   | int64           | Required if type == 'partial_replacement_from_beginning' or 'partial_replacement_from_end'. It must be > 0.                                                                                                                                                                                                                                                                                                                                                                           |
| text_replacement               | replacement_string                | string          | Required if type == 'replacement_string'.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | should_save_match                 | boolean         | Only valid when type == `replacement_string`. When enabled, matches can be unmasked in logs by users with 'Data Scanner Unmask' permission. As a security best practice, avoid masking for highly-sensitive, long-lived data.                                                                                                                                                                                                                                                         |
| text_replacement               | type                              | enum            | Type of the replacement text. None means no replacement. hash means the data will be stubbed. replacement_string means that one can chose a text to replace the data. partial_replacement_from_beginning allows a user to partially replace the data from the beginning, and partial_replacement_from_end on the other hand, allows to replace data from the end. Allowed enum values: `none,hash,replacement_string,partial_replacement_from_beginning,partial_replacement_from_end` |
| Option 1                       | id                                | string          | ID of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1                       | relationships                     | object          | Relationships of a scanning rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| relationships                  | group                             | object          | A scanning group data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| group                          | data                              | object          | A scanning group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| data                           | id                                | string          | ID of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| data                           | type                              | enum            | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                                                                                                                                                                                                                                                                                                                                                                                                |
| relationships                  | standard_pattern                  | object          | A standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| standard_pattern               | data                              | object          | Data containing the standard pattern id.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| data                           | id                                | string          | ID of the standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| data                           | type                              | enum            | Sensitive Data Scanner standard pattern type. Allowed enum values: `sensitive_data_scanner_standard_pattern`                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1                       | type                              | enum            | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                                                                                                                                                                                                                                                                                                                                                                                                  |
| included                       | Option 2                          | object          | A Scanning Group included item.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2                       | attributes                        | object          | Attributes of the Sensitive Data Scanner group.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes                     | description                       | string          | Description of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| attributes                     | filter                            | object          | Filter for the Scanning Group.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| filter                         | query                             | string          | Query to filter the events.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| attributes                     | is_enabled                        | boolean         | Whether or not the group is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| attributes                     | name                              | string          | Name of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| attributes                     | product_list                      | [string]        | List of products the scanning group applies.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes                     | samplings                         | [object]        | List of sampling rates per product type.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| samplings                      | product                           | enum            | Datadog product onto which Sensitive Data Scanner can be activated. Allowed enum values: `logs,rum,events,apm`                                                                                                                                                                                                                                                                                                                                                                        |
| samplings                      | rate                              | double          | Rate at which data in product type will be scanned, as a percentage.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 2                       | id                                | string          | ID of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 2                       | relationships                     | object          | Relationships of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| relationships                  | configuration                     | object          | A Sensitive Data Scanner configuration data.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| configuration                  | data                              | object          | A Sensitive Data Scanner configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| data                           | id                                | string          | ID of the configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| data                           | type                              | enum            | Sensitive Data Scanner configuration type. Allowed enum values: `sensitive_data_scanner_configuration`                                                                                                                                                                                                                                                                                                                                                                                |
| relationships                  | rules                             | object          | Rules included in the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| rules                          | data                              | [object]        | Rules included in the group. The order is important.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| data                           | id                                | string          | ID of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| data                           | type                              | enum            | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 2                       | type                              | enum            | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                                                                                                                                                                                                                                                                                                                                                                                                |
|                                | meta                              | object          | Meta response containing information about the API.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| meta                           | count_limit                       | int64           | Maximum number of scanning rules allowed for the org.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| meta                           | group_count_limit                 | int64           | Maximum number of scanning groups allowed for the org.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| meta                           | has_highlight_enabled             | boolean         | **DEPRECATED**: (Deprecated) Whether or not scanned events are highlighted in Logs or RUM for the org.                                                                                                                                                                                                                                                                                                                                                                                |
| meta                           | has_multi_pass_enabled            | boolean         | **DEPRECATED**: (Deprecated) Whether or not scanned events have multi-pass enabled.                                                                                                                                                                                                                                                                                                                                                                                                   |
| meta                           | is_pci_compliant                  | boolean         | Whether or not the org is compliant to the payment card industry standard.                                                                                                                                                                                                                                                                                                                                                                                                            |
| meta                           | version                           | int64           | Version of the API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {},
    "id": "string",
    "relationships": {
      "groups": {
        "data": [
          {
            "id": "string",
            "type": "sensitive_data_scanner_group"
          }
        ]
      }
    },
    "type": "sensitive_data_scanner_configuration"
  },
  "included": [
    {
      "attributes": {
        "description": "string",
        "excluded_namespaces": [
          "admin.name"
        ],
        "included_keyword_configuration": {
          "character_count": 30,
          "keywords": [
            "email",
            "address",
            "login"
          ],
          "use_recommended_keywords": false
        },
        "is_enabled": false,
        "name": "string",
        "namespaces": [
          "admin"
        ],
        "pattern": "string",
        "priority": "integer",
        "suppressions": {
          "ends_with": [
            "@example.com",
            "another.example.com"
          ],
          "exact_match": [
            "admin@example.com",
            "user@example.com"
          ],
          "starts_with": [
            "admin",
            "user"
          ]
        },
        "tags": [],
        "text_replacement": {
          "number_of_chars": "integer",
          "replacement_string": "string",
          "should_save_match": false,
          "type": "string"
        }
      },
      "id": "string",
      "relationships": {
        "group": {
          "data": {
            "id": "string",
            "type": "sensitive_data_scanner_group"
          }
        },
        "standard_pattern": {
          "data": {
            "id": "string",
            "type": "sensitive_data_scanner_standard_pattern"
          }
        }
      },
      "type": "sensitive_data_scanner_rule"
    }
  ],
  "meta": {
    "count_limit": "integer",
    "group_count_limit": "integer",
    "has_highlight_enabled": false,
    "has_multi_pass_enabled": false,
    "is_pci_compliant": false,
    "version": 0
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Scanning Groups returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.list_scanning_groups()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Scanning Groups returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new
p api_instance.list_scanning_groups()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List Scanning Groups returns "OK" response

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
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.ListScanningGroups(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.ListScanningGroups`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.ListScanningGroups`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List Scanning Groups returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerGetConfigResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    try {
      SensitiveDataScannerGetConfigResponse result = apiInstance.listScanningGroups();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#listScanningGroups");
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
// List Scanning Groups returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.list_scanning_groups().await;
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
 * List Scanning Groups returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

apiInstance
  .listScanningGroups()
  .then((data: v2.SensitiveDataScannerGetConfigResponse) => {
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

## Reorder Groups{% #reorder-groups %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/sensitive-data-scanner/config     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config |

### Overview

Reorder the list of groups. This endpoint requires the `data_scanner_write` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                  | Type     | Description                                                                                            |
| ------------- | ---------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
|               | data [*required*] | object   | Data related to the reordering of scanning groups.                                                     |
| data          | id                     | string   | ID of the configuration.                                                                               |
| data          | relationships          | object   | Relationships of the configuration.                                                                    |
| relationships | groups                 | object   | List of groups, ordered.                                                                               |
| groups        | data                   | [object] | List of groups. The order is important.                                                                |
| data          | id                     | string   | ID of the group.                                                                                       |
| data          | type                   | enum     | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                 |
| data          | type                   | enum     | Sensitive Data Scanner configuration type. Allowed enum values: `sensitive_data_scanner_configuration` |
|               | meta [*required*] | object   | Meta payload containing information about the API.                                                     |
| meta          | version                | int64    | Version of the API (optional).                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "relationships": {
      "groups": {
        "data": [
          {
            "type": "sensitive_data_scanner_group",
            "id": "string"
          }
        ]
      }
    },
    "type": "sensitive_data_scanner_configuration",
    "id": "55482444-d71c-c45c-7d1f-31984f64e6d2"
  },
  "meta": {}
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Group reorder response.

| Parent field | Field                  | Type    | Description                                                                                            |
| ------------ | ---------------------- | ------- | ------------------------------------------------------------------------------------------------------ |
|              | meta                   | object  | Meta response containing information about the API.                                                    |
| meta         | count_limit            | int64   | Maximum number of scanning rules allowed for the org.                                                  |
| meta         | group_count_limit      | int64   | Maximum number of scanning groups allowed for the org.                                                 |
| meta         | has_highlight_enabled  | boolean | **DEPRECATED**: (Deprecated) Whether or not scanned events are highlighted in Logs or RUM for the org. |
| meta         | has_multi_pass_enabled | boolean | **DEPRECATED**: (Deprecated) Whether or not scanned events have multi-pass enabled.                    |
| meta         | is_pci_compliant       | boolean | Whether or not the org is compliant to the payment card industry standard.                             |
| meta         | version                | int64   | Version of the API.                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {
    "count_limit": "integer",
    "group_count_limit": "integer",
    "has_highlight_enabled": false,
    "has_multi_pass_enabled": false,
    "is_pci_compliant": false,
    "version": 0
  }
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
                          \# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "relationships": {
      "groups": {
        "data": [
          {
            "type": "sensitive_data_scanner_group",
            "id": "string"
          }
        ]
      }
    },
    "type": "sensitive_data_scanner_configuration",
    "id": "55482444-d71c-c45c-7d1f-31984f64e6d2"
  },
  "meta": {}
}
EOF
                        
##### 

```go
// Reorder Groups returns "OK" response

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
	// there is a valid "scanning_group" in the system
	GroupDataID := os.Getenv("GROUP_DATA_ID")

	// a valid "configuration" in the system
	ConfigurationDataID := os.Getenv("CONFIGURATION_DATA_ID")

	body := datadogV2.SensitiveDataScannerConfigRequest{
		Data: datadogV2.SensitiveDataScannerReorderConfig{
			Relationships: &datadogV2.SensitiveDataScannerConfigurationRelationships{
				Groups: &datadogV2.SensitiveDataScannerGroupList{
					Data: []datadogV2.SensitiveDataScannerGroupItem{
						{
							Type: datadogV2.SENSITIVEDATASCANNERGROUPTYPE_SENSITIVE_DATA_SCANNER_GROUP.Ptr(),
							Id:   datadog.PtrString(GroupDataID),
						},
					},
				},
			},
			Type: datadogV2.SENSITIVEDATASCANNERCONFIGURATIONTYPE_SENSITIVE_DATA_SCANNER_CONFIGURATIONS.Ptr(),
			Id:   datadog.PtrString(ConfigurationDataID),
		},
		Meta: datadogV2.SensitiveDataScannerMetaVersionOnly{},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.ReorderScanningGroups(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.ReorderScanningGroups`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.ReorderScanningGroups`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Reorder Groups returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfigRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfigurationRelationships;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfigurationType;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupItem;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupList;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupType;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;
import com.datadog.api.client.v2.model.SensitiveDataScannerReorderConfig;
import com.datadog.api.client.v2.model.SensitiveDataScannerReorderGroupsResponse;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // there is a valid "scanning_group" in the system
    String GROUP_DATA_ID = System.getenv("GROUP_DATA_ID");

    // a valid "configuration" in the system
    String CONFIGURATION_DATA_ID = System.getenv("CONFIGURATION_DATA_ID");

    SensitiveDataScannerConfigRequest body =
        new SensitiveDataScannerConfigRequest()
            .data(
                new SensitiveDataScannerReorderConfig()
                    .relationships(
                        new SensitiveDataScannerConfigurationRelationships()
                            .groups(
                                new SensitiveDataScannerGroupList()
                                    .data(
                                        Collections.singletonList(
                                            new SensitiveDataScannerGroupItem()
                                                .type(
                                                    SensitiveDataScannerGroupType
                                                        .SENSITIVE_DATA_SCANNER_GROUP)
                                                .id(GROUP_DATA_ID)))))
                    .type(
                        SensitiveDataScannerConfigurationType.SENSITIVE_DATA_SCANNER_CONFIGURATIONS)
                    .id(CONFIGURATION_DATA_ID))
            .meta(new SensitiveDataScannerMetaVersionOnly());

    try {
      SensitiveDataScannerReorderGroupsResponse result = apiInstance.reorderScanningGroups(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#reorderScanningGroups");
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
Reorder Groups returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_config_request import SensitiveDataScannerConfigRequest
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_relationships import (
    SensitiveDataScannerConfigurationRelationships,
)
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_type import SensitiveDataScannerConfigurationType
from datadog_api_client.v2.model.sensitive_data_scanner_group_item import SensitiveDataScannerGroupItem
from datadog_api_client.v2.model.sensitive_data_scanner_group_list import SensitiveDataScannerGroupList
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_reorder_config import SensitiveDataScannerReorderConfig

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = environ["CONFIGURATION_DATA_ID"]

body = SensitiveDataScannerConfigRequest(
    data=SensitiveDataScannerReorderConfig(
        relationships=SensitiveDataScannerConfigurationRelationships(
            groups=SensitiveDataScannerGroupList(
                data=[
                    SensitiveDataScannerGroupItem(
                        type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
                        id=GROUP_DATA_ID,
                    ),
                ],
            ),
        ),
        type=SensitiveDataScannerConfigurationType.SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
        id=CONFIGURATION_DATA_ID,
    ),
    meta=SensitiveDataScannerMetaVersionOnly(),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.reorder_scanning_groups(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Reorder Groups returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = ENV["GROUP_DATA_ID"]

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = ENV["CONFIGURATION_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerConfigRequest.new({
  data: DatadogAPIClient::V2::SensitiveDataScannerReorderConfig.new({
    relationships: DatadogAPIClient::V2::SensitiveDataScannerConfigurationRelationships.new({
      groups: DatadogAPIClient::V2::SensitiveDataScannerGroupList.new({
        data: [
          DatadogAPIClient::V2::SensitiveDataScannerGroupItem.new({
            type: DatadogAPIClient::V2::SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP,
            id: GROUP_DATA_ID,
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::SensitiveDataScannerConfigurationType::SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
    id: CONFIGURATION_DATA_ID,
  }),
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
})
p api_instance.reorder_scanning_groups(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Reorder Groups returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfigRequest;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfigurationRelationships;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfigurationType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupItem;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupList;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;
use datadog_api_client::datadogV2::model::SensitiveDataScannerReorderConfig;

#[tokio::main]
async fn main() {
    // there is a valid "scanning_group" in the system
    let group_data_id = std::env::var("GROUP_DATA_ID").unwrap();

    // a valid "configuration" in the system
    let configuration_data_id = std::env::var("CONFIGURATION_DATA_ID").unwrap();
    let body = SensitiveDataScannerConfigRequest::new(
        SensitiveDataScannerReorderConfig::new()
            .id(configuration_data_id.clone())
            .relationships(
                SensitiveDataScannerConfigurationRelationships::new().groups(
                    SensitiveDataScannerGroupList::new().data(vec![
                        SensitiveDataScannerGroupItem::new()
                            .id(group_data_id.clone())
                            .type_(SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP),
                    ]),
                ),
            )
            .type_(SensitiveDataScannerConfigurationType::SENSITIVE_DATA_SCANNER_CONFIGURATIONS),
        SensitiveDataScannerMetaVersionOnly::new(),
    );
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.reorder_scanning_groups(body).await;
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
 * Reorder Groups returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// there is a valid "scanning_group" in the system
const GROUP_DATA_ID = process.env.GROUP_DATA_ID as string;

// a valid "configuration" in the system
const CONFIGURATION_DATA_ID = process.env.CONFIGURATION_DATA_ID as string;

const params: v2.SensitiveDataScannerApiReorderScanningGroupsRequest = {
  body: {
    data: {
      relationships: {
        groups: {
          data: [
            {
              type: "sensitive_data_scanner_group",
              id: GROUP_DATA_ID,
            },
          ],
        },
      },
      type: "sensitive_data_scanner_configuration",
      id: CONFIGURATION_DATA_ID,
    },
    meta: {},
  },
};

apiInstance
  .reorderScanningGroups(params)
  .then((data: v2.SensitiveDataScannerReorderGroupsResponse) => {
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

## List standard patterns{% #list-standard-patterns %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config/standard-patterns |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config/standard-patterns |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config/standard-patterns      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config/standard-patterns      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/sensitive-data-scanner/config/standard-patterns     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config/standard-patterns |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/standard-patterns |

### Overview

Returns all standard patterns. This endpoint requires the `data_scanner_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List Standard patterns response data.

| Parent field | Field             | Type     | Description                                                                                                                                                     |
| ------------ | ----------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data              | [object] | List Standard patterns response.                                                                                                                                |
| data         | attributes        | object   | Attributes of the Sensitive Data Scanner standard pattern.                                                                                                      |
| attributes   | description       | string   | Description of the standard pattern.                                                                                                                            |
| attributes   | included_keywords | [string] | List of included keywords.                                                                                                                                      |
| attributes   | name              | string   | Name of the standard pattern.                                                                                                                                   |
| attributes   | pattern           | string   | **DEPRECATED**: (Deprecated) Regex to match, optionally documented for older standard rules. Refer to the `description` field to understand what the rule does. |
| attributes   | priority          | int64    | Integer from 1 (high) to 5 (low) indicating standard pattern issue severity.                                                                                    |
| attributes   | tags              | [string] | List of tags.                                                                                                                                                   |
| data         | id                | string   | ID of the standard pattern.                                                                                                                                     |
| data         | type              | enum     | Sensitive Data Scanner standard pattern type. Allowed enum values: `sensitive_data_scanner_standard_pattern`                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "description": "string",
        "included_keywords": [],
        "name": "string",
        "pattern": "string",
        "priority": "integer",
        "tags": []
      },
      "id": "string",
      "type": "sensitive_data_scanner_standard_pattern"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/standard-patterns" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List standard patterns returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.list_standard_patterns()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List standard patterns returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new
p api_instance.list_standard_patterns()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List standard patterns returns "OK" response

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
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.ListStandardPatterns(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.ListStandardPatterns`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.ListStandardPatterns`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List standard patterns returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerStandardPatternsResponseData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    try {
      SensitiveDataScannerStandardPatternsResponseData result = apiInstance.listStandardPatterns();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#listStandardPatterns");
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
// List standard patterns returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.list_standard_patterns().await;
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
 * List standard patterns returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

apiInstance
  .listStandardPatterns()
  .then((data: v2.SensitiveDataScannerStandardPatternsResponseData) => {
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

## Create Scanning Group{% #create-scanning-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config/groups |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config/groups |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config/groups      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config/groups      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/sensitive-data-scanner/config/groups     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config/groups |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/groups |

### Overview

Create a scanning group. The request MAY include a configuration relationship. A rules relationship can be omitted entirely, but if it is included it MUST be null or an empty array (rules cannot be created at the same time). The new group will be ordered last within the configuration. This endpoint requires the `data_scanner_write` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                        | Type     | Description                                                                                                    |
| ------------- | ---------------------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
|               | data                         | object   | Data related to the creation of a group.                                                                       |
| data          | attributes [*required*] | object   | Attributes of the Sensitive Data Scanner group.                                                                |
| attributes    | description                  | string   | Description of the group.                                                                                      |
| attributes    | filter                       | object   | Filter for the Scanning Group.                                                                                 |
| filter        | query                        | string   | Query to filter the events.                                                                                    |
| attributes    | is_enabled                   | boolean  | Whether or not the group is enabled.                                                                           |
| attributes    | name                         | string   | Name of the group.                                                                                             |
| attributes    | product_list                 | [string] | List of products the scanning group applies.                                                                   |
| attributes    | samplings                    | [object] | List of sampling rates per product type.                                                                       |
| samplings     | product                      | enum     | Datadog product onto which Sensitive Data Scanner can be activated. Allowed enum values: `logs,rum,events,apm` |
| samplings     | rate                         | double   | Rate at which data in product type will be scanned, as a percentage.                                           |
| data          | relationships                | object   | Relationships of the group.                                                                                    |
| relationships | configuration                | object   | A Sensitive Data Scanner configuration data.                                                                   |
| configuration | data                         | object   | A Sensitive Data Scanner configuration.                                                                        |
| data          | id                           | string   | ID of the configuration.                                                                                       |
| data          | type                         | enum     | Sensitive Data Scanner configuration type. Allowed enum values: `sensitive_data_scanner_configuration`         |
| relationships | rules                        | object   | Rules included in the group.                                                                                   |
| rules         | data                         | [object] | Rules included in the group. The order is important.                                                           |
| data          | id                           | string   | ID of the rule.                                                                                                |
| data          | type                         | enum     | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                           |
| data          | type [*required*]       | enum     | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                         |
|               | meta                         | object   | Meta payload containing information about the API.                                                             |
| meta          | version                      | int64    | Version of the API (optional).                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {},
  "data": {
    "type": "sensitive_data_scanner_group",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "is_enabled": false,
      "product_list": [
        "logs"
      ],
      "filter": {
        "query": "*"
      }
    },
    "relationships": {
      "configuration": {
        "data": {
          "type": "sensitive_data_scanner_configuration",
          "id": "string"
        }
      },
      "rules": {
        "data": []
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Create group response.

| Parent field  | Field         | Type     | Description                                                                                                    |
| ------------- | ------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
|               | data          | object   | Response data related to the creation of a group.                                                              |
| data          | attributes    | object   | Attributes of the Sensitive Data Scanner group.                                                                |
| attributes    | description   | string   | Description of the group.                                                                                      |
| attributes    | filter        | object   | Filter for the Scanning Group.                                                                                 |
| filter        | query         | string   | Query to filter the events.                                                                                    |
| attributes    | is_enabled    | boolean  | Whether or not the group is enabled.                                                                           |
| attributes    | name          | string   | Name of the group.                                                                                             |
| attributes    | product_list  | [string] | List of products the scanning group applies.                                                                   |
| attributes    | samplings     | [object] | List of sampling rates per product type.                                                                       |
| samplings     | product       | enum     | Datadog product onto which Sensitive Data Scanner can be activated. Allowed enum values: `logs,rum,events,apm` |
| samplings     | rate          | double   | Rate at which data in product type will be scanned, as a percentage.                                           |
| data          | id            | string   | ID of the group.                                                                                               |
| data          | relationships | object   | Relationships of the group.                                                                                    |
| relationships | configuration | object   | A Sensitive Data Scanner configuration data.                                                                   |
| configuration | data          | object   | A Sensitive Data Scanner configuration.                                                                        |
| data          | id            | string   | ID of the configuration.                                                                                       |
| data          | type          | enum     | Sensitive Data Scanner configuration type. Allowed enum values: `sensitive_data_scanner_configuration`         |
| relationships | rules         | object   | Rules included in the group.                                                                                   |
| rules         | data          | [object] | Rules included in the group. The order is important.                                                           |
| data          | id            | string   | ID of the rule.                                                                                                |
| data          | type          | enum     | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                           |
| data          | type          | enum     | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                         |
|               | meta          | object   | Meta payload containing information about the API.                                                             |
| meta          | version       | int64    | Version of the API (optional).                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "string",
      "filter": {
        "query": "string"
      },
      "is_enabled": false,
      "name": "string",
      "product_list": [],
      "samplings": [
        {
          "product": "string",
          "rate": 100
        }
      ]
    },
    "id": "string",
    "relationships": {
      "configuration": {
        "data": {
          "id": "string",
          "type": "sensitive_data_scanner_configuration"
        }
      },
      "rules": {
        "data": [
          {
            "id": "string",
            "type": "sensitive_data_scanner_rule"
          }
        ]
      }
    },
    "type": "sensitive_data_scanner_group"
  },
  "meta": {
    "version": 0
  }
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/groups" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {},
  "data": {
    "type": "sensitive_data_scanner_group",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "is_enabled": false,
      "product_list": [
        "logs"
      ],
      "filter": {
        "query": "*"
      }
    },
    "relationships": {
      "configuration": {
        "data": {
          "type": "sensitive_data_scanner_configuration",
          "id": "string"
        }
      },
      "rules": {
        "data": []
      }
    }
  }
}
EOF
                        
##### 

```go
// Create Scanning Group returns "OK" response

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
	// a valid "configuration" in the system
	ConfigurationDataID := os.Getenv("CONFIGURATION_DATA_ID")

	body := datadogV2.SensitiveDataScannerGroupCreateRequest{
		Meta: &datadogV2.SensitiveDataScannerMetaVersionOnly{},
		Data: &datadogV2.SensitiveDataScannerGroupCreate{
			Type: datadogV2.SENSITIVEDATASCANNERGROUPTYPE_SENSITIVE_DATA_SCANNER_GROUP,
			Attributes: datadogV2.SensitiveDataScannerGroupAttributes{
				Name:      datadog.PtrString("Example-Sensitive-Data-Scanner"),
				IsEnabled: datadog.PtrBool(false),
				ProductList: []datadogV2.SensitiveDataScannerProduct{
					datadogV2.SENSITIVEDATASCANNERPRODUCT_LOGS,
				},
				Filter: &datadogV2.SensitiveDataScannerFilter{
					Query: datadog.PtrString("*"),
				},
			},
			Relationships: &datadogV2.SensitiveDataScannerGroupRelationships{
				Configuration: &datadogV2.SensitiveDataScannerConfigurationData{
					Data: &datadogV2.SensitiveDataScannerConfiguration{
						Type: datadogV2.SENSITIVEDATASCANNERCONFIGURATIONTYPE_SENSITIVE_DATA_SCANNER_CONFIGURATIONS.Ptr(),
						Id:   datadog.PtrString(ConfigurationDataID),
					},
				},
				Rules: &datadogV2.SensitiveDataScannerRuleData{
					Data: []datadogV2.SensitiveDataScannerRule{},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.CreateScanningGroup(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.CreateScanningGroup`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.CreateScanningGroup`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create Scanning Group returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfiguration;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfigurationData;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfigurationType;
import com.datadog.api.client.v2.model.SensitiveDataScannerCreateGroupResponse;
import com.datadog.api.client.v2.model.SensitiveDataScannerFilter;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupAttributes;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupCreate;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupCreateRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupRelationships;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupType;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;
import com.datadog.api.client.v2.model.SensitiveDataScannerProduct;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleData;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // a valid "configuration" in the system
    String CONFIGURATION_DATA_ID = System.getenv("CONFIGURATION_DATA_ID");

    SensitiveDataScannerGroupCreateRequest body =
        new SensitiveDataScannerGroupCreateRequest()
            .meta(new SensitiveDataScannerMetaVersionOnly())
            .data(
                new SensitiveDataScannerGroupCreate()
                    .type(SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP)
                    .attributes(
                        new SensitiveDataScannerGroupAttributes()
                            .name("Example-Sensitive-Data-Scanner")
                            .isEnabled(false)
                            .productList(
                                Collections.singletonList(SensitiveDataScannerProduct.LOGS))
                            .filter(new SensitiveDataScannerFilter().query("*")))
                    .relationships(
                        new SensitiveDataScannerGroupRelationships()
                            .configuration(
                                new SensitiveDataScannerConfigurationData()
                                    .data(
                                        new SensitiveDataScannerConfiguration()
                                            .type(
                                                SensitiveDataScannerConfigurationType
                                                    .SENSITIVE_DATA_SCANNER_CONFIGURATIONS)
                                            .id(CONFIGURATION_DATA_ID)))
                            .rules(new SensitiveDataScannerRuleData())));

    try {
      SensitiveDataScannerCreateGroupResponse result = apiInstance.createScanningGroup(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#createScanningGroup");
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
Create Scanning Group returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_configuration import SensitiveDataScannerConfiguration
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_data import SensitiveDataScannerConfigurationData
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_type import SensitiveDataScannerConfigurationType
from datadog_api_client.v2.model.sensitive_data_scanner_filter import SensitiveDataScannerFilter
from datadog_api_client.v2.model.sensitive_data_scanner_group_attributes import SensitiveDataScannerGroupAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_group_create import SensitiveDataScannerGroupCreate
from datadog_api_client.v2.model.sensitive_data_scanner_group_create_request import (
    SensitiveDataScannerGroupCreateRequest,
)
from datadog_api_client.v2.model.sensitive_data_scanner_group_relationships import (
    SensitiveDataScannerGroupRelationships,
)
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_product import SensitiveDataScannerProduct
from datadog_api_client.v2.model.sensitive_data_scanner_rule_data import SensitiveDataScannerRuleData

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = environ["CONFIGURATION_DATA_ID"]

body = SensitiveDataScannerGroupCreateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerGroupCreate(
        type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
        attributes=SensitiveDataScannerGroupAttributes(
            name="Example-Sensitive-Data-Scanner",
            is_enabled=False,
            product_list=[
                SensitiveDataScannerProduct.LOGS,
            ],
            filter=SensitiveDataScannerFilter(
                query="*",
            ),
        ),
        relationships=SensitiveDataScannerGroupRelationships(
            configuration=SensitiveDataScannerConfigurationData(
                data=SensitiveDataScannerConfiguration(
                    type=SensitiveDataScannerConfigurationType.SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
                    id=CONFIGURATION_DATA_ID,
                ),
            ),
            rules=SensitiveDataScannerRuleData(
                data=[],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.create_scanning_group(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create Scanning Group returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = ENV["CONFIGURATION_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerGroupCreateRequest.new({
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
  data: DatadogAPIClient::V2::SensitiveDataScannerGroupCreate.new({
    type: DatadogAPIClient::V2::SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP,
    attributes: DatadogAPIClient::V2::SensitiveDataScannerGroupAttributes.new({
      name: "Example-Sensitive-Data-Scanner",
      is_enabled: false,
      product_list: [
        DatadogAPIClient::V2::SensitiveDataScannerProduct::LOGS,
      ],
      filter: DatadogAPIClient::V2::SensitiveDataScannerFilter.new({
        query: "*",
      }),
    }),
    relationships: DatadogAPIClient::V2::SensitiveDataScannerGroupRelationships.new({
      configuration: DatadogAPIClient::V2::SensitiveDataScannerConfigurationData.new({
        data: DatadogAPIClient::V2::SensitiveDataScannerConfiguration.new({
          type: DatadogAPIClient::V2::SensitiveDataScannerConfigurationType::SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
          id: CONFIGURATION_DATA_ID,
        }),
      }),
      rules: DatadogAPIClient::V2::SensitiveDataScannerRuleData.new({
        data: [],
      }),
    }),
  }),
})
p api_instance.create_scanning_group(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create Scanning Group returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfiguration;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfigurationData;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfigurationType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerFilter;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupAttributes;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupCreate;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupCreateRequest;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupRelationships;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;
use datadog_api_client::datadogV2::model::SensitiveDataScannerProduct;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleData;

#[tokio::main]
async fn main() {
    // a valid "configuration" in the system
    let configuration_data_id = std::env::var("CONFIGURATION_DATA_ID").unwrap();
    let body =
        SensitiveDataScannerGroupCreateRequest::new()
            .data(
                SensitiveDataScannerGroupCreate::new(
                    SensitiveDataScannerGroupAttributes::new()
                        .filter(SensitiveDataScannerFilter::new().query("*".to_string()))
                        .is_enabled(false)
                        .name("Example-Sensitive-Data-Scanner".to_string())
                        .product_list(vec![SensitiveDataScannerProduct::LOGS]),
                    SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP,
                ).relationships(
                    SensitiveDataScannerGroupRelationships::new()
                        .configuration(
                            SensitiveDataScannerConfigurationData
                            ::new().data(
                                SensitiveDataScannerConfiguration::new()
                                    .id(configuration_data_id.clone())
                                    .type_(
                                        SensitiveDataScannerConfigurationType::SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
                                    ),
                            ),
                        )
                        .rules(SensitiveDataScannerRuleData::new().data(vec![])),
                ),
            )
            .meta(SensitiveDataScannerMetaVersionOnly::new());
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.create_scanning_group(body).await;
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
 * Create Scanning Group returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// a valid "configuration" in the system
const CONFIGURATION_DATA_ID = process.env.CONFIGURATION_DATA_ID as string;

const params: v2.SensitiveDataScannerApiCreateScanningGroupRequest = {
  body: {
    meta: {},
    data: {
      type: "sensitive_data_scanner_group",
      attributes: {
        name: "Example-Sensitive-Data-Scanner",
        isEnabled: false,
        productList: ["logs"],
        filter: {
          query: "*",
        },
      },
      relationships: {
        configuration: {
          data: {
            type: "sensitive_data_scanner_configuration",
            id: CONFIGURATION_DATA_ID,
          },
        },
        rules: {
          data: [],
        },
      },
    },
  },
};

apiInstance
  .createScanningGroup(params)
  .then((data: v2.SensitiveDataScannerCreateGroupResponse) => {
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

## Update Scanning Group{% #update-scanning-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config/groups/{group_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config/groups/{group_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |

### Overview

Update a group, including the order of the rules. Rules within the group are reordered by including a rules relationship. If the rules relationship is present, its data section MUST contain linkages for all of the rules currently in the group, and MUST NOT contain any others. This endpoint requires the `data_scanner_write` permission.

### Arguments

#### Path Parameters

| Name                       | Type   | Description                 |
| -------------------------- | ------ | --------------------------- |
| group_id [*required*] | string | The ID of a group of rules. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                  | Type     | Description                                                                                                    |
| ------------- | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
|               | data [*required*] | object   | Data related to the update of a group.                                                                         |
| data          | attributes             | object   | Attributes of the Sensitive Data Scanner group.                                                                |
| attributes    | description            | string   | Description of the group.                                                                                      |
| attributes    | filter                 | object   | Filter for the Scanning Group.                                                                                 |
| filter        | query                  | string   | Query to filter the events.                                                                                    |
| attributes    | is_enabled             | boolean  | Whether or not the group is enabled.                                                                           |
| attributes    | name                   | string   | Name of the group.                                                                                             |
| attributes    | product_list           | [string] | List of products the scanning group applies.                                                                   |
| attributes    | samplings              | [object] | List of sampling rates per product type.                                                                       |
| samplings     | product                | enum     | Datadog product onto which Sensitive Data Scanner can be activated. Allowed enum values: `logs,rum,events,apm` |
| samplings     | rate                   | double   | Rate at which data in product type will be scanned, as a percentage.                                           |
| data          | id                     | string   | ID of the group.                                                                                               |
| data          | relationships          | object   | Relationships of the group.                                                                                    |
| relationships | configuration          | object   | A Sensitive Data Scanner configuration data.                                                                   |
| configuration | data                   | object   | A Sensitive Data Scanner configuration.                                                                        |
| data          | id                     | string   | ID of the configuration.                                                                                       |
| data          | type                   | enum     | Sensitive Data Scanner configuration type. Allowed enum values: `sensitive_data_scanner_configuration`         |
| relationships | rules                  | object   | Rules included in the group.                                                                                   |
| rules         | data                   | [object] | Rules included in the group. The order is important.                                                           |
| data          | id                     | string   | ID of the rule.                                                                                                |
| data          | type                   | enum     | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                           |
| data          | type                   | enum     | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                         |
|               | meta [*required*] | object   | Meta payload containing information about the API.                                                             |
| meta          | version                | int64    | Version of the API (optional).                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {},
  "data": {
    "id": "string",
    "type": "sensitive_data_scanner_group",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "is_enabled": false,
      "product_list": [
        "logs"
      ],
      "filter": {
        "query": "*"
      }
    },
    "relationships": {
      "configuration": {
        "data": {
          "type": "sensitive_data_scanner_configuration",
          "id": "55482444-d71c-c45c-7d1f-31984f64e6d2"
        }
      },
      "rules": {
        "data": []
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Update group response.

| Parent field | Field   | Type   | Description                                        |
| ------------ | ------- | ------ | -------------------------------------------------- |
|              | meta    | object | Meta payload containing information about the API. |
| meta         | version | int64  | Version of the API (optional).                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {
    "version": 0
  }
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
                          \# Path parametersexport group_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/${group_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {},
  "data": {
    "id": "string",
    "type": "sensitive_data_scanner_group",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "is_enabled": false,
      "product_list": [
        "logs"
      ],
      "filter": {
        "query": "*"
      }
    },
    "relationships": {
      "configuration": {
        "data": {
          "type": "sensitive_data_scanner_configuration",
          "id": "55482444-d71c-c45c-7d1f-31984f64e6d2"
        }
      },
      "rules": {
        "data": []
      }
    }
  }
}
EOF
                        
##### 

```go
// Update Scanning Group returns "OK" response

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
	// there is a valid "scanning_group" in the system
	GroupDataID := os.Getenv("GROUP_DATA_ID")

	// a valid "configuration" in the system
	ConfigurationDataID := os.Getenv("CONFIGURATION_DATA_ID")

	body := datadogV2.SensitiveDataScannerGroupUpdateRequest{
		Meta: datadogV2.SensitiveDataScannerMetaVersionOnly{},
		Data: datadogV2.SensitiveDataScannerGroupUpdate{
			Id:   datadog.PtrString(GroupDataID),
			Type: datadogV2.SENSITIVEDATASCANNERGROUPTYPE_SENSITIVE_DATA_SCANNER_GROUP.Ptr(),
			Attributes: &datadogV2.SensitiveDataScannerGroupAttributes{
				Name:      datadog.PtrString("Example-Sensitive-Data-Scanner"),
				IsEnabled: datadog.PtrBool(false),
				ProductList: []datadogV2.SensitiveDataScannerProduct{
					datadogV2.SENSITIVEDATASCANNERPRODUCT_LOGS,
				},
				Filter: &datadogV2.SensitiveDataScannerFilter{
					Query: datadog.PtrString("*"),
				},
			},
			Relationships: &datadogV2.SensitiveDataScannerGroupRelationships{
				Configuration: &datadogV2.SensitiveDataScannerConfigurationData{
					Data: &datadogV2.SensitiveDataScannerConfiguration{
						Type: datadogV2.SENSITIVEDATASCANNERCONFIGURATIONTYPE_SENSITIVE_DATA_SCANNER_CONFIGURATIONS.Ptr(),
						Id:   datadog.PtrString(ConfigurationDataID),
					},
				},
				Rules: &datadogV2.SensitiveDataScannerRuleData{
					Data: []datadogV2.SensitiveDataScannerRule{},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.UpdateScanningGroup(ctx, GroupDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.UpdateScanningGroup`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.UpdateScanningGroup`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update Scanning Group returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfiguration;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfigurationData;
import com.datadog.api.client.v2.model.SensitiveDataScannerConfigurationType;
import com.datadog.api.client.v2.model.SensitiveDataScannerFilter;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupAttributes;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupRelationships;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupType;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupUpdate;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupUpdateRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupUpdateResponse;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;
import com.datadog.api.client.v2.model.SensitiveDataScannerProduct;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleData;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // there is a valid "scanning_group" in the system
    String GROUP_DATA_ID = System.getenv("GROUP_DATA_ID");

    // a valid "configuration" in the system
    String CONFIGURATION_DATA_ID = System.getenv("CONFIGURATION_DATA_ID");

    SensitiveDataScannerGroupUpdateRequest body =
        new SensitiveDataScannerGroupUpdateRequest()
            .meta(new SensitiveDataScannerMetaVersionOnly())
            .data(
                new SensitiveDataScannerGroupUpdate()
                    .id(GROUP_DATA_ID)
                    .type(SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP)
                    .attributes(
                        new SensitiveDataScannerGroupAttributes()
                            .name("Example-Sensitive-Data-Scanner")
                            .isEnabled(false)
                            .productList(
                                Collections.singletonList(SensitiveDataScannerProduct.LOGS))
                            .filter(new SensitiveDataScannerFilter().query("*")))
                    .relationships(
                        new SensitiveDataScannerGroupRelationships()
                            .configuration(
                                new SensitiveDataScannerConfigurationData()
                                    .data(
                                        new SensitiveDataScannerConfiguration()
                                            .type(
                                                SensitiveDataScannerConfigurationType
                                                    .SENSITIVE_DATA_SCANNER_CONFIGURATIONS)
                                            .id(CONFIGURATION_DATA_ID)))
                            .rules(new SensitiveDataScannerRuleData())));

    try {
      SensitiveDataScannerGroupUpdateResponse result =
          apiInstance.updateScanningGroup(GROUP_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#updateScanningGroup");
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
Update Scanning Group returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_configuration import SensitiveDataScannerConfiguration
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_data import SensitiveDataScannerConfigurationData
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_type import SensitiveDataScannerConfigurationType
from datadog_api_client.v2.model.sensitive_data_scanner_filter import SensitiveDataScannerFilter
from datadog_api_client.v2.model.sensitive_data_scanner_group_attributes import SensitiveDataScannerGroupAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_group_relationships import (
    SensitiveDataScannerGroupRelationships,
)
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_group_update import SensitiveDataScannerGroupUpdate
from datadog_api_client.v2.model.sensitive_data_scanner_group_update_request import (
    SensitiveDataScannerGroupUpdateRequest,
)
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_product import SensitiveDataScannerProduct
from datadog_api_client.v2.model.sensitive_data_scanner_rule_data import SensitiveDataScannerRuleData

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = environ["CONFIGURATION_DATA_ID"]

body = SensitiveDataScannerGroupUpdateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerGroupUpdate(
        id=GROUP_DATA_ID,
        type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
        attributes=SensitiveDataScannerGroupAttributes(
            name="Example-Sensitive-Data-Scanner",
            is_enabled=False,
            product_list=[
                SensitiveDataScannerProduct.LOGS,
            ],
            filter=SensitiveDataScannerFilter(
                query="*",
            ),
        ),
        relationships=SensitiveDataScannerGroupRelationships(
            configuration=SensitiveDataScannerConfigurationData(
                data=SensitiveDataScannerConfiguration(
                    type=SensitiveDataScannerConfigurationType.SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
                    id=CONFIGURATION_DATA_ID,
                ),
            ),
            rules=SensitiveDataScannerRuleData(
                data=[],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.update_scanning_group(group_id=GROUP_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update Scanning Group returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = ENV["GROUP_DATA_ID"]

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = ENV["CONFIGURATION_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerGroupUpdateRequest.new({
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
  data: DatadogAPIClient::V2::SensitiveDataScannerGroupUpdate.new({
    id: GROUP_DATA_ID,
    type: DatadogAPIClient::V2::SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP,
    attributes: DatadogAPIClient::V2::SensitiveDataScannerGroupAttributes.new({
      name: "Example-Sensitive-Data-Scanner",
      is_enabled: false,
      product_list: [
        DatadogAPIClient::V2::SensitiveDataScannerProduct::LOGS,
      ],
      filter: DatadogAPIClient::V2::SensitiveDataScannerFilter.new({
        query: "*",
      }),
    }),
    relationships: DatadogAPIClient::V2::SensitiveDataScannerGroupRelationships.new({
      configuration: DatadogAPIClient::V2::SensitiveDataScannerConfigurationData.new({
        data: DatadogAPIClient::V2::SensitiveDataScannerConfiguration.new({
          type: DatadogAPIClient::V2::SensitiveDataScannerConfigurationType::SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
          id: CONFIGURATION_DATA_ID,
        }),
      }),
      rules: DatadogAPIClient::V2::SensitiveDataScannerRuleData.new({
        data: [],
      }),
    }),
  }),
})
p api_instance.update_scanning_group(GROUP_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update Scanning Group returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfiguration;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfigurationData;
use datadog_api_client::datadogV2::model::SensitiveDataScannerConfigurationType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerFilter;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupAttributes;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupRelationships;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupUpdate;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupUpdateRequest;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;
use datadog_api_client::datadogV2::model::SensitiveDataScannerProduct;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleData;

#[tokio::main]
async fn main() {
    // there is a valid "scanning_group" in the system
    let group_data_id = std::env::var("GROUP_DATA_ID").unwrap();

    // a valid "configuration" in the system
    let configuration_data_id = std::env::var("CONFIGURATION_DATA_ID").unwrap();
    let body =
        SensitiveDataScannerGroupUpdateRequest::new(
            SensitiveDataScannerGroupUpdate::new()
                .attributes(
                    SensitiveDataScannerGroupAttributes::new()
                        .filter(SensitiveDataScannerFilter::new().query("*".to_string()))
                        .is_enabled(false)
                        .name("Example-Sensitive-Data-Scanner".to_string())
                        .product_list(vec![SensitiveDataScannerProduct::LOGS]),
                )
                .id(group_data_id.clone())
                .relationships(
                    SensitiveDataScannerGroupRelationships::new()
                        .configuration(
                            SensitiveDataScannerConfigurationData
                            ::new().data(
                                SensitiveDataScannerConfiguration::new()
                                    .id(configuration_data_id.clone())
                                    .type_(
                                        SensitiveDataScannerConfigurationType::SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
                                    ),
                            ),
                        )
                        .rules(SensitiveDataScannerRuleData::new().data(vec![])),
                )
                .type_(SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP),
            SensitiveDataScannerMetaVersionOnly::new(),
        );
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.update_scanning_group(group_data_id.clone(), body).await;
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
 * Update Scanning Group returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// there is a valid "scanning_group" in the system
const GROUP_DATA_ID = process.env.GROUP_DATA_ID as string;

// a valid "configuration" in the system
const CONFIGURATION_DATA_ID = process.env.CONFIGURATION_DATA_ID as string;

const params: v2.SensitiveDataScannerApiUpdateScanningGroupRequest = {
  body: {
    meta: {},
    data: {
      id: GROUP_DATA_ID,
      type: "sensitive_data_scanner_group",
      attributes: {
        name: "Example-Sensitive-Data-Scanner",
        isEnabled: false,
        productList: ["logs"],
        filter: {
          query: "*",
        },
      },
      relationships: {
        configuration: {
          data: {
            type: "sensitive_data_scanner_configuration",
            id: CONFIGURATION_DATA_ID,
          },
        },
        rules: {
          data: [],
        },
      },
    },
  },
  groupId: GROUP_DATA_ID,
};

apiInstance
  .updateScanningGroup(params)
  .then((data: v2.SensitiveDataScannerGroupUpdateResponse) => {
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

## Delete Scanning Group{% #delete-scanning-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config/groups/{group_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config/groups/{group_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/{group_id} |

### Overview

Delete a given group. This endpoint requires the `data_scanner_write` permission.

### Arguments

#### Path Parameters

| Name                       | Type   | Description                 |
| -------------------------- | ------ | --------------------------- |
| group_id [*required*] | string | The ID of a group of rules. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                        |
| ------------ | ---------------------- | ------ | -------------------------------------------------- |
|              | meta [*required*] | object | Meta payload containing information about the API. |
| meta         | version                | int64  | Version of the API (optional).                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {}
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Delete group response.

| Parent field | Field   | Type   | Description                                        |
| ------------ | ------- | ------ | -------------------------------------------------- |
|              | meta    | object | Meta payload containing information about the API. |
| meta         | version | int64  | Version of the API (optional).                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {
    "version": 0
  }
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
                          \# Path parametersexport group_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/groups/${group_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {}
}
EOF
                        
##### 

```go
// Delete Scanning Group returns "OK" response

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
	// there is a valid "scanning_group" in the system
	GroupDataID := os.Getenv("GROUP_DATA_ID")

	body := datadogV2.SensitiveDataScannerGroupDeleteRequest{
		Meta: datadogV2.SensitiveDataScannerMetaVersionOnly{},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.DeleteScanningGroup(ctx, GroupDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.DeleteScanningGroup`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.DeleteScanningGroup`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Scanning Group returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupDeleteRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupDeleteResponse;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // there is a valid "scanning_group" in the system
    String GROUP_DATA_ID = System.getenv("GROUP_DATA_ID");

    SensitiveDataScannerGroupDeleteRequest body =
        new SensitiveDataScannerGroupDeleteRequest()
            .meta(new SensitiveDataScannerMetaVersionOnly());

    try {
      SensitiveDataScannerGroupDeleteResponse result =
          apiInstance.deleteScanningGroup(GROUP_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#deleteScanningGroup");
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
Delete Scanning Group returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_group_delete_request import (
    SensitiveDataScannerGroupDeleteRequest,
)
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

body = SensitiveDataScannerGroupDeleteRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.delete_scanning_group(group_id=GROUP_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Scanning Group returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = ENV["GROUP_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerGroupDeleteRequest.new({
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
})
p api_instance.delete_scanning_group(GROUP_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Delete Scanning Group returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupDeleteRequest;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;

#[tokio::main]
async fn main() {
    // there is a valid "scanning_group" in the system
    let group_data_id = std::env::var("GROUP_DATA_ID").unwrap();
    let body =
        SensitiveDataScannerGroupDeleteRequest::new(SensitiveDataScannerMetaVersionOnly::new());
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.delete_scanning_group(group_data_id.clone(), body).await;
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
 * Delete Scanning Group returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// there is a valid "scanning_group" in the system
const GROUP_DATA_ID = process.env.GROUP_DATA_ID as string;

const params: v2.SensitiveDataScannerApiDeleteScanningGroupRequest = {
  body: {
    meta: {},
  },
  groupId: GROUP_DATA_ID,
};

apiInstance
  .deleteScanningGroup(params)
  .then((data: v2.SensitiveDataScannerGroupDeleteResponse) => {
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

## Create Scanning Rule{% #create-scanning-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config/rules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config/rules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config/rules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config/rules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/sensitive-data-scanner/config/rules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config/rules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/rules |

### Overview

Create a scanning rule in a sensitive data scanner group, ordered last. The posted rule MUST include a group relationship. It MUST include either a standard_pattern relationship or a regex attribute, but not both. If included_attributes is empty or missing, we will scan all attributes except excluded_attributes. If both are missing, we will scan the whole event. This endpoint requires the `data_scanner_write` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field                   | Field                             | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------ | --------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                | data [*required*]            | object   | Data related to the creation of a rule.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| data                           | attributes [*required*]      | object   | Attributes of the Sensitive Data Scanner rule.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | description                       | string   | Description of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes                     | excluded_namespaces               | [string] | Attributes excluded from the scan. If namespaces is provided, it has to be a sub-path of the namespaces array.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | included_keyword_configuration    | object   | Object defining a set of keywords and a number of characters that help reduce noise. You can provide a list of keywords you would like to check within a defined proximity of the matching pattern. If any of the keywords are found within the proximity check, the match is kept. If none are found, the match is discarded.                                                                                                                                                        |
| included_keyword_configuration | character_count [*required*] | int64    | The number of characters behind a match detected by Sensitive Data Scanner to look for the keywords defined. `character_count` should be greater than the maximum length of a keyword defined for a rule.                                                                                                                                                                                                                                                                             |
| included_keyword_configuration | keywords [*required*]        | [string] | Keyword list that will be checked during scanning in order to validate a match. The number of keywords in the list must be less than or equal to 30.                                                                                                                                                                                                                                                                                                                                  |
| included_keyword_configuration | use_recommended_keywords          | boolean  | Should the rule use the underlying standard pattern keyword configuration. If set to `true`, the rule must be tied to a standard pattern. If set to `false`, the specified keywords and `character_count` are applied.                                                                                                                                                                                                                                                                |
| attributes                     | is_enabled                        | boolean  | Whether or not the rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes                     | name                              | string   | Name of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| attributes                     | namespaces                        | [string] | Attributes included in the scan. If namespaces is empty or missing, all attributes except excluded_namespaces are scanned. If both are missing the whole event is scanned.                                                                                                                                                                                                                                                                                                            |
| attributes                     | pattern                           | string   | Not included if there is a relationship to a standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | priority                          | int64    | Integer from 1 (high) to 5 (low) indicating rule issue severity.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| attributes                     | suppressions                      | object   | Object describing the suppressions for a rule. There are three types of suppressions, `starts_with`, `ends_with`, and `exact_match`. Suppressed matches are not obfuscated, counted in metrics, or displayed in the Findings page.                                                                                                                                                                                                                                                    |
| suppressions                   | ends_with                         | [string] | List of strings to use for suppression of matches ending with these strings.                                                                                                                                                                                                                                                                                                                                                                                                          |
| suppressions                   | exact_match                       | [string] | List of strings to use for suppression of matches exactly matching these strings.                                                                                                                                                                                                                                                                                                                                                                                                     |
| suppressions                   | starts_with                       | [string] | List of strings to use for suppression of matches starting with these strings.                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | tags                              | [string] | List of tags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| attributes                     | text_replacement                  | object   | Object describing how the scanned event will be replaced.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | number_of_chars                   | int64    | Required if type == 'partial_replacement_from_beginning' or 'partial_replacement_from_end'. It must be > 0.                                                                                                                                                                                                                                                                                                                                                                           |
| text_replacement               | replacement_string                | string   | Required if type == 'replacement_string'.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | should_save_match                 | boolean  | Only valid when type == `replacement_string`. When enabled, matches can be unmasked in logs by users with 'Data Scanner Unmask' permission. As a security best practice, avoid masking for highly-sensitive, long-lived data.                                                                                                                                                                                                                                                         |
| text_replacement               | type                              | enum     | Type of the replacement text. None means no replacement. hash means the data will be stubbed. replacement_string means that one can chose a text to replace the data. partial_replacement_from_beginning allows a user to partially replace the data from the beginning, and partial_replacement_from_end on the other hand, allows to replace data from the end. Allowed enum values: `none,hash,replacement_string,partial_replacement_from_beginning,partial_replacement_from_end` |
| data                           | relationships [*required*]   | object   | Relationships of a scanning rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| relationships                  | group                             | object   | A scanning group data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| group                          | data                              | object   | A scanning group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| data                           | id                                | string   | ID of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| data                           | type                              | enum     | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                                                                                                                                                                                                                                                                                                                                                                                                |
| relationships                  | standard_pattern                  | object   | A standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| standard_pattern               | data                              | object   | Data containing the standard pattern id.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| data                           | id                                | string   | ID of the standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| data                           | type                              | enum     | Sensitive Data Scanner standard pattern type. Allowed enum values: `sensitive_data_scanner_standard_pattern`                                                                                                                                                                                                                                                                                                                                                                          |
| data                           | type [*required*]            | enum     | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                | meta [*required*]            | object   | Meta payload containing information about the API.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| meta                           | version                           | int64    | Version of the API (optional).                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "meta": {},
  "data": {
    "type": "sensitive_data_scanner_rule",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "pattern": "pattern",
      "namespaces": [
        "admin"
      ],
      "excluded_namespaces": [
        "admin.name"
      ],
      "text_replacement": {
        "type": "none"
      },
      "tags": [
        "sensitive_data:true"
      ],
      "is_enabled": true,
      "priority": 1,
      "included_keyword_configuration": {
        "keywords": [
          "credit card"
        ],
        "character_count": 35
      }
    },
    "relationships": {
      "group": {
        "data": {
          "type": "sensitive_data_scanner_group",
          "id": "string"
        }
      }
    }
  }
}
```

##### 

```json
{
  "meta": {},
  "data": {
    "type": "sensitive_data_scanner_rule",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "pattern": "pattern",
      "text_replacement": {
        "type": "replacement_string",
        "replacement_string": "REDACTED",
        "should_save_match": true
      },
      "tags": [
        "sensitive_data:true"
      ],
      "is_enabled": true,
      "priority": 1
    },
    "relationships": {
      "group": {
        "data": {
          "type": "sensitive_data_scanner_group",
          "id": "string"
        }
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Create rule response.

| Parent field                   | Field                             | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------ | --------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                | data                              | object   | Response data related to the creation of a rule.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| data                           | attributes                        | object   | Attributes of the Sensitive Data Scanner rule.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | description                       | string   | Description of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes                     | excluded_namespaces               | [string] | Attributes excluded from the scan. If namespaces is provided, it has to be a sub-path of the namespaces array.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | included_keyword_configuration    | object   | Object defining a set of keywords and a number of characters that help reduce noise. You can provide a list of keywords you would like to check within a defined proximity of the matching pattern. If any of the keywords are found within the proximity check, the match is kept. If none are found, the match is discarded.                                                                                                                                                        |
| included_keyword_configuration | character_count [*required*] | int64    | The number of characters behind a match detected by Sensitive Data Scanner to look for the keywords defined. `character_count` should be greater than the maximum length of a keyword defined for a rule.                                                                                                                                                                                                                                                                             |
| included_keyword_configuration | keywords [*required*]        | [string] | Keyword list that will be checked during scanning in order to validate a match. The number of keywords in the list must be less than or equal to 30.                                                                                                                                                                                                                                                                                                                                  |
| included_keyword_configuration | use_recommended_keywords          | boolean  | Should the rule use the underlying standard pattern keyword configuration. If set to `true`, the rule must be tied to a standard pattern. If set to `false`, the specified keywords and `character_count` are applied.                                                                                                                                                                                                                                                                |
| attributes                     | is_enabled                        | boolean  | Whether or not the rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes                     | name                              | string   | Name of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| attributes                     | namespaces                        | [string] | Attributes included in the scan. If namespaces is empty or missing, all attributes except excluded_namespaces are scanned. If both are missing the whole event is scanned.                                                                                                                                                                                                                                                                                                            |
| attributes                     | pattern                           | string   | Not included if there is a relationship to a standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | priority                          | int64    | Integer from 1 (high) to 5 (low) indicating rule issue severity.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| attributes                     | suppressions                      | object   | Object describing the suppressions for a rule. There are three types of suppressions, `starts_with`, `ends_with`, and `exact_match`. Suppressed matches are not obfuscated, counted in metrics, or displayed in the Findings page.                                                                                                                                                                                                                                                    |
| suppressions                   | ends_with                         | [string] | List of strings to use for suppression of matches ending with these strings.                                                                                                                                                                                                                                                                                                                                                                                                          |
| suppressions                   | exact_match                       | [string] | List of strings to use for suppression of matches exactly matching these strings.                                                                                                                                                                                                                                                                                                                                                                                                     |
| suppressions                   | starts_with                       | [string] | List of strings to use for suppression of matches starting with these strings.                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | tags                              | [string] | List of tags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| attributes                     | text_replacement                  | object   | Object describing how the scanned event will be replaced.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | number_of_chars                   | int64    | Required if type == 'partial_replacement_from_beginning' or 'partial_replacement_from_end'. It must be > 0.                                                                                                                                                                                                                                                                                                                                                                           |
| text_replacement               | replacement_string                | string   | Required if type == 'replacement_string'.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | should_save_match                 | boolean  | Only valid when type == `replacement_string`. When enabled, matches can be unmasked in logs by users with 'Data Scanner Unmask' permission. As a security best practice, avoid masking for highly-sensitive, long-lived data.                                                                                                                                                                                                                                                         |
| text_replacement               | type                              | enum     | Type of the replacement text. None means no replacement. hash means the data will be stubbed. replacement_string means that one can chose a text to replace the data. partial_replacement_from_beginning allows a user to partially replace the data from the beginning, and partial_replacement_from_end on the other hand, allows to replace data from the end. Allowed enum values: `none,hash,replacement_string,partial_replacement_from_beginning,partial_replacement_from_end` |
| data                           | id                                | string   | ID of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| data                           | relationships                     | object   | Relationships of a scanning rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| relationships                  | group                             | object   | A scanning group data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| group                          | data                              | object   | A scanning group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| data                           | id                                | string   | ID of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| data                           | type                              | enum     | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                                                                                                                                                                                                                                                                                                                                                                                                |
| relationships                  | standard_pattern                  | object   | A standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| standard_pattern               | data                              | object   | Data containing the standard pattern id.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| data                           | id                                | string   | ID of the standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| data                           | type                              | enum     | Sensitive Data Scanner standard pattern type. Allowed enum values: `sensitive_data_scanner_standard_pattern`                                                                                                                                                                                                                                                                                                                                                                          |
| data                           | type                              | enum     | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                | meta                              | object   | Meta payload containing information about the API.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| meta                           | version                           | int64    | Version of the API (optional).                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "string",
      "excluded_namespaces": [
        "admin.name"
      ],
      "included_keyword_configuration": {
        "character_count": 30,
        "keywords": [
          "email",
          "address",
          "login"
        ],
        "use_recommended_keywords": false
      },
      "is_enabled": false,
      "name": "string",
      "namespaces": [
        "admin"
      ],
      "pattern": "string",
      "priority": "integer",
      "suppressions": {
        "ends_with": [
          "@example.com",
          "another.example.com"
        ],
        "exact_match": [
          "admin@example.com",
          "user@example.com"
        ],
        "starts_with": [
          "admin",
          "user"
        ]
      },
      "tags": [],
      "text_replacement": {
        "number_of_chars": "integer",
        "replacement_string": "string",
        "should_save_match": false,
        "type": "string"
      }
    },
    "id": "string",
    "relationships": {
      "group": {
        "data": {
          "id": "string",
          "type": "sensitive_data_scanner_group"
        }
      },
      "standard_pattern": {
        "data": {
          "id": "string",
          "type": "sensitive_data_scanner_standard_pattern"
        }
      }
    },
    "type": "sensitive_data_scanner_rule"
  },
  "meta": {
    "version": 0
  }
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {},
  "data": {
    "type": "sensitive_data_scanner_rule",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "pattern": "pattern",
      "namespaces": [
        "admin"
      ],
      "excluded_namespaces": [
        "admin.name"
      ],
      "text_replacement": {
        "type": "none"
      },
      "tags": [
        "sensitive_data:true"
      ],
      "is_enabled": true,
      "priority": 1,
      "included_keyword_configuration": {
        "keywords": [
          "credit card"
        ],
        "character_count": 35
      }
    },
    "relationships": {
      "group": {
        "data": {
          "type": "sensitive_data_scanner_group",
          "id": "string"
        }
      }
    }
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {},
  "data": {
    "type": "sensitive_data_scanner_rule",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "pattern": "pattern",
      "text_replacement": {
        "type": "replacement_string",
        "replacement_string": "REDACTED",
        "should_save_match": true
      },
      "tags": [
        "sensitive_data:true"
      ],
      "is_enabled": true,
      "priority": 1
    },
    "relationships": {
      "group": {
        "data": {
          "type": "sensitive_data_scanner_group",
          "id": "string"
        }
      }
    }
  }
}
EOF
                        
##### 

```go
// Create Scanning Rule returns "OK" response

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
	// there is a valid "scanning_group" in the system
	GroupDataID := os.Getenv("GROUP_DATA_ID")

	body := datadogV2.SensitiveDataScannerRuleCreateRequest{
		Meta: datadogV2.SensitiveDataScannerMetaVersionOnly{},
		Data: datadogV2.SensitiveDataScannerRuleCreate{
			Type: datadogV2.SENSITIVEDATASCANNERRULETYPE_SENSITIVE_DATA_SCANNER_RULE,
			Attributes: datadogV2.SensitiveDataScannerRuleAttributes{
				Name:    datadog.PtrString("Example-Sensitive-Data-Scanner"),
				Pattern: datadog.PtrString("pattern"),
				Namespaces: []string{
					"admin",
				},
				ExcludedNamespaces: []string{
					"admin.name",
				},
				TextReplacement: &datadogV2.SensitiveDataScannerTextReplacement{
					Type: datadogV2.SENSITIVEDATASCANNERTEXTREPLACEMENTTYPE_NONE.Ptr(),
				},
				Tags: []string{
					"sensitive_data:true",
				},
				IsEnabled: datadog.PtrBool(true),
				Priority:  datadog.PtrInt64(1),
				IncludedKeywordConfiguration: &datadogV2.SensitiveDataScannerIncludedKeywordConfiguration{
					Keywords: []string{
						"credit card",
					},
					CharacterCount: 35,
				},
			},
			Relationships: datadogV2.SensitiveDataScannerRuleRelationships{
				Group: &datadogV2.SensitiveDataScannerGroupData{
					Data: &datadogV2.SensitiveDataScannerGroup{
						Type: datadogV2.SENSITIVEDATASCANNERGROUPTYPE_SENSITIVE_DATA_SCANNER_GROUP.Ptr(),
						Id:   datadog.PtrString(GroupDataID),
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.CreateScanningRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.CreateScanningRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.CreateScanningRule`:\n%s\n", responseContent)
}
```

##### 

```go
// Create Scanning Rule with should_save_match returns "OK" response

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
	// there is a valid "scanning_group" in the system
	GroupDataID := os.Getenv("GROUP_DATA_ID")

	body := datadogV2.SensitiveDataScannerRuleCreateRequest{
		Meta: datadogV2.SensitiveDataScannerMetaVersionOnly{},
		Data: datadogV2.SensitiveDataScannerRuleCreate{
			Type: datadogV2.SENSITIVEDATASCANNERRULETYPE_SENSITIVE_DATA_SCANNER_RULE,
			Attributes: datadogV2.SensitiveDataScannerRuleAttributes{
				Name:    datadog.PtrString("Example-Sensitive-Data-Scanner"),
				Pattern: datadog.PtrString("pattern"),
				TextReplacement: &datadogV2.SensitiveDataScannerTextReplacement{
					Type:              datadogV2.SENSITIVEDATASCANNERTEXTREPLACEMENTTYPE_REPLACEMENT_STRING.Ptr(),
					ReplacementString: datadog.PtrString("REDACTED"),
					ShouldSaveMatch:   datadog.PtrBool(true),
				},
				Tags: []string{
					"sensitive_data:true",
				},
				IsEnabled: datadog.PtrBool(true),
				Priority:  datadog.PtrInt64(1),
			},
			Relationships: datadogV2.SensitiveDataScannerRuleRelationships{
				Group: &datadogV2.SensitiveDataScannerGroupData{
					Data: &datadogV2.SensitiveDataScannerGroup{
						Type: datadogV2.SENSITIVEDATASCANNERGROUPTYPE_SENSITIVE_DATA_SCANNER_GROUP.Ptr(),
						Id:   datadog.PtrString(GroupDataID),
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.CreateScanningRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.CreateScanningRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.CreateScanningRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create Scanning Rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerCreateRuleResponse;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroup;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupData;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupType;
import com.datadog.api.client.v2.model.SensitiveDataScannerIncludedKeywordConfiguration;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleAttributes;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleCreate;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleCreateRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleRelationships;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleType;
import com.datadog.api.client.v2.model.SensitiveDataScannerTextReplacement;
import com.datadog.api.client.v2.model.SensitiveDataScannerTextReplacementType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // there is a valid "scanning_group" in the system
    String GROUP_DATA_ID = System.getenv("GROUP_DATA_ID");

    SensitiveDataScannerRuleCreateRequest body =
        new SensitiveDataScannerRuleCreateRequest()
            .meta(new SensitiveDataScannerMetaVersionOnly())
            .data(
                new SensitiveDataScannerRuleCreate()
                    .type(SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE)
                    .attributes(
                        new SensitiveDataScannerRuleAttributes()
                            .name("Example-Sensitive-Data-Scanner")
                            .pattern("pattern")
                            .namespaces(Collections.singletonList("admin"))
                            .excludedNamespaces(Collections.singletonList("admin.name"))
                            .textReplacement(
                                new SensitiveDataScannerTextReplacement()
                                    .type(SensitiveDataScannerTextReplacementType.NONE))
                            .tags(Collections.singletonList("sensitive_data:true"))
                            .isEnabled(true)
                            .priority(1L)
                            .includedKeywordConfiguration(
                                new SensitiveDataScannerIncludedKeywordConfiguration()
                                    .keywords(Collections.singletonList("credit card"))
                                    .characterCount(35L)))
                    .relationships(
                        new SensitiveDataScannerRuleRelationships()
                            .group(
                                new SensitiveDataScannerGroupData()
                                    .data(
                                        new SensitiveDataScannerGroup()
                                            .type(
                                                SensitiveDataScannerGroupType
                                                    .SENSITIVE_DATA_SCANNER_GROUP)
                                            .id(GROUP_DATA_ID)))));

    try {
      SensitiveDataScannerCreateRuleResponse result = apiInstance.createScanningRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#createScanningRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Create Scanning Rule with should_save_match returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerCreateRuleResponse;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroup;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupData;
import com.datadog.api.client.v2.model.SensitiveDataScannerGroupType;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleAttributes;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleCreate;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleCreateRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleRelationships;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleType;
import com.datadog.api.client.v2.model.SensitiveDataScannerTextReplacement;
import com.datadog.api.client.v2.model.SensitiveDataScannerTextReplacementType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // there is a valid "scanning_group" in the system
    String GROUP_DATA_ID = System.getenv("GROUP_DATA_ID");

    SensitiveDataScannerRuleCreateRequest body =
        new SensitiveDataScannerRuleCreateRequest()
            .meta(new SensitiveDataScannerMetaVersionOnly())
            .data(
                new SensitiveDataScannerRuleCreate()
                    .type(SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE)
                    .attributes(
                        new SensitiveDataScannerRuleAttributes()
                            .name("Example-Sensitive-Data-Scanner")
                            .pattern("pattern")
                            .textReplacement(
                                new SensitiveDataScannerTextReplacement()
                                    .type(
                                        SensitiveDataScannerTextReplacementType.REPLACEMENT_STRING)
                                    .replacementString("REDACTED")
                                    .shouldSaveMatch(true))
                            .tags(Collections.singletonList("sensitive_data:true"))
                            .isEnabled(true)
                            .priority(1L))
                    .relationships(
                        new SensitiveDataScannerRuleRelationships()
                            .group(
                                new SensitiveDataScannerGroupData()
                                    .data(
                                        new SensitiveDataScannerGroup()
                                            .type(
                                                SensitiveDataScannerGroupType
                                                    .SENSITIVE_DATA_SCANNER_GROUP)
                                            .id(GROUP_DATA_ID)))));

    try {
      SensitiveDataScannerCreateRuleResponse result = apiInstance.createScanningRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#createScanningRule");
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
Create Scanning Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_group import SensitiveDataScannerGroup
from datadog_api_client.v2.model.sensitive_data_scanner_group_data import SensitiveDataScannerGroupData
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_included_keyword_configuration import (
    SensitiveDataScannerIncludedKeywordConfiguration,
)
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_rule_attributes import SensitiveDataScannerRuleAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_rule_create import SensitiveDataScannerRuleCreate
from datadog_api_client.v2.model.sensitive_data_scanner_rule_create_request import SensitiveDataScannerRuleCreateRequest
from datadog_api_client.v2.model.sensitive_data_scanner_rule_relationships import SensitiveDataScannerRuleRelationships
from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement_type import (
    SensitiveDataScannerTextReplacementType,
)

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

body = SensitiveDataScannerRuleCreateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerRuleCreate(
        type=SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE,
        attributes=SensitiveDataScannerRuleAttributes(
            name="Example-Sensitive-Data-Scanner",
            pattern="pattern",
            namespaces=[
                "admin",
            ],
            excluded_namespaces=[
                "admin.name",
            ],
            text_replacement=SensitiveDataScannerTextReplacement(
                type=SensitiveDataScannerTextReplacementType.NONE,
            ),
            tags=[
                "sensitive_data:true",
            ],
            is_enabled=True,
            priority=1,
            included_keyword_configuration=SensitiveDataScannerIncludedKeywordConfiguration(
                keywords=[
                    "credit card",
                ],
                character_count=35,
            ),
        ),
        relationships=SensitiveDataScannerRuleRelationships(
            group=SensitiveDataScannerGroupData(
                data=SensitiveDataScannerGroup(
                    type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
                    id=GROUP_DATA_ID,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.create_scanning_rule(body=body)

    print(response)
```

##### 

```python
"""
Create Scanning Rule with should_save_match returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_group import SensitiveDataScannerGroup
from datadog_api_client.v2.model.sensitive_data_scanner_group_data import SensitiveDataScannerGroupData
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_rule_attributes import SensitiveDataScannerRuleAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_rule_create import SensitiveDataScannerRuleCreate
from datadog_api_client.v2.model.sensitive_data_scanner_rule_create_request import SensitiveDataScannerRuleCreateRequest
from datadog_api_client.v2.model.sensitive_data_scanner_rule_relationships import SensitiveDataScannerRuleRelationships
from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement_type import (
    SensitiveDataScannerTextReplacementType,
)

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

body = SensitiveDataScannerRuleCreateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerRuleCreate(
        type=SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE,
        attributes=SensitiveDataScannerRuleAttributes(
            name="Example-Sensitive-Data-Scanner",
            pattern="pattern",
            text_replacement=SensitiveDataScannerTextReplacement(
                type=SensitiveDataScannerTextReplacementType.REPLACEMENT_STRING,
                replacement_string="REDACTED",
                should_save_match=True,
            ),
            tags=[
                "sensitive_data:true",
            ],
            is_enabled=True,
            priority=1,
        ),
        relationships=SensitiveDataScannerRuleRelationships(
            group=SensitiveDataScannerGroupData(
                data=SensitiveDataScannerGroup(
                    type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
                    id=GROUP_DATA_ID,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.create_scanning_rule(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create Scanning Rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = ENV["GROUP_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerRuleCreateRequest.new({
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
  data: DatadogAPIClient::V2::SensitiveDataScannerRuleCreate.new({
    type: DatadogAPIClient::V2::SensitiveDataScannerRuleType::SENSITIVE_DATA_SCANNER_RULE,
    attributes: DatadogAPIClient::V2::SensitiveDataScannerRuleAttributes.new({
      name: "Example-Sensitive-Data-Scanner",
      pattern: "pattern",
      namespaces: [
        "admin",
      ],
      excluded_namespaces: [
        "admin.name",
      ],
      text_replacement: DatadogAPIClient::V2::SensitiveDataScannerTextReplacement.new({
        type: DatadogAPIClient::V2::SensitiveDataScannerTextReplacementType::NONE,
      }),
      tags: [
        "sensitive_data:true",
      ],
      is_enabled: true,
      priority: 1,
      included_keyword_configuration: DatadogAPIClient::V2::SensitiveDataScannerIncludedKeywordConfiguration.new({
        keywords: [
          "credit card",
        ],
        character_count: 35,
      }),
    }),
    relationships: DatadogAPIClient::V2::SensitiveDataScannerRuleRelationships.new({
      group: DatadogAPIClient::V2::SensitiveDataScannerGroupData.new({
        data: DatadogAPIClient::V2::SensitiveDataScannerGroup.new({
          type: DatadogAPIClient::V2::SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP,
          id: GROUP_DATA_ID,
        }),
      }),
    }),
  }),
})
p api_instance.create_scanning_rule(body)
```

##### 

```ruby
# Create Scanning Rule with should_save_match returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = ENV["GROUP_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerRuleCreateRequest.new({
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
  data: DatadogAPIClient::V2::SensitiveDataScannerRuleCreate.new({
    type: DatadogAPIClient::V2::SensitiveDataScannerRuleType::SENSITIVE_DATA_SCANNER_RULE,
    attributes: DatadogAPIClient::V2::SensitiveDataScannerRuleAttributes.new({
      name: "Example-Sensitive-Data-Scanner",
      pattern: "pattern",
      text_replacement: DatadogAPIClient::V2::SensitiveDataScannerTextReplacement.new({
        type: DatadogAPIClient::V2::SensitiveDataScannerTextReplacementType::REPLACEMENT_STRING,
        replacement_string: "REDACTED",
        should_save_match: true,
      }),
      tags: [
        "sensitive_data:true",
      ],
      is_enabled: true,
      priority: 1,
    }),
    relationships: DatadogAPIClient::V2::SensitiveDataScannerRuleRelationships.new({
      group: DatadogAPIClient::V2::SensitiveDataScannerGroupData.new({
        data: DatadogAPIClient::V2::SensitiveDataScannerGroup.new({
          type: DatadogAPIClient::V2::SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP,
          id: GROUP_DATA_ID,
        }),
      }),
    }),
  }),
})
p api_instance.create_scanning_rule(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create Scanning Rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroup;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupData;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerIncludedKeywordConfiguration;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleAttributes;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleCreate;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleCreateRequest;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleRelationships;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerTextReplacement;
use datadog_api_client::datadogV2::model::SensitiveDataScannerTextReplacementType;

#[tokio::main]
async fn main() {
    // there is a valid "scanning_group" in the system
    let group_data_id = std::env::var("GROUP_DATA_ID").unwrap();
    let body = SensitiveDataScannerRuleCreateRequest::new(
        SensitiveDataScannerRuleCreate::new(
            SensitiveDataScannerRuleAttributes::new()
                .excluded_namespaces(vec!["admin.name".to_string()])
                .included_keyword_configuration(
                    SensitiveDataScannerIncludedKeywordConfiguration::new(
                        35,
                        vec!["credit card".to_string()],
                    ),
                )
                .is_enabled(true)
                .name("Example-Sensitive-Data-Scanner".to_string())
                .namespaces(vec!["admin".to_string()])
                .pattern("pattern".to_string())
                .priority(1)
                .tags(vec!["sensitive_data:true".to_string()])
                .text_replacement(
                    SensitiveDataScannerTextReplacement::new()
                        .type_(SensitiveDataScannerTextReplacementType::NONE),
                ),
            SensitiveDataScannerRuleRelationships::new().group(
                SensitiveDataScannerGroupData::new().data(
                    SensitiveDataScannerGroup::new()
                        .id(group_data_id.clone())
                        .type_(SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP),
                ),
            ),
            SensitiveDataScannerRuleType::SENSITIVE_DATA_SCANNER_RULE,
        ),
        SensitiveDataScannerMetaVersionOnly::new(),
    );
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.create_scanning_rule(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Create Scanning Rule with should_save_match returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroup;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupData;
use datadog_api_client::datadogV2::model::SensitiveDataScannerGroupType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleAttributes;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleCreate;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleCreateRequest;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleRelationships;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerTextReplacement;
use datadog_api_client::datadogV2::model::SensitiveDataScannerTextReplacementType;

#[tokio::main]
async fn main() {
    // there is a valid "scanning_group" in the system
    let group_data_id = std::env::var("GROUP_DATA_ID").unwrap();
    let body = SensitiveDataScannerRuleCreateRequest::new(
        SensitiveDataScannerRuleCreate::new(
            SensitiveDataScannerRuleAttributes::new()
                .is_enabled(true)
                .name("Example-Sensitive-Data-Scanner".to_string())
                .pattern("pattern".to_string())
                .priority(1)
                .tags(vec!["sensitive_data:true".to_string()])
                .text_replacement(
                    SensitiveDataScannerTextReplacement::new()
                        .replacement_string("REDACTED".to_string())
                        .should_save_match(true)
                        .type_(SensitiveDataScannerTextReplacementType::REPLACEMENT_STRING),
                ),
            SensitiveDataScannerRuleRelationships::new().group(
                SensitiveDataScannerGroupData::new().data(
                    SensitiveDataScannerGroup::new()
                        .id(group_data_id.clone())
                        .type_(SensitiveDataScannerGroupType::SENSITIVE_DATA_SCANNER_GROUP),
                ),
            ),
            SensitiveDataScannerRuleType::SENSITIVE_DATA_SCANNER_RULE,
        ),
        SensitiveDataScannerMetaVersionOnly::new(),
    );
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.create_scanning_rule(body).await;
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
 * Create Scanning Rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// there is a valid "scanning_group" in the system
const GROUP_DATA_ID = process.env.GROUP_DATA_ID as string;

const params: v2.SensitiveDataScannerApiCreateScanningRuleRequest = {
  body: {
    meta: {},
    data: {
      type: "sensitive_data_scanner_rule",
      attributes: {
        name: "Example-Sensitive-Data-Scanner",
        pattern: "pattern",
        namespaces: ["admin"],
        excludedNamespaces: ["admin.name"],
        textReplacement: {
          type: "none",
        },
        tags: ["sensitive_data:true"],
        isEnabled: true,
        priority: 1,
        includedKeywordConfiguration: {
          keywords: ["credit card"],
          characterCount: 35,
        },
      },
      relationships: {
        group: {
          data: {
            type: "sensitive_data_scanner_group",
            id: GROUP_DATA_ID,
          },
        },
      },
    },
  },
};

apiInstance
  .createScanningRule(params)
  .then((data: v2.SensitiveDataScannerCreateRuleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Create Scanning Rule with should_save_match returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// there is a valid "scanning_group" in the system
const GROUP_DATA_ID = process.env.GROUP_DATA_ID as string;

const params: v2.SensitiveDataScannerApiCreateScanningRuleRequest = {
  body: {
    meta: {},
    data: {
      type: "sensitive_data_scanner_rule",
      attributes: {
        name: "Example-Sensitive-Data-Scanner",
        pattern: "pattern",
        textReplacement: {
          type: "replacement_string",
          replacementString: "REDACTED",
          shouldSaveMatch: true,
        },
        tags: ["sensitive_data:true"],
        isEnabled: true,
        priority: 1,
      },
      relationships: {
        group: {
          data: {
            type: "sensitive_data_scanner_group",
            id: GROUP_DATA_ID,
          },
        },
      },
    },
  },
};

apiInstance
  .createScanningRule(params)
  .then((data: v2.SensitiveDataScannerCreateRuleResponse) => {
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

## Update Scanning Rule{% #update-scanning-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config/rules/{rule_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config/rules/{rule_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |

### Overview

Update a scanning rule. The request body MUST NOT include a standard_pattern relationship, as that relationship is non-editable. Trying to edit the regex attribute of a rule with a standard_pattern relationship will also result in an error. This endpoint requires the `data_scanner_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| rule_id [*required*] | string | The ID of the rule. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field                   | Field                             | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------ | --------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                | data [*required*]            | object   | Data related to the update of a rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| data                           | attributes                        | object   | Attributes of the Sensitive Data Scanner rule.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | description                       | string   | Description of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes                     | excluded_namespaces               | [string] | Attributes excluded from the scan. If namespaces is provided, it has to be a sub-path of the namespaces array.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | included_keyword_configuration    | object   | Object defining a set of keywords and a number of characters that help reduce noise. You can provide a list of keywords you would like to check within a defined proximity of the matching pattern. If any of the keywords are found within the proximity check, the match is kept. If none are found, the match is discarded.                                                                                                                                                        |
| included_keyword_configuration | character_count [*required*] | int64    | The number of characters behind a match detected by Sensitive Data Scanner to look for the keywords defined. `character_count` should be greater than the maximum length of a keyword defined for a rule.                                                                                                                                                                                                                                                                             |
| included_keyword_configuration | keywords [*required*]        | [string] | Keyword list that will be checked during scanning in order to validate a match. The number of keywords in the list must be less than or equal to 30.                                                                                                                                                                                                                                                                                                                                  |
| included_keyword_configuration | use_recommended_keywords          | boolean  | Should the rule use the underlying standard pattern keyword configuration. If set to `true`, the rule must be tied to a standard pattern. If set to `false`, the specified keywords and `character_count` are applied.                                                                                                                                                                                                                                                                |
| attributes                     | is_enabled                        | boolean  | Whether or not the rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes                     | name                              | string   | Name of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| attributes                     | namespaces                        | [string] | Attributes included in the scan. If namespaces is empty or missing, all attributes except excluded_namespaces are scanned. If both are missing the whole event is scanned.                                                                                                                                                                                                                                                                                                            |
| attributes                     | pattern                           | string   | Not included if there is a relationship to a standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | priority                          | int64    | Integer from 1 (high) to 5 (low) indicating rule issue severity.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| attributes                     | suppressions                      | object   | Object describing the suppressions for a rule. There are three types of suppressions, `starts_with`, `ends_with`, and `exact_match`. Suppressed matches are not obfuscated, counted in metrics, or displayed in the Findings page.                                                                                                                                                                                                                                                    |
| suppressions                   | ends_with                         | [string] | List of strings to use for suppression of matches ending with these strings.                                                                                                                                                                                                                                                                                                                                                                                                          |
| suppressions                   | exact_match                       | [string] | List of strings to use for suppression of matches exactly matching these strings.                                                                                                                                                                                                                                                                                                                                                                                                     |
| suppressions                   | starts_with                       | [string] | List of strings to use for suppression of matches starting with these strings.                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes                     | tags                              | [string] | List of tags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| attributes                     | text_replacement                  | object   | Object describing how the scanned event will be replaced.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | number_of_chars                   | int64    | Required if type == 'partial_replacement_from_beginning' or 'partial_replacement_from_end'. It must be > 0.                                                                                                                                                                                                                                                                                                                                                                           |
| text_replacement               | replacement_string                | string   | Required if type == 'replacement_string'.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text_replacement               | should_save_match                 | boolean  | Only valid when type == `replacement_string`. When enabled, matches can be unmasked in logs by users with 'Data Scanner Unmask' permission. As a security best practice, avoid masking for highly-sensitive, long-lived data.                                                                                                                                                                                                                                                         |
| text_replacement               | type                              | enum     | Type of the replacement text. None means no replacement. hash means the data will be stubbed. replacement_string means that one can chose a text to replace the data. partial_replacement_from_beginning allows a user to partially replace the data from the beginning, and partial_replacement_from_end on the other hand, allows to replace data from the end. Allowed enum values: `none,hash,replacement_string,partial_replacement_from_beginning,partial_replacement_from_end` |
| data                           | id                                | string   | ID of the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| data                           | relationships                     | object   | Relationships of a scanning rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| relationships                  | group                             | object   | A scanning group data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| group                          | data                              | object   | A scanning group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| data                           | id                                | string   | ID of the group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| data                           | type                              | enum     | Sensitive Data Scanner group type. Allowed enum values: `sensitive_data_scanner_group`                                                                                                                                                                                                                                                                                                                                                                                                |
| relationships                  | standard_pattern                  | object   | A standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| standard_pattern               | data                              | object   | Data containing the standard pattern id.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| data                           | id                                | string   | ID of the standard pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| data                           | type                              | enum     | Sensitive Data Scanner standard pattern type. Allowed enum values: `sensitive_data_scanner_standard_pattern`                                                                                                                                                                                                                                                                                                                                                                          |
| data                           | type                              | enum     | Sensitive Data Scanner rule type. Allowed enum values: `sensitive_data_scanner_rule`                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                | meta [*required*]            | object   | Meta payload containing information about the API.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| meta                           | version                           | int64    | Version of the API (optional).                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {},
  "data": {
    "id": "string",
    "type": "sensitive_data_scanner_rule",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "pattern": "pattern",
      "text_replacement": {
        "type": "none"
      },
      "tags": [
        "sensitive_data:true"
      ],
      "is_enabled": true,
      "priority": 5,
      "included_keyword_configuration": {
        "keywords": [
          "credit card",
          "cc"
        ],
        "character_count": 35
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Update rule response.

| Parent field | Field   | Type   | Description                                        |
| ------------ | ------- | ------ | -------------------------------------------------- |
|              | meta    | object | Meta payload containing information about the API. |
| meta         | version | int64  | Version of the API (optional).                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {
    "version": 0
  }
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
                          \# Path parametersexport rule_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {},
  "data": {
    "id": "string",
    "type": "sensitive_data_scanner_rule",
    "attributes": {
      "name": "Example-Sensitive-Data-Scanner",
      "pattern": "pattern",
      "text_replacement": {
        "type": "none"
      },
      "tags": [
        "sensitive_data:true"
      ],
      "is_enabled": true,
      "priority": 5,
      "included_keyword_configuration": {
        "keywords": [
          "credit card",
          "cc"
        ],
        "character_count": 35
      }
    }
  }
}
EOF
                        
##### 

```go
// Update Scanning Rule returns "OK" response

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
	// the "scanning_group" has a "scanning_rule"
	RuleDataID := os.Getenv("RULE_DATA_ID")

	body := datadogV2.SensitiveDataScannerRuleUpdateRequest{
		Meta: datadogV2.SensitiveDataScannerMetaVersionOnly{},
		Data: datadogV2.SensitiveDataScannerRuleUpdate{
			Id:   datadog.PtrString(RuleDataID),
			Type: datadogV2.SENSITIVEDATASCANNERRULETYPE_SENSITIVE_DATA_SCANNER_RULE.Ptr(),
			Attributes: &datadogV2.SensitiveDataScannerRuleAttributes{
				Name:    datadog.PtrString("Example-Sensitive-Data-Scanner"),
				Pattern: datadog.PtrString("pattern"),
				TextReplacement: &datadogV2.SensitiveDataScannerTextReplacement{
					Type: datadogV2.SENSITIVEDATASCANNERTEXTREPLACEMENTTYPE_NONE.Ptr(),
				},
				Tags: []string{
					"sensitive_data:true",
				},
				IsEnabled: datadog.PtrBool(true),
				Priority:  datadog.PtrInt64(5),
				IncludedKeywordConfiguration: &datadogV2.SensitiveDataScannerIncludedKeywordConfiguration{
					Keywords: []string{
						"credit card",
						"cc",
					},
					CharacterCount: 35,
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.UpdateScanningRule(ctx, RuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.UpdateScanningRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.UpdateScanningRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update Scanning Rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerIncludedKeywordConfiguration;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleAttributes;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleType;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleUpdate;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleUpdateRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleUpdateResponse;
import com.datadog.api.client.v2.model.SensitiveDataScannerTextReplacement;
import com.datadog.api.client.v2.model.SensitiveDataScannerTextReplacementType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // the "scanning_group" has a "scanning_rule"
    String RULE_DATA_ID = System.getenv("RULE_DATA_ID");

    SensitiveDataScannerRuleUpdateRequest body =
        new SensitiveDataScannerRuleUpdateRequest()
            .meta(new SensitiveDataScannerMetaVersionOnly())
            .data(
                new SensitiveDataScannerRuleUpdate()
                    .id(RULE_DATA_ID)
                    .type(SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE)
                    .attributes(
                        new SensitiveDataScannerRuleAttributes()
                            .name("Example-Sensitive-Data-Scanner")
                            .pattern("pattern")
                            .textReplacement(
                                new SensitiveDataScannerTextReplacement()
                                    .type(SensitiveDataScannerTextReplacementType.NONE))
                            .tags(Collections.singletonList("sensitive_data:true"))
                            .isEnabled(true)
                            .priority(5L)
                            .includedKeywordConfiguration(
                                new SensitiveDataScannerIncludedKeywordConfiguration()
                                    .keywords(Arrays.asList("credit card", "cc"))
                                    .characterCount(35L))));

    try {
      SensitiveDataScannerRuleUpdateResponse result =
          apiInstance.updateScanningRule(RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#updateScanningRule");
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
Update Scanning Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_included_keyword_configuration import (
    SensitiveDataScannerIncludedKeywordConfiguration,
)
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_rule_attributes import SensitiveDataScannerRuleAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType
from datadog_api_client.v2.model.sensitive_data_scanner_rule_update import SensitiveDataScannerRuleUpdate
from datadog_api_client.v2.model.sensitive_data_scanner_rule_update_request import SensitiveDataScannerRuleUpdateRequest
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement_type import (
    SensitiveDataScannerTextReplacementType,
)

# the "scanning_group" has a "scanning_rule"
RULE_DATA_ID = environ["RULE_DATA_ID"]

body = SensitiveDataScannerRuleUpdateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerRuleUpdate(
        id=RULE_DATA_ID,
        type=SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE,
        attributes=SensitiveDataScannerRuleAttributes(
            name="Example-Sensitive-Data-Scanner",
            pattern="pattern",
            text_replacement=SensitiveDataScannerTextReplacement(
                type=SensitiveDataScannerTextReplacementType.NONE,
            ),
            tags=[
                "sensitive_data:true",
            ],
            is_enabled=True,
            priority=5,
            included_keyword_configuration=SensitiveDataScannerIncludedKeywordConfiguration(
                keywords=[
                    "credit card",
                    "cc",
                ],
                character_count=35,
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.update_scanning_rule(rule_id=RULE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update Scanning Rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# the "scanning_group" has a "scanning_rule"
RULE_DATA_ID = ENV["RULE_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerRuleUpdateRequest.new({
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
  data: DatadogAPIClient::V2::SensitiveDataScannerRuleUpdate.new({
    id: RULE_DATA_ID,
    type: DatadogAPIClient::V2::SensitiveDataScannerRuleType::SENSITIVE_DATA_SCANNER_RULE,
    attributes: DatadogAPIClient::V2::SensitiveDataScannerRuleAttributes.new({
      name: "Example-Sensitive-Data-Scanner",
      pattern: "pattern",
      text_replacement: DatadogAPIClient::V2::SensitiveDataScannerTextReplacement.new({
        type: DatadogAPIClient::V2::SensitiveDataScannerTextReplacementType::NONE,
      }),
      tags: [
        "sensitive_data:true",
      ],
      is_enabled: true,
      priority: 5,
      included_keyword_configuration: DatadogAPIClient::V2::SensitiveDataScannerIncludedKeywordConfiguration.new({
        keywords: [
          "credit card",
          "cc",
        ],
        character_count: 35,
      }),
    }),
  }),
})
p api_instance.update_scanning_rule(RULE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update Scanning Rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerIncludedKeywordConfiguration;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleAttributes;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleType;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleUpdate;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleUpdateRequest;
use datadog_api_client::datadogV2::model::SensitiveDataScannerTextReplacement;
use datadog_api_client::datadogV2::model::SensitiveDataScannerTextReplacementType;

#[tokio::main]
async fn main() {
    // the "scanning_group" has a "scanning_rule"
    let rule_data_id = std::env::var("RULE_DATA_ID").unwrap();
    let body = SensitiveDataScannerRuleUpdateRequest::new(
        SensitiveDataScannerRuleUpdate::new()
            .attributes(
                SensitiveDataScannerRuleAttributes::new()
                    .included_keyword_configuration(
                        SensitiveDataScannerIncludedKeywordConfiguration::new(
                            35,
                            vec!["credit card".to_string(), "cc".to_string()],
                        ),
                    )
                    .is_enabled(true)
                    .name("Example-Sensitive-Data-Scanner".to_string())
                    .pattern("pattern".to_string())
                    .priority(5)
                    .tags(vec!["sensitive_data:true".to_string()])
                    .text_replacement(
                        SensitiveDataScannerTextReplacement::new()
                            .type_(SensitiveDataScannerTextReplacementType::NONE),
                    ),
            )
            .id(rule_data_id.clone())
            .type_(SensitiveDataScannerRuleType::SENSITIVE_DATA_SCANNER_RULE),
        SensitiveDataScannerMetaVersionOnly::new(),
    );
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.update_scanning_rule(rule_data_id.clone(), body).await;
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
 * Update Scanning Rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// the "scanning_group" has a "scanning_rule"
const RULE_DATA_ID = process.env.RULE_DATA_ID as string;

const params: v2.SensitiveDataScannerApiUpdateScanningRuleRequest = {
  body: {
    meta: {},
    data: {
      id: RULE_DATA_ID,
      type: "sensitive_data_scanner_rule",
      attributes: {
        name: "Example-Sensitive-Data-Scanner",
        pattern: "pattern",
        textReplacement: {
          type: "none",
        },
        tags: ["sensitive_data:true"],
        isEnabled: true,
        priority: 5,
        includedKeywordConfiguration: {
          keywords: ["credit card", "cc"],
          characterCount: 35,
        },
      },
    },
  },
  ruleId: RULE_DATA_ID,
};

apiInstance
  .updateScanningRule(params)
  .then((data: v2.SensitiveDataScannerRuleUpdateResponse) => {
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

## Delete Scanning Rule{% #delete-scanning-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/sensitive-data-scanner/config/rules/{rule_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/sensitive-data-scanner/config/rules/{rule_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/{rule_id} |

### Overview

Delete a given rule. This endpoint requires the `data_scanner_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| rule_id [*required*] | string | The ID of the rule. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                        |
| ------------ | ---------------------- | ------ | -------------------------------------------------- |
|              | meta [*required*] | object | Meta payload containing information about the API. |
| meta         | version                | int64  | Version of the API (optional).                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {}
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Delete rule response.

| Parent field | Field   | Type   | Description                                        |
| ------------ | ------- | ------ | -------------------------------------------------- |
|              | meta    | object | Meta payload containing information about the API. |
| meta         | version | int64  | Version of the API (optional).                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "meta": {
    "version": 0
  }
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
                          \# Path parametersexport rule_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/sensitive-data-scanner/config/rules/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {}
}
EOF
                        
##### 

```go
// Delete Scanning Rule returns "OK" response

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
	// the "scanning_group" has a "scanning_rule"
	RuleDataID := os.Getenv("RULE_DATA_ID")

	body := datadogV2.SensitiveDataScannerRuleDeleteRequest{
		Meta: datadogV2.SensitiveDataScannerMetaVersionOnly{},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSensitiveDataScannerApi(apiClient)
	resp, r, err := api.DeleteScanningRule(ctx, RuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SensitiveDataScannerApi.DeleteScanningRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SensitiveDataScannerApi.DeleteScanningRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Scanning Rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SensitiveDataScannerApi;
import com.datadog.api.client.v2.model.SensitiveDataScannerMetaVersionOnly;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleDeleteRequest;
import com.datadog.api.client.v2.model.SensitiveDataScannerRuleDeleteResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SensitiveDataScannerApi apiInstance = new SensitiveDataScannerApi(defaultClient);

    // the "scanning_group" has a "scanning_rule"
    String RULE_DATA_ID = System.getenv("RULE_DATA_ID");

    SensitiveDataScannerRuleDeleteRequest body =
        new SensitiveDataScannerRuleDeleteRequest().meta(new SensitiveDataScannerMetaVersionOnly());

    try {
      SensitiveDataScannerRuleDeleteResponse result =
          apiInstance.deleteScanningRule(RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensitiveDataScannerApi#deleteScanningRule");
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
Delete Scanning Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_rule_delete_request import SensitiveDataScannerRuleDeleteRequest

# the "scanning_group" has a "scanning_rule"
RULE_DATA_ID = environ["RULE_DATA_ID"]

body = SensitiveDataScannerRuleDeleteRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.delete_scanning_rule(rule_id=RULE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Scanning Rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SensitiveDataScannerAPI.new

# the "scanning_group" has a "scanning_rule"
RULE_DATA_ID = ENV["RULE_DATA_ID"]

body = DatadogAPIClient::V2::SensitiveDataScannerRuleDeleteRequest.new({
  meta: DatadogAPIClient::V2::SensitiveDataScannerMetaVersionOnly.new({}),
})
p api_instance.delete_scanning_rule(RULE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Delete Scanning Rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_sensitive_data_scanner::SensitiveDataScannerAPI;
use datadog_api_client::datadogV2::model::SensitiveDataScannerMetaVersionOnly;
use datadog_api_client::datadogV2::model::SensitiveDataScannerRuleDeleteRequest;

#[tokio::main]
async fn main() {
    // the "scanning_group" has a "scanning_rule"
    let rule_data_id = std::env::var("RULE_DATA_ID").unwrap();
    let body =
        SensitiveDataScannerRuleDeleteRequest::new(SensitiveDataScannerMetaVersionOnly::new());
    let configuration = datadog::Configuration::new();
    let api = SensitiveDataScannerAPI::with_config(configuration);
    let resp = api.delete_scanning_rule(rule_data_id.clone(), body).await;
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
 * Delete Scanning Rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SensitiveDataScannerApi(configuration);

// the "scanning_group" has a "scanning_rule"
const RULE_DATA_ID = process.env.RULE_DATA_ID as string;

const params: v2.SensitiveDataScannerApiDeleteScanningRuleRequest = {
  body: {
    meta: {},
  },
  ruleId: RULE_DATA_ID,
};

apiInstance
  .deleteScanningRule(params)
  .then((data: v2.SensitiveDataScannerRuleDeleteResponse) => {
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
