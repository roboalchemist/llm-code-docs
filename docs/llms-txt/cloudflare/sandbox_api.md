# Source: https://developers.cloudflare.com/sandbox/api/index.md

---

title: API Reference · Cloudflare Sandbox SDK docs
description: The Sandbox SDK provides a comprehensive API for executing code,
  managing files, running processes, and exposing services in isolated
  sandboxes.
lastUpdated: 2026-02-09T23:08:08.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/sandbox/api/
  md: https://developers.cloudflare.com/sandbox/api/index.md
---

The Sandbox SDK provides a comprehensive API for executing code, managing files, running processes, and exposing services in isolated sandboxes.

[Lifecycle](https://developers.cloudflare.com/sandbox/api/lifecycle/)

Create and manage sandbox containers. Get sandbox instances, configure options, and clean up resources.

[Commands](https://developers.cloudflare.com/sandbox/api/commands/)

Execute commands and stream output. Run scripts, manage background processes, and capture execution results.

[Files](https://developers.cloudflare.com/sandbox/api/files/)

Read, write, and manage files in the sandbox filesystem. Includes directory operations and file metadata.

[File Watching](https://developers.cloudflare.com/sandbox/api/file-watching/)

Monitor real-time filesystem changes using native inotify. Build development tools, hot-reload systems, and responsive file processing.

[Code Interpreter](https://developers.cloudflare.com/sandbox/api/interpreter/)

Execute Python and JavaScript code with rich outputs including charts, tables, and formatted data.

[Ports](https://developers.cloudflare.com/sandbox/api/ports/)

Expose services running in the sandbox via preview URLs. Access web servers and APIs from the internet.

[Storage](https://developers.cloudflare.com/sandbox/api/storage/)

Mount S3-compatible buckets (R2, S3, GCS) as local filesystems for persistent data storage across sandbox lifecycles.

[Sessions](https://developers.cloudflare.com/sandbox/api/sessions/)

Create isolated execution contexts within a sandbox. Each session maintains its own shell state, environment variables, and working directory.

[Terminal](https://developers.cloudflare.com/sandbox/api/terminal/)

Connect browser-based terminal UIs to sandbox shells via WebSocket, with the xterm.js SandboxAddon for automatic reconnection and resize handling.
