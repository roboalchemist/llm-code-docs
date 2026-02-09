# Source: https://docs.datadoghq.com/api/latest/reference-tables.md

---
title: Reference Tables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Reference Tables
---

# Reference Tables

View and manage Reference Tables in your organization.

## Create reference table upload{% #create-reference-table-upload %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/reference-tables/uploads |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/reference-tables/uploads |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/reference-tables/uploads      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/reference-tables/uploads      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/reference-tables/uploads     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/reference-tables/uploads |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/reference-tables/uploads |

### Overview

Create a reference table upload for bulk data ingestion

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                 |
| ------------ | ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Request data for creating an upload for a file to be ingested into a reference table.                                       |
| data         | attributes                   | object   | Upload configuration specifying how data is uploaded by the user, and properties of the table to associate the upload with. |
| attributes   | headers [*required*]    | [string] | The CSV file headers that define the schema fields, provided in the same order as the columns in the uploaded file.         |
| attributes   | part_count [*required*] | int32    | Number of parts to split the file into for multipart upload.                                                                |
| attributes   | part_size [*required*]  | int64    | The size of each part in the upload in bytes. All parts except the last one must be at least 5,000,000 bytes.               |
| attributes   | table_name [*required*] | string   | Name of the table to associate with this upload.                                                                            |
| data         | type [*required*]       | enum     | Upload resource type. Allowed enum values: `upload`                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "headers": [
        "field_1",
        "field_2"
      ],
      "part_count": 3,
      "part_size": 10000000,
      "table_name": ""
    },
    "type": "upload"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Information about the upload created containing the upload ID and pre-signed URLs to PUT chunks of the CSV file to.

| Parent field | Field                  | Type     | Description                                                                       |
| ------------ | ---------------------- | -------- | --------------------------------------------------------------------------------- |
|              | data                   | object   | Upload ID and attributes of the created upload.                                   |
| data         | attributes             | object   | Pre-signed URLs for uploading parts of the file.                                  |
| attributes   | part_urls              | [string] | The pre-signed URLs for uploading parts. These URLs expire after 5 minutes.       |
| data         | id                     | string   | Unique identifier for this upload. Use this ID when creating the reference table. |
| data         | type [*required*] | enum     | Upload resource type. Allowed enum values: `upload`                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "part_urls": []
    },
    "id": "string",
    "type": "upload"
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
Forbidden
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/uploads" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "headers": [
        "field_1",
        "field_2"
      ],
      "part_count": 3,
      "part_size": 10000000,
      "table_name": ""
    },
    "type": "upload"
  }
}
EOF
                
##### 

```python
"""
Create reference table upload returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.create_upload_request import CreateUploadRequest
from datadog_api_client.v2.model.create_upload_request_data import CreateUploadRequestData
from datadog_api_client.v2.model.create_upload_request_data_attributes import CreateUploadRequestDataAttributes
from datadog_api_client.v2.model.create_upload_request_data_type import CreateUploadRequestDataType

body = CreateUploadRequest(
    data=CreateUploadRequestData(
        attributes=CreateUploadRequestDataAttributes(
            headers=[
                "id",
                "name",
                "value",
            ],
            table_name="test_upload_table_Example-Reference-Table",
            part_count=1,
            part_size=1024,
        ),
        type=CreateUploadRequestDataType.UPLOAD,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.create_reference_table_upload(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create reference table upload returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new

body = DatadogAPIClient::V2::CreateUploadRequest.new({
  data: DatadogAPIClient::V2::CreateUploadRequestData.new({
    attributes: DatadogAPIClient::V2::CreateUploadRequestDataAttributes.new({
      headers: [
        "id",
        "name",
        "value",
      ],
      table_name: "test_upload_table_Example-Reference-Table",
      part_count: 1,
      part_size: 1024,
    }),
    type: DatadogAPIClient::V2::CreateUploadRequestDataType::UPLOAD,
  }),
})
p api_instance.create_reference_table_upload(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create reference table upload returns "Created" response

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
	body := datadogV2.CreateUploadRequest{
		Data: &datadogV2.CreateUploadRequestData{
			Attributes: &datadogV2.CreateUploadRequestDataAttributes{
				Headers: []string{
					"id",
					"name",
					"value",
				},
				TableName: "test_upload_table_Example-Reference-Table",
				PartCount: 1,
				PartSize:  1024,
			},
			Type: datadogV2.CREATEUPLOADREQUESTDATATYPE_UPLOAD,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewReferenceTablesApi(apiClient)
	resp, r, err := api.CreateReferenceTableUpload(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.CreateReferenceTableUpload`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ReferenceTablesApi.CreateReferenceTableUpload`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create reference table upload returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.CreateUploadRequest;
import com.datadog.api.client.v2.model.CreateUploadRequestData;
import com.datadog.api.client.v2.model.CreateUploadRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateUploadRequestDataType;
import com.datadog.api.client.v2.model.CreateUploadResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    CreateUploadRequest body =
        new CreateUploadRequest()
            .data(
                new CreateUploadRequestData()
                    .attributes(
                        new CreateUploadRequestDataAttributes()
                            .headers(Arrays.asList("id", "name", "value"))
                            .tableName("test_upload_table_Example-Reference-Table")
                            .partCount(1)
                            .partSize(1024L))
                    .type(CreateUploadRequestDataType.UPLOAD));

    try {
      CreateUploadResponse result = apiInstance.createReferenceTableUpload(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#createReferenceTableUpload");
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
// Create reference table upload returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;
use datadog_api_client::datadogV2::model::CreateUploadRequest;
use datadog_api_client::datadogV2::model::CreateUploadRequestData;
use datadog_api_client::datadogV2::model::CreateUploadRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreateUploadRequestDataType;

#[tokio::main]
async fn main() {
    let body = CreateUploadRequest::new().data(
        CreateUploadRequestData::new(CreateUploadRequestDataType::UPLOAD).attributes(
            CreateUploadRequestDataAttributes::new(
                vec!["id".to_string(), "name".to_string(), "value".to_string()],
                1,
                1024,
                "test_upload_table_Example-Reference-Table".to_string(),
            ),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.create_reference_table_upload(body).await;
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
 * Create reference table upload returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiCreateReferenceTableUploadRequest = {
  body: {
    data: {
      attributes: {
        headers: ["id", "name", "value"],
        tableName: "test_upload_table_Example-Reference-Table",
        partCount: 1,
        partSize: 1024,
      },
      type: "upload",
    },
  },
};

apiInstance
  .createReferenceTableUpload(params)
  .then((data: v2.CreateUploadResponse) => {
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

## Create reference table{% #create-reference-table %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/reference-tables/tables |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/reference-tables/tables |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/reference-tables/tables      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/reference-tables/tables      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/reference-tables/tables     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/reference-tables/tables |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/reference-tables/tables |

### Overview



Creates a reference table. You can provide data in two ways:

1. Call POST /api/v2/reference-tables/upload to get an upload ID. Then, PUT the CSV data (not the file itself) in chunks to each URL in the request body. Finally, call this POST endpoint with `upload_id` in `file_metadata`.
1. Provide `access_details` in `file_metadata` pointing to a CSV file in cloud storage.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field   | Field                                        | Type          | Description                                                                                                                                                |
| -------------- | -------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data                                         | object        | The data object containing the table definition.                                                                                                           |
| data           | attributes                                   | object        | Attributes that define the reference table's configuration and properties.                                                                                 |
| attributes     | description                                  | string        | Optional text describing the purpose or contents of this reference table.                                                                                  |
| attributes     | file_metadata                                |  <oneOf> | Metadata specifying where and how to access the reference table's data file.                                                                               |
| file_metadata  | Option 1                                     | object        | Cloud storage file metadata for create requests. Both access_details and sync_enabled are required.                                                        |
| Option 1       | access_details [*required*]             | object        | Cloud storage access configuration for the reference table data file.                                                                                      |
| access_details | aws_detail                                   | object        | Amazon Web Services S3 storage access configuration.                                                                                                       |
| aws_detail     | aws_account_id [*required*]             | string        | AWS account ID where the S3 bucket is located.                                                                                                             |
| aws_detail     | aws_bucket_name [*required*]            | string        | S3 bucket containing the CSV file.                                                                                                                         |
| aws_detail     | file_path [*required*]                  | string        | The relative file path from the S3 bucket root to the CSV file.                                                                                            |
| access_details | azure_detail                                 | object        | Azure Blob Storage access configuration.                                                                                                                   |
| azure_detail   | azure_client_id [*required*]            | string        | Azure service principal (application) client ID with permissions to read from the container.                                                               |
| azure_detail   | azure_container_name [*required*]       | string        | Azure Blob Storage container containing the CSV file.                                                                                                      |
| azure_detail   | azure_storage_account_name [*required*] | string        | Azure storage account where the container is located.                                                                                                      |
| azure_detail   | azure_tenant_id [*required*]            | string        | Azure Active Directory tenant ID.                                                                                                                          |
| azure_detail   | file_path [*required*]                  | string        | The relative file path from the Azure container root to the CSV file.                                                                                      |
| access_details | gcp_detail                                   | object        | Google Cloud Platform storage access configuration.                                                                                                        |
| gcp_detail     | file_path [*required*]                  | string        | The relative file path from the GCS bucket root to the CSV file.                                                                                           |
| gcp_detail     | gcp_bucket_name [*required*]            | string        | GCP bucket containing the CSV file.                                                                                                                        |
| gcp_detail     | gcp_project_id [*required*]             | string        | GCP project ID where the bucket is located.                                                                                                                |
| gcp_detail     | gcp_service_account_email [*required*]  | string        | Service account email with read permissions for the GCS bucket.                                                                                            |
| Option 1       | sync_enabled [*required*]               | boolean       | Whether this table is synced automatically.                                                                                                                |
| file_metadata  | Option 2                                     | object        | Local file metadata for create requests using the upload ID.                                                                                               |
| Option 2       | upload_id [*required*]                  | string        | The upload ID.                                                                                                                                             |
| attributes     | schema [*required*]                     | object        | Schema defining the structure and columns of the reference table.                                                                                          |
| schema         | fields [*required*]                     | [object]      | The schema fields.                                                                                                                                         |
| fields         | name [*required*]                       | string        | The field name.                                                                                                                                            |
| fields         | type [*required*]                       | enum          | The field type for reference table schema fields. Allowed enum values: `STRING,INT32`                                                                      |
| schema         | primary_keys [*required*]               | [string]      | List of field names that serve as primary keys for the table. Only one primary key is supported, and it is used as an ID to retrieve rows.                 |
| attributes     | source [*required*]                     | enum          | The source type for creating reference table data. Only these source types can be created through this API. Allowed enum values: `LOCAL_FILE,S3,GCS,AZURE` |
| attributes     | table_name [*required*]                 | string        | Name to identify this reference table.                                                                                                                     |
| attributes     | tags                                         | [string]      | Tags for organizing and filtering reference tables.                                                                                                        |
| data           | type [*required*]                       | enum          | Reference table resource type. Allowed enum values: `reference_table`                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "string",
      "file_metadata": {
        "access_details": {
          "aws_detail": {
            "aws_account_id": "123456789000",
            "aws_bucket_name": "example-data-bucket",
            "file_path": "reference-tables/users.csv"
          },
          "azure_detail": {
            "azure_client_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
            "azure_container_name": "reference-data",
            "azure_storage_account_name": "examplestorageaccount",
            "azure_tenant_id": "cccccccc-4444-5555-6666-dddddddddddd",
            "file_path": "tables/users.csv"
          },
          "gcp_detail": {
            "file_path": "data/reference_tables/users.csv",
            "gcp_bucket_name": "example-data-bucket",
            "gcp_project_id": "example-gcp-project-12345",
            "gcp_service_account_email": "example-service@example-gcp-project-12345.iam.gserviceaccount.com"
          }
        },
        "sync_enabled": false
      },
      "schema": {
        "fields": [
          {
            "name": "field_1",
            "type": "STRING"
          }
        ],
        "primary_keys": [
          "field_1"
        ]
      },
      "source": "LOCAL_FILE",
      "table_name": "table_1",
      "tags": [
        "tag_1",
        "tag_2"
      ]
    },
    "type": "reference_table"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
A reference table resource containing its full configuration and state.

| Parent field   | Field                          | Type     | Description                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data                           | object   | The data object containing the reference table configuration and state.                                                                                                                                                                                                    |
| data           | attributes                     | object   | Attributes that define the reference table's configuration and properties.                                                                                                                                                                                                 |
| attributes     | created_by                     | string   | UUID of the user who created the reference table.                                                                                                                                                                                                                          |
| attributes     | description                    | string   | Optional text describing the purpose or contents of this reference table.                                                                                                                                                                                                  |
| attributes     | file_metadata                  | object   | Metadata specifying where and how to access the reference table's data file.                                                                                                                                                                                               | For cloud storage tables (S3/GCS/Azure): | For local file tables: |
| file_metadata  | access_details                 | object   | Cloud storage access configuration. Only present for cloud storage sources (S3, GCS, Azure).                                                                                                                                                                               |
| access_details | aws_detail                     | object   | Amazon Web Services S3 storage access configuration.                                                                                                                                                                                                                       |
| aws_detail     | aws_account_id                 | string   | AWS account ID where the S3 bucket is located.                                                                                                                                                                                                                             |
| aws_detail     | aws_bucket_name                | string   | S3 bucket containing the CSV file.                                                                                                                                                                                                                                         |
| aws_detail     | file_path                      | string   | The relative file path from the S3 bucket root to the CSV file.                                                                                                                                                                                                            |
| access_details | azure_detail                   | object   | Azure Blob Storage access configuration.                                                                                                                                                                                                                                   |
| azure_detail   | azure_client_id                | string   | Azure service principal (application) client ID with permissions to read from the container.                                                                                                                                                                               |
| azure_detail   | azure_container_name           | string   | Azure Blob Storage container containing the CSV file.                                                                                                                                                                                                                      |
| azure_detail   | azure_storage_account_name     | string   | Azure storage account where the container is located.                                                                                                                                                                                                                      |
| azure_detail   | azure_tenant_id                | string   | Azure Active Directory tenant ID.                                                                                                                                                                                                                                          |
| azure_detail   | file_path                      | string   | The relative file path from the Azure container root to the CSV file.                                                                                                                                                                                                      |
| access_details | gcp_detail                     | object   | Google Cloud Platform storage access configuration.                                                                                                                                                                                                                        |
| gcp_detail     | file_path                      | string   | The relative file path from the GCS bucket root to the CSV file.                                                                                                                                                                                                           |
| gcp_detail     | gcp_bucket_name                | string   | GCP bucket containing the CSV file.                                                                                                                                                                                                                                        |
| gcp_detail     | gcp_project_id                 | string   | GCP project ID where the bucket is located.                                                                                                                                                                                                                                |
| gcp_detail     | gcp_service_account_email      | string   | Service account email with read permissions for the GCS bucket.                                                                                                                                                                                                            |
| file_metadata  | error_message                  | string   | The error message returned from the last operation (sync for cloud storage, upload for local file).                                                                                                                                                                        |
| file_metadata  | error_row_count                | int64    | The number of rows that failed to process.                                                                                                                                                                                                                                 |
| file_metadata  | error_type                     | enum     | The type of error that occurred during file processing. Only applicable for cloud storage sources. Allowed enum values: `TABLE_SCHEMA_ERROR,FILE_FORMAT_ERROR,CONFIGURATION_ERROR,QUOTA_EXCEEDED,CONFLICT_ERROR,VALIDATION_ERROR,STATE_ERROR,OPERATION_ERROR,SYSTEM_ERROR` |
| file_metadata  | sync_enabled                   | boolean  | Whether this table is synced automatically from cloud storage. Only applicable for cloud storage sources.                                                                                                                                                                  |
| attributes     | last_updated_by                | string   | UUID of the user who last updated the reference table.                                                                                                                                                                                                                     |
| attributes     | row_count                      | int64    | The number of successfully processed rows in the reference table.                                                                                                                                                                                                          |
| attributes     | schema                         | object   | Schema defining the structure and columns of the reference table.                                                                                                                                                                                                          |
| schema         | fields [*required*]       | [object] | The schema fields.                                                                                                                                                                                                                                                         |
| fields         | name [*required*]         | string   | The field name.                                                                                                                                                                                                                                                            |
| fields         | type [*required*]         | enum     | The field type for reference table schema fields. Allowed enum values: `STRING,INT32`                                                                                                                                                                                      |
| schema         | primary_keys [*required*] | [string] | List of field names that serve as primary keys for the table. Only one primary key is supported, and it is used as an ID to retrieve rows.                                                                                                                                 |
| attributes     | source                         | enum     | The source type for reference table data. Includes all possible source types that can appear in responses. Allowed enum values: `LOCAL_FILE,S3,GCS,AZURE,SERVICENOW,SALESFORCE,DATABRICKS,SNOWFLAKE`                                                                       |
| attributes     | status                         | string   | The processing status of the table.                                                                                                                                                                                                                                        |
| attributes     | table_name                     | string   | Unique name to identify this reference table. Used in enrichment processors and API calls.                                                                                                                                                                                 |
| attributes     | tags                           | [string] | Tags for organizing and filtering reference tables.                                                                                                                                                                                                                        |
| attributes     | updated_at                     | string   | When the reference table was last updated, in ISO 8601 format.                                                                                                                                                                                                             |
| data           | id                             | string   | Unique identifier for the reference table.                                                                                                                                                                                                                                 |
| data           | type [*required*]         | enum     | Reference table resource type. Allowed enum values: `reference_table`                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_by": "00000000-0000-0000-0000-000000000000",
      "description": "example description",
      "file_metadata": {
        "access_details": {
          "aws_detail": {
            "aws_account_id": "123456789000",
            "aws_bucket_name": "my-bucket",
            "file_path": "path/to/file.csv"
          }
        },
        "sync_enabled": true
      },
      "last_updated_by": "00000000-0000-0000-0000-000000000000",
      "row_count": 5,
      "schema": {
        "fields": [
          {
            "name": "id",
            "type": "INT32"
          },
          {
            "name": "name",
            "type": "STRING"
          }
        ],
        "primary_keys": [
          "id"
        ]
      },
      "source": "S3",
      "status": "DONE",
      "table_name": "test_reference_table",
      "tags": [
        "tag1",
        "tag2"
      ],
      "updated_at": "2000-01-01T01:00:00+00:00"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "reference_table"
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
Forbidden
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
                  \## Create table from cloud storage (S3)
# 
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Customer reference data synced from S3",
      "file_metadata": {
        "access_details": {
          "aws_detail": {
            "aws_account_id": "924305315327",
            "aws_bucket_name": "my-data-bucket",
            "file_path": "customers.csv"
          }
        },
        "sync_enabled": true
      },
      "schema": {
        "fields": [
          {
            "name": "customer_id",
            "type": "STRING"
          },
          {
            "name": "customer_name",
            "type": "STRING"
          },
          {
            "name": "email",
            "type": "STRING"
          }
        ],
        "primary_keys": [
          "customer_id"
        ]
      },
      "source": "S3",
      "table_name": "customer_reference_data",
      "tags": [
        "team:data-platform"
      ]
    },
    "type": "reference_table"
  }
}
EOF\## Create table from local file upload
# 
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Product catalog uploaded via local file",
      "file_metadata": {
        "upload_id": "00000000-0000-0000-0000-000000000000"
      },
      "schema": {
        "fields": [
          {
            "name": "product_id",
            "type": "STRING"
          },
          {
            "name": "product_name",
            "type": "STRING"
          },
          {
            "name": "price",
            "type": "DOUBLE"
          }
        ],
        "primary_keys": [
          "product_id"
        ]
      },
      "source": "LOCAL_FILE",
      "table_name": "product_catalog",
      "tags": [
        "team:ecommerce"
      ]
    },
    "type": "reference_table"
  }
}
EOF
                
##### 

```python
"""
Create reference table returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.create_table_request import CreateTableRequest
from datadog_api_client.v2.model.create_table_request_data import CreateTableRequestData
from datadog_api_client.v2.model.create_table_request_data_attributes import CreateTableRequestDataAttributes
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_cloud_storage import (
    CreateTableRequestDataAttributesFileMetadataCloudStorage,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_azure_detail import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_schema import (
    CreateTableRequestDataAttributesSchema,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_schema_fields_items import (
    CreateTableRequestDataAttributesSchemaFieldsItems,
)
from datadog_api_client.v2.model.create_table_request_data_type import CreateTableRequestDataType
from datadog_api_client.v2.model.reference_table_create_source_type import ReferenceTableCreateSourceType
from datadog_api_client.v2.model.reference_table_schema_field_type import ReferenceTableSchemaFieldType

body = CreateTableRequest(
    data=CreateTableRequestData(
        attributes=CreateTableRequestDataAttributes(
            file_metadata=CreateTableRequestDataAttributesFileMetadataCloudStorage(
                access_details=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails(
                    aws_detail=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail(
                        aws_account_id="123456789000",
                        aws_bucket_name="example-data-bucket",
                        file_path="reference-tables/users.csv",
                    ),
                    azure_detail=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail(
                        azure_client_id="aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
                        azure_container_name="reference-data",
                        azure_storage_account_name="examplestorageaccount",
                        azure_tenant_id="cccccccc-4444-5555-6666-dddddddddddd",
                        file_path="tables/users.csv",
                    ),
                    gcp_detail=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail(
                        file_path="data/reference_tables/users.csv",
                        gcp_bucket_name="example-data-bucket",
                        gcp_project_id="example-gcp-project-12345",
                        gcp_service_account_email="example-service@example-gcp-project-12345.iam.gserviceaccount.com",
                    ),
                ),
                sync_enabled=False,
            ),
            schema=CreateTableRequestDataAttributesSchema(
                fields=[
                    CreateTableRequestDataAttributesSchemaFieldsItems(
                        name="field_1",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                ],
                primary_keys=[
                    "field_1",
                ],
            ),
            source=ReferenceTableCreateSourceType.LOCAL_FILE,
            table_name="table_1",
            tags=[
                "tag_1",
                "tag_2",
            ],
        ),
        type=CreateTableRequestDataType.REFERENCE_TABLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.create_reference_table(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create reference table returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new

body = DatadogAPIClient::V2::CreateTableRequest.new({
  data: DatadogAPIClient::V2::CreateTableRequestData.new({
    attributes: DatadogAPIClient::V2::CreateTableRequestDataAttributes.new({
      file_metadata: DatadogAPIClient::V2::CreateTableRequestDataAttributesFileMetadataCloudStorage.new({
        access_details: DatadogAPIClient::V2::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails.new({
          aws_detail: DatadogAPIClient::V2::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail.new({
            aws_account_id: "123456789000",
            aws_bucket_name: "example-data-bucket",
            file_path: "reference-tables/users.csv",
          }),
          azure_detail: DatadogAPIClient::V2::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail.new({
            azure_client_id: "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
            azure_container_name: "reference-data",
            azure_storage_account_name: "examplestorageaccount",
            azure_tenant_id: "cccccccc-4444-5555-6666-dddddddddddd",
            file_path: "tables/users.csv",
          }),
          gcp_detail: DatadogAPIClient::V2::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail.new({
            file_path: "data/reference_tables/users.csv",
            gcp_bucket_name: "example-data-bucket",
            gcp_project_id: "example-gcp-project-12345",
            gcp_service_account_email: "example-service@example-gcp-project-12345.iam.gserviceaccount.com",
          }),
        }),
        sync_enabled: false,
      }),
      schema: DatadogAPIClient::V2::CreateTableRequestDataAttributesSchema.new({
        fields: [
          DatadogAPIClient::V2::CreateTableRequestDataAttributesSchemaFieldsItems.new({
            name: "field_1",
            type: DatadogAPIClient::V2::ReferenceTableSchemaFieldType::STRING,
          }),
        ],
        primary_keys: [
          "field_1",
        ],
      }),
      source: DatadogAPIClient::V2::ReferenceTableCreateSourceType::LOCAL_FILE,
      table_name: "table_1",
      tags: [
        "tag_1",
        "tag_2",
      ],
    }),
    type: DatadogAPIClient::V2::CreateTableRequestDataType::REFERENCE_TABLE,
  }),
})
p api_instance.create_reference_table(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create reference table returns "Created" response

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
	body := datadogV2.CreateTableRequest{
		Data: &datadogV2.CreateTableRequestData{
			Attributes: &datadogV2.CreateTableRequestDataAttributes{
				FileMetadata: &datadogV2.CreateTableRequestDataAttributesFileMetadata{
					CreateTableRequestDataAttributesFileMetadataCloudStorage: &datadogV2.CreateTableRequestDataAttributesFileMetadataCloudStorage{
						AccessDetails: datadogV2.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails{
							AwsDetail: &datadogV2.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail{
								AwsAccountId:  "123456789000",
								AwsBucketName: "example-data-bucket",
								FilePath:      "reference-tables/users.csv",
							},
							AzureDetail: &datadogV2.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail{
								AzureClientId:           "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
								AzureContainerName:      "reference-data",
								AzureStorageAccountName: "examplestorageaccount",
								AzureTenantId:           "cccccccc-4444-5555-6666-dddddddddddd",
								FilePath:                "tables/users.csv",
							},
							GcpDetail: &datadogV2.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail{
								FilePath:               "data/reference_tables/users.csv",
								GcpBucketName:          "example-data-bucket",
								GcpProjectId:           "example-gcp-project-12345",
								GcpServiceAccountEmail: "example-service@example-gcp-project-12345.iam.gserviceaccount.com",
							},
						},
						SyncEnabled: false,
					}},
				Schema: datadogV2.CreateTableRequestDataAttributesSchema{
					Fields: []datadogV2.CreateTableRequestDataAttributesSchemaFieldsItems{
						{
							Name: "field_1",
							Type: datadogV2.REFERENCETABLESCHEMAFIELDTYPE_STRING,
						},
					},
					PrimaryKeys: []string{
						"field_1",
					},
				},
				Source:    datadogV2.REFERENCETABLECREATESOURCETYPE_LOCAL_FILE,
				TableName: "table_1",
				Tags: []string{
					"tag_1",
					"tag_2",
				},
			},
			Type: datadogV2.CREATETABLEREQUESTDATATYPE_REFERENCE_TABLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewReferenceTablesApi(apiClient)
	resp, r, err := api.CreateReferenceTable(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.CreateReferenceTable`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ReferenceTablesApi.CreateReferenceTable`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create reference table returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.CreateTableRequest;
import com.datadog.api.client.v2.model.CreateTableRequestData;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesFileMetadata;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesFileMetadataCloudStorage;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesSchema;
import com.datadog.api.client.v2.model.CreateTableRequestDataAttributesSchemaFieldsItems;
import com.datadog.api.client.v2.model.CreateTableRequestDataType;
import com.datadog.api.client.v2.model.ReferenceTableCreateSourceType;
import com.datadog.api.client.v2.model.ReferenceTableSchemaFieldType;
import com.datadog.api.client.v2.model.TableResultV2;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    CreateTableRequest body =
        new CreateTableRequest()
            .data(
                new CreateTableRequestData()
                    .attributes(
                        new CreateTableRequestDataAttributes()
                            .fileMetadata(
                                new CreateTableRequestDataAttributesFileMetadata(
                                    new CreateTableRequestDataAttributesFileMetadataCloudStorage()
                                        .accessDetails(
                                            new CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails()
                                                .awsDetail(
                                                    new CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail()
                                                        .awsAccountId("123456789000")
                                                        .awsBucketName("example-data-bucket")
                                                        .filePath("reference-tables/users.csv"))
                                                .azureDetail(
                                                    new CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail()
                                                        .azureClientId(
                                                            "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb")
                                                        .azureContainerName("reference-data")
                                                        .azureStorageAccountName(
                                                            "examplestorageaccount")
                                                        .azureTenantId(
                                                            "cccccccc-4444-5555-6666-dddddddddddd")
                                                        .filePath("tables/users.csv"))
                                                .gcpDetail(
                                                    new CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail()
                                                        .filePath("data/reference_tables/users.csv")
                                                        .gcpBucketName("example-data-bucket")
                                                        .gcpProjectId("example-gcp-project-12345")
                                                        .gcpServiceAccountEmail(
                                                            "example-service@example-gcp-project-12345.iam.gserviceaccount.com")))
                                        .syncEnabled(false)))
                            .schema(
                                new CreateTableRequestDataAttributesSchema()
                                    .fields(
                                        Collections.singletonList(
                                            new CreateTableRequestDataAttributesSchemaFieldsItems()
                                                .name("field_1")
                                                .type(ReferenceTableSchemaFieldType.STRING)))
                                    .primaryKeys(Collections.singletonList("field_1")))
                            .source(ReferenceTableCreateSourceType.LOCAL_FILE)
                            .tableName("table_1")
                            .tags(Arrays.asList("tag_1", "tag_2")))
                    .type(CreateTableRequestDataType.REFERENCE_TABLE));

    try {
      TableResultV2 result = apiInstance.createReferenceTable(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#createReferenceTable");
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
// Create reference table returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;
use datadog_api_client::datadogV2::model::CreateTableRequest;
use datadog_api_client::datadogV2::model::CreateTableRequestData;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesFileMetadata;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesFileMetadataCloudStorage;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesSchema;
use datadog_api_client::datadogV2::model::CreateTableRequestDataAttributesSchemaFieldsItems;
use datadog_api_client::datadogV2::model::CreateTableRequestDataType;
use datadog_api_client::datadogV2::model::ReferenceTableCreateSourceType;
use datadog_api_client::datadogV2::model::ReferenceTableSchemaFieldType;

#[tokio::main]
async fn main() {
    let body =
        CreateTableRequest
        ::new().data(
            CreateTableRequestData::new(
                CreateTableRequestDataType::REFERENCE_TABLE,
            ).attributes(
                CreateTableRequestDataAttributes::new(
                    CreateTableRequestDataAttributesSchema::new(
                        vec![
                            CreateTableRequestDataAttributesSchemaFieldsItems::new(
                                "field_1".to_string(),
                                ReferenceTableSchemaFieldType::STRING,
                            )
                        ],
                        vec!["field_1".to_string()],
                    ),
                    ReferenceTableCreateSourceType::LOCAL_FILE,
                    "table_1".to_string(),
                )
                    .file_metadata(
                        CreateTableRequestDataAttributesFileMetadata
                        ::CreateTableRequestDataAttributesFileMetadataCloudStorage(
                            Box::new(
                                CreateTableRequestDataAttributesFileMetadataCloudStorage::new(
                                    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails::new()
                                        .aws_detail(
                                            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail
                                            ::new(
                                                "123456789000".to_string(),
                                                "example-data-bucket".to_string(),
                                                "reference-tables/users.csv".to_string(),
                                            ),
                                        )
                                        .azure_detail(
                                            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail
                                            ::new(
                                                "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb".to_string(),
                                                "reference-data".to_string(),
                                                "examplestorageaccount".to_string(),
                                                "cccccccc-4444-5555-6666-dddddddddddd".to_string(),
                                                "tables/users.csv".to_string(),
                                            ),
                                        )
                                        .gcp_detail(
                                            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail
                                            ::new(
                                                "data/reference_tables/users.csv".to_string(),
                                                "example-data-bucket".to_string(),
                                                "example-gcp-project-12345".to_string(),
                                                "example-service@example-gcp-project-12345.iam.gserviceaccount.com".to_string(),
                                            ),
                                        ),
                                    false,
                                ),
                            ),
                        ),
                    )
                    .tags(vec!["tag_1".to_string(), "tag_2".to_string()]),
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.create_reference_table(body).await;
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
 * Create reference table returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiCreateReferenceTableRequest = {
  body: {
    data: {
      attributes: {
        fileMetadata: {
          accessDetails: {
            awsDetail: {
              awsAccountId: "123456789000",
              awsBucketName: "example-data-bucket",
              filePath: "reference-tables/users.csv",
            },
            azureDetail: {
              azureClientId: "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
              azureContainerName: "reference-data",
              azureStorageAccountName: "examplestorageaccount",
              azureTenantId: "cccccccc-4444-5555-6666-dddddddddddd",
              filePath: "tables/users.csv",
            },
            gcpDetail: {
              filePath: "data/reference_tables/users.csv",
              gcpBucketName: "example-data-bucket",
              gcpProjectId: "example-gcp-project-12345",
              gcpServiceAccountEmail:
                "example-service@example-gcp-project-12345.iam.gserviceaccount.com",
            },
          },
          syncEnabled: false,
        },
        schema: {
          fields: [
            {
              name: "field_1",
              type: "STRING",
            },
          ],
          primaryKeys: ["field_1"],
        },
        source: "LOCAL_FILE",
        tableName: "table_1",
        tags: ["tag_1", "tag_2"],
      },
      type: "reference_table",
    },
  },
};

apiInstance
  .createReferenceTable(params)
  .then((data: v2.TableResultV2) => {
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

## List tables{% #list-tables %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/reference-tables/tables |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/reference-tables/tables |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/reference-tables/tables      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/reference-tables/tables      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/reference-tables/tables     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/reference-tables/tables |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/reference-tables/tables |

### Overview

List all reference tables in this organization.

### Arguments

#### Query Strings

| Name                         | Type    | Description                                                                                                                                                                                                      |
| ---------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[limit]                  | integer | Number of tables to return.                                                                                                                                                                                      |
| page[offset]                 | integer | Number of tables to skip for pagination.                                                                                                                                                                         |
| sort                         | enum    | Sort field and direction for the list of reference tables. Use field name for ascending, prefix with "-" for descending.Allowed enum values: `updated_at, table_name, status, -updated_at, -table_name, -status` |
| filter[status]               | string  | Filter by table status.                                                                                                                                                                                          |
| filter[table_name][exact]    | string  | Filter by exact table name match.                                                                                                                                                                                |
| filter[table_name][contains] | string  | Filter by table name containing substring.                                                                                                                                                                       |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of reference tables.

| Parent field   | Field                          | Type     | Description                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data [*required*]         | [object] | The reference tables.                                                                                                                                                                                                                                                      |
| data           | attributes                     | object   | Attributes that define the reference table's configuration and properties.                                                                                                                                                                                                 |
| attributes     | created_by                     | string   | UUID of the user who created the reference table.                                                                                                                                                                                                                          |
| attributes     | description                    | string   | Optional text describing the purpose or contents of this reference table.                                                                                                                                                                                                  |
| attributes     | file_metadata                  | object   | Metadata specifying where and how to access the reference table's data file.                                                                                                                                                                                               | For cloud storage tables (S3/GCS/Azure): | For local file tables: |
| file_metadata  | access_details                 | object   | Cloud storage access configuration. Only present for cloud storage sources (S3, GCS, Azure).                                                                                                                                                                               |
| access_details | aws_detail                     | object   | Amazon Web Services S3 storage access configuration.                                                                                                                                                                                                                       |
| aws_detail     | aws_account_id                 | string   | AWS account ID where the S3 bucket is located.                                                                                                                                                                                                                             |
| aws_detail     | aws_bucket_name                | string   | S3 bucket containing the CSV file.                                                                                                                                                                                                                                         |
| aws_detail     | file_path                      | string   | The relative file path from the S3 bucket root to the CSV file.                                                                                                                                                                                                            |
| access_details | azure_detail                   | object   | Azure Blob Storage access configuration.                                                                                                                                                                                                                                   |
| azure_detail   | azure_client_id                | string   | Azure service principal (application) client ID with permissions to read from the container.                                                                                                                                                                               |
| azure_detail   | azure_container_name           | string   | Azure Blob Storage container containing the CSV file.                                                                                                                                                                                                                      |
| azure_detail   | azure_storage_account_name     | string   | Azure storage account where the container is located.                                                                                                                                                                                                                      |
| azure_detail   | azure_tenant_id                | string   | Azure Active Directory tenant ID.                                                                                                                                                                                                                                          |
| azure_detail   | file_path                      | string   | The relative file path from the Azure container root to the CSV file.                                                                                                                                                                                                      |
| access_details | gcp_detail                     | object   | Google Cloud Platform storage access configuration.                                                                                                                                                                                                                        |
| gcp_detail     | file_path                      | string   | The relative file path from the GCS bucket root to the CSV file.                                                                                                                                                                                                           |
| gcp_detail     | gcp_bucket_name                | string   | GCP bucket containing the CSV file.                                                                                                                                                                                                                                        |
| gcp_detail     | gcp_project_id                 | string   | GCP project ID where the bucket is located.                                                                                                                                                                                                                                |
| gcp_detail     | gcp_service_account_email      | string   | Service account email with read permissions for the GCS bucket.                                                                                                                                                                                                            |
| file_metadata  | error_message                  | string   | The error message returned from the last operation (sync for cloud storage, upload for local file).                                                                                                                                                                        |
| file_metadata  | error_row_count                | int64    | The number of rows that failed to process.                                                                                                                                                                                                                                 |
| file_metadata  | error_type                     | enum     | The type of error that occurred during file processing. Only applicable for cloud storage sources. Allowed enum values: `TABLE_SCHEMA_ERROR,FILE_FORMAT_ERROR,CONFIGURATION_ERROR,QUOTA_EXCEEDED,CONFLICT_ERROR,VALIDATION_ERROR,STATE_ERROR,OPERATION_ERROR,SYSTEM_ERROR` |
| file_metadata  | sync_enabled                   | boolean  | Whether this table is synced automatically from cloud storage. Only applicable for cloud storage sources.                                                                                                                                                                  |
| attributes     | last_updated_by                | string   | UUID of the user who last updated the reference table.                                                                                                                                                                                                                     |
| attributes     | row_count                      | int64    | The number of successfully processed rows in the reference table.                                                                                                                                                                                                          |
| attributes     | schema                         | object   | Schema defining the structure and columns of the reference table.                                                                                                                                                                                                          |
| schema         | fields [*required*]       | [object] | The schema fields.                                                                                                                                                                                                                                                         |
| fields         | name [*required*]         | string   | The field name.                                                                                                                                                                                                                                                            |
| fields         | type [*required*]         | enum     | The field type for reference table schema fields. Allowed enum values: `STRING,INT32`                                                                                                                                                                                      |
| schema         | primary_keys [*required*] | [string] | List of field names that serve as primary keys for the table. Only one primary key is supported, and it is used as an ID to retrieve rows.                                                                                                                                 |
| attributes     | source                         | enum     | The source type for reference table data. Includes all possible source types that can appear in responses. Allowed enum values: `LOCAL_FILE,S3,GCS,AZURE,SERVICENOW,SALESFORCE,DATABRICKS,SNOWFLAKE`                                                                       |
| attributes     | status                         | string   | The processing status of the table.                                                                                                                                                                                                                                        |
| attributes     | table_name                     | string   | Unique name to identify this reference table. Used in enrichment processors and API calls.                                                                                                                                                                                 |
| attributes     | tags                           | [string] | Tags for organizing and filtering reference tables.                                                                                                                                                                                                                        |
| attributes     | updated_at                     | string   | When the reference table was last updated, in ISO 8601 format.                                                                                                                                                                                                             |
| data           | id                             | string   | Unique identifier for the reference table.                                                                                                                                                                                                                                 |
| data           | type [*required*]         | enum     | Reference table resource type. Allowed enum values: `reference_table`                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_by": "00000000-0000-0000-0000-000000000000",
        "description": "example description",
        "file_metadata": {
          "access_details": {},
          "error_message": "",
          "error_row_count": 0,
          "upload_id": "00000000-0000-0000-0000-000000000000"
        },
        "last_updated_by": "",
        "row_count": 5,
        "schema": {
          "fields": [
            {
              "name": "id",
              "type": "INT32"
            },
            {
              "name": "name",
              "type": "STRING"
            }
          ],
          "primary_keys": [
            "id"
          ]
        },
        "source": "LOCAL_FILE",
        "status": "DONE",
        "table_name": "test_reference_table",
        "tags": [
          "tag1",
          "tag2"
        ],
        "updated_at": "2000-01-01T01:00:00+00:00"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "reference_table"
    },
    {
      "attributes": {
        "created_by": "00000000-0000-0000-0000-000000000000",
        "description": "example description",
        "file_metadata": {
          "access_details": {
            "aws_detail": {
              "aws_account_id": "test-account-id",
              "aws_bucket_name": "test-bucket",
              "file_path": "test_rt.csv"
            }
          },
          "error_message": "",
          "error_row_count": 0,
          "sync_enabled": true
        },
        "last_updated_by": "00000000-0000-0000-0000-000000000000",
        "row_count": 5,
        "schema": {
          "fields": [
            {
              "name": "location",
              "type": "STRING"
            },
            {
              "name": "file_name",
              "type": "STRING"
            }
          ],
          "primary_keys": [
            "location"
          ]
        },
        "source": "S3",
        "status": "DONE",
        "table_name": "test_reference_table_2",
        "tags": [
          "test_tag1",
          "tag2",
          "3"
        ],
        "updated_at": "2000-01-01T01:00:00+00:00"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "reference_table"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List tables returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.list_tables()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List tables returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new
p api_instance.list_tables()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List tables returns "OK" response

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
	api := datadogV2.NewReferenceTablesApi(apiClient)
	resp, r, err := api.ListTables(ctx, *datadogV2.NewListTablesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.ListTables`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ReferenceTablesApi.ListTables`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List tables returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.TableResultV2Array;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    try {
      TableResultV2Array result = apiInstance.listTables();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#listTables");
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
// List tables returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ListTablesOptionalParams;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.list_tables(ListTablesOptionalParams::default()).await;
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
 * List tables returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

apiInstance
  .listTables()
  .then((data: v2.TableResultV2Array) => {
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

## Get table{% #get-table %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/reference-tables/tables/{id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/reference-tables/tables/{id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/reference-tables/tables/{id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/reference-tables/tables/{id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/reference-tables/tables/{id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/reference-tables/tables/{id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/reference-tables/tables/{id} |

### Overview

Get a reference table by ID

### Arguments

#### Path Parameters

| Name                 | Type   | Description                                          |
| -------------------- | ------ | ---------------------------------------------------- |
| id [*required*] | string | Unique identifier of the reference table to retrieve |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A reference table resource containing its full configuration and state.

| Parent field   | Field                          | Type     | Description                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data                           | object   | The data object containing the reference table configuration and state.                                                                                                                                                                                                    |
| data           | attributes                     | object   | Attributes that define the reference table's configuration and properties.                                                                                                                                                                                                 |
| attributes     | created_by                     | string   | UUID of the user who created the reference table.                                                                                                                                                                                                                          |
| attributes     | description                    | string   | Optional text describing the purpose or contents of this reference table.                                                                                                                                                                                                  |
| attributes     | file_metadata                  | object   | Metadata specifying where and how to access the reference table's data file.                                                                                                                                                                                               | For cloud storage tables (S3/GCS/Azure): | For local file tables: |
| file_metadata  | access_details                 | object   | Cloud storage access configuration. Only present for cloud storage sources (S3, GCS, Azure).                                                                                                                                                                               |
| access_details | aws_detail                     | object   | Amazon Web Services S3 storage access configuration.                                                                                                                                                                                                                       |
| aws_detail     | aws_account_id                 | string   | AWS account ID where the S3 bucket is located.                                                                                                                                                                                                                             |
| aws_detail     | aws_bucket_name                | string   | S3 bucket containing the CSV file.                                                                                                                                                                                                                                         |
| aws_detail     | file_path                      | string   | The relative file path from the S3 bucket root to the CSV file.                                                                                                                                                                                                            |
| access_details | azure_detail                   | object   | Azure Blob Storage access configuration.                                                                                                                                                                                                                                   |
| azure_detail   | azure_client_id                | string   | Azure service principal (application) client ID with permissions to read from the container.                                                                                                                                                                               |
| azure_detail   | azure_container_name           | string   | Azure Blob Storage container containing the CSV file.                                                                                                                                                                                                                      |
| azure_detail   | azure_storage_account_name     | string   | Azure storage account where the container is located.                                                                                                                                                                                                                      |
| azure_detail   | azure_tenant_id                | string   | Azure Active Directory tenant ID.                                                                                                                                                                                                                                          |
| azure_detail   | file_path                      | string   | The relative file path from the Azure container root to the CSV file.                                                                                                                                                                                                      |
| access_details | gcp_detail                     | object   | Google Cloud Platform storage access configuration.                                                                                                                                                                                                                        |
| gcp_detail     | file_path                      | string   | The relative file path from the GCS bucket root to the CSV file.                                                                                                                                                                                                           |
| gcp_detail     | gcp_bucket_name                | string   | GCP bucket containing the CSV file.                                                                                                                                                                                                                                        |
| gcp_detail     | gcp_project_id                 | string   | GCP project ID where the bucket is located.                                                                                                                                                                                                                                |
| gcp_detail     | gcp_service_account_email      | string   | Service account email with read permissions for the GCS bucket.                                                                                                                                                                                                            |
| file_metadata  | error_message                  | string   | The error message returned from the last operation (sync for cloud storage, upload for local file).                                                                                                                                                                        |
| file_metadata  | error_row_count                | int64    | The number of rows that failed to process.                                                                                                                                                                                                                                 |
| file_metadata  | error_type                     | enum     | The type of error that occurred during file processing. Only applicable for cloud storage sources. Allowed enum values: `TABLE_SCHEMA_ERROR,FILE_FORMAT_ERROR,CONFIGURATION_ERROR,QUOTA_EXCEEDED,CONFLICT_ERROR,VALIDATION_ERROR,STATE_ERROR,OPERATION_ERROR,SYSTEM_ERROR` |
| file_metadata  | sync_enabled                   | boolean  | Whether this table is synced automatically from cloud storage. Only applicable for cloud storage sources.                                                                                                                                                                  |
| attributes     | last_updated_by                | string   | UUID of the user who last updated the reference table.                                                                                                                                                                                                                     |
| attributes     | row_count                      | int64    | The number of successfully processed rows in the reference table.                                                                                                                                                                                                          |
| attributes     | schema                         | object   | Schema defining the structure and columns of the reference table.                                                                                                                                                                                                          |
| schema         | fields [*required*]       | [object] | The schema fields.                                                                                                                                                                                                                                                         |
| fields         | name [*required*]         | string   | The field name.                                                                                                                                                                                                                                                            |
| fields         | type [*required*]         | enum     | The field type for reference table schema fields. Allowed enum values: `STRING,INT32`                                                                                                                                                                                      |
| schema         | primary_keys [*required*] | [string] | List of field names that serve as primary keys for the table. Only one primary key is supported, and it is used as an ID to retrieve rows.                                                                                                                                 |
| attributes     | source                         | enum     | The source type for reference table data. Includes all possible source types that can appear in responses. Allowed enum values: `LOCAL_FILE,S3,GCS,AZURE,SERVICENOW,SALESFORCE,DATABRICKS,SNOWFLAKE`                                                                       |
| attributes     | status                         | string   | The processing status of the table.                                                                                                                                                                                                                                        |
| attributes     | table_name                     | string   | Unique name to identify this reference table. Used in enrichment processors and API calls.                                                                                                                                                                                 |
| attributes     | tags                           | [string] | Tags for organizing and filtering reference tables.                                                                                                                                                                                                                        |
| attributes     | updated_at                     | string   | When the reference table was last updated, in ISO 8601 format.                                                                                                                                                                                                             |
| data           | id                             | string   | Unique identifier for the reference table.                                                                                                                                                                                                                                 |
| data           | type [*required*]         | enum     | Reference table resource type. Allowed enum values: `reference_table`                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_by": "00000000-0000-0000-0000-000000000000",
      "description": "example description",
      "file_metadata": {
        "access_details": {
          "aws_detail": {
            "aws_account_id": "123456789000",
            "aws_bucket_name": "my-bucket",
            "file_path": "path/to/file.csv"
          }
        },
        "sync_enabled": true
      },
      "last_updated_by": "00000000-0000-0000-0000-000000000000",
      "row_count": 5,
      "schema": {
        "fields": [
          {
            "name": "id",
            "type": "INT32"
          },
          {
            "name": "name",
            "type": "STRING"
          }
        ],
        "primary_keys": [
          "id"
        ]
      },
      "source": "S3",
      "status": "DONE",
      "table_name": "test_reference_table",
      "tags": [
        "tag1",
        "tag2"
      ],
      "updated_at": "2000-01-01T01:00:00+00:00"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "reference_table"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get table returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.get_table(
        id="id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get table returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new
p api_instance.get_table("id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get table returns "OK" response

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
	api := datadogV2.NewReferenceTablesApi(apiClient)
	resp, r, err := api.GetTable(ctx, "id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.GetTable`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ReferenceTablesApi.GetTable`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get table returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.TableResultV2;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    try {
      TableResultV2 result = apiInstance.getTable("id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#getTable");
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
// Get table returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.get_table("id".to_string()).await;
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
 * Get table returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiGetTableRequest = {
  id: "id",
};

apiInstance
  .getTable(params)
  .then((data: v2.TableResultV2) => {
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

## Get rows by id{% #get-rows-by-id %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/reference-tables/tables/{id}/rows      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/reference-tables/tables/{id}/rows      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/reference-tables/tables/{id}/rows     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |

### Overview

Get reference table rows by their primary key values.

### Arguments

#### Path Parameters

| Name                 | Type   | Description                                               |
| -------------------- | ------ | --------------------------------------------------------- |
| id [*required*] | string | Unique identifier of the reference table to get rows from |

#### Query Strings

| Name                     | Type  | Description                                                                |
| ------------------------ | ----- | -------------------------------------------------------------------------- |
| row_id [*required*] | array | List of row IDs (primary key values) to retrieve from the reference table. |

### Response

{% tab title="200" %}
Some or all requested rows were found.
{% tab title="Model" %}
List of rows from a reference table query.

| Parent field | Field                  | Type     | Description                                                                            |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------- |
|              | data [*required*] | [object] | The rows.                                                                              |
| data         | attributes             | object   | Column values for this row in the reference table.                                     |
| attributes   | values                 | object   | Key-value pairs representing the row data, where keys are field names from the schema. |
| data         | id                     | string   | Row identifier, corresponding to the primary key value.                                |
| data         | type [*required*] | enum     | Row resource type. Allowed enum values: `row`                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "values": {}
      },
      "id": "string",
      "type": "row"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Path parametersexport id="table-123"\# Required query argumentsexport row_id_0="row_id_0"export row_id_1="row_id_1"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables/${id}/rows?row_id=${row_id_0}&row_id=${row_id_1}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get rows by id returns "Some or all requested rows were found." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.get_rows_by_id(
        id="id",
        row_id=[],
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get rows by id returns "Some or all requested rows were found." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new
p api_instance.get_rows_by_id("id", [])
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get rows by id returns "Some or all requested rows were found." response

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
	api := datadogV2.NewReferenceTablesApi(apiClient)
	resp, r, err := api.GetRowsByID(ctx, "id", []string{})

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.GetRowsByID`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ReferenceTablesApi.GetRowsByID`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get rows by id returns "Some or all requested rows were found." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.TableRowResourceArray;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    try {
      TableRowResourceArray result =
          apiInstance.getRowsByID("table-123", Arrays.asList("row1", "row2"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#getRowsByID");
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
// Get rows by id returns "Some or all requested rows were found." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.get_rows_by_id("id".to_string(), vec![]).await;
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
 * Get rows by id returns "Some or all requested rows were found." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiGetRowsByIDRequest = {
  id: "id",
  rowId: [],
};

apiInstance
  .getRowsByID(params)
  .then((data: v2.TableRowResourceArray) => {
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

## Update reference table{% #update-reference-table %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/reference-tables/tables/{id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/reference-tables/tables/{id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/reference-tables/tables/{id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/reference-tables/tables/{id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/reference-tables/tables/{id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/reference-tables/tables/{id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/reference-tables/tables/{id} |

### Overview

Update a reference table by ID. You can update the table's data, description, and tags. Note: The source type cannot be changed after table creation. For data updates: For existing tables of type `source:LOCAL_FILE`, call POST api/v2/reference-tables/uploads first to get an upload ID, then PUT chunks of CSV data to each provided URL, and finally call this PATCH endpoint with the upload_id in file_metadata. For existing tables with `source:` types of `S3`, `GCS`, or `AZURE`, provide updated access_details in file_metadata pointing to a CSV file in the same type of cloud storage.

### Arguments

#### Path Parameters

| Name                 | Type   | Description                                        |
| -------------------- | ------ | -------------------------------------------------- |
| id [*required*] | string | Unique identifier of the reference table to update |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field   | Field                          | Type          | Description                                                                                                                                                                                     |
| -------------- | ------------------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data                           | object        | The data object containing the partial table definition updates.                                                                                                                                |
| data           | attributes                     | object        | Attributes that define the updates to the reference table's configuration and properties.                                                                                                       |
| attributes     | description                    | string        | Optional text describing the purpose or contents of this reference table.                                                                                                                       |
| attributes     | file_metadata                  |  <oneOf> | Metadata specifying where and how to access the reference table's data file.                                                                                                                    |
| file_metadata  | Option 1                       | object        | Cloud storage file metadata for patch requests. Allows partial updates of access_details and sync_enabled.                                                                                      |
| Option 1       | access_details                 | object        | Cloud storage access configuration for the reference table data file.                                                                                                                           |
| access_details | aws_detail                     | object        | Amazon Web Services S3 storage access configuration.                                                                                                                                            |
| aws_detail     | aws_account_id                 | string        | AWS account ID where the S3 bucket is located.                                                                                                                                                  |
| aws_detail     | aws_bucket_name                | string        | S3 bucket containing the CSV file.                                                                                                                                                              |
| aws_detail     | file_path                      | string        | The relative file path from the S3 bucket root to the CSV file.                                                                                                                                 |
| access_details | azure_detail                   | object        | Azure Blob Storage access configuration.                                                                                                                                                        |
| azure_detail   | azure_client_id                | string        | Azure service principal (application) client ID with permissions to read from the container.                                                                                                    |
| azure_detail   | azure_container_name           | string        | Azure Blob Storage container containing the CSV file.                                                                                                                                           |
| azure_detail   | azure_storage_account_name     | string        | Azure storage account where the container is located.                                                                                                                                           |
| azure_detail   | azure_tenant_id                | string        | Azure Active Directory tenant ID.                                                                                                                                                               |
| azure_detail   | file_path                      | string        | The relative file path from the Azure container root to the CSV file.                                                                                                                           |
| access_details | gcp_detail                     | object        | Google Cloud Platform storage access configuration.                                                                                                                                             |
| gcp_detail     | file_path                      | string        | The relative file path from the GCS bucket root to the CSV file.                                                                                                                                |
| gcp_detail     | gcp_bucket_name                | string        | GCP bucket containing the CSV file.                                                                                                                                                             |
| gcp_detail     | gcp_project_id                 | string        | GCP project ID where the bucket is located.                                                                                                                                                     |
| gcp_detail     | gcp_service_account_email      | string        | Service account email with read permissions for the GCS bucket.                                                                                                                                 |
| Option 1       | sync_enabled                   | boolean       | Whether this table is synced automatically.                                                                                                                                                     |
| file_metadata  | Option 2                       | object        | Local file metadata for patch requests using upload ID.                                                                                                                                         |
| Option 2       | upload_id [*required*]    | string        | The upload ID.                                                                                                                                                                                  |
| attributes     | schema                         | object        | Schema defining the updates to the structure and columns of the reference table. Schema fields cannot be deleted or renamed.                                                                    |
| schema         | fields [*required*]       | [object]      | The schema fields.                                                                                                                                                                              |
| fields         | name [*required*]         | string        | The field name.                                                                                                                                                                                 |
| fields         | type [*required*]         | enum          | The field type for reference table schema fields. Allowed enum values: `STRING,INT32`                                                                                                           |
| schema         | primary_keys [*required*] | [string]      | List of field names that serve as primary keys for the table. Only one primary key is supported, and it is used as an ID to retrieve rows. Primary keys cannot be changed after table creation. |
| attributes     | tags                           | [string]      | Tags for organizing and filtering reference tables.                                                                                                                                             |
| data           | type [*required*]         | enum          | Reference table resource type. Allowed enum values: `reference_table`                                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "example description",
      "file_metadata": {
        "access_details": {
          "aws_detail": {
            "aws_account_id": "123456789000",
            "aws_bucket_name": "example-data-bucket",
            "file_path": "reference-tables/users.csv"
          },
          "azure_detail": {
            "azure_client_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
            "azure_container_name": "reference-data",
            "azure_storage_account_name": "examplestorageaccount",
            "azure_tenant_id": "cccccccc-4444-5555-6666-dddddddddddd",
            "file_path": "tables/users.csv"
          },
          "gcp_detail": {
            "file_path": "data/reference_tables/users.csv",
            "gcp_bucket_name": "example-data-bucket",
            "gcp_project_id": "example-gcp-project-12345",
            "gcp_service_account_email": "example-service@example-gcp-project-12345.iam.gserviceaccount.com"
          }
        },
        "sync_enabled": false
      },
      "schema": {
        "fields": [
          {
            "name": "field_1",
            "type": "STRING"
          }
        ],
        "primary_keys": [
          "field_1"
        ]
      },
      "tags": [
        "tag_1",
        "tag_2"
      ]
    },
    "type": "reference_table"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
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
Forbidden
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
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "schema": {
        "fields": [
          {
            "name": "field_1",
            "type": "STRING"
          }
        ],
        "primary_keys": [
          "field_1"
        ]
      }
    },
    "type": "reference_table"
  }
}
EOF
                
##### 

```python
"""
Update reference table returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.patch_table_request import PatchTableRequest
from datadog_api_client.v2.model.patch_table_request_data import PatchTableRequestData
from datadog_api_client.v2.model.patch_table_request_data_attributes import PatchTableRequestDataAttributes
from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_cloud_storage import (
    PatchTableRequestDataAttributesFileMetadataCloudStorage,
)
from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details import (
    PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails,
)
from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
    PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
)
from datadog_api_client.v2.model.patch_table_request_data_attributes_schema import PatchTableRequestDataAttributesSchema
from datadog_api_client.v2.model.patch_table_request_data_attributes_schema_fields_items import (
    PatchTableRequestDataAttributesSchemaFieldsItems,
)
from datadog_api_client.v2.model.patch_table_request_data_type import PatchTableRequestDataType
from datadog_api_client.v2.model.reference_table_schema_field_type import ReferenceTableSchemaFieldType

body = PatchTableRequest(
    data=PatchTableRequestData(
        attributes=PatchTableRequestDataAttributes(
            description="this is a cloud table generated via a cloud bucket sync",
            file_metadata=PatchTableRequestDataAttributesFileMetadataCloudStorage(
                access_details=PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails(
                    aws_detail=PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail(
                        aws_account_id="test-account-id",
                        aws_bucket_name="test-bucket",
                        file_path="test_rt.csv",
                    ),
                ),
                sync_enabled=True,
            ),
            schema=PatchTableRequestDataAttributesSchema(
                fields=[
                    PatchTableRequestDataAttributesSchemaFieldsItems(
                        name="id",
                        type=ReferenceTableSchemaFieldType.INT32,
                    ),
                    PatchTableRequestDataAttributesSchemaFieldsItems(
                        name="name",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                ],
                primary_keys=[
                    "id",
                ],
            ),
            sync_enabled=False,
            tags=[
                "test_tag",
            ],
        ),
        type=PatchTableRequestDataType.REFERENCE_TABLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    api_instance.update_reference_table(id="id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update reference table returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new

body = DatadogAPIClient::V2::PatchTableRequest.new({
  data: DatadogAPIClient::V2::PatchTableRequestData.new({
    attributes: DatadogAPIClient::V2::PatchTableRequestDataAttributes.new({
      description: "this is a cloud table generated via a cloud bucket sync",
      file_metadata: DatadogAPIClient::V2::PatchTableRequestDataAttributesFileMetadataCloudStorage.new({
        access_details: DatadogAPIClient::V2::PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails.new({
          aws_detail: DatadogAPIClient::V2::PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail.new({
            aws_account_id: "test-account-id",
            aws_bucket_name: "test-bucket",
            file_path: "test_rt.csv",
          }),
        }),
        sync_enabled: true,
      }),
      schema: DatadogAPIClient::V2::PatchTableRequestDataAttributesSchema.new({
        fields: [
          DatadogAPIClient::V2::PatchTableRequestDataAttributesSchemaFieldsItems.new({
            name: "id",
            type: DatadogAPIClient::V2::ReferenceTableSchemaFieldType::INT32,
          }),
          DatadogAPIClient::V2::PatchTableRequestDataAttributesSchemaFieldsItems.new({
            name: "name",
            type: DatadogAPIClient::V2::ReferenceTableSchemaFieldType::STRING,
          }),
        ],
        primary_keys: [
          "id",
        ],
      }),
      sync_enabled: false,
      tags: [
        "test_tag",
      ],
    }),
    type: DatadogAPIClient::V2::PatchTableRequestDataType::REFERENCE_TABLE,
  }),
})
p api_instance.update_reference_table("id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Update reference table returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.PatchTableRequest{
		Data: &datadogV2.PatchTableRequestData{
			Attributes: &datadogV2.PatchTableRequestDataAttributes{
				Description: datadog.PtrString("this is a cloud table generated via a cloud bucket sync"),
				FileMetadata: &datadogV2.PatchTableRequestDataAttributesFileMetadata{
					PatchTableRequestDataAttributesFileMetadataCloudStorage: &datadogV2.PatchTableRequestDataAttributesFileMetadataCloudStorage{
						AccessDetails: &datadogV2.PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails{
							AwsDetail: &datadogV2.PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail{
								AwsAccountId:  datadog.PtrString("test-account-id"),
								AwsBucketName: datadog.PtrString("test-bucket"),
								FilePath:      datadog.PtrString("test_rt.csv"),
							},
						},
						SyncEnabled: datadog.PtrBool(true),
					}},
				Schema: &datadogV2.PatchTableRequestDataAttributesSchema{
					Fields: []datadogV2.PatchTableRequestDataAttributesSchemaFieldsItems{
						{
							Name: "id",
							Type: datadogV2.REFERENCETABLESCHEMAFIELDTYPE_INT32,
						},
						{
							Name: "name",
							Type: datadogV2.REFERENCETABLESCHEMAFIELDTYPE_STRING,
						},
					},
					PrimaryKeys: []string{
						"id",
					},
				},
				SyncEnabled: datadog.PtrBool(false),
				Tags: []string{
					"test_tag",
				},
			},
			Type: datadogV2.PATCHTABLEREQUESTDATATYPE_REFERENCE_TABLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewReferenceTablesApi(apiClient)
	r, err := api.UpdateReferenceTable(ctx, "id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.UpdateReferenceTable`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update reference table returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.PatchTableRequest;
import com.datadog.api.client.v2.model.PatchTableRequestData;
import com.datadog.api.client.v2.model.PatchTableRequestDataAttributes;
import com.datadog.api.client.v2.model.PatchTableRequestDataAttributesFileMetadata;
import com.datadog.api.client.v2.model.PatchTableRequestDataAttributesFileMetadataCloudStorage;
import com.datadog.api.client.v2.model.PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails;
import com.datadog.api.client.v2.model.PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail;
import com.datadog.api.client.v2.model.PatchTableRequestDataAttributesSchema;
import com.datadog.api.client.v2.model.PatchTableRequestDataAttributesSchemaFieldsItems;
import com.datadog.api.client.v2.model.PatchTableRequestDataType;
import com.datadog.api.client.v2.model.ReferenceTableSchemaFieldType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    PatchTableRequest body =
        new PatchTableRequest()
            .data(
                new PatchTableRequestData()
                    .attributes(
                        new PatchTableRequestDataAttributes()
                            .description("this is a cloud table generated via a cloud bucket sync")
                            .fileMetadata(
                                new PatchTableRequestDataAttributesFileMetadata(
                                    new PatchTableRequestDataAttributesFileMetadataCloudStorage()
                                        .accessDetails(
                                            new PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails()
                                                .awsDetail(
                                                    new PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail()
                                                        .awsAccountId("test-account-id")
                                                        .awsBucketName("test-bucket")
                                                        .filePath("test_rt.csv")))
                                        .syncEnabled(true)))
                            .schema(
                                new PatchTableRequestDataAttributesSchema()
                                    .fields(
                                        Arrays.asList(
                                            new PatchTableRequestDataAttributesSchemaFieldsItems()
                                                .name("id")
                                                .type(ReferenceTableSchemaFieldType.INT32),
                                            new PatchTableRequestDataAttributesSchemaFieldsItems()
                                                .name("name")
                                                .type(ReferenceTableSchemaFieldType.STRING)))
                                    .primaryKeys(Collections.singletonList("id")))
                            .syncEnabled(false)
                            .tags(Collections.singletonList("test_tag")))
                    .type(PatchTableRequestDataType.REFERENCE_TABLE));

    try {
      apiInstance.updateReferenceTable("id", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#updateReferenceTable");
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
// Update reference table returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;
use datadog_api_client::datadogV2::model::PatchTableRequest;
use datadog_api_client::datadogV2::model::PatchTableRequestData;
use datadog_api_client::datadogV2::model::PatchTableRequestDataAttributes;
use datadog_api_client::datadogV2::model::PatchTableRequestDataAttributesFileMetadata;
use datadog_api_client::datadogV2::model::PatchTableRequestDataAttributesFileMetadataCloudStorage;
use datadog_api_client::datadogV2::model::PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails;
use datadog_api_client::datadogV2::model::PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail;
use datadog_api_client::datadogV2::model::PatchTableRequestDataAttributesSchema;
use datadog_api_client::datadogV2::model::PatchTableRequestDataAttributesSchemaFieldsItems;
use datadog_api_client::datadogV2::model::PatchTableRequestDataType;
use datadog_api_client::datadogV2::model::ReferenceTableSchemaFieldType;

#[tokio::main]
async fn main() {
    let body =
        PatchTableRequest
        ::new().data(
            PatchTableRequestData::new(
                PatchTableRequestDataType::REFERENCE_TABLE,
            ).attributes(
                PatchTableRequestDataAttributes::new()
                    .description("this is a cloud table generated via a cloud bucket sync".to_string())
                    .file_metadata(
                        PatchTableRequestDataAttributesFileMetadata
                        ::PatchTableRequestDataAttributesFileMetadataCloudStorage(
                            Box::new(
                                PatchTableRequestDataAttributesFileMetadataCloudStorage::new()
                                    .access_details(
                                        PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails
                                        ::new().aws_detail(
                                            PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail
                                            ::new()
                                                .aws_account_id("test-account-id".to_string())
                                                .aws_bucket_name("test-bucket".to_string())
                                                .file_path("test_rt.csv".to_string()),
                                        ),
                                    )
                                    .sync_enabled(true),
                            ),
                        ),
                    )
                    .schema(
                        PatchTableRequestDataAttributesSchema::new(
                            vec![
                                PatchTableRequestDataAttributesSchemaFieldsItems::new(
                                    "id".to_string(),
                                    ReferenceTableSchemaFieldType::INT32,
                                ),
                                PatchTableRequestDataAttributesSchemaFieldsItems::new(
                                    "name".to_string(),
                                    ReferenceTableSchemaFieldType::STRING,
                                )
                            ],
                            vec!["id".to_string()],
                        ),
                    )
                    .sync_enabled(false)
                    .tags(vec!["test_tag".to_string()]),
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.update_reference_table("id".to_string(), body).await;
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
 * Update reference table returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiUpdateReferenceTableRequest = {
  body: {
    data: {
      attributes: {
        description: "this is a cloud table generated via a cloud bucket sync",
        fileMetadata: {
          accessDetails: {
            awsDetail: {
              awsAccountId: "test-account-id",
              awsBucketName: "test-bucket",
              filePath: "test_rt.csv",
            },
          },
          syncEnabled: true,
        },
        schema: {
          fields: [
            {
              name: "id",
              type: "INT32",
            },
            {
              name: "name",
              type: "STRING",
            },
          ],
          primaryKeys: ["id"],
        },
        syncEnabled: false,
        tags: ["test_tag"],
      },
      type: "reference_table",
    },
  },
  id: "id",
};

apiInstance
  .updateReferenceTable(params)
  .then((data: any) => {
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

## Delete table{% #delete-table %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/reference-tables/tables/{id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/reference-tables/tables/{id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/reference-tables/tables/{id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/reference-tables/tables/{id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/reference-tables/tables/{id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/reference-tables/tables/{id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/reference-tables/tables/{id} |

### Overview

Delete a reference table by ID

### Arguments

#### Path Parameters

| Name                 | Type   | Description                                        |
| -------------------- | ------ | -------------------------------------------------- |
| id [*required*] | string | Unique identifier of the reference table to delete |

### Response

{% tab title="200" %}
OK
{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete table returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    api_instance.delete_table(
        id="id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete table returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new
p api_instance.delete_table("id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete table returns "OK" response

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
	api := datadogV2.NewReferenceTablesApi(apiClient)
	r, err := api.DeleteTable(ctx, "id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.DeleteTable`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete table returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    try {
      apiInstance.deleteTable("id");
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#deleteTable");
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
// Delete table returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.delete_table("id".to_string()).await;
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
 * Delete table returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiDeleteTableRequest = {
  id: "id",
};

apiInstance
  .deleteTable(params)
  .then((data: any) => {
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

## Upsert rows{% #upsert-rows %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/reference-tables/tables/{id}/rows      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/reference-tables/tables/{id}/rows      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/reference-tables/tables/{id}/rows     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |

### Overview

Create or update rows in a Reference Table by their primary key values. If a row with the specified primary key exists, it is updated; otherwise, a new row is created.

### Arguments

#### Path Parameters

| Name                 | Type   | Description                                                  |
| -------------------- | ------ | ------------------------------------------------------------ |
| id [*required*] | string | Unique identifier of the reference table to upsert rows into |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field         | Field                    | Type          | Description                                                                                                               |
| -------------------- | ------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------- |
|                      | data [*required*]   | [object]      |
| data                 | attributes               | object        | Attributes containing row data values for row creation or update operations.                                              |
| attributes           | values [*required*] | object        | Key-value pairs representing row data, where keys are schema field names and values match the corresponding column types. |
| additionalProperties | <any-key>                |  <oneOf> | Types allowed for Reference Table row values.                                                                             |
| <any-key>            | Option 1                 | string        |
| <any-key>            | Option 2                 | int32         |
| data                 | id [*required*]     | string        |
| data                 | type [*required*]   | enum          | Row resource type. Allowed enum values: `row`                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "values": {
          "<any-key>": {
            "example": "undefined",
            "type": "undefined"
          }
        }
      },
      "id": "primary_key_value",
      "type": "row"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
Rows created or updated successfully
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
Forbidden
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

{% tab title="500" %}
Internal Server Error
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
                  \## Upsert a row with mixed string and int values
# 
\# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables/${id}/rows" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "attributes": {
        "values": {
          "age": 25,
          "example_key_value": "primary_key_value",
          "name": "row_name"
        }
      },
      "id": "primary_key_value",
      "type": "row"
    }
  ]
}
EOF
                
##### 

```python
"""
Upsert rows returns "Rows created or updated successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.batch_upsert_rows_request_array import BatchUpsertRowsRequestArray
from datadog_api_client.v2.model.batch_upsert_rows_request_data import BatchUpsertRowsRequestData
from datadog_api_client.v2.model.batch_upsert_rows_request_data_attributes import BatchUpsertRowsRequestDataAttributes
from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType

body = BatchUpsertRowsRequestArray(
    data=[
        BatchUpsertRowsRequestData(
            attributes=BatchUpsertRowsRequestDataAttributes(
                values=dict(
                    example_key_value="primary_key_value",
                    name="row_name",
                ),
            ),
            id="primary_key_value",
            type=TableRowResourceDataType.ROW,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    api_instance.upsert_rows(id="id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Upsert rows returns "Rows created or updated successfully" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new

body = DatadogAPIClient::V2::BatchUpsertRowsRequestArray.new({
  data: [
    DatadogAPIClient::V2::BatchUpsertRowsRequestData.new({
      attributes: DatadogAPIClient::V2::BatchUpsertRowsRequestDataAttributes.new({
        values: {
          example_key_value: "primary_key_value", name: "row_name",
        },
      }),
      id: "primary_key_value",
      type: DatadogAPIClient::V2::TableRowResourceDataType::ROW,
    }),
  ],
})
p api_instance.upsert_rows("id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Upsert rows returns "Rows created or updated successfully" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.BatchUpsertRowsRequestArray{
		Data: []datadogV2.BatchUpsertRowsRequestData{
			{
				Attributes: &datadogV2.BatchUpsertRowsRequestDataAttributes{
					Values: map[string]interface{}{
						"example_key_value": "primary_key_value",
						"name":              "row_name",
					},
				},
				Id:   "primary_key_value",
				Type: datadogV2.TABLEROWRESOURCEDATATYPE_ROW,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewReferenceTablesApi(apiClient)
	r, err := api.UpsertRows(ctx, "id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.UpsertRows`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Upsert rows returns "Rows created or updated successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.BatchUpsertRowsRequestArray;
import com.datadog.api.client.v2.model.BatchUpsertRowsRequestData;
import com.datadog.api.client.v2.model.BatchUpsertRowsRequestDataAttributes;
import com.datadog.api.client.v2.model.TableRowResourceDataType;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    BatchUpsertRowsRequestArray body =
        new BatchUpsertRowsRequestArray()
            .data(
                Collections.singletonList(
                    new BatchUpsertRowsRequestData()
                        .attributes(
                            new BatchUpsertRowsRequestDataAttributes()
                                .values(
                                    Map.ofEntries(
                                        Map.entry("example_key_value", "primary_key_value"),
                                        Map.entry("name", "row_name"))))
                        .id("primary_key_value")
                        .type(TableRowResourceDataType.ROW)));

    try {
      apiInstance.upsertRows("id", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#upsertRows");
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
// Upsert rows returns "Rows created or updated successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;
use datadog_api_client::datadogV2::model::BatchUpsertRowsRequestArray;
use datadog_api_client::datadogV2::model::BatchUpsertRowsRequestData;
use datadog_api_client::datadogV2::model::BatchUpsertRowsRequestDataAttributes;
use datadog_api_client::datadogV2::model::TableRowResourceDataType;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = BatchUpsertRowsRequestArray::new(vec![BatchUpsertRowsRequestData::new(
        "primary_key_value".to_string(),
        TableRowResourceDataType::ROW,
    )
    .attributes(BatchUpsertRowsRequestDataAttributes::new(BTreeMap::from([
        (
            "example_key_value".to_string(),
            Value::from("primary_key_value"),
        ),
        ("name".to_string(), Value::from("row_name")),
    ])))]);
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.upsert_rows("id".to_string(), body).await;
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
 * Upsert rows returns "Rows created or updated successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiUpsertRowsRequest = {
  body: {
    data: [
      {
        attributes: {
          values: {
            example_key_value: "primary_key_value",
            name: "row_name",
          },
        },
        id: "primary_key_value",
        type: "row",
      },
    ],
  },
  id: "id",
};

apiInstance
  .upsertRows(params)
  .then((data: any) => {
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

## Delete rows{% #delete-rows %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/reference-tables/tables/{id}/rows      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/reference-tables/tables/{id}/rows      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/reference-tables/tables/{id}/rows     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/reference-tables/tables/{id}/rows |

### Overview

Delete multiple rows from a Reference Table by their primary key values.

### Arguments

#### Path Parameters

| Name                 | Type   | Description                                                  |
| -------------------- | ------ | ------------------------------------------------------------ |
| id [*required*] | string | Unique identifier of the reference table to delete rows from |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                   |
| ------------ | ---------------------- | -------- | --------------------------------------------- |
|              | data [*required*] | [object] |
| data         | id [*required*]   | string   |
| data         | type [*required*] | enum     | Row resource type. Allowed enum values: `row` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "primary_key_value",
      "type": "row"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
Rows deleted successfully
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
Forbidden
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

{% tab title="500" %}
Internal Server Error
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
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/reference-tables/tables/${id}/rows" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "id": "primary_key_value",
      "type": "row"
    }
  ]
}
EOF
                
##### 

```python
"""
Delete rows returns "Rows deleted successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.batch_delete_rows_request_array import BatchDeleteRowsRequestArray
from datadog_api_client.v2.model.batch_delete_rows_request_data import BatchDeleteRowsRequestData
from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType

body = BatchDeleteRowsRequestArray(
    data=[
        BatchDeleteRowsRequestData(
            id="primary_key_value",
            type=TableRowResourceDataType.ROW,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    api_instance.delete_rows(id="id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete rows returns "Rows deleted successfully" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ReferenceTablesAPI.new

body = DatadogAPIClient::V2::BatchDeleteRowsRequestArray.new({
  data: [
    DatadogAPIClient::V2::BatchDeleteRowsRequestData.new({
      id: "primary_key_value",
      type: DatadogAPIClient::V2::TableRowResourceDataType::ROW,
    }),
  ],
})
p api_instance.delete_rows("id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete rows returns "Rows deleted successfully" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.BatchDeleteRowsRequestArray{
		Data: []datadogV2.BatchDeleteRowsRequestData{
			{
				Id:   "primary_key_value",
				Type: datadogV2.TABLEROWRESOURCEDATATYPE_ROW,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewReferenceTablesApi(apiClient)
	r, err := api.DeleteRows(ctx, "id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReferenceTablesApi.DeleteRows`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete rows returns "Rows deleted successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ReferenceTablesApi;
import com.datadog.api.client.v2.model.BatchDeleteRowsRequestArray;
import com.datadog.api.client.v2.model.BatchDeleteRowsRequestData;
import com.datadog.api.client.v2.model.TableRowResourceDataType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ReferenceTablesApi apiInstance = new ReferenceTablesApi(defaultClient);

    BatchDeleteRowsRequestArray body =
        new BatchDeleteRowsRequestArray()
            .data(
                Collections.singletonList(
                    new BatchDeleteRowsRequestData()
                        .id("primary_key_value")
                        .type(TableRowResourceDataType.ROW)));

    try {
      apiInstance.deleteRows("id", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceTablesApi#deleteRows");
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
// Delete rows returns "Rows deleted successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_reference_tables::ReferenceTablesAPI;
use datadog_api_client::datadogV2::model::BatchDeleteRowsRequestArray;
use datadog_api_client::datadogV2::model::BatchDeleteRowsRequestData;
use datadog_api_client::datadogV2::model::TableRowResourceDataType;

#[tokio::main]
async fn main() {
    let body = BatchDeleteRowsRequestArray::new(vec![BatchDeleteRowsRequestData::new(
        "primary_key_value".to_string(),
        TableRowResourceDataType::ROW,
    )]);
    let configuration = datadog::Configuration::new();
    let api = ReferenceTablesAPI::with_config(configuration);
    let resp = api.delete_rows("id".to_string(), body).await;
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
 * Delete rows returns "Rows deleted successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ReferenceTablesApi(configuration);

const params: v2.ReferenceTablesApiDeleteRowsRequest = {
  body: {
    data: [
      {
        id: "primary_key_value",
        type: "row",
      },
    ],
  },
  id: "id",
};

apiInstance
  .deleteRows(params)
  .then((data: any) => {
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
