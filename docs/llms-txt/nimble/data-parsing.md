# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/data-parsing.md

# Data Parsing

## What? <a href="#what-and-why" id="what-and-why"></a>

Transforming raw HTML into clean, accurate, and useable data is no easy task. With each website having its own unique layout and unpredictable updates, it's important to have a diverse set of powerful tools to ensure consistent and accurate data extraction.

Nimble's Web API comes built-in with three tools to help you effectively extract the key data you need easily, reliably, and at scale.

* [x] **Parsing Templates:** flexible, precise user-defined parsing templates based on CSS selectors.
* [x] **Merge Dynamic Parser:** provides users with the ability to seamlessly integrate Nimble's AI-powered parsing with custom parsing logic into a single, unified response.&#x20;
* [x] **Nimble AI Parsing Skills (coming soon):** fully-automated, AI-powered parsing engine with high customizability.

Let's look at each one in more detail and examine some examples to understand when it's right to use each one.

<details>

<summary>Parsing Templates</summary>

Nimble Parsing Templates provide users with an easy to use, surgical parsing tool for parsing with a high degree of control and specificity. Parsing Templates provide a set of functions (called Types, Extractors, and Objects) that users can harness to accurately parse the exact web data they want.

Parsing Templates offer similar levels of accuracy and freedom to Beautiful Soup, but with significantly less complexity. Their goal is to help users fill gaps left by automated systems when collecting data from unorthodox or highly-specialized sources.

However, unlike Beautiful Soup, Parsing Templates have a much lower learning curve, and operate seamlessly alongside AI Parsing Skills, allowing for them to be used in parallel or independently from Nimble's other parsing solutions.

[Learn more about Parsing Templates ->](#parsing-templates)

</details>

<details>

<summary>Merge Dynamic Parser</summary>

The Merge Dynamics feature enables users to combine Nimble's AI-powered parsing with their own custom parsing logic into a single, unified response.&#x20;

This allows for a highly customizable and flexible approach to data extraction, where the precision and automation of AI parsing can be enhanced or tailored by incorporating specific user-defined parsing rules.&#x20;

The result is a comprehensive and cohesive data set that aligns perfectly with your unique requirements.

This feature is particularly useful for scenarios where standard AI parsing might need refinement or additional context provided by custom logic, ensuring that the final output meets your exact needs.

learn more

</details>

<details>

<summary>Nimble AI Parsing Skills (Beta)</summary>

Nimble AI Parsing Skills empower engineers to easily parse web data from any webpage into accurate, consistent JSON structures. By combining HTML-trained LLMs with classical parsing techniques, AI Parsing Skills make scalable parsing of any quantity and variety of web pages in real-time possible.

* **Automatic mode:** in automatic mode, no user input is needed at all. [Simply enable parsing](#enable-parsing), and our system does the rest. Behind the scenes, Nimble uses our built-in collection of generic parsing skills to extract data from webpages. Results are generally good, but may vary from page to page.
* **Skills Mode&#x20;**<mark style="color:purple;">**(coming soon)**</mark> : In Skills mode, the user creates a simple, plain-English schema that guides the creation of custom parsers - also called Skills.

</details>

## &#x20;Why? <a href="#what-and-why" id="what-and-why"></a>

1. **Enhanced Accuracy**: LLMs are adept at understanding the context and structure of web content, enabling them to parse complex web data more accurately than traditional parsing tools. This results in higher-quality data extraction, particularly from sophisticated web pages including site stricture changes.
2. **Scalability**: AI models can handle a wide range of website layouts and structures without needing specific rules for each site. This scalability makes it easier to process data from a broad spectrum of sources with minimal setup time.
3. **Continuity:** Unlike traditional parsers that require pre-defined schemas and are often brittle to changes in web page design, AI-based parsing adapts to changes in webpage layouts and content schemes, reducing the need for frequent manual updates.
4. **Efficiency**: By automating the structuring of data into usable formats, this feature saves significant time and effort that would otherwise be spent on manual data cleaning and organization. This allows users to focus on analysis and insights rather than data preprocessing.
5. **Integration Readiness**: The structured data output from AI Parsing is readily integrable into various data analysis tools and applications, enhancing the workflow from data collection to actionable insights.

### Which tool is right for me?

Each tool has its own unique advantages and disadvantages. The below table should help clarify the features of each individual tool, and help you decide which is right for you. It's also important to remember that these tools can operate in parallel within each request, and we encourage users to try out each one and experiment to get the best results

<table><thead><tr><th></th><th width="171">AI Parsing Skills</th><th width="180">Parsing Templates</th><th>Merge Dynamic</th></tr></thead><tbody><tr><td>Fully-automated</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Manual control</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Auto-healing</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Easy to use</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>CSS Selector targeting</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>

## Additional Information <a href="#how" id="how"></a>

* <mark style="color:green;">Supported</mark> by realtime (except cloud delivery), asynchronous, and batch requests.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api) and [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api).
* <mark style="color:red;">Not supported</mark> Endpoints: [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api)

## Request Option <a href="#request-option" id="request-option"></a>

### Enable Parsing <a href="#enable-parsing" id="enable-parsing"></a>

To run Nimble API request that requires data parsing (HTML -> JSON), the user simply needs to include the `parse` parameter to  `true`. Behind the scenes, the Nimble AI Parser will dynamically parse the webpage HTML content into structured data format (JSON).

### Data Formatting <a href="#json-structuring-2" id="json-structuring-2"></a>

To set Nimble API data response format as JSON (instead of HTML), the user simply needs to include the parameter `"format": JSON` in the body of the request. Actually this is the default value of `format` param so the user don't need manually set it, but this is configurable.

<table><thead><tr><th width="138">Parameter</th><th width="168">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>parse</code></td><td>Optional (default = <code>false</code>)</td><td>Enum: <code>true</code> | <code>false</code> - True - the page's content will be parsed and returned in a JSON format. False - Response will include page headers and raw data (without parsing). </td></tr><tr><td><code>format</code></td><td>Optional (default = <code>JSON</code>)</td><td>Enum: <code>JSON</code> | <code>HTML</code> - The data response format. HTML - in case of error, returns JSON with error message.</td></tr></tbody></table>

{% hint style="info" %}
When setting `parse` as `true`, the `format` must be set to `JSON` (which is the default format)
{% endhint %}

**Example Request**

* Actually no need as JSON is the default value of `format`

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.google.com",
    "parse": true,
    "format": "json"
}'
```

{% endtab %}
{% endtabs %}

### Next Steps

Dive into the full guides for each of Nimble's parsing solutions:

<table data-view="cards"><thead><tr><th></th><th align="center"></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td align="center">AI Parsing Skills - <br>Coming Soon</td><td></td><td><a href="broken-reference">Broken link</a></td></tr><tr><td></td><td align="center">Parsing Templates</td><td></td><td><a href="broken-reference">Broken link</a></td></tr><tr><td></td><td align="center">Merge Dynamics</td><td></td><td><a href="broken-reference">Broken link</a></td></tr></tbody></table>
