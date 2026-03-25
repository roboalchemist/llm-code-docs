# Source: https://docs.nimbleway.io/general/onboarding-guide/nimble-api-basics.md

# Nimble API Basics

{% embed url="<https://www.loom.com/share/5838132ea57c4c649ea081c13ad14012?sid=05f6a7bc-499a-409d-98db-457185c51cf5>" %}

### Which API is right for me?

Nimble APIs includes four different APIs - but knowing which one is right for you is easy!

<table data-card-size="large" data-view="cards"><thead><tr><th align="center"></th><th></th><th></th></tr></thead><tbody><tr><td align="center"><strong>Web API</strong></td><td><strong>Stream Public Web Data from Any URL.</strong></td><td>Includes powerful tools such as page interactions, parsing templates, Internal API Network Capture, and more.</td></tr><tr><td align="center"><strong>SERP API</strong></td><td><strong>Seamlessly scrape search engine data.</strong></td><td>Specialized for SERPs including Google, Bing, and Yandex, and includes granular localization tools.</td></tr><tr><td align="center"><strong>Maps API</strong></td><td><strong>Capture fresh &#x26; rich business data from Maps engines.</strong></td><td>Discover businesses in any geographic area, collect in-depth public data about each one, and gather user-generated reviews.</td></tr><tr><td align="center"><strong>E-commerce API</strong></td><td><strong>Gather product data from major E-commerce marketplaces.</strong></td><td>Find and collect clean, accurate product data from marketplaces such as Amazon, Walmart, Google Shopping, and more.</td></tr></tbody></table>

If you're not sure which API is right for you, we recommend starting with the Web API. However, if your use case fits in one of our specialized APIs, we encourage you to explore those as well for more tailored solutions to meet your specific needs.

### Setting Up An API Pipeline

By default, you account will come with an out-of-the-box API pipeline. If you prefer to keep things simple, feel free to skip this step and just use that pipeline. However, as your usage expands, pipelines will become more and more useful in organizing, compartmentalizing, and tracking your activity.

To create a new pipeline, follow these steps:

1. Log in to the User Dashboard.
2. Go to the "Pipelines" page.
3. Click "+ Add Pipeline" on the right side of the page.
4. Enter a name for the pipeline, and select "Nimble API" as the pipeline type in order to use it for data requests, then click "Next".

Your new pipeline is ready to go! On the completion screen you'll receive the pipeline username, password, authentication token, and a "Hello World" request example.

You can always get the pipeline's details again in the pipeline overview page.

### Sending Your First Data Request

{% hint style="info" %}
If you followed along with the previous step, you can copy the "Hello World" example from the pipeline creation confirmation and skip straight ahead to executing your request.
{% endhint %}

<details>

<summary>Using the Playground Query Builder</summary>

The easiest way to get started with Nimble APIs is to head to the **Playground.** The Playground features an interactive query builder that can help you learn how to write API requests, and even execute and display the results.

To visit the Playground:

1. Log in to the User Dashboard.
2. Click on "Playground" on the left hand side.

At the top of the page, you'll be able to select which Nimble product you'd like to try. By default, Nimble API will already be open.

Next, select the relevant API. If you're not sure which API you need, see "Which API is right for me?" at the top of this page.

On the left hand side, you'll see the parameters and options you can configure, such as the pipeline to use, the URL from which to collect data, Javascript page rendering, parsing, and more. As you make changes, the query builder on the right will automatically highlight and update your sample query in keeping with your changes.

For your first request, we recommend enabling "Page Render" and "Parse". This will execute javascript on the page, ensuring it's fully rendered, and parse the results into a readable format.

Once you've configured your request, click "**Run Request**" on the bottom right. After a few moments, the page you requested will appear on the bottom left, and the result data on the right.

**Congratulations! You just ran your first request.**

You can also copy the sample request code that the playground constructed and execute it in your terminal or application.

</details>

<details>

<summary>Sending A Basic cURL request</summary>

Sending Nimble API requests is straightforward. Let’s break down a basic cURL request:

<pre class="language-bash"><code class="lang-bash">
curl -X POST '&#x3C;https://api.webit.live/api/v1/realtime/web>' \\
<strong>    -H 'Authorization: Basic &#x3C;Base64 Token>' \\
</strong>    -H 'Content-Type: application/json' \\
--data-raw '{
<strong>    "url": "&#x3C;https://www.google.com/search?q=hello> world",
</strong>    "render": false,
<strong>    "parse": false,
</strong>    "country": "ALL",
    "locale": "en"
}'
</code></pre>

* **`<credential string>`** - Replace this with your API Pipeline's Base64 Token.
* **`url`** - The target URL you'd like to collect.
* **`country`** - The origin country from which to send the request.
* **`render`** - Execute JS on the requested webpage.
* **`parse`** - Structures the HTML into a machine-readable JSON format.

</details>

### Next Steps

Nimble's APIs are rich with features! To take your data collection to the next level, we recommend checking out the following resources:

* [x] [**Nimble API Quick Start Guide:**](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide) Learn more about the capabilities of Nimble APIs and take your data collection to the next level.
* [x] [**Delivery Methods**:](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/delivery-methods) Nimble APIs can deliver data asynchronously to your cloud storage or via push pull.
* [x] [**Page Interactions:**](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction) Nimble's APIs can click, scroll, wait, and perform other interactions with a webpage before returning data.
* [x] [**Batch Processing:**](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/batch-processing)Group up to 1,000 different requests in a single batch - with fully customizable options for each one.
