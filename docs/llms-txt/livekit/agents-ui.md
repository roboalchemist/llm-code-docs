# Source: https://docs.livekit.io/reference/components/agents-ui.md

# Source: https://docs.livekit.io/frontends/components/agents-ui.md

LiveKit docs › UI Components › Agents UI

---

# Agents UI overview

> Agents UI is the fastest way to build multi-modal, agentic experiences on top of LiveKit's platform primitives.

## Overview

Agents UI is a component library built on top of [Shadcn](https://ui.shadcn.com/) and [AI Elements](https://ai-sdk.dev/elements) to accelerate the creation of agentic applications built with LiveKit's real-time platform. It provides pre-built components for controlling IO, managing sessions, rendering transcripts, visualing audio streams, and more.

The [AgentAudioVisualizerAura](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-aura.md) component featured above was designed in partnership with Unicorn Studio

## Quick reference

### Prerequisites

Before installing Agents UI, make sure your environment meets the following requirements:

- [Node.js](https://nodejs.org/), version 18 or later
- [Shadcn](https://ui.shadcn.com/docs/installation/next) is installed in your project.

> ℹ️ **Note**
> 
> Running any install command will automatically install shadcn/ui for you. Agents UI is built targeting React 19 (no `forwardRef` usage) and Tailwind CSS 4.

### Installation

You can install Agents UI components using the Shadcn CLI.

Confirm you've navigated to the root of your project, and if you haven’t set up shadcn run:

```bash
npx shadcn@latest init

```

Then add the Agents UI registry with:

```bash
npx shadcn@latest registry add @agents-ui

```

Finally, install the components you need from the CLI with:

```bash
npx shadcn@latest add @agents-ui/{component-name}

```

### Usage

Most Agents UI components require access to a LiveKit session object for access to values like agent state or audio tracks. A Session object can be created from a [TokenSource](https://docs.livekit.io/reference/client-sdk-js/variables/TokenSource.html.md), and provided by wrapping the component in an [AgentSessionProvider](https://docs.livekit.io/reference/components/agents-ui/component/agent-session-provider.md).

```tsx
'use client';

import { useSession } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentControlBar } from '@/components/agents-ui/agent-control-bar';

const TOKEN_SOURCE = TokenSource.sandboxTokenServer(
  process.env.NEXT_PUBLIC_ SANDBOX_TOKEN_SERVER_ID
);

export function Demo() {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <AgentControlBar
        variant={{variant}}
        isChatOpen={{isChatOpen}}
        isConnected={{isConnected}}
        controls={{controls}}
      />
    </AgentSessionProvider>
  );
}

```

## Extensibility

Agents UI components take as many primitive attributes as possible. For example, the [AgentControlBar](https://docs.livekit.io/reference/components/agents-ui/component/agent-control-bar/page.mdoc.md) component extends `HTMLAttributes<HTMLDivElement>`, so you can pass any props that a div supports. This makes it easy to extend the component with your own styles or functionality.

You can edit any Agents UI component's source code in the `components/agents-ui` directory. For style changes, we recommend passing in tailwind classes to override the default styles. Take a look at the [source code](https://github.com/livekit/components-js/tree/main/packages/shadcn) to get a sense of how to override a component's default styles.

If you reinstall any Agents UI components by rerunning `npx shadcn@latest add @agents-ui/{component-name}`, the CLI will ask before overwriting the file so you can avoid losing any customizations you made.

After installation, no additional setup is needed. The component's styles (Tailwind CSS classes) and scripts are already integrated. You can start building with the component in your app immediately.

## Additional resources

Find in-depth API reference documentation for our Agents UI components references below.

- **[Agents UI reference](https://docs.livekit.io/reference/components/agents-ui.md)**: Beautiful components, built with shadcn/ui.

- **[GitHub repository](https://github.com/livekit/components-js/tree/main/packages/shadcn)**: Open source React component code.

---

This document was rendered at 2026-02-03T03:25:08.894Z.
For the latest version of this document, see [https://docs.livekit.io/frontends/components/agents-ui.md](https://docs.livekit.io/frontends/components/agents-ui.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).