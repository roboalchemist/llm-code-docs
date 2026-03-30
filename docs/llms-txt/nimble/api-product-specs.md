# Source: https://docs.nimbleway.io/nimble-sdk/web-api/api-product-specs.md

# API Product Specs

## **Overview**

Nimble's Web API is designed as a product with clear rate limits and performance specifications. Customers can expect transparent access to supported rate limits across driver versions and dynamic selection capabilities without needing to consider the internal server management or associated costs.

## **Rate Limits**

Our rate limits vary based on both the selected [Browserless Driver](https://docs.nimbleway.io/technologies/browserless-drivers) (VX6 to VX12) and the selected Plan. Below is a table summarizing request-per-second (r/s) limitations per driver and plan:

<table data-full-width="false"><thead><tr><th width="96">Driver</th><th width="112">PAYG</th><th width="121">Beginner</th><th width="137">Essential</th><th width="143">Advanced</th><th width="169">Professional</th><th>Enterprise</th></tr></thead><tbody><tr><td><strong>VX6</strong></td><td>20 r/s</td><td>40 r/s</td><td>60 r/s</td><td>80 r/s</td><td>100 r/s</td><td>∞</td></tr><tr><td><strong>VX8</strong></td><td>10 r/s</td><td>20 r/s</td><td>30 r/s</td><td>45 r/s</td><td>60 r/s</td><td>∞</td></tr><tr><td><strong>VX10</strong></td><td>5 r/s</td><td>10 r/s</td><td>20 r/s</td><td>30 r/s</td><td>40 r/s</td><td>∞</td></tr><tr><td><strong>VX12</strong></td><td>5 r/s</td><td>5 r/s</td><td>5 r/s</td><td>5 r/s</td><td>10 r/s</td><td>20 r/s</td></tr></tbody></table>

{% hint style="info" %}
**Configurations Beyond Standard Support -** For configurations beyond standard rate limits or driver capabilities, additional service options are available. Contact our support team for more details on custom configurations.
{% endhint %}

### **Driver Overview**

Nimble [Browserless Drivers](https://docs.nimbleway.io/technologies/browserless-drivers) are a collection of unique data gathering technologies designed for specific data retrieval needs, with dynamic selection as a core feature. Here’s an outline of each driver’s capabilities:

* **Driver VX6:** Suitable for simple, low-demand requests.
* **Driver VX8:** Offers enhanced stealth undetection for general data gathering and web automation.
* **Driver VX10:** Advanced stealth and access capabilities for complex websites.
* **Driver VX12:** Optimized for social media and person-data retrieval.

Web API dynamically selects the optimal driver based on your specific request’s requirements to ensure efficient and reliable data collection.

### **Dynamic Driver Selection**

Our API’s dynamic selection feature uses website-specific knowledge to automatically choose the best driver for each request, enhancing performance and ensuring rate limit efficiency. Customers can also manually select a driver to tailor the request as needed.
