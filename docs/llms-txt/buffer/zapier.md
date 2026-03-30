# Source: https://developers.buffer.com/guides/integrations/zapier.md

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="https://static.buffer.com/publish/zapier-B5YW4nQ2.png" alt="Zapier" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Zapier</div>
    <div class="integration-page-subtitle">Automate workflows with Zapier</div>
  </div>
</div>

Zapier supercharges Buffer with 5,000+ no-code integrations to automate your entire workflow. Picture this: auto-post Buffer updates to Discord communities, pipe engagement stats into Looker Studio dashboards for real-time insights, or instantly transform Trello card updates into ready-to-schedule Buffer drafts — unlocking pro-level efficiency!

## Setup

<div class="setup-steps">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Zapier.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Navigate to Zapier Connections</h3>
      <p>Click "Add connection" to connect Buffer. <a href="https://actions.zapier.com/credentials/" target="_blank" rel="noopener noreferrer">Zapier Connections</a></p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Search for MCP Client</h3>
      <p>Search for "MCP Client by Zapier" and select it, then click "Add connection".</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Configure the connection</h3>
      <p>Fill in the form with the following settings:</p>
      <ul class="setup-settings-list">
        <li>
          <span>Server URL:</span>
          <code>https://mcp.buffer.com/mcp</code>
          <button class="inline-copy-btn" data-copy="https://mcp.buffer.com/mcp" title="Copy URL">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li><span>Transport:</span> Streamable HTTP</li>
        <li><span>OAuth:</span> No</li>
        <li>
          <span>Bearer Token:</span>
          <code>YOUR_API_KEY</code>
          <button class="inline-copy-btn" data-copy="YOUR_API_KEY" title="Copy bearer token">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Complete the setup</h3>
      <p>Click "Yes, Continue to MCP Client by Zapier" to finish.</p>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with Zapier:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>When a new blog post is published in WordPress, create a draft post in Buffer with the post title and link</span>
    <button class="inline-copy-btn" data-copy="When a new blog post is published in WordPress, create a draft post in Buffer with the post title and link" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>When a new row is added to my Google Sheet, add a post to my Buffer queue with that content</span>
    <button class="inline-copy-btn" data-copy="When a new row is added to my Google Sheet, add a post to my Buffer queue with that content" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Every Monday at 8am, check my Buffer queue and notify me in Slack if any channel has no posts scheduled</span>
    <button class="inline-copy-btn" data-copy="Every Monday at 8am, check my Buffer queue and notify me in Slack if any channel has no posts scheduled" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>
