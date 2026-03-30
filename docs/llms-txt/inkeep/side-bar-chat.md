# Source: https://docs.inkeep.com/talk-to-your-agents/javascript/side-bar-chat

# Add Sidebar Chat with JavaScript (/talk-to-your-agents/javascript/side-bar-chat)

Integrate Inkeep's sidebar chat component into your JavaScript application for seamless agent conversations.



The SidebarChat widget provides a slide-out panel interface for conversing with your agents. It can be positioned on either side of your application and supports both manual triggering and automatic element triggers.

## Quick Start

<Steps>
  <Step>
    Add the below `<script>` tag to the `<head>` or `<body>` of your website.

    ```html
    <script
        type="module"
        src="https://cdn.jsdelivr.net/npm/@inkeep/agents-ui-js@0.15/dist/embed.js"
        defer

    > </script>

    ```
  </Step>

  <Step>
    Define an element in your page that will be the "container" for the embedded chat.

    ```html
    <div style="display: flex; flex-direction: row; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow: hidden;">
      <div style="display: flex; flex-direction: column; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow-y: auto; flex: 1;">
        <!-- your app content here -->
      </div>
      <!-- the sidebar chat will be inserted into this div -->
      <div id="sidebar-chat"></div>
    </div>
    ```
  </Step>

  <Step>
    Add a button element that will trigger the sidebar chat and give it the data attribute data-inkeep-sidebar-chat-trigger. You can also use your own custom attribute if you prefer, just be sure to pass it to the triggerSelector prop.

    ```html
    <div style="display: flex; flex-direction: row; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow: hidden;">
      <div style="display: flex; flex-direction: column; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow-y: auto; flex: 1;">
        <!-- your app content here -->
        <button data-inkeep-sidebar-chat-trigger="">Toggle Sidebar Chat</button>
      </div>
      <!-- the sidebar chat will be inserted into this div -->
      <div id="ikp-sidebar-chat-target"></div>
    </div>
    ```
  </Step>

  <Step>
    Insert the EmbeddedChat widget by using the `Inkeep.EmbeddedChat()` function.

    ```ts
    <script type="module">
      const config = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/run/api/chat",
          apiKey: process.env.INKEEP_API_KEY, // Your API key
        },
      };

      // Initialize the widget
      const widget = Inkeep.SidebarChat("#ikp-sidebar-chat-target", config);
    </script>
    ```
  </Step>
</Steps>

## Config

<AutoTypeTable name="default" type="export { InkeepEmbeddedChatProps as default } from '@inkeep/agents-ui'" />

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
