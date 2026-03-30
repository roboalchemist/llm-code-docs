# Source: https://docs.nimbleway.io/nimble-sdk/search-api/output-formats.md

# Output Formats

The Search API supports three parsing formats to suit different use cases:

### markdown (default)

Converts HTML to markdown format, preserving headings, links, and basic formatting. Best for:

* Documentation extraction
* Content migration
* LLM-friendly input
* Human-readable output

**Example output:**

```markdown
# Latest AI Trends in 2025

The artificial intelligence landscape has evolved dramatically...

## Key Developments
- Generative AI advances
- Autonomous systems
```

***

### plain\_text

Converts HTML to clean plain text with preserved line breaks. Scripts, styles, and images are removed. Best for:

* Text analysis and NLP tasks
* Content summarization
* Simple content extraction

**Example output:**

```
Latest AI Trends in 2025

The artificial intelligence landscape has evolved dramatically in recent years...
```

***

### simplified\_html

Strips unnecessary attributes and elements while maintaining HTML structure. Best for:

* Web scraping with structure preservation
* Custom parsing pipelines
* Lightweight HTML processing

**Example output:**

```html
<h1>Latest AI Trends in 2025</h1>
<p>The artificial intelligence landscape...</p>
<ul>
<li>Generative AI advances</li>
<li>Autonomous systems</li>
</ul>
```
