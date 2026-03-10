# Source: https://docs.inkeep.com/talk-to-your-agents/javascript/custom-trigger

# Custom Trigger for JavaScript (/talk-to-your-agents/javascript/custom-trigger)

Create custom UI elements to trigger Inkeep modals with complete control over appearance and behavior in JavaScript.



## Overview

Custom triggers give you complete control over how users open Inkeep modals in your JavaScript application. Instead of using pre-built widgets like `Inkeep.ChatButton()`, you can create your own UI elements that match your design system while maintaining full functionality.

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
    Insert the ModalChat widget by using the `Inkeep.ModalChat()` function.

    ```js
    const config = {
      baseSettings: {
        apiKey: "YOUR_API_KEY",
      },
      aiChatSettings: {
        aiAssistantName: "Keepie",
      },
      openSettings: {
        onOpenChange: handleOpenChange,
      },
    };

    // Initialize modal chat
    const modalChat = Inkeep.ModalChat(config);

    function handleOpenChange(newOpen) {
      modalChat.update({ openSettings: { isOpen: newOpen } });
    }

    // trigger
    document.querySelector("#chat-button").addEventListener("click", () => {
      modalChat.update({ openSettings: { isOpen: true } });
    });

    // Access chat methods
    modalChat.clearChat();
    ```
  </Step>
</Steps>

## Config

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
