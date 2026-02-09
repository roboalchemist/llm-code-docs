# Source: https://docs.datadoghq.com/api/latest/service-definition

# Service Definition
API to create, update, retrieve and delete service definitions. Note: Service Catalog [v3.0 schema](https://docs.datadoghq.com/service_catalog/service_definitions/v3-0/) has new API endpoints documented under [Software Catalog](https://docs.datadoghq.com/api/latest/software-catalog/). Use the following Service Definition endpoints for v2.2 and earlier.
## [Get all service definitions](https://docs.datadoghq.com/api/latest/service-definition/#get-all-service-definitions)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-definition/#get-all-service-definitions-v2)


GET https://api.ap1.datadoghq.com/api/v2/services/definitionshttps://api.ap2.datadoghq.com/api/v2/services/definitionshttps://api.datadoghq.eu/api/v2/services/definitionshttps://api.ddog-gov.com/api/v2/services/definitionshttps://api.datadoghq.com/api/v2/services/definitionshttps://api.us3.datadoghq.com/api/v2/services/definitionshttps://api.us5.datadoghq.com/api/v2/services/definitions
### Overview
Get a list of all service definitions from the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_read` permission.
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[number]
integer
Specific page number to return.
schema_version
enum
The schema version desired in the response.  
Allowed enum values: `v1, v2, v2.1, v2.2`
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-definition/#ListServiceDefinitions-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-definition/#ListServiceDefinitions-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-definition/#ListServiceDefinitions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


Create service definitions response.
Field
Type
Description
data
[object]
Data representing service definitions.
attributes
object
Service definition attributes.
meta
object
Metadata about a service definition.
github-html-url
string
GitHub HTML URL.
ingested-schema-version
string
Ingestion schema version.
ingestion-source
string
Ingestion source of the service definition.
last-modified-time
string
Last modified time of the service definition.
origin
string
User defined origin of the service definition.
origin-detail
string
User defined origin's detail of the service definition.
warnings
[object]
A list of schema validation warnings.
instance-location
string
The warning instance location.
keyword-location
string
The warning keyword location.
message
string
The warning message.
schema
<oneOf>
Service definition schema.
Option 1
object
**DEPRECATED** : Deprecated - Service definition V1 for providing additional service metadata and integrations.
contact
object
Contact information about the service.
email
string
Service owner’s email.
slack
string
Service owner’s Slack channel.
extensions
object
Extensions to V1 schema.
external-resources
[object]
A list of external links related to the services.
name [_required_]
string
Link name.
type [_required_]
enum
Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`
url [_required_]
string
Link URL.
info [_required_]
object
Basic information about a service.
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
display-name
string
A friendly name of the service.
service-tier
string
Service tier.
integrations
object
Third party integrations that Datadog supports.
pagerduty
string
PagerDuty service URL for the service.
org
object
Org related information about the service.
application
string
App feature this service supports.
team
string
Team that owns the service.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v1`
default: `v1`
tags
[string]
A set of custom tags.
Option 2
object
Service definition V2 for providing service metadata and integrations.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
dd-team
string
Experimental feature. A Team handle that matches a Team in the Datadog Teams product.
docs
[object]
A list of documentation related to the services.
name [_required_]
string
Document name.
provider
string
Document provider.
url [_required_]
string
Document URL.
extensions
object
Extensions to V2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
string
PagerDuty service URL for the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
type [_required_]
enum
Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`
url [_required_]
string
Link URL.
repos
[object]
A list of code repositories related to the services.
name [_required_]
string
Repository name.
provider
string
Repository provider.
url [_required_]
string
Repository URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2`
default: `v2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service.
Option 3
object
Service definition v2.1 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.1 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
enum
Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.1`
default: `v2.1`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
Option 4
object
Service definition v2.2 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
ci-pipeline-fingerprints
[string]
A set of CI fingerprints.
contacts
[object]
A list of contacts related to the services.
contact [_required_]
string
Contact value.
name
string
Contact Name.
type [_required_]
string
Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
languages
[string]
The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.2`
default: `v2.2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
type
string
The type of service.
id
string
Service definition id.
type
string
Service definition type.
```
{
  "data": [
    {
      "attributes": {
        "meta": {
          "github-html-url": "string",
          "ingested-schema-version": "string",
          "ingestion-source": "string",
          "last-modified-time": "string",
          "origin": "string",
          "origin-detail": "string",
          "warnings": [
            {
              "instance-location": "string",
              "keyword-location": "string",
              "message": "string"
            }
          ]
        },
        "schema": {
          "contact": {
            "email": "contact@datadoghq.com",
            "slack": "https://yourcompany.slack.com/archives/channel123"
          },
          "extensions": {
            "myorg/extension": "extensionValue"
          },
          "external-resources": [
            {
              "name": "Runbook",
              "type": "runbook",
              "url": "https://my-runbook"
            }
          ],
          "info": {
            "dd-service": "myservice",
            "description": "A shopping cart service",
            "display-name": "My Service",
            "service-tier": "Tier 1"
          },
          "integrations": {
            "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
          },
          "org": {
            "application": "E-Commerce",
            "team": "my-team"
          },
          "schema-version": "v1",
          "tags": [
            "my:tag",
            "service:tag"
          ]
        }
      },
      "id": "string",
      "type": "string"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=typescript)


#####  Get all service definitions
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all service definitions
```
"""
Get all service definitions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_schema_versions import ServiceDefinitionSchemaVersions

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.list_service_definitions(
        schema_version=ServiceDefinitionSchemaVersions.V2_1,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all service definitions
```
# Get all service definitions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new
opts = {
  schema_version: ServiceDefinitionSchemaVersions::V2_1,
}
p api_instance.list_service_definitions(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all service definitions
```
// Get all service definitions returns "OK" response

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
	api := datadogV2.NewServiceDefinitionApi(apiClient)
	resp, r, err := api.ListServiceDefinitions(ctx, *datadogV2.NewListServiceDefinitionsOptionalParameters().WithSchemaVersion(datadogV2.SERVICEDEFINITIONSCHEMAVERSIONS_V2_1))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.ListServiceDefinitions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.ListServiceDefinitions`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all service definitions
```
// Get all service definitions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.api.ServiceDefinitionApi.ListServiceDefinitionsOptionalParameters;
import com.datadog.api.client.v2.model.ServiceDefinitionSchemaVersions;
import com.datadog.api.client.v2.model.ServiceDefinitionsListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    try {
      ServiceDefinitionsListResponse result =
          apiInstance.listServiceDefinitions(
              new ListServiceDefinitionsOptionalParameters()
                  .schemaVersion(ServiceDefinitionSchemaVersions.V2_1));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDefinitionApi#listServiceDefinitions");
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

#####  Get all service definitions
```
// Get all service definitions returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ListServiceDefinitionsOptionalParams;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionSchemaVersions;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api
        .list_service_definitions(
            ListServiceDefinitionsOptionalParams::default()
                .schema_version(ServiceDefinitionSchemaVersions::V2_1),
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

#####  Get all service definitions
```
/**
 * Get all service definitions returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiListServiceDefinitionsRequest = {
  schemaVersion: "v2.1",
};

apiInstance
  .listServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionsListResponse) => {
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
## [Create or update service definition](https://docs.datadoghq.com/api/latest/service-definition/#create-or-update-service-definition)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-definition/#create-or-update-service-definition-v2)


POST https://api.ap1.datadoghq.com/api/v2/services/definitionshttps://api.ap2.datadoghq.com/api/v2/services/definitionshttps://api.datadoghq.eu/api/v2/services/definitionshttps://api.ddog-gov.com/api/v2/services/definitionshttps://api.datadoghq.com/api/v2/services/definitionshttps://api.us3.datadoghq.com/api/v2/services/definitionshttps://api.us5.datadoghq.com/api/v2/services/definitions
### Overview
Create or update service definition in the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_write` permission.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.
### Request
#### Body Data (required)
Service Definition YAML/JSON.
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


Field
Type
Description
Option 1
object
Service definition v2.2 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
ci-pipeline-fingerprints
[string]
A set of CI fingerprints.
contacts
[object]
A list of contacts related to the services.
contact [_required_]
string
Contact value.
name
string
Contact Name.
type [_required_]
string
Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
languages
[string]
The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.2`
default: `v2.2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
type
string
The type of service.
Option 2
object
Service definition v2.1 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.1 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
enum
Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.1`
default: `v2.1`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
Option 3
object
Service definition V2 for providing service metadata and integrations.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
dd-team
string
Experimental feature. A Team handle that matches a Team in the Datadog Teams product.
docs
[object]
A list of documentation related to the services.
name [_required_]
string
Document name.
provider
string
Document provider.
url [_required_]
string
Document URL.
extensions
object
Extensions to V2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
string
PagerDuty service URL for the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
type [_required_]
enum
Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`
url [_required_]
string
Link URL.
repos
[object]
A list of code repositories related to the services.
name [_required_]
string
Repository name.
provider
string
Repository provider.
url [_required_]
string
Repository URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2`
default: `v2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service.
Option 4
string
Service Definition in raw JSON/YAML representation.
#####  Create or update service definition using schema v2 returns "CREATED" response
```
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "dd-team": "my-team",
  "docs": [
    {
      "name": "Architecture",
      "provider": "google drive",
      "url": "https://gdrive/mydoc"
    }
  ],
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    }
  ],
  "repos": [
    {
      "name": "Source Code",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    }
  ],
  "schema-version": "v2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
```

Copy
#####  Create or update service definition using schema v2-1 returns "CREATED" response
```
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.1",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
```

Copy
#####  Create or update service definition using schema v2-2 returns "CREATED" response
```
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-definition/#CreateOrUpdateServiceDefinitions-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-definition/#CreateOrUpdateServiceDefinitions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-definition/#CreateOrUpdateServiceDefinitions-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/service-definition/#CreateOrUpdateServiceDefinitions-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-definition/#CreateOrUpdateServiceDefinitions-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


Create service definitions response.
Field
Type
Description
data
[object]
Create service definitions response payload.
attributes
object
Service definition attributes.
meta
object
Metadata about a service definition.
github-html-url
string
GitHub HTML URL.
ingested-schema-version
string
Ingestion schema version.
ingestion-source
string
Ingestion source of the service definition.
last-modified-time
string
Last modified time of the service definition.
origin
string
User defined origin of the service definition.
origin-detail
string
User defined origin's detail of the service definition.
warnings
[object]
A list of schema validation warnings.
instance-location
string
The warning instance location.
keyword-location
string
The warning keyword location.
message
string
The warning message.
schema
<oneOf>
Service definition schema.
Option 1
object
**DEPRECATED** : Deprecated - Service definition V1 for providing additional service metadata and integrations.
contact
object
Contact information about the service.
email
string
Service owner’s email.
slack
string
Service owner’s Slack channel.
extensions
object
Extensions to V1 schema.
external-resources
[object]
A list of external links related to the services.
name [_required_]
string
Link name.
type [_required_]
enum
Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`
url [_required_]
string
Link URL.
info [_required_]
object
Basic information about a service.
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
display-name
string
A friendly name of the service.
service-tier
string
Service tier.
integrations
object
Third party integrations that Datadog supports.
pagerduty
string
PagerDuty service URL for the service.
org
object
Org related information about the service.
application
string
App feature this service supports.
team
string
Team that owns the service.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v1`
default: `v1`
tags
[string]
A set of custom tags.
Option 2
object
Service definition V2 for providing service metadata and integrations.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
dd-team
string
Experimental feature. A Team handle that matches a Team in the Datadog Teams product.
docs
[object]
A list of documentation related to the services.
name [_required_]
string
Document name.
provider
string
Document provider.
url [_required_]
string
Document URL.
extensions
object
Extensions to V2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
string
PagerDuty service URL for the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
type [_required_]
enum
Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`
url [_required_]
string
Link URL.
repos
[object]
A list of code repositories related to the services.
name [_required_]
string
Repository name.
provider
string
Repository provider.
url [_required_]
string
Repository URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2`
default: `v2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service.
Option 3
object
Service definition v2.1 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.1 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
enum
Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.1`
default: `v2.1`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
Option 4
object
Service definition v2.2 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
ci-pipeline-fingerprints
[string]
A set of CI fingerprints.
contacts
[object]
A list of contacts related to the services.
contact [_required_]
string
Contact value.
name
string
Contact Name.
type [_required_]
string
Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
languages
[string]
The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.2`
default: `v2.2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
type
string
The type of service.
id
string
Service definition id.
type
string
Service definition type.
```
{
  "data": [
    {
      "attributes": {
        "meta": {
          "github-html-url": "string",
          "ingested-schema-version": "string",
          "ingestion-source": "string",
          "last-modified-time": "string",
          "origin": "string",
          "origin-detail": "string",
          "warnings": [
            {
              "instance-location": "string",
              "keyword-location": "string",
              "message": "string"
            }
          ]
        },
        "schema": {
          "contact": {
            "email": "contact@datadoghq.com",
            "slack": "https://yourcompany.slack.com/archives/channel123"
          },
          "extensions": {
            "myorg/extension": "extensionValue"
          },
          "external-resources": [
            {
              "name": "Runbook",
              "type": "runbook",
              "url": "https://my-runbook"
            }
          ],
          "info": {
            "dd-service": "myservice",
            "description": "A shopping cart service",
            "display-name": "My Service",
            "service-tier": "Tier 1"
          },
          "integrations": {
            "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
          },
          "org": {
            "application": "E-Commerce",
            "team": "my-team"
          },
          "schema-version": "v1",
          "tags": [
            "my:tag",
            "service:tag"
          ]
        }
      },
      "id": "string",
      "type": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=typescript)


#####  Create or update service definition using schema v2 returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "dd-team": "my-team",
  "docs": [
    {
      "name": "Architecture",
      "provider": "google drive",
      "url": "https://gdrive/mydoc"
    }
  ],
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    }
  ],
  "repos": [
    {
      "name": "Source Code",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    }
  ],
  "schema-version": "v2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
EOF  

                        
```

#####  Create or update service definition using schema v2-1 returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.1",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
EOF  

                        
```

#####  Create or update service definition using schema v2-2 returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
EOF  

                        
```

#####  Create or update service definition using schema v2 returns "CREATED" response 
```
// Create or update service definition using schema v2 returns "CREATED" response

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
	body := datadogV2.ServiceDefinitionsCreateRequest{
		ServiceDefinitionV2: &datadogV2.ServiceDefinitionV2{
			Contacts: []datadogV2.ServiceDefinitionV2Contact{
				datadogV2.ServiceDefinitionV2Contact{
					ServiceDefinitionV2Email: &datadogV2.ServiceDefinitionV2Email{
						Contact: "contact@datadoghq.com",
						Name:    datadog.PtrString("Team Email"),
						Type:    datadogV2.SERVICEDEFINITIONV2EMAILTYPE_EMAIL,
					}},
			},
			DdService: "service-exampleservicedefinition",
			DdTeam:    datadog.PtrString("my-team"),
			Docs: []datadogV2.ServiceDefinitionV2Doc{
				{
					Name:     "Architecture",
					Provider: datadog.PtrString("google drive"),
					Url:      "https://gdrive/mydoc",
				},
			},
			Extensions: map[string]interface{}{
				"myorgextension": "extensionvalue",
			},
			Integrations: &datadogV2.ServiceDefinitionV2Integrations{
				Opsgenie: &datadogV2.ServiceDefinitionV2Opsgenie{
					Region:     datadogV2.SERVICEDEFINITIONV2OPSGENIEREGION_US.Ptr(),
					ServiceUrl: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
				},
				Pagerduty: datadog.PtrString("https://my-org.pagerduty.com/service-directory/PMyService"),
			},
			Links: []datadogV2.ServiceDefinitionV2Link{
				{
					Name: "Runbook",
					Type: datadogV2.SERVICEDEFINITIONV2LINKTYPE_RUNBOOK,
					Url:  "https://my-runbook",
				},
			},
			Repos: []datadogV2.ServiceDefinitionV2Repo{
				{
					Name:     "Source Code",
					Provider: datadog.PtrString("GitHub"),
					Url:      "https://github.com/DataDog/schema",
				},
			},
			SchemaVersion: datadogV2.SERVICEDEFINITIONV2VERSION_V2,
			Tags: []string{
				"my:tag",
				"service:tag",
			},
			Team: datadog.PtrString("my-team"),
		}}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceDefinitionApi(apiClient)
	resp, r, err := api.CreateOrUpdateServiceDefinitions(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`:\n%s\n", responseContent)
}

```

Copy
#####  Create or update service definition using schema v2-1 returns "CREATED" response 
```
// Create or update service definition using schema v2-1 returns "CREATED" response

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
	body := datadogV2.ServiceDefinitionsCreateRequest{
		ServiceDefinitionV2Dot1: &datadogV2.ServiceDefinitionV2Dot1{
			Contacts: []datadogV2.ServiceDefinitionV2Dot1Contact{
				datadogV2.ServiceDefinitionV2Dot1Contact{
					ServiceDefinitionV2Dot1Email: &datadogV2.ServiceDefinitionV2Dot1Email{
						Contact: "contact@datadoghq.com",
						Name:    datadog.PtrString("Team Email"),
						Type:    datadogV2.SERVICEDEFINITIONV2DOT1EMAILTYPE_EMAIL,
					}},
			},
			DdService: "service-exampleservicedefinition",
			Extensions: map[string]interface{}{
				"myorgextension": "extensionvalue",
			},
			Integrations: &datadogV2.ServiceDefinitionV2Dot1Integrations{
				Opsgenie: &datadogV2.ServiceDefinitionV2Dot1Opsgenie{
					Region:     datadogV2.SERVICEDEFINITIONV2DOT1OPSGENIEREGION_US.Ptr(),
					ServiceUrl: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
				},
				Pagerduty: &datadogV2.ServiceDefinitionV2Dot1Pagerduty{
					ServiceUrl: datadog.PtrString("https://my-org.pagerduty.com/service-directory/PMyService"),
				},
			},
			Links: []datadogV2.ServiceDefinitionV2Dot1Link{
				{
					Name: "Runbook",
					Type: datadogV2.SERVICEDEFINITIONV2DOT1LINKTYPE_RUNBOOK,
					Url:  "https://my-runbook",
				},
				{
					Name:     "Source Code",
					Type:     datadogV2.SERVICEDEFINITIONV2DOT1LINKTYPE_REPO,
					Provider: datadog.PtrString("GitHub"),
					Url:      "https://github.com/DataDog/schema",
				},
				{
					Name:     "Architecture",
					Type:     datadogV2.SERVICEDEFINITIONV2DOT1LINKTYPE_DOC,
					Provider: datadog.PtrString("Gigoogle drivetHub"),
					Url:      "https://my-runbook",
				},
			},
			SchemaVersion: datadogV2.SERVICEDEFINITIONV2DOT1VERSION_V2_1,
			Tags: []string{
				"my:tag",
				"service:tag",
			},
			Team: datadog.PtrString("my-team"),
		}}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceDefinitionApi(apiClient)
	resp, r, err := api.CreateOrUpdateServiceDefinitions(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`:\n%s\n", responseContent)
}

```

Copy
#####  Create or update service definition using schema v2-2 returns "CREATED" response 
```
// Create or update service definition using schema v2-2 returns "CREATED" response

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
	body := datadogV2.ServiceDefinitionsCreateRequest{
		ServiceDefinitionV2Dot2: &datadogV2.ServiceDefinitionV2Dot2{
			Contacts: []datadogV2.ServiceDefinitionV2Dot2Contact{
				{
					Contact: "contact@datadoghq.com",
					Name:    datadog.PtrString("Team Email"),
					Type:    "email",
				},
			},
			DdService: "service-exampleservicedefinition",
			Extensions: map[string]interface{}{
				"myorgextension": "extensionvalue",
			},
			Integrations: &datadogV2.ServiceDefinitionV2Dot2Integrations{
				Opsgenie: &datadogV2.ServiceDefinitionV2Dot2Opsgenie{
					Region:     datadogV2.SERVICEDEFINITIONV2DOT2OPSGENIEREGION_US.Ptr(),
					ServiceUrl: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
				},
				Pagerduty: &datadogV2.ServiceDefinitionV2Dot2Pagerduty{
					ServiceUrl: datadog.PtrString("https://my-org.pagerduty.com/service-directory/PMyService"),
				},
			},
			Links: []datadogV2.ServiceDefinitionV2Dot2Link{
				{
					Name: "Runbook",
					Type: "runbook",
					Url:  "https://my-runbook",
				},
				{
					Name:     "Source Code",
					Type:     "repo",
					Provider: datadog.PtrString("GitHub"),
					Url:      "https://github.com/DataDog/schema",
				},
				{
					Name:     "Architecture",
					Type:     "doc",
					Provider: datadog.PtrString("Gigoogle drivetHub"),
					Url:      "https://my-runbook",
				},
			},
			SchemaVersion: datadogV2.SERVICEDEFINITIONV2DOT2VERSION_V2_2,
			Tags: []string{
				"my:tag",
				"service:tag",
			},
			Team: datadog.PtrString("my-team"),
		}}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceDefinitionApi(apiClient)
	resp, r, err := api.CreateOrUpdateServiceDefinitions(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create or update service definition using schema v2 returns "CREATED" response 
```
// Create or update service definition using schema v2 returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.model.ServiceDefinitionCreateResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionV2;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Contact;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Doc;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Email;
import com.datadog.api.client.v2.model.ServiceDefinitionV2EmailType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Integrations;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Link;
import com.datadog.api.client.v2.model.ServiceDefinitionV2LinkType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Opsgenie;
import com.datadog.api.client.v2.model.ServiceDefinitionV2OpsgenieRegion;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Repo;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Version;
import com.datadog.api.client.v2.model.ServiceDefinitionsCreateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    ServiceDefinitionsCreateRequest body =
        new ServiceDefinitionsCreateRequest(
            new ServiceDefinitionV2()
                .contacts(
                    Collections.singletonList(
                        new ServiceDefinitionV2Contact(
                            new ServiceDefinitionV2Email()
                                .contact("contact@datadoghq.com")
                                .name("Team Email")
                                .type(ServiceDefinitionV2EmailType.EMAIL))))
                .ddService("service-exampleservicedefinition")
                .ddTeam("my-team")
                .docs(
                    Collections.singletonList(
                        new ServiceDefinitionV2Doc()
                            .name("Architecture")
                            .provider("google drive")
                            .url("https://gdrive/mydoc")))
                .extensions(Map.ofEntries(Map.entry("myorgextension", "extensionvalue")))
                .integrations(
                    new ServiceDefinitionV2Integrations()
                        .opsgenie(
                            new ServiceDefinitionV2Opsgenie()
                                .region(ServiceDefinitionV2OpsgenieRegion.US)
                                .serviceUrl(
                                    "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"))
                        .pagerduty("https://my-org.pagerduty.com/service-directory/PMyService"))
                .links(
                    Collections.singletonList(
                        new ServiceDefinitionV2Link()
                            .name("Runbook")
                            .type(ServiceDefinitionV2LinkType.RUNBOOK)
                            .url("https://my-runbook")))
                .repos(
                    Collections.singletonList(
                        new ServiceDefinitionV2Repo()
                            .name("Source Code")
                            .provider("GitHub")
                            .url("https://github.com/DataDog/schema")))
                .schemaVersion(ServiceDefinitionV2Version.V2)
                .tags(Arrays.asList("my:tag", "service:tag"))
                .team("my-team"));

    try {
      ServiceDefinitionCreateResponse result = apiInstance.createOrUpdateServiceDefinitions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceDefinitionApi#createOrUpdateServiceDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create or update service definition using schema v2-1 returns "CREATED" response 
```
// Create or update service definition using schema v2-1 returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.model.ServiceDefinitionCreateResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Contact;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Email;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1EmailType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Integrations;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Link;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1LinkType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Opsgenie;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1OpsgenieRegion;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Pagerduty;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Version;
import com.datadog.api.client.v2.model.ServiceDefinitionsCreateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    ServiceDefinitionsCreateRequest body =
        new ServiceDefinitionsCreateRequest(
            new ServiceDefinitionV2Dot1()
                .contacts(
                    Collections.singletonList(
                        new ServiceDefinitionV2Dot1Contact(
                            new ServiceDefinitionV2Dot1Email()
                                .contact("contact@datadoghq.com")
                                .name("Team Email")
                                .type(ServiceDefinitionV2Dot1EmailType.EMAIL))))
                .ddService("service-exampleservicedefinition")
                .extensions(Map.ofEntries(Map.entry("myorgextension", "extensionvalue")))
                .integrations(
                    new ServiceDefinitionV2Dot1Integrations()
                        .opsgenie(
                            new ServiceDefinitionV2Dot1Opsgenie()
                                .region(ServiceDefinitionV2Dot1OpsgenieRegion.US)
                                .serviceUrl(
                                    "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"))
                        .pagerduty(
                            new ServiceDefinitionV2Dot1Pagerduty()
                                .serviceUrl(
                                    "https://my-org.pagerduty.com/service-directory/PMyService")))
                .links(
                    Arrays.asList(
                        new ServiceDefinitionV2Dot1Link()
                            .name("Runbook")
                            .type(ServiceDefinitionV2Dot1LinkType.RUNBOOK)
                            .url("https://my-runbook"),
                        new ServiceDefinitionV2Dot1Link()
                            .name("Source Code")
                            .type(ServiceDefinitionV2Dot1LinkType.REPO)
                            .provider("GitHub")
                            .url("https://github.com/DataDog/schema"),
                        new ServiceDefinitionV2Dot1Link()
                            .name("Architecture")
                            .type(ServiceDefinitionV2Dot1LinkType.DOC)
                            .provider("Gigoogle drivetHub")
                            .url("https://my-runbook")))
                .schemaVersion(ServiceDefinitionV2Dot1Version.V2_1)
                .tags(Arrays.asList("my:tag", "service:tag"))
                .team("my-team"));

    try {
      ServiceDefinitionCreateResponse result = apiInstance.createOrUpdateServiceDefinitions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceDefinitionApi#createOrUpdateServiceDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create or update service definition using schema v2-2 returns "CREATED" response 
```
// Create or update service definition using schema v2-2 returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.model.ServiceDefinitionCreateResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Contact;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Integrations;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Link;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Opsgenie;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2OpsgenieRegion;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Pagerduty;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Version;
import com.datadog.api.client.v2.model.ServiceDefinitionsCreateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    ServiceDefinitionsCreateRequest body =
        new ServiceDefinitionsCreateRequest(
            new ServiceDefinitionV2Dot2()
                .contacts(
                    Collections.singletonList(
                        new ServiceDefinitionV2Dot2Contact()
                            .contact("contact@datadoghq.com")
                            .name("Team Email")
                            .type("email")))
                .ddService("service-exampleservicedefinition")
                .extensions(Map.ofEntries(Map.entry("myorgextension", "extensionvalue")))
                .integrations(
                    new ServiceDefinitionV2Dot2Integrations()
                        .opsgenie(
                            new ServiceDefinitionV2Dot2Opsgenie()
                                .region(ServiceDefinitionV2Dot2OpsgenieRegion.US)
                                .serviceUrl(
                                    "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"))
                        .pagerduty(
                            new ServiceDefinitionV2Dot2Pagerduty()
                                .serviceUrl(
                                    "https://my-org.pagerduty.com/service-directory/PMyService")))
                .links(
                    Arrays.asList(
                        new ServiceDefinitionV2Dot2Link()
                            .name("Runbook")
                            .type("runbook")
                            .url("https://my-runbook"),
                        new ServiceDefinitionV2Dot2Link()
                            .name("Source Code")
                            .type("repo")
                            .provider("GitHub")
                            .url("https://github.com/DataDog/schema"),
                        new ServiceDefinitionV2Dot2Link()
                            .name("Architecture")
                            .type("doc")
                            .provider("Gigoogle drivetHub")
                            .url("https://my-runbook")))
                .schemaVersion(ServiceDefinitionV2Dot2Version.V2_2)
                .tags(Arrays.asList("my:tag", "service:tag"))
                .team("my-team"));

    try {
      ServiceDefinitionCreateResponse result = apiInstance.createOrUpdateServiceDefinitions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceDefinitionApi#createOrUpdateServiceDefinitions");
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

#####  Create or update service definition using schema v2 returns "CREATED" response 
```
"""
Create or update service definition using schema v2 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2 import ServiceDefinitionV2
from datadog_api_client.v2.model.service_definition_v2_doc import ServiceDefinitionV2Doc
from datadog_api_client.v2.model.service_definition_v2_email import ServiceDefinitionV2Email
from datadog_api_client.v2.model.service_definition_v2_email_type import ServiceDefinitionV2EmailType
from datadog_api_client.v2.model.service_definition_v2_integrations import ServiceDefinitionV2Integrations
from datadog_api_client.v2.model.service_definition_v2_link import ServiceDefinitionV2Link
from datadog_api_client.v2.model.service_definition_v2_link_type import ServiceDefinitionV2LinkType
from datadog_api_client.v2.model.service_definition_v2_opsgenie import ServiceDefinitionV2Opsgenie
from datadog_api_client.v2.model.service_definition_v2_opsgenie_region import ServiceDefinitionV2OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_repo import ServiceDefinitionV2Repo
from datadog_api_client.v2.model.service_definition_v2_version import ServiceDefinitionV2Version

body = ServiceDefinitionV2(
    contacts=[
        ServiceDefinitionV2Email(
            contact="contact@datadoghq.com",
            name="Team Email",
            type=ServiceDefinitionV2EmailType.EMAIL,
        ),
    ],
    dd_service="service-exampleservicedefinition",
    dd_team="my-team",
    docs=[
        ServiceDefinitionV2Doc(
            name="Architecture",
            provider="google drive",
            url="https://gdrive/mydoc",
        ),
    ],
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Integrations(
        opsgenie=ServiceDefinitionV2Opsgenie(
            region=ServiceDefinitionV2OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty="https://my-org.pagerduty.com/service-directory/PMyService",
    ),
    links=[
        ServiceDefinitionV2Link(
            name="Runbook",
            type=ServiceDefinitionV2LinkType.RUNBOOK,
            url="https://my-runbook",
        ),
    ],
    repos=[
        ServiceDefinitionV2Repo(
            name="Source Code",
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
    ],
    schema_version=ServiceDefinitionV2Version.V2,
    tags=[
        "my:tag",
        "service:tag",
    ],
    team="my-team",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.create_or_update_service_definitions(body=body)

    print(response)

```

Copy
#####  Create or update service definition using schema v2-1 returns "CREATED" response 
```
"""
Create or update service definition using schema v2-1 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2_dot1 import ServiceDefinitionV2Dot1
from datadog_api_client.v2.model.service_definition_v2_dot1_email import ServiceDefinitionV2Dot1Email
from datadog_api_client.v2.model.service_definition_v2_dot1_email_type import ServiceDefinitionV2Dot1EmailType
from datadog_api_client.v2.model.service_definition_v2_dot1_integrations import ServiceDefinitionV2Dot1Integrations
from datadog_api_client.v2.model.service_definition_v2_dot1_link import ServiceDefinitionV2Dot1Link
from datadog_api_client.v2.model.service_definition_v2_dot1_link_type import ServiceDefinitionV2Dot1LinkType
from datadog_api_client.v2.model.service_definition_v2_dot1_opsgenie import ServiceDefinitionV2Dot1Opsgenie
from datadog_api_client.v2.model.service_definition_v2_dot1_opsgenie_region import ServiceDefinitionV2Dot1OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_dot1_pagerduty import ServiceDefinitionV2Dot1Pagerduty
from datadog_api_client.v2.model.service_definition_v2_dot1_version import ServiceDefinitionV2Dot1Version

body = ServiceDefinitionV2Dot1(
    contacts=[
        ServiceDefinitionV2Dot1Email(
            contact="contact@datadoghq.com",
            name="Team Email",
            type=ServiceDefinitionV2Dot1EmailType.EMAIL,
        ),
    ],
    dd_service="service-exampleservicedefinition",
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Dot1Integrations(
        opsgenie=ServiceDefinitionV2Dot1Opsgenie(
            region=ServiceDefinitionV2Dot1OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty=ServiceDefinitionV2Dot1Pagerduty(
            service_url="https://my-org.pagerduty.com/service-directory/PMyService",
        ),
    ),
    links=[
        ServiceDefinitionV2Dot1Link(
            name="Runbook",
            type=ServiceDefinitionV2Dot1LinkType.RUNBOOK,
            url="https://my-runbook",
        ),
        ServiceDefinitionV2Dot1Link(
            name="Source Code",
            type=ServiceDefinitionV2Dot1LinkType.REPO,
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
        ServiceDefinitionV2Dot1Link(
            name="Architecture",
            type=ServiceDefinitionV2Dot1LinkType.DOC,
            provider="Gigoogle drivetHub",
            url="https://my-runbook",
        ),
    ],
    schema_version=ServiceDefinitionV2Dot1Version.V2_1,
    tags=[
        "my:tag",
        "service:tag",
    ],
    team="my-team",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.create_or_update_service_definitions(body=body)

    print(response)

```

Copy
#####  Create or update service definition using schema v2-2 returns "CREATED" response 
```
"""
Create or update service definition using schema v2-2 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2_dot2 import ServiceDefinitionV2Dot2
from datadog_api_client.v2.model.service_definition_v2_dot2_contact import ServiceDefinitionV2Dot2Contact
from datadog_api_client.v2.model.service_definition_v2_dot2_integrations import ServiceDefinitionV2Dot2Integrations
from datadog_api_client.v2.model.service_definition_v2_dot2_link import ServiceDefinitionV2Dot2Link
from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie import ServiceDefinitionV2Dot2Opsgenie
from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie_region import ServiceDefinitionV2Dot2OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_dot2_pagerduty import ServiceDefinitionV2Dot2Pagerduty
from datadog_api_client.v2.model.service_definition_v2_dot2_version import ServiceDefinitionV2Dot2Version

body = ServiceDefinitionV2Dot2(
    contacts=[
        ServiceDefinitionV2Dot2Contact(
            contact="contact@datadoghq.com",
            name="Team Email",
            type="email",
        ),
    ],
    dd_service="service-exampleservicedefinition",
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Dot2Integrations(
        opsgenie=ServiceDefinitionV2Dot2Opsgenie(
            region=ServiceDefinitionV2Dot2OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty=ServiceDefinitionV2Dot2Pagerduty(
            service_url="https://my-org.pagerduty.com/service-directory/PMyService",
        ),
    ),
    links=[
        ServiceDefinitionV2Dot2Link(
            name="Runbook",
            type="runbook",
            url="https://my-runbook",
        ),
        ServiceDefinitionV2Dot2Link(
            name="Source Code",
            type="repo",
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
        ServiceDefinitionV2Dot2Link(
            name="Architecture",
            type="doc",
            provider="Gigoogle drivetHub",
            url="https://my-runbook",
        ),
    ],
    schema_version=ServiceDefinitionV2Dot2Version.V2_2,
    tags=[
        "my:tag",
        "service:tag",
    ],
    team="my-team",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.create_or_update_service_definitions(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create or update service definition using schema v2 returns "CREATED" response 
```
# Create or update service definition using schema v2 returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new

body = DatadogAPIClient::V2::ServiceDefinitionV2.new({
  contacts: [
    DatadogAPIClient::V2::ServiceDefinitionV2Email.new({
      contact: "contact@datadoghq.com",
      name: "Team Email",
      type: DatadogAPIClient::V2::ServiceDefinitionV2EmailType::EMAIL,
    }),
  ],
  dd_service: "service-exampleservicedefinition",
  dd_team: "my-team",
  docs: [
    DatadogAPIClient::V2::ServiceDefinitionV2Doc.new({
      name: "Architecture",
      provider: "google drive",
      url: "https://gdrive/mydoc",
    }),
  ],
  extensions: {
    "myorgextension": "extensionvalue",
  },
  integrations: DatadogAPIClient::V2::ServiceDefinitionV2Integrations.new({
    opsgenie: DatadogAPIClient::V2::ServiceDefinitionV2Opsgenie.new({
      region: DatadogAPIClient::V2::ServiceDefinitionV2OpsgenieRegion::US,
      service_url: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
    }),
    pagerduty: "https://my-org.pagerduty.com/service-directory/PMyService",
  }),
  links: [
    DatadogAPIClient::V2::ServiceDefinitionV2Link.new({
      name: "Runbook",
      type: DatadogAPIClient::V2::ServiceDefinitionV2LinkType::RUNBOOK,
      url: "https://my-runbook",
    }),
  ],
  repos: [
    DatadogAPIClient::V2::ServiceDefinitionV2Repo.new({
      name: "Source Code",
      provider: "GitHub",
      url: "https://github.com/DataDog/schema",
    }),
  ],
  schema_version: DatadogAPIClient::V2::ServiceDefinitionV2Version::V2,
  tags: [
    "my:tag",
    "service:tag",
  ],
  team: "my-team",
})
p api_instance.create_or_update_service_definitions(body)

```

Copy
#####  Create or update service definition using schema v2-1 returns "CREATED" response 
```
# Create or update service definition using schema v2-1 returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new

body = DatadogAPIClient::V2::ServiceDefinitionV2Dot1.new({
  contacts: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Email.new({
      contact: "contact@datadoghq.com",
      name: "Team Email",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1EmailType::EMAIL,
    }),
  ],
  dd_service: "service-exampleservicedefinition",
  extensions: {
    "myorgextension": "extensionvalue",
  },
  integrations: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Integrations.new({
    opsgenie: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Opsgenie.new({
      region: DatadogAPIClient::V2::ServiceDefinitionV2Dot1OpsgenieRegion::US,
      service_url: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
    }),
    pagerduty: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Pagerduty.new({
      service_url: "https://my-org.pagerduty.com/service-directory/PMyService",
    }),
  }),
  links: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Link.new({
      name: "Runbook",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1LinkType::RUNBOOK,
      url: "https://my-runbook",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Link.new({
      name: "Source Code",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1LinkType::REPO,
      provider: "GitHub",
      url: "https://github.com/DataDog/schema",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Link.new({
      name: "Architecture",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1LinkType::DOC,
      provider: "Gigoogle drivetHub",
      url: "https://my-runbook",
    }),
  ],
  schema_version: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Version::V2_1,
  tags: [
    "my:tag",
    "service:tag",
  ],
  team: "my-team",
})
p api_instance.create_or_update_service_definitions(body)

```

Copy
#####  Create or update service definition using schema v2-2 returns "CREATED" response 
```
# Create or update service definition using schema v2-2 returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new

body = DatadogAPIClient::V2::ServiceDefinitionV2Dot2.new({
  contacts: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Contact.new({
      contact: "contact@datadoghq.com",
      name: "Team Email",
      type: "email",
    }),
  ],
  dd_service: "service-exampleservicedefinition",
  extensions: {
    "myorgextension": "extensionvalue",
  },
  integrations: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Integrations.new({
    opsgenie: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Opsgenie.new({
      region: DatadogAPIClient::V2::ServiceDefinitionV2Dot2OpsgenieRegion::US,
      service_url: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
    }),
    pagerduty: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Pagerduty.new({
      service_url: "https://my-org.pagerduty.com/service-directory/PMyService",
    }),
  }),
  links: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Link.new({
      name: "Runbook",
      type: "runbook",
      url: "https://my-runbook",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Link.new({
      name: "Source Code",
      type: "repo",
      provider: "GitHub",
      url: "https://github.com/DataDog/schema",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Link.new({
      name: "Architecture",
      type: "doc",
      provider: "Gigoogle drivetHub",
      url: "https://my-runbook",
    }),
  ],
  schema_version: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Version::V2_2,
  tags: [
    "my:tag",
    "service:tag",
  ],
  team: "my-team",
})
p api_instance.create_or_update_service_definitions(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create or update service definition using schema v2 returns "CREATED" response 
```
// Create or update service definition using schema v2 returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Contact;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Doc;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Email;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2EmailType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Integrations;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Link;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2LinkType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Opsgenie;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2OpsgenieRegion;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Repo;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Version;
use datadog_api_client::datadogV2::model::ServiceDefinitionsCreateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = ServiceDefinitionsCreateRequest::ServiceDefinitionV2(Box::new(
        ServiceDefinitionV2::new(
            "service-exampleservicedefinition".to_string(),
            ServiceDefinitionV2Version::V2,
        )
        .contacts(vec![ServiceDefinitionV2Contact::ServiceDefinitionV2Email(
            Box::new(
                ServiceDefinitionV2Email::new(
                    "contact@datadoghq.com".to_string(),
                    ServiceDefinitionV2EmailType::EMAIL,
                )
                .name("Team Email".to_string()),
            ),
        )])
        .dd_team("my-team".to_string())
        .docs(vec![ServiceDefinitionV2Doc::new(
            "Architecture".to_string(),
            "https://gdrive/mydoc".to_string(),
        )
        .provider("google drive".to_string())])
        .extensions(BTreeMap::from([(
            "myorgextension".to_string(),
            Value::from("extensionvalue"),
        )]))
        .integrations(
            ServiceDefinitionV2Integrations::new()
                .opsgenie(
                    ServiceDefinitionV2Opsgenie::new(
                        "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
                            .to_string(),
                    )
                    .region(ServiceDefinitionV2OpsgenieRegion::US),
                )
                .pagerduty("https://my-org.pagerduty.com/service-directory/PMyService".to_string()),
        )
        .links(vec![ServiceDefinitionV2Link::new(
            "Runbook".to_string(),
            ServiceDefinitionV2LinkType::RUNBOOK,
            "https://my-runbook".to_string(),
        )])
        .repos(vec![ServiceDefinitionV2Repo::new(
            "Source Code".to_string(),
            "https://github.com/DataDog/schema".to_string(),
        )
        .provider("GitHub".to_string())])
        .tags(vec!["my:tag".to_string(), "service:tag".to_string()])
        .team("my-team".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api.create_or_update_service_definitions(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create or update service definition using schema v2-1 returns "CREATED" response 
```
// Create or update service definition using schema v2-1 returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Contact;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Email;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1EmailType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Integrations;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Link;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1LinkType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Opsgenie;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1OpsgenieRegion;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Pagerduty;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Version;
use datadog_api_client::datadogV2::model::ServiceDefinitionsCreateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = ServiceDefinitionsCreateRequest::ServiceDefinitionV2Dot1(Box::new(
        ServiceDefinitionV2Dot1::new(
            "service-exampleservicedefinition".to_string(),
            ServiceDefinitionV2Dot1Version::V2_1,
        )
        .contacts(vec![
            ServiceDefinitionV2Dot1Contact::ServiceDefinitionV2Dot1Email(Box::new(
                ServiceDefinitionV2Dot1Email::new(
                    "contact@datadoghq.com".to_string(),
                    ServiceDefinitionV2Dot1EmailType::EMAIL,
                )
                .name("Team Email".to_string()),
            )),
        ])
        .extensions(BTreeMap::from([(
            "myorgextension".to_string(),
            Value::from("extensionvalue"),
        )]))
        .integrations(
            ServiceDefinitionV2Dot1Integrations::new()
                .opsgenie(
                    ServiceDefinitionV2Dot1Opsgenie::new(
                        "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
                            .to_string(),
                    )
                    .region(ServiceDefinitionV2Dot1OpsgenieRegion::US),
                )
                .pagerduty(ServiceDefinitionV2Dot1Pagerduty::new().service_url(
                    "https://my-org.pagerduty.com/service-directory/PMyService".to_string(),
                )),
        )
        .links(vec![
            ServiceDefinitionV2Dot1Link::new(
                "Runbook".to_string(),
                ServiceDefinitionV2Dot1LinkType::RUNBOOK,
                "https://my-runbook".to_string(),
            ),
            ServiceDefinitionV2Dot1Link::new(
                "Source Code".to_string(),
                ServiceDefinitionV2Dot1LinkType::REPO,
                "https://github.com/DataDog/schema".to_string(),
            )
            .provider("GitHub".to_string()),
            ServiceDefinitionV2Dot1Link::new(
                "Architecture".to_string(),
                ServiceDefinitionV2Dot1LinkType::DOC,
                "https://my-runbook".to_string(),
            )
            .provider("Gigoogle drivetHub".to_string()),
        ])
        .tags(vec!["my:tag".to_string(), "service:tag".to_string()])
        .team("my-team".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api.create_or_update_service_definitions(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create or update service definition using schema v2-2 returns "CREATED" response 
```
// Create or update service definition using schema v2-2 returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Contact;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Integrations;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Link;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Opsgenie;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2OpsgenieRegion;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Pagerduty;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Version;
use datadog_api_client::datadogV2::model::ServiceDefinitionsCreateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = ServiceDefinitionsCreateRequest::ServiceDefinitionV2Dot2(Box::new(
        ServiceDefinitionV2Dot2::new(
            "service-exampleservicedefinition".to_string(),
            ServiceDefinitionV2Dot2Version::V2_2,
        )
        .contacts(vec![ServiceDefinitionV2Dot2Contact::new(
            "contact@datadoghq.com".to_string(),
            "email".to_string(),
        )
        .name("Team Email".to_string())])
        .extensions(BTreeMap::from([(
            "myorgextension".to_string(),
            Value::from("extensionvalue"),
        )]))
        .integrations(
            ServiceDefinitionV2Dot2Integrations::new()
                .opsgenie(
                    ServiceDefinitionV2Dot2Opsgenie::new(
                        "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
                            .to_string(),
                    )
                    .region(ServiceDefinitionV2Dot2OpsgenieRegion::US),
                )
                .pagerduty(ServiceDefinitionV2Dot2Pagerduty::new().service_url(
                    "https://my-org.pagerduty.com/service-directory/PMyService".to_string(),
                )),
        )
        .links(vec![
            ServiceDefinitionV2Dot2Link::new(
                "Runbook".to_string(),
                "runbook".to_string(),
                "https://my-runbook".to_string(),
            ),
            ServiceDefinitionV2Dot2Link::new(
                "Source Code".to_string(),
                "repo".to_string(),
                "https://github.com/DataDog/schema".to_string(),
            )
            .provider("GitHub".to_string()),
            ServiceDefinitionV2Dot2Link::new(
                "Architecture".to_string(),
                "doc".to_string(),
                "https://my-runbook".to_string(),
            )
            .provider("Gigoogle drivetHub".to_string()),
        ])
        .tags(vec!["my:tag".to_string(), "service:tag".to_string()])
        .team("my-team".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api.create_or_update_service_definitions(body).await;
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

#####  Create or update service definition using schema v2 returns "CREATED" response 
```
/**
 * Create or update service definition using schema v2 returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiCreateOrUpdateServiceDefinitionsRequest = {
  body: {
    contacts: [
      {
        contact: "contact@datadoghq.com",
        name: "Team Email",
        type: "email",
      },
    ],
    ddService: "service-exampleservicedefinition",
    ddTeam: "my-team",
    docs: [
      {
        name: "Architecture",
        provider: "google drive",
        url: "https://gdrive/mydoc",
      },
    ],
    extensions: {
      myorgextension: "extensionvalue",
    },
    integrations: {
      opsgenie: {
        region: "US",
        serviceUrl:
          "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
      },
      pagerduty: "https://my-org.pagerduty.com/service-directory/PMyService",
    },
    links: [
      {
        name: "Runbook",
        type: "runbook",
        url: "https://my-runbook",
      },
    ],
    repos: [
      {
        name: "Source Code",
        provider: "GitHub",
        url: "https://github.com/DataDog/schema",
      },
    ],
    schemaVersion: "v2",
    tags: ["my:tag", "service:tag"],
    team: "my-team",
  },
};

apiInstance
  .createOrUpdateServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create or update service definition using schema v2-1 returns "CREATED" response 
```
/**
 * Create or update service definition using schema v2-1 returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiCreateOrUpdateServiceDefinitionsRequest = {
  body: {
    contacts: [
      {
        contact: "contact@datadoghq.com",
        name: "Team Email",
        type: "email",
      },
    ],
    ddService: "service-exampleservicedefinition",
    extensions: {
      myorgextension: "extensionvalue",
    },
    integrations: {
      opsgenie: {
        region: "US",
        serviceUrl:
          "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
      },
      pagerduty: {
        serviceUrl: "https://my-org.pagerduty.com/service-directory/PMyService",
      },
    },
    links: [
      {
        name: "Runbook",
        type: "runbook",
        url: "https://my-runbook",
      },
      {
        name: "Source Code",
        type: "repo",
        provider: "GitHub",
        url: "https://github.com/DataDog/schema",
      },
      {
        name: "Architecture",
        type: "doc",
        provider: "Gigoogle drivetHub",
        url: "https://my-runbook",
      },
    ],
    schemaVersion: "v2.1",
    tags: ["my:tag", "service:tag"],
    team: "my-team",
  },
};

apiInstance
  .createOrUpdateServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create or update service definition using schema v2-2 returns "CREATED" response 
```
/**
 * Create or update service definition using schema v2-2 returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiCreateOrUpdateServiceDefinitionsRequest = {
  body: {
    contacts: [
      {
        contact: "contact@datadoghq.com",
        name: "Team Email",
        type: "email",
      },
    ],
    ddService: "service-exampleservicedefinition",
    extensions: {
      myorgextension: "extensionvalue",
    },
    integrations: {
      opsgenie: {
        region: "US",
        serviceUrl:
          "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
      },
      pagerduty: {
        serviceUrl: "https://my-org.pagerduty.com/service-directory/PMyService",
      },
    },
    links: [
      {
        name: "Runbook",
        type: "runbook",
        url: "https://my-runbook",
      },
      {
        name: "Source Code",
        type: "repo",
        provider: "GitHub",
        url: "https://github.com/DataDog/schema",
      },
      {
        name: "Architecture",
        type: "doc",
        provider: "Gigoogle drivetHub",
        url: "https://my-runbook",
      },
    ],
    schemaVersion: "v2.2",
    tags: ["my:tag", "service:tag"],
    team: "my-team",
  },
};

apiInstance
  .createOrUpdateServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionCreateResponse) => {
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
## [Get a single service definition](https://docs.datadoghq.com/api/latest/service-definition/#get-a-single-service-definition)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-definition/#get-a-single-service-definition-v2)


GET https://api.ap1.datadoghq.com/api/v2/services/definitions/{service_name}https://api.ap2.datadoghq.com/api/v2/services/definitions/{service_name}https://api.datadoghq.eu/api/v2/services/definitions/{service_name}https://api.ddog-gov.com/api/v2/services/definitions/{service_name}https://api.datadoghq.com/api/v2/services/definitions/{service_name}https://api.us3.datadoghq.com/api/v2/services/definitions/{service_name}https://api.us5.datadoghq.com/api/v2/services/definitions/{service_name}
### Overview
Get a single service definition from the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_read` permission.
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
service_name [_required_]
string
The name of the service.
#### Query Strings
Name
Type
Description
schema_version
enum
The schema version desired in the response.  
Allowed enum values: `v1, v2, v2.1, v2.2`
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-definition/#GetServiceDefinition-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-definition/#GetServiceDefinition-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-definition/#GetServiceDefinition-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-definition/#GetServiceDefinition-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/service-definition/#GetServiceDefinition-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-definition/#GetServiceDefinition-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


Get service definition response.
Field
Type
Description
data
object
Service definition data.
attributes
object
Service definition attributes.
meta
object
Metadata about a service definition.
github-html-url
string
GitHub HTML URL.
ingested-schema-version
string
Ingestion schema version.
ingestion-source
string
Ingestion source of the service definition.
last-modified-time
string
Last modified time of the service definition.
origin
string
User defined origin of the service definition.
origin-detail
string
User defined origin's detail of the service definition.
warnings
[object]
A list of schema validation warnings.
instance-location
string
The warning instance location.
keyword-location
string
The warning keyword location.
message
string
The warning message.
schema
<oneOf>
Service definition schema.
Option 1
object
**DEPRECATED** : Deprecated - Service definition V1 for providing additional service metadata and integrations.
contact
object
Contact information about the service.
email
string
Service owner’s email.
slack
string
Service owner’s Slack channel.
extensions
object
Extensions to V1 schema.
external-resources
[object]
A list of external links related to the services.
name [_required_]
string
Link name.
type [_required_]
enum
Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`
url [_required_]
string
Link URL.
info [_required_]
object
Basic information about a service.
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
display-name
string
A friendly name of the service.
service-tier
string
Service tier.
integrations
object
Third party integrations that Datadog supports.
pagerduty
string
PagerDuty service URL for the service.
org
object
Org related information about the service.
application
string
App feature this service supports.
team
string
Team that owns the service.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v1`
default: `v1`
tags
[string]
A set of custom tags.
Option 2
object
Service definition V2 for providing service metadata and integrations.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
dd-team
string
Experimental feature. A Team handle that matches a Team in the Datadog Teams product.
docs
[object]
A list of documentation related to the services.
name [_required_]
string
Document name.
provider
string
Document provider.
url [_required_]
string
Document URL.
extensions
object
Extensions to V2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
string
PagerDuty service URL for the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
type [_required_]
enum
Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`
url [_required_]
string
Link URL.
repos
[object]
A list of code repositories related to the services.
name [_required_]
string
Repository name.
provider
string
Repository provider.
url [_required_]
string
Repository URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2`
default: `v2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service.
Option 3
object
Service definition v2.1 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
contacts
[ <oneOf>]
A list of contacts related to the services.
Option 1
object
Service owner's email.
contact [_required_]
string
Contact value.
name
string
Contact email.
type [_required_]
enum
Contact type. Allowed enum values: `email`
Option 2
object
Service owner's Slack channel.
contact [_required_]
string
Slack Channel.
name
string
Contact Slack.
type [_required_]
enum
Contact type. Allowed enum values: `slack`
Option 3
object
Service owner's Microsoft Teams.
contact [_required_]
string
Contact value.
name
string
Contact Microsoft Teams.
type [_required_]
enum
Contact type. Allowed enum values: `microsoft-teams`
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.1 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
enum
Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.1`
default: `v2.1`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
Option 4
object
Service definition v2.2 for providing service metadata and integrations.
application
string
Identifier for a group of related services serving a product feature, which the service is a part of.
ci-pipeline-fingerprints
[string]
A set of CI fingerprints.
contacts
[object]
A list of contacts related to the services.
contact [_required_]
string
Contact value.
name
string
Contact Name.
type [_required_]
string
Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.
dd-service [_required_]
string
Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
description
string
A short description of the service.
extensions
object
Extensions to v2.2 schema.
integrations
object
Third party integrations that Datadog supports.
opsgenie
object
Opsgenie integration for the service.
region
enum
Opsgenie instance region. Allowed enum values: `US,EU`
service-url [_required_]
string
Opsgenie service url.
pagerduty
object
PagerDuty integration for the service.
service-url
string
PagerDuty service url.
languages
[string]
The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`.
lifecycle
string
The current life cycle phase of the service.
links
[object]
A list of links related to the services.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.
url [_required_]
string
Link URL.
schema-version [_required_]
enum
Schema version being used. Allowed enum values: `v2.2`
default: `v2.2`
tags
[string]
A set of custom tags.
team
string
Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.
tier
string
Importance of the service.
type
string
The type of service.
id
string
Service definition id.
type
string
Service definition type.
```
{
  "data": {
    "attributes": {
      "meta": {
        "github-html-url": "string",
        "ingested-schema-version": "string",
        "ingestion-source": "string",
        "last-modified-time": "string",
        "origin": "string",
        "origin-detail": "string",
        "warnings": [
          {
            "instance-location": "string",
            "keyword-location": "string",
            "message": "string"
          }
        ]
      },
      "schema": {
        "contact": {
          "email": "contact@datadoghq.com",
          "slack": "https://yourcompany.slack.com/archives/channel123"
        },
        "extensions": {
          "myorg/extension": "extensionValue"
        },
        "external-resources": [
          {
            "name": "Runbook",
            "type": "runbook",
            "url": "https://my-runbook"
          }
        ],
        "info": {
          "dd-service": "myservice",
          "description": "A shopping cart service",
          "display-name": "My Service",
          "service-tier": "Tier 1"
        },
        "integrations": {
          "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
        },
        "org": {
          "application": "E-Commerce",
          "team": "my-team"
        },
        "schema-version": "v1",
        "tags": [
          "my:tag",
          "service:tag"
        ]
      }
    },
    "id": "string",
    "type": "string"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=typescript)


#####  Get a single service definition
Copy
```
                  # Path parameters  
export service_name="my-service"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions/${service_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a single service definition
```
"""
Get a single service definition returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_schema_versions import ServiceDefinitionSchemaVersions

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.get_service_definition(
        service_name="service-definition-test",
        schema_version=ServiceDefinitionSchemaVersions.V2_1,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a single service definition
```
# Get a single service definition returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new
opts = {
  schema_version: ServiceDefinitionSchemaVersions::V2_1,
}
p api_instance.get_service_definition("service-definition-test", opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a single service definition
```
// Get a single service definition returns "OK" response

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
	api := datadogV2.NewServiceDefinitionApi(apiClient)
	resp, r, err := api.GetServiceDefinition(ctx, "service-definition-test", *datadogV2.NewGetServiceDefinitionOptionalParameters().WithSchemaVersion(datadogV2.SERVICEDEFINITIONSCHEMAVERSIONS_V2_1))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.GetServiceDefinition`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.GetServiceDefinition`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a single service definition
```
// Get a single service definition returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.api.ServiceDefinitionApi.GetServiceDefinitionOptionalParameters;
import com.datadog.api.client.v2.model.ServiceDefinitionGetResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionSchemaVersions;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    try {
      ServiceDefinitionGetResponse result =
          apiInstance.getServiceDefinition(
              "service-definition-test",
              new GetServiceDefinitionOptionalParameters()
                  .schemaVersion(ServiceDefinitionSchemaVersions.V2_1));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDefinitionApi#getServiceDefinition");
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

#####  Get a single service definition
```
// Get a single service definition returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::GetServiceDefinitionOptionalParams;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionSchemaVersions;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api
        .get_service_definition(
            "service-definition-test".to_string(),
            GetServiceDefinitionOptionalParams::default()
                .schema_version(ServiceDefinitionSchemaVersions::V2_1),
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

#####  Get a single service definition
```
/**
 * Get a single service definition returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiGetServiceDefinitionRequest = {
  serviceName: "service-definition-test",
  schemaVersion: "v2.1",
};

apiInstance
  .getServiceDefinition(params)
  .then((data: v2.ServiceDefinitionGetResponse) => {
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
## [Delete a single service definition](https://docs.datadoghq.com/api/latest/service-definition/#delete-a-single-service-definition)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-definition/#delete-a-single-service-definition-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/services/definitions/{service_name}https://api.ap2.datadoghq.com/api/v2/services/definitions/{service_name}https://api.datadoghq.eu/api/v2/services/definitions/{service_name}https://api.ddog-gov.com/api/v2/services/definitions/{service_name}https://api.datadoghq.com/api/v2/services/definitions/{service_name}https://api.us3.datadoghq.com/api/v2/services/definitions/{service_name}https://api.us5.datadoghq.com/api/v2/services/definitions/{service_name}
### Overview
Delete a single service definition in the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_write` permission.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
service_name [_required_]
string
The name of the service.
### Response
  * [204](https://docs.datadoghq.com/api/latest/service-definition/#DeleteServiceDefinition-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-definition/#DeleteServiceDefinition-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-definition/#DeleteServiceDefinition-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-definition/#DeleteServiceDefinition-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-definition/#DeleteServiceDefinition-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-definition/)
  * [Example](https://docs.datadoghq.com/api/latest/service-definition/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-definition/?code-lang=typescript)


#####  Delete a single service definition
Copy
```
                  # Path parameters  
export service_name="my-service"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions/${service_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a single service definition
```
"""
Delete a single service definition returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    api_instance.delete_service_definition(
        service_name="service-definition-test",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a single service definition
```
# Delete a single service definition returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new
api_instance.delete_service_definition("service-definition-test")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a single service definition
```
// Delete a single service definition returns "OK" response

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
	api := datadogV2.NewServiceDefinitionApi(apiClient)
	r, err := api.DeleteServiceDefinition(ctx, "service-definition-test")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.DeleteServiceDefinition`: %v\n", err)
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

#####  Delete a single service definition
```
// Delete a single service definition returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    try {
      apiInstance.deleteServiceDefinition("service-definition-test");
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDefinitionApi#deleteServiceDefinition");
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

#####  Delete a single service definition
```
// Delete a single service definition returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api
        .delete_service_definition("service-definition-test".to_string())
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

#####  Delete a single service definition
```
/**
 * Delete a single service definition returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiDeleteServiceDefinitionRequest = {
  serviceName: "service-definition-test",
};

apiInstance
  .deleteServiceDefinition(params)
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=5591b8fb-a754-4282-907b-bfdb45fbf4f5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=5e6c5e0d-4ca5-4dda-be2a-c66a8514c958&pt=Service%20Definition&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-definition%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=5591b8fb-a754-4282-907b-bfdb45fbf4f5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=5e6c5e0d-4ca5-4dda-be2a-c66a8514c958&pt=Service%20Definition&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-definition%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=edafb5bb-09f8-4519-a38c-812a6be0b879&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Service%20Definition&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-definition%2F&r=&lt=15024&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=418360)
