# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/network-capture/filter-by-resource-type/real-world-demo-capturing-ajax-requests.md

# Real World Demo: Capturing Ajax Requests

One of the most popular use cases for Network Capture is capturing Ajax requests. Websites use Ajax requests to communicate information back and forth between the frontend and backend of their websites or applications.

Because the exchanged data is often structured, capturing Ajax requests can be a great way to access parsed data directly.

Furthermore, many internal APIs can be communicated with directly, saving bandwidth by not loading the frontend on every request.

To capture Ajax requests, use **`network_capture`** with the **`resource_type`** filter set to `XHR` and `Fetch`:

Copy

```
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.walmart.com/search?q=iphone",
    "render": true,
    "network_capture": [
        {
            "method": "GET",
            "resource_type": [
                "xhr", "fetch"
            ]
        }
    ]
}'
```
