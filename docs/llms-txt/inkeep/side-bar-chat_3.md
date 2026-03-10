# Source: https://docs.inkeep.com/talk-to-your-agents/react/side-bar-chat

# Add Sidebar Chat to React (/talk-to-your-agents/react/side-bar-chat)

Integrate Inkeep's sidebar chat component into your React application for seamless agent conversations.



The InkeepSidebarChat component provides a slide-out panel interface for conversing with your agents. It can be positioned on either side of your application and supports both manual triggering and automatic element triggers.

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

    ### Trigger through React state

    ```tsx
    import { useState } from "react";
    import { InkeepSidebarChat, type InkeepSidebarChatProps } from "@inkeep/agents-ui";

    export default function App() {
      const [isOpen, setIsOpen] = useState(false);

      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/run/api/chat",
          apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
        },
        position: "right",
        openSettings: {
          isOpen: isOpen,
          onOpenChange: setIsOpen,
        },
      };

      return (
        <div>
          <button onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? "Close" : "Open"} Sidebar Chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    ### Trigger through data attributes

    ```tsx
    import {
      InkeepSidebarChat,
      type InkeepSidebarChatProps,
    } from "@inkeep/agents-ui";

    export default function App() {
      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/run/api/chat",
          apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
        },
        position: "right",
      };

      return (
        <div>
          <button data-inkeep-sidebar-chat-trigger>
            Click here to open sidebar chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
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

    ### Trigger through React state

    ```tsx
    import { useState } from "react";
    import {
      InkeepSidebarChat,
      type InkeepSidebarChatProps,
    } from "@inkeep/agents-ui";

    export default function App() {
      const [isOpen, setIsOpen] = useState(false);

      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "http://localhost:3002/run/api/chat",
          headers: {
            "x-inkeep-tenant-id": "your-tenant-id",
            "x-inkeep-project-id": "your-project-id",
            "x-inkeep-agent-id": "your-agent-id",
          },
        },
        position: "right",
        openSettings: {
          isOpen: isOpen,
          onOpenChange: setIsOpen,
        },
      };

      return (
        <div>
          <button onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? "Close" : "Open"} Sidebar Chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    ### Trigger through data attributes

    ```tsx
    import {
      InkeepSidebarChat,
      type InkeepSidebarChatProps,
    } from "@inkeep/agents-ui";

    export default function App() {
      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "http://localhost:3002/run/api/chat",
          headers: {
            "x-inkeep-tenant-id": "your-tenant-id",
            "x-inkeep-project-id": "your-project-id",
            "x-inkeep-agent-id": "your-agent-id",
          },
        },
        position: "right",
      };

      return (
        <div>
          <button data-inkeep-sidebar-chat-trigger>
            Click here to open sidebar chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Configuration Options

### Required Props

| Property                  | Type   | Description                                         |
| ------------------------- | ------ | --------------------------------------------------- |
| `aiChatSettings`          | object | Configuration for the AI chat connection            |
| `aiChatSettings.agentUrl` | string | The URL of your agent endpoint                      |
| `aiChatSettings.headers`  | object | Headers for authentication and agent identification |

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
