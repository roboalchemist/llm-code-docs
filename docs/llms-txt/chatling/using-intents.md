# Source: https://docs.chatling.ai/chatbot/intents/using-intents.md

# Using intents

> Learn how to use intents to create more complex chatbot flows

To make your intents work, there are two essential steps:

1. Enable intent matching in blocks to tell the chatbot which intents to look for in user messages.
2. Define the flow of the chatbot when an intent is matched.

## 1. Intent matching

Currently, intent matching can be enabled in [Text input blocks](/chatbot/builder/blocks/inputs/text).

When users send messages using the Text block, you can configure whether these messages should be checked against one or more defined intents. This allows you to control when intent matching occurs and trigger appropriate flows based on the matches.

### Enabling intent matching

1. Open the editor for a text block.
2. Next to the `Match intent` option, click the `+` button.

<img src="https://chatling-assets.b-cdn.net/match_intent_block_option.jpg" alt="Match intent option" width="400" />

3. Select the intents you want user messages to be checked against.

<img src="https://chatling-assets.b-cdn.net/add-intents-to-intent-matcher-block-option.jpg" alt="Select intents for intent matcher" width="400" />

When a user sends a message, the chatbot will check if the message matches any of the selected intents and trigger the appropriate flow. If there are no matches, the flow will continue normally.

## 2. Defining intent flows

There are two ways to define the actions for an intent:

1. Intent trigger block (global)
2. Local trigger

### Intent trigger block

Intent triggers are flows that will be executed when an intent is matched. These triggers are global, meaning that they will be executed by any block that matches the intent. This is useful if you want to create a standard response for an intent that can be used in multiple places in your chatbot.

For example, if you create an Intent trigger for `Order Tracking`:

* Any block that matches this intent will start this flow.
* The same flow runs whether matched in a welcome message or support conversation.
* Flow can include actions like fetching order status, asking for order number, etc.

This provides a consistent response when users ask about order tracking anywhere in your chatbot.

**To add the trigger:**

1. Open `Blocks` from the sidebar.

<img src="https://chatling-assets.b-cdn.net/open-blocks-menu-builder-sidebar.jpg" alt="Open Blocks menu" width="400" />

2. Under the `Triggers` section, drag and drop the `Intent` block onto the canvas.

<img src="https://chatling-assets.b-cdn.net/intent-trigger-block-sidebar.jpg" alt="Drag and drop Intent trigger" width="400" />

3. Click on the block to open the editor.

4. Select an intent this trigger belongs to.

<img src="https://chatling-assets.b-cdn.net/select-intent-in-intent-trigger.jpg" alt="Select intent for trigger" width="600" />

5. Define the flow to run when the intent is triggered.

<img src="https://chatling-assets.b-cdn.net/intent-trigger-sales-sample-flow.jpg" alt="Define flow for intent trigger" width="450" />

### Local trigger

Sometimes you want different flows for the same intent depending on where in the conversation it was matched. This is where local triggers come in.

* Open the block where you want to enable local trigger for an intent.
* Find the intent under the `Match intent` option and click the `Local trigger` icon as shown below. For example, we will enable local trigger for the `Order status` intent.

<img src="https://chatling-assets.b-cdn.net/local-trigger-order-status-intent.jpg" alt="Enable local trigger for intent" width="350" />

* Define the specific flow for this intent. For example, we will ask the user for their order number before fetching the order status. As such, whenever the input in this block matches the `Order status` intent, the flow defined here will be executed instead of the global trigger.

<img src="https://chatling-assets.b-cdn.net/order-status-local-flow-example.jpg" alt="Define flow for local trigger" width="500" />

Note that the local trigger takes precedence over the global trigger when enabled.

### Using both triggers

You can have both global and local triggers for intents:

* Use global triggers for standard responses
* Override with local triggers where context-specific flows are needed

This flexibility allows you to:

* Maintain consistent base responses
* Customize flows for specific conversation stages
* Create more dynamic user experiences

## What happens when no intents match?

If no intent is matched, the chatbot will continue with the flow as normal.
