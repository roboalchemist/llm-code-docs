# Source: https://developers.buffer.com/guides/integrations/claude.md

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="https://static.buffer.com/publish/claude-Cy2cH_fJ.png" alt="Claude" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Claude</div>
    <div class="integration-page-subtitle">Manage your content from Claude</div>
  </div>
</div>

Claude lets you manage your Buffer content using natural language.

You can create posts, schedule content, and manage your social media presence directly from Claude using the Buffer MCP server.

<div class="setup-tabs-container">
  <div class="setup-tabs">
    <button class="setup-tab active" data-tab="claude-desktop">Claude Desktop</button>
    <button class="setup-tab" data-tab="claude-code">Claude Code</button>
  </div>

  <div class="setup-tab-content active" data-tab-content="claude-desktop">

<div class="setup-steps" style="--step-color: #D97757;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Claude.</p>
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
      <p class="setup-note"><strong>Note:</strong> If you have multiple Node.js versions installed, verify that Claude Desktop is picking up version 18 or higher.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Open Claude Settings</h3>
      <p>Open Claude desktop and go to "Settings..."</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Navigate to Developer Tab</h3>
      <p>Click on the "Developer" tab.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Edit Configuration</h3>
      <p>Click "Edit config" to open the configuration file.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">6</div>
    <div class="setup-step-content">
      <h3>Add Buffer MCP Server</h3>
      <p>Open claude_desktop_config.json and add the following configuration:</p>
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
    <div class="setup-step-number">7</div>
    <div class="setup-step-content">
      <h3>Save and Restart</h3>
      <p>Save the configuration file and restart Claude desktop to apply the changes.</p>
    </div>
  </div>
</div>

  </div>

  <div class="setup-tab-content" data-tab-content="claude-code">

<div class="setup-steps" style="--step-color: #D97757;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Claude Code.</p>
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
      <h3>Add Buffer MCP Server</h3>
      <p>Run the following command to add the Buffer MCP server to Claude Code:</p>
      <div class="setup-code-block">
        <button class="inline-copy-btn" data-copy="claude mcp add buffer -- npx -y mcp-remote https://mcp.buffer.com/mcp --header &quot;Authorization: Bearer YOUR_API_KEY&quot;" title="Copy command">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        </button>
<pre><code>claude mcp add buffer -- npx -y mcp-remote \
  https://mcp.buffer.com/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"</code></pre>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Start Using Buffer</h3>
      <p>Launch Claude Code and start managing your Buffer content with natural language.</p>
    </div>
  </div>
</div>

  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with Claude:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>Show me all my scheduled Buffer posts for this week</span>
    <button class="inline-copy-btn" data-copy="Show me all my scheduled Buffer posts for this week" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Create a draft post in Buffer that says 'We just launched our redesigned dashboard!' for my Twitter channel</span>
    <button class="inline-copy-btn" data-copy="Create a draft post in Buffer that says 'We just launched our redesigned dashboard!' for my Twitter channel" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>List my Buffer channels and show me which ones have posts scheduled for tomorrow</span>
    <button class="inline-copy-btn" data-copy="List my Buffer channels and show me which ones have posts scheduled for tomorrow" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>
