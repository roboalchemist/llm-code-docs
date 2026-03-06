# Source: https://io.net/docs/reference/caas/get-started-with-caas-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with CaaS API

> The CaaS API lets you programmatically deploy and manage high-performance containerized workloads on io.net’s decentralized GPU network.

<iframe width="100%" src="https://www.youtube.com/embed/o5bCqYcBPyc" title="Get Started with CaaS API" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Generate an API key

You can obtain an API key for IO Cloud in two ways:

1. Via the web interface
2. By using a two-step process (first generate a JWT token, then request the API key using cURL).

### Option 1: Generate an API Key via Web Interface

IO Clouds APIs authenticate requests using API keys. You can [generate API keys from your user](https://ai.io.net/ai/api-keys) account. **Note: When generating an API key, make sure to specify the associated IO Cloud project.**

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

### Option 2: Generate an API Key Using a JWT Token

#### Step 1. Get a JWT Token

IO's API is built around [RESTful](https://en.wikipedia.org/wiki/REST) principles. You can use IO's APIs to gain insights into different elements of our network.

To use IO's APIs, you must supply a JWT token in the header of your request. Follow the instructions below to generate a token:

1. Go to **io.net** > **IO ID** > **io.cloud** tab.
2. In the UI, right-click and select **Inspect**.
3. In the Inspect tool, click **Network**.
4. Refresh the **io.cloud** page.
5. In the list of elements, click **Devices**.
6. Scroll down to the **Request Headers** section.
7. Copy and store the **Token**.

<Info>
  This token is valid for 21 days.
</Info>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=dcb9f11c208478d858fc2a9f05eaca51" alt="" data-og-width="2100" width="2100" data-og-height="1071" height="1071" data-path="images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=62352930fd0d5bbedf3e67a8eee81f60 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c54846d692987372ed1962474dd72578 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9620d2dfadb1d229287a0ba949c72cad 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=aa3ce3c0824d36eaef44ef4fd017f5b5 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5519e1df67181a6796f6bc6bdab96f31 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/7871c6217eaab2813019860f8f0eaca5e01ef4295838e14d50c9777e4272694b-45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=857081ee2942d675a2a27bb8d8b769e9 2500w" />
</Frame>

#### Step 2. Generate an API Key via `cURL`

Use the **JWT token** to request your API key:

<CodeGroup>
  ```curl curl theme={null}
  curl -X POST 'https://api.io.solutions/v1/api-keys/' /
    -H 'accept: application/json' /
    -H 'token: $JWT_TOKEN' /
    -H 'Content-Type: application/json' /
    -d '{
      "description": "API Key Name",
      "expires_at": "2025-07-17T19:54:36.418Z",
      "project": "io-cloud",
      "scopes": ["all"]
  }'
  ```
</CodeGroup>

Use the returned key with the `X-API-KEY` header in your requests.

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5cb5da643d6ec0c049c89d646ff40497" alt="" data-og-width="1457" width="1457" data-og-height="939" height="939" data-path="images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=8c87b1d5bc567fd798a8ea05c77293cc 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9d8e3e871b0c74a84ed4a627c4fba0d8 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9174032f1cc90f18c3cceff4f35f929f 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1b353d88b6f924bd57ab11c402c78b68 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=52ebd6884e0e741e076c49bfd4d9dba3 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/89ab76409859c2f7bd75f88f932c24c7fa847bc0093c39a43e6efef78020266b-Containers6.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=e0625abe15e3107f86becdf663833111 2500w" />
</Frame>

## Making requests

<Danger>
  Accessing APIs requires IO Credits. Please make sure to request IO credits before using any API endpoints. Contact support or visit the [IO Credits](/guides/payment/io-credits) page for more information.
</Danger>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: X-API-KEY \$IOCLOUD_API_KEY
```

Replace `$IOCLOUD_API_KEY` with your actual **API key.**

### Example: Check Available Replicas per Location

Here is an example `cURL` command to check available replicas per location in IO Cloud:

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.io.solutions/enterprise/v1/io-cloud/caas/available-replicas?hardware_id={hardawer_id}&hardware_qty={hardware_qty} /
    -H "X-API-KEY: \$IOCLOUD_API_KEY" 
  ```
</CodeGroup>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=a5a818b49b5c4c2c436f4a886951bc25" alt="" data-og-width="1457" width="1457" data-og-height="522" height="522" data-path="images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=d0dd238e53f38c75d06b0348d1c48409 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=4f14a4d3f5694a3c15846cf17f1aeaef 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=564d17f339ab56688a168afe24df31e4 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=70c6d7ccef74f17b83a865c68cbae471 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c722a4a980b9f3605dabe0a0236073c5 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/53092fbca3b4f3a0eb6aa24faff77e70cb6d6f6f7519125d655babac48552ed9-Containers7.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c3ed2737a2e5d703143e6139bd8dc677 2500w" />
</Frame>

This request should return a response as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "data": [
      {
        "id": 0,
        "iso2": "string",
        "name": "string",
        "available_replicas": 0
      }
    ]
  }
  ```
</CodeGroup>
