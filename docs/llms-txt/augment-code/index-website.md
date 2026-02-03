# Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/index-website.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Index Website

> Crawl and index a static website for semantic search in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* Node.js 18+
* Augment API credentials
* For chat: An LLM API key (OpenAI, Anthropic, or Google)

## Steps

### 1. Install

```bash  theme={null}
npm install @augmentcode/context-connectors
```

### 2. Set credentials

```bash  theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

### 3. Index the site

```bash  theme={null}
npx ctxc index website --url https://docs.example.com -i example-docs
```

You should see:

```
Crawling https://docs.example.com...
Indexing complete: 87 pages indexed, 12 skipped
```

### 4. Search

```bash  theme={null}
npx ctxc search "how to configure SSO" -i example-docs
```

You should see an LLM-generated answer based on the documentation:

```
Answer:

Based on the documentation at https://docs.example.com/auth/sso, SSO can be configured by...
```

For raw search results without LLM processing, add `--raw`:

```bash  theme={null}
npx ctxc search "SSO" -i example-docs --raw
```

### 5. Chat (Optional)

For an interactive AI agent that can search and read the documentation:

```bash  theme={null}
export OPENAI_API_KEY='your-openai-key'
npx ctxc agent -i example-docs --provider openai
```

You should see:

```
Agent ready. Type your question or 'exit' to quit.

>
```

Ask questions interactively:

```
> How do I set up SSO with Okta?

Searching: "SSO Okta setup"...
Reading: https://docs.example.com/auth/sso-okta...

Based on the documentation, to set up SSO with Okta you need to...
```

Type `exit` to quit.

## Done!

You can now:

* **Search** the documentation semantically with the `search` command
* **Chat** with an AI agent that understands the docs using the `agent` command

## Limitations

* Only static HTML is indexed. JavaScript-rendered content (SPAs) won't work.
* Only pages linked from the starting URL are discovered.

## Also Works With

| Instead of...    | Try...                                                                                              |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| Single site      | Index multiple sites with different `-i` names                                                      |
| Local storage    | `--store s3` with `CC_S3_BUCKET` for team sharing                                                   |
| Interactive chat | `npx ctxc agent -i example-docs --provider openai "your question" --print` for single-question mode |
| OpenAI           | `--provider anthropic` or `--provider google` for other LLM providers                               |
