# Source: https://docs.exa.ai/changelog/markdown-contents-as-default.md

# Markdown Contents as Default

> Markdown content is now the default format for all Exa API endpoints, providing cleaner, more readable content that's ideal for AI applications and text processing.

***

**Date: 23 June 2025**

We've updated all Exa API endpoints to return content in markdown format by default. This change provides cleaner, more structured content that's optimized for AI applications, RAG systems, and general text processing workflows.

<Info>
  All endpoints now process webpage content into clean markdown format by default. Use the `includeHtmlTags` parameter to control content formatting.
</Info>

## What Changed

Previously, our endpoints returned content in various formats depending on the specific endpoint configuration. Now, all endpoints consistently return content processed into clean markdown format, making it easier to work with the data across different use cases.

## Content Processing Behavior

The `includeHtmlTags` parameter now controls how we process webpage content:

* **`includeHtmlTags=false` (default)**: We process webpage content into clean markdown format
* **`includeHtmlTags=true`**: We return content as HTML without processing to markdown

In all cases, we remove extraneous data, advertisements, navigation elements, and other boilerplate content, keeping only what we detect as the main content of the page.

**No action required** if you want the new markdown format - it's now the default! If you need HTML content instead:

## Benefits of Markdown Default

1. **Better for AI applications**: Markdown format is more structured and easier for LLMs to process
2. **Improved readability**: Clean formatting without HTML tags makes content more readable
3. **RAG optimization**: Markdown content chunks more naturally for retrieval systems

If you have any questions about this change or need help adapting your implementation, please reach out to [hello@exa.ai](mailto:hello@exa.ai).

We're excited for you to experience the improved content quality with markdown as the default!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt