# Source: https://docs.asapp.com/generativeagent/configuring/conversations.md

# Review Conversations

> Review and analyze GenerativeAgent conversations to improve performance.

<Note>
  **”Conversations”**, formerly known as Conversation Explorer, is now fully integrated into the AI-Console to provide a centralized platform for viewing, monitoring, and managing conversations. This integration also enables faster navigation, improved usability, and streamlines access control and permission management.
</Note>

As you add use cases and refine GenerativeAgent's configuration, you can review and fine-tune how the GenerativeAgent handles real customer interactions.

For each conversation, you can see the full model actions GenerativeAgent took which includes its input, knowledge, reasoning, actions, and output back to the customer.

You can also see conversations that have been flagged as having [quality issues](#quality-issues).

## Before you Begin

Before reviewing conversations, you need to:

* **Get Access to "Conversations"** - Request access to "Conversations" from your admin. Once granted, you can access the "Conversations" section in the AI-Console.

## Review Conversations

To get started reviewing Conversations:

<Steps>
  <Step title="Access Conversations">
    Once you have access to Conversations:

    1. Sign in to the AI-Console.
    2. From the AI-Console landing page, navigate to the "GenerativeAgent" section in the left-hand menu.
    3. On the left-hand panel, navigate to Conversations.

       <Frame>
           <img src="https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/Conversations.png?fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=79f544866fcdc6328b6030378e058b41" alt="Conversations" data-og-width="1937" width="1937" data-og-height="1245" height="1245" data-path="images/generativeagent/reporting/Conversations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/Conversations.png?w=280&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=45a47cb55ee7be6d98e20d61d0b34001 280w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/Conversations.png?w=560&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=5d79d026702e571cda8855ac24d28e4d 560w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/Conversations.png?w=840&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=7d36edc08d1ce09b3efae39eac4b2f31 840w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/Conversations.png?w=1100&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=0bcf6db55294b2eaab3327071db5e158 1100w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/Conversations.png?w=1650&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=55fc14ee84a66cf289327e66cfc6e997 1650w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/Conversations.png?w=2500&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=04a694175912bab76ed4904e7d28643b 2500w" />
       </Frame>
  </Step>

  <Step title="Find a conversation">
    Use the search and filter interface to locate specific interactions or patterns:

    * Use date filters to narrow your search
    * Search by conversation ID, customer name, or keywords
    * Filter by specific tasks, functions, or model actions

    <Frame>
            <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-search.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=b2c54597db0c9597772ca0d9eeab733e" alt="Search functionality" data-og-width="609" width="609" data-og-height="299" height="299" data-path="images/generativeagent/reporting/ce-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-search.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=2556437e018754a0af0cc20a91e6c25a 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-search.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=38e933130e692186252567edefee8959 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-search.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=77268ab5cc01db1347f3edcaff6b1ce3 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-search.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=b855d3e2795562f8de3b0c6900633dff 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-search.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=dc14b76dc8f1cc684920f6333c7fb116 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-search.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=851d76a81134e0b7da7905130b567d80 2500w" />
    </Frame>
  </Step>

  <Step title="Review the interaction">
    Once you have found a conversation, you can see exactly how GenerativeAgent makes decisions:

    * Enable model actions to see GenerativeAgent's reasoning
    * Click on model actions for detailed function responses
    * Check the quality tab for flagged interactions

    <Frame>
            <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3e359cfcd11497358dad885d179b21d1" alt="Model actions in conversation" data-og-width="1178" width="1178" data-og-height="730" height="730" data-path="images/generativeagent/reporting/ce-model-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=7dcff704a3cfe2298eea1520e6307311 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=5cb541ecda2a6af06ab418b541706b4b 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=0dc5a7ed16e5db9f2b74c73ccfc83710 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=bdf33f4c2f33fb5585ab62e1d9371ead 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=94695b464cf6c1456f6daf31ef99d075 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=4c90a9c27defd320978632559687e8b6 2500w" />
    </Frame>
  </Step>
</Steps>

<Note>
  Your admin must grant "Conversations" permissions before you can access the interface.
</Note>

## Find conversations

You can use the search and filter interface to locate specific Conversations or patterns.

### Search and filter options

Use the search bar to find conversations containing specific words or phrases. Enclose terms in quotes for exact matches.

<Frame>
    <img src="https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-filters.png?fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=5d685f7c9b1c54a5b6181b482d798862" alt="Filter options" data-og-width="540" width="540" data-og-height="204" height="204" data-path="images/generativeagent/reporting/ce-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-filters.png?w=280&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=c1cf68dda4f8adf85e9a79aea2ef0f08 280w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-filters.png?w=560&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=3c27d9f7a00463105142e18f3d12fc8e 560w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-filters.png?w=840&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=baa9e866224c46b3467c7c56939319c5 840w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-filters.png?w=1100&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=07007e4b39a49e06c5efc74dec957022 1100w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-filters.png?w=1650&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=fabb16e78b997555c0600bd1a86cb947 1650w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-filters.png?w=2500&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=2f5bbdedfb4a703a5120f4d98df161e8 2500w" />
</Frame>

* **Date range**: Select specific time periods
* **Task**: Find conversations where specific tasks were performed
* **Functions**: Locate conversations that called particular APIs
* **Conversation ID**: Search for a specific conversation

### Filter for flagged conversations

To find [Quality Issues](#quality-issues):

1. Add the "GenerativeAgent Flags" filter
2. Review flagged interactions to understand quality alerts

<Frame>
    <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-flags-filter.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=a35cbde943efe15ff8d38394f91c43ad" alt="Flags filter" data-og-width="368" width="368" data-og-height="190" height="190" data-path="images/generativeagent/reporting/ce-flags-filter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-flags-filter.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8bd7167769fb905905ef466985210adc 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-flags-filter.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=1f3a7563c0da86060303852a57ee45f0 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-flags-filter.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=245990a540d59d6ef33b8470ad61cbe2 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-flags-filter.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=b8c3d7ecf9687878361ea07a862ea237 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-flags-filter.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=9117733baeae927f424c1b3529c93ae5 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-flags-filter.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=ff55fe7f04e2d843b14e9aff0cdc72f5 2500w" />
</Frame>

### Share a conversation

You can share a conversation with others by clicking the "Copy Link" button when viewing a conversation.

<Frame>
    <img src="https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-copy-link.png?fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=fef67871a34ce5f3d92a4d44129445f9" alt="Copy link" data-og-width="1937" width="1937" data-og-height="1245" height="1245" data-path="images/generativeagent/reporting/ce-copy-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-copy-link.png?w=280&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=b44753197c922af8c9e97f1e750f73f3 280w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-copy-link.png?w=560&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=dc3d08bbff7f7d372c67521a0b8714ca 560w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-copy-link.png?w=840&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=a2e17818d72650d650eb5895c6d23806 840w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-copy-link.png?w=1100&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=d44c0f4cb18773ef4578e77fe9529aac 1100w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-copy-link.png?w=1650&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=302c7ef1e033fd5a2a0383d1e2ba0946 1650w, https://mintcdn.com/asapp/4cd9rve7uZ_fQdjk/images/generativeagent/reporting/ce-copy-link.png?w=2500&fit=max&auto=format&n=4cd9rve7uZ_fQdjk&q=85&s=b154d7fb67e31d7160a3d4cd48a51c90 2500w" />
</Frame>

You can also share your current filtered view by copying the URL of your current page.

## Analyze Model Actions

Once you have found a conversation, you can see exactly how GenerativeAgent makes decisions by viewing its internal reasoning process via **model actions**.

Model actions are the input, knowledge, api calls, reasoning, and output of GenerativeAgent's model while handling the customer interaction.

The information in the model actions can drive how you update the configuration of your tasks and functions.

<Frame>
    <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3e359cfcd11497358dad885d179b21d1" alt="Model actions in conversation" data-og-width="1178" width="1178" data-og-height="730" height="730" data-path="images/generativeagent/reporting/ce-model-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=7dcff704a3cfe2298eea1520e6307311 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=5cb541ecda2a6af06ab418b541706b4b 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=0dc5a7ed16e5db9f2b74c73ccfc83710 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=bdf33f4c2f33fb5585ab62e1d9371ead 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=94695b464cf6c1456f6daf31ef99d075 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=4c90a9c27defd320978632559687e8b6 2500w" />
</Frame>

### Model actions categories

Model actions are categorized into the following:

<Note>
  When enabling a model action category, there may be multiple model actions with the same category that will be displayed. e.g. enabling Functions will show both a "Function Call" for the request and a "Function Response" for the response.
</Note>

<AccordionGroup>
  <Accordion title="Authentication">
    Actions occur when GenerativeAgent needs authentication data to call an API. Only used for API Connections that require [client data](/generativeagent/configuring/connect-apis/authentication-methods#client-authentication-data).
  </Accordion>

  <Accordion title="Confirmation requests">
    Actions occur when GenerativeAgent needs to confirm an action with the customer.
  </Accordion>

  <Accordion title="Functions">
    Actions that occur when GenerativeAgent calls a function to handle the customer interaction.

    The model actions will show:

    * The function name
    * Input parameters
    * Output

    Function calls may appear as multiple entries in the model action stream.

    You can also see the "Raw" JSON interaction between GenerativeAgent and the function.
  </Accordion>

  <Accordion title="Errors">
    Actions occur when GenerativeAgent encounters an error.
  </Accordion>

  <Accordion title="HILA">
    Actions occur when GenerativeAgent needs consultation from a human agent as part of [Human in the Loop](/generativeagent/human-in-the-loop).
  </Accordion>

  <Accordion title="Input variables">
    The [input variables](/generativeagent/configuring/tasks-and-functions/input-variables) that GenerativeAgent uses to call a function.
  </Accordion>

  <Accordion title="Knowledge">
    The Knowledgebase articles that GenerativeAgent was given to answer the customer's question.
  </Accordion>

  <Accordion title="Out-of-scope Customer Message">
    This occurs when GenerativeAgent determines that the customer's question is out of scope for the current task.
  </Accordion>

  <Accordion title="Tasks">
    The task that GenerativeAgent is entering or changing into in order to handle the customer interaction.
  </Accordion>

  <Accordion title="Thoughts">
    GenerativeAgent's internal thoughts and reasoning process.
  </Accordion>

  <Accordion title="Transfer to agent">
    This occurs when GenerativeAgent performs a [transfer to agent](/generativeagent/configuring/tasks-and-functions/system-transfer#transfer-to-agent) to escalate the conversation to a human agent.
  </Accordion>

  <Accordion title="Unsafe Customer Input">
    This occurs when GenerativeAgent determines that the customer's input is unsafe.
  </Accordion>
</AccordionGroup>

### Review model actions

When looking at a conversation, model actions are displayed inline with the conversation flow. This allows you to understand exactly when and why the AI made specific decisions during the interaction.

To review model actions:

1. Open a conversation
2. In the center panel, enable the model actions you want to review

   <Frame>
       <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions-filter.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=cb7cab45b0c530e58aba0f3a3e7e67e2" alt="Model actions filter" data-og-width="428" width="428" data-og-height="360" height="360" data-path="images/generativeagent/reporting/ce-model-actions-filter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions-filter.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=10e0fb0833c1943e8eba3139ae3e67bf 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions-filter.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8b8bf9943346694bceb4ceb0f92ddd26 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions-filter.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=e80ee1cd1156518af2c6bbb6f7fb8203 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions-filter.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8bdae9580a37b60a5fde9d8e8db7afc9 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions-filter.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=863d7aa68f0f16d756be9d523f1c782d 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-actions-filter.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=787351b7e08e923c324876d5b2ccaa04 2500w" />
   </Frame>
3. View the AI's reasoning process inline with the conversation, showing the chronological flow of decisions
4. Click any model action to see detailed information.

   This example shows a function response.

   <Frame>
       <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-action-details.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=f9c1d999e477d076b5a1ba5c2cf2466e" alt="Model action details" data-og-width="1008" width="1008" data-og-height="719" height="719" data-path="images/generativeagent/reporting/ce-model-action-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-action-details.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=0285dd954191ec182213147647b6f93b 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-action-details.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=11ed3ef4687f512aad1442b093deb636 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-action-details.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=06356f052e4d5f749fbc2895208cb244 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-action-details.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=33253a01aa2083daff2022dc5373b3f5 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-action-details.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=c2717e56f35007ca2a24dcd6aca0b068 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reporting/ce-model-action-details.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=a57e5e5b58ffa36aef1629ea5f49b246 2500w" />
   </Frame>

   You can also see the "Raw" JSON interaction between GenerativeAgent and the function.

## Quality issues

Our monitoring system can flag a conversation as having potential quality issues as determined by our quality evaluators. When quality issues are detected:

* **Inline indicators**: Flagged messages appear with visual indicators directly in the conversation flow
* **Quality tab**: The "Quality" tab provides detailed information about each flagged utterance.
* **Customizable flagging:** Define which messages should be flagged to match your team’s needs.

<Frame>
    <img src="https://mintcdn.com/asapp/aI_Mwk6owa9HxWdJ/images/generativeagent/Conversation_Monitoring.gif?s=671df6a10f968e24d1ad5d0748203350" alt="Quality tab" data-og-width="3328" width="3328" data-og-height="1840" height="1840" data-path="images/generativeagent/Conversation_Monitoring.gif" data-optimize="true" data-opv="3" />
</Frame>

<Accordion title="Quality Evaluators">
  Our monitoring system uses quality evaluators to flag conversations that may have quality issues. Work with your ASAPP Account team to understand the quality evaluators for your company.
</Accordion>

## Next steps

<CardGroup cols={2}>
  <Card title="Improve Tasks" href="/generativeagent/configuring/tasks-and-functions/improving">
    Refine tasks, functions, and knowledge base based on your analysis.
  </Card>

  <Card title="Previewer" href="/generativeagent/configuring/previewer">
    Live test your configuration within the dashboard using the Previewer.
  </Card>

  <Card title="Troubleshooting" href="/generativeagent/configuring/safety-and-troubleshooting">
    Fix problems identified through conversation review.
  </Card>
</CardGroup>
