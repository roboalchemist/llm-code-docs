# Source: https://docs.inkeep.com/talk-to-your-agents/javascript/chat-button

# Chat Button for JavaScript (/talk-to-your-agents/javascript/chat-button)

Learn how to use the chat button component in JavaScript



The chat button component is a simple way to trigger the Inkeep chat bubble in your JavaScript application.

## Quick Start

<Steps>
  <Step>
    Add the below `<script>` tag to the `<head>` or `<body>` of your website.

    ```html
    <script
        type="module"
        src="https://cdn.jsdelivr.net/npm/@inkeep/agents-ui-js@0.15/dist/embed.js"
        defer
    ></script>
    ```
  </Step>

  <Step>
    Insert the Chat Button by using the `Inkeep.ChatButton()` function.

    ```ts
    const config: InkeepChatButtonProps = {
      aiChatSettings: {
        agentUrl: "https://your-api.example.com/run/api/chat",
        apiKey: process.env.INKEEP_API_KEY, // Your API key
      },
    };

    const chatButton = Inkeep.ChatButton(config);
    ```
  </Step>
</Steps>

## Config

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
