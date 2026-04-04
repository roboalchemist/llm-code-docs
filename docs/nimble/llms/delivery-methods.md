# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api/delivery-methods.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/delivery-methods.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api/delivery-methods.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/delivery-methods.md

# Delivery methods

Nimble API supports three delivery methods:

* [x] **Real-time** - the collected data is returned immediately to the user.
* [x] **Cloud** - the collected data is delivered to your preferred cloud storage repository.
* [x] **Push/Pull** - the collected data is stored on Nimble's servers, and can be downloaded via a provided URL.

For real-time delivery, see our page on performing a [real-time URL request](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/real-time-url-request). To use Cloud or Push/Pull delivery, use an **asynchronous request** instead. Asynchronous requests also have the added benefit of running in the background, so you can continue working without waiting for the job to complete.

To send an asynchronous request, use the ***<https://api.webit.live/api/v1/async/web>*** endpoint, such as in the example below:

{% hint style="info" %}
Nimble APIs requires that a base64 encoded credential string be sent with every request to authenticate your account. For detailed examples, see [Nimble APIs Authentication](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/nimble-apis-authentication).
{% endhint %}

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/async/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "storage_type": "s3",
    "storage_url" : "s3://Your.Repository.Path/",
    "callback_url": "https://your.callback.url/path"
}'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/async/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.example.com",
    "storage_type": "s3",
    "storage_url" : "s3://Your.Repository.Path/",
    "callback_url": "https://your.callback.url/path"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/async/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.example.com",
  "storage_type": "s3",
  "storage_url" : "s3://Your.Repository.Path/",
  "callback_url": "https://your.callback.url/path"
};

axios.post(url, data, { headers })
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
 "bytes"
 "encoding/base64"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/async/web"
 payload := []byte(`{
  "url": "https://www.example.com",
  "storage_type": "s3",
  "storage_url": "s3://Your.Repository.Path/",
  "callback_url": "https://your.callback.url/path"
 }`)
 headers := map[string]string{
  "Authorization":  "Basic <credential string>",
  "Content-Type":   "application/json",
 }

 req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
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

Asynchronous requests share the same parameters as real-time requests, but include a few additional parameters.

### Parameters

| Parameter         | Required | Description                                                                                                                                                                                                     |                                                                                                                  |
| ----------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **storage\_type** | Optional | <p>ENUM: s3                                                                                                                                                                                                     | gs - Use s3 for Amazon S3 and gs for Google Cloud Platform.<br><br>Leave blank to enable Push/Pull delivery.</p> |
| **storage\_url**  | Optional | <p>Repository URL: s3://Your.Bucket.Name/your/object/name/prefix/ The output will be saved to: s3://Your.Bucket.Name/your/object/name/prefix/TASK\_ID.json<br><br>Leave blank to enable Push/Pull delivery.</p> |                                                                                                                  |
| **callback\_url** | Optional | A URL to callback once the data is delivered. A POST request will be sent to the callback\_url with the task details once the task is complete (this “notification” will not include the requested data).       |                                                                                                                  |

{% hint style="info" %}
Before data can be delivered to a cloud storage location, certain permissions need to be set within your cloud storage provider.&#x20;
{% endhint %}

<details>

<summary> Setting GCS/AWS access permissions</summary>

### GCS Repository Configuration

In order to use Google Cloud Storage as your destination repository, please add Nimble’s system user as a principal to the relevant bucket. To do so, navigate to the “bucket details” page in your GCP console, and click on “Permission” in the submenu.

<img src="https://www.nimbleway.com/wp-content/uploads/2022/11/Screenshot-2022-11-13-185404.png" alt="" data-size="original">

Next, past our system user <mark style="color:red;background-color:yellow;"><nimbleway-gcp-storage@nimbleway-gcp.iam.gserviceaccount.com></mark> into the “New Principals” box, select <mark style="color:red;background-color:yellow;">Storage Object Creator</mark> as the role, and click save.

<img src="https://www.nimbleway.com/wp-content/uploads/2022/11/Screenshot-2022-11-13-185709.png" alt="" data-size="original">

That’s all! At this point, Nimble will be able to upload files to your chosen GCS bucket.

### S3 repository configuration

In order to use S3 as your destination repository, please give Nimble’s service user permission to upload files to the relevant S3 bucket. Paste the following JSON into the “Bucket Policy” (found under “Permissions”) in the AWS console.

**Follow these steps:**

&#x20;    1\. Go to the “Permissions” tab on the bucket’s dashboard:

<img src="https://www.nimbleway.com/wp-content/uploads/2022/11/Screenshot-2022-11-13-190030.png" alt="" data-size="original">

&#x20;    2\. Scroll down to “Bucket policy” and press edit:

<img src="https://www.nimbleway.com/wp-content/uploads/2022/11/Screenshot-2022-11-13-190216.png" alt="" data-size="original">

&#x20;    3\. Paste the following bucket policy configuration into your bucket:

{% code overflow="wrap" %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::744254827463:user/webit-uploader"
            },
            "Action": [
                "s3:PutObject",
                "s3:PutObjectACL"
            ],
            "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
        },
        {
            "Sid": "Statement2",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::744254827463:user/webit-uploader"
            },
            "Action": "s3:GetBucketLocation",
            "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME"
        }
    ]
}
```

{% endcode %}

**Important**: Remember to replace “YOUR\_BUCKET\_NAME” with your actual bucket name.

Here is what the bucket policy should look like:

<img src="https://www.nimbleway.com/wp-content/uploads/2022/11/Screenshot-2022-11-13-190440.png" alt="" data-size="original">

&#x20;    4\. Scroll down and press “Save changes”

<img src="https://www.nimbleway.com/wp-content/uploads/2022/11/Screenshot-2022-11-13-190635.png" alt="" data-size="original">

### S3 Encrypted Buckets

If your S3 bucket is encrypted using an AWS Key Management Service (KMS) key, additional permissions to those outlined above are also needed. Specifically, Nimble's service user will need to be given permission to encrypt and decrypt objects using a KMS key. To do this, follow the steps below:

1. Sign in to the AWS Management Console and open the AWS Key Management Service (KMS) console.

   <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/j5qIsCoZjFZ15GjgiUa9/S3%20Keys%20-%20Step%201.png" alt="" width="563"><figcaption></figcaption></figure>
2. In the navigation pane, choose "Customer managed keys".

   <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/RTx8Br12gRG1wQ3BzMfu/S3%20Keys%20-%20Step%202.png" alt="" width="563"><figcaption></figcaption></figure>
3. Select the KMS key you want to modify.<br>

   <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/Ns4Zv6LpAeGMwqtWwJ0T/S3%20Keys%20-%20Step%203.png" alt="" width="563"><figcaption></figcaption></figure>
4. Choose the "Key policy" tab, then "Switch to policy view".<br>

   <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/mYjdta81K01AE1nZPPXZ/S3%20Keys%20-%20Step%204.png" alt="" width="375"><figcaption></figcaption></figure>
5. Click "Edit".<br>

   <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/FKGqtmCHoASnEjKFIR26/S3%20Keys%20-%20Step%205.png" alt="" width="563"><figcaption></figcaption></figure>
6. Add the following statement to the existing policy JSON, ensuring it's inside the Statement array:

```json
{
 "Version": "2012-10-17",
 "Id": "example-key-policy",
 "Statement": [
  // ... your pre-existing statements ...
  {
   "Sid": "Allow Nimble APIs account",
   "Effect": "Allow",
   "Principal": {
    "AWS": "arn:aws:iam::744254827463:user/webit-uploader"
   },
   "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey"
   ],
   "Resource": "*"
  },
 ]
}
```

1. Click "Save changes" to update the key policy.<br>

   <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/KoN9YlDPlhXaTs8v9VcI/S3%20Keys%20-%20Step%206.png" alt="" width="563"><figcaption></figcaption></figure>

That's it! You've now given Nimble APIs permission to encrypt and decrypt objects, enabling access to encrypted buckets.

</details>

### Selecting a delivery method

**To enable cloud delivery:**

* Set the **storage\_type** parameter to either s3 or gs
* Set the **storage\_url** parameter to the bucket/folder URL of your cloud storage where you'd like the data to be saved.

**To enable Push/Pull delivery:**

* Leave both the **storage\_type** and **storage\_url** fields blank. Nimble will automatically recognize that Push/Pull delivery has been selected.

### Asynchronous Request Process

![](https://www.nimbleway.com/wp-content/uploads/2022/10/asynchronous-request.png)

Unlike real-time requests, asynchronous requests do not return the result directly to the client. Instead, an asynchronous request produces a “task” that runs in the background and delivers the resulting data to a cloud storage bucket and/or callback URL. Tasks go through four stages:

| Status    | Description                                                                    |
| --------- | ------------------------------------------------------------------------------ |
| pending   | The task is still being processed.                                             |
| uploading | The results are being uploaded to the destination repository.                  |
| success   | Task was complete and stored in the destination repository.                    |
| failed    | Nimble was unable to complete the task, no file was created in the repository. |

### **Initial Response**

In response to triggering an asynchronous request, the details of the created task are returned, which can later be used to check its status. The response contains the Task ID, as well as other information, and is structured as follows:

{% code overflow="wrap" %}

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

{% endcode %}

### **Checking Task Status**

To check the status of an asynchronous task, use the endpoint ***<https://api.webit.live/api/v1/tasks/\\>\<task\_id>***

For example:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X GET 'https://api.webit.live/api/v1/tasks/Task_ID' \
--header 'Authorization: Basic <credential string>'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/tasks/Task_ID'
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

const url = 'https://api.webit.live/api/v1/tasks/Task_ID';
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
 url := "https://api.webit.live/api/v1/tasks/Task_ID"
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

The response object has the same structure as the Task Completion object that is sent to the <mark style="color:red;background-color:yellow;">callback\_url</mark> upon task completion.

### **Checking Tasks List**

To check the status of asynchronous tasks list, use the endpoint \
\&#xNAN;***<https://api.webit.live/api/v1/tasks/list>***

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

### **Task Completion**

A POST request will be sent to the <mark style="color:red;background-color:yellow;">callback\_url</mark> once the task is complete which contains the following information:

{% code overflow="wrap" %}

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

{% endcode %}

Asynchronous requests also have methods for handling upload failures. For more information, see the Nimble Web API Documentation.
