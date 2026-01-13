# Source: https://docs.datadoghq.com/api/latest/logs-archives/

# Logs Archives
Archives forward all the logs ingested to a cloud storage system.
See the [Archives Page](https://app.datadoghq.com/logs/pipelines/archives) for a list of the archives currently configured in Datadog.
## [Get all archives](https://docs.datadoghq.com/api/latest/logs-archives/#get-all-archives)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#get-all-archives-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/archiveshttps://api.ap2.datadoghq.com/api/v2/logs/config/archiveshttps://api.datadoghq.eu/api/v2/logs/config/archiveshttps://api.ddog-gov.com/api/v2/logs/config/archiveshttps://api.datadoghq.com/api/v2/logs/config/archiveshttps://api.us3.datadoghq.com/api/v2/logs/config/archiveshttps://api.us5.datadoghq.com/api/v2/logs/config/archives
### Overview
Get the list of configured logs archives with their definitions. This endpoint requires the `logs_read_archives` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-archives/#ListLogsArchives-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#ListLogsArchives-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#ListLogsArchives-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


The available archives.
Field
Type
Description
data
[object]
A list of archives.
attributes
object
The attributes associated with the archive.
destination [_required_]
object <oneOf>
An archive's destination.
Option 1
object
The Azure archive destination.
container [_required_]
string
The container where the archive will be stored.
integration [_required_]
object
The Azure archive's integration destination.
client_id [_required_]
string
A client ID.
tenant_id [_required_]
string
A tenant ID.
path
string
The archive path.
region
string
The region where the archive will be stored.
storage_account [_required_]
string
The associated storage account.
type [_required_]
enum
Type of the Azure archive destination. Allowed enum values: `azure`
default: `azure`
Option 2
object
The GCS archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
integration [_required_]
object
The GCS archive's integration destination.
client_email [_required_]
string
A client email.
project_id
string
A project ID.
path
string
The archive path.
type [_required_]
enum
Type of the GCS archive destination. Allowed enum values: `gcs`
default: `gcs`
Option 3
object
The S3 archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
encryption
object
The S3 encryption settings.
key
string
An Amazon Resource Name (ARN) used to identify an AWS KMS key.
type [_required_]
enum
Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`
integration [_required_]
object
The S3 Archive's integration destination.
account_id [_required_]
string
The account ID for the integration.
role_name [_required_]
string
The path of the integration.
path
string
The archive path.
storage_class
enum
The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`
default: `STANDARD`
type [_required_]
enum
Type of the S3 archive destination. Allowed enum values: `s3`
default: `s3`
include_tags
boolean
To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive.
name [_required_]
string
The archive name.
query [_required_]
string
The archive query/filter. Logs matching this query are included in the archive.
rehydration_max_scan_size_in_gb
int64
Maximum scan size for rehydration from this archive.
rehydration_tags
[string]
An array of tags to add to rehydrated logs from an archive.
state
enum
The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`
id
string
The archive ID.
type [_required_]
string
The type of the resource. The value should always be archives.
default: `archives`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Get all archives
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all archives
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all archives
```
# Get all archives returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.list_logs_archives()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all archives
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all archives
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get all archives
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get all archives
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create an archive](https://docs.datadoghq.com/api/latest/logs-archives/#create-an-archive)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#create-an-archive-v2)


POST https://api.ap1.datadoghq.com/api/v2/logs/config/archiveshttps://api.ap2.datadoghq.com/api/v2/logs/config/archiveshttps://api.datadoghq.eu/api/v2/logs/config/archiveshttps://api.ddog-gov.com/api/v2/logs/config/archiveshttps://api.datadoghq.com/api/v2/logs/config/archiveshttps://api.us3.datadoghq.com/api/v2/logs/config/archiveshttps://api.us5.datadoghq.com/api/v2/logs/config/archives
### Overview
Create an archive in your organization. This endpoint requires the `logs_write_archives` permission.
### Request
#### Body Data (required)
The definition of the new archive.
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


Field
Type
Description
data
object
The definition of an archive.
attributes
object
The attributes associated with the archive.
destination [_required_]
<oneOf>
An archive's destination.
Option 1
object
The Azure archive destination.
container [_required_]
string
The container where the archive will be stored.
integration [_required_]
object
The Azure archive's integration destination.
client_id [_required_]
string
A client ID.
tenant_id [_required_]
string
A tenant ID.
path
string
The archive path.
region
string
The region where the archive will be stored.
storage_account [_required_]
string
The associated storage account.
type [_required_]
enum
Type of the Azure archive destination. Allowed enum values: `azure`
default: `azure`
Option 2
object
The GCS archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
integration [_required_]
object
The GCS archive's integration destination.
client_email [_required_]
string
A client email.
project_id
string
A project ID.
path
string
The archive path.
type [_required_]
enum
Type of the GCS archive destination. Allowed enum values: `gcs`
default: `gcs`
Option 3
object
The S3 archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
encryption
object
The S3 encryption settings.
key
string
An Amazon Resource Name (ARN) used to identify an AWS KMS key.
type [_required_]
enum
Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`
integration [_required_]
object
The S3 Archive's integration destination.
account_id [_required_]
string
The account ID for the integration.
role_name [_required_]
string
The path of the integration.
path
string
The archive path.
storage_class
enum
The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`
default: `STANDARD`
type [_required_]
enum
Type of the S3 archive destination. Allowed enum values: `s3`
default: `s3`
include_tags
boolean
To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive.
name [_required_]
string
The archive name.
query [_required_]
string
The archive query/filter. Logs matching this query are included in the archive.
rehydration_max_scan_size_in_gb
int64
Maximum scan size for rehydration from this archive.
rehydration_tags
[string]
An array of tags to add to rehydrated logs from an archive.
type [_required_]
string
The type of the resource. The value should always be archives.
default: `archives`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-archives/#CreateLogsArchive-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#CreateLogsArchive-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#CreateLogsArchive-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#CreateLogsArchive-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


The logs archive.
Field
Type
Description
data
object
The definition of an archive.
attributes
object
The attributes associated with the archive.
destination [_required_]
object <oneOf>
An archive's destination.
Option 1
object
The Azure archive destination.
container [_required_]
string
The container where the archive will be stored.
integration [_required_]
object
The Azure archive's integration destination.
client_id [_required_]
string
A client ID.
tenant_id [_required_]
string
A tenant ID.
path
string
The archive path.
region
string
The region where the archive will be stored.
storage_account [_required_]
string
The associated storage account.
type [_required_]
enum
Type of the Azure archive destination. Allowed enum values: `azure`
default: `azure`
Option 2
object
The GCS archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
integration [_required_]
object
The GCS archive's integration destination.
client_email [_required_]
string
A client email.
project_id
string
A project ID.
path
string
The archive path.
type [_required_]
enum
Type of the GCS archive destination. Allowed enum values: `gcs`
default: `gcs`
Option 3
object
The S3 archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
encryption
object
The S3 encryption settings.
key
string
An Amazon Resource Name (ARN) used to identify an AWS KMS key.
type [_required_]
enum
Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`
integration [_required_]
object
The S3 Archive's integration destination.
account_id [_required_]
string
The account ID for the integration.
role_name [_required_]
string
The path of the integration.
path
string
The archive path.
storage_class
enum
The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`
default: `STANDARD`
type [_required_]
enum
Type of the S3 archive destination. Allowed enum values: `s3`
default: `s3`
include_tags
boolean
To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive.
name [_required_]
string
The archive name.
query [_required_]
string
The archive query/filter. Logs matching this query are included in the archive.
rehydration_max_scan_size_in_gb
int64
Maximum scan size for rehydration from this archive.
rehydration_tags
[string]
An array of tags to add to rehydrated logs from an archive.
state
enum
The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`
id
string
The archive ID.
type [_required_]
string
The type of the resource. The value should always be archives.
default: `archives`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Create an archive
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives" \
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

                
```

#####  Create an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get an archive](https://docs.datadoghq.com/api/latest/logs-archives/#get-an-archive)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#get-an-archive-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}
### Overview
Get a specific archive from your organization. This endpoint requires the `logs_read_archives` permission.
### Arguments
#### Path Parameters
Name
Type
Description
archive_id [_required_]
string
The ID of the archive.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchive-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchive-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchive-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchive-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchive-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


The logs archive.
Field
Type
Description
data
object
The definition of an archive.
attributes
object
The attributes associated with the archive.
destination [_required_]
object <oneOf>
An archive's destination.
Option 1
object
The Azure archive destination.
container [_required_]
string
The container where the archive will be stored.
integration [_required_]
object
The Azure archive's integration destination.
client_id [_required_]
string
A client ID.
tenant_id [_required_]
string
A tenant ID.
path
string
The archive path.
region
string
The region where the archive will be stored.
storage_account [_required_]
string
The associated storage account.
type [_required_]
enum
Type of the Azure archive destination. Allowed enum values: `azure`
default: `azure`
Option 2
object
The GCS archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
integration [_required_]
object
The GCS archive's integration destination.
client_email [_required_]
string
A client email.
project_id
string
A project ID.
path
string
The archive path.
type [_required_]
enum
Type of the GCS archive destination. Allowed enum values: `gcs`
default: `gcs`
Option 3
object
The S3 archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
encryption
object
The S3 encryption settings.
key
string
An Amazon Resource Name (ARN) used to identify an AWS KMS key.
type [_required_]
enum
Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`
integration [_required_]
object
The S3 Archive's integration destination.
account_id [_required_]
string
The account ID for the integration.
role_name [_required_]
string
The path of the integration.
path
string
The archive path.
storage_class
enum
The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`
default: `STANDARD`
type [_required_]
enum
Type of the S3 archive destination. Allowed enum values: `s3`
default: `s3`
include_tags
boolean
To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive.
name [_required_]
string
The archive name.
query [_required_]
string
The archive query/filter. Logs matching this query are included in the archive.
rehydration_max_scan_size_in_gb
int64
Maximum scan size for rehydration from this archive.
rehydration_tags
[string]
An array of tags to add to rehydrated logs from an archive.
state
enum
The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`
id
string
The archive ID.
type [_required_]
string
The type of the resource. The value should always be archives.
default: `archives`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Get an archive
Copy
```
                  # Path parameters  
export archive_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an archive
```
# Get an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.get_logs_archive("archive_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update an archive](https://docs.datadoghq.com/api/latest/logs-archives/#update-an-archive)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#update-an-archive-v2)


PUT https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}
### Overview
Update a given archive configuration.
**Note** : Using this method updates your archive configuration by **replacing** your current configuration with the new one sent to your Datadog organization.
This endpoint requires the `logs_write_archives` permission.
### Arguments
#### Path Parameters
Name
Type
Description
archive_id [_required_]
string
The ID of the archive.
### Request
#### Body Data (required)
New definition of the archive.
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


Field
Type
Description
data
object
The definition of an archive.
attributes
object
The attributes associated with the archive.
destination [_required_]
<oneOf>
An archive's destination.
Option 1
object
The Azure archive destination.
container [_required_]
string
The container where the archive will be stored.
integration [_required_]
object
The Azure archive's integration destination.
client_id [_required_]
string
A client ID.
tenant_id [_required_]
string
A tenant ID.
path
string
The archive path.
region
string
The region where the archive will be stored.
storage_account [_required_]
string
The associated storage account.
type [_required_]
enum
Type of the Azure archive destination. Allowed enum values: `azure`
default: `azure`
Option 2
object
The GCS archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
integration [_required_]
object
The GCS archive's integration destination.
client_email [_required_]
string
A client email.
project_id
string
A project ID.
path
string
The archive path.
type [_required_]
enum
Type of the GCS archive destination. Allowed enum values: `gcs`
default: `gcs`
Option 3
object
The S3 archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
encryption
object
The S3 encryption settings.
key
string
An Amazon Resource Name (ARN) used to identify an AWS KMS key.
type [_required_]
enum
Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`
integration [_required_]
object
The S3 Archive's integration destination.
account_id [_required_]
string
The account ID for the integration.
role_name [_required_]
string
The path of the integration.
path
string
The archive path.
storage_class
enum
The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`
default: `STANDARD`
type [_required_]
enum
Type of the S3 archive destination. Allowed enum values: `s3`
default: `s3`
include_tags
boolean
To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive.
name [_required_]
string
The archive name.
query [_required_]
string
The archive query/filter. Logs matching this query are included in the archive.
rehydration_max_scan_size_in_gb
int64
Maximum scan size for rehydration from this archive.
rehydration_tags
[string]
An array of tags to add to rehydrated logs from an archive.
type [_required_]
string
The type of the resource. The value should always be archives.
default: `archives`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchive-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchive-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchive-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchive-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchive-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


The logs archive.
Field
Type
Description
data
object
The definition of an archive.
attributes
object
The attributes associated with the archive.
destination [_required_]
object <oneOf>
An archive's destination.
Option 1
object
The Azure archive destination.
container [_required_]
string
The container where the archive will be stored.
integration [_required_]
object
The Azure archive's integration destination.
client_id [_required_]
string
A client ID.
tenant_id [_required_]
string
A tenant ID.
path
string
The archive path.
region
string
The region where the archive will be stored.
storage_account [_required_]
string
The associated storage account.
type [_required_]
enum
Type of the Azure archive destination. Allowed enum values: `azure`
default: `azure`
Option 2
object
The GCS archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
integration [_required_]
object
The GCS archive's integration destination.
client_email [_required_]
string
A client email.
project_id
string
A project ID.
path
string
The archive path.
type [_required_]
enum
Type of the GCS archive destination. Allowed enum values: `gcs`
default: `gcs`
Option 3
object
The S3 archive destination.
bucket [_required_]
string
The bucket where the archive will be stored.
encryption
object
The S3 encryption settings.
key
string
An Amazon Resource Name (ARN) used to identify an AWS KMS key.
type [_required_]
enum
Type of S3 encryption for a destination. Allowed enum values: `NO_OVERRIDE,SSE_S3,SSE_KMS`
integration [_required_]
object
The S3 Archive's integration destination.
account_id [_required_]
string
The account ID for the integration.
role_name [_required_]
string
The path of the integration.
path
string
The archive path.
storage_class
enum
The storage class where the archive will be stored. Allowed enum values: `STANDARD,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,GLACIER_IR`
default: `STANDARD`
type [_required_]
enum
Type of the S3 archive destination. Allowed enum values: `s3`
default: `s3`
include_tags
boolean
To store the tags in the archive, set the value "true". If it is set to "false", the tags will be deleted when the logs are sent to the archive.
name [_required_]
string
The archive name.
query [_required_]
string
The archive query/filter. Logs matching this query are included in the archive.
rehydration_max_scan_size_in_gb
int64
Maximum scan size for rehydration from this archive.
rehydration_tags
[string]
An array of tags to add to rehydrated logs from an archive.
state
enum
The state of the archive. Allowed enum values: `UNKNOWN,WORKING,FAILING,WORKING_AUTH_LEGACY`
id
string
The archive ID.
type [_required_]
string
The type of the resource. The value should always be archives.
default: `archives`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Update an archive
Copy
```
                  # Path parameters  
export archive_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}" \
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

                
```

#####  Update an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete an archive](https://docs.datadoghq.com/api/latest/logs-archives/#delete-an-archive)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#delete-an-archive-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}https://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}https://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}https://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}
### Overview
Delete a given archive from your organization. This endpoint requires the `logs_write_archives` permission.
### Arguments
#### Path Parameters
Name
Type
Description
archive_id [_required_]
string
The ID of the archive.
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-archives/#DeleteLogsArchive-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#DeleteLogsArchive-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#DeleteLogsArchive-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-archives/#DeleteLogsArchive-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#DeleteLogsArchive-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Delete an archive
Copy
```
                  # Path parameters  
export archive_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an archive
```
# Delete an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
api_instance.delete_logs_archive("archive_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [List read roles for an archive](https://docs.datadoghq.com/api/latest/logs-archives/#list-read-roles-for-an-archive)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#list-read-roles-for-an-archive-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}/readershttps://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers
### Overview
Returns all read roles a given archive is restricted to. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
archive_id [_required_]
string
The ID of the archive.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-archives/#ListArchiveReadRoles-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#ListArchiveReadRoles-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#ListArchiveReadRoles-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-archives/#ListArchiveReadRoles-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#ListArchiveReadRoles-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


Response containing information about multiple roles.
Field
Type
Description
data
[object]
Array of returned roles.
attributes
object
Attributes of the role.
created_at
date-time
Creation time of the role.
modified_at
date-time
Time of last role modification.
name
string
The name of the role. The name is neither unique nor a stable identifier of the role.
user_count
int64
Number of users with that role.
id
string
The unique identifier of the role.
relationships
object
Relationships of the role object returned by the API.
permissions
object
Relationship to multiple permissions objects.
data
[object]
Relationships to permission objects.
id
string
ID of the permission.
type
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
meta
object
Object describing meta attributes of response.
page
object
Pagination object.
total_count
int64
Total count.
total_filtered_count
int64
Total count of elements matched by the filter.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  List read roles for an archive
Copy
```
                  # Path parameters  
export archive_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}/readers" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List read roles for an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List read roles for an archive
```
# List read roles for an archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.list_archive_read_roles("archive_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List read roles for an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List read roles for an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List read roles for an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List read roles for an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Grant role to an archive](https://docs.datadoghq.com/api/latest/logs-archives/#grant-role-to-an-archive)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#grant-role-to-an-archive-v2)


POST https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}/readershttps://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers
### Overview
Adds a read role to an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) This endpoint requires the `logs_write_archives` permission.
### Arguments
#### Path Parameters
Name
Type
Description
archive_id [_required_]
string
The ID of the archive.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


Field
Type
Description
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "type": "roles"
  }
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-archives/#AddReadRoleToArchive-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#AddReadRoleToArchive-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#AddReadRoleToArchive-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-archives/#AddReadRoleToArchive-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#AddReadRoleToArchive-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Grant role to an archive
Copy
```
                  # Path parameters  
export archive_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}/readers" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Grant role to an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Grant role to an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Grant role to an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Grant role to an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Grant role to an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Grant role to an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Revoke role from an archive](https://docs.datadoghq.com/api/latest/logs-archives/#revoke-role-from-an-archive)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#revoke-role-from-an-archive-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.ap2.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.datadoghq.eu/api/v2/logs/config/archives/{archive_id}/readershttps://api.ddog-gov.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.us3.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readershttps://api.us5.datadoghq.com/api/v2/logs/config/archives/{archive_id}/readers
### Overview
Removes a role from an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) This endpoint requires the `logs_write_archives` permission.
### Arguments
#### Path Parameters
Name
Type
Description
archive_id [_required_]
string
The ID of the archive.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


Field
Type
Description
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "type": "roles"
  }
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-archives/#RemoveRoleFromArchive-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#RemoveRoleFromArchive-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#RemoveRoleFromArchive-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-archives/#RemoveRoleFromArchive-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#RemoveRoleFromArchive-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Revoke role from an archive
Copy
```
                  # Path parameters  
export archive_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archives/${archive_id}/readers" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Revoke role from an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Revoke role from an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Revoke role from an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Revoke role from an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Revoke role from an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Revoke role from an archive
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get archive order](https://docs.datadoghq.com/api/latest/logs-archives/#get-archive-order)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#get-archive-order-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.ap2.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.datadoghq.eu/api/v2/logs/config/archive-orderhttps://api.ddog-gov.com/api/v2/logs/config/archive-orderhttps://api.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.us3.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.us5.datadoghq.com/api/v2/logs/config/archive-order
### Overview
Get the current order of your archives. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchiveOrder-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchiveOrder-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#GetLogsArchiveOrder-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


A ordered list of archive IDs.
Field
Type
Description
data
object
The definition of an archive order.
attributes [_required_]
object
The attributes associated with the archive order.
archive_ids [_required_]
[string]
An ordered array of `<ARCHIVE_ID>` strings, the order of archive IDs in the array define the overall archives order for Datadog.
type [_required_]
enum
Type of the archive order definition. Allowed enum values: `archive_order`
default: `archive_order`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Get archive order
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archive-order" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get archive order
```
# Get archive order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsArchivesAPI.new
p api_instance.get_logs_archive_order()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update archive order](https://docs.datadoghq.com/api/latest/logs-archives/#update-archive-order)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-archives/#update-archive-order-v2)


PUT https://api.ap1.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.ap2.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.datadoghq.eu/api/v2/logs/config/archive-orderhttps://api.ddog-gov.com/api/v2/logs/config/archive-orderhttps://api.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.us3.datadoghq.com/api/v2/logs/config/archive-orderhttps://api.us5.datadoghq.com/api/v2/logs/config/archive-order
### Overview
Update the order of your archives. Since logs are processed sequentially, reordering an archive may change the structure and content of the data processed by other archives.
**Note** : Using the `PUT` method updates your archive’s order by replacing the current order with the new one.
This endpoint requires the `logs_write_archives` permission.
### Request
#### Body Data (required)
An object containing the new ordered list of archive IDs.
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


Field
Type
Description
data
object
The definition of an archive order.
attributes [_required_]
object
The attributes associated with the archive order.
archive_ids [_required_]
[string]
An ordered array of `<ARCHIVE_ID>` strings, the order of archive IDs in the array define the overall archives order for Datadog.
type [_required_]
enum
Type of the archive order definition. Allowed enum values: `archive_order`
default: `archive_order`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchiveOrder-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchiveOrder-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchiveOrder-403-v2)
  * [422](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchiveOrder-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-archives/#UpdateLogsArchiveOrder-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


A ordered list of archive IDs.
Field
Type
Description
data
object
The definition of an archive order.
attributes [_required_]
object
The attributes associated with the archive order.
archive_ids [_required_]
[string]
An ordered array of `<ARCHIVE_ID>` strings, the order of archive IDs in the array define the overall archives order for Datadog.
type [_required_]
enum
Type of the archive order definition. Allowed enum values: `archive_order`
default: `archive_order`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
Unprocessable Entity
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-archives/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-archives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-archives/?code-lang=typescript)


#####  Update archive order
Copy
```
                  # Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/archive-order" \
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

                
```

#####  Update archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update archive order
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=08b78d98-66d5-4336-b8d3-2e559efcef0e&bo=1&sid=ca97aff0f0bf11f0b225ebe7018368cd&vid=ca980060f0bf11f09385b797b877861f&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Logs%20Archives&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-archives%2F&r=&lt=2386&evt=pageLoad&sv=2&cdb=AQAQ&rn=858097)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=892cca82-d58a-46c9-91cf-7057e8326871&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=142a5ea7-c314-41ff-8288-28aa8ccd8278&pt=Logs%20Archives&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-archives%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=892cca82-d58a-46c9-91cf-7057e8326871&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=142a5ea7-c314-41ff-8288-28aa8ccd8278&pt=Logs%20Archives&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-archives%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
