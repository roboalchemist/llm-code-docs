# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/realtime-async-and-batch-request.md

# Realtime, Async & Batch Request

What?

### Real Time Request <a href="#real-time-request" id="real-time-request"></a>

A real-time scraping request executes the scraping task on the target domain and delivers the response immediately after the desired data is received

* dependent on timeout settings and potentially affected by rendering delays (as data loads), the response is returned to the user as soon as it becomes available.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api), [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api) and [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api)

### Async Request <a href="#async-request" id="async-request"></a>

An asynchronous scraping request initiates the scraping task on the target domain and operates independently of the user's immediate session.

* The user doesn't wait for a response directly after the request. Instead, once the scraping is complete and the data is ready, the user is notified through a callback URL or a specified cloud storage URL.
* This method allows the scraping process to run in the background, enabling the user to continue with other tasks and receive the scraped data once it's available, without having to manage or monitor the ongoing process actively.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api), [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api) and [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api)

### Batch Request <a href="#async-request" id="async-request"></a>

**Batch Processing** feature allow users to perform queries of up to **1K** URLs in a single batch request, significantly improving efficiency and reducing the time needed for large-scale data collection tasks:

* Supports custom settings for each URL in a batch, including different geolocations, rendering options, and parsing templates, to meet specific data collection requirements.
* Offers asynchronous processing, enabling data collection tasks to run in the background without interrupting other operations, and providing flexibility in handling large volumes of data.
* Integrates with cloud storage solutions for automated data delivery, facilitating seamless workflow integration and immediate access to collected data.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api), [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api) and [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api)

## &#x20;Why? <a href="#what-and-why" id="what-and-why"></a>

### Real Time Request <a href="#real-time-request-1" id="real-time-request-1"></a>

* **Immediate & Accurate Data Access**: Real-time scraping retrieves data as it is currently displayed on websites. This is crucial for obtaining the most up-to-date information, whether for monitoring prices, stock levels, news updates, or social sentiment. This immediacy ensures that decisions are based on the latest data available.
* **Event-Driven Responses**: By scraping data in real time, you can trigger actions based on specific conditions or changes detected on the target website. For instance, receiving alerts when a product goes on sale, when a competitor changes their pricing, or when new content is posted, enabling prompt and relevant responses.
* **Event-Driven Responses**: By scraping data in real time, you can trigger actions based on specific conditions or changes detected on the target website. For instance, receiving alerts when a product goes on sale, when a competitor changes their pricing, or when new content is posted, enabling prompt and relevant responses.

### Async Request <a href="#async-request-1" id="async-request-1"></a>

* **Non-blocking Operations**: Async requests allow other processes to run concurrently while the data request is being handled. This means that your application doesn't have to pause and wait for the data retrieval to complete, enhancing overall performance and user experience, especially in applications that handle large volumes of data or require high responsiveness.
* **Efficiency in Handling Multiple Requests**: With async requests, you can send out multiple data requests simultaneously rather than waiting for each to complete sequentially. This is particularly useful in scenarios like data scraping, API data retrieval, or loading data from different sources, as it significantly speeds up the overall process.
* **Scalability**: Asynchronous processing is more scalable as it better manages resources and handles increases in workload. For services that expect a high volume of requests or need to scale dynamically, async requests ensure that the system remains responsive and performant under varying loads.

### Batch Request <a href="#async-request-1" id="async-request-1"></a>

* **Increased Efficiency**: Handling up to 1,000 URLs in a single batch request streamlines operations by reducing the number of individual requests needed. This consolidation minimizes overhead associated with setting up and tearing down connections, thereby enhancing the overall efficiency of data processing.
* **Asynchronous Processing with Flexible Data Handling**: The batch processing feature operates asynchronously, allowing users to execute other tasks while their request processes. With options to use a callback URL or direct cloud storage for results, this feature enhances workflow efficiency and offers versatile data management, seamlessly integrating with various systems and needs.
* **Reduced Resource Consumption**: With fewer HTTP connections needed for the same amount of work, your server resources are better utilized. This not only optimizes server performance but also potentially lowers costs related to bandwidth and computing power.
* **Simplified Management**: Managing one request with multiple URLs is simpler and more straightforward than handling numerous single-URL requests. This simplifies the workflow for developers and reduces the complexity of code needed to handle large volumes of data.

## Asynchronous Request Process <a href="#asynchronous-request-process" id="asynchronous-request-process"></a>

Unlike real-time requests, asynchronous requests do not return the result directly to the client. Instead, an asynchronous request produces a “task” that runs in the background and delivers the resulting data to a cloud storage bucket and/or callback URL. Tasks go through four stages:

| Status    | Description                                                                    |
| --------- | ------------------------------------------------------------------------------ |
| pending   | The task is still being processed.                                             |
| uploading | The results are being uploaded to the destination repository.                  |
| success   | Task was complete and stored in the destination repository.                    |
| failed    | Nimble was unable to complete the task, no file was created in the repository. |

## Delivery Methods <a href="#request-option" id="request-option"></a>

Nimble API supports three delivery methods:

* [x] **Real-time** - the collected data is returned immediately to the user.
* [x] **Cloud** - the collected data is delivered to your preferred cloud storage repository.
* [x] **Push/Pull** - the collected data is stored on Nimble's servers, and can be downloaded via a provided URL.

For real-time delivery, see our page on performing a [real-time URL request](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/real-time-url-request). To use Cloud or Push/Pull delivery, use an **asynchronous request** instead. Asynchronous requests also have the added benefit of running in the background, so you can continue working without waiting for the job to complete.

## Request Option <a href="#request-option" id="request-option"></a>

### Example - Realtime Request <a href="#example" id="example"></a>

A simple real-time request uses the following syntax

**Path**: `https://api.webit.live/api/v1/`<mark style="color:orange;">**`realtime`**</mark>`/...`

<table><thead><tr><th width="198">Parameter</th><th width="206">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>url</code></td><td>Required </td><td>URL | The page or resource to be fetched. Note: when using a URL with a query string, encode the URL and place it at the end of the query string</td></tr></tbody></table>

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com"
}'
```

{% endtab %}
{% endtabs %}

### Example - Async Request <a href="#example" id="example"></a>

A simple async request uses the following syntax

**Path**: `https://api.webit.live/api/v1/`<mark style="color:orange;">**`async`**</mark>`/...`

<table><thead><tr><th width="214">Parameter</th><th width="162">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>storage_type</code></td><td>Optional (default = push/pull)</td><td><p>ENUM: s3 | gs - Use s3 for Amazon S3 and gs for Google Cloud Platform.</p><p>Leave blank to enable Push/Pull delivery.</p></td></tr><tr><td><code>storage_url</code></td><td>Optional (default = push/pull)</td><td><p>Repository URL: s3://Your.Bucket.Name/your/object/name/prefix/ - Output will be saved to TASK_ID.json</p><p>Leave blank to enable Push/Pull delivery.</p></td></tr><tr><td><code>callback_url</code></td><td>Optional </td><td>A url to callback once the data is delivered. The WebAPI will send a POST request to the callback_url with the task details once the task is complete (this “notification” will not include the requested data).</td></tr><tr><td><code>storage_compress</code></td><td>Optional (default = false)</td><td>When set to <code>true</code>, the response saved to the <code>storage_url</code> will be compressed using GZIP format. This can help reduce storage size and improve data transfer efficiency. If not set or set to <code>false</code>, the response will be saved in its original uncompressed format.</td></tr><tr><td><code>storage_object_name</code></td><td>Optional (default = <code>task_id</code>)</td><td>String | Allows setting a custom name for the stored object instead of the default task ID. </td></tr></tbody></table>

{% hint style="warning" %}
Please add Nimble's system/service user to your GCS or S3 bucket to ensure that data can be delivered successfully.
{% endhint %}

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/async/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "method": "GET",
    "parse": true,
    "render": false,
    "storage_type": "s3",
    "storage_url" : "s3://Your.Repository.Path/",
    "callback_url": "https://your.callback.url/path"
}'
```

{% endtab %}
{% endtabs %}

#### **Initial Response** <a href="#initial-response" id="initial-response"></a>

In response to triggering an asynchronous request, the details of the created task are returned, which can later be used to check its status. The response contains the Task ID, as well as other information, and is structured as follows:

```json
{
    "status": "success",
    "task": {
        "id": "Task_ID",
        "state": "pending",
        "output_url": "s3://Your.Repository.Path/Task_ID.json",
        "callback_url": "https://your.callback.url/path",
        "status_url": "https://api.webit.live/api/v1/tasks/Task_ID",
        "created_at": "0000-00-00T00:00:00.000Z",
        "modified_at": "0000-00-00T00:00:00.000Z",
        "input": {
            "parse": "true",
            "render": "false",
            "storage_url": "s3://Your.Repository.Path/",
            "storage_type": "s3",
            "url": "https://www.example.com",
            "callback_url": "https://your.callback.url/path"
        },
        "status_code": 200
    }
}
```

### Retrieving Task Status (Async) <a href="#retrieving-batch-summary" id="retrieving-batch-summary"></a>

To check the status of an asynchronous task, use the endpoint Path:`https://api.webit.live/api/v1/`<mark style="color:orange;">**`tasks`**</mark>`/`<mark style="color:orange;">**`<task_id>`**</mark>

#### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X GET 'https://api.webit.live/api/v1/tasks/Task_ID' \
--header 'Authorization: Basic <credential string>'
```

{% endtab %}
{% endtabs %}

The response object has the same structure as the Task Completion object that is sent to the callback\_url upon task completion.

#### **Example Response** <a href="#task-completion" id="task-completion"></a>

A POST request will be sent to the callback\_url once the task is complete which contains the following information:

```json
{
    "status": "success",
    "task": {
        "id": "Task_ID",
        "state": "success",
        "output_url": "s3://Your.Repository.Path/Task_ID.json",
        "callback_url": "https://your.callback.url/path",
        "status_url": "https://api.webit.live/api/v1/tasks/Task_ID",
        "created_at": "0000-00-00T00:00:00.000Z",
        "modified_at": "0000-00-00T00:00:00.000Z",
        "input": {...},
        "status_code": 200
    }
}
```

Asynchronous requests also have methods for handling upload failures. For more information, see the Nimble Web API Documentation.

### **Checking Tasks List**

To check the status of asynchronous tasks list, use the endpoint \
Path ***`https://api.webit.live/api/v1/tasks/list`***

### Parameters

<table><thead><tr><th width="172.45052083333331">Parameter</th><th width="258.7734375">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>limit</code></td><td>Optional (default = 100)</td><td>Number | List item limit</td></tr><tr><td><strong><code>cursor</code></strong></td><td>Optional</td><td>String | Cursor for pagination. </td></tr></tbody></table>

&#x20;Example Request:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X GET 'https://api.webit.live/api/v1/tasks/list?limit=20' \
--header 'Authorization: Basic <credential string>'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/tasks/list?limit=20'
headers = {
    'Authorization': 'Basic <credential string>'
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/tasks/list?limit=20';
const headers = {
  'Authorization': 'Basic <credential string>'
};

axios.get(url, { headers })
  .then(response => {
    console.log(response.status);
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```

{% endtab %}

{% tab title="Go" %}

```go
package main

import (
 "fmt"
 "net/http"
)

func main() {
 url := "https://api.webit.live/api/v1/tasks/list?limit=20"
 headers := map[string]string{
  "Authorization": "Basic <credential string>",
 }

 req, err := http.NewRequest("GET", url, nil)
 if err != nil {
  fmt.Println(err)
  return
 }

 for key, value := range headers {
  req.Header.Set(key, value)
 }

 client := &http.Client{}
 resp, err := client.Do(req)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer resp.Body.Close()

 fmt.Println(resp.StatusCode)
 // Read the response body if needed
 // body, err := ioutil.ReadAll(resp.Body)
 // fmt.Println(string(body))
}
```

{% endtab %}
{% endtabs %}

Example Response:&#x20;

```json
{
    "data": [
       ...
    ],
    "pagination": {
        "hasNext": true,
        "nextCursor": ...,
        "total": 102
    }
}
```

The response objects within `data` has the same structure as the Task Completion object that is sent to the <mark style="color:red;background-color:yellow;">callback\_url</mark> upon task completion.

* For pagination, run until pagination.hasNext = false or pagination.nextCursor = null

### Example - Batch Request  <a href="#example" id="example"></a>

A simple batch processing request uses the following syntax

**Path**: `https://api.webit.live/api/v1/`<mark style="color:orange;">**`batch`**</mark>`/...`

* Supporting up to 1000 URL within a signle batch request

<table><thead><tr><th width="211">Parameter</th><th width="207">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>requests</code></td><td>Only when Batch processing is required</td><td>Object array - Allows for defining custom parameters for each request within the bulk. Any of the parameters below can be used in an individual request</td></tr><tr><td><code>storage_type</code></td><td>Optional (default = push/pull)</td><td><p>ENUM: s3 | gs - Use s3 for Amazon S3 and gs for Google Cloud Platform.</p><p>Leave blank to enable Push/Pull delivery.</p></td></tr><tr><td><code>storage_url</code></td><td>Optional (default = push/pull)</td><td><p>Repository URL: s3://Your.Bucket.Name/your/object/name/prefix/ - Output will be saved to TASK_ID.json</p><p>Leave blank to enable Push/Pull delivery.</p></td></tr><tr><td><code>callback_url</code></td><td>Optional </td><td>A url to callback once the data is delivered. The WebAPI will send a POST request to the callback_url with the task details once the task is complete (this “notification” will not include the requested data).</td></tr><tr><td><code>storage_compress</code></td><td>Optional (default = false)</td><td>When set to <code>true</code>, the response saved to the <code>storage_url</code> will be compressed using GZIP format. This can help reduce storage size and improve data transfer efficiency. If not set or set to <code>false</code>, the response will be saved in its original uncompressed format.</td></tr><tr><td><code>storage_object_name</code></td><td>Optional (default = <code>task_id</code>)</td><td>String | Allows setting a custom name for the stored object instead of the default task ID. </td></tr></tbody></table>

{% hint style="warning" %}
Please add Nimble's system/service user to your GCS or S3 bucket to ensure that data can be delivered successfully.
{% endhint %}

**Example #1 - collecting data from multiple URLs**

In this first example, we'll collect data from several unique URLs. To do so, we set the URLs we want to collect in the `url` fields of the `requests` object.

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/batch/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "requests": [
        { "url": "https://www.finance.com" },
        { "url": "https://www.travel.com" },
        { "url": "https://www.socialmedia.com" }
    ],
    "storage_type": "s3",
    "storage_url": "s3://Your.Repository.Path/",
    "callback_url": "https://your.callback.url/path"
}'
```

{% endtab %}
{% endtabs %}

Parameters that are placed outside the `requests` object, such as `storage_type`, `storage_url`, and `callback_url` , are automatically applied as defaults to all defined requests.

If a parameter is set both inside and outside the `requests` object, the value inside the request overrides the one outside.

**Example #2- collecting multiple URLs from multiple countries**

In this example, we'll collect multiple URLs with a different country set for each URL. To do so, we'll take advantage of the requests object, which allows us to set any parameter inside each request:

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/batch/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "requests": [
        { "url": "https://www.finance.com", "country": "US", "locale": "en-US" },
        { "url": "https://www.travel.com",  "country": "FR", "locale": "fr" },
        { "url": "https://www.socialmedia.com",  "country": "GR", "locale": "de" },
        { "url": "https://www.searchengine.com" }
    ],
    "country": "CA", 
    "locale": "ca",
    "storage_type": "s3",
    "storage_url": "s3://Your.Repository.Path/",
    "callback_url": "https://your.callback.url/path"
}'
```

{% endtab %}
{% endtabs %}

For the above request, each URL would be requested from the corresponding country. "examplefour.com" does not have a country set in its request, and thus will default to the country defined outside the `requests` object (CA - Canada). If no default country had been set, by default the request would have used a randomly selected country.

**Example #3- collecting the same URL from different countries**

Any parameter can be defined inside and/or outside the `requests` object. We can take advantage of this in some cases by setting our URL once as a default and setting various other parameters in the requests object. For example:

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/batch/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "requests": [
        { "country": "US", "locale": "en-US" },
        { "country": "FR", "locale": "fr" },
        { "country": "GR", "locale": "de" },
    ],
    "url": "https://www.finance.com",
    "storage_type": "s3",
    "storage_url": "s3://Your.Repository.Path/",
    "callback_url": "https://your.callback.url/path"
}'
```

{% endtab %}
{% endtabs %}

In the above example, the URL "exampleone.com" would be requested three times - once from the US, once from France, and once from Germany.

Like asynchronous tasks, the status of a batch is available for 24 hours, and the user can check the batch progress status below.

### Initial Response

Upon sending a batch request, you will immediately receive a response containing the details of the received batch including a `batch_id` - which can be used to check execution progress and retrieve a summary of the job.

The initial request is structured as follows:

```json
{
  "batch_id": "7c891d6d-fd6b-430b-8649-107181c0de33",
  "batch_size": 2,
  "tasks": [
    {
      "id": "45b54220-76bc-4b38-b056-e97f05c8f5a5",
      "state": "pending",
      "status_url": "https://api.webit.live/api/v1/tasks/45b54220-76bc-4b38-b056-e97f05c8f5a5",
      "created_at": "2025-05-25T08:57:56.839Z",
      "modified_at": "2025-05-25T08:57:56.839Z",
      "input": {
        "render": false,
        "url": "https://example.com/page-one"
      },
      "batch_id": "7c891d6d-fd6b-430b-8649-107181c0de33",
      "account_name": "demo-account",
      "api_type": "web",
      "download_url": "https://api.webit.live/api/v1/tasks/45b54220-76bc-4b38-b056-e97f05c8f5a5/results"
    },
    {
      "id": "e933d45d-588d-4608-a039-17b30b2645a6",
      "state": "pending",
      "status_url": "https://api.webit.live/api/v1/tasks/e933d45d-588d-4608-a039-17b30b2645a6",
      "created_at": "2025-05-25T08:57:56.839Z",
      "modified_at": "2025-05-25T08:57:56.839Z",
      "input": {
        "render": false,
        "url": "https://example.com/page-two"
      },
      "batch_id": "7c891d6d-fd6b-430b-8649-107181c0de33",
      "account_name": "demo-account",
      "api_type": "web",
      "download_url": "https://api.webit.live/api/v1/tasks/e933d45d-588d-4608-a039-17b30b2645a6/results"
    }
  ]
}
```

In the above example, our batch includes two requests, both of which are pending execution. The `batch_id` is also listed in each nested request, not to be confused with the `id` field, which identifies individual jobs within the batch.

### Tracking Batch Execution Progress

<details>

<summary>Checking batch progress and status</summary>

`https://api.webit.live/api/v1/batches/<batch-id>/progress`

Like asynchronous tasks, the status of a batch is available for 24 hours.

{% code overflow="wrap" %}

```bash
curl -X GET 'https://api.webit.live/api/v1/batches/<batch_id>/progress' \--header 'Authorization: Basic <credential string>'
```

{% endcode %}

**Response**

The progress of a batch is reported in percentages.

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "completed": false,
    "progress": 0.333333
}
```

{% endcode %}

Once a batch is finished, its progress will be reported as “1”.

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "completed": true,
    "progress": 1
}
```

{% endcode %}

</details>

<details>

<summary>Checking Batch List</summary>

To check the status of Batch list, use the endpoint \
Path `https://api.webit.live/api/v1/batches/list`

### Parameters

<table><thead><tr><th width="172.45052083333331">Parameter</th><th width="258.7734375">Required</th><th>Description</th></tr></thead><tbody><tr><td><strong><code>limit</code></strong></td><td>Optional (default = 100)</td><td>Number | List item limit</td></tr><tr><td><code>cursor</code></td><td>Optional</td><td>String | Cursor for pagination. </td></tr></tbody></table>

&#x20;Example Request:

```bash
curl -X GET 'https://api.webit.live/api/v1/batches/list?limit=20' \
--header 'Authorization: Basic <credential string>'
```

Example Response:&#x20;

```json
{
    "data": [
       ...
    ],
    "pagination": {
        "hasNext": true,
        "nextCursor": ...,
        "total": 102
    }
}
```

{% hint style="info" %}
For pagination, run until pagination.hasNext = false or pagination.nextCursor = null
{% endhint %}

</details>

<details>

<summary>Retrieving Batch Summary</summary>

Once a batch has finished, it’s possible to return a summary of the completed tasks, by using the following endpoint: `https://api.webit.live/api/v1/batches/<batch-id>`

#### Example Request

```bash
curl -X GET 'https://api.webit.live/api/v1/batches/7a07a96d-c402-4d98-a17f-4ecb390d11a3' \
--header 'Authorization: Basic <credential string>'
```

The response object lists the status of the overall batch, as well as the individual tasks and their details:

**Example Response**

```json
{
    "status": "success",
    "tasks": [
        {
            "batch_id": "7a07a96d-c402-4d98-a17f-4ecb390d11a3",
            "id": "2e508d43-8b02-4fc0-96c7-0968ab454a0c",
            "state": "success",
            "query_time": "2023-01-01T12:00:00.007Z",
            "output_url": "s3://Your.Repository.Path/2e508d43-8b02-4fc0-96c7-0968ab454a0c.json",
            "callback_url": "https://your.callback.url/path",
            "status_url": "https://[base_url]/api/v1/tasks/2e508d43-8b02-4fc0-96c7-0968ab454a0c",
            "created_at": "2022-07-24T08:09:23.205Z",
            "modified_at": "2022-07-24T08:10:27.244Z",
            "input": {...},
            "status_code": 200
        },
        {
            "batch_id": "7a07a96d-c402-4d98-a17f-4ecb390d11a3",
            "id": "63cc3bd5-01b4-4787-90a2-f382b9960c77",
            "state": "success",
            "query_time": "2023-01-01T12:00:00.007Z",
            "output_url": "s3://Your.Repository.Path/63cc3bd5-01b4-4787-90a2-f382b9960c77.json",
            "callback_url": "https://your.callback.url/path",
            "status_url": "https://[base_url]/api/v1/tasks/63cc3bd5-01b4-4787-90a2-f382b9960c77",
            "created_at": "2022-07-24T08:09:23.205Z",
            "modified_at": "2022-07-24T08:10:27.973Z",
            "input": {...},
            "status_code": 200
         },
        {
            "batch_id": "7a07a96d-c402-4d98-a17f-4ecb390d11a3",
            "id": "4cb39bbf-5580-4c50-8ed4-4a7905e2ec52",
            "state": "success",
            "query_time": "2023-01-01T12:00:00.007Z",
            "output_url": "s3://Your.Repository.Path/4cb39bbf-5580-4c50-8ed4-4a7905e2ec52.json",
            "callback_url": "https://your.callback.url/path",
            "status_url": "https://[base_url]/api/v1/tasks/4cb39bbf-5580-4c50-8ed4-4a7905e2ec52",
            "created_at": "2022-07-24T08:09:23.205Z",
            "modified_at": "2022-07-24T08:10:30.292Z",
            "input": {...},
            "status_code": 200
        }
    ],
    "completed": true,
    "progress": 1
}
```

</details>

<details>

<summary>Batch Replay - Ensure Data Completeness with Ease</summary>

Batches are a powerful way to execute high-volume data collection asynchronously. Occasionally, some individual tasks within a batch may not yield results due to temporary issues such as website unavailability, network instability, server errors and more.

To help you **maximize data completeness effortlessly**, the **Batch Replay** feature allows you to **re-run only the incomplete or non-successful tasks** from an existing batch ID — no need to resubmit or rebuild your batch manually,  just by using the following endpoint: `https://api.webit.live/api/v1/replay/batch/<batch-id>`

{% hint style="warning" %}
Replay is available for **up to 7 days** after the original batch submission. During this window, you can confidently re-run tasks to fill any gaps. After 7 days, the batch logs are archived and replay is no longer possible.
{% endhint %}

#### Example Request

```bash
curl -X POST 'https://api.webit.live/api/v1/replay/batch/613b0964-ebf1-4e16-a893-e4588d465d0' \
--header 'Authorization: Basic <credential string>'
```

The response object lists the status of the overall batch, as well as the individual tasks and their details:

**Example Response**

```json
{
  "batch_id": "613b0964-ebf1-4e16-a893-e4588d465d0",
  "replayed_tasks": 0
}
```

* `replayed_tasks`: Number of tasks from the original batch that were retried. In the example above, the batch completed successfully earlier, so no tasks required replay.

</details>

### Batch Output <a href="#retrieving-batch-summary" id="retrieving-batch-summary"></a>

Batch requests operate similarly to asynchronous requests, delivering the collected data to your cloud storage provider of choice or being available to download via a push/pull endpoint.

The results are stored in the following structure:

```json
{
  "status": "success",
  "id": "ba0220e0-c0ab-4cd3-920e-f7633142db82",
  "tasks": [
    {
      "id": "47e75a83-510d-4bd0-bfb1-03478cbab874",
      "state": "success",
      "status_url": "https://api.webit.live/api/v1/tasks/47e75a83-510d-4bd0-bfb1-03478cbab874",
      "download_url": "https://api.webit.live/api/v1/tasks/47e75a83-510d-4bd0-bfb1-03478cbab874/results",
      "created_at": "2025-05-25T10:20:36.744Z",
      "modified_at": "2025-05-25T10:20:39.617Z",
      "account_name": "demo-account",
      "input": {
        "render": false,
        "url": "https://example.com/page-one"
      },
      "batch_id": "ba0220e0-c0ab-4cd3-920e-f7633142db82",
      "status_code": 200,
      "api_type": "web"
    },
    {
      "id": "9415ce96-78be-4af1-8558-829ae6199464",
      "state": "success",
      "status_url": "https://api.webit.live/api/v1/tasks/9415ce96-78be-4af1-8558-829ae6199464",
      "download_url": "https://api.webit.live/api/v1/tasks/9415ce96-78be-4af1-8558-829ae6199464/results",
      "created_at": "2025-05-25T10:20:36.744Z",
      "modified_at": "2025-05-25T10:20:42.269Z",
      "account_name": "demo-account",
      "input": {
        "render": false,
        "url": "https://example.com/page-two"
      },
      "batch_id": "ba0220e0-c0ab-4cd3-920e-f7633142db82",
      "status_code": 200,
      "api_type": "web"
    }
  ],
  "account_name": "https://example.com/page-one",
  "username": "user@domain.com",
  "completed": true,
  "completed_at": "2025-05-25T10:20:42.278Z",
  "completed_count": 2,
  "created_at": "2025-05-25T10:20:36.744Z",
  "progress": 1
}
```

{% hint style="success" %}
Each task within the batch request includes a download URL to access the data collected in that task.
{% endhint %}
