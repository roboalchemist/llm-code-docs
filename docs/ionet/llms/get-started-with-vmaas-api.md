# Source: https://io.net/docs/reference/vmaas/get-started-with-vmaas-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with VMaaS API

The **Virtual Machine as a Service (VMaaS) APIs** lets you programmatically deploy and manage virtual machines on io.net Cloud. Unlike CaaS (Containers as a Service), VMaaS provides full VM instances with CPU, GPU, memory, and storage resources — ideal for long-running workloads, custom environments, or GPU-intensive tasks.

## Generate an API key

You can obtain an API key for io.net Cloud to use VMaaS in two ways:

1. From the web interface.
2. By using a two-step process (first generate a JWT token, then request the API key using curl).

### Option 1: Generate an API Key via Web Interface

IO Clouds APIs authenticate requests using API keys. You can [generate API keys from your user](https://ai.io.net/ai/api-keys) account.\
**Note: When generating an API key, make sure to specify the associated IO Cloud project.**

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service in your backend server.
</Warning>

### Option 2: Generate an API Key Using a JWT Token

#### Step 1: Get a JWT Token

io.net APIs are built around [RESTful](https://en.wikipedia.org/wiki/REST) principles. You can use io.net APIs to gain insight into different elements of the network.

To use [io.net](http://io.net) APIs, you must provide a JWT token in the header of your request.

Follow the instructions below to generate a token:

1. Go to **io.net** > **IO ID** > **IO Clouds** tab.
2. In the UI, right-click and select **Inspect**.
3. In the Inspect tool, click **Network**.
4. Refresh the **IO Clouds** page.
5. In the list of elements, click **Devices**.
6. Scroll down to the **Request Headers** section.
7. Copy and store the token.

<Note>
  This token is valid for 21 days.
</Note>

<img src="https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas1.jpg?fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=e0dc81e10dcfba57a05a938479aee905" alt="Vmaas1 Jp" data-og-width="2100" width="2100" data-og-height="1071" height="1071" data-path="images/reference/vmaas/vmaas1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas1.jpg?w=280&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=403b173e7cabd322862e433a570dce0d 280w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas1.jpg?w=560&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=30994305323fed3947871aee83f8a8bf 560w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas1.jpg?w=840&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=882ae9d9d4177ae7d5ace14041f1b324 840w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas1.jpg?w=1100&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=21ffa61625350f5c405e6cf6b3921685 1100w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas1.jpg?w=1650&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=aa4b0a08960825591fc0169bd9991cc4 1650w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas1.jpg?w=2500&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=3df1ac7b9bd5bb6a3bcee2504b6d0aae 2500w" />

#### Step 2. Generate an API Key via `curl`

Use the **JWT token** to request your API key:

```curl  theme={null}
curl -X POST 'https://api.io.solutions/v1/api-keys/' \
  -H 'accept: application/json' \
  -H 'token: $JWT_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "description": "API Key Name",
    "expires_at": "2025-07-17T19:54:36.418Z",
    "project": "io-cloud",
    "scopes": ["all"]
}'
```

Use the returned key with the `X-API-KEY` header in your requests.

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service in your backend server.
</Warning>

<img src="https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas2.jpg?fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=295d00739280e14b1bac8a42261bfa46" alt="Vmaas2 Jp" data-og-width="1457" width="1457" data-og-height="939" height="939" data-path="images/reference/vmaas/vmaas2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas2.jpg?w=280&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=4b85ec2f302b46c7f81a2b60e7f89511 280w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas2.jpg?w=560&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=624a9a9d8dc93debfdfba2039b52207e 560w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas2.jpg?w=840&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=f4d9554fcad63b4a141e08a5aec28d38 840w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas2.jpg?w=1100&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=a0021f62ca40110c16356e04e3ea9674 1100w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas2.jpg?w=1650&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=c7e61b43a81d0a6ba5670ac10703393e 1650w, https://mintcdn.com/ionet-cca8037f/kqMMgYJJK8i2i1uK/images/reference/vmaas/vmaas2.jpg?w=2500&fit=max&auto=format&n=kqMMgYJJK8i2i1uK&q=85&s=a8e82818eb8cf330ab38ec59ecb94fe4 2500w" />

## Making requests

<Note>
  Accessing APIs requires IO credits. Make sure you have sufficient IO credits before using any API endpoint.

  Contact support or visit the IO Credits documentation page for more details.
</Note>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: X-API-KEY $IOCLOUD_API_KEY
```

Replace `$IOCLOUD_API_KEY` with your **API key**.

### Example: Deploy VMs

The following `curl` command demonstrates how to deploy VMs in IO Cloud.\
Make sure to include your `x-api-key` header and, if needed, adjust the query parameters such as `status`, `page`, or `page_size`.:

```curl  theme={null}
curl -X POST "https://api.io.solutions/enterprise/v1/io-cloud/vmaas/deploy?page=0&page_size=10&status=running" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY_HERE" \
  -d '{
    "name": "test-deployment",
    "hardware_quantity": 2,
    "hardware_name": "NVIDIA A100",
    "region": "us-east-1"
  }'
```

This request should return a similar response:

```json  theme={null}
{
  "data": {
    "deployments": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "status": "running",
        "name": "test-deployment",
        "completed_percent": 75,
        "hardware_quantity": 2,
        "brand_name": "NVIDIA",
        "hardware_name": "A100",
        "compute_minutes_served": 120,
        "compute_minutes_remaining": 240
      }
    ],
    "total": 1,
    "statuses": ["running"]
  }
}
```
