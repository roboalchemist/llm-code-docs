# Source: https://docs.linkup.so/pages/documentation/get-started/concepts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Concepts

> Key concepts to understand how Linkup works

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


Built with [Mintlify](https://mintlify.com).