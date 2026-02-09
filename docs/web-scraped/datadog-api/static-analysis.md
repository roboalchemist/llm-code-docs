# Source: https://docs.datadoghq.com/api/latest/static-analysis

# Static Analysis
API for static analysis
## [POST request to resolve vulnerable symbols](https://docs.datadoghq.com/api/latest/static-analysis/#post-request-to-resolve-vulnerable-symbols)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/static-analysis/#post-request-to-resolve-vulnerable-symbols-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbolshttps://api.ap2.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbolshttps://api.datadoghq.eu/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbolshttps://api.ddog-gov.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbolshttps://api.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbolshttps://api.us3.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbolshttps://api.us5.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols
### Overview
OAuth apps require the `code_analysis_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#static-analysis) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/static-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/static-analysis/)


Field
Type
Description
data
object
attributes
object
purls
[string]
id
string
type [_required_]
enum
default: `resolve-vulnerable-symbols-request`
```
{
  "data": {
    "attributes": {
      "purls": []
    },
    "id": "string",
    "type": "resolve-vulnerable-symbols-request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/static-analysis/#CreateSCAResolveVulnerableSymbols-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/static-analysis/#CreateSCAResolveVulnerableSymbols-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/static-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/static-analysis/)


Field
Type
Description
data
object
attributes
object
results
[object]
purl
string
vulnerable_symbols
[object]
advisory_id
string
symbols
[object]
name
string
type
string
value
string
id
string
type [_required_]
enum
default: `resolve-vulnerable-symbols-response`
```
{
  "data": {
    "attributes": {
      "results": [
        {
          "purl": "string",
          "vulnerable_symbols": [
            {
              "advisory_id": "string",
              "symbols": [
                {
                  "name": "string",
                  "type": "string",
                  "value": "string"
                }
              ]
            }
          ]
        }
      ]
    },
    "id": "string",
    "type": "resolve-vulnerable-symbols-response"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/static-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/static-analysis/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=typescript)


#####  POST request to resolve vulnerable symbols
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "resolve-vulnerable-symbols-request"
  }
}
EOF  

                
```

#####  POST request to resolve vulnerable symbols
```
"""
POST request to resolve vulnerable symbols returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request import ResolveVulnerableSymbolsRequest
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data import ResolveVulnerableSymbolsRequestData
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_attributes import (
    ResolveVulnerableSymbolsRequestDataAttributes,
)
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_type import (
    ResolveVulnerableSymbolsRequestDataType,
)

body = ResolveVulnerableSymbolsRequest(
    data=ResolveVulnerableSymbolsRequestData(
        attributes=ResolveVulnerableSymbolsRequestDataAttributes(
            purls=[],
        ),
        type=ResolveVulnerableSymbolsRequestDataType.RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sca_resolve_vulnerable_symbols"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_sca_resolve_vulnerable_symbols(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  POST request to resolve vulnerable symbols
```
# POST request to resolve vulnerable symbols returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_sca_resolve_vulnerable_symbols".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::ResolveVulnerableSymbolsRequest.new({
  data: DatadogAPIClient::V2::ResolveVulnerableSymbolsRequestData.new({
    attributes: DatadogAPIClient::V2::ResolveVulnerableSymbolsRequestDataAttributes.new({
      purls: [],
    }),
    type: DatadogAPIClient::V2::ResolveVulnerableSymbolsRequestDataType::RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
  }),
})
p api_instance.create_sca_resolve_vulnerable_symbols(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  POST request to resolve vulnerable symbols
```
// POST request to resolve vulnerable symbols returns "OK" response

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
	body := datadogV2.ResolveVulnerableSymbolsRequest{
		Data: &datadogV2.ResolveVulnerableSymbolsRequestData{
			Attributes: &datadogV2.ResolveVulnerableSymbolsRequestDataAttributes{
				Purls: []string{},
			},
			Type: datadogV2.RESOLVEVULNERABLESYMBOLSREQUESTDATATYPE_RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateSCAResolveVulnerableSymbols", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.CreateSCAResolveVulnerableSymbols(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.CreateSCAResolveVulnerableSymbols`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.CreateSCAResolveVulnerableSymbols`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  POST request to resolve vulnerable symbols
```
// POST request to resolve vulnerable symbols returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequest;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequestData;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequestDataAttributes;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequestDataType;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createSCAResolveVulnerableSymbols", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    ResolveVulnerableSymbolsRequest body =
        new ResolveVulnerableSymbolsRequest()
            .data(
                new ResolveVulnerableSymbolsRequestData()
                    .attributes(new ResolveVulnerableSymbolsRequestDataAttributes())
                    .type(
                        ResolveVulnerableSymbolsRequestDataType
                            .RESOLVE_VULNERABLE_SYMBOLS_REQUEST));

    try {
      ResolveVulnerableSymbolsResponse result = apiInstance.createSCAResolveVulnerableSymbols(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling StaticAnalysisApi#createSCAResolveVulnerableSymbols");
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

#####  POST request to resolve vulnerable symbols
```
// POST request to resolve vulnerable symbols returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequest;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequestData;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequestDataAttributes;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequestDataType;

#[tokio::main]
async fn main() {
    let body = ResolveVulnerableSymbolsRequest::new().data(
        ResolveVulnerableSymbolsRequestData::new(
            ResolveVulnerableSymbolsRequestDataType::RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
        )
        .attributes(ResolveVulnerableSymbolsRequestDataAttributes::new().purls(vec![])),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateSCAResolveVulnerableSymbols", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api.create_sca_resolve_vulnerable_symbols(body).await;
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

#####  POST request to resolve vulnerable symbols
```
/**
 * POST request to resolve vulnerable symbols returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createSCAResolveVulnerableSymbols"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiCreateSCAResolveVulnerableSymbolsRequest = {
  body: {
    data: {
      attributes: {
        purls: [],
      },
      type: "resolve-vulnerable-symbols-request",
    },
  },
};

apiInstance
  .createSCAResolveVulnerableSymbols(params)
  .then((data: v2.ResolveVulnerableSymbolsResponse) => {
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
## [Post dependencies for analysis](https://docs.datadoghq.com/api/latest/static-analysis/#post-dependencies-for-analysis)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/static-analysis/#post-dependencies-for-analysis-v2)


**Note** : This endpoint may be subject to changes.
POST https://api.ap1.datadoghq.com/api/v2/static-analysis-sca/dependencieshttps://api.ap2.datadoghq.com/api/v2/static-analysis-sca/dependencieshttps://api.datadoghq.eu/api/v2/static-analysis-sca/dependencieshttps://api.ddog-gov.com/api/v2/static-analysis-sca/dependencieshttps://api.datadoghq.com/api/v2/static-analysis-sca/dependencieshttps://api.us3.datadoghq.com/api/v2/static-analysis-sca/dependencieshttps://api.us5.datadoghq.com/api/v2/static-analysis-sca/dependencies
### Overview
OAuth apps require the `code_analysis_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#static-analysis) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/static-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/static-analysis/)


Field
Type
Description
data
object
attributes
object
commit
object
author_date
string
author_email
string
author_name
string
branch
string
committer_email
string
committer_name
string
sha
string
dependencies
[object]
exclusions
[string]
group
string
is_dev
boolean
is_direct
boolean
language
string
locations
[object]
block
object
end
object
col
int32
line
int32
file_name
string
start
object
col
int32
line
int32
name
object
end
object
col
int32
line
int32
file_name
string
start
object
col
int32
line
int32
namespace
object
end
object
col
int32
line
int32
file_name
string
start
object
col
int32
line
int32
version
object
end
object
col
int32
line
int32
file_name
string
start
object
col
int32
line
int32
name
string
package_manager
string
purl
string
reachable_symbol_properties
[object]
name
string
value
string
version
string
env
string
files
[object]
name
string
purl
string
relations
[object]
depends_on
[string]
ref
string
repository
object
url
string
service
string
tags
object
<any-key>
string
vulnerabilities
[object]
affects
[object]
ref
string
bom_ref
string
id
string
id
string
type [_required_]
enum
default: `scarequests`
```
{
  "data": {
    "attributes": {
      "commit": {
        "author_date": "string",
        "author_email": "string",
        "author_name": "string",
        "branch": "string",
        "committer_email": "string",
        "committer_name": "string",
        "sha": "string"
      },
      "dependencies": [
        {
          "exclusions": [],
          "group": "string",
          "is_dev": false,
          "is_direct": false,
          "language": "string",
          "locations": [
            {
              "block": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              },
              "name": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              },
              "namespace": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              },
              "version": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              }
            }
          ],
          "name": "string",
          "package_manager": "string",
          "purl": "string",
          "reachable_symbol_properties": [
            {
              "name": "string",
              "value": "string"
            }
          ],
          "version": "string"
        }
      ],
      "env": "string",
      "files": [
        {
          "name": "string",
          "purl": "string"
        }
      ],
      "relations": [
        {
          "depends_on": [],
          "ref": "string"
        }
      ],
      "repository": {
        "url": "string"
      },
      "service": "string",
      "tags": {
        "<any-key>": "string"
      },
      "vulnerabilities": [
        {
          "affects": [
            {
              "ref": "string"
            }
          ],
          "bom_ref": "string",
          "id": "string"
        }
      ]
    },
    "id": "string",
    "type": "scarequests"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/static-analysis/#CreateSCAResult-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/static-analysis/#CreateSCAResult-429-v2)


OK
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/static-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/static-analysis/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/static-analysis/?code-lang=typescript)


#####  Post dependencies for analysis
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis-sca/dependencies" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "scarequests"
  }
}
EOF  

                
```

#####  Post dependencies for analysis
```
"""
Post dependencies for analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.sca_request import ScaRequest
from datadog_api_client.v2.model.sca_request_data import ScaRequestData
from datadog_api_client.v2.model.sca_request_data_attributes import ScaRequestDataAttributes
from datadog_api_client.v2.model.sca_request_data_attributes_commit import ScaRequestDataAttributesCommit
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items import (
    ScaRequestDataAttributesDependenciesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items import (
    ScaRequestDataAttributesDependenciesItemsLocationsItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_file_position import (
    ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_position import (
    ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_reachable_symbol_properties_items import (
    ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_files_items import ScaRequestDataAttributesFilesItems
from datadog_api_client.v2.model.sca_request_data_attributes_relations_items import (
    ScaRequestDataAttributesRelationsItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_repository import ScaRequestDataAttributesRepository
from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items import (
    ScaRequestDataAttributesVulnerabilitiesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items_affects_items import (
    ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems,
)
from datadog_api_client.v2.model.sca_request_data_type import ScaRequestDataType

body = ScaRequest(
    data=ScaRequestData(
        attributes=ScaRequestDataAttributes(
            commit=ScaRequestDataAttributesCommit(),
            dependencies=[
                ScaRequestDataAttributesDependenciesItems(
                    exclusions=[],
                    locations=[
                        ScaRequestDataAttributesDependenciesItemsLocationsItems(
                            block=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            name=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            namespace=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            version=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                        ),
                    ],
                    reachable_symbol_properties=[
                        ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems(),
                    ],
                ),
            ],
            files=[
                ScaRequestDataAttributesFilesItems(),
            ],
            relations=[
                ScaRequestDataAttributesRelationsItems(
                    depends_on=[],
                ),
            ],
            repository=ScaRequestDataAttributesRepository(),
            vulnerabilities=[
                ScaRequestDataAttributesVulnerabilitiesItems(
                    affects=[
                        ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems(),
                    ],
                ),
            ],
        ),
        type=ScaRequestDataType.SCAREQUESTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sca_result"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.create_sca_result(body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Post dependencies for analysis
```
# Post dependencies for analysis returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_sca_result".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::ScaRequest.new({
  data: DatadogAPIClient::V2::ScaRequestData.new({
    attributes: DatadogAPIClient::V2::ScaRequestDataAttributes.new({
      commit: DatadogAPIClient::V2::ScaRequestDataAttributesCommit.new({}),
      dependencies: [
        DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItems.new({
          exclusions: [],
          locations: [
            DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItems.new({
              block: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
              name: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
              namespace: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
              version: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
            }),
          ],
          reachable_symbol_properties: [
            DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems.new({}),
          ],
        }),
      ],
      files: [
        DatadogAPIClient::V2::ScaRequestDataAttributesFilesItems.new({}),
      ],
      relations: [
        DatadogAPIClient::V2::ScaRequestDataAttributesRelationsItems.new({
          depends_on: [],
        }),
      ],
      repository: DatadogAPIClient::V2::ScaRequestDataAttributesRepository.new({}),
      vulnerabilities: [
        DatadogAPIClient::V2::ScaRequestDataAttributesVulnerabilitiesItems.new({
          affects: [
            DatadogAPIClient::V2::ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems.new({}),
          ],
        }),
      ],
    }),
    type: DatadogAPIClient::V2::ScaRequestDataType::SCAREQUESTS,
  }),
})
p api_instance.create_sca_result(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Post dependencies for analysis
```
// Post dependencies for analysis returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.ScaRequest{
		Data: &datadogV2.ScaRequestData{
			Attributes: &datadogV2.ScaRequestDataAttributes{
				Commit: &datadogV2.ScaRequestDataAttributesCommit{},
				Dependencies: []datadogV2.ScaRequestDataAttributesDependenciesItems{
					{
						Exclusions: []string{},
						Locations: []datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItems{
							{
								Block: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
								Name: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
								Namespace: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
								Version: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
							},
						},
						ReachableSymbolProperties: []datadogV2.ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems{
							{},
						},
					},
				},
				Files: []datadogV2.ScaRequestDataAttributesFilesItems{
					{},
				},
				Relations: []datadogV2.ScaRequestDataAttributesRelationsItems{
					{
						DependsOn: []string{},
					},
				},
				Repository: &datadogV2.ScaRequestDataAttributesRepository{},
				Vulnerabilities: []datadogV2.ScaRequestDataAttributesVulnerabilitiesItems{
					{
						Affects: []datadogV2.ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems{
							{},
						},
					},
				},
			},
			Type: datadogV2.SCAREQUESTDATATYPE_SCAREQUESTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateSCAResult", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	r, err := api.CreateSCAResult(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.CreateSCAResult`: %v\n", err)
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

#####  Post dependencies for analysis
```
// Post dependencies for analysis returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.ScaRequest;
import com.datadog.api.client.v2.model.ScaRequestData;
import com.datadog.api.client.v2.model.ScaRequestDataAttributes;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesCommit;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsLocationsItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesFilesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesRelationsItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesRepository;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesVulnerabilitiesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems;
import com.datadog.api.client.v2.model.ScaRequestDataType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createSCAResult", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    ScaRequest body =
        new ScaRequest()
            .data(
                new ScaRequestData()
                    .attributes(
                        new ScaRequestDataAttributes()
                            .commit(new ScaRequestDataAttributesCommit())
                            .dependencies(
                                Collections.singletonList(
                                    new ScaRequestDataAttributesDependenciesItems()
                                        .locations(
                                            Collections.singletonList(
                                                new ScaRequestDataAttributesDependenciesItemsLocationsItems()
                                                    .block(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))
                                                    .name(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))
                                                    .namespace(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))
                                                    .version(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))))
                                        .reachableSymbolProperties(
                                            Collections.singletonList(
                                                new ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems()))))
                            .files(
                                Collections.singletonList(new ScaRequestDataAttributesFilesItems()))
                            .relations(
                                Collections.singletonList(
                                    new ScaRequestDataAttributesRelationsItems()))
                            .repository(new ScaRequestDataAttributesRepository())
                            .vulnerabilities(
                                Collections.singletonList(
                                    new ScaRequestDataAttributesVulnerabilitiesItems()
                                        .affects(
                                            Collections.singletonList(
                                                new ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems())))))
                    .type(ScaRequestDataType.SCAREQUESTS));

    try {
      apiInstance.createSCAResult(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#createSCAResult");
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

#####  Post dependencies for analysis
```
// Post dependencies for analysis returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::ScaRequest;
use datadog_api_client::datadogV2::model::ScaRequestData;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributes;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesCommit;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsLocationsItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesFilesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesRelationsItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesRepository;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesVulnerabilitiesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems;
use datadog_api_client::datadogV2::model::ScaRequestDataType;

#[tokio::main]
async fn main() {
    let body =
        ScaRequest
        ::new().data(
            ScaRequestData::new(
                ScaRequestDataType::SCAREQUESTS,
            ).attributes(
                ScaRequestDataAttributes::new()
                    .commit(ScaRequestDataAttributesCommit::new())
                    .dependencies(
                        vec![
                            ScaRequestDataAttributesDependenciesItems::new()
                                .exclusions(vec![])
                                .locations(
                                    vec![
                                        ScaRequestDataAttributesDependenciesItemsLocationsItems::new()
                                            .block(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                            .name(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                            .namespace(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                            .version(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                    ],
                                )
                                .reachable_symbol_properties(
                                    vec![
                                        ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems::new()
                                    ],
                                )
                        ],
                    )
                    .files(vec![ScaRequestDataAttributesFilesItems::new()])
                    .relations(vec![ScaRequestDataAttributesRelationsItems::new().depends_on(vec![])])
                    .repository(ScaRequestDataAttributesRepository::new())
                    .vulnerabilities(
                        vec![
                            ScaRequestDataAttributesVulnerabilitiesItems
                            ::new().affects(vec![ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems::new()])
                        ],
                    ),
            ),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateSCAResult", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api.create_sca_result(body).await;
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

#####  Post dependencies for analysis
```
/**
 * Post dependencies for analysis returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createSCAResult"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiCreateSCAResultRequest = {
  body: {
    data: {
      attributes: {
        commit: {},
        dependencies: [
          {
            exclusions: [],
            locations: [
              {
                block: {
                  end: {},
                  start: {},
                },
                name: {
                  end: {},
                  start: {},
                },
                namespace: {
                  end: {},
                  start: {},
                },
                version: {
                  end: {},
                  start: {},
                },
              },
            ],
            reachableSymbolProperties: [{}],
          },
        ],
        files: [{}],
        relations: [
          {
            dependsOn: [],
          },
        ],
        repository: {},
        vulnerabilities: [
          {
            affects: [{}],
          },
        ],
      },
      type: "scarequests",
    },
  },
};

apiInstance
  .createSCAResult(params)
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=cf65a979-d183-4b7d-a723-f756b26cee53&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=28c4c534-4020-4337-b0f5-85e67c351d17&pt=Static%20Analysis&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fstatic-analysis%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=cf65a979-d183-4b7d-a723-f756b26cee53&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=28c4c534-4020-4337-b0f5-85e67c351d17&pt=Static%20Analysis&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fstatic-analysis%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=e154694d-f455-4d0b-8bc6-b6180e9cdeac&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Static%20Analysis&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fstatic-analysis%2F&r=&lt=10031&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=760814)
