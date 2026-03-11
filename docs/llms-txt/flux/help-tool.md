# Source: https://docs.flux.ai/reference/help-tool.md

# Flux Help Tool

Flux includes a powerful help tool that allows you to quickly find information about Flux Editor features and functionality directly from the chat interface. This tool combines both traditional keyword-based search and advanced semantic search capabilities to help you find the information you need.

## Overview

The help tool enables you to:

- Search the entire Flux documentation directly from the Flux Chat interface
- Get relevant results based on both keyword matching and semantic understanding
- Access direct links to the documentation pages containing the information you need
- Receive summarized information without leaving your design workflow

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/obnq6v05v1x6u6ayffuk2ec3hs8hooktz6mezusg8fzvcxkjt73lfs58c71ev9dk.png)

## How to Use Documentation Search

To search the Flux documentation using Flux, use the `@help` tool in your query:

```none
@help How do I add a via in my PCB layout?

@help What's the best way to organize my schematic in Flux?
```



When you use the `@help` tool, Flux will:

1. Process your query using advanced semantic search technology
2. Search through the entire Flux documentation
3. Return the most relevant results with direct links to the documentation
4. Provide a summary of the information found

## Search Technology

Flux's help tool uses two complementary search methods to ensure you get the most relevant results:

### Vector-Based Semantic Search

The primary search method uses vector embeddings to understand the meaning behind your query, not just the keywords. This allows Flux to find relevant documentation even when your query doesn't contain the exact words used in the documentation.

For example, if you ask "How do I connect layers on my board?", the semantic search can understand you're looking for information about vias, even if you don't use that specific term.

### Keyword-Based Fulltext Search

As a fallback, Flux also uses traditional keyword-based search to find exact matches in the documentation. This ensures that if the semantic search doesn't find relevant results, you'll still get useful information based on keyword matching.

## Example Queries

Here are some examples of how you can use the help tool:

### Learning Flux Features

```none
@help How do I use the layout rules system?

@help What are the keyboard shortcuts in Flux?

@help How do I export my design for manufacturing?
```



### Troubleshooting

```none
@help Why can't I route this trace?

@help How do I fix DRC errors?

@help What does this error message mean?
```



### Finding Specific Information

```none
@help What are the supported file formats for import?

@help How do I set up impedance-controlled routing?

@help What are the minimum clearance requirements?
```



## Search Results Format

When Flux returns search results, they are presented in a structured format that includes:

- The title of the relevant documentation page
- A snippet of content from the page that answers your query
- A direct link to the documentation page
- Additional context about where in the documentation the information was found

If multiple relevant results are found, Flux will organize them by relevance and present them in a clear, readable format.

## Tips for Effective Searches

To get the most out of the help tool:

1. **Be specific in your queries** - The more specific your question, the more targeted the results will be.
2. **Use natural language** - You don't need to use special syntax or keywords; ask your question as you would to another person.
3. **Refine your search if needed** - If the initial results don't answer your question, try rephrasing or being more specific.
4. **Combine with other tools** - You can use documentation search alongside other Flux tools for a comprehensive design experience.

## Limitations

While the documentation search feature is powerful, it has some limitations to be aware of:

- The search is limited to the official Flux documentation and doesn't include community forums or third-party resources.
- Very recent documentation updates may not be immediately reflected in search results.
- Complex or highly technical queries might require more specific phrasing to get the most relevant results.
- The search doesn't currently support filtering by documentation section or type.

## Related Features

The documentation search feature works well with other Flux capabilities:

- [Getting Started With Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Learn the basics of using Flux in your workflow
- [Flux Reference](https://docs.flux.ai/flux/reference/copilot) - Comprehensive reference for all Flux features
- [AI-Assisted Design with Flux](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design) - Discover how to leverage AI in your design process