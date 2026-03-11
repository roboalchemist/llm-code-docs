# Source: https://docs.anyscale.com/kb/vscode-vpn-chrome-loading.md

# VS Code not loading in workspace over VPN (Chrome)

[View Markdown](/kb/vscode-vpn-chrome-loading.md)

# VS Code not loading in workspace over VPN (Chrome)

This article explains how to fix VS Code not loading in an Anyscale workspace when you use Chrome and connect through a VPN. It applies to workspaces in private clouds that require VPN access, for example Tailscale. The fix involves Chrome's Local Network Access setting.

## Symptoms[​](#symptoms "Direct link to Symptoms")

When opening a workspace that runs VS Code while connected through a VPN, VS Code might not load. Instead of the editor, you might see a grey screen with a message such as:

```
The connection is blocked because it was initiated by a public page to connect to devices or servers on your local network.
```

The cluster is running and reachable over the VPN. The problem is the browser blocking the connection to the head node.

## Cause[​](#cause "Direct link to Cause")

Chrome's **Local Network Access** setting prompts you when a page tries to send a request to a local server, including certain private IP ranges. When the workspace head node is behind a VPN, Chrome can treat its address as local—for example, Tailscale uses the `100.64.0.0/10` range, which Chrome may classify as local. If you block the request when prompted, the browser blocks the connection and VS Code can't load.

This issue only appears when all of the following are true:

* The workspace is in a private cloud that requires VPN access
* You're using Chrome or another Chromium-based browser
* You haven't yet granted local network access for this case, or you previously denied the prompt

## Solution[​](#solution "Direct link to Solution")

Use one of the following approaches. Both are valid; choose based on your preference.

### Option 1: Disable local network access checks (recommended for unblocking)[​](#option-1-disable-local-network-access-checks-recommended-for-unblocking "Direct link to Option 1: Disable local network access checks (recommended for unblocking)")

Many users deny the initial Chrome prompt because it looks like a security warning. Disabling the setting avoids that prompt and lets VS Code connect.

1. In Chrome's address bar, open:
   <!-- -->
   ```
   chrome://flags/#local-network-access-check
   ```
2. Select **Disabled** for **Local Network Access Checks**.
3. Restart Chrome when prompted.

### Option 2: Keep the setting enabled and allow the request[​](#option-2-keep-the-setting-enabled-and-allow-the-request "Direct link to Option 2: Keep the setting enabled and allow the request")

If you prefer to keep Local Network Access Checks enabled, allow the request when Chrome prompts you to send a request to a local server. When the prompt appears, accept it so the workspace page can connect to the head node. You may need to refresh the page after accepting.

## Verification[​](#verification "Direct link to Verification")

After applying either solution, refresh the workspace page in your browser. VS Code should load in the iframe and you can use it normally.

## Related resources[​](#related "Direct link to Related resources")

* [Workspaces](/platform/workspaces.md)
