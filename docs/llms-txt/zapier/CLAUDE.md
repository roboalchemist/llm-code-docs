# Source: https://docs.zapier.com/CLAUDE.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is Zapier's public API documentation site built with Mintlify. The docs are structured as a monorepo containing documentation for multiple Zapier products and solutions:

* **Developer Platform** - Integration development tools and documentation
* **Powered by Zapier** - Embeddable workflow APIs and components
* **AI Actions** - AI-powered automation APIs
* **MCP** - Model Context Protocol integration

## Development Commands

### Local Development

```bash  theme={null}
# Install dependencies
pnpm i

# Run locally
pnpm run dev
```

### Build and Quality Checks

```bash  theme={null}
# Format TypeScript files
pnpm run format

# Compile TypeScript
pnpm run compile

# Full build process (format + compile + scriptify)
pnpm run build

# Check for broken links
pnpx mintlify broken-links
```

### Pre-commit Hook

The repository includes a TypeScript pre-commit hook (`pre-commit.ts`) that:

* Downloads and processes OpenAPI schemas
* Updates navigation configuration automatically
* Validates links and routes
* Ensures documentation consistency

## Project Structure

### Configuration Files

* `docs.json` - Main Mintlify configuration with navigation structure
* `package.json` - Node.js dependencies and scripts
* `tsconfig.json` - TypeScript compilation settings
* `ignore-endpoints` - Lists API endpoints to exclude from auto-generation

### Content Organization

* `ai-actions/` - AI Actions API documentation and guides
* `mcp/` - Model Context Protocol documentation
* `platform/` - Developer Platform docs (CLI, UI, reference)
* `powered-by-zapier/` - Embeddable workflows and APIs
* `images/` - Static image assets
* `snippets/` - Reusable content snippets

### Build Process

The pre-commit hook automatically:

1. Fetches OpenAPI schemas from configured endpoints
2. Generates Mintlify documentation pages
3. Updates navigation configuration in `docs.json`
4. Validates all internal links and routes
5. Filters out ignored endpoints per `ignore-endpoints` file

## Key Architecture Notes

* **Mintlify-based**: Uses Mintlify's documentation framework
* **Auto-generated API docs**: OpenAPI schemas are automatically converted to MDX pages
* **Multi-product structure**: Each major product has its own section with dedicated navigation
* **Validation pipeline**: Automated checks ensure documentation consistency and link validity
* **TypeScript tooling**: Build scripts and validation tools are written in TypeScript

## Working with Documentation

* All content files use `.mdx` format
* Navigation must be declared in `docs.json` to appear on the site
* New pages require adding entries to the navigation configuration
* API reference pages are auto-generated from OpenAPI schemas
* Images should be placed in the `images/` directory
* Use `snippets/` for content that needs to be reused across multiple pages

## Testing and Validation

* Run `mintlify dev` for local development server
* Use `pnpx mintlify broken-links` to check for broken internal links
* The pre-commit hook validates route configurations automatically
* Python script `check_redirects.py` can validate external links against localhost:3000
