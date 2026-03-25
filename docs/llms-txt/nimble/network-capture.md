# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/network-capture.md

# Network Capture

{% hint style="info" %}
It's important to fully understand and abide by the Terms Of Use of every website, and to avoid collecting private data in accordance with all relevant laws and regulations.
{% endhint %}

## Overview <a href="#what-and-why" id="what-and-why"></a>

In the past, when a webpage was requested, all of the information presented on the page would be loaded and presented together as a single package. All the HTML, images, Javascript, CSS, and other resources were an inherent part of the webpage itself.

However, over time businesses discovered many advantages in loading some data dynamically. Retail platforms like Amazon run dynamic pricing algorithms that adjust the price of each product in real time. Search Engines use lazy-loading strategies instead of pagination - loading new information as the user scrolls without reloading the page.

A common technical approach to managing and loading information dynamically in this manner involves creating internal APIs. Businesses use internal APIs - which are not explicitly exposed to users - to request information and then add it to the presented webpage.

In the below example, we use Chrome's Developer Tools to demonstrate how Expedia loads data dynamically from an internal API:

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/WVytbuxx6AhWRUs43aR9/section-3.png" alt=""><figcaption></figcaption></figure>

By capturing these internal API calls, developers can directly access key data in machine-readable formats - typically JSON. This circumvents the need to parse the desired data out of HTML.

Furthermore, by understanding the inputs of these internal APIs, developers over time can learn how to interact with them directly, with no need to go through the public-facing webpages.

## What?

**Network Capture** Feature allow users to capture internal API calls to collect lazy-loaded/dynamic data and to interact with it directly, with no need to go through the public-facing webpages.

To capture internal website APIs, the user could filter the desired calls based on:

* **Exact match filter** - based on internal call URL and method (GET/POST/Any)
* **Containing a match** - based on internal call URL and method (GET/POST/Any)
* **Resource Type** - based on the internal API resource type (Fetch/XHR/Stylesheet/Script/etc.)

## &#x20;Why? <a href="#what-and-why" id="what-and-why"></a>

* **Access to Dynamic and Lazy-Loaded Content**: Many websites today load data asynchronously after the initial page load, often in response to user actions or as the user scrolls down the page. The network capture feature allows you to intercept these internal API calls and capture this dynamic content directly. This is essential for extracting data that isn't immediately available on the webpage at load time but is instead loaded dynamically as needed.
* **Direct Interaction with APIs**: By capturing internal API calls, you can bypass the need to interact with the user interface of public-facing webpages. This direct interaction with APIs is not only faster but also more efficient as it eliminates the overhead associated with rendering the UI. It allows for more precise and targeted data extraction, directly from the source of the data.
* **Efficiency and Speed**: Interacting with internal APIs is generally more efficient than scraping content from fully rendered webpages. APIs are designed to transmit data in a structured format, typically JSON, which is easier and quicker to parse compared to extracting information from HTML content. This increases the overall speed and efficiency of the data collection process.
* **Reduced Overhead and Lower Resource Usage**: Since you are bypassing the graphical elements of a website and focusing only on the data transfer, the network capture feature reduces the computational load on your system. This leads to lower resource usage and can significantly decrease the costs associated with data extraction, particularly at scale.
* **Enhanced Data Accuracy and Reliability**: API data is typically more structured and less prone to errors compared to data scraped from the frontend of a website. By capturing data directly from API calls, you reduce the likelihood of scraping errors associated with frontend changes, ensuring higher data accuracy and reliability.

## Additional Information <a href="#how" id="how"></a>

* <mark style="color:green;">Supported</mark> by real-time, asynchronous, and batch requests.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api)
* <mark style="color:red;">Not supported</mark> Endpoints: [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api) and [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api).
* Requires page rendering
* While no one field of `network_capture` is required, **sending at least one field** is required.
* If a `url` filter is defined, the `value` field must be set as well.

{% hint style="warning" %}
Network Capture will not function if rendering is not enabled in the request. Please be sure to set <mark style="color:red;background-color:yellow;">render:true</mark> in order for it to function correctly.
{% endhint %}

### Example Request <a href="#example" id="example"></a>

Requests can be captured by using the **`network_capture`** field, which receives a JSON array that can include one or more filters. Each filter specifies which requests should be collected for later inspection.

<table><thead><tr><th width="184">Parameter</th><th width="225">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>url</code></td><td>Required when filtering by URL</td><td>Object | Describes the URL(s) to filter and capture, for more info see <a href="network-capture/filter-by-url-matching">Filtering by URL</a></td></tr><tr><td><code>resource_type</code></td><td>Required when filtering by resource type</td><td>List [Enums] | set all required resource type to filter, for more info see <a href="network-capture/filter-by-resource-type">Filtering by Resource Type</a></td></tr><tr><td><code>method</code></td><td>Optional (default = <code>Any</code>)</td><td>Enum |  HTTP method should be filtered for. Examples: <code>GET</code>, <code>POST</code>, <code>PUT</code>. </td></tr><tr><td><code>validation</code></td><td>Optional (default = false)</td><td>Bool | Determine whether to run content validation on the responses or not</td></tr></tbody></table>

The below example demonstrates two simple network capture filters, and how they are performed:

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/web/' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
    "country": "US",
    "network_capture": [
        {
            "method": "GET",
            "url": {
               "type": "exact",
               "value": "https://i5.walmartimages.com/a14/capabilities.min.js"
            }
        },
        {
            "url": {
                "type": "contains",
                "value": "/graphql/Search"
            }
        }
    ]
}'
```

{% endtab %}
{% endtabs %}
