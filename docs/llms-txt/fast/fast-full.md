# Fast Documentation

Source: https://docs.fast.io/docs/llms-full.txt

---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fast.io API Documentation</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

<header class="site-header">
  <a href="/" class="logo">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="10 12 118 24" width="140" height="28" fill="none" class="logo-light">
      <path fill="#0D0557" d="M119.689 35.145c-4.08 0-8.28-2.79-8.28-8.1s4.2-8.1 8.28-8.1c4.08 0 8.28 2.79 8.28 8.1s-4.2 8.1-8.28 8.1Zm-3.69-8.1c0 2.4 1.68 3.9 3.69 3.9s3.69-1.5 3.69-3.9-1.68-3.9-3.69-3.9-3.69 1.5-3.69 3.9Z"/>
      <path fill="#FF4C57" d="M110.014 17.6a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
      <path fill="#0D0557" d="M104.689 21.8v13.045h4.65V21.8a4.78 4.78 0 0 1-2.325.6 4.777 4.777 0 0 1-2.325-.6ZM99.54 35.025c-2.88 0-4.98-1.41-4.98-4.98v-7.11h-2.31v-3.69h2.31v-3.99h4.65v3.99h3.269v3.69h-3.27v6.36c0 .78.45 1.62 1.86 1.62.36 0 .9-.06 1.47-.24v3.54c-.6.6-1.92.81-3 .81ZM85.062 35.145c-3.15 0-5.52-1.47-6-4.44l3.69-.99c.24.75.78 1.8 2.25 1.8.84 0 1.62-.42 1.62-1.29 0-.51-.3-.99-1.32-1.32l-2.1-.78c-2.58-.93-3.69-2.61-3.69-4.56 0-2.91 2.61-4.62 5.67-4.62 2.94 0 5.07 1.65 5.61 4.17l-3.63.9c-.39-1.2-1.17-1.47-1.8-1.47-.9 0-1.35.54-1.35 1.08 0 .51.3.99 1.35 1.32l1.95.72c1.68.57 3.9 1.74 3.9 4.56 0 3.15-2.67 4.92-6.15 4.92ZM67.785 35.145c-3.54 0-7.44-2.67-7.44-8.1s3.9-8.1 7.44-8.1c2.76 0 4.38 1.5 4.62 2.07h.09v-1.77h4.65v15.6h-4.65v-1.77h-.09c-.24.57-1.86 2.07-4.62 2.07Zm-2.85-8.1c0 2.52 1.83 3.96 3.81 3.96 2.04 0 3.87-1.41 3.87-3.96s-1.83-3.96-3.87-3.96c-1.98 0-3.81 1.44-3.81 3.96ZM51.07 18.525c0-4.92 3.45-5.67 5.61-5.67.75 0 1.98.03 2.94.6v3.63c-.84-.36-1.56-.3-1.68-.3-1.56 0-2.22.9-2.22 2.22v.24h3.9v3.69h-3.9v11.91h-4.65v-11.91H49v-3.69h2.07v-.72Z"/>
      <path fill="#FF4C57" d="M18 16c0-1.657 1.34-3 2.996-3H35a3 3 0 1 1 0 6H21a4.978 4.978 0 0 0-3 1v-4Z"/>
      <path fill="#CB37FF" d="M18 24c0-1.657 1.34-3 2.996-3H35a3 3 0 1 1 0 6H21a4.978 4.978 0 0 0-3 1v-4Z"/>
      <path fill="#0469FF" d="M18 32a3 3 0 0 1 2.999-3H25a3 3 0 1 1 0 6h-4a4.978 4.978 0 0 0-3 1v-4Z"/>
      <path fill="#FF4C57" fill-rule="evenodd" d="M13 17.2a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4Zm0 1.8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd"/>
      <path fill="#CB37FF" fill-rule="evenodd" d="M13 25.2a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4Zm0 1.8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd"/>
      <path fill="#0469FF" fill-rule="evenodd" d="M13 33.2a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4Zm0 1.8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd"/>
    </svg>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="10 12 118 24" width="140" height="28" fill="none" class="logo-dark">
      <path fill="#fff" d="M119.689 35.145c-4.08 0-8.28-2.79-8.28-8.1s4.2-8.1 8.28-8.1c4.08 0 8.28 2.79 8.28 8.1s-4.2 8.1-8.28 8.1Zm-3.69-8.1c0 2.4 1.68 3.9 3.69 3.9s3.69-1.5 3.69-3.9-1.68-3.9-3.69-3.9-3.69 1.5-3.69 3.9Z"/>
      <path fill="#FF4C57" d="M110.014 17.6a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
      <path fill="#fff" d="M104.688 21.8v13.045h4.65V21.8c-.688.382-1.481.6-2.325.6a4.78 4.78 0 0 1-2.325-.6ZM99.539 35.025c-2.88 0-4.98-1.41-4.98-4.98v-7.11h-2.31v-3.69h2.31v-3.99h4.65v3.99h3.27v3.69h-3.27v6.36c0 .78.45 1.62 1.86 1.62.36 0 .9-.06 1.47-.24v3.54c-.6.6-1.92.81-3 .81ZM85.062 35.145c-3.15 0-5.52-1.47-6-4.44l3.69-.99c.24.75.78 1.8 2.25 1.8.84 0 1.62-.42 1.62-1.29 0-.51-.3-.99-1.32-1.32l-2.1-.78c-2.58-.93-3.69-2.61-3.69-4.56 0-2.91 2.61-4.62 5.67-4.62 2.94 0 5.07 1.65 5.61 4.17l-3.63.9c-.39-1.2-1.17-1.47-1.8-1.47-.9 0-1.35.54-1.35 1.08 0 .51.3.99 1.35 1.32l1.95.72c1.68.57 3.9 1.74 3.9 4.56 0 3.15-2.67 4.92-6.15 4.92ZM67.785 35.145c-3.54 0-7.44-2.67-7.44-8.1s3.9-8.1 7.44-8.1c2.76 0 4.38 1.5 4.62 2.07h.09v-1.77h4.65v15.6h-4.65v-1.77h-.09c-.24.57-1.86 2.07-4.62 2.07Zm-2.85-8.1c0 2.52 1.83 3.96 3.81 3.96 2.04 0 3.87-1.41 3.87-3.96s-1.83-3.96-3.87-3.96c-1.98 0-3.81 1.44-3.81 3.96ZM51.07 18.525c0-4.92 3.45-5.67 5.61-5.67.75 0 1.98.03 2.94.6v3.63c-.84-.36-1.56-.3-1.68-.3-1.56 0-2.22.9-2.22 2.22v.24h3.9v3.69h-3.9v11.91h-4.65v-11.91H49v-3.69h2.07v-.72Z"/>
      <path fill="#FF4C57" d="M18 16c0-1.657 1.34-3 2.996-3H35a3 3 0 1 1 0 6H21a4.978 4.978 0 0 0-3 1v-4Z"/>
      <path fill="#CB37FF" d="M18 24c0-1.657 1.34-3 2.996-3H35a3 3 0 1 1 0 6H21a4.978 4.978 0 0 0-3 1v-4Z"/>
      <path fill="#0469FF" d="M18 32a3 3 0 0 1 2.999-3H25a3 3 0 1 1 0 6h-4a4.978 4.978 0 0 0-3 1v-4Z"/>
      <path fill="#FF4C57" fill-rule="evenodd" d="M13 17.2a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4Zm0 1.8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd"/>
      <path fill="#CB37FF" fill-rule="evenodd" d="M13 25.2a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4Zm0 1.8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd"/>
      <path fill="#0469FF" fill-rule="evenodd" d="M13 33.2a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4Zm0 1.8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd"/>
    </svg>
    <span class="logo-divider"></span>
    <span class="logo-label">API Docs</span>
  </a>
  <nav>
    <a href="https://api.fast.io/current/llms/full/">Full Reference</a>
    <a href="https://mcp.fast.io/mcp">MCP Server</a>
  </nav>
</header>

<div class="layout">

<aside class="sidebar">
  <div class="sidebar-section">
    <div class="sidebar-section-title">Overview</div>
    <a href="#about" class="active">About Fast.io</a>
    <a href="#agent-plan">Agent Plan</a>
    <a href="#profile-hierarchy">Profile Hierarchy</a>
    <a href="#authentication">Authentication</a>
    <a href="#response-envelope">Response Envelope</a>
    <a href="#error-codes">Error Codes</a>
    <a href="#rate-limiting">Rate Limiting</a>
    <a href="#pagination">Pagination</a>
    <a href="#id-formats">ID Formats</a>
    <a href="#field-constraints">Field Constraints</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-title">Agent Workflows</div>
    <a href="#upload-files">Upload Files</a>
    <a href="#query-ai">Query Documents with AI</a>
    <a href="#share-files">Share Files</a>
    <a href="#transfer-ownership">Transfer Ownership</a>
    <a href="#monitor-usage">Monitor Usage</a>
    <a href="#activity-polling">Activity Polling</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-title">API References</div>
    <a href="auth.html">Auth &amp; Users</a>
    <a href="oauth.html">OAuth 2.0</a>
    <a href="orgs.html">Organizations</a>
    <a href="workspaces.html">Workspaces</a>
    <a href="storage.html">Storage</a>
    <a href="shares.html">Shares</a>
    <a href="upload.html">Upload</a>
    <a href="ai.html">AI &amp; Chat</a>
    <a href="events.html">Events &amp; Activity</a>
    <a href="comments.html">Comments</a>
    <a href="workflow.html">Workflow</a>
  </div>
</aside>

<main class="content content-wide">

  <div class="hero">
    <h1>Fast.io API Documentation
      <span class="subtitle">Workspaces for Agentic Teams. Collaborate, share, and query with AI &mdash; all through one API, free.</span>
    </h1>
  </div>

  <div class="meta-bar">
    <span>Base URL: <code>https://api.fast.io/current/</code></span>
    <span>API Version: <code>1.0</code></span>
    <span>Doc Version: <code>2.0</code></span>
    <span>Format: <code>JSON</code></span>
  </div>

  <p>Fast.io provides workspaces for agentic teams &mdash; where agents collaborate with other agents and with humans. Upload outputs, create branded data rooms, ask questions about documents using built-in AI, and hand everything off to a human when the job is done. No infrastructure to manage, no subscriptions, no credit card required.</p>

  <p><strong>For AI agents:</strong> Create an account with <code>agent=true</code>, get 50 GB storage and 5,000 monthly credits free, build workspaces for your team (agents and humans), query documents with built-in RAG, and transfer ownership to humans when ready.</p>

  <p><strong>For MCP-enabled agents:</strong> Connect via the Model Context Protocol to interact with Fast.io workspaces, shares, files, and storage directly. Connect to <code>https://mcp.fast.io/mcp</code> (Streamable HTTP) or <code>https://mcp.fast.io/sse</code> (legacy SSE). The server exposes 14 consolidated tools with action-based routing.</p>

  <h2 id="references">Detailed API References</h2>

  <div class="category-grid">
    <a href="auth.html" class="category-card">
      <h3>Auth &amp; Users</h3>
      <p>Authentication methods, user CRUD, getting started patterns</p>
    </a>
    <a href="oauth.html" class="category-card">
      <h3>OAuth 2.0</h3>
      <p>PKCE flow, token exchange, session management, DCR, resource indicators</p>
    </a>
    <a href="orgs.html" class="category-card">
      <h3>Organizations</h3>
      <p>Org CRUD, members, billing, transfer (agent&rarr;human), discovery</p>
    </a>
    <a href="workspaces.html" class="category-card">
      <h3>Workspaces</h3>
      <p>Workspace CRUD, members, assets, discovery</p>
    </a>
    <a href="storage.html" class="category-card">
      <h3>Storage</h3>
      <p>File/folder operations, locking, previews, transforms</p>
    </a>
    <a href="shares.html" class="category-card">
      <h3>Shares</h3>
      <p>Share types, storage modes, members, branding, quickshare</p>
    </a>
    <a href="upload.html" class="category-card">
      <h3>Upload</h3>
      <p>Chunked upload flow, web upload, status polling</p>
    </a>
    <a href="ai.html" class="category-card">
      <h3>AI &amp; Chat</h3>
      <p>RAG chat, intelligence, notes, metadata extraction</p>
    </a>
    <a href="events.html" class="category-card">
      <h3>Events &amp; Activity</h3>
      <p>Event search, activity polling, WebSocket, realtime</p>
    </a>
    <a href="comments.html" class="category-card">
      <h3>Comments</h3>
      <p>Threading, mentions, reactions, JSON body format</p>
    </a>
    <a href="workflow.html" class="category-card">
      <h3>Workflow</h3>
      <p>Task lists, tasks, worklogs, interjections, approvals, todos</p>
    </a>
  </div>

  <h2 id="about">What Fast.io Does</h2>

  <table>
    <thead>
      <tr><th>Capability</th><th>What It Does</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Workspaces</strong></td><td>Shared workspaces for agentic teams with file versioning, search, and AI chat</td></tr>
      <tr><td><strong>Shares</strong></td><td>Purpose-built spaces for agent-human exchange with two storage modes: <strong>Room</strong> (independent data room with passwords, expiration, guest access) or <strong>Shared Folder</strong> (live-synced workspace folder). Three share types: Send, Receive, Exchange</td></tr>
      <tr><td><strong>Built-in AI</strong></td><td>RAG-powered document Q&amp;A, semantic search, auto-summarization, metadata extraction</td></tr>
      <tr><td><strong>File Preview</strong></td><td>Inline rendering for PDF, images, video, audio, spreadsheets, code &mdash; no download needed</td></tr>
      <tr><td><strong>Ownership Transfer</strong></td><td>Agent builds everything, generates a claim link, human takes over with one click</td></tr>
      <tr><td><strong>Activity Tracking</strong></td><td>Full audit trail with AI-powered natural language summaries</td></tr>
    </tbody>
  </table>

  <h2 id="agent-plan">Agent Plan (Free)</h2>

  <table>
    <thead>
      <tr><th>Resource</th><th>Included</th></tr>
    </thead>
    <tbody>
      <tr><td>Price</td><td>$0 &mdash; no credit card, no trial, no expiration, no auto-deletion</td></tr>
      <tr><td>Storage</td><td>50 GB</td></tr>
      <tr><td>Monthly credits</td><td>5,000 (resets every 30 days)</td></tr>
      <tr><td>Workspaces</td><td>5</td></tr>
      <tr><td>Shares</td><td>50</td></tr>
      <tr><td>Members per workspace</td><td>5</td></tr>
    </tbody>
  </table>

  <p>Credits cover: storage (100/GB), bandwidth (212/GB), AI tokens (1/100 tokens), document ingestion (10/page), video ingestion (5/sec), image ingestion (5/image), file conversions (25/each). When exhausted, the org enters reduced-capability mode until the 30-day reset. The org is never deleted.</p>

  <p><strong>When credits run out (agent accounts):</strong> Transfer ownership to a human who can upgrade. Create a transfer token via <code>POST /current/org/{org_id}/transfer/token/create/</code>, then give the human the claim URL: <code>https://go.fast.io/claim?token={token}</code>. See <a href="orgs.html">Organizations reference</a> for details.</p>

  <p><strong>When credits run out (human accounts):</strong> Direct the user to upgrade at <code>https://fast.io</code> or via <code>POST /current/org/{org_id}/billing/</code>.</p>

  <h2 id="profile-hierarchy">Profile Hierarchy</h2>

  <p>User (Type 1) &rarr; Organization (Type 2) &rarr; Workspace (Type 3) / Share (Type 4)</p>
  <p>Users own organizations. An organization is a collector of workspaces &mdash; it can represent a company, a business unit, a team, or simply a personal collection. Organizations own workspaces and shares. Users can also directly own shares.</p>
  <p>All profile IDs are 19-digit numeric strings (e.g., <code>"1234567890123456789"</code>). Most endpoints also accept a custom name in place of the numeric ID.</p>
  <p>Account types: <code>human</code> or <code>agent</code> &mdash; visible in all user objects via <code>account_type</code> field.</p>

  <h2 id="authentication">Authentication</h2>

  <p>All authenticated endpoints require: <code>Authorization: Bearer {jwt_token}</code></p>

  <p>Four methods:</p>
  <ul>
    <li><strong>Basic Auth &rarr; JWT:</strong> <code>GET /current/user/auth/</code> with HTTP Basic Auth. Returns JWT. If 2FA enabled, token has limited scope until verified.</li>
    <li><strong>OAuth 2.0 PKCE:</strong> For desktop/mobile apps and MCP agents. S256 only. Supports Dynamic Client Registration (RFC 7591), CIMD for URL-based client_id, and Resource Indicators (RFC 8707). See <a href="oauth.html">OAuth reference</a>.</li>
    <li><strong>API Keys:</strong> Long-lived tokens. Same Bearer header. Create via <code>POST /current/user/auth/key/</code>. Optionally supports scoped permissions, agent names, and expiration. Update via <code>POST /current/user/auth/key/{id}/</code>.</li>
    <li><strong>2FA:</strong> Limited-scope token &rarr; full token after <code>POST /current/user/auth/2factor/auth/{token}/</code>.</li>
  </ul>

  <h3>Choose your access pattern</h3>
  <ol>
    <li><strong>Human's account</strong> &mdash; Human creates API key, gives it to you. You operate as them. &rarr; <a href="auth.html">Auth reference</a></li>
    <li><strong>Autonomous agent</strong> &mdash; Create agent account (<code>agent=true</code>), create org, work independently. &rarr; <a href="auth.html">Auth reference</a></li>
    <li><strong>Collaboration</strong> &mdash; Create agent account, human invites you to their org/workspace. &rarr; <a href="auth.html">Auth reference</a></li>
    <li><strong>PKCE browser login</strong> &mdash; Secure, no password sharing, supports SSO. &rarr; <a href="oauth.html">OAuth reference</a></li>
  </ol>

  <h2 id="response-envelope">Response Envelope</h2>

  <p>Success (data fields at root level):</p>
  <pre><code>{"result": true, "status": "ok", ...}</code></pre>

  <p>Error:</p>
  <pre><code>{
  "result": false,
  "error": {
    "code": 195654,
    "text": "Human-readable message",
    "documentation_url": "https://api.fast.io/llms.txt",
    "resource": "POST /current/user/"
  }
}</code></pre>

  <ul>
    <li><code>result</code>: boolean &mdash; <code>true</code> on success, <code>false</code> on error</li>
    <li><code>error.code</code>: Unique error identifier (integer) for debugging</li>
    <li><code>error.text</code>: Human-readable error message, safe to display</li>
    <li><code>error.documentation_url</code>: Link to error documentation (string or null)</li>
    <li><code>error.resource</code>: The endpoint that produced the error</li>
  </ul>

  <h2 id="error-codes">Error Codes</h2>

  <h3>Client Errors</h3>
  <table>
    <thead>
      <tr><th>Code</th><th>Constant</th><th>HTTP Status</th></tr>
    </thead>
    <tbody>
      <tr><td><code>1605</code></td><td>APP_ERROR_INPUT_INVALID</td><td>406 Not Acceptable</td></tr>
      <tr><td><code>1607</code></td><td>APP_ERROR_INPUT_DUPLICATE</td><td>406 Not Acceptable</td></tr>
      <tr><td><code>1650</code></td><td>APP_AUTH_INVALID</td><td>401 Unauthorized</td></tr>
      <tr><td><code>1651</code></td><td>APP_REQUEST_TYPE</td><td>405 Method Not Allowed</td></tr>
      <tr><td><code>1609</code></td><td>APP_ERROR_NOT_FOUND</td><td>404 Not Found</td></tr>
      <tr><td><code>1652</code></td><td>APP_RESOURCE_NOT_FOUND</td><td>404 Not Found</td></tr>
      <tr><td><code>1653</code></td><td>APP_USER_NOT_FOUND</td><td>404 Not Found</td></tr>
      <tr><td><code>1656</code></td><td>APP_EXCEEDED_LIMIT</td><td>413 Payload Too Large</td></tr>
      <tr><td><code>1667</code></td><td>APP_MAX_LIMIT</td><td>429 Too Many Requests</td></tr>
      <tr><td><code>1685</code></td><td>APP_FEATURE_LIMIT</td><td>412 Precondition Failed</td></tr>
      <tr><td><code>1658</code></td><td>APP_NOT_ACCEPTABLE</td><td>406 Not Acceptable</td></tr>
      <tr><td><code>1660</code></td><td>APP_CONFLICT</td><td>409 Conflict</td></tr>
      <tr><td><code>1669</code></td><td>APP_EXISTS</td><td>409 Conflict</td></tr>
      <tr><td><code>1670</code></td><td>APP_RESTRICTED</td><td>406 Not Acceptable</td></tr>
      <tr><td><code>1680</code></td><td>APP_DENIED</td><td>401 Unauthorized</td></tr>
      <tr><td><code>1671</code></td><td>APP_ENHANCE_CALM</td><td>429 Too Many Requests</td></tr>
      <tr><td><code>1677</code></td><td>APP_LOCKED</td><td>423 Locked</td></tr>
    </tbody>
  </table>

  <h3>Server Errors</h3>
  <table>
    <thead>
      <tr><th>Code</th><th>Constant</th><th>HTTP Status</th></tr>
    </thead>
    <tbody>
      <tr><td><code>1654</code></td><td>APP_INTERNAL_ERROR</td><td>500</td></tr>
      <tr><td><code>1664</code></td><td>APP_ERROR_DATASTORE</td><td>500</td></tr>
      <tr><td><code>1686</code></td><td>APP_ERROR_NOT_IMPLEMENTED</td><td>501</td></tr>
    </tbody>
  </table>

  <h2 id="rate-limiting">Rate Limiting</h2>

  <p>Headers: <code>X-Rate-Limit-Available</code>, <code>X-Rate-Limit-Expiry</code>, <code>X-Rate-Limit-Max</code></p>
  <p>When exceeded: HTTP 429 with error code 1671 (<code>APP_ENHANCE_CALM</code>).</p>

  <h2 id="pagination">Pagination</h2>

  <h3>Offset Pagination (List Endpoints)</h3>
  <p>Most list endpoints support offset-based pagination:</p>
  <ul>
    <li><code>limit</code>: 1&ndash;500 (default: 100) &mdash; number of items to return</li>
    <li><code>offset</code>: 0+ (default: 0) &mdash; number of items to skip</li>
    <li>Response: <code>pagination.total</code>, <code>pagination.limit</code>, <code>pagination.offset</code>, <code>pagination.has_more</code></li>
  </ul>

  <h3>Keyset Pagination (Storage List Endpoints)</h3>
  <p>Storage listing uses cursor-based pagination:</p>
  <ul>
    <li><code>sort_by</code>: name | updated | created | type (default: name)</li>
    <li><code>sort_dir</code>: asc | desc (default: asc)</li>
    <li><code>page_size</code>: 100 | 250 | 500 (default: 100)</li>
    <li><code>cursor</code>: opaque string from previous response</li>
    <li>Response: <code>pagination.has_more</code>, <code>pagination.next_cursor</code>, <code>pagination.page_size</code></li>
  </ul>

  <h2 id="id-formats">ID Formats</h2>

  <ul>
    <li><strong>Profile IDs</strong> (user, org, workspace, share): 19-digit numeric string</li>
    <li><strong>Node IDs</strong> (files, folders): OpaqueId &mdash; 30-character alphanumeric with hyphens (e.g., <code>f3jm5-zqzfx-pxdr2-dx8z5-bvnb3-rpjfm4</code>). Prefix: <code>f</code> = file, <code>d</code> = folder, <code>n</code> = note.</li>
    <li><strong>Upload IDs</strong>: OpaqueId &mdash; alphanumeric string</li>
    <li><strong>Opaque IDs</strong> (quickshare tokens): 30-character alphanumeric string</li>
    <li><strong>Special folder aliases</strong>: <code>"root"</code> for storage root, <code>"trash"</code> for trash folder</li>
  </ul>

  <h3>Custom names as identifiers</h3>
  <table>
    <thead>
      <tr><th>Profile Type</th><th>Custom Name</th></tr>
    </thead>
    <tbody>
      <tr><td>Workspace</td><td>Folder name (e.g., <code>my-project</code>)</td></tr>
      <tr><td>Share</td><td>URL name (e.g., <code>q4-financials</code>)</td></tr>
      <tr><td>Organization</td><td>Domain name (e.g., <code>acme</code>)</td></tr>
      <tr><td>User</td><td>Email address (e.g., <code>user@example.com</code>)</td></tr>
    </tbody>
  </table>

  <h2 id="field-constraints">Field Constraints</h2>

  <p>Profile fields (org, workspace, share) have validation rules enforced server-side.</p>

  <table>
    <thead>
      <tr><th>Entity</th><th>Field</th><th>API Key</th><th>Min</th><th>Max</th><th>Regex</th><th>Required</th></tr>
    </thead>
    <tbody>
      <tr><td>Org</td><td>domain</td><td><code>domain</code></td><td>2</td><td>80</td><td><code>^[a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?$</code></td><td>Yes (create)</td></tr>
      <tr><td>Org</td><td>name</td><td><code>name</code></td><td>3</td><td>100</td><td>No control chars</td><td>Yes</td></tr>
      <tr><td>Org</td><td>description</td><td><code>description</code></td><td>10</td><td>1000</td><td>No control chars</td><td>No</td></tr>
      <tr><td>Workspace</td><td>folder_name</td><td><code>folder_name</code></td><td>4</td><td>80</td><td><code>^[\p{L}\p{N}-]+$</code></td><td>Yes (create)</td></tr>
      <tr><td>Workspace</td><td>name</td><td><code>name</code></td><td>2</td><td>100</td><td>No control chars</td><td>Yes</td></tr>
      <tr><td>Workspace</td><td>description</td><td><code>description</code></td><td>10</td><td>1000</td><td>No control chars</td><td>No</td></tr>
      <tr><td>Share</td><td>custom_name</td><td><code>custom_name</code></td><td>4</td><td>80</td><td><code>^[\p{L}\p{N}]+$</code></td><td>Yes (create)</td></tr>
      <tr><td>Share</td><td>title</td><td><code>title</code></td><td>2</td><td>80</td><td>No control chars</td><td>Yes</td></tr>
      <tr><td>Share</td><td>description</td><td><code>description</code></td><td>10</td><td>500</td><td>No control chars</td><td>No</td></tr>
    </tbody>
  </table>

  <h2 id="workflows">Agent Workflows</h2>

  <h3 id="upload-files">Upload Files</h3>
  <p>Small files (&lt; 4MB): single-request upload. Large files: chunked upload with parallel chunks.</p>
  <p>&rarr; Full details: <a href="upload.html">Upload reference</a></p>

  <h3 id="query-ai">Query Documents with AI</h3>
  <p>Create chats with <code>chat</code> (general) or <code>chat_with_files</code> (RAG with citations). Stream responses via SSE.</p>
  <p>&rarr; Full details: <a href="ai.html">AI reference</a></p>

  <h3 id="share-files">Share Files with Humans</h3>
  <p>Create Send/Receive/Exchange shares with Room or Shared Folder storage modes.</p>
  <p>&rarr; Full details: <a href="shares.html">Shares reference</a></p>

  <h3 id="transfer-ownership">Transfer Ownership to a Human</h3>
  <p>Agent creates transfer token &rarr; build claim URL <code>https://go.fast.io/claim?token={token}</code> &rarr; human claims org.</p>
  <p>&rarr; Full details: <a href="orgs.html">Organizations reference</a></p>

  <h3 id="monitor-usage">Monitor Usage</h3>
  <ul>
    <li><code>GET /current/org/{org_id}/billing/usage/limits/credits/</code> &mdash; credit consumption</li>
    <li><code>GET /current/org/{org_id}/billing/usage/meters/list/</code> &mdash; detailed breakdown</li>
    <li><code>GET /current/events/search/</code> &mdash; activity feed</li>
  </ul>
  <p>&rarr; Full details: <a href="events.html">Events reference</a></p>

  <h3 id="activity-polling">Activity Polling</h3>
  <p>Long-poll for changes instead of looping on individual endpoints:</p>
  <pre><code>GET /current/activity/poll/{entityId}?wait=95&amp;lastactivity={timestamp}</code></pre>
  <p>&rarr; Full details: <a href="events.html">Events reference</a></p>

  <h2 id="endpoint-summary">Endpoint Summary</h2>

  <h3>System</h3>
  <table>
    <thead>
      <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
    </thead>
    <tbody>
      <tr><td><span class="method method-get">GET</span></td><td class="endpoint-path">/current/ping/</td><td>Health check (no auth)</td></tr>
      <tr><td><span class="method method-get">GET</span></td><td class="endpoint-path">/current/system/status/</td><td>System status (no auth)</td></tr>
      <tr><td><span class="method method-get">GET</span></td><td class="endpoint-path">/current/llms/</td><td>This reference file (no auth)</td></tr>
      <tr><td><span class="method method-get">GET</span></td><td class="endpoint-path">/current/agents/</td><td>Agent integration guide (no auth)</td></tr>
      <tr><td><span class="method method-get">GET</span></td><td class="endpoint-path">/.well-known/oauth-authorization-server/</td><td>OAuth server metadata (no auth)</td></tr>
      <tr><td><span class="method method-get">GET</span></td><td class="endpoint-path">/.well-known/oauth-protected-resource/</td><td>OAuth resource metadata (no auth)</td></tr>
    </tbody>
  </table>

  <h3>Category References</h3>
  <table>
    <thead>
      <tr><th>Category</th><th>Page</th><th>What It Covers</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Auth &amp; Users</strong></td><td><a href="auth.html">auth.html</a></td><td>Authentication methods, user CRUD, getting started patterns</td></tr>
      <tr><td><strong>OAuth 2.0</strong></td><td><a href="oauth.html">oauth.html</a></td><td>PKCE flow, token exchange, session management, DCR, resource indicators</td></tr>
      <tr><td><strong>Organizations</strong></td><td><a href="orgs.html">orgs.html</a></td><td>Org CRUD, members, billing, transfer (agent&rarr;human), discovery</td></tr>
      <tr><td><strong>Workspaces</strong></td><td><a href="workspaces.html">workspaces.html</a></td><td>Workspace CRUD, members, assets, discovery</td></tr>
      <tr><td><strong>Storage</strong></td><td><a href="storage.html">storage.html</a></td><td>File/folder operations, locking, previews, transforms</td></tr>
      <tr><td><strong>Shares</strong></td><td><a href="shares.html">shares.html</a></td><td>Share types, storage modes, members, branding, quickshare</td></tr>
      <tr><td><strong>Upload</strong></td><td><a href="upload.html">upload.html</a></td><td>Chunked upload flow, web upload, status polling</td></tr>
      <tr><td><strong>AI &amp; Chat</strong></td><td><a href="ai.html">ai.html</a></td><td>RAG chat, intelligence, notes, metadata extraction</td></tr>
      <tr><td><strong>Events &amp; Activity</strong></td><td><a href="events.html">events.html</a></td><td>Event search, activity polling, WebSocket, realtime</td></tr>
      <tr><td><strong>Comments</strong></td><td><a href="comments.html">comments.html</a></td><td>Threading, mentions, reactions, JSON body format</td></tr>
      <tr><td><strong>Workflow</strong></td><td><a href="workflow.html">workflow.html</a></td><td>Task lists, tasks, worklogs, interjections, approvals, todos</td></tr>
    </tbody>
  </table>

  <h2 id="common-patterns">Common Patterns</h2>
  <ul>
    <li>List endpoints return arrays in a <code>response</code> wrapper with consistent pagination</li>
    <li>All profile operations require membership with sufficient permissions</li>
    <li>Owner &gt; Admin &gt; Member &gt; Guest permission hierarchy</li>
    <li><code>"me"</code> can be used as user_id to reference the authenticated user</li>
    <li>Profile path parameters accept either a 19-digit numeric ID or a custom name</li>
    <li>Storage operations (workspace and share) follow identical patterns</li>
    <li>AI chat endpoints (workspace and share) follow identical patterns</li>
    <li>Member management endpoints (org, workspace, share) follow identical patterns</li>
    <li>Long-polling supported on activity/poll and upload/details endpoints</li>
    <li>Most POST endpoints use <code>application/x-www-form-urlencoded</code> bodies; comments use <code>application/json</code></li>
  </ul>

  <h2 id="additional-resources">Additional Resources</h2>
  <ul>
    <li>Full single-file reference: <a href="https://api.fast.io/current/llms/full/">https://api.fast.io/current/llms/full/</a></li>
    <li>Agent integration guide: available at <code>/current/agents/</code></li>
    <li>MCP Server: <code>https://mcp.fast.io/mcp</code> (Streamable HTTP) or <code>https://mcp.fast.io/sse</code> (legacy SSE)</li>
    <li>MCP Skills: available at <code>/skill.md</code> on the MCP server</li>
    <li>Claim URL for org transfer: <code>https://go.fast.io/claim?token={token}</code></li>
  </ul>

  <a href="#" class="back-to-top">&uarr; Back to top</a>

</main>

</div>

<footer class="site-footer">
  Fast.io API Documentation &middot; Generated from <code>llms.txt</code> v2.0
</footer>

</body>
</html>
