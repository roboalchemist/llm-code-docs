# Source: https://docs.datadoghq.com/api/latest/datasets

# Datasets
Data Access Controls in Datadog is a feature that allows administrators and access managers to regulate access to sensitive data. By defining Restricted Datasets, you can ensure that only specific teams or roles can view certain types of telemetry (for example, logs, traces, metrics, and RUM data).
## [Create a dataset](https://docs.datadoghq.com/api/latest/datasets/#create-a-dataset)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/datasets/#create-a-dataset-v2)


**Note: Data Access is in preview. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
POST https://api.ap1.datadoghq.com/api/v2/datasetshttps://api.ap2.datadoghq.com/api/v2/datasetshttps://api.datadoghq.eu/api/v2/datasetshttps://api.ddog-gov.com/api/v2/datasetshttps://api.datadoghq.com/api/v2/datasetshttps://api.us3.datadoghq.com/api/v2/datasetshttps://api.us5.datadoghq.com/api/v2/datasets
### Overview
Create a dataset with the configurations in the request. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.
### Request
#### Body Data (required)
Dataset payload
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


Field
Type
Description
data [_required_]
object
**Datasets Object Constraints**
  * **Tag limit per dataset** :
    * Each restricted dataset supports a maximum of 10 key:value pairs per product.
  * **Tag key rules per telemetry type** :
    * Only one tag key or attribute may be used to define access within a single telemetry type.
    * The same or different tag key may be used across different telemetry types.
  * **Tag value uniqueness** :
    * Tag values must be unique within a single dataset.
    * A tag value used in one dataset cannot be reused in another dataset of the same telemetry type.


attributes [_required_]
object
Dataset metadata and configurations.
name [_required_]
string
Name of the dataset.
principals [_required_]
[string]
List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.
product_filters [_required_]
[object]
List of product-specific filters.
filters [_required_]
[string]
Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type.
product [_required_]
string
Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.
type [_required_]
enum
Resource type, always set to `dataset`. Allowed enum values: `dataset`
default: `dataset`
```
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/datasets/#CreateDataset-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/datasets/#CreateDataset-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/datasets/#CreateDataset-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/datasets/#CreateDataset-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/datasets/#CreateDataset-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


Response containing a single dataset object.
Field
Type
Description
data
object
**Datasets Object Constraints**
  * **Tag Limit per Dataset** :
    * Each restricted dataset supports a maximum of 10 key:value pairs per product.
  * **Tag Key Rules per Telemetry Type** :
    * Only one tag key or attribute may be used to define access within a single telemetry type.
    * The same or different tag key may be used across different telemetry types.
  * **Tag Value Uniqueness** :
    * Tag values must be unique within a single dataset.
    * A tag value used in one dataset cannot be reused in another dataset of the same telemetry type.


attributes
object
Dataset metadata and configuration(s).
created_at
date-time
Timestamp when the dataset was created.
created_by
uuid
Unique ID of the user who created the dataset.
name
string
Name of the dataset.
principals
[string]
List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.
product_filters
[object]
List of product-specific filters.
filters [_required_]
[string]
Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type.
product [_required_]
string
Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.
id
string
Unique identifier for the dataset.
type
enum
Resource type, always set to `dataset`. Allowed enum values: `dataset`
default: `dataset`
```
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "name": "Security Audit Dataset",
      "principals": [
        "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "logs"
        }
      ]
    },
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "type": "dataset"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/datasets/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/datasets/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/datasets/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/datasets/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/datasets/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/datasets/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/datasets/?code-lang=typescript)


#####  Create a dataset returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
EOF  

                        
```

#####  Create a dataset returns "OK" response
```
// Create a dataset returns "OK" response

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
	body := datadogV2.DatasetCreateRequest{
		Data: datadogV2.DatasetRequest{
			Attributes: datadogV2.DatasetAttributesRequest{
				Name: "Security Audit Dataset",
				Principals: []string{
					"role:94172442-be03-11e9-a77a-3b7612558ac1",
				},
				ProductFilters: []datadogV2.FiltersPerProduct{
					{
						Filters: []string{
							"@application.id:ABCD",
						},
						Product: "metrics",
					},
				},
			},
			Type: datadogV2.DATASETTYPE_DATASET,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateDataset", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDatasetsApi(apiClient)
	resp, r, err := api.CreateDataset(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.CreateDataset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.CreateDataset`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a dataset returns "OK" response
```
// Create a dataset returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetAttributesRequest;
import com.datadog.api.client.v2.model.DatasetCreateRequest;
import com.datadog.api.client.v2.model.DatasetRequest;
import com.datadog.api.client.v2.model.DatasetResponseSingle;
import com.datadog.api.client.v2.model.DatasetType;
import com.datadog.api.client.v2.model.FiltersPerProduct;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    DatasetCreateRequest body =
        new DatasetCreateRequest()
            .data(
                new DatasetRequest()
                    .attributes(
                        new DatasetAttributesRequest()
                            .name("Security Audit Dataset")
                            .principals(
                                Collections.singletonList(
                                    "role:94172442-be03-11e9-a77a-3b7612558ac1"))
                            .productFilters(
                                Collections.singletonList(
                                    new FiltersPerProduct()
                                        .filters(Collections.singletonList("@application.id:ABCD"))
                                        .product("metrics"))))
                    .type(DatasetType.DATASET));

    try {
      DatasetResponseSingle result = apiInstance.createDataset(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#createDataset");
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

#####  Create a dataset returns "OK" response
```
"""
Create a dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi
from datadog_api_client.v2.model.dataset_attributes_request import DatasetAttributesRequest
from datadog_api_client.v2.model.dataset_create_request import DatasetCreateRequest
from datadog_api_client.v2.model.dataset_request import DatasetRequest
from datadog_api_client.v2.model.dataset_type import DatasetType
from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

body = DatasetCreateRequest(
    data=DatasetRequest(
        attributes=DatasetAttributesRequest(
            name="Security Audit Dataset",
            principals=[
                "role:94172442-be03-11e9-a77a-3b7612558ac1",
            ],
            product_filters=[
                FiltersPerProduct(
                    filters=[
                        "@application.id:ABCD",
                    ],
                    product="metrics",
                ),
            ],
        ),
        type=DatasetType.DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.create_dataset(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a dataset returns "OK" response
```
# Create a dataset returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

body = DatadogAPIClient::V2::DatasetCreateRequest.new({
  data: DatadogAPIClient::V2::DatasetRequest.new({
    attributes: DatadogAPIClient::V2::DatasetAttributesRequest.new({
      name: "Security Audit Dataset",
      principals: [
        "role:94172442-be03-11e9-a77a-3b7612558ac1",
      ],
      product_filters: [
        DatadogAPIClient::V2::FiltersPerProduct.new({
          filters: [
            "@application.id:ABCD",
          ],
          product: "metrics",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::DatasetType::DATASET,
  }),
})
p api_instance.create_dataset(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a dataset returns "OK" response
```
// Create a dataset returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;
use datadog_api_client::datadogV2::model::DatasetAttributesRequest;
use datadog_api_client::datadogV2::model::DatasetCreateRequest;
use datadog_api_client::datadogV2::model::DatasetRequest;
use datadog_api_client::datadogV2::model::DatasetType;
use datadog_api_client::datadogV2::model::FiltersPerProduct;

#[tokio::main]
async fn main() {
    let body = DatasetCreateRequest::new(DatasetRequest::new(
        DatasetAttributesRequest::new(
            "Security Audit Dataset".to_string(),
            vec!["role:94172442-be03-11e9-a77a-3b7612558ac1".to_string()],
            vec![FiltersPerProduct::new(
                vec!["@application.id:ABCD".to_string()],
                "metrics".to_string(),
            )],
        ),
        DatasetType::DATASET,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.create_dataset(body).await;
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

#####  Create a dataset returns "OK" response
```
/**
 * Create a dataset returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

const params: v2.DatasetsApiCreateDatasetRequest = {
  body: {
    data: {
      attributes: {
        name: "Security Audit Dataset",
        principals: ["role:94172442-be03-11e9-a77a-3b7612558ac1"],
        productFilters: [
          {
            filters: ["@application.id:ABCD"],
            product: "metrics",
          },
        ],
      },
      type: "dataset",
    },
  },
};

apiInstance
  .createDataset(params)
  .then((data: v2.DatasetResponseSingle) => {
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
## [Get a single dataset by ID](https://docs.datadoghq.com/api/latest/datasets/#get-a-single-dataset-by-id)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/datasets/#get-a-single-dataset-by-id-v2)


**Note: Data Access is in preview. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
GET https://api.ap1.datadoghq.com/api/v2/datasets/{dataset_id}https://api.ap2.datadoghq.com/api/v2/datasets/{dataset_id}https://api.datadoghq.eu/api/v2/datasets/{dataset_id}https://api.ddog-gov.com/api/v2/datasets/{dataset_id}https://api.datadoghq.com/api/v2/datasets/{dataset_id}https://api.us3.datadoghq.com/api/v2/datasets/{dataset_id}https://api.us5.datadoghq.com/api/v2/datasets/{dataset_id}
### Overview
Retrieves the dataset associated with the ID.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
dataset_id [_required_]
string
The ID of a defined dataset.
### Response
  * [200](https://docs.datadoghq.com/api/latest/datasets/#GetDataset-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/datasets/#GetDataset-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/datasets/#GetDataset-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/datasets/#GetDataset-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/datasets/#GetDataset-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


Response containing a single dataset object.
Field
Type
Description
data
object
**Datasets Object Constraints**
  * **Tag Limit per Dataset** :
    * Each restricted dataset supports a maximum of 10 key:value pairs per product.
  * **Tag Key Rules per Telemetry Type** :
    * Only one tag key or attribute may be used to define access within a single telemetry type.
    * The same or different tag key may be used across different telemetry types.
  * **Tag Value Uniqueness** :
    * Tag values must be unique within a single dataset.
    * A tag value used in one dataset cannot be reused in another dataset of the same telemetry type.


attributes
object
Dataset metadata and configuration(s).
created_at
date-time
Timestamp when the dataset was created.
created_by
uuid
Unique ID of the user who created the dataset.
name
string
Name of the dataset.
principals
[string]
List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.
product_filters
[object]
List of product-specific filters.
filters [_required_]
[string]
Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type.
product [_required_]
string
Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.
id
string
Unique identifier for the dataset.
type
enum
Resource type, always set to `dataset`. Allowed enum values: `dataset`
default: `dataset`
```
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "name": "Security Audit Dataset",
      "principals": [
        "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "logs"
        }
      ]
    },
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "type": "dataset"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/datasets/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/datasets/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/datasets/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/datasets/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/datasets/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/datasets/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/datasets/?code-lang=typescript)


#####  Get a single dataset by ID
Copy
```
                  # Path parameters  
export dataset_id="0879ce27-29a1-481f-a12e-bc2a48ec9ae1"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets/${dataset_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a single dataset by ID
```
"""
Get a single dataset by ID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.get_dataset(
        dataset_id=DATASET_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a single dataset by ID
```
# Get a single dataset by ID returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

# there is a valid "dataset" in the system
DATASET_DATA_ID = ENV["DATASET_DATA_ID"]
p api_instance.get_dataset(DATASET_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a single dataset by ID
```
// Get a single dataset by ID returns "OK" response

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
	// there is a valid "dataset" in the system
	DatasetDataID := os.Getenv("DATASET_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetDataset", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDatasetsApi(apiClient)
	resp, r, err := api.GetDataset(ctx, DatasetDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.GetDataset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.GetDataset`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a single dataset by ID
```
// Get a single dataset by ID returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetResponseSingle;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    // there is a valid "dataset" in the system
    String DATASET_DATA_ID = System.getenv("DATASET_DATA_ID");

    try {
      DatasetResponseSingle result = apiInstance.getDataset(DATASET_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#getDataset");
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

#####  Get a single dataset by ID
```
// Get a single dataset by ID returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dataset" in the system
    let dataset_data_id = std::env::var("DATASET_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.get_dataset(dataset_data_id.clone()).await;
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

#####  Get a single dataset by ID
```
/**
 * Get a single dataset by ID returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

// there is a valid "dataset" in the system
const DATASET_DATA_ID = process.env.DATASET_DATA_ID as string;

const params: v2.DatasetsApiGetDatasetRequest = {
  datasetId: DATASET_DATA_ID,
};

apiInstance
  .getDataset(params)
  .then((data: v2.DatasetResponseSingle) => {
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
## [Get all datasets](https://docs.datadoghq.com/api/latest/datasets/#get-all-datasets)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/datasets/#get-all-datasets-v2)


**Note: Data Access is in preview. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
GET https://api.ap1.datadoghq.com/api/v2/datasetshttps://api.ap2.datadoghq.com/api/v2/datasetshttps://api.datadoghq.eu/api/v2/datasetshttps://api.ddog-gov.com/api/v2/datasetshttps://api.datadoghq.com/api/v2/datasetshttps://api.us3.datadoghq.com/api/v2/datasetshttps://api.us5.datadoghq.com/api/v2/datasets
### Overview
Get all datasets that have been configured for an organization. This endpoint requires the `user_access_read` permission.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/datasets/#GetAllDatasets-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/datasets/#GetAllDatasets-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/datasets/#GetAllDatasets-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


Response containing a list of datasets.
Field
Type
Description
data
[object]
The list of datasets returned in response.
attributes
object
Dataset metadata and configuration(s).
created_at
date-time
Timestamp when the dataset was created.
created_by
uuid
Unique ID of the user who created the dataset.
name
string
Name of the dataset.
principals
[string]
List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.
product_filters
[object]
List of product-specific filters.
filters [_required_]
[string]
Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type.
product [_required_]
string
Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.
id
string
Unique identifier for the dataset.
type
enum
Resource type, always set to `dataset`. Allowed enum values: `dataset`
default: `dataset`
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "created_by": "string",
        "name": "Security Audit Dataset",
        "principals": [
          "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
        ],
        "product_filters": [
          {
            "filters": [
              "@application.id:ABCD"
            ],
            "product": "logs"
          }
        ]
      },
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "type": "dataset"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/datasets/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/datasets/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/datasets/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/datasets/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/datasets/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/datasets/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/datasets/?code-lang=typescript)


#####  Get all datasets
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all datasets
```
"""
Get all datasets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

configuration = Configuration()
configuration.unstable_operations["get_all_datasets"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.get_all_datasets()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all datasets
```
# Get all datasets returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_all_datasets".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new
p api_instance.get_all_datasets()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all datasets
```
// Get all datasets returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.GetAllDatasets", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDatasetsApi(apiClient)
	resp, r, err := api.GetAllDatasets(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.GetAllDatasets`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.GetAllDatasets`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all datasets
```
// Get all datasets returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetResponseMulti;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getAllDatasets", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    try {
      DatasetResponseMulti result = apiInstance.getAllDatasets();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#getAllDatasets");
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

#####  Get all datasets
```
// Get all datasets returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetAllDatasets", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.get_all_datasets().await;
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

#####  Get all datasets
```
/**
 * Get all datasets returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getAllDatasets"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

apiInstance
  .getAllDatasets()
  .then((data: v2.DatasetResponseMulti) => {
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
## [Edit a dataset](https://docs.datadoghq.com/api/latest/datasets/#edit-a-dataset)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/datasets/#edit-a-dataset-v2)


**Note: Data Access is in preview. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
PUT https://api.ap1.datadoghq.com/api/v2/datasets/{dataset_id}https://api.ap2.datadoghq.com/api/v2/datasets/{dataset_id}https://api.datadoghq.eu/api/v2/datasets/{dataset_id}https://api.ddog-gov.com/api/v2/datasets/{dataset_id}https://api.datadoghq.com/api/v2/datasets/{dataset_id}https://api.us3.datadoghq.com/api/v2/datasets/{dataset_id}https://api.us5.datadoghq.com/api/v2/datasets/{dataset_id}
### Overview
Edits the dataset associated with the ID. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
dataset_id [_required_]
string
The ID of a defined dataset.
### Request
#### Body Data (required)
Dataset payload
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


Field
Type
Description
data [_required_]
object
**Datasets Object Constraints**
  * **Tag limit per dataset** :
    * Each restricted dataset supports a maximum of 10 key:value pairs per product.
  * **Tag key rules per telemetry type** :
    * Only one tag key or attribute may be used to define access within a single telemetry type.
    * The same or different tag key may be used across different telemetry types.
  * **Tag value uniqueness** :
    * Tag values must be unique within a single dataset.
    * A tag value used in one dataset cannot be reused in another dataset of the same telemetry type.


attributes [_required_]
object
Dataset metadata and configurations.
name [_required_]
string
Name of the dataset.
principals [_required_]
[string]
List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.
product_filters [_required_]
[object]
List of product-specific filters.
filters [_required_]
[string]
Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type.
product [_required_]
string
Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.
type [_required_]
enum
Resource type, always set to `dataset`. Allowed enum values: `dataset`
default: `dataset`
```
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:1234"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/datasets/#UpdateDataset-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/datasets/#UpdateDataset-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/datasets/#UpdateDataset-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/datasets/#UpdateDataset-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/datasets/#UpdateDataset-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


Response containing a single dataset object.
Field
Type
Description
data
object
**Datasets Object Constraints**
  * **Tag Limit per Dataset** :
    * Each restricted dataset supports a maximum of 10 key:value pairs per product.
  * **Tag Key Rules per Telemetry Type** :
    * Only one tag key or attribute may be used to define access within a single telemetry type.
    * The same or different tag key may be used across different telemetry types.
  * **Tag Value Uniqueness** :
    * Tag values must be unique within a single dataset.
    * A tag value used in one dataset cannot be reused in another dataset of the same telemetry type.


attributes
object
Dataset metadata and configuration(s).
created_at
date-time
Timestamp when the dataset was created.
created_by
uuid
Unique ID of the user who created the dataset.
name
string
Name of the dataset.
principals
[string]
List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.
product_filters
[object]
List of product-specific filters.
filters [_required_]
[string]
Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type.
product [_required_]
string
Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.
id
string
Unique identifier for the dataset.
type
enum
Resource type, always set to `dataset`. Allowed enum values: `dataset`
default: `dataset`
```
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "name": "Security Audit Dataset",
      "principals": [
        "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "logs"
        }
      ]
    },
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "type": "dataset"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/datasets/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/datasets/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/datasets/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/datasets/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/datasets/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/datasets/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/datasets/?code-lang=typescript)


#####  Edit a dataset returns "OK" response
Copy
```
                          # Path parameters  
export dataset_id="0879ce27-29a1-481f-a12e-bc2a48ec9ae1"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets/${dataset_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:1234"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
EOF  

                        
```

#####  Edit a dataset returns "OK" response
```
// Edit a dataset returns "OK" response

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
	// there is a valid "dataset" in the system
	DatasetDataID := os.Getenv("DATASET_DATA_ID")

	body := datadogV2.DatasetUpdateRequest{
		Data: datadogV2.DatasetRequest{
			Attributes: datadogV2.DatasetAttributesRequest{
				Name: "Security Audit Dataset",
				Principals: []string{
					"role:94172442-be03-11e9-a77a-3b7612558ac1",
				},
				ProductFilters: []datadogV2.FiltersPerProduct{
					{
						Filters: []string{
							"@application.id:1234",
						},
						Product: "metrics",
					},
				},
			},
			Type: datadogV2.DATASETTYPE_DATASET,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateDataset", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDatasetsApi(apiClient)
	resp, r, err := api.UpdateDataset(ctx, DatasetDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.UpdateDataset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.UpdateDataset`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Edit a dataset returns "OK" response
```
// Edit a dataset returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetAttributesRequest;
import com.datadog.api.client.v2.model.DatasetRequest;
import com.datadog.api.client.v2.model.DatasetResponseSingle;
import com.datadog.api.client.v2.model.DatasetType;
import com.datadog.api.client.v2.model.DatasetUpdateRequest;
import com.datadog.api.client.v2.model.FiltersPerProduct;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    // there is a valid "dataset" in the system
    String DATASET_DATA_ID = System.getenv("DATASET_DATA_ID");

    DatasetUpdateRequest body =
        new DatasetUpdateRequest()
            .data(
                new DatasetRequest()
                    .attributes(
                        new DatasetAttributesRequest()
                            .name("Security Audit Dataset")
                            .principals(
                                Collections.singletonList(
                                    "role:94172442-be03-11e9-a77a-3b7612558ac1"))
                            .productFilters(
                                Collections.singletonList(
                                    new FiltersPerProduct()
                                        .filters(Collections.singletonList("@application.id:1234"))
                                        .product("metrics"))))
                    .type(DatasetType.DATASET));

    try {
      DatasetResponseSingle result = apiInstance.updateDataset(DATASET_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#updateDataset");
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

#####  Edit a dataset returns "OK" response
```
"""
Edit a dataset returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi
from datadog_api_client.v2.model.dataset_attributes_request import DatasetAttributesRequest
from datadog_api_client.v2.model.dataset_request import DatasetRequest
from datadog_api_client.v2.model.dataset_type import DatasetType
from datadog_api_client.v2.model.dataset_update_request import DatasetUpdateRequest
from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

body = DatasetUpdateRequest(
    data=DatasetRequest(
        attributes=DatasetAttributesRequest(
            name="Security Audit Dataset",
            principals=[
                "role:94172442-be03-11e9-a77a-3b7612558ac1",
            ],
            product_filters=[
                FiltersPerProduct(
                    filters=[
                        "@application.id:1234",
                    ],
                    product="metrics",
                ),
            ],
        ),
        type=DatasetType.DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.update_dataset(dataset_id=DATASET_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Edit a dataset returns "OK" response
```
# Edit a dataset returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

# there is a valid "dataset" in the system
DATASET_DATA_ID = ENV["DATASET_DATA_ID"]

body = DatadogAPIClient::V2::DatasetUpdateRequest.new({
  data: DatadogAPIClient::V2::DatasetRequest.new({
    attributes: DatadogAPIClient::V2::DatasetAttributesRequest.new({
      name: "Security Audit Dataset",
      principals: [
        "role:94172442-be03-11e9-a77a-3b7612558ac1",
      ],
      product_filters: [
        DatadogAPIClient::V2::FiltersPerProduct.new({
          filters: [
            "@application.id:1234",
          ],
          product: "metrics",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::DatasetType::DATASET,
  }),
})
p api_instance.update_dataset(DATASET_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Edit a dataset returns "OK" response
```
// Edit a dataset returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;
use datadog_api_client::datadogV2::model::DatasetAttributesRequest;
use datadog_api_client::datadogV2::model::DatasetRequest;
use datadog_api_client::datadogV2::model::DatasetType;
use datadog_api_client::datadogV2::model::DatasetUpdateRequest;
use datadog_api_client::datadogV2::model::FiltersPerProduct;

#[tokio::main]
async fn main() {
    // there is a valid "dataset" in the system
    let dataset_data_id = std::env::var("DATASET_DATA_ID").unwrap();
    let body = DatasetUpdateRequest::new(DatasetRequest::new(
        DatasetAttributesRequest::new(
            "Security Audit Dataset".to_string(),
            vec!["role:94172442-be03-11e9-a77a-3b7612558ac1".to_string()],
            vec![FiltersPerProduct::new(
                vec!["@application.id:1234".to_string()],
                "metrics".to_string(),
            )],
        ),
        DatasetType::DATASET,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.update_dataset(dataset_data_id.clone(), body).await;
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

#####  Edit a dataset returns "OK" response
```
/**
 * Edit a dataset returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

// there is a valid "dataset" in the system
const DATASET_DATA_ID = process.env.DATASET_DATA_ID as string;

const params: v2.DatasetsApiUpdateDatasetRequest = {
  body: {
    data: {
      attributes: {
        name: "Security Audit Dataset",
        principals: ["role:94172442-be03-11e9-a77a-3b7612558ac1"],
        productFilters: [
          {
            filters: ["@application.id:1234"],
            product: "metrics",
          },
        ],
      },
      type: "dataset",
    },
  },
  datasetId: DATASET_DATA_ID,
};

apiInstance
  .updateDataset(params)
  .then((data: v2.DatasetResponseSingle) => {
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
## [Delete a dataset](https://docs.datadoghq.com/api/latest/datasets/#delete-a-dataset)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/datasets/#delete-a-dataset-v2)


**Note: Data Access is in preview. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
DELETE https://api.ap1.datadoghq.com/api/v2/datasets/{dataset_id}https://api.ap2.datadoghq.com/api/v2/datasets/{dataset_id}https://api.datadoghq.eu/api/v2/datasets/{dataset_id}https://api.ddog-gov.com/api/v2/datasets/{dataset_id}https://api.datadoghq.com/api/v2/datasets/{dataset_id}https://api.us3.datadoghq.com/api/v2/datasets/{dataset_id}https://api.us5.datadoghq.com/api/v2/datasets/{dataset_id}
### Overview
Deletes the dataset associated with the ID. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
dataset_id [_required_]
string
The ID of a defined dataset.
### Response
  * [204](https://docs.datadoghq.com/api/latest/datasets/#DeleteDataset-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/datasets/#DeleteDataset-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/datasets/#DeleteDataset-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/datasets/#DeleteDataset-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/datasets/#DeleteDataset-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Model](https://docs.datadoghq.com/api/latest/datasets/)
  * [Example](https://docs.datadoghq.com/api/latest/datasets/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/datasets/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/datasets/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/datasets/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/datasets/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/datasets/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/datasets/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/datasets/?code-lang=typescript)


#####  Delete a dataset
Copy
```
                  # Path parameters  
export dataset_id="0879ce27-29a1-481f-a12e-bc2a48ec9ae1"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets/${dataset_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a dataset
```
"""
Delete a dataset returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    api_instance.delete_dataset(
        dataset_id=DATASET_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a dataset
```
# Delete a dataset returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

# there is a valid "dataset" in the system
DATASET_DATA_ID = ENV["DATASET_DATA_ID"]
api_instance.delete_dataset(DATASET_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a dataset
```
// Delete a dataset returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "dataset" in the system
	DatasetDataID := os.Getenv("DATASET_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteDataset", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDatasetsApi(apiClient)
	r, err := api.DeleteDataset(ctx, DatasetDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.DeleteDataset`: %v\n", err)
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

#####  Delete a dataset
```
// Delete a dataset returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    // there is a valid "dataset" in the system
    String DATASET_DATA_ID = System.getenv("DATASET_DATA_ID");

    try {
      apiInstance.deleteDataset(DATASET_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#deleteDataset");
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

#####  Delete a dataset
```
// Delete a dataset returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dataset" in the system
    let dataset_data_id = std::env::var("DATASET_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.delete_dataset(dataset_data_id.clone()).await;
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

#####  Delete a dataset
```
/**
 * Delete a dataset returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

// there is a valid "dataset" in the system
const DATASET_DATA_ID = process.env.DATASET_DATA_ID as string;

const params: v2.DatasetsApiDeleteDatasetRequest = {
  datasetId: DATASET_DATA_ID,
};

apiInstance
  .deleteDataset(params)
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
![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=6832aae6-6843-4a84-90db-a8b6df1d8976&bo=1&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Datasets&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdatasets%2F&r=&evt=pageLoad&sv=2&cdb=AQAA&rn=985995)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=13c71917-f22a-4a0e-aafa-4dddc146023c&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c076f32d-a550-4a31-9216-5b51cbd905da&pt=Datasets&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdatasets%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=13c71917-f22a-4a0e-aafa-4dddc146023c&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c076f32d-a550-4a31-9216-5b51cbd905da&pt=Datasets&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdatasets%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
