# Linkup Documentation

Source: https://docs.linkup.so/llms-full.txt

---

# Adding Images
Source: https://docs.linkup.so/pages/changelog/addingimages

_Released: January 07, 2025_

We're excited to introduce the ability to include images in your search results. This new feature allows you to retrieve relevant images alongside your regular search data.

### How to Enable

To include images in your search results, simply add `includeImages=true` to your API request.

**Example Request**

```shell curl theme={null}
curl --request POST \
  --url https://api.linkup.so/v1/search \
  --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
  --header 'Content-Type: application/json' \
  --data '{
  "q": "Who is Barack Obama?",
  "depth": "standard",
  "outputType": "searchResults",
  "includeImages": "true"
}'
```

**Example Response**

```json json theme={null}
{
  "results": [
    {
      "type": "image",
      "name": "Barack Obama | Biography, Presidency, & Facts | Britannica.com",
      "url": "https://cdn.britannica.com/43/172743-138-545C299D/overview-Barack-Obama.jpg"
    },
    {
      "type": "text",
      "name": "Barack Obama Biography",
      "url": "https://www.biography.com/political-figures/barack-obama",
      "content": "Barack Obama was the 44th president of the United States and the first Black commander-in-chief. He served two terms, from 2009 until 2017."
    }
  ]
}
```


# Dates Filtering
Source: https://docs.linkup.so/pages/changelog/datefiltering

_Released: March 19, 2024_

We're excited to introduce date filtering capabilities for your search results. This new feature allows you to narrow down your search results to specific time periods, making it easier to find the most relevant and up-to-date information.

### How to Enable

To filter your search results by date, add the `fromDate` and `toDate` parameters to your API request. You can specify either a start date, end date, or both.

**Example Request**

```shell curl theme={null}
curl --request POST \
  --url https://api.linkup.so/v1/search \
  --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
  --header 'Content-Type: application/json' \
  --data '{
  "q": "Latest developments in AI",
  "depth": "standard",
  "outputType": "searchResults",
  "fromDate": "2024-01-01",
  "toDate": "2024-03-19"
}'
```

**Example Response**

```json theme={null}
{
  "results": [
    {
      "type": "text",
      "name": "Recent AI Developments",
      "url": "https://example.com/ai-news",
      "content": "Latest breakthroughs in artificial intelligence...",
      "date": "2024-03-15"
    }
  ]
}
```

The date filtering parameters accept dates in ISO 8601 format (YYYY-MM-DD). You can use either:

* `fromDate`: Filter results from this date onwards
* `toDate`: Filter results up to this date
* Both `fromDate` and `toDate`: Filter results within this date range


# Fetch Endpoint
Source: https://docs.linkup.so/pages/changelog/fetch-endpoint

_Released: September 12, 2025_

We're excited to introduce the new **`/fetch`** endpoint, which allows you to retrieve the raw HTML or markdown content of any webpage with optional JavaScript rendering capabilities.

### How to Use

The `/fetch` endpoint accepts a URL and returns the webpage content in your preferred format. You can choose whether to render JavaScript or retrieve the static HTML.

**Example Request**

```shell curl theme={null}
curl --request POST \
  --url https://api.linkup.so/v1/fetch \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://example.com/page",
  "outputFormat": "html",
  "renderJS": false
}'
```

**Example Response**

```json json theme={null}
{
  "url": "https://example.com/page",
  "content": "<html><head><title>Example Page</title></head><body><h1>Example Domain</h1><p>This domain is for use in illustrative examples in documents...</p></body></html>",
  "outputFormat": "html",
  "timestamp": "2025-09-12T10:30:00Z"
}
```

### Key Features

* **Flexible Content Retrieval**: Get webpage content as raw HTML or clean markdown
* **JavaScript Rendering**: Optional JavaScript execution for dynamic content
* **Direct URL Access**: Fetch content from any publicly accessible webpage
* **Clean Output**: Structured response with metadata and content

This endpoint is perfect for content extraction, web scraping, and building applications that need to process webpage data programmatically.


# maxResults parameter
Source: https://docs.linkup.so/pages/changelog/max-results

_Released: November 14, 2025_

We're excited to introduce the new `maxResults` parameter for the `/search` endpoint, which allows you to specify the maximum number of search results returned in a single API call. This feature is designed to give you more control on the size of the context passed to downstream LLMs.

### How to Use

To specify a maximum number of search results, add the `maxResults` parameter to your API request.

**Example Request**

<CodeGroup>
  ```shell curl theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "Latest developments in AI",
    "depth": "standard",
    "outputType": "sourcedAnswer",
    "maxResults": 10
  }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """Latest developments in AI"""

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer",
    max_results=10,
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `Latest developments in AI`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer",
    maxResults: 10
  }).then(console.log);
  ```
</CodeGroup>


# URL Filtering
Source: https://docs.linkup.so/pages/changelog/urlfiltering

_Released: jun 20, 2025_

We're excited to introduce URL filtering capabilities for your search results. This new feature allows you to exclude or obligate some URLs on your search results, making it easier to find the most relevant information.

### How to Enable

To filter your search results by URLs or domains, add the `excludeDomains` or `includeDomains` parameters to your API request.

**Example Request with excludeDomains**

<CodeGroup>
  ```shell curl theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "Latest developments in AI",
    "depth": "standard",
    "outputType": "sourcedAnswer",
    "excludeDomains": ["apple.com"]
  }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """Latest developments in AI"""

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer",
    exclude_domains=["apple.com"]
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `Latest developments in AI`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer",
    excludeDomains: ["apple.com"]
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json theme={null}
{
  "answer": "AI agents are the dominant innovation in 2025, focusing on autonomous AI programs that can independently complete projects...",
  "sources": [
    {
      "name": "AI Agents in 2025: Expectations vs. Reality | IBM",
      "snippet": "For 2025, the dominant innovation narrative is the AI agent...",
      "url": "https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality"
    }
  ]
}
```

**Example Request with includeDomains**

<CodeGroup>
  ```shell curl theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "How to build MCP server",
    "depth": "standard",
    "outputType": "sourcedAnswer",
    "includeDomains": ["dev.to"]
  }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """How to build MCP server?"""

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer",
    include_domains=["dev.to"]
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `How to build MCP server?`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer",
    includeDomains: ["dev.to"]
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json theme={null}
{
  "answer": "Steps to build an MCP server in 2025:[...]",
  "sources": [
    {
      "name": "🚀Top 10 MCP Servers for 2025 (Yes, GitHub’s Included!) - DEV Community",
      "snippet": "Enter the Model Context Protocol ... ",
      "url": "https://dev.to/fallon_jimmy/top-10-mcp-servers-for-2025-yes-githubs-included-15jg"
    }
  ]
}
```

The URLs filtering parameters accept an Array of strings. You can use:

* `excludeDomains`: Don't use those Domains/URLs in the results
* `includeDomains`: Only use those Domains/URLs in the results

<Warning>
  If you use `excludeDomains` and `includeDomains`, the results will logically only include Domains/URLs that match the inclusion.
</Warning>


# /credits/balance
Source: https://docs.linkup.so/pages/documentation/api-reference/endpoint/get-balance

https://api.linkup.so/v1/openapi.json get /v1/credits/balance
The `/credits/balance` endpoint allows you to retrieve your current credits balance.

The **`/credits/balance`** endpoint allows you to check your current credit balance.

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>


# /fetch
Source: https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-fetch

https://api.linkup.so/v1/openapi.json post /v1/fetch
The `/fetch` endpoint allows you to fetch a single webpage from a given URL.

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

The **`/fetch`** endpoint retrieves a markdown representation of a webpage at the given URL, with the ability to render the Javascript or not.


# /search
Source: https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-search

https://api.linkup.so/v1/openapi.json post /v1/search
The `/search` endpoint allows you to retrieve web content.

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

The **`/search`** endpoint is a context retrieval tool for Web content. For a natural language query, it finds online information to ground your LLM's answer, along with sources.

<Tip>Our search is optimized for precision. Make sure to craft detailed prompts for optimal results. Learn more [here](../../../documentation/get-started/prompting).</Tip>

Depending on the `depth` parameter, results may be faster (`standard`) or slower but more complete (`deep`).

If `outputType` is set to `structured`, you may provide a JSON `structuredOutputSchema` to dictate the response format.

<Tip>JSON formats are tricky. Learn more about structured output in [our guide](../../../documentation/tutorials/structured-output-guide).</Tip>

Learn more about these parameters in [Concepts](/pages/documentation/get-started/concepts).


# Authentication
Source: https://docs.linkup.so/pages/documentation/development/authentication

Authenticate with the Linkup API

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

## Using cURL

Your API key needs to be sent along all your request as a Bearer token in the `Authorization` header.

```shell curl theme={null}
curl "https://api.linkup.so/v1/search" \
    -G \
    -H "Authorization: Bearer <YOUR_LINKUP_API_KEY>" \
    ...
```

## Using the Python SDK

**Option 1:** Set a `LINKUP_API_KEY` environment variable in your shell before using the SDK.

```shell shell theme={null}
export LINKUP_API_KEY='<YOUR_LINKUP_API_KEY>'
```

**Option 2:**  Set the `LINKUP_API_KEY` environment variable directly within Python, using for instance `os.environ` or [python-dotenv](https://github.com/theskumar/python-dotenv).

```python python theme={null}
import os
from linkup import LinkupClient

os.environ["LINKUP_API_KEY"] = "<YOUR_LINKUP_API_KEY>"
# or dotenv.load_dotenv()
client = LinkupClient()
...
```

**Option 3**: Directly pass the Linkup API key to the Linkup Client.

```python python theme={null}
from linkup import LinkupClient

client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")
...
```

## Using the JS SDK

Pass the Linkup API key to the Linkup Client.

```js js theme={null}
import { LinkupClient } from 'linkup-sdk';

const client = new LinkupClient({
  apiKey: '<YOUR_LINKUP_API_KEY>',
});
```

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Errors
Source: https://docs.linkup.so/pages/documentation/development/errors

Linkup API errors and how to handle them

This guide includes an overview of error codes you might see from both the API and our SDKs.

## API Errors

Whatever the HTTP error code is, the response payload will contain the following object:

**`statusCode`**: number - HTTP error code.

**`error`**: object - Linkup error details containing:

* **`code`**: string - Error name
* **`message`**: string - Description of the error
* **`details`**: array - Details of the error. This array may be empty or include objects with the following properties:
  * **`field`**: string - The field that caused the error
  * **`message`**: string - A description of the field error

Here is an example:

```json theme={null}
{
	"statusCode": 400,
	"error": {
		"code": "VALIDATION_ERROR",
		"message": "Validation failed",
		"details": [
			{
				"field": "outputType",
				"message": "outputType must be one of the following values: sourcedAnswer, searchResults, structured"
			}
		]
	}
}
```

**API Error Codes**

| Code                        | Possible Reasons                                                                                                                                                                                     |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400 - Bad Request           | <ul><li>Required parameter is missing</li><li>Invalid parameter</li><li>Search query yields no result</li><li>Fetch request targets a web page > 20MB</li><li>Fetch request targets a file</li></ul> |
| 401 - Unauthorized          | API Key is missing or invalid                                                                                                                                                                        |
| 403 - Forbidden             | API key does not have permission to access this resource                                                                                                                                             |
| 409 - Conflict              | Resource conflict (e.g., duplicate entry or conflicting request)                                                                                                                                     |
| 429 - Too Many Requests     | You have run out of credit or you are sending too many concurrent requests                                                                                                                           |
| 500 - Internal Server Error | Something's up on our end                                                                                                                                                                            |

## SDK Errors

**Python & JS SDK Error Types**

| Type                               | Reason                                                                             |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| `LinkupInvalidRequestError`        | Required parameter is missing, or invalid parameter                                |
| `LinkupNoResultError`              | Search query yield no result                                                       |
| `LinkupAuthenticationError`        | API Key is missing, invalid or you do not have permission to access this ressource |
| `LinkupInsufficientCreditError`    | You have run out of credit                                                         |
| `LinkupTooManyRequestsError`       | You are sending too many concurrent requests                                       |
| `LinkupFetchError`                 | The provided URL might not be found or can't be fetched                            |
| `LinkupFetchResponseTooLargeError` | The provided URL's response is too large to be processed (>20MB)                   |
| `LinkupFetchUrlIsFileError`        | The provided URL points to a file and not a web page                               |
| `LinkupUnknownError`               | Anything else                                                                      |


# Source Filtering
Source: https://docs.linkup.so/pages/documentation/development/filtering

How to filter your search on sources.

<Info>
  **Date filtering** information can be found [here](../api-reference/endpoint/post-search#body-from-date).
</Info>

## Overview

You can fine-tune your search results by:

* **including**
* **excluding**
* **prioritizing**

specific domains or URLs, ensuring more control over where your answers are retrieved from.

<Warning>
  If you use `excludeDomains` and `includeDomains`, the results will logically only include URLs that match the inclusion.
</Warning>

### Exclude Domains/URLs

To filter your search results by exclusively excluding some URLs or domains, you can add the `excludeDomains` parameter to your API request. Currently, the parameter supports up to 50 URLs to exclude.

**Example Request with excludeDomains**

<CodeGroup>
  ```shell curl theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "Latest developments in AI",
    "depth": "standard",
    "outputType": "sourcedAnswer",
    "excludeDomains": ["apple.com"]
  }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """Latest developments in AI"""

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer",
    exclude_domains=["apple.com"]
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `Latest developments in AI`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer",
    excludeDomains: ["apple.com"]
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json theme={null}
{
  "answer": "AI agents are the dominant innovation in 2025, focusing on autonomous AI programs that can independently complete projects...",
  "sources": [
    {
      "name": "AI Agents in 2025: Expectations vs. Reality | IBM",
      "snippet": "For 2025, the dominant innovation narrative is the AI agent...",
      "url": "https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality"
    }
  ]
}
```

### Include Domains/URLs

To filter your search results by exclusively consulting some URLs or domains, you can add the `includeDomains` parameter to your API request. Currently, the parameter supports up to 50 URLs to include.

**Example Request with includeDomains**

<CodeGroup>
  ```shell curl theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "How to build MCP server",
    "depth": "standard",
    "outputType": "sourcedAnswer",
    "includeDomains": ["dev.to"]
  }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """How to build MCP server?"""

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer",
    include_domains=["dev.to"]
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `How to build MCP server?`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer",
    includeDomains: ["dev.to"]
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json theme={null}
{
  "answer": "Steps to build an MCP server in 2025:[...]",
  "sources": [
    {
      "name": "🚀Top 10 MCP Servers for 2025 (Yes, GitHub’s Included!) - DEV Community",
      "snippet": "Enter the Model Context Protocol ... ",
      "url": "https://dev.to/fallon_jimmy/top-10-mcp-servers-for-2025-yes-githubs-included-15jg"
    }
  ]
}
```

### Prioritize Domains

To **Prioritize** some domains, you can use the `<guidance>` XML structure in your query.

**Example Request with Prioritize**

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST 'https://api.linkup.so/v1/search' \
    -H 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    -H 'Content-Type: application/json' \
    -d '{
      "q": "<guidance>Use only the sources listed here. Do not rely on any external references.\n  - wikipedia.org\n  - lvmh.com\n<priority>\n  - wikipedia.org\n</priority></guidance>Who is the CEO of LVMH?",
      "outputType": "sourcedAnswer",
      "depth": "standard"
    }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """
  <guidance>
  Use only the sources listed here. Do not rely on any external references.
      - wikipedia.org
      - lvmh.com
    <priority>
      - wikipedia.org
    </priority>
  </guidance>
  Who is the CEO of LVMH?
  """

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer"
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `
  <guidance>
      Use only the sources listed here. Do not rely on any external references.
      - wikipedia.org
      - lvmh.com
    <priority>
      - wikipedia.org
    </priority>
  </guidance>
  Who is the CEO of LVMH?`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer"
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json theme={null}
{
  "answer": "The CEO of LVMH is Bernard Arnault.",
  "sources": [
    {
      "name": "Actual CEO of LVMH",
      "url": "https://www.wikipedia.org/wiki/lvmh",
      "snippet": "LVMH Moët Hennessy Louis Vuitton SE, commonly known as LVMH, is a French multinational luxury goods conglomerate. The current CEO is Bernard Arnault."
    },
    {
      "name": "The CEO of LVMH is Bernard Arnault",
      "url": "https://lvmh.com/about-us",
      "snippet": "Bernard Arnault is the CEO of LVMH, a leading luxury goods company. Under his leadership, LVMH has seen significant growth and expansion in the luxury market."
    }
  ]
}
```


# Pricing
Source: https://docs.linkup.so/pages/documentation/development/pricing

How the Linkup API pricing system works

## Billing

When you first sign up, your account is automatically credited with 5 euros. We will top up your credits back to 5 euros each month. You can add money to your account in the [Billing](https://app.linkup.so/organization/billing) section of the Linkup app.

<Tip>If you top up your account with 1,000 euros or more, we will add free credits to your account</Tip>

| Top up amount | Extra credits |
| ------------- | ------------- |
| >€1,000       | 10%           |
| >€5,000       | 15%           |
| >€10,000      | 20%           |

Please reach out to [support@linkup.so](mailto:support@linkup.so) for custom needs.

Each time you make a successful request to our API endpoints, an amount is subtracted from your account. The amount deducted per call depends on the endpoint and parameters:

## Search Endpoint

For the `/search` endpoint, the cost depends on the depth parameter:

| Call Type | Cost   |
| --------- | ------ |
| Standard  | €0.005 |
| Deep      | €0.05  |

## Fetch Endpoint

For the `/fetch` endpoint, the cost depends on the renderJS parameter:

| Call Type                    | Cost   |
| ---------------------------- | ------ |
| Without JS (renderJS: false) | €0.001 |
| With JS (renderJS: true)     | €0.005 |

If your account runs out, the API will respond with a 429 HTTP error.

<Check>
  **Important note**: No credit is subtracted when an error occurs, whether it is because of a missing parameter, an internal server error, but also when we were not able to find anything relevant to your query.
</Check>

You can view your current consumption by visiting the [Linkup App](https://app.linkup.so/consumer/dashboard).


# Rate Limits
Source: https://docs.linkup.so/pages/documentation/development/rate-limits



For our `/search` and `/fetch` endpoints, our rate limits are currently set at `10 queries per second` per organization. If you need higher rate limits, please reach out to [contact@linkup.so](mailto:contact@linkup.so) to discuss Custom plans.


# Concepts
Source: https://docs.linkup.so/pages/documentation/get-started/concepts

Key concepts to understand how Linkup works

## Overview

The Linkup `/search` endpoint allows you to discover and access relevant web content based on a natural language query. Once the content is retrieved, it can serve as factual grounding for Large Language Models (LLMs), AI agents, and automated retrieval systems, helping them produce more accurate and informed responses.

## Agentic search

Linkup does not return keyword-matched links.

Instead, it performs **agentic search**: the system interprets your query, executes one or more retrieval steps, and returns grounded outputs designed to be consumed directly by AI systems.

Depending on your instructions and selected search depth, Linkup may:

* run one or several web searches
* open and scrape webpages
* reuse information discovered in earlier steps
* refine or expand queries until the requested data is found

You can be explicit in the way you prompt the system to perform a search (eg "first, find the official website of the AI company linkup, then scrape the page and return the full content").

## Parameters

### Query

Your query should be as specific as possible to improve the quality of the results. Consider providing additional context or constraints. For example:

| Initial Query                                   | Improved Query                                             | Explanation                                                                                                |
| ----------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| What is the website of the company named Total? | What is the website of the **French** company named Total? | Adding the country ("French") helps narrow down results, making it easier to identify the correct company. |

### Depth

You can choose between two search depths, depending on your performance and accuracy needs:

**`standard`**:

**Behavior**

* Executes **a single iteration of retrieval**
* Does not reuse outputs from one iteration in another (e.g. an extracted URL cannot be reused in a follow-up step)
* Optimizes for latency by minimizing retrieval operations
* May split a query into sub-searches **if**:
  * explicitly instructed to do so, or
  * required to answer the query correctly

**Best suited for**

* low latency optimization
* simple or direct questions
* high-volume or low-latency use cases
* queries where the answer is likely found quickly

Costs €0.005 per call.

**`deep`**:

**Behavior**

* Can executes **up to 10 iterations of retrieval** (will iterate until the context sufficiently answers the data requested in the query)
* Each iteration is aware of the context produced by previous iterations
* If required information is missing, additional iterations may be launched with refined or adjacent queries
* Supports **sequential instructions**, where outputs from one step are used in the next (e.g. search first, then scrape a discovered URL)

**Best suited for**

* complex or multi-step queries
* cases where information is not reliably found in a single pass
* prompts that explicitly require several searches or sequential actions

Costs €0.05 per call.

**Rule of thumb**

* One Google search → `standard`
* Multiple tabs → `deep`

### OutputType

The API supports several output formats to match different use cases:

* **`sourcedAnswer`**: Returns a natural language answer with source attributions.
* **`searchResults`**: Provides chunks of contextual data suitable for grounding in LLM prompts.
* **`structured`**: Produces a response following a specified JSON schema, ideal for structured data extraction.

<Tip>
  JSON formats are tricky. Learn more about structured output in [our
  guide](../../../pages/documentation/tutorials/structured-output-guide).
</Tip>

### Additional Parameters

* **`includeImages`**: Boolean parameter to include relevant images in search results
* **`fromDate`**: Filter results from a specific date (format: YYYY-MM-DD)
* **`toDate`**: Filter results until a specific date (format: YYYY-MM-DD)
* **`includeDomains`**: Filter results to only include specific domains (up to 50 URLs)
* **`excludeDomains`**: Filter results to exclude specific domains (up to 50 URLs)
* **`maxResults`**: Limit the maximum number of search results to a specific number

## Rate Limits

Both /search and /fetch endpoints have a rate limit of 10 queries per second per account. If you need higher rate limits, please contact us at [contact@linkup.so](mailto:contact@linkup.so) to discuss custom plans.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>

## Best Practices

1. **Query Specificity**

   * Be as specific as possible in your queries
   * Include relevant context (time periods, locations, industries)
   * Use natural language but be precise
   * Read our [prompting guide](../tutorials/prompting) to know more.

2. **Depth Selection**

   * Use `standard` for quick, general queries
   * Use `deep` for complex research or when accuracy is critical
   * Consider cost implications (€0.005 vs €0.05 per call)

3. **Output Format**

   * Choose `sourcedAnswer` for direct answers with citations
   * Use `searchResults` for LLM grounding
   * Select `structured` when you need specific data points returned in a json format. Read our [structured output](../tutorials/structured-output-guide) guide to know more.

4. **Error Handling**
   * The API returns standard HTTP status codes
   * No credit is deducted for failed requests
   * Common errors include:
     * 400: Bad Request (missing/invalid parameters)
     * 401: Unauthorized (invalid API key)
     * 429: Too Many Requests (rate limit or insufficient credit)

<Info>
  Your account starts with 5 euros of credit and is topped up monthly. You can
  add more credit in the [Billing](https://app.linkup.so/organization/billing)
  section of the Linkup app.
</Info>


# Introduction
Source: https://docs.linkup.so/pages/documentation/get-started/introduction

Get started for free, no credit card required.

Linkup is a web search engine for AI apps. We connect your AI application to the internet. Our API provides grounding data to enrich your AI's output and increase its precision, accuracy and factuality. Linkup is [#1 in the world for factuality](https://www.linkup.so/blog/linkup-establishes-sota-performance-on-simpleqa), scoring state-of-the-art results on OpenAI's SimpleQA benchmark.

<Tip>**Important**: the more precise and detailed your prompts, the better the results. Read more about Prompting [here](../tutorials/prompting) or test our Prompt Optimizer [here](https://prompt.linkup.so) </Tip>

<CardGroup>
  <Card title="Quickstart" icon="forward" href="/pages/documentation/get-started/quickstart">
    Integrate with Linkup in 5 minutes
  </Card>

  <Card title="Playground" icon="play" href="https://app.linkup.so/playground">
    Test Linkup Search in 1 click
  </Card>

  <Card title="API Reference" icon="code" href="/pages/documentation/api-reference">
    Review the Linkup API reference
  </Card>

  <Card title="Explore our tutorials" icon="books" href="../tutorials/signup-radar">
    Start building based on tutorials
  </Card>
</CardGroup>


# Quickstart
Source: https://docs.linkup.so/pages/documentation/get-started/quickstart

Integrate with Linkup in 5 minutes

The Linkup API can be used in AI workflows to find and access high quality content from the internet. You can follow the steps below to integrate Linkup easily.

1. Get your API key for free

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

2. Install the Linkup SDK

<CodeGroup>
  ```python python theme={null}
  pip install linkup-sdk
  ```

  ```js js theme={null}
  npm i linkup-sdk
  ```
</CodeGroup>

3. Call the Search API to retrieve context. This enables you to RAG the internet. Linkup will return the context you need to ground your LLM's answer.

<CodeGroup>
  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")

  response = client.search(
      query="What is Microsoft's 2024 revenue?",
      depth="deep",
      output_type="sourcedAnswer"
  )

  print(response)
  ```

  ```js js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '<YOUR API KEY>',
  });

  const askLinkup = async () => {
    return await client.search({
      query: "What is Microsoft's 2024 revenue?",
      depth: 'deep',
      outputType: 'sourcedAnswer',
    });
  };

  askLinkup().then(console.log);
  ```

  ```shell curl theme={null}
  curl "https://api.linkup.so/v1/search" \
      -G \
      -H "Authorization: Bearer $LINKUP_API_KEY" \
      --data-urlencode "q=What is Microsoft's 2024 revenue?" \
      --data-urlencode "depth=deep" \
      --data-urlencode "outputType=sourcedAnswer"
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```json 200 [expandable] theme={null}
  {
      "answer": "Microsoft's revenue for fiscal year 2024 was $245.1 billion, reflecting a 16% increase from the previous year.",
      "sources": [
          {
              "name": "Microsoft 2024 Annual Report",
              "url": "https://www.microsoft.com/investor/reports/ar24/index.html",
              "snippet": "Highlights from fiscal year 2024 compared with fiscal year 2023 included: Microsoft Cloud revenue increased 23% to $137.4 billion.\nMore broadly, we continued to see sustained revenue growth from migrations as customers turn to Azure. Azure Arc is helping customers streamline their transition, as they secure, develop, and operate workloads with Azure services anywhere. We have 36,000 Arc customers, up 90 percent year-over-year.\nWith our acquisition of Activision Blizzard King, which closed October 2023, we’ve added hundreds of millions of players to our ecosystem. We now have 20 franchises that have generated over $1 billion in lifetime revenue—from Candy Crush, Diablo, and Halo, to Warcraft, Elder Scrolls, and Gears of War.\nGrowth depends on our ability to reach new users in new markets such as frontline workers, small and medium businesses, and growth markets, as well as add value to our core product and service offerings to span AI and productivity categories such as communication, collaboration, analytics, security, and compliance. Office Commercial revenue is mainly affected by a combination of continued installed base growth and average revenue per user expansion, as well as the continued shift from Office licensed on-premises to Office 365.\nGrowth depends on our ability to reach new users, add value to our core product set with new features including AI tools, and continue to expand our product and service offerings into new markets. Office Consumer revenue is mainly affected by the percentage of customers that buy Office with their new devices and the continued shift from Office licensed on-premises to Microsoft 365 Consumer subscriptions.",
              "favicon": "https://www.microsoft.com/favicon.ico"
          },
          {
              "name": "Microsoft's Financial Results in FY24 Q4 – AGOLUTION",
              "url": "https://agolution.com/en/microsoft/financial-reporting/2024-q4/",
              "snippet": "What did the other quarterly figures look like and how did Microsoft fare in fiscal year 2024 as a whole? Microsoft’s revenue amounted to $64.7 billion - and increased by 15%.\nWhat did the other quarterly figures look like and how did Microsoft fare in fiscal year 2024 as a whole? Microsoft’s revenue amounted to $64.7 billion - and increased by 15%.\nThe Xbox and Gaming segment recorded a remarkable jump in revenue of 61%, with the majority of this increase being due to the acquisition of Activision Blizzard King by Microsoft at the end of last year. Since then, Microsoft has owned popular video games such as “Call of Duty”, “Overwatch” and “Candy Crush”. The results for Microsoft’s fiscal year 2024 as compared to fiscal year 2023 were as follows.\nMicrosoft achieved total revenue of $245.1 billion, an increase of 16%. The operating income amounted to $109.4 billion and increased by 24%. Total net income amounted to $88.1 billion and increased by 22%. Earnings per share amounted to $11.8 - here too there was an increase of 22%. Solid fiscal year 2024: Microsoft remains one of the market leaders in the era of AI.\nThe third quarter of Microsoft’s 2024 fiscal year was again characterized by strong cloud results.",
              "favicon": "https://agolution.com/favicon.ico"
          },
          {
              "name": "Microsoft Revenue 2010-2024 | MSFT | MacroTrends",
              "url": "https://www.macrotrends.net/stocks/charts/MSFT/microsoft/revenue",
              "snippet": "Microsoft revenue for the quarter ending December 31, 2024 was $69.632B, a 12.27% increase year-over-year.\nMicrosoft annual/quarterly revenue history and growth rate from 2010 to 2024. Revenue can be defined as the amount of money a company receives from its customers in exchange for the sales of goods or services. Revenue is the top line item on an income statement from which all costs and expenses are subtracted to arrive at net income.\nMicrosoft revenue for the quarter ending December 31, 2024 was $69.632B, a 12.27% increase year-over-year.\nMicrosoft annual revenue for 2023 was $211.915B, a 6.88% increase from 2022. Microsoft annual revenue for 2022 was $198.27B, a 17.96% increase from 2021.",
              "favicon": "https://www.macrotrends.net/favicon.ico"
          },
          ...
      ]
  }
  ```
</CodeGroup>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>

<Card title="Best Practice" icon="link" href="https://docs.linkup.so/pages/documentation/tutorials/prompting">
  The more precise and detailed your prompts, the better the results.
</Card>


# Instructions for AI Agents
Source: https://docs.linkup.so/pages/documentation/tutorials/agent-instructions

Context for your AI agents to use linkup effectively — covers MCP, SDKs, skills, and agent design patterns

Give your AI agents access to accurate, real-time web data. This guide covers how to integrate Linkup into any agent environment — from MCP-based setups to custom-built pipelines — and how to configure your agent to use Linkup effectively.

You can give this page as context to your agent. We also publish a [**Linkup Skill**](/pages/documentation/tutorials/linkup-skill) — a reusable knowledge module that agents can install and reference automatically for better Linkup API usage.

<Card title="Install the Linkup Skill" icon="graduation-cap" href="/pages/documentation/tutorials/linkup-skill">
  One command: `npx skills add LinkupPlatform/skills` — works with Claude Code, Cursor, Windsurf, and more.
</Card>

***

## 1. System Prompt Snippet

Copy this into your agent's system prompt, tool description, or `CLAUDE.md` file. It teaches any LLM how to use Linkup well.

```text theme={null}
## Linkup Web Search — Usage Instructions

You have access to Linkup, a web search and content extraction API. Follow these rules:

### Before Writing a Query
Reason through three questions in order:
1. INPUTS: What do I already have? A URL? A company name? A topic?
   - If I have a URL → scrape it directly, don't search for it.
2. DATA LOCATION: Where does the data I need live?
   - In search snippets (facts, dates, names, short claims) → search is enough.
   - On full web pages (tables, specs, detailed content) → need to scrape.
   - Not sure → default to standard.
3. SEQUENCING: Do I need to chain steps?
   - Parallel searches only → standard.
   - Find URL then scrape it, or scrape then search again → deep.
   - Scrape multiple URLs → deep.

### Search Depth
- depth="standard" (€0.005): multiple parallel searches + scrape one provided URL. Cannot scrape multiple URLs. Cannot chain search → scrape.
- depth="deep" (€0.05): up to 10 iterative steps. Can scrape multiple URLs. Can chain search → scrape. Can run new searches based on extracted information.
- When uncertain, default to standard.

### Query Style
- Simple factual lookups → short keyword queries.
- Complex extraction → natural language instructions: what to find, where to look, what to extract.
- Broad research → "Run several searches with adjacent keywords." Works in standard.
- Don't ask Linkup to analyze or reason. Ask it to retrieve. You do the thinking.

### Scraping Rules
- Standard: scrape one URL provided in the prompt. That's it.
- Deep: scrape multiple URLs, scrape URLs discovered during search.

### Output Type
- outputType="searchResults": raw sources for you to process (default for agents).
- outputType="sourcedAnswer": natural language answer with citations.
- outputType="structured" + JSON schema: machine-parseable data.

### Fetch
- Use /fetch instead of /search for a single known URL.
- Always set renderJs=true unless the page is static HTML.
```

> **Where to put this:** System prompt, `CLAUDE.md`, `.cursorrules`, MCP tool descriptions, or framework tool docstrings. It works everywhere.

***

## 2. Query Construction — Examples

Your query should tell Linkup **what to retrieve**, not what to think. The system prompt snippet above teaches the 3-step reasoning (inputs → data location → sequencing). Here's how it plays out:

```
Task: Get a company's pricing
Reasoning: no URL → need to find it → then scrape → sequential → deep
→ query: "Find the pricing page for {company}. Scrape it. Extract plan names, prices, and features."
```

```
Task: Get a company's latest funding round
Reasoning: no URL → answer lives in snippets → no chaining → standard
→ query: "Find {company}'s latest funding round amount and date"
```

```
Task: Extract data from a known URL
Reasoning: have URL → just scrape → no chaining → standard or /fetch
→ query: "Scrape https://example.com/pricing. Extract plan names, prices, and included features."
```

```
Task: Build an ICP from a company's web presence
Reasoning: no URL → need full pages → find then scrape multiple → deep
→ query: "Find and scrape {company}'s homepage, use case pages, and 2-3 recent blog posts. Extract: industries mentioned, company sizes referenced, job titles targeted, and pain points addressed."
```

For more query examples and patterns, see the [Prompting Guide](/pages/documentation/get-started/prompting).

***

## 3. Output Types

For most agent use cases, use `searchResults`.

| Output Type     | Returns                         | Best For                                          |
| --------------- | ------------------------------- | ------------------------------------------------- |
| `searchResults` | Array of `{name, url, content}` | Agent-side reasoning, RAG, multi-source synthesis |
| `sourcedAnswer` | Answer + source citations       | User-facing chatbots, Q\&A                        |
| `structured`    | JSON matching your schema       | CRM updates, data pipelines, enrichment           |

For details on structured output schemas, see [API Reference](/pages/documentation/api-reference/endpoint/post-search).

***

## 4. `/fetch` Endpoint

Use `/fetch` instead of `/search` when your agent already has the exact URL. It's faster, cheaper, and returns clean markdown.

Always set `renderJs: true` (most sites need it).

[Full fetch documentation →](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-fetch)

***

## 5. Integration by Environment

* **MCP:** [Linkup MCP Server](https://docs.linkup.so/pages/integrations/mcp/mcp)
* **VS Code:** [MCP Configuration Examples](https://docs.linkup.so/pages/integrations/mcp/mcp#configuration-examples)
* **Claude Desktop:** [Linkup + Claude](https://docs.linkup.so/pages/integrations/linkup-claude)
* **Smithery CLI:** [Quick Start](https://docs.linkup.so/pages/integrations/mcp/mcp#quick-start-with-smithery)
* **Python SDK:** [Python](https://docs.linkup.so/pages/sdk/python/python)
* **LangChain:** [LangChain Integration](https://docs.linkup.so/pages/integrations/langchain)
* **CrewAI:** [CrewAI Integration](https://docs.linkup.so/pages/integrations/crewai)
* **Node.js:** [TypeScript / JavaScript SDK](https://docs.linkup.so/pages/sdk/js/js)
* **No-Code / Low-Code:** [Integrations](https://docs.linkup.so/pages/integrations/integrations)
* **cURL / HTTP:** [Quickstart](https://docs.linkup.so/pages/documentation/get-started/quickstart)

***

## To Go Further

* [Prompting Guide](/pages/documentation/get-started/prompting) — Detailed best practices
* [Prompt Optimizer](https://prompt.linkup.so) — Optimize prompts interactively
* [Prompt Templates](https://prompt.linkup.so/templates) — Ready-to-use templates
* [API Reference](/pages/documentation/api-reference/endpoint/post-search) — Full endpoint docs
* [MCP Server (GitHub)](https://github.com/LinkupPlatform/linkup-mcp-server) — Source and setup
* [Integrations](/pages/integrations/integrations) — n8n, Make, Zapier, and more

Need help? Reach out at [support@linkup.so](mailto:support@linkup.so), on [Discord](https://discord.com/invite/9q9mCYJa86), or [book a 15-minute call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9).


# Automating Lead Qualification
Source: https://docs.linkup.so/pages/documentation/tutorials/company-data-enrichment

Learn how to automatically research and score your leads using Linkup AI to prioritize high-value prospects

<Note>
  **Time-saving Automation:** This tutorial shows you how to build a system that
  can process hundreds of leads automatically, saving 5+ hours of manual
  research per week while ensuring you focus on the right opportunities.
</Note>

# The Challenge: From Manual Research to Automated Intelligence

Every day, new users sign up for Linkup. When they do, we capture two crucial pieces of information:

* Their company name
* Their email address

When we had a few signups every day, our team could spend time researching each company manually and identify the most important ones. But as we grow and the number of daily signups becomes too high to handle manually, we face a challenge: **How do we know which leads to focus on first?**

**Before automation:** Our sales team spent hours manually researching each company, often missing high-value opportunities because of the volume.

**After automation:** We instantly identify and prioritize the most promising leads based on AI-powered analysis of their company profile and website.

## The Solution: An Automated Enrichment Pipeline to Qualify Leads

By the end of this tutorial, you'll have a working system that:

1. **Finds Official Websites:** Cross-references company names with email domains
2. **Analyzes Company Websites:** Determines how well each company fits your ideal customer profile
3. **Prioritizes Leads:** Assigns a score from 1-5 so your team knows who to contact first

For this tutorial, we are going to use:

* **Attio CRM data pull:** to generate the input .json file with org names and company domains.
* **Linkup API:** to search the web and enrich the leads.

## The Complete Process: Visual Overview

Here's how the data transforms throughout this process:

```mermaid theme={null}
graph LR
    A[User Signup] -->|Extract| B[Name + Email Domain]
    B -->|Linkup API Lookup| C[Verified Website]
    C -->|Linkup API Analysis| D[ICP Score]

    style A fill:#f9d4d4
    style D fill:#c9f7c9
```

## Project Setup: Getting Started

Let's start with our project structure and requirements:

```bash theme={null}
your-project-directory/
├── .env                                 # API keys
├── organization_names_with_domains.json # Input file
├── company_analysis_results.json        # Output file
└── linkup_enrich.py                     # Enrichment script
```

<Steps>
  <Step title="Create Your Environment">
    First, let's set up our environment and install the required packages:

    ```bash theme={null}
    # Create a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    #### Install required packages
    pip install requests python-dotenv
    ```
  </Step>

  <Step title="Set Up Your API Keys">
    Create a `.env` file in your project directory with your API keys:

    ```env theme={null}
    LINKUP_API_KEY=your_api_key_here
    ATTIO_API_KEY=your_attio_api_key_here
    ```

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    <Note type="warning">
      Never put your API KEYS directly in your code. Always include them in a `.env`
      file.
    </Note>
  </Step>

  <Step title="Add your input file">
    Our starting point is a JSON file containing user signup information:

    * Organizations
    * Email address (or rather: the domains of the email addresses)

    In our case, we extracted this file from our CRM (Attio) since this is where we send signup data (and want to send the enriched data back after the process). This file could be the output of a signup form or any lead generation document you're using.

    Let's look at the structure:

    ```json theme={null}
    "034Q2K4NXVY6JIWZ": {
        "name": "test",
        "people_ids": "01HQ2K4NX123457",
        "domain": "anthropic.com"
    },
    "01HQ2K4NXVY6GPWZ": {
        "name": "Personal",
        "people_ids": "01HQ2K4NX123456",
        "domain": "live.fr"
    },
    "CHDY2K4NXVY6GJUE": {
        "name": "MistralAI",
        "people_ids": "01HQ2K4NX120987",
        "domain": "gmail.com"
    },
    ```

    <Note>
      As you can see, data quality might not be optimal:

      * Some users provide personal email addresses
      * Others do not put the name of their company

      This is why we're combining both information to try and get better results.

      We could add a Linkup search for LinkedIn profiles associated with the first part of the emails.
    </Note>
  </Step>
</Steps>

## The Enrichment Pipeline: Step-by-Step Implementation

Before we share the whole script (see the end of the tutorial), let's break down our enrichment pipeline into steps:

<Steps>
  <Step title="Finding Official Websites">
    Our first challenge is to reliably find the official website for each company. We'll use Linkup's API with a carefully crafted prompt:

    ```python {8-13} theme={null}
    url = "https://api.linkup.so/v1/search"
    headers = {
        "Authorization": f"Bearer {LINKUP_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
      "q": f"Based on the name {company_name} and the email domain {domain_info}, " +
          f"find the most likely company website URL. Only return a result if you are 90% sure " +
          f"this is the correct website. If {company_name} seems like a generic company name " +
          f"(e.g. personal, perso, n/a), return nothing. If the domain is a generic domain " +
          f"(e.g. gmail.com, yahoo.com, hotmail.com, icloud.com), do not consider it. " +
          f"Only consider professional email domains. Only return the company domain URL.",
      "depth": "standard",
      "outputType": "sourcedAnswer",
      "includeImages": "false"
    }
    ```

    <Tip>
      **Understanding key parameters**:

      * **depth: "standard"**: For website finding,
        "standard" depth provides a good balance between speed and accuracy
      * **outputType: "sourcedAnswer"**: Returns a natural language answer with just
        the URL
      * **includeImages: "false"**: We don't need images, which speeds up
        the response
    </Tip>

    <Accordion title="Prompt Design Strategy">
      Notice how the prompt includes specific instructions:

      * Only return results with 90% confidence
      * Ignore generic company names
      * Skip generic email domains
      * Focus on professional email domains
        These constraints help ensure we get high-quality, reliable results.
    </Accordion>
  </Step>

  <Step title="Analyzing Company Fit">
    Once we have the website, we need to determine how well each company fits our ideal customer profile. For this, we're using a second prompt to Linkup that gives the domain URL as input and asks for an ICP score as output.

    ```python {7-13} theme={null}
    url = "https://api.linkup.so/v1/search"
    headers = {
      "Authorization": f"Bearer {LINKUP_API_KEY}",
      "Content-Type": "application/json"
    }
    payload = {
      "q": f"Analyze the website {website_url}. Determine if this company could be an Ideal Customer Profile (ICP) " +
            f"for my company https://www.linkup.so/. For context, we are selling a search API. We target AI companies, " +
            f"Tech Companies, and corporates, as well as consulting and financial firms. " +
            f"Our search API allows companies to enrich applications with real-time web knowledge and business intelligence, " +
            f"at scale. Consider factors like industry and whether they're likely to need API services, and if they " +
            f"might be building software products. Return a rating from 1 to 5, 1 being lowest ICP, 5 being highest ICP. " +
            f"Universities and schools should get a 3. Only return the rating, nothing else.",
      "depth": "deep",
      "outputType": "sourcedAnswer",
      "includeImages": "false"
    }
    ```

    <Tip>
      **We use 'deep' depth** for ICP analysis because:

      * It provides more thorough analysis of the company website
      * It considers more pages and context when making its assessment
      * The accuracy of ICP scoring is worth the slightly longer processing time
    </Tip>

    **The output will be an ICP (Ideal Customer Profile) score ranging from 1-5:**

    * **1** - Perfect match - AI companies, Tech Companies with clear API needs
    * **2** - Strong potential - Corporates, Financial Firms, Consulting companies
    * **3** - Moderate fit - Universities, Educational Institutions, Research Organizations
    * **4** - Might need education - Companies with potential but unclear use cases
    * **5** - Probably not a good fit - Consumer businesses, local services, etc.

    Notice how we don't have to explicitly explain our rating system - AIs understand it intuitively.
  </Step>

  <Step title="Checking the results">
    After we run the script with these two API calls, a new file will be created with two new fields for each company:

    * Website domain
    * ICP Analysis

    ```json {5-6,12-13,19-20} theme={null}
    "034Q2K4NXVY6JIWZ": {
      "name": "test",
      "people_ids": "01HQ2K4NX123457",
      "domain": "anthropic.com"
      "website": "https://www.anthropic.com/"
      "icp_analysis": "5"
    },
    "01HQ2K4NXVY6GPWZ": {
      "name": "Personal",
      "people_ids": "01HQ2K4NX123456",
      "domain": "live.fr"
      "website": ""
      "icp_analysis": "1"
    },
    "CHDY2K4NXVY6GJUE": {
      "name": "MistralAI",
      "people_ids": "01HQ2K4NX120987",
      "domain": "gmail.com"
      "website": "https://mistral.ai/"
      "icp_analysis": "5"
    }
    ```

    Great! As you can see, combining company name and email domain allows us to identify ICPs we would have missed if we had only considered one of the two factors.

    <Note>
      The complete script below includes additional functionality beyond the two
      Linkup API calls shown above. For example:

      * We implement logic to skip the ICP analysis call when no website is found, automatically assigning a rating of "1" (as seen in the second example output)
      * We include an incremental processing system that only analyzes companies without existing ratings, preventing redundant API calls and allowing you to resume processing after interruptions
      * The code handles file operations safely, maintains a processing counter, and includes appropriate rate limiting between API calls
    </Note>
  </Step>
</Steps>

## Next Steps and Customization Opportunities

This script is just the beginning! Here are ways you can extend it:

1. **Additional Enrichment**: Add other API calls to find additional information (company industry, value chain positioning, pricing strategy...)
2. **CRM Integration**: Add code to push results back to your CRM automatically (what we're doing at Linkup)
3. **Multi-threaded Processing**: Speed up processing by handling multiple companies simultaneously

In our case, we're actually sending the data back to our CRM so that new signups get automatically rated. We then have live alerts that tell us when important customers sign up to our products.

## The Complete Code

Below is the complete Python script that implements our lead qualification system. The file is more complex than the two functions to allow for observability, troubleshooting, batch processing, etc. Do not hesitate to reach out if you have any questions.

```python [expandable] theme={null}
import os
import json
import time
import re
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# API keys from environment variables
ATTIO_API_KEY = os.getenv('ATTIO_API_KEY')
LINKUP_API_KEY = os.getenv('LINKUP_API_KEY')

if not ATTIO_API_KEY or not LINKUP_API_KEY:
    print("Error: Missing API keys in .env file")
    exit(1)

# File paths and settings
FILE = 'new_companies.json'
MAX_COMPANIES = 50

def load_existing_data():
    """Load file with new companies to enrich"""
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Could not load {FILE}")
        exit(1)

def find_website_url(company_name, company_domain=None):
    if not company_name or not company_name.strip():
        return ""

    url = "https://api.linkup.so/v1/search"
    headers = {
        "Authorization": f"Bearer {LINKUP_API_KEY}",
        "Content-Type": "application/json"
    }

    domain_info = company_domain if company_domain else ""
    payload = {
        "q": f"Based on the name {company_name} and the email domain {domain_info}, find the most likely company website URL. Only return a result if you are 90% sure this is the correct website. If {company_name} seems like a generic company name (e.g. personal, perso, n/a), return nothing. If the domain is a generic domain (e.g. gmail.com, yahoo.com, hotmail.com, icloud.com), do not consider it. Only consider professional email domains. Only return the company domain URL.",
        "depth": "standard",
        "outputType": "sourcedAnswer",
        "includeImages": "false"
    }

    print(f"Sending API request to Linkup for: {company_name}")
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"API response status: {response.status_code}")
        response.raise_for_status()

        result = response.json()
        if 'answer' in result:
            url_text = result['answer']
            url_pattern = re.compile(r'https?://\S+')
            url_match = url_pattern.search(url_text)

            if url_match:
                website_url = url_match.group(0)
                return re.sub(r'[.,;:"\')]\s*$', '', website_url)
        return ""

    except Exception as e:
        print(f"Error in API call: {e}")
        return ""

def analyze_icp_fit(company_name, website_url):
    if not website_url:
        return "1"

    url = "https://api.linkup.so/v1/search"
    headers = {
        "Authorization": f"Bearer {LINKUP_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "q": f"Analyze the website {website_url}. Determine if this company could be an Ideal Customer Profile (ICP) for my company https://www.linkup.so/. For context, we are selling a search API. We target AI companies, Tech Companies, and corporates, as well as consulting and financial firms. Our search API allows companies to enrich applications with real-time web knowledge and business intelligence, at scale. Consider factors like industry and whether they're likely to need API services, and if they might be building software products. Return a rating from 1 to 5, 1 being lowest ICP, 5 being highest ICP. Universities and schools should get a 3.  Only return the rating, nothing else.",
        "depth": "deep",
        "outputType": "sourcedAnswer",
        "includeImages": "false"
    }

    print(f"Sending ICP analysis request to Linkup for: {company_name}")
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"ICP API response status: {response.status_code}")
        response.raise_for_status()

        result = response.json()
        if 'answer' in result:
            return result['answer']
        return "1"

    except Exception as e:
        print(f"Error in ICP API call: {e}")
        return "1"

def save_results(results):
    print(f"\nSaving results to {FILE}...")
    try:
        # First try to save to a temporary file
        temp_file = f"{FILE}.tmp"
        with open(temp_file, 'w') as f:
            json.dump(results, f, indent=2)

        # If successful, rename the temp file to the actual file
        if os.path.exists(FILE):
            os.replace(temp_file, FILE)
        else:
            os.rename(temp_file, FILE)

        print(f"Successfully saved {len(results)} results")

        # Verify the save
        with open(FILE, 'r') as f:
            saved_data = json.load(f)
            print(f"Verified save: {len(saved_data)} results in file")

    except Exception as e:
        print(f"Error saving results: {e}")
        # Try to clean up temp file if it exists
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except:
                pass

def main():
    results = load_existing_data()
    print(f"\nLoaded {len(results)} existing results")

    # Find organizations to process
    to_process = {record_id: (results[record_id]["name"], results[record_id].get("domain"))
                  for record_id in results
                  if not results[record_id].get("website") and
                     results[record_id].get("name") and
                     (not results[record_id].get("icp_analysis") or results[record_id].get("icp_analysis") == "")}

    companies_to_process = dict(list(to_process.items())[:MAX_COMPANIES])

    print(f"\nFound {len(to_process)} organizations to process")
    print(f"Will process {len(companies_to_process)} organizations...")

    processed_count = 0
    websites_found = 0

    for record_id, (org_name, org_domain) in companies_to_process.items():
        print(f"\nProcessing: {org_name}")

        company_result = results[record_id]
        website_url = find_website_url(org_name, org_domain)

        if website_url:
            company_result["website"] = website_url
            websites_found += 1
            print(f"Found: {website_url}")

            time.sleep(2)
            icp_analysis = analyze_icp_fit(org_name, website_url)
            company_result["icp_analysis"] = icp_analysis
            print(f"Updated {org_name} with website: {website_url} and ICP: {icp_analysis}")
        else:
            # Set default ICP analysis to "1" when no website is found
            company_result["icp_analysis"] = "1"
            print(f"Updated {org_name} with default ICP: 1")

        results[record_id] = company_result
        processed_count += 1

        # Save after each company
        save_results(results)
        print(f"Saved results after processing {org_name}")

        if processed_count < len(companies_to_process):
            time.sleep(3)

    websites_with_analysis = sum(1 for r in results.values() if r.get("website") and r.get("icp_analysis"))

    print(f"\nFinal Results:")
    print(f"Processed {processed_count} organizations")
    print(f"Found {websites_found} websites")
    print(f"Total organizations with websites: {sum(1 for r in results.values() if r.get('website'))}")
    print(f"Total organizations with analysis: {websites_with_analysis}")

    # Final save with verification
    save_results(results)

if __name__ == "__main__":
    main()
```

# Try It Yourself

<AccordionGroup>
  <Accordion title="Customize Your ICP Definition">
    Try modifying the ICP analysis prompt to match your specific business needs:

    1. Update the description of your company
    2. List your target industries
    3. Define what makes an ideal customer for you
    4. Run the script and see how the results change
  </Accordion>

  <Accordion title="Add Company Size Estimation">
    Extend the script to also estimate company size:

    1. Create a new function similar to `analyze_icp_fit`
    2. Craft a prompt asking Linkup to estimate employee count
    3. Add this data to your results structure
    4. Use it as an additional factor in prioritization
  </Accordion>
</AccordionGroup>

# Conclusion

You've now built an automated system that transforms basic CRM information into actionable intelligence. By leveraging the Linkup API, you can:

1. **Save Time**: Eliminate manual research
2. **Improve Targeting**: Focus on the most promising leads
3. **Scale Your Process**: Handle hundreds of leads with ease

This approach combines the best of both worlds: AI-powered analysis with your business expertise to define what makes an ideal customer.

For more sophisticated implementations, check out our other tutorials or reach out to our support team!

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Company Descriptions Generator
Source: https://docs.linkup.so/pages/documentation/tutorials/company-descriptions

Building a tool to generate rich company descriptions using Linkup API

This tutorial will show you how to build a company description generator that takes a company name and country as input and returns comprehensive information about the company using the Linkup API's structured output feature.

## What We're Building

Our company description generator will:

* Take a company name and country as input
* Use Linkup API to search for information about the company
* Return structured data about the company (description, industry, size, location, etc.)

## Building the Generator

<Steps>
  <Step title="Define the Schema">
    Before we start coding, let's define the schema that specifies what information we want to extract about companies. This schema will be used throughout our implementation:

    <CodeGroup>
      ```python python [expandable] theme={null}
      COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      }
      ```

      ```javascript js [expandable] theme={null}
      const COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      };
      ```
    </CodeGroup>

    This schema defines all the fields we want to extract about a company. The required fields are `name`, `description`, and `industry`, while the rest are optional but provide valuable additional information.
  </Step>

  <Step title="Install the SDK">
    Next, let's install the Linkup SDK in your preferred language:

    <CodeGroup>
      ```python python theme={null}
      pip install linkup-sdk
      ```

      ```javascript js theme={null}
      npm i linkup-sdk
      ```
    </CodeGroup>
  </Step>

  <Step title="Set Up the Client">
    Initialize the Linkup client with your API key:

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")
      ```

      ```javascript js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: '<YOUR_LINKUP_API_KEY>',
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Create the Query Generator">
    Create a function to generate the search query:

    <CodeGroup>
      ```python python theme={null}
      def generate_query(company_name: str, country: str) -> str:
          query = (
                  f"Find detailed information about {company_name} in {country}. "
                  "Include their main products/services, industry focus, company size, "
                  "and any notable achievements or recent news. Also find their "
                  "LinkedIn company page if available."
              )
          return query
      ```

      ```typescript js theme={null}
      function generateQuery(companyName: string, country: string) {
          let query;

          query = (
                  `Find detailed information about ${companyName} in ${country}. ` +
                  "Include their main products/services, industry focus, company size, " +
                  "and any notable achievements or recent news. Also find their " +
                  "LinkedIn company page if available."
              );

          return query;
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Complete Implementation">
    Here's the complete implementation that puts everything together:

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient
      import json
      from typing import Dict, Any
      from pprint import pprint

      # Schema definition (from Step 1)
      COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      }

      # Initialize the client
      client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")

      # Query generator (from Step 4)
      def generate_query(company_name: str, country: str) -> str:
          query = (
                  f"Find detailed information about {company_name} in {country}. "
                  "Include their main products/services, industry focus, company size, "
                  "and any notable achievements or recent news. Also find their "
                  "LinkedIn company page if available."
              )
          return query

      def generate_company_description(company_name: str, country: str) -> Dict[str, Any]:
          """
          Generate a structured description of a company using its name, country.

          Args:
              company_name: Name of the company
              country: Country where the company operates

          Returns:
              Dictionary containing structured company information
          """
          try:
              # Clean input
              company_name = company_name.strip()
              country = country.strip()

              # Generate search query using the function from Step 4
              query = generate_query(company_name, country)

              # Call Linkup API
              response = client.search(
                  query=query,
                  depth="deep",  # Use deep for more thorough results
                  output_type="structured",
                  structured_output_schema=json.dumps(COMPANY_SCHEMA)
              )

              return response

          except Exception as e:
              return {
                  "error": str(e),
                  "company_name": company_name,
                  "country": country
              }

      # Example usage
      if __name__ == "__main__":
          # Example companies
          companies = [
              ("Anthropic", "United States"),
              ("Stripe", "United States"),
              ("OpenAI", "United States")
          ]

          for company_name, country in companies:
              print(f"\nLooking up: {company_name} in {country}")
              result = generate_company_description(company_name, country)
              pprint(result)
      ```

      ```typescript js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      // Schema definition (from Step 1)
      const COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      };

      // Initialize the client
      const client = new LinkupClient({
          apiKey: '<YOUR_LINKUP_API_KEY>',
      });

      // Query generator (from Step 4)
      function generateQuery(companyName: string, country: string) {
          let query;
          query = (
                  `Find detailed information about ${companyName} in ${country}. ` +
                  "Include their main products/services, industry focus, company size, " +
                  "and any notable achievements or recent news. Also find their " +
                  "LinkedIn company page if available."
              );
          return query;
      }

      async function generateCompanyDescription(companyName: string, country: string) {
          try {
              // Clean input
              companyName = companyName.trim();
              country = country.trim();

              // Generate search query using the function from Step 4
              const query = generateQuery(companyName, country);

              // Call Linkup API
              const response = await client.search({
                  query: query,
                  depth: "deep",  // Use deep for more thorough results
                  outputType: "structured",
                  structuredOutputSchema: COMPANY_SCHEMA
              });

              return response;

          } catch (error: any) {
              return {
                  error: error.message,
                  companyName: companyName,
                  country: country
              };
          }
      }

      // Example usage
      async function main() {
          // Example companies
          const companies = [
              ["Anthropic", "United States"],
              ["Stripe", "United States"],
              ["OpenAI", "United States"]
          ];

          for await (const [companyName, country] of companies) {
              console.log(`\nLooking up: ${companyName} in ${country}`);
              const result = await generateCompanyDescription(companyName, country);
              console.log(JSON.stringify(result, null, 2));
          }
      }

      main().catch(console.error);
      ```
    </CodeGroup>
  </Step>
</Steps>

## How It Works

The company description generator works in three main steps:

1. **Input Processing**: The tool takes a company name and country as input and cleans them.
2. **Query Generation**: It creates a search query that includes both the company name and country to improve search accuracy.
3. **Structured Output**: Uses Linkup's structured output feature with a comprehensive schema to ensure consistent, well-formatted results.

## Possible Enhancements

For a production version, consider adding:

* Add as much information you have about companies in the queries, to limit ambiguity about which company you are searching for.
* Implement rate limiting and error handling for API usage.
* Batch processing to search for multiple companies in parallel if you are enriching a dataset for example.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Company Intelligence Engine
Source: https://docs.linkup.so/pages/documentation/tutorials/company-intelligence/company-intelligence

Build a real-time company research system using the Linkup API.

In this tutorial, you'll learn how to build a real-time company intelligence system that automatically gathers and structures information about any company. This system is perfect for sales teams, market researchers, and anyone needing up-to-date company information.

## Prerequisites

Before starting, ensure you have:

* Python 3.7 or newer installed
* Basic familiarity with Python programming
* A Linkup API key (required for making requests)

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

## Project Setup

Let's start by creating a new project and installing the necessary dependencies:

```shell shell theme={null}
# Create a new project directory
mkdir company-intel
cd company-intel

# Install required packages
pip install linkup-sdk pydantic fastapi uvicorn
```

## Implementation Guide

### 1. Define Your Data Structure

First, we'll create a data model that specifies exactly what company information we want to collect. Create a new file called `schema.py`:

```python python theme={null}
from pydantic import BaseModel
from typing import List, Optional

class CompanyInfo(BaseModel):
    # Basic company information
    name: str = ""              # Company name
    website: str = ""           # Official website URL
    description: str = ""       # Brief company description

    # Detailed information
    latest_funding: str = ""    # Most recent funding information
    recent_news: List[str] = [] # Latest company news
    leadership_team: List[str] = [] # Key executives and leaders
    tech_stack: List[str] = []  # Technologies used by the company
```

This schema ensures our data is consistently structured and validated.

### 2. Build the Intelligence Engine

Next, create `company_intel.py` to handle the core functionality:

```python python theme={null}
from linkup import LinkupClient
from schema import CompanyInfo

class CompanyIntelligence:
    def __init__(self, api_key: str):
        """Initialize the intelligence engine with your API key."""
        self.client = LinkupClient(api_key=api_key)

    def research_company(self, company_name: str) -> CompanyInfo:
        """
        Gather comprehensive information about a company.

        Args:
            company_name (str): Name of the company to research

        Returns:
            CompanyInfo: Structured company information
        """
        query = f"""
        Research {company_name} and provide:
        - Company name, website, and brief description
        - Most recent funding round or financial announcement
        - Current leadership team members
        - Technologies and tools they use
        - Recent news from the last 3 months

        Focus on current, verified information.
        """

        # Make the API request with structured output
        response = self.client.search(
            query=query,
            depth="deep",           # Get comprehensive results
            output_type="structured",
            structured_output_schema=CompanyInfo
        )

        return response
```

### 3. Create the API Layer

Now let's make our intelligence engine accessible via HTTP. Create `api.py`:

```python python theme={null}
from fastapi import FastAPI, HTTPException
from company_intel import CompanyIntelligence

# Initialize FastAPI with metadata
app = FastAPI(
    title="Company Intelligence API",
    description="Real-time company research and intelligence",
    version="1.0.0"
)

# Create intelligence engine instance
intel = CompanyIntelligence(api_key="your-linkup-api-key")

@app.get("/company/{name}", tags=["Company Research"])
async def get_company_info(name: str):
    """
    Retrieve detailed information about a company.

    Parameters:
        name (str): Company name to research

    Returns:
        CompanyInfo: Structured company information
    """
    try:
        return intel.research_company(name)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error researching company: {str(e)}"
        )
```

## Using the System

### Basic Usage Example

At first, let's use the intelligence engine directly in Python. We will create a new file called `main.py` and add the following code to it:

```python python theme={null}
from company_intel import CompanyIntelligence

# Initialize the intelligence engine
intel = CompanyIntelligence(api_key="your-api-key")

# Research a company
company = intel.research_company("Vercel")

# Access the information
print(f"Company: {company.name}")
print(f"Website: {company.website}")
print(f"Description: {company.description}")
print(f"Latest Funding: {company.latest_funding}")
print(f"Recent News: {', '.join(company.recent_news)}")
print(f"Leadership Team: {', '.join(company.leadership_team)}")
print(f"Technologies: {', '.join(company.tech_stack)}")
```

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

You can run the code by executing the following command:

```shell shell theme={null}
python main.py
```

### Running the API Server

Let's now try our API server.

```shell shell theme={null}
# Start the server with auto-reload enabled
uvicorn api:app --reload
```

You can now access the API at `http://localhost:8000/docs`.

#### Step 1

Click on the endpoint `GET /company/{name}`, and click on the `Try it out` button.

<img alt="Step 1" />

#### Step 2

<img alt="Step 2" />

Now, enter the company name, for example `Vercel`, and click on the `Execute` button.

#### Step 3

<img alt="Step 3" />

#### Step 4

You should see the response in JSON format.

<img alt="Step 4" />

## Response Examples

### Successful Response

A typical successful request to `/company/Vercel` returns:

```json theme={null}
{
    "name": "Vercel",
    "website": "https://vercel.com",
    "description": "Vercel is a cloud platform for static sites and Serverless Functions that fits perfectly with your workflow. It enables developers to host websites and web services that deploy instantly and scale automatically.",
    "latest_funding": "Series D - $150M (December 2023)",
    "recent_news": [
        "Vercel announces Edge Functions improvements with streaming support",
        "New Next.js 14 release brings major performance improvements",
        "Vercel launches new Enterprise Security features"
    ],
    "leadership_team": [
        "Guillermo Rauch - CEO",
        "Malte Ubl - CTO"
    ],
    "tech_stack": [
        "Next.js",
        "React",
        "Node.js",
        "TypeScript",
        "PostgreSQL",
        "Redis",
        "AWS"
    ]
}
```

### Error Responses

The API returns appropriate error responses in these situations:

#### Company Not Found

```json theme={null}
{
    "status_code": 404,
    "detail": "Unable to find information for the specified company",
    "timestamp": "2024-12-16T10:30:45Z"
}
```

#### Invalid API Key

```json theme={null}
{
    "status_code": 401,
    "detail": "Invalid or missing API key",
    "timestamp": "2024-12-16T10:30:45Z"
}
```

#### Rate Limit Exceeded

```json theme={null}
{
    "status_code": 429,
    "detail": "Rate limit exceeded. Please try again in 60 seconds",
    "timestamp": "2024-12-16T10:30:45Z"
}
```

## Engine Response Fields

| Field            | Type   | Description                     | Example                                       |
| ---------------- | ------ | ------------------------------- | --------------------------------------------- |
| name             | string | Company name                    | "Vercel"                                      |
| website          | string | Company website URL             | "[https://vercel.com](https://vercel.com)"    |
| description      | string | Brief company description       | "Vercel is a cloud platform..."               |
| latest\_funding  | string | Most recent funding information | "Series D - \$150M (December 2023)"           |
| recent\_news     | array  | List of recent news headlines   | \["Vercel announces...", "New Next.js 14..."] |
| leadership\_team | array  | List of key leadership members  | \["Guillermo Rauch - CEO", ...]               |
| tech\_stack      | array  | List of technologies used       | \["Next.js", "React", ...]                    |
| news\_sentiment  | float  | Optional sentiment score        | 0.8                                           |
| company\_size    | string | Optional size estimation        | "Large Enterprise"                            |

## Best Practices

For production use, consider implementing these best practices:

1. **Error Handling**
   * Implement comprehensive error handling for API calls
   * Log errors appropriately
   * Provide meaningful error messages to users

2. **Rate Limiting**
   * Implement rate limiting to avoid API quota issues
   * Consider using a queue for batch processing
   * Add retry logic for failed requests

3. **Caching**
   * Cache frequently requested company data
   * Use appropriate TTL values based on data freshness requirements
   * Implement cache invalidation strategies

4. **Data Validation**
   * Validate all input data
   * Use Pydantic's validation features
   * Implement data cleaning where necessary

## Common Applications

This system can be used for:

* Pre-sales research automation
* CRM data enrichment
* Competitor monitoring
* Market intelligence gathering
* Investment research
* Due diligence automation

## Conclusion

You now have a powerful company intelligence engine that provides:

* Real-time company information
* Structured, consistent data
* Easy API access
* Extensible architecture

Remember to:

* Keep your API key secure
* Respect API rate limits
* Implement appropriate caching for your use case
* Add error handling for production use

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Find LinkedIn Profiles
Source: https://docs.linkup.so/pages/documentation/tutorials/linkedin-profile

A practical guide to quickly locate official LinkedIn home‑page URLs for companies or people

This tutorial will show you how to build find the LinkedIn profile of a company or an individual using Linkup.

## What We'll Build

This tutorial will show you how to build find the LinkedIn profile of a company or an individual using Linkup.

* **Input**: Any text prompt that describes the profile you're after (company, school, person, etc.).
* **Process**:
  1. Send the prompt to the **Linkup API** with `depth="standard"`.
  2. Ask for **sourcedAnswer** output so we can inspect citations.
  3. Decide whether we're ≥ 99 % sure.
* **Output**: A single LinkedIn URL or `undefined`.

This pattern is perfect for enriching CRMs, onboarding forms, or internal tools where you need fast links with a very low false‑positive rate.

## How To Build

<Steps>
  <Step title="Install the SDK">
    <CodeGroup>
      ```python python theme={null}
      pip install linkup-sdk
      ```

      ```javascript js theme={null}
      npm i linkup-sdk
      ```
    </CodeGroup>
  </Step>

  <Step title="Set Up the Client">
    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")
      ```

      ```javascript js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: '<YOUR_LINKUP_API_KEY>',
      });
      ```
    </CodeGroup>

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Make the API Call">
    <CodeGroup>
      ```python python theme={null}
      # 🔎  Example
      response = client.search(
          query="Please locate the official LinkedIn page for Linkup (their website is linkup.so).\nReturn only the LinkedIn home‑page URL.\nIf you're not at least 99 % sure the link is accurate, answer with undefined.",
          depth="standard",          # fast yet accurate
          output_type="sourcedAnswer",
          include_images=False,
      )
      print(response.answer)  # either the URL or 'undefined'
      ```

      ```javascript js theme={null}
      // 🔎  Example
      const response = await client.search({
        query: `Please locate the official LinkedIn page for Linkup (their website is linkup.so).
        Return only the LinkedIn home‑page URL.
        If you're not at least 99 % sure the link is accurate, answer with undefined.`,
        depth: 'standard', // fast yet accurate
        outputType: 'sourcedAnswer',
        includeImages: false,
      });
      console.log(response.answer); // either the URL or 'undefined'
      ```
    </CodeGroup>
  </Step>

  <Step title="Craft Better Prompts">
    For best accuracy, include **at least two unique signals**:

    | ✅ Good signal         | 📝 Example                         |
    | --------------------- | ---------------------------------- |
    | Official domain       | "(their website is acme.com)"      |
    | City or region        | "based in Berlin, Germany"         |
    | Stock ticker          | "listed on NASDAQ : ACME"          |
    | Unique slogan/tagline | "company slogan 'Think tangerine'" |

    > **Tip:** Keep the "Return only the LinkedIn home‑page URL…" and the 99 % clause; it gives the model explicit, measurable instructions.
  </Step>

  <Step title="Batch Lookup">
    Need to process a list of companies? Here's a tiny batch helper:

    <CodeGroup>
      ```python python theme={null}
      companies = [
          ("Stripe", "stripe.com"),
          ("Intercom", "intercom.com"),
          ("Monzo", "monzo.com"),
      ]

      for name, domain in companies:
          q = (
              f"Locate the official LinkedIn page for {name} (their website is {domain}). "
              "Return only the LinkedIn home‑page URL. If you're not at least 99 % sure, answer with undefined."
          )
          response = client.search(
              query=q,
              depth="standard",
              output_type="sourcedAnswer",
              include_images=False,
          )
          print(name, "→", response.answer)
      ```

      ```javascript js theme={null}
      const companies = [
        ['Stripe', 'stripe.com'],
        ['Intercom', 'intercom.com'],
        ['Monzo', 'monzo.com'],
      ];

      for (const [name, domain] of companies) {
        const q = `Locate the official LinkedIn page for ${name} (their website is ${domain}). ` +
                  `Return only the LinkedIn home‑page URL. If you're not at least 99 % sure, answer with undefined.`;
        const response = await client.search({
          query: q,
          depth: 'standard',
          outputType: 'sourcedAnswer',
          includeImages: false,
        });
        console.log(name, '→', response.answer);
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Advanced Enhancements

* **Fallback to Deep Search**: Retry with `depth="deep"` when standard depth yields `undefined`.
* **Multiple Entities**: Adjust the prompt to return an *array* of URLs when searching generic terms like "Acme Inc".
* **Integrate with CRMs**: Enrich company records automatically, then store URL + confidence + timestamp.
* **Rate Limiting**: Use `asyncio` / `Promise.allSettled` with a limiter when batch‑processing thousands.

## Conclusion

With fewer than 20 lines of code you now have a **LinkedIn‑URL resolver** that's fast, accurate, and completely configurable. Plug it into sign‑up flows, prospecting pipelines, or internal dashboards—and never copy‑paste a LinkedIn link again.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Linkup Skill
Source: https://docs.linkup.so/pages/documentation/tutorials/linkup-skill

A reusable knowledge module that teaches AI agents how to use Linkup effectively

<video>
  <source type="video/mp4" />
</video>

## What is a Skill?

Skills are **knowledge for AI agents**, not tools. They are markdown-based instruction files that agents load automatically when a task matches the skill's purpose. The agent then follows the skill's guidance to make better API calls — choosing the right parameters, writing effective queries, and avoiding common mistakes.

Skills work across agent environments: Claude Code, Cursor, Windsurf, Cline, GitHub Copilot, and any platform that supports instruction files.

Skills are installed with the Skill Comand Line Interface (CLI). Read more [here](https://skills.sh/).

<Card title="Install the Linkup Skill" icon="link" href="https://github.com/LinkupPlatform/skills">
  Teach your agent how to use Linkup with our official Skill. Redirects to source code repository with SKILL.md file.
</Card>

***

## The Linkup Skill

The **linkup-search** skill teaches agents how to use the Linkup API effectively. Instead of relying on generic tool descriptions, agents get structured guidance on:

* **Query construction** — A 3-step reasoning framework: what inputs do I have? Where does the data live? Do I need to chain steps?
* **Depth selection** — When to use `standard` vs `deep`, with decision rules and worked examples
* **Output types** — Choosing between `searchResults`, `sourcedAnswer`, and `structured` based on the use case
* **Effective prompting** — Keyword-style for simple lookups, instruction-style for complex extraction
* **Scraping and fetch** — When to scrape within search vs use the `/fetch` endpoint directly
* **Advanced patterns** — LinkedIn extraction, parallel multi-query coverage, sequential search chains
* **MCP setup** — Configuration for Claude Code, VS Code, Cursor, and Claude Desktop

***

## Installation

```bash theme={null}
npx skills add LinkupPlatform/skills
```

This installs the skill into your project. Agents will automatically reference it when handling web search, content extraction, or research tasks via Linkup.

### Supported environments

| Environment                | How it works                                |
| -------------------------- | ------------------------------------------- |
| **Claude Code**            | Skill is loaded automatically when relevant |
| **Cursor**                 | Loaded via `.cursor/rules/`                 |
| **Windsurf**               | Loaded via `.windsurfrules`                 |
| **Cline / GitHub Copilot** | Loaded from project-level instruction files |

***

## How It Works

When an agent encounters a task that involves web search, company research, or content extraction:

1. The agent detects it has access to Linkup tools (via MCP or SDK)
2. The skill's instructions are loaded into the agent's context
3. The agent follows the skill's reasoning framework to decide depth, query style, and output type
4. The result: more accurate queries, fewer wasted API calls, better results

No manual invocation needed — skills activate when relevant.

***

## Example

Without the skill, an agent might write:

```
query: "Tell me about Datadog"
depth: "standard"
```

With the skill, the agent reasons through the framework and writes:

```
query: "Find Datadog's pricing page. Scrape it. Extract plan names, per-host prices, and included features for each tier."
depth: "deep"
```

The skill teaches agents to be specific about what to retrieve, where to look, and how to chain steps — the same way an experienced developer would use the API.

***

## Resources

* [GitHub Repository](https://github.com/LinkupPlatform/skills) — Source code and SKILL.md
* [Prompting Guide](/pages/documentation/tutorials/prompting) — Detailed query writing best practices
* [Agent Instructions](/pages/documentation/tutorials/agent-instructions) — System prompt snippets and integration patterns
* [MCP Setup](/pages/integrations/mcp/mcp) — Connect Linkup to your agent via MCP

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Meeting Prep
Source: https://docs.linkup.so/pages/documentation/tutorials/meeting-prep/meeting-prep

Build a meeting prep agent using Linkup inside Xpander

## Overview

Linkup integrates with [Xpander.ai](http://xpander.ai/) to give your agents access to real-time web data. This tutorial walks through how to build a meeting preparation agent that uses that data to generate useful briefings.

## Configuration Steps

<Steps>
  <Step title="Create a New Agent">
    1. Go to the Agents tab in Xpander.

    2. Click “New Agent”

    3. Name it something like “Meeting Brief Agent”

       <img alt="Create Agent" />

    4. Paste the following into the **Instructions** section:

    ```
    Your job is to help someone prepare for a sales meeting.
    They’ll give you a company name. Use Linkup to find useful, recent info about that company.
    Write a clear, short briefing with:
    - What the company does
    - Recent updates
    - Their likely challenges
    - How we might approach them
    - Notes and key questions
    ```

    <img alt="Paste Prompt" />
  </Step>

  <Step title="Add the Linkup Tool">
    1. Go to the Tools section in the agent builder

       <img alt="Go Tools" />

    2. Click “Add Tool” and select **Linkup.so**

       <img alt="Add Tool" />

    3. Choose the “Retrieve Web Content by Query” option

       <img alt="Select Action" />

    4. Under “Prompt Input Mapping”, link the user's input (e.g. company name) to the Linkup query

    **Query Tip:**

    ```
    Give me recent updates, funding info, hiring trends, product launches, and blog posts about {{company}}
    ```
  </Step>

  <Step title="Add 'Send Email' Step">
    1. Click the "+" button in the agent editor
    2. Select **Send Email** tool
    3. You don’t need to wire it to previous steps
    4. Make sure your prompt includes:

    ```
    Always email the final output to [email]
    ```

    <img alt="Send Email" />
  </Step>

  <Step title="Add 'Send Slack Message' Step">
    1. Click the "+" button again

    2. Select **Send Slack Message**

       <img alt="Send Slack" />

    3. Configure credentials with OAuth2 and log in to Slack

       <img alt="Slack Auth" />

    4. Include this in the prompt:

    ```
    Also send the meeting briefing to the configured Slack channel
    ```
  </Step>

  <Step title="Test with a Sample Prospect">
    Company: Airtable
    Name: Daniel Kim
    Title: Director of Product Strategy
    Email: [daniel.kim@airtable.com](mailto:daniel.kim@airtable.com)

    Type into chat:

    > Can you prep a briefing for Daniel Kim from Airtable?

    <img alt="Test Prompt" />
  </Step>

  <Step title="Final Look & Output">
    <img alt="Final Look" />
  </Step>
</Steps>

You are all set to use Linkup to build an intelligent meeting prep agent in Xpander. Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about how Linkup works.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Peers Finder
Source: https://docs.linkup.so/pages/documentation/tutorials/peers-finder/peers-finder

Learn how to find comparable companies using the Linkup API with Google Sheets

Struggling to identify your company's true competitors and industry peers? This comprehensive step-by-step guide shows you how to leverage the powerful Linkup API with Google Sheets to build your own automated peer comparison tool. Perfect for investors, market analysts, and business strategists who need accurate competitive intelligence without expensive enterprise solutions.

Don't walk away if you're not a developer! This tutorial is designed to be accessible for everyone - no coding experience required. Just follow our simple copy-paste instructions and clear screenshots to set up your own peer comparison tool in minutes.

## Prerequisites

Before starting, ensure you have:

* A Google account
* A Linkup API key (required for making requests)

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

## Setup Guide

### Step 1: Open Google Sheets

1. Open a new Google Sheet
2. Name it "Company Peer Finder" or any name you prefer

### Step 2: Access Apps Script

1. Click on "Extensions" in the menu bar
2. Select "Apps Script" from the dropdown menu

<img alt="Extensions Menu" />

*1: Accessing Apps Script through the Extensions menu*

### Step 3: Set Up the Script

1. In the Apps Script editor, delete any existing code
2. Copy and paste the following script:

```javascript theme={null}
// Google Apps Script for Company Peer Finder with direct Linkup integration
// This script uses Linkup API to find peer companies based on input companies

// Configuration - replace with your actual Linkup API key
const LINKUP_API_KEY = "YOUR_API_KEY"; // Replace with your Linkup API key
const LINKUP_API_URL = "https://api.linkup.so/v1"; // Linkup API base URL

// Create the menu when the spreadsheet opens
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('Peer Finder')
    .addItem('Extract Common Characteristics', 'extractCommonCharacteristics')
    .addItem('Find Peer Companies', 'findPeerCompanies')
    .addToUi();
}

// Function to extract common characteristics from input companies
function extractCommonCharacteristics() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const inputSheet = ss.getSheetByName('Input Companies');
  const charSheet = ss.getSheetByName('Characteristics');
  
  if (!inputSheet || !charSheet) {
    setupSpreadsheet();
    return;
  }

  const companies = inputSheet.getRange('A2:A6').getValues().flat().filter(Boolean);
  if (companies.length === 0) {
    SpreadsheetApp.getUi().alert('Please enter at least one company name in the Input Companies sheet.');
    return;
  }

  const characteristics = [];
  for (const company of companies) {
    const response = fetchCompanyData(company);
    if (response && response.characteristics) {
      characteristics.push(...response.characteristics);
    }
  }

  // Count frequency of each characteristic
  const charCount = {};
  characteristics.forEach(char => {
    charCount[char] = (charCount[char] || 0) + 1;
  });

  // Sort by frequency
  const sortedChars = Object.entries(charCount)
    .sort((a, b) => b[1] - a[1])
    .map(([char, count]) => [char, count, false]);

  // Update characteristics sheet
  charSheet.clear();
  charSheet.getRange(1, 1, 1, 3).setValues([['Characteristic', 'Frequency', 'Use for Search']]);
  if (sortedChars.length > 0) {
    charSheet.getRange(2, 1, sortedChars.length, 3).setValues(sortedChars);
  }
}

// Function to find peer companies based on selected characteristics
function findPeerCompanies() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const charSheet = ss.getSheetByName('Characteristics');
  const resultsSheet = ss.getSheetByName('Peer Companies');
  
  if (!charSheet || !resultsSheet) {
    setupSpreadsheet();
    return;
  }

  const selectedChars = charSheet.getRange('B2:B').getValues()
    .flat()
    .map((checked, i) => checked ? charSheet.getRange(i + 2, 1).getValue() : null)
    .filter(Boolean);

  if (selectedChars.length === 0) {
    SpreadsheetApp.getUi().alert('Please select at least one characteristic to use for finding peer companies.');
    return;
  }

  const peers = findPeersByCharacteristics(selectedChars);
  
  // Update results sheet
  resultsSheet.clear();
  resultsSheet.getRange(1, 1, 1, 4).setValues([['Company', 'Match Score', 'Industry', 'Size']]);
  if (peers.length > 0) {
    resultsSheet.getRange(2, 1, peers.length, 4).setValues(peers);
  }
}

// Helper function to fetch company data from Linkup API
function fetchCompanyData(companyName) {
  const options = {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${LINKUP_API_KEY}`,
      'Content-Type': 'application/json'
    }
  };

  try {
    const response = UrlFetchApp.fetch(`${LINKUP_API_URL}/companies/search?q=${encodeURIComponent(companyName)}`, options);
    return JSON.parse(response.getContentText());
  } catch (error) {
    console.error(`Error fetching data for ${companyName}:`, error);
    return null;
  }
}

// Helper function to find peers based on characteristics
function findPeersByCharacteristics(characteristics) {
  const options = {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${LINKUP_API_KEY}`,
      'Content-Type': 'application/json'
    },
    payload: JSON.stringify({ characteristics })
  };

  try {
    const response = UrlFetchApp.fetch(`${LINKUP_API_URL}/companies/peers`, options);
    return JSON.parse(response.getContentText());
  } catch (error) {
    console.error('Error finding peers:', error);
    return [];
  }
}

// Function to set up the initial spreadsheet structure
function setupSpreadsheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Create or clear sheets
  const sheets = ['Input Companies', 'Characteristics', 'Peer Companies'];
  sheets.forEach(sheetName => {
    let sheet = ss.getSheetByName(sheetName);
    if (!sheet) {
      sheet = ss.insertSheet(sheetName);
    }
    sheet.clear();
  });

  // Set up Input Companies sheet
  const inputSheet = ss.getSheetByName('Input Companies');
  inputSheet.getRange('A1').setValue('Enter up to 5 company names below:');
  inputSheet.getRange('A2:A6').setBackground('#f3f3f3');

  // Set up Characteristics sheet
  const charSheet = ss.getSheetByName('Characteristics');
  charSheet.getRange('A1:C1').setValues([['Characteristic', 'Frequency', 'Use for Search']]);
  charSheet.getRange('C2:C').setDataValidation(SpreadsheetApp.newDataValidation()
    .requireCheckbox()
    .build());

  // Set up Peer Companies sheet
  const resultsSheet = ss.getSheetByName('Peer Companies');
  resultsSheet.getRange('A1:D1').setValues([['Company', 'Match Score', 'Industry', 'Size']]);

  // Hide unused sheets
  ss.getSheets().forEach(sheet => {
    if (!sheets.includes(sheet.getName())) {
      sheet.hideSheet();
    }
  });

  SpreadsheetApp.getUi().alert('Spreadsheet setup complete! You can now enter company names and use the Peer Finder menu.');
}
```

### Step 4: Configure Your API Key

1. Replace `YOUR_API_KEY` with your actual Linkup API key
2. If you don't have an API key:
   * Go to [app.linkup.so](https://app.linkup.so)
   * Create an account or sign in
   * Navigate to your API settings
   * Copy your API key

### Step 5: Save the Script

1. Click the "Save" button (or press Ctrl+S/Cmd+S)

### Step 6: Authorize the Script

1. When prompted, authorize the script to:
   * Access your Google Sheets
   * Make external API calls
   * Display dialogs

<img alt="Authorization Screen" />

*2: The Google authorization screen*

### Step 7: Initialize the Spreadsheet

1. Click "Run" and select "SetupSpreadsheet"

<img alt="Setup Spreadsheet" />

*3: Selecting SetupSpreadsheet*

### Step 8: Verify Setup

1. Look for a confirmation popup in your main sheet

<img alt="Confirmation Popup" />

*4: The confirmation popup*

### Step 9: Launch the Tool

1. Click "Run" and select "OnOpen"

<img alt="OnOpen Selection" />

*5: Selecting OnOpen*

## Using the Peer Finder

### Step 1: Enter Companies

1. Go to the "Input Companies" sheet
2. Enter up to 5 companies in cells A2-A6
3. Make sure to enter the full company names

### Step 2: Extract Characteristics

1. Click on the "Peer Finder" menu
2. Select "Extract Common Characteristics"
3. Wait for the process to complete
4. Review the extracted characteristics in the "Characteristics" sheet

### Step 3: Select Characteristics

1. In the "Characteristics" sheet, review the list of common characteristics
2. Use the checkboxes in column B to select which characteristics to use for finding peer companies
3. Select at least one characteristic

### Step 4: Find Peer Companies

1. Click on the "Peer Finder" menu again
2. Select "Find Peer Companies"
3. Wait for the process to complete
4. Review the list of peer companies in the "Peer Companies" sheet

### Step 5: Review and Refine

1. Review the list of peer companies
2. If needed, go back to Step 3 and adjust your characteristic selections
3. Run the peer finder again with different characteristics

<Info>
  For more detailed examples and use cases, check out our [Prompt Catalog](../../../documentation/tutorials/prompt-catalog).
</Info>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Prompting
Source: https://docs.linkup.so/pages/documentation/tutorials/prompting

Learn how to best prompt Linkup search with - tips, templates, and best practices

Linkup is a precise engine designed to follow **detailed instructions** like a research assistant. The more guidance you give, the better the result. This guide explains how Linkup works, provides practical prompting techniques, and offers templates to get you started.

***

## 1. How the Search API Works

Linkup uses agentic search powered by AI to return content that is as precise and accurate as possible for a given query.

For each request, Linkup:

* Interprets the query and the user's instructions
* Determines how to execute retrieval steps using the available retrieval mechanisms
* Executes those steps according to the selected search depth

Linkup is aware of its internal search and extraction tools and can be explicitly instructed to use them in a certain way through prompting (e.g., run several searches, scrape specific URLs, execute steps sequentially).

**Key implication:** Agentic search follows instructions literally. Clear and detailed prompts lead to more precise retrieval behavior, especially in `deep` search.

***

## 2. Search Depth: Standard vs. Deep

Linkup supports two search depths. You select the depth for each request, and it defines how retrieval steps are executed.

### Standard search (`depth="standard"`)

**Behavior:**

* Executes a single iteration of retrieval
* Does not reuse outputs from one step in another (e.g., an extracted URL cannot be used in a follow-up step)
* Optimizes for latency by minimizing retrieval operations
* May split a query into sub-searches only if explicitly instructed or required to answer correctly

**Best suited for:**

* Simple or direct questions
* High-volume or low-latency use cases
* Queries where the answer is likely found quickly

### Deep search (`depth="deep"`)

**Behavior:**

* Executes up to 10 iterations of retrieval (iterates until the context sufficiently answers the query)
* Each iteration is aware of the context produced by previous iterations
* If required information is missing, additional iterations may be launched with refined or adjacent queries
* Supports sequential instructions, where outputs from one step are used in the next (e.g., search first, then scrape a discovered URL)

**Best suited for:**

* Complex or multi-step queries
* Company or market research
* Cases where information is not reliably found in a single pass
* Prompts that explicitly require several searches or sequential actions

> **Rule of thumb:**
>
> * If you could answer the question with one Google search → use `standard`
> * If a human would open multiple tabs → use `deep`

### When Simple Prompts Are Enough

Not every query needs a structured prompt. If your goal is **breadth** (source coverage) rather than **precision** (specific data extraction), keep it simple.

**Research and news queries** are a good example. Users typically want search results and will handle synthesis on their end. For these, you don't need roles, extraction steps, or output formatting.

| Use case | Simple prompt                                                                                       |
| -------- | --------------------------------------------------------------------------------------------------- |
| Research | Find the latest significant research on consciousness. Run several searches with adjacent keywords. |
| News     | Find recent news about OpenAI. Run several searches with adjacent keywords.                         |
| Trends   | What are people saying about AI agents on Twitter and Reddit? Run several searches.                 |

**When to keep it simple:**

* You want many sources, not one precise answer
* You'll process/filter the results yourself
* The topic is broad or exploratory

**When to add structure:**

* You need specific data points (prices, names, dates)
* You want Linkup to scrape and extract from pages
* The output needs a defined format

### Bad vs. Good Prompts

| Bad                                                      | Good (standard)                                                                                                                                                                                                                       | Good (deep)                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generate a business description of linkup.so             | You are an expert company researcher. Run a web search to find what the company  does. Then, scrape the page: . Only return a 3-sentence description of the company: what it does, who it serves, and its main differentiator.        | You are an expert business analyst. Your role is to generate a detailed description of the company . To do so you must consult: its homepage, product page, about us page, and LinkedIn profile. First, find these page URLs, then scrape each URL. Do not stop until you have scraped each URL. Return a structured company overview including: what the company does, products/services, target customers, value proposition, and founding story.                                      |
| Analyze the company website to determine its GTM motion. | You are an expert GTM analyst. Run a web search to find if  uses self-service signup, free trials, or sales demos. Then, scrape the page: . Only return whether the company is PLG or SLG, with the evidence found, and nothing else. | You are an expert GTM analyst. Your objective is to determine if  follows Product-Led Growth (PLG) or Sales-Led Growth (SLG). First, find and scrape the company's homepage, pricing page, and sign-up flow. For each page, extract evidence of: self-service signup options, free trial availability, demo request CTAs, sales contact requirements, pricing transparency. Then, based on the data collected, determine whether the company is PLG or SLG with a 3-sentence conclusion. |
| Latest research on consciousness                         | Find the latest significant research on consciousness. Run several searches with adjacent keywords.                                                                                                                                   | Find the latest significant research on consciousness. For each topic below, run several searches with adjacent keywords: - neuroscience of consciousness - integrated information theory - global workspace theory - AI and machine consciousness. For each publicly-available result, scrape the page to extract the full abstract or article summary.                                                                                                                                 |

***

## 3. Anatomy of a Good Prompt

### Core Principle: Focus on Data Retrieval

If you're using Linkup, you're most likely looking for data — this is what your prompt should focus on. Answer generation should not be the objective of your prompt.

| Bad                                                          | Good                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to estimate the annual IT costs of the company Total SA? | You are an expert information systems consultant. Your objective is to find data that can be used to estimate the total cost of ownership (TCO) of Total SA's intranet. First, search for data that can support this estimation. Then, produce an estimate. If no information allows for a precise estimation, still produce an estimate based on the data you were able to find. |

The first prompt asks for an answer directly. The second prompt focuses on finding the data first, then using it to produce an estimate.

### The Four Components

A strong prompt usually includes:

| Component                                            | Description                                                            | Example                                                                                                         |
| ---------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Goal**                                             | What do you want to find or understand?                                | "You are an expert business analyst. Your goal is find context to generate a detailed business description of " |
| **Scope**                                            | Where should the system look?                                          | "The company domain is linkup.so. Analyze the homepage, about us page, and blog section."                       |
| **Criteria / Method**                                | What type of information and analytical depth should the system apply? | "Include products, business model, target market, and value chain positioning"                                  |
| **Format (when using sourcedAnswer and Structured)** | How should the response be structured or returned?                     | "Be sharp and business oriented in your answer."                                                                |

**Tip**: If you want us to look into specific sources, tell us! Examples include: company domains, news articles, LinkedIn URLs, etc.

### Common Mistakes

Weak prompts often:

* Are vague: "Tell me about the company" → What exactly? Revenue? Product strategy?
* Lack instructions: "Summarize this page" → How? As a bullet list? As a paragraph?
* Are unstructured: "Give me pricing, hiring plans, GTM strategy, and roadmap" → No sequence, no sources, no extraction steps. Instead, specify which pages to scrape and what data to extract from each.

***

## 4. Advanced Prompting Techniques

### Leverage the Scraper (standard and deep)

Since Linkup has a scraper as a tool, you can provide a URL and query the page in natural language. Even in `standard`, you can both scrape a page and force a web search in parallel.

**Example:**

```
Scrape the website linkup.so.
Also run a search to find articles, news, and posts mentioning linkup.so clients.
Based on the content from the website and from the search, return a list of clients that use Linkup, as well as the source of the information.
```

### Run Multiple Searches for Better Coverage (standard and deep)

If you want to optimize for source coverage (e.g., for research or news use cases), add to your prompt: "run several searches with adjacent keywords."

If you want to find several pieces of information that would be handled through separate searches, be explicit about it. Linkup can execute multiple searches even in `standard` mode.

### Use Sequential Search with LinkedIn

LinkedIn content often requires a two-step approach:

```
First find LinkedIn posts on context engineering.
Then, for each URL, extract the LinkedIn comments.
Then, return the LinkedIn profile URL of the commenters.
```

### Use Sequential Search: Search → Scrape (deep)

If what you're looking for requires you to 1) find a website URL, then 2) scrape the website, use **`deep`** and explicitly ask to "first find the URL, then scrape the URL."

This is essential for:

* Detailed answers that rely on full pages vs. search snippets
* Returning a list of precise items on a page (product characteristics, PDF links, other URLs, etc.)
* Tasks requiring prices, images, or specifications

**Example:**

```
**Your role is to** map a company's value proposition from its website.

**Inputs:**
- `{company_name}`
- `{company_website}`

**Objective:** Extract the core value proposition communicated on public-facing product pages.

**Instructions:**
- First, find and scrape the homepage and primary product pages.
- From each page, extract: headline claims, customer benefits, differentiator language, and CTAs.
- Then, synthesize the extracted data into a summary of the value proposition.
- Avoid vague marketing fluff. Focus on concrete external value claims.
```

***

## 5. Resources

### Prompt Optimizer

Get the most out of Linkup by optimizing your search prompts. Our prompt optimizer helps you craft better queries that yield more accurate and relevant results.

[**Launch Prompt Optimizer →**](https://prompt.linkup.so)

### Prompt Templates

Access our curated library of proven prompt templates for common business intelligence and research scenarios.

[**Browse Prompt Templates →**](https://prompt.linkup.so/templates)

**Template categories:**

* **Business Intelligence**: Analyze companies, competitors, and market dynamics
* **Research**: Conduct thorough investigations on specific topics
* **Competitive Analysis**: Understand positioning and strategies
* **Market Research**: Gather insights about industries and trends

### Sample Prompts for Business Intelligence

Below is a list of prompts you can leverage to extract intelligence from company websites. We have a full list [here](https://linkup-platform.notion.site/The-100-Prompts-You-Need-to-Leverage-AI-in-Your-GTM-Strategy-1cb161ecef69809593b3d2c51bbee943?pvs=74), or you can access our [Prompting Templates library](https://prompt.linkup.so/templates).

#### Map a Competitor's Value Proposition

**Your role is to** map a company's value proposition from its website.

**Inputs:**

* `{company_name}`
* `{company_website}`

**Objective:** Extract the core value proposition communicated on public-facing product pages.

**Instructions:**

* First, find and scrape the homepage and primary product pages.
* From each page, extract: headline claims, customer benefits, differentiator language, and CTAs.
* Then, synthesize the extracted data into a summary of the value proposition.
* Avoid vague marketing fluff. Focus on concrete external value claims.

#### Identify a Company's ICP

**Your role is to** determine a company's Ideal Customer Profile (ICP).

**Inputs:**

* `{company_name}`
* `{company_website}`

**Objective:** Infer the ICP based on how the company communicates publicly.

**Instructions:**

* First, find and scrape the homepage, use case pages, and 2-3 recent blog posts.
* From each page, extract: industries mentioned, company sizes referenced, job titles targeted, and pain points addressed.
* Also extract any visible customer logos.
* Then, based on the extracted data, infer the ICP (industry, company size, buyer persona, key pain points).

#### Determine if the Company Publishes a Public Roadmap

**Your role is to** check whether the company shares future product features publicly.

**Inputs:**

* `{company_website}`

**Objective:** Evaluate product transparency and customer feedback incorporation.

**Instructions:**

* First, search for "roadmap", "coming soon", or "what's next" pages on .
* Also search for any Canny, Trello, or Notion boards linked to the company.
* For each relevant URL found, scrape the page to extract roadmap items.
* Return: roadmap URL (if found), items with their status (planned/in progress/live), and whether the roadmap is public or requires login.

***

## To Go Further

There are many ways to optimize your prompts and results with Linkup. If you'd like to discuss your use case further, please feel free to reach out to our team at [support@linkup.so](mailto:support@linkup.so) or via our Discord.

You can also [book a quick 15-minute call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9).


# Signup Radar 
Source: https://docs.linkup.so/pages/documentation/tutorials/signup-radar

Building a signup radar to get to know your new users

This tutorial will show you how to build a simple "signup radar" that takes an email address and returns information about the person who signed up, using the Linkup API's structured output feature.

## What We're Building

Our signup radar will:

* Take an email address as input
* Use Linkup API to search for information about the person
* Return structured data about the person (name, position, company, LinkedIn URL, etc.)

## Prerequisites

* A Linkup API key
* Python or Node.js installed

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

<Steps>
  <Step title="Install the SDK">
    <CodeGroup>
      ```python python theme={null}
      pip install linkup-sdk
      ```

      ```javascript js theme={null}
      npm i linkup-sdk
      ```
    </CodeGroup>
  </Step>

  <Step title="Set Up the Client">
    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")
      ```

      ```javascript js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: '<YOUR_LINKUP_API_KEY>',
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Define the Structured Output Schema">
    The key to our signup radar is using Linkup's structured output feature. We need to define a schema that specifies what information we want to extract.

    <CodeGroup>
      ```python python theme={null}
      import json

      schema = {
        "type": "object",
        "properties": {
          "fullName": {
            "type": "string",
            "description": "The full name of the person"
          },
          "company": {
            "type": "string",
            "description": "The company the person works for"
          },
          "position": {
            "type": "string",
            "description": "The job title or position of the person"
          },
          "linkedInUrl": {
            "type": "string",
            "description": "The LinkedIn profile URL of the person"
          },
          "companyWebsite": {
            "type": "string",
            "description": "The website of the company"
          },
          "additionalInfo": {
            "type": "string",
            "description": "Any additional relevant information about the person"
          }
        },
        "required": ["fullName", "company"]
      }

      schema_str = json.dumps(schema)
      ```

      ```javascript js theme={null}
      const schema = {
        type: "object",
        properties: {
          fullName: {
            type: "string",
            description: "The full name of the person"
          },
          company: {
            type: "string",
            description: "The company the person works for"
          },
          position: {
            type: "string",
            description: "The job title or position of the person"
          },
          linkedInUrl: {
            type: "string",
            description: "The LinkedIn profile URL of the person"
          },
          companyWebsite: {
            type: "string",
            description: "The website of the company"
          },
          additionalInfo: {
            type: "string",
            description: "Any additional relevant information about the person"
          }
        },
        required: ["fullName", "company"]
      };
      ```
    </CodeGroup>
  </Step>

  <Step title="Create the Signup Radar Function">
    <CodeGroup>
      ```python python theme={null}
      def signup_radar(email):
          # Extract name and domain
          name_part = email.split('@')[0]
          domain = email.split('@')[1]
          
          # Format name for searching (convert saksena to Saksena)
          formatted_name = name_part.capitalize()
          
          # Determine company from domain (if not common email provider)
          company_hint = ""
          common_domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"]
          if domain not in common_domains:
              company_hint = domain.split('.')[0]
          
          # Create search query
          if company_hint:
              query = f"Find the LinkedIn profile URL for {formatted_name} who works at {company_hint}. Return their full name, current position, and company information."
          else:
              query = f"Find the LinkedIn profile URL for someone with the email username {formatted_name}. Return their full name, current position, and company information."
          
          # Call Linkup API
          response = client.search(
              query=query,
              depth="deep",  # Use deep for more thorough results
              output_type="structured",
              structured_output_schema=schema_str
          )
          
          return response

      # Example usage
      from pprint import pprint

      result = signup_radar("philippe@linkup.so")
      pprint(result)
      ```

      ```javascript js theme={null}
      async function signupRadar(email) {
          // Extract name and domain
          const [namePart, domain] = email.split('@');
          
          // Format name for searching
          const formattedName = namePart.charAt(0).toUpperCase() + namePart.slice(1);
          
          // Determine company from domain (if not common email provider)
          let companyHint = "";
          const commonDomains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"];
          if (!commonDomains.includes(domain)) {
              companyHint = domain.split('.')[0];
          }
          
          // Create search query
          let query;
          if (companyHint) {
              query = `Find the LinkedIn profile URL for ${formattedName} who works at ${companyHint}. Return their full name, current position, and company information.`;
          } else {
              query = `Find the LinkedIn profile URL for someone with the email username ${formattedName}. Return their full name, current position, company, and LinkedIn URL.`;
          }
          
          // Call Linkup API
          const response = await client.search({
              query: query,
              depth: "deep",  // Use deep for more thorough results
              outputType: "structured",
              structuredOutputSchema: schema
          });
          
          return response;
      }

      // Example usage
      signupRadar("philippe@linkup.so").then(console.log);
      ```
    </CodeGroup>
  </Step>

  <Step title="Enhance Query Generation">
    Let's improve our query to get better results:

    <CodeGroup>
      ```python python theme={null}
      def generate_query(email):
          name_part = email.split('@')[0]
          domain = email.split('@')[1]
          
          # Handle different name formats (snake_case, dot.case, etc.)
          if "_" in name_part:
              name_parts = name_part.split("_")
              formatted_name = " ".join(part.capitalize() for part in name_parts)
          elif "." in name_part:
              name_parts = name_part.split(".")
              formatted_name = " ".join(part.capitalize() for part in name_parts)
          else:
              formatted_name = name_part.capitalize()
          
          # Determine company from domain
          common_domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"]
          if domain not in common_domains:
              company = domain.split('.')[0].capitalize()
              return f"Find the LinkedIn profile URL for this person: {formatted_name} at {company}. If the domain of the email address ({domain}) is not a common email provider, it is probably the name of the company this person works for and {domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, LinkedIn URL, as well as any relevant information you can find about them."
          else:
              return f"Find the LinkedIn profile URL for this person with email username {formatted_name}. Return their full name, current position, company, and LinkedIn URL."
      ```

      ```javascript js theme={null}
      function generateQuery(email) {
          const [namePart, domain] = email.split('@');
          
          // Handle different name formats (snake_case, dot.case, etc.)
          let formattedName;
          if (namePart.includes("_")) {
              formattedName = namePart.split("_")
                  .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                  .join(" ");
          } else if (namePart.includes(".")) {
              formattedName = namePart.split(".")
                  .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                  .join(" ");
          } else {
              formattedName = namePart.charAt(0).toUpperCase() + namePart.slice(1);
          }
          
          // Determine company from domain
          const commonDomains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"];
          if (!commonDomains.includes(domain)) {
              const company = domain.split('.')[0].charAt(0).toUpperCase() + domain.split('.')[0].slice(1);
              return `Find the LinkedIn profile URL for this person: ${formattedName} at ${company}. If the domain of the email address (${domain}) is not a common email provider, it is probably the name of the company this person works for and ${domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, and LinkedIn URL, as well as any relevant information you can find about them.`;
          } else {
              return `Find the LinkedIn profile URL for this person with email username ${formattedName}. Return their full name, current position, company, and LinkedIn URL.`;
          }
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Put It All Together">
    Here's the complete implementation:

    <CodeGroup>
      ```python python [expandable] theme={null}
      from linkup import LinkupClient
      import json
      from pprint import pprint

      class SignupRadar:
          def __init__(self, api_key):
              self.client = LinkupClient(api_key=api_key)
              self.schema = {
                  "type": "object",
                  "properties": {
                      "fullName": {
                          "type": "string",
                          "description": "The full name of the person"
                      },
                      "company": {
                          "type": "string",
                          "description": "The company the person works for"
                      },
                      "position": {
                          "type": "string",
                          "description": "The job title or position of the person"
                      },
                      "linkedInUrl": {
                          "type": "string",
                          "description": "The LinkedIn profile URL of the person"
                      },
                      "companyWebsite": {
                          "type": "string",
                          "description": "The website of the company"
                      },
                      "additionalInfo": {
                          "type": "string",
                          "description": "Any additional relevant information about the person"
                      }
                  },
                  "required": ["fullName", "company"]
              }
              self.schema_str = json.dumps(self.schema)
          
          def generate_query(self, email):
              name_part = email.split('@')[0]
              domain = email.split('@')[1]
              
              # Handle different name formats (snake_case, dot.case, etc.)
              if "_" in name_part:
                  name_parts = name_part.split("_")
                  formatted_name = " ".join(part.capitalize() for part in name_parts)
              elif "." in name_part:
                  name_parts = name_part.split(".")
                  formatted_name = " ".join(part.capitalize() for part in name_parts)
              else:
                  formatted_name = name_part.capitalize()
              
              # Determine company from domain
              common_domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"]
              if domain not in common_domains:
                  company = domain.split('.')[0].capitalize()
                  return f"Find the LinkedIn profile URL for this person: {formatted_name} at {company}. If the domain of the email address ({domain}) is not a common email provider, it is probably the name of the company this person works for and {domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, LinkedIn URL, as well as any relevant information you can find about them."
              else:
                  return f"Find the LinkedIn profile URL for this person with email username {formatted_name}. Return their full name, current position, company, and LinkedIn URL."
          
          def lookup(self, email):
              query = self.generate_query(email)
              
              response = self.client.search(
                  query=query,
                  depth="deep",  # Use deep for more thorough results
                  output_type="structured",
                  structured_output_schema=self.schema_str
              )
              
              return response

      # Example usage
      if __name__ == "__main__":
          radar = SignupRadar(api_key="<YOUR_LINKUP_API_KEY>")
          
          # Example emails
          emails = [
              "philippe@linkup.so",
              "boris@linkup.so"
          ]
          
          for email in emails:
              print(f"\nLooking up: {email}")
              result = radar.lookup(email)
              pprint(result)
      ```

      ```javascript js [expandable] theme={null}
      import { LinkupClient } from 'linkup-sdk';

      class SignupRadar {
          constructor(apiKey) {
              this.client = new LinkupClient({
                  apiKey: apiKey,
              });
              
              this.schema = {
                  type: "object",
                  properties: {
                      fullName: {
                          type: "string",
                          description: "The full name of the person"
                      },
                      company: {
                          type: "string",
                          description: "The company the person works for"
                      },
                      position: {
                          type: "string",
                          description: "The job title or position of the person"
                      },
                      linkedInUrl: {
                          type: "string",
                          description: "The LinkedIn profile URL of the person"
                      },
                      companyWebsite: {
                          type: "string",
                          description: "The website of the company"
                      },
                      additionalInfo: {
                          type: "string",
                          description: "Any additional relevant information about the person"
                      }
                  },
                  required: ["fullName", "company"]
              };
          }
          
          generateQuery(email) {
              const [namePart, domain] = email.split('@');
              
              // Handle different name formats (snake_case, dot.case, etc.)
              let formattedName;
              if (namePart.includes("_")) {
                  formattedName = namePart.split("_")
                      .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                      .join(" ");
              } else if (namePart.includes(".")) {
                  formattedName = namePart.split(".")
                      .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                      .join(" ");
              } else {
                  formattedName = namePart.charAt(0).toUpperCase() + namePart.slice(1);
              }
              
              // Determine company from domain
              const commonDomains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"];
              if (!commonDomains.includes(domain)) {
                  const company = domain.split('.')[0].charAt(0).toUpperCase() + domain.split('.')[0].slice(1);
                  return `Find the LinkedIn profile URL for this person: ${formattedName} at ${company}. If the domain of the email address (${domain}) is not a common email provider, it is probably the name of the company this person works for and ${domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, and LinkedIn URL, as well as any relevant information you can find about them.`;
              } else {
                  return `Find the LinkedIn profile URL for this person with email username ${formattedName}. Return their full name, current position, company, and LinkedIn URL.`;
              }
          }
          
          async lookup(email) {
              const query = this.generateQuery(email);
              
              const response = await this.client.search({
                  query: query,
                  depth: "deep",  // Use deep for more thorough results
                  outputType: "structured",
                  structuredOutputSchema: this.schema
              });
              
              return response;
          }
      }

      // Example usage
      async function main() {
          const radar = new SignupRadar('<YOUR_LINKUP_API_KEY>');
          
          // Example emails
          const emails = [
              "philippe@linkup.so",
              "boris@linkup.so"
          ];
          
          for (const email of emails) {
              console.log(`\nLooking up: ${email}`);
              const result = await radar.lookup(email);
              console.log(JSON.stringify(result, null, 2));
          }
      }

      main().catch(console.error);
      ```
    </CodeGroup>
  </Step>
</Steps>

## How It Works

1. **Email Analysis**: The tool parses the email to extract the username and domain.
2. **Query Generation**: It creates a smart search query based on the email components:
   * Formats the username to handle common patterns (first.last, first\_last)
   * Uses the domain as a company hint if it's not a common email provider
3. **Structured Output**: Uses Linkup's structured output feature with a custom schema to ensure consistent, well-formatted results.
4. **Deep Search**: Uses the "deep" search depth for more comprehensive results.

## Test Examples

Try the signup radar with these email examples:

* [philippe@linkup.so](mailto:philippe@linkup.so)
* [boris@linkup.so](mailto:boris@linkup.so)
* [sacha@linkup.so](mailto:sacha@linkup.so)
* [philippe.mizrahi@gmail.com](mailto:philippe.mizrahi@gmail.com)

## Advanced Enhancements

For a production version, consider adding:

* Other relevant information on your users you receive in the sign up form. These should be added to the prompt
* Better manage ambiguity when multiple people could own the same email. Change the prompt and the structured output format to allow for multiple potential people
* Error handling for invalid emails or API failures
* Rate limiting to manage API usage
* Async batch processing for multiple emails

## Conclusion

You've now built a simple but powerful "signup radar" using the Linkup API that can extract structured information about users from just their email address. The structured output feature ensures you get consistent, well-formatted data that can be easily integrated into your systems.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Structured Output Guide
Source: https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide

How to take advantage of Structured Outputs

Linkup's structured output feature allows you to receive responses in a custom format that you define. This is particularly useful when you need to integrate Linkup's responses directly into your application's data structure or when you want to ensure consistency in the response format.

## How It Works

To use structured outputs:

1. Set `outputType` to `structured` in your API request
2. Provide a JSON schema string in the `structuredOutputSchema` parameter
3. The API will return a response that strictly follows your schema

<Warning>
  Write your query so that its answer contains the information requested in the
  `structuredOutputSchema`- the system will use the query response to fill the
  output
</Warning>

## Basic Examples

Let's look at some simple examples that demonstrate how to use structured outputs for different use cases:

<AccordionGroup>
  <Accordion title="Company Revenue Example" icon="building">
    <p>This example extracts company classification information:</p>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="YOUR_API_KEY")

      schema = """{
          "type": "object",
          "properties": {
              "companyName": {
                  "type": "string",
                  "description": "The name of the company"
              },
              "revenueAmount": {
                  "type": "number",
                  "description": "The revenue amount"
              },
              "fiscalYear": {
                  "type": "string",
                  "description": "The fiscal year for this revenue"
              }
          }
      }"""

      response = client.search(
          query="What is Microsoft's 2024 revenue?",
          depth="deep",
          output_type="structured",
          structured_output_schema=schema
      )

      print(response)
      ```

      ```js js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: 'YOUR_API_KEY',
      });

      const schema = {
        "type": "object",
        "properties": {
          "companyName": {
            "type": "string",
            "description": "The name of the company"
          },
          "revenueAmount": {
            "type": "number",
            "description": "The revenue amount"
          },
          "fiscalYear": {
            "type": "string",
            "description": "The fiscal year for this revenue"
          }
        }
      };

      const getCompanyRevenue = async () => {
        return await client.search({
          query: "What is Microsoft's 2024 revenue?",
          depth: 'deep',
          outputType: 'structured',
          structuredOutputSchema: schema
        });
      };

      getCompanyRevenue().then(console.log);
      ```

      ```bash curl theme={null}
      curl --request POST \
        --url https://api.linkup.so/v1/search \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "q": "What is Microsoft'\''s 2024 revenue?",
        "depth": "deep",
        "outputType": "structured",
        "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"companyName\":{\"type\":\"string\",\"description\":\"The name of the company\"},\"revenueAmount\":{\"type\":\"number\",\"description\":\"The revenue amount\"},\"fiscalYear\":{\"type\":\"string\",\"description\":\"The fiscal year for this revenue\"}}}"
      }'
      ```
    </CodeGroup>

    Example response:

    ```json theme={null}
    {
        "companyName": "Microsoft",
        "revenueAmount": 245100000000,
        "fiscalYear": "2024"
    }
    ```
  </Accordion>

  <Accordion title="Movie Information Example" icon="film">
    <p>This example shows how to retrieve basic information about a movie:</p>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="YOUR_API_KEY")

      schema = """{
          "type": "object",
          "properties": {
              "movieTitle": {
                  "type": "string",
                  "description": "The title of the movie"
              },
              "director": {
                  "type": "string",
                  "description": "The director of the movie"
              },
              "releaseYear": {
                  "type": "integer",
                  "description": "The year the movie was released"
              },
              "boxOfficeRevenue": {
                  "type": "number",
                  "description": "The worldwide box office revenue in USD"
              }
          },
          "required": ["movieTitle", "director", "releaseYear", "boxOfficeRevenue"]
      }"""

      response = client.search(
          query="What was the director, release year, and box office revenue for The Matrix?",
          depth="deep",
          output_type="structured",
          structured_output_schema=schema
      )

      print(response)
      ```

      ```js js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: 'YOUR_API_KEY',
      });

      const schema = {
          "type": "object",
          "properties": {
              "movieTitle": {
                  "type": "string",
                  "description": "The title of the movie"
              },
              "director": {
                  "type": "string",
                  "description": "The director of the movie"
              },
              "releaseYear": {
                  "type": "integer",
                  "description": "The year the movie was released"
              },
              "boxOfficeRevenue": {
                  "type": "number",
                  "description": "The worldwide box office revenue in USD"
              }
          },
          "required": ["movieTitle", "director", "releaseYear", "boxOfficeRevenue"]
      };

      const getMovieInfo = async () => {
        return await client.search({
          query: "What was the director, release year, and box office revenue for The Matrix?",
          depth: 'deep',
          outputType: 'structured',
          structuredOutputSchema: schema
        });
      };

      getMovieInfo().then(console.log);
      ```

      ```bash curl theme={null}
      curl --request POST \
        --url https://api.linkup.so/v1/search \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "q": "What was the director, release year, and box office revenue for The Matrix?",
        "depth": "deep",
        "outputType": "structured",
        "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"movieTitle\":{\"type\":\"string\",\"description\":\"The title of the movie\"},\"director\":{\"type\":\"string\",\"description\":\"The director of the movie\"},\"releaseYear\":{\"type\":\"integer\",\"description\":\"The year the movie was released\"},\"boxOfficeRevenue\":{\"type\":\"number\",\"description\":\"The worldwide box office revenue in USD\"}}}"
      }'
      ```
    </CodeGroup>

    Example response:

    ```json theme={null}
    {
        "movieTitle": "The Matrix",
        "director": "Lana and Lilly Wachowski",
        "releaseYear": 1999,
        "boxOfficeRevenue": 465300000
    }
    ```
  </Accordion>

  <Accordion title="Weather Information Example" icon="cloud-sun">
    <p>This example retrieves weather information for travel planning:</p>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="YOUR_API_KEY")

      schema = """{
          "type": "object",
          "properties": {
              "city": {
                  "type": "string",
                  "description": "The name of the city"
              },
              "averageTemperature": {
                  "type": "object",
                  "properties": {
                      "summer": {
                          "type": "number",
                          "description": "Average temperature in summer (°C)"
                      },
                      "winter": {
                          "type": "number",
                          "description": "Average temperature in winter (°C)"
                      }
                  }
              },
              "annualRainfall": {
                  "type": "number",
                  "description": "Annual rainfall in millimeters"
              },
              "bestTimeToVisit": {
                  "type": "array",
                  "items": {
                      "type": "string"
                  },
                  "description": "The recommended months to visit"
              }
          }
      }"""

      response = client.search(
          query="What is the average temperature, rainfall, and best time to visit Tokyo?",
          depth="deep",
          output_type="structured",
          structured_output_schema=schema
      )

      print(response)
      ```

      ```js js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: 'YOUR_API_KEY',
      });

      const schema = {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The name of the city"
          },
          "averageTemperature": {
            "type": "object",
            "properties": {
              "summer": {
                "type": "number",
                "description": "Average temperature in summer (°C)"
              },
              "winter": {
                "type": "number",
                "description": "Average temperature in winter (°C)"
              }
            }
          },
          "annualRainfall": {
            "type": "number",
            "description": "Annual rainfall in millimeters"
          },
          "bestTimeToVisit": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The recommended months to visit"
          }
        }
      };

      const getWeatherInfo = async () => {
        return await client.search({
          query: "What is the average temperature, rainfall, and best time to visit Tokyo?",
          depth: 'deep',
          outputType: 'structured',
          structuredOutputSchema: schema
        });
      };

      getWeatherInfo().then(console.log);
      ```

      ```bash curl theme={null}
      curl --request POST \
        --url https://api.linkup.so/v1/search \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "q": "What is the average temperature, rainfall, and best time to visit Tokyo?",
        "depth": "deep",
        "outputType": "structured",
        "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"city\":{\"type\":\"string\",\"description\":\"The name of the city\"},\"averageTemperature\":{\"type\":\"object\",\"properties\":{\"summer\":{\"type\":\"number\",\"description\":\"Average temperature in summer (°C)\"},\"winter\":{\"type\":\"number\",\"description\":\"Average temperature in winter (°C)\"}}},\"annualRainfall\":{\"type\":\"number\",\"description\":\"Annual rainfall in millimeters\"},\"bestTimeToVisit\":{\"type\":\"array\",\"items\":{\"type\":\"string\"},\"description\":\"The recommended months to visit\"}}}"
      }'
      ```
    </CodeGroup>

    Example response:

    ```json theme={null}
    {
        "city": "Tokyo",
        "averageTemperature": {
            "summer": 26.4,
            "winter": 6.1
        },
        "annualRainfall": 1530.8,
        "bestTimeToVisit": ["March", "April", "October", "November"]
    }
    ```
  </Accordion>
</AccordionGroup>

## Advanced Example: Competitive Analysis

This example shows how to extract structured competitive analysis information:

<CodeGroup>
  ```python python [expandable] theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="YOUR_API_KEY")

  schema = """{
    "type": "object",
    "properties": {
      "companies": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "marketPosition": {
              "type": "object",
              "properties": {
                "globalMarketShare": {
                  "type": "number"
                },
                "rankingByRevenue": {
                  "type": "integer"
                }
              }
            },
            "strengths": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "challenges": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      },
      "marketOverview": {
        "type": "string"
      }
    }
  }"""

  response = client.search(
    query="Compare Apple and Samsung in the smartphone market, focusing on their market share, global revenue, key strengths, and primary challenges.",
    depth="deep",
    output_type="structured",
    structured_output_schema=schema
  )

  print(response)

  ```

  ```js js [expandable] theme={null}
  import { LinkupClient } from "linkup-sdk";

  const client = new LinkupClient({
  	apiKey: "YOUR_API_KEY",
  });

  const schema = {
  	type: "object",
  	properties: {
  		companies: {
  			type: "array",
  			items: {
  				type: "object",
  				properties: {
  					name: {
  						type: "string",
  					},
  					marketPosition: {
  						type: "object",
  						properties: {
  							globalMarketShare: {
  								type: "number",
  							},
  							rankingByRevenue: {
  								type: "integer",
  							},
  						},
  					},
  					strengths: {
  						type: "array",
  						items: {
  							type: "string",
  						},
  					},
  					challenges: {
  						type: "array",
  						items: {
  							type: "string",
  						},
  					},
  				},
  			},
  		},
  		marketOverview: {
  			type: "string",
  		},
  	},
  };

  const getCompetitiveAnalysis = async () => {
  	return await client.search({
  		query:
  			"Compare Apple and Samsung in the smartphone market, focusing on their market share, global revenue, key strengths, and primary challenges.",
  		depth: "deep",
  		outputType: "structured",
  		structuredOutputSchema: schema,
  	});
  };

  getCompetitiveAnalysis().then(console.log);
  ```

  ```bash curl [expandable] theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "Compare Apple and Samsung in the smartphone market, focusing on their market share, global revenue, key strengths, and primary challenges.",
    "outputType": "structured",
    "depth": "deep",
    "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"companies\":{\"type\":\"array\",\"items\":{\"type\":\"object\",\"properties\":{\"name\":{\"type\":\"string\"},\"marketPosition\":{\"type\":\"object\",\"properties\":{\"globalMarketShare\":{\"type\":\"number\"},\"rankingByRevenue\":{\"type\":\"integer\"}}},\"strengths\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}},\"challenges\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}}}}},\"marketOverview\":{\"type\":\"string\"}}}"
  }'
  ```
</CodeGroup>

Example response:

```json [expandable] theme={null}
{
	"companies": [
		{
			"name": "Apple",
			"marketPosition": {
				"globalMarketShare": 17.2,
				"rankingByRevenue": 1
			},
			"strengths": [
				"Strong brand loyalty",
				"Premium pricing power",
				"Integrated ecosystem"
			],
			"challenges": [
				"Market saturation",
				"Strong competition in emerging markets",
				"Supply chain dependencies"
			]
		},
		{
			"name": "Samsung",
			"marketPosition": {
				"globalMarketShare": 20.1,
				"rankingByRevenue": 2
			},
			"strengths": [
				"Diverse product portfolio",
				"Vertical integration",
				"Strong presence in emerging markets"
			],
			"challenges": [
				"Intense competition at all price points",
				"Margin pressure in mid-range segment",
				"Brand perception vs Apple in premium segment"
			]
		}
	],
	"marketOverview": "The smartphone market continues to be highly competitive with a focus on 5G capabilities and AI integration. Premium segment shows steady growth while mid-range experiences intense competition."
}
```

## Making Fields Required

To make sure that the key fields you defined are filled, you can mark them as `required` in your json schema.

```json Required Fields Highlight {17} theme={null}
{
	"type": "object",
	"properties": {
		"movieTitle": {
			"type": "string",
			"description": "The title of the movie"
		},
		"director": {
			"type": "string",
			"description": "The director of the movie"
		},
		"releaseYear": {
			"type": "integer",
			"description": "The year the movie was released"
		}
	},
	"required": ["movieTitle", "director"]
}
```

## Best Practices

1. **Schema Design**:

   * Keep your schema as simple as possible while meeting your needs
   * Add descriptions to the fields to limit ambiguity
   * Use appropriate data types (string, number, boolean, etc.)
   * When in doubt, refer to the [JSON documentation](https://json-schema.org/learn/getting-started-step-by-step)

2. **Query Formulation**:
   * Write your query so that its answer contains the information requested in the `structuredOutputSchema`- the system will use the query response to fill the output
   * Provide clear context in your query and use explicit instructions

## Common Use Cases

* Company classification and categorization
* Competitive analysis
* Market research
* Product comparisons
* Company performance assessments

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Frequently Asked Questions
Source: https://docs.linkup.so/pages/faq/faq



<AccordionGroup>
  <Accordion title="What is the difference between Linkup and Perplexity Sonar?">
    * While Perplexity is a generalist chatbot, Linkup was designed from the ground up to be the most accurate search engine for AIs. This makes Linkup [score higher](https://www.linkup.so/blog/linkup-establishes-sota-performance-on-simpleqa) on OpenAI’s factuality benchmark SimpleQA.
    * To that end, Linkup has made partnerships with trusted data providers and premium information sources, ensuring our customers can make critical business decisions based on Linkup’s answers.
    * In addition, Linkup is hyper focused on the needs of our users: AI Agents and technology systems,  vs. humans. For example, this means we can provide raw context or structured outputs, vs. natural language answers only.
  </Accordion>

  <Accordion title="What is the difference between Standard and Deep?">
    * **Standard**: Fast and affordable web search. Linkup Standard is great for quickly finding straightforward grounding data that improves the accuracy of your AI. Try queries such as “What is Microsoft’s Q3 2024 revenue?”. Standard queries cost 5 euros per 1,000 queries.
    * **Deep**: Comprehensive, in-depth web search. Linkup Deep handles complex queries that require digging, multi-steps information gathering and reflection. Try queries such as “What are the differences in strategy between Apple and Samsung for 2025?”. Deep queries cost 50 euros per 1,000 queries.
  </Accordion>

  <Accordion title="How can I stay up to date with changes to the API?">
    We post key changes to the API on our [Changelog](../../pages/changelog/). We also discuss them on our [Discord](https://discord.gg/HHv29dPa) and on [X](https://x.com/Linkup_platform).
  </Accordion>

  <Accordion title="I have an issue with Linkup, how can I get some help?">
    You can send us an email at [support@linkup.so](mailto:support@linkup.so) or ask us directly on [Discord](https://discord.gg/HHv29dPa).
  </Accordion>

  <Accordion title="Which AI models is Linkup using?">
    Linkup leverages a range of state-of-the-art AI models across its tech stack, continuously optimizing for accuracy, speed, and relevance. To power our search, we've developed a proprietary model designed specifically for high-precision retrieval and business intelligence.
  </Accordion>

  <Accordion title="ModuleNotFoundError or import errors after installing linkup?">
    If you get this type of error, make sure you have installed the correct package:

    `pip install linkup-sdk`

    You can reach out to [support@linkup.so](mailto:support@linkup.so) if you still experience issues.
  </Accordion>
</AccordionGroup>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Agno
Source: https://docs.linkup.so/pages/integrations/agno/agno

How to use Linkup with Agno

## Overview

Linkup can be integrate with [Agno](https://www.agno.com) as a tool to provide real-time web search capabilities to your Agno AI agents.

## Installation

<Steps>
  <Step title="Set Up API Key">
    1. Get your Linkup API Key:
       <Card title="Get your API key" icon="key" href="https://app.linkup.so">
         Create a Linkup account for free to get your API key.
       </Card>

    2. Set the API key in your environment:
       ```shell theme={null}
       export LINKUP_API_KEY=your_api_key_here
       ```
  </Step>

  <Step title="Install Linkup SDK">
    1. Install the Linkup SDK using pip:
       ```shell theme={null}
       pip install linkup-sdk
       ```
  </Step>

  <Step title="Install Agno">
    1. Install Agno using pip:
       ```shell theme={null}
       pip install agno
       ```
  </Step>
</Steps>

## Example Usage

The following agent will search the web for the latest news in French politics and print the response.

```python python theme={null}
    from agno.agent import Agent
    from agno.tools.linkup import LinkupTools

    agent = Agent(tools=[LinkupTools()], show_tool_calls=True)
    agent.print_response("What's the latest news in French politics?", markdown=True)
```

## Toolkit Functions

| Function                 | Description                                                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `web_search_with_linkup` | Searches the web for a query using Linkup API. Takes a query string and optional depth/output\_type parameters. Returns search results as a string. |

## Toolkit Parameters

| Parameter     | Type                                        | Default           | Description                                                                                                                                                                                                       |
| ------------- | ------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`     | `Optional[str]`                             | `None`            | API key for authentication. If not provided, will check LINKUP\_API\_KEY environment variable.                                                                                                                    |
| `depth`       | `Literal["standard", "deep"]`               | `"standard"`      | Depth of the search. Use 'standard' for fast and affordable web search or 'deep' for comprehensive, in-depth web search.                                                                                          |
| `output_type` | `Literal["sourcedAnswer", "searchResults"]` | `"searchResults"` | Type of output. 'sourcedAnswer' provides a comprehensive natural language answer to the query along with citations to the source material. 'searchResults' returns the raw search context data without synthesis. |

You are now ready to use Linkup in Agno as a tool for your agents !

<Tip>
  You can check the [Agno documention](https://docs.agno.com/introduction/agents) for more information about agents and tools.
</Tip>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Baseten
Source: https://docs.linkup.so/pages/integrations/baseten/baseten

Use Linkup as a real-time web search tool for models served on Baseten's serverless inference platform

Baseten provides serverless GPU inference for open-source models with no infrastructure to manage. With Linkup, you can ground these models in real-time web data, giving them the ability to retrieve current facts, news, and source-backed information beyond their training data.

This guide demonstrates the integration using GPT-OSS 120B, but the same approach works with any model available on Baseten that supports function calling.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Baseten API key" icon="key" href="https://app.baseten.co/settings/api-keys">
        Navigate to your Baseten settings, select API Keys, click Create API key, and copy the generated key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Set Up Your Environment">
    Initialize your project and create a virtual environment:

    ```bash theme={null}
    mkdir baseten-linkup
    cd baseten-linkup
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

    Install dependencies:

    ```bash theme={null}
    pip install openai linkup-sdk
    ```

    Configure your API keys as environment variables:

    <CodeGroup>
      ```bash Mac / Linux theme={null}
      export BASETEN_API_KEY=paste_your_baseten_key_here
      export LINKUP_API_KEY=paste_your_linkup_key_here
      ```

      ```bash Windows theme={null}
      set BASETEN_API_KEY=paste_your_baseten_key_here
      set LINKUP_API_KEY=paste_your_linkup_key_here
      ```
    </CodeGroup>
  </Step>

  <Step title="Build the Agent">
    Create a file named `agent.py` and add the following code:

    ```python agent.py theme={null}
    import os
    import json
    from datetime import datetime
    from openai import OpenAI
    from linkup import LinkupClient

    client = OpenAI(
        api_key=os.environ.get("BASETEN_API_KEY"),
        base_url="https://inference.baseten.co/v1"
    )
    linkup_client = LinkupClient(api_key=os.environ.get("LINKUP_API_KEY"))

    tools = [{
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web in real time. Use this tool whenever the user needs trusted facts, news, or source-backed information. Returns comprehensive content from the most relevant sources.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }]

    def main():
        print("--- GPT-OSS 120B + Linkup ---")
        print("Type 'quit' to exit.\n")

        today_str = datetime.now().strftime("%B %d, %Y")
        system_prompt = (
            f"You are a helpful assistant. Today is {today_str}. "
            f"Use web search when you need current information. "
            f"Prefer searching over relying on your training data for anything that could be outdated."
        )

        history = [{"role": "system", "content": system_prompt}]

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["quit", "exit"]:
                    print("Goodbye!")
                    break

                history.append({"role": "user", "content": user_input})

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=history,
                    tools=tools,
                    tool_choice="auto"
                )
                message = response.choices[0].message

                while message.tool_calls:
                    history.append(message)
                    for tc in message.tool_calls:
                        q = json.loads(tc.function.arguments)["query"]
                        print(f"Searching using Linkup: {q}...")
                        try:
                            result = linkup_client.search(
                                query=q,
                                depth="standard",
                                output_type="searchResults"
                            )
                            content = "\n\n".join(
                                f"{r.name}\n{r.url}\n{r.content}"
                                for r in result.results
                            )
                        except Exception as e:
                            content = f"Search error: {e}"
                        history.append({
                            "role": "tool",
                            "tool_call_id": tc.id,
                            "content": content
                        })

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=history,
                        tools=tools,
                        tool_choice="auto"
                    )
                    message = response.choices[0].message

                print(f"Agent: {message.content}\n")
                history.append(message)

            except Exception as e:
                print(f"Error: {e}")

    if __name__ == "__main__":
        main()
    ```
  </Step>

  <Step title="Run the Agent">
    ```bash theme={null}
    python agent.py
    ```
  </Step>

  <Step title="Try Different Scenarios">
    **Internal knowledge (no tool call):**

    ```
    You: What is the definition of philosophy?
    Agent: Philosophy is the study of fundamental questions about existence,
           knowledge, values, reason, mind, and language...
    ```

    **Tool-augmented reasoning:**

    ```
    You: What are the latest books published on logic?
    Searching using Linkup: latest logic books 2025...
    Agent: Synthesizes a response citing recent publications found via Linkup.
    ```
  </Step>
</Steps>

For more information, visit:

* [Baseten Documentation](https://docs.baseten.co/)

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Cerebras
Source: https://docs.linkup.so/pages/integrations/cerebras

Use Linkup as a real-time web search tool for models served on Cerebras' ultra-fast inference platform

Cerebras provides ultra-fast inference (3,000+ tokens/sec) for open-source models. With Linkup, you can ground these models in real-time web data, giving them the ability to retrieve current facts, news, and source-backed information beyond their training data.

This guide demonstrates the integration using GPT-OSS 120B, but the same approach works with any model available on Cerebras that supports function calling.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Cerebras API key" icon="key" href="https://cloud.cerebras.ai/">
        Create a Cerebras account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install and Setup">
    Install the required packages:

    ```bash theme={null}
    pip install linkup-sdk cerebras-cloud-sdk
    ```

    Set up your clients:

    ```python theme={null}
    from cerebras.cloud.sdk import Cerebras
    from linkup import LinkupClient
    import json
    from datetime import datetime

    cerebras_client = Cerebras(api_key="your_cerebras_api_key")
    linkup_client = LinkupClient(api_key="your_linkup_api_key")
    ```
  </Step>

  <Step title="Define the Function Schema">
    Tell Cerebras about your search function:

    ```python theme={null}
    tools = [{
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for current information. Returns comprehensive content from relevant sources.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }]
    ```
  </Step>

  <Step title="Build the Chatbot">
    Put it all together in a conversational loop:

    ```python theme={null}
    system_prompt = f"You are a helpful assistant. Today is {datetime.now().strftime('%B %d, %Y')}. Use web search when you need current information."
    messages = [{"role": "system", "content": system_prompt}]

    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = cerebras_client.chat.completions.create(
                model="gpt-oss-120b",
                messages=messages,
                tools=tools
            )

            message = response.choices[0].message

            while message.tool_calls:
                messages.append(message)
                for tool_call in message.tool_calls:
                    args = json.loads(tool_call.function.arguments)
                    print(f"Searching with Linkup: {args['query']}...")
                    linkup_response = linkup_client.search(
                        query=args["query"],
                        depth="standard",
                        output_type="searchResults"
                    )
                    search_results = json.dumps(
                        [{"content": r.content} for r in linkup_response.results]
                    )
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": search_results
                    })

                response = cerebras_client.chat.completions.create(
                    model="gpt-oss-120b",
                    messages=messages,
                    tools=tools
                )
                message = response.choices[0].message

            print(f"\nAssistant: {message.content}\n")
            messages.append({"role": "assistant", "content": message.content})

        except Exception as e:
            print(f"Error: {e}\n")
            messages.pop()
    ```
  </Step>
</Steps>

For more information, visit:

* [Cerebras Inference Documentation](https://inference-docs.cerebras.ai/)

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Chainlit Chatbot
Source: https://docs.linkup.so/pages/integrations/chatbot/build-your-chatbot

Connect your Chainlit chatbot to the internet with Linkup

<img alt="Search the Web" />

Linkup is natively integrated in [Chainlit](https://docs.chainlit.io), an open-source Python framework specifically designed for building production-ready Conversational AI applications. You can now deploy an open source chatbot with "search the web" capabilities, in minutes.

This chatbot will feature:

* Real-time web search using Linkup
* A web interface with Chainlit, supporting conversation context management and message streaming

## Implementation Guide

<Steps>
  <Step title="Get Started with Chainlit">
    Follow the Chainlit documentation to set up your chatbot application. Visit the [Chainlit getting started guide](https://docs.chainlit.io/get-started/overview) to learn the basics of creating a Chainlit application. This will require [an Anthropic API key](https://docs.anthropic.com/en/api/admin-api/apikeys/get-api-key) or an API key from any LLM provider.
  </Step>

  <Step title="Integrate Linkup">
    Add web search capabilities to your Chainlit app by following the very simple integration steps in the [Chainlit cookbook](https://github.com/Chainlit/cookbook/tree/main/ai-web-search-linkup). This will enable your chatbot to perform real-time web searches using Linkup. This will require a Linkup API key.

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Claude Desktop
Source: https://docs.linkup.so/pages/integrations/claude





# Clay
Source: https://docs.linkup.so/pages/integrations/clay/clay

Enrich Companies in Clay using Linkup Web Search

## Overview

You can connect a [Clay](https://clay.com) table to web search through Linkup, which can be used as an enrichment provider to get contextual information from the internet for your prospects and leads.

Below is a short Youtube Tutorial:

<iframe title="Install Linkup on Google Sheets" />

## Installation

### 1. Open Clay

Go to your Clay account and navigate to the table you would like to enrich.

<img alt="Clay" />

### 2. Add HTTP API Enrichment

Click on "Add enrichment" and search for HTTP API.

<img alt="Clay" />

<img alt="Clay" />

### 3. Configure the HTTP API to call the Linkup API

After clicking on HTTP API, you will see the configuration sidebar opening.

<img alt="Clay" />

There are a few things we'll need to configure:

* **Endpoint & Header** (think of it as the address and name you would put on an envelope)
* **Body** (the actual content of the letter)

Let's first configure the *HTTP API (Headers) account* - this is how Linkup will authenticate you. In the *Account* section, select "Add account". You will see a box popping up, where you need to add two key/value pairs:

* `Authorization` / `Bearer {your API key}`
* `Content-Type` / `application/json`

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

<img alt="Clay" />

Once this is done, we'll configure the Method, Endpoint and Body.

To find the endpoint, head over to the [API Reference](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-search). You'll see the endpoint url is `https://api.linkup.so/v1/search`, using a the *POST* Method.

Then for the Body, you need to send the query parameters of the API (see the [API Reference](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-search) for more details on output type, filters, and depth).

You can copy the configuration below, replacing "q" with your actual query:

```json theme={null}
{
  "q": "your search query here",
  "outputType": "sourcedAnswer",
  "depth": "standard"
}
```

<img alt="Clay" />

### 4. Call the API and create a new column for the results

You can then save and run the column directly from the table.

**Important**: This column will not get you the enriched data directly, but shows the API response. You need to open the API response and create a new column based on the field "answer", which is included in the response.

<img alt="Clay" />

You now have your enrichment working!

### 5. Save the enrichment as a template and reuse it with different queries

If you open the configuration panel of the HTTP API call, you can save the parameters as a new template, and then re-use this template in new columns. All you will have to change is your query.

<img alt="Clay" />\\

<img alt="Clay" />

## Use Cases

**Company Intelligence & Research**

* Research any company based on its website or public information
* Find detailed information about customers, job positions, office locations
* Discover funding stages, technology stacks, and SOC-II compliance status
* Analyze competitive landscape and market positioning

**Lead Qualification & Scoring**

* Automate the research process to identify highly-qualified leads
* Gather contextual information that helps prioritize prospects
* Filter leads based on your ideal customer profile (ICP) criteria

**Sales Intelligence & Pre-call Research**

* Automatically gather facts about companies and contacts before sales calls
* Replace manual Googling with automated research
* Create more confident, relevant conversations with prospects

**Account-Based Marketing (ABM) Research**

* Find companies of particular sizes that use specific technologies
* Identify prospects that aren't in your CRM yet
* Expand your total addressable market (TAM) with targeted research

**Contact & Email Discovery**

* Obtain valid email addresses and contact information
* Research across various platforms and public sources
* Automate contact discovery in one streamlined process

**Competitor Analysis & Market Research**

* Analyze competitors and their market positioning
* Research industry trends and market opportunities
* Gather intelligence to inform your sales strategy

**Signal & Trigger Detection**

* Track key customer events and buying signals
* Monitor company changes like hiring sprees or funding announcements
* Identify technology adoptions that indicate sales opportunities

**Customer Success & Expansion Research**

* Research existing customers to identify expansion opportunities
* Analyze renewal risks and success patterns
* Monitor public activities and business changes for upsell signals

You are all set to use Linkup in your Clay workflows! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Composio
Source: https://docs.linkup.so/pages/integrations/composio/composio

How to use Linkup in Composio

## Overview

Linkup can be used with [Composio](https://composio.dev) as a Tool to get contextual information from the internet. This integration allows your Composio workflows to search the web and incorporate up-to-date information.

## Setting Up Linkup in Composio

<Steps>
  <Step title="Access your Composio account">
    Log in to your Composio account at [composio.dev](https://composio.dev).
  </Step>

  <Step title="Find and select the Linkup tool">
    Navigate to the All Apps section in Composio and search for "Linkup".

    <img alt="Search for tools in Composio" />

    <img alt="Search results showing Linkup" />
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Configure the integration">
    Click on "Setup Linkup integration".

    <img alt="Setup Linkup integration" />

    Enter your Linkup API Key in the provided field and click on "Try connecting default's linkup".

    <img alt="Enter your API key" />
  </Step>
</Steps>

## Example with Composio and CrewAI

Composio gives you the ability to build with CrewAI, a powerful agentic framewwork.

<Steps>
  <Step title="Install required packages">
    ```bash theme={null}
    pip install crewai langchain_openai composio_crewai
    ```
  </Step>

  <Step title="Get your API keys">
    You'll need:

    1. Your Composio API key
    2. An OpenAI API key (get one [here](https://openai.com/index/openai-api/))
  </Step>

  <Step title="Create your CrewAI script">
    Create a new Python file and add the following code:

    ```python theme={null}
    from crewai import Agent, Task, Crew
    from langchain_openai import ChatOpenAI
    from composio_crewai import ComposioToolSet, Action, App

    # Initialize Composio toolset with your API key
    composio_toolset = ComposioToolSet(api_key="YOUR_COMPOSIO_API_KEY")

    # Get the Linkup search tool
    tools = composio_toolset.get_tools(actions=['LINKUP_PERFORM_A_SEARCH_QUERY'])

    # Create a CrewAI agent with the Linkup tool
    crewai_agent = Agent(
        role="Research Assistant",
        goal="""You analyze information and provide accurate answers based on 
                web searches using the Linkup tool.""",
        backstory=(
            "You are an AI research assistant that helps users find accurate and 
             up-to-date information from the web."
        ),
        verbose=True,
        tools=tools,
        llm=ChatOpenAI(api_key="YOUR_OPENAI_API_KEY"),
    )

    # Create a task for the agent
    task = Task(
        description="Can you tell me which women were awarded the Physics Nobel Prize",
        agent=crewai_agent,
        expected_output="A comprehensive list of female Nobel Physics Prize winners with years"
    )

    # Create and run the crew
    my_crew = Crew(agents=[crewai_agent], tasks=[task])
    result = my_crew.kickoff()

    # Print the result
    print(result)
    ```

    Be sure to replace `YOUR_COMPOSIO_API_KEY` and `YOUR_OPENAI_API_KEY` with your actual API keys.
  </Step>

  <Step title="Run your script">
    Execute your Python script:

    ```bash theme={null}
    python your_script.py
    ```

    The script will use the Linkup tool through Composio to search for information about female Nobel Physics Prize winners and return the results.

    **Example Response**

    ```
    Four women have been awarded the Nobel Prize in Physics:

    1. Marie Curie (1903) - Awarded for her research on radiation phenomena
    2. Maria Goeppert Mayer (1963) - Awarded for discoveries concerning nuclear shell structure
    3. Donna Strickland (2018) - Awarded for groundbreaking inventions in laser physics
    4. Andrea Ghez (2020) - Awarded for the discovery of a supermassive compact object at the center of our galaxy

    Marie Curie was the first woman to win a Nobel Prize in any category and remains the only woman to win Nobel Prizes in two different scientific fields (Physics in 1903 and Chemistry in 1911).
    ```

    **Advanced Usage**

    You can expand your CrewAI agents to use additional Linkup capabilities by specifying different actions in the `get_tools()` function:

    ```python theme={null}
    # Get multiple Linkup tools
    tools = composio_toolset.get_tools(actions=[
        'LINKUP_PERFORM_A_SEARCH_QUERY', 
        'LINKUP_PERFORM_A_DEEP_SEARCH_QUERY'
    ])
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# CrewAI
Source: https://docs.linkup.so/pages/integrations/crewai

Use Linkup as a web search tool with CrewAI multi-agent systems

CrewAI is a cutting-edge framework for orchestrating role-playing, autonomous AI agents. By working together, these agents can tackle complex tasks more effectively than working alone. Linkup provides real-time web search capabilities that can be integrated with CrewAI agents, enabling them to access current information and perform research tasks with accurate citations.

<Card title="CrewAI LinkupSearchTool Documentation" href="https://docs.crewai.com/en/tools/search-research/linkupsearchtool">
  Visit the CrewAI documentation to learn how to integrate Linkup's search capabilities into your multi-agent workflows.
</Card>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Dify
Source: https://docs.linkup.so/pages/integrations/dify/dify

Integrate Linkup with Dify to enhance your AI workflows

## Overview

Linkup can be integrated with [Dify](https://dify.ai) as a tool to provide real-time web search capabilities to your AI applications. This integration allows your Dify agents to access up-to-date information from the internet.

## Installation

<Steps>
  <Step title="Install Linkup Plugin">
    1. Log in to your Dify account

    2. Install the Linkup Plugin from the [Marketplace](https://marketplace.dify.ai/plugins/linkup/search-web)

       <img alt="Dify Marketplace" />

    3. Click "Install" to add it to your workspace

       <img alt="Install Plugin" />
  </Step>

  <Step title="Authorize Linkup">
    1. After installation, click on "Authorize" to set up the plugin

       <img alt="Authorize Plugin" />

    2. Get your Linkup API Key:

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    3. Enter your API key in the authorization page

       <img alt="API Key Authorization" />
  </Step>

  <Step title="Add Linkup to Agent">
    1. Go to your Dify application
    2. Navigate to the Tools section
    3. Add Linkup as a tool to your agent

       <img alt="Agent Tool" />
  </Step>

  <Step title="Configure Tool Settings">
    1. Access the tool settings for Linkup

    2. Configure the search parameters according to your needs

       <img alt="Tool Settings" />

    3. Select the appropriate search depth for your use case

       <img alt="Tool Depth Selection" />
  </Step>

  <Step title="Other Uses in Dify">
    You can also use it in workflows, chatbots, chatflows, ..
    Example of Linkup being used in a workflow:

    <img alt="Tool Workflow" />

    <img alt="Workflow Example" />
  </Step>
</Steps>

You are now ready to use Linkup in your Dify applications! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters and how to optimize your searches.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# FriendliAI
Source: https://docs.linkup.so/pages/integrations/friendliai/friendliai

Use Linkup as a web search tool for LLMs served by FriendliAI

FriendliAI provides fast, efficient and reliable AI inference. Linkup provides real-time web search capabilities that can be seamlessly integrated with models served by FriendliAI. This combination allows your AI applications to access up-to-date information beyond the model's training data, enabling you to create applications that retrieve current facts, information, and events with accurate citations.

## FriendliAI's Playground

Linkup's web search can be turned on directly in FriendliAI's API playground.

<img alt="Playground" />

## FriendliAI's API Integitgration

Linkup's web search can be integrated as a default tool in calls made to the FriendliAI serverless APIs, simply by adding `"tools": [{ "type": "linkup:search" }]` in your OpenAI format API call.

To that end, follow these steps:

<Steps>
  <Step title="Create your FriendliAI account">
    Create a new [FriendliAI account](https://friendli.ai/) if you don't have one yet.
  </Step>

  <Step title="Subscribe to the free trial">
    You need to enroll in the Serverless Endpoints product free trial. Information can be found [here](https://friendli.ai/docs/guides/free_credits?_gl=1*12pdpy8*_gcl_au*MTMwNDY4MzczNS4xNzU1MDc1NDA5#receiving-when-you-start).
  </Step>

  <Step title="Add your Linkup API key to your FriendliAI account">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    In Friendli Suite, open Personal settings > Integrations and add your Linkup API key.
  </Step>

  <Step title="Make your first API call">
    In the following code snippet, `FRIENDLI_TOKEN` refers to your Personal Access Token, which you can obtain from Personal settings > Settings > Tokens [(guide)](https://friendli.ai/docs/guides/personal_access_tokens?_gl=1*bqbtwa*_gcl_au*MTMwNDY4MzczNS4xNzU1MDc1NDA5).
    <Note>Make sure your Linkup integration is enabled in your Friendli account before calling the API — otherwise the `linkup:search` tool will error.</Note>

    <CodeGroup>
      ```python python theme={null}
      import os
      from openai import OpenAI

      client = OpenAI(
          api_key=os.getenv("FRIENDLI_TOKEN"),
          base_url="https://api.friendli.ai/serverless/tools/v1",
      )

      completion = client.chat.completions.create(
          model="meta-llama-3.1-8b-instruct",
          messages=[
              {
                  "role": "user",
                  "content": "Find information on the popular movies currently showing in theaters and provide their ratings."
              }
          ],
          tools=[{"type": "linkup:search"}],
          stream=False
      )

      print(completion.choices[0].message.content)
      ```

      ```shell curl theme={null}
      curl --request POST \
        --url https://api.friendli.ai/serverless/tools/v1/chat/completions \
        --header 'Authorization: Bearer <FRIENDLI_TOKEN>' \
        --header 'Content-Type: application/json' \
        --data '{
          "model": "meta-llama-3.1-8b-instruct",
          "messages": [
            {
              "content": "Find information on the popular movies currently showing in theaters and provide their ratings.",
              "role": "user"
            }
          ],
          "tools": [
            { "type": "linkup:search" }
          ]
        }'
      ```
    </CodeGroup>
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Google Sheet
Source: https://docs.linkup.so/pages/integrations/google-sheet/google-sheet

How to use Linkup in Google Sheet

## Overview

Linkup can be used with [GoogleSheet](https://docs.google.com/spreadsheets) as a Formula to get contextual information from the internet.

<img alt="Linkup Search" />

## Installation

The Linkup Google Sheets app is available on the Google Workspace Marketplace. The short video below shows you how to install it in a few clicks.

In the installation, you will need a Linkup API key.

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

*

<iframe title="Install Linkup on Google Sheets" />

<Warning>Refreshing the sheet or modifying your formula will re-launch the queries made to Linkup. If you are happy with your answers and don't want the cells to refresh ever, you can avoid any mistakes by copying the cells and pasting "values only".</Warning>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Huggingface
Source: https://docs.linkup.so/pages/integrations/huggingface

How to use Linkup with Huggingface

## Overview

Linkup can be used with [Huggingface](https://huggingface.co/docs/smolagents/en/index) (smolagents) to create advanced AI agents and workflows based on internal and web data.

## Getting Started with Linkup in Huggingface

<Steps>
  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Install dependencies">
    ```shell theme={null}
    pip install linkup-sdk smolagents openai
    ```
  </Step>

  <Step title="Create your agent">
    ```python theme={null}
    from smolagents import CodeAgent, load_tool
    from smolagents.models import OpenAIServerModel

    linkup_tool = load_tool("Linkup-Platform/linkup-search-tool", trust_remote_code=True)
    ```
  </Step>

  <Step title="Initialize and run your agent">
    ```python theme={null}
    # Agent initialization
    agent = CodeAgent(
        tools=[linkup_tool],
        model=OpenAIServerModel(
          model="gpt-4o-mini",
          api_key="your_openai_api_key"
        ),
    )
    # Agent invocation
    response = agent.run("What was Microsoft's revenue last quarter and was it well perceived by the market?")
    print(response)
    ```
  </Step>
</Steps>

## Example Response

```
Microsoft's revenue last quarter (3Q2024) was approximately $65.59 billion. The market's perception is mixed; while many analysts are optimistic about growth fueled by AI and cloud services, 
there are concerns regarding a lack of guidance in their report, leading to a cautious reaction from some investors.
```

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Integrations
Source: https://docs.linkup.so/pages/integrations/integrations

How to integrate Linkup in your application.

There are a few different ways to integrate Linkup in your application, depending on your stack and personal preference.

<CardGroup>
  <Card title="MCP" icon="server" href="/pages/integrations/mcp/mcp">
    Integrate with the Linkup MCP server
  </Card>

  <Card title="LLM Function Calling" icon="microchip-ai" href="/pages/integrations/linkup-mistral">
    Integrate with LLMs via function calling
  </Card>

  <Card title="Agentic Frameworks" icon="arrow-progress" href="/pages/integrations/langchain">
    Use your favorite orchestration framework
  </Card>

  <Card title="Workflows" icon="diagram-nested" href="/pages/integrations/zapier/zapier">
    Plug-in your preferred automation tool
  </Card>

  <Card title="Google Sheets" icon="file-spreadsheet" href="/pages/integrations/google-sheet/google-sheet">
    Use Linkup as a Google Sheets function
  </Card>

  <Card title="Lovable" icon="heart" href="/pages/integrations/lovable/lovable">
    Connect your Lovable app to the internet
  </Card>
</CardGroup>


# Keywords AI
Source: https://docs.linkup.so/pages/integrations/keywordsai

How to use Keywords AI with Linkup to call 300+ LLMs and get LLM observability

[Keywords AI](https://www.keywordsai.co) is an LLM engineering platform that allows you to do monitoring, prompt management, and LLM evals.

This tutorial will show you how to set up Linkup in the Keywords AI API payload to monitor LLM performance and usage.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Keywords AI API key" icon="key" href="https://docs.keywordsai.co/get-started/overview">
        Create a Keywords AI account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Build the Keywords AI request">
    ```python Python {24-30} theme={null}
    import requests

    def demo_call(
        company,
        model="gpt-4o-mini",
        token="KEYWORDSAI_API_KEY"
    ):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        data = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "What is " + company + "'s 2024 revenue? Base your answer on the following trusted data: \n\n{% if linkup_search_response %}{{ linkup_search_response.results }}{% else %}I don't have that information.{% endif %}}"
                }
            ],
            "linkup_params": {
                "apiKey": "LINKUP_API_KEY",
                "q": "What is " + company + "'s 2024 revenue?",
                "depth": "deep",
                "outputType": "searchResults",
                "includeImages": False
            },
            "model": "gpt-4o-mini"
        }

        response = requests.post('https://api.keywordsai.co/api/chat/completions', headers=headers, json=data)
        return response

    input_text = "Microsoft"
    response = demo_call(input_text)
    print(response.json())
    ```

    You can also use prompt templates as follows:

    ```python theme={null}
    Please provide information about {{ company_name }}'s 2024 revenue and cite your sources.

    {% if linkup_search_response %}
      Here's what I found:
      {{ linkup_search_response.answer }}

      Sources:
      {% for source in linkup_search_response.sources %}
      - {{ source.name }}: {{ source.url }}
      {% endfor %}
    {% endif %}

    ```
  </Step>

  <Step title="Monitor LLM performance and usage">
    After you set up the environment and run the request, you can see [LLM logs](https://platform.keywordsai.co/platform/requests?sort_by=-timestamp) in Keywords AI.

    <img alt="LLM logging" />
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Langchain
Source: https://docs.linkup.so/pages/integrations/langchain

How to use Linkup with our Langchain SDK

## Overview

Linkup can be used with [LangChain](https://www.langchain.com/) as a [Retriever](https://python.langchain.com/api_reference/core/retrievers.html). This integration allows you to build powerful applications that retrieve contextual information from the internet.

## Getting Started with Linkup in LangChain

<Steps>
  <Step title="Install the LangChain integration">
    ```shell theme={null}
    pip install langchain-linkup
    ```
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Create and use the Linkup Retriever">
    ```python theme={null}
    from langchain_linkup import LinkupSearchRetriever
    import os

    os.environ["LINKUP_API_KEY"] = "PASTE_YOUR_API_KEY_HERE"

    retriever = LinkupSearchRetriever(
    depth="deep",  # "standard" or "deep"
    )

    # Perform a search query
    documents = retriever.invoke(input="What is Linkup, the new French AI startup?")
    print(documents)
    ```

    <Info>
      <table>
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Options</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td><code>depth</code></td>
            <td><code>standard</code>, <code>deep</code></td>
            <td>Controls search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
          </tr>

          <tr>
            <td><code>output\_type</code></td>
            <td><code>searchResults</code>, <code>sourcedAnswer</code>, <code>structured</code></td>
            <td>Determines the format of returned information.</td>
          </tr>
        </tbody>
      </table>
    </Info>
  </Step>
</Steps>

## Example Project: RAG Pipeline with OpenAI

<Steps>
  <Step title="Install dependencies">
    ```shell theme={null}
    pip install langchain-openai python-dotenv
    ```
  </Step>

  <Step title="Set up API keys">
    <Info>
      You need API keys for both Linkup and OpenAI. You can get an OpenAI API key [here](https://openai.com/index/openai-api/).
    </Info>

    ```python theme={null}
    import os
    from dotenv import load_dotenv

    # Load from .env file if available
    load_dotenv()

    # Or set manually
    os.environ["LINKUP_API_KEY"] = "YOUR_LINKUP_API_KEY"
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    ```
  </Step>

  <Step title="Create the RAG pipeline">
    ```python theme={null}
    from typing import Any, Literal
    from langchain_core.documents import Document
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough
    from langchain_openai import ChatOpenAI
    from langchain_linkup import LinkupSearchRetriever

    # Configuration
    query: str = "What is Linkup, the new French AI startup?"
    linkup_depth: Literal["standard", "deep"] = "standard"
    open_ai_model: str = "gpt-4o-mini"

    # Initialize retriever
    retriever = LinkupSearchRetriever(depth=linkup_depth)

    # Format documents helper function
    def format_retrieved_documents(docs: list[Document]) -> str:
        return "\n\n".join(
            [
                f"{document.metadata['name']} ({document.metadata['url']}):\n{document.page_content}"
                for document in docs
            ]
        )

    # Debug helper function
    def inspect_context(state: dict[str, Any]) -> dict[str, Any]:
        print(f"Context: {state['context']}\n\n")
        return state

    # Create prompt and model
    generation_prompt_template = """Answer the question based only on the following context:

    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(generation_prompt_template)
    model = ChatOpenAI(model=open_ai_model)
    ```
  </Step>

  <Step title="Run the pipeline">
    ```python theme={null}
    # Build and execute the chain
    chain: Runnable[Any, str] = (
        {"context": retriever | format_retrieved_documents, "question": RunnablePassthrough()}
        | RunnableLambda(inspect_context)
        | prompt
        | model
        | StrOutputParser()
    )

    # Get response
    response = chain.invoke(input=query)
    print(f"Response: {response}")
    ```

    **Example Response**

    ```
    Context: Linkup (https://www.linkup.fr):
    Linkup is a French AI startup that provides a search API for LLMs, enabling them to search the web and access up-to-date information.

    Response: Linkup is a French AI startup that has developed a search API specifically designed for Large Language Models (LLMs). Their technology allows LLMs to search the web and access current information, which helps overcome the limitation of outdated training data that many AI models face. This enables applications built with LLMs to provide more accurate and up-to-date responses by connecting them to real-time information from the internet.
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Linkup + Claude
Source: https://docs.linkup.so/pages/integrations/linkup-claude

Use Claude's function calling capabilities to integrate with Linkup

This tutorial shows you how to use Claude's function calling with Linkup to build a chatbot with real-time web search capabilities.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Anthropic API key" icon="key" href="https://console.anthropic.com/settings/keys">
        Create an Anthropic account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install and Setup">
    Install the required packages:

    ```bash theme={null}
    pip install linkup-sdk anthropic
    ```

    Set up your clients:

    ```python theme={null}
    import anthropic
    from linkup import LinkupClient
    import json
    from datetime import datetime

    claude_client = anthropic.Anthropic(api_key="your_anthropic_api_key")
    linkup_client = LinkupClient(api_key="your_linkup_api_key")
    ```
  </Step>

  <Step title="Define the Function Schema">
    Tell Claude about your search function:

    ```python theme={null}
    tools = [{
        "name": "search_web",
        "description": "Search the web in real time. Use this tool whenever the user needs trusted facts, news, or source-backed information. Returns comprehensive content from the most relevant sources.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }]
    ```
  </Step>

  <Step title="Build the Chatbot">
    Put it all together in a conversational loop that supports multiple and chained tool calls:

    ```python theme={null}
    system_prompt = (
        f"You are a helpful assistant. Today is {datetime.now().strftime('%B %d, %Y')}. "
        f"Use web search when you need current information."
    )
    messages = []

    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = claude_client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                system=system_prompt,
                messages=messages,
                tools=tools
            )

            while response.stop_reason == "tool_use":
                tool_calls = [block for block in response.content if block.type == "tool_use"]

                tool_results = []
                for tool_use in tool_calls:
                    print(f"Searching with Linkup: {tool_use.input['query']}...")
                    linkup_response = linkup_client.search(
                        query=tool_use.input["query"],
                        depth="standard",
                        output_type="searchResults"
                    )
                    search_results = json.dumps(
                        [{"content": r.content} for r in linkup_response.results]
                    )
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tool_use.id,
                        "content": search_results
                    })

                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})

                response = claude_client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=1000,
                    system=system_prompt,
                    messages=messages,
                    tools=tools
                )

            text = next(
                (block.text for block in response.content if hasattr(block, "text")),
                None
            )
            if text:
                print(f"\nAssistant: {text}\n")

            messages.append({"role": "assistant", "content": response.content})

        except Exception as e:
            print(f"Error: {e}\n")
            messages.pop()
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Linkup + Mistral
Source: https://docs.linkup.so/pages/integrations/linkup-mistral

Use Mistral AI's function calling capabilities to integrate with Linkup

This tutorial shows you how to use Mistral AI's function calling with Linkup to build a chatbot with real-time web search capabilities.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Mistral API key" icon="key" href="https://console.mistral.ai/api-keys/">
        Create a Mistral AI account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install and Setup">
    Install the required packages:

    ```bash theme={null}
    pip install linkup-sdk mistralai
    ```

    Set up your clients:

    ```python theme={null}
    from mistralai import Mistral
    from linkup import LinkupClient
    import json
    from datetime import datetime

    mistral_client = Mistral(api_key="your_mistral_api_key")
    linkup_client = LinkupClient(api_key="your_linkup_api_key")
    ```
  </Step>

  <Step title="Define the Function Schema">
    Tell Mistral about your search function:

    ```python theme={null}
    tools = [{
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for current information. Returns comprehensive content from relevant sources.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }]
    ```
  </Step>

  <Step title="Build the Chatbot">
    Put it all together in a conversational loop:

    ```python theme={null}
    system_prompt = f"You are a helpful assistant. Today is {datetime.now().strftime('%B %d, %Y')}. Use web search when you need current information."
    messages = [{"role": "system", "content": system_prompt}]

    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = mistral_client.chat.complete(
                model="mistral-large-latest",
                messages=messages,
                tools=tools
            )

            message = response.choices[0].message

            while message.tool_calls:
                messages.append(message)
                for tool_call in message.tool_calls:
                    args = json.loads(tool_call.function.arguments)
                    print(f"Searching with Linkup: {args['query']}...")
                    linkup_response = linkup_client.search(
                        query=args["query"],
                        depth="standard",
                        output_type="searchResults"
                    )
                    search_results = json.dumps(
                        [{"content": r.content} for r in linkup_response.results]
                    )
                    messages.append({
                        "role": "tool",
                        "name": "search_web",
                        "content": search_results,
                        "tool_call_id": tool_call.id
                    })

                response = mistral_client.chat.complete(
                    model="mistral-large-latest",
                    messages=messages,
                    tools=tools
                )
                message = response.choices[0].message

            print(f"\nAssistant: {message.content}\n")
            messages.append({"role": "assistant", "content": message.content})

        except Exception as e:
            print(f"Error: {e}\n")
            messages.pop()
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Linkup + OpenAI
Source: https://docs.linkup.so/pages/integrations/linkup-openai

Use OpenAI's function calling capabilities to integrate with Linkup

<Card title="Looking for OpenAI SDK?" icon="link" href="https://docs.linkup.so/pages/sdk/open-ai/open-ai">
  We have a dedicated guide for using the OpenAI SDK with Linkup.
</Card>

This tutorial shows you how to use OpenAI's function calling with Linkup to build a chatbot with real-time web search capabilities.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your OpenAI API key" icon="key" href="https://platform.openai.com/api-keys">
        Create an OpenAI account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install and Setup">
    Install the required packages:

    ```bash theme={null}
    pip install linkup-sdk openai
    ```

    Set up your clients:

    ```python theme={null}
    from openai import OpenAI
    from linkup import LinkupClient
    import json
    from datetime import datetime

    openai_client = OpenAI(api_key="your_openai_api_key")
    linkup_client = LinkupClient(api_key="your_linkup_api_key")
    ```
  </Step>

  <Step title="Define the Function Schema">
    Tell OpenAI about your search function using the Responses API format:

    ```python theme={null}
    tools = [{
        "type": "function",
        "name": "search_web",
        "description": "Search the web for current information. Returns comprehensive content from relevant sources.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }]
    ```
  </Step>

  <Step title="Build the Chatbot">
    Put it all together in a conversational loop using the Responses API:

    ```python theme={null}
    system_prompt = f"You are a helpful assistant. Today is {datetime.now().strftime('%B %d, %Y')}. Use web search when you need current information."
    input_list = [{"role": "system", "content": system_prompt}]

    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "quit":
            break

        input_list.append({"role": "user", "content": user_input})

        try:
            response = openai_client.responses.create(
                model="gpt-5",
                tools=tools,
                input=input_list,
            )

            while any(item.type == "function_call" for item in response.output):
                input_list += response.output

                for item in response.output:
                    if item.type == "function_call":
                        args = json.loads(item.arguments)
                        print(f"Searching with Linkup: {args['query']}...")
                        linkup_response = linkup_client.search(
                            query=args["query"],
                            depth="standard",
                            output_type="searchResults"
                        )
                        search_results_json = json.dumps(
                            linkup_response.model_dump(), indent=2
                        )
                        input_list.append({
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": search_results_json
                        })

                response = openai_client.responses.create(
                    model="gpt-5",
                    tools=tools,
                    input=input_list,
                )

            input_list += response.output

            print(f"\nAssistant: {response.output_text}\n")

        except Exception as e:
            print(f"Error: {e}\n")
            input_list.pop()
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# LlamaIndex
Source: https://docs.linkup.so/pages/integrations/llama-index

How to use Linkup in LlamaIndex

## Overview

Linkup can be used with [LlamaIndex](https://www.llamaindex.ai/) to create advanced AI agents and workflows based on internal and web data.

## Getting Started with Linkup in LLamaIndex

<Steps>
  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Install dependencies">
    ```shell theme={null}
    pip install llama-index llama-index-tools-linkup-research
    ```
  </Step>

  <Step title="Create your agent">
    ```python theme={null}
    from llama_index.core.agent import FunctionCallingAgent
    from llama_index.llms.openai import OpenAI
    from llama_index.tools.linkup_research.base import LinkupToolSpec

    # Tool initialization
    linkup_tool = LinkupToolSpec(
        api_key="<YOUR LINKUP API KEY>",
        depth="standard", # Options: "standard" or "deep"
        output_type="searchResults", # Options: "searchResults", "sourcedAnswer", or "structured"
    )
    ```

    <Info>
      <table>
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Options</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td><code>depth</code></td>
            <td><code>standard</code>, <code>deep</code></td>
            <td>Controls search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
          </tr>

          <tr>
            <td><code>output\_type</code></td>
            <td><code>searchResults</code>, <code>sourcedAnswer</code>, <code>structured</code></td>
            <td>Determines the format of returned information.</td>
          </tr>
        </tbody>
      </table>
    </Info>
  </Step>

  <Step title="Initialize and run your agent">
    ```python theme={null}
    # Agent initialization
    agent = FunctionCallingAgent.from_tools(
        linkup_tool.to_tool_list(),
        llm=OpenAI(
          api_key="<YOUR OPENAI API KEY>",
          model="gpt-4o-mini"
        ),
    )

    # Agent invocation
    response = agent.chat("Can you tell me which women were awarded the Physics Nobel Prize")
    print(response)
    ```
  </Step>
</Steps>

## Example Response

```python theme={null}
# Sample output
{
  "response": "Marie Curie (1903), Maria Goeppert Mayer (1963), Donna Strickland (2018), and Andrea Ghez (2020) have been awarded the Nobel Prize in Physics.",
  "sources": [
    # Source information would appear here
  ]
}
```

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Lovable
Source: https://docs.linkup.so/pages/integrations/lovable/lovable

How to use Linkup with Lovable

## Overview

This guide will show you how to integrate Linkup API into your Lovable applications, whether you're starting from scratch or adding Linkup to an existing app.

## Integration Steps

<Steps>
  <Step title="Access your Lovable account">
    Log in to your Lovable account at [lovable.dev](https://lovable.dev).
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Add Linkup to Your Lovable App">
    <Frame>
      <img alt="Lovable Chatbot Interface" />
    </Frame>

    In your Lovable chatbot window, use the prompt below:

    ```bash theme={null}
    # Install the Linkup SDK
    npm i linkup-sdk

    # Import and initialize the client
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: '<YOUR API KEY>', # your api key here
    });

    # Create the search function
    const askLinkup = async () => {
      return await client.search({
        query: "Your Query here",
        depth: 'standard', # "standard" or "deep"
        outputType: 'sourcedAnswer',
      });
    };

    # Call the function
    askLinkup().then(console.log);
    ```

    <Info>
      <table>
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Options</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td><code>depth</code></td>
            <td><code>standard</code>, <code>deep</code></td>
            <td>Controls search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
          </tr>

          <tr>
            <td><code>output\_type</code></td>
            <td><code>searchResults</code>, <code>sourcedAnswer</code>, <code>structured</code></td>
            <td>Determines the format of returned information.</td>
          </tr>
        </tbody>
      </table>
    </Info>
  </Step>

  <Step title="Start Building Your Web-Connected App">
    Now that you have Linkup integrated with Lovable, you can start building applications that have access to the entire web. Your Lovable app can now:

    * Search and retrieve real-time information from across the web
    * Provide up-to-date answers with source citations
    * Access and analyze web content to enhance user interactions

    Start by testing your integration with a simple query, then expand your application's capabilities using the advanced configuration options below.
  </Step>
</Steps>

For advanced configuration like including images, date filtering and supported output types,
check <a href="/pages/sdk/js/js#input-parameters"> configuration parameters </a>.

## Best Practices

1. **API Key Security**: Never expose your API key in client-side code. Use environment variables or secure backend storage.

2. **Error Handling**: Implement proper error handling for API calls:

```javascript theme={null}
const askLinkup = async () => {
  try {
    const result = await client.search({
      query: "Your query here",
      depth: 'deep',
      outputType: 'sourcedAnswer',
    });
    return result;
  } catch (error) {
    console.error('Error fetching data from Linkup:', error);
    // Handle error appropriately
  }
};
```

3. **Rate Limiting**: Be mindful of API rate limits and implement appropriate caching strategies if needed.

## Next Steps

* Check out [Lovable documentation](https://docs.lovable.dev) to enhance your Lovable application
* Join our [Discord community](https://discord.com/invite/9q9mCYJa86) for support and updates

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Make
Source: https://docs.linkup.so/pages/integrations/make/make

How to connect Make to web search

## Overview

You can connect a [Make](https://eu2.make.com) workflow to web search through Linkup, which can be used as a Module to get contextual information from the internet.

## Installation

<Steps>
  <Step title="Open Make">
    Go to your Make account and navigate to dashboard > Scenario > Create a new scenario.

    <img alt="Make" />

    <img alt="Make" />
  </Step>

  <Step title="Select Linkup Action">
    Search for Linkup in the searchbar and select the Linkup Action you want to use.

    <img alt="Make" />
  </Step>

  <Step title="Connect Your Account">
    Get your Linkup API Key and create a connection.

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    Click on Create a Connection and enter your Linkup API Key.

    <img alt="Make" />

    <img alt="Make" />

    Click on Save to complete the connection.
  </Step>

  <Step title="Configure Your Action">
    Enter your search query and choose the depth of the search.

    <img alt="Make" />

    <img alt="Make" />

    Click on Save to complete the setup.
  </Step>
</Steps>

You are all set to use Linkup in your Make workflow! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Linkup MCP Server
Source: https://docs.linkup.so/pages/integrations/mcp/mcp

Linkup MCP Server allows you to use the Linkup API in your MCP clients.

Developed by Anthropic, the [Model Context Protocol](https://github.com/modelcontextprotocol) (MCP) is an open protocol that standardizes how applications provide context to LLMs. It is particularly helpful when building agents and complex workflows on top of LLMs.

> Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

-*Anthropic*

<Info>
  Learn more about the Model Context Protocol in Anthropic's [official documentation](https://modelcontextprotocol.io/introduction)
</Info>

<CardGroup>
  <Card title="Remote MCP" icon="cloud" href="#remote-mcp">
    Use our hosted MCP endpoint (recommended)
  </Card>

  <Card title="MCPB Bundle" icon="cube" href="#mcpb-bundle">
    Single-file bundle for Claude Desktop
  </Card>

  <Card title="Local MCP" icon="computer" href="#local-mcp">
    Run MCP locally with NPM package
  </Card>
</CardGroup>

<Card title="GitHub Repository" icon="github" href="https://github.com/LinkupPlatform/linkup-mcp-server">
  View the source code and see detailed documentation
</Card>

<Tip>
  The Linkup MCP server is compatible with any MCP client, such as [Cursor](https://docs.cursor.com/context/model-context-protocol) or [Claude
  Desktop](https://modelcontextprotocol.io/quickstart/user). Choose between local installation or our hosted endpoint based on your needs.
</Tip>

## Features

The Linkup MCP server provides two powerful tools:

* **🔍 `linkup-search`**: Real-time web search with natural language queries
  * Standard and deep search modes
  * Access to current information from trusted sources

* **🌐 `linkup-fetch`**: Fetch and extract content from any webpage
  * Optional JavaScript rendering for dynamic content
  * Perfect for article extraction and content analysis

<img alt="MCP demo" />

## Remote MCP

Use our hosted MCP endpoint for a quick setup without any local installation. This is the recommended approach for most users.

### Prerequisites

To use Remote MCP, you need:

* A Linkup API key
* Any MCP client that supports HTTP/SSE connections

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

### Quick Start with Smithery

The easiest way to get started is using [Smithery](https://smithery.ai/server/@LinkupPlatform/linkup-mcp-server).
From there, you'll be able to install the server into your favorite MCP compatible client. The remote MCP server is using the Streamable HTTP transport.

### Manual Configuration

<Tabs>
  <Tab title="Cursor">
    [![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=linkup\&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vbWNwLmxpbmt1cC5zby9tY3A%2FYXBpS2V5PVlPVVJfQVBJX0tFWSJ9)

    Add to your `~/.cursor/mcp.json`:

    ```json theme={null}
    {
      "mcpServers": {
        "linkup": {
          "type": "http",
          "url": "https://mcp.linkup.so/mcp?apiKey=YOUR_API_KEY"
        }
      }
    }
    ```
  </Tab>

  <Tab title="VS Code">
    Add to your VS Code MCP config:

    ```json theme={null}
    {
      "servers": {
        "linkup": {
          "url": "https://mcp.linkup.so/mcp?apiKey=YOUR_API_KEY",
          "type": "http"
        }
      }
    }
    ```
  </Tab>
</Tabs>

<Info>
  Don't forget to replace `YOUR_API_KEY` with your actual API key!
</Info>

## MCPB Bundle

Download a pre-built MCPB (MCP Bundle) - a self-contained, single-file package that works across compatible MCP clients. This is the recommended approach for Claude Desktop.

### What is MCPB?

MCPB (MCP Bundle) is a new format developed by Anthropic for distributing MCP servers. Learn more in the [official MCPB documentation](https://github.com/anthropics/mcpb).

### Download

**Quick Download:**

```bash theme={null}
curl -L -o linkup-mcp-server.mcpb https://github.com/LinkupPlatform/linkup-mcp-server/releases/latest/download/linkup-mcp-server.mcpb
```

Or download directly from [here](https://github.com/LinkupPlatform/linkup-mcp-server/releases/latest/download/linkup-mcp-server.mcpb).

### Installation

<Steps>
  <Step title="Download the MCPB file">
    Use the curl command above or download from GitHub releases.
  </Step>

  <Step title="Install in Claude Desktop">
    Double-click the `.mcpb` file to install it in Claude Desktop.
  </Step>

  <Step title="Configure API Key">
    When prompted, enter your Linkup API key.
  </Step>
</Steps>

## Local MCP

Run the Linkup MCP server locally using NPM.

### Prerequisites

* A Linkup API key
* Node.js (v18.0.0 or higher)

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

### Configuration Examples

<Tabs>
  <Tab title="Claude Desktop">
    Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

    ```json theme={null}
    {
      "mcpServers": {
        "linkup": {
          "command": "npx",
          "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_LINKUP_API_KEY"]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Cursor">
    Edit `~/.cursor/mcp.json`:

    ```json theme={null}
    {
      "mcpServers": {
        "linkup": {
          "command": "npx",
          "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_LINKUP_API_KEY"]
        }
      }
    }
    ```
  </Tab>

  <Tab title="VS Code">
    Add to your VS Code MCP config:

    ```json theme={null}
    {
      "servers": {
        "linkup": {
          "command": "npx",
          "type": "stdio",
          "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_LINKUP_API_KEY"]
        }
      }
    }
    ```
  </Tab>
</Tabs>

Replace `YOUR_LINKUP_API_KEY` with your actual API key, then restart your application.

<Info>
  For more configuration examples and advanced usage, see the [GitHub README](https://github.com/LinkupPlatform/linkup-mcp-server#readme).
</Info>

## Available Tools

Once configured, you'll have access to two powerful tools:

### linkup-search

Search the web in real time to retrieve current information, facts, and news from trusted sources.

**Parameters:**

* `query` (required): Natural language search query. Full questions work best.
* `depth` (optional): Search depth - "standard" (default) or "deep"
  * **standard**: For queries with direct answers (weather, stock prices, simple facts)
  * **deep**: For complex research requiring analysis across multiple sources

**Example prompts:**

* "Search for the latest news about AI developments"
* "What's the current weather in Tokyo?"
* "Find information about the new EU AI Act"

### linkup-fetch

Fetch and extract content from any webpage URL.

**Parameters:**

* `url` (required): The URL to fetch content from
* `renderJs` (optional): Whether to render JavaScript content (default: false)
  * Enable for dynamic pages that load content via JavaScript
  * Note: Makes the request slower

**Example prompts:**

* "Fetch the content from [https://example.com/article](https://example.com/article)"
* "Get this blog post and summarize it: [https://blog.example.com/post](https://blog.example.com/post)"
* "What are the events happening in Paris this week? Fetch the content from [https://example.com/events](https://example.com/events)"

## Troubleshooting

### Authentication Format

**Important**: The new version (2.x) of the Linkup MCP server uses a different authentication format:

✅ **Correct (v2.x)**:

```json theme={null}
{
  "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_API_KEY"]
}
```

❌ **Old format (v1.x)**:

```json theme={null}
{
  "env": {
    "LINKUP_API_KEY": "YOUR_API_KEY"
  }
}
```

If you were using v1.x, please update your configuration to the new format.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# n8n
Source: https://docs.linkup.so/pages/integrations/n8n/n8n

Connect your n8n workflow to an internet search

## Overview

We are actively working on creating a Linkup node for [n8n](https://n8n.io).
In the meantime, follow this tutorial to get contextual information from the internet.

## Configuration Steps

<Steps>
  <Step title="Open your n8n account and create a workflow">
    Go to Workflows > Create Workflows

    <img alt="n8n" />
  </Step>

  <Step title="Add a trigger">
    Click on the + button to add a trigger

    <img alt="n8n" />
  </Step>

  <Step title="Select your trigger">
    Choose your trigger (Trigger Manually is selected in this example)

    <img alt="n8n" />
  </Step>

  <Step title="Add HTTP Request node">
    Click on the + button > Core > HTTP Request

    <img alt="n8n" />

    <img alt="n8n" />
  </Step>

  <Step title="Configure HTTP method">
    Select POST as Method

    <img alt="n8n" />
  </Step>

  <Step title="Enter API endpoint">
    Enter `https://api.linkup.so/v1/search` in URL

    <img alt="n8n" />
  </Step>

  <Step title="Set up authentication">
    In Authentication, select "Predifined Credential Type"

    <img alt="n8n" />
  </Step>

  <Step title="Credential Type">
    In Credential Type, select "Bearer Auth"

    <img alt="n8n" />
  </Step>

  <Step title="Create new credential">
    In Bearer Auth, click on "+ Create new credential"

    <img alt="n8n" />
  </Step>

  <Step title="Add Bearer Token">
    Copy your Linkup API key in the Bearer Token field, click save and close the window

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    <img alt="n8n" />
  </Step>

  <Step title="Enable request body">
    Toggle on "Send Body"

    <img alt="n8n" />
  </Step>

  <Step title="Body Content Type">
    Select "JSON" as the Content Type

    <img alt="n8n" />
  </Step>

  <Step title="Specify Body">
    Select "Using JSON" as the Specify Body option

    <img alt="n8n" />
  </Step>

  <Step title="JSON Body">
    Use JSON to specify your search parameters

    ```json theme={null}
    {
      "q": "How's the weather in Paris today?",
      "depth": "standard",
      "outputType": "sourcedAnswer"
    }
    ```

    <img alt="n8n" />

    Save and run your workflow.
  </Step>
</Steps>

You are all set to use Linkup in your n8n workflow! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Pipedream
Source: https://docs.linkup.so/pages/integrations/pipedream/pipedream

How to use Linkup in Pipedream

## Overview

Linkup can be used with [Pipedream](https://pipedream.com) as an Action to get contextual information from the internet.

## Installation

<Steps>
  <Step title="Create your project">
    1. Open your Pipedream account and click on **New project**

       <img alt="Pipedream" />

    2. Name your project and click on **Create Project**

       <img alt="Pipedream" />

    3. Click on **New** > **Workflow**.

       <img alt="Pipedream" />

    4. Name your workflow and click on **Create Workflow**

       <img alt="Pipedream" />
  </Step>

  <Step title="Select your Linkup Action">
    1. On the workflow page, click on the `+` icon to add the Linkup Action

       <img alt="Pipedream" />

    2. Search for **Linkup** and Click on it

       <img alt="Pipedream" />

    3. Select the Linkup Action you want to use
  </Step>

  <Step title="Connect your Linkup Account">
    1. Get your Linkup API Key

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    2. Go to create a Linkup account, enter your API Key and choose your connection Name

    <img alt="Pipedream" />

    <img alt="Pipedream" />
  </Step>

  <Step title="Run your Action">
    1. Enter the Query you want to search for and the depth you want to use

    <img alt="Pipedream" />

    <img alt="Pipedream" />

    2. ✅ Click on **Test** to run your action
  </Step>
</Steps>

You are all set to use Linkup in your Pipedream workflow! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# SurfSense
Source: https://docs.linkup.so/pages/integrations/surfsense/surfsense

How to use Linkup with SurfSense

## Overview

Linkup can be used with [SurfSense](https://github.com/MODSetter/SurfSense) as a Search Engine connector to create advanced AI agents and workflows based on internal and web data.

## Getting Started with Linkup in SurfSense

<Steps>
  <Step title="Setup SurfSense">
    Follow the guides here.

    1. [Setting up Docker](https://github.com/MODSetter/SurfSense/blob/main/surfsense_web/content/docs/docker-installation.mdx)
    2. [Setting up environment variables](https://github.com/MODSetter/SurfSense/blob/main/surfsense_web/content/docs/index.mdx)
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Add Linkup Connector">
    Navigate to the Add Connector page under Connectors section in SurfSense and configure with your Linkup API Key.

    <img alt="Connector Page" />

    <img alt="Adding Linkup API" />
  </Step>

  <Step title="Select the Linkup Connector during Research">
    While performing a query under Researcher, select the Linkup Connector and save it.

    <img alt="Selecting Linkup Connector" />
  </Step>

  You are all set to use the Linkup Search API with SurfSense.
</Steps>

## Example

<img alt="Example Usage - Linkup with Surfsense" />

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Vercel AI SDK
Source: https://docs.linkup.so/pages/integrations/vercel-ai-sdk

How to use Linkup with the Vercel AI SDK

## Overview

Linkup can be used with the [Vercel AI SDK](https://sdk.vercel.ai/) as a tool for web search. This integration allows you to build AI applications that can access real-time information from the internet using any model supported by the AI SDK.

<Card title="GitHub Repository" icon="github" href="https://github.com/LinkupPlatform/linkup-ai-sdk" />

## Getting Started with Linkup in Vercel AI SDK

<Steps>
  <Step title="Install the Linkup AI SDK">
    ```bash theme={null}
    npm install linkup-ai-sdk ai @ai-sdk/openai
    ```

    <Info>
      We have chosen OpenAI as the default model provider, but you can use any provider supported by the Vercel AI SDK (like `@ai-sdk/anthropic`, `@ai-sdk/mistral`, etc.)
    </Info>
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Set up your environment variables">
    Create a `.env` file in your project root:

    ```bash theme={null}
    LINKUP_API_KEY=your_linkup_api_key_here
    OPENAI_API_KEY=your_openai_api_key_here
    ```
  </Step>

  <Step title="Create and use the Linkup web search tool">
    ```typescript theme={null}
    import { openai } from '@ai-sdk/openai';
    import { generateText, stepCountIs } from 'ai';
    import { webSearch } from 'linkup-ai-sdk';

    const { text } = await generateText({
      model: openai('gpt-4o-mini'),
      prompt: 'What was Microsoft's revenue last quarter and was it well perceived by the market?',
      tools: {
        webSearch: webSearch({ depth: 'standard' }),
      },
      stopWhen: stepCountIs(3),
    });

    console.log(text);
    ```
  </Step>
</Steps>

## Configuration Options

The `webSearch` tool accepts the following configuration options:

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>apiKey</code></td>
      <td><code>string</code></td>
      <td><code>process.env.LINKUP\_API\_KEY</code></td>
      <td>Your Linkup API key. If not provided, it will be read from the environment variable.</td>
    </tr>

    <tr>
      <td><code>depth</code></td>
      <td><code>'standard' | 'deep'</code></td>
      <td><code>'standard'</code></td>
      <td>Search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
    </tr>

    <tr>
      <td><code>includeImages</code></td>
      <td><code>boolean</code></td>
      <td><code>false</code></td>
      <td>Whether to include images in the search results.</td>
    </tr>

    <tr>
      <td><code>includeDomains</code></td>
      <td><code>string\[]</code></td>
      <td><code>\[]</code></td>
      <td>Array of domains to include in the search results.</td>
    </tr>

    <tr>
      <td><code>excludeDomains</code></td>
      <td><code>string\[]</code></td>
      <td><code>\[]</code></td>
      <td>Array of domains to exclude from the search results.</td>
    </tr>

    <tr>
      <td><code>fromDate</code></td>
      <td><code>Date</code></td>
      <td><code>null</code></td>
      <td>Start date for filtering search results.</td>
    </tr>

    <tr>
      <td><code>toDate</code></td>
      <td><code>Date</code></td>
      <td><code>null</code></td>
      <td>End date for filtering search results.</td>
    </tr>
  </tbody>
</table>

For more details on search capabilities, see our [Search Concepts documentation](/pages/documentation/get-started/concepts).

## Resources

* [Linkup AI SDK on npm](https://www.npmjs.com/package/linkup-ai-sdk)
* [Linkup AI SDK on GitHub](https://github.com/LinkupPlatform/linkup-ai-sdk)
* [Vercel AI SDK Documentation](https://sdk.vercel.ai/)
* [Search Concepts](/pages/documentation/get-started/concepts)

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Xpander
Source: https://docs.linkup.so/pages/integrations/xpander/xpander

Integrate Linkup with Xpander to enhance your AI workflows

## Overview

Linkup can be used in [Xpander.ai](http://Xpander.ai) to get contextual information from the internet in a workflow.

## Installation

<Steps>
  <Step title="Open Xpander">
    1. Open your Xpander account.
    2. Go to the **Agents** tab.
    3. Click **New Agent**
    4. Name your agent (e.g. “Linkup Agent”)

       <img alt="Step 1" />
  </Step>

  <Step title="Open the Tools Panel">
    1. Inside the agent editor, click on the **Tools** tab
    2. Click **+ Add Tools**

       <img alt="Step 2" />
  </Step>

  <Step title="Select Linkup">
    1. From the list, choose [**Linkup.so**](http://Linkup.so) (auth required)

       <img alt="Step 3" />

    2. Choose “API Key” under Authentication Mode

    3. Enter your Linkup API Key

    4. Choose “Bearer”

       <img alt="Step 4" />

    5. Select the action: `Retrieve Web Content by Query`

       <img alt="Step 5" />

    6. Click **Add**
  </Step>

  <Step title="Confirm the Tool is Active">
    1. Linkup should now appear in your Tools list
    2. You don’t need to connect it to other tools manually
    3. Xpander AI will automatically detect when to use Linkup

       <img alt="Step 6" />
  </Step>
</Steps>

You are all set to use Linkup in your Xpander workflow! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Zapier
Source: https://docs.linkup.so/pages/integrations/zapier/zapier

Integrate Linkup in Zapier to augment your workflows

## Overview

Linkup can be used as a [Zapier](https://zapier.com) Action to get contextual information from the internet in a workflow.

## Installation

<Steps>
  <Step title="Open Zapier">
    1. Open your Zapier account.
    2. Go to the dashboard Create > Zaps.

       <img alt="Zapier" />
  </Step>

  <Step title="Select Linkup Action">
    1. Click on Action to select a Linkup Action

       <img alt="Zapier" />

    2. Search for Linkup and click on Linkup

       <img alt="Zapier" />

    3. Select the Linkup Action you want to use

       <img alt="Zapier" />
  </Step>

  <Step title="Connect Linkup Account">
    1. Get your Linkup API Key:

    <Card title="Get your API key" icon="key" href="https://app.linkup.so">
      Create a Linkup account for free to get your API key.
    </Card>

    2. Click on Account.

    3. Enter your Linkup API Key.

       <img alt="Zapier" />

    4. Click on Yes, Continue to Linkup.

    5. Click on Continue

       <img alt="Zapier" />
  </Step>

  <Step title="Configure and Run">
    1. Enter your search query.

       <img alt="Zapier" />

    2. Choose the depth of the search.

       <img alt="Zapier" />

    3. Click on Continue.
  </Step>
</Steps>

You are all set to use Linkup in your Zapier workflow! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Typescript SDK
Source: https://docs.linkup.so/pages/sdk/js/js

How to use Linkup Javascript SDK natively in your apps.

## Introduction

The Typescript SDK allows for easy interaction with the Linkup API, offering the full range of our search functionality. Easily integrate smart search capabilities into your applications, harnessing Linkup’s powerful search features.
You can use our [playground](https://app.linkup.so/playground) to have interactive examples and see how to implement them with the SDK.

<CardGroup>
  <Card title="Github" icon="github" href="https://github.com/LinkupPlatform/linkup-js-sdk">
    Repository (feel free to contribute)
  </Card>

  <Card title="NPM" icon="npm" href="https://www.npmjs.com/package/linkup-sdk">
    NPM page
  </Card>
</CardGroup>

## Quickstart

Get started with our Typescript SDK in less than 5 minutes!

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

## Installation

You can install the Linkup Typescript SDK using the following:

```shell theme={null}
npm i linkup-sdk
```

## Usage

Here is a basic usage showing how to use the Linkup SDK:

```typescript theme={null}
import { LinkupClient } from "linkup-sdk";

const client = new LinkupClient({
	apiKey: "<YOUR API KEY>",
});

const askLinkup = async () => {
	return await client.search({
		query: "Can you tell me which women were awarded the Physics Nobel Prize",
		depth: "standard",
		outputType: "sourcedAnswer",
	});
};

askLinkup().then(console.log);
```

## Input Parameters

| Parameter              | Type      | Description                                                                                        | Default   |
| ---------------------- | --------- | -------------------------------------------------------------------------------------------------- | --------- |
| query                  | str       | The input query string                                                                             | Required  |
| depth                  | string    | Type of search to perform "standard" or "deep"                                                     | Required  |
| outputType             | string    | Linkup response type, can be "sourcedAnswer", "searchResults", "structuredOutput"                  | Required  |
| structuredOutputSchema | string    | The returned schema from the Linkup API. It should be used only if the outputType is 'structured'. | undefined |
| includeImages          | boolean   | To also return images                                                                              | undefined |
| fromDate               | date      | From date to search                                                                                | undefined |
| toDate                 | date      | To date to search                                                                                  | undefined |
| includeDomains         | string\[] | To include domain(s)                                                                               | undefined |
| excludeDomains         | string\[] | To exclude domain(s)                                                                               | undefined |
| includeInlineCitations | boolean   | To include inline citations in the answer, if `outputType` is `sourcedAnswer`                      | undefined |
| includeSources         | boolean   | To include the sources, if `outputType` is `structured` (modifies the schema of the output)        | undefined |
| maxResults             | number    | Maximum number of results to return                                                                | undefined |

### Query

The `query` parameter is the core input string that defines your search intent. It represents the question or information request that you want Linkup to answer. How you formulate this query significantly impacts the quality and relevance of results.

Effective queries should be:

* **Clear and specific**: "What were the key findings of NASA's James Webb telescope in 2023?" provides better results than "Tell me about space discoveries"
* **Contextually rich**: Include relevant context when needed ("What are the environmental impacts of lithium mining for EV batteries?")
* **Naturally phrased**: Write as you would ask a knowledgeable person, not with keywords

For optimal results, consider reviewing our [prompting guide](https://docs.linkup.so/pages/documentation/tutorials/prompting-guide), which provides detailed strategies for crafting effective queries.

### Depth

The `depth` field is used to select the type of search you want to perform:

* **standard**: the search will be straightforward and fast, suited for relatively simple queries (e.g. "What's the weather in Paris today?")
* **depth**: the search will use an agentic workflow, which makes it in general slower, but it will be able to solve more complex queries (e.g. "What is the company profile of LangChain accross the last few years, and how does it compare to its concurrents?")

### Output type

The type of output which is expected:

* **sourcedAnswer**: Provides a comprehensive natural language answer to the query along with citations to the source material. Ideal for when you need well-formed responses with verifiable information and transparent sourcing.
* **searchResults**: Returns the raw search context data without synthesis, giving you direct access to the underlying information. Useful for custom processing, or when you need to implement your own answer generation logic.
* **structured**: Allows you to receive responses in a custom format based on the format provided in
  `structuredOutputSchema`. If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

### Structured output schema

Linkup’s structured output feature allows you to receive responses in a custom format that you define. This is particularly useful when you need to integrate Linkup’s responses directly into your application’s data structure or when you want to ensure consistency in the response format.
To do that, you have to use the `structuredOutputSchema` field.
If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

### Include images

The `includeImages` parameter allows you to receive image results alongside text results in your search responses. When set to `true`, Linkup will return relevant images related to your query, each with a URL and metadata. This is particularly useful for:

* Creating visual search experiences
* Building content that combines text and images
* Researching topics where visual information is important

Image results are returned with the same structure as text results but with `type: "image"`.

### fromDate

The `fromDate` parameter filters search results to only include content published after the specified date. This helps you:

* Focus on recent information
* Exclude outdated content

The date should be a Date type, for example: `new Date("2024-01-01")`.

### toDate

The `toDate` parameter complements `fromDate` by restricting search results to only include content published or updated before the specified date. This is useful for:

* Historical research on specific time periods
* Analyzing content published within a specific date range
* Avoiding more recent information that might skew results

Like `fromDate`, the date should be a Date type, for example: `new Date("2024-12-31")`.

When used together, `fromDate` and `toDate` create a date range filter for your search results.

### includeDomains

The `includeDomains` parameter allows you to specify a list of domains that must be included in the search results. This is useful for:

* focus on specific sources
* ensure that results come from trusted domains.

### excludeDomains

The `excludeDomains` parameter allows you to specify a list of domains that should be excluded from the search results. This is useful for:

* Filtering out unwanted sources
* Avoiding results from specific domains that may not be relevant or trustworthy.

### includeInlineCitations

The `includeInlineCitations` parameter is specifically designed for use with the `sourcedAnswer` output type. When enabled, it embeds citations directly within the answer text, making it easier to identify which parts of the response correspond to specific sources. This is particularly useful for:

* Academic or research applications where source attribution is critical
* Creating content that needs verifiable claims with clear sourcing
* Building applications where users need to quickly verify information

When `includeInlineCitations` is set to `true`, the answer will contain inline references like \[1], \[2] that correspond to the sources in the response.

### includeSources

The `includeSources` parameter is specifically designed for use with the `structured` output type. When enabled, it modifies the schema of the structured response to include source information alongside your custom data structure. This is particularly useful for:

* Applications that need both structured data and source attribution
* Building systems that require traceability of information
* Creating responses where you want to maintain both custom format and source verification

When `includeSources` is set to `true`, the response will have a `data` property and a `sources` property.

### maxResults

The `maxResults` parameter allows you to specify the maximum number of results to return. This is useful for:

* Limiting the number of results returned
* Reducing the context size

## Examples

<AccordionGroup>
  <Accordion title="Last Formula 1 race" description="Standard example" icon="flag">
    <p>This example show you how to combine the standard search with a sourced answer</p>

    ```typescript theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getRaceResume = async () => {
      return await client.search({
        query:"Can you resume me the last Formula 1 race ?",
        depth:"standard",
        outputType:"sourcedAnswer",
      });
    };

    getRaceResume().then(console.log);
    ```

    Example response:

    ```json theme={null}
    {
      "answer": "Lando Norris won the 2025 Australian Grand Prix, the season opener, in challenging wet conditions. The race saw multiple incidents, including crashes on the first lap, leading to six drivers not finishing. Notably, Lewis Hamilton finished in 10th place. The race was marked by dramatic weather changes that affected many competitors. For more details, you can read the full results [here](https://www.motorsportweek.com/2025/03/16/f1-2025-australian-grand-prix-race-results/).",
      "sources": [
        {
          "name": "F1 2025 Australian Grand Prix – Race Results",
          "url": "https://www.motorsportweek.com/2025/03/16/f1-2025-australian-grand-prix-race-results/",
          "snippet": "McLaren's Lando Norris has won the Formula 1 season-opening Australian Grand Prix in a mixed conditions thriller at the Albert",
          "favicon": "https://www.motorsportweek.com/wp-content/uploads/2020/04/cropped-favicon-32x32.png"
        },
        {
          "name": "McLaren’s Lando Norris wins wet and wild Australian Grand Prix. Hamilton finishes 10th",
          "url": "https://www.msn.com/en-us/sports/other/mclarens-lando-norris-wins-wet-and-wild-australian-grand-prix-hamilton-finishes-10th/ar-AA1B0kIf",
          "snippet": "The Melbourne race had a thrilling start with Racing Bull’s Isack Hadjar out on the formation lap, and Alpine’s Jack Doohan and Williams’ Carlos Sainz crashing out on the opening lap.",
          "favicon": "https://static.msn.com/en-us/entertainment/favicon.ico"
        },
        {
          "name": "F1 Australian Grand Prix 2025 results: Norris wins, rookies spin out in the rain",
          "url": "https://www.msn.com/en-us/sports/other/f1-australian-grand-prix-2025-results-norris-wins-rookies-spin-out-in-the-rain/ar-AA1B4irD",
          "snippet": "If you like drama in racing, the 2025 F1 Australian Grand Prix didn’t disappoint. Intermittent rain caused havoc on the track, and six drivers didn’t complete the 57 laps, including four of this year’s full-season rookies.",
          "favicon": "https://static.msn.com/en-us/entertainment/favicon.ico"
        },
        ...
      ]
    }
    ```
  </Accordion>

  <Accordion title="Company Revenue" description="Deep + structured output" icon="building">
    <p>This example shows you how to use the deep with a relative complexe structured output:</p>

    ```typescript theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const schema = {
      "type": "object",
      "properties": {
        "companyName": {
          "type": "string",
          "description": "The name of the company"
        },
        "revenueAmount": {
          "type": "number",
          "description": "The revenue amount"
        },
        "fiscalYear": {
          "type": "string",
          "description": "The fiscal year for this revenue"
        }
      }
    };

    const getCompanyRevenue = async () => {
      return await client.search({
        query: "What is Microsoft's 2024 revenue?",
        depth: 'deep',
        outputType: 'structured',
        structuredOutputSchema: schema
      });
    };

    getCompanyRevenue().then(console.log);
    ```

    Example response:

    ```json theme={null}
    {
        "companyName": "Microsoft",
        "revenueAmount": 245100000000,
        "fiscalYear": "2024"
    }
    ```
  </Accordion>

  <Accordion title="Latest politic news" description="Search results as outputType" icon="newspaper">
    <p>This example shows you how to use the standard with a search results:</p>

    ```typescript theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getNews = async () => {
      return await client.search({
        query: "Latest politic news",
        depth: 'standard',
        outputType: 'searchResults'
      });
    };

    getNews().then(console.log);
    ```

    Example response:

    ```json theme={null}
    {
      "results": [
        {
          "type": "text",
          "name": "‘I’m Still Here’ invites reflection on world politics, history",
          "url": "https://www.thepostathens.com/article/2025/03/im-still-here-movie-review",
          "content": "For “I’m Still Here,” viewers do not walk away with the same feeling. It begins with excitement and energy but ends feeling empty and reflective. It is a movie about memory and the ability to keep the ones we’ve lost alive in our psyches.",
          "favicon": "https://www.thepostathens.com/favicon.ico"
        },
        {
          "type": "text",
          "name": "Local Politics",
          "url": "https://www.seattletimes.com/seattle-news/politics/",
          "content": "House Bill 1175 would have required cities across Washington to allow cafes and stores in all residential areas, superseding any local zoning restrictions. Initiative 2081, signed by over 448,000 ...",
          "favicon": "https://www.seattletimes.com/favicon.ico"
        },
        {
          "type": "text",
          "name": "Spruce Creeker allegedly points gun at fellow resident over politics",
          "url": "https://www.villages-news.com/2025/03/17/spruce-creeker-allegedly-points-gun-at-fellow-resident-over-politics/",
          "content": "A resident of the Spruce Creek Del Webb community in Summerfield was arrested after he allegedly pointed a gun at a fellow resident over politics.",
          "favicon": "https://www.villages-news.com/wp-content/uploads/2019/06/cropped-villages-news-favicon-32x32.png"
        },
        ...
      ]
    }
    ```
  </Accordion>

  <Accordion title="Amazon deforestation" description="IncludeImages filter" icon="trees">
    <p>This example return text and images sources</p>

    ```typescript theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getData = async () => {
      return await client.search({
        query: "Amazon deforestation",
        depth: 'standard',
        outputType: 'searchResults',
        includeImages: true
      });
    };

    getData().then(console.log);
    ```

    Exemple response

    ```json theme={null}
    {
      "results":
        [
          {"type":"text","name":"The rough road to sustainable farming in an Amazon deforestation hotspot","url":"https://www.msn.com/en-us/society-culture-and-history/social-issues/the-rough-road-to-sustainable-farming-in-an-amazon-deforestation-hotspot/ar-AA1B64yY","content":"Bartolomeu Moraes, better known as Brasília, was a peasant leader and trade unionist in Brazil involved in a long, bloody land war. In 2002, he was killed after years of opposing powerful local ranchers along the BR-163 highway area,", "favicon":"https://static.msn.com/en-us/entertainment/favicon.ico"},
          {"type":"text","name":"Forest management ambitions in Brazilian Amazon aim to make up for lost time","url":"https://www.msn.com/en-us/news/world/forest-management-ambitions-in-brazilian-amazon-aim-to-make-up-for-lost-time/ar-AA1ALyxz","content":"In the early 2000s, deforestation levels in the Brazilian Amazon rose so tremendously that, faced with both national and international pressure, the federal government decided to implement forest timber management as a way to curb the destruction.", "favicon":"https://static.msn.com/en-us/entertainment/favicon.ico"},
          {"type":"text","name":"Race to save the rainforest: Why replacing cocaine barons with cattle ranchers is destroying the Amazon","url":"https://www.telegraph.co.uk/news/amazon-deforestation-in-colombia/","content":"Though the Amazon rainforest proved a useful screen ... Should the recent rates of deforestation continue, experts warn, the implications will prove devastating for us all. Marisela Silva Parra ...", "favicon":"https://www.telegraph.co.uk/favicon.ico"},
          ...
          {"type":"image","name":"Deforestation: Primary Forest Losses Impact Climate Change — Carmen ...","url":"https://images.squarespace-cdn.com/content/v1/584738ff20099e6c2da92f74/1556207140784-08HFC1PNAYWX368IJGXM/ke17ZwdGBToddI8pDm48kNvT88LknE-K9M4pGNO0Iqd7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1USOFn4xF8vTWDNAUBm5ducQhX-V3oVjSmr829Rco4W2Uo49ZdOtO_QXox0_W7i2zEA/Deforestation+in+Brazil"},
          {"type":"image","name":"Amazon Rainforest Deforestation Before And After","url":"https://media.wired.com/photos/59372bbfd80dd005b42b626f/master/w_2560%2Cc_limit/AP4997094644081.jpg"},
          {"type":"image","name":"11 Amazon Rainforest Deforestation Facts to Know About | Earth.Org","url":"https://u4d2z7k9.rocketcdn.me/wp-content/uploads/2021/11/Untitled-design-88.jpg"},
          ...
        ]
    }
    ```
  </Accordion>

  <Accordion title="AI Avancements" description="Dates filtering" icon="calendar">
    <p>This example shows you how to use the dates filter:</p>

    ```typescript theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getNews = async () => {
      return await client.search({
        query: "What are the recent advancements in artificial intelligence technology",
        "depth": "standard",
        "outputType": "sourcedAnswer",
        "fromDate": new Date("2025-03-01"),
        "toDate": new Date("2025-03-05"),
      });
    };

    getNews().then(console.log);
    ```

    Example response:

    ```json theme={null}
    {
      "answer":"1. **MBZUAI Launches AI Undergraduate Program**: The Mohamed bin Zayed University of Artificial Intelligence has introduced a pioneering undergraduate program aimed at shaping future AI leaders. [Read more](https://www.finanznachrichten.de/nachrichten-2025-03/64714165-mbzuai-unveils-first-of-its-kind-undergraduate-program-in-artificial-intelligence-designed-to-empower-future-ai-leaders-200.htm)\n\n2. **DeepSeek AI Chatbot Raises Cybersecurity Concerns**: The release of DeepSeek, an AI chatbot, has sparked discussions about new cybersecurity challenges associated with rapidly advancing AI technologies. [Read more](https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/)\n\n3. **AI's Impact on Business Innovation**: The integration of AI and other technologies is becoming essential for business success, driving innovation and growth. [Read more](https://www.independent.com.mt/articles/2025-03-02/newspaper-opinions/The-intersection-of-technology-and-business-Paving-the-way-for-innovation-and-growth-6736268254)\n\n4. **Research on Achieving Human-Level AI**: Experts are calling for a change in approach to develop AI systems capable of human-level reasoning, indicating current methods may not suffice. [Read more](https://www.nature.com/articles/d41586-025-00649-4)",
      "sources":
        [
          {
            "name":"MBZUAI Unveils First-of-its-Kind Undergraduate Program in Artificial Intelligence Designed to Empower Future AI Leaders",
            "url":"https://www.finanznachrichten.de/nachrichten-2025-03/64714165-mbzuai-unveils-first-of-its-kind-undergraduate-program-in-artificial-intelligence-designed-to-empower-future-ai-leaders-200.htm",
            "snippet":"ABU DHABI, AE / ACCESS Newswire / March 3, 2025 / The Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) is disrupting the AI education landscape with the launch of its first-ever underg",
            "favicon":"https://www.finanznachrichten.de/favicon.ico"
          },
          {
            "name":"The intersection of technology and business: Paving the way for innovation and growth",
            "url":"https://www.independent.com.mt/articles/2025-03-02/newspaper-opinions/The-intersection-of-technology-and-business-Paving-the-way-for-innovation-and-growth-6736268254",
            "snippet":"In the fast-paced world of business, the integration of innovative technologies has become a crucial driver of success. As an advocate for Artificial Intelligence (AI), Blockchain, Data Analytics, and",
            "favicon":"https://www.independent.com.mt/favicon.ico"
          },
          {
            "name":"DeepSeek Sparks New Cyber Challenges In the AI Chatbot Era",
            "url":"https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/",
            "snippet":"This article discusses DeepSeek, an artificial intelligence chatbot that was released in January of this year, and the concerns it raises around security and rapidly advancing technology.",
            "favicon":"https://www.law.com/favicon.ico"
          },
          ...
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

## Additional ressources

### Prompting guide

We strongly recommend you to read our [prompting guide](https://docs.linkup.so/pages/documentation/tutorials/prompting-guide) to best prompt the Linkup API and get optimal results. Even small improvements in how you structure your prompts can dramatically enhance the quality of responses and the overall user experience.

### Structured output guide

We strongly recommend you to read our [structured output guide](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide) to ensure consistency in the response format. Mastering structured outputs allows you to fully leverage Linkup's capabilities while maintaining complete control over how the information is presented and processed in your application.

### Tutorials

Don't hesitate to [check our tutorials](https://docs.linkup.so/pages/documentation/tutorials/signup-radar) for other ideas of what to build with Linkup!

And voilà ! You're now ready to implement the Linkup SDK inside your fabulous project ! 🚀

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# OpenAI SDK
Source: https://docs.linkup.so/pages/sdk/open-ai/open-ai

How to use OpenAI SDK natively in your apps.

## Introduction

The OpenAI SDK can be used to interact with the Linkup API, to generate responses.

<Info>
  We are only compatible with [Responses API](https://platform.openai.com/docs/api-reference/responses).<br />
  Chat Completions API is **NOT** supported at the moment.
</Info>

## Quickstart

Get started with the OpenAI SDK in less than 5 minutes!

<Tabs>
  <Tab title="Python">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You can install the OpenAI SDK using the following:

        ```shell theme={null}
        pip install openai
        ```
      </Step>

      <Step title="Usage">
        Here is a basic usage showing how to use the OpenAI SDK:

        ```python theme={null}
        from openai import OpenAI

        client = OpenAI(
          base_url='https://api.linkup.so/v1',
          api_key="<YOUR API KEY>"
        )

        response = client.responses.create(
          model="linkup-standard",
          input="Can you tell me which women were awarded the Physics Nobel Prize",
        )

        print(response.output_text)
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="TypeScript">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You can install the OpenAI SDK using the following:

        ```shell theme={null}
        npm i openai
        ```
      </Step>

      <Step title="Usage">
        Here is a basic usage showing how to use the OpenAI SDK:

        ```typescript theme={null}
        import OpenAI from 'openai';

        const client = new OpenAI({
          baseURL: 'https://api.linkup.so/v1',
          apiKey: "<YOUR API KEY>"
        });

        const response = await client.responses.create({
          model: "linkup-standard",
          input: "Can you tell me which women were awarded the Physics Nobel Prize",
        });

        console.log(response.output_text);
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Input Parameters

| Parameter | Type   | Description                                                  | Default  |
| --------- | ------ | ------------------------------------------------------------ | -------- |
| model     | string | Type of search to perform "linkup-standard" or "linkup-deep" | Required |

For others parameters, please refer to the [Responses API](https://platform.openai.com/docs/api-reference/responses).

### Model

The `model` field is used to select the type of search you want to perform:

* **linkup-standard**: the search will be straightforward and fast, suited for relatively simple queries (e.g. "What's the weather in Paris today?")
* **linkup-deep**: the search will use an agentic workflow, which makes it in general slower, but it will be able to solve more complex queries (e.g. "What is the company profile of LangChain accross the last few years, and how does it compare to its concurrents?")

## Using structured output (advanced)

<Tabs>
  <Tab title="Python">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You need to install the OpenAI SDK and Pydantic using the following:

        ```shell theme={null}
        pip install openai pydantic
        ```
      </Step>

      <Step title="Usage">
        Here is a example of how to use the structured output with the OpenAI SDK:

        ```python theme={null}
        from openai import OpenAI
        from pydantic import BaseModel

        class Winner(BaseModel):
          name: str
          year: str

        class Response(BaseModel):
          winners: list[Winner]

        client = OpenAI(
          base_url='https://api.linkup.so/v1',
          api_key="<YOUR API KEY>"
        )

        response = client.responses.parse(
          model="linkup-standard",
          input="Can you tell me which women were awarded the Physics Nobel Prize",
          text_format=Response,
        )

        print(response.output_parsed)
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="TypeScript">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You need to install the OpenAI SDK and Zod using the following:

        ```shell theme={null}
        npm i openai zod
        ```
      </Step>

      <Step title="Usage">
        Here is a example of how to use the structured output with the OpenAI SDK:

        ```typescript theme={null}
        import OpenAI from 'openai';
        import { zodTextFormat } from 'openai/helpers/zod.mjs';
        import { z } from "zod";

        const client = new OpenAI({
          baseURL: 'https://api.linkup.so/v1',
          apiKey: "<YOUR API KEY>"
        });

        const NobelWinners = z.object({
          winners: z.array(
            z.object({
              name: z.string(),
              year: z.string(),
            })
          )
        });

        const response = await client.responses.create({
          model: "linkup-standard",
          input: "Can you tell me which women were awarded the Physics Nobel Prize",
          text: {
            format: zodTextFormat(NobelWinners, "winners"),
          }
        });

        console.log(response.output_text);
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Python SDK
Source: https://docs.linkup.so/pages/sdk/python/python

How to use Linkup Python SDK natively in your apps.

## Introduction

The Python SDK allows for easy interaction with the Linkup API, offering the full range of our search functionality. Easily integrate smart search capabilities into your applications, harnessing Linkup’s powerful search features.
You can use our [playground](https://app.linkup.so/playground) to have interactive examples and see how to implement them with the SDK.

<CardGroup>
  <Card title="Github" icon="github" href="https://github.com/LinkupPlatform/linkup-python-sdk">
    Repository (feel free to contribute)
  </Card>

  <Card title="PyPi" icon="python" href="https://pypi.org/project/linkup-sdk/">
    PyPi page
  </Card>
</CardGroup>

## Quickstart

Get started with our Python SDK in less than 5 minutes!

<Card title="Get your API key" icon="key" href="https://app.linkup.so">
  Create a Linkup account for free to get your API key.
</Card>

## Installation

You can install the Linkup Python SDK as any Python package, for instance using `pip`:

```shell theme={null}
pip install linkup-sdk
```

## Usage

Here is a basic usage example showing how to use the Linkup Python SDK:

```python theme={null}
from linkup import LinkupClient

client = LinkupClient(
    api_key="<your-api-key>", # Or set the LINKUP_API_KEY environment variable
)

# Perform a search query
search_response = client.search(
    query="What are the 3 major events in the life of Abraham Lincoln?",
    depth="deep",
    output_type="sourcedAnswer",
)
print(search_response)

# Fetch the content of a web page
response = client.fetch(
    url="https://docs.linkup.so",
)
print(response)
```

### Search parameters

| Parameter                  | Type                                                             | Description                                                                                          | Default  |
| -------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------- |
| query                      | `str`                                                            | The input query                                                                                      | Required |
| depth                      | `typing.Literal["standard", "deep"]`                             | The depth of the search                                                                              | Required |
| output\_type               | `typing.Literal["searchResults", "sourcedAnswer", "structured"]` | The desired output type                                                                              | Required |
| structured\_output\_schema | `pydantic.BaseModel`, `str` or `None`                            | The desired schema for the output, if `output_type` is `structured`                                  | `None`   |
| include\_images            | `datetime.bool` or `None`                                        | Whether to include images in the search                                                              | `None`   |
| from\_date                 | `datetime.date` or `None`                                        | The date from which the search results should be considered                                          | `None`   |
| to\_date                   | `datetime.date` or `None`                                        | The date until which the search results should be considered                                         | `None`   |
| exclude\_domains           | `list[str]` or `None`                                            | The domains to exclude from the search                                                               | `None`   |
| include\_domains           | `list[str]` or `None`                                            | The domains to restrict the search with                                                              | `None`   |
| include\_inline\_citations | `bool` or `None`                                                 | Whether to include inline citations in the answer, if `output_type` is `sourcedAnswer`               | `None`   |
| include\_sources           | `bool` or `None`                                                 | Whether to include the sources, if `output_type` is `structured` (modifies the schema of the output) | `None`   |
| max\_results               | `int` or `None`                                                  | Maximum number of results to return                                                                  | `None`   |

#### Query

The `query` parameter is the core input string that defines your search intent. It represents the question or information request that you want Linkup to answer. How you formulate this query significantly impacts the quality and relevance of results.

Effective queries should be:

* **Clear and specific**: "What were the key findings of NASA's James Webb telescope in 2023?" provides better results than "Tell me about space discoveries"
* **Contextually rich**: Include relevant context when needed ("What are the environmental impacts of lithium mining for EV batteries?")
* **Naturally phrased**: Write as you would ask a knowledgeable person, not with keywords

For optimal results, consider reviewing our [prompting guide](https://docs.linkup.so/pages/documentation/tutorials/prompting-guide), which provides detailed strategies for crafting effective queries.

#### Depth

The `depth` field is used to select the type of search you want to perform:

* **standard**: the search will be straightforward and fast, suited for relatively simple queries (e.g. "What's the weather in Paris today?")
* **depth**: the search will use an agentic workflow, which makes it in general slower, but it will be able to solve more complex queries (e.g. "What is the company profile of LangChain accross the last few years, and how does it compare to its concurrents?")

#### Output type

The type of output which is expected:

* **sourcedAnswer**: Provides a comprehensive natural language answer to the query along with citations to the source material. Ideal for when you need well-formed responses with verifiable information and transparent sourcing.
* **searchResults**: Returns the raw search context data without synthesis, giving you direct access to the underlying information. Useful for custom processing, or when you need to implement your own answer generation logic.
* **structured**: Allows you to receive responses in a custom format based on the format provided in
  `structured_output_schema`. If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

#### Structured output schema

Linkup’s structured output feature allows you to receive responses in a custom format that you define. This is particularly useful when you need to integrate Linkup’s responses directly into your application’s data structure or when you want to ensure consistency in the response format.
To do that, you have to use the `structured_output_schema` field. Supported formats are a pydantic.BaseModel or a string representing a valid object JSON schema.
If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

#### Include images

The `include_images` parameter allows you to receive image results alongside text results in your search responses. When set to `True`, Linkup will return relevant images related to your query, each with a URL and metadata. This is particularly useful for:

* Creating visual search experiences
* Building content that combines text and images
* Researching topics where visual information is important

Image results are returned with the same structure as text results but with `type: "image"`.

#### From date

The `from_date` parameter filters search results to only include content published after the specified date. This helps you:

* Focus on recent information
* Exclude outdated content

The date should be a `datetime.date` type, for example: `datetime.date(2025, 3, 1)`.

#### To date

The `to_date` parameter complements `from_date` by restricting search results to only include content published or updated before the specified date. This is useful for:

* Historical research on specific time periods
* Analyzing content published within a specific date range
* Avoiding more recent information that might skew results

Like `from_date`, the date should be a `datetime.date` type, for example: `date(2025, 3, 15)`.

When used together, `from_date` and `to_date` create a date range filter for your search results.

#### Exclude domains

The `exclude_domains` parameter allows you to specify a list of domains that should be excluded from the search results. This is useful for:

* Filtering out unwanted sources
* Avoiding results from specific domains that may not be relevant or trustworthy.

#### Include domains

The `include_domains` parameter allows you to specify a list of domains that must be included in the search results. This is useful for:

* focus on specific sources
* ensure that results come from trusted domains.

#### Include inline citations

The `include_inline_citations` parameter is specifically designed for use with the `sourcedAnswer` output type. When enabled, it embeds citations directly within the answer text, making it easier to identify which parts of the response correspond to specific sources. This is particularly useful for:

* Academic or research applications where source attribution is critical
* Creating content that needs verifiable claims with clear sourcing
* Building applications where users need to quickly verify information

When `include_inline_citations` is set to `True`, the answer will contain inline references like \[1], \[2] that correspond to the sources in the response.

#### Include sources

The `include_sources` parameter is specifically designed for use with the `structured` output type. When enabled, it modifies the schema of the structured response to include source information alongside your custom data structure. This is particularly useful for:

* Applications that need both structured data and source attribution
* Building systems that require traceability of information
* Creating responses where you want to maintain both custom format and source verification

When `include_sources` is set to `True`, the response will be wrapped in a `LinkupSearchStructuredResponse` object containing both your structured data and source information.

### maxResults

The `maxResults` parameter allows you to specify the maximum number of results to return. This is useful for:

* Limiting the number of results returned
* Reducing the context size

### Fetch parameters

| Parameter          | Type             | Description                                          | Default  |
| ------------------ | ---------------- | ---------------------------------------------------- | -------- |
| url                | `str`            | The URL of the web page to fetch                     | Required |
| include\_raw\_html | `bool` or `None` | Whether to include the raw HTML in the response      | `None`   |
| render\_js         | `bool` or `None` | Whether the API should render JavaScript on the page | `None`   |

#### URL

The `url` parameter specifies the web page URL that you want to fetch content from. This should be a fully qualified URL including the protocol (http\:// or https\://). The fetch endpoint will retrieve the page content and return it in a cleaned up mardown, making it easy to process the web page by AI agents or other applications.

#### Include raw HTML

The `include_raw_html` parameter controls whether the raw HTML source code of the web page is included in the response alongside the cleaned up markdown content. This is useful for applications that need to perform custom HTML parsing, preserve specific formatting, or access elements that might be filtered out during the standard content extraction process.

#### Render JS

The `render_js` parameter determines whether JavaScript should be executed when fetching the web page. When set to `True`, the API will render the page in a browser-like environment, executing JavaScript code and waiting for dynamic content to load before extracting the content. This is essential for modern web applications that rely heavily on JavaScript for content generation, such as single-page applications (SPAs) or pages with dynamically loaded content, but induces additional latency.

## Examples

<AccordionGroup>
  <Accordion title="Last Formula 1 race" description="Standard example" icon="flag">
    <p>This example show you how to combine the standard search with a sourced answer</p>

    ```python theme={null}
    from linkup import LinkupClient

    client = LinkupClient()

    search_response = client.search(
        query="Last Formula 1 race",
        depth="standard",
        output_type="sourcedAnswer",
    )
    print(search_response)
    ```

    Example response:

    ```python theme={null}
    answer='The last Formula 1 race was the Australian Grand Prix, where Lando Norris won. The race took place recently, and it was marked by intermittent rain causing several challenges on the track. The next race is the Chinese Grand Prix, scheduled for March 21-23, 2025.'
    sources=[
      LinkupSource(name='Formula 1 season begins with dramatic Australian Grand Prix', url='https://www.emorywheel.com/article/2025/03/pivexulgpch8', snippet='The Australian Grand Prix was a thrilling way to start the 2025 F1 season for the many fans eager to have F1 back after the long winter break. The excitement will continue with the Chinese Grand Prix, the first sprint race of the season, in Shanghai on March 21-23.', favicon='https://www.emorywheel.com/wp-content/uploads/2023/09/cropped-Emory-Wheel-Favicon-32x32.png'),
      LinkupSource(name="AUTO RACING: Bell's three-race win streak snapped and Norris takes the F1 season opener", url='https://www.washingtonpost.com/sports/auto-racing/2025/03/18/auto-racing-glance/414c4f32-0419-11f0-941f-6ca83a0bd35b_story.html', snippet='Schedule: Saturday, practice, 1:05 p.m., qualifying, 2:10 p.m.; Sunday, race, 3 p.m. (FS1). Track: Homestead-Miami Speedway. Race distance: 267 laps, 400.5 miles. Last year: Tyler Reddick secured the win from the pole after a last-lap pass of Ryan Blaney.', favicon='https://www.washingtonpost.com/wp-stat/assets/favicon-32x32.png'),
      LinkupSource(name='F1 Australian Grand Prix 2025 results: Norris wins, rookies spin out in the rain', url='https://www.yahoo.com/lifestyle/f1-australian-grand-prix-2025-083408114.html', snippet='Intermittent rain caused havoc on the track before and during the 2025 F1 Australian Grand Prix. The post F1 Australian Grand Prix 2025 results: Norris wins, rookies spin out in the rain appeared first on The Manual.', favicon='https://s.yimg.com/rz/l/favicon.ico'),
      ...
    ]
    ```
  </Accordion>

  <Accordion title="Company Revenue" description="Deep + structured output" icon="building">
    <p>This example shows you how to use the deep with a relative complexe structured output:</p>

    ```python theme={null}
    from linkup import LinkupClient

    client = LinkupClient(api_key="YOUR_API_KEY")

    schema = """{
        "type": "object",
        "properties": {
            "companyName": {
                "type": "string",
                "description": "The name of the company"
            },
            "revenueAmount": {
                "type": "number",
                "description": "The revenue amount"
            },
            "fiscalYear": {
                "type": "string",
                "description": "The fiscal year for this revenue"
            }
        }
    }"""

    response = client.search(
        query="What is Microsoft's 2024 revenue?",
        depth="deep",
        output_type="structured",
        structured_output_schema=schema
    )

    print(response)
    ```

    Example response:

    ```json theme={null}
    {
        "companyName": "Microsoft",
        "revenueAmount": 245100000000,
        "fiscalYear": "2024"
    }
    ```
  </Accordion>

  <Accordion title="Latest politic news" description="Search results as outputType" icon="newspaper">
    <p>This example shows you how to use the standard with a search results:</p>

    ```python theme={null}
    from linkup import LinkupClient

    client = LinkupClient(api_key="YOUR_API_KEY")

    search_response = client.search(
        query="Latest politic news",
        depth="standard",
        output_type="searchResults",
    )

    print(search_response)
    ```

    Example response:

    ```python theme={null}
    results=[
      LinkupSearchTextResult(type='text', name='CNN host Van Jones shares personal upbringing, reflects on state of American politics', url='https://www.browndailyherald.com/article/2025/03/cnn-host-van-jones-shares-personal-upbringing-reflects-on-state-of-american-politics', content='On Wednesday night, the Watson Institute for International and Public Affairs welcomed CNN Host Van Jones for a conversation on the state of American politics. In his talk, Jones explained increasingly strained ties between Jewish and Black activist communities,', favicon='https://www.browndailyherald.com/wp-content/uploads/2023/09/cropped-BDH-Favicon-32x32.png'),
      LinkupSearchTextResult(type='text', name='Politics latest: Billions being shaved off welfare bill - join our live Q&A on what it means for you', url='https://news.sky.com/story/politics-latest-trump-wants-to-shock-europe-into-action-with-false-ukraine-claims-says-boris-johnson-12593360', content='Work and Pensions Secretary Liz Kendall has announced changes to the welfare system - including merging some benefits and a plan to scrap the work capability assessment used to claim universal credit.', favicon='https://e1.365dm.com/21/03/1600x900/skysports-politics-latest-live_5311164.jpg?20210310123112'),
      LinkupSearchTextResult(type='text', name='Politics', url='https://www.npr.org/sections/politics/', content="March 19, 2025 • The decision offers a venue compromise in the bellwether case, while Khalil's legal team seeks to release him from detention and block his deportation.", favicon='https://media.npr.org/favicon.ico'),
      ...
    ]
    ```
  </Accordion>

  <Accordion title="Amazon deforestation" description="IncludeImages filter" icon="trees">
    <p>This example return text and images sources</p>

    ```python theme={null}
    from linkup import LinkupClient

    client = LinkupClient(api_key="YOUR_API_KEY")

    search_response = client.search(
        query="Amazon deforestation",
        depth="standard",
        output_type="searchResults",
        include_images=True
    )

    print(search_response)
    ```

    Exemple response

    ```python theme={null}
    results=[
      LinkupSearchTextResult(type='text', name='How a grassroots financing model is helping Indigenous communities save the Amazon', url='https://www.unep.org/news-and-stories/story/how-grassroots-financing-model-helping-indigenous-communities-save-amazon', content='A United Nations effort is channeling more finance to communities to help them conserve, restore and sustainably manage forests.', favicon='https://www.unep.org/sites/all/themes/custom/unep/favicon.ico'),
      LinkupSearchTextResult(type='text', name='Amazon Rainforest Razed To Build Highway For UN Climate Summit', url='https://ijr.com/amazon-rainforest-razed-to-build-highway-for-un-climate-summit/', content='Ahead of the COP30 climate summit in Belém, Brazil, developers are carving a four-lane highway through protected tracts of the', favicon='https://ijr.com/wp-content/uploads/2021/08/cropped-ijr-favicon-32x32.png'),
      LinkupSearchTextResult(type='text', name='Roads less traveled multiply deforestation in the Amazon and beyond', url='https://www.msn.com/en-us/news/world/roads-less-traveled-multiply-deforestation-in-the-amazon-and-beyond/ar-AA1AGYEe', content='James Cook University-led research has revealed secondary roads branching from major highways in tropical forests linked to extensive deforestation across the Brazilian Amazon, the Congo Basin, and New Guinea.', favicon='https://static.msn.com/favicon.ico'),
      ...
      LinkupSearchImageResult(type='image', name='Amazon Fires and the Horrifying Science of Deforestation | WIRED', url='https://media.wired.com/photos/5d6027925af21f000859fc13/master/w_2000,c_limit/Science_AmazonASAP_1125307709.jpg'),
      LinkupSearchImageResult(type='image', name='Deforestation In The Amazon Rainforest | emr.ac.uk', url='https://en.mercopress.com/data/cache/noticias/73326/0x0/1-88.jpg'),
      LinkupSearchImageResult(type='image', name='Amazon Deforestation WWF - Green Queen', url='https://www.greenqueen.com.hk/wp-content/uploads/2020/06/Amazon-Deforestation-WWF.jpg'),
      ...
    ]
    ```
  </Accordion>

  <Accordion title="AI Avancements" description="Dates filtering" icon="calendar">
    <p>This example shows you how to use the dates filter:</p>

    ```python theme={null}
    from linkup import LinkupClient
    from datetime import date

    client = LinkupClient(api_key="YOUR_API_KEY")

    search_response = client.search(
        query="What are the recent advancements in artificial intelligence technology",
        depth="standard",
        output_type="sourcedAnswer",
        from_date=date(2025, 3, 1),
        to_date=date(2025, 3, 5),
    )

    print(search_response)
    ```

    Example response:

    ```python theme={null}
    answer='1. A call for a new approach to achieve human-level reasoning in AI systems has been highlighted by researchers. [Read more](https://www.nature.com/articles/d41586-025-00649-4).\n\n2. The release of DeepSeek, an AI chatbot, has raised new cybersecurity concerns. [Read more](https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/).\n\n3. AI continues to transform everyday life, influencing communication, work, and leisure activities. [Read more](https://signalscv.com/2025/03/how-technology-is-changing-our-everyday-life-from-ai-to-the-internet-of-things/).\n\n4. The integration of AI with other technologies is driving innovation and growth in business sectors. [Read more](https://www.independent.com.mt/articles/2025-03-02/newspaper-opinions/The-intersection-of-technology-and-business-Paving-the-way-for-innovation-and-growth-6736268254).'
    sources=[
      LinkupSource(name='How AI can achieve human-level intelligence: researchers call for change in tack', url='https://www.nature.com/articles/d41586-025-00649-4', snippet='Artificial intelligence (AI) systems with human-level reasoning are unlikely to be achieved through the approach and technology ... Heights, New York, who spearheaded the survey in her role as president of the Association for the Advancement of Artificial ...', favicon='https://media.nature.com/lw1024/magazine-assets/d41586-025-00649-4/d41586-025-00649-4_17996430.png'),
      LinkupSource(name='DeepSeek Sparks New Cyber Challenges In the AI Chatbot Era', url='https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/', snippet='This article discusses DeepSeek, an artificial intelligence chatbot that was released in January of this year, and the concerns it raises around security and rapidly advancing technology.', favicon='https://www.law.com/img/NYLJ/favicon.ico'),
      LinkupSource(name='How Technology is Changing Our Everyday Life: From AI to the Internet of Things', url='https://signalscv.com/2025/03/how-technology-is-changing-our-everyday-life-from-ai-to-the-internet-of-things/', snippet='Technology has revolutionized our lives, transforming how we communicate, work, shop, and even unwind. In a world driven by rapid innovation, technologies like artificial intelligence (AI), the Internet of Things', favicon='https://signalscv.com/wp-content/uploads/2023/01/cropped-Signals-favicon-32x32.png'),
      ...
    ]
    ```
  </Accordion>
</AccordionGroup>

## Additional ressources

### Prompting guide

We strongly recommend you to read our [prompting guide](https://docs.linkup.so/pages/documentation/tutorials/prompting-guide) to best prompt the Linkup API and get optimal results. Even small improvements in how you structure your prompts can dramatically enhance the quality of responses and the overall user experience.

### Structured output guide

We strongly recommend you to read our [structured output guide](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide) to ensure consistency in the response format. Mastering structured outputs allows you to fully leverage Linkup's capabilities while maintaining complete control over how the information is presented and processed in your application.

### Tutorials

Don't hesitate to [check our tutorials](https://docs.linkup.so/pages/documentation/tutorials/signup-radar) for other ideas of what to build with Linkup!

And voilà ! You're now ready to implement the Linkup SDK inside your fabulous project ! 🚀

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


# Data Privacy
Source: https://docs.linkup.so/pages/security-and-privacy/data-privacy



Linkup Technologies takes data privacy and security seriously. As a search API provider serving enterprise clients across financial services, consulting, and technology sectors, we've successfully completed rigorous vendor security assessments and maintain compliance with strict regulatory requirements.

Our Data Protection Officer (DPO) oversees compliance with the EU's General Data Protection Regulation (GDPR), ePrivacy Directive, the California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA), and other applicable data protection laws. The DPO participates in privacy impact assessments, manages data subject rights requests, and ensures our privacy policies remain current and compliant. Linkup adopts GDPR as our baseline standard for data protection globally, adapting our approach where necessary for specific jurisdictions and regulatory frameworks.

We act as a Data Processor for our clients and are prepared to execute Data Processing Agreements (DPAs) that clearly define our data handling responsibilities and your rights as a Data Controller. A DPA can be signed upon request and aligns with GDPR Article 28 requirements.

## Zero Data Retention (ZDR)

<Callout>
  Privacy is built into our architecture from the ground up. Our Zero Data Retention (ZDR) option ensures that search queries and results are never stored.
</Callout>

When ZDR is enabled:

* **No query logging**: Search queries are not logged or stored on our systems.
* **No result retention**: Results are not retained after delivery to the client.

### How it works

ZDR requests are processed in temporary computing environments where all data is held only in RAM (memory) during processing.
No data is written to persistent storage. Once the search results are returned, all temporary data is automatically destroyed and cannot be recovered.

### When to use ZDR

ZDR is particularly valuable for clients in highly regulated industries or those handling sensitive competitive intelligence, where even temporary storage poses compliance or confidentiality risks. ZDR can be enabled on demand — contact us for details.

## Contact

For privacy requests please contact `support@linkup.so`.

## Documentation links

* **Trust Center**: [View here](https://trust.linkup.so/)
* **Privacy Policy**: [View here](https://www.linkup.so/privacy-policy)
* **Data Processing Agreement**: <a href="https://linkupinfrastorageprod.blob.core.windows.net/docs/template-data-processing-agreement-linkup.pdf?sp=r&st=2025-11-02T20:06:27Z&se=2026-11-02T20:06:27Z&spr=https&sv=2024-11-04&sr=b&sig=H9aaPYptcd68eYVHzifxDXIf9FLL9cX4%2FRVd2D2K5tI%3D">Download here</a>
* **Terms and Conditions**: [View here](https://linkup-platform.notion.site/Linkup-Client-General-Terms-and-Conditions-13f161ecef69806784dfe808b4e162a1)


# Frequently Asked Questions
Source: https://docs.linkup.so/pages/security-and-privacy/faq



<AccordionGroup>
  <Accordion title="Where is my data stored and processed?">
    All data processing occurs exclusively within the EU, ensuring compliance with EU data residency requirements and GDPR. We can accommodate specific regional requirements for global clients.
  </Accordion>

  <Accordion title="Do you offer Zero Data Retention (ZDR)?">
    Yes. When enabled, Zero Data Retention ensures that no search queries or results are stored.
  </Accordion>

  <Accordion title="Can you sign a Data Processing Agreement (DPA)?">
    Yes. We act as a Data Processor under GDPR and are prepared to execute DPAs that align with GDPR Article 28 requirements. Our DPA template is available upon request and clearly defines data handling responsibilities.
  </Accordion>

  <Accordion title="What certifications do you hold?">
    We are SOC 2 Type II certified. Our SOC 2 report is available upon request. We also undergo quarterly vulnerability scanning and annual penetration testing by independent third parties.
  </Accordion>

  <Accordion title="How quickly will you notify us of a security incident?">
    We commit to notifying affected clients within 72 hours of confirming a security incident that impacts client data, with 24‑hour capability for critical incidents. Our Security Incident Management Policy defines escalation procedures and response timelines.
  </Accordion>

  <Accordion title="Can you exclude specific domains or websites from search results?">
    Yes. We offer flexible content filtering through our <code>ExcludeDomains</code> API parameter, allowing you to exclude specific domains, competitors, or content sources from search results. Custom exclusion lists can be configured per API key for enterprise clients.
  </Accordion>

  <Accordion title="What subprocessors or third parties do you use?">
    We use a limited number of carefully vetted subprocessors, primarily Microsoft Azure (infrastructure) and Google Workspace (internal operations). All subprocessors are SOC 2 certified. A complete subprocessor list is available upon request.
  </Accordion>

  <Accordion title="How do you prevent crawling malicious or inappropriate content?">
    Our AI-powered content filtering identifies and blocks malicious content, malware distribution sites, phishing sites, adult content, and sensitive personal information before indexing or delivery. We respect robots.txt directives and ethical crawling standards, and never circumvent access controls or authentication.
  </Accordion>

  <Accordion title="What is your data retention policy?">
    Standard retention is 3 years after last interaction for business continuity. Upon contract termination or written request, all customer data is securely purged within 30 days from primary storage and 90 days from backups. Custom retention periods (including immediate deletion with ZDR) can be established based on client requirements.
  </Accordion>

  <Accordion title="How do you handle vulnerability management?">
    We conduct quarterly vulnerability scans through Bastion Technologies and annual penetration testing. Remediation follows defined SLAs: Critical/High (30 days), Medium (60 days), Low (90 days).
  </Accordion>

  <Accordion title="What encryption standards do you use?">
    All data in transit uses TLS 1.2+ encryption, and data at rest is protected with AES‑256 encryption. Encryption keys are managed through enterprise key management services with strict access controls.
  </Accordion>

  <Accordion title="Can you crawl content behind paywalls or login walls?">
    No. We only index and provide publicly available content. We do not access content behind authentication, paywalls, or registration requirements, in accordance with our Acceptable Use Policy and ethical crawling standards.
  </Accordion>

  <Accordion title="Do you perform background checks on employees?">
    Yes. Background checks are performed on all newly hired employees where permitted by law. All employees and contractors must sign confidentiality agreements and acknowledge our security policies.
  </Accordion>

  <Accordion title="Can you accommodate custom security requirements for enterprise clients?">
    Yes. While our standard security controls meet industry benchmarks, we work with enterprise partners to customize incident notification timelines, vulnerability remediation SLAs, compliance reporting, data handling configurations (like ZDR or domain exclusions), and contract terms to align with your specific security and regulatory requirements.
  </Accordion>
</AccordionGroup>


# Policies
Source: https://docs.linkup.so/pages/security-and-privacy/policies



Linkup maintains a comprehensive set of security and operational policies as part of our Information Security Management System (ISMS). These policies are regularly reviewed and updated to reflect current best practices and regulatory requirements. Policy documentation is available upon request for qualified prospects and clients.

## Core security policies

| Policy                                         | Description                                                                                                                                    |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Information Security Policy                    | Defines governance, security objectives, risk management framework, and responsibilities for protecting company and client assets.             |
| Data Classification & Handling Policy          | Establishes classification levels (Public, Internal, Confidential, Restricted) and handling, storage, transmission, and disposal requirements. |
| Access Control Policy                          | Covers user access management, RBAC, privileged access, access review procedures, and account lifecycle management.                            |
| Incident Response & Management Policy          | Procedures for detecting, reporting, responding to, and recovering from incidents; includes notification timelines and escalation.             |
| Business Continuity & Disaster Recovery Policy | Strategies and procedures to maintain operations during disruptions and recover systems/data (defined RTOs/RPOs).                              |
| Data Retention & Deletion Policy               | Retention periods by data type; secure disposal procedures, including Zero Data Retention (ZDR) capabilities.                                  |
| Change Management Policy                       | Processes for planning, testing, approving, and implementing changes to minimize risk and maintain stability.                                  |
| Vulnerability Management Policy                | Identification, assessment, prioritization, and remediation via scanning, pen testing, and patching with SLAs by severity.                     |
| Backup & Recovery Policy                       | Backup frequency, retention, storage, encryption, and testing to ensure recoverability.                                                        |
| Vendor & Third-Party Risk Management Policy    | Requirements to assess, onboard, and monitor vendors/service providers against security and compliance standards.                              |
| Acceptable Use Policy                          | Appropriate and prohibited use of Linkup systems, data, and resources by employees and authorized users.                                       |
| Encryption & Cryptography Policy               | Encryption standards for data at rest/in transit, key management procedures, and approved algorithms/protocols.                                |

## Additional policies

Additional specialized policies covering physical security, human resources security, network security, secure development, privacy management, and other areas are maintained as part of our comprehensive ISMS and are available upon request.

## Accessing policy documents

To request specific policies or attestations, contact `support@linkup.so`.


# Security
Source: https://docs.linkup.so/pages/security-and-privacy/security



Linkup Technologies implements enterprise-grade security controls to protect our infrastructure, services, and client data. Our security program is designed to meet the stringent requirements of clients in highly regulated industries including financial services, consulting, and healthcare.

<Card title="Trust Center" icon="shield" href="https://trust.linkup.so/">
  Visit Linkup's Trust Center
</Card>

​

## Certifications and compliance

* **SOC 2 Type II** certification validating security, availability, and confidentiality controls (report available upon request).

## Data encryption

* **In transit**: TLS 1.2+ for all API communications.
* **At rest**: AES-256 for any stored data.
* **Key management**: Enterprise key management services with strict access controls.

## Infrastructure security

* **Cloud infrastructure**: Hosted on enterprise-grade cloud platforms.
* **Network security**: VPC segregation, network segmentation via security groups and ACLs, multi-layer firewalls, DDoS protection, and no public database endpoints.
* **Hardening**: Baseline configurations, timely patching, and least-privilege service roles.

## Privileged access management

<Callout type="success" icon="check" title="RBAC + MFA">
  Privileged and administrative access requires multi‑factor authentication with strict role‑based access control.
</Callout>

<Callout type="success" icon="check" title="Monitored privileged access">
  All privileged access is logged, continuously monitored, and regularly reviewed.
</Callout>

<Callout type="success" icon="check" title="Least privilege & JIT">
  Access follows least‑privilege principles with just‑in‑time elevation where applicable.
</Callout>

## Vulnerability management and secure development

<Callout type="success" icon="check" title="Quarterly vulnerability scanning">
  Independent scans (Bastion Technologies) with tracked remediation.
</Callout>

<Callout type="success" icon="check" title="Annual penetration testing">
  Independent assessors validate controls and exploit paths.
</Callout>

<Callout type="success" icon="check" title="Continuous monitoring">
  Automated threat detection and alerting across infrastructure and apps.
</Callout>

<Callout type="success" icon="check" title="Remediation SLAs">
  Defined timelines by severity for fast, predictable fixes.
</Callout>

<Callout type="success" icon="check" title="Security‑by‑design SDLC">
  Design reviews, code scanning, dependency checks, and secure API patterns.
</Callout>

<Callout type="success" icon="check" title="Staff security training">
  Regular training to maintain security awareness and best practices.
</Callout>

## Malware and threat prevention (crawling safeguards)

<Callout type="success" icon="check" title="AI‑powered filtering">
  Blocks malware, phishing, and malicious sources before indexing or serving.
</Callout>

<Callout type="success" icon="check" title="Result curation safeguards">
  Ranking protects against sensitive and prohibited content exposure.
</Callout>

<Callout type="success" icon="check" title="Web filtering & DNS security">
  High‑risk sites are automatically blocked.
</Callout>

<Callout type="success" icon="check" title="Configurable domain exclusions">
  Control results via the <code>ExcludeDomains</code> API parameter.
</Callout>

<Callout type="success" icon="check" title="Ethical crawling standards">
  Respect for <code>robots.txt</code>; no circumvention of CAPTCHAs or access controls.
</Callout>

Enterprise customization available: We can accommodate custom breach notification timelines, tailored remediation SLAs, dedicated security reviews, and bespoke compliance reporting.


