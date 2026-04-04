# Source: https://docs.replit.com/replitai/mcp/figma.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Figma MCP integration

> Connect Agent to your Figma files via MCP to explore layers, extract design data, capture screenshots, and generate starter code from designs.

Use Agent with Model Context Protocol (MCP) to work with your Figma designs directly in chat. Paste a Figma link to explore layers, extract variables and components, capture screenshots, and generate code from selected frames.

<Note>
  <strong>Requirements:</strong> A Figma <strong>Dev</strong> or <strong>Full</strong> seat is required for Agent chat features. The import flow at <a href="/getting-started/quickstarts/import-from-figma">replit.com/import</a> does not require a seat.
</Note>

<Callout>
  Want to turn a Figma design into a new app? See the <a href="/getting-started/quickstarts/import-from-figma">Import from Figma quickstart</a>.
</Callout>

<Note>
  The Figma MCP integration uses a <strong>remote server</strong>—you do not need the Figma desktop app running or installed to use this feature in Agent.
</Note>

## Features

* **Generate starter code**: Turn selected frames into production-ready code to bootstrap features or iterate faster.
* **Extract design data**: Access variables, components, and layout specifications defined in your file.
* **Capture frame screenshots**: Create visual references from any frame to guide implementation.
* **Inspect MCP activity**: Expand chat events to view raw requests and responses.

## Demo

Watch a quick walkthrough of the workflow from link detection to code generation:

<Frame>
  <video autoPlay muted loop playsInline src="https://cdn.replit.com/sanity/figma-mcp-v3.mp4" />
</Frame>

## Usage

### Connect in Agent chat

1. Open Agent chat in your workspace.
2. Paste a valid Figma file or prototype link into the message box.
3. When a valid link is detected, a <strong>Figma design</strong> card appears. Click <strong>Log in with Figma</strong> to authorize.

After pasting a supported link, Agent shows a Figma design card for quick authorization:

<Frame>
  <img src="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/figma-design-card.png?fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=91abb671ede47c85eaadc4b5f5faf88e" alt="Connect Figma card appears in Agent chat when a valid Figma link is pasted" data-og-width="475" width="475" data-og-height="216" height="216" data-path="images/replitai/mcp-figma/figma-design-card.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/figma-design-card.png?w=280&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=6120628c4a54bcec34d1564c1ac07b6f 280w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/figma-design-card.png?w=560&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=77c77487202edff5e8500d4921ecba83 560w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/figma-design-card.png?w=840&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=a10bc1b7a1d2e5ff53a2520f3d57345e 840w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/figma-design-card.png?w=1100&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=dd1d2e213aacefb7b6959a0f96a58249 1100w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/figma-design-card.png?w=1650&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=3f4c45e6c607f692584bfa30b8687dea 1650w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/figma-design-card.png?w=2500&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=76d78c1ab80fe848e7f790692a74bfe7 2500w" />
</Frame>

### Work with Figma links

Use link-based workflows to act on precise parts of your design:

1. In Figma, copy the link to any frame or layer.
2. Share the URL with Agent in the chat box and describe what you want.

In Figma, copy a link to the exact frame or layer you want Agent to work with:

<Frame>
  <img src="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/client-link.png?fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=25c66c48dac21b5fe527c32f0586e4f9" alt="Selecting a frame in Figma" data-og-width="1000" width="1000" data-og-height="612" height="612" data-path="images/replitai/mcp-figma/client-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/client-link.png?w=280&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=c079a76dc73124ff824bf3c5c1cb5af8 280w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/client-link.png?w=560&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=6601c38ac881ce1b5b92a13c0311b05e 560w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/client-link.png?w=840&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=a3a469f1cc89970a6bfc926f22f0833b 840w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/client-link.png?w=1100&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=8d1ce6f53b9744195d43023b716fe78a 1100w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/client-link.png?w=1650&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=14117f9c30f1848e062fc5123aaa9f94 1650w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/client-link.png?w=2500&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=c1f0284e744e3ea7948d9d1af01a2515 2500w" />
</Frame>

Then paste the link into Agent along with a short instruction (for example, “generate React for this frame”):

<Frame>
  <img src="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/agent-chat.png?fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=2e1d278c4f81028e2cb11b475435cb2b" alt="Sharing the URL with Agent in the chat box" data-og-width="921" width="921" data-og-height="495" height="495" data-path="images/replitai/mcp-figma/agent-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/agent-chat.png?w=280&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=9186669441c087d436bb216718fe48ea 280w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/agent-chat.png?w=560&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=62c0fca4f7086e5662a9e3b33b892a84 560w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/agent-chat.png?w=840&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=69c1ada31f470257d980089ef2739c77 840w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/agent-chat.png?w=1100&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=9d743f52e6537f855ff57da249605d32 1100w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/agent-chat.png?w=1650&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=8e076e7396ae2c5bfe002bb3c16eabed 1650w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/agent-chat.png?w=2500&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=9c280d4e9e5acfce96c569edd585e45e 2500w" />
</Frame>

### View MCP calls

Open the timeline event labeled <strong>Used Figma MCP (Beta)</strong> to see the underlying requests and responses.

Here is where to expand the timeline event to inspect MCP calls:

<Frame>
  <img src="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/mcp-calls.png?fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=a0277ab413c385d4c2ef9e2d3a30e26f" alt="Expanded chat event showing MCP calls to the Figma integration" data-og-width="725" width="725" data-og-height="928" height="928" data-path="images/replitai/mcp-figma/mcp-calls.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/mcp-calls.png?w=280&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=667d336b6e15e63a76660440391d4873 280w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/mcp-calls.png?w=560&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=5214cea4b13905305a1ed7c79764a40e 560w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/mcp-calls.png?w=840&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=7ef52a06bc1f4bdf218b0822b92662d3 840w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/mcp-calls.png?w=1100&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=422e4ffe776b64636749524ac438ce8a 1100w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/mcp-calls.png?w=1650&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=7f0b6cbb222e13819eeb65f89187c002 1650w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/mcp-calls.png?w=2500&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=df0fecad423a3512eb12a82d786f5ae6 2500w" />
</Frame>

<Callout>
  MCP access to Figma is read‑oriented and respects your Figma permissions. If a file is private or you lack access, the integration cannot fetch content.
</Callout>

### Manage connections

Manage or disconnect the Figma integration at <a href="https://replit.com/integrations" target="_blank" rel="noreferrer">replit.com/integrations</a>.

Find and manage connections from your workspace integrations:

<Frame>
  <img src="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/managing-mcps.png?fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=800e9bfe4881c4ec6785646f11151198" alt="Integrations pane in the personal workspace showing the Figma integration" data-og-width="2384" width="2384" data-og-height="468" height="468" data-path="images/replitai/mcp-figma/managing-mcps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/managing-mcps.png?w=280&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=335235b2325770e97bccefdb2df061d8 280w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/managing-mcps.png?w=560&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=ba72df97e19c8c1fc88fba90dd230d93 560w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/managing-mcps.png?w=840&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=a14080b8a9ff3d651a0ebee78a04dae7 840w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/managing-mcps.png?w=1100&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=9bfad8a9041738e6a8d6c313bd77ad5c 1100w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/managing-mcps.png?w=1650&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=63577a63ee078465f66b8c2ee1ebccdd 1650w, https://mintcdn.com/replit/SLo-1yBQr-cqDnLT/images/replitai/mcp-figma/managing-mcps.png?w=2500&fit=max&auto=format&n=SLo-1yBQr-cqDnLT&q=85&s=1370a0f4cd8a1d2319c2ef40d6296b66 2500w" />
</Frame>
