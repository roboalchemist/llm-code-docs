# Search Domain Filter

Source: https://docs.perplexity.ai/docs/search/filters/domain-filter

<Note>
  The `search_domain_filter` parameter allows you to limit search results to specific domains or exclude certain domains from search results. This supports domain-level filtering for precise content control.
</Note>

<Warning>
  You can add a maximum of 20 domains to the `search_domain_filter` list. The filter works in either allowlist mode (include only) or denylist mode (exclude), but not both simultaneously.
</Warning>

<Info>
  Domain filters allow you to specify which domains to include or exclude in search results. You can filter by specific domains, top-level domains (TLDs), or domain parts. You can specify up to 20 domains per request. Domains should be provided without the protocol (e.g., "nature.com" not "[https://nature.com](https://nature.com)").
</Info>

## Overview

The domain filter for the Search API allows you to control which sources appear in your search results by limiting them to specific domains or excluding certain domains. This is particularly useful when you need to:

* Focus research on authoritative or trusted sources
* Filter out specific domains from search results
* Search within specific publication networks or organizations
* Build domain-specific search applications
* Conduct competitive research within specific industry domains

The `search_domain_filter` parameter accepts an array of domain strings. The filter operates in two modes:

* **Allowlist mode**: Include only the specified domains (no `-` prefix)
* **Denylist mode**: Exclude the specified domains (use `-` prefix)

```bash theme={null}
