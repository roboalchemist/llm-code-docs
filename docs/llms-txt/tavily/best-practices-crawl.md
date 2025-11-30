# Source: https://docs.tavily.com/documentation/best-practices/best-practices-crawl.md

# Best Practices for Crawl

> Learn how to effectively use Tavily's Crawl API to extract and process web content.

## When to Use `crawl` vs `map`

### Use Crawl when you need:

* Full content extraction from pages
* Deep content analysis
* Processing of paginated or nested content
* Extraction of specific content patterns
* Integration with RAG systems

### Use Map when you need:

* Quick site structure discovery
* URL collection without content extraction
* Sitemap generation
* Path pattern matching
* Domain structure analysis

## Use Cases

### 1. Deep or Unlinked Content

Many sites have content that's difficult to access through standard means:

* Deeply nested pages not in main navigation
* Paginated archives (old blog posts, changelogs)
* Internal search-only content

**Best Practice:**

```json  theme={null}
{
  "url": "example.com",
  "max_depth": 3,
  "max_breadth": 50,
  "limit": 200,
  "select_paths": ["/blog/.*", "/changelog/.*"],
  "exclude_paths": ["/private/.*", "/admin/.*"]
}
```

### 2. Structured but Nonstandard Layouts

For content that's structured but not marked up in schema.org:

* Documentation
* Changelogs
* FAQs

**Best Practice:**

```json  theme={null}
{
  "url": "docs.example.com",
  "max_depth": 2,
  "extract_depth": "advanced",
  "select_paths": ["/docs/.*"]
}
```

### 3. Multi-modal Information Needs

When you need to combine information from multiple sections:

* Cross-referencing content
* Finding related information
* Building comprehensive knowledge bases

**Best Practice:**

```json  theme={null}
{
  "url": "example.com",
  "max_depth": 2,
  "instructions": "Find all documentation pages that link to API reference docs",
  "extract_depth": "advanced"
}
```

### 4. Rapidly Changing Content

For content that updates frequently:

* API documentation
* Product announcements
* News sections

**Best Practice:**

```json  theme={null}
{
  "url": "api.example.com",
  "max_depth": 1,
  "max_breadth": 100,
  "extract_depth": "basic"
}
```

### 5. Behind Auth / Paywalls

For content requiring authentication:

* Internal knowledge bases
* Customer help centers
* Gated documentation

**Best Practice:**

```json  theme={null}
{
  "url": "help.example.com",
  "max_depth": 2,
  "select_domains": ["^help\.example\.com$"],
  "exclude_domains": ["^public\.example\.com$"]
}
```

### 6. Complete Coverage / Auditing

For comprehensive content analysis:

* Legal compliance checks
* Security audits
* Policy verification

**Best Practice:**

```json  theme={null}
{
  "url": "example.com",
  "max_depth": 3,
  "max_breadth": 100,
  "limit": 1000,
  "extract_depth": "advanced",
  "instructions": "Find all mentions of GDPR and data protection policies"
}
```

### 7. Semantic Search or RAG Integration

For feeding content into LLMs or search systems:

* RAG systems
* Enterprise search
* Knowledge bases

**Best Practice:**

```json  theme={null}
{
  "url": "docs.example.com",
  "max_depth": 2,
  "extract_depth": "advanced",
  "include_images": true
}
```

### 8. Known URL Patterns

When you have specific paths to crawl:

* Sitemap-based crawling
* Section-specific extraction
* Pattern-based content collection

**Best Practice:**

```json  theme={null}
{
  "url": "example.com",
  "max_depth": 1,
  "select_paths": ["/docs/.*", "/api/.*", "/guides/.*"],
  "exclude_paths": ["/private/.*", "/admin/.*"]
}
```

## Performance Considerations

### Depth vs. Performance

* Each level of depth increases crawl time exponentially
* Start with `max_depth: 1` and increase as needed
* Use `max_breadth` to control horizontal expansion
* Set appropriate `limit` to prevent excessive crawling

### Resource Optimization

* Use `basic` extract\_depth for simple content
* Use `advanced` extract\_depth only when needed
* Set appropriate `max_breadth` based on site structure
* Use `select_paths` and `exclude_paths` to focus crawling

### Rate Limiting

* Respect site's robots.txt
* Implement appropriate delays between requests
* Monitor API usage and limits
* Use appropriate error handling for rate limits

## Best Practices Summary

1. **Start Small**
   * Begin with limited depth and breadth
   * Gradually increase based on needs
   * Monitor performance and adjust

2. **Be Specific**
   * Use path patterns to focus crawling
   * Exclude irrelevant sections

3. **Optimize Resources**
   * Choose appropriate extract\_depth
   * Set reasonable limits
   * Use include\_images only when needed

4. **Handle Errors**
   * Implement retry logic
   * Monitor failed results
   * Handle rate limits appropriately

5. **Security**
   * Respect robots.txt
   * Use appropriate authentication
   * Exclude sensitive paths

6. **Integration**
   * Plan for data processing
   * Consider storage requirements
   * Design for scalability

## Common Pitfalls

1. **Excessive Depth**
   * Avoid setting max\_depth too high
   * Start with 1-2 levels
   * Increase only if necessary

2. **Unfocused Crawling**
   * Use instructions for guidance

3. **Resource Overuse**
   * Monitor API usage
   * Set appropriate limits
   * Use basic extract\_depth when possible

4. **Missing Content**
   * Verify path patterns
   * Monitor crawl coverage

## Integration with Map

Consider using Map before Crawl to:

1. Discover site structure
2. Identify relevant paths
3. Plan crawl strategy
4. Validate URL patterns

Example workflow:

1. Use Map to get site structure
2. Analyze paths and patterns
3. Configure Crawl with discovered paths
4. Execute focused crawl

## Conclusion

Tavily's Crawl API is powerful for extracting structured content from websites. By following these best practices, you can:

* Optimize crawl performance
* Ensure complete coverage
* Maintain resource efficiency
* Build robust content extraction pipelines

Remember to:

* Start with limited scope
* Use appropriate parameters
* Monitor performance
* Handle errors gracefully
* Respect site policies


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.tavily.com/llms.txt