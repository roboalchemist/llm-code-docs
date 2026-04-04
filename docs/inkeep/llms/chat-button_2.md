# Source: https://docs.inkeep.com/talk-to-your-agents/nextjs/chat-button

# Chat Button for Next.js (/talk-to-your-agents/nextjs/chat-button)

Use the chat button component in Next.js with App Router and dynamic import.



<Note>
  For Next.js apps that use App Router, use the `"use client"` directive at the
  top of the file to load the widget client-side.
</Note>

The chat button component is a simple way to trigger the Inkeep chat bubble. In Next.js, load it with `next/dynamic` and `ssr: false`.

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

    ```tsx
    'use client';

    import dynamic from 'next/dynamic';
    import type { InkeepChatButtonProps } from '@inkeep/agents-ui';

    const InkeepChatButton = dynamic(
      () => import('@inkeep/agents-ui').then((mod) => mod.InkeepChatButton),
      { ssr: false },
    );

    const buttonProps: InkeepChatButtonProps = {
      aiChatSettings: {
        agentUrl: 'https://your-api.example.com/run/api/chat',
        apiKey: process.env.NEXT_PUBLIC_INKEEP_API_KEY,
      },
    };

    export default function ChatButton() {
      return <InkeepChatButton {...buttonProps} />;
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

    ```tsx
    'use client';

    import dynamic from 'next/dynamic';
    import type { InkeepChatButtonProps } from '@inkeep/agents-ui';

    const InkeepChatButton = dynamic(
      () => import('@inkeep/agents-ui').then((mod) => mod.InkeepChatButton),
      { ssr: false },
    );

    const buttonProps: InkeepChatButtonProps = {
      aiChatSettings: {
        agentUrl: 'http://localhost:3003/api/chat',
        headers: {
          'x-inkeep-tenant-id': 'your-tenant-id',
          'x-inkeep-project-id': 'your-project-id',
          'x-inkeep-agent-id': 'your-agent-id',
        },
      },
    };

    export default function ChatButton() {
      return <InkeepChatButton {...buttonProps} />;
    }
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Props

<AutoTypeTable name="default" type="export { InkeepChatButtonProps as default } from '@inkeep/agents-ui'" />

<>
  ### InkeepBaseSettings

  <AutoTypeTable name="default" type="export { InkeepBaseSettings as default } from '@inkeep/agents-ui/types'" />

  #### ColorModeConfig

  <AutoTypeTable name="default" type="export { ColorModeConfig as default } from '@inkeep/agents-ui/types'" />

  #### UserProperties

  <AutoTypeTable name="default" type="export { UserProperties as default } from '@inkeep/agents-ui/types'" />
</>

### OpenSettingsChatButton

<AutoTypeTable name="default" type="export { OpenSettingsChatButton as default } from '@inkeep/agents-ui/types'" />

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
