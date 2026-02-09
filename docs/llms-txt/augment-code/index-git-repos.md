# Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/index-git-repos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Index and Search Code

> Index a Git repository and search or chat with it in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* Node.js 18+
* Augment API credentials (`AUGMENT_API_TOKEN`, `AUGMENT_API_URL`)
* Git provider token with repo read access:
  * GitHub: `GITHUB_TOKEN`
  * GitLab: `GITLAB_TOKEN`
  * BitBucket: `BITBUCKET_TOKEN`
* For chat: An LLM API key (OpenAI, Anthropic, or Google)

## Steps

### 1. Install

```bash  theme={null}
npm install @augmentcode/context-connectors
```

### 2. Set credentials

<Tabs>
  <Tab title="GitHub">
    ```bash  theme={null}
    export AUGMENT_API_TOKEN='your-token'
    export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
    export GITHUB_TOKEN='your-github-token'
    ```
  </Tab>

  <Tab title="GitLab">
    ```bash  theme={null}
    export AUGMENT_API_TOKEN='your-token'
    export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
    export GITLAB_TOKEN='your-gitlab-token'
    ```
  </Tab>

  <Tab title="BitBucket">
    ```bash  theme={null}
    export AUGMENT_API_TOKEN='your-token'
    export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
    export BITBUCKET_TOKEN='your-bitbucket-token'
    ```
  </Tab>
</Tabs>

### 3. Index the repository

<Tabs>
  <Tab title="GitHub">
    ```bash  theme={null}
    npx ctxc index github --owner facebook --repo react -i react
    ```
  </Tab>

  <Tab title="GitLab">
    ```bash  theme={null}
    npx ctxc index gitlab --project mygroup/myrepo -i myrepo
    ```
  </Tab>

  <Tab title="Bitbucket">
    ```bash  theme={null}
    npx ctxc index bitbucket --workspace myws --repo myrepo -i myrepo
    ```
  </Tab>
</Tabs>

You should see:

```
Fetching file tree from facebook/react...
Indexing complete: 2847 files indexed, 156 skipped
```

### 4. Search

```bash  theme={null}
npx ctxc search "How does the reconciliation algorithm work?" -i react
```

You should see an LLM-generated answer based on the codebase:

```
Answer:

Based on the code in packages/react-reconciler/src/ReactFiberReconciler.js...
```

For raw search results without LLM processing, add `--raw`:

```bash  theme={null}
npx ctxc search "reconciliation" -i react --raw
```

### 5. Chat (Optional)

For an interactive AI agent that can search and read the codebase:

```bash  theme={null}
export OPENAI_API_KEY='your-openai-key'
npx ctxc agent -i react --provider openai
```

You should see:

```
Agent ready. Type your question or 'exit' to quit.

>
```

Ask questions interactively:

```
> How does React handle component updates?

Searching: "component updates"...
Reading: packages/react-reconciler/src/ReactFiberWorkLoop.js...

Based on the code, React handles component updates by...
```

Type `exit` to quit.

## Done!

You can now:

* **Search** your codebase semantically with the `search` command
* **Chat** with an AI agent that understands your code using the `agent` command

No need to clone the repository locally - Context Connectors fetches files directly from the Git provider API.

## Also Works With

| Instead of...    | Try...                                                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Default branch   | `--ref main`, `--ref v1.0.0`, or `--ref abc123` for specific branch/tag/commit                                             |
| Local storage    | `--store s3` with `CC_S3_BUCKET` for team sharing                                                                          |
| Manual updates   | Set up [GitHub Actions](/context-services/context-connectors/quickstart/github-actions-indexing) to re-index on every push |
| Interactive chat | `npx ctxc agent -i react --provider openai "your question" --print` for single-question mode                               |
| OpenAI           | `--provider anthropic` or `--provider google` for other LLM providers                                                      |
| Code repos       | [Index websites](/context-services/context-connectors/quickstart/index-website) to chat with documentation sites           |
