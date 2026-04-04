# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api/batch-processing.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/batch-processing.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api/batch-processing.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/batch-processing.md

# Batch processing

To collect data from multiple URLs with a single request, use a **batch request**. Batch requests share largely the same structure and cycle as [asynchronous requests](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/delivery-methods), but can perform up to 1,000 tasks in a single batch, and have a dedicated endpoint. To initiate a batch request, use the ***<https://api.webit.live/api/v1/batch/web>*** endpoint, such as in the example below:

{% hint style="info" %}
Nimble APIs requires that a base64 encoded credential string be sent with every request to authenticate your account. For detailed examples, see [Nimble APIs Authentication](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/nimble-apis-authentication).
{% endhint %}

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

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

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

url = 'https://api.webit.live/api/v1/batch/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "requests": [
        { "url": "https://www.finance.com" },
        { "url": "https://www.travel.com" },
        { "url": "https://www.socialmedia.com" }
    ],
    "storage_type": "s3",
    "storage_url": "s3://Your.Repository.Path/",
    "callback_url": "https://your.callback.url/path"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code overflow="wrap" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/batch/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "requests": [
    { "url": "https://www.finance.com" },
    { "url": "https://www.travel.com" },
    { "url": "https://www.socialmedia.com" }
  ],
  "storage_type": "s3",
  "storage_url": "s3://Your.Repository.Path/",
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

{% endcode %}
{% endtab %}

{% tab title="Go" %}
{% code overflow="wrap" %}

```go
package main

import (
 "bytes"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/batch/web"
 payload := []byte(`{
  "requests": [
   { "url": "https://www.finance.com" },
   { "url": "https://www.travel.com" },
   { "url": "https://www.socialmedia.com" }
  ],
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

{% endcode %}
{% endtab %}
{% endtabs %}

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

Tasks in a batch request all share the same request settings, such as location, rendering, parsing, etc.

Once a batch request is initiated, a `batch_id` is produced that can be used to check the progress/status of a batch or retrieve a summary of the batch. Every time a task within the batch is completed, an individual completion notification is sent to the provided callback URL.

For a more in-depth walkthrough on batch requests, please see the [API Functions Documentation](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions).
