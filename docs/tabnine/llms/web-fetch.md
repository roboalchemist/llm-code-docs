# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/web-fetch.md

# Web Fetch

### What Web Fetch Does <a href="#what-web-fetch-does" id="what-web-fetch-does"></a>

The Web Fetch tool allows the Tabnine Agent to retrieve content from specific web pages, analyze it, and use that information when responding to your requests. It is especially useful when you need documentation or API references that exist only on public websites, recent blog posts, changelogs, or release notes, or examples, tutorials, or configuration snippets from public documentation or blogs.

When Web Fetch is enabled, the agent can decide to use it automatically when your prompt contains one or more URLs and the task clearly depends on information that is not already available in your local context or configured tools. The fetched content is then summarized, filtered for relevance, and incorporated into the agent’s response.

When using Web Fetch, the agent prefers technical documentation and references over marketing or promotional sections of the same page. Web Fetch is not a general‑purpose web crawler; it only reads the URLs you provide and may sometimes follow obvious “next” or “previous” links in the same documentation flow.

### Usage Examples <a href="#usage-examples" id="usage-examples"></a>

You don’t need to “call” the Web Fetch tool directly; you just:

1. Ask your question in natural language, *and*
2. Include one or more URLs that the agent should use.

#### Example prompts:

* “Read the documentation at this URL and tell me how to configure OAuth: `<https://example.com/docs/oauth`.”>
* “Compare the breaking changes between version 5.0 and 6.0 in the framework’s release notes at these URLs.”
* “Use this tutorial to create a minimal working example for my project: `<https://example.com/blog/tutorial`.”>
* “Check this API reference page and generate a sample cURL request for the `createUser` endpoint.”

When you provide URLs, the agent will decide whether Web Fetch is needed, retrieve the page content, then summarize and extract the details relevant to your instructions.\
If Web Fetch is disabled or cannot access the URL, the agent will fall back to its existing context and will note that web content could not be retrieved when this affects the answer.

#### Technical Reference <a href="#technical-reference" id="technical-reference"></a>

**Arguments**

The Web Fetch tool takes a single structured request that includes:

* A natural language instruction (what you want done with the pages), and
* A list of one or more URLs to fetch.

Recommended constraints:

* No more than 20 URLs per request.
* Start URLs with `<http://`> or `<https://`.>

**Example (Conceptual Schema)**

```json
{
  "prompt": "Summarize the authentication section and list all required headers.",
  "urls": [
    "https://example.com/docs/api/authentication"
  ]
}
```
