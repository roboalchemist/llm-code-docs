# Source: https://docs.datadoghq.com/api/latest/logs.md

---
title: Logs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Logs
---

# Logs

Search your logs and send them to your Datadog platform over HTTP. See the [Log Management page](https://docs.datadoghq.com/logs/) for more information.

## Send logs{% #send-logs %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | POST https://http-intake.logs.ap1.datadoghq.com/v1/input |
| ap2.datadoghq.com | POST https://http-intake.logs.ap2.datadoghq.com/v1/input |
| app.datadoghq.eu  | POST https://http-intake.logs.datadoghq.eu/v1/input      |
| app.ddog-gov.com  | POST https://http-intake.logs.ddog-gov.com/v1/input      |
| app.datadoghq.com | POST https://http-intake.logs.datadoghq.com/v1/input     |
| us3.datadoghq.com | POST https://http-intake.logs.us3.datadoghq.com/v1/input |
| us5.datadoghq.com | POST https://http-intake.logs.us5.datadoghq.com/v1/input |

### Overview



Send your logs to your Datadog platform over HTTP. Limits per HTTP request are:

- Maximum content size per payload (uncompressed): 5MB
- Maximum size for a single log: 1MB
- Maximum array size if sending multiple logs in an array: 1000 entries

Any log exceeding 1MB is accepted and truncated by Datadog:

- For a single log request, the API truncates the log at 1MB and returns a 2xx.
- For a multi-logs request, the API processes all logs, truncates only logs larger than 1MB, and returns a 2xx.

Datadog recommends sending your logs compressed. Add the `Content-Encoding: gzip` header to the request when sending compressed logs.

The status codes answered by the HTTP API are:

- 200: OK
- 400: Bad request (likely an issue in the payload formatting)
- 403: Permission issue (likely using an invalid API Key)
- 413: Payload too large (batch is above 5MB uncompressed)
- 5xx: Internal error, request should be retried after some time



### Arguments

#### Query Strings

| Name   | Type   | Description                                                                |
| ------ | ------ | -------------------------------------------------------------------------- |
| ddtags | string | Log tags can be passed as query parameters with `text/plain` content type. |

#### Header Parameters

| Name             | Type   | Description                                  |
| ---------------- | ------ | -------------------------------------------- |
| Content-Encoding | string | HTTP header used to compress the media-type. |

### Request

#### Body Data (required)

Log to send (JSON format).

{% tab title="Model" %}

| Field    | Type   | Description                                                                                                                                                                                                                                                                                                              |
| -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ddsource | string | The integration name associated with your log: the technology from which the log originated. When it matches an integration name, Datadog automatically installs the corresponding parsers and facets. See [reserved attributes](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes).                   |
| ddtags   | string | Tags associated with your logs.                                                                                                                                                                                                                                                                                          |
| hostname | string | The name of the originating host of the log.                                                                                                                                                                                                                                                                             |
| message  | string | The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. |
| service  | string | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products. See [reserved attributes](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes).                                              |

{% /tab %}

{% tab title="Example" %}
##### 

```json
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
```

##### 

```json
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
```

##### 

```json
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
```

{% /tab %}

{% tab title="Model" %}

| Field    | Type   | Description                                                                                                                                                                                                                                                                                                              |
| -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ddsource | string | The integration name associated with your log: the technology from which the log originated. When it matches an integration name, Datadog automatically installs the corresponding parsers and facets. See [reserved attributes](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes).                   |
| ddtags   | string | Tags associated with your logs.                                                                                                                                                                                                                                                                                          |
| hostname | string | The name of the originating host of the log.                                                                                                                                                                                                                                                                             |
| message  | string | The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. |
| service  | string | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products. See [reserved attributes](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes).                                              |

{% /tab %}

{% tab title="Example" %}
##### 

```json
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
```

##### 

```json
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
```

##### 

```json
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
```

{% /tab %}

### Response

{% tab title="200" %}
Response from server (always 200 empty JSON).
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
unexpected error
{% tab title="Model" %}
Invalid query performed.

| Field                     | Type   | Description    |
| ------------------------- | ------ | -------------- |
| code [*required*]    | int32  | Error code.    |
| message [*required*] | string | Error message. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "code": 0,
  "message": "Your browser sent an invalid request."
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                          \## Multi JSON Messages
# Pass multiple log objects at once.
See one of the other client libraries for an example of sending deflate-compressed data.\## Simple JSON Message
# Log attributes can be passed as `key:value` pairs in valid JSON messages.
See one of the other client libraries for an example of sending deflate-compressed data.\## Multi Logplex Messages
# Submit log messages.
See one of the other client libraries for an example of sending deflate-compressed data.\## Simple Logplex Message
# Submit log string.
See one of the other client libraries for an example of sending deflate-compressed data.\## Multi Raw Messages
# Submit log string.
See one of the other client libraries for an example of sending deflate-compressed data.\## Simple Raw Message
# Submit log string. Log attributes can be passed as query parameters in the URL. This enables the addition of tags or the source by using the `ddtags` and `ddsource` parameters: `?host=my-hostname&service=my-service&ddsource=my-source&ddtags=env:prod,user:my-user`.
See one of the other client libraries for an example of sending deflate-compressed data.
                        
##### 
                          \## Multi JSON Messages
# Pass multiple log objects at once.
\# Curl commandecho $(cat << EOF
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Simple JSON Message
# Log attributes can be passed as `key:value` pairs in valid JSON messages.
\# Curl commandecho $(cat << EOF
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/json;simple" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Multi Logplex Messages
# Submit log messages.
\# Curl commandecho $(cat << EOF
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Simple Logplex Message
# Submit log string.
\# Curl commandecho $(cat << EOF
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Multi Raw Messages
# Submit log string.
\# Curl commandecho $(cat << EOF
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Simple Raw Message
# Submit log string. Log attributes can be passed as query parameters in the URL. This enables the addition of tags or the source by using the `ddtags` and `ddsource` parameters: `?host=my-hostname&service=my-service&ddsource=my-source&ddtags=env:prod,user:my-user`.
\# Curl commandecho $(cat << EOF
[
  {
    "message": "Example-Log",
    "ddtags": "host:ExampleLog"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-
                        
##### 
                          \## Multi JSON Messages
# Pass multiple log objects at once.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
[
  {
    "message": "hello"
  },
  {
    "message": "world"
  }
]
EOF\## Simple JSON Message
# Log attributes can be passed as `key:value` pairs in valid JSON messages.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/json;simple" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "ddsource": "agent",
  "ddtags": "env:prod,user:joe.doe",
  "hostname": "fa1e1e739d95",
  "message": "hello world"
}
EOF\## Multi Logplex Messages
# Submit log messages.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
hello
world
EOF\## Simple Logplex Message
# Submit log string.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
hello world
EOF\## Multi Raw Messages
# Submit log string.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
hello
world
EOF\## Simple Raw Message
# Submit log string. Log attributes can be passed as query parameters in the URL. This enables the addition of tags or the source by using the `ddtags` and `ddsource` parameters: `?host=my-hostname&service=my-service&ddsource=my-source&ddtags=env:prod,user:my-user`.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/v1/input" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
hello world
EOF
                        
##### 

```go
// Send deflate logs returns "Response from server (always 200 empty JSON)." response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := []datadogV1.HTTPLogItem{
		{
			Message: "Example-Log",
			Ddtags:  datadog.PtrString("host:ExampleLog"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsApi(apiClient)
	resp, r, err := api.SubmitLog(ctx, body, *datadogV1.NewSubmitLogOptionalParameters().WithContentEncoding(datadogV1.CONTENTENCODING_DEFLATE))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.SubmitLog`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.SubmitLog`:\n%s\n", responseContent)
}
```

##### 

```go
// Send gzip logs returns "Response from server (always 200 empty JSON)." response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := []datadogV1.HTTPLogItem{
		{
			Message: "Example-Log",
			Ddtags:  datadog.PtrString("host:ExampleLog"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsApi(apiClient)
	resp, r, err := api.SubmitLog(ctx, body, *datadogV1.NewSubmitLogOptionalParameters().WithContentEncoding(datadogV1.CONTENTENCODING_GZIP))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.SubmitLog`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.SubmitLog`:\n%s\n", responseContent)
}
```

##### 

```go
// Send logs returns "Response from server (always 200 empty JSON)." response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := []datadogV1.HTTPLogItem{
		{
			Message: "Example-Log",
			Ddtags:  datadog.PtrString("host:ExampleLog"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsApi(apiClient)
	resp, r, err := api.SubmitLog(ctx, body, *datadogV1.NewSubmitLogOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.SubmitLog`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.SubmitLog`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
##### 

```java
// Send deflate logs returns "Response from server (always 200 empty JSON)." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsApi;
import com.datadog.api.client.v1.api.LogsApi.SubmitLogOptionalParameters;
import com.datadog.api.client.v1.model.ContentEncoding;
import com.datadog.api.client.v1.model.HTTPLogItem;
import java.util.Collections;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    List<HTTPLogItem> body =
        Collections.singletonList(
            new HTTPLogItem().message("Example-Log").ddtags("host:ExampleLog"));

    try {
      apiInstance.submitLog(
          body, new SubmitLogOptionalParameters().contentEncoding(ContentEncoding.DEFLATE));
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#submitLog");
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
// Send gzip logs returns "Response from server (always 200 empty JSON)." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsApi;
import com.datadog.api.client.v1.api.LogsApi.SubmitLogOptionalParameters;
import com.datadog.api.client.v1.model.ContentEncoding;
import com.datadog.api.client.v1.model.HTTPLogItem;
import java.util.Collections;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    List<HTTPLogItem> body =
        Collections.singletonList(
            new HTTPLogItem().message("Example-Log").ddtags("host:ExampleLog"));

    try {
      apiInstance.submitLog(
          body, new SubmitLogOptionalParameters().contentEncoding(ContentEncoding.GZIP));
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#submitLog");
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
// Send logs returns "Response from server (always 200 empty JSON)." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsApi;
import com.datadog.api.client.v1.model.HTTPLogItem;
import java.util.Collections;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    List<HTTPLogItem> body =
        Collections.singletonList(
            new HTTPLogItem().message("Example-Log").ddtags("host:ExampleLog"));

    try {
      apiInstance.submitLog(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#submitLog");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
##### 

```python
"""
Send deflate logs returns "Response from server (always 200 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.content_encoding import ContentEncoding
from datadog_api_client.v1.model.http_log import HTTPLog
from datadog_api_client.v1.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            message="Example-Log",
            ddtags="host:ExampleLog",
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(content_encoding=ContentEncoding.DEFLATE, body=body)

    print(response)
```

##### 

```python
"""
Send gzip logs returns "Response from server (always 200 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.content_encoding import ContentEncoding
from datadog_api_client.v1.model.http_log import HTTPLog
from datadog_api_client.v1.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            message="Example-Log",
            ddtags="host:ExampleLog",
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(content_encoding=ContentEncoding.GZIP, body=body)

    print(response)
```

##### 

```python
"""
Send logs returns "Response from server (always 200 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.http_log import HTTPLog
from datadog_api_client.v1.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            message="Example-Log",
            ddtags="host:ExampleLog",
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
##### 

```ruby
# Send deflate logs returns "Response from server (always 200 empty JSON)." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsAPI.new

body = [
  DatadogAPIClient::V1::HTTPLogItem.new({
    message: "Example-Log",
    ddtags: "host:ExampleLog",
  }),
]
opts = {
  content_encoding: ContentEncoding::DEFLATE,
}
p api_instance.submit_log(body, opts)
```

##### 

```ruby
# Send gzip logs returns "Response from server (always 200 empty JSON)." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsAPI.new

body = [
  DatadogAPIClient::V1::HTTPLogItem.new({
    message: "Example-Log",
    ddtags: "host:ExampleLog",
  }),
]
opts = {
  content_encoding: ContentEncoding::GZIP,
}
p api_instance.submit_log(body, opts)
```

##### 

```ruby
# Send logs returns "Response from server (always 200 empty JSON)." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsAPI.new

body = [
  DatadogAPIClient::V1::HTTPLogItem.new({
    message: "Example-Log",
    ddtags: "host:ExampleLog",
  }),
]
p api_instance.submit_log(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```rust
// Send deflate logs returns "Response from server (always 200 empty JSON)."
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs::LogsAPI;
use datadog_api_client::datadogV1::api_logs::SubmitLogOptionalParams;
use datadog_api_client::datadogV1::model::ContentEncoding;
use datadog_api_client::datadogV1::model::HTTPLogItem;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = vec![HTTPLogItem::new("Example-Log".to_string())
        .ddtags("host:ExampleLog".to_string())
        .additional_properties(BTreeMap::from([]))];
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .submit_log(
            body,
            SubmitLogOptionalParams::default().content_encoding(ContentEncoding::DEFLATE),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Send gzip logs returns "Response from server (always 200 empty JSON)." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs::LogsAPI;
use datadog_api_client::datadogV1::api_logs::SubmitLogOptionalParams;
use datadog_api_client::datadogV1::model::ContentEncoding;
use datadog_api_client::datadogV1::model::HTTPLogItem;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = vec![HTTPLogItem::new("Example-Log".to_string())
        .ddtags("host:ExampleLog".to_string())
        .additional_properties(BTreeMap::from([]))];
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .submit_log(
            body,
            SubmitLogOptionalParams::default().content_encoding(ContentEncoding::GZIP),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Send logs returns "Response from server (always 200 empty JSON)." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs::LogsAPI;
use datadog_api_client::datadogV1::api_logs::SubmitLogOptionalParams;
use datadog_api_client::datadogV1::model::HTTPLogItem;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = vec![HTTPLogItem::new("Example-Log".to_string())
        .ddtags("host:ExampleLog".to_string())
        .additional_properties(BTreeMap::from([]))];
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .submit_log(body, SubmitLogOptionalParams::default())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
##### 

```typescript
/**
 * Send deflate logs returns "Response from server (always 200 empty JSON)." response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsApi(configuration);

const params: v1.LogsApiSubmitLogRequest = {
  body: [
    {
      message: "Example-Log",
      ddtags: "host:ExampleLog",
    },
  ],
  contentEncoding: "deflate",
};

apiInstance
  .submitLog(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Send gzip logs returns "Response from server (always 200 empty JSON)." response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsApi(configuration);

const params: v1.LogsApiSubmitLogRequest = {
  body: [
    {
      message: "Example-Log",
      ddtags: "host:ExampleLog",
    },
  ],
  contentEncoding: "gzip",
};

apiInstance
  .submitLog(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Send logs returns "Response from server (always 200 empty JSON)." response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsApi(configuration);

const params: v1.LogsApiSubmitLogRequest = {
  body: [
    {
      message: "Example-Log",
      ddtags: "host:ExampleLog",
    },
  ],
};

apiInstance
  .submitLog(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | POST https://http-intake.logs.ap1.datadoghq.com/api/v2/logs |
| ap2.datadoghq.com | POST https://http-intake.logs.ap2.datadoghq.com/api/v2/logs |
| app.datadoghq.eu  | POST https://http-intake.logs.datadoghq.eu/api/v2/logs      |
| app.ddog-gov.com  | POST https://http-intake.logs.ddog-gov.com/api/v2/logs      |
| app.datadoghq.com | POST https://http-intake.logs.datadoghq.com/api/v2/logs     |
| us3.datadoghq.com | POST https://http-intake.logs.us3.datadoghq.com/api/v2/logs |
| us5.datadoghq.com | POST https://http-intake.logs.us5.datadoghq.com/api/v2/logs |

### Overview



Send your logs to your Datadog platform over HTTP. Limits per HTTP request are:

- Maximum content size per payload (uncompressed): 5MB
- Maximum size for a single log: 1MB
- Maximum array size if sending multiple logs in an array: 1000 entries

Any log exceeding 1MB is accepted and truncated by Datadog:

- For a single log request, the API truncates the log at 1MB and returns a 2xx.
- For a multi-logs request, the API processes all logs, truncates only logs larger than 1MB, and returns a 2xx.

Datadog recommends sending your logs compressed. Add the `Content-Encoding: gzip` header to the request when sending compressed logs. Log events can be submitted with a timestamp that is up to 18 hours in the past.

The status codes answered by the HTTP API are:

- 202: Accepted: the request has been accepted for processing
- 400: Bad request (likely an issue in the payload formatting)
- 401: Unauthorized (likely a missing API Key)
- 403: Permission issue (likely using an invalid API Key)
- 408: Request Timeout, request should be retried after some time
- 413: Payload too large (batch is above 5MB uncompressed)
- 429: Too Many Requests, request should be retried after some time
- 500: Internal Server Error, the server encountered an unexpected condition that prevented it from fulfilling the request, request should be retried after some time
- 503: Service Unavailable, the server is not ready to handle the request probably because it is overloaded, request should be retried after some time



### Arguments

#### Query Strings

| Name   | Type   | Description                                                                |
| ------ | ------ | -------------------------------------------------------------------------- |
| ddtags | string | Log tags can be passed as query parameters with `text/plain` content type. |

#### Header Parameters

| Name             | Type   | Description                                  |
| ---------------- | ------ | -------------------------------------------- |
| Content-Encoding | string | HTTP header used to compress the media-type. |

### Request

#### Body Data (required)

Log to send (JSON format).

{% tab title="Model" %}

| Field    | Type   | Description                                                                                                                                                                                                                                                                                                                                              |
| -------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ddsource | string | The integration name associated with your log: the technology from which the log originated. When it matches an integration name, Datadog automatically installs the corresponding parsers and facets. See [reserved attributes](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes).                   |
| ddtags   | string | Tags associated with your logs.                                                                                                                                                                                                                                                                                                                          |
| hostname | string | The name of the originating host of the log.                                                                                                                                                                                                                                                                                                             |
| message  | string | The message [reserved attribute](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. |
| service  | string | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products. See [reserved attributes](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes).                                              |

{% /tab %}

{% tab title="Example" %}
##### 

```json
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
```

##### 

```json
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
```

##### 

```json
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment",
    "status": "info"
  }
]
```

{% /tab %}

### Response

{% tab title="202" %}
Request accepted for processing (always 202 empty JSON).
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="408" %}
Request Timeout
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="413" %}
Payload Too Large
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too Many Requests
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="503" %}
Service Unavailable
{% tab title="Model" %}
Invalid query performed.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                          \## Multi JSON Messages
# Pass multiple log objects at once.
See one of the other client libraries for an example of sending deflate-compressed data.\## Simple JSON Message
# Log attributes can be passed as `key:value` pairs in valid JSON messages.
See one of the other client libraries for an example of sending deflate-compressed data.\## Multi Logplex Messages
# Submit log messages.
See one of the other client libraries for an example of sending deflate-compressed data.\## Simple Logplex Message
# Submit log string.
See one of the other client libraries for an example of sending deflate-compressed data.\## Multi Raw Messages
# Submit log string.
See one of the other client libraries for an example of sending deflate-compressed data.\## Simple Raw Message
# Submit log string. Log attributes can be passed as query parameters in the URL. This enables the addition of tags or the source by using the `ddtags` and `ddsource` parameters: `?host=my-hostname&service=my-service&ddsource=my-source&ddtags=env:prod,user:my-user`.
See one of the other client libraries for an example of sending deflate-compressed data.
                        
##### 
                          \## Multi JSON Messages
# Pass multiple log objects at once.
\# Curl commandecho $(cat << EOF
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Simple JSON Message
# Log attributes can be passed as `key:value` pairs in valid JSON messages.
\# Curl commandecho $(cat << EOF
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Multi Logplex Messages
# Submit log messages.
\# Curl commandecho $(cat << EOF
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Simple Logplex Message
# Submit log string.
\# Curl commandecho $(cat << EOF
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Multi Raw Messages
# Submit log string.
\# Curl commandecho $(cat << EOF
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-\## Simple Raw Message
# Submit log string. Log attributes can be passed as query parameters in the URL. This enables the addition of tags or the source by using the `ddtags` and `ddsource` parameters: `?host=my-hostname&service=my-service&ddsource=my-source&ddtags=env:prod,user:my-user`.
\# Curl commandecho $(cat << EOF
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    "service": "payment"
  }
]
EOF
) | gzip | curl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "Content-Encoding: gzip" \
-H "DD-API-KEY: ${DD_API_KEY}" \
--data-binary @-
                        
##### 
                          \## Multi JSON Messages
# Pass multiple log objects at once.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
[
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345678",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello",
    "service": "payment"
  },
  {
    "ddsource": "nginx",
    "ddtags": "env:staging,version:5.1",
    "hostname": "i-012345679",
    "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] World",
    "service": "payment"
  }
]
EOF\## Simple JSON Message
# Log attributes can be passed as `key:value` pairs in valid JSON messages.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "ddsource": "nginx",
  "ddtags": "env:staging,version:5.1",
  "hostname": "i-012345678",
  "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
  "service": "payment"
}
EOF\## Multi Logplex Messages
# Submit log messages.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
2019-11-19T14:37:58,995 INFO [process.name][20081] Hello
2019-11-19T14:37:58,995 INFO [process.name][20081] World
EOF\## Simple Logplex Message
# Submit log string.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: application/logplex-1" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World
EOF\## Multi Raw Messages
# Submit log string.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
2019-11-19T14:37:58,995 INFO [process.name][20081] Hello
2019-11-19T14:37:58,995 INFO [process.name][20081] World
EOF\## Simple Raw Message
# Submit log string. Log attributes can be passed as query parameters in the URL. This enables the addition of tags or the source by using the `ddtags` and `ddsource` parameters: `?host=my-hostname&service=my-service&ddsource=my-source&ddtags=env:prod,user:my-user`.
\# Curl commandcurl -X POST "https://http-intake.logs.ap1.datadoghq.com"https://http-intake.logs.ap2.datadoghq.com"https://http-intake.logs.datadoghq.eu"https://http-intake.logs.ddog-gov.com"https://http-intake.logs.datadoghq.com"https://http-intake.logs.us3.datadoghq.com"https://http-intake.logs.us5.datadoghq.com/api/v2/logs" \
-H "Accept: application/json" \
-H "Content-Type: text/plain" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World
EOF
                        
##### 

```go
// Send deflate logs returns "Request accepted for processing (always 202 empty JSON)." response

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
	body := []datadogV2.HTTPLogItem{
		{
			Ddsource: datadog.PtrString("nginx"),
			Ddtags:   datadog.PtrString("env:staging,version:5.1"),
			Hostname: datadog.PtrString("i-012345678"),
			Message:  "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
			Service:  datadog.PtrString("payment"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.SubmitLog(ctx, body, *datadogV2.NewSubmitLogOptionalParameters().WithContentEncoding(datadogV2.CONTENTENCODING_DEFLATE))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.SubmitLog`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.SubmitLog`:\n%s\n", responseContent)
}
```

##### 

```go
// Send gzip logs returns "Request accepted for processing (always 202 empty JSON)." response

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
	body := []datadogV2.HTTPLogItem{
		{
			Ddsource: datadog.PtrString("nginx"),
			Ddtags:   datadog.PtrString("env:staging,version:5.1"),
			Hostname: datadog.PtrString("i-012345678"),
			Message:  "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
			Service:  datadog.PtrString("payment"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.SubmitLog(ctx, body, *datadogV2.NewSubmitLogOptionalParameters().WithContentEncoding(datadogV2.CONTENTENCODING_GZIP))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.SubmitLog`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.SubmitLog`:\n%s\n", responseContent)
}
```

##### 

```go
// Send logs returns "Request accepted for processing (always 202 empty JSON)." response

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
	body := []datadogV2.HTTPLogItem{
		{
			Ddsource: datadog.PtrString("nginx"),
			Ddtags:   datadog.PtrString("env:staging,version:5.1"),
			Hostname: datadog.PtrString("i-012345678"),
			Message:  "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
			Service:  datadog.PtrString("payment"),
			AdditionalProperties: map[string]interface{}{
				"status": "info",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.SubmitLog(ctx, body, *datadogV2.NewSubmitLogOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.SubmitLog`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.SubmitLog`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
##### 

```java
// Send deflate logs returns "Request accepted for processing (always 202 empty JSON)." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.api.LogsApi.SubmitLogOptionalParameters;
import com.datadog.api.client.v2.model.ContentEncoding;
import com.datadog.api.client.v2.model.HTTPLogItem;
import java.util.Collections;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    List<HTTPLogItem> body =
        Collections.singletonList(
            new HTTPLogItem()
                .ddsource("nginx")
                .ddtags("env:staging,version:5.1")
                .hostname("i-012345678")
                .message("2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World")
                .service("payment"));

    try {
      apiInstance.submitLog(
          body, new SubmitLogOptionalParameters().contentEncoding(ContentEncoding.DEFLATE));
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#submitLog");
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
// Send gzip logs returns "Request accepted for processing (always 202 empty JSON)." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.api.LogsApi.SubmitLogOptionalParameters;
import com.datadog.api.client.v2.model.ContentEncoding;
import com.datadog.api.client.v2.model.HTTPLogItem;
import java.util.Collections;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    List<HTTPLogItem> body =
        Collections.singletonList(
            new HTTPLogItem()
                .ddsource("nginx")
                .ddtags("env:staging,version:5.1")
                .hostname("i-012345678")
                .message("2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World")
                .service("payment"));

    try {
      apiInstance.submitLog(
          body, new SubmitLogOptionalParameters().contentEncoding(ContentEncoding.GZIP));
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#submitLog");
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
// Send logs returns "Request accepted for processing (always 202 empty JSON)." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.model.HTTPLogItem;
import java.util.Collections;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    List<HTTPLogItem> body =
        Collections.singletonList(
            new HTTPLogItem()
                .ddsource("nginx")
                .ddtags("env:staging,version:5.1")
                .hostname("i-012345678")
                .message("2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World")
                .service("payment")
                .putAdditionalProperty("status", "info"));

    try {
      apiInstance.submitLog(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#submitLog");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
##### 

```python
"""
Send deflate logs returns "Request accepted for processing (always 202 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.content_encoding import ContentEncoding
from datadog_api_client.v2.model.http_log import HTTPLog
from datadog_api_client.v2.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
            service="payment",
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(content_encoding=ContentEncoding.DEFLATE, body=body)

    print(response)
```

##### 

```python
"""
Send gzip logs returns "Request accepted for processing (always 202 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.content_encoding import ContentEncoding
from datadog_api_client.v2.model.http_log import HTTPLog
from datadog_api_client.v2.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
            service="payment",
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(content_encoding=ContentEncoding.GZIP, body=body)

    print(response)
```

##### 

```python
"""
Send logs returns "Request accepted for processing (always 202 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.http_log import HTTPLog
from datadog_api_client.v2.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
            service="payment",
            status="info",
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
##### 

```ruby
# Send deflate logs returns "Request accepted for processing (always 202 empty JSON)." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = [
  DatadogAPIClient::V2::HTTPLogItem.new({
    ddsource: "nginx",
    ddtags: "env:staging,version:5.1",
    hostname: "i-012345678",
    message: "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    service: "payment",
  }),
]
opts = {
  content_encoding: ContentEncoding::DEFLATE,
}
p api_instance.submit_log(body, opts)
```

##### 

```ruby
# Send gzip logs returns "Request accepted for processing (always 202 empty JSON)." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = [
  DatadogAPIClient::V2::HTTPLogItem.new({
    ddsource: "nginx",
    ddtags: "env:staging,version:5.1",
    hostname: "i-012345678",
    message: "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    service: "payment",
  }),
]
opts = {
  content_encoding: ContentEncoding::GZIP,
}
p api_instance.submit_log(body, opts)
```

##### 

```ruby
# Send logs returns "Request accepted for processing (always 202 empty JSON)." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = [
  DatadogAPIClient::V2::HTTPLogItem.new({
    ddsource: "nginx",
    ddtags: "env:staging,version:5.1",
    hostname: "i-012345678",
    message: "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
    service: "payment",
    status: "info",
  }),
]
p api_instance.submit_log(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```rust
// Send deflate logs returns "Request accepted for processing (always 202 empty
// JSON)." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::api_logs::SubmitLogOptionalParams;
use datadog_api_client::datadogV2::model::ContentEncoding;
use datadog_api_client::datadogV2::model::HTTPLogItem;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = vec![HTTPLogItem::new(
        "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World".to_string(),
    )
    .ddsource("nginx".to_string())
    .ddtags("env:staging,version:5.1".to_string())
    .hostname("i-012345678".to_string())
    .service("payment".to_string())
    .additional_properties(BTreeMap::from([]))];
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .submit_log(
            body,
            SubmitLogOptionalParams::default().content_encoding(ContentEncoding::DEFLATE),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Send gzip logs returns "Request accepted for processing (always 202 empty
// JSON)." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::api_logs::SubmitLogOptionalParams;
use datadog_api_client::datadogV2::model::ContentEncoding;
use datadog_api_client::datadogV2::model::HTTPLogItem;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = vec![HTTPLogItem::new(
        "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World".to_string(),
    )
    .ddsource("nginx".to_string())
    .ddtags("env:staging,version:5.1".to_string())
    .hostname("i-012345678".to_string())
    .service("payment".to_string())
    .additional_properties(BTreeMap::from([]))];
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .submit_log(
            body,
            SubmitLogOptionalParams::default().content_encoding(ContentEncoding::GZIP),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Send logs returns "Request accepted for processing (always 202 empty JSON)."
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::api_logs::SubmitLogOptionalParams;
use datadog_api_client::datadogV2::model::HTTPLogItem;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = vec![HTTPLogItem::new(
        "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World".to_string(),
    )
    .ddsource("nginx".to_string())
    .ddtags("env:staging,version:5.1".to_string())
    .hostname("i-012345678".to_string())
    .service("payment".to_string())
    .additional_properties(BTreeMap::from([(
        "status".to_string(),
        Value::from("info"),
    )]))];
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .submit_log(body, SubmitLogOptionalParams::default())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
##### 

```typescript
/**
 * Send deflate logs returns "Request accepted for processing (always 202 empty JSON)." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiSubmitLogRequest = {
  body: [
    {
      ddsource: "nginx",
      ddtags: "env:staging,version:5.1",
      hostname: "i-012345678",
      message: "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
      service: "payment",
    },
  ],
  contentEncoding: "deflate",
};

apiInstance
  .submitLog(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Send gzip logs returns "Request accepted for processing (always 202 empty JSON)." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiSubmitLogRequest = {
  body: [
    {
      ddsource: "nginx",
      ddtags: "env:staging,version:5.1",
      hostname: "i-012345678",
      message: "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
      service: "payment",
    },
  ],
  contentEncoding: "gzip",
};

apiInstance
  .submitLog(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Send logs returns "Request accepted for processing (always 202 empty JSON)." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiSubmitLogRequest = {
  body: [
    {
      ddsource: "nginx",
      ddtags: "env:staging,version:5.1",
      hostname: "i-012345678",
      message: "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
      service: "payment",
      additionalProperties: {
        status: "info",
      },
    },
  ],
};

apiInstance
  .submitLog(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}

## Aggregate events{% #aggregate-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/analytics/aggregate |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/analytics/aggregate |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/analytics/aggregate      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/analytics/aggregate      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/analytics/aggregate     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/analytics/aggregate |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/analytics/aggregate |

### Overview

The API endpoint to aggregate events into buckets and compute metrics and timeseries. This endpoint requires the `logs_read_data` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                         | Type          | Description                                                                                                                                                            |
| ------------ | ----------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | compute                       | [object]      | The list of metrics or timeseries to compute for the retrieved buckets.                                                                                                |
| compute      | aggregation [*required*] | enum          | An aggregation function Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`                                                       |
| compute      | interval                      | string        | The time buckets' size (only used for type=timeseries) Defaults to a resolution of 150 points                                                                          |
| compute      | metric                        | string        | The metric to use                                                                                                                                                      |
| compute      | type                          | enum          | The type of compute Allowed enum values: `timeseries,total`                                                                                                            |
|              | filter                        | object        | The search and filter query settings                                                                                                                                   |
| filter       | from                          | string        | The minimum time for the requested logs, supports date math and regular timestamps (milliseconds).                                                                     |
| filter       | indexes                       | [string]      | For customers with multiple indexes, the indexes to search. Defaults to ['*'] which means all indexes.                                                                 |
| filter       | query                         | string        | The search query - following the log search syntax.                                                                                                                    |
| filter       | storage_tier                  | enum          | Specifies storage type as indexes, online-archives or flex Allowed enum values: `indexes,online-archives,flex`                                                         |
| filter       | to                            | string        | The maximum time for the requested logs, supports date math and regular timestamps (milliseconds).                                                                     |
|              | group_by                      | [object]      | The rules for the group by                                                                                                                                             |
| group_by     | facet [*required*]       | string        | The name of the facet to use (required)                                                                                                                                |
| group_by     | histogram                     | object        | Used to perform a histogram computation (only for measure facets). Note: at most 100 buckets are allowed, the number of buckets is (max - min)/interval.               |
| histogram    | interval [*required*]    | double        | The bin size of the histogram buckets                                                                                                                                  |
| histogram    | max [*required*]         | double        | The maximum value for the measure used in the histogram (values greater than this one are filtered out)                                                                |
| histogram    | min [*required*]         | double        | The minimum value for the measure used in the histogram (values smaller than this one are filtered out)                                                                |
| group_by     | limit                         | int64         | The maximum buckets to return for this group by. Note: at most 10000 buckets are allowed. If grouping by multiple facets, the product of limits must not exceed 10000. |
| group_by     | missing                       |  <oneOf> | The value to use for logs that don't have the facet used to group by                                                                                                   |
| missing      | Option 1                      | string        | The missing value to use if there is string valued facet.                                                                                                              |
| missing      | Option 2                      | double        | The missing value to use if there is a number valued facet.                                                                                                            |
| group_by     | sort                          | object        | A sort rule                                                                                                                                                            |
| sort         | aggregation                   | enum          | An aggregation function Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`                                                       |
| sort         | metric                        | string        | The metric to sort by (only used for `type=measure`)                                                                                                                   |
| sort         | order                         | enum          | The order to use, ascending or descending Allowed enum values: `asc,desc`                                                                                              |
| sort         | type                          | enum          | The type of sorting algorithm Allowed enum values: `alphabetical,measure`                                                                                              |
| group_by     | total                         |  <oneOf> | A resulting object to put the given computes in over all the matching records.                                                                                         |
| total        | Option 1                      | boolean       | If set to true, creates an additional bucket labeled "$facet_total"                                                                                                    |
| total        | Option 2                      | string        | A string to use as the key value for the total bucket                                                                                                                  |
| total        | Option 3                      | double        | A number to use as the key value for the total bucket                                                                                                                  |
|              | options                       | object        | **DEPRECATED**: Global query options that are used during the query. Note: These fields are currently deprecated and do not affect the query results.                  |
| options      | timeOffset                    | int64         | The time offset (in seconds) to apply to the query.                                                                                                                    |
| options      | timezone                      | string        | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).                              |
|              | page                          | object        | Paging settings                                                                                                                                                        |
| page         | cursor                        | string        | The returned paging point to use to get the next results. Note: at most 1000 results can be paged.                                                                     |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "compute": [
    {
      "aggregation": "count",
      "interval": "5m",
      "type": "timeseries"
    }
  ],
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "query": "*",
    "to": "now"
  }
}
```

##### 

```json
{
  "compute": [
    {
      "aggregation": "count",
      "interval": "5m",
      "type": "timeseries"
    }
  ],
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "query": "*",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "host",
      "missing": "miss",
      "sort": {
        "type": "measure",
        "order": "asc",
        "aggregation": "pc90",
        "metric": "@duration"
      }
    }
  ]
}
```

##### 

```json
{
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "query": "*",
    "to": "now"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object for the logs aggregate API endpoint

| Parent field         | Field      | Type          | Description                                                                                                                                   |
| -------------------- | ---------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data       | object        | The query results                                                                                                                             |
| data                 | buckets    | [object]      | The list of matching buckets, one item per bucket                                                                                             |
| buckets              | by         | object        | The key, value pairs for each group by                                                                                                        |
| additionalProperties | <any-key>  |               | The values for each group by                                                                                                                  |
| buckets              | computes   | object        | A map of the metric name -> value for regular compute or list of values for a timeseries                                                      |
| additionalProperties | <any-key>  |  <oneOf> | A bucket value, can be either a timeseries or a single value                                                                                  |
| <any-key>            | Option 1   | string        | A single string value                                                                                                                         |
| <any-key>            | Option 2   | double        | A single number value                                                                                                                         |
| <any-key>            | Option 3   | [object]      | A timeseries array                                                                                                                            |
| Option 3             | time       | string        | The time value for this point                                                                                                                 |
| Option 3             | value      | double        | The value for this point                                                                                                                      |
|                      | meta       | object        | The metadata associated with a request                                                                                                        |
| meta                 | elapsed    | int64         | The time elapsed in milliseconds                                                                                                              |
| meta                 | page       | object        | Paging attributes.                                                                                                                            |
| page                 | after      | string        | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`. |
| meta                 | request_id | string        | The identifier of the request                                                                                                                 |
| meta                 | status     | enum          | The status of the response Allowed enum values: `done,timeout`                                                                                |
| meta                 | warnings   | [object]      | A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.                 |
| warnings             | code       | string        | A unique code for this type of warning                                                                                                        |
| warnings             | detail     | string        | A detailed explanation of this specific warning                                                                                               |
| warnings             | title      | string        | A short human-readable summary of the warning                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "buckets": [
      {
        "by": {
          "<any-key>": "undefined"
        },
        "computes": {
          "<any-key>": {
            "description": "undefined",
            "type": "undefined"
          }
        }
      }
    ]
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
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
Not Authorized
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/analytics/aggregate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "compute": [
    {
      "aggregation": "count",
      "interval": "5m",
      "type": "timeseries"
    }
  ],
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "query": "*",
    "to": "now"
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/analytics/aggregate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "compute": [
    {
      "aggregation": "count",
      "interval": "5m",
      "type": "timeseries"
    }
  ],
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "query": "*",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "host",
      "missing": "miss",
      "sort": {
        "type": "measure",
        "order": "asc",
        "aggregation": "pc90",
        "metric": "@duration"
      }
    }
  ]
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/analytics/aggregate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "query": "*",
    "to": "now"
  }
}
EOF
                        
##### 

```go
// Aggregate compute events returns "OK" response

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
	body := datadogV2.LogsAggregateRequest{
		Compute: []datadogV2.LogsCompute{
			{
				Aggregation: datadogV2.LOGSAGGREGATIONFUNCTION_COUNT,
				Interval:    datadog.PtrString("5m"),
				Type:        datadogV2.LOGSCOMPUTETYPE_TIMESERIES.Ptr(),
			},
		},
		Filter: &datadogV2.LogsQueryFilter{
			From: datadog.PtrString("now-15m"),
			Indexes: []string{
				"main",
			},
			Query: datadog.PtrString("*"),
			To:    datadog.PtrString("now"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.AggregateLogs(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.AggregateLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.AggregateLogs`:\n%s\n", responseContent)
}
```

##### 

```go
// Aggregate compute events with group by returns "OK" response

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
	body := datadogV2.LogsAggregateRequest{
		Compute: []datadogV2.LogsCompute{
			{
				Aggregation: datadogV2.LOGSAGGREGATIONFUNCTION_COUNT,
				Interval:    datadog.PtrString("5m"),
				Type:        datadogV2.LOGSCOMPUTETYPE_TIMESERIES.Ptr(),
			},
		},
		Filter: &datadogV2.LogsQueryFilter{
			From: datadog.PtrString("now-15m"),
			Indexes: []string{
				"main",
			},
			Query: datadog.PtrString("*"),
			To:    datadog.PtrString("now"),
		},
		GroupBy: []datadogV2.LogsGroupBy{
			{
				Facet: "host",
				Missing: &datadogV2.LogsGroupByMissing{
					LogsGroupByMissingString: datadog.PtrString("miss")},
				Sort: &datadogV2.LogsAggregateSort{
					Type:        datadogV2.LOGSAGGREGATESORTTYPE_MEASURE.Ptr(),
					Order:       datadogV2.LOGSSORTORDER_ASCENDING.Ptr(),
					Aggregation: datadogV2.LOGSAGGREGATIONFUNCTION_PERCENTILE_90.Ptr(),
					Metric:      datadog.PtrString("@duration"),
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.AggregateLogs(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.AggregateLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.AggregateLogs`:\n%s\n", responseContent)
}
```

##### 

```go
// Aggregate events returns "OK" response

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
	body := datadogV2.LogsAggregateRequest{
		Filter: &datadogV2.LogsQueryFilter{
			From: datadog.PtrString("now-15m"),
			Indexes: []string{
				"main",
			},
			Query: datadog.PtrString("*"),
			To:    datadog.PtrString("now"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.AggregateLogs(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.AggregateLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.AggregateLogs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Aggregate compute events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.model.LogsAggregateRequest;
import com.datadog.api.client.v2.model.LogsAggregateResponse;
import com.datadog.api.client.v2.model.LogsAggregationFunction;
import com.datadog.api.client.v2.model.LogsCompute;
import com.datadog.api.client.v2.model.LogsComputeType;
import com.datadog.api.client.v2.model.LogsQueryFilter;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    LogsAggregateRequest body =
        new LogsAggregateRequest()
            .compute(
                Collections.singletonList(
                    new LogsCompute()
                        .aggregation(LogsAggregationFunction.COUNT)
                        .interval("5m")
                        .type(LogsComputeType.TIMESERIES)))
            .filter(
                new LogsQueryFilter()
                    .from("now-15m")
                    .indexes(Collections.singletonList("main"))
                    .query("*")
                    .to("now"));

    try {
      LogsAggregateResponse result = apiInstance.aggregateLogs(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#aggregateLogs");
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
// Aggregate compute events with group by returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.model.LogsAggregateRequest;
import com.datadog.api.client.v2.model.LogsAggregateResponse;
import com.datadog.api.client.v2.model.LogsAggregateSort;
import com.datadog.api.client.v2.model.LogsAggregateSortType;
import com.datadog.api.client.v2.model.LogsAggregationFunction;
import com.datadog.api.client.v2.model.LogsCompute;
import com.datadog.api.client.v2.model.LogsComputeType;
import com.datadog.api.client.v2.model.LogsGroupBy;
import com.datadog.api.client.v2.model.LogsGroupByMissing;
import com.datadog.api.client.v2.model.LogsQueryFilter;
import com.datadog.api.client.v2.model.LogsSortOrder;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    LogsAggregateRequest body =
        new LogsAggregateRequest()
            .compute(
                Collections.singletonList(
                    new LogsCompute()
                        .aggregation(LogsAggregationFunction.COUNT)
                        .interval("5m")
                        .type(LogsComputeType.TIMESERIES)))
            .filter(
                new LogsQueryFilter()
                    .from("now-15m")
                    .indexes(Collections.singletonList("main"))
                    .query("*")
                    .to("now"))
            .groupBy(
                Collections.singletonList(
                    new LogsGroupBy()
                        .facet("host")
                        .missing(new LogsGroupByMissing("miss"))
                        .sort(
                            new LogsAggregateSort()
                                .type(LogsAggregateSortType.MEASURE)
                                .order(LogsSortOrder.ASCENDING)
                                .aggregation(LogsAggregationFunction.PERCENTILE_90)
                                .metric("@duration"))));

    try {
      LogsAggregateResponse result = apiInstance.aggregateLogs(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#aggregateLogs");
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
// Aggregate events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.model.LogsAggregateRequest;
import com.datadog.api.client.v2.model.LogsAggregateResponse;
import com.datadog.api.client.v2.model.LogsQueryFilter;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    LogsAggregateRequest body =
        new LogsAggregateRequest()
            .filter(
                new LogsQueryFilter()
                    .from("now-15m")
                    .indexes(Collections.singletonList("main"))
                    .query("*")
                    .to("now"));

    try {
      LogsAggregateResponse result = apiInstance.aggregateLogs(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#aggregateLogs");
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
Aggregate compute events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest
from datadog_api_client.v2.model.logs_aggregation_function import LogsAggregationFunction
from datadog_api_client.v2.model.logs_compute import LogsCompute
from datadog_api_client.v2.model.logs_compute_type import LogsComputeType
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter

body = LogsAggregateRequest(
    compute=[
        LogsCompute(
            aggregation=LogsAggregationFunction.COUNT,
            interval="5m",
            type=LogsComputeType.TIMESERIES,
        ),
    ],
    filter=LogsQueryFilter(
        _from="now-15m",
        indexes=[
            "main",
        ],
        query="*",
        to="now",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.aggregate_logs(body=body)

    print(response)
```

##### 

```python
"""
Aggregate compute events with group by returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest
from datadog_api_client.v2.model.logs_aggregate_sort import LogsAggregateSort
from datadog_api_client.v2.model.logs_aggregate_sort_type import LogsAggregateSortType
from datadog_api_client.v2.model.logs_aggregation_function import LogsAggregationFunction
from datadog_api_client.v2.model.logs_compute import LogsCompute
from datadog_api_client.v2.model.logs_compute_type import LogsComputeType
from datadog_api_client.v2.model.logs_group_by import LogsGroupBy
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
from datadog_api_client.v2.model.logs_sort_order import LogsSortOrder

body = LogsAggregateRequest(
    compute=[
        LogsCompute(
            aggregation=LogsAggregationFunction.COUNT,
            interval="5m",
            type=LogsComputeType.TIMESERIES,
        ),
    ],
    filter=LogsQueryFilter(
        _from="now-15m",
        indexes=[
            "main",
        ],
        query="*",
        to="now",
    ),
    group_by=[
        LogsGroupBy(
            facet="host",
            missing="miss",
            sort=LogsAggregateSort(
                type=LogsAggregateSortType.MEASURE,
                order=LogsSortOrder.ASCENDING,
                aggregation=LogsAggregationFunction.PERCENTILE_90,
                metric="@duration",
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.aggregate_logs(body=body)

    print(response)
```

##### 

```python
"""
Aggregate events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter

body = LogsAggregateRequest(
    filter=LogsQueryFilter(
        _from="now-15m",
        indexes=[
            "main",
        ],
        query="*",
        to="now",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.aggregate_logs(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Aggregate compute events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = DatadogAPIClient::V2::LogsAggregateRequest.new({
  compute: [
    DatadogAPIClient::V2::LogsCompute.new({
      aggregation: DatadogAPIClient::V2::LogsAggregationFunction::COUNT,
      interval: "5m",
      type: DatadogAPIClient::V2::LogsComputeType::TIMESERIES,
    }),
  ],
  filter: DatadogAPIClient::V2::LogsQueryFilter.new({
    from: "now-15m",
    indexes: [
      "main",
    ],
    query: "*",
    to: "now",
  }),
})
p api_instance.aggregate_logs(body)
```

##### 

```ruby
# Aggregate compute events with group by returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = DatadogAPIClient::V2::LogsAggregateRequest.new({
  compute: [
    DatadogAPIClient::V2::LogsCompute.new({
      aggregation: DatadogAPIClient::V2::LogsAggregationFunction::COUNT,
      interval: "5m",
      type: DatadogAPIClient::V2::LogsComputeType::TIMESERIES,
    }),
  ],
  filter: DatadogAPIClient::V2::LogsQueryFilter.new({
    from: "now-15m",
    indexes: [
      "main",
    ],
    query: "*",
    to: "now",
  }),
  group_by: [
    DatadogAPIClient::V2::LogsGroupBy.new({
      facet: "host",
      missing: "miss",
      sort: DatadogAPIClient::V2::LogsAggregateSort.new({
        type: DatadogAPIClient::V2::LogsAggregateSortType::MEASURE,
        order: DatadogAPIClient::V2::LogsSortOrder::ASCENDING,
        aggregation: DatadogAPIClient::V2::LogsAggregationFunction::PERCENTILE_90,
        metric: "@duration",
      }),
    }),
  ],
})
p api_instance.aggregate_logs(body)
```

##### 

```ruby
# Aggregate events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = DatadogAPIClient::V2::LogsAggregateRequest.new({
  filter: DatadogAPIClient::V2::LogsQueryFilter.new({
    from: "now-15m",
    indexes: [
      "main",
    ],
    query: "*",
    to: "now",
  }),
})
p api_instance.aggregate_logs(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Aggregate compute events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::model::LogsAggregateRequest;
use datadog_api_client::datadogV2::model::LogsAggregationFunction;
use datadog_api_client::datadogV2::model::LogsCompute;
use datadog_api_client::datadogV2::model::LogsComputeType;
use datadog_api_client::datadogV2::model::LogsQueryFilter;

#[tokio::main]
async fn main() {
    let body = LogsAggregateRequest::new()
        .compute(vec![LogsCompute::new(LogsAggregationFunction::COUNT)
            .interval("5m".to_string())
            .type_(LogsComputeType::TIMESERIES)])
        .filter(
            LogsQueryFilter::new()
                .from("now-15m".to_string())
                .indexes(vec!["main".to_string()])
                .query("*".to_string())
                .to("now".to_string()),
        );
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api.aggregate_logs(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Aggregate compute events with group by returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::model::LogsAggregateRequest;
use datadog_api_client::datadogV2::model::LogsAggregateSort;
use datadog_api_client::datadogV2::model::LogsAggregateSortType;
use datadog_api_client::datadogV2::model::LogsAggregationFunction;
use datadog_api_client::datadogV2::model::LogsCompute;
use datadog_api_client::datadogV2::model::LogsComputeType;
use datadog_api_client::datadogV2::model::LogsGroupBy;
use datadog_api_client::datadogV2::model::LogsGroupByMissing;
use datadog_api_client::datadogV2::model::LogsQueryFilter;
use datadog_api_client::datadogV2::model::LogsSortOrder;

#[tokio::main]
async fn main() {
    let body = LogsAggregateRequest::new()
        .compute(vec![LogsCompute::new(LogsAggregationFunction::COUNT)
            .interval("5m".to_string())
            .type_(LogsComputeType::TIMESERIES)])
        .filter(
            LogsQueryFilter::new()
                .from("now-15m".to_string())
                .indexes(vec!["main".to_string()])
                .query("*".to_string())
                .to("now".to_string()),
        )
        .group_by(vec![LogsGroupBy::new("host".to_string())
            .missing(LogsGroupByMissing::LogsGroupByMissingString(
                "miss".to_string(),
            ))
            .sort(
                LogsAggregateSort::new()
                    .aggregation(LogsAggregationFunction::PERCENTILE_90)
                    .metric("@duration".to_string())
                    .order(LogsSortOrder::ASCENDING)
                    .type_(LogsAggregateSortType::MEASURE),
            )]);
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api.aggregate_logs(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Aggregate events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::model::LogsAggregateRequest;
use datadog_api_client::datadogV2::model::LogsQueryFilter;

#[tokio::main]
async fn main() {
    let body = LogsAggregateRequest::new().filter(
        LogsQueryFilter::new()
            .from("now-15m".to_string())
            .indexes(vec!["main".to_string()])
            .query("*".to_string())
            .to("now".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api.aggregate_logs(body).await;
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
 * Aggregate compute events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiAggregateLogsRequest = {
  body: {
    compute: [
      {
        aggregation: "count",
        interval: "5m",
        type: "timeseries",
      },
    ],
    filter: {
      from: "now-15m",
      indexes: ["main"],
      query: "*",
      to: "now",
    },
  },
};

apiInstance
  .aggregateLogs(params)
  .then((data: v2.LogsAggregateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Aggregate compute events with group by returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiAggregateLogsRequest = {
  body: {
    compute: [
      {
        aggregation: "count",
        interval: "5m",
        type: "timeseries",
      },
    ],
    filter: {
      from: "now-15m",
      indexes: ["main"],
      query: "*",
      to: "now",
    },
    groupBy: [
      {
        facet: "host",
        missing: "miss",
        sort: {
          type: "measure",
          order: "asc",
          aggregation: "pc90",
          metric: "@duration",
        },
      },
    ],
  },
};

apiInstance
  .aggregateLogs(params)
  .then((data: v2.LogsAggregateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Aggregate events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiAggregateLogsRequest = {
  body: {
    filter: {
      from: "now-15m",
      indexes: ["main"],
      query: "*",
      to: "now",
    },
  },
};

apiInstance
  .aggregateLogs(params)
  .then((data: v2.LogsAggregateResponse) => {
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

## Search logs{% #search-logs %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/logs-queries/list |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/logs-queries/list |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/logs-queries/list      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/logs-queries/list      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/logs-queries/list     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/logs-queries/list |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/logs-queries/list |

### Overview



List endpoint returns logs that match a log search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

**If you are considering archiving logs for your organization, consider use of the Datadog archive capabilities instead of the log list API. See [Datadog Logs Archive documentation](https://docs.datadoghq.com/logs/archives).**
This endpoint requires the `logs_read_data` permission.


### Request

#### Body Data (required)

Logs filter

{% tab title="Model" %}

| Parent field | Field                  | Type      | Description                                                                                                                                                               |
| ------------ | ---------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | index                  | string    | The log index on which the request is performed. For multi-index organizations, the default is all live indexes. Historical indexes of rehydrated logs must be specified. |
|              | limit                  | int32     | Number of logs return in the response.                                                                                                                                    |
|              | query                  | string    | The search query - following the log search syntax.                                                                                                                       |
|              | sort                   | enum      | Time-ascending `asc` or time-descending `desc` results. Allowed enum values: `asc,desc`                                                                                   |
|              | startAt                | string    | Hash identifier of the first log to return in the list, available in a log `id` attribute. This parameter is used for the pagination feature.                             | **Note**: This parameter is ignored if the corresponding log is out of the scope of the specified time window. |
|              | time [*required*] | object    | Timeframe to retrieve the log from.                                                                                                                                       |
| time         | from [*required*] | date-time | Minimum timestamp for requested logs.                                                                                                                                     |
| time         | timezone               | string    | Timezone can be specified both as an offset (for example "UTC+03:00") or a regional zone (for example "Europe/Paris").                                                    |
| time         | to [*required*]   | date-time | Maximum timestamp for requested logs.                                                                                                                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "index": "main",
  "query": "host:Test*",
  "sort": "asc",
  "time": {
    "from": "2021-11-11T10:11:11+00:00",
    "timezone": "Europe/Paris",
    "to": "2021-11-11T11:11:11+00:00"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all logs matching the request and pagination information.

| Parent field | Field      | Type      | Description                                                                                                                                                                                                                                                                                                              |
| ------------ | ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | logs       | [object]  | Array of logs matching the request and the `nextLogId` if sent.                                                                                                                                                                                                                                                          |
| logs         | content    | object    | JSON object containing all log attributes and their associated values.                                                                                                                                                                                                                                                   |
| content      | attributes | object    | JSON object of attributes from your log.                                                                                                                                                                                                                                                                                 |
| content      | host       | string    | Name of the machine from where the logs are being sent.                                                                                                                                                                                                                                                                  |
| content      | message    | string    | The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. |
| content      | service    | string    | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products.                                                                                                                                              |
| content      | tags       | [string]  | Array of tags associated with your log.                                                                                                                                                                                                                                                                                  |
| content      | timestamp  | date-time | Timestamp of your log.                                                                                                                                                                                                                                                                                                   |
| logs         | id         | string    | ID of the Log.                                                                                                                                                                                                                                                                                                           |
|              | nextLogId  | string    | Hash identifier of the next log to return in the list. This parameter is used for the pagination feature.                                                                                                                                                                                                                |
|              | status     | string    | Status of the response.                                                                                                                                                                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "logs": [
    {
      "content": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "host": "i-0123",
        "message": "Host connected to remote",
        "service": "agent",
        "tags": [
          "team:A"
        ],
        "timestamp": "2020-05-26T13:36:14Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA"
    }
  ],
  "nextLogId": "string",
  "status": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs-queries/list" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "index": "main",
  "query": "host:Test*",
  "sort": "asc",
  "time": {
    "from": "2021-11-11T10:11:11+00:00",
    "timezone": "Europe/Paris",
    "to": "2021-11-11T11:11:11+00:00"
  }
}
EOF
                        
##### 

```go
// Search test logs returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.LogsListRequest{
		Index: datadog.PtrString("main"),
		Query: datadog.PtrString("host:Test*"),
		Sort:  datadogV1.LOGSSORT_TIME_ASCENDING.Ptr(),
		Time: datadogV1.LogsListRequestTime{
			From:     time.Now().Add(time.Hour * -1),
			Timezone: datadog.PtrString("Europe/Paris"),
			To:       time.Now(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewLogsApi(apiClient)
	resp, r, err := api.ListLogs(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.ListLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.ListLogs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Search test logs returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsApi;
import com.datadog.api.client.v1.model.LogsListRequest;
import com.datadog.api.client.v1.model.LogsListRequestTime;
import com.datadog.api.client.v1.model.LogsListResponse;
import com.datadog.api.client.v1.model.LogsSort;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    LogsListRequest body =
        new LogsListRequest()
            .index("main")
            .query("host:Test*")
            .sort(LogsSort.TIME_ASCENDING)
            .time(
                new LogsListRequestTime()
                    .from(OffsetDateTime.now().plusHours(-1))
                    .timezone("Europe/Paris")
                    .to(OffsetDateTime.now()));

    try {
      LogsListResponse result = apiInstance.listLogs(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#listLogs");
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

```python
"""
Search test logs returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.logs_list_request import LogsListRequest
from datadog_api_client.v1.model.logs_list_request_time import LogsListRequestTime
from datadog_api_client.v1.model.logs_sort import LogsSort

body = LogsListRequest(
    index="main",
    query="host:Test*",
    sort=LogsSort.TIME_ASCENDING,
    time=LogsListRequestTime(
        _from=(datetime.now() + relativedelta(hours=-1)),
        timezone="Europe/Paris",
        to=datetime.now(),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Search test logs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsAPI.new

body = DatadogAPIClient::V1::LogsListRequest.new({
  index: "main",
  query: "host:Test*",
  sort: DatadogAPIClient::V1::LogsSort::TIME_ASCENDING,
  time: DatadogAPIClient::V1::LogsListRequestTime.new({
    from: (Time.now + -1 * 3600),
    timezone: "Europe/Paris",
    to: Time.now,
  }),
})
p api_instance.list_logs(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Search test logs returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs::LogsAPI;
use datadog_api_client::datadogV1::model::LogsListRequest;
use datadog_api_client::datadogV1::model::LogsListRequestTime;
use datadog_api_client::datadogV1::model::LogsSort;

#[tokio::main]
async fn main() {
    let body = LogsListRequest::new(
        LogsListRequestTime::new(
            DateTime::parse_from_rfc3339("2021-11-11T10:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
        )
        .timezone("Europe/Paris".to_string()),
    )
    .index("main".to_string())
    .query("host:Test*".to_string())
    .sort(LogsSort::TIME_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api.list_logs(body).await;
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
 * Search test logs returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsApi(configuration);

const params: v1.LogsApiListLogsRequest = {
  body: {
    index: "main",
    query: "host:Test*",
    sort: "asc",
    time: {
      from: new Date(new Date().getTime() + -1 * 3600 * 1000),
      timezone: "Europe/Paris",
      to: new Date(),
    },
  },
};

apiInstance
  .listLogs(params)
  .then((data: v1.LogsListResponse) => {
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

## Search logs (POST){% #search-logs-post %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/events/search |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/events/search |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/events/search      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/events/search      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/events/search     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/events/search |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/events/search |

### Overview



List endpoint returns logs that match a log search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to search and filter your logs.

**If you are considering archiving logs for your organization, consider use of the Datadog archive capabilities instead of the log list API. See [Datadog Logs Archive documentation](https://docs.datadoghq.com/logs/archives).**
This endpoint requires the `logs_read_data` permission.


### Request

#### Body Data 



{% tab title="Model" %}

| Parent field | Field        | Type     | Description                                                                                                                                           |
| ------------ | ------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | filter       | object   | The search and filter query settings                                                                                                                  |
| filter       | from         | string   | The minimum time for the requested logs, supports date math and regular timestamps (milliseconds).                                                    |
| filter       | indexes      | [string] | For customers with multiple indexes, the indexes to search. Defaults to ['*'] which means all indexes.                                                |
| filter       | query        | string   | The search query - following the log search syntax.                                                                                                   |
| filter       | storage_tier | enum     | Specifies storage type as indexes, online-archives or flex Allowed enum values: `indexes,online-archives,flex`                                        |
| filter       | to           | string   | The maximum time for the requested logs, supports date math and regular timestamps (milliseconds).                                                    |
|              | options      | object   | **DEPRECATED**: Global query options that are used during the query. Note: These fields are currently deprecated and do not affect the query results. |
| options      | timeOffset   | int64    | The time offset (in seconds) to apply to the query.                                                                                                   |
| options      | timezone     | string   | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).             |
|              | page         | object   | Paging attributes for listing logs.                                                                                                                   |
| page         | cursor       | string   | List following results with a cursor provided in the previous query.                                                                                  |
| page         | limit        | int32    | Maximum number of logs in the response.                                                                                                               |
|              | sort         | enum     | Sort parameters when querying logs. Allowed enum values: `timestamp,-timestamp`                                                                       |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "filter": {
    "query": "datadog-agent",
    "indexes": [
      "main"
    ],
    "from": "2020-09-17T11:48:36+01:00",
    "to": "2020-09-17T12:48:36+01:00"
  },
  "sort": "timestamp",
  "page": {
    "limit": 5
  }
}
```

##### 

```json
{
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all logs matching the request and pagination information.

| Parent field | Field      | Type      | Description                                                                                                                                                                                                                                                                                                              |
| ------------ | ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data       | [object]  | Array of logs matching the request.                                                                                                                                                                                                                                                                                      |
| data         | attributes | object    | JSON object containing all log attributes and their associated values.                                                                                                                                                                                                                                                   |
| attributes   | attributes | object    | JSON object of attributes from your log.                                                                                                                                                                                                                                                                                 |
| attributes   | host       | string    | Name of the machine from where the logs are being sent.                                                                                                                                                                                                                                                                  |
| attributes   | message    | string    | The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. |
| attributes   | service    | string    | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products.                                                                                                                                              |
| attributes   | status     | string    | Status of the message associated with your log.                                                                                                                                                                                                                                                                          |
| attributes   | tags       | [string]  | Array of tags associated with your log.                                                                                                                                                                                                                                                                                  |
| attributes   | timestamp  | date-time | Timestamp of your log.                                                                                                                                                                                                                                                                                                   |
| data         | id         | string    | Unique ID of the Log.                                                                                                                                                                                                                                                                                                    |
| data         | type       | enum      | Type of the event. Allowed enum values: `log`                                                                                                                                                                                                                                                                            |
|              | links      | object    | Links attributes.                                                                                                                                                                                                                                                                                                        |
| links        | next       | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                                                                                                                                                                        |
|              | meta       | object    | The metadata associated with a request                                                                                                                                                                                                                                                                                   |
| meta         | elapsed    | int64     | The time elapsed in milliseconds                                                                                                                                                                                                                                                                                         |
| meta         | page       | object    | Paging attributes.                                                                                                                                                                                                                                                                                                       |
| page         | after      | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.                                                                                                                                                                            |
| meta         | request_id | string    | The identifier of the request                                                                                                                                                                                                                                                                                            |
| meta         | status     | enum      | The status of the response Allowed enum values: `done,timeout`                                                                                                                                                                                                                                                           |
| meta         | warnings   | [object]  | A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.                                                                                                                                                                                            |
| warnings     | code       | string    | A unique code for this type of warning                                                                                                                                                                                                                                                                                   |
| warnings     | detail     | string    | A detailed explanation of this specific warning                                                                                                                                                                                                                                                                          |
| warnings     | title      | string    | A short human-readable summary of the warning                                                                                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "host": "i-0123",
        "message": "Host connected to remote",
        "service": "agent",
        "status": "INFO",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "log"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/logs/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
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
Not Authorized
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "datadog-agent",
    "indexes": [
      "main"
    ],
    "from": "2020-09-17T11:48:36+01:00",
    "to": "2020-09-17T12:48:36+01:00"
  },
  "sort": "timestamp",
  "page": {
    "limit": 5
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "indexes": [
      "main"
    ],
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
EOF
                        
##### 

```go
// Search logs returns "OK" response

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
	body := datadogV2.LogsListRequest{
		Filter: &datadogV2.LogsQueryFilter{
			Query: datadog.PtrString("datadog-agent"),
			Indexes: []string{
				"main",
			},
			From: datadog.PtrString("2020-09-17T11:48:36+01:00"),
			To:   datadog.PtrString("2020-09-17T12:48:36+01:00"),
		},
		Sort: datadogV2.LOGSSORT_TIMESTAMP_ASCENDING.Ptr(),
		Page: &datadogV2.LogsListRequestPage{
			Limit: datadog.PtrInt32(5),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.ListLogs(ctx, *datadogV2.NewListLogsOptionalParameters().WithBody(body))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.ListLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.ListLogs`:\n%s\n", responseContent)
}
```

##### 

```go
// Search logs returns "OK" response with pagination

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
	body := datadogV2.LogsListRequest{
		Filter: &datadogV2.LogsQueryFilter{
			From: datadog.PtrString("now-15m"),
			Indexes: []string{
				"main",
			},
			To: datadog.PtrString("now"),
		},
		Options: &datadogV2.LogsQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
		Page: &datadogV2.LogsListRequestPage{
			Limit: datadog.PtrInt32(2),
		},
		Sort: datadogV2.LOGSSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsApi(apiClient)
	resp, _ := api.ListLogsWithPagination(ctx, *datadogV2.NewListLogsOptionalParameters().WithBody(body))

	for paginationResult := range resp {
		if paginationResult.Error != nil {
			fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.ListLogs`: %v\n", paginationResult.Error)
		}
		responseContent, _ := json.MarshalIndent(paginationResult.Item, "", "  ")
		fmt.Fprintf(os.Stdout, "%s\n", responseContent)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Search logs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.api.LogsApi.ListLogsOptionalParameters;
import com.datadog.api.client.v2.model.LogsListRequest;
import com.datadog.api.client.v2.model.LogsListRequestPage;
import com.datadog.api.client.v2.model.LogsListResponse;
import com.datadog.api.client.v2.model.LogsQueryFilter;
import com.datadog.api.client.v2.model.LogsSort;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    LogsListRequest body =
        new LogsListRequest()
            .filter(
                new LogsQueryFilter()
                    .query("datadog-agent")
                    .indexes(Collections.singletonList("main"))
                    .from("2020-09-17T11:48:36+01:00")
                    .to("2020-09-17T12:48:36+01:00"))
            .sort(LogsSort.TIMESTAMP_ASCENDING)
            .page(new LogsListRequestPage().limit(5));

    try {
      LogsListResponse result = apiInstance.listLogs(new ListLogsOptionalParameters().body(body));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#listLogs");
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
// Search logs returns "OK" response with pagination

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.PaginationIterable;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.api.LogsApi.ListLogsOptionalParameters;
import com.datadog.api.client.v2.model.Log;
import com.datadog.api.client.v2.model.LogsListRequest;
import com.datadog.api.client.v2.model.LogsListRequestPage;
import com.datadog.api.client.v2.model.LogsQueryFilter;
import com.datadog.api.client.v2.model.LogsQueryOptions;
import com.datadog.api.client.v2.model.LogsSort;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    LogsListRequest body =
        new LogsListRequest()
            .filter(
                new LogsQueryFilter()
                    .from("now-15m")
                    .indexes(Collections.singletonList("main"))
                    .to("now"))
            .options(new LogsQueryOptions().timezone("GMT"))
            .page(new LogsListRequestPage().limit(2))
            .sort(LogsSort.TIMESTAMP_ASCENDING);

    try {
      PaginationIterable<Log> iterable =
          apiInstance.listLogsWithPagination(new ListLogsOptionalParameters().body(body));

      for (Log item : iterable) {
        System.out.println(item);
      }
    } catch (RuntimeException e) {
      System.err.println("Exception when calling LogsApi#listLogsWithPagination");
      System.err.println("Reason: " + e.getMessage());
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
Search logs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_list_request import LogsListRequest
from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
from datadog_api_client.v2.model.logs_sort import LogsSort

body = LogsListRequest(
    filter=LogsQueryFilter(
        query="datadog-agent",
        indexes=[
            "main",
        ],
        _from="2020-09-17T11:48:36+01:00",
        to="2020-09-17T12:48:36+01:00",
    ),
    sort=LogsSort.TIMESTAMP_ASCENDING,
    page=LogsListRequestPage(
        limit=5,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs(body=body)

    print(response)
```

##### 

```python
"""
Search logs returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_list_request import LogsListRequest
from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
from datadog_api_client.v2.model.logs_query_options import LogsQueryOptions
from datadog_api_client.v2.model.logs_sort import LogsSort

body = LogsListRequest(
    filter=LogsQueryFilter(
        _from="now-15m",
        indexes=[
            "main",
        ],
        to="now",
    ),
    options=LogsQueryOptions(
        timezone="GMT",
    ),
    page=LogsListRequestPage(
        limit=2,
    ),
    sort=LogsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    items = api_instance.list_logs_with_pagination(body=body)
    for item in items:
        print(item)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Search logs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = DatadogAPIClient::V2::LogsListRequest.new({
  filter: DatadogAPIClient::V2::LogsQueryFilter.new({
    query: "datadog-agent",
    indexes: [
      "main",
    ],
    from: "2020-09-17T11:48:36+01:00",
    to: "2020-09-17T12:48:36+01:00",
  }),
  sort: DatadogAPIClient::V2::LogsSort::TIMESTAMP_ASCENDING,
  page: DatadogAPIClient::V2::LogsListRequestPage.new({
    limit: 5,
  }),
})
opts = {
  body: body,
}
p api_instance.list_logs(opts)
```

##### 

```ruby
# Search logs returns "OK" response with pagination

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new

body = DatadogAPIClient::V2::LogsListRequest.new({
  filter: DatadogAPIClient::V2::LogsQueryFilter.new({
    from: "now-15m",
    indexes: [
      "main",
    ],
    to: "now",
  }),
  options: DatadogAPIClient::V2::LogsQueryOptions.new({
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::LogsListRequestPage.new({
    limit: 2,
  }),
  sort: DatadogAPIClient::V2::LogsSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
api_instance.list_logs_with_pagination(opts) { |item| puts item }
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Search logs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::ListLogsOptionalParams;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::model::LogsListRequest;
use datadog_api_client::datadogV2::model::LogsListRequestPage;
use datadog_api_client::datadogV2::model::LogsQueryFilter;
use datadog_api_client::datadogV2::model::LogsSort;

#[tokio::main]
async fn main() {
    let body = LogsListRequest::new()
        .filter(
            LogsQueryFilter::new()
                .from("2020-09-17T11:48:36+01:00".to_string())
                .indexes(vec!["main".to_string()])
                .query("datadog-agent".to_string())
                .to("2020-09-17T12:48:36+01:00".to_string()),
        )
        .page(LogsListRequestPage::new().limit(5))
        .sort(LogsSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .list_logs(ListLogsOptionalParams::default().body(body))
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Search logs returns "OK" response with pagination
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::ListLogsOptionalParams;
use datadog_api_client::datadogV2::api_logs::LogsAPI;
use datadog_api_client::datadogV2::model::LogsListRequest;
use datadog_api_client::datadogV2::model::LogsListRequestPage;
use datadog_api_client::datadogV2::model::LogsQueryFilter;
use datadog_api_client::datadogV2::model::LogsQueryOptions;
use datadog_api_client::datadogV2::model::LogsSort;
use futures_util::pin_mut;
use futures_util::stream::StreamExt;

#[tokio::main]
async fn main() {
    let body = LogsListRequest::new()
        .filter(
            LogsQueryFilter::new()
                .from("now-15m".to_string())
                .indexes(vec!["main".to_string()])
                .to("now".to_string()),
        )
        .options(LogsQueryOptions::new().timezone("GMT".to_string()))
        .page(LogsListRequestPage::new().limit(2))
        .sort(LogsSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let response = api.list_logs_with_pagination(ListLogsOptionalParams::default().body(body));
    pin_mut!(response);
    while let Some(resp) = response.next().await {
        if let Ok(value) = resp {
            println!("{:#?}", value);
        } else {
            println!("{:#?}", resp.unwrap_err());
        }
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Search logs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiListLogsRequest = {
  body: {
    filter: {
      query: "datadog-agent",
      indexes: ["main"],
      from: "2020-09-17T11:48:36+01:00",
      to: "2020-09-17T12:48:36+01:00",
    },
    sort: "timestamp",
    page: {
      limit: 5,
    },
  },
};

apiInstance
  .listLogs(params)
  .then((data: v2.LogsListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Search logs returns "OK" response with pagination
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

const params: v2.LogsApiListLogsRequest = {
  body: {
    filter: {
      from: "now-15m",
      indexes: ["main"],
      to: "now",
    },
    options: {
      timezone: "GMT",
    },
    page: {
      limit: 2,
    },
    sort: "timestamp",
  },
};

(async () => {
  try {
    for await (const item of apiInstance.listLogsWithPagination(params)) {
      console.log(item);
    }
  } catch (error) {
    console.error(error);
  }
})();
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Search logs (GET){% #search-logs-get %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/events |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/events |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/events      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/events      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/events     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/events |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/events |

### Overview



List endpoint returns logs that match a log search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to search and filter your logs.

**If you are considering archiving logs for your organization, consider use of the Datadog archive capabilities instead of the log list API. See [Datadog Logs Archive documentation](https://docs.datadoghq.com/logs/archives).**
This endpoint requires the `logs_read_data` permission.


### Arguments

#### Query Strings

| Name                 | Type    | Description                                                                                         |
| -------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| filter[query]        | string  | Search query following logs syntax.                                                                 |
| filter[indexes]      | array   | For customers with multiple indexes, the indexes to search. Defaults to '*' which means all indexes |
| filter[from]         | string  | Minimum timestamp for requested logs.                                                               |
| filter[to]           | string  | Maximum timestamp for requested logs.                                                               |
| filter[storage_tier] | enum    | Specifies the storage type to be usedAllowed enum values: `indexes, online-archives, flex`          |
| sort                 | enum    | Order of logs in results.Allowed enum values: `timestamp, -timestamp`                               |
| page[cursor]         | string  | List following results with a cursor provided in the previous query.                                |
| page[limit]          | integer | Maximum number of logs in the response.                                                             |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all logs matching the request and pagination information.

| Parent field | Field      | Type      | Description                                                                                                                                                                                                                                                                                                              |
| ------------ | ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data       | [object]  | Array of logs matching the request.                                                                                                                                                                                                                                                                                      |
| data         | attributes | object    | JSON object containing all log attributes and their associated values.                                                                                                                                                                                                                                                   |
| attributes   | attributes | object    | JSON object of attributes from your log.                                                                                                                                                                                                                                                                                 |
| attributes   | host       | string    | Name of the machine from where the logs are being sent.                                                                                                                                                                                                                                                                  |
| attributes   | message    | string    | The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. |
| attributes   | service    | string    | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products.                                                                                                                                              |
| attributes   | status     | string    | Status of the message associated with your log.                                                                                                                                                                                                                                                                          |
| attributes   | tags       | [string]  | Array of tags associated with your log.                                                                                                                                                                                                                                                                                  |
| attributes   | timestamp  | date-time | Timestamp of your log.                                                                                                                                                                                                                                                                                                   |
| data         | id         | string    | Unique ID of the Log.                                                                                                                                                                                                                                                                                                    |
| data         | type       | enum      | Type of the event. Allowed enum values: `log`                                                                                                                                                                                                                                                                            |
|              | links      | object    | Links attributes.                                                                                                                                                                                                                                                                                                        |
| links        | next       | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                                                                                                                                                                        |
|              | meta       | object    | The metadata associated with a request                                                                                                                                                                                                                                                                                   |
| meta         | elapsed    | int64     | The time elapsed in milliseconds                                                                                                                                                                                                                                                                                         |
| meta         | page       | object    | Paging attributes.                                                                                                                                                                                                                                                                                                       |
| page         | after      | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.                                                                                                                                                                            |
| meta         | request_id | string    | The identifier of the request                                                                                                                                                                                                                                                                                            |
| meta         | status     | enum      | The status of the response Allowed enum values: `done,timeout`                                                                                                                                                                                                                                                           |
| meta         | warnings   | [object]  | A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.                                                                                                                                                                                            |
| warnings     | code       | string    | A unique code for this type of warning                                                                                                                                                                                                                                                                                   |
| warnings     | detail     | string    | A detailed explanation of this specific warning                                                                                                                                                                                                                                                                          |
| warnings     | title      | string    | A short human-readable summary of the warning                                                                                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "host": "i-0123",
        "message": "Host connected to remote",
        "service": "agent",
        "status": "INFO",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "log"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/logs/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
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
Not Authorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Search logs (GET) returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs_get()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Search logs (GET) returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsAPI.new
p api_instance.list_logs_get()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Search logs (GET) returns "OK" response

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
	api := datadogV2.NewLogsApi(apiClient)
	resp, r, err := api.ListLogsGet(ctx, *datadogV2.NewListLogsGetOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsApi.ListLogsGet`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsApi.ListLogsGet`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Search logs (GET) returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsApi;
import com.datadog.api.client.v2.model.LogsListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsApi apiInstance = new LogsApi(defaultClient);

    try {
      LogsListResponse result = apiInstance.listLogsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#listLogsGet");
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
// Search logs (GET) returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs::ListLogsGetOptionalParams;
use datadog_api_client::datadogV2::api_logs::LogsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsAPI::with_config(configuration);
    let resp = api
        .list_logs_get(ListLogsGetOptionalParams::default())
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
 * Search logs (GET) returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsApi(configuration);

apiInstance
  .listLogsGet()
  .then((data: v2.LogsListResponse) => {
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
