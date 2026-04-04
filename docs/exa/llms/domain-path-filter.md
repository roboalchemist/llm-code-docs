# Source: https://exa.ai/docs/changelog/domain-path-filter.md

> **Documentation Index**
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain Path Filter Support

> `includeDomains` and `excludeDomains` now support URL path filtering and subdomain wildcards.

***

**Date: August 4, 2025**

## What's New

The `includeDomains` and `excludeDomains` parameters now support:

* **Path-specific filtering**: Target specific sections of a domain by including the path
* **Subdomain wildcard matching**: Use `*.domain.com` to match all subdomains

## Examples

| Pattern                  | What it matches                 | Example URLs                                                          |
| ------------------------ | ------------------------------- | --------------------------------------------------------------------- |
| `"*.substack.com"`       | Any subdomain of substack.com   | `https://thehobbyist.substack.com/p/location-matters-6-days-273-bets` |
| `"exa.ai/blog"`          | Only the blog section of exa.ai | `https://exa.ai/blog/meet-the-exacluster`                             |
| `"linkedin.com/company"` | Company profiles on LinkedIn    | `https://www.linkedin.com/company/exa-ai`                             |

## When to Use Path Filtering

Path filtering is useful for things like:

1. **Blogs**: Search within blogs like `stripe.com/blog`, `openai.com/blog`, or `stratechery.com/2025`
2. **Product Catalogs**: Query product pages like `amazon.com/dp`, `etsy.com/listing`, or `ikea.com/us/en/cat`
3. **Directories**: Search specific directories like `ycombinator.com/companies`, `crunchbase.com/organization`, or `github.com/orgs`

## How To Use Path Filtering

You can use the same `includeDomains` and `excludeDomains` parameters:

<CodeGroup>
  ```python Python theme={null}
  result = exa.search_and_contents(
      "gradient descent",
      type="auto",
      livecrawl="never",
      includeDomains=["https://explained.ai", "https://huggingface.co/blog"],
      num_results=10
  )
  ```

  ```javascript JavaScript theme={null}

  const result = await exa.searchAndContents(
      "gradient descent",
      {
          type: "auto",
          livecrawl: "never",
          includeDomains: ["https://explained.ai", "https://huggingface.co/blog"],
          numResults: 10
      }
  );
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.exa.AI/search \
    -H "x-api-key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "gradient descent",
      "type": "auto",
      "includeDomains": ["https://explained.ai", "https://huggingface.co/blog"],
      "numResults": 10
    }'
  ```
</CodeGroup>

## Need Help?

If you have any questions about domain filtering or need help with your specific use case, please reach out to [hello@exa.ai](mailto:hello@exa.ai).
