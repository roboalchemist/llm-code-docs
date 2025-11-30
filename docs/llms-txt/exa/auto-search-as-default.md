# Source: https://docs.exa.ai/changelog/auto-search-as-default.md

# Auto search as Default

> Auto search, which intelligently combines Exa's proprietary neural search with other search methods, is now the default search type for all queries.

***

The change to Auto search as default leverages the best of Exa's proprietary neural search and other search methods to give you the best results. Out of the box, Exa now automatically routes your queries to the best search type.

<Info>
  Read our documentation on Exa's different search types [here](/reference/exas-capabilities-explained).
</Info>

## What This Means for You

1. **Enhanced results**: Auto search automatically routes queries to the most appropriate search method, optimizing your search results without any extra effort on your part.
2. **No Action required**: If you want to benefit from Auto search, you don't need to change anything in your existing implementation. It'll just work!
3. **Maintaining current behavior**: If you prefer to keep your current search behavior, you can still explicitly set `type="neural"` in your search requests.

## Quick Example

Here's what this means for your code when default switches over:

```Python Python theme={null}
# New default behavior (Auto search)
result = exa.search_and_contents("hottest AI startups")

# Explicitly use neural search
result = exa.search_and_contents("hottest AI startups", type="neural")
```

We're confident this update will significantly improve your search experience. If you have any questions or want to chat about how this might impact your specific use case, please reach out to [hello@exa.ai](mailto:hello@exa.ai).

We can't wait for you to try out the new Auto search as default!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt