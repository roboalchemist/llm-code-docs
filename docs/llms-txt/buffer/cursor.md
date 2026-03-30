# Source: https://developers.buffer.com/guides/integrations/cursor.md

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="data:image/avif;base64,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" alt="Cursor" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Cursor</div>
    <div class="integration-page-subtitle">Manage Buffer from your code editor</div>
  </div>
</div>

Use the Buffer MCP server within Cursor to manage social media content directly from your AI-powered code editor. Schedule posts, check your queue, and draft content — all without leaving your IDE.

## Setup

<div class="setup-steps" style="--step-color: #2563EB;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Cursor.</p>
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
      <h3>Install Node.js (one-time setup)</h3>
      <p>This integration requires Node.js 18 or higher. <a href="https://nodejs.org" target="_blank" rel="noopener noreferrer">Download Node.js</a></p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Open Cursor Settings</h3>
      <p>Open Cursor and go to Settings. You can use the keyboard shortcut <code>Cmd+Shift+J</code> (Mac) or <code>Ctrl+Shift+J</code> (Windows/Linux).</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Navigate to MCP</h3>
      <p>Click on the "MCP" tab in the settings sidebar.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Add Buffer MCP Server</h3>
      <p>Click "Add new global MCP server" and add the following configuration:</p>
      <div class="setup-code-block">
        <button class="inline-copy-btn" data-copy='{
  "mcpServers": {
    "Buffer": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.buffer.com/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}' title="Copy configuration">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        </button>
<pre><code>{
  "mcpServers": {
    "Buffer": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.buffer.com/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}</code></pre>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">6</div>
    <div class="setup-step-content">
      <h3>Verify Connection</h3>
      <p>After saving, you should see a green indicator next to "Buffer" in the MCP settings confirming the server is connected.</p>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with Cursor:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>List all my connected Buffer channels</span>
    <button class="inline-copy-btn" data-copy="List all my connected Buffer channels" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Draft a Buffer post announcing the new feature I just committed and schedule it for tomorrow morning</span>
    <button class="inline-copy-btn" data-copy="Draft a Buffer post announcing the new feature I just committed and schedule it for tomorrow morning" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Show me all my draft posts in Buffer so I can review what's pending</span>
    <button class="inline-copy-btn" data-copy="Show me all my draft posts in Buffer so I can review what's pending" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>
