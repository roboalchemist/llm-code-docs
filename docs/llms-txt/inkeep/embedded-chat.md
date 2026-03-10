# Source: https://docs.inkeep.com/talk-to-your-agents/javascript/embedded-chat

# Embedded Chat for JavaScript (/talk-to-your-agents/javascript/embedded-chat)

Integrate Inkeep's embedded chat component directly into your JavaScript application for inline agent conversations.



The EmbeddedChat widget provides a fully embedded chat interface that you can integrate directly into your JavaScript application's layout. Unlike modal or sidebar implementations, the embedded chat becomes part of your page structure, perfect for dedicated support pages, dashboards, or help centers.

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
    <div style="display: flex; align-items: center; justify-content: center; height: calc(100vh - 16px);">
      <div style="max-height: 600px; height: 100%;">
        <div id="ikp-embedded-chat-target"></div>
      </div>
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
      const widget = Inkeep.EmbeddedChat("#ikp-embedded-chat-target", config);
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
