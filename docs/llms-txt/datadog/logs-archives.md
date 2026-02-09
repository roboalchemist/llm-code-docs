# Source: https://docs.datadoghq.com/api/latest/logs-archives.md

---
title: Logs Archives
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Logs Archives
---

# Logs Archives

Archives forward all the logs ingested to a cloud storage system.

See the [Archives Page](https://app.datadoghq.com/logs/pipelines/archives) for a list of the archives currently configured in Datadog.

## Get all archives{% #get-all-archives %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/archives |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/archives |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/archives      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/archives      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/archives     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/archives |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/archives |

### Overview

Get the list of configured logs archives with their definitions. This endpoint requires the `logs_read_archives` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The available archives.

| Parent field | Field                             | Type                | Description                                                                                                                                      |
| ------------ | --------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                              | [object]            | A list of archives.                                                                                                                              |
| data         | attributes                        | object              | The attributes associated with the archive.                                                                                                      |
| attributes   | destination [*required*]     | object <oneOf> | An archive's destination.                                                                                                                        |
| destination  | Option 1                          | object              | The Azure archive destination.                                                                                                                   |
| Option 1     | container [*required*]       | string              | The container where the archive will be stored.                                                                                                  |
| Option 1     | integration [*required*]     | object              | The Azure archive's integration destination.                                                                                                     |
| integration  | client_id [*required*]       | string              | A client ID.                                                                                                                                     |
| integration  | tenant_id [*required*]       | string              | A tenant ID.                                                                                                                                     |
| Option 1     | path                              | string              | The archive path.                                                                                                                                |
| Option 1     | region                            | string              | The region where the archive will be stored.                                                                                                     |
| Option 1     | storage_account [*required*] | string              | The associated storage account.                                                                                                                  |
| Option 1     | type [*required*]            | enum                | Type of the Azure archive destination. Allowed enum values: `azure`                                                                              |
| destination  | Option 2                          | object              | The GCS archive destination.                                                                                                                     |
| Option 2     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 2     | integration [*required*]     | object              | The GCS archive's integration destination.                                                                                                       |
| integration  | client_email [*required*]    | string              | A client email.                                                                                                                                  |
| integration  | project_id                        | string              | A project ID.                                                                                                                                    |
| Option 2     | path                              | string              | The archive path.                                                                                                                                |
| Option 2     | type [*required*]            | enum                | Type of the GCS archive destination. Allowed enum values: `gcs`                                                                                  |
| destination  | Option 3                          | object              | The S3 archive destination.                                                                                                                      |
| Option 3     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 3     | encryption                        | object              | The S3 encryption settings.                                                                                                                      |
| encryption   | key                               | string              | An Amazon Resource Name (ARN) used to identify an AWS KMS key.                                                                                   |
| encryption   | type [*required*]            | enum                | Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`                                                       |
| Option 3     | integration [*required*]     | object              | The S3 Archive's integration destination.                                                                                                        |
| integration  | account_id [*required*]      | string              | The account ID for the integration.                                                                                                              |
| integration  | role_name [*required*]       | string              | The path of the integration.                                                                                                                     |
| Option 3     | path                              | string              | The archive path.                                                                                                                                |
| Option 3     | storage_class                     | enum                | The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`        |
| Option 3     | type [*required*]            | enum                | Type of the S3 archive destination. Allowed enum values: `s3`                                                                                    |
| attributes   | include_tags                      | boolean             | To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive. |
| attributes   | name [*required*]            | string              | The archive name.                                                                                                                                |
| attributes   | query [*required*]           | string              | The archive query/filter. Logs matching this query are included in the archive.                                                                  |
| attributes   | rehydration_max_scan_size_in_gb   | int64               | Maximum scan size for rehydration from this archive.                                                                                             |
| attributes   | rehydration_tags                  | [string]            | An array of tags to add to rehydrated logs from an archive.                                                                                      |
| attributes   | state                             | enum                | The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`                                                     |
| data         | id                                | string              | The archive ID.                                                                                                                                  |
| data         | type [*required*]            | string              | The type of the resource. The value should always be archives.                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "destination": {
          "container": "container-name",
          "integration": {
            "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
            "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
          },
          "path": "string",
          "region": "string",
          "storage_account": "account-name",
          "type": "azure"
        },
        "include_tags": false,
        "name": "Nginx Archive",
        "query": "source:nginx",
        "rehydration_max_scan_size_in_gb": 100,
        "rehydration_tags": [
          "team:intake",
          "team:app"
        ],
        "state": "WORKING"
      },
      "id": "a2zcMylnM4OCHpYusxIi3g",
      "type": "archives"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all archives returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.list_logs_archives()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all archives returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.list_logs_archives()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all archives returns "OK" response

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
	api := datadogV2.NewLogsArchivesApi(apiClient)
	resp, r, err := api.ListLogsArchives(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.ListLogsArchives`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsArchivesApi.ListLogsArchives`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all archives returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.LogsArchives;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    try {
      LogsArchives result = apiInstance.listLogsArchives();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#listLogsArchives");
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
// Get all archives returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api.list_logs_archives().await;
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
 * Get all archives returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

apiInstance
  .listLogsArchives()
  .then((data: v2.LogsArchives) => {
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

## Create an archive{% #create-an-archive %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/config/archives |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/config/archives |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/config/archives      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/config/archives      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/config/archives     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/config/archives |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/config/archives |

### Overview

Create an archive in your organization. This endpoint requires the `logs_write_archives` permission.

### Request

#### Body Data (required)

The definition of the new archive.

{% tab title="Model" %}

| Parent field | Field                             | Type          | Description                                                                                                                                      |
| ------------ | --------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                              | object        | The definition of an archive.                                                                                                                    |
| data         | attributes                        | object        | The attributes associated with the archive.                                                                                                      |
| attributes   | destination [*required*]     |  <oneOf> | An archive's destination.                                                                                                                        |
| destination  | Option 1                          | object        | The Azure archive destination.                                                                                                                   |
| Option 1     | container [*required*]       | string        | The container where the archive will be stored.                                                                                                  |
| Option 1     | integration [*required*]     | object        | The Azure archive's integration destination.                                                                                                     |
| integration  | client_id [*required*]       | string        | A client ID.                                                                                                                                     |
| integration  | tenant_id [*required*]       | string        | A tenant ID.                                                                                                                                     |
| Option 1     | path                              | string        | The archive path.                                                                                                                                |
| Option 1     | region                            | string        | The region where the archive will be stored.                                                                                                     |
| Option 1     | storage_account [*required*] | string        | The associated storage account.                                                                                                                  |
| Option 1     | type [*required*]            | enum          | Type of the Azure archive destination. Allowed enum values: `azure`                                                                              |
| destination  | Option 2                          | object        | The GCS archive destination.                                                                                                                     |
| Option 2     | bucket [*required*]          | string        | The bucket where the archive will be stored.                                                                                                     |
| Option 2     | integration [*required*]     | object        | The GCS archive's integration destination.                                                                                                       |
| integration  | client_email [*required*]    | string        | A client email.                                                                                                                                  |
| integration  | project_id                        | string        | A project ID.                                                                                                                                    |
| Option 2     | path                              | string        | The archive path.                                                                                                                                |
| Option 2     | type [*required*]            | enum          | Type of the GCS archive destination. Allowed enum values: `gcs`                                                                                  |
| destination  | Option 3                          | object        | The S3 archive destination.                                                                                                                      |
| Option 3     | bucket [*required*]          | string        | The bucket where the archive will be stored.                                                                                                     |
| Option 3     | encryption                        | object        | The S3 encryption settings.                                                                                                                      |
| encryption   | key                               | string        | An Amazon Resource Name (ARN) used to identify an AWS KMS key.                                                                                   |
| encryption   | type [*required*]            | enum          | Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`                                                       |
| Option 3     | integration [*required*]     | object        | The S3 Archive's integration destination.                                                                                                        |
| integration  | account_id [*required*]      | string        | The account ID for the integration.                                                                                                              |
| integration  | role_name [*required*]       | string        | The path of the integration.                                                                                                                     |
| Option 3     | path                              | string        | The archive path.                                                                                                                                |
| Option 3     | storage_class                     | enum          | The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`        |
| Option 3     | type [*required*]            | enum          | Type of the S3 archive destination. Allowed enum values: `s3`                                                                                    |
| attributes   | include_tags                      | boolean       | To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive. |
| attributes   | name [*required*]            | string        | The archive name.                                                                                                                                |
| attributes   | query [*required*]           | string        | The archive query/filter. Logs matching this query are included in the archive.                                                                  |
| attributes   | rehydration_max_scan_size_in_gb   | int64         | Maximum scan size for rehydration from this archive.                                                                                             |
| attributes   | rehydration_tags                  | [string]      | An array of tags to add to rehydrated logs from an archive.                                                                                      |
| data         | type [*required*]            | string        | The type of the resource. The value should always be archives.                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "destination": {
        "container": "container-name",
        "integration": {
          "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
        },
        "path": "string",
        "region": "string",
        "storage_account": "account-name",
        "type": "azure"
      },
      "include_tags": false,
      "name": "Nginx Archive",
      "query": "source:nginx",
      "rehydration_max_scan_size_in_gb": 100,
      "rehydration_tags": [
        "team:intake",
        "team:app"
      ]
    },
    "type": "archives"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The logs archive.

| Parent field | Field                             | Type                | Description                                                                                                                                      |
| ------------ | --------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                              | object              | The definition of an archive.                                                                                                                    |
| data         | attributes                        | object              | The attributes associated with the archive.                                                                                                      |
| attributes   | destination [*required*]     | object <oneOf> | An archive's destination.                                                                                                                        |
| destination  | Option 1                          | object              | The Azure archive destination.                                                                                                                   |
| Option 1     | container [*required*]       | string              | The container where the archive will be stored.                                                                                                  |
| Option 1     | integration [*required*]     | object              | The Azure archive's integration destination.                                                                                                     |
| integration  | client_id [*required*]       | string              | A client ID.                                                                                                                                     |
| integration  | tenant_id [*required*]       | string              | A tenant ID.                                                                                                                                     |
| Option 1     | path                              | string              | The archive path.                                                                                                                                |
| Option 1     | region                            | string              | The region where the archive will be stored.                                                                                                     |
| Option 1     | storage_account [*required*] | string              | The associated storage account.                                                                                                                  |
| Option 1     | type [*required*]            | enum                | Type of the Azure archive destination. Allowed enum values: `azure`                                                                              |
| destination  | Option 2                          | object              | The GCS archive destination.                                                                                                                     |
| Option 2     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 2     | integration [*required*]     | object              | The GCS archive's integration destination.                                                                                                       |
| integration  | client_email [*required*]    | string              | A client email.                                                                                                                                  |
| integration  | project_id                        | string              | A project ID.                                                                                                                                    |
| Option 2     | path                              | string              | The archive path.                                                                                                                                |
| Option 2     | type [*required*]            | enum                | Type of the GCS archive destination. Allowed enum values: `gcs`                                                                                  |
| destination  | Option 3                          | object              | The S3 archive destination.                                                                                                                      |
| Option 3     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 3     | encryption                        | object              | The S3 encryption settings.                                                                                                                      |
| encryption   | key                               | string              | An Amazon Resource Name (ARN) used to identify an AWS KMS key.                                                                                   |
| encryption   | type [*required*]            | enum                | Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`                                                       |
| Option 3     | integration [*required*]     | object              | The S3 Archive's integration destination.                                                                                                        |
| integration  | account_id [*required*]      | string              | The account ID for the integration.                                                                                                              |
| integration  | role_name [*required*]       | string              | The path of the integration.                                                                                                                     |
| Option 3     | path                              | string              | The archive path.                                                                                                                                |
| Option 3     | storage_class                     | enum                | The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`        |
| Option 3     | type [*required*]            | enum                | Type of the S3 archive destination. Allowed enum values: `s3`                                                                                    |
| attributes   | include_tags                      | boolean             | To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive. |
| attributes   | name [*required*]            | string              | The archive name.                                                                                                                                |
| attributes   | query [*required*]           | string              | The archive query/filter. Logs matching this query are included in the archive.                                                                  |
| attributes   | rehydration_max_scan_size_in_gb   | int64               | Maximum scan size for rehydration from this archive.                                                                                             |
| attributes   | rehydration_tags                  | [string]            | An array of tags to add to rehydrated logs from an archive.                                                                                      |
| attributes   | state                             | enum                | The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`                                                     |
| data         | id                                | string              | The archive ID.                                                                                                                                  |
| data         | type [*required*]            | string              | The type of the resource. The value should always be archives.                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "destination": {
        "container": "container-name",
        "integration": {
          "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
        },
        "path": "string",
        "region": "string",
        "storage_account": "account-name",
        "type": "azure"
      },
      "include_tags": false,
      "name": "Nginx Archive",
      "query": "source:nginx",
      "rehydration_max_scan_size_in_gb": 100,
      "rehydration_tags": [
        "team:intake",
        "team:app"
      ],
      "state": "WORKING"
    },
    "id": "a2zcMylnM4OCHpYusxIi3g",
    "type": "archives"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "destination": {
        "integration": {
          "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
        }
      },
      "name": "Nginx Archive",
      "query": "source:nginx"
    },
    "type": "archives"
  }
}
EOF
                
##### 

```python
"""
Create an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.logs_archive_create_request import LogsArchiveCreateRequest
from datadog_api_client.v2.model.logs_archive_create_request_attributes import LogsArchiveCreateRequestAttributes
from datadog_api_client.v2.model.logs_archive_create_request_definition import LogsArchiveCreateRequestDefinition
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_azure_type import LogsArchiveDestinationAzureType
from datadog_api_client.v2.model.logs_archive_integration_azure import LogsArchiveIntegrationAzure

body = LogsArchiveCreateRequest(
    data=LogsArchiveCreateRequestDefinition(
        attributes=LogsArchiveCreateRequestAttributes(
            destination=LogsArchiveDestinationAzure(
                container="container-name",
                integration=LogsArchiveIntegrationAzure(
                    client_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
                    tenant_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
                ),
                storage_account="account-name",
                type=LogsArchiveDestinationAzureType.AZURE,
            ),
            include_tags=False,
            name="Nginx Archive",
            query="source:nginx",
            rehydration_max_scan_size_in_gb=100,
            rehydration_tags=[
                "team:intake",
                "team:app",
            ],
        ),
        type="archives",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.create_logs_archive(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new

body = DatadogAPIClient::V2::LogsArchiveCreateRequest.new({
  data: DatadogAPIClient::V2::LogsArchiveCreateRequestDefinition.new({
    attributes: DatadogAPIClient::V2::LogsArchiveCreateRequestAttributes.new({
      destination: DatadogAPIClient::V2::LogsArchiveDestinationAzure.new({
        container: "container-name",
        integration: DatadogAPIClient::V2::LogsArchiveIntegrationAzure.new({
          client_id: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          tenant_id: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
        }),
        storage_account: "account-name",
        type: DatadogAPIClient::V2::LogsArchiveDestinationAzureType::AZURE,
      }),
      include_tags: false,
      name: "Nginx Archive",
      query: "source:nginx",
      rehydration_max_scan_size_in_gb: 100,
      rehydration_tags: [
        "team:intake",
        "team:app",
      ],
    }),
    type: "archives",
  }),
})
p api_instance.create_logs_archive(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Create an archive returns "OK" response

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
	body := datadogV2.LogsArchiveCreateRequest{
		Data: &datadogV2.LogsArchiveCreateRequestDefinition{
			Attributes: &datadogV2.LogsArchiveCreateRequestAttributes{
				Destination: datadogV2.LogsArchiveCreateRequestDestination{
					LogsArchiveDestinationAzure: &datadogV2.LogsArchiveDestinationAzure{
						Container: "container-name",
						Integration: datadogV2.LogsArchiveIntegrationAzure{
							ClientId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
							TenantId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
						},
						StorageAccount: "account-name",
						Type:           datadogV2.LOGSARCHIVEDESTINATIONAZURETYPE_AZURE,
					}},
				IncludeTags:                datadog.PtrBool(false),
				Name:                       "Nginx Archive",
				Query:                      "source:nginx",
				RehydrationMaxScanSizeInGb: *datadog.NewNullableInt64(datadog.PtrInt64(100)),
				RehydrationTags: []string{
					"team:intake",
					"team:app",
				},
			},
			Type: "archives",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsArchivesApi(apiClient)
	resp, r, err := api.CreateLogsArchive(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.CreateLogsArchive`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsArchivesApi.CreateLogsArchive`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create an archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.LogsArchive;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequest;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequestAttributes;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequestDefinition;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequestDestination;
import com.datadog.api.client.v2.model.LogsArchiveDestinationAzure;
import com.datadog.api.client.v2.model.LogsArchiveDestinationAzureType;
import com.datadog.api.client.v2.model.LogsArchiveIntegrationAzure;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    LogsArchiveCreateRequest body =
        new LogsArchiveCreateRequest()
            .data(
                new LogsArchiveCreateRequestDefinition()
                    .attributes(
                        new LogsArchiveCreateRequestAttributes()
                            .destination(
                                new LogsArchiveCreateRequestDestination(
                                    new LogsArchiveDestinationAzure()
                                        .container("container-name")
                                        .integration(
                                            new LogsArchiveIntegrationAzure()
                                                .clientId("aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa")
                                                .tenantId("aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"))
                                        .storageAccount("account-name")
                                        .type(LogsArchiveDestinationAzureType.AZURE)))
                            .includeTags(false)
                            .name("Nginx Archive")
                            .query("source:nginx")
                            .rehydrationMaxScanSizeInGb(100L)
                            .rehydrationTags(Arrays.asList("team:intake", "team:app")))
                    .type("archives"));

    try {
      LogsArchive result = apiInstance.createLogsArchive(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#createLogsArchive");
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
// Create an archive returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequest;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequestAttributes;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequestDefinition;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequestDestination;
use datadog_api_client::datadogV2::model::LogsArchiveDestinationAzure;
use datadog_api_client::datadogV2::model::LogsArchiveDestinationAzureType;
use datadog_api_client::datadogV2::model::LogsArchiveIntegrationAzure;

#[tokio::main]
async fn main() {
    let body = LogsArchiveCreateRequest::new().data(
        LogsArchiveCreateRequestDefinition::new("archives".to_string()).attributes(
            LogsArchiveCreateRequestAttributes::new(
                LogsArchiveCreateRequestDestination::LogsArchiveDestinationAzure(Box::new(
                    LogsArchiveDestinationAzure::new(
                        "container-name".to_string(),
                        LogsArchiveIntegrationAzure::new(
                            "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa".to_string(),
                            "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa".to_string(),
                        ),
                        "account-name".to_string(),
                        LogsArchiveDestinationAzureType::AZURE,
                    ),
                )),
                "Nginx Archive".to_string(),
                "source:nginx".to_string(),
            )
            .include_tags(false)
            .rehydration_max_scan_size_in_gb(Some(100))
            .rehydration_tags(vec!["team:intake".to_string(), "team:app".to_string()]),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api.create_logs_archive(body).await;
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
 * Create an archive returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiCreateLogsArchiveRequest = {
  body: {
    data: {
      attributes: {
        destination: {
          container: "container-name",
          integration: {
            clientId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
            tenantId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          },
          storageAccount: "account-name",
          type: "azure",
        },
        includeTags: false,
        name: "Nginx Archive",
        query: "source:nginx",
        rehydrationMaxScanSizeInGb: 100,
        rehydrationTags: ["team:intake", "team:app"],
      },
      type: "archives",
    },
  },
};

apiInstance
  .createLogsArchive(params)
  .then((data: v2.LogsArchive) => {
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

## Get an archive{% #get-an-archive %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id} |

### Overview

Get a specific archive from your organization. This endpoint requires the `logs_read_archives` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| archive_id [*required*] | string | The ID of the archive. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The logs archive.

| Parent field | Field                             | Type                | Description                                                                                                                                      |
| ------------ | --------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                              | object              | The definition of an archive.                                                                                                                    |
| data         | attributes                        | object              | The attributes associated with the archive.                                                                                                      |
| attributes   | destination [*required*]     | object <oneOf> | An archive's destination.                                                                                                                        |
| destination  | Option 1                          | object              | The Azure archive destination.                                                                                                                   |
| Option 1     | container [*required*]       | string              | The container where the archive will be stored.                                                                                                  |
| Option 1     | integration [*required*]     | object              | The Azure archive's integration destination.                                                                                                     |
| integration  | client_id [*required*]       | string              | A client ID.                                                                                                                                     |
| integration  | tenant_id [*required*]       | string              | A tenant ID.                                                                                                                                     |
| Option 1     | path                              | string              | The archive path.                                                                                                                                |
| Option 1     | region                            | string              | The region where the archive will be stored.                                                                                                     |
| Option 1     | storage_account [*required*] | string              | The associated storage account.                                                                                                                  |
| Option 1     | type [*required*]            | enum                | Type of the Azure archive destination. Allowed enum values: `azure`                                                                              |
| destination  | Option 2                          | object              | The GCS archive destination.                                                                                                                     |
| Option 2     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 2     | integration [*required*]     | object              | The GCS archive's integration destination.                                                                                                       |
| integration  | client_email [*required*]    | string              | A client email.                                                                                                                                  |
| integration  | project_id                        | string              | A project ID.                                                                                                                                    |
| Option 2     | path                              | string              | The archive path.                                                                                                                                |
| Option 2     | type [*required*]            | enum                | Type of the GCS archive destination. Allowed enum values: `gcs`                                                                                  |
| destination  | Option 3                          | object              | The S3 archive destination.                                                                                                                      |
| Option 3     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 3     | encryption                        | object              | The S3 encryption settings.                                                                                                                      |
| encryption   | key                               | string              | An Amazon Resource Name (ARN) used to identify an AWS KMS key.                                                                                   |
| encryption   | type [*required*]            | enum                | Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`                                                       |
| Option 3     | integration [*required*]     | object              | The S3 Archive's integration destination.                                                                                                        |
| integration  | account_id [*required*]      | string              | The account ID for the integration.                                                                                                              |
| integration  | role_name [*required*]       | string              | The path of the integration.                                                                                                                     |
| Option 3     | path                              | string              | The archive path.                                                                                                                                |
| Option 3     | storage_class                     | enum                | The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`        |
| Option 3     | type [*required*]            | enum                | Type of the S3 archive destination. Allowed enum values: `s3`                                                                                    |
| attributes   | include_tags                      | boolean             | To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive. |
| attributes   | name [*required*]            | string              | The archive name.                                                                                                                                |
| attributes   | query [*required*]           | string              | The archive query/filter. Logs matching this query are included in the archive.                                                                  |
| attributes   | rehydration_max_scan_size_in_gb   | int64               | Maximum scan size for rehydration from this archive.                                                                                             |
| attributes   | rehydration_tags                  | [string]            | An array of tags to add to rehydrated logs from an archive.                                                                                      |
| attributes   | state                             | enum                | The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`                                                     |
| data         | id                                | string              | The archive ID.                                                                                                                                  |
| data         | type [*required*]            | string              | The type of the resource. The value should always be archives.                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "destination": {
        "container": "container-name",
        "integration": {
          "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
        },
        "path": "string",
        "region": "string",
        "storage_account": "account-name",
        "type": "azure"
      },
      "include_tags": false,
      "name": "Nginx Archive",
      "query": "source:nginx",
      "rehydration_max_scan_size_in_gb": 100,
      "rehydration_tags": [
        "team:intake",
        "team:app"
      ],
      "state": "WORKING"
    },
    "id": "a2zcMylnM4OCHpYusxIi3g",
    "type": "archives"
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

{% tab title="404" %}
Not found
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
                  \# Path parametersexport archive_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.get_logs_archive(
        archive_id="archive_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.get_logs_archive("archive_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get an archive returns "OK" response

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
	api := datadogV2.NewLogsArchivesApi(apiClient)
	resp, r, err := api.GetLogsArchive(ctx, "archive_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.GetLogsArchive`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsArchivesApi.GetLogsArchive`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get an archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.LogsArchive;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    try {
      LogsArchive result = apiInstance.getLogsArchive("archive_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#getLogsArchive");
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
// Get an archive returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api.get_logs_archive("archive_id".to_string()).await;
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
 * Get an archive returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiGetLogsArchiveRequest = {
  archiveId: "archive_id",
};

apiInstance
  .getLogsArchive(params)
  .then((data: v2.LogsArchive) => {
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

## Update an archive{% #update-an-archive %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id} |

### Overview



Update a given archive configuration.

**Note**: Using this method updates your archive configuration by **replacing** your current configuration with the new one sent to your Datadog organization.
This endpoint requires the `logs_write_archives` permission.


### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| archive_id [*required*] | string | The ID of the archive. |

### Request

#### Body Data (required)

New definition of the archive.

{% tab title="Model" %}

| Parent field | Field                             | Type          | Description                                                                                                                                      |
| ------------ | --------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                              | object        | The definition of an archive.                                                                                                                    |
| data         | attributes                        | object        | The attributes associated with the archive.                                                                                                      |
| attributes   | destination [*required*]     |  <oneOf> | An archive's destination.                                                                                                                        |
| destination  | Option 1                          | object        | The Azure archive destination.                                                                                                                   |
| Option 1     | container [*required*]       | string        | The container where the archive will be stored.                                                                                                  |
| Option 1     | integration [*required*]     | object        | The Azure archive's integration destination.                                                                                                     |
| integration  | client_id [*required*]       | string        | A client ID.                                                                                                                                     |
| integration  | tenant_id [*required*]       | string        | A tenant ID.                                                                                                                                     |
| Option 1     | path                              | string        | The archive path.                                                                                                                                |
| Option 1     | region                            | string        | The region where the archive will be stored.                                                                                                     |
| Option 1     | storage_account [*required*] | string        | The associated storage account.                                                                                                                  |
| Option 1     | type [*required*]            | enum          | Type of the Azure archive destination. Allowed enum values: `azure`                                                                              |
| destination  | Option 2                          | object        | The GCS archive destination.                                                                                                                     |
| Option 2     | bucket [*required*]          | string        | The bucket where the archive will be stored.                                                                                                     |
| Option 2     | integration [*required*]     | object        | The GCS archive's integration destination.                                                                                                       |
| integration  | client_email [*required*]    | string        | A client email.                                                                                                                                  |
| integration  | project_id                        | string        | A project ID.                                                                                                                                    |
| Option 2     | path                              | string        | The archive path.                                                                                                                                |
| Option 2     | type [*required*]            | enum          | Type of the GCS archive destination. Allowed enum values: `gcs`                                                                                  |
| destination  | Option 3                          | object        | The S3 archive destination.                                                                                                                      |
| Option 3     | bucket [*required*]          | string        | The bucket where the archive will be stored.                                                                                                     |
| Option 3     | encryption                        | object        | The S3 encryption settings.                                                                                                                      |
| encryption   | key                               | string        | An Amazon Resource Name (ARN) used to identify an AWS KMS key.                                                                                   |
| encryption   | type [*required*]            | enum          | Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`                                                       |
| Option 3     | integration [*required*]     | object        | The S3 Archive's integration destination.                                                                                                        |
| integration  | account_id [*required*]      | string        | The account ID for the integration.                                                                                                              |
| integration  | role_name [*required*]       | string        | The path of the integration.                                                                                                                     |
| Option 3     | path                              | string        | The archive path.                                                                                                                                |
| Option 3     | storage_class                     | enum          | The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`        |
| Option 3     | type [*required*]            | enum          | Type of the S3 archive destination. Allowed enum values: `s3`                                                                                    |
| attributes   | include_tags                      | boolean       | To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive. |
| attributes   | name [*required*]            | string        | The archive name.                                                                                                                                |
| attributes   | query [*required*]           | string        | The archive query/filter. Logs matching this query are included in the archive.                                                                  |
| attributes   | rehydration_max_scan_size_in_gb   | int64         | Maximum scan size for rehydration from this archive.                                                                                             |
| attributes   | rehydration_tags                  | [string]      | An array of tags to add to rehydrated logs from an archive.                                                                                      |
| data         | type [*required*]            | string        | The type of the resource. The value should always be archives.                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "destination": {
        "container": "container-name",
        "integration": {
          "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
        },
        "path": "string",
        "region": "string",
        "storage_account": "account-name",
        "type": "azure"
      },
      "include_tags": false,
      "name": "Nginx Archive",
      "query": "source:nginx",
      "rehydration_max_scan_size_in_gb": 100,
      "rehydration_tags": [
        "team:intake",
        "team:app"
      ]
    },
    "type": "archives"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The logs archive.

| Parent field | Field                             | Type                | Description                                                                                                                                      |
| ------------ | --------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                              | object              | The definition of an archive.                                                                                                                    |
| data         | attributes                        | object              | The attributes associated with the archive.                                                                                                      |
| attributes   | destination [*required*]     | object <oneOf> | An archive's destination.                                                                                                                        |
| destination  | Option 1                          | object              | The Azure archive destination.                                                                                                                   |
| Option 1     | container [*required*]       | string              | The container where the archive will be stored.                                                                                                  |
| Option 1     | integration [*required*]     | object              | The Azure archive's integration destination.                                                                                                     |
| integration  | client_id [*required*]       | string              | A client ID.                                                                                                                                     |
| integration  | tenant_id [*required*]       | string              | A tenant ID.                                                                                                                                     |
| Option 1     | path                              | string              | The archive path.                                                                                                                                |
| Option 1     | region                            | string              | The region where the archive will be stored.                                                                                                     |
| Option 1     | storage_account [*required*] | string              | The associated storage account.                                                                                                                  |
| Option 1     | type [*required*]            | enum                | Type of the Azure archive destination. Allowed enum values: `azure`                                                                              |
| destination  | Option 2                          | object              | The GCS archive destination.                                                                                                                     |
| Option 2     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 2     | integration [*required*]     | object              | The GCS archive's integration destination.                                                                                                       |
| integration  | client_email [*required*]    | string              | A client email.                                                                                                                                  |
| integration  | project_id                        | string              | A project ID.                                                                                                                                    |
| Option 2     | path                              | string              | The archive path.                                                                                                                                |
| Option 2     | type [*required*]            | enum                | Type of the GCS archive destination. Allowed enum values: `gcs`                                                                                  |
| destination  | Option 3                          | object              | The S3 archive destination.                                                                                                                      |
| Option 3     | bucket [*required*]          | string              | The bucket where the archive will be stored.                                                                                                     |
| Option 3     | encryption                        | object              | The S3 encryption settings.                                                                                                                      |
| encryption   | key                               | string              | An Amazon Resource Name (ARN) used to identify an AWS KMS key.                                                                                   |
| encryption   | type [*required*]            | enum                | Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`                                                       |
| Option 3     | integration [*required*]     | object              | The S3 Archive's integration destination.                                                                                                        |
| integration  | account_id [*required*]      | string              | The account ID for the integration.                                                                                                              |
| integration  | role_name [*required*]       | string              | The path of the integration.                                                                                                                     |
| Option 3     | path                              | string              | The archive path.                                                                                                                                |
| Option 3     | storage_class                     | enum                | The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`        |
| Option 3     | type [*required*]            | enum                | Type of the S3 archive destination. Allowed enum values: `s3`                                                                                    |
| attributes   | include_tags                      | boolean             | To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive. |
| attributes   | name [*required*]            | string              | The archive name.                                                                                                                                |
| attributes   | query [*required*]           | string              | The archive query/filter. Logs matching this query are included in the archive.                                                                  |
| attributes   | rehydration_max_scan_size_in_gb   | int64               | Maximum scan size for rehydration from this archive.                                                                                             |
| attributes   | rehydration_tags                  | [string]            | An array of tags to add to rehydrated logs from an archive.                                                                                      |
| attributes   | state                             | enum                | The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`                                                     |
| data         | id                                | string              | The archive ID.                                                                                                                                  |
| data         | type [*required*]            | string              | The type of the resource. The value should always be archives.                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "destination": {
        "container": "container-name",
        "integration": {
          "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
        },
        "path": "string",
        "region": "string",
        "storage_account": "account-name",
        "type": "azure"
      },
      "include_tags": false,
      "name": "Nginx Archive",
      "query": "source:nginx",
      "rehydration_max_scan_size_in_gb": 100,
      "rehydration_tags": [
        "team:intake",
        "team:app"
      ],
      "state": "WORKING"
    },
    "id": "a2zcMylnM4OCHpYusxIi3g",
    "type": "archives"
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

{% tab title="404" %}
Not found
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
                  \# Path parametersexport archive_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "destination": {
        "integration": {
          "client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"
        }
      },
      "name": "Nginx Archive",
      "query": "source:nginx"
    },
    "type": "archives"
  }
}
EOF
                
##### 

```python
"""
Update an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.logs_archive_create_request import LogsArchiveCreateRequest
from datadog_api_client.v2.model.logs_archive_create_request_attributes import LogsArchiveCreateRequestAttributes
from datadog_api_client.v2.model.logs_archive_create_request_definition import LogsArchiveCreateRequestDefinition
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_azure_type import LogsArchiveDestinationAzureType
from datadog_api_client.v2.model.logs_archive_integration_azure import LogsArchiveIntegrationAzure

body = LogsArchiveCreateRequest(
    data=LogsArchiveCreateRequestDefinition(
        attributes=LogsArchiveCreateRequestAttributes(
            destination=LogsArchiveDestinationAzure(
                container="container-name",
                integration=LogsArchiveIntegrationAzure(
                    client_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
                    tenant_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
                ),
                storage_account="account-name",
                type=LogsArchiveDestinationAzureType.AZURE,
            ),
            include_tags=False,
            name="Nginx Archive",
            query="source:nginx",
            rehydration_max_scan_size_in_gb=100,
            rehydration_tags=[
                "team:intake",
                "team:app",
            ],
        ),
        type="archives",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.update_logs_archive(archive_id="archive_id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new

body = DatadogAPIClient::V2::LogsArchiveCreateRequest.new({
  data: DatadogAPIClient::V2::LogsArchiveCreateRequestDefinition.new({
    attributes: DatadogAPIClient::V2::LogsArchiveCreateRequestAttributes.new({
      destination: DatadogAPIClient::V2::LogsArchiveDestinationAzure.new({
        container: "container-name",
        integration: DatadogAPIClient::V2::LogsArchiveIntegrationAzure.new({
          client_id: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          tenant_id: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
        }),
        storage_account: "account-name",
        type: DatadogAPIClient::V2::LogsArchiveDestinationAzureType::AZURE,
      }),
      include_tags: false,
      name: "Nginx Archive",
      query: "source:nginx",
      rehydration_max_scan_size_in_gb: 100,
      rehydration_tags: [
        "team:intake",
        "team:app",
      ],
    }),
    type: "archives",
  }),
})
p api_instance.update_logs_archive("archive_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Update an archive returns "OK" response

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
	body := datadogV2.LogsArchiveCreateRequest{
		Data: &datadogV2.LogsArchiveCreateRequestDefinition{
			Attributes: &datadogV2.LogsArchiveCreateRequestAttributes{
				Destination: datadogV2.LogsArchiveCreateRequestDestination{
					LogsArchiveDestinationAzure: &datadogV2.LogsArchiveDestinationAzure{
						Container: "container-name",
						Integration: datadogV2.LogsArchiveIntegrationAzure{
							ClientId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
							TenantId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
						},
						StorageAccount: "account-name",
						Type:           datadogV2.LOGSARCHIVEDESTINATIONAZURETYPE_AZURE,
					}},
				IncludeTags:                datadog.PtrBool(false),
				Name:                       "Nginx Archive",
				Query:                      "source:nginx",
				RehydrationMaxScanSizeInGb: *datadog.NewNullableInt64(datadog.PtrInt64(100)),
				RehydrationTags: []string{
					"team:intake",
					"team:app",
				},
			},
			Type: "archives",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsArchivesApi(apiClient)
	resp, r, err := api.UpdateLogsArchive(ctx, "archive_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.UpdateLogsArchive`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsArchivesApi.UpdateLogsArchive`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update an archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.LogsArchive;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequest;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequestAttributes;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequestDefinition;
import com.datadog.api.client.v2.model.LogsArchiveCreateRequestDestination;
import com.datadog.api.client.v2.model.LogsArchiveDestinationAzure;
import com.datadog.api.client.v2.model.LogsArchiveDestinationAzureType;
import com.datadog.api.client.v2.model.LogsArchiveIntegrationAzure;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    LogsArchiveCreateRequest body =
        new LogsArchiveCreateRequest()
            .data(
                new LogsArchiveCreateRequestDefinition()
                    .attributes(
                        new LogsArchiveCreateRequestAttributes()
                            .destination(
                                new LogsArchiveCreateRequestDestination(
                                    new LogsArchiveDestinationAzure()
                                        .container("container-name")
                                        .integration(
                                            new LogsArchiveIntegrationAzure()
                                                .clientId("aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa")
                                                .tenantId("aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"))
                                        .storageAccount("account-name")
                                        .type(LogsArchiveDestinationAzureType.AZURE)))
                            .includeTags(false)
                            .name("Nginx Archive")
                            .query("source:nginx")
                            .rehydrationMaxScanSizeInGb(100L)
                            .rehydrationTags(Arrays.asList("team:intake", "team:app")))
                    .type("archives"));

    try {
      LogsArchive result = apiInstance.updateLogsArchive("archive_id", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#updateLogsArchive");
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
// Update an archive returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequest;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequestAttributes;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequestDefinition;
use datadog_api_client::datadogV2::model::LogsArchiveCreateRequestDestination;
use datadog_api_client::datadogV2::model::LogsArchiveDestinationAzure;
use datadog_api_client::datadogV2::model::LogsArchiveDestinationAzureType;
use datadog_api_client::datadogV2::model::LogsArchiveIntegrationAzure;

#[tokio::main]
async fn main() {
    let body = LogsArchiveCreateRequest::new().data(
        LogsArchiveCreateRequestDefinition::new("archives".to_string()).attributes(
            LogsArchiveCreateRequestAttributes::new(
                LogsArchiveCreateRequestDestination::LogsArchiveDestinationAzure(Box::new(
                    LogsArchiveDestinationAzure::new(
                        "container-name".to_string(),
                        LogsArchiveIntegrationAzure::new(
                            "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa".to_string(),
                            "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa".to_string(),
                        ),
                        "account-name".to_string(),
                        LogsArchiveDestinationAzureType::AZURE,
                    ),
                )),
                "Nginx Archive".to_string(),
                "source:nginx".to_string(),
            )
            .include_tags(false)
            .rehydration_max_scan_size_in_gb(Some(100))
            .rehydration_tags(vec!["team:intake".to_string(), "team:app".to_string()]),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api
        .update_logs_archive("archive_id".to_string(), body)
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
 * Update an archive returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiUpdateLogsArchiveRequest = {
  body: {
    data: {
      attributes: {
        destination: {
          container: "container-name",
          integration: {
            clientId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
            tenantId: "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
          },
          storageAccount: "account-name",
          type: "azure",
        },
        includeTags: false,
        name: "Nginx Archive",
        query: "source:nginx",
        rehydrationMaxScanSizeInGb: 100,
        rehydrationTags: ["team:intake", "team:app"],
      },
      type: "archives",
    },
  },
  archiveId: "archive_id",
};

apiInstance
  .updateLogsArchive(params)
  .then((data: v2.LogsArchive) => {
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

## Delete an archive{% #delete-an-archive %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id} |

### Overview

Delete a given archive from your organization. This endpoint requires the `logs_write_archives` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| archive_id [*required*] | string | The ID of the archive. |

### Response

{% tab title="204" %}
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

{% tab title="404" %}
Not found
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
                  \# Path parametersexport archive_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    api_instance.delete_logs_archive(
        archive_id="archive_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
api_instance.delete_logs_archive("archive_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete an archive returns "OK" response

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
	api := datadogV2.NewLogsArchivesApi(apiClient)
	r, err := api.DeleteLogsArchive(ctx, "archive_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.DeleteLogsArchive`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete an archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    try {
      apiInstance.deleteLogsArchive("archive_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#deleteLogsArchive");
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
// Delete an archive returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api.delete_logs_archive("archive_id".to_string()).await;
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
 * Delete an archive returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiDeleteLogsArchiveRequest = {
  archiveId: "archive_id",
};

apiInstance
  .deleteLogsArchive(params)
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

## List read roles for an archive{% #list-read-roles-for-an-archive %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}/readers      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}/readers      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |

### Overview

Returns all read roles a given archive is restricted to. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| archive_id [*required*] | string | The ID of the archive. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about multiple roles.

| Parent field  | Field                  | Type      | Description                                                                           |
| ------------- | ---------------------- | --------- | ------------------------------------------------------------------------------------- |
|               | data                   | [object]  | Array of returned roles.                                                              |
| data          | attributes             | object    | Attributes of the role.                                                               |
| attributes    | created_at             | date-time | Creation time of the role.                                                            |
| attributes    | modified_at            | date-time | Time of last role modification.                                                       |
| attributes    | name                   | string    | The name of the role. The name is neither unique nor a stable identifier of the role. |
| attributes    | user_count             | int64     | Number of users with that role.                                                       |
| data          | id                     | string    | The unique identifier of the role.                                                    |
| data          | relationships          | object    | Relationships of the role object returned by the API.                                 |
| relationships | permissions            | object    | Relationship to multiple permissions objects.                                         |
| permissions   | data                   | [object]  | Relationships to permission objects.                                                  |
| data          | id                     | string    | ID of the permission.                                                                 |
| data          | type                   | enum      | Permissions resource type. Allowed enum values: `permissions`                         |
| data          | type [*required*] | enum      | Roles type. Allowed enum values: `roles`                                              |
|               | meta                   | object    | Object describing meta attributes of response.                                        |
| meta          | page                   | object    | Pagination object.                                                                    |
| page          | total_count            | int64     | Total count.                                                                          |
| page          | total_filtered_count   | int64     | Total count of elements matched by the filter.                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "user_count": "integer"
      },
      "id": "string",
      "relationships": {
        "permissions": {
          "data": [
            {
              "id": "string",
              "type": "permissions"
            }
          ]
        }
      },
      "type": "roles"
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
Not found
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
                  \# Path parametersexport archive_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}/readers" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List read roles for an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.list_archive_read_roles(
        archive_id="archive_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List read roles for an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.list_archive_read_roles("archive_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List read roles for an archive returns "OK" response

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
	api := datadogV2.NewLogsArchivesApi(apiClient)
	resp, r, err := api.ListArchiveReadRoles(ctx, "archive_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.ListArchiveReadRoles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsArchivesApi.ListArchiveReadRoles`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List read roles for an archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.RolesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    try {
      RolesResponse result = apiInstance.listArchiveReadRoles("archive_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#listArchiveReadRoles");
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
// List read roles for an archive returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api.list_archive_read_roles("archive_id".to_string()).await;
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
 * List read roles for an archive returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiListArchiveReadRolesRequest = {
  archiveId: "archive_id",
};

apiInstance
  .listArchiveReadRoles(params)
  .then((data: v2.RolesResponse) => {
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

## Grant role to an archive{% #grant-role-to-an-archive %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}/readers      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}/readers      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |

### Overview

Adds a read role to an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) This endpoint requires the `logs_write_archives` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| archive_id [*required*] | string | The ID of the archive. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field | Type   | Description                              |
| ------------ | ----- | ------ | ---------------------------------------- |
|              | data  | object | Relationship to role object.             |
| data         | id    | string | The unique identifier of the role.       |
| data         | type  | enum   | Roles type. Allowed enum values: `roles` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "type": "roles"
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
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

{% tab title="404" %}
Not found
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
                  \# Path parametersexport archive_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}/readers" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF
                
##### 

```python
"""
Grant role to an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    api_instance.add_read_role_to_archive(archive_id="archive_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Grant role to an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new

body = DatadogAPIClient::V2::RelationshipToRole.new({
  data: DatadogAPIClient::V2::RelationshipToRoleData.new({
    id: "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    type: DatadogAPIClient::V2::RolesType::ROLES,
  }),
})
api_instance.add_read_role_to_archive("archive_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Grant role to an archive returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.RelationshipToRole{
		Data: &datadogV2.RelationshipToRoleData{
			Id:   datadog.PtrString("3653d3c6-0c75-11ea-ad28-fb5701eabc7d"),
			Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsArchivesApi(apiClient)
	r, err := api.AddReadRoleToArchive(ctx, "archive_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.AddReadRoleToArchive`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Grant role to an archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    RelationshipToRole body =
        new RelationshipToRole()
            .data(
                new RelationshipToRoleData()
                    .id("3653d3c6-0c75-11ea-ad28-fb5701eabc7d")
                    .type(RolesType.ROLES));

    try {
      apiInstance.addReadRoleToArchive("archive_id", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#addReadRoleToArchive");
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
// Grant role to an archive returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    let body = RelationshipToRole::new().data(
        RelationshipToRoleData::new()
            .id("3653d3c6-0c75-11ea-ad28-fb5701eabc7d".to_string())
            .type_(RolesType::ROLES),
    );
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api
        .add_read_role_to_archive("archive_id".to_string(), body)
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
 * Grant role to an archive returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiAddReadRoleToArchiveRequest = {
  body: {
    data: {
      id: "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
      type: "roles",
    },
  },
  archiveId: "archive_id",
};

apiInstance
  .addReadRoleToArchive(params)
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

## Revoke role from an archive{% #revoke-role-from-an-archive %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}/readers      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}/readers      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers |

### Overview

Removes a role from an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) This endpoint requires the `logs_write_archives` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| archive_id [*required*] | string | The ID of the archive. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field | Type   | Description                              |
| ------------ | ----- | ------ | ---------------------------------------- |
|              | data  | object | Relationship to role object.             |
| data         | id    | string | The unique identifier of the role.       |
| data         | type  | enum   | Roles type. Allowed enum values: `roles` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "type": "roles"
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
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

{% tab title="404" %}
Not found
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
                  \# Path parametersexport archive_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}/readers" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF
                
##### 

```python
"""
Revoke role from an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    api_instance.remove_role_from_archive(archive_id="archive_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Revoke role from an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new

body = DatadogAPIClient::V2::RelationshipToRole.new({
  data: DatadogAPIClient::V2::RelationshipToRoleData.new({
    id: "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    type: DatadogAPIClient::V2::RolesType::ROLES,
  }),
})
api_instance.remove_role_from_archive("archive_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Revoke role from an archive returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.RelationshipToRole{
		Data: &datadogV2.RelationshipToRoleData{
			Id:   datadog.PtrString("3653d3c6-0c75-11ea-ad28-fb5701eabc7d"),
			Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsArchivesApi(apiClient)
	r, err := api.RemoveRoleFromArchive(ctx, "archive_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.RemoveRoleFromArchive`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Revoke role from an archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    RelationshipToRole body =
        new RelationshipToRole()
            .data(
                new RelationshipToRoleData()
                    .id("3653d3c6-0c75-11ea-ad28-fb5701eabc7d")
                    .type(RolesType.ROLES));

    try {
      apiInstance.removeRoleFromArchive("archive_id", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#removeRoleFromArchive");
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
// Revoke role from an archive returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    let body = RelationshipToRole::new().data(
        RelationshipToRoleData::new()
            .id("3653d3c6-0c75-11ea-ad28-fb5701eabc7d".to_string())
            .type_(RolesType::ROLES),
    );
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api
        .remove_role_from_archive("archive_id".to_string(), body)
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
 * Revoke role from an archive returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiRemoveRoleFromArchiveRequest = {
  body: {
    data: {
      id: "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
      type: "roles",
    },
  },
  archiveId: "archive_id",
};

apiInstance
  .removeRoleFromArchive(params)
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

## Get archive order{% #get-archive-order %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/archive-order |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/archive-order |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/archive-order      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/archive-order      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/archive-order     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/archive-order |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/archive-order |

### Overview

Get the current order of your archives. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A ordered list of archive IDs.

| Parent field | Field                         | Type     | Description                                                                                                                      |
| ------------ | ----------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
|              | data                          | object   | The definition of an archive order.                                                                                              |
| data         | attributes [*required*]  | object   | The attributes associated with the archive order.                                                                                |
| attributes   | archive_ids [*required*] | [string] | An ordered array of `<ARCHIVE_ID>` strings, the order of archive IDs in the array define the overall archives order for Datadog. |
| data         | type [*required*]        | enum     | Type of the archive order definition. Allowed enum values: `archive_order`                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archive_ids": [
        "a2zcMylnM4OCHpYusxIi1g",
        "a2zcMylnM4OCHpYusxIi2g",
        "a2zcMylnM4OCHpYusxIi3g"
      ]
    },
    "type": "archive_order"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archive-order" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get archive order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.get_logs_archive_order()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get archive order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.get_logs_archive_order()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get archive order returns "OK" response

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
	api := datadogV2.NewLogsArchivesApi(apiClient)
	resp, r, err := api.GetLogsArchiveOrder(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.GetLogsArchiveOrder`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsArchivesApi.GetLogsArchiveOrder`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get archive order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.LogsArchiveOrder;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    try {
      LogsArchiveOrder result = apiInstance.getLogsArchiveOrder();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#getLogsArchiveOrder");
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
// Get archive order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api.get_logs_archive_order().await;
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
 * Get archive order returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

apiInstance
  .getLogsArchiveOrder()
  .then((data: v2.LogsArchiveOrder) => {
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

## Update archive order{% #update-archive-order %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/logs/config/archive-order |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/logs/config/archive-order |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/logs/config/archive-order      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/logs/config/archive-order      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/logs/config/archive-order     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/logs/config/archive-order |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/logs/config/archive-order |

### Overview



Update the order of your archives. Since logs are processed sequentially, reordering an archive may change the structure and content of the data processed by other archives.

**Note**: Using the `PUT` method updates your archive's order by replacing the current order with the new one.
This endpoint requires the `logs_write_archives` permission.


### Request

#### Body Data (required)

An object containing the new ordered list of archive IDs.

{% tab title="Model" %}

| Parent field | Field                         | Type     | Description                                                                                                                      |
| ------------ | ----------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
|              | data                          | object   | The definition of an archive order.                                                                                              |
| data         | attributes [*required*]  | object   | The attributes associated with the archive order.                                                                                |
| attributes   | archive_ids [*required*] | [string] | An ordered array of `<ARCHIVE_ID>` strings, the order of archive IDs in the array define the overall archives order for Datadog. |
| data         | type [*required*]        | enum     | Type of the archive order definition. Allowed enum values: `archive_order`                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archive_ids": [
        "a2zcMylnM4OCHpYusxIi1g",
        "a2zcMylnM4OCHpYusxIi2g",
        "a2zcMylnM4OCHpYusxIi3g"
      ]
    },
    "type": "archive_order"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A ordered list of archive IDs.

| Parent field | Field                         | Type     | Description                                                                                                                      |
| ------------ | ----------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
|              | data                          | object   | The definition of an archive order.                                                                                              |
| data         | attributes [*required*]  | object   | The attributes associated with the archive order.                                                                                |
| attributes   | archive_ids [*required*] | [string] | An ordered array of `<ARCHIVE_ID>` strings, the order of archive IDs in the array define the overall archives order for Datadog. |
| data         | type [*required*]        | enum     | Type of the archive order definition. Allowed enum values: `archive_order`                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archive_ids": [
        "a2zcMylnM4OCHpYusxIi1g",
        "a2zcMylnM4OCHpYusxIi2g",
        "a2zcMylnM4OCHpYusxIi3g"
      ]
    },
    "type": "archive_order"
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
                  \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archive-order" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "archive_ids": [
        "a2zcMylnM4OCHpYusxIi1g",
        "a2zcMylnM4OCHpYusxIi2g",
        "a2zcMylnM4OCHpYusxIi3g"
      ]
    },
    "type": "archive_order"
  }
}
EOF
                
##### 

```python
"""
Update archive order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.logs_archive_order import LogsArchiveOrder
from datadog_api_client.v2.model.logs_archive_order_attributes import LogsArchiveOrderAttributes
from datadog_api_client.v2.model.logs_archive_order_definition import LogsArchiveOrderDefinition
from datadog_api_client.v2.model.logs_archive_order_definition_type import LogsArchiveOrderDefinitionType

body = LogsArchiveOrder(
    data=LogsArchiveOrderDefinition(
        attributes=LogsArchiveOrderAttributes(
            archive_ids=[
                "a2zcMylnM4OCHpYusxIi1g",
                "a2zcMylnM4OCHpYusxIi2g",
                "a2zcMylnM4OCHpYusxIi3g",
            ],
        ),
        type=LogsArchiveOrderDefinitionType.ARCHIVE_ORDER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.update_logs_archive_order(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update archive order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new

body = DatadogAPIClient::V2::LogsArchiveOrder.new({
  data: DatadogAPIClient::V2::LogsArchiveOrderDefinition.new({
    attributes: DatadogAPIClient::V2::LogsArchiveOrderAttributes.new({
      archive_ids: [
        "a2zcMylnM4OCHpYusxIi1g",
        "a2zcMylnM4OCHpYusxIi2g",
        "a2zcMylnM4OCHpYusxIi3g",
      ],
    }),
    type: DatadogAPIClient::V2::LogsArchiveOrderDefinitionType::ARCHIVE_ORDER,
  }),
})
p api_instance.update_logs_archive_order(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Update archive order returns "OK" response

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
	body := datadogV2.LogsArchiveOrder{
		Data: &datadogV2.LogsArchiveOrderDefinition{
			Attributes: datadogV2.LogsArchiveOrderAttributes{
				ArchiveIds: []string{
					"a2zcMylnM4OCHpYusxIi1g",
					"a2zcMylnM4OCHpYusxIi2g",
					"a2zcMylnM4OCHpYusxIi3g",
				},
			},
			Type: datadogV2.LOGSARCHIVEORDERDEFINITIONTYPE_ARCHIVE_ORDER,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsArchivesApi(apiClient)
	resp, r, err := api.UpdateLogsArchiveOrder(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsArchivesApi.UpdateLogsArchiveOrder`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsArchivesApi.UpdateLogsArchiveOrder`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update archive order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsArchivesApi;
import com.datadog.api.client.v2.model.LogsArchiveOrder;
import com.datadog.api.client.v2.model.LogsArchiveOrderAttributes;
import com.datadog.api.client.v2.model.LogsArchiveOrderDefinition;
import com.datadog.api.client.v2.model.LogsArchiveOrderDefinitionType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsArchivesApi apiInstance = new LogsArchivesApi(defaultClient);

    LogsArchiveOrder body =
        new LogsArchiveOrder()
            .data(
                new LogsArchiveOrderDefinition()
                    .attributes(
                        new LogsArchiveOrderAttributes()
                            .archiveIds(
                                Arrays.asList(
                                    "a2zcMylnM4OCHpYusxIi1g",
                                    "a2zcMylnM4OCHpYusxIi2g",
                                    "a2zcMylnM4OCHpYusxIi3g")))
                    .type(LogsArchiveOrderDefinitionType.ARCHIVE_ORDER));

    try {
      LogsArchiveOrder result = apiInstance.updateLogsArchiveOrder(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsArchivesApi#updateLogsArchiveOrder");
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
// Update archive order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_archives::LogsArchivesAPI;
use datadog_api_client::datadogV2::model::LogsArchiveOrder;
use datadog_api_client::datadogV2::model::LogsArchiveOrderAttributes;
use datadog_api_client::datadogV2::model::LogsArchiveOrderDefinition;
use datadog_api_client::datadogV2::model::LogsArchiveOrderDefinitionType;

#[tokio::main]
async fn main() {
    let body = LogsArchiveOrder::new().data(LogsArchiveOrderDefinition::new(
        LogsArchiveOrderAttributes::new(vec![
            "a2zcMylnM4OCHpYusxIi1g".to_string(),
            "a2zcMylnM4OCHpYusxIi2g".to_string(),
            "a2zcMylnM4OCHpYusxIi3g".to_string(),
        ]),
        LogsArchiveOrderDefinitionType::ARCHIVE_ORDER,
    ));
    let configuration = datadog::Configuration::new();
    let api = LogsArchivesAPI::with_config(configuration);
    let resp = api.update_logs_archive_order(body).await;
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
 * Update archive order returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsArchivesApi(configuration);

const params: v2.LogsArchivesApiUpdateLogsArchiveOrderRequest = {
  body: {
    data: {
      attributes: {
        archiveIds: [
          "a2zcMylnM4OCHpYusxIi1g",
          "a2zcMylnM4OCHpYusxIi2g",
          "a2zcMylnM4OCHpYusxIi3g",
        ],
      },
      type: "archive_order",
    },
  },
};

apiInstance
  .updateLogsArchiveOrder(params)
  .then((data: v2.LogsArchiveOrder) => {
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
