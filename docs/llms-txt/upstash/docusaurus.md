# Source: https://upstash.com/docs/search/integrations/docusaurus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Docusaurus Integration

> AI-powered search component for Docusaurus using Upstash Search.

## Features

* 🤖 AI-powered search results based on your documentation
* 🎨 Modern and responsive UI
* 🌜 Dark/Light mode support

## Installation

To install the package, run:

```bash  theme={"system"}
npm install @upstash/docusaurus-theme-upstash-search
```

## Configuration

### Enabling the Searchbar

To enable the searchbar, add the following to your docusaurus config file:

```js  theme={"system"}
export default {
  themes: ['@upstash/docusaurus-theme-upstash-search'],
  // ...
  themeConfig: {
    // ...
    upstash: {
      upstashSearchRestUrl: "UPSTASH_SEARCH_REST_URL",
      upstashSearchReadOnlyRestToken: "UPSTASH_SEARCH_READ_ONLY_REST_TOKEN",
      upstashSearchIndexName: "UPSTASH_SEARCH_INDEX_NAME",
    },
  },
};
```

The default index name is `docusaurus`. You can override it by setting the `upstashSearchIndexName` option.

You can fetch your URL and read only token from [Upstash Console](https://console.upstash.com/search). **Make sure to use the read only token!**

If you do not have a search database yet, you can create one from [Upstash Console](https://console.upstash.com/search). Make sure to use Upstash generated embedding model.

## Indexing Your Documentation

### Setting Up Environment Variables

To index your documentation, create a `.env` file with the following environment variables:

```bash  theme={"system"}
UPSTASH_SEARCH_REST_URL=
UPSTASH_SEARCH_REST_TOKEN=
UPSTASH_SEARCH_INDEX_NAME=
DOCS_PATH=
```

You can fetch your URL and token from [Upstash Console](https://console.upstash.com/search). This time **do not use the read only token** since we are upserting data.

### Running the Indexing Script

After setting up your environment variables, run the indexing command:

```bash  theme={"system"}
npx index-docs-upstash
```

### Configuration Options

* **DOCS\_PATH**: The indexing script looks for documentation in the `docs` directory by default. You can specify a different path using the `DOCS_PATH` option.
* **UPSTASH\_SEARCH\_INDEX\_NAME**: The default index name is `docusaurus`. You can override it by setting the `UPSTASH_SEARCH_INDEX_NAME` option. Make sure the name you set while indexing matches with your themeConfig `upstashSearchIndexName` option.

For more details on how this integration works, check out [the official repository](https://github.com/upstash/docusaurus-theme-upstash-search).
