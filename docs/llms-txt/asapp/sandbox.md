# Source: https://docs.asapp.com/ai-productivity/ai-summary/sandbox.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Summary Sandbox

> Learn how to use the AI Summary Sandbox to test and validate summary generation.

The AI Summary Sandbox is a testing environment accessible through AI-Console that allows administrators and developers to:

* Generate and visualize free-text summaries and structured data
* Test summary generation on voice and messaging conversations
* Validate summary outputs before deploying to production
* Simulate conversations or upload existing transcripts

<Frame caption="AI Summary Sandbox showing intent and free-text summary generation">
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1da7132fb6e4cc5554f36713e58568ad" data-og-width="1981" width="1981" data-og-height="1228" height="1228" data-path="image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=58a35811cfcfc090b61047b40c271503 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e684a55299b1e94cb1e460a75191663a 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=41a024c1c5d2221d5539c5e8c95812de 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4f7049f353d2b1c7e867357ebbb259ed 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d250493f08959f8ad9d7729119ef6462 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d3616c89dac9fc080f5808be3387f17c 2500w" />
</Frame>

## Creating Test Conversations

The AI Summary Sandbox supports two methods for testing summary generation:

**Simulate Conversations**

* Create new conversations by switching between customer and agent roles
* Test voice conversations using real-time transcription via AI Transcribe
* Validate summary generation on different conversation types and scenarios

**Upload Transcripts**

* Load existing conversation transcripts
* Test summary generation on historical conversations
* Validate model performance on real customer interactions

## Available Summary Types

The Sandbox generates summaries based on your environment's configuration:

| Type              | Description                                               | Availability                                                   |
| :---------------- | :-------------------------------------------------------- | :------------------------------------------------------------- |
| Free Text Summary | Concise narrative summary of the conversation             | Always available                                               |
| Intent            | Topic-level categorization of customer's primary issue    | Available after custom model training                          |
| Structured Data   | Extracted data points and answers to predefined questions | Available after customizing your structured data configuration |

<Note>
  You must configure intent and structured data capabilities for your specific business needs. Contact your ASAPP account team to enable these features.
</Note>

## Using the Sandbox

Depending on the type of conversation you want to test, you can use one of the following methods:

<Tabs>
  <Tab title="Voice Conversations">
    When testing voice conversations in the Sandbox:

    * AI Transcribe powers real-time transcription
    * If no custom AI Transcribe model exists, the system uses a baseline contact center model
    * The system generates transcripts in real-time as you speak
  </Tab>

  <Tab title="Messaging Conversations">
    For messaging conversations, you can:

    * Switch between customer and agent roles to simulate a chat
    * Type messages directly in the interface
    * Upload existing chat transcripts
  </Tab>
</Tabs>

### Generating Summaries

1. Create or upload a conversation using one of the methods above
2. Click "Generate Summary" to process the conversation
3. View the generated free-text summary and any enabled structured data
4. Use the conversation ID to retrieve summaries via API if needed
