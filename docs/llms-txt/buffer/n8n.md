# Source: https://developers.buffer.com/guides/integrations/n8n.md

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="data:image/avif;base64,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" alt="n8n" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">n8n</div>
    <div class="integration-page-subtitle">Workflow automation with n8n</div>
  </div>
</div>

n8n is a workflow automation tool that connects Buffer with hundreds of apps.

Create complex automation workflows, trigger posts based on events, and integrate Buffer into your existing automation pipelines.

## Setup

<div class="setup-steps" style="--step-color: #EA4B71;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with n8n.</p>
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
      <h3>Add MCP Client to Workflow</h3>
      <p>Inside of a workflow, add an "MCP Client" node.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Configure the MCP Client</h3>
      <p>Fill in the form with the following details:</p>
      <ul class="setup-settings-list">
        <li><span>Server Transport:</span> HTTP Streamable</li>
        <li>
          <span>MCP Endpoint URL:</span>
          <code>https://mcp.buffer.com/mcp</code>
          <button class="inline-copy-btn" data-copy="https://mcp.buffer.com/mcp" title="Copy URL">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li><span>Authentication:</span> Bearer Auth</li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Add Your Credentials</h3>
      <p>Click on "Credential for Bearer Auth" and configure:</p>
      <ul class="setup-settings-list">
        <li>Select "Create new credential"</li>
        <li>
          Add your API key: <code>YOUR_API_KEY</code>
          <button class="inline-copy-btn" data-copy="YOUR_API_KEY" title="Copy API key">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li>Click "Save"</li>
        <li>Close the modal</li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Select Buffer MCP Tools</h3>
      <p>Select the MCP tool you want the workflow to use from the available Buffer MCP tools, then configure it as needed.</p>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with n8n:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>When a new RSS feed item appears, automatically create a draft post in Buffer with the article title and link</span>
    <button class="inline-copy-btn" data-copy="When a new RSS feed item appears, automatically create a draft post in Buffer with the article title and link" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Every Friday, pull my scheduled posts in Buffer for the next week and send a summary to Slack</span>
    <button class="inline-copy-btn" data-copy="Every Friday, pull my scheduled posts in Buffer for the next week and send a summary to Slack" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>When a form submission comes in, create a draft post in Buffer using the submitted content</span>
    <button class="inline-copy-btn" data-copy="When a form submission comes in, create a draft post in Buffer using the submitted content" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>
