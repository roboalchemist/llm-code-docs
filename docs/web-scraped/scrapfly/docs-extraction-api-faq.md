# Source: https://scrapfly.io/docs/extraction-api/faq

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/extraction-api/faq

Markdown Content:
FAQ
---

Here are some of the most common issues and questions that come up when using Scrapfly Extraction API. See the tag filter on the right for more.

#Basics

The Extraction API is a powerful tool that extracts structured data from any text content including HTML, Markdown, and plain text. It uses AI models, LLMs, and custom parsing instructions to convert unstructured content into structured formats like JSON.

The API supports three extraction methods:

*   [extraction_model](https://scrapfly.io/docs/extraction-api/automatic-ai) - Automatic extraction using predefined AI models for common data types (products, articles, reviews, etc.)
*   [extraction_prompt](https://scrapfly.io/docs/extraction-api/llm-prompt) - LLM-powered extraction using custom prompts
*   [extraction_template](https://scrapfly.io/docs/extraction-api/rules-and-template) - Template-based extraction using JSON schemas and CSS/XPath selectors

[How do I use the Extraction API?](https://scrapfly.io/docs/extraction-api/faq#how-to-use)
------------------------------------------------------------------------------------------

#Basics

Make a `POST` request to `https://api.scrapfly.io/extraction` with:

*   Your API key as the `key` parameter
*   The content to extract from in the request body
*   One extraction method: `extraction_model`, `extraction_prompt`, or `extraction_template`

See the [Getting Started guide](https://scrapfly.io/docs/extraction-api/getting-started) for detailed examples.

#Basics

Yes! The [Web Scraping API](https://scrapfly.io/docs/scrape-api/extraction) directly integrates extraction capabilities. You can add `extraction_model`, `extraction_prompt`, or `extraction_template` parameters to your scraping requests to get extracted data in a single API call.

This is the recommended approach when you need both scraping and extraction.

[What extraction models are available?](https://scrapfly.io/docs/extraction-api/faq#available-models)
-----------------------------------------------------------------------------------------------------

#Models

Scrapfly supports automatic extraction models for common web data types:

*   **E-commerce:** product, product_listing
*   **Content:** article, review_list, social_media_post
*   **Real Estate:** real_estate_property, real_estate_property_listing
*   **Jobs:** job_posting, job_listing
*   **Travel:** hotel, hotel_listing, event
*   **Other:** organization, software, stock, vehicle_ad, food_recipe, search_engine_results

See the [complete model list](https://scrapfly.io/docs/extraction-api/automatic-ai#models) for details on each model's schema.

[How accurate are the automatic extraction models?](https://scrapfly.io/docs/extraction-api/faq#model-accuracy)
---------------------------------------------------------------------------------------------------------------

#Models

Automatic extraction models use advanced AI to identify and extract data patterns. Accuracy depends on:

*   How well the page structure matches common patterns for that data type
*   The quality and structure of the source HTML
*   Whether the page uses semantic HTML markup (schema.org, microdata, etc.)

For best results on non-standard pages, consider using [extraction_prompt](https://scrapfly.io/docs/extraction-api/llm-prompt) or [extraction_template](https://scrapfly.io/docs/extraction-api/rules-and-template) for more control.

#LLM

LLM prompt extraction uses AI language models to understand your natural language instructions and extract data accordingly. Simply provide a prompt describing what data you want to extract, and the AI will interpret the content and return structured results.

Example: `extraction_prompt=Extract all product names, prices, and ratings in JSON format`

See the [LLM Prompt documentation](https://scrapfly.io/docs/extraction-api/llm-prompt) for more examples and best practices.

[What are best practices for writing extraction prompts?](https://scrapfly.io/docs/extraction-api/faq#prompt-tips)
------------------------------------------------------------------------------------------------------------------

#LLM

For effective LLM prompt extraction:

*   Be specific about what data fields you want
*   Specify the output format (JSON, CSV, etc.)
*   Include examples of the expected structure when possible
*   Mention data types and formatting requirements
*   Keep prompts concise but descriptive

Example: `"Extract product information as JSON with fields: name (string), price (number), availability (boolean)"`

#Template

Use [extraction_template](https://scrapfly.io/docs/extraction-api/rules-and-template) when:

*   You need precise control over data extraction
*   You're scraping the same website structure repeatedly
*   You want deterministic, rule-based extraction
*   You need to extract data from specific HTML elements using CSS or XPath selectors
*   Cost efficiency is important (template extraction is cheaper than LLM-based methods)

[What content types can I extract from?](https://scrapfly.io/docs/extraction-api/faq#content-types)
---------------------------------------------------------------------------------------------------

#Content

The Extraction API supports:

*   **HTML** - Web pages and HTML documents
*   **Markdown** - Markdown formatted text
*   **Plain Text** - Raw text content
*   **JSON** - JSON data (for transformation/restructuring)

Specify the content type using the [content-type](https://scrapfly.io/docs/extraction-api/getting-started#content-type) header (e.g., `text/html`, `text/markdown`).

[Can I send compressed content?](https://scrapfly.io/docs/extraction-api/faq#compress-content)
----------------------------------------------------------------------------------------------

#Content

Yes! To reduce bandwidth and improve performance, you can send gzip-compressed content by:

*   Compressing your content with gzip
*   Setting the `Content-Encoding: gzip` header
*   Sending the compressed data in the request body

This is especially useful for large HTML documents.

#Billing

Extraction API costs vary by method:

*   **Template extraction:** Most cost-effective, charged per extraction
*   **Automatic models:** Moderate cost, charged per extraction
*   **LLM prompts:** Higher cost due to AI processing, charged based on content size and complexity

See the [Billing page](https://scrapfly.io/docs/extraction-api/billing) for detailed pricing information. You can also check extraction costs in the API response headers (`X-Scrapfly-Api-Cost`).

[How do I check extraction costs?](https://scrapfly.io/docs/extraction-api/faq#check-cost)
------------------------------------------------------------------------------------------

#Billing

Extraction costs are available in:

*   **API Response:** Check the `X-Scrapfly-Api-Cost` response header
*   **Response Body:** Look at the `context.cost` field in the JSON response
*   **Dashboard:** View detailed cost breakdown in the [Monitoring dashboard](https://scrapfly.io/dashboard/monitoring)

[What does HTTP status code 400 mean?](https://scrapfly.io/docs/extraction-api/faq#status-400)
----------------------------------------------------------------------------------------------

#Errors#Debugging

Status 400 indicates a malformed request. Common causes:

*   Missing required parameters (`key`, extraction method)
*   Invalid extraction template JSON syntax
*   Incorrect content-type header
*   Invalid parameter values

Check the error message in the response body for specific details. See the [Errors page](https://scrapfly.io/docs/extraction-api/errors) for all error codes.

[What does HTTP status code 401 mean?](https://scrapfly.io/docs/extraction-api/faq#status-401)
----------------------------------------------------------------------------------------------

#Errors#Debugging

Status 401 indicates authentication failure. Make sure you:

*   Include the `key` parameter with your valid API key
*   Have an active Scrapfly subscription
*   Are using the correct API endpoint

[Why are my extraction results empty?](https://scrapfly.io/docs/extraction-api/faq#empty-results)
-------------------------------------------------------------------------------------------------

#Errors#Debugging

Empty or incomplete results can occur when:

*   **Template extraction:** CSS/XPath selectors don't match the content structure. Verify selectors using browser dev tools.
*   **Automatic models:** Content doesn't match expected patterns. Try a different model or use LLM prompt extraction.
*   **LLM prompts:** Prompt is too vague or content is ambiguous. Make your prompt more specific.
*   **Content issue:** The source content is dynamically loaded via JavaScript (use [Web Scraping API](https://scrapfly.io/docs/scrape-api/extraction) with `render_js=true`)

#Performance

To improve extraction performance:

*   Use [extraction_template](https://scrapfly.io/docs/extraction-api/rules-and-template) for fastest processing (rule-based, no AI)
*   Send compressed content using gzip to reduce transfer time
*   Minimize content size by pre-filtering unnecessary HTML
*   Use specific extraction models instead of generic LLM prompts when possible
*   Consider caching results if extracting from the same content repeatedly

[Does Extraction API support webhooks?](https://scrapfly.io/docs/extraction-api/faq#webhook-support)
----------------------------------------------------------------------------------------------------

#Features#Integration

Yes! You can use the `webhook` parameter to receive extraction results asynchronously. This is useful for long-running extractions or integrating with other systems.

See the [Webhook documentation](https://scrapfly.io/docs/extraction-api/webhook) for details on setup and payload format.

[What is the maximum content size for extraction?](https://scrapfly.io/docs/extraction-api/faq#content-size-limit)
------------------------------------------------------------------------------------------------------------------

#Features

Content size limits vary by extraction method:

*   **Template extraction:** Up to 10MB of HTML content
*   **Automatic models:** Up to 5MB of HTML content
*   **LLM prompts:** Up to 1MB of content (due to LLM token limits)

For larger content, consider splitting it into chunks or pre-processing to extract relevant sections.

[What is the URL parameter used for?](https://scrapfly.io/docs/extraction-api/faq#url-parameter)
------------------------------------------------------------------------------------------------

#Features

The [url](https://scrapfly.io/docs/extraction-api/getting-started#api_param_url) parameter is optional and provides context to the extraction engine. It helps:

*   Resolve relative URLs in the content to absolute URLs
*   Provide additional context for AI models
*   Track extraction source in monitoring dashboards

While optional, including the URL parameter is recommended for better results.

[Which extraction method should I use?](https://scrapfly.io/docs/extraction-api/faq#which-method)
-------------------------------------------------------------------------------------------------

Choose based on your needs:

*   **Template extraction:** You know the exact structure, need fastest performance, want lowest cost
*   **Automatic models:** Extracting common data types (products, articles), want balance of ease and accuracy
*   **LLM prompts:** Need flexibility, extracting unique/complex data, willing to pay more for AI-powered extraction

You can also combine methods: use templates for structured parts and LLM prompts for unstructured content.

[Do SDKs support the Extraction API?](https://scrapfly.io/docs/extraction-api/faq#sdk-support)
----------------------------------------------------------------------------------------------

#Integration

Yes! Both Python and TypeScript SDKs fully support the Extraction API with convenient methods for all three extraction types. The SDKs handle request formatting, authentication, and response parsing automatically.

See the [Scrape API Getting Started](https://scrapfly.io/docs/scrape-api/getting-started) guide for SDK installation and usage examples.

[What format do extraction results use?](https://scrapfly.io/docs/extraction-api/faq#output-format)
---------------------------------------------------------------------------------------------------

All extraction methods return results as JSON by default. The structure varies:

*   **Template extraction:** Matches your template schema exactly
*   **Automatic models:** Uses predefined schemas specific to each model (see model documentation)
*   **LLM prompts:** Structure depends on your prompt instructions

Results are available in the `result.extracted_data.data` field of the API response.

#Debugging

Test your extraction configurations using:

*   **Web Player:** Try extraction in the Scrapfly dashboard player (if using combined scraping + extraction)
*   **Test websites:** Use [web-scraping.dev](https://web-scraping.dev/) for practice
*   **Small batches:** Start with a few examples before scaling
*   **Monitoring:** Check extraction logs in the [dashboard](https://scrapfly.io/dashboard/monitoring)
