# Source: https://exa.ai/docs/home.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Home

<div className="home-page" />

## Build with Exa

<p className="home-subtitle">
  Get started with Exa's web search and contents APIs
</p>

<div className="home-cards">
  <a href="/docs/reference/search-quickstart" className="home-card">
    <span>Start with the search API</span>

    <svg className="arrow" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12h14" />

      <path d="m12 5 7 7-7 7" />
    </svg>
  </a>

  <a href="/docs/reference/exa-mcp" className="home-card">
    <span>MCP Quickstart</span>

    <svg className="arrow" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12h14" />

      <path d="m12 5 7 7-7 7" />
    </svg>
  </a>

  <a href="https://dashboard.exa.ai" target="_blank" className="home-card">
    <span>API Playground</span>

    <svg className="arrow" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12h14" />

      <path d="m12 5 7 7-7 7" />
    </svg>
  </a>
</div>

## Make your first API call in minutes

<Tabs>
  <Tab title="cURL">
    ```bash  theme={null}
    curl -X POST "https://api.exa.ai/search" \
      -H "Content-Type: application/json" \
      -H "x-api-key: YOUR_API_KEY" \
      -d '{
        "query": "blog post about artificial intelligence",
        "type": "auto",
        "contents": {
          "text": true
        }
      }'
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from exa_py import Exa

    exa = Exa(api_key="your-api-key")

    result = exa.search(
      "blog post about artificial intelligence",
      type="auto",
      contents={
        "text": True
      }
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import Exa from 'exa-js';

    const exa = new Exa("your-api-key");

    const result = await exa.search(
      "blog post about artificial intelligence",
      {
        type: "auto",
        contents: {
          text: true
        }
      }
    );
    ```
  </Tab>
</Tabs>

<div className="home-footer-cards">
  <a href="https://dashboard.exa.ai/playground" className="home-footer-card">
    <Icon icon="play" className="icon" />

    <span className="title">Playground</span>
    <span className="subtitle">Try Exa's API, parameters, and responses</span>
  </a>

  <a href="https://github.com/exa-labs" target="_blank" className="home-footer-card">
    <Icon icon="github" className="icon" />

    <span className="title">GitHub</span>
    <span className="subtitle">Check out our open-source projects</span>
  </a>

  <a href="https://exa.ai/careers" target="_blank" className="home-footer-card">
    <Icon icon="users" className="icon" />

    <span className="title">Careers</span>

    <span className="subtitle">
      Come build the best search engine in the world
    </span>
  </a>
</div>
