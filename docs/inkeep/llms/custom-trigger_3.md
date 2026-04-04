# Source: https://docs.inkeep.com/talk-to-your-agents/react/custom-trigger

# Custom Trigger (/talk-to-your-agents/react/custom-trigger)

Create custom UI elements to trigger Inkeep modals with complete control over appearance and behavior.



## Overview

Custom triggers give you complete control over how users open Inkeep modals in your React application. Instead of using pre-built components like `InkeepChatButton`, you can create your own UI elements that match your design system while maintaining full functionality.

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
    import { useState } from "react";
    import { InkeepModalChat, type InkeepModalChatProps } from "@inkeep/agents-ui";

    function App() {
      const [isModalOpen, setIsModalOpen] = useState(false);

      const modalProps: InkeepModalChatProps = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/api/chat",
          apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
        },
        openSettings: {
          isOpen: isModalOpen,
          onOpenChange: setIsModalOpen,
        },
      };

      return (
        <>
          <button onClick={() => setIsModalOpen(true)}>
            Open Inkeep Assistant
          </button>

          <InkeepModalChat {...modalProps} />
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

    ```tsx
    import { useState } from "react";
    import {
      InkeepModalChat,
      type InkeepModalChatProps,
    } from "@inkeep/cxkit-react";

    function App() {
      const [isModalOpen, setIsModalOpen] = useState(false);

      const modalProps: InkeepModalChatProps = {
        aiChatSettings: {
          agentUrl: "http://localhost:3003/api/chat",
          headers: {
            "x-inkeep-tenant-id": "your-tenant-id",
            "x-inkeep-project-id": "your-project-id",
            "x-inkeep-agent-id": "your-agent-id",
          },
        },
        openSettings: {
          isOpen: isModalOpen,
          onOpenChange: setIsModalOpen,
        },
      };

      return (
        <>
          <button onClick={() => setIsModalOpen(true)}>
            Open Inkeep Assistant
          </button>

          <InkeepModalChat {...modalProps} />
        </>
      );
    }
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Props

<AutoTypeTable name="default" type="export { InkeepModalChatProps as default } from '@inkeep/agents-ui'" />

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

### OpenSettingsModal

<AutoTypeTable name="default" type="export { OpenSettingsModal as default } from '@inkeep/agents-ui/types'" />
