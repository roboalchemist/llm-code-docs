# Source: https://docs.inkeep.com/talk-to-your-agents/nextjs/side-bar-chat

# Add Sidebar Chat to Next.js (/talk-to-your-agents/nextjs/side-bar-chat)

Integrate Inkeep's sidebar chat component in Next.js with App Router and dynamic import.



<Note>
  For Next.js apps that use App Router, use the `"use client"` directive at the
  top of the file to load the widget client-side.
</Note>

The InkeepSidebarChat component provides a slide-out panel for conversing with your agents. In Next.js, load it with `next/dynamic` and `ssr: false`. It can be positioned on either side and supports state or data-attribute triggers.

## Installation

<CodeGroup>
  ```bash title="npm"
  npm install @inkeep/agents-ui
  ```

  ```bash title="yarn"
  yarn add @inkeep/agents-ui
  ```

  ```bash title="pnpm"
  pnpm add @inkeep/agents-ui
  ```
</CodeGroup>

## Quick Start

<Tabs>
  <Tab title="Production">
    Use an API key for secure authentication in production:

    ### Trigger through state

    ```tsx
    'use client';

    import { useState } from 'react';
    import dynamic from 'next/dynamic';
    import type { InkeepSidebarChatProps } from '@inkeep/agents-ui';

    const InkeepSidebarChat = dynamic(
      () => import('@inkeep/agents-ui').then((mod) => mod.InkeepSidebarChat),
      { ssr: false },
    );

    export default function SidebarChatPage() {
      const [isOpen, setIsOpen] = useState(false);

      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: 'https://your-api.example.com/run/api/chat',
          apiKey: process.env.NEXT_PUBLIC_INKEEP_API_KEY,
        },
        position: 'right',
        openSettings: {
          isOpen,
          onOpenChange: setIsOpen,
        },
      };

      return (
        <div>
          <button onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? 'Close' : 'Open'} Sidebar Chat
          </button>
          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    ### Trigger through data attributes

    ```tsx
    'use client';

    import dynamic from 'next/dynamic';
    import type { InkeepSidebarChatProps } from '@inkeep/agents-ui';

    const InkeepSidebarChat = dynamic(
      () => import('@inkeep/agents-ui').then((mod) => mod.InkeepSidebarChat),
      { ssr: false },
    );

    const sidebarChatProps: InkeepSidebarChatProps = {
      aiChatSettings: {
        agentUrl: 'https://your-api.example.com/run/api/chat',
        apiKey: process.env.NEXT_PUBLIC_INKEEP_API_KEY,
      },
      position: 'right',
    };

    export default function SidebarChatPage() {
      return (
        <>
          <button data-inkeep-sidebar-chat-trigger>
            Click here to open sidebar chat
          </button>
          <InkeepSidebarChat {...sidebarChatProps} />
        </>
      );
    }
    ```

    **To get an API key:**

    1. Open the Visual Builder Dashboard
    2. Navigate to your Project → **API Keys**
    3. Click **Create New Key** and select your agent
    4. Copy the key (shown once) and store it in your environment variables
  </Tab>

  <Tab title="Development">
    For local development, use headers with your agent IDs:

    ### Trigger through state

    ```tsx
    'use client';

    import { useState } from 'react';
    import dynamic from 'next/dynamic';
    import type { InkeepSidebarChatProps } from '@inkeep/agents-ui';

    const InkeepSidebarChat = dynamic(
      () => import('@inkeep/agents-ui').then((mod) => mod.InkeepSidebarChat),
      { ssr: false },
    );

    export default function SidebarChatPage() {
      const [isOpen, setIsOpen] = useState(false);

      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: 'http://localhost:3002/run/api/chat',
          headers: {
            'x-inkeep-tenant-id': 'your-tenant-id',
            'x-inkeep-project-id': 'your-project-id',
            'x-inkeep-agent-id': 'your-agent-id',
          },
        },
        position: 'right',
        openSettings: {
          isOpen,
          onOpenChange: setIsOpen,
        },
      };

      return (
        <div>
          <button onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? 'Close' : 'Open'} Sidebar Chat
          </button>
          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    ### Trigger through data attributes

    ```tsx
    'use client';

    import dynamic from 'next/dynamic';
    import type { InkeepSidebarChatProps } from '@inkeep/agents-ui';

    const InkeepSidebarChat = dynamic(
      () => import('@inkeep/agents-ui').then((mod) => mod.InkeepSidebarChat),
      { ssr: false },
    );

    const sidebarChatProps: InkeepSidebarChatProps = {
      aiChatSettings: {
        agentUrl: 'http://localhost:3002/run/api/chat',
        headers: {
          'x-inkeep-tenant-id': 'your-tenant-id',
          'x-inkeep-project-id': 'your-project-id',
          'x-inkeep-agent-id': 'your-agent-id',
        },
      },
      position: 'right',
    };

    export default function SidebarChatPage() {
      return (
        <>
          <button data-inkeep-sidebar-chat-trigger>
            Click here to open sidebar chat
          </button>
          <InkeepSidebarChat {...sidebarChatProps} />
        </>
      );
    }
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Configuration Options

### Required Props

| Property                  | Type   | Description                              |
| ------------------------- | ------ | ---------------------------------------- |
| `aiChatSettings`          | object | Configuration for the AI chat connection |
| `aiChatSettings.agentUrl` | string | The URL of your agent endpoint           |
| `aiChatSettings.headers`  | object | Headers for authentication (dev)         |

## Props

<AutoTypeTable name="default" type="export { InkeepSidebarChatProps as default } from '@inkeep/agents-ui'" />

<>
  ### InkeepBaseSettings

  <AutoTypeTable name="default" type="export { InkeepBaseSettings as default } from '@inkeep/agents-ui/types'" />

  #### ColorModeConfig

  <AutoTypeTable name="default" type="export { ColorModeConfig as default } from '@inkeep/agents-ui/types'" />

  #### UserProperties

  <AutoTypeTable name="default" type="export { UserProperties as default } from '@inkeep/agents-ui/types'" />
</>

<>
  ### InkeepAIChatSettings

  <AutoTypeTable name="default" type="export { InkeepAIChatSettings as default } from '@inkeep/agents-ui/types'" />

  #### AIChatFunctions

  <AutoTypeTable name="default" type="export { AIChatFunctions as default } from '@inkeep/agents-ui/types'" />

  #### AIChatDisclaimerSettings

  <AutoTypeTable name="default" type="export { AIChatDisclaimerSettings as default } from '@inkeep/agents-ui/types'" />

  #### GetHelpOption

  <AutoTypeTable name="default" type="export { GetHelpOption as default } from '@inkeep/agents-ui/types'" />

  #### CustomMessageAction

  <AutoTypeTable name="default" type="export { CustomMessageAction as default } from '@inkeep/agents-ui/types'" />

  #### AIChatToolbarButtonLabels

  <AutoTypeTable name="default" type="export { AIChatToolbarButtonLabels as default } from '@inkeep/agents-ui/types'" />

  #### SearchAndChatFilters

  <AutoTypeTable name="default" type="export { SearchAndChatFilters as default } from '@inkeep/agents-ui/types'" />

  #### ComponentsConfig

  <AutoTypeTable name="default" type="export { ComponentsConfig as default } from '@inkeep/agents-ui/types'" />
</>

### OpenSettingsSidebar

<AutoTypeTable name="default" type="export { OpenSettingsSidebar as default } from '@inkeep/agents-ui/types'" />
