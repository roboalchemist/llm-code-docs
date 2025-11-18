# Source: https://flatfile.com/docs/reference/for-llms.md

# For LLMs

> AI-optimized documentation formats and tools for better LLM integration

The Flatfile documentation is optimized for use with Large Language Models (LLMs) and AI tools. We provide several features to help you get faster, more accurate responses when using our documentation as context.

## Contextual Menu

We provide a contextual menu on every documentation page with quick access to AI-optimized content and direct integrations with popular AI tools:

<img className="block dark:hidden" src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/static/images/contextual-menu.png" alt="Contextual menu showing AI integration options" />

<img className="hidden dark:block" src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/static/images/contextual-menu.png" alt="Contextual menu showing AI integration options" />

* **Copy page** - Copies the current page as Markdown for pasting as context into AI tools
* **View as Markdown** - Opens the current page in a clean Markdown format
* **Open in ChatGPT** - Creates a ChatGPT conversation with the current page as context
* **Open in Claude** - Creates a Claude conversation with the current page as context

Access this menu by right-clicking on any page or using the contextual menu button (when available).

## LLM-Optimized File Formats

### /llms.txt

The `/llms.txt` file follows the [industry standard](https://llmstxt.org) that helps general-purpose LLMs index documentation more efficiently, similar to how a sitemap helps search engines.

**What it contains:**

* Complete list of all available pages in our documentation
* Page titles and URLs for easy navigation
* Structured format that AI tools can quickly parse

**How to use:**

* Access at: [https://flatfile.com/docs/llms.txt](https://flatfile.com/docs/llms.txt)
* Reference this file when asking AI tools to understand our documentation structure
* Use it to help LLMs find relevant content for specific topics

### /llms-full.txt

The `/llms-full.txt` file combines our entire documentation site into a single file, optimized for use as comprehensive context in AI tools.

**What it contains:**

* Full text content of all documentation pages
* Structured with clear page boundaries and headers
* Optimized formatting for LLM consumption

**How to use:**

* Access at: [https://flatfile.com/docs/llms-full.txt](https://flatfile.com/docs/llms-full.txt)
* Download and use as context for comprehensive questions about Flatfile
* Ideal for complex queries that might span multiple documentation areas

**Note:** This file is large and may consume significant tokens. You might want to use `/llms.txt` first to identify specific pages, then use individual page URLs or the contextual menu for targeted questions.

## Markdown Versions of Pages

All documentation pages are available in Markdown format, which provides structured text that AI tools can process more efficiently than HTML.

### .md Extension

Add `.md` to any page's URL to view the Markdown version:

```
https://flatfile.com/docs/getting-started/welcome.md
https://flatfile.com/docs/embedding/overview.md
https://flatfile.com/docs/core-concepts/workbooks.md
```

## Best Practices for AI Tool Usage

### For Specific Questions

1. **Start with targeted pages** - Use the contextual menu or `.md` extension for specific topics
2. **Reference multiple related pages** - Copy 2-3 relevant pages for comprehensive context
3. **Include the page URL** - Help the AI tool understand the source and context

### For Comprehensive Questions

1. **Use `/llms.txt` first** - Help the AI understand our documentation structure
2. **Follow up with specific pages** - Use targeted content based on the structure overview
3. **Consider `/llms-full.txt`** - For complex questions spanning multiple areas (token usage permitting)

### Example Prompts

**For specific integration help:**

```
I'm trying to embed Flatfile in my React app. Here's the relevant documentation:
[paste content from /embedding/react.md]

How do I configure it for my use case where...
```

**For comprehensive understanding:**

```
I need to understand Flatfile's architecture. Here's their documentation structure:
[paste content from /llms.txt]

Can you explain how Environments, Apps, and Spaces work together?
```

## Technical Implementation

These AI-optimization features are built into our documentation platform and automatically maintained:

* **Auto-generated** - Files are updated automatically when documentation changes
* **Optimized formatting** - Content is structured for optimal LLM processing
* **Consistent structure** - All pages follow the same format for predictable parsing

## Feedback

These AI optimization features are continuously improved based on usage patterns and feedback. If you have suggestions for better LLM integration or notice issues with the generated formats, please [join our Slack community](https://flatfile.com/join-slack/) and share your thoughts in the #docs channel.
