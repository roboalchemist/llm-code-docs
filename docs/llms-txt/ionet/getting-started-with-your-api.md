# Source: https://io.net/docs/reference/io-explorer/getting-started-with-your-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with IO Explorer API

> Use IO Explorer APIs to gain insight into the different elements of our network.

<iframe width="724" src="https://www.youtube.com/embed/XB54fut02cI" title="Get Started with the IO Explorer API" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Authentication

To use io.net APIs, you must supply a *JWT token* in the header of your request.

Follow the instructions below to generate a token:

1. Go to io.net > **Get Started** > **IO Explore** > and the **Workers** tab.
2. In the **UI**, right-click and select **Inspect**.
3. In the **Inspect** tool, click **Network**.
4. Refresh the **Workers** page.
5. In the list of elements, click **Devices**.
6. Scroll down to the **Request Headers** section.
7. Copy and store the token.

<Info>
  The token is valid for 21 days.
</Info>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1ffd3e640132d24930493d4b47ca81bf" alt="" data-og-width="2100" width="2100" data-og-height="1071" height="1071" data-path="images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f0fe4bed422b6ee4eccf97116af20cf6 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=327db7a2387ec83d8833f8e68f89beba 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=305152410f2b6fb3a75708437a9c3d18 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=7806d9e33a32e0aecc0a0dc3ade24272 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=ab0a042a1f06fe4bb93337297e4801a2 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/45b951bf59c4a475d763f3679454767ef7ee1890203e9add65bf58bfde5e73ae-api1.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=93162d35d60c72b8784f7c9743071d9d 2500w" />
</Frame>

### Make an API Call

You can use **cURL** to make API requests. Make sure you replace the following variables:

* `{device_id}`: Your actual **Device ID**, which you can copy from the *Device View* page.

  <Frame>
      <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=03a7d7bb5e9dfa852995d39d934565a7" alt="" data-og-width="698" width="698" data-og-height="88" height="88" data-path="images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f691769328656954ca93e168c6b29b27 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=6255b13b613c7ae7a3bb922358b7e5b6 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=d98e60cec5beb4b9ee71cb93dedb2d24 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=855e510ee7dff4b7f725266cb0704cbf 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=bcc33966d1c7c9a44dadc9e6639c8f8e 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/c62bb3b13e52950ecbbb8aead1c6da59d28c3092acdad7a791eec95fa46228d5-deviceID.png?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=b591f3c38b4497b9bdf441c906447efd 2500w" />
  </Frame>
* `{your_token}` : The **Token** you previously copied using the **Inspect Tool**.

```bash  theme={null}
curl X GET "https://api.io.solutions/v1/io-explorer/devices/{device_id}/details"
    -H "Token: {your_token}"
```

### Rate Limits

The base io.net API rate limit is as follows:

* 150 reqs / 10 second (umbrella Rate Limit on IO Explorer)
* **Summary:** 100 / 5 minutes
* **Details:** 100 / 5 minutes
* **Search:** 80 / 1 minute
