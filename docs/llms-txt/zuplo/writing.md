# Source: https://www.zuplo.com/docs/dev-portal/zudoku/writing.md

# Writing

Get started with creating rich documentation in Dev Portal using Markdown and MDX. This guide covers the
essentials to help you begin documenting your project.

## Quick Start

1. **Create a markdown file** in your `pages` directory
2. **Add frontmatter** with title and metadata
3. **Configure navigation** to make it discoverable
4. **Write content** using Markdown or MDX

### Basic Document Structure

```md
---
title: My Document
sidebar_icon: file-text
---

Your content goes here using standard Markdown syntax.
```

## Adding to Navigation

To make your documentation discoverable, add it to the navigation configuration. Documents are
referenced by their file path:

```ts title="zudoku.config.ts"
const config = {
  navigation: [
    {
      type: "doc",
      file: "my-document",
      label: "My Document",
    },
  ],
};
```

Learn more about configuring navigation at
[Navigation → Documents](/dev-portal/zudoku/configuration/navigation#type-doc).

## File Organization

Organize your documentation files in logical directories:

```
pages/
├── getting-started/
│   ├── installation.md
│   └── quick-start.md
├── guides/
│   ├── authentication.md
│   └── deployment.md
└── api/
    └── reference.md
```

## What's Next?

Explore the detailed guides to enhance your documentation:

- **[Markdown Overview](/dev-portal/zudoku/markdown/overview)** - Complete markdown syntax reference
- **[Frontmatter](/dev-portal/zudoku/markdown/frontmatter)** - Document metadata and configuration
- **[MDX](/dev-portal/zudoku/markdown/mdx)** - Interactive components in markdown
- **[Admonitions](/dev-portal/zudoku/markdown/admonitions)** - Callouts and alerts
- **[Code Blocks](/dev-portal/zudoku/markdown/code-blocks)** - Syntax highlighting and features
