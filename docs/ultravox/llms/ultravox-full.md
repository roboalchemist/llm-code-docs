# Ultravox Documentation

Source: https://docs.ultravox.ai/llms-full.txt

---

# Building & Editing Agents
Source: https://docs.ultravox.ai/agents/building-and-editing-agents

Create and manage reusable voice assistant templates for consistent experiences.

## Planning Your Agent

Before creating an agent, consider these key design decisions:

<Steps>
  <Step title="Define Purpose & Personality">
    What is your agent's role? Customer support, sales assistant, information provider? Define the personality, tone, and expertise level.
  </Step>

  <Step title="Identify Required Capabilities">
    What tools and integrations does your agent need? Knowledge base access, CRM integration, payment processing?
  </Step>

  <Step title="Plan Dynamic Content">
    What information changes between calls? Customer names, account details, product catalogs? These become template variables.
  </Step>

  <Step title="Choose Voice & Language">
    Select appropriate voice characteristics and language settings for your target audience.
  </Step>
</Steps>

## Creating Agents

<Tip>
  <b>Agent Quickstart</b>

  <br />

  Want to dive right in? Use our [Agent Quickstart](/gettingstarted/quickstart/agent-console) to build your first agent now.
</Tip>

<Note>
  The web app and API are fully compatible. Agents created in either can be managed through both interfaces.
</Note>

### Using the No-Code Web App

For teams preferring visual interfaces, Ultravox provides a [web-based agent builder](https://app.ultravox.ai/agents/new):

**When to Use the Web App:**

* Rapid prototyping and experimentation
* Non-technical team members need to create agents
* Visual configuration is preferred over code
* Quick testing of voice and personality combinations

**When to Use the API:**

* Production deployments, CI/CD integration, and version control
* Complex template variable schemas
* Advanced tool configurations

**Transitioning Between Approaches:**

* Start with the web app for rapid prototyping
* Export configurations to API calls for production
* Use the web app for quick edits, API for deployment

### Using the API

Create agents programmatically for full control and integration with your development workflow:

```js Example: Creating a New Customer Support Agent theme={null}
// Note: we are using a template variable for customerName
const createAgent = async () => {
  const response = await fetch('https://api.ultravox.ai/api/agents', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': 'your-api-key'
    },
    body: JSON.stringify({
      name: 'Customer Support Agent',
      callTemplate: {
        systemPrompt: "You are Anna, a friendly customer support agent for Acme Inc. You are talking to {{customerName}}. You should help them with their questions about our products and services. If you can't answer a question, offer to connect them with a human support agent.",
        voice: "Jessica",
        temperature: 0.4,
        recordingEnabled: true,
        firstSpeakerSettings: {
          agent: {
            text: "Hello! This is Anna from Acme customer support. How can I help you today?"
          }
        },
        selectedTools: [
          { toolName: 'knowledgebaseLookup' },
          { toolName: 'orderStatus' },
          { toolName: 'transferToHuman' }
        ]
      }
    })
  });
  
  return await response.json();
};
```

## Call Template Configuration

The call template is the heart of your agent, defining all behavior and capabilities:

### System Prompt

Design effective system prompts that define your agent's personality and knowledge. Here's an example prompt using various template variables that will be populated at call creation time using the [templateContext](/api-reference/agents/agents-calls-post#body-template-context) property:

```text Example: Defining an Agent System Prompt theme={null}
You are {{agentName}}, a {{role}} for {{companyName}}. 

Your personality: {{personality}}
Your expertise: {{expertise}}

Guidelines:
- Always be {{tone}} and professional
- If you don't know something, offer to transfer the call to a human agent using the 'transferToHuman' tool
- Keep responses concise but helpful
- Reference the customer as {{customerName}} when appropriate

Context about this conversation:
- Customer type: {{customerTier}}
- Previous interaction: {{lastInteraction}}
```

For more, see our [Prompting Guide →](/gettingstarted/prompting)

### Voice Configuration

Choose a voice that matches your brand and audience.

```js Example: Built-in vs. External Voice theme={null}
// Built-in Ultravox voice
voice: "Jessica"  // Professional, friendly

// External voice providers (requires API keys)
externalVoice: {
  elevenLabs: {
    voiceId: "your-elevenlabs-voice-id",
    model: "eleven_turbo_v2_5",
    speed: 1.0,
    stability: 0.8
  }
}
```

Learn more in the [Voices Overview →](/voices/overview)

### Tool Selection and Configuration

Connect your agent to external capabilities using tools:

```js Example: Defining Selected Tools theme={null}
selectedTools: [
  {
    toolName: 'knowledgebaseLookup',
    descriptionOverride: 'Search our product documentation and FAQ',
    parameterOverrides: {
      maxResults: 3
    }
  },
  {
    toolName: 'orderStatus',
    authTokens: {
      apiKey: 'your-order-system-key'
    }
  },
  {
    toolName: 'transferToHuman'
  }
]
```

Dig into more in the [Tools Overview →](/tools/overview)

## Agent Management

### Updating Agents

You can update the agent via the [Ultravox web app](https://app.ultravox.ai/agents) or via the [Update Agent](/api-reference/agents/agents-patch) API.

```js Example: Updating Agent via API theme={null}
const updateAgent = async (agentId) => {
  const response = await fetch(`https://api.ultravox.ai/api/agents/${agentId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': 'your-api-key'
    },
    body: JSON.stringify({
      callTemplate: {
        systemPrompt: "Updated system prompt...",
        temperature: 0.4  // Only fields you want to change
      }
    })
  });
  
  return await response.json();
};
```

<Warning>
  Agent changes only affect new calls. Active calls continue using the configuration they started with.
</Warning>

### Monitoring and Analytics

Track agent performance and usage:

```js Example: Getting Agent Stats & Calls theme={null}
// Get agent statistics
const getAgentStats = async (agentId) => {
  const response = await fetch(`https://api.ultravox.ai/api/agents/${agentId}`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  const agent = await response.json();
  console.log('Total calls:', agent.statistics.calls);
};

// Get recent calls for this agent
const getAgentCalls = async (agentId) => {
  const response = await fetch(`https://api.ultravox.ai/api/agents/${agentId}/calls`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};
```

## When to Use Advanced Features

**Start Simple:** Begin with mono prompts that handle your core use case in a single system prompt. This approach works well for:

* Straightforward customer support
* Information lookup
* Basic transaction flows

**Add Complexity When Needed:** If mono prompting isn't sufficient for your use case, gradually add:

* **Inline instructions** for multi-step processes → [Guiding Agents](/agents/guiding-agents)
* **Call stages** for completely different conversation phases → [Call Stages](/agents/call-stages)

**Don't Over-Engineer:** Resist the temptation to add complexity early. Most voice applications can be built successfully with simple agent configurations.

## Next Steps

<CardGroup>
  <Card title="Start Making Calls" icon="phone" href="/agents/making-calls">
    Use your agents to create conversations with users.
  </Card>

  <Card title="Advanced Conversation Control" icon="steering-wheel" href="/agents/guiding-agents">
    Learn how to use inline instructions for complex workflows.
  </Card>
</CardGroup>


# Call Management
Source: https://docs.ultravox.ai/agents/call-management

Retrieve call information, from active conversation monitoring to historical data analysis and cleanup.

## Monitoring Active Calls

Track ongoing conversations across your application:

```js theme={null}
// List all calls with filtering
const getActiveCalls = async () => {
  const response = await fetch('https://api.ultravox.ai/api/calls?pageSize=50', {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  const data = await response.json();
  
  // Filter for active calls (those that are joined but not ended)
  const activeCalls = data.results.filter(call => 
    call.joined && !call.ended
  );
  
  return activeCalls;
};

// Get calls with specific metadata
const getCallsBySource = async (source) => {
  const params = new URLSearchParams({
    'metadata.source': source,
    pageSize: 100
  });
  
  const response = await fetch(`https://api.ultravox.ai/api/calls?${params}`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};
```

## Advanced Filtering

Use query parameters to find specific calls:

```js theme={null}
// Filter by date range and duration
const getRecentLongCalls = async () => {
  const params = new URLSearchParams({
    fromDate: '2024-01-01',
    toDate: '2024-01-31',
    durationMin: '300s',  // 5 minutes or longer
    sort: '-created'      // Newest first
  });
  
  const response = await fetch(`https://api.ultravox.ai/api/calls?${params}`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};

// Search calls by content
const searchCalls = async (searchTerm) => {
  const params = new URLSearchParams({
    search: searchTerm,
    pageSize: 20
  });
  
  const response = await fetch(`https://api.ultravox.ai/api/calls?${params}`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};
```

## Retrieving Call Details

Get comprehensive information about specific calls:

```js theme={null}
// Get call details
const getCallDetails = async (callId) => {
  const response = await fetch(`https://api.ultravox.ai/api/calls/${callId}`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  const call = await response.json();
  
  console.log('Call Status:', call.ended ? 'Completed' : 'Active');
  console.log('Duration:', call.ended ? 
    calculateDuration(call.joined, call.ended) : 'Ongoing');
  console.log('End Reason:', call.endReason);
  
  return call;
};

// Get conversation messages
const getCallMessages = async (callId) => {
  const response = await fetch(`https://api.ultravox.ai/api/calls/${callId}/messages`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};

// Get call events and logs
const getCallEvents = async (callId) => {
  const response = await fetch(`https://api.ultravox.ai/api/calls/${callId}/events`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};
```

## Working with Call Stages

For calls using [Call Stages](/agents/call-stages), use stage-specific endpoints:

```js theme={null}
// Get all stages for a call
const getCallStages = async (callId) => {
  const response = await fetch(`https://api.ultravox.ai/api/calls/${callId}/stages`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};

// Get messages for a specific stage
const getStageMessages = async (callId, stageId) => {
  const response = await fetch(
    `https://api.ultravox.ai/api/calls/${callId}/stages/${stageId}/messages`,
    { headers: { 'X-API-Key': 'your-api-key' } }
  );
  
  return await response.json();
};
```

## Call Recordings

Retrieve audio recordings when recording is enabled:

```js theme={null}
// Get call recording
const getCallRecording = async (callId) => {
  const response = await fetch(`https://api.ultravox.ai/api/calls/${callId}/recording`, {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  if (response.ok) {
    const audioBlob = await response.blob();
    // Handle audio data (save to file, play, etc.)
    return audioBlob;
  } else {
    console.log('Recording not available');
    return null;
  }
};
```

## Call Deletion

Remove calls and all associated messages, recordings, and stages:

```js theme={null}
// Delete a specific call
const deleteCall = async (callId) => {
  const response = await fetch(`https://api.ultravox.ai/api/calls/${callId}`, {
    method: 'DELETE',
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return response.ok;
};
```

### List Deleted Calls

When calls are deleted, we retain basic metadata for record keeping:

```js theme={null}
// View deleted calls (tombstone records)
const getDeletedCalls = async () => {
  const response = await fetch('https://api.ultravox.ai/api/deleted_calls', {
    headers: { 'X-API-Key': 'your-api-key' }
  });
  
  return await response.json();
};
```


# Call Stages
Source: https://docs.ultravox.ai/agents/call-stages

Create dynamic, multi-stage conversations.

The Ultravox API's Call Stages functionality allows you to create dynamic, multi-stage conversations. Stages enable more complex and nuanced agent interactions, giving you fine-grained control over the conversation flow.

Each stage can have a new system prompt, a different set of tools, a new voice, an updated conversation history, and more.

<Note>
  <b>Advanced Feature</b>

  Call stages require planning and careful implementation and are likely not required for simple use cases. Make sure to read [Guiding Agents](/agents/guiding-agents) before jumping into the deep end of stages.
</Note>

## Understanding Call Stages

Call Stages ("Stages") provide a way to segment a conversation into distinct phases, each with its own system prompt and potentially different parameters. This enables interactions that can adapt and change focus as the conversation progresses.

Key points to understand about Stages:

**Dynamic System Prompts** → Stages allow you to give granular system prompts to the model as the conversation progresses.

**Flexibility** → You have full control to determine when and how you want the conversation to progress to the next stage.

**Thoughtful Design** → Implementing stages requires careful planning and consideration of the conversation structure. Consider how to handle stage transitions and test thoroughly to ensure a natural flow to the conversation.

**Maintain Context** → Think about how the agent will maintain context about the user between stages if you need to ensure a coherent conversation.

## Creating and Managing Stages

To implement Call Stages in your Ultravox application, follow these steps:

<Steps>
  <Step title="Plan Your Stages">
    Determine the different phases of your conversation and what prompts or parameters should change at each stage.
  </Step>

  <Step title="Implement a Stage Change Tool">
    Create a custom tool that will trigger stage changes when called. This tool should:

    * Respond with a `new-stage` response type. This creates the new stage. How you send the response depends on the tool type:
      * For server/HTTP tools, set the `X-Ultravox-Response-Type` header to `new-stage`.
      * For [client tools](/sdk-reference/introduction#client-tools), set `responseType="new-stage"` on your `ClientToolResult` object.
    * Provide the updated parameters (e.g., system prompt, tools, voice) for the new stage in the response body.

    Unless overridden, stages inherit all properties of the existing call. See [Stages Call Properties](#stages-call-properties) for the list of call properties that can be changed.
  </Step>

  <Step title="Configure Stage Transitions">
    * Prompt the agent to use the stage change tool at appropriate points in the conversation.
    * Ensure the stage change tool is part of `selectedTools` when creating the call as well as during new stages (if needed).
    * Update your system prompt as needed to instruct the agent on when/how to use the stage change tool.
  </Step>
</Steps>

<Warning>
  <b>Things to Remember</b>

  * New stages inherit all properties from the previous stage unless explicitly overridden.
  * Refer to [Stages Call Properties](#stages-call-properties) to understand which call properties can be changed as part of a new stage.
  * Test your stage transitions thoroughly to ensure the conversation flows naturally.
</Warning>

### Example Stage Change Implementation

Here's a basic example of how to implement a new call stage.

First, we create a tool that is responsible for changing stages:

```js theme={null}
function changeStage(requestBody) {
  const responseBody = {
    systemPrompt: "...", // new prompt
    ..., // other properties to change, like the voice
    // You may optionally also set toolResultText, which will be the content
    // of the tool result message in conversation history. The tool result
    // will be the most recent message the model sees during its next generation
    // unless you set initialMessages. Defaults to "OK".
    toolResultText: "(New Stage) Next, focus on..."
  };

  return {
    body: responseBody,
    headers: {
      'X-Ultravox-Response-Type': 'new-stage'
    }
  };
}
```

We also need to ensure that we have instructed our agent to use the tool and that we add the tool to our `selectedTools` during the creation of the call.

```js theme={null}
// Instruct the agent on how to use the stage management tool
// Add the tool to selectedTools
{
  systemPrompt: "You are a helpful assistant...you have access to a tool called changeStage...",
  ...
  selectedTools: [
    {
      "temporaryTool": {
        "modelToolName": "changeStage",
        "description": ...,
        "dynamicParameters": [...],
      }
    }
  ]
}
```

<Tip>
  <b>Inheritance</b>

  New stages inherit all properties from the previous stage.
  You can selectively overwrite properties as needed when defining a new stage.

  See [Stages Call Properties](#stages-call-properties) for more.
</Tip>

## Ultravox API Implications

If you are not using stages for a call, retrieving calls or call messages via the API (e.g. [`List Calls`](/api-reference/calls/calls-list)) works as expected.

However, if you are using call stages then you most likely want to use the stage-centric API endpoints to get stage-specific settings, messages, etc.

Use [`List Call Stages`](/api-reference/calls/calls-stages-list) to get all the stages for a given call.

| Ultravox API                                                     | Stage-Centric Equivalent                                                      |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [`Get Call`](/api-reference/calls/calls-get)                     | [`Get Call Stage`](/api-reference/calls/calls-stages-get)                     |
| [`List Call Messages`](/api-reference/calls/calls-messages-list) | [`List Call Stage Messages`](/api-reference/calls/calls-stages-messages-list) |
| [`List Call Tools`](/api-reference/calls/calls-tools-list)       | [`List Call Stage Tools`](/api-reference/calls/calls-stages-tools-list)       |

## Stages Call Properties

<Tip>
  The schema used for a Stages response body is a subset of the request body schema used when creating a new call. The response body must contain the new values for any properties you want to change in the new stage.
</Tip>

Unless overridden, stages inherit all properties of the existing call.

Here is the list of all call properties that can and cannot be changed during a new stage:

| property            | change with new stage? |
| ------------------- | ---------------------- |
| systemPrompt        | Yes                    |
| temperature         | Yes                    |
| voice               | Yes                    |
| languageHint        | Yes                    |
| initialMessages     | Yes                    |
| selectedTools       | Yes                    |
| firstSpeaker        | No                     |
| model               | No                     |
| joinTimeout         | No                     |
| maxDuration         | No                     |
| timeExceededMessage | No                     |
| inactivityMessages  | No                     |
| medium              | No                     |
| recordingEnabled    | No                     |

## Use Cases for Call Stages

Call Stages are particularly useful for complex conversational flows. Here are some example scenarios:

**Data Gathering** → Scenarios where the agent needs to collect a lot of data. Examples: job applications, medical intake forms, applying for a mortgage.

Here are potential stages for a **Mortgage Application**:

* Stage 1: Greeting and basic information gathering
* Stage 2: Financial assessment
* Stage 3: Property evaluation
* Stage 4: Presentation of loan options
* Stage 5: Hand-off to loan officer

**Switching Contexts** → Scenarios where the agent needs to navigate different contexts. Examples: customer support escalation, triaging IT issues.

Let's consider what the potential stages might be for **Customer Support**:

* Stage 1: Initial greeting and problem identification
* Stage 2: Troubleshooting
* Stage 3: Resolution or escalation (to another stage or to a human support agent)

## Conclusion

Call Stages in the Ultravox API give you the ability to create adaptive conversations for more complex scenarios like data gathering or switching contexts. By allowing granular control over system prompts and conversation parameters at different stages, you can create more dynamic and context-aware interactions.


# Guiding Agents
Source: https://docs.ultravox.ai/agents/guiding-agents

A guide to steering your agent toward good experiences

## Introduction to Inline Instructions

Inline instructions use tool responses and deferred messages to guide the agent at each step of the conversation. Rather than trying to frontload all instructions, you continuously remind the agent of what to do next.

This guide is intended to help you get better outcomes from an agent where mono prompting isn't cutting it. If you haven't tried a mono prompt approach yet, stop reading and go do that first. This guide is for you if:

* **Monoprompting Isn't Working** → You've tried mono prompting but things are not working. The agent won't complete necessary steps or follow more complex instructions.
* **You Have Clear Steps** → There are clear steps you want the agent to follow (e.g. asking the user 10 specific questions) and you can map to a state diagram.

<Note>
  <b>Building an IVR?</b>

  <br />

  If you are building an IVR or if your scenario includes non-overlapping stages, you may want to use [Call Stages](/agents/call-stages).
</Note>

## How Inline Instructions Work

<CodeGroup>
  ```text Overview theme={null}
  1. Start with a simple system prompt focused on the agent's
     general role and behavior.
  2. Use tools to provide step-specific instructions to the agent.
  3. The tool responses include guidance on what the agent should
     do next.
  4. Tool state maintains context between turns.
  5. Deferred messages allow inserting information without
     derailing the conversation flow.
  ```

  ```text Example: Insurance Claims Processing theme={null}
  An insurance claims agent that guides customers through the
  claims submission process. The agent uses a claims tool that
  maintains state about which documents have been collected,
  what information is still missing, and what step comes next.

  At each step, the tool response includes clear instructions
  on what to ask the customer next, helping the agent stay
  focused on the current step of the process rather than trying
  to hold the entire claims procedure in context.
  ```
</CodeGroup>

<Info>
  <b>Layer into Mono Prompt</b>

  <br />

  Inline instructions are layered into your mono prompt and provide the ability to guide the model.
</Info>

## Inline Instructions Building Blocks <Icon icon="cubes" />

The inline instructions approach leverages three key building blocks:

<CardGroup>
  <Card title="Deferred Messages" icon="cube" href="#deferred-messages">
    Inject instruction messages without triggering a response from the model.
  </Card>

  <Card title="Tool State" icon="cube" href="#tool-state">
    Pass additional context via tools to maintain state.
  </Card>

  <Card title="Tool Response Messages" icon="cube" href="#tool-response-messages">
    Instruct the agent what to do next via tool call responses.
  </Card>
</CardGroup>

### **Deferred Messages** <Icon icon="cube" />

Deferred messages allow you to inject a user message without causing the agent to generate a response immediately. These messages allow you to provide the model with guidance and direction and don't trigger an LLM generation. The messages are appended to the conversation history.

<Note>
  Brackets are not addable via voice, so these messages are only viable via text.
</Note>

**Using Deferred Messages**

Send a [UserTextMessage](/apps/datamessages#usertextmessage) and set `urgency` to `soon` or `later` depending on whether you want to wait for the next user input to start a generation.

```ts Example: Sending Message with Ultravox SDK theme={null}

session.sendText({
  text: "<instruction>Next, collect the user's mailing address</instruction>",
  deferResponse: true,
})
```

**Priming for Deferred Messages**
You should consider priming your agent for deferred messages in the system prompt.

```text Example: Priming via System Prompt theme={null}
You must always look for and follow instructions contained within
<instruction> tags. These instructions take precedence over other
directions and must be followed precisely.
```

### **Tool State** <Icon icon="cube" />

Tool state allows you to maintain state between tool calls, passing context from one tool call to the next. This is particularly useful for guiding the agent through a multi-step process.

<Note>
  <b>Tool State is Explicit</b>

  <br />

  Unlike dynamic parameters (i.e. populated by the model), tool state is explicit (i.e. the model doesn't interact with it). This allows for adding a bit more determinism.
</Note>

**Using Tool State**

You can provide initial tool state when you create the call by using [`initialState`](/api-reference/calls/calls-post#body-initial-state). This can be any JSON object you define.

Tools can then set the tool state as follows:

* **Client Tools** → Use the `updateCallState` value on a client tool results (works with WebSockets or Ultravox Client SDK).
* **Server Tools** → Set the `X-Ultravox-Update-Call-State` header which will be parsed as a JSON dict.

The tool state can be read via:

* **Automatic Parameter** → Use the [`KNOWN_PARAM_CALL_STATE`](/api-reference/tools/tools-post#response-definition-automatic-parameters-known-value) known value.
* **Tool Result Message** → Use the [`callState`](/api-reference/calls/calls-stages-messages-list#response-results-call-state) property.

The agent will not see the tool state directly. It allows you to pass information between tool calls and then use that information inside tools and to impact the responses from tool calls.

### **Tool Response Messages** <Icon icon="cube" />

Instead of having a tool call result send a 200 with "Successfully entered customer information", provide an instruction of what the agent should do next.

```js Example: Tool Response Message theme={null}
function createProfile(parameters) {
  const { ...profileData } = parameters;

  return {
    result: "Successfully recorded customer name. Next ask for their email",
    responseType: "tool-response",
    agentReaction: "speaks-once"
  }
};
```

## Pros of Inline Instructions

* **Focused guidance**: Instructions are context-specific and timely.
* **Dynamic adaptation**: Can respond to changing conversation flow.
* **Reduced cognitive load**: The agent only needs to understand the current step.
* **Maintainable complexity**: Can handle complex workflows without overwhelming the system prompt.
* **No latency spikes**: Avoids the performance hit of call stage transitions.

## Cons of Inline Instructions

* **Implementation complexity**: Requires more backend code to manage state.
* **Requires Tool Call**: Adding guidance requires the model to invoke a tool. If you forget to invoke the tool, you may never be able to provide further instructions.

## Ideal Use Cases

* **Multi-step processes**: Tasks with clear sequential steps like form filling or data collection.
* **Transaction flows**: E-commerce, booking systems, or other task-completion scenarios.
* **Customer support triage**: Guiding agents through problem diagnosis trees.
* **Interactive tutorials**: Step-by-step guidance through a learning process.

## Conclusion

Keeping your AI agent "on rails" is a balance between control and natural conversation. The right approach depends on your specific use case:

* **Mono Prompt**: Always start here. Graduate to using inline instructions if and when needed.
* **Inline Instructions**: For complex, multi-step processes requiring dynamic guidance.
* **Call Stages**: For conversations with fundamentally different phases (i.e. no overlap) requiring complete parameter changes.

As you develop your Ultravox application, start with the simplest approach that meets your needs, and gradually increase complexity as required. Remember that the most effective voice experiences feel natural while still accomplishing their goals reliably.

By leveraging building blocks like deferred messages, tool state, and targeted tool response messages, you can create sophisticated conversational flows that guide users through complex processes while maintaining the natural feel of human conversation.


# Making Calls
Source: https://docs.ultravox.ai/agents/making-calls

Start conversations using agents or direct call configuration.

## Creating Calls with Agents (Recommended)

For all new projects, use agents to create calls. This approach provides consistency, reusability, and easier maintenance.

### Basic Agent Call

Start a call using an existing agent and pass in any template variables:

```js Example: Create a New Agent Call theme={null}
const startAgentCall = async (agentId) => {
  const response = await fetch(`https://api.ultravox.ai/api/agents/${agentId}/calls`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': 'your-api-key'
    },
    body: JSON.stringify({
      templateContext: {
        customerName: "Jane Smith",
        accountType: "Premium"
      }
    })
  });
  
  return await response.json();
};
```

### Template Context and Variables

Provide dynamic data to your agent at call creation time:

```js Example: Template Context Variables theme={null}
{
  templateContext: {
    customerName: "John Doe",
    accountType: "enterprise",
    lastInteraction: "2025-05-15",
    accountBalance: "$1,250.00"
  }
}
```

### Overriding Agent Settings

When starting a call with an agent, you can override specific settings from the agent's call template. Here are the parameters you can include in the request body:

| Parameter              | Description                         | Type    | Example                      |
| ---------------------- | ----------------------------------- | ------- | ---------------------------- |
| `templateContext`      | Variables for template substitution | Object  | `{ customerName: "John" }`   |
| `initialMessages`      | Conversation history to start from  | Array   | Previous chat context        |
| `metadata`             | Key-value pairs for tracking        | Object  | `{ source: "website" }`      |
| `medium`               | Communication protocol              | Object  | `{ twilio: {} }`.            |
| `joinTimeout`          | Time limit for user to join         | String  | `"60s"`                      |
| `maxDuration`          | Maximum call length                 | String  | `"1800s"`                    |
| `recordingEnabled`.    | Whether to record audio             | Boolean | `true` / `false`             |
| `initialOutputMedium`  | Start with voice or text            | String  | `"voice"` / `"text"`         |
| `firstSpeakerSettings` | Initial conversation behavior       | Object  | `{ agent: { text: "..." } }` |
| `experimentalSettings` | Experimental settings for the call  | Object  | Varies                       |

Example of overriding agent settings when creating a call:

```js Example: Overriding Agent Settings theme={null}
const response = await fetch(`https://api.ultravox.ai/api/agents/${agentId}/calls`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'your-api-key'
  },
  body: JSON.stringify({
    // Template context
    templateContext: {
      customerName: "VIP Customer",
      accountType: "enterprise"
    },
    
    // Override agent settings for this specific call
    maxDuration: "900s", // 15 minutes instead of default
    recordingEnabled: false  // Disable call recording
  })
});
```

## Direct Call Alternative

For legacy integration, testing, or very simple use cases, you can create calls directly without agents:

```js theme={null}
const startDirectCall = async () => {
  const response = await fetch('https://api.ultravox.ai/api/calls', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': 'your-api-key'
    },
    body: JSON.stringify({
      systemPrompt: "You are a helpful customer service agent. Be friendly and professional.",
      voice: "Jessica",
      temperature: 0.3,
      model: "ultravox-v0.7",
      joinTimeout: "30s",
      maxDuration: "3600s",
      recordingEnabled: false,
      
      firstSpeakerSettings: {
        agent: {
          text: "Hello! How can I help you today?"
        }
      },
      
      selectedTools: [
        { toolName: 'knowledgebaseLookup' },
        { toolName: 'transferToHuman' }
      ],
      
      metadata: {
        purpose: "customer_support",
        test: "true"
      }
    })
  });
  
  return await response.json();
};
```

### Prior Call Inheritance

You can reuse the same properties (including message history) from a prior call by passing in a query param:

```js Example: Using Prior Call ID theme={null}
const continueFromPriorCall = async (priorCallId) => {
  const response = await fetch(`https://api.ultravox.ai/api/calls?priorCallId=${priorCallId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': 'your-api-key'
    },
    body: JSON.stringify({
      // Only override what you need to change
      systemPrompt: "Continue the previous conversation with updated context...",
      metadata: {
        continuation: "true",
        originalCall: priorCallId
      }
    })
  });
  
  return await response.json();
};
```

<Note>
  When using `priorCallId`, the new call inherits all properties from the prior call unless explicitly overridden. The prior call's message history becomes the new call's `initialMessages`.
</Note>

## Next Steps

<CardGroup>
  <Card title="Scaling & Concurrency" icon="wave-pulse" href="/gettingstarted/concurrency">
    Learn how call concurrency works and how to manage it.
  </Card>

  <Card title="Webhooks" icon="webhook" href="/webhooks/overview">
    Learn how to integrate and monitor real-time events.
  </Card>

  <Card title="Test & Debug Your Calls" icon="bug-slash" href="/agents/testing-and-debugging">
    Learn to monitor, troubleshoot, and optimize your voice conversations
  </Card>
</CardGroup>


# Overview: Agents & Calls
Source: https://docs.ultravox.ai/agents/overview

Create consistent, reusable voice AI experience with agents or direct call configuration.

## Introduction

Ultravox provides two ways to create voice conversations: **Agents** (recommended) and **Direct Calls**. For all new projects, we strongly recommend starting with agents as they provide better consistency, reusability, and maintainability.

## Agents vs Direct Calls

<CardGroup>
  <Card title="Agents (Recommended)" icon="robot">
    <br />

    **Reusable templates** that define assistant behavior, personality, and capabilities. Create once, use for multiple calls.

    <br />

    **Best for:** Production applications, consistent experiences, team collaboration.
  </Card>

  <Card title="Direct Calls" icon="phone">
    <br />

    **One-time configurations** where you specify all settings for each individual call.

    <br />

    **Best for:** Quick testing, very simple one-off use cases.
  </Card>
</CardGroup>

## Why Start with Agents?

[Agents](/api-reference/agents/agents-post) provide a way to define voice assistants that can be reused across multiple calls, ensuring consistent behavior and capabilities. This enables you to maintain a cohesive user experience with minimal configuration overhead at call creation time. Each agent includes a call template that defines system prompts, voice settings, available tools, and more.

Key benefits of using Agents:

**Reusable Configuration** → Create a single agent definition and use it for multiple calls without repeating configuration settings.

**Consistent Experience** → Ensure your voice experience maintains the same personality, capabilities, and behavior across all interactions.

**Version Control** → Update an agent's configuration in one place and have changes apply to all future calls.

**Simplified Deployment** → Reduce the complexity of starting calls by referencing an existing agent instead of providing all configuration details.

<Note>
  <b>Time-Saving Feature</b>

  Agents are ideal for production applications where you want consistent behavior across multiple user interactions.
</Note>

## Next Steps

<CardGroup>
  <Card title="Build Your First Agent" icon="hammer" href="/agents/building-and-editing-agents">
    Create reusable voice assistant templates
  </Card>

  <Card title="Start Making Calls" icon="phone" href="/agents/making-calls">
    Use agents or direct calls to create conversations
  </Card>

  <Card title="Advanced Techniques" icon="graduation-cap" href="/agents/guiding-agents">
    Learn sophisticated conversation control
  </Card>
</CardGroup>


# Testing & Debugging
Source: https://docs.ultravox.ai/agents/testing-and-debugging

Monitor, troubleshoot, and optimize your voice conversations for production quality.

\[Under Construction]


# Get Account
Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-get

get /api/accounts/me
Returns account details for a single account



# Set Telephony Credentials
Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-telephony-config-partial-update

patch /api/accounts/me/telephony_config
Allows adding or updating telephony provider credentials to an account



# Get Telephony Credentials
Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-telephony-config-retrieve

get /api/accounts/me/telephony_config
Returns the telephony credentials associated with the active account



# Set TTS API keys
Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-tts-api-keys-partial-update

patch /api/accounts/me/tts_api_keys
Allows adding or updating TTS provider API keys to an account, enabling ExternalVoices

This is not necessary for using the service's included voices or your own voice clones added to the service.


# Get Account TTS API Keys
Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-tts-api-keys-retrieve

get /api/accounts/me/tts_api_keys
Returns the TTS provider API keys associated with the active account

Only key prefixes are included and only for providers for which a key has been added.


# Get Call Usage
Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-usage-calls-get

get /api/accounts/me/usage/calls
Returns aggregated and per-day call usage data



# List Agent Calls
Source: https://docs.ultravox.ai/api-reference/agents/agents-calls-list

get /api/agents/{agent_id}/calls
Lists all calls that were created using the specified agent



# Create Agent Call
Source: https://docs.ultravox.ai/api-reference/agents/agents-calls-post

post /api/agents/{agent_id}/calls
Creates a new call using the the specified agent



# Delete Agent
Source: https://docs.ultravox.ai/api-reference/agents/agents-delete

delete /api/agents/{agent_id}
Deletes the specified agent



# Get Agent
Source: https://docs.ultravox.ai/api-reference/agents/agents-get

get /api/agents/{agent_id}
Gets details for the specified agent



# List Agents
Source: https://docs.ultravox.ai/api-reference/agents/agents-list

get /api/agents
Returns details for all agents



# Update Agent
Source: https://docs.ultravox.ai/api-reference/agents/agents-patch

patch /api/agents/{agent_id}
Updates the specified agent

Allows partial modifications to the agent.


# Create Agent
Source: https://docs.ultravox.ai/api-reference/agents/agents-post

post /api/agents
Creates a new agent using the specified name and call template



# List Scheduled Call Batch Created Calls
Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-created-calls-list

get /api/agents/{agent_id}/scheduled_batches/{batch_id}/created_calls
Returns details for all created calls in a scheduled call batch



# Delete Scheduled Call Batch
Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-delete

delete /api/agents/{agent_id}/scheduled_batches/{batch_id}
Deletes a scheduled call batch



# Get Scheduled Call Batch
Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-get

get /api/agents/{agent_id}/scheduled_batches/{batch_id}
Returns details for a scheduled call batch



# List Scheduled Call Batches
Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-list

get /api/agents/{agent_id}/scheduled_batches
Returns details for all an agent's scheduled call batches



# Update Scheduled Call Batch
Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-patch

patch /api/agents/{agent_id}/scheduled_batches/{batch_id}
Updates a scheduled call batch

Allows partial modifications to the scheduled call batch.


# Create Scheduled Call Batch
Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-post

post /api/agents/{agent_id}/scheduled_batches
Creates a new scheduled call batch using the the specified agent



# List Scheduled Call Batch Scheduled Calls
Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-scheduled-calls-list

get /api/agents/{agent_id}/scheduled_batches/{batch_id}/scheduled_calls
Returns details for all scheduled calls in a scheduled call batch



# Delete Call
Source: https://docs.ultravox.ai/api-reference/calls/calls-delete

delete /api/calls/{call_id}
Deletes the specified call

Also deletes all associated messages, recordings, and stages.


# Get Deleted Call
Source: https://docs.ultravox.ai/api-reference/calls/calls-deleted-calls-get

get /api/deleted_calls/{call_id}
Gets details for the specified deleted call



# List Deleted Calls
Source: https://docs.ultravox.ai/api-reference/calls/calls-deleted-calls-list

get /api/deleted_calls
Returns details for all deleted calls



# List Call Events
Source: https://docs.ultravox.ai/api-reference/calls/calls-events-list

get /api/calls/{call_id}/events
Returns any events logged during the call



# Get Call
Source: https://docs.ultravox.ai/api-reference/calls/calls-get

get /api/calls/{call_id}
Gets details for the specified call



# List Calls
Source: https://docs.ultravox.ai/api-reference/calls/calls-list

get /api/calls
Returns details for all calls



# List Call Messages
Source: https://docs.ultravox.ai/api-reference/calls/calls-messages-list

get /api/calls/{call_id}/messages
Returns all messages generated during the given call



# Create Call
Source: https://docs.ultravox.ai/api-reference/calls/calls-post

post /api/calls
Creates a new call using the specified system prompt and other properties



# Get Call Recording
Source: https://docs.ultravox.ai/api-reference/calls/calls-recording-get

get /api/calls/{call_id}/recording
Returns a link to the recording of the call



# Send Data Message to Call
Source: https://docs.ultravox.ai/api-reference/calls/calls-send-data-message-post

post /api/calls/{call_id}/send_data_message
Sends a data message to a live call

The request body for this API is determined by the type of message being sent. See [Data Messages](/apps/datamessages) for details.


# Get Sip Logs for a call
Source: https://docs.ultravox.ai/api-reference/calls/calls-sip-logs-get

get /api/calls/{call_id}/sip_logs
Redirects to the SIP logs for a call, if available. This is only available for calls with sip medium and only after the call has ended.



# Get Call Stage
Source: https://docs.ultravox.ai/api-reference/calls/calls-stages-get

get /api/calls/{call_id}/stages/{call_stage_id}
Retrieves details for a specific stage of a call



# List Call Stages
Source: https://docs.ultravox.ai/api-reference/calls/calls-stages-list

get /api/calls/{call_id}/stages
Lists all stages that occurred during the specified call

Stages represent distinct segments of the conversation where different parameters (e.g. system prompt or tools) may have been used.


# Get Call Stage Message Audio
Source: https://docs.ultravox.ai/api-reference/calls/calls-stages-message-audio-get

get /api/calls/{call_id}/stages/{call_stage_id}/messages/{call_stage_message_index}/audio
Gets the audio for the specified message



# List Call Stage Messages
Source: https://docs.ultravox.ai/api-reference/calls/calls-stages-messages-list

get /api/calls/{call_id}/stages/{call_stage_id}/messages
Returns all messages that were exchanged during a specific stage of a call



# List Call Stage Tools
Source: https://docs.ultravox.ai/api-reference/calls/calls-stages-tools-list

get /api/calls/{call_id}/stages/{call_stage_id}/tools
Returns all tools that were available during a specific stage of a call



# List Call Tools
Source: https://docs.ultravox.ai/api-reference/calls/calls-tools-list

get /api/calls/{call_id}/tools
Returns all tools that were available at any point during the call



# Calls Overview
Source: https://docs.ultravox.ai/api-reference/calls/overview

Understanding Calls in Ultravox

This section of the API reference covers the APIs for managing voice calls. The APIs provide methods to create and manage calls, retrieve recordings, handle user inactivity, and access conversation history through stages and messages. The system supports features like call recording, language hints, and maximum duration limits to help manage the conversation flow.

**Calls** → At the core are Calls, which represent complete conversations between users and AI agents, configured with parameters like system prompts, voice settings, and language preferences.

**Stages** → Calls can be broken down into Stages, which represent distinct segments of conversation where different parameters (like prompts or tools) may be used.

**Messages** → Within each stage, Messages capture the back-and-forth dialogue between users and agents.

## More Info

This section contains additional details for some properties.

### inactivityMessages

Inactivity messages  allow your agent to gracefully handle periods of user silence and end the call after a period of user inactivity. This feature helps maintain engagement and ensures calls don't remain open indefinitely when users have disconnected or finished their interaction.

* **Messages are Ordered** → Messages are delivered by the agent in the order provided.
* **Message Durations are Cumulative** → The first message is delivered when the user has been inactive for its duration. Each subsequent message m is delivered its duration after message m-1 (provided the user remains inactive).
* **User Interactions Reset** → Any activity from the user will reset the message sequence.
* **Different Behaviors** → Messages can have different end behaviors and can terminate the call.

<b>Best Practices</b>

* Keep messages concise and natural-sounding.
* Start with friendly check-in messages before moving to call termination.
* Provide clear context in messages if the call will be terminated.

<b>Message Format</b>

When creating a new call, `inactivityMessages` are an array of message objects.

<ResponseField name="message" type="Message Object">
  <Expandable title="properties">
    <ResponseField name="duration" type="string">
      The duration (in seconds) after which the message should be spoken.

      Pattern: `^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$`

      Examples: "60s", "5.5s"
    </ResponseField>

    <ResponseField name="message" type="string">
      The message to speak.

      Examples: "Are you still there?", "If there's nothing else, I will end the call now."
    </ResponseField>

    <ResponseField name="endBehavior" type="string">
      The behavior to exhibit when the message is finished being spoken. Must be one of the enumerated values.

      Possible values:

      `END_BEHAVIOR_UNSPECIFIED` - Default. The system will continue to wait for user input.

      `END_BEHAVIOR_HANG_UP_SOFT` - Will end the call unless the user interacts while the agent is delivering the message.

      `END_BEHAVIOR_HANG_UP_STRICT` - Will end the call after speaking the message, regardless of whether the user interrupts.
    </ResponseField>
  </Expandable>
</ResponseField>

#### Example: Adding Inactivity Messages

Let's look at how we could add inactivity messages to a call.

```js Example: Adding Inactivity Messages theme={null}
{
  "systemPrompt": "You are a helpful assistant.",
  "inactivityMessages": [
    {
      "duration": "30s",
      "message": "Are you still there?"
    },
    {
      "duration": "15s",
      "message": "If there's nothing else, may I end the call?"
    },
    {
      "duration": "10s",
      "message": "Thank you for calling. Have a great day. Goodbye.",
      "endBehavior": "END_BEHAVIOR_HANG_UP_SOFT"
    }
  ]
}
```

<Steps>
  <Step title="Call Starts">Using the `inactivityMessages` above, the call is created and joined.</Step>

  <Step title="User Stops Interacting - First Message">
    After 30 seconds of no user interaction, agent says "Are you still there?".

    If user interacts, call continues.
  </Step>

  <Step title="Inactivity Continues - Second Message">If no user interaction occurs for another 15 seconds, agent says "If there's nothing else, may I end the call?".</Step>
  <Step title="Inactivity Continues - Call Ends">If no user interaction occurs for another 10 seconds, agent says the provided message and the call ends unless the agent is interrupted during this final message.</Step>
</Steps>

### initialMessages

When creating a new call or a new call stage, you can provide messages to the agent via `initialMessages`. By default, new calls don't have initial messages and call stages inherit the prior stage's messages. New calls will inherit messages if `priorCallId` is set.

These messages can serve the purpose of giving the agent call history or to give examples for few-shotting (e.g. if you want the agent to learn how to respond in a specific way to user input).

#### Message Format

`initialMessages` must be an array of message objects where each message contains a `role` and `text`.

See "Response" under [List Call Messages](/api-reference/calls/calls-messages-list) for more details.

```js Example: Providing Initial Messages theme={null}
{
  "systemPrompt": "You are a helpful assistant.",
  "initialMessages": [
    {
      "role": "MESSAGE_ROLE_USER",
      "text": "My name is Steve"
    },
    {
      "role": "MESSAGE_ROLE_AGENT",
      "text": "Great to meet you, Steve! How can I help?"
    },
  ]
}
```

### Deleting Calls

If you don't want call details (e.g. recordings, messages/transcripts) to remain in the system, you can use the [Delete Call](/api-reference/calls/calls-delete) API.

When you delete a call, Ultravox deletes the call and all associated messages/transcripts, recordings, and stages. The system also creates a new entry for each deleted call and only keeps the high-level metadata necessary for billing purposes.

To view deleted calls you can use either the [Get Deleted Call](/api-reference/calls/calls-deleted-calls-get) or the [List Deleted Calls](/api-reference/calls/calls-deleted-calls-list) endpoints.


# Delete Corpus
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-delete

delete /api/corpora/{corpus_id}
Deletes the specified corpus

Also deletes all associated corpus sources.


# Get Corpus
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-get

get /api/corpora/{corpus_id}
Gets details for the specified corpus



# List Corpora
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-list

get /api/corpora
Returns details for all corpora



# Update Corpus
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-patch

patch /api/corpora/{corpus_id}
Updates the specified corpus

Allows partial modifications to the corpus.


# Create Corpus
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-post

post /api/corpora
Creates a new corpus using the specified name and description



# Delete Corpus Source
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-delete

delete /api/corpora/{corpus_id}/sources/{source_id}
Deletes the specified source



# Get Corpus Source Document
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-documents-get

get /api/corpora/{corpus_id}/sources/{source_id}/documents/{document_id}
Retrieves details for the specified source document



# List Corpus Source Documents
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-documents-list

get /api/corpora/{corpus_id}/sources/{source_id}/documents
Returns details for all documents contained in the source



# Get Corpus Source
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-get

get /api/corpora/{corpus_id}/sources/{source_id}
Retrieves details for the specified source



# List Corpus Sources
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-list

get /api/corpora/{corpus_id}/sources
Lists all sources that are part of the specified corpus



# Update Corpus Source
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-patch

patch /api/corpora/{corpus_id}/sources/{source_id}
Updates the specified source

Allows partial updates to the source.


# Create Corpus Source
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-post

post /api/corpora/{corpus_id}/sources
Creates a new source for the specified corpus



# Create Corpus File Upload
Source: https://docs.ultravox.ai/api-reference/corpora/corpora-uploads-post

post /api/corpora/{corpus_id}/uploads
Creates a new URL and document ID to use for uploading a static file

<Warning>Upload URLs expire after 5 minutes. You can request a new URL if needed.</Warning>


# Query Corpus
Source: https://docs.ultravox.ai/api-reference/corpora/corpus-query

post /api/corpora/{corpus_id}/query
Queries the specified corpus and returns the specified number of results

<Warning>
  <b>Use the queryCorpus Tool</b>

  <br />

  Any agents that you deploy should use the <a href="/tools/built-in-tools#querycorpus">built-in queryCorpus tool</a>.

  <br />

  This endpoint should be use for testing.
</Warning>


# Corpus Service (RAG) Overview
Source: https://docs.ultravox.ai/api-reference/corpora/overview

Understanding Retrieval Augmented Generation in Ultravox

The Ultravox corpus service is the easiest way to add [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) to your agents. All of the relevant APIs appear under `/api/corpora` (note: 'corpora' is the plural of 'corpus').

## Corpus Overview

```mermaid theme={null}
flowchart LR
    1(Corpus) -->|contains| 2(Source) -->|produces| 3(Document) -->|comprised of| 4(Chunk) -->|referenceable by| 5(Vector)
```

Each `Corpus` can contain one or more sources. Each `Source` contributes one or more documents, which are single files (HTML page, PDF, DOC, etc.). Each `Document` is broken up into one or more chunks, which are the units that may be returned for a query. For each `Chunk` several vectors are produced for similarity search.

The API exposes metadata about documents as well as the number of chunks and vectors in a corpus. However, there are no APIs provided to directly manipulate or edit documents, chunks, or vectors. If you need to update or delete documents, you must update or delete the source.

## Providing Corpus Access to Agents

<Warning>
  <b>Keep API Keys Safe</b>

  <br />

  Using the [Query Corpus](/api-reference/corpora/corpus-query) endpoint directly from your agents could expose your Ultravox API key. Use the `queryCorpus` tool instead.
</Warning>

We provide the built-in [queryCorpus](/tools/built-in-tools) tool that should be used by your agents. For example, if we wanted to create a voice agent to answer questions about Seattle, we could provide the tool like this:

```json theme={null}
{
  "systemPrompt": "Use the queryCorpus tool to answer questions about Seattle.",
  "selectedTools": [
    {
      "toolName": "queryCorpus", 
      "parameterOverrides": {
        "corpus_id": "<your_corpus_id_here>",
        "max_results": 5
      }
    }
  ]
}
```

### queryCorpus Tool Performance

* Maximum of 20 chunks per query
  * By default, the model may dynamically choose a value between 1-20, defaulting to 5. A static value may be provided via override.
  * Query response latency is not significantly impacted by the number of chunks returned.
  * More chunks returned will grow the overall agent context, which will mean slower subsequent generations.
  * More chunks may also confuse the agent if most chunks are irrelevant.

## Limits and Configuration

### Overall Limits

The system has the following limits:

* 20 sources (max) per corpus
* 200 documents (max) per source
* 10MB (max) document size for file uploads

### Account Limits

* Default limit is 2 corpora per account
* [Paid plans](https://ultravox.ai/pricing) have higher limits on corpora

### Document Management

* Documents can be viewed but not edited directly
* To update documents, create a new source
* Supported document types:

  * Text files (including Markdown)
  * PDFs
  * Word documents
  * EPUB files
  * PowerPoint presentations

  Note: If there are additional content types you need, please [let us know](https://discord.com/channels/1240071833798184990/1323352273165881426).

### Source Management

* PATCH requests on a source triggers a refresh/recrawl while maintaining the ID and created timestamp
* The corpus is still queryable during a recrawl but might return inconsistent (i.e. outdated) resources until the recrawl is finished
* Provided urls via `startUrls` will trigger crawling on anything in the same domain (subdomains must be specified separately)

### Deletion Behavior

* Deleting a corpus cascades to remove all associated:
  * Sources
  * Documents
  * Chunks
  * Vectors
* Deleted corpora cannot be queried
* Deleting a source cascades to remove all associated documents, chunks, and vectors


# Ultravox REST API Overview
Source: https://docs.ultravox.ai/api-reference/introduction



<Info>
  <b>Get an API Key</b>

  Using the Ultravox API requires an API key.

  You can [sign-up](https://app.ultravox.ai) for a free account that comes with 30 free minutes for creating calls.
</Info>

## Base URL

The Ultravox API is available at `https://api.ultravox.ai/api/`.

## API Keys

Ultravox API keys are 41 characters long and are made up of two alphanumeric parts separated by a period. The first part is 8 characters long and the second is 32 characters.

For example: `Zk9Ht7Lm.wX7pN9fM3kLj6tRq2bGhA8yE5cZvD4sT`

Throughout the docs we use `aBCDef.123456` for brevity.

## X-API-Key Header

When making API calls, pass your key in using the `X-API-Key` header.

<Warning>
  <b>You should never expose your API key to client code</b>

  If you *really* want to ignore this advice for a local demo, use the X-Unsafe-API-Key header instead at your own risk. It works the same way except that our server will allow it in CORS preflight requests.
</Warning>

Here's an example showing how to use the fictional API key `aBCDef.123456` to get a list of calls:

<CodeGroup>
  ```bash curl theme={null}
  curl --request GET \
  --url https://api.ultravox.ai/api/calls \
  --header 'X-API-Key: aBCDef.123456'
  ```

  ```js JavaScript theme={null}
  fetch('https://api.ultravox.ai/api/calls', {
    method: 'GET',
    headers: {
      'X-API-Key': 'aBCDef.123456'
    }
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
  ```
</CodeGroup>

## Rate Limits

The Ultravox API includes safeguards to help maximize stability for all customers. Too many API requests can trigger an error with status code `429`. See [Scaling & Call Concurrency](/gettingstarted/concurrency) for more information on `429` errors and how to properly handle them.

### API Limits

We restrict the number of total API requests per second. This restriction applies to all API endpoints that are part of `https://api.ultravox.ai/api/`.

We restrict at the account and API key level as follows:

| Level          | API Requests per Second |
| -------------- | ----------------------- |
| <b>Account</b> | 500                     |
| <b>API Key</b> | 200                     |

### Call Creation Limits

In addition to the overall [API limits](#api-limits) above, we place additional restrictions on how quickly accounts can create calls in the system.

| Plan Type    | Per Second | Per Minute |
| ------------ | ---------- | ---------- |
| Free / PAYGO | 5          | 30         |
| Pro          | 10         | 120        |
| Scale        | 30         | 360        |

> *Call creation is limited by whichever threshold is reached first (per second or per minute).*

### Call Concurrency Limits

The number of concurrent calls allowed depends on your plan.

| Plan Type    | Concurrency Cap | Priority Access |
| ------------ | --------------- | --------------- |
| Free / PAYGO | 5 calls         | ❌               |
| Pro          | No hard cap\*   | ❌               |
| Scale        | No hard cap\*   | ✅ Up to 100     |

> \*Still subject to infra limits under extreme load.

See [Scaling & Call Concurrency](/gettingstarted/concurrency) for more details on how call concurrency works in Ultravox Realtime.

## Playground

If you want to quickly experiment with prompts and voices, the fastest way to do that is in the [Ultravox Dashboard](https://app.ultravox.ai/playground).

You can also paste in an Ultravox API key throughout the API reference (look for "Authorization" and paste your key where it asks for `X-API-Key`) and test the REST API endpoints.


# List Models
Source: https://docs.ultravox.ai/api-reference/other/models-get

get /api/models
Retrieves the list of all available models that can be used for inference



# Get OpenAPI Schema
Source: https://docs.ultravox.ai/api-reference/other/schema-get

get /api/schema/
Gets the OpenAPI schema for the Ultravox REST API

Format can be selected via content negotiation.

* YAML: application/vnd.oai.openapi
* JSON: application/vnd.oai.openapi+json


# Base Tool Definition
Source: https://docs.ultravox.ai/api-reference/schema/base-tool-definition





# Call Definition
Source: https://docs.ultravox.ai/api-reference/schema/call-definition





# Ultravox Data Message Protocol
Source: https://docs.ultravox.ai/api-reference/schema/datamessages

Protocol documentation for messages exchanged between client and server during Ultravox calls.

See [Data Messages](/apps/datamessages) for more information.


# Get Account SIP configuration
Source: https://docs.ultravox.ai/api-reference/sip/sip-get

get /api/sip
Returns the SIP configuration for your account



# Update Account SIP configuration
Source: https://docs.ultravox.ai/api-reference/sip/sip-partial-update

patch /api/sip
Allows updating your account's SIP configuration



# Create SIP Registration
Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-create

post /api/sip/registrations
Creates a new SIP registration using the given properties



# Delete SIP Registration
Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-delete

delete /api/sip/registrations/{registration_id}
Deletes the specified registration



# Get SIP Registration
Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-get

get /api/sip/registrations/{registration_id}
Gets details for the specified registration



# List SIP Registrations
Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-list

get /api/sip/registrations
Lists SIP registrations for your account



# Update SIP Registration
Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-partial-update

patch /api/sip/registrations/{registration_id}
Updates an existing registration



# Delete Tool
Source: https://docs.ultravox.ai/api-reference/tools/tools-delete

delete /api/tools/{tool_id}
Deletes the specified tool



# Get Tool
Source: https://docs.ultravox.ai/api-reference/tools/tools-get

get /api/tools/{tool_id}
Gets details for the specified tool



# Get Tool History
Source: https://docs.ultravox.ai/api-reference/tools/tools-history-get

get /api/tools/{tool_id}/history
Gets all calls that have used the specified tool



# List Tools
Source: https://docs.ultravox.ai/api-reference/tools/tools-list

get /api/tools
Retrieves all available tools



# Create Tool
Source: https://docs.ultravox.ai/api-reference/tools/tools-post

post /api/tools
Creates a new tool



# Update Tool
Source: https://docs.ultravox.ai/api-reference/tools/tools-put

put /api/tools/{tool_id}
Replaces an existing tool

Updating a single field in a tool is not supported. The entire tool definition must be provided.


# Test Tool
Source: https://docs.ultravox.ai/api-reference/tools/tools-test-post

post /api/tools/{tool_id}/test
Tests a tool by executing it with the provided parameters



# Preview Voice
Source: https://docs.ultravox.ai/api-reference/voices/voice-preview-post

post /api/voice_preview
Performs a test generation of a voice, returning the resulting audio or error.



# Delete Voice
Source: https://docs.ultravox.ai/api-reference/voices/voices-delete

delete /api/voices/{voice_id}
Deletes the specified voice



# Get Voice
Source: https://docs.ultravox.ai/api-reference/voices/voices-get

get /api/voices/{voice_id}
Gets details for the specified voice



# List Voices
Source: https://docs.ultravox.ai/api-reference/voices/voices-list

get /api/voices
Retrieves all available voices



# Update Voice
Source: https://docs.ultravox.ai/api-reference/voices/voices-patch

patch /api/voices/{voice_id}
Updates the specified voice

Allows partial modifications to the voice.


# Create (Clone) Voice
Source: https://docs.ultravox.ai/api-reference/voices/voices-post

post /api/voices
Create a new cloned voice

Any created voices are private to your account.

Uses multipart/form-data encoding to provide the name of the voice along with an audio file containing the voice to be used for cloning.

<VoiceCloneLimit />


# Get Voice Sample
Source: https://docs.ultravox.ai/api-reference/voices/voices-preview-get

get /api/voices/{voice_id}/preview
Provides an audio sample for a voice, or the error caused by using it.



# Replace Voice
Source: https://docs.ultravox.ai/api-reference/voices/voices-put

put /api/voices/{voice_id}
Replaces the specified voice



# Delete Webhook
Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-delete

delete /api/webhooks/{webhook_id}
Deletes the specified webhook configuration



# Get Webhook
Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-get

get /api/webhooks/{webhook_id}
Gets details for the specified webhook configuration



# List Webhooks
Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-list

get /api/webhooks
Retrieves all webhooks configured on an account



# Update Webhook
Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-patch

patch /api/webhooks/{webhook_id}
Updates the specified webhook configuration

Allows partial modifications to the webhook.


# Create Webhook
Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-post

post /api/webhooks
Creates a new webhook configuration for an account



# Replace Webhook
Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-put

put /api/webhooks/{webhook_id}
Replaces the specified webhook configuration

Completely replaces the webhook. For partial modifications, use [Update Webhook](./webhooks-patch)


# Protocol & Data Messages
Source: https://docs.ultravox.ai/apps/datamessages

Protocol documentation for messages exchanged between client and server during Ultravox calls.

Data messages are used to communicate non-audio information during Ultravox calls. These messages enable real-time control and interaction with ongoing conversations.

## Communication Methods

* **Client Data Channels** → Used by our [SDKs](/apps/sdks) and [WebSocket](/apps/websockets) connections for bi-directional, real-time message exchange during calls. This is the primary method for client apps to interact with calls.
* **Data Connection** → Add a [data connection](/api-reference/calls/calls-post#body-data-connection) to your call to receive messages via a separate WebSocket connection. This is particularly useful for:
  * Telephony integrations where the client doesn't support WebRTC
  * Server-side applications that need to monitor call events or route data to external systems
* **REST API** → Inject messages into active calls via HTTP POST requests. See [Sending Messages to Live Calls via REST API](#sending-messages-to-live-calls-via-rest-api) below for detailed implementation guidelines.

## Messages at a Glance

Details on each message type appear below in [Data Message Details](#data-message-details).

### Client-to-Server Messages

| Type           | Message                                                                                         | Description                                                            |
| -------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Agent Behavior | [ForcedAgentMessage](#forcedagentmessage)                                                       | Forces the agent to say a specific message or invoke tools.            |
| Call Control   | [HangUp](#hangup)                                                                               | Instructs the agent to end the call with an optional farewell message. |
| Call Control   | [SetOutputMedium](#setoutputmedium)                                                             | Sets server's output medium to text or voice.                          |
| System         | [Ping](#ping)                                                                                   | Measures round-trip data latency.                                      |
| Tools          | [ClientToolResult and DataConnectionToolResult](#clienttoolresult-and-dataconnectiontoolresult) | Contains the result of a tool invocation.                              |
| User Input     | [UserTextMessage](#usertextmessage)                                                             | Used to send a user message to the agent.                              |

### Server-to-Client Messages

| Type         | Message                                                                                                         | Description                                                  |
| ------------ | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Conversation | [CallStarted](#callstarted)                                                                                     | Provides some basic information about the call at its start. |
| Conversation | [Transcript](#transcript)                                                                                       | Contains text for an utterance made during the call.         |
| System       | [Debug](#debug)                                                                                                 | Useful for application debugging. Excluded by default.       |
| System       | [PlaybackClearBuffer](#playbackclearbuffer)                                                                     | Used to clear buffered output audio. WebSocket only.         |
| System       | [Pong](#pong)                                                                                                   | Server reply to a ping message.                              |
| System       | [State](#state)                                                                                                 | Indicates the server's current state.                        |
| Tools        | [ClientToolInvocation and DataConnectionToolInvocation](#clienttoolinvocation-and-dataconnectiontoolinvocation) | Asks the client or data connection to invoke a tool.         |

## Data Message Details

All messages are JSON objects with camelCase keys containing:

* A required `type` field identifying the message type
* Additional fields specific to each message type

### Ping

A message sent by the client to measure round-trip data message latency.

**Message Structure**

```js theme={null}
{
  "type": "ping",
  "timestamp": 1234567890.123
}
```

**Fields**

<ResponseField name="timestamp" type="float">
  Unix timestamp with millisecond precision. Client timestamp for latency measurement.
</ResponseField>

### Pong

A message sent by the server in response to a PingMessage. The timestamp is copied from the PingMessage.

**Message Structure**

```js theme={null}
{
  "type": "pong",
  "timestamp": 1234567890.123
}
```

**Fields**

<ResponseField name="timestamp" type="float">
  Echoed timestamp from the original ping message.
</ResponseField>

### State

A message sent by the server to indicate its current state.

**Message Structure**

```js theme={null}
{
  "type": "state",
  "state": "listening"
}
```

**Fields**

<ResponseField name="state" type="string">
  Current session state.  One of: `idle`, `listening`, `thinking`, or `speaking`.
</ResponseField>

### Transcript

A message containing text transcripts of user and agent utterances.

**Message Structure**

```js theme={null}
{
  "type": "transcript",
  "role": "agent",
  "medium": "voice",
  "text": "Full transcript so far",  // Either text or delta will be set
  "delta": null,
  "final": false,
  "ordinal": 1
}
```

**Fields**

<ResponseField name="role" type="string">
  Who emitted the utterance. Must be either "user" or "agent".
</ResponseField>

<ResponseField name="medium" type="string">
  The medium through which the utterance was emitted. Either "text" or "voice".
</ResponseField>

<ResponseField name="text" type="string">
  The full text of the transcript so far. Either this or delta will be set, but not both.
</ResponseField>

<ResponseField name="delta" type="string">
  The additional transcript text added since the last transcript message. Either this or text will be set, but not both.
</ResponseField>

<ResponseField name="final" type="boolean">
  Whether to expect additional transcript messages for this conversation round.
</ResponseField>

<ResponseField name="ordinal" type="integer">
  The ordinal of the message within the current call, used for ordering transcripts.
</ResponseField>

### UserTextMessage

A user message sent via text. The message appears to the agent as if it came from the user.

**Message Structure**

```js theme={null}
{
  "type": "user_text_message",
  "text": "Your message here",
  "urgency": "soon"  // Optional, defaults to "soon"
}
```

**Fields**

<ResponseField name="text" type="string">
  The content of the user message.
</ResponseField>

<ResponseField name="urgency" type="string">
  Determines whether this message can interrupt the agent and whether it should trigger a generation. Options:

  * immediate → Interrupts the agent if speaking and starts a new generation immediately.
  * soon → Doesn't interrupt but starts a generation at the next opportunity.
  * later → Message is considered during the next natural generation without forcing a new generation.
</ResponseField>

### SetOutputMedium

Message sent by the client to set the server's output medium.

**Message Structure**

```js theme={null}
{
  "type": "set_output_medium",
  "medium": "voice"
}
```

**Fields**

<ResponseField name="medium" type="string">
  Output medium to use. Must be either "voice" or "text".
</ResponseField>

### ClientToolInvocation and DataConnectionToolInvocation

Sent by the server to ask the client or data connection to invoke a tool with the given parameters. The client or data connection is expected to send back a ClientToolResultMessage or DataConnectionToolResultMessage with a matching invocationId.

**Message Structure**

```js theme={null}
{
  "type": "client_tool_invocation", // Or "data_connection_tool_invocation" for data connections
  "toolName": "get_weather",
  "invocationId": "unique-invocation-id",
  "parameters": {
    "location": "Seattle"
  }
}
```

**Fields**

<ResponseField name="toolName" type="string">
  Name of the tool to invoke.
</ResponseField>

<ResponseField name="invocationId" type="string">
  Unique identifier for this invocation. Must be included in the corresponding result.
</ResponseField>

<ResponseField name="parameters" type="object">
  Tool-specific parameters as a JSON object.
</ResponseField>

### ClientToolResult and DataConnectionToolResult

Contains the result of a tool invocation.

**Message Structure**

```js theme={null}
{
  "type": "client_tool_result", // Or "data_connection_tool_result" for data connections
  "invocationId": "matching-invocation-id",
  "result": "Tool execution result",
  "responseType": "tool-response",
  "agentReaction": "speaks",
  "errorType": null,
  "errorMessage": null,
  "updateCallState": null
}
```

**Fields**

<ResponseField name="invocationId" type="string">
  Must match the invocationId from the corresponding invocation.
</ResponseField>

<ResponseField name="result" type="string">
  Typically the tool execution result as viewed by the agent, which is often a JSON string. May be omitted for errors.
  For responseTypes other than `tool-response`, this may be a JSON string for an object that further specifies how the response should be handled. See [special response types](https://docs.ultravox.ai/tools/custom/changing-call-state#special-tool-response-types).
</ResponseField>

<ResponseField name="responseType" type="string">
  Type of response being provided. See [special response types](https://docs.ultravox.ai/tools/custom/changing-call-state#special-tool-response-types).
</ResponseField>

<ResponseField name="agentReaction" type="string">
  How the agent should react. Options: "speaks" (default), "listens", or "speaks-once". See [Agent Responses to Tools](/tools/custom/agent-responses) for more.
</ResponseField>

<ResponseField name="errorType" type="string">
  Error classification if the tool failed. Should be omitted when result is set.

  Options:

  * undefined → Tool with the given name does not exist
  * implementation-error → Tool exists but execution failed
</ResponseField>

<ResponseField name="errorMessage" type="string">
  Human-readable error description if the tool failed. This is not seen by the model but may be used for debugging.
</ResponseField>

<ResponseField name="updateCallState" type="object">
  Optional state updates to apply to the call. See [Tool State](/agents/guiding-agents#tool-state) for more.
</ResponseField>

### Debug

A message sent by the server to communicate debug information. Disabled by default.

**Message Structure**

```js theme={null}
{
  "type": "debug",
  "message": "Debug information here"
}
```

**Fields**

<ResponseField name="message" type="string">
  Debug information or diagnostic details.
</ResponseField>

<Note>
  Debug messages are disabled by default and must be explicitly enabled for debugging purposes.
</Note>

### CallStarted

Basic call metadata shared by the server when a call begins.

**Message Structure**

```js theme={null}
{
  "type": "call_started",
  "callId": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Fields**

<ResponseField name="callId" type="string">
  The UUID of the call that has started.
</ResponseField>

### PlaybackClearBuffer

Message sent by the server to clear buffered output audio. Integrators should drop as much unplayed output audio as possible for interruptions to function properly.

**Message Structure**

```js theme={null}
{
  "type": "playback_clear_buffer"
}
```

<Note>
  This message is only used with WebSocket connections. Handling this message allows for [larger client buffers](/api-reference/agents/agents-post#body-call-template-medium-server-web-socket-client-buffer-size-ms) while maintaining responsive interrupts. Larger client buffers make choppy audio less likely in the presence of network disruption or resource contention.
</Note>

### ForcedAgentMessage

Forces the agent to say a specific message or invoke tools.

**Message Structure**

```js theme={null}
{
  "type": "forced_agent_message",
  "content": "Text for the agent to say",  // Optional (default: "")
  "toolCalls": [  // Optional array of tool calls
    {
      "id": "unique-invocation-id",  // Optional, generated if not provided
      "name": "tool_name",
      "arguments": {
        "param1": "value1"
      }
    }
  ],
  "uninterruptible": false,  // Optional (default: false)
  "urgency": "soon"  // Optional: "immediate" or "soon" (default: "soon")
}
```

**Fields**

<ResponseField name="content" type="string">
  Text content the agent should speak.
</ResponseField>

<ResponseField name="toolCalls" type="array">
  Array of tool invocations to execute.
</ResponseField>

<ResponseField name="uninterruptible" type="boolean">
  If true, prevents interruption while the agent speaks this message. (Note that tools are always uninterruptible.)
</ResponseField>

<ResponseField name="urgency" type="string">
  Controls when the message is processed. Must be either "immediate" (may interrupt the user or agent) or "soon" (process at next opportunity).
</ResponseField>

### HangUp

Instructs the agent to end the call with an optional farewell message.

**Message Structure**

```js theme={null}
{
  "type": "hang_up",
  "message": "Goodbye!"
}
```

**Fields**

<ResponseField name="message" type="string">
  Final message to speak before ending the call.
</ResponseField>

## Sending Messages to Live Calls via REST API

The [Send Data Message to Call](/api-reference/calls/calls-send-data-message-post) endpoint allows you to inject messages into active calls (calls that are joined and not yet ended).

### Supported Message Types

* [ForcedAgentMessage](#forcedagentmessage)
* [HangUp](#hangup)
* [UserTextMessage](#usertextmessage)

### Responses

Successful messages sent via the REST API will receive a `204 No Content` response with an empty body.

Potential error responses include:

* `401 Unauthorized`: Missing or invalid API key
* `403 Forbidden`: Insufficient authorization
* `422 Unprocessable Entity`: Call is not active (either not joined yet or already ended)


# Overview: Using Ultravox in Apps or via WebSockets.
Source: https://docs.ultravox.ai/apps/overview

Add conversational voice AI to any application - from web and mobile apps to custom server integrations using WebSockets.

In addition to enabling voice AI agents via [Telephony](/telephony/overview), Ultravox Realtime provides support for web & native applications and provides a native protocol that supports fully custom integrations via WebSockets.

<Columns>
  <Card title="Web Apps" icon="globe" href="/apps/sdks">
    Integrate agents into web applications using our JS SDK.
  </Card>

  <Card title="Native Apps" icon="mobile" href="/apps/sdks">
    Use one of our supported SDKs for mobile or native apps.
  </Card>

  <Card title="WebSockets Protocol" icon="plug">
    Use the native websockets protocol for custom server-to-server integrations.
  </Card>
</Columns>

## Next Steps

* Explore our native [SDKs →](./sdks)
* Dive into the complete [SDK Reference →](/sdk-reference/introduction)
* Learn how to do a custom integration via [WebSockets →](./websockets) and read the guide on the [Ultravox Protocol →](./datamessages)


# SDKs
Source: https://docs.ultravox.ai/apps/sdks

Ultravox Client SDK for building user-facing experiences.

If you are building a voice AI application that has a front end (e.g. web, mobile, desktop), then you should use our client SDK which is designed to deliver high-quality audio at low-latency. The Ultravox Client SDK uses WebRTC.

## SDK Features

All the features of the SDK are documented in the [SDK Reference](/sdk-reference/introduction).

## SDK Implementations

<SDKCards />

## Additional Resources

* Need your voice AI agent to make or receive phone calls? Check out our guide on [Telephony →](/telephony/overview)
* Ultravox has a native protocol for fully custom integrations via [WebSockets →](/apps/websockets)


# WebSocket Integration
Source: https://docs.ultravox.ai/apps/websockets

Integrate with your server via direct WebSocket connections.

<Warning>
  <b>Server-to-Server Only</b>

  <br />

  WebSocket connections are designed for server-to-server communication. For browser or mobile applications, use our client SDKs with WebRTC for optimal performance. WebSocket connections over TCP can experience audio blocking and ordering constraints that make them unsuitable for direct client use.
</Warning>

### Creating a WebSocket Call

Creating a WebSocket-based call with Ultravox requires setting `medium` to `serverWebSocket` and passing in parameters for sample rates and buffer size.

* **inputSampleRate** (required): Sample rate for input (user) audio (e.g., 48000).
* **outputSampleRate** (optional): Sample rate for output (agent) audio (defaults to inputSampleRate).
* **clientBufferSizeMs** (optional): Size of the client-side audio buffer in milliseconds. Smaller buffers allow for faster interruptions but may cause audio underflow if network latency fluctuates too greatly. For the best of both worlds, set this to some large value (e.g. 30000) and implement support for [PlaybackClearBuffer](/apps/datamessages#playbackclearbuffer) messages. (Defaults to 60).

```js Example: Creating an Ultravox Call for WebSockets theme={null}
    const response = await fetch('https://api.ultravox.ai/api/calls', {
        method: 'POST',
        headers: {
            'X-API-Key': 'your_api_key',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            systemPrompt: "You are a helpful assistant...",
            model: "ultravox-v0.7",
            voice: "Mark",
            medium: {
                serverWebSocket: {
                    inputSampleRate: 48000,
                    outputSampleRate: 48000,
                }
            }
        })
    });

    const { joinUrl } = await response.json();
```

```python Example: Joining an Ultravox Call via Websockets theme={null}
import websockets

socket = await websockets.connect(join_url)
audio_send_task = asyncio.create_task(_send_audio(socket))
async for message in socket:
    if isinstance(message, bytes):
        # Handle agent audio data
    else:
        # Handle data message. See "Data Messages"

...

async def _send_audio(socket: websockets.WebSocketClientProtocol):
    async for chunk in some_audio_source:
        # chunk should be a bytes object containing s16le PCM audio from the user
        self._socket.send(chunk)
```

See [Data Messages](/apps/datamessages) for more information on all available messages.

<Note>
  <b>Data Messages</b>

  <br />

  WebSocket connections use the same message format as WebRTC data channels. See our [Data Messages](/apps/datamessages) documentation for detailed message specifications.
</Note>


# Deprecation Guide
Source: https://docs.ultravox.ai/changelog/deprecation

Track upcoming breaking changes, migration timelines, and deprecation notices for the Ultravox platform.

## Active Deprecations

### Currently Scheduled Changes

| Feature/API                           | Status        | Deprecation Date | Removal Date | Migration Guidance                  |
| ------------------------------------- | ------------- | ---------------- | ------------ | ----------------------------------- |
| `fixie-ai/ultravox-qwen3-32b-preview` | ⚠️ \< 30 days | 2025-12-03       | 2025-12-22   | [Guide](/changelog/migration/qwen3) |

### Current Migration Guides

* [Migrating from Qwen3 32B Model](/changelog/migration/qwen3)

## Deprecation Process

We recognize that breaking changes and deprecation notices are not fun and we try to avoid them when possible.

However, the Ultravox APIs have not yet reached v1 and we are committed to having our APIs and SDKs work better and be as clear as possible. This means we will inevitably need to revisit some choices early on.

This process will evolve as the APIs mature. Please share your feedback with us if you'd like to see any changes to the process or policy.

### Lifecycle Stages

<Tabs>
  <Tab title="1. Announcement">
    * Feature marked as deprecated in documentation
    * Migration guidance published
  </Tab>

  <Tab title="2. Deprecation Period">
    * Minimum 30-day window
    * Reminders in changelog and community updates
    * Direct communications to affected users
  </Tab>

  <Tab title="3. Removal">
    * Feature removed
    * Fallback behavior documented if applicable
  </Tab>
</Tabs>

## Deprecation Policy

### Standard Timeline

* Pre-release features: 30-day minimum deprecation period
* Breaking changes require publication of migration guidance

### Security Exceptions

Critical security updates may bypass the standard deprecation timeline. These will be:

* Clearly marked and documented
* Communicated directly to affected users
* Accompanied by immediate mitigation steps

<Note>
  <b>Need Help?</b>

  If you need assistance with a migration, please visit our [Discord community ](https://discord.gg/62X253zeWB).
</Note>

## Past Deprecations

| Feature/API | Status   | Deprecation Date | Removal Date | Migration Guidance                         |
| ----------- | -------- | ---------------- | ------------ | ------------------------------------------ |
| `initiator` | 🛑 ended | 2024-10-01       | 2024-12-31   | [Guide](/changelog/migration/firstspeaker) |

### Past Migrations

* [Migrating from Call `initiator`](/changelog/migration/firstspeaker)


# News & Updates
Source: https://docs.ultravox.ai/changelog/news

Stay informed about Ultravox platform announcements.

<Card title="Be in the Know" icon="head-side-brain">
  All Ultravox customers automatically receive email updates. Create a [free account](https://app.ultravox.ai) to start building with the the best voice AI and to stay in the loop.
</Card>

## Latest Update

### 2025-12-03 - Ultravox v0.7 Model

We're announcing an important upgrade to Ultravox's default model that will deliver better instruction following, more reliable tool calling, and improved accuracy for your voice AI applications.

#### Default Model Switching to GLM 4.6

* **The Big Change** → On December 22, 2025, our default model will switch from Llama 3.3 70B to GLM 4.6. While Llama has served us well, GLM 4.6 delivers superior performance in critical areas: instruction following, tool calling accuracy, and overall speech understanding. It's a significant upgrade for voice AI applications.
* **Production Ready** → The new model is production-ready today and we've already upgraded Blocky, our built-in agent builder, to use it.
* **Same Great Price** → Stays at our standard \$0.05 per minute rate. Better model, same price.

<Danger>
  **Calls Default to v0.7**
  Not setting a model string or using the generic `fixie-ai/ultravox` string will default to using the v0.7 model. If you are not ready to migrate from Llama, use the `ultravox-v0.6` model string.
</Danger>

#### Model Timeline and Migration Details

**What You Need to Do:**
Depending on your current agent settings, expect the following changes on December 22:

* **Default Model Change** → Agents and calls not setting the model or using the default `fixie-ai/ultravox` model will automatically switch from Llama 3.3 70B to GLM 4.6.
* **Stick with Llama** → If you are not ready to switch from Llama, we are adding the model string `ultravox-v0.6` (or `ultravox-v0.6-llama3.3-70b`) that will continue to use Llama 3.3 70B. `fixie-ai/ultravox-llama3.3-70b` will continue to work.
* **Qwen Support Ends** → If your agent is configured to use `fixie-ai/ultravox-qwen3-32b-preview`, you will need to choose a different model before December 22. If you do not select a different model before that date, your calls will fail until you update your configuration.

<Warning>
  **Start Testing Today:**
  Use model string `ultravox-v0.7` to test the new GLM 4.6 backed model with your agents now.
</Warning>

**Timeline:**

* **Today (December 3)** → Start testing with `ultravox-v0.7` and adjust your prompts as needed (GLM is a much better instruction follower so you may need to cut down on repetitive or overt instructions used to get Llama to comply).
* **December 22**:
  * Default model becomes GLM 4.6 (model string `ultravox-v0.7`)
  * Llama 3.3 70B remains available via `ultravox-v0.6` (or `ultravox-v0.6-llama3.3-70b`)
  * Qwen3 support ends (`fixie-ai/ultravox-qwen3-32b-preview` will no longer work)

#### Available Models and Status

##### Currently Supported Models

| Model String                 | Base LLM      | Status |
| ---------------------------- | ------------- | ------ |
| `ultravox-v0.7`              | GLM 4.6       | ✅      |
| `ultravox-v0.6`              | Llama 3.3 70B | ✅      |
| `ultravox-v0.6-llama3.3-70b` | Llama 3.3 70B | ✅      |
| `ultravox-v0.6-gemma3-27b`   | Gemma 27B     | ✅      |

##### Model Transition Status

| Model                | Model String                                                         | Status                                                                                                                                                                                                       |
| -------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ultravox Default     | `fixie-ai/ultravox`                                                  | Currently points to `ultravox-v0.6-llama3.3-70b`<br />Will instead point to `ultravox-v0.7` beginning Dec 22                                                                                                 |
| GLM 4.6              | `fixie-ai/ultravox-v0.7` and `fixie-ai/ultravox-glm4.6-355b-preview` | Available now and ongoing as model string `ultravox-v0.7`                                                                                                                                                    |
| GLM 4.5 (Preview)    | `fixie-ai/ultravox-glm4.5-355b-preview`                              | Redirects to GLM 4.6. Switch to `ultravox-v0.7`                                                                                                                                                              |
| Llama 3.3 70B        | `fixie-ai/ultravox-llama3.3-70b`                                     | Available now and will continue post Dec 22<br />The only way to use this model post Dec 22 is to manually set the full model string to either `ultravox-v0.6` (recommended) or `ultravox-v0.6-llama3.3-70b` |
| Qwen 3 32B (Preview) | `fixie-ai/ultravox-qwen3-32b-preview`                                | Will be removed on Dec 22                                                                                                                                                                                    |
| Gemma 27B (Preview)  | `fixie-ai/ultravox-gemma3-27b-preview`                               | Available now and ongoing as model string `ultravox-v0.6-gemma3-27b`                                                                                                                                         |

#### What's Next

**Multiple Models for Flexibility** → We train multiple Ultravox model variants using various LLMs to give customers choice and flexibility. While GLM 4.6 will become our default due to superior performance, we'll continue to make other models like Llama 3.3 and Gemma available for customers who find they work better for specific scenarios.

**Testing Recommendation** → If you're not specifying a model string for your calls or are using `fixie-ai/ultravox`, your agents will automatically get GLM 4.6 on December 22. We strongly recommend upgrading to `ultravox-v0.7` immediately and testing before then to ensure your prompts work as expected. If you're using Llama and have emphasized importance to the model with phrases like "you must...", ensure those instructions don't harm performance with GLM 4.6, which is a better instruction follower.

## Prior Updates

### 2025-01-03 - Upgrades to Model, Tools Performance, and Docs

We're kicking off 2025 with exciting improvements and community-driven developments build on our leading platform for voice AI (5 cents per minute, highest quality voices, low latency, and SDKs for all major languages).

#### What's Hot

1. Model Upgrades and Performance Improvements
2. New Dashboard Features and Documentation
3. Community Hack Day Results

##### Model Upgrades and Performance Improvements

* **Model Upgrade** → Upgraded Ultravox 0.4.1 to run on the newest Llama 3.3 model, delivering significantly improved instruction following and tool usage capabilities. This new model is now the default in the Ultravox Realtime service and the [HF model](https://huggingface.co/fixie-ai) and model card are available.
* **Improved Tool Performance** → Updated our vLLM tool parser with more lenient processing to better handle Llama's tool calling patterns, resulting in more consistent performance. We fixed an issue with large tool calls being unstable.
* **More Improvements** → Added [`vadSettings`](/api-reference/calls/calls-post) parameters for more control, new public [`hang-up`](/tools/built-in-tools#hangUp) tool, and added [`timeout`](/api-reference/schema/base-tool-definition) for tools.

##### New Dashboard Features and Documentation

* **Call History** → Introducing the [Call History](https://app.ultravox.ai/calls) page at app.ultravox.ai - dive deep into detailed call analytics, including tool error tracking. This is just the first of many dashboard improvements coming your way.

##### Community Hack Day Results

Last week's impromptu hack day brought our community together to share their vision for future voice agents.

Members were particularly interested in implementing features like knowledge lookup/RAG, human agent handoff, end-of-call transcript retrieval, Make.com integration, and Cal.com API calendar availability checking.

In response, we've released a new sample application that implements all these features as tools for the voice AI agent to call when needed (with end-of-call transcripts handled via webhooks). You can find the complete implementation on our [GitHub repo](https://github.com/fixie-ai/ultravox-examples/tree/main/telephony/twilio-incoming-advanced-js), along with a detailed [video walkthrough](https://youtu.be/sa9uF5Rr9Os).

#### What's Next

**Dashboard Evolution** → The new [Call History](https://app.ultravox.ai/calls) page is just the beginning. We're developing a no-code builder that will allow you to create and customize voice AI agents without writing any code. This will make it easier than ever to implement complex features like those showcased in our latest sample application, while still maintaining the flexibility for developers who prefer to code their own solutions.

**Other Improvements** → Building on our recent Llama 3.3 integration, we're focusing on further enhancing tool usage reliability and model performance. We are also working on providing automatic conversation summaries on call end.

### 2024-12-10 - WebSockets and More

We're excited to announce several new features and improvements to the Ultravox platform, including new integration options, model support, and infrastructure updates.

#### What's Hot

1. New Features: WebSockets, Telnyx, and Plivo
2. SDK and Other Improvements
3. Docs Updates (Including "News" and "Deprecation" pages)

##### New Features: WebSockets, Telnyx, and Plivo

* **WebSockets:** You can now integrate on the server side via [WebSockets](/apps/websockets).
* **Telnyx & Plivo:** New telephony integrations for Telnyx and Plivo are now available in addition to our existing support for Twilio. Check the [docs](/telephony/overview).

##### SDK and Other Improvements

* **SDK Updates:** New [client version](/apps/sdks/#joincall) tracking allows you to set an arbitrary value that is tied to calls (retrieve with GET on /calls endpoint).
* **Enhanced Call Transcripts:** For more accurate transcripts, you can now pass in the `languageHint` at call creation time to help guide the model.
* **Bug Fix:** Fixed an issue where errant connections could affect proper call termination.

##### Docs Updates

* Introduced new pages for [News](/changelog/news) and [Deprecations](/changelog/deprecation) to help you stay informed.
* Added comprehensive documentation for [initialMessages](/api-reference/calls/calls-post#body-initial-messages) and [inactivityMessages](/api-reference/calls/calls-post#body-inactivity-messages).

#### What's Not

We have one active deprecation: `initiator` will be deleted at the end of the month. This has been replaced with `firstSpeaker`. Not using `initiator`? You can ignore this. Otherwise, check out the [migration guide](/changelog/migration/firstspeaker/).

#### What's Next

We're actively working on several exciting features and improvements:

**Language and Voice Expansion:** Finnish language support is up next. We welcome your input on additional language requirements. Pop into [#feature-requests](https://discord.com/channels/1240071833798184990/1315065334058713198) to let us know which voices you'd like to see added to our roadmap!

**Infrastructure and Compliance:** EU datacenter planning in progress and GDPR compliance implementation is underway. If these initiatives are important to your operations, please schedule a meeting using my calendar link to discuss your specific requirements.

**Platform Enhancements:** Enhanced call visibility in the dashboard to help you more easily monitor usage and debug issues. We are working on adding a low latency RAG service and are continuing to work on additional optimizations for transcripts and function calling.

**Holiday Schedule Update:** Our team will be operating on a reduced schedule between Christmas and New Year's. While we'll maintain system health and provide emergency support, response times on Discord and email may be longer than usual during this period. Rest assured that all critical systems will remain fully monitored and supported by our on-call team.

### 2024-11-14 - Ultravox v0.4.1 Release

We're excited to announce the release of Ultravox v0.4.1, which brings significant improvements to the model you're already using. We've also added a new web console and have enabled your agents to start conversations via text.

#### What's Hot

1. Ultravox v0.4.1:  Six new languages, higher quality, new variants.
2. Ultravox Console:  Your web playground and place to manage your account.
3. initialOutputMedium: Agents can now start conversations via text.

##### Ultravox v0.4.1

**Expanded Language Coverage**

* Added 6 new languages (Chinese, Dutch, Hindi, Swedish, Turkish, and Ukrainian).
* Total of 15 languages are now supported by the model.

**Enhanced Performance**

* Improved BLEU scores across all languages.
* Now achieving average BLEU score of 38.97 (vs. GPT-4's 40.35).

**New Model Variants**

* Added Mistral NeMo variant.
* Updated Llama variants (8B model and 70B model) trained on 8xH100s.

The 0.4.1 updates are now live as the default on our managed Ultravox Realtime APIs. Pricing starts at just 5 cents per minute (⅓ the cost of GPT-4o).

The model weights are available on [Hugging Face](https://huggingface.co/fixie-ai), and you can find detailed release notes on our [GitHub repository](https://github.com/fixie-ai/ultravox). If you need on-premises support for end-to-end data sovereignty, please reach out via email or set-up a call to discuss.

For insights into our roadmap and strategy and to see a live demonstration of the new model in action, check out our latest [blog post](https://www.ultravox.ai/blog/ultravox-an-open-weight-alternative-to-gpt-4o-realtime).

##### Ultravox Console

There's now a web-based console application at [https://app.ultravox.ai](https://app.ultravox.ai) that you can use for keeping track of usage, generating API keys, managing your subscription, and playing around with different voices and system prompts. The console is a work-in-progress so don't hesitate to reach out with requests for new features!

##### initialOutputMedium

This new property can be set at call creation to have the agent's initial output be text (voice remains the default). This enables text-based scenarios and can be used with the SDK's [`setOutputMedium()`](/sdk-reference/introduction#setoutputmedium) to toggle between text and voice. Check out the Create Call docs for more info.

#### What's Next

We're already working on the next major release of Ultravox with even more exciting features. Your feedback has been invaluable in shaping our development, and we'd love to hear your thoughts on these latest improvements.

### 2024-10-18 - Call Stages and Client-Implemented Tools

We're thrilled to share the latest updates we've made to the Ultravox APIs. All of these enhancements have been made due to feedback from our community. Please keep the feedback coming! If there's anything we can do to make things work better for you, don't hesitate to get in touch!

#### What's Hot

1. Call Stages: Dynamic, Multi-Stage Conversations
2. Client-Implemented Tools: Implement Tools in Your App
3. More Improvements: setOutputMedium + Webhooks

##### Call Stages: Dynamic, Multi-Stage Conversations

* **What's new:** Stages enable more complex and nuanced agent interactions, giving you fine-grained control over the conversation flow.
* **Why it matters:** Each stage can have a new system prompt, a different set of tools, a new voice, an updated conversation history, and more.
* **Where to use:** Stages are designed for complex conversational flows like data gathering (job applications, medical intake forms, applying for a mortgage) or context switching (customer support escalation, triaging IT issues).
* **Where to start:** Check our [docs](/agents/call-stages) for the details on how to get started.

##### Client-Implemented Tools: Implement Tools in Your App

* **What's new:** In our previous update we added support for tools. Those were “server” tools and required you to implement the logic on a server and expose things via a URL. Client-implemented tools enable putting all the logic in your client application and are still called by your agent.
* **Why it matters:** Enable dynamic UI or other interactivity in your app without having to rely on putting all the logic on a server.
* **Learn more:** Visit our [SDK page](/sdk-reference/introduction#client-tools) for more info.

##### More Improvements: setOutputMedium + Webhooks

* **setOutputMedium():** Added to our SDKs to give you more control over how your agents respond. Allows toggling the agent's output between text and voice. See the [docs](/sdk-reference/introduction#setoutputmedium).
* **Webhooks:** Ultravox now has [webhooks](/api-reference/webhooks/webhooks-list) for two key events: `call.started` and `call.ended`. This opens up new opportunities for triggering external processes when calls start/end, logging call data in real-time to your own systems, or integrating Ultravox more deeply with other workflows.

#### What's Not

1. Breaking Change: SDK SessionState
2. Deprecation Notice: initiator on new call creation

We recognize that breaking changes and deprecation notices are not fun and we try to avoid them when possible. However, we are committed to having our APIs and SDKs work better and be as clear as possible. That means we will inevitably need to revisit some choices early on.

##### Breaking Change: SDK SessionState

In the latest versions of our client SDKs, the UltravoxSession joinCall() method no longer returns an object. UltravoxSession now exposes properties for `status` and `transcripts`.

##### Deprecation: `initiator` is now `firstSpeaker`

This change is being made because `firstSpeaker` is more descriptive of what is happening when the call starts. For example, if you are making an outbound call, you expect the user to answer the call and be the first to speak.
When creating a new call, you should start using `firstSpeaker` and choose either “FIRST\_SPEAKER\_AGENT” (the default) or “FIRST\_SPEAKER\_USER” (for outbound calls) as the value.

*`initiator` will be removed at the end of November, 2024.*

#### What's Next

We are working on a new version of the Ultravox model that will add new language support for Chinese, Dutch, Hindi, Swedish, Turkish, and Ukrainian. We are also creating a web-based application for the Ultravox service (sign-up, API key management, usage tracking) and are adding a Swift client SDK for iOS developers.

If you have any suggestions for new features or improvements, please don't hesitate to reach out.

### 2024-09-30 - 70B and Tools

We are continuing to get great feedback (thank you!) and have been working to add more capabilities.

#### What's Hot

1. Ultravox 70B: Our Smartest Model Yet
2. Tools Support: Give Your Agents New Abilities
3. Expanded SDK Coverage: Flutter, Kotlin, and Python

##### 1. Ultravox 70B: Brains Meet Brawn

* **Why it matters:** More complex reasoning, better understanding
* **How to use:** It's now the default! Just use 'fixie-ai/ultravox' in your API calls
* **Pro tip:** Need the 8B version? Use 'fixie-ai/ultravox-8B' (Note: Tools not supported)
* **Model weights:** Available on [HuggingFace](https://huggingface.co/fixie-ai/ultravox-v0_4-llama-3_1-70b)

##### 2. Tools: Your AI's New Superpowers

* **What's new:** Durable tools (create once, use often) and Temporary tools (perfect for iterating)
* **Where to start:** Check our [docs](/tools/overview) for the how-to
* **See it in action:** Try our [tools demo](https://demo.ultravox.ai/) on our website

##### 3. New SDKs: Code Your Way

* **New additions:** Flutter, Kotlin, and Python join our JavaScript SDK
* **Cool features:** [Debug Messages](/sdk-reference/introduction/#debug-messages), mic/speaker controls
* **Learn more:** Visit our [SDK page](/apps/sdks) for details

#### In Case You Missed It

* **Price drop:** Now just \$0.05/minute (cheaper than coffee, and way more talkative!)
* **Voice cloning:** Create [customized voices](/api-reference/voices/#create-clone-voice) for your agents
* **Conversation continuity:** Because [why start over](/api-reference/calls/calls-post)?

#### What's Next?

You tell us! We're all ears for your suggestions to make Ultravox even better for you.

### 2024-09-04 - Price Reduction, Resume Calls, Voice Cloning

* Our managed Ultravox APIs are getting *much* cheaper. We're decreasing our price to **\$0.05/min**. That's full-on, real-time, speech-to-speech voice chat. We think this is the highest quality, lowest cost system out there.
* We continue to offer 30 minutes of free usage to try it out for yourself. If you'd like to continue using our managed APIs after that, you'll need to set up a Stripe subscription. You can now do that by accessing the billingUrl from the new [/accounts API](/api-reference/accounts).
* We've added the ability to seamlessly continue a prior conversation. This is as simple as passing in a priorCallId parameter when [starting a call](/api-reference/calls).
* We've added support for [Voice Cloning](/api-reference/voices/voices-post#create-clone-voice).
* We released a new version of the Ultravox Model, [v0.4](https://github.com/fixie-ai/ultravox/releases/tag/v0.4).
* Tool support is coming very soon!


# Scaling & Call Concurrency
Source: https://docs.ultravox.ai/gettingstarted/concurrency

How to scale call volume with Ultravox.

<Info>
  <b>Call Concurrency `noun`</b>

  <br />

  The maximum number of simultaneous calls that your account can have active at any given moment.
</Info>

## 🔑 TL;DR

| Plan Type    | Concurrency Cap | Priority Access |
| ------------ | --------------- | --------------- |
| Free / PAYGO | 5 calls         | ❌               |
| Pro          | No hard cap\*   | ❌               |
| Scale        | No hard cap\*   | ✅ Up to 100     |

> \*Still subject to infra limits under extreme load.

## Call Concurrency in Ultravox Realtime

Ultravox works differently than most other voice AI platforms. Unlike other providers, we manage our own GPUs running the Ultravox model. This gives us granular control over the performance of our system. When you create a voice AI call on Ultravox Realtime, we dedicate GPU resources to your call for its entire lifespan. This allows us to keep your latency low and consistent, regardless of conversation length or traffic to our system.

In contrast, most voice AI providers rely on shared inference pools provided by LLM vendors. These systems queue each request and dynamically assign them to available GPUs, often using microbatching for efficiency. This leads to variable latency during the call and makes scaling reliably challenging.

If you're on a paid subscription plan, there are no hard caps on concurrency. If you're on the pay as you go model, there is a hard cap of 5 concurrent calls. Our goal is to dynamically match compute with demand, but during periods of extremely high load, it's possible that we might not have compute available to serve your call. When that happens, we'll issue an `HTTP 429` status code (“Too Many Request”) so you know to try again after a short wait.

This system is designed to help customers scale without having to overpay for concurrency. Most customers don't need the same amount of concurrency 24 hours a day. Ultravox Realtime is designed to scale with you, and we balance load with `429`s to keep the system fair for everyone. More on how to handle 429s [below](#managing-concurrency).

For customers that have high, sustained load, we offer [priority call concurrency](#priority-concurrency) on our Scale plan. We also offer dedicated capacity as part of our enterprise plans.

### Unbounded Concurrency

All accounts on a paid subscription enjoy no hard caps on call concurrency. This means not having to worry about paying for concurrency slots that are only needed occasionally for spikes in traffic. If the system is under load and we are unable to fulfill a request to create a call, you may receive a 429 "Too Many Requests" response. See [below](#keeping-the-pipe-full) for more on how to properly handle this.

### Priority Concurrency

Accounts on the Scale plan enjoy priority in the system for up to 100 concurrent calls (need even more? [contact us](mailto:sales@ultravox.ai?subject=Need%20More%20Concurrency) to discuss our enterprise agreements). This provides peace of mind for high impact inbound calls and ensuring that your most critical voice interactions are always available, even during peak system demand. If we are unable to create a call when an account is below its allotted priority call count, we will return a 503 "Service Unavailable" error. 429s are used if we are unable to fulfill new call requests above an account's priority call limit. See [below](#keeping-the-pipe-full) for more on how to properly handle 429s and 503s in your code.

### Hard Concurrency Caps

Ultravox Realtime accounts default to a hard cap on call concurrency. Any account not on a monthly or annual subscription is limited to five concurrent calls. Any attempt to create additional calls above the hard cap will result in an immediate HTTP 429 "Too Many Requests" response, allowing you to implement proper retry logic and queue management in your application. See [below](#keeping-the-pipe-full) for more on how to properly handle this.

## Managing Concurrency

If you encounter concurrency limits, proper handling in your application ensures a smooth user experience and optimal resource utilization. The key is implementing robust retry logic and monitoring your concurrent call usage.

### Example: Hitting the Cap

Let's consider an example where a pay-as-you-go account attempts to create multiple Ultravox calls over a short time:

| Time | Active Calls   | New Request   | Status     | Concurrent Count |
| ---- | -------------- | ------------- | ---------- | ---------------- |
| 0s   | -              | Create Call 1 | ✅ Success  | 1/5              |
| 2s   | Call 1         | Create Call 2 | ✅ Success  | 2/5              |
| 3s   | Call 1,2       | Create Call 3 | ✅ Success  | 3/5              |
| 4s   | Call 1,2,3     | Create Call 4 | ✅ Success  | 4/5              |
| 5s   | Call 1,2,3,4   | Create Call 5 | ✅ Success  | 5/5 (At Limit)   |
| 6s   | Call 1,2,3,4,5 | Create Call 6 | ❌ HTTP 429 | 5/5 (Rejected)   |
| 7s   | Call 2,3,4,5   | Create Call 7 | ❌ HTTP 429 | 5/5 (Rejected)   |
| 8s   | Call 2,3,5     | Create Call 8 | ✅ Success  | 4/5              |

### Keeping the Pipe Full

When you receive a 429 or 503 response, it's important to use `Retry-After` header to implement a proper retry strategy and avoid overwhelming the system. The `Retry-After` header is used to provide the number of seconds to wait before making any additional new requests.

Here's an example of how to do that with an exponential backoff + retry handling:

<Tabs>
  <Tab title="JavaScript">
    ```js Creating Calls with Retry Logic theme={null}
    async function createCallWithRetry(callConfig, maxRetries = 3) {
      for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
          const response = await fetch('https://api.ultravox.ai/api/calls', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(callConfig)
          });

          const retryAfter = response.headers.get('Retry-After');
          
          if (retryAfter) {
            const delay = parseInt(retryAfter) * 1000;
            console.log(`Retry-After header found. Retrying in ${delay/1000}s...`);
            await new Promise(resolve => setTimeout(resolve, delay));
            continue;
          }

          if (response.ok) {
            return await response.json();
          }
          
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        } catch (error) {
          if (attempt === maxRetries - 1) throw error;
          await new Promise(resolve => setTimeout(resolve, Math.pow(2, attempt) * 1000));
        }
      }
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python Creating Calls with Retry Logic theme={null}
    import time
    import requests
    from datetime import datetime
    from email.utils import parsedate_to_datetime

    def create_call_with_retry(call_config, max_retries=3):
        for attempt in range(max_retries):
            response = requests.post('https://api.ultravox.ai/calls', json=call_config)
            
            retry_after = response.headers.get('Retry-After')
            if retry_after:
                try:
                    delay = int(retry_after)
                except ValueError:
                    delay = (parsedate_to_datetime(retry_after) - datetime.utcnow()).total_seconds()
                
                print(f"Retry-After header found. Retrying in {delay:.1f} seconds...")
                time.sleep(delay)
                continue
            
            response.raise_for_status()
            return response.json()
    ```
  </Tab>
</Tabs>

### Outbound Call Scheduler (`Expected July 2025`)

Set it and forget it. You don't have to sweat the load or keep track of 429s. Leave that to us. Available to all accounts with a paid subscription.

**You Provide**

* Time window (e.g. tomorrow between 8am-5pm)
* List of destination phone numbers
* Desired agent to use for the calls

**We Handle**

* Queueing of all calls
* Load balancing
* Retries and 429 handling (these are fully abstracted)

**Use Cases**

* Marketing call campaigns
* Proactive customer service follow-ups
* High-volume appointment reminders


# Overview: Example Code
Source: https://docs.ultravox.ai/gettingstarted/examples

Explore working code examples and sample applications built with Ultravox.

Ready to see Ultravox in action? We've created a collection of working examples and sample apps to help you get started quickly and understand best practices for building with Ultravox.

## Ultravox Examples Repository

All our examples are available in the [**ultravox-examples**](https://github.com/fixie-ai/ultravox-examples) repository on GitHub, featuring:

* **Complete source code** for each example
* **Setup instructions** and requirements
* **Live demos** where applicable

Each example includes a README with instructions on how to setup and run the code.

[View Examples on GitHub →](https://github.com/fixie-ai/ultravox-examples)

## Your First Agent in Under 5 Minutes

<CardGroup>
  <Card title="I have a phone number ready" icon="phone" href="/gettingstarted/quickstart/telephony-outbound">
    Connect Ultravox to an outbound phone call
  </Card>

  <Card title="I want to test in browser first" icon="browser" href="/gettingstarted/quickstart/agent-console">
    Build a voice agent using the Ultravox console
  </Card>
</CardGroup>

## Need Help?

If you have questions about any of the examples or need help adapting them for your use case, please see [Getting Help](/gettingstarted/getting-help).


# Inbound Phone Calls
Source: https://docs.ultravox.ai/gettingstarted/examples/inbound-phone-call

Connect inbound phone calls to an AI agent in 6 minutes.

<Note>
  This is the full example of the [Inbound Call Quickstart](/gettingstarted/quickstart/telephony-inbound).
</Note>

This guide walks you through connecting inbound phone calls using Twilio to an Ultravox agent.

## Prerequisites

* Node.js 20 or higher
* A Twilio account with:
  * Account SID
  * Auth Token
  * Phone Number
* An Ultravox API key
* For incoming calls: A publicly accessible URL for your webhook (e.g., using ngrok)

## Set-up and Installation

<Steps>
  <Step title="Get the Source Code">
    Copy all the code locally from the [`twilio-inbound-quickstart-js`](https://github.com/fixie-ai/ultravox-examples/tree/main/telephony/twilio-inbound-quickstart-js) example.
  </Step>

  <Step title="Install the Required Dependencies">
    ```bash theme={null}
    pnpm install
    ```

    or

    ```bash theme={null}
    npm install
    ```
  </Step>
</Steps>

### Configure Twilio Webhook

<Steps>
  <Step title="Make Your Server Publicly Accessible">
    Use ngrok or a similar service to create a public URL for your local server:

    ```bash theme={null}
    ngrok http 3000
    ```
  </Step>

  <Step title="Set Up Webhook">
    1. Go to your Twilio Console
    2. Navigate to your phone number's configuration
    3. Under "Voice & Fax", set the webhook URL for incoming calls to:
       `https://your-ngrok-url/incoming`
  </Step>
</Steps>

### Update Configuration

The AI assistant will introduce itself as Steve and have a conversation with the recipient. You need to update the variable for the Ultravox API key. You may also (optionally) update the system prompt.

* `ULTRAVOX_API_KEY`: Your Ultravox API key
* `SYSTEM_PROMPT`: Instructions for the AI agent's behavior

```js Configuring Variables theme={null}
// Ultravox configuration
const ULTRAVOX_API_KEY = 'your_ultravox_api_key_here';
const SYSTEM_PROMPT = 'Your name is Steve. You are receiving a phone call. Ask them their name and see how they are doing.';
```

### Start the Server

Run the server:

```bash theme={null}
pnpm start
```

or

```bash theme={null}
npm start
```

Now, when someone calls your Twilio number, they'll be connected to your AI assistant.

## Next Steps

1. Check out the [Outbound Phone Call](/gettingstarted/examples/outbound-phone-call) example.
2. Ultravox Realtime provides telephony integrations for Telnyx, Twilio, Plivo, and Exotel. Learn more [here](/telephony/overview).

### Additional Resources

* [Twilio Documentation](https://www.twilio.com/docs)
* [Express.js Documentation](https://expressjs.com/)
* [ngrok Documentation](https://expressjs.com/)


# Outbound Phone Calls
Source: https://docs.ultravox.ai/gettingstarted/examples/outbound-phone-call

Connect outbound Twilio calls to an Ultravox agent in 5 minutes or less.

<Note>
  This is the full example of the [Outbound Call Quickstart](/gettingstarted/quickstart/telephony-outbound).
</Note>

This guide will help you set up and make your first automated call using Ultravox and Twilio.

## Prerequisites

* Node.js 20 or higher
* A Twilio account with:
  * Account SID
  * Auth Token
  * Phone Number
* An Ultravox API key

## Set-up and Installation

<Steps>
  <Step title="Get the Source Code">
    Copy all the code locally from the [`twilio-outbound-quickstart-js`](https://github.com/fixie-ai/ultravox-examples/tree/main/telephony/twilio-outbound-quickstart-js) example.
  </Step>

  <Step title="Install the Required Dependencies">
    ```bash theme={null}
    pnpm install
    ```

    or

    ```bash theme={null}
    npm install
    ```
  </Step>
</Steps>

## Making Your First Outbound Call

The AI assistant will introduce itself as Steve and have a conversation with the recipient. To make a call you need to update the variables for keys and phone numbers. You may also update the system prompt.

### Update Configuration

* `TWILIO_ACCOUNT_SID`: Your Twilio Account SID from the Twilio Console
* `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
* `TWILIO_PHONE_NUMBER`: The Twilio phone number to make calls from
* `DESTINATION_PHONE_NUMBER`: The recipient's phone number
* `ULTRAVOX_API_KEY`: Your Ultravox API key
* `SYSTEM_PROMPT`: Instructions for the AI agent's behavior

```js Configuring Variables theme={null}

// Twilio configuration
const TWILIO_ACCOUNT_SID = 'your_twilio_account_sid_here';
const TWILIO_AUTH_TOKEN = 'your_twilio_auth_token_here';
const TWILIO_PHONE_NUMBER = 'your_twilio_phone_number_here';
const DESTINATION_PHONE_NUMBER = 'the_destination_phone_number_here';

// Ultravox configuration
const ULTRAVOX_API_KEY = 'your_ultravox_api_key_here';
const SYSTEM_PROMPT = 'Your name is Steve and you are calling a person on the phone. Ask them their name and see how they are doing.';
```

### User Speaks First

By default, Ultravox Realtime defaults to having the agent speak first. This is exactly what you want for an inbound call you want the agent to answer. However, this is not what is wanted for outbound calls where someone can be expected to answer the call with something like "Hello".

When creating the call in Ultravox, you need to address this by setting the first speaker to user:

```js User speaks first theme={null}
const ULTRAVOX_CALL_CONFIG = {
    systemPrompt: SYSTEM_PROMPT,
    firstSpeakerSettings: { user: {} },     // For outgoing calls, the user will answer the call (i.e. speak first)
    medium: { twilio: {} }                  // Use twilio medium
};
```

### Start the Call

Once you've configured and saved everything, start the call:

```bash theme={null}
pnpm start
```

or

```bash theme={null}
npm start
```

## Next Steps

1. Check out the [Inbound Phone Call](/gettingstarted/examples/inbound-phone-call) example.
2. Ultravox Realtime provides telephony integrations for Telnyx, Twilio, Plivo, and Exotel. Learn more [here](/telephony/overview).


# FAQ
Source: https://docs.ultravox.ai/gettingstarted/faq

Answers to common questions

## Ultravox Web Console

### <Icon icon="circle-question" /> What is the web console?

Available at [https://app.ultravox.ai](https://app.ultravox.ai), the console provides:

* [Agent Builder](https://app.ultravox.ai/agents/new) → Build and view your existing voice agents. Blocky, our AI agent builder, is here to help you get started, iterate, and incorporate best-practices.
* [Dashboard](https://app.ultravox.ai/dashboard) → See charts for your usage along with views for the number of live calls happening for your account.
* [Call History](https://app.ultravox.ai/calls) → See all the details (timestamps, durations, summaries, full transcripts, and more) for every call that's been made in your account. Easily copy call IDs to use for troubleshooting or diving in deeper via the REST API.
* [Voices Explorer](https://app.ultravox.ai/voices) → Create custom voices and discover all the built-in voices your agents can use.
* [Tools](https://app.ultravox.ai/tools) → View, create, edit, and test agent [tools](/tools/overview).
* [RAG](https://app.ultravox.ai/rag) → Create and manage knowledge bases (we call them "corpora") that your agents can use to answer questions specific to your company, product, or topic.
* [Webhooks](https://app.ultravox.ai/webhooks) → Create and edit active [webhooks](/webhooks/overview) to drive integrations and automations.
* [Settings](https://app.ultravox.ai/settings) → Create and manage API keys to integrate your agents with your application, set custom TTS keys, and dive into billing and invoice details.

### <Icon icon="circle-question" /> What are "unlimited playground calls"?

These are calls that you make in the agent builder using the [web console application](#what-is-the-web-console). There is no charge for these calls and we encourage you to make use of this feature to thoroughly test your agents before deploying them.

## Billing

### <Icon icon="circle-question" /> How can I see my usage details? What about invoices?

The [Dashboard](https://app.ultravox.ai/dashboard) provides charts to see usage. [Call History](https://app.ultravox.ai/calls) gives granular details for each call and you can use the [REST API](https://docs.ultravox.ai/api-reference/introduction) to go even deeper.

View your [list of invoices](https://app.ultravox.ai/billing/invoices), click on one, and then click on "View invoice and payment details" to view details on your usage for the given billing period.

### <Icon icon="circle-question" /> When does Ultravox send out bills?

We send out monthly invoices to bill for usage (calls and SIP) in the prior period (AKA billing in arrears). If you are a Pro plan subscriber, we bill you at the beginning of each period to cover your subscription usage in advance.

Pay as you go (PAYGO) and Pro plan customers may also receive bills before the regular monthly cycle if usage exceeds the set threshold (`$10` for PAYGO, `$100` for Pro plan).

### <Icon icon="circle-question" /> How does Ultravox bill for calls that are less than a full minute?

Calls are rounded to the nearest "deciminute" (every six seconds). This means that we effectively bill our standard `$0.05` per minute rate as `$0.005` for every six seconds of call time. This chart provides some examples:

| Call Length (seconds) | Rounded To (seconds) | Billed Amount |
| --------------------- | -------------------- | ------------- |
| 0                     | 0                    | \$0.000       |
| 1                     | 6                    | \$0.005       |
| 12                    | 12                   | \$0.010       |
| 37                    | 42                   | \$0.035       |
| 55                    | 60                   | \$0.050       |

### <Icon icon="circle-question" /> Why is billing duration sometimes different than the length of the call recording?

When you choose to enable a recording for your call, the recording is force aligned with the user audio we receive. Billing duration is based on the clock that is running for the entire length of the call. Depending on your setup, there may be overhead incurred before Ultravox receives any user audio (this would mean billed duration > call recording).

Additionally, call summaries are generated in parallel with ending the call recording. This can add a couple of seconds of additional drift between recording length and billed duration.

Finally, all calls are rounded up to the [nearest deciminute.](#how-does-ultravox-bill-for-calls-that-are-less-than-a-full-minute)

<Warning>
  **Continuous PCM**

  Large duration mismatches typically indicate Ultravox didn't receive continuous user audio. Send continuous raw PCM (s16le) audio from your integration (e.g. websocket server).
</Warning>

## Miscellaneous

### <Icon icon="circle-question" /> How do I get my agent to best handle voicemail when making outgoing calls?

<Steps>
  <Step title="Use the `leaveVoicemail` tool">
    Ultravox provides the [built-in `leaveVoicemail` tool](/tools/built-in-tools#leavevoicemail) that the agent will use to leave a message and end the call. By default, the agent will dynamically create the message, or you can choose to override the message parameter with a pre-canned message if you prefer.

    ```js Overriding with a set message theme={null}

    {
      "selectedTools": [
        {
          "toolName": "leaveVoicemail",
          "parameterOverrides": {
            "message": "Hi, {{first_name}}. This is Anna from Acme Corporation. I'm calling because {{reason_for_call}}. Please give us a call back at your convenience. Thank you."
          }
        }
      ]
    }
    ```
  </Step>

  <Step title="Prompt the agent">
    Prompt the agent with explicit instructions on how you want voicemail handled. For example, to have the agent leave a message that was passed in via a [context variable](/agents/making-calls#template-context-and-variables) we could use the following:

    ```bash Sample Voicemail Prompt Instructions theme={null}
    <custom_voicemail_instructions>
    # Custom Voicemail Instructions

    If you encounter a voicemail, leave a message for {{first_name}} explaining you are calling about {{reason_for_call}}. Then invoke `hangUp` to end the call.

    </custom_voicemail_instructions>
    ```
  </Step>
</Steps>


# Getting Help
Source: https://docs.ultravox.ai/gettingstarted/getting-help

Connect with our community and get support for building voice AI agents

<Info>
  **Quick Help**: Join our [Discord community](https://discord.gg/62X253zeWB) where our team and fellow developers are ready to help!
</Info>

## Join Our Community

Questions? Need help? Just want to say hi? Join our [community on Discord](https://discord.gg/62X253zeWB). We're building more than just technology—we're building a community of innovators and creators who are reshaping the future of voice AI.

Our Discord community is the best place to:

* Get quick answers from our product and engineering team
* Connect with other developers building voice AI agents
* Share your projects and get feedback
* Stay updated on new features and announcements
* Participate in discussions about voice AI best practices

## Product Support & Enterprise Inquiries

For product support issues, billing questions, or inquiries about custom enterprise plans, reach out to us directly at:

**[hello@ultravox.ai](mailto:hello@ultravox.ai)**

Our team will get back to you promptly to help resolve any issues or discuss your specific needs.

## What to Include When Asking for Help

To help us assist you more effectively, please include:

1. **Description**: clear description of what you're trying to achieve
2. **Code snippets**: relevant code or configuration details (remove any API keys!)
3. **Error messages**: any errors or unexpected behavior you're experiencing
4. **Steps to reproduce**: details of the steps used to reproduce the issue (if applicable)

Whether you reach out on Discord or via email, we're here to help you build amazing voice AI experiences with Ultravox!


# How Ultravox Works
Source: https://docs.ultravox.ai/gettingstarted/how-ultravox-works

Understanding the core concepts and architecture of Ultravox Realtime

<Note>
  Ultravox powers millions of voice interactions monthly for companies ranging from YC startups to Fortune 500s.
</Note>

## Introduction

Ultravox Realtime enables you to build voice AI agents that work with your choice of telephony provider, with web or native apps, or in custom ways by using websockets and our native protocol. Built on our best-in-class open-weight model, Ultravox understands speech directly without relying on traditional ASR pipelines.

## What Makes Ultravox Different

<CardGroup>
  <Card title="No ASR = Real Understanding" icon="brain">
    Direct speech processing = faster responses + better context awareness.
  </Card>

  <Card title="Unlimited Scale" icon="infinity">
    No concurrency caps on paid plans.
  </Card>

  <Card title="BYOT" icon="plug">
    Bring Your Own Telephony. Total flexibility.
  </Card>

  <Card title="$0.05/min Enterprise Performance" icon="dollar-sign">
    Production-ready voice AI at an unbeatable price.
  </Card>
</CardGroup>

## Getting Started: Console vs API

### Ultravox Console (No-Code)

The [Ultravox Console](https://app.ultravox.ai) lets you quickly build and test agents without writing any code.

Perfect for:

* Experimenting with prompts and voices
* Testing agent behavior
* Rapid prototyping
* Getting familiar with Ultravox capabilities

[Explore Console →](https://app.ultravox.ai)

### API-First Platform

While the console is great for getting started, Ultravox is fundamentally an **API-first platform**. You should expect to write code to integrate voice agents into your applications.

Our REST API and SDKs give you complete control over:

* Dynamic agent configuration
* Custom tool integration
* Advanced call flows
* Production deployments
* Integrating voice AI into phone calls, web apps, and native apps

[Learn More →](/apps/overview)

## Core Architecture

<Note>
  **No ASR Pipeline**: Unlike traditional, component model voice AI systems, Ultravox understands speech directly. There's no automatic speech recognition (ASR) stage, making conversations faster and more context-aware. Context matters. We want Ultravox to hear the world as we hear it. This makes Ultravox faster and better at understanding than other systems that rely on ASR and speech to text.
</Note>

### Creating & Joining Calls

Every Ultravox interaction follows a simple pattern:

1. **Call Creation** → Configure and create calls via REST API
2. **Join Call** → Connect users through SDKs, telephony, or WebSockets

```mermaid theme={null}
graph LR
    A[REST API] -->|Create Call| B[Call Configuration]
    B -->|Returns joinUrl| C[Join Methods]
    C --> D[Client SDK]
    C --> E[Telephony Bridge]
    C --> F[WebSocket]
```

## Bring Your Own Telephony

Ultravox is designed as a **bring-your-own-telephony platform**, giving you complete flexibility in how you connect voice AI to your users (inbound or outbound). Whether you're using SIP trunking, Twilio, or any other telephony provider, Ultravox seamlessly integrates with your existing infrastructure.

[Learn More →](/telephony/overview)

## Key Principles

### 1. It's All About Prompting

Everything your agents do is based on the prompt instructions you give them. While it's tempting to write verbose prompts, focused instructions yield better results.

Remember:

* Tool names and descriptions are visible to the model
* Complex interactions may need multiple call stages
* Less is often more when it comes to instruction clarity

[Explore Prompting Guide →](/gettingstarted/prompting)

[Guiding Agents →](/agents/guiding-agents)

### 2. Tools Are Just Functions

Ultravox includes built-in tools and you can create custom tools. Tools (AKA function calling) give your agents superpowers—from accessing databases to making API calls. They're versatile, powerful, and straightforward to implement. Whether you're building customer support bots or sales agents, tools connect your AI to the real world.

At their core, tools are functions that agents can invoke to perform actions or retrieve information. Any functionality you can encapsulate in a function can be exposed to your agents as a tool. Addtionally, Ultravox automatically calls the underlying function so you don't have to sweat gluing things together.

[Learn More →](/tools/overview)

### 3. Speed and Affordability

Voice AI only works when conversations feel natural and fluid. No awkward pause.  No lag. Just smooth back-and-forth dialogue that feels human. Ultravox Realtime doesn't just meet this standard—it sets it.

#### Speed That Speaks for Itself

Don't take our word for it. [See the numbers](https://www.ultravox.ai/blog/ultravox-v0-5-taking-the-lead-in-speech-understanding) yourself for comparisons between Ultravox Realtime and other leading platforms. Our benchmarks tell a clear story: when it comes to real-time voice AI, speed matters, and we deliver.

#### Enterprise Performance. Consumer Prices.

At just \$0.05 per minute, Ultravox Realtime delivers enterprise-grade performance at consumer prices. Why? Because we believe groundbreaking technology should come with groundbreaking pricing. You can pay-as-you-go if you have commitment issues. We also have [paid plans](https://www.ultravox.ai/pricing) that remove all call concurrency caps so you can scale.

No hidden fees. Just straightforward rates that make premium voice AI accessible to everyone.

## Your First Agent in Under 5 Minutes

<CardGroup>
  <Card title="I have a phone number ready" icon="phone" href="/gettingstarted/quickstart/telephony-outbound">
    Connect Ultravox to an outbound phone call
  </Card>

  <Card title="I want to test in browser first" icon="browser" href="/gettingstarted/quickstart/agent-console">
    Build a voice agent using the Ultravox console
  </Card>
</CardGroup>

## Need Help?

<Info>
  **Still have questions?** Our engineering team hangs out in Discord and typically responds within minutes. See [Getting Help](/gettingstarted/getting-help).
</Info>


# Prompting Guide
Source: https://docs.ultravox.ai/gettingstarted/prompting

A guide to prompting for great voice AI experiences

## Introduction

As we say in the [How Ultravox Works](/gettingstarted/how-ultravox-works#key-principles) guide, it's all about prompting. Prompting is how we get Voice AI agents to do what we want, but all models work a little bit differently. Under the hood, the Realtime platform runs a version of the Ultravox model built on Llama 3.3 70B, so we recommend looking at the [Llama Prompting Guides](https://www.llama.com/docs/how-to-guides/prompting/) as a good starting point.

Below, we try to lay out the core patterns that we see working well at scale, but you'll probably need to customize these approaches based on your particular use case.

Remember that prompting is the most effective tool we have for controlling LLMs. In the majority of cases, the answer to "How do I get the model to do X?" is "You need to prompt it to do X."

> **Default Prompting Note:** Unlike many other Voice AI offerings, Ultravox does not append a default prompt to your input. This means that you should always provide a complete prompt, including any context or information that you want the model to consider. We do this to ensure you have full control over what the model does. We don't want anything hidden from view.

## Prompt As-If It's a Text-Based LLM

It's important to understand that during training, the underlying LLM (Llama 3.3 70B in our default case) is *frozen*. This means that you should prompt the model as though it's a text model. For most scenarios, we recommend telling the model at the top of your prompt that you're talking to it as a voice model.

Here's an example that works well:

```text Example: General Voice Prompt theme={null}
You are [Name], a friendly AI [customer service agent / helper / etc].
You're interacting with the user over voice, so speak casually.
Keep your responses short and to the point, much like someone would in dialogue. 
Since this is a voice conversation, do not use lists, bullets, emojis, or other 
things that do not translate to voice. In addition, do not use stage directions 
or otherwise engage in action-based roleplay (e.g., "(pauses), "*laughs").
```

## General Guidance

* **Start simple:** It's best to always start simple and then add complexity as needed. Begin by outlining in a few paragraphs what you want the model to do. Then have a chat with it, see where it needs work, and then iterate from there.

* **Be clear:** Llama is a very literal instruction follower. So if you want the model to do something, you need to be very clear about it. If you're trying to write a set of step-by-step flows, be sure to break them down into very clear, concise steps. Note that you don't HAVE to provide clear step-by-step instructions. General guidance works very well if you're looking for a more conversational output (but the model will exert more control in driving the conversation).

* **Use examples:** The model learns very well from examples. So after describing the high-level flow you want the model to follow, it can be helpful to provide a few examples of what you're looking for.

* **Iterate:** Prompting is an iterative process. You'll need to prompt the model, see how it does, and then adjust your prompts based on the results. It can take time to get things right, so be patient.

## Common Prompting Patterns

This section includes patterns and example prompts for dealing with common challenges.

### Tools

Tools are how your model interacts with the outside world, but you have to help the model understand when and how those [tools](/tools/overview) should be used. Here's a good pattern for prompting the model to use a tool:

<Steps>
  <Step title="Use Good Tool Definitions">
    It's critical to remember that the entire tool definition is seen by the LLM, and the LLM will use those definitions to guide its behavior. Make sure that your tool definitions are clear and concise.
  </Step>

  <Step title="Prompt for More Context">
    Give the LLM additional context or guidance on whenever the tool should be used. For example, if you want the model to look up information from an address book, you might add something like this to your prompt:

    ```text Example: Providing More Tool Context theme={null}
    You have access to an address book that contains personnel information. 
    If someone asks for information for a particular person, you MUST use 
    the lookUpAddressBook tool to find that information before replying.
    ```
  </Step>
</Steps>

### Numbers

Text to speech engines can sometimes have trouble with numbers, but we can help them by asking the LLM to output numbers in a more voice-friendly format. A pattern that we see that works well is to ask the LLM to separate numbers into individual digits, separated by a hyphen.

```text Example: Speaking Numbers theme={null}
Output account numbers, codes, or phone numbers as individual digits, 
separated by hyphens (e.g. 1234 → '1-2-3-4'). For decimals, 
say 'point' and then each digit (e.g., 3.14 → 'three point one four')."
```

### Dates & Times

Similar to numbers, dates and times can be tricky for speech generation, so it can be helpful to provide clearer guidance on how to produce the correct date/time format for effective speech generation.

```text Example: Reading Out Dates theme={null}
Output dates as individual components (e.g. 12/25/2022 → "December 
twenty-fifth twenty twenty-two"). For times, "10:00 AM" should be 
outputted as "10 AM". Read years naturally (e.g., 2024 → 'twenty 
twenty-four').
```

### Jailbreaks

Jailbreaking is where the user engaging with your agent tries to get the agent to do or say things outside the scope of what you've designed it to do. There is still no perfect system for preventing jailbreaking, but some simple prompting can make it much harder to jailbreak. Here's a simple pattern that works well:

```text Example: Minimizing Jailbreaking theme={null}
Your only job is to [primary job of your agent]. If someone asks you a question 
that is not related to [the thing you're asking the model to do], politely 
decline and redirect the conversation back to the task at hand.
```

### Creating More Natural Pauses

If you'd like to create more natural pauses, a simple but effective technique is to ask the model to add an ellipsis between sentences or after punctuation.

```text Example: Speaking with Pauses theme={null}
You want to speak slowly and clearly, so you must inject pauses between sentences. 
Do this by emitting "..." at the end of a sentence but before any final 
punctuation (e.g., “Wow, that's really interesting… can you tell me a bit more 
about that…?”. You should do this more when the topic is complex or requires 
special attention.
```

### Step-by-Step Instructions

Often times in customer support scenarios, you want the LLM to give instructions one at a time. You can achieve this by providing an example or two.

```text Example: Step-by-Step Help theme={null}
Example: User asks for help changing their password
- You will call the "searchArticle" tool
- Response from tool: {"content": "1. Click "Forgot Password" on the login screen 2. Enter your email address and click "Submit" 3. Check your email for the reset link 4. Click the link and enter your new password 5. Log in with your new password"}
- You will then use this information and proceed step-by-step with the user like this:
  * agent: "There are a few steps we need to go through."
  * agent: "The first step is Click on Forgot Password on the login screen. Let me know when you're there."
  * user: "OK done."
  * agent: "Great. next you need to enter your email address and click Submit."
  * user: "got it."
  * agent: "Now check your email for the reset link"
  * user: "uh huh."
- Repeat in this manner until you complete the entire process.
```

## Related Resources

* Learn how [Agents](/agents/overview) work and how to build them
* Check out the guide on [Guiding Agents](/agents/guiding-agents) to learn techniques for steering agents toward good experiences


# Agent Quickstart
Source: https://docs.ultravox.ai/gettingstarted/quickstart/agent-console

Create your first voice AI agent in 2 minutes with the Ultravox Console.

## Create Agent

<Steps>
  <Step title="Start with the Ultravox Console">
    Go to [Agents](https://app.ultravox.ai/agents).

    <img />

    <img />
  </Step>

  <Step title="Create a New Agent">
    Click on `New Agent` in the top right corner.
  </Step>

  <Step title="Enter a Name and Prompt">
    Copy & paste the following for the name of your agent:

    ```text theme={null}
    Hello_Steve
    ```

    Next, copy and paste this system prompt:

    ```text theme={null}
    Your name is Steve. You are a world-class conversationalist.
    Ask the person their name and then chat with them.
    ```

    <img />

    <img />
  </Step>

  <Step title="Choose a Voice">
    You can keep the default voice, or choose one of the dozens available.

    <img />

    <img />
  </Step>

  <Step title="Talk to Steve">
    Start a call with your agent by clicking the `Test Agent` button on the bottom right.

    Then use the `End Call` button to stop the call.

    <img />

    <img />
  </Step>
</Steps>

## Next Steps

1. Learn more about all the ways you can [customize agents](/agents/overview) in Ultravox
2. Connect your agent to [phone calls](/telephony/overview) or use it in a [web or native app](/apps/overview)
3. Create a [knowledge base](/tools/rag/overview) (AKA RAG) for your agent to give it specialized knowledge about your product or key topics


# Creating an API Key
Source: https://docs.ultravox.ai/gettingstarted/quickstart/apikeys

Generate authentication keys for REST API access and voice agent deployment.

<Info>If you don't have an Ultravox account, you can sign up at [https://app.ultravox.ai](https://app.ultravox.ai). All new accounts get 30 free minutes of call time.</Info>

API keys must be managed using the Ultravox console. Once you have created an API key, you can use the REST API.

<Steps>
  <Step title="Sign-In">
    Make sure you are signed into you account at [https://app.ultravox.ai](https://app.ultravox.ai)
  </Step>

  <Step title="Go to Settings">
    In the left nav, click on Settings. Or navigate to [https://app.ultravox.ai/settings/](https://app.ultravox.ai/settings/).

    <img />

    <img />
  </Step>

  <Step title="Click 'Generate New Key'">
    In the API Keys sections, click on "Generate New Key".

    <img />

    <img />
  </Step>

  <Step title="Name the Key and Save">
    Create a name for your new API key and create it. Make sure you save the key in a secure secrets manager.

    <img />

    <img />
  </Step>
</Steps>


# Inbound Call Quickstart
Source: https://docs.ultravox.ai/gettingstarted/quickstart/telephony-inbound

Connect inbound phone calls to an Ultravox agent in under 6 minutes.

## TL;DR

<Steps>
  <Step title="Steal this code">Save the following code locally as `index.js`.</Step>
  <Step title="Install twilio node library">Install `twilio` via `pnpm | npm install twilio`.</Step>
  <Step title="Install Express.js">Install `express` via `pnpm | npm install express`.</Step>
  <Step title="Configure variables">Add your Ultravox API key.</Step>
  <Step title="Start the server">Run it with `node index.js`.</Step>
  <Step title="Expose the endpoint">`ngrok http 3000`.</Step>
  <Step title="Configure incoming call webhook in Twilio">Set the value to `your_ngrok_url/incoming`.</Step>
  <Step title="Call your Twilio number">Call your Twilio number and it will be answered by Steve.</Step>
</Steps>

```js theme={null}
import express from 'express';
import https from 'https';
import twilio from 'twilio';

const app = express();
const port = 3000;

// ------------------------------------------------------------
// Step 1:  Configure Ultravox API key
//
// Optional:  Modify the system prompt
// ------------------------------------------------------------
const ULTRAVOX_API_KEY = 'your_ultravox_api_key_here';
const SYSTEM_PROMPT = 'Your name is Steve. You are receiving a phone call. Ask them their name and see how they are doing.';

// Ultravox configuration that will be used to create the call
const ULTRAVOX_CALL_CONFIG = {
    systemPrompt: SYSTEM_PROMPT,
    model: 'ultravox-v0.7',
    voice: 'Mark',
    temperature: 0.3,
    medium: { "twilio": {} }
};

// Ensure required configuration vars are set
function validateConfiguration() {
    const requiredConfig = [
        { name: 'ULTRAVOX_API_KEY', value: ULTRAVOX_API_KEY, pattern: /^[a-zA-Z0-9]{8}\.[a-zA-Z0-9]{32}$/ }
    ];

    const errors = [];

    for (const config of requiredConfig) {
        if (!config.value || config.value.includes('your_') || config.value.includes('_here')) {
            errors.push(`❌ ${config.name} is not set or still contains placeholder text`);
        } else if (config.pattern && !config.pattern.test(config.value)) {
            errors.push(`❌ ${config.name} format appears invalid`);
        }
    }

    if (errors.length > 0) {
        console.error('🚨 Configuration Error(s):');
        errors.forEach(error => console.error(`   ${error}`));
        console.error('\n💡 Please update the configuration variables at the top of this file:');
        console.error('   • ULTRAVOX_API_KEY should be 8 chars + period + 32 chars (e.g., Zk9Ht7Lm.wX7pN9fM3kLj6tRq2bGhA8yE5cZvD4sT)');
        return false;
    }

    console.log('✅ Configuration validation passed!');
    return true;
}

// Create Ultravox call and get join URL
async function createUltravoxCall() {
    const ULTRAVOX_API_URL = 'https://api.ultravox.ai/api/calls';
    const request = https.request(ULTRAVOX_API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-API-Key': ULTRAVOX_API_KEY
        }
    });

    return new Promise((resolve, reject) => {
        let data = '';
        request.on('response', (response) => {
            response.on('data', chunk => data += chunk);
            response.on('end', () => {
                try {
                    const parsedData = JSON.parse(data);
                    if (response.statusCode >= 200 && response.statusCode < 300) {
                        resolve(parsedData);
                    } else {
                        reject(new Error(`Ultravox API error (${response.statusCode}): ${data}`));
                    }
                } catch (parseError) {
                    reject(new Error(`Failed to parse Ultravox response: ${data}`));
                }
            });
        });
        request.on('error', (error) => {
            reject(new Error(`Network error calling Ultravox: ${error.message}`));
        });
        request.write(JSON.stringify(ULTRAVOX_CALL_CONFIG));
        request.end();
    });
}

// Handle incoming calls from Twilio
// Note: We have to expose this endpoint publicly (e.g. using ngrok in dev)
//       and set as incoming call webhook in Twilio
app.post('/incoming', async (req, res) => {
    try {
        console.log('📞 Incoming call received');
        
        // Validate configuration on each call
        if (!validateConfiguration()) {
            console.error('💥 Configuration validation failed for incoming call');
            const twiml = new twilio.twiml.VoiceResponse();
            twiml.say('Sorry, there was a configuration error. Please contact support.');
            res.type('text/xml');
            res.send(twiml.toString());
            return;
        }

        console.log('🤖 Creating Ultravox call...');
        const response = await createUltravoxCall();
        
        if (!response.joinUrl) {
            throw new Error('No joinUrl received from Ultravox API');
        }
        
        console.log('✅ Got Ultravox joinUrl:', response.joinUrl);

        const twiml = new twilio.twiml.VoiceResponse();
        const connect = twiml.connect();
        connect.stream({
            url: response.joinUrl,
            name: 'ultravox'
        });

        const twimlString = twiml.toString();
        console.log('📋 Sending TwiML response to Twilio');
        res.type('text/xml');
        res.send(twimlString);

    } catch (error) {
        console.error('💥 Error handling incoming call:');
        
        if (error.message.includes('Ultravox')) {
            console.error('   🤖 Ultravox API issue - check your API key and try again');
        } else if (error.message.includes('Authentication')) {
            console.error('   🔐 Authentication failed - check your Ultravox API key');
        } else {
            console.error(`   ${error.message}`);
        }
        
        console.error('\n🔍 Troubleshooting tips:');
        console.error('   • Double-check your ULTRAVOX_API_KEY configuration');
        console.error('   • Verify your Ultravox API key is valid and active');
        console.error('   • Check your internet connection');
        
        const twiml = new twilio.twiml.VoiceResponse();
        twiml.say('Sorry, there was an error connecting your call. Please try again later.');
        res.type('text/xml');
        res.send(twiml.toString());
    }
});

// Starts Express.js server to expose the /incoming route
function startServer() {
    console.log('🚀 Starting Inbound Ultravox Voice AI Phone Server...\n');
    
    // Check configuration on startup but don't exit - just warn
    const isConfigValid = validateConfiguration();
    if (!isConfigValid) {
        console.warn('⚠️  Server starting with invalid configuration.');
        console.warn('📞 Calls will fail until configuration is updated.\n');
    }

    app.listen(port, () => {
        console.log(`🎉 Server running successfully on port ${port}`);
        console.log(`📞 Ready to handle incoming calls at POST /incoming`);
        console.log(`🌐 Webhook URL: http://your-server:${port}/incoming`);
        console.log('\n💡 Setup reminder:');
        console.log('   • Configure your Twilio phone number webhook to point to this server');
        console.log('   • Make sure this server is accessible from the internet (consider using ngrok for testing)');
        if (!isConfigValid) {
            console.log('   • ⚠️  Update your ULTRAVOX_API_KEY before handling calls');
        }
    });
}

startServer();
```

## Next Steps

1. Check out the full [Inbound Phone Call](/gettingstarted/examples/inbound-phone-call) example for a fuller explanation of how to have incoming calls answered by an AI agent.
2. Ultravox Realtime provides telephony integrations for Telnyx, Twilio, Plivo, and Exotel. Learn more [here](/telephony/overview).


# Outbound Call Quickstart
Source: https://docs.ultravox.ai/gettingstarted/quickstart/telephony-outbound

Create an outbound voice AI call with Ultravox and Twilio in under 3 minutes.

## TL;DR

<Steps>
  <Step title="Steal this code">Save the following code locally as `index.js`.</Step>
  <Step title="Install twilio node library">Install `twilio` via `pnpm | npm install twilio`.</Step>
  <Step title="Configure variables">Add your Twilio account creds, phone numbers, and Ultravox API key.</Step>
  <Step title="Make the outbound phone call">Run it with `node index.js`.</Step>
</Steps>

```js theme={null}
import twilio from 'twilio';
import https from 'https';

// ------------------------------------------------------------
// Step 1:  Configure Twilio account and destination number
// ------------------------------------------------------------
const TWILIO_ACCOUNT_SID = 'your_twilio_account_sid_here';
const TWILIO_AUTH_TOKEN = 'your_twilio_auth_token_here';
const TWILIO_PHONE_NUMBER = 'your_twilio_phone_number_here';
const DESTINATION_PHONE_NUMBER = 'the_destination_phone_number_here';

// ------------------------------------------------------------
// Step 2:  Configure Ultravox API key
//
// Optional: Modify the system prompt
// ------------------------------------------------------------
const ULTRAVOX_API_KEY = 'your_ultravox_api_key_here';
const SYSTEM_PROMPT = 'Your name is Steve and you are calling a person on the phone. Ask them their name and see how they are doing.';

const ULTRAVOX_CALL_CONFIG = {
    systemPrompt: SYSTEM_PROMPT,
    model: 'ultravox-v0.7',
    voice: 'Mark',
    temperature: 0.3,
    firstSpeakerSettings: { user: {} },     // For outgoing calls, the user will answer the call (i.e. speak first)
    medium: { twilio: {} }                  // Use twilio medium
};

// Validates all required config vars are set
function validateConfiguration() {
    const requiredConfig = [
        { name: 'TWILIO_ACCOUNT_SID', value: TWILIO_ACCOUNT_SID, pattern: /^AC[a-zA-Z0-9]{32}$/ },
        { name: 'TWILIO_AUTH_TOKEN', value: TWILIO_AUTH_TOKEN, pattern: /^[a-zA-Z0-9]{32}$/ },
        { name: 'TWILIO_PHONE_NUMBER', value: TWILIO_PHONE_NUMBER, pattern: /^\+[1-9]\d{1,14}$/ },
        { name: 'DESTINATION_PHONE_NUMBER', value: DESTINATION_PHONE_NUMBER, pattern: /^\+[1-9]\d{1,14}$/ },
        { name: 'ULTRAVOX_API_KEY', value: ULTRAVOX_API_KEY, pattern: /^[a-zA-Z0-9]{8}\.[a-zA-Z0-9]{32}$/ }
    ];

    const errors = [];

    for (const config of requiredConfig) {
        if (!config.value || config.value.includes('your_') || config.value.includes('_here')) {
            errors.push(`❌ ${config.name} is not set or still contains placeholder text`);
        } else if (config.pattern && !config.pattern.test(config.value)) {
            errors.push(`❌ ${config.name} format appears invalid`);
        }
    }

    if (errors.length > 0) {
        console.error('🚨 Configuration Error(s):');
        errors.forEach(error => console.error(`   ${error}`));
        console.error('\n💡 Please update the configuration variables at the top of this file:');
        console.error('   • TWILIO_ACCOUNT_SID should start with "AC" and be 34 characters');
        console.error('   • TWILIO_AUTH_TOKEN should be 32 characters');
        console.error('   • Phone numbers should be in E.164 format (e.g., +1234567890)');
        console.error('   • ULTRAVOX_API_KEY should be 8 chars + period + 32 chars (e.g., Zk9Ht7Lm.wX7pN9fM3kLj6tRq2bGhA8yE5cZvD4sT)');
        console.error('\n📦 If you get module import errors, install dependencies with:');
        console.error('   npm install twilio');
        process.exit(1);
    }

    console.log('✅ Configuration validation passed!');
}

// Creates the Ultravox call using the above config
async function createUltravoxCall() {
    const ULTRAVOX_API_URL = 'https://api.ultravox.ai/api/calls';
    const request = https.request(ULTRAVOX_API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-API-Key': ULTRAVOX_API_KEY
        }
    });

    return new Promise((resolve, reject) => {
        let data = '';
        request.on('response', (response) => {
            response.on('data', chunk => data += chunk);
            response.on('end', () => {
                try {
                    const parsedData = JSON.parse(data);
                    if (response.statusCode >= 200 && response.statusCode < 300) {
                        resolve(parsedData);
                    } else {
                        reject(new Error(`Ultravox API error (${response.statusCode}): ${data}`));
                    }
                } catch (parseError) {
                    reject(new Error(`Failed to parse Ultravox response: ${data}`));
                }
            });
        });
        request.on('error', (error) => {
            reject(new Error(`Network error calling Ultravox: ${error.message}`));
        });
        request.write(JSON.stringify(ULTRAVOX_CALL_CONFIG));
        request.end();
    });
}

// Starts the program and makes the call
async function main() {
    console.log('🚀 Starting Outbound Ultravox Voice AI Phone Call...\n');
    validateConfiguration();
    
    try {
        console.log('📞 Creating Ultravox call...');
        const ultravoxResponse = await createUltravoxCall();
        
        if (!ultravoxResponse.joinUrl) {
            throw new Error('No joinUrl received from Ultravox API');
        }
        
        console.log('✅ Got Ultravox joinUrl:', ultravoxResponse.joinUrl);

        console.log('📱 Initiating Twilio call...');
        const client = twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN);
        
        const call = await client.calls.create({
            twiml: `<Response><Connect><Stream url="${ultravoxResponse.joinUrl}"/></Connect></Response>`,
            to: DESTINATION_PHONE_NUMBER,
            from: TWILIO_PHONE_NUMBER
        });

        console.log('🎉 Twilio outbound phone call initiated successfully!');
        console.log(`📋 Twilio Call SID: ${call.sid}`);
        console.log(`📞 Calling ${DESTINATION_PHONE_NUMBER} from ${TWILIO_PHONE_NUMBER}`);
        
    } catch (error) {
        console.error('💥 Error occurred:');
        
        if (error.message.includes('Authentication')) {
            console.error('   🔐 Authentication failed - check your Twilio credentials');
        } else if (error.message.includes('phone number')) {
            console.error('   📞 Phone number issue - verify your phone numbers are correct');
        } else if (error.message.includes('Ultravox')) {
            console.error('   🤖 Ultravox API issue - check your API key and try again');
        } else {
            console.error(`   ${error.message}`);
        }
        
        console.error('\n🔍 Troubleshooting tips:');
        console.error('   • Double-check all configuration values');
        console.error('   • Ensure phone numbers are in E.164 format (+1234567890)');
        console.error('   • Verify your Twilio account has sufficient balance');
        console.error('   • Check that your Ultravox API key is valid');
        console.error('   • If you get import errors, run: npm install twilio');
    }
}

main();
```

## Next Steps

1. Check out the full [Outbound Phone Call](/gettingstarted/examples/outbound-phone-call) example for a fuller explanation of how to do outbound voice AI calls.
2. Ultravox Realtime provides telephony integrations for Telnyx, Twilio, Plivo, and Exotel. Learn more [here](/telephony/overview).


# Tools Quickstart
Source: https://docs.ultravox.ai/gettingstarted/quickstart/tools

Learn how to start using built-in tools and how to create custom tools.

This quickstart contains two parts. This guide will use the [Ultravox Web App](https://app.ultravox.ai) but you can also use the [Ultravox API](/api-reference/introduction) if you prefer (not covered in this guide).

<CardGroup>
  <Card title="Part 1: Using the Built-in Hang Up Tool" icon="screwdriver-wrench" href="#using-the-built-in-hangup-tool">
    Add the `hangUp` tool so the agent can end the call at the right time.
  </Card>

  <Card title="Part 2: Creating a Custom Tool" icon="wand-magic-sparkles" href="#creating-a-custom-tool">
    Create a custom tool that retrieves information from a 3rd party API and provides the information to the user.
  </Card>
</CardGroup>

## Using the Built-in `hangUp` Tool

<Steps>
  <Step title="Start with the Ultravox Console">
    Go to [Agents](https://app.ultravox.ai/agents).

    <img />

    <img />
  </Step>

  <Step title="Create a New Agent">
    Click on `New Agent` in the top right corner.
  </Step>

  <Step title="Enter a Name and Prompt">
    Copy & paste the following for the name of your agent:

    ```text theme={null}
    Tools_Agent
    ```

    Next, copy and paste this system prompt:

    ```text theme={null}
    If the user says "Oklahoma" you must immediately call the 'hangUp' tool.
    ```
  </Step>

  <Step title="Add the hangUp Tool">
    Use the `Tools` drop-down and select the `hangUp` tool.

    <img />

    <img />
  </Step>

  <Step title="Save & Test the Agent">
    * Save the agent using the `Save` button. This agent will be used in part two of this quickstart.

    * Start a call with your agent by clicking the `Test Agent` button on the bottom right.

    * When you say the word "Oklahoma", the agent will call the tool and the call will end and you will see the call state change to `DISCONNECTED`.
  </Step>
</Steps>

## Creating a Custom Tool

<Info>
  This part uses the `Tools_Agent` we created above in [Using Built-in Tools](#using-built-in-tools).
</Info>

<Steps>
  <Step title="Create the getAdvice Tool">
    <img />

    <img />

    Under `Tools` click on [New Tool](https://app.ultravox.ai/tools/new). Set properties as follows and then click on `Save`:

    **Tool Name:**

    ```text theme={null}
    getAdvice
    ```

    **Description:**

    ```text theme={null}
    This tool provides random advice.
    ```

    **Custom Endpoint URL:**

    ```text theme={null}
    api.adviceslip.com/advice
    ```

    <Note>We are using the public adviceslip API as a quick example.</Note>
  </Step>

  <Step title="Edit Tools_Agent">
    * Go to [Agents](https://app.ultravox.ai/agents)
    * Click `...` on the right side of our `Tools_Agent`
    * Choose `Edit`
  </Step>

  <Step title="Add the getAdvice Tool">
    Use the `Tools` drop-down and select the `getAdvice` tool. You can keep the `hangUp` tool selected.
  </Step>

  <Step title="Update Prompt">
    Copy & paste the following for the system prompt:

    ```text theme={null}
    You are the world's best companion. You love talking to people.

    If someone asks for or needs advice, you must use the 'getAdvice' tool. 
    When you receive advice from the tool call, relay it back to the user.

    If the user says "Oklahoma" you must immediately call the 'hangUp' tool.
    ```
  </Step>

  <Step title="Save & Test the Agent">
    * Save the agent using the `Save` button.

    * Start a call with your agent by clicking the `Test Agent` button on the bottom right.

    * If you ask for advice, the agent will now use the tool to get random advice from the adviceslip API.

    * Saying "Oklahoma" will continue to trigger the hangUp tool.
  </Step>
</Steps>

## Next Steps

1. Learn more about [Built-in Tools](/tools/built-in-tools) you can use.
2. Dig into [HTTP vs. Client Tools](/tools/custom/http-vs-client-tools) to understand the differences.
3. Read about [Durable vs. Temp Tools](/tools/custom/durable-vs-temporary-tools).


# Web Quickstart
Source: https://docs.ultravox.ai/gettingstarted/quickstart/web-app

Create calls with an agent in the browser in under 2 minutes

<Danger>
  This quickstart uses [X-Unsafe-API-Key](/api-reference/introduction#x-api-key-header) which is not safe for production.

  See the [nextjs-ts](https://github.com/fixie-ai/ultravox-examples/tree/main/web/nextjs-ts) example for a more robust example.
</Danger>

## TL;DR

<Steps>
  <Step title="Steal this code">Save the following code locally as `index.html`.</Step>
  <Step title="Open in browser">Open `index.html` in your browser.</Step>
  <Step title="Add API key">Add your Ultravox API key.</Step>
  <Step title="Start call">Click the button.</Step>
</Steps>

```html theme={null}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ultravox Web Quickstart</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-gray-100 min-h-screen py-8">
  <div class="max-w-4xl mx-auto px-4">
    <div class="bg-white rounded-lg shadow-lg p-6">
      <!-- WARNING: DO NOT USE IN PRODUCTION -->
      <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-6">
        <div class="flex">
          <div class="flex-shrink-0 fas fa-exclamation-triangle text-yellow-400"></div>
          <div class="ml-3">
            <h3 class="text-sm text-yellow-800">DEVELOPMENT ONLY - DO NOT USE IN PRODUCTION</h3>
            <p class="mt-1 text-sm text-yellow-700">This interface exposes API keys in client-side code and uses unsafe headers to bypass CORS.</p>
            <p class="mt-1 text-sm text-yellow-700">For a robust example, see the <a href="https://github.com/fixie-ai/ultravox-examples/tree/main/web/nextjs-ts">nextjs-ts</a> example.</p>
          </div>
        </div>
      </div>
      <form class="space-y-6">
        <div class="bg-gray-50 rounded-lg p-4">
          <h3 class="text-sm text-gray-900 mb-2">Call Status</h3>
          <div id="callStatus" class="text-sm text-gray-600">Ready</div>
        </div>
        <div>
          <label for="apiKey" class="block text-sm text-gray-700 mb-2">Ultravox API Key:</label>
          <input type="password" id="apiKey" 
            class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            placeholder="Enter your Ultravox API key">
          <p class="mt-1 text-sm text-gray-500">Your API key will be used to create the call. Keep this secure!</p>
        </div>
        <div>
          <label for="systemPrompt" class="block text-sm text-gray-700 mb-2">System Prompt:</label>
          <textarea id="systemPrompt" rows="3" 
            class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            placeholder="Enter system prompt for the AI assistant">You are a helpful assistant.</textarea>
          <p class="mt-1 text-sm text-gray-500">This prompt will define how the AI assistant behaves during the call.</p>
        </div>
        <div class="flex space-x-3">
          <button type="button" id="startCall"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm rounded-md shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 transition-colors">
            Start Call
          </button>
          <button type="button" id="endCall"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm rounded-md shadow-sm text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors">
            End Call
          </button>
        </div>
      </form>
    </div>
  </div>
  <script type="module">
    import { UltravoxSession } from 'https://esm.sh/ultravox-client@0.3.6';
    
    let uvSession = new UltravoxSession();
    
    function appendUpdate(target, message) {
        const updateTarget = document.getElementById(target);
        if(target === 'callTranscript') {
            let transcriptText = '';
            message.map((transcript, index) => (
                transcriptText += '<div class="p-2 bg-gray-50 rounded border-l-4 border-blue-400"><span class="font-semibold text-gray-800">' + transcript.speaker + ':</span> <span class="text-gray-700">' + transcript.text + '</span></div>'
            ));
            updateTarget.innerHTML = transcriptText;
            updateTarget.scrollTop = updateTarget.scrollHeight;
        } else {
            updateTarget.innerHTML = message;
        }
    }
    
    // ⚠️ WARNING: DO NOT USE IN PRODUCTION! ⚠️
    // This function makes API calls directly from the client with API keys exposed
    // API keys should never be handled in client-side code in production
    // In production, API calls should be made from a secure server
    // Here we are using unsafe API endpoint to bypass CORS - this is a security risk
    async function createCall(apiKey, systemPrompt) {
      try {
        appendUpdate('callStatus', '<span class="text-blue-600">Creating call...</span>');
        
        const payload = {
          temperature: 0.3,
          systemPrompt: systemPrompt
        };
        
        console.log('Creating call with payload:', payload);
        
        // ⚠️ WARNING: X-Unsafe-API-Key header is used to bypass CORS ⚠️
        // This is NOT secure and should NEVER be used in production
        const response = await fetch('https://api.ultravox.ai/api/calls', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-Unsafe-API-Key': apiKey  // ⚠️ UNSAFE - DO NOT USE IN PROD ⚠️
          },
          body: JSON.stringify(payload)
        });
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const callData = await response.json();
        console.log('Call created successfully:', callData);
        
        return callData.joinUrl;
          
      } catch (error) {
          console.error('Error creating call:', error);
          appendUpdate('callStatus', `<span class="text-red-600">Error creating call: ${error.message}</span>`);
          throw error;
      }
    }
    
    // Start Call button click event handler
    document.getElementById('startCall').onclick = async function() {
      const apiKey = document.getElementById('apiKey').value;
      const systemPrompt = document.getElementById('systemPrompt').value || 'You are a helpful assistant.';
      
      if (!apiKey) {
        appendUpdate('callStatus', '<span class="text-red-600">Please enter your Ultravox API key</span>');
        return;
      }
      
      try {
        const joinUrl = await createCall(apiKey, systemPrompt);
        
        if (!joinUrl) {
          appendUpdate('callStatus', '<span class="text-red-600">Failed to get join URL from API</span>');
          return;
        }
        
        appendUpdate('callStatus', '<span class="text-blue-600">Joining call...</span>');
        
        uvSession.addEventListener('status', (event) => {
          let statusClass = 'text-blue-600';
          if (uvSession.status === 'connected') statusClass = 'text-green-600';
          if (uvSession.status === 'disconnected') statusClass = 'text-gray-600';
          appendUpdate('callStatus', `<span class="${statusClass}">Session status: ${uvSession.status}</span>`);
        });
        
        uvSession.joinCall(joinUrl);
          
      } catch (error) {
          appendUpdate('callStatus', `<span class="text-red-600">Failed to start call: ${error.message}</span>`);
      }
    };
    
    // End Call button click event handler
    document.getElementById('endCall').onclick = async function() {
      appendUpdate('callStatus', '<span class="text-yellow-600">Ending call...</span>');
      uvSession.leaveCall();
    };
  </script>
</body>
</html>
```

## Next Steps

1. Check out the [nextjs-ts](https://github.com/fixie-ai/ultravox-examples/tree/main/web/nextjs-ts) example for a more complete, production ready web app.


# Voximplant
Source: https://docs.ultravox.ai/integrations/voximplant

Connecting Ultravox to SIP Using Voximplant

<Note>
  Voximplant provides a platform for telephony and has created a native integration with Ultravox to enable SIP calling. This content has been provided courtesy of Voximplant.
</Note>

## Connecting to SIP Trunk with Voximplant

With Voximplant, you can connect Ultravox Realtime to an existing SIP telephony server. This allows you to use Ultravox AI assistants to handle your calls and assist your customers right from your existing infrastructure.

Voximplant acts as a gateway, managing connections with Ultravox via WebSockets and making/receiving calls via SIP.

```mermaid theme={null}
graph LR
    A[AI \n agent] <-->|WebSockets| B((Voximplant \n Cloud))
    B <-->|PSTN| C[Phone \n Network]
    B <-->|SIP Trunk| D[VoIP \n Infrastructure]
    B <-->|WebRTC| E[SDK]

    classDef cloud fill:#a881f7,stroke:#a881f7,shape:cloud;
    class B cloud

    %%Highlight SIP
    linkStyle 2 stroke:#a881f7,stroke-width:6px;

```

Follow the steps below to connect Ultravox to your SIP PBX server.

### Step 1: Create a Voximplant Application

To create an application, [log in to your Voximplant account](https://manage.voximplant.com/?utm_source=docs\&utm_medium=applications\&utm_campaign=gettingstarted) or create a new one. Then, navigate to the [application section](https://manage.voximplant.com/applications?utm_source=docs\&utm_medium=applications\&utm_campaign=gettingstarted) from the upper left corner of the page. Click **New application** in the upper right corner or **Create** at the bottom of the page.

<img alt="Create an application" />

This opens a new application editor window where you can set it up and save by clicking **Create**. The newly created app appears in the application list. To modify its name, icon, or description, click the three dots menu and select **Edit**.

<img alt="Edit an application" />

You can learn more about Voximplant applications and their sections in the [Getting started → Applications](https://voximplant.com/docs/getting-started/basic-concepts/applications) section of their documentation.

### Step 2: Create Scenarios Within the Application

Scenarios in Voximplant are JavaScript documents within a Voximplant application, where you can implement logic processing calls and messages.

To create a scenario, open your existing or newly created [application](https://voximplant.com/docs/getting-started/basic-concepts/applications), select **Scenarios** on the left menu, and click on the plus icon to create a new scenario. Give it a name.

<img alt="Create a scenario" />

This opens a new tab in the online IDE on the right, where you can write your code. If needed, you can rename the scenario or modify the source code later.

You can learn more about scenarios and their best practice tips in the [Getting started → Scenarios](https://voximplant.com/docs/getting-started/basic-concepts/scenarios) section of the Voximplant documentation.

### Step 3: Utilize Ready-to-use Scenarios

To connect your SIP PBX with Ultravox, Voximplant prepared two ready-to use scenarios for incoming and outgoing calls.

<Info>
  **Please note**: We have hidden sensitive information in these scenarios, such as API keys, with placeholders. Please, replace the placeholders with your actual Ultravox credentials.
</Info>

Here is the `incoming` scenario for processing incoming calls forwarded to Voximplant:

```js theme={null}
require(Modules.Ultravox);

VoxEngine.addEventListener(AppEvents.CallAlerting, async ({ call }) => {
  let webSocketAPIClient = undefined;

  call.answer();
  const callBaseHandler = () => {
    if (webSocketAPIClient) webSocketAPIClient.close();
    VoxEngine.terminate();
  };
  call.addEventListener(CallEvents.Disconnected, callBaseHandler);
  call.addEventListener(CallEvents.Failed, callBaseHandler);

  const onWebSocketClose = (event) => {
    Logger.write('===ON_WEB_SOCKET_CLOSE==');
    Logger.write(JSON.stringify(event));
    VoxEngine.terminate();
  };

  const ULTRAVOX_API_KEY = 'YOUR_ULTRAVOX_API_KEY';
  const AUTHORIZATIONS = {
    'X-API-Key': ULTRAVOX_API_KEY,
  };

  const MODEL = 'ultravox-v0.7';
  const VOICE_NAME = 'Mark';
  const PATH_PARAMETERS = {};

  // Use this object when Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
  const PATH_PARAMETERS_AGENT_CALL = {agent_id: "YOUR-AGENT-ID"};

  const QUERY_PARAMETERS = {};
  const BODY_CREATE_CALL = {
    systemPrompt: 'You are a helpful assistant',
    model: MODEL,
    voice: VOICE_NAME,
  };

  // Use this object when Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
  const BODY_CREATE_AGENT_CALL = {
  };

  const webSocketAPIClientParameters = {
    // or Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
    endpoint: Ultravox.HTTPEndpoint.CREATE_CALL, // Change for agent call
    authorizations: AUTHORIZATIONS,
    pathParameters: PATH_PARAMETERS, // Change for agent call
    queryParameters: QUERY_PARAMETERS,
    body: BODY_CREATE_CALL, // Change for agent call
    onWebSocketClose,
  };

  try {
    webSocketAPIClient = await Ultravox.createWebSocketAPIClient(webSocketAPIClientParameters);
    VoxEngine.sendMediaBetween(call, webSocketAPIClient);

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Unknown, (event) => {
      Logger.write('===Ultravox.WebSocketAPIEvents.Unknown===');
      Logger.write(JSON.stringify(event));
    });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.HTTPResponse, (event) => {
      Logger.write('===Ultravox.WebSocketAPIEvents.HTTPResponse===');
      Logger.write(JSON.stringify(event));
    });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.State, (event) => {
      Logger.write('===Ultravox.WebSocketAPIEvents.State===');
      Logger.write(JSON.stringify(event));
    });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Transcript, (event) => {
      Logger.write('===Ultravox.WebSocketAPIEvents.Transcript===');
      Logger.write(JSON.stringify(event));
    });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.ClientToolInvocation, (event) => {
      Logger.write('===Ultravox.WebSocketAPIEvents.ClientToolInvocation===');
      Logger.write(JSON.stringify(event));
    });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Debug, (event) => {
      Logger.write('===Ultravox.WebSocketAPIEvents.Debug===');
      Logger.write(JSON.stringify(event));
    });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.PlaybackClearBuffer, (event) => {
      Logger.write('===Ultravox.WebSocketAPIEvents.PlaybackClearBuffer===');
      Logger.write(JSON.stringify(event));
      if (webSocketAPIClient) webSocketAPIClient.clearMediaBuffer();
    });

    const userTextMessageContent = {
      type: 'user_text_message',
      text: 'HI!',
    };
    webSocketAPIClient.inputTextMessage(userTextMessageContent);
  } catch (error) {
    Logger.write('===SOMETHING_WENT_WRONG===');
    Logger.write(error);
    VoxEngine.terminate();
  }
});
```

Here is the `outgoing` scenario for processing outgoing calls:

```js theme={null}
require(Modules.Ultravox);

VoxEngine.addEventListener(AppEvents.Started, async () => {
  let webSocketAPIClient = undefined;
  //Obtain parameters passed to call
  const customData = JSON.parse(VoxEngine.customData());

  const call = VoxEngine.callSIP(`sip:${customData["number"]}@sip.example.org`,customData["callerid"]);

  const callBaseHandler = () => {
    if (webSocketAPIClient) webSocketAPIClient.close();
    VoxEngine.terminate();
  };
  call.addEventListener(CallEvents.Disconnected, callBaseHandler);
  call.addEventListener(CallEvents.Failed, callBaseHandler);

  call.addEventListener(CallEvents.Connected, async () => {

    const onWebSocketClose = (event) => {
        Logger.write('===ON_WEB_SOCKET_CLOSE==');
        Logger.write(JSON.stringify(event));
        VoxEngine.terminate();
      };

    const ULTRAVOX_API_KEY = 'YOUR_ULTRAVOX_API_KEY';
      const AUTHORIZATIONS = {
        'X-API-Key': ULTRAVOX_API_KEY,
      };

      const MODEL = 'ultravox-v0.7';
      const VOICE_NAME = 'Mark';
      const PATH_PARAMETERS = {};

    // Use this object when Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
      const PATH_PARAMETERS_AGENT_CALL = {agent_id: "YOUR-AGENT-ID"};

    const QUERY_PARAMETERS = {};
      const BODY_CREATE_CALL = {
        systemPrompt: 'You are a helpful assistant',
        model: MODEL,
        voice: VOICE_NAME,
      };

    // Use this object when Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
      const BODY_CREATE_AGENT_CALL = {
      };

    const webSocketAPIClientParameters = {
        // or Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
        endpoint: Ultravox.HTTPEndpoint.CREATE_CALL, // Change for agent call
        authorizations: AUTHORIZATIONS,
        pathParameters: PATH_PARAMETERS, // Change for agent call
        queryParameters: QUERY_PARAMETERS,
        body: BODY_CREATE_CALL, // Change for agent call
        onWebSocketClose,
      };

    try {
        webSocketAPIClient = await Ultravox.createWebSocketAPIClient(webSocketAPIClientParameters);
        VoxEngine.sendMediaBetween(call, webSocketAPIClient);

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Unknown, (event) => {
          Logger.write('===Ultravox.WebSocketAPIEvents.Unknown===');
          Logger.write(JSON.stringify(event));
        });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.HTTPResponse, (event) => {
          Logger.write('===Ultravox.WebSocketAPIEvents.HTTPResponse===');
          Logger.write(JSON.stringify(event));
        });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.State, (event) => {
          Logger.write('===Ultravox.WebSocketAPIEvents.State===');
          Logger.write(JSON.stringify(event));
        });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Transcript, (event) => {
          Logger.write('===Ultravox.WebSocketAPIEvents.Transcript===');
          Logger.write(JSON.stringify(event));
        });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.ClientToolInvocation, (event) => {
          Logger.write('===Ultravox.WebSocketAPIEvents.ClientToolInvocation===');
          Logger.write(JSON.stringify(event));
        });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Debug, (event) => {
          Logger.write('===Ultravox.WebSocketAPIEvents.Debug===');
          Logger.write(JSON.stringify(event));
        });

    webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.PlaybackClearBuffer, (event) => {
          Logger.write('===Ultravox.WebSocketAPIEvents.PlaybackClearBuffer===');
          Logger.write(JSON.stringify(event));
          if (webSocketAPIClient) webSocketAPIClient.clearMediaBuffer();
        });

    const userTextMessageContent = {
          type: 'user_text_message',
          text: 'HI!',
        };
        webSocketAPIClient.inputTextMessage(userTextMessageContent);
      } catch (error) {
        Logger.write('===SOMETHING_WENT_WRONG===');
        Logger.write(error);
        VoxEngine.terminate();
      }
    });
});
```

The outgoing scenario accepts the `customData` parameter in the following format:

```js theme={null}
{"callerid":"16503333333", "number":"16504444444"}
```

You can provide this parameter when launching the scenario via a **routing rule** or [StartScenarios](https://voximplant.com/docs/references/httpapi/scenarios#startscenarios) Management API method.

### Step 4: Create Routing Rules

Routing rules in a Voximplant application define when and how to launch existing scenarios. When an incoming call arrives or you make call via your SIP PBX server, a routing rule decides which scenario to launch.

To create a routing rule, navigate to the **Routing** tab in your [application](https://voximplant.com/docs/getting-started/basic-concepts/applications). You can either click **Create** in the center of the screen or **New rule** in the upper right corner:

<img alt="Create a rule" />

This opens the **New rule** editor, where you can specify the rule name, properties, and attach one or more scenarios:

<img alt="New rule editor" />

If you intend to use the scenario for video conferencing, enable the **Video conference** switch. Without this parameter, all video conferences fail with an error.

Disable the **Video conference** switch, as you do not plan to use the scenario as a video conference.

The **Pattern** field checks if the call’s destination (the dialed number or username specified in the `e.destination` property of the incoming call) matches any rule’s pattern. If the call’s destination aligns with the pattern, the attached scenario(s) are executed. If the call’s destination doesn’t match the pattern, the attached scenario(s) remain inactive, and the call proceeds to the next routing rule.

The application systematically evaluates the routing rules from top to bottom, with higher-priority rules taking precedence. When the call’s destination matches one of the rules, the rule is executed, and the application disregards any subsequent rules, ensuring that only one rule is executed at a time.

<Info>
  **Note**: If the destination phone number meets several rules' patterns, only **the first rule** executes.
</Info>

The **Pattern** field employs regular expressions to create masks for phone numbers or usernames. Common expressions include:

* `.*` means any quantity of any symbols, so all the numbers or usernames match the rule.
* `+?[1-9]\d{1,14}` matches any phone number
* `123.+` matches 1234, 12356, and so on.

For more information on building regular expressions, refer to [Wikipedia](https://en.wikipedia.org/wiki/Regular_expression).

The **Available scenarios** dropdown list enables you to attach one or more scenarios to execute when the rule is triggered.

You can attach **multiple scenarios** to a single rule. In this scenario, the rule executes all the attached scenarios sequentially within a single context, promoting code reuse. This allows you to encapsulate all the functions within a scenario and utilize them in another scenario.

You can view all the attached scenarios in the **Assigned scenarios** field.

After specifying all the settings, click the **Create rule** button to create a rule.

You can learn more about routing rules and ways to launch them in the [Getting started → Routing rules](https://voximplant.com/docs/getting-started/basic-concepts/applications) section of the Voximplant documentation.

## Configure Your SIP PBX

Your configuration depends on the type of the PBX that you use and internet access that it has.

### Using an Internet-Connected, Self-Hosted PBX with Fixed Public IP

In this case you need to:

1. Whitelist the IP address of your PBX in the [Secrity](https://manage.voximplant.com/settings/security/white_list) section of Voximplant Control Panel.
2. Configure your PBX to forward calls to the following SIP URI: sip:@..voximplant.com. `number` may be any number or username that matches the regular expression specified earlier when configuring the routing rules. `app_name` and `account_name` are the names of the Voximplant application and account respectively.

### Using a Cloud PBX

In this case, Voximplant can resemble a user in your cloud PBX. To complete the configuration you need to:

1. Create a user in your cloud PBX account.
2. Configure your PBX to forward calls that need to be handled by the voice bot to the user you have just created.
3. Create a [SIP registration](https://manage.voximplant.com/settings/sip_registrations) with credentials of the created user and the domain name of the cloud PBX instance you use.
4. Attach the SIP registration to the application in `SIP registations` section of application configuration. When doing so, select the routing rule for incoming calls created earlier.

## Making Outgoing Calls

Voximplant can initiate outgoing calls to your PBX and join them to the voice agent. This can be done by calling the [StartScenarios](https://voximplant.com/docs/references/httpapi/scenarios#startscenarios) Management API method from your system and passing the number and caller ID parameters as it is explained below.

### Configuring Your Voximplant Account

<Steps>
  <Step>
    Create an application the same way as [described above](#step-1%3A-create-a-voximplant-application).
  </Step>

  <Step>
    Create a call scenario. Here is the sample scenario for starting outgoing calls. Please note that Ultravox and PBX connection information need to be provided in the script instead of placeholders.

    ```js theme={null}
    require(Modules.Ultravox);

    VoxEngine.addEventListener(AppEvents.Started, async () => {
      let webSocketAPIClient = undefined;
      // Obtain parameters passed to call
      const customData = JSON.parse(VoxEngine.customData());

      const call = VoxEngine.callSIP(`sip:${customData["number"]}@YOUR_PBX_ADDRESS`,customData["callerid"]);

      const callBaseHandler = () => {
        if (webSocketAPIClient) webSocketAPIClient.close();
        VoxEngine.terminate();
      };
      call.addEventListener(CallEvents.Disconnected, callBaseHandler);
      call.addEventListener(CallEvents.Failed, callBaseHandler);

      call.addEventListener(CallEvents.Connected, async () => {

        const onWebSocketClose = (event) => {
            Logger.write('===ON_WEB_SOCKET_CLOSE==');
            Logger.write(JSON.stringify(event));
            VoxEngine.terminate();
          };

        const ULTRAVOX_API_KEY = 'YOUR_ULTRAVOX_API_KEY';
          const AUTHORIZATIONS = {
            'X-API-Key': ULTRAVOX_API_KEY,
          };

          const MODEL = 'ultravox-v0.7';
          const VOICE_NAME = 'Mark';
          const PATH_PARAMETERS = {};

        // Use this object when Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
          const PATH_PARAMETERS_AGENT_CALL = {agent_id: "YOUR-AGENT-ID"};

        const QUERY_PARAMETERS = {};
          const BODY_CREATE_CALL = {
            systemPrompt: 'You are a helpful assistant',
            model: MODEL,
            voice: VOICE_NAME,
          };

        // Use this object when Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
          const BODY_CREATE_AGENT_CALL = {
          };

        const webSocketAPIClientParameters = {
            // or Ultravox.HTTPEndpoint.CREATE_AGENT_CALL
            endpoint: Ultravox.HTTPEndpoint.CREATE_CALL, // Change for agent call
            authorizations: AUTHORIZATIONS,
            pathParameters: PATH_PARAMETERS, // Change for agent call
            queryParameters: QUERY_PARAMETERS,
            body: BODY_CREATE_CALL, // Change for agent call
            onWebSocketClose,
          };

        try {
            webSocketAPIClient = await Ultravox.createWebSocketAPIClient(webSocketAPIClientParameters);
            VoxEngine.sendMediaBetween(call, webSocketAPIClient);

        webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Unknown, (event) => {
              Logger.write('===Ultravox.WebSocketAPIEvents.Unknown===');
              Logger.write(JSON.stringify(event));
            });

        webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.HTTPResponse, (event) => {
              Logger.write('===Ultravox.WebSocketAPIEvents.HTTPResponse===');
              Logger.write(JSON.stringify(event));
            });

        webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.State, (event) => {
              Logger.write('===Ultravox.WebSocketAPIEvents.State===');
              Logger.write(JSON.stringify(event));
            });

        webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Transcript, (event) => {
              Logger.write('===Ultravox.WebSocketAPIEvents.Transcript===');
              Logger.write(JSON.stringify(event));
            });

        webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.ClientToolInvocation, (event) => {
              Logger.write('===Ultravox.WebSocketAPIEvents.ClientToolInvocation===');
              Logger.write(JSON.stringify(event));
            });

        webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.Debug, (event) => {
              Logger.write('===Ultravox.WebSocketAPIEvents.Debug===');
              Logger.write(JSON.stringify(event));
            });

        webSocketAPIClient.addEventListener(Ultravox.WebSocketAPIEvents.PlaybackClearBuffer, (event) => {
              Logger.write('===Ultravox.WebSocketAPIEvents.PlaybackClearBuffer===');
              Logger.write(JSON.stringify(event));
              if (webSocketAPIClient) webSocketAPIClient.clearMediaBuffer();
            });

        const userTextMessageContent = {
              type: 'user_text_message',
              text: 'HI!',
            };
            webSocketAPIClient.inputTextMessage(userTextMessageContent);
          } catch (error) {
            Logger.write('===SOMETHING_WENT_WRONG===');
            Logger.write(error);
            VoxEngine.terminate();
          }
        });
    });
    ```
  </Step>

  <Step>
    Create a routing rule and attach the scenario to it. The rule pattern can be arbitrary in this case because the pattern is only used when processing incoming calls.
  </Step>
</Steps>

### Configure your PBX

You can either whitelist the Voximplant SIP IP addresses or create a user in your PBX and use those credentials to authenticate. In the first case you can use the [API endpoint](http://api.voximplant.com/getMediaResources?with_sbcs) to get Voximplant SIP IP addresses. In the latter case you need to pass authentication information to the [callSIP](https://voximplant.com/docs/references/voxengine/voxengine/callsip) function in the secnario.

The outgoing scenario accepts the `customData` parameter in the following format:

```js theme={null}
{"callerid":"16503333333", "number":"16504444444"}
```

You can provide this parameter when launching the scenario via a **routing rule** or [StartScenarios](https://voximplant.com/docs/references/httpapi/scenarios#startscenarios) Management API method.


# Handling Background Noise
Source: https://docs.ultravox.ai/noise/handling-background-noise

Built-in robust noise handling to keep your calls on track and fast.

Ultravox Realtime provides robust, built-in support for handling background noise and challenging acoustic environments. The system is designed to deliver clear voice interactions even in noisy real-world conditions.

<Note>
  <b>Automatic Protection</b>

  Background noise handling is enabled by default for all Ultravox calls. No configuration is required to benefit from these capabilities.
</Note>

## Multi-Layer Noise Handling

Ultravox employs a comprehensive approach to noise management through multiple integrated components:

**Krisp Noise Cancellation** → Advanced noise suppression technology that filters out background sounds in real-time.

**Model Training** → The Ultravox model is specifically trained to recognize and process speech in noisy environments, understanding end user intent and context even when audio quality is compromised.

**Custom Architecture** → A specialized low-latency architecture that seamlessly integrates noise handling components while maintaining real-time performance.

The result is natural, clear voice interactions that work reliably across diverse acoustic conditions, allowing your AI agents to perform effectively in real-world environments.


# Handling Background Speakers
Source: https://docs.ultravox.ai/noise/handling-background-speakers

Built-in filtering to focus on the primary speaker in multi-speaker environments.

Ultravox Realtime provides built-in support for handling background speakers and multi-speaker environments. The system is designed to focus on the primary speaker while filtering out cross-talk and unwanted voice interactions.

<Note>
  <b>Automatic Filtering</b>

  Background speaker filtering is enabled by default for all Ultravox calls. This helps your AI agent focus on the intended speaker even in challenging multi-speaker scenarios.
</Note>

## Addressing a Complex Challenge

Multi-speaker environments present unique difficulties for voice AI systems:

* **Speaker phone scenarios** where multiple voices may be muffled or distant
* **Cross-talk situations** with overlapping conversations
* **Background conversations** that shouldn't trigger the AI agent

## Advanced Speaker Detection

Ultravox employs sophisticated techniques to handle these challenging scenarios:

**Model Training** → The Ultravox model distinguishes between speech and noise/unintelligible speech.

**Speaker Tracking** → Advanced algorithms analyze voical power levels and patterns to identify the primary speaker and filter out background voices.

**Real-time Processing** → All speaker detection and filtering happens in real-time without adding latency to the conversation.

The result is cleaner voice interactions where your AI agent responds to the intended speaker, reducing confusion and improving conversation quality in complex acoustic environments.


# Overview: Noise & VAD
Source: https://docs.ultravox.ai/noise/overview

Learn how Ultravox intelligently handles voice activity detection and background noise to create natural, responsive conversations.

Voice Activity Detection (VAD) and noise handling are critical components that determine how natural and responsive your voice conversations feel. Ultravox provides an intelligent, multi-layered approach to managing audio input that works seamlessly out of the box.

## Our Philosophy: Smart Defaults

At its core, Ultravox handles VAD complexity for you. Our system uses multiple models working together to provide a great experience out of the box.

We are very aggressive about triggering VAD by default because:

1. **Latency Matters** → Users expect immediate responses in voice conversations.
2. **Smart Models Compensate** → Neural VAD and noise cancellation handle edge cases (e.g. false positives, interruptions).
3. **Context is Key** → The conversation state helps determine when users are truly done speaking.

Additionally, Ultravox Realtime provides `vadSettings` that can be customized if and when needed. However, customizing VAD involves a series of tradeoffs.

### Key Benefits

**Low Latency** → Aggressive VAD settings combined with intelligent models minimize response delays.

**Natural Conversations** → Context-aware models understand conversation flow and turn-taking.

**Robust Audio Handling** → Built-in noise cancellation and background speaker management.

**Minimal Configuration** → Works excellently with default settings for most use cases.

## When to Customize

The default VAD settings are carefully tuned and work well for the vast majority of applications. You may need to adjust VAD settings for extremely noisy environments, accessibility needs, or other specialized situations.

If you are experiencing issues:

1. **Start with troubleshooting** → Verify your audio setup and environment.
2. **Test with default settings** → Ensure the issue isn't environmental or hardware-related.
3. **Make incremental changes** → Adjust one parameter at a time.
4. **Monitor the trade-offs** → Test thoroughly with real users and use cases.

The system is designed to be intelligent and adaptive. Trust the defaults unless you have a specific, tested need to change them.

<Warning>
  <b>Proceed with Caution</b>

  Changing VAD parameters is a trade-off game. Every adjustment has consequences for latency, accuracy, or user experience. We recommend extensive testing when modifying default settings.
</Warning>

## What's in This Section

<CardGroup>
  <Card title="Understanding VAD" href="/noise/understanding-vad" icon="sliders">
    Learn how VAD works, what the parameters control, and how our multi-model approach functions.
  </Card>

  <Card title="Handling Background Noise" href="/noise/handling-background-noise" icon="volume-slash">
    Strategies for managing environmental noise, audio interference, and input quality issues.
  </Card>

  <Card title="Handling Background Speakers" href="/noise/handling-background-speakers" icon="users">
    Techniques for environments with multiple speakers, echo, and cross-talk situations.
  </Card>
</CardGroup>


# Understanding VAD
Source: https://docs.ultravox.ai/noise/understanding-vad

Learn how Ultravox's multi-model VAD system works and when to adjust voice activity detection parameters.

Voice Activity Detection (VAD) determines when a user is speaking and when they've finished their turn. Understanding how Ultravox's VAD system works will help you make informed decisions about when and how to adjust settings.

## How Ultravox VAD Works

Ultravox Realtime uses a multi-layered approach to VAD which results in low latency and an overall experience that feels fluid and natural.

### Traditional VAD Model

The foundation is a classic VAD model that analyzes audio frames (32ms each) to predict "speechiness" - whether each frame contains human speech. This model is intentionally aggressive, meaning it has a low threshold for detecting potential speech.

### Neural VAD

Our neural VAD model makes intelligent predictions about conversation state and turn-taking patterns. It understands context like:

* Whether the user is likely finished speaking based on conversation flow
* Typical pause patterns in natural dialogue
* The difference between a thoughtful pause and the end of a turn

### Noise Cancellation & Audio Processing

Additional models handle:

* Background noise filtering
* Echo cancellation
* Audio quality enhancement
* False positive reduction

## VAD Parameters Explained

Ultravox exposes several VAD parameters that control this behavior. These parameters are exposed via the [vadSettings](/api-reference/calls/calls-post#body-vad-settings) object that can be set when creating new calls or call stages.

The following settings are available:

### `turnEndpointDelay`

<ResponseField name="turnEndpointDelay" type="string">
  The minimum time the agent waits before responding after the user appears to stop speaking.

  Only multiples of 32ms are meaningful (anything from 1ms - 31ms produces the same result).

  **Trade-offs:**

  * **Shorter delays** → Leads to faster responses, but more likely to interrupt users mid-thought.
  * **Longer delays** → Makes agent less eager to respond (i.e. interrupt the user), but perceived as slower or less responsive.

  ```js Adjusting turnEndpointDelay theme={null}
  vadSettings: {
    turnEndpointDelay: "0.384s"  // 12 VAD frames at 32ms each
  }
  ```
</ResponseField>

### `minimumTurnDuration`

<ResponseField name="minimumTurnDuration" type="string">
  The minimum duration of user speech required to be considered a valid turn.

  **Trade-offs:**

  * **Shorter durations** → Captures very short user audio.
  * **Longer durations** → Ignores very short user audio segments that might be noise but could ignore meaningful, short user responses like "yes" or "no".

  ```js Adjusting minimumTurnDuration theme={null}
  vadSettings: {
    minimumTurnDuration: "0s"  // Consider all user audio
  }
  ```
</ResponseField>

### `minimumInterruptionDuration`

<ResponseField name="minimumInterruptionDuration" type="string">
  The minimum duration of user speech required to interrupt the agent when it's speaking. Similar to minimumTurnDuration but provides a higher threshold for interrupting the agent. Ignored if the value is less than minimumTurnDuration.

  **Trade-offs:**

  * **Shorter durations** → More sensitive to interruptions, may trigger on background noise.
  * **Longer durations** → Less sensitive to noise, but may miss legitimate interruption attempts.

  ```js Adjusting minimumInterruptionDuration theme={null}
  vadSettings: {
    minimumInterruptionDuration: "0.09s"
  }
  ```
</ResponseField>

### `frameActivationThreshold`

<ResponseField name="frameActivationThreshold" type="number">
  The threshold for considering an individual audio frame as containing speech (0.1 to 1.0).

  **Trade-offs:**

  * **Lower thresholds** → More sensitive to quiet speech, but more false positives.
  * **Higher thresholds** → Less sensitive to noise, but may miss quiet or distant speakers.

  ```js Adjusting frameActivationThreshold theme={null}
  vadSettings: {
    frameActivationThreshold: 0.1  // Very sensitive to potential speech
  }
  ```
</ResponseField>

## Best Practices for VAD Tuning

<Warning>
  <b>Start with Defaults</b>

  The default VAD settings work well for most applications. Only adjust them if you have specific, tested issues that can't be resolved through environmental or hardware improvements.
</Warning>

### The Safest Parameter to Adjust

If you venture into adjusting VAD settings, `turnEndpointDelay` is the safest parameter to modify. As noted in the [API reference](/api-reference/schema/call-definition#schema-vad-settings-turn-endpoint-delay), "there's nothing special about this value" - it's simply a starting point that works well in most scenarios.

### Making Changes Safely

1. **Change one parameter at a time** → Isolate the effects of each adjustment.
2. **Test thoroughly** → Use real users and realistic environments.
3. **Monitor the trade-offs** → Every improvement in one area may cause issues in another.

### Environmental Solutions First

Before adjusting VAD parameters, consider:

* **Audio quality** → Better microphones reduce VAD complexity.
* **Network quality** → Poor connections can affect VAD performance.

Remember: VAD tuning is a series of trade-offs. The system is designed to be intelligent and adaptive. Trust the defaults unless you have a compelling, well-tested reason to change them.


# Overview: Ultravox Realtime
Source: https://docs.ultravox.ai/overview

Build Voice AI Agents That Work Anywhere

<CardGroup>
  <Card title="Sign-up" icon="user-plus" href="https://app.ultravox.ai?utm_source=docs" />

  <Card title="Quickstart" icon="person-running-fast" href="/gettingstarted/quickstart/agent-console" />

  <Card title="API Reference + Playground" icon="code" href="api-reference" />
</CardGroup>

## Key Features

Built on our best-in-class, [open-weight model](https://github.com/fixie-ai/ultravox), Ultravox Realtime provides a fully hosted platform for creating real-time, low-latency voice AI applications.

We provide everything you need:

<Icon icon="language" /> **Multi-lingual** → Support for 26 spoken languages (Arabic, Bulgarian, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hindi, Hungarian, Italian, Japanese, Polish, Portuguese, Romanian, Russian, Slovak, Spanish, Swedish, Tamil, Turkish, Ukrainian, Vietnamese)

<Icon icon="toolbox" /> [**Tools**](/tools/overview) → Give your agent the ability to connect to the world (AKA function calling)

<Icon icon="book" /> [**Knowledge (RAG)**](/tools/rag) → Amp up your agent's knowledge with custom, contextual knowledge

<Icon icon="arrow-progress" /> [**Call Stages**](/agents/call-stages) → Advanced agent branching and flows

<Icon icon="clock-rotate-left" /> [**Conversation History**](/api-reference/calls/calls-messages-list) → Audio recordings and full text transcripts

<Icon icon="circle-microphone" /> [**Voice Cloning**](/voices/overview) → Create the perfect voice for your agent

<Icon icon="code" /> [**SDKs**](/apps/sdks) → Build in your favorite language

<Icon icon="phone-plus" /> [**Telephony Integrations**](/telephony/overview) → Quickly use Ultravox with telephony partners

<Icon icon="webhook" /> [**Webhooks**](/webhooks/overview) → Get realtime notifications for key events


# Ultravox Client SDK
Source: https://docs.ultravox.ai/sdk-reference/introduction



The Ultravox [REST API](/api-reference/) is used to create calls but a client must still join the call. For web and mobile applications, you can do this with one of our SDKs. This page primarily uses examples in JavaScript. The concepts are the same across all the [different SDK implementations](#sdk-implementations).

## Methods

The core of the SDK is the `UltravoxSession`. The session is used to join and leave calls. The `UltravoxSession` contains methods for:

* Joining/leaving a call
* Sending text messages to the agent
* Changing the output medium for how the agent replies
* Registering client tools
* Muting the microphone/speaker

### joinCall()

Joins a call.

```ts theme={null}
joinCall(joinUrl: string, clientVersion?: string): void
```

<ParamField type="string">
  The joinUrl that was returned from the [`Create Call`](/api-reference/calls/calls-post) request.
</ParamField>

<ParamField type="string">
  Optional string that can be used for application version tracking. Will be appended to the call and be available in the `clientVersion` field in the [`Get Call`](/api-reference/calls/calls-get) response.
</ParamField>

### leaveCall()

Leaves the current call. Returns a promise (with no return value) that resolves when the call has successfully been left.

```ts theme={null}
async leaveCall(): Promise<void>
```

### sendText()

Sends a text message to the agent. If `deferResponse` is set, the agent will not respond (i.e. no LLM generation will be done).

```ts theme={null}
sendText(text: string, deferResponse?: boolean): void
```

<ParamField type="string">
  The message to send to the agent.
</ParamField>

<ParamField type="boolean">
  Set to `true` to skip LLM generation (agent won't reply). Can be used to provide additional guidance to the model.
</ParamField>

### setOutputMedium()

Sets the agent's output medium for future utterances. If the agent is currently speaking, this will take effect at the end of the agent's utterance.

```ts theme={null}
setOutputMedium(medium: Medium): void
```

<ParamField type="Medium">
  How replies are communicated. Must be either `'text'` or `'voice'`.
</ParamField>

Also see [muteSpeaker](#mutespeaker) and [unmuteSpeaker](#unmutespeaker) below.

### registerToolImplementation()

Registers a client tool implementation with the given name. If the call is started with a client-implemented tool, this implementation will be invoked when the model calls the tool.

```ts theme={null}
registerToolImplementation(name: string, implementation: ClientToolImplementation): void
```

<ParamField type="string">
  The name of the tool. Must match what is defined in `selectedTools` during [`Create Call`](/api-reference/calls/calls-post).<br /><br />If `nameOverride` is set then must match that name. Otherwise must match `modelToolName`.
</ParamField>

<ParamField type="ClientToolImplementation">
  The function that implements the tool's logic. This is a function that:

  **Accepts `parameters`** → An object containing key-value pairs for the tool's parameters. The keys will be strings.

  **Returns** → Either a string result, or an object with a result string and a responseType, or a Promise that resolves to one of these.

  For example:

  ```js theme={null}
    const stock_price = (parameters) => {
      ...  // to be implemented
      return `Stock price is ${value}`;
    };
  ```
</ParamField>

### registerToolImplementations()

Convenience batch wrapper for [`registerToolImplementation`](#registertoolimplementation).

```ts theme={null}
registerToolImplementations(implementationMap: { [name: string]: ClientToolImplementation }): void
```

<ParamField type="Object">
  An object where each key (a string) represents the name of the tool and each value is a `ClientToolImplementation` function.
</ParamField>

### isMicMuted()

Returns a boolen indicating if the end user's microphone is muted. This is scoped to the Ultravox SDK and does not detect muting done by the user outside of your application.

```ts theme={null}
isMicMuted(): boolean
```

### isSpeakerMuted()

Returns a boolen indicating if the speaker (the agent's voice output) is muted. This is scoped to the Ultravox SDK and does not detect muting done by the user outside of your application.

```ts theme={null}
isSpeakerMuted(): boolean
```

### muteMic()

Mutes the end user's microphone. This is scoped to the Ultravox SDK.

```ts theme={null}
muteMic(): void
```

### unmuteMic()

Unmutes the end user's microphone. This is scoped to the Ultravox SDK.

```ts theme={null}
unmuteMic(): void
```

### muteSpeaker()

Mutes the end user's speaker (the agent's voice output). This is scoped to the Ultravox SDK.

```ts theme={null}
muteSpeaker(): void
```

### unmuteSpeaker()

Unmutes the end user's speaker (the agent's voice output). This is scoped to the Ultravox SDK.

```ts theme={null}
unmuteSpeaker(): void
```

## Client Tools

Ultravox has robust support for [tools](/tools/overview). The SDK has support for client tools. Client tools will be invoked in your client code and enable you to add interactivity in your app that is driven by user interactions with your agent. For example, your agent could choose to invoke a tool that would trigger some UI change.

<Note>
  <b>Message Size Limit</b>

  Messages larger than 15-16KB may cause timeouts. Keep payload sizes within this limit.
</Note>

<br />

<b>Creating Client Tools</b>

Client tools are defined just like "server" tools with three exceptions:

<Steps>
  <Step title="'client' not 'http'">
    You don't add the URL and HTTP method for client tools.

    Instead, you add `"client": {}` to the tool definition.

    <CodeGroup>
      ```js Using a Client Tool {18} theme={null}
      {
        "systemPrompt": ...
        "selectedTools": [
          "temporaryTool": {
            "modelToolName": "stock_price",
            "description": "Get the current stock price for a given symbol",
            "dynamicParameters": [
              {
                "name": "symbol",
                "location": "PARAMETER_LOCATION_BODY",
                "schema": {
                  "type": "string",
                  "description": "Stock symbol (e.g., AAPL for Apple Inc.)"
                },
                "required": true
              }
            ],
            "client": {}
          }
        ]
      }
      ```

      ```js Using a Server Tool {18-21} theme={null}
      {
        "systemPrompt": ...
        "selectedTools": [
          "temporaryTool": {
            "modelToolName": "stock_price",
            "description": "Get the current stock price for a given symbol",
            "dynamicParameters": [
              {
                "name": "symbol",
                "location": "PARAMETER_LOCATION_QUERY",
                "schema": {
                  "type": "string",
                  "description": "Stock symbol (e.g., AAPL for Apple Inc.)"
                },
                "required": true
              }
            ],
            "http": {
              "baseUrlPattern": "https://api.stockmarket.com/v1/price",
              "httpMethod": "GET"
            }
          }
        ]
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Register Tool with Client">
    Your client tool must be registered in your client code. Here's a snippet that might be found in client code to register the client tool and implement the logic for the tool.

    See the SDK method [`registerToolImplementation()`](#registertoolimplementation) for more information.

    ```js Registering a Client Tool theme={null}
    // Start up our Ultravox Session
    uvSession = new UltravoxSession();

    // Register our client-side tool
    uvSession.registerToolImplementation(
      "stock_price",
      stock_price
    );

    uvSession.joinCall(joinUrl);

    // Function that implements tool logic
    const stock_price = (parameters) => {
      ...  // to be implemented
      return `Stock price is ${value}`;
    };
    ```
  </Step>

  <Step title="Only Body Parameters Allowed">
    Unlike server tools (which accept parameters passed by path, header, body, etc.), client tools only allow parameters to be passed in the body of the request. That means client tools will always have parameter location set like this:

    ```js theme={null}
    "location": "PARAMETER_LOCATION_BODY"
    ```
  </Step>
</Steps>

## Session Status

The `UltravoxSession` exposes status. Based on the `UltravoxSessionStatus` enum, status can be one of the following:

| status        | description                                                            |
| ------------- | ---------------------------------------------------------------------- |
| disconnected  | Session is not connected. This is the initial state prior to joinCall. |
| disconnecting | Session is in the process of disconnecting.                            |
| connecting    | Session is establishing the connection.                                |
| idle          | Session is connected but not yet active.                               |
| listening     | Listening to the end user.                                             |
| thinking      | The model is processing/thinking.                                      |
| speaking      | The model is speaking.                                                 |

<b>Status Events</b>

The status can be retrieved by adding an event listener to the session status.

```js Get Session Status Events theme={null}
// Listen for status changing events
session.addEventListener('status', (event) => {
  console.log('Session status changed: ', session.status);
});
```

## Transcripts

Sometimes you may want to augment the audio with text transcripts (e.g. if you want to show the end user the model's output in real-time). Transcripts can be retrieved by adding an event listener:

```js Get Transcripts theme={null}
// Listen for transcripts changing events
session.addEventListener('transcripts', (event) => {
  console.log('Transcripts updated: ', session.transcripts);
});
```

Transcripts are returned as an array of transcript objects.

<ResponseField name="transcript" type="Transcript Object">
  <Expandable title="properties">
    <ResponseField name="text" type="string">
      Text transcript of the speech from the end user or the agent.
    </ResponseField>

    <ResponseField name="isFinal" type="boolean">
      True if the transcript represents a complete utterance. False if it is a fragment of an utterance that is still underway.
    </ResponseField>

    <ResponseField name="speaker" type="Role">
      Either "user" or "agent". Denotes who was speaking.
    </ResponseField>

    <ResponseField name="medium" type="Medium">
      Either "voice" or "text". Denotes how the message was sent.
    </ResponseField>
  </Expandable>
</ResponseField>

## Debug Messages

<Warning>
  <b>No Guarantee</b>

  Debug messages from Ultravox should be treated as debug logs. They can change regularly and don't have a contract. Relying on the specific structure or content should be avoided.
</Warning>

The `UltravoxSession` object also provides debug messages. Debug messages must be enabled when creating a new session and then are available via an event listener similar to status and transcripts:

```js Get Debug Messages theme={null}
// Start up our Ultravox Session with Debug Messages Enabled
session = new UltravoxSession({ experimentalMessages: ["debug"] });

// Listen for debug messages
session.addEventListener('experimental_message', (msg) => {
  console.log('Got a debug message: ', JSON.stringify(msg));
});
```

<b>Debug Message:  Tool Call</b>

When the agent invokes a tool, the message contains the function, all arguments, and an invocation ID:

```bash theme={null}
LLM response: Tool calls: [FunctionCall(name='createProfile', args='{"firstName":"Ron","lastName":"Burgandy","organization":"Fixie.ai","useCase":"creating a talking AI news reporter"}', invocation_id='call_D2qQVS8OQc998aMEw5PRa9cF')]
```

<b>Debug Message:  Tool Call Result</b>

When the tool call completes, the message contains an array of messages. Multiple tools can be invoked by the model. This message array will conatain all the calls followed by all the results. These messages are also available via [List Call Messages](/api-reference/calls/calls-messages-list).

Here's an example of what we might see from a single tool invocation:

```bash theme={null}
Tool call complete.

Result: [
  role: MESSAGE_ROLE_TOOL_CALL ordinal: 6 text: "{\"firstName\":\"Ron\",\"lastName\":\"Burgandy\",\"organization\":\"Fixie.ai\",\"useCase\":\"creating a talking AI news reporter\"}" tool_name: "createProfile" invocation_id: "call_D2qQVS8OQc998aMEw5PRa9cF" tool_id: "aa737e12-0989-4adb-9895-f387f40557d8" ,
  role: MESSAGE_ROLE_TOOL_RESULT ordinal: 7 text: "{\"firstName\":\"Ron\",\"lastName\":\"Burgandy\",\"emailAddress\":null,\"organization\":\"Fixie\",\"useCase\":\"creating a talking AI news reporter\"}" tool_name: "createProfile" invocation_id: "call_D2qQVS8OQc998aMEw5PRa9cF" tool_id: "aa737e12-0989-4adb-9895-f387f40557d8"
]
```

## SDK Implementations

<SDKCards />


# Call Transfers
Source: https://docs.ultravox.ai/telephony/call-transfers

Transfer calls between AI agents and human operators.

Call transfers allow your AI agents to seamlessly hand off conversations to human operators when needed. This is essential for scenarios where the AI agent cannot resolve a customer's issue, needs to escalate to a specialist, or when the caller specifically requests to speak with a human.

## Understanding Call Transfers

Call transfers work by providing your AI agent with a custom tool that enables it to transfer active calls to human operators. The agent uses this tool based on instructions in your system prompt and the tool's description, determining when and how to initiate transfers.

<Note>
  <b>Agent-Initiated Transfers</b>

  The AI agent decides when to transfer calls based on your instructions. You control this behavior through your system prompt and tool configuration.
</Note>

### Transfer Variants

There are two main types of call transfers you can implement:

**Cold Transfer** → The call is immediately transferred to the human operator without any preparation or context sharing. Also known as a blind transfer or unattended transfer.

**Warm Transfer** → The agent provides context about the conversation to the human operator before the caller is connected. Also known as an attended transfer or whisper transfer.

Additionally, there are two methods by which a transfer may be implemented:

**Refer** → The SIP REFER verb is used to connect the caller with the human operator, removing the agent and related SIP stack altogether. This is almost always preferable as long as all the relevant SIP providers support it.

**Bridge** → The human operator is dialed using a second SIP INVITE. While the agent leaves the call, the SIP stack remains and bridges audio between the caller and the human operator. This is less efficient and will incur additional costs, but may be necessary if your SIP provider does not support REFER transfers.

<Note>
  <b>Bridge Transfers Cost More</b>

  Using bridge transfers will result in SIP charges beyond the Ultravox call duration as our SIP infrastructure remains active to bridge audio between the caller and human operator.
</Note>

## SIP Call Transfers

For SIP calls, transfers can be achieved using built-in tools for [cold transfers](/tools/built-in-tools#coldtransfer) or [warm transfers](/tools/built-in-tools#warmtransfer).

### Cold Transfers

Cold transfer uses refer transfers by default. If you need to use bridge transfers instead, you can override the `sipVerb` parameter from `REFER` to `INVITE` when adding the tool to your agent (or call). You may also wish to set `from`, `username`, and/or `password` in order to authenticate the subsequent INVITE. The `from` parameter defaults to the user's sip address if not specified.

Should the transfer fail (e.g., the human operator declines the call or otherwise fails to answer), the caller will be returned to the AI agent to continue the conversation. Transfers may be retried by the agent as needed.

### Warm Transfers

When an agent begins a warm transfer, a second SIP call is created to connect the agent with a human operator. This always happens with an INVITE, so you likely want to set `from`, `username`, and `password` parameter overrides in addition to the required `target` parameter override. As with `coldTransfer`, the `from` parameter defaults to the user's sip address if not specified.

When the human operator answers, they speak with the agent to receive context about the caller and reason for the transfer. They may accept or reject the transfer using natural conversation. If they reject the transfer, the agent reconnects with the original caller and explains that the transfer was rejected, offering a reason if provided by the human operator.

If the human operator accepts the transfer, the human operator and original caller are connected and the agent leaves the call.  By default the connection happens using an in-session REFER while falling back on bridging the calls if the REFER fails. You can override this behavior by setting the `transferType` parameter to either `REFER` or `BRIDGE` to force a specific transfer method. (The default is called `TRY_REFER`.)

## Call Transfers with Other Telephony Providers

<Info>
  <b>Built-in coldTransfer tool with Twilio</b>

  <br />

  The built-in `coldTransfer` tool also works with Twilio if you've [added your credentials](/telephony/supported-providers#providing-telephony-credentials), but be aware that invoking the tool will immediately end the Ultravox call regardless of whether the transfer succeeds.
</Info>

To implement call transfers:

<Steps>
  <Step title="Create a Transfer Tool">
    Build a custom tool that your AI agent can call to initiate transfers. This tool should handle the telephony provider's transfer APIs.
  </Step>

  <Step title="Configure Agent Instructions">
    Update your system prompt to instruct the agent when and how to use the transfer tool. Include guidelines for all transfer scenarios and when transfers should occur (e.g., "Transfer when you cannot answer billing questions" or "Transfer if the customer asks for a manager").

    Instruct your agent to politely explain the transfer to the customer before initiating it (e.g., "I'm going to connect you with a specialist who can better help with your billing question").
  </Step>

  <Step title="Handle Transfer Logic">
    Implement the backend logic to manage the actual call transfer using your telephony provider's APIs.
  </Step>
</Steps>

```js Example Call Transfer Tool Definition theme={null}
{
  "toolName": "transferCall",
  "description": "Transfer the current call to a human agent when you cannot resolve the customer's issue or when they specifically request to speak with a human.",
  "parameters": {
    "destinationNumber": {
      "type": "string",
      "description": "The phone number to transfer the call to"
    },
    "transferReason": {
      "type": "string",
      "description": "Brief explanation of why the call is being transferred"
    }
  }
}
```

### Twilio

Twilio supports both blind and attended transfers through different APIs. Blind transfers use the simple `<Dial>` verb to immediately connect the caller to a new destination, while attended transfers utilize Twilio's Conference API to create a three-way call before the agent disconnects.

**Blind Transfer**: Uses Twilio's `calls.update()` method with TwiML containing a `<Dial>` verb to immediately redirect the call.

**Attended Transfer**: Creates a conference call, places the original caller on hold, calls the human agent with a whisper message, and allows the agent to join the conference after hearing the context.

The attended transfer process involves:

1. Putting the caller on hold with music
2. Creating a conference call
3. Calling the human agent with the transfer reason
4. Requiring the agent to press a key to join
5. Connecting all parties to the conference
6. Allowing the AI agent to disconnect

<Tip>
  <b>Complete Example Available</b>

  We have a full working example of Twilio call transfers (including both blind and attended transfers) available in the [`ultravox-examples`](https://github.com/fixie-ai/ultravox-examples/tree/main/telephony/twilio-call-transfer-ts) repo.
</Tip>

## Conclusion

Call transfers are essential for creating robust AI-powered voice applications that can seamlessly escalate to human operators when needed. By implementing both blind and attended transfer capabilities, you can ensure customers receive the appropriate level of service while maintaining a smooth experience throughout the conversation.


# Inbound Calls
Source: https://docs.ultravox.ai/telephony/inbound-calls

Configure AI agents to answer incoming phone calls.

Ultravox can power AI agents that automatically answer incoming phone calls from your users. This is perfect for customer service, support lines, or any application where users initiate contact.

## How Inbound Calls Work

The simplest way to set up inbound calls is to [import your credentials](/telephony/supported-providers#providing-telephony-credentials) and point your telephony provider directly to Ultravox. Just set your telephony provider's webhook callback to `https://app.ultravox.ai/api/agents/{agent_id}/telephony_xml` to have incoming phone calls automatically create and connect to Ultravox calls.

Alternatively, you can use these steps when routing calls through your own application.

<Steps>
  <Step title="User Dials You">
    User dials your phone number purchased from your telephony provider.
  </Step>

  <Step title="Incoming Webhook">
    Provider routes the call to your configured webhook/application.
  </Step>

  <Step title="Create Ultravox Call">
    Your server creates an Ultravox call and gets a `joinUrl`.
  </Step>

  <Step title="Connect & Answer">
    Connect the call to your provider using the `joinUrl`. The AI agent answers and begins the conversation.
  </Step>
</Steps>

## Using Template Variables

When you use [Agents](/agents/overview#why-start-with-agents%3F) for creating calls, you can define template variables that get passed in at call creation time.

When using simplified incoming call handling (i.e. you have imported your credentials from a [supported provider](/telephony/supported-providers#providing-telephony-credentials)), you can define a mapping from your provider's requests to template context fields. For example, for Twilio you could add an entry like `{"From": "user.phone_number"}` to add `{"user": {"phone_number": "+15551234567"}}` to the template context .

When handling telephony webhooks yourself, this data might come from an IVR or your own application. You then specify it as usual (i.e. via template variables) when creating your Ultravox call, e.g.

```js Example: Template Context theme={null}
// System prompt expects template variables
systemPrompt: "You are calling {{customerName}}..."

// Set templateContext at call creation time
templateContext: {
  customerName: "VIP Customer",
  accountType: "enterprise"
}
```

For more see [Template Context →](/agents/making-calls#template-context-and-variables)

## Next Steps

* Check out the [Inbound Call Quickstart](/gettingstarted/quickstart/telephony-inbound)
* Learn about [Call Transfers](/telephony/call-transfers) to escalate calls to human agents


# Handling IVR Flows
Source: https://docs.ultravox.ai/telephony/ivr-flows

Build interactive voice response systems with keypad input and DTMF tones.

Ultravox provides comprehensive support for DTMF (Dual-Tone Multi-Frequency) tones, enabling both [sending](#sending-dtmf-tones) and [receiving](#receiving-dtmf-tones) tones during phone calls. This enables AI agents to interact with traditional phone systems and allows you to build voice applications that can respond to keypad inputs.

<Note>
  <b>DTMF and WebRTC</b>

  <br />

  Due to the audio codec used in WebRTC connections, DTMF tones are inaudible when using WebRTC. The `playDtmfSounds` tool is intended for use with [telephony integrations](/telephony/overview).
</Note>

## Receiving DTMF Tones

Ultravox automatically converts incoming DTMF tones to text, making it easy to build interactive voice applications that respond to keypad input. When a caller presses keys on their phone keypad, the tones are converted to text that your AI agent can understand and respond to.

For example, if a caller presses "5" on their keypad, your agent will receive this as text and can respond accordingly:

```js theme={null}
// Example system prompt for an agent that handles DTMF input
{
  "systemPrompt": `You are an automated phone system.
    When a caller joins, say: "Welcome! Press 1 for sales, 2 for support, or 3 for billing."
    If they press 1, transfer them to sales using the transfer tool.
    If they press 2, transfer them to support.
    If they press 3, transfer them to billing.
    If they press any other key, ask them to try again with a valid option."`
}
```

## Sending DTMF Tones

The [built-in](/tools/built-in-tools#playdtmfsounds) `playDtmfSounds` tool allows your AI agent to send DTMF tones, which is useful for navigating Interactive Voice Response (IVR) systems or other phone trees. To enable the tool, add it to the `selectedTools` array when creating a call or call stage:

```js theme={null}
// Example request body for creating a call with DTMF capability
{
  "systemPrompt": "You are a helpful assistant. When prompted to dial an extension, use the 'playDtmfSounds' tool to send the appropriate tones.",
  "selectedTools": [
    { "toolName": "playDtmfSounds" }
  ]
}
```

The `playDtmfSounds` tool accepts a string parameter named `digits` and works with the following tones: 0-9, \*, #, A-D.

For example:

```js theme={null}
// Example of using the playDtmfSounds tool to dial an extension
{
  "digits": "123#"  // Will play tones for 1, 2, 3, and # in sequence
}
```

Note: the `playDtmfSounds` tool uses an [automatic parameter](/tools/custom/parameters#automatic-parameters) that sends the proper sample rate of the source audio and should be treated as an implementation detail.

## Common Use Cases

* Building interactive phone trees or IVR systems
* Creating agents that can navigate existing phone systems
* Enabling quick responses through keypad input
* Collecting numeric input (e.g., account numbers, PIN codes)
* Building hybrid voice/keypad interfaces


# Outbound Call Scheduler
Source: https://docs.ultravox.ai/telephony/outbound-call-scheduler

Schedule and manage batches of outbound calls automatically with concurrency control and retry handling.

<Callout icon="star">
  <b>Premium Feature</b>

  <br />

  Outbound Call Scheduler is available on select plans.

  See [https://ultravox.ai/pricing](https://ultravox.ai/pricing) for details.
</Callout>

The Outbound Call Scheduler (OCS) enables you to create and manage batches of outbound calls that will be sent by Ultravox. This allows you to simplify your deployment and stop worrying about things like retry logic. Simply define a time window and upload your call list - Ultravox handles the rest.

## Overview

The OCS eliminates the complexity of managing outbound call campaigns by:

* **Automatic Concurrency Management** - No more 429 errors from hitting rate limits
* **Flexible Scheduling** - Define time windows for when calls should be made
* **Automatic capacity reservation** - Save room for high priority or incoming calls while your campaign is running
* **Batch Management** - Track progress and control execution

<Danger>
  <b>Call Delivery Not Guaranteed</b>

  <br />

  Unless your call batch is scheduled without an end date/time, using OCS does not guarantee that all calls will be made. If capacity limitations result in calls not being made by the end of your window, those scheduled calls will have the `EXPIRED` status.
</Danger>

## How It Works

<Steps>
  <Step title="Create a Scheduled Batch">
    Pick an agent and upload a batch of calls with a time window and configuration.
  </Step>

  <Step title="Automatic Processing">
    Ultravox processes calls within your specified window, maximizing allowed utilization.
  </Step>

  <Step title="Call Execution">
    Calls are either initiated automatically or via webhook notifications.
  </Step>

  <Step title="Monitor Progress">
    Track batch status and individual call outcomes.
  </Step>
</Steps>

## Creating a Scheduled Batch

Use the [Create Scheduled Batch](/api-reference/agents/agents-scheduled-batches-post) API to upload your call batch.

### Batch Parameters

<ParamField type="string">
  The earliest time when calls in this batch can be initiated.
</ParamField>

<ParamField type="string">
  The latest time when calls in this batch can be initiated.
</ParamField>

<ParamField type="string">
  Optional. URL to notify when calls are ready to be initiated. Required if any call doesn't have an outgoing medium.
</ParamField>

<ParamField type="string">
  Optional. Secret for webhook request verification. Auto-generated if not provided.
</ParamField>

<ParamField type="array">
  Array of call configurations. Each call can include:

  * `medium` - Must be a valid call [medium](/api-reference/schema/call-definition#schema-medium)
    * Automatic outgoing calls work with `sip`, `twilio`, `telnyx`, or `plivo`
    * `webRtc` or `serverWebSocket` require providing a webhook URL
  * `templateContext` - Variables for agent template substitution
  * `metadata` - Key-value pairs associated with the call
  * `experimentalSettings` - Advanced call configuration
</ParamField>

### Examples

<Tabs>
  <Tab title="Creating a Batch" icon="plus">
    When all calls in your batch have an `outgoing` medium, Ultravox initiates calls automatically.

    ```js Example: Creating a Scheduled Batch theme={null}
    {
      "windowStart": "2025-09-25T09:00:00Z",
      "windowEnd": "2025-09-25T17:00:00Z",
      "calls": [
        {
          "medium": {
            "sip": {
              "outgoing": {
                "to": "sip:+15551234567@carrier.com",
                "from": "Your Company"
              }
            }
          },
          "templateContext": {
            "customerName": "John Doe",
            "appointmentTime": "3 PM tomorrow"
          },
          "metadata": {
            "customer_id": "12345",
            "campaign": "appointment_reminders"
          }
        },
        {
          "medium": {
            "twilio": {
              "outgoing": {
                "to": "+15551234567",
                "from": "+15559876543"
              }
            }
          },
          "templateContext": {
            "customerName": "Jane Smith", 
            "appointmentTime": "2 PM tomorrow"
          },
          "metadata": {
            "customer_id": "67890",
            "campaign": "appointment_reminders"
          }
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Example: Webhook Notification" icon="webhook">
    When calls don't have outgoing mediums or you want more control, Ultravox notifies your webhook when capacity is available and your call is created. Your endpoint's job is to then join and connect the call.

    ```js Example: Webhook Notification theme={null}
    {
      "webhookUrl": "https://your-server.com/call-ready",
      "webhookSecret": "your-secret-key",
      "calls": [
        {
          "medium": {"webRtc": {}},
          "templateContext": { "customerName": "John" },
          "metadata": { "phone": "+15551234567" }
        }
      ]
    }
    ```

    Your webhook receives the payload for the [call.started](/webhooks/available-webhooks#event-payload-reference) webhook event:

    ```js Call Definition Webhook Payload theme={null}
    {
      "event": "call.started",
      "call": {
        "callId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "created": "2023-11-07T05:31:56Z",
        "joined": "2023-11-07T05:31:56Z",
        ...
      }
    }
    ```

    <Warning>
      <b>No Retries</b>

      <br />

      OCS webhooks do not retry failed notifications automatically. When your endpoint is unavailable, the system marks that delivery as "ERROR" and proceeds to the next scheduled call after a delay period.
    </Warning>
  </Tab>
</Tabs>

## Managing Batches

### Monitor Batch Progress

Use [Get Scheduled Batch](/api-reference/agents/agents-scheduled-batches-get) to check status:

```js Response Example theme={null}
{
  "batchId": "uuid",
  "totalCount": 1000,
  "completedCount": 750,
  "windowStart": "2024-01-15T09:00:00Z",
  "windowEnd": "2024-01-15T17:00:00Z",
  "paused": false,
  "endedAt": null
}
```

### List Scheduled Calls

View individual calls with [List Scheduled Calls](/api-reference/agents/agents-scheduled-batches-scheduled-calls-list):

```bash theme={null}
GET /api/agents/{agent_id}/scheduled_batches/{batch_id}/scheduled_calls?status=SUCCESS
```

### List Created Calls

See completed calls with [List Created Calls](/api-reference/agents/agents-scheduled-batches-created-calls-list):

```bash theme={null}
GET /api/agents/{agent_id}/scheduled_batches/{batch_id}/created_calls
```

### Pause a Batch

Use [Update Scheduled Batch](/api-reference/agents/agents-scheduled-batches-patch) to pause execution:

```js Pause Batch theme={null}
{
  "paused": true
}
```

<Warning>
  <b>No Resume Function</b>

  <br />

  Once paused, batches cannot currently be resumed. Pausing effectively stops processing without deleting the batch.
</Warning>

### Delete a Batch

Use [Delete Scheduled Batch](/api-reference/agents/agents-scheduled-batches-delete) to remove a batch entirely.

## Limits and Considerations

### Request Limits

* **Call Count**: No specific limit on number of calls per batch
* **Request Size**: Maximum 32MB per batch request
* **Multiple Batches**: Create additional batches if your request size is > 32MB

### Time Windows

* Calls will only be processed during the specified window
* Use appropriate time zones in your ISO 8601 timestamps
* Consider business hours and time zones of your recipients

### Error Handling

* Monitor batch progress to identify systematic issues
* Completed calls have a status and will indicate any calls experiencing errors

## Next Steps

* Explore the [Scheduled Call Batch](/api-reference/agents/agents-scheduled-batches-list) APIs
* Learn about [Outbound Calls](/telephony/outbound-calls) for single-call scenarios
* Explore [Template Context](/agents/making-calls#template-context-and-variables) for dynamic call personalization


# Outbound Calls
Source: https://docs.ultravox.ai/telephony/outbound-calls

Configure AI agents to make outbound phone calls to users.

It's easy to have your Ultravox agent make outbound calls for appointment reminders, customer outreach, surveys, proactive customer service, or anything else you can dream up.

## The Easy Way: Built-in Telephony

The simplest way to make outbound calls is using Ultravox's built-in telephony integration. Configure your telephony provider credentials once, then Ultravox handles call creation automatically.

<Steps>
  <Step title="Configure Provider Credentials">
    [Import credentials](/telephony/supported-providers#providing-telephony-credentials) for Twilio, Telnyx, or Plivo.
  </Step>

  <Step title="Create Outbound Call">
    Create an Ultravox call with the `outgoing` parameter added to the call medium - no external API calls needed.
  </Step>

  <Step title="Call Initiated Automatically">
    Ultravox creates and connects the call using your provider credentials.
  </Step>
</Steps>

<Info>
  For outbound calls, make sure to set [`firstSpeakerSettings`](#firstspeakersettings) to `user` if you expect the call recipient to answer before the agent speaks. Also see the [user fallback](/api-reference/schema/call-definition#schema-first-speaker-settings-user-fallback).
</Info>

### Example: Direct Outbound Call

```js Built-in Telephony Example theme={null}
{
  "systemPrompt": "You are calling to remind John Doe about their appointment.",
  "firstSpeakerSettings": { "user": {} },
  "medium": {
    "twilio": {
      "outgoing": {
        "to": "+15551234567",
        "from": "+15559876543",
        "additionalParams": {
          "statusCallback": "https://your-server.com/status"
        }
      }
    }
  }
}
```

### Outgoing Parameters by Provider

<Tabs>
  <Tab title="Twilio">
    ```js Twilio Outgoing theme={null}
    // When `to` is a SIP address, `from` does not have to be a phone number.
    {
      "twilio": {
        "outgoing": {
          "to": "+15551234567",        // Phone number or SIP address
          "from": "+15559876543",      // Your Twilio phone number or a string
          "additionalParams": {        // See Twilio docs for all options
            "statusCallback": "https://your-server.com/status"
            "record": true
          }
        }
      }
    }
    ```

    See [Twilio Call API](https://www.twilio.com/docs/voice/api/call-resource#request-body-parameters) for all `additionalParams` options.
  </Tab>

  <Tab title="Telnyx">
    ```js Telnyx Outgoing theme={null}
    {
      "telnyx": {
        "outgoing": {
          "to": "+15551234567",        // Phone number in E.164 format
          "from": "+15559876543",      // Your Telnyx phone number
          "additionalParams": {        // See Telnyx docs for all options
            "statusCallback": "https://your-server.com/webhook"
          }
        }
      }
    }
    ```

    See [Telnyx Call API](https://developers.telnyx.com/api/call-scripting/initiate-texml-call) for all `additionalParams` options.
  </Tab>

  <Tab title="Plivo">
    ```js Plivo Outgoing theme={null}
    {
      "plivo": {
        "outgoing": {
          "to": "+15551234567",        // Phone number or SIP URI
          "from": "+15559876543",      // Your Plivo phone number
          "additionalParams": {        // See Plivo docs for all options
            "hangup_url": "https://your-server.com/answer"
          }
        }
      }
    }
    ```

    See [Plivo Call API](https://www.plivo.com/docs/voice/api/call/make-a-call) for all `additionalParams` options.
  </Tab>
</Tabs>

## The Other Way: External Integration

You can also integrate Ultravox with your existing telephony workflows by creating calls manually through your provider's API.

<Steps>
  <Step title="Call Trigger">
    Your application triggers an outbound call (user action, scheduled event, etc.).
  </Step>

  <Step title="Create Ultravox Call">
    Create an Ultravox call with correct [firstSpeakerSetting](#firstspeakersettings).
  </Step>

  <Step title="Initiate Phone Call">
    Initiate the phone call using your telephony provider's API and connect it to Ultravox using the `joinUrl`. User answers and the agent engages in the conversation.
  </Step>
</Steps>

## Bulk Outbound Calls

For scheduling large volumes of outbound calls, use the [Outbound Call Scheduler (OCS)](/telephony/outbound-call-scheduler) which provides:

* **Automatic Concurrency Management** - No more 429 errors from hitting rate limits
* **Flexible Scheduling** - Define time windows for when calls should be made
* **Automatic capacity reservation** - Save room for high priority or incoming calls while your campaign is running
* **Batch Management** - Track progress and control execution

The OCS supports both the simplified built-in telephony approach and external integration methods.

## `firstSpeakerSettings`

By default, Ultravox calls assume the agent begins conversations. This is typically what you want for inbound calls (i.e. an agent answering incoming customer support calls). However, outbound calls require modifying this behavior since the user will typically answer the phone with something like "Hello".

```js Settings for Outbound Call theme={null}
{
  "firstSpeakerSettings": { "user": {} }
}
```

## Using Template Variables

When you use [Agents](/agents/overview#why-start-with-agents%3F) for creating calls, you can define template variables that get passed in a call creation time.

```js Example: Template Context theme={null}
// System prompt expects template variables
systemPrompt: "You are calling {{customerName}}..."

// Set templateContext at call creation time
templateContext: {
  customerName: "VIP Customer",
  accountType: "enterprise"
}
```

For more see [Template Context →](/agents/making-calls#template-context-and-variables)

## Next Steps

* Check out the [Outbound Call Quickstart](/gettingstarted/quickstart/telephony-outbound)
* Learn about [Call Transfers](/telephony/call-transfers) to escalate calls to human agents
* Read [Managing Concurrency](/gettingstarted/concurrency) to learn how to keep the pipe full when making many calls
* Use [Outbound Call Scheduler](/telephony/outbound-call-scheduler) for bulk calling campaigns


# Overview: Telephony
Source: https://docs.ultravox.ai/telephony/overview

Connect Ultravox to traditional phone networks for AI-powered voice calls.

Ultravox Realtime is a "BYOT" (bring your own telephony) platform and integrates with major telephony providers to enable AI-powered voice applications that work with regular phone numbers. Your AI agents can make outbound calls and answer inbound calls through traditional phone networks.

## Connection Methods

Ultravox supports multiple ways to connect to phone networks:

<Columns>
  <Card title="Telephony Providers" href="./supported-providers">
    Native support for Twilio, Telnyx, Plivo, and Exotel.
  </Card>

  <Card title="Voice Platforms" href="./supported-providers">
    Integrations with Voximplant and jambonz.
  </Card>

  <Card title="SIP" href="./sip">
    Connect your existing phone system through our SIP integration.
  </Card>
</Columns>

Learn more: [Supported Providers →](./supported-providers)

Learn more: [SIP Guide →](./sip)

## Key Capabilities

Create AI agents that can handle both directions of phone communication:

* [Outbound Calls](/gettingstarted/examples/outbound-phone-call) - AI agents initiate calls to users.
* [Incoming Calls](/gettingstarted/examples/inbound-phone-call) - AI agents answer calls from users.

You can also enable your agents to handle more advanced tasks:

* [Call Transfers](./call-transfers) - Route calls between agents and humans.
* [IVR Flows](./ivr-flows) - Interactive voice response with keypad input using Ultravox's native support for DTMF.

## Simplified Outbound Calling

With Ultravox's built-in telephony integration, you can make outbound calls directly without managing external telephony provider APIs. Simply configure your Twilio, Telnyx, or Plivo credentials once, then create calls with the `outgoing` parameter - Ultravox handles the rest automatically.

Learn more: [Outbound Calls →](./outbound-calls)

## Connecting Ultravox to a Phone Call

<Warning>
  <b>"Calls" is Overloaded</b>

  <br />

  It can be a bit confusing because Ultravox Realtime uses the concept of a "call" to mean a voice session between an AI agent and another party. For phone calls, you will accept inbound or make outbound calls via your chosen telephony provider and then connect those calls to an Ultravox call.
</Warning>

Creating an Ultravox call that you can connect with a phone call requires specific parameters in the [Create Call](/api-reference/calls/calls-post) command:

<ParamField type="object">
  Tells Ultravox which protocol to use. For phone calls, must be set to one of:

  `{"telnyx": {}}`, `{"twilio": {}}`, or `{"plivo": {}}`.

  Defaults to `{"webRtc": {}}`.
</ParamField>

<ParamField type="object">
  Tells Ultravox who should speak first.

  For outbound calls, typically set to `user: {}`.

  The default is `agent: {}`.
</ParamField>

```js Example: Outbound Call via Twilio {4-7} theme={null}
{
  "systemPrompt": "You are a helpful assistant...",
  ...
  "medium": {
    "twilio": {} // or "telnyx": {} or "plivo": {} or "exotel": {}
  },
  "firstSpeakerSettings": { "user": {} }
}
```

## Learn More

* Discover how to get started with [Supported Providers](./supported-providers).
* Learn how to integrate with your existing phone system in the [SIP Guide](./sip).
* Set your agent up to receive [Inbound Calls](/gettingstarted/examples/inbound-phone-call) or make [Outbound Calls](/gettingstarted/examples/outbound-phone-call).


# SIP Guide
Source: https://docs.ultravox.ai/telephony/sip

Create incoming & outgoing SIP calls with Ultravox agents.

<Danger>
  <b>SIP Billing Starts November 10, 2025</b>

  <br />

  Calls via the SIP medium will start to incur additional charges on Monday, November 10, 2025.

  See [https://ultravox.ai/pricing](https://ultravox.ai/pricing) for details.
</Danger>

Session Initiation Protocol (SIP) enables Ultravox agents to connect with your existing phone systems and SIP clients. This guide explains how to set up both incoming and outgoing SIP calls with Ultravox agents.

## SIP Quickstart

The fastest way to start using SIP with Ultravox:

<Steps>
  <Step title="Create an Agent">Create an agent using the [Ultravox Realtime console](https://app.ultravox.ai/agents).</Step>
  <Step title="Create a SIP Call">Create an agent call using the [Create Agent Call](/api-reference/agents/agents-calls-post) API and use the `sip` medium.</Step>
</Steps>

<Note>
  <b>API Key Required</b>

  <br />

  Make sure you have an Ultravox API key. You can create one in the [console](https://app.ultravox.ai/settings/).
</Note>

## Incoming SIP Calls

For incoming calls, you can configure Ultravox to accept calls from your SIP system then send a sip invite directly to your agent. The SIP invite will create an Ultravox call and connect to it, no other requests required.

Ultravox supports two setups for incoming SIP calls: IP allowlisting and SIP registration. IP allowlisting works well with dedicated PBX systems, while SIP registration is recommended for cloud PBX setups.

In either setup, you can choose to allow incoming calls to all of your agents or to specific agents only. Calls will be created automatically from your agent's call template when a SIP invite is received.

By default, calls must be directed to the sip user `agent_{agent_id}` to reach your agent, but you can override this with your own regex matching. The regex for your agents will be checked in order with the first matching agent used for the call. If none match, the global `agent_{agent_id}` will be used if allowAllAgents is enabled. Otherwise (or if that doesn't match either), the call will be rejected.

### IP Allowlisting

To set up IP Allowlisting, use the [sip configuration API](/api-reference/sip/sip-partial-update) to add your SIP system's public IP addresses to the `allowedCidrRanges` list. Entries in this list must be IPv4 [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) ranges, e.g. `0.0.0.0/0` for any IP address (not recommended) or `91.200.160.14/32` for the single `91.200.160.14` IP address.

Once your SIP system's IP address(es) are allowed, you can have them send SIP invites to your agents using the pattern `agent_{agent_id}@{your_account_sip_domain}` by default. The value for `{your_account_sip_domain}` is available when you [view your SIP configuration](/api-reference/sip/sip-get). The user portion of the SIP address may be overridden by setting your own per-agent regex.

### SIP Registration

In the registration model, Ultravox acts as a SIP client (similar to a softphone) and registers with your SIP server as the user you specify. To set this up, you'll need to create a user in your PBX, configure your PBX to send relevant calls to that user, and then [create a registration](/api-reference/sip/sip-registrations-create) for that user in Ultravox.

When creating a registration, you'll need to provide the following information:

* `username`: The username of the user you created in your PBX.
* `password`: The password for that user.
* `proxy`: The domain or IP address of your SIP server.

In this case, you'll most likely want to alter the regex for your agents since the to address on invites is unlikely to be `agent_{agent_id}`.
For example, if your PBX sends calls to `sip:sales@your_sip_domain`, you could set the regex for your sales agent to `^sales$`. Similarly, if your SIP server interacts with PSTN, you could have your agent answer calls to +1-555-123-4567 and +1-555-765-4321 by setting the regex to `^15551234567$|^15557654321$`.

### Personalizing the Call

Many parts of an agent can use context to personalize a call. (See [Call Template Configuration](/agents/building-and-editing-agents#call-template-configuration).) You can use SIP headers to populate template context for incoming SIP calls. Each header value is interpretted as JSON to allow for complex values.

For example including the headers `X-Customer-Name: Bob` and `X-Complex-Value: {"subkey": "value"}` becomes `{"customer_name": "Bob", "complex_value": {"subkey": "value"}}`.

In addition to headers you send, Ultravox will automatically add the following context values for incoming SIP calls, provided they are allowed by your agent's context schema:

* `ultravox.sip.caller_id`: The caller id presented for the incoming call, typically a phone number.
* `ultravox.sip.from_display_name`: The display name of the caller, often the name of a person or business if known and a phone number otherwise.
* `ultravox.sip.from_uri`: The full SIP URI of the caller.

If your agent's context allows additional properties (or allows these properties explicitly), the added context will be structured as:

```json theme={null}
{
  "ultravox": {
    "sip": {
      "caller_id": "<caller_id>",
      "from_display_name": "<from_display_name>",
      "from_uri": "<from_uri>"
    }
  }
}
```

## Outgoing SIP Calls

For outgoing calls, you can create a SIP call with Ultravox Realtime [Create Agent Call](/api-reference/agents/agents-calls-post) or [Create Call](/api-reference/calls/calls-post) endpoints using the `sip` medium with `outgoing` property.

```js theme={null}
medium: {
  sip: {
    outgoing: {
      to: "sip:<destination>@<sip_domain>",
      from: "<your_identifier>",
      username: "<authentication_username>",
      password: "<authentication_password>"
    }
  }
}
```

When you create the call, Ultravox will automatically send a SIP invite using the properties provided.

### Outgoing SIP Parameters

<ParamField type="string">
  The target SIP URL to which the Ultravox call will connect.

  Examples:
  `sip:username@domain`, `sip:+15551234567@carrier.com`
</ParamField>

<ParamField type="string">
  The caller identifier. Must conform to what your SIP trunk allows.
</ParamField>

<ParamField type="string">
  Optional. Username for connecting to your SIP trunk.
</ParamField>

<ParamField type="string">
  Optional. Password for connecting to your SIP trunk.
</ParamField>

### Examples

```js Example: Creating an Outgoing SIP Call to Linphone theme={null}
    medium: {
      sip: {
        outgoing: {
          to: "sip:<username>@sip.linphone.org",
          from: "<company_name>"
        }
      }
    }
```

```js Example: Creating an Outgoing SIP Call using a Twilio trunk theme={null}
    medium: {
      sip: {
        outgoing: {
          to: "+15551234567@trunkname.pstn.twilio.com",
          from: "+15557654321",  // Some phone number you've purchased from Twilio
          username: "authorized_user",  // A user you've created in Twilio allowed to use this number
          password: "password_for_authorized_user"
        }
      }
    }
```

## Supported Transport Protocols

By default, UDP is used as the SIP transport protocol. You may optionally use TCP and/or TLS by explicitly adding a port and transport parameter to the target SIP URL.

| Protocol | How to Use in SIP URL                               |
| -------- | --------------------------------------------------- |
| UDP      | Default. No action required.                        |
| TCP      | `sip:<destination>@<sip_domain>:5060;transport=tcp` |
| TLS      | `sip:<destination>@<sip_domain>:5060;transport=tls` |

## Supported Codecs

Ultravox Realtime supports wideband (AKA "HD audio") and narrowband SIP via various codecs:

| Codec              | Audio Quality      |
| ------------------ | ------------------ |
| G.722              | HD (16kHz)         |
| G.722.1            | HD (16kHz)         |
| G.722.2            | HD (16kHz)         |
| Opus               | Premium HD (48kHz) |
| G.711 (PCMU/u-law) | Standard (8kHz)    |
| G.711 (PCMA/a-law) | Standard (8kHz)    |
| iLBC               | Standard (8kHz)    |

Using any other codec will cause calls to fail.

## Logs

Once a call has ended, you can see SIP logs for the call using the [sip logs](/api-reference/calls/calls-sip-logs-get) endpoint.


# Supported Providers
Source: https://docs.ultravox.ai/telephony/supported-providers

Comprehensive guide to telephony providers that integrate with Ultravox.

Ultravox integrates with multiple telephony providers and voice platforms.

## Native Integrations

Ultravox provides native integrations for the following. Each has their own unique call [`medium`](api-reference/schema/call-definition#schema-medium) that must be used when creating calls.

| Provider   | Call Medium    | Streaming API                                                                                  | Import Credentials? | Out of Band DTMF? |
| ---------- | -------------- | ---------------------------------------------------------------------------------------------- | ------------------- | ----------------- |
| **Twilio** | `"twilio": {}` | [Media Streams](https://www.twilio.com/docs/voice/media-streams)                               | ✅                   | ❌                 |
| **Telnyx** | `"telnyx": {}` | [Media Streaming](https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming) | ✅                   | ✅                 |
| **Plivo**  | `"plivo": {}`  | [AudioStream](https://www.plivo.com/docs/voice/xml/the-stream-element/)                        | ✅                   | ✅                 |
| **Exotel** | `"exotel": {}` | [Voice Streaming](https://developer.exotel.com/api/product-voice-version-3)                    | ❌                   | ❌                 |

## Providing Telephony Credentials

If you are using Twilio, Telnyx, or Plivo, you can import your credentials to unlock new capabilities:

* **Simplified Outbound Calling** → Allow Ultravox to create and connect [all outbound calls](/telephony/outbound-calls#the-easy-way%3A-built-in-telephony) for Twilio, Telnyx, and Plivo.
* **Outbound Call Scheduler** → [Schedule batches of outbound calls](/telephony/outbound-call-scheduler) and let us manage the call concurrency and retry logic.
* **Out of Band DTMF** → By default, the built-in [`playDtmfSounds`](/tools/built-in-tools#playdtmfsounds) tool emits in-band DTMF. When you import credentials for Telnyx or Plivo (Twilio doesn't support out of band DTMF), the `playDtmfSounds` tool will use out of band DTMF.
* **Simplified Incoming Call Handling** → Configure your provider to send webhooks directly to Ultravox for incoming calls. No need to run your own server.

### Importing Credentials

To import credentials for Twilio, Telnyx, or Plivo:

1. Use the [Set Telephony Credentials](/api-reference/accounts/accounts-me-telephony-config-partial-update) API
2. Provide your credentials (up to one per provider) in the request body:

```js Example: Proving telephony credentials theme={null}
{
  "twilio": {
    "accountSid": "string",
    "authToken": "string"
  },
  "telnyx": {
    "accountSid": "string",
    "apiKey": "string",
    "publicKey": "string",
    "applicationSid": "string"
  },
  "plivo": {
    "authId": "string",
    "authToken": "string"
  }
}
```

For each provider, you may also choose which agents can be used with [simplified incoming call handling](/telephony/inbound-calls). You can set `callCreationAllowAllAgents` to `true` to allow all of your agents or you can set `callCreationAllowedAgentIds` to specific agent ids to allow only those agents. For any allowed agent, you can direct your telephony provider to send webhooks to `https://app.ultravox.ai/api/agents/{agent_id}/telephony_xml` to have incoming phone calls automatically create and connect to Ultravox calls.

## SIP

Ultravox Realtime has native support for SIP. See the [SIP Guide](./sip) for more.

## Partner Integrations

Our voice platform partners have native integrations for Ultravox:

### Voximplant

[Voximplant](https://voximplant.com/) provides a hosted voice platform. Check out the [Integration Guide →](/integrations/voximplant)

### jambonz

[jambonz](https://www.jambonz.org/) provides a voice platform that runs in a fully managed cloud or can be self-hosted. Details on how to make and receive calls using jambonz appear [below](#jambonz-2).

## Provider-Specific Integration Examples

### Twilio

#### Outbound Calls with Twilio

<Steps>
  <Step title="Create an Ultravox Call">
    Create a new call as shown above with `medium: { "twilio": {} }`, `firstSpeakerSettings: { user: {} }`, and get a `joinUrl`.
  </Step>

  <Step title="Connect Ultravox to the Twilio Phone Call">
    Use the `joinUrl` with a Twilio `<Stream>`:

    ```js theme={null}
    // Example using the twilio node library
    const call = await client.calls.create({
        twiml: `<Response>
                    <Connect>
                        <Stream url="${joinUrl}"/>
                    </Connect>
                </Response>`,
        to: phoneNumber,
        from: twilioPhoneNumber
    });
    ```
  </Step>
</Steps>

<Info>Full example code in [Outbound Quickstart →](/gettingstarted/quickstart/telephony-outbound)</Info>

#### Incoming Calls with Twilio

<Steps>
  <Step title="Create an Ultravox Call">
    Create a new call with `medium: { "twilio": {} }` and `firstSpeakerSettings` set to `{ agent: {} }`.
  </Step>

  <Step title="Connect the Inbound Twilio Call to Ultravox">
    Use the `joinUrl` with a Twilio `<Stream>`:

    ```xml theme={null}
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Connect>
            <Stream url="your_ultravox_join_url" />
        </Connect>
    </Response>
    ```
  </Step>
</Steps>

<Info>Full example code in [Inbound Quickstart →](/gettingstarted/quickstart/telephony-inbound)</Info>

### Telnyx

#### Outbound Calls with Telnyx

<Steps>
  <Step title="Create an Ultravox Call">
    Create a new call as shown above with `medium: { "telnyx": {} }`, `firstSpeakerSettings: { user: {} }`, and get a `joinUrl`.
  </Step>

  <Step title="Connect Ultravox to the Telnyx Phone Call">
    Use the `joinUrl` with a TeXML `<Stream>`:

    ```js theme={null}
    // Example using the telnyx node library
    const call = await telnyx.calls.create({
      connection_id: "uuid",
      to: phoneNumber,
      from: telnyxPhoneNumber,
      stream_url: joinUrl,
      stream_track: "inbound_track",
      stream_bidirectional_mode: "rtp"
      stream_codec: "L16",
      stream_bidirectional_codec: "L16",
      stream_bidirectional_sampling_rate: 16000,
      stream_bidirectional_target_legs: "opposite",
    });
    ```

    Or using TeXML:

    ```xml theme={null}
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
      <Connect>
        <Stream url="${joinUrl}" bidirectionalMode="rtp"  codec="L16" bidirectionalCodec="L16" bidirectionalSamplingRate="16000"/>
      </Connect>
    </Response>
    ```
  </Step>
</Steps>

#### Incoming Calls with Telnyx

<Steps>
  <Step title="Create an Ultravox Call">
    Create a new call with `medium: { "telnyx": {} }` and `firstSpeakerSettings` set to `{ agent: {} }`.
  </Step>

  <Step title="Connect the Inbound Telnyx Call to Ultravox">
    Use the `joinUrl` with a TeXML `<Stream>`:

    ```xml theme={null}
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
      <Connect>
        <Stream url="${joinUrl}" bidirectionalMode="rtp"  codec="L16" bidirectionalCodec="L16" bidirectionalSamplingRate="16000"/>
      </Connect>
    </Response>
    ```
  </Step>
</Steps>

<Warning>
  <b>Telnyx `codec`</b>

  <br />

  Telnyx allows setting both `codec` and `bidirectionalCodec`. The former controls user audio while the latter controls agent audio. When using with Ultravox, **these must have the same value** because Telnyx only tells us about one of them! Now that Telnyx supports HD Audio, you most likely want "L16" for both.
</Warning>

For more details, see the [Telnyx documentation](https://developers.telnyx.com/).

### Plivo

<Info>Full example code for outbound and inbound calls with Plivo on GitHub [here →](https://github.com/fixie-ai/ultravox-examples/tree/main/telephony/plivo/plivo-phone-calls-ts)</Info>

#### Outbound Calls with Plivo

<Steps>
  <Step title="Create an Ultravox Call">
    Create a new call as shown above with `medium: { "plivo": {} }`, `firstSpeakerSettings: { user: {} }`, and get a `joinUrl`.
  </Step>

  <Step title="Connect Ultravox to the Plivo Phone Call">
    Use the `joinUrl` with AudioStream:

    ```js theme={null}
    // Example using the plivo node library
    // This assumes our server exposes an endpoint at `answerUrl`
    const call = await plivo.calls.create({
      to: phoneNumber,
      from: plivoPhoneNumber,
      answer_url: answerUrl, // URL that returns the XML below
      answer_method: "GET"
    });
    ```

    The answer URL should return:

    ```xml theme={null}
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Stream keepCallAlive="true"
                contentType="audio/x-l16;rate=16000"
                bidirectional="true">
            ${joinUrl}
        </Stream>
    </Response>
    ```

    Note: For best audio quality, we recommend `audio/x-l16;rate=16000`. However, any contentType supported by Plivo will work with Ultravox.
  </Step>
</Steps>

#### Incoming Calls with Plivo

<Steps>
  <Step title="Create an Ultravox Call">
    Create a new call with `medium: { "plivo": {} }` and `firstSpeakerSettings` set to `{ agent: {} }`.
  </Step>

  <Step title="Connect the Inbound Twilio Call to Ultravox">
    Use the `joinUrl` with AudioStream:

    ```xml theme={null}
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Stream keepCallAlive="true"
                contentType="audio/x-l16;rate=16000"
                bidirectional="true">
            ${joinUrl}
        </Stream>
    </Response>
    ```
  </Step>
</Steps>

For more details, see the [Plivo documentation](https://www.plivo.com/docs/).

### jambonz

#### jambonz Portal Setup

jambonz is a “bring your own everything” open-source telephony platform that integrates Ultravox directly via their [llm](https://docs.jambonz.org/verbs/verbs/llm) verb.
This gives you the flexibility to choose your carrier of choice, you'll just need to add it in your jambonz dashboard.

<Steps>
  <Step title="Add Your Carrier in jambonz">
    In jambonz, we use the terms “carrier” and “SIP trunk” interchangeably. jambonz is a “Bring your own carrier” platform, which means that you can connect any sip network provider or device. [Add your carrier of choice](https://docs.jambonz.org/guides/using-the-jambonz-portal/basic-concepts/creating-carriers) in your jambonz dashboard to get started.
  </Step>

  <Step title="Add a Speech Provider in jambonz">
    Next, you need to [add speech credentials](https://docs.jambonz.org/guides/using-the-jambonz-portal/basic-concepts/creating-speech-credentials) for your chosen vendor.
  </Step>

  <Step title="Create a New jambonz Application">
    ​A jambonz application configured via the jambonz portal defines how calls are handled by linking them to your custom logic through webhooks or WebSocket endpoints. When you create an application, you specify:​

    * Call webhook URL: Where jambonz sends call events.​
    * Call status webhook URL: For receiving call status updates.​
    * Speech vendors: Your chosen TTS/STT providers.​

    Once saved, you can associate phone numbers or SIP trunks with this application, ensuring that incoming calls are routed to your specified logic. This setup allows you to implement features like speech recognition, text-to-speech, call routing, and integration with AI services.
  </Step>

  <Step title="Add a Phone Number in jambonz">
    Finally, you need to [add a phone number](https://docs.jambonz.org/guides/using-the-jambonz-portal/basic-concepts/creating-phone-numbers) provisioned from your carrier of choice. At the bottom of the page select the jambonz application you just created to link your new virtual number to that application.
  </Step>
</Steps>

#### Incoming Calls with jambonz

```js theme={null}
// Example using the @jambonz/node-client-ws library
session
.pause({length: 1.5})
.llm({
  vendor: 'ultravox',
  model: 'ultravox-v0.7',
  auth: {
    apiKey
  },
  actionHook: '/final',
  eventHook: '/event',
  llmOptions: {
    systemPrompt: 'You are an agent named Karen. Greet the user and ask how you can help.',
    firstSpeakerSettings: { agent: {} },
    initialMessages: [{
      medium: 'MESSAGE_MEDIUM_VOICE',
      role: 'MESSAGE_ROLE_USER'
    }],
    model: 'ultravox-v0.7',
    voice: 'Tanya-English',
    transcriptOptional: true,
  }
})
.hangup()
.send();
```

For more details see the `llm` verb in the [jambonz docs](https://docs.jambonz.org/verbs/verbs/llm).

#### Outbound Calls with jambonz

In addition to the inbound scenario, you'll have to create a call that connects to the destination number (`phoneNumber`) and points to the jambonz application that defines how the call should be handled. Find the `APPLICATION_SID` in the jambonz portal by clicking on the application you created during the setup process.

```js theme={null}
  const JambonzClient = require('@jambonz/node-client');

  const client = JambonzClient(
    process.env.JAMBONZ_ACCOUNT_SID,
    process.env.JAMBONZ_API_KEY,
    {baseUrl: process.env.JAMBONZ_REST_API_BASE_URL || 'https://api.jambonz.cloud/v1'}
  );

  const call = await client.calls.create({
      from: process.env.FROM_NUMBER,
        to: {
          type : 'phone',
          number: phoneNumber,
          trunk: process.env.CARRIER
          },
      application_sid: process.env.APPLICATION_SID
  });
```

For more details, see the [jambonz documentation](https://docs.jambonz.org/) and [example code](https://github.com/jambonz/ultravox-s2s-example).


# Async Tools
Source: https://docs.ultravox.ai/tools/async-tools

Handle long-running operations and optimize tool performance for real-time conversations.

## The Latency Challenge

In real-time conversations, tool performance is critical. When adding your own tools, it's important to keep in mind that there's always a user actively waiting for your tool to respond. Some operations naturally take time but tools need to be (or at least appear) fast to make sense in a real-time context.

During tool execution, conversations are essentially frozen. Users can continue talking, but the agent won't respond until the tool completes. This creates several challenges:

* **User Experience**: Long waits feel like connection problems.
* **Conversation Flow**: Delays break natural conversation rhythm.
* **Tool Timeout**: Tools are limited to 2.5 seconds by default (max of 40 seconds).

### Tool Invocation Timing

By default, tool invocations are always included in the conversation history. This is done so that you can always understand the timing and context of all tool invocations. In cases when the LLM produces a combination of an agent utterance + a tool call, maintaining this conversation history requires delaying tool invocations until after the agent is done speaking speaking. Otherwise, there's no way to ensure the agent wouldn't be interrupted by the user (and potentially render the queued tool call irrelevant).

This is essential for tools that modify state since there's no good way to revert changes if the agent is interrupted. However, it's obviously suboptimal for tools like `queryCorpus` where we'd like to look up information while the agent is speaking and simply ignore the response if the agent is interrupted. Tools like this can be marked `precomputable`.

## Precomputable Tools

The most effective way to handle latency is to execute tools speculatively while the agent is speaking.

Any tool marked `precomputable` will be speculatively invoked as soon as the model produces the tool call. When the model produces both an agent utterance and the tool call, the tool's latency will be masked by the agent speaking, but if the agent is interrupted there will be no record of the invocation.

### How Precomputable Tools Work

1. Agent generates both speech and a tool call
2. Precomputable tool executes immediately while agent speaks
3. Tool result is available when speech finishes
4. If agent is interrupted, tool result is discarded

**Example:**

```js Marking Tool as Precomputable theme={null}
{
  "name": "lookupProduct",
  "definition": {
    "modelToolName": "lookupProduct",
    "description": "Look up product information",
    "precomputable": true, // ← Key property
    "dynamicParameters": [
      {
        "name": "productId",
        "location": "PARAMETER_LOCATION_QUERY",
        "schema": { "type": "string" },
        "required": true
      }
    ],
    "http": {
      "baseUrlPattern": "https://api.example.com/products/{productId}",
      "httpMethod": "GET"
    }
  }
}
```

In order to safely be marked `precomputable`, a tool should have three properties:

1. *No state changes*. For `http` tools, GET requests are usually safe while methods like POST are not.
2. *No side effects*. Even a GET request is not safe to precompute if it has a side effect! (It's up to you to decide what counts here though. Side effects like logging probably don't matter to you for example while any database write likely does.)
3. *Idempotent*. The tool must return the same result when called with the same parameters, regardless of when or how many times it is called.

If your tool meets these requirements, you can mark it `precomputable` using the [corresponding field](/api-reference/tools/tools-post#body-definition-precomputable).

### Requirements for Precomputable Tools

For a tool to be safely marked `precomputable`, it must be:

✅ **Read-only**: No state changes (GET requests are usually safe, POST requests are not).

✅ **No Side Effects**: No logging critical events, sending notifications, etc.

✅ **Idempotent**: Same input always produces same output, regardless of when or how many times it's called.

### Examples

**✅ Good Precomputable Tools:**

* Database lookups
* API queries for reference data
* File reads or cache retrievals
* Mathematical calculations

**❌ Bad Precomputable Tools:**

* Sending emails or notifications
* Database writes or updates
* Payment processing
* File uploads

## Custom Tool Timeouts

While tools are executing, the conversation is essentially frozen. The user can continue talking all they like, but the agent will never respond until after the tool invocation completes. (The agent does have access to anything the user said during tool execution once execution completes.)

To users this may feel like the call was disconnected or that there was an unnatural delay. In order to avoid these causes of perceived latency, tools are limited to a default execution time of 2.5 seconds. If your tool needs longer (and you can't make it faster), you can increase the timeout up to 40 seconds by setting the tool's [timeout field](/api-reference/tools/tools-post#body-definition-timeout). You can also reduce your tool's timeout. The value is a duration in seconds, like `5s` for 5 seconds or `0.1s` for 100 milliseconds.

**Example:**

```js Increasing Tool Timeout theme={null}
{
  "name": "complexAnalysis",
  "definition": {
    "modelToolName": "complexAnalysis",
    "description": "Perform complex data analysis",
    "timeout": "10s", // ← Custom timeout (up to 40s max)
    "dynamicParameters": [
      {
        "name": "dataset",
        "location": "PARAMETER_LOCATION_BODY",
        "schema": { "type": "string" },
        "required": true
      }
    ],
    "http": {
      "baseUrlPattern": "https://api.example.com/analyze",
      "httpMethod": "POST"
    }
  }
}
```

For tools that take even longer, consider responding immediately and later using a [user\_text\_message](/apps/datamessages#usertextmessage) with the real tool result. This is easiest with a `dataConnection` implementation since data connections are also able to send input text messages (and the response is always deferred in that case). Keep in mind that the model will see whatever response you send back initially, so you'll want to make it clear to the model what's going on by initially responding with some text like "Tool started. The full response will be available soon."

**Custom Timeout Considerations**

* **Start Small**: Begin with default 2.5s, increase only if needed.
* **Set User Expectations**: Tell users when operations will take time.
* **Fallback Plans**: Handle timeout failures gracefully.


# Built-in Tools
Source: https://docs.ultravox.ai/tools/built-in-tools

Ready-to-use tools for common functionality in voice applications.

Ultravox Realtime includes several built-in tools that provide common functionality out of the box. These tools are publicly available and work exactly like custom tools you create yourself.

## Available Built-in Tools

| Tool Name      | Description                                                                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| queryCorpus    | Retrieves relevant information from an existing corpus (knowledge base). See [Query Corpus API](/api-reference/corpora/corpus-query) for details. |
| leaveVoicemail | Leaves a voicemail and ends the call. Intended to be used with outbound phone calls.                                                              |
| hangUp         | Terminates the call programmatically. Useful for ending conversations gracefully.                                                                 |
| playDtmfSounds | Plays dual-tone multi-frequency (dialpad) tones. See [DTMF documentation](/telephony/overview#dtmf) for sending and receiving tones.              |
| coldTransfer   | Transfers the current call to a human operator. See [Call Transfers](/telephony/call-transfers) for more details.                                 |

More information about these can be found below in [Tool Details →](#built-in-tool-details)

<Info>
  Built-in tools use the same definition structure as custom tools. You can view their complete specifications using the [List Tools API](/api-reference/tools/tools-list).
</Info>

## Using Built-in Tools

Using built-in tools is the same as using any other [custom durable tool](./custom/durable-vs-temporary-tools) that you have created except for one difference: you can override built-in tools by using the same name.

For example, if you created a durable tool named "hangUp" and then provide that tool by name (i.e. not by the toolId), then your tool would be used instead of the built-in hangUp tool.

Add built-in tools when creating agents, calls, or [call stages](/agents/call-stages):

### Using Tool Names

```js theme={null}
// Add the hangUp tool by name
{
  "systemPrompt": "You are a helpful assistant. When the conversation naturally concludes, use the 'hangUp' tool to end the call.",
  "selectedTools": [
    { "toolName": "hangUp" }
  ]
}
```

### Using Tool IDs

If you have multiple tools with the same name, you can use the unique `toolId` instead. Agents will see the `modelToolName`.

```js theme={null}
// Add the hangUp tool by ID (more explicit)
{
  "systemPrompt": "You are a helpful assistant. When the conversation naturally concludes, use the 'hangUp' tool to end the call.",
  "selectedTools": [
    { "toolId": "56294126-5a7d-4948-b67d-3b7e13d55ea7" }
  ]
}
```

### Viewing Available Tools

Use the [List Tools API](/api-reference/tools/tools-list) to see all available tools, including built-ins:

```bash theme={null}
curl -X GET "https://api.ultravox.ai/api/tools" \
  -H "X-API-Key: your-api-key"
```

<Tip>
  The List Tools API returns both built-in tools and any custom tools you've created, making it easy to see all tools available in your account.
</Tip>

### Tool Parameters

Tools can use and pass parameters (i.e. send variables to the underlying API). The parameters for each built-in tool are explained below.

See [Tool Parameters →](./custom/parameters) for details about the different types of parameters used by tools.

<Info>
  <b>Tool Parameters</b>

  <br />

  Tools can use and pass parameters (i.e. send variables to the underlying API). The parameters for each built-in tool are explained below.

  See [Tool Parameters →](./custom/parameters) to learn about the different types of parameters used by tools.
</Info>

## Built-in Tool Details

### `queryCorpus`

Searches through a knowledge base (corpus) to find relevant information (AKA RAG).

Requires the ID of the corpus (`corpus_id`) to be used for all queries and a dynamic `query` parameter is used for each query. Optionally, you can restrict the number of results that are returned to the agent (via `max_results`) along with a minimum semantic similarity score (`minimum_score`).

**Example Usage:**

```js Using queryCorpus Tool theme={null}

// Basic usage
{
  "selectedTools": [
    {
      "toolName": "queryCorpus",
      "parameterOverrides": {
        "corpus_id": "your-corpus-id-here"
      }
    }
  ]
}

// Require semantic similarity of 0.8 or higher
{
  "selectedTools": [
    {
      "toolName": "queryCorpus",
      "parameterOverrides": {
        "corpus_id": "your-corpus-id-here",
        "minimum_score": 0.8
      }
    }
  ]
}
```

#### Parameters

**Required Parameter Override:**

<ParamField type="string">
  The ID of the corpus to be used for all queries.
</ParamField>

**Dynamic Parameters:**

<ParamField type="string">
  What to search for.
</ParamField>

<ParamField type="integer">
  How many chunks to receive back. Can be any value from 1-20.
</ParamField>

**Static Parameters:**

<ParamField type="number">
  Can be used to only return content with a minimum semantic similarity score.
</ParamField>

### `leaveVoicemail`

When making outbound phone calls, used to leave a voicemail and then end the call.

A dynamic `message` parameter is used for the message that will be left. Optionally, you can change the hang up behavior with `strict` and the return message with `result`.

**Example Usage:**

```js Using leaveVoicemail Tool theme={null}

// Basic usage
{
  "selectedTools": [
    {
      "toolName": "leaveVoicemail"
    }
  ]
}
```

#### Parameters

**Dynamic Parameters:**

<ParamField type="string">
  The voicemail message to leave.
</ParamField>

**Static Parameters:**

<ParamField type="bool">
  `true` ends the call regardless of user interaction. If set to `false`, any user interaction (i.e. speech or interrupting the voicemail) will cause the call to continue.
</ParamField>

<ParamField type="string">
  The message that is returned from the tool call. Will be added to conversation history.
</ParamField>

### `hangUp`

Ends the current call programmatically.

Optionally accepts a dynamic parameter called `reason`. A static parameter called `strict` can be overridden to enable the call to continue if the user speaks and continues the call.

**Example Usage:**

```js Using hangUp Tool theme={null}
// Basic usage
{
  "systemPrompt": "Help users with their questions. When they say goodbye or the conversation naturally ends, use the hangUp tool to end the call politely.",
  "selectedTools": [
    { "toolName": "hangUp" }
  ]
}

// Enable soft hangup behavior
{
  "selectedTools": [
    {
      "toolName": "hangUp",
      "parameterOverrides": {
        "strict": false
      }
    }
  ]
}
```

#### Parameters

**Dynamic Parameters:**

<ParamField type="string">
  A brief reason for hanging up.
</ParamField>

**Static Parameters:**

<ParamField type="bool">
  `true` ends the call regardless of user interaction. If set to `false`, any user interaction (i.e. speech) will cause the call to continue.
</ParamField>

### `playDtmfSounds`

Plays telephone keypad tones (dual-tone multi-frequency signals).

Requires a dynamic parameter called `digits`. Static parameters for `toneDuration` and `spaceDuration` can be overridden. Automatically sets the sample rate based on current call medium.

**Example:**

```js Using playDtmfSounds Tool theme={null}
// Basic usage
{
  "selectedTools": [
    { "toolName": "playDtmfSounds" }
  ]
}

// Increasing length of tones and spaces
{
  "selectedTools": [
    {
      "toolName": "playDtmfSounds",
      "parameterOverrides": {
        "toneDuration": "0.5s",
        "spaceDuration": "0.3s"
      }
    }
  ]
}
```

#### Parameters

**Dynamic Parameters:**

<ParamField type="string">
  The digits for which tones should be produced. May include: 0-9, \*, #, or A-D.
</ParamField>

**Static Parameters:**

<ParamField type="string">
  The length (in seconds) that tones will be emitted.
</ParamField>

<ParamField type="string">
  The length (in seconds) that spaces (AKA silence between DTMF tones) will be emitted.
</ParamField>

### `coldTransfer`

Transfers the current call to a human operator.

Requires the transfer target. You can optionally include additional headers that will be used in the SIP REFER (or INVITE).

For bridge transfers (sip medium only), you can override the `sipVerb` parameter from `REFER` to `INVITE` when adding the tool to your agent or call. You may also wish to set `from`, `username`, and/or `password` in order to authenticate the subsequent INVITE. Note that bridge transfers will incur additional cost.

**Example Usage:**

```js Using coldTransfer Tool theme={null}

// Basic usage
{
  "selectedTools": [
    {
      "toolName": "coldTransfer",
      "parameterOverrides": {
        "target": "sip:user@mytrunk.com"
      }
    }
  ]
}

// With headers and name/description overrides
{
  "selectedTools": [
    {
      "toolName": "coldTransfer",
      "nameOverride": "escalateToManager",
      "descriptionOverride": "Transfers the call to your shift manager.",
      "parameterOverrides": {
        "target": "sip:manager@mytrunk.com",
        "extraHeaders": {
          "Referred-By": "sip:agent@mytrunk.com",
          "X-Custom-Header": "customValue"
        }
      }
    }
  ]
}

// With bridge transfer (sip medium only)
{
  "selectedTools": [
    {
      "toolName": "coldTransfer",
      "nameOverride": "escalateToManager",
      "descriptionOverride": "Transfers the call to your shift manager.",
      "parameterOverrides": {
        "target": "sip:manager@mytrunk.com",
        "extraHeaders": {
          "X-Custom-Header": "customValue"
        },
        "sipVerb": "INVITE",
        "from": "+15551234567",  // Caller ID for the INVITE. Defaults to the user's number.
        "username": "authorized_user",  // Optional username for authenticating the INVITE
        "password": "password_for_authorized_user"  // Optional password for authenticating as username
      }
    }
  ]
}
```

#### Parameters

**Required Parameter Override:**

<ParamField type="string">
  The target of the transfer. This is who the user's client should be REFER'ed to.
  A SIP URI is always allowed. A phone number in E.164 format may be allowed depending on your medium and telephony configuration.
</ParamField>

**Optional Parameters:**

<ParamField type="object">
  A string-to-string map of headers to include in the REFER (or INVITE) request. Custom headers should use the "X-" prefix to avoid conflicts with standard SIP headers.
</ParamField>

<ParamField type="string | null">
  Music to play to the user while the transfer is in progress. Set to `null` to disable hold music.
  Note that hold music will not be present in Ultravox call recordings as it is added at the SIP level.
  If you elect to use your own hold music, make sure it is either mp3 or wav, can be downloaded without authentication, and does not exceed 5MB.
  Default: <audio><source type="audio/mpeg" />"[https://storage.googleapis.com/fixie-web-public/defaultHold.mp3](https://storage.googleapis.com/fixie-web-public/defaultHold.mp3)"</audio>
</ParamField>

<ParamField type="string">
  The SIP method to use for the transfer. Can be either `REFER` (default) or `INVITE` (for bridge transfers).
</ParamField>

<ParamField type="string">
  The caller ID to use when performing an INVITE transfer. Defaults to the user's number. (Unused for REFER transfers.)
</ParamField>

<ParamField type="string">
  Optional username for authenticating the INVITE request. (Unused for REFER transfers.)
</ParamField>

<ParamField type="string">
  Optional password for authenticating as `username` in the INVITE request. (Unused for REFER transfers.)
</ParamField>

### `warmTransfer`

Transfers the current call to a human operator, with a warm handoff.

Requires the transfer target. See [call transfers](/telephony/call-transfers) for more details.

**Example Usage:**

```js Using warmTransfer Tool theme={null}

// Basic usage
{
  "selectedTools": [
    {
      "toolName": "warmTransfer",
      "parameterOverrides": {
        "target": "sip:user@mytrunk.com"
      }
    }
  ]
}

// With more customization
{
  "selectedTools": [
    {
      "toolName": "warmTransfer",
      "nameOverride": "escalateToManager",
      "descriptionOverride": "Transfers the call to your shift manager.",
      "parameterOverrides": {
        "target": "sip:manager@mytrunk.com",
        "from": "+15551234567",  // Caller ID for the INVITE. Defaults to the user's number.
        "username": "authorized_user",  // Optional username for authenticating the INVITE
        "password": "password_for_authorized_user",  // Optional password for authenticating as username
        "inviteHeaders": {
          "X-Custom-Header": "customValue"
        },
        "transferSystemPromptTemplate": "You are a drive-thru order taker at a donut shop called \"Dr. Donut.\" You've just called your manager to transfer a customer to them. You have this context from your call with the customer:\n\n{context}",
        "referHeaders": {
          "Referred-By": "sip:agent@mytrunk.com",
          "X-Custom-Header": "customValue"
        }
      }
    }
  ]
}
```

#### Parameters

**Required Parameter Override:**

<ParamField type="string">
  The target of the transfer. This is who an INVITE will be sent to for the second call.
  Must be a valid SIP URI.
</ParamField>

**Optional Parameters:**

<ParamField type="string">
  The caller ID to use for the INVITE. Defaults to the user's number.
</ParamField>

<ParamField type="string">
  Optional username for authenticating the INVITE request.
</ParamField>

<ParamField type="string">
  Optional password for authenticating as `username` in the INVITE request.
</ParamField>

<ParamField type="object">
  A string-to-string map of extra headers to include in the INVITE request. Custom headers should use the "X-" prefix to avoid conflicts with standard SIP headers.
</ParamField>

<ParamField type="string | null">
  Music to play to the user while the transfer is in progress. Set to `null` to disable hold music.
  Note that hold music will not be present in Ultravox call recordings as it is added at the SIP level.
  If you elect to use your own hold music, make sure it is either mp3 or wav, can be downloaded without authentication, and does not exceed 5MB.
  Default: <audio><source type="audio/mpeg" />"[https://storage.googleapis.com/fixie-web-public/defaultHold.mp3](https://storage.googleapis.com/fixie-web-public/defaultHold.mp3)"</audio>
</ParamField>

<ParamField type="string">
  The system prompt the agent will use when talking with the transfer target. The `{context}` variable may be added anywhere you like and will be replaced with context generated by the agent when invoking `warmTransfer` initially.
</ParamField>

<ParamField type="string">
  The type of transfer to perform once the human operator accepts the transfer. Can be either `REFER`, `BRIDGE`, or `TRY_REFER` (default). `TRY_REFER` will first attempt an in-session REFER and fall back on bridging the calls if the REFER fails.
</ParamField>

<ParamField type="object">
  A string-to-string map of extra headers to include in the REFER request (if any). Custom headers should use the "X-" prefix to avoid conflicts with standard SIP headers.
</ParamField>

## Customizing Built-in Tools

### Overriding Tool Behavior

You can customize built-in tools by overriding their names or descriptions:

```js Overriding Tool Name & Description theme={null}
{
  "selectedTools": [
    {
      "toolName": "hangUp",
      "nameOverride": "endConversation",
      "descriptionOverride": "Politely end the conversation when the user is satisfied with the help provided."
    }
  ]
}
```

### Parameter Overrides

Some built-in tools require or allow parameter overrides:

```js theme={null}
{
  "selectedTools": [
    {
      "toolName": "queryCorpus",
      "parameterOverrides": {
        "corpus_id": "corp-123",
        "maxResults": 5
      }
    }
  ]
}
```

See the guide on [Parameter Overrides →](./custom/parameter-overrides)

### Replacing Built-in Tools

You can override built-in tools by creating your own tool with the same name:

```js theme={null}
// Create a custom "hangUp" tool that logs before ending calls
{
  "name": "hangUp",
  "definition": {
    "modelToolName": "hangUp",
    "description": "Log conversation details and end the call",
    "http": {
      "baseUrlPattern": "https://your-api.com/log-and-hangup",
      "httpMethod": "POST"
    }
  }
}
```

When you reference a tool by name, your custom tool will be used instead of the built-in version.

<Warning>
  **Tool ID vs Name Priority**

  If you reference a tool by `toolId`, you'll always get that specific tool. If you reference by `toolName` and have a custom tool with the same name, your custom tool takes precedence over the built-in version.
</Warning>

## Authentication

Built-in tools handle authentication automatically - no additional setup required. However, some tools like `queryCorpus` require you to specify which corpus to search via parameter overrides.

## Next Steps

* For more advanced tool usage, see our guides on [parameter overrides](/tools/custom/parameter-overrides) and [async tools](/tools/async-tools).


# Agent Responses to Tools
Source: https://docs.ultravox.ai/tools/custom/agent-responses

Configure when and how your agent responds after tool calls - whether to speak immediately, listen for input, or speak conditionally.

## Post-Tool Call Behavior

By default, the agent speaks again immediately after a tool call. This is typically the desired behavior for tools that gather information since the agent can immediately respond based on the information retrieved.

However, this may make less sense for other tools. For example, if your agent is gathering information for the user and you have a tool that allows the agent to store what's been gathered so far, you may want the agent to speak either before or after the tool but not both.

Ultravox Realtime allows you to define how the agent reacts after a tool call by setting the `agent reaction`. A default can be set on the tool itself or you can use either the `X-Ultravox-Agent-Reaction` header (for http tools) or the `agent_reaction` field on the tool result message (for client and data connection tools) similar to how you'd set a response type (see above).

| Reaction    | Description                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| speaks      | Agent will speak immediately after the tool call returns. This is the default behavior if agent reaction is not set. Should be used for tools that gather information. |
| listens     | Agent listens for user input and doesn't speak.                                                                                                                        |
| speaks-once | Agent speaks only if it didn't speak immediately before the tool call. Prevents agent repeating things before and after the tool call.                                 |


# Tool Authentication
Source: https://docs.ultravox.ai/tools/custom/authentication

How to use auth tokens with tools.

Ultravox has rich support for tool auth. When creating a tool, you must specify what is required for successful authentication to the backend service.

## Methods for Passing Keys

Three methods for passing API keys are supported and are used when creating the tool.

### Method 1: Query Parameter

The API key will be passed via the query string. The name of the parameter must be provided when the tool is created.

```js Creating a tool with a query param auth key theme={null}
// Create a tool that uses a query parameter called 'apiKey'
{
  "name": "stock_price"
  "definition": {
    "description": "Get the current stock price for a given symbol",
    "requirements": {
      "httpSecurityOptions": {
        "options": [
          "requirements": {
            "myServiceApiKey": {
              "queryApiKey": {
                "name": "apiKey"
              }
            }
          }
        ]
      }
    }
  }
}
```

```js Providing the auth key during call creation theme={null}
// Pass the API key during call creation
// Requests will include ?apiKey=your_token_here in the url
{
  "systemPrompt": ...
  "selectedTools": [
    {
      "toolName": "stock_price"
      "authTokens": {
        "myServiceApiKey": "your_token_here"
      }
    }
  ]
}
```

### Method 2: Header

The API key will be passed via a custom header. The name of the header must be provided when the tool is created.

```js Creating a tool with a custom header auth key theme={null}
// Create a tool that uses an HTTP Header named 'X-My-Header'
{
  "name": "stock_price"
  "definition": {
    "description": "Get the current stock price for a given symbol",
    "requirements": {
      "httpSecurityOptions": {
        "options": [
          "requirements": {
            "myServiceApiKey": {
              "headerApiKey": {
                "name": "X-My-Header"
              }
            }
          }
        ]
      }
    }
  }
}
```

```js Providing the auth key during call creation theme={null}
// Pass the API key during call creation
// Requests will include the header "X-My-Header: your_token_here"
{
  "systemPrompt": ...
  "selectedTools": [
    {
      "toolName": "stock_price"
      "authTokens": {
        "myServiceApiKey": "your_token_here"
      }
    }
  ]
}
```

### Method 3: HTTP Authentication

The API key will be passed via the HTTP Authentication header. The name of the scheme (e.g. `Bearer`) must be provided when the tool is created.

```js Creating a tool that passes auth key via HTTP Authentication header theme={null}
// Create a tool that uses HTTP Authentication scheme 'Bearer'.
{
  "name": "stock_price"
  "definition": {
    "description": "Get the current stock price for a given symbol",
    "requirements": {
      "httpSecurityOptions": {
        "options": [
          "requirements": {
            "myServiceApiKey": {
              "httpAuth": {
                "scheme": "Bearer"
              }
            }
          }
        ]
      }
    }
  }
}
```

```js Providing the auth key during call creation theme={null}
// Pass the API key during call creation
// Requests will include the header "Authorization: Bearer your_token_here"
{
  "systemPrompt": ...
  "selectedTools": [
    {
      "toolName": "stock_price"
      "authTokens": {
        "myServiceApiKey": "your_token_here"
      }
    }
  ]
}
```

## Multiple Options Supported

Your tool can specify multiple options for fulfilling auth requirements (for example if your server allows either query or header auth).
Each option may also contain multiple requirements, for example if your server requires both a user\_id and an auth\_token for that user.

## Passing Keys at Call Creation Time

When defining an agent or creating a call, you pass in the key(s) in the `authTokens` property of `selectedTools`.
If the tokens you provide satisfy multiple options, the first non-empty option whose requirements are all satisfied
will be used. An unauthenticated option, if present, will only be used if no other option can be satisfied.


# Changing Call State
Source: https://docs.ultravox.ai/tools/custom/changing-call-state

Learn how to programmatically end calls or transition between call stages using special tool response types.

## Special Tool Response Types

For most tools, the response will include data you want the model to use (e.g. the results of a lookup). However, Ultravox has support for special tool actions that can end the call or change the call stage.

These tool actions require setting a special response type.

| Response Type | Tool Action                                                                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hang-up       | Terminates the call. In addition to having Ultravox end the call after [periods of user inactivity](/api-reference/calls/overview#inactivitymessages), your custom tool can end the call. |
| new-stage     | Creates a new call stage. See [here](/agents/call-stages) for more.                                                                                                                       |

How you set the response type depends on your tool implementation.
HTTP tools set the response type via the `X-Ultravox-Response-Type` header.
Client and data connection tools should set the responseType field in their tool result message.


# Durable vs. Temporary Tools
Source: https://docs.ultravox.ai/tools/custom/durable-vs-temporary-tools

Understand when to use durable tools versus temporary tools for different development stages and use cases.

Custom tools in Ultravox come in two varieties: **durable** and **temporary**. Understanding when to use each type is crucial for effective development and production deployment. Choose the approach that fits your development stage and team structure. Consider starting with temporary tools for rapid development, then graduate to durable tools for production stability and team collaboration.

## Quick Comparison

| Aspect          | Temporary Tools      | Durable Tools                                                                                    |
| --------------- | -------------------- | ------------------------------------------------------------------------------------------------ |
| **Creation**    | In call request body | Via [Tools API](/api-reference/tools/tools-post) or the [Web app](https://app.ultravox.ai/tools) |
| **Persistence** | Call-scoped only     | Permanently stored                                                                               |
| **Reusability** | Single call          | Across calls and agents                                                                          |

### Ultravox Web App Integration

<Warning>
  **Web App Compatibility**

  If you plan to use agents in the Ultravox web app or share them with team members who use the web app, you must use durable tools. Temporary tools are only available for agents created via API.
</Warning>

#### Agents Created in Web App

* **✅ Durable Tools**: Can be selected and used
* **❌ Temporary Tools**: Not supported

#### Agents Created via API

* **✅ Durable Tools**: Can be referenced by name or ID
* **✅ Temporary Tools**: Can be defined inline

```js theme={null}
// API-created agent with both tool types
{
  "name": "Hybrid Agent",
  "callTemplate": {
    "selectedTools": [
      { "toolName": "durableTool" },        // Durable tool
      { "temporaryTool": { /* definition */ } } // Temporary tool
    ]
  }
}
```

## Temporary Tools

Temporary tools are defined inline when creating a call and exist only for that specific call session.

### When to Use Temporary Tools

✅ **Early Development**: Rapid prototyping and experimentation.\
✅ **Testing New Ideas**: Quick iteration without overhead of separately creating or updating the tool.\
✅ **One-off Use Cases**: Tools needed for a single specific call.\
✅ **Development Environment**: Testing before creating durable versions.

<Warning>
  **Web App Compatibility**

  If you plan to use agents in the Ultravox web app or share them with team members who use the web app, you must use durable tools. Temporary tools are only available for agents created via API.
</Warning>

### Creating Temporary Tools

```js theme={null}
// Temporary tool defined in call creation
{
  "systemPrompt": "You are a helpful assistant...",
  "selectedTools": [
    {
      "temporaryTool": {
        "modelToolName": "sendNotification",
        "description": "Send a notification to the user",
        "dynamicParameters": [
          {
            "name": "message",
            "location": "PARAMETER_LOCATION_BODY",
            "schema": {
              "type": "string",
              "description": "Notification message to send"
            },
            "required": true
          }
        ],
        "http": {
          "baseUrlPattern": "https://api.example.com/notify",
          "httpMethod": "POST"
        }
      }
    }
  ]
}
```

### Temporary Tool Limitations

❌ **Not Reusable**: Must redefine for every call.\
❌ **No Web App Support**: Can't be used with agents created in Ultravox web app.\
❌ **API Creation Only**: Only work with agents created via API.\
❌ **No Team Sharing**: Can't share tools across team members easily.

## Durable Tools

Durable tools are created once via the Ultravox web app or Tools API and can be reused across multiple calls and agents.

### When to Use Durable Tools

✅ **Production Applications**: Stable, tested functionality.\
✅ **Web App Agents**: Required for agents created in Ultravox web app.\
✅ **Team Collaboration**: Share tools across team members or split ownership of tools from the rest of your agent.\
✅ **Reusable Functionality**: Use same tool across multiple agents.\
✅ **Stable APIs**: When tool definitions won't change frequently.

### Creating Durable Tools

See the [Tools Quickstart →](gettingstarted/quickstart/tools#creating-a-custom-tool) for an introduction to creating a durable tool using the Ultravox web app.

```bash Creating a durable tool via API theme={null}
curl -X POST "https://api.ultravox.ai/api/tools" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "name": "sendNotification",
    "definition": {
      "modelToolName": "sendNotification",
      "description": "Send a notification to the user",
      "dynamicParameters": [
        {
          "name": "message",
          "location": "PARAMETER_LOCATION_BODY",
          "schema": {
            "type": "string",
            "description": "Notification message to send"
          },
          "required": true
        }
      ],
      "http": {
        "baseUrlPattern": "https://api.example.com/notify",
        "httpMethod": "POST"
      }
    }
  }'
```

### Using Durable Tools

Durable tools are added at call creation time via the `selectedTools` array and can be added by name or ID.

```js Reference durable tool by name or ID theme={null}
{
  "systemPrompt": "You are a helpful assistant...",
  "selectedTools": [
    { "toolName": "sendNotification" }
    // or
    // { "toolId": "tool-uuid-here" }
  ]
}
```

### Durable Tool Limitations

❌ **Slower Iteration**: Requires API calls or using the web app to create/update.\
❌ **API Dependency**: Need to manage tool lifecycle via the Ultravox web app or API.\
❌ **Update Overhead**: Changes affect all existing usage.

## Recommended Development Workflow

<Steps>
  <Step title="Prototype with Temporary Tools">
    Start with temporary tools for rapid iteration and testing

    ```js theme={null}
    // Quick prototype in call creation
    {
      "selectedTools": [
        { "temporaryTool": { /* your tool definition */ } }
      ]
    }
    ```
  </Step>

  <Step title="Stabilize and Test">
    Refine your tool definition through multiple iterations

    ```js theme={null}
    // Update tool definition and test with new calls
    {
      "temporaryTool": {
        "modelToolName": "improvedTool",
        "description": "Updated description...",
        // refined parameters and implementation
      }
    }
    ```
  </Step>

  <Step title="Create Durable Version">
    Once stable, create a durable tool for production use

    ```bash theme={null}
    # Create production-ready durable tool
    curl -X POST "https://api.ultravox.ai/api/tools" \
      -H "X-API-Key: your-api-key" \
      -d '{ "name": "finalTool", "definition": { /* stable definition */ } }'
    ```
  </Step>

  <Step title="Deploy and Reuse">
    Use the durable tool across all agents and applications

    ```js theme={null}
    {
      "selectedTools": [
        { "toolName": "finalTool" }
      ]
    }
    ```
  </Step>
</Steps>


# HTTP vs. Client Tools
Source: https://docs.ultravox.ai/tools/custom/http-vs-client-tools

Choose the right tool implementation for your use case.

<Info>
  <b>Real Tool Execution</b>

  Unlike using tools with single-generation LLM APIs, Ultravox Realtime actually calls your tool. This means you need to do a bit more work upfront in defining tools with the proper authentication and parameters.
</Info>

Ultravox supports three primary types of tool implementations: HTTP tools, Client tools, and Data Connection tools. Each has distinct advantages and use cases.

## HTTP Tools

HTTP tools (AKA "server tools") are the most common and flexible option. Your tool runs on your server, and Ultravox calls it via HTTP requests during conversations.

### How HTTP Tools Work

1. Agent triggers tool during conversation.
2. Ultravox sends HTTP request to your server.
3. Your server processes the request and returns a response.
4. Agent continues conversation with the tool result.

```js Example HTTP tool definition theme={null}
{
  "temporaryTool": {
    "modelToolName": "lookupCustomer",
    "description": "Look up customer information by phone number",
    "dynamicParameters": [
      {
        "name": "phoneNumber",
        "location": "PARAMETER_LOCATION_BODY",
        "schema": {
          "type": "string",
          "description": "Customer's phone number"
        },
        "required": true
      }
    ],
    "http": {
      "baseUrlPattern": "https://your-api.com/customers/lookup",
      "httpMethod": "POST"
    }
  }
}
```

### HTTP Tool Advantages

✅ **Server-side logic**: Full access to databases, APIs, and business logic\
✅ **Any call medium**: Works with WebRTC, telephony, and websockets\
✅ **Scalable**: Runs on your infrastructure with your scaling strategies\
✅ **Secure**: Keep sensitive data and credentials on your servers\
✅ **Language agnostic**: Implement in any programming language

### HTTP Tool Implementation

```js Example of a simple API endpoint for HTTP tool theme={null}
// Express.js example
app.post('/customers/lookup', async (req, res) => {
  try {
    const { phoneNumber } = req.body;
    
    // Look up customer in database
    const customer = await db.customers.findByPhone(phoneNumber);
    
    if (!customer) {
      return res.status(200).json({
        message: "No customer found with that phone number. Please verify the number and try again."
      });
    }
    
    return res.status(200).json({
      message: `Found customer: ${customer.name}, Account type: ${customer.tier}, Last contact: ${customer.lastContact}`
    });
  } catch (error) {
    return res.status(500).json({
      message: "Unable to look up customer information at this time."
    });
  }
});
```

### Error Handling

Return appropriate HTTP status codes:

```js theme={null}
// Success
res.status(200).json({ message: "Operation completed" });

// Client error  
res.status(400).json({ message: "Invalid input provided" });

// Server error
res.status(500).json({ message: "Internal server error" });
```

## Client Tools

Client tools run directly in the client application using our SDKs. They're perfect for UI interactions and client-side operations.

Client tools work best with our client SDKs, which are designed for the webrtc call medium. See [Client Tools](/sdk-reference/introduction#client-tools) to learn how those are registered and used with the [Ultravox Client SDK](/sdk-reference/).

You can also use client tools with a websocket medium. See the `ClientToolInvocation` and `ClientToolResult` [data messages](/apps/datamessages).

If you want a similar experience to client tools with a telephony medium, you have two options:

* Handle telephony using [voximplant](/integrations/voximplant) and define your tools in your voximplant session code.
* Use a [Data Connection Tool](#data-connection-tools).

### How Client Tools Work

1. Agent triggers tool during conversation.
2. Ultravox sends tool invocation to your client.
3. Your client code executes the tool logic.
4. Client sends result back to Ultravox.
5. Agent continues conversation with the tool result.

```js Example client tool definition theme={null}
{
  "temporaryTool": {
    "modelToolName": "updateUserInterface",
    "description": "Update the user interface to show relevant information",
    "dynamicParameters": [
      {
        "name": "content",
        "location": "PARAMETER_LOCATION_BODY",
        "schema": {
          "type": "string",
          "description": "Content to display in the UI"
        },
        "required": true
      }
    ],
    "client": {}
  }
}
```

### Client Tool Advantages

✅ **UI integration**: Direct access to update interface elements\
✅ **Low latency**: No network round trip to your servers\
✅ **Client-side data**: Access to local storage, camera, microphone\
✅ **Real-time updates**: Immediate visual feedback

### Client Tool Implementation

```js Example of client tool implementation theme={null}
// Using Ultravox Client SDK
import { UltravoxSession } from 'ultravox-client';

const session = new UltravoxSession();

// Register client tool handler
session.registerClientTool("updateUserInterface", (parameters) => {
  const { content } = parameters;
  
  // Update your UI
  document.getElementById('chat-display').innerHTML = content;
  
  return {
    responseText: "Interface updated successfully",
    responseType: "tool-response"
  };
});
```

### Error Handling

Return error information in the response:

```js theme={null}
return {
  responseText: "Unable to update interface: element not found",
  responseType: "tool-response"
};
```

## Data Connection Tools

A third option combines benefits of both: Data Connection tools run on your server but communicate via websocket, enabling both server-side logic and real-time capabilities.

Data connections are like another participant in your call. Like the client, they can receive tool invocation messages and can send back tool result messages. Implementation lives in your websocket server and can be used regardless of the call medium used.

```js Example Data Connection tool definition theme={null}
{
  "temporaryTool": {
    "modelToolName": "processPayment",
    "description": "Process a payment transaction",
    "dataConnection": {}
  }
}
```

Data connection tools are ideal for:

* Long-running operations
* Real-time data streaming
* Complex server operations that need immediate feedback

## Choosing the Right Tool Type

**Use HTTP Tools When:**

* Accessing databases or external APIs
* Processing sensitive data
* Performing server-side calculations
* Sending emails or notifications
* Working with telephony (Twilio, etc.)
* Need authentication with external services

**Use Client Tools When:**

* Updating user interface elements
* Accessing client device features (camera, microphone)
* Performing client-side validation
* Managing local application state
* Need immediate visual feedback
* Working with WebRTC calls primarily

**Use Data Connection Tools When:**

* Need both server logic and real-time feedback
* Handling long-running operations
* Streaming real-time data
* Complex workflows requiring immediate updates

## Call Medium Compatibility

| Tool Type       | WebRTC | Websocket | Telephony |
| --------------- | ------ | --------- | --------- |
| HTTP            | ✅      | ✅         | ✅         |
| Client          | ✅      | ✅         | ❌         |
| Data Connection | ✅      | ✅         | ✅         |

## Authentication

**HTTP Tools**: Full authentication support including API keys, tokens, and custom headers. See [Tools Authentication →](./authentication)

**Client Tools**: No built-in authentication - handle security in your client application.

**Data Connection Tools**: Authentication handled via websocket connection setup.


# Overview: Custom Tools
Source: https://docs.ultravox.ai/tools/custom/overview

Create powerful integrations that enable your agent to communicate with external systems and perform real-world actions.

Custom tools enable you to communicate with the outside world. Anything that you can do in a function can now be done by your agent via a custom tool.

<Tip>
  <b>Adding Tools for an Existing API</b>

  If you already run a server with a well-defined OpenAPI spec, you can quickly create tools for all your API endpoints by
  [uploading that spec](/api-reference/tools/tools-post). Your OpenAPI spec must be either `json` or `yaml` format.

  Once uploaded, your tools are just like any other durable tool, so you can use, modify, or delete them as you wish.
</Tip>

## Creating Your First Custom Tool

Let's look at creating a tool that sends an email with a summary of the conversation.

There are three steps:

### Step 1:  Define the Tool

We need to define the tool and provide it to our agent. The name, description, and parameters we provide here will be seen by the agent so we need to be thoughtful with them.

```js Creating a custom tool theme={null}
// Creating a tool called 'sendConversationSummary'
//
// A 'string' parameter named 'conversationSummary'
// is passed in the body of a POST request to https://foo.bar/sendSummary
{
  "systemPrompt": "You are a helpful assistant...",
  "selectedTools": [
    {
      "temporaryTool": {
        "modelToolName": "sendConversationSummary",
        "description": "Use this tool at the end of a conversation to send the caller a summary of the conversation.",
        "dynamicParameters": [
          {
            "name": "conversationSummary",
            "location": "PARAMETER_LOCATION_BODY",
            "schema": {
              "description": "A 2-3 sentence summary of the conversation.",
              "type": "string"
            },
            "required": true
          }
        ],
        "http": {
          "baseUrlPattern": "https://foo.bar/sendSummary",
          "httpMethod": "POST"
        }
      }
    }
  ]
}
```

What's happening here:

* We are adding `selectedTools` to the request body of the [Create Call](/api-reference/calls/calls-post) API request.
* There's a single tool named `sendConversationSummary`.
* This tool requires a single [dynamic parameter](./parameters#dynamic-parameters) called `conversationSummary` that is passed in the request body.
* The tool's functionality is available via POST at the url `https://foo.bar/sendSummary`.
* The tool is a [temporary tool](./durable-vs-temporary-tools#temporary-tools), so it will only be available for this call.

### Step 2:  Implement the Function

Now that we've defined the tool, let's implement the functionality. This is a simplified example using Express.js and imagines a generic email API provider.

```js Simple API endpoint theme={null}
const express = require('express');
const router = express.Router();

router.post('/sendSummary', async (req, res) => {
  try {
    const { conversationSummary } = req.body;

    // Send the email using our email provider
    sendEmail(conversationSummary);

    return res.status(200).json({
      message: 'Conversation summary sent successfully. Continue the conversation with the user.'
    });
  } catch (error) {
    return res.status(500).json({
      message: 'Internal server error',
      error: error.message
    });
  }
});

module.exports = router;
```

This function does the following:

* Accepts the `conversationSummary` via a POST.
* Passes the data along to another function (`sendEmail`) that will send it via email.

### Step 3:  Instruct the Agent on Tool Use

The last thing we need to do is provide additional instructions to the agent on how to use the tool. This is primarily done using the tool's own description along with the `systemPrompt`. Let's update what we used in the first step.

```js Prompting the agent on how to use the tool theme={null}
const updatedPrompt = `
You're a friendly and fun guy. You like to chat casually while learning 
more about the person you're chatting with (name, hobbies, likes/dislikes).

Be casual. Be fun to chat with. Don't talk too much. Keep your sentences 
pretty short and fun. Let the user guide the conversation.

As you chat, try and learn more about the person you are talking to such 
as their name, hobbies, and their likes/dislikes.

Once you have all the information, call the 'sendSummary' tool to send 
a summary of the conversation.
`;
{
  "systemPrompt": updatedPrompt,
  "selectedTools": [
      // Same as before
  ]
}
```

We've updated the system prompt that is used when the Ultravox call is created to instruct the agent when and how to use the tool.

## Debugging Tool Calls

The Ultravox SDK enables viewing [debug messages](/sdk-reference/introduction#debug-messages) for any active call. These messages include tool calls.

## Keep Learning

* Learn all about [Tool Parameters →](./parameters)
* Learn how to secure tool calls in [Tool Authentication →](./authentication)
* Check out our [API reference](/api-reference/tools) for all tools endpoints.


# Parameter Overrides
Source: https://docs.ultravox.ai/tools/custom/parameter-overrides

Advanced parameter customization for fine-tuned tool behavior across different agents and calls.

Parameter overrides allow you to customize tool behavior without modifying the base tool definition. This powerful feature enables tool reuse across different contexts while maintaining specific configurations for each use case.

## Parameter Override Capabilities

### Override Dynamic Parameters

Convert dynamic parameters to static values for specific use cases:

```js theme={null}
// Base tool: Generic stock lookup
{
  "name": "stockPrice",
  "definition": {
    "modelToolName": "stockPrice",
    "description": "Get current stock price for any symbol",
    "dynamicParameters": [
      {
        "name": "symbol",
        "location": "PARAMETER_LOCATION_QUERY",
        "schema": {
          "type": "string",
          "description": "Stock symbol (e.g., AAPL, GOOGL)"
        },
        "required": true
      }
    ]
  }
}

// Override for NVIDIA-specific agent
{
  "selectedTools": [
    {
      "toolName": "stockPrice",
      "nameOverride": "nvidiaStockPrice",
      "descriptionOverride": "Get current NVIDIA stock price",
      "parameterOverrides": {
        "symbol": "NVDA" // AI won't see this parameter anymore
      }
    }
  ]
}
```

### Override Static Parameters

Modify static parameter values for different environments or configurations:

```js theme={null}
// Base tool with production API endpoint
{
  "name": "processPayment",
  "staticParameters": [
    {
      "name": "environment",
      "location": "PARAMETER_LOCATION_BODY",
      "value": "production"
    },
    {
      "name": "timeout",
      "location": "PARAMETER_LOCATION_BODY", 
      "value": 30
    }
  ]
}

// Override for testing environment
{
  "selectedTools": [
    {
      "toolName": "processPayment",
      "parameterOverrides": {
        "environment": "sandbox", // Override static value
        "timeout": 10 // Shorter timeout for testing
      }
    }
  ]
}
```

## Required Parameter Overrides

Some tools require certain parameters to be overridden at call creation time. This is common with built-in tools that need context-specific configuration.

### Example: queryCorpus Tool

The built-in `queryCorpus` tool requires the corpus ID to be specified:

```js theme={null}
{
  "selectedTools": [
    {
      "toolName": "queryCorpus",
      "parameterOverrides": {
        "corpusId": "your-corpus-id-here" // Required override
      }
    }
  ]
}
```

### Creating Tools with Required Overrides

```js theme={null}
{
  "name": "customerQuery",
  "definition": {
    "modelToolName": "customerQuery",
    "description": "Query customer database",
    "requirements": {
      "requiredParameterOverrides": ["databaseId"] // Must be overridden
    },
    "dynamicParameters": [
      {
        "name": "databaseId",
        "location": "PARAMETER_LOCATION_QUERY",
        "schema": { "type": "string" },
        "required": true
      },
      {
        "name": "searchTerm", 
        "location": "PARAMETER_LOCATION_BODY",
        "schema": { "type": "string" },
        "required": true
      }
    ]
  }
}

// Usage requires databaseId override
{
  "selectedTools": [
    {
      "toolName": "customerQuery",
      "parameterOverrides": {
        "databaseId": "prod-customers" // Required
        // searchTerm remains dynamic for the AI to set
      }
    }
  ]
}
```

## Advanced Override Patterns

### Multi-Environment Tool Configuration

```js theme={null}
// Base tool definition
{
  "name": "emailService",
  "definition": {
    "modelToolName": "sendEmail",
    "staticParameters": [
      {
        "name": "apiEndpoint",
        "location": "PARAMETER_LOCATION_HEADER",
        "value": "https://api.production-email.com"
      },
      {
        "name": "fromAddress",
        "location": "PARAMETER_LOCATION_BODY",
        "value": "noreply@production.com"
      }
    ]
  }
}

// Development environment override
const devEmailConfig = {
  "toolName": "emailService",
  "parameterOverrides": {
    "apiEndpoint": "https://api.dev-email.com",
    "fromAddress": "noreply@dev.com"
  }
};

// Staging environment override  
const stagingEmailConfig = {
  "toolName": "emailService",
  "parameterOverrides": {
    "apiEndpoint": "https://api.staging-email.com",
    "fromAddress": "noreply@staging.com"
  }
};
```

### Feature-Specific Tool Variants

```js theme={null}
// Base search tool
{
  "name": "searchProducts",
  "dynamicParameters": [
    {
      "name": "query",
      "location": "PARAMETER_LOCATION_BODY",
      "schema": { "type": "string" },
      "required": true
    },
    {
      "name": "category",
      "location": "PARAMETER_LOCATION_BODY", 
      "schema": { "type": "string" },
      "required": false
    },
    {
      "name": "maxResults",
      "location": "PARAMETER_LOCATION_BODY",
      "schema": { "type": "integer" },
      "required": false
    }
  ]
}

// Electronics-focused agent
{
  "selectedTools": [
    {
      "toolName": "searchProducts",
      "nameOverride": "searchElectronics",
      "descriptionOverride": "Search for electronic products",
      "parameterOverrides": {
        "category": "electronics", // Lock to electronics
        "maxResults": 5 // Limit results
      }
    }
  ]
}

// Quick search variant
{
  "selectedTools": [
    {
      "toolName": "searchProducts", 
      "nameOverride": "quickSearch",
      "descriptionOverride": "Quick product search (top 3 results)",
      "parameterOverrides": {
        "maxResults": 3 // Quick results only
      }
    }
  ]
}
```

### Authentication Context Overrides

```js theme={null}
// Multi-tenant tool
{
  "name": "databaseQuery",
  "staticParameters": [
    {
      "name": "tenantId",
      "location": "PARAMETER_LOCATION_HEADER",
      "value": "default"
    }
  ],
  "automaticParameters": [
    {
      "name": "authToken",
      "location": "PARAMETER_LOCATION_HEADER", 
      "knownValue": "KNOWN_PARAM_CALL_STATE"
    }
  ]
}

// Tenant-specific override
{
  "selectedTools": [
    {
      "toolName": "databaseQuery",
      "parameterOverrides": {
        "tenantId": "customer-abc-123"
      }
    }
  ]
}
```

## Template Variables in Overrides

When using agents, parameter overrides can include template variables:

```js theme={null}
// Agent with template-based overrides
{
  "name": "Customer Service Agent",
  "callTemplate": {
    "selectedTools": [
      {
        "toolName": "customerLookup",
        "parameterOverrides": {
          "customerId": "{{customerId}}", // Template variable
          "region": "{{customerRegion}}"
        }
      }
    ]
  }
}

// Call creation with template context
{
  "templateContext": {
    "customerId": "cust-456789",
    "customerRegion": "us-west"
  }
}
```


# Tool Parameters
Source: https://docs.ultravox.ai/tools/custom/parameters

Learn about dynamic, static, and automatic tool parameters.

Tool parameters define what gets passed to your backend function when the tool is called. When creating a tool, parameters are defined as one of three types:

<Steps>
  <Step title="Dynamic">The model will choose which values to pass. These are the parameters you'd use for a single-generation LLM API.</Step>
  <Step title="Static">This value is known when the tool is defined and is unconditionally set on invocations. The parameter is not exposed to or set by the model.</Step>
  <Step title="Automatic">Like "Static", except that the value may not be known when the tool is defined but will instead be populated by the system when the tool is invoked.</Step>
</Steps>

## Dynamic Parameters

Dynamic parameters will have their values set by the model. Creating a dynamic parameter on a tool looks like this:

```js Adding a dynamic parameter to a tool theme={null}
// Adding a dynamic parameter to a stock price tool
// The parameter will be named 'symbol' and will be passed as a query parameter
{
  "name": "stock_price",
  "description": "Get the current stock price for a given symbol",
  "dynamicParameters": [
    {
      "name": "symbol",
      "location": "PARAMETER_LOCATION_QUERY",
      "schema": {
        "type": "string",
        "description": "Stock symbol (e.g., AAPL for Apple Inc.)"
      },
      "required": true
    }
  ]
}
```

### Parameter Overrides

You can choose to set static values for dynamic parameters when you create an agent or start a call. The model won't see any parameters that you override. When creating a call simply pass in the overrides with each tool, as below. You should also consider overriding the tool name or description to give the model a more specific understanding of what the tool will do in this case.

```js Overriding a dynamic parameter with a static value theme={null}
// Overriding dynamic parameter when starting a new call
// Always set the stock symbol to 'NVDA'
{
  "systemPrompt": ...
  "selectedTools": [
    "toolName": "stock_price",
    "nameOverride": "nvidia_stock_price",
    "descriptionOverride": "Looks up the current stock price for Nvidia.",
    "parameterOverrides": {
      "symbol": "NVDA"
    }
  ]
}
```

## Static Parameters

If you have parameters that are known at the time you create the tool, static parameters can be used. Static parameters are not exposed to or set by the LLM.

```js Adding a static parameter to a tool theme={null}
// Adding a static parameter that always sends utm=ultravox
{
  "name": "stock_price",
  "description": "Get the current stock price for a given symbol",
  "staticParameters": [
    {
      "name": "utm",
      "location": "PARAMETER_LOCATION_QUERY",
      "value": "ultravox"
    }
  ]
}
```

### Parameter Overrides

Static parameters can also be overridden when you create an agent or start a call. This is most useful with built-in tools.
For example, the built-in `queryCorpus` tool allows you to statically override `max_results`.

See [queryCorpus Tool →](/tools/built-in-tools#querycorpus) for more.

## Automatic Parameters

Automatic parameters are used when you want a consistent, predictable value (not generated by the model) but you don't know the value when the tool is created.

Here are some of the most common automatic parameters:

| knownValue                          | Description                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| KNOWN\_PARAM\_CALL\_ID              | Used for sending the current Ultravox call ID to the tool.                                                         |
| KNOWN\_PARAM\_CONVERSATION\_HISTORY | Includes the full conversation history leading up to this tool call. Typically should be in the body of a request. |
| KNOWN\_PARAM\_CALL\_STATE           | Includes arbitrary state previously set by tools. See [Guiding Agents](/agents/guiding-agents#tool-state).         |

More details can be found in the [Tool Definition Schema →](/api-reference/schema/base-tool-definition#schema-automatic-parameters)

```js Adding an automatic parameter to a tool theme={null}
// Adding automatic parameters to a profile creation tool
// There are two parameters added:
// 'call_id' which is sent as a query param
// 'conversation_history' which is sent in the request body
{
  "name": "create_profile",
  "description": "Creates a profile for the current caller",
  "automaticParameters": [
    {
      "name": "call_id",
      "location": "PARAMETER_LOCATION_QUERY",
      "knownValue": "KNOWN_PARAM_CALL_ID"
    },
    {
      "name": "conversation_history",
      "location": "PARAMETER_LOCATION_BODY",
      "knownValue": "KNOWN_PARAM_CONVERSATION_HISTORY"
    }
  ]
}
```

## Required Parameter Overrides

Sometimes your tool will require a parameter to function that you need to have defined when the call is created instead of having the model come up with a value. In these cases, you can require that the parameter be overridden at call creation.  For example, the built-in `queryCorpus` tool requires the corpus id to be specified during call creation.

More advanced information can be found in [Parameter Overrides →](/tools/custom/parameter-overrides)


# Overview: Tools
Source: https://docs.ultravox.ai/tools/overview

Give your agents additional capabilities while maintaining a natural conversation flow.

<ToolsPossibilities />

## Types of Tools

### Built-in Tools

Ultravox provides several ready-to-use tools for common functionality:

* **queryCorpus**: Retrieve information from knowledge bases.
* **playDtmfSounds**: Play dial tones for telephony applications.
* **leaveVoicemail**: Leaves voicemail message and ends the call.
* **hangUp**: End calls programmatically.

[Learn more about Built-in Tools →](/tools/built-in-tools)

### Custom Tools

Create your own tools to integrate with any external system or API. Custom tools can:

* Send emails or notifications
* Look up customer information
* Process payments
* Update databases
* Integrate with third-party services

[Learn more about Custom Tools →](/tools/custom/overview)

## Tool Implementation Types

**HTTP Tools**: Most common type - your tool runs on your server and Ultravox calls it via HTTP.

**Client Tools**: Run directly in the client application using our SDKs.

[Compare HTTP vs Client Tools →](/tools/custom/http-vs-client-tools)

## Tool Persistence

**Durable Tools**: Created once via API or the web app, reused across calls and agents. Best for production.

**Temporary Tools**: Defined per-call, great for testing and rapid iteration.

[Learn about Durable vs Temporary Tools →](/tools/custom/durable-vs-temporary-tools)

## Getting Started with Tools

Ready to build your first tool? [Check out the Tools Quickstart →](/gettingstarted/quickstart/tools)

## Keep Building

* Learn about [Built-in Tools](./built-in-tools) you can use.
* Dig into [HTTP vs. Client Tools](./custom/http-vs-client-tools) to understand the differences.
* Read about [Durable vs. Temp Tools](./custom/durable-vs-temporary-tools).


# Crawling Websites
Source: https://docs.ultravox.ai/tools/rag/crawling-websites

Build a corpus source by crawling your website.

\[Under Construction]


# Overview: RAG
Source: https://docs.ultravox.ai/tools/rag/overview

Give you agent access to product documents, KBs, and more.

LLMs have tremendous knowledge about the world, but they don't have all the up-to-date specifics about your organization, your products, or other relevant information you might want to provide to your AI voice agents.

RAG is a common technique for grounding agents in the relevant information for your use case.

## Examples of Knowledge Sources

Let's consider some of the content that might be useful to serve some popular use cases:

**Customer Success & Support:**

* **Product Documentation** → user guides, FAQs, troubleshooting steps.
* **Onboarding Materials** → getting started guides, best practices, transcripts from training videos.

**Customer Acquisition:**

* **Product Information** → features, pricing tiers, competitive comparisons.
* **Sales Scripts** → qualification questions, objection handling, industry-specific use cases.

**Operations:**

* **Internal Processes** → call routing rules, department directories.
* **Survey Materials** → question banks, follow-up questions, rating scales.

## Adding RAG to Ultravox

As we saw in the [Tools](/tools/overview) overview, tools provide power-ups for your agents. To use RAG with an Ultravox agent, it's as simple as using the built-in `queryCorpus` tool and instructing the agent on how to use the tool.

### Using the Web App

The easiest way to create a new knowledge base (we call them `Corpora`) is to use the Ultravox web application. You can also [use the API](#using-the-api).

<Steps>
  <Step title="Create a Corpus">
    * Go to [RAG](https://app.ultravox.ai/rag) in the Ultravox web app.
    * Click `New Source` in the top right corner.

    <img />

    <img />

    * Under `Collection` click on `New Collection`.
    * Give it a `Name` and `Description` then click `Save`.
  </Step>

  <Step title="Create a Source">
    * Select the `Collection` you just created.
    * Add a `Name` and `Description` for the new source.
    * Click `Web` and then add any URLs to be crawled.
    * Click `Save` and then wait a few moments for the pages to be crawled and the content to be ingested.

    <img />

    <img />
  </Step>

  <Step title="Use the queryCorpus Tool">
    Give the built-in [queryCorpus](/tools/built-in-tools#querycorpus) tool. to your agents and provide the `corpusId`. For example, if we wanted to create a voice agent to answer questions about Seattle, we could provide the tool like this:

    ```json theme={null}
    {
      "systemPrompt": "Use the queryCorpus tool to answer questions about Seattle.",
      "selectedTools": [
        {
          "toolName": "queryCorpus", 
          "parameterOverrides": {
            "corpus_id": "<your_corpus_id_here>",
            "max_results": 5
          }
        }
      ]
    }
    ```
  </Step>
</Steps>

### Using the API

Ultravox provides the [corpus service](/api-reference/corpora/) for RAG.

<Steps>
  <Step title="Create a Corpus">
    Use the [Create Corpus](/api-reference/corpora/corpora-post) endpoint. Give your new corpus a name and (optional) description. This returns a `corpusId`.
  </Step>

  <Step title="Create a Source">
    Add a website to crawl using [Create Corpus Source](/api-reference/corpora/corpora-sources-post). Each source is given a unique `sourceId`. We will crawl the URL(s) and ingest all the content.
  </Step>

  <Step title="Query the Corpus">
    After everything is loaded, try some queries using the [Query Corpus](/api-reference/corpora/corpus-query) endpoint.
  </Step>

  <Step title="Use the queryCorpus Tool">
    Give the built-in [queryCorpus](/tools/built-in-tools#querycorpus) tool. to your agents and provide the `corpusId`. For example, if we wanted to create a voice agent to answer questions about Seattle, we could provide the tool like this:

    ```json theme={null}
    {
      "systemPrompt": "Use the queryCorpus tool to answer questions about Seattle.",
      "selectedTools": [
        {
          "toolName": "queryCorpus", 
          "parameterOverrides": {
            "corpus_id": "<your_corpus_id_here>",
            "max_results": 5
          }
        }
      ]
    }
    ```
  </Step>
</Steps>

### Using External Vector DB

Let's assume we have already stored our product documentation in a vector database and can search that content at `https://foo.bar/lookupProductInfo`.

All you need to do is create a custom tool that uses the external API and then give the tool to your agent.

Here's how we might create a tool for our Ultravox agent to use:

```js Example: Adding an external RAG tool theme={null}
{
  "systemPrompt": "You are a helpful assistant. You have a tool called 'lookupProductInfo' that you must use to find answers.",
  "model": "ultravox-v0.7",
  "selectedTools": [
    {
      "temporaryTool": {
        "modelToolName": "lookupProductInfo",
        "description": "Searches official product documentation using semantic similarity to find relevant information. Use this tool to look up specific product features, specifications, limitations, pricing, or support information. The tool returns the most relevant text chunks from the documentation.",
        "dynamicParameters": [
          {
            "name": "query",
            "location": "PARAMETER_LOCATION_BODY",
            "schema": {
              "description": "A specific, focused search query to find relevant product information",
              "type": "string"
            },
            "required": true
          }
        ],
        "http": {
          "baseUrlPattern": "https://foo.bar/lookupProductInfo",
          "httpMethod": "POST"
        }
      }
    }
  ]
}
```

## Learn More

* Learn more about [Crawling Websites](./crawling-websites) for your knowledge base.
* Add [Static Documents](./using-static-documents) for RAG.
* Explore the full [Corpus API reference](/api-reference/corpora/overview).


# Using Static Documents
Source: https://docs.ultravox.ai/tools/rag/using-static-documents

Use text, PDF, Word, and other documents in your corpus.

You can use files as sources for any of your corpora.

Files can be added via the [Web App](https://app.ultravox.ai/rag) or via the [Create Corpus File Upload API](/api-reference/corpora/corpora-uploads-post).

## Upload Files via Web App

<Steps>
  <Step title="Create New Source">
    * Go to [RAG](https://app.ultravox.ai/rag) in the Ultravox web application.
    * Click `New Source` in the top right corner.
  </Step>

  <Step title="Add Details and Files">
    * Select the `Collection` to which you want to add the content.
    * (Optionally) Add a `Name` and `Description` for the new source.
    * Select `Document` and add files.

    <img />

    <img />
  </Step>

  <Step title="Save">
    * Click `Save` and wait a few moments for your content to be uploaded and ingested.
  </Step>
</Steps>

## Upload Files via API

To upload files using the API, follow these steps:

<Steps>
  <Step title="Step 1: Request Upload URL">
    * Use the [Create Corpus File Upload API](/api-reference/corpora/corpora-uploads-post)
    * Include the MIME type string in the request body
    * This returns the URL to use for upload and the unique ID for the document
    * URLs expire after 5 minutes. Request a new one if it expires before using it

    <Note>The URL that is returned is tied to the provided MIME type. The same MIME type must be used during upload.</Note>
  </Step>

  <Step title="Step 2: Upload File">
    * Use the `presignedUrl` from Step 1 to upload the document
    * Ensure the MIME type in the upload matches what was specified in Step 1

    For example, if we requested an upload URL for a text file (MIME type `text/plain`):

    ```bash theme={null}
    FILE_PATH="/path/to/your/file"
    UPLOAD_URL="https://storage.googleapis.com/fixie-ultravox-prod/..."

    curl -X PUT \
      -H "Content-Type: text/plain" \
      --data-binary @"$FILE_PATH" \
      "$UPLOAD_URL"
    ```
  </Step>

  <Step title="Step 3: Create New Source with Uploaded Document">
    * Use the [Create Corpus Source API](/api-reference/corpora/corpora-sources-post)
    * Use `upload` to provide the `documentId` from Step 1

    <Note>You can provide an array of Document IDs to bulk create a source.</Note>
  </Step>
</Steps>

## Supported File Types

The following types of static files are currently supported:

| File Extension | Type of File                               | MIME Type                                                                 |
| -------------- | ------------------------------------------ | ------------------------------------------------------------------------- |
| doc            | Microsoft Word Document                    | application/msword                                                        |
| docx           | Microsoft Word Open XML Document           | application/vnd.openxmlformats-officedocument.wordprocessingml.document   |
| txt            | Plain Text Document                        | text/plain                                                                |
| md             | Markdown Document                          | text/markdown                                                             |
| ppt            | Microsoft PowerPoint Presentation          | application/vnd.ms-powerpoint                                             |
| pptx           | Microsoft PowerPoint Open XML Presentation | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| pdf            | Portable Document Format                   | application/pdf                                                           |

## Limits

See the [Overall Limits](/api-reference/corpora/overview#overall-limits) section for details on limits for the number of sources, file sizes, and more.


# Tutorial: Customer Escalation with Call Stages
Source: https://docs.ultravox.ai/tutorials/callstages

Learn how to implement customer service escalation in Ultravox using call stages to handle customer complaints by transferring them to a manager.

Learn how to implement customer service escalation in Ultravox using call stages to handle customer complaints by transferring them to a manager.

**What you'll learn:**

* How to implement an escalation tool
* How to use call stages to switch conversation context
* How to handle manager takeover with a new system prompt
* Testing escalation scenarios

**Time to complete:** 25 minutes

## Prerequisites

Before starting this tutorial, make sure you have:

* Basic knowledge of TypeScript and React
* The starter code from our [tutorial repository](https://github.com/fixie-ai/ultravox-tutorial-call-stages)
* Node.js 16+ installed on your machine
* [ngrok](https://ngrok.com/docs/getting-started/) installed on your machine

## Understanding Call Stages

Call stages in Ultravox enable dynamic changes to an ongoing conversation by:

* Switching system prompts mid-conversation
* Changing voice personalities
* Maintaining conversation context
* Handling role transitions seamlessly

In this tutorial, we'll use call stages to transfer angry customers to a manager who can better handle their complaints.

## Project Overview: Dr. Donut Manager Escalation

We'll build an escalation system for our Dr. Donut drive-thru that allows the AI agent to transfer difficult situations to a manager. The system will:

1. Recognize when a customer needs manager assistance
2. Collect complaint details
3. Switch to a manager persona with authority to resolve issues

### Implementation Steps

<Steps>
  <Step title="Set Up ngrok">
    Enable external access to our escalation endpoint
  </Step>

  <Step title="Define the Tool">
    Create a schema for escalation requests
  </Step>

  <Step title="Create Manager Handler">
    Build the API route for manager takeover
  </Step>

  <Step title="Update System Prompt">
    Add escalation rules to the base prompt
  </Step>

  <Step title="Test the System">
    Verify escalation flows
  </Step>
</Steps>

<Tip>
  <b>Stuck?</b>

  <br />

  If at any point you get lost, you can refer to the [`/final`](https://github.com/fixie-ai/ultravox-tutorial-call-stages/tree/main/final) folder in the repo to get final versions of the various files you will create or edit.
</Tip>

<Tip>
  <b>Debugging</b>

  <br />

  During testing, watch your terminal for ngrok request logs to verify the escalation endpoint is being called correctly.
</Tip>

## Step 1: Set Up ngrok

First, we need to make our escalation endpoint accessible to Ultravox.

1. Start your development server:

```bash theme={null}
pnpm run dev
```

2. In a new terminal, start ngrok:

```bash theme={null}
ngrok http 3000
```

3. Copy the HTTPS URL from ngrok (it will look like `https://1234-56-78-910-11.ngrok-free.app`)

4. Update `toolsBaseUrl` in `demo-config.ts`:

```ts theme={null}
const toolsBaseUrl = 'https://your-ngrok-url-here';
```

## Step 2: Define the Escalation Tool

We'll define an `escalateToManager` tool that the AI agent will use to transfer difficult customers.

Update the `selectedTools` array in `demo-config.ts` and add to our call definition:

```ts theme={null}
const selectedTools: SelectedTool[] = [
  {
    "temporaryTool": {
      "modelToolName": "escalateToManager",
      "description": "Escalate to the manager in charge. Use this tool if a customer becomes irate, asks for a refund, or complains about the food.",
      "dynamicParameters": [
        {
          "name": "complaintDetails",
          "location": ParameterLocation.BODY,
          "schema": {
            "description": "An object containing details about the nature of the complaint or issue.",
            "type": "object",
            "properties": {
              "complaintType": {
                "type": "string",
                "enum": ["refund", "food", "price", "other"],
                "description": "The type of complaint."
              },
              "complaintDetails": {
                "type": "string",
                "description": "The details of the complaint."
              },
              "desiredResolution": {
                "type": "string",
                "description": "The resolution the customer is seeking."
              },
              "firstName": {
                "type": "string",
                "description": "Customer first name."
              },
              "lastName": {
                "type": "string",
                "description": "Customer last name."
              }
            },
            "required": ["complaintType", "complaintDetails"]
          },
          "required": true
        }
      ],
      "http": {
        "baseUrlPattern": `${toolsBaseUrl}/api/managerEscalation`,
        "httpMethod": "POST"
      }
    }
  }
];

// Update call definition to add selectedTools
export const demoConfig: DemoConfig = {
  title: "Dr. Donut",
  overview: "This agent has been prompted to facilitate orders at a fictional drive-thru called Dr. Donut.",
  callConfig: {
    systemPrompt: getSystemPrompt(),
    model: "ultravox-v0.7",
    languageHint: "en",
    voice: "Mark",
    temperature: 0.4,
    selectedTools: selectedTools
  }
};
```

## Step 3: Create Manager Handler

Create a new file at `app/api/managerEscalation/route.ts` to handle the escalation:

```ts theme={null}
import { NextRequest, NextResponse } from 'next/server';

const managerPrompt: string = `
  # Drive-Thru Order System Configuration

  ## Agent Role
  - Name: Dr. Donut Drive-Thru Manager
  - Context: Voice-based order taking system with TTS output
  - Current time: ${new Date()}

  ## Menu Items
    [Menu items section - same as base prompt]

  ## Conversation Flow
  1. Greeting -> Apologize for Situation -> Offer Resolution -> Order Confirmation -> End

  ## Response Guidelines
  1. Voice-Optimized Format
    - Use spoken numbers ("one twenty-nine" vs "$1.29")
    - Avoid special characters and formatting
    - Use natural speech patterns

  2. Conversation Management
    - Keep responses brief (1-2 sentences)
    - Use clarifying questions for ambiguity
    - Maintain conversation flow without explicit endings
    - Allow for casual conversation

  3. Greeting
    - Tell the customer that you are the manager
    - Inform the customer you were just informed of the issue
    - Then move to the apology

  4. Apology
    - Acknowledge customer concern
    - Apologize and reaffirm Dr. Donut's commitment to quality and customer happiness

  5. Resolving Customer Concern
    - Offer reasonable remedy
    - Maximum refund amount equal to purchase amount
    - Offer $10 or $20 gift cards for more extreme issues

  [Rest of guidelines section]
`;

export async function POST(request: NextRequest) {
  const body = await request.json();
  console.log(`Got escalation!`);

  // Set-up escalation
  const responseBody = {
    systemPrompt: managerPrompt,
    voice: 'Jessica'  // Different voice for manager
  };
  const response = NextResponse.json(responseBody);
  // Set our custom header for starting a new call stage
  response.headers.set('X-Ultravox-Response-Type', 'new-stage');

  return response;
}
```

## Step 4: Update System Prompt

Add escalation rules to your base system prompt in `demo-config.ts`:

```ts theme={null}
## Response Guidelines
  [Previous guidelines...]

  6. Angry Customers or Complaints
    - You must escalate to your manager for angry customers, refunds, or big problems
    - Before you escalate, ask the customer if they would like to talk to your manager
    - If the customer wants the manager, you MUST call the tool "escalateToManager"

  ## State Management
    [Previous instructions...]
  - Use the "escalateToManager" tool for any complaints or angry customers
```

## Testing Your Implementation

Here are three scenarios to test the escalation system:

### Scenario 1: Food Quality Issue

```
Customer: "I just found hair in my donuts! This is disgusting!"
Expected: Agent should offer manager assistance and escalate with complaint type "food"
```

### Scenario 2: Out of Stock Frustration

```
Customer: "You don't have the Magic Rainbow donuts in stock and this is the third time I drove down here this week for them! This is ridiculous!"
Expected: Agent should offer manager assistance and escalate with complaint type "other"
```

### Scenario 3: Product and Refund

```
Customer: "This coffee is cold and I want a refund right now!"
Expected: Agent should offer manager assistance and escalate with complaint type "refund"
```

For each scenario, verify:

1. The agent offers manager assistance
2. The escalation tool is called with appropriate details
3. The manager persona takes over with the new voice
4. The manager follows the resolution guidelines

## Common Issues

1. **ngrok URL Not Working**
   * Make sure ngrok is running
   * Check the URL is correctly copied to `demo-config.ts`
   * Verify no trailing slash in the URL

2. **Escalation Not Triggering**
   * Check the system prompt includes escalation guidelines
   * Verify the complaint is clearly expressed
   * Try using keywords like "manager", "refund", or "complaint"

3. **Manager Voice Not Changing**
   * Verify the `X-Ultravox-Response-Type` header is set
   * Check the voice parameter in the response body

## Next Steps

Now that you've implemented basic escalation, you can:

* Implement different manager personalities for different situations
* Create a complaint logging system
* Add resolution tracking and follow-up mechanisms

## Resources

* [Call Stages Reference](/agents/call-stages)
* [Tutorial Source Code](https://github.com/fixie-ai/ultravox-tutorial-call-stages)


# Tutorial: Building Interactive UI with Client Tools
Source: https://docs.ultravox.ai/tutorials/clienttools

Learn how to implement client-side tools in Ultravox to create dynamic, interactive user interfaces.

This tutorial walks you through implementing client-side tools in Ultravox to create real-time, interactive UI elements. You'll build a drive-thru order display screen that updates dynamically as customers place orders through an AI agent.

**What you'll learn:**

* How to define and implement client tools
* Real-time UI updates using custom events
* State management with React components
* Integration with Ultravox's AI agent system

**Time to complete:** 30 minutes

## Prerequisites

Before starting this tutorial, make sure you have:

* Basic knowledge of TypeScript and React
* The starter code from our [tutorial repository](https://github.com/fixie-ai/ultravox-tutorial-client-tools)
* Node.js 16+ installed on your machine

## Understanding Client Tools

Client tools in Ultravox enable direct interaction between AI agents and your frontend application. Unlike [server-side tools](/tools/custom/http-vs-client-tools#http-tools) that handle backend operations, client tools are specifically designed for:

* **UI Updates** → Modify interface elements in real-time
* **State Management** → Handle application state changes
* **User Interaction** → Respond to and process user actions
* **Event Handling** → Dispatch and manage custom events

## Project Overview: Dr Donut Drive-Thru

We'll build a drive-thru order display for a fictional restaurant called "Dr. Donut". The display will update in real-time as customers place orders through our AI agent.

This tutorial will take you through the following steps:

### Implementation Steps

<Steps>
  <Step title="Define the Tool">
    Create a schema for order updates
  </Step>

  <Step title="Implement Logic">
    Build the tool's functionality
  </Step>

  <Step title="Register the Tool">
    Connect it to the Ultravox system
  </Step>

  <Step title="Create the UI">
    Build the order display component
  </Step>
</Steps>

<Tip>
  <b>Stuck?</b>

  <br />

  If at any point you get lost, you can refer to the [`/final`](https://github.com/fixie-ai/ultravox-tutorial-client-tools/tree/main/final) folder in the repo to get final versions of the various files you will create or edit.
</Tip>

## Step 1: Define the Tool

First, we'll define our `updateOrder` tool that the AI agent will use to modify the order display.

Modify `.demo-config.ts`:

```ts theme={null}
const selectedTools: SelectedTool[] = [
  {
    "temporaryTool": {
      "modelToolName": "updateOrder",
      "description": "Update order details. Used any time items are added or removed or when the order is finalized. Call this any time the user updates their order.",      
      "dynamicParameters": [
        {
          "name": "orderDetailsData",
          "location": ParameterLocation.BODY,
          "schema": {
            "description": "An array of objects contain order items.",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": { "type": "string", "description": "The name of the item to be added to the order." },
                "quantity": { "type": "number", "description": "The quantity of the item for the order." },
                "specialInstructions": { "type": "string", "description": "Any special instructions that pertain to the item." },
                "price": { "type": "number", "description": "The unit price for the item." },
              },
              "required": ["name", "quantity", "price"]
            }
          },
          "required": true
        },
      ],
      "client": {}
    }
  },
];
```

Here's what this is doing:

* Defines a client tool called `updateOrder` and describes what it does and how to use it.
* Defines a single, required parameter called `orderDetailsData` that:
  * Is passed in the request body
  * Is an array of objects where each object can contain `name`, `quantity`, `specialInstructions`, and `price`. Only `specialInstructions` is optional.

#### Update System Prompt

Now, we need to update the system prompt to tell the agent how to use the tool.

Update the `sysPrompt` variable:

```ts theme={null}
sysPrompt = `
  # Drive-Thru Order System Configuration

  ## Agent Role
  - Name: Dr. Donut Drive-Thru Assistant
  - Context: Voice-based order taking system with TTS output
  - Current time: ${new Date()}

  ## Menu Items
    # DONUTS
    PUMPKIN SPICE ICED DOUGHNUT $1.29
    PUMPKIN SPICE CAKE DOUGHNUT $1.29
    OLD FASHIONED DOUGHNUT $1.29
    CHOCOLATE ICED DOUGHNUT $1.09
    CHOCOLATE ICED DOUGHNUT WITH SPRINKLES $1.09
    RASPBERRY FILLED DOUGHNUT $1.09
    BLUEBERRY CAKE DOUGHNUT $1.09
    STRAWBERRY ICED DOUGHNUT WITH SPRINKLES $1.09
    LEMON FILLED DOUGHNUT $1.09
    DOUGHNUT HOLES $3.99

    # COFFEE & DRINKS
    PUMPKIN SPICE COFFEE $2.59
    PUMPKIN SPICE LATTE $4.59
    REGULAR BREWED COFFEE $1.79
    DECAF BREWED COFFEE $1.79
    LATTE $3.49
    CAPPUCINO $3.49
    CARAMEL MACCHIATO $3.49
    MOCHA LATTE $3.49
    CARAMEL MOCHA LATTE $3.49

  ## Conversation Flow
  1. Greeting -> Order Taking -> Call "updateOrder" Tool -> Order Confirmation -> Payment Direction

  ## Tool Usage Rules
  - You must call the tool "updateOrder" immediately when:
    - User confirms an item
    - User requests item removal
    - User modifies quantity
  - Do not emit text during tool calls
  - Validate menu items before calling updateOrder

  ## Response Guidelines
  1. Voice-Optimized Format
    - Use spoken numbers ("one twenty-nine" vs "$1.29")
    - Avoid special characters and formatting
    - Use natural speech patterns

  2. Conversation Management
    - Keep responses brief (1-2 sentences)
    - Use clarifying questions for ambiguity
    - Maintain conversation flow without explicit endings
    - Allow for casual conversation

  3. Order Processing
    - Validate items against menu
    - Suggest similar items for unavailable requests
    - Cross-sell based on order composition:
      - Donuts -> Suggest drinks
      - Drinks -> Suggest donuts
      - Both -> No additional suggestions

  4. Standard Responses
    - Off-topic: "Um... this is a Dr. Donut."
    - Thanks: "My pleasure."
    - Menu inquiries: Provide 2-3 relevant suggestions

  5. Order confirmation
    - Call the "updateOrder" tool first
    - Only confirm the full order at the end when the customer is done

  ## Error Handling
  1. Menu Mismatches
    - Suggest closest available item
    - Explain unavailability briefly
  2. Unclear Input
    - Request clarification
    - Offer specific options
  3. Invalid Tool Calls
    - Validate before calling
    - Handle failures gracefully

  ## State Management
  - Track order contents
  - Monitor order type distribution (drinks vs donuts)
  - Maintain conversation context
  - Remember previous clarifications    
  `;
```

#### Update Configuration + Import

Now we need to add the `selectedTools` to our call definition and update our import statement.

Add the tool to your demo configuration:

```ts theme={null}
export const demoConfig: DemoConfig = {
  title: "Dr. Donut",
  overview: "This agent has been prompted to facilitate orders at a fictional drive-thru called Dr. Donut.",
  callConfig: {
    systemPrompt: getSystemPrompt(),
    model: "ultravox-v0.7",
    languageHint: "en",
    selectedTools: selectedTools,
    voice: "Mark",
    temperature: 0.4
  }
};
```

Add `ParameterLocation` and `SelectedTool` to our import:

```ts theme={null}
import { DemoConfig, ParameterLocation, SelectedTool } from "@/lib/types";
```

## Step 2: Implement Tool Logic

Now that we've defined the `updateOrder` tool, we need to implement the logic for it.

Create `/lib/clientTools.ts` to handle the tool's functionality:

```ts theme={null}
import { ClientToolImplementation } from 'ultravox-client';

export const updateOrderTool: ClientToolImplementation = (parameters) => {
  const { ...orderData } = parameters;
  
  if (typeof window !== "undefined") {
    const event = new CustomEvent("orderDetailsUpdated", {
      detail: orderData.orderDetailsData,
    });
    window.dispatchEvent(event);
  }

  return "Updated the order details.";
};
```

We will do most of the heavy lifting in the UI component that we'll build in [step 4](#step-4-build-the-ui).

## Step 3: Register the Tool

Next, we are going to register the client tool with the Ultravox client SDK.

Update `/lib/callFunctions.ts`:

```ts theme={null}
import { updateOrderTool } from '@/lib/clientTools';

// Initialize Ultravox session
uvSession = new UltravoxSession({ experimentalMessages: debugMessages });

// Register tool
uvSession.registerToolImplementation(
    "updateOrder",
    updateOrderTool
);

// Handle call ending -- This allows clearing the order details screen
export async function endCall(): Promise<void> {
  if (uvSession) {
    uvSession.leaveCall();
    uvSession = null;
    
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('callEnded'));
    }
  }
}
```

## Step 4: Build the UI

Create a new React component to display order details. This component will:

* Listen for order updates
* Format currency and order items
* Handle order clearing when calls end

Create `/components/OrderDetails.tsx`:

```ts theme={null}
'use client';

import React, { useState, useEffect } from 'react';
import { OrderDetailsData, OrderItem } from '@/lib/types';

// Function to calculate order total
function prepOrderDetails(orderDetailsData: string): OrderDetailsData {
  try {
    const parsedItems: OrderItem[] = JSON.parse(orderDetailsData);
    const totalAmount = parsedItems.reduce((sum, item) => {
      return sum + (item.price * item.quantity);
    }, 0);

    // Construct the final order details object with total amount
    const orderDetails: OrderDetailsData = {
      items: parsedItems,
      totalAmount: Number(totalAmount.toFixed(2))
    };

    return orderDetails;
  } catch (error) {
    throw new Error(`Failed to parse order details: ${error}`);
  }
}

const OrderDetails: React.FC = () => {
  const [orderDetails, setOrderDetails] = useState<OrderDetailsData>({
    items: [],
    totalAmount: 0
  });

  useEffect(() => {
    // Update order details as things change
    const handleOrderUpdate = (event: CustomEvent<string>) => {
      console.log(`got event: ${JSON.stringify(event.detail)}`);

      const formattedData: OrderDetailsData = prepOrderDetails(event.detail);
      setOrderDetails(formattedData);
    };

    // Clear out order details when the call ends so it's empty for the next call
    const handleCallEnded = () => {
      setOrderDetails({
        items: [],
        totalAmount: 0
      });
    };

    window.addEventListener('orderDetailsUpdated', handleOrderUpdate as EventListener);
    window.addEventListener('callEnded', handleCallEnded as EventListener);

    return () => {
      window.removeEventListener('orderDetailsUpdated', handleOrderUpdate as EventListener);
      window.removeEventListener('callEnded', handleCallEnded as EventListener);
    };
  }, []);

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  };

  const formatOrderItem = (item: OrderItem, index: number) => (
    <div key={index} className="mb-2 pl-4 border-l-2 border-gray-200">
      <div className="flex justify-between items-center">
        <span className="font-medium">{item.quantity}x {item.name}</span>
        <span className="text-gray-600">{formatCurrency(item.price * item.quantity)}</span>
      </div>
      {item.specialInstructions && (
        <div className="text-sm text-gray-500 italic mt-1">
          Note: {item.specialInstructions}
        </div>
      )}
    </div>
  );

  return (
    <div className="mt-10">
      <h1 className="text-xl font-bold mb-4">Order Details</h1>
      <div className="shadow-md rounded p-4">
        <div className="mb-4">
          <span className="text-gray-400 font-mono mb-2 block">Items:</span>
          {orderDetails.items.length > 0 ? (
            orderDetails.items.map((item, index) => formatOrderItem(item, index))
          ) : (
            <span className="text-gray-500 text-base font-mono">No items</span>
          )}
        </div>
        <div className="mt-6 pt-4 border-t border-gray-200">
          <div className="flex justify-between items-center font-bold">
            <span className="text-gray-400 font-mono">Total:</span>
            <span>{formatCurrency(orderDetails.totalAmount)}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default OrderDetails;
```

#### Add to Main Page

Update the main page (`page.tsx`) to include the new component:

```tsx theme={null}
import OrderDetails from '@/components/OrderDetails';

// In the JSX:
{/* Call Status */}
<CallStatus status={agentStatus}>
    <OrderDetails />
</CallStatus>
```

## Testing Your Implementation

1. Start the development server:
   ```bash theme={null}
   pnpm run dev
   ```

2. Navigate to `http://localhost:3000`

3. Start a call and place an order. You should see:
   * Real-time updates to the order display
   * Formatted prices and item details
   * Special instructions when provided
   * Order clearing when calls end

## Next Steps

Now that you've implemented basic client tools, you can:

* Add additional UI features like order modification or nutritional information
* Add animations for updates
* Enhance the display with customer and/or vehicle information

## Resources

* [Tools Reference](/tools/overview)
* [Tutorial Source Code](https://github.com/fixie-ai/ultravox-tutorial-client-tools)


# Bring Your Own (Key)
Source: https://docs.ultravox.ai/voices/bring-your-own

How to use Ultravox with your own text-to-speech provider

Ultravox Realtime allows you to bring your own TTS provider to have your agent sound however you like.

<Note>
  <b>Advanced Feature</b>

  Integrating your own TTS provider means you're responsible for speech generation issues.
  You'll need to work with your provider to ensure your requests will be fulfilled reliably and quickly
  and will sound the way you want. If you encounter generation errors, see [Debugging](#debugging) below.
</Note>

## Setting up your account

To use your own TTS provider, you'll need to add your API key for that provider to your Ultravox account.
You can do that in the [Ultravox console](https://app.ultravox.ai/settings/) or using the
[Set TTS API keys endpoint](/api-reference/accounts/accounts-me-tts-api-keys-partial-update).

<Note>
  <b>Generic option</b>

  You can skip this step if you're using the "generic" ExternalVoice integration.
</Note>

## Named Providers

When setting an [ExternalVoice](/api-reference/calls/calls-post#body-external-voice) on your agent or call,
there are a few different providers available. The named providers such as ElevenLabs and Cartesia have
customized integrations that make their voices work as smoothly as possible with Ultravox. This typically means
Ultravox uses their streaming API and takes advantage of audio timing information from the provider to
synchronize transcripts.  While you'll still need to work with the provider to ensure your agent's requests will
be fulfilled reliably and quickly, you can be confident that Ultravox knows how to interact with your provider.

If you'd like to use some other TTS provider, you may be able to get by with our [Generic TTS](#generic-tts-options) integration option.

### Cartesia

Cartesia also provides many high quality voices. We use their websocket API to stream text in and audio out in
parallel. Cartesia provides word-level timing information interspersed with audio, helping to keep transcripts
in sync with audio.

```json theme={null}
"cartesia": {
  "voiceId": "af346552-54bf-4c2b-a4d4-9d2820f51b6c",
  "model": "sonic-2"
}
```

### Eleven Labs

Eleven Labs is our most commonly used provider (and as of May 2025 backs most of our internal voices). We use
their websocket API to stream text in and audio out in parallel. Eleven Labs provides character-level timing
information alongside audio, ensuring transcripts are kept in sync and conversation history accurately reflects
what was spoken in the event of an interruption.

<Note>
  <b>Slurring</b>

  Eleven Labs seems much more likely to slur words or generally hallucinate audio in the past couple months.
  Several of their customers (including Ultravox) have reported this and it is being worked on. In the meantime,
  prompting your agent to avoid special characters like asterisks may be helpful. Alternatively, you could try
  their more robust (but slower) multilingual model.
</Note>

```json theme={null}
"elevenLabs": {
  "voiceId": "21m00Tcm4TlvDq8ikWAM",
  "model": "eleven_turbo_v2_5"
}
```

### LMNT

LMNT's "aurora" model lags the other providers in terms of quality, though their experimental "blizzard" model shows
potential. LMNT has by far the simplest streaming integration (and the only SDK worth using). They also offer unlimited
concurrency and no rate limits even on their \$10/month plan. Like Eleven Labs and Cartesia, LMNT allows for streaming
text in and audio out in parallel and provides audio timing information to help Ultravox align transcripts with speech.

```json theme={null}
"lmnt": {
  "voiceId": "lily",
  "model": "blizzard"
}
```

## Generic TTS Options

The "generic" TTS route gives you much more flexibility to define requests to your provider. Any provider that accepts json
post requests and that returns either WAV or raw PCM audio (including within JSON bodies) ought to work.

Since generic integrations don't stream text in (but can stream audio out) Ultravox has to buffer input text
before sending it to your provider, which means slightly higher agent response times and possible audio
discontinuities at sentence boundaries.

Additionally since generic integrations don't provide audio timing information, transcript timing must be approximated.
Once Ultravox has a full generation (and therefore the true audio duration), it assumes each character requires
the same duration and approximates transcripts based on that. While the first generation is still streaming, Ultravox
relies on an estimated words-per-minute speaking rate to approximate transcripts.

### Deepgram

Deepgram's latest Aura-2 model claims to be in line with other providers in terms of quality. However, it isn't supported
in their streaming API yet and Ultravox has no special integration with it yet as a result. That said, you can use our
"generic" ExternalVoice to give Deepgram a try now using their REST API.

```json theme={null}
{
  "url": "https://api.deepgram.com/v1/speak?model=aura-2-asteria-en&encoding=linear16&sample_rate=48000&container=none",
  "headers": {
    "Authorization": "Token YOUR_DEEPGRAM_API_KEY",
    "Content-Type": "application/json"
  },
  "body": {
    "text": "{text}"
  },
  "responseSampleRate": 48000
}
```

### Google

Google's TTS API returns json, so it requires an extra `jsonAudioFieldPath` in your generic ExternalVoice.

```json theme={null}
{
  "url": "https://texttospeech.googleapis.com/v1/text:synthesize",
  "headers": {
    "Authorization": "Bearer YOUR_GOOGLE_SERVICE_ACCOUNT_CREDENTIALS",
    "Content-Type": "application/json"
  },
  "body": {
    "input": {"text": "{text}"},
    "voice": {
      "languageCode": "en-US",
      "name": "en-US-Chirp3-HD-Charon"
    },
    "audioConfig": {
      "audioEncoding": "LINEAR16",
      "speakingRate": 1.0,
      "sampleRateHertz": 48000
    }
  },
  "responseSampleRate": 48000,
  "jsonAudioFieldPath": "audioContent"
}
```

### Inworld

Inworld's TTS API returns json, so it requires an extra `jsonAudioFieldPath` field. To use the streaming endpoint, you'll also need to override the `responseMimeType` field so we know to treat the response as [json lines](https://jsonlines.org/).

```json theme={null}
{
  "url": "https://api.inworld.ai/tts/v1/voice:stream",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Basic YOUR_INWORLD_BASIC_API_KEY"
  },
  "body": {
    "voiceId": "Dennis",
    "modelId": "inworld-tts-1.5-max",
    "text": "{text}",
    "audioConfig": {
        "audioEncoding": "LINEAR16",
        "speakingRate": 1.0,
        "sampleRateHertz": 48000
    }
  },
  "responseSampleRate": 48000,
  "responseMimeType": "application/jsonl",
  "jsonAudioFieldPath": "result.audioContent"
}
```

### OpenAI

OpenAI also has a TTS API you can use with our generic ExternalVoice option.

```json theme={null}
{
  "url": "https://api.openai.com/v1/audio/speech",
  "headers": {
    "Authorization": "Bearer YOUR_OPENAI_API_KEY",
    "Content-Type": "application/json",
  },
  "body": {
    "input": "{text}",
    "model": "gpt-4o-mini-tts",
    "voice": "shimmer",
    "response_format": "pcm",
    "speed": 1.0
  },
  "responseSampleRate": 24000
}
```

### Orpheus

Orpheus is an open-source TTS model with a Llama 3 backbone. Along with several similar models, Orpheus
likely represents the next generation of realism for AI voices. They've partnered with baseten to provide a
simple [self-hosting option](https://www.baseten.co/library/orpheus-tts/) you can set up for yourself.

You can use a generic ExternalVoice with your self-hosted Orpheus instance:

```json theme={null}
{
  "url": "YOUR_BASETEN_DEPLOYMENT_URL",
  "headers": {
    "Authorization": "Api-Key YOUR_BASETEN_API_KEY",
    "Content-Type": "application/json"
  },
  "body": {
    "prompt": "{text}",
    "request_id": "SOME_UUID",
    "max_tokens": 4096,
    "voice": "tara",
    "stop_token_ids": [128258, 128009]
  },
  "responseSampleRate": 24000,
  "responseMimeType": "audio/l16"
}
```

### Resemble

Resemble also has a TTS API you can use with our generic ExternalVoice option.

```json theme={null}
{
  "url": "https://p.cluster.resemble.ai/stream",
  "headers": {
    "Authorization": "Bearer YOUR_RESEMBLE_API_KEY",
    "Content-Type": "application/json",
    "Accept": "audio/wav"
  },
  "body": {
    "data": "{text}",
    "voice_uuid": "0842fdf9",
    "precision": "PCM_16",
    "sample_rate": 44100
  },
  "responseSampleRate": 44100
}
```

### Rime

Rime provides a [spell()](https://docs.rime.ai/api-reference/spell) tool to help nail the pronunciation of unique IDs, email addresses, etc.

```json theme={null}
{
  "url": "https://users.rime.ai/v1/rime-tts",
  "headers": {
    "Authorization": "Bearer YOUR_RIME_API_KEY",
    "Content-Type": "application/json",
    "Accept": "audio/pcm"
  },
  "body": {
    "text": "{text}",
    "repetition_penalty": 1.5,
    "top_p": 1,
    "speaker": "luna",
    "modelId": "arcana",
    "samplingRate": 24000,
    "max_tokens": 1200,
    "temperature": 0.5
  },
  "responseSampleRate": 24000
}
```

### Sarvam

Sarvam's TTS API returns json, so it requires an extra `jsonAudioFieldPath` field in your generic ExternalVoice.

```json theme={null}
{
  "url": "https://api.sarvam.ai/text-to-speech",
  "headers": {
    "Content-Type": "application/json",
    "api-subscription-key": "YOUR_SARVAM_API_KEY"
  },
  "body": {
    "text": "{text}",
    "targetLanguageCode": "en-IN",
    "speaker": "anushka",
    "model": "bulbul:v2",
    "pace": 1,
    "speechSampleRate": 24000,
    "outputAudioCodec": "linear16"
  },
  "responseSampleRate": 24000,
  "jsonAudioFieldPath": "audios"
}
```

## Debugging

If you start a call with an external voice and don't hear anything from the agent, your external voice is
probably misconfigured. You can figure out what's wrong using the [call event API](/api-reference/calls/calls-events-list).
Events are also visible when viewing the call in the Ultravox console.  Here are some common issues and their resolutions:

| Example error text                                                                                                         | Provider                 | Resolution                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Requested output format pcm_44100 (PCM at 44100hz) is only allowed for Pro tier and above.`                               | ElevenLabs               | Your ElevenLabs subscription limits your generation sample rate. Find the maximum sample rate allowed for your subscription on [their pricing page](https://elevenlabs.io/pricing) (you'll need to click "Show API details") and then set maxSampleRate on your voice to match. |
| `A model with requested ID does not exist`                                                                                 | ElevenLabs               | Your model name is wrong. See [their model page](https://elevenlabs.io/docs/models#models-overview) for the correct ids.                                                                                                                                                        |
| `A voice with voice_id 2bNrEsM0omyhLiEyOwqY does not exist.`                                                               | ElevenLabs               | The voiceId you provided doesn't correspond to a voice in your ElevenLabs library. Make sure your ElevenLabs API key is what you expect and then add the voice to your library in Eleven.                                                                                       |
| `The API key you used is missing the permission text_to_speech to execute this operation.`                                 | ElevenLabs               | Check your key and/or upgrade your account with ElevenLabs.                                                                                                                                                                                                                     |
| `This request exceeds your quota of 10000. You have 14 credits remaining, while 46 credits are required for this request.` | ElevenLabs               | Check your key and/or upgrade your account with ElevenLabs.                                                                                                                                                                                                                     |
| `Error initializing streaming TTS connection`                                                                              | ElevenLabs/Cartesia/LMNT | The provider rejected our attempt to create a streaming connection. This occurs most commonly with ElevenLabs and usually means your API key is incorrect.                                                                                                                      |
| `HTTP error: 500 Response:{"error": "Internal server error"} Request:{"text": "How can I help you?"}`                      | Generic                  | This is the sort of error you'll get for generic external voices. You should be able to use the complete request and response to reproduce and debug the error with your provider.                                                                                              |

If you can't figure out your issue from the call events or the common issues below, you can also try our [Discord](https://discord.gg/62X253zeWB).


# Voice Cloning
Source: https://docs.ultravox.ai/voices/cloning

Create Custom Voices

Ultravox Realtime includes multiple, high-quality voices for all supported languages. The fastest way to experience the included voices is in the [Voices explorer](https://app.ultravox.ai/voices) in the web console. You can also use the [List Voices](/api-reference/voices/voices-list) endpoint to see all voices and their details.

## Creating a Custom Voice

<VoiceCloneLimit />

You can create a custom voice by uploading an audio sample using the [Create (Clone) Voice](/api-reference/voices/voices-post) endpoint. This process allows you to generate a unique voice that matches the characteristics of your audio sample.

### Prerequisites

* An Ultravox Realtime API key
* A single audio file containing a clear voice sample (30 seconds recommended)
* The audio file must be in .mp3 or .wav format

### Using the API

To create a custom voice, send a POST request to the `/api/voices` endpoint with your audio file. Note: multiple files are not supported.

Here's how to do it:

```bash theme={null}
curl --request POST https://api.ultravox.ai/api/voices \
  --header 'Content-Type: multipart/form-data' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --form 'file=@"/path/to/your/audio-sample.wav"'
  --form 'name=My Custom Voice' \
  --form 'description=Voice recorded on Jan 1, 2024'
```

### Requirements for Audio Samples

For optimal results, ensure your audio sample meets these criteria:

* Clear, high-quality audio without background noise or echo
* Single speaker throughout the recording
* Natural speaking pace and tone
* No music or other voices in the background
* 30-60 seconds in length (longer samples do not typically lead to better clones)

### Limitations

* Maximum of one audio file per voice
* 10MB file size maximum


# Overview: Voices
Source: https://docs.ultravox.ai/voices/overview

Voice options available in Ultravox Realtime

Ultravox Realtime offers three ways to customize how your AI agents sound:

## Built-in Voices

Ready-to-use, high-quality voices for all supported languages. Perfect for getting started quickly.

* Try them in the [Voices explorer](https://app.ultravox.ai/voices)
* Browse all options via the [List Voices API](/api-reference/voices/voices-list)

## Voice Cloning

Create custom voices from audio samples to match your brand or requirements.

* Upload a 30-60 second audio sample
* Get a unique voice that matches your sample's characteristics
* Learn more: [Voice Cloning Guide](/voices/cloning)

## Bring Your Own TTS

Integrate your preferred TTS provider for specialized needs or existing investments.

* Supports ElevenLabs, Cartesia, OpenAI, and many others
* Complete control over voice generation
* Learn more: [Bring Your Own TTS Guide](/voices/bring-your-own)

## API Reference

For complete voice management documentation, see the [Voices API Reference](/api-reference/voices).


# Available Webhooks
Source: https://docs.ultravox.ai/webhooks/available-webhooks

Complete reference of all webhook events available in Ultravox.

Ultravox offers several webhook events that you can subscribe to for real-time notifications. Each event provides detailed information about what happened in your account.

## Available Events

The following events are available and can be specified when creating or updating a webhoook.

| event        | description                                |
| ------------ | ------------------------------------------ |
| call.started | Fires when a call is created.              |
| call.joined  | Fires when a client connects to your call. |
| call.ended   | Fires when a call ends.                    |
| call.billed  | Fires when a call is billed.               |

### `call.started`

Fires when a call is created.

If you create calls directly using either the [Create Agent Call](/api-reference/agents/agents-calls-post) or [Create Call](/api-reference/calls/calls-post) API, you likely won't need this event as a 201 response to your call creation request is equivalent.

The `call.started` event is most useful with telephony integrations where you've allowed calls to be created on your behalf either in response to qualified [SIP INVITEs](/telephony/sip#incoming-sip-calls) or verified requests from your [telephony](/telephony/inbound-calls) provider (Twilio, Telnyx, or Plivo).

### `call.joined`

Fires when a client connects to your call.

Useful if you need to keep track of live calls or for monitoring deltas in timing from call creation.

### `call.ended`

Fires when a call ends.

The call's messages are now immutable because the call is over. However, billing information may not be available yet (in particular for SIP calls, where the SIP session could be ongoing — see [call.billed](#call-billed)). This event is also sent for unjoined calls when their join timeout is reached.

### `call.billed`

Fires when a call is billed.

Billing information will always be available. Typically you'll only want one of `call.ended` or `call.billed`. If you aren't using SIP or don't need billing details for your integration, `call.ended` may be preferable.

## Event Payload Reference

All webhooks follow a consistent structure. The payload always includes:

* **event**: The type of event that triggered the webhook.
* **call**: Complete call object matching our API response format.

<Tabs>
  <Tab title="Generic Structure">
    ```json theme={null}
    {
      "event": {event_name},
      "call": {call_object}
    }
    ```
  </Tab>

  <Tab title="Example Payload: call.started">
    ```json theme={null}
    {
      "event": "call.started",
      "call": {
        "callId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "clientVersion": "<string>",
        "created": "2023-11-07T05:31:56Z",
        "...": "..."
      }
    }
    ```
  </Tab>
</Tabs>

### Event Name

The `event` field contains the exact event name you subscribed to:

* `"call.started"`
* `"call.ended"`
* `"call.joined"`
* `"call.billed"`

### Call Object

The `call` object contains the complete [call definition](/api-reference/schema/call-definition), identical to what you'd receive from the [Get Call API endpoint](/api-reference/calls/calls-get). This ensures consistency across your application whether you're receiving webhook data or making API requests.

**Key call object fields:**

* `callId`: Unique call identifier
* `created`: Timestamp when call was created
* `joined`: Timestamp when call was joined
* `ended`: Timestamp when call was ended
* `shortSummary`: Short summary of the call
* `metadata`: Custom metadata you've associated with the call

See the [Call definition schema](/api-reference/schema/call-definition) for the complete list of fields.

## Webhook Configuration

When creating or updating a webhook, specify which events you want to receive:

```bash theme={null}
curl -X POST https://api.ultravox.ai/api/webhooks \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://your-app.com/webhooks/ultravox",
    "events": ["call.started", "call.ended"],
    "secrets": ["your-webhook-secret"]
  }'
```

## HTTP Requirements

Your webhook endpoint must meet these requirements:

**Accept POST Requests**: All webhooks are sent as HTTP POST requests.

**Return 2xx Status**: Return any 2xx status code (we recommend 204) to acknowledge receipt.

**Respond Quickly**: Respond quickly to avoid timeouts.

**Handle JSON**: Parse the JSON payload from the request body.

```js Example: Handling Webhook Events theme={null}
// Express.js webhook handler example
app.post('/ultravox-webhook', (req, res) => {
  const event = req.body;
  
  switch (event.event) {
    case 'call.started':
      console.log('Call started:', event.call.callId);
      // Initialize any required resources
      break;
      
    case 'call.joined':
      console.log('User joined call:', event.call.callId);
      // Update UI, start monitoring, etc.
      break;
      
    case 'call.ended':
      console.log('Call ended:', event.call.callId, 'Reason:', event.call.endReason);
      // Clean up resources, analyze results, etc.
      break;
    
    case 'call.billed':
      console.log('Call billed:', event.call.callId);
      // Update customer invoice, etc.
      break;
  }
  
  res.status(200).send('OK');
});
```

## Error Responses

If your endpoint returns a non-2xx status code (e.g. 4xx or 5xx), Ultravox will retry delivery. See [Error Handling & Retries](./errors-and-retries) for more details.

## Testing Webhooks

During development, consider using tools like:

* **ngrok**: Expose local development servers to receive webhooks
* **webhook.site**: Test webhook payloads without writing code
* **Postman**: Mock webhook endpoints for testing

Remember that webhook events reflect real activity in your Ultravox account, so test carefully to avoid processing duplicate or test data in production systems.


# Error Handling & Retries
Source: https://docs.ultravox.ai/webhooks/errors-and-retries

Understand how Ultravox automatically retries failed webhook deliveries with exponential backoff to ensure reliable event notifications.

## Retrying Failed Webhook Event Deliveries

If your webhook endpoint is temporarily unavailable or returns an error status code (e.g. 4xx or 5xx), Ultravox will automatically retry delivery using an exponential backoff strategy.

We'll make up to 10 retry attempts over several hours as follows:

* First retry will occur approximately 30 seconds later.
* Subsequent retries will double the retry interval. (e.g. second retry again after 1m, third retry after 2m, etc.)
* Total of 10 retries.

For permanent failures or extended downtime, you can always use our REST API to retrieve information about any calls/events you may have missed.

## Keep Building

* Learn about all [Available Webhooks](./available-webhooks) you can subscribe to
* Implement [Webhook Security](./securing-webhooks) to protect your endpoints
* Check out our [API reference](/api-reference/webhooks/webhooks-list) for webhook management endpoints


# Overview: Webhooks
Source: https://docs.ultravox.ai/webhooks/overview

Learn how webhooks work with Ultravox and get started with real-time notifications.

Webhooks provide a powerful way to receive real-time notifications about events in your Ultravox Realtime account. Instead of repeatedly polling our API to check for updates, webhooks push event data directly to your application as soon as something happens.

When you configure a webhook in Ultravox, we'll send an HTTP POST request to your specified URL whenever a subscribed event occurs. This allows your application to react immediately to important events like call starts, call ends, etc. Your server needs to respond with a 2xx to confirm receipt. If delivery fails, we will [retry delivery](./errors-and-retries).

## Getting Started

To start using webhooks with Ultravox:

1. **Set up an endpoint**: Create a URL on a server that can receive POST requests.
2. **Create a webhook**: Use the Ultravox API to register the URL that will receive webhook events and select events you want to receive.
3. **Handle events**: Process incoming webhook data in your application.
4. **Secure your webhook**: Implement signature verification for security (recommended).

## Webhook Payload Structure

All webhooks follow a consistent structure and return the event and details about the call.

```json theme={null}
{
  "event": {event_name},
  "call": {call_object}
}
```

See [Event Payload Reference](./available-webhooks#event-payload-reference).

## Best Practices

**Respond Quickly**: Return a 2xx status code (we recommend 204) as soon as you receive the webhook. Process the data asynchronously if needed.

**Handle Duplicates**: In rare cases, you might receive the same webhook twice. Make your processing idempotent.

**Implement Security**: Always verify webhook signatures to ensure requests are from Ultravox Realtime.

**Monitor Failures**: Keep track of failed webhook deliveries and have a backup plan to retrieve missed data via our API.

**Use HTTPS**: Always use HTTPS endpoints for webhooks to protect sensitive data in transit.

## Keep Building

* Learn about all [Available Webhooks](./available-webhooks) you can subscribe to.
* Learn about webhook [errors and our retry strategy](./errors-and-retries).
* Implement [Webhook Security](./securing-webhooks) to protect your endpoints.
* Check out our [API reference](/api-reference/webhooks/webhooks-list) for webhook management endpoints.


# Securing Webhooks
Source: https://docs.ultravox.ai/webhooks/securing-webhooks

Learn how to verify webhook authenticity and protect your endpoints from malicious requests.

Webhook security is crucial for protecting your application from malicious requests and ensuring that you only process authentic notifications from Ultravox. This guide covers how to implement proper webhook verification.

## Why Webhook Security Matters

Without proper verification, anyone could send fake webhook requests to your endpoint, potentially:

* Triggering unauthorized actions in your application or bypassing your business logic
* Corrupting your data with false information
* Overwhelming your system with spam requests

## How Ultravox Secures Webhooks

Ultravox uses HMAC-SHA256 signatures to ensure webhook authenticity. Each webhook request includes cryptographic proof that:

1. The request came from Ultravox
2. The payload hasn't been tampered with
3. The request is recent (not a replay attack)

## Securing Your Webhooks

You can optionally choose to secure your webhooks with a key. When creating a webhook, a secret key is automatically generated for you or you can choose to provide your own secret. You can update or patch your webhooks to change secrets in the event of a leak or as part of regular key rotation.

Each time your server receives an incoming webhook from Ultravox here's how you can ensure the webhook was sent by Ultravox and hasn't been tampered with:

<Steps>
  <Step title="Timestamp Verification">
    * Each incoming webhook request includes a `X-Ultravox-Webhook-Timestamp` header with the time the webhook was sent.
    * Verify that this timestamp is recent (e.g. within the last minute) to prevent replay attacks.
  </Step>

  <Step title="Signature Verification">
    * Ultravox signs each webhook using HMAC-SHA256.
    * The signature is included in the `X-Ultravox-Webhook-Signature` header.
    * To verify the signature:
      * Concatenate the raw request body with the timestamp.
      * Create an HMAC-SHA256 hash of this concatenated string using your webhook secret as the key.
      * Compare this hash with the provided signature.

    ```python Verifying Webhook Signature theme={null}
    import datetime
    import hmac

    request_timestamp = request.headers["X-Ultravox-Webhook-Timestamp"]
    if datetime.datetime.now() - datetime.datetime.fromisoformat(request_timestamp) > datetime.timedelta(minutes=1):
      raise RuntimeError("Expired message")
    expected_signature = hmac.new(WEBHOOK_SECRET.encode(), request.content + request_timestamp.encode(), "sha256").hexdigest()
    for signature in request.headers["X-Ultravox-Webhook-Signature"].split(","):
      if hmac.compare_digest(signature, expected_signature):
        break  # Valid signature
    else:
      raise RuntimeError("Message or timestamp was tampered with")
    ```
  </Step>

  <Step title="Multiple Signatures">
    * `The X-Ultravox-Webhook-Signature` header may contain multiple signatures separated by commas.
    * This allows for key rotation without downtime.
    * Your code should check if any of the provided signatures match your computed signature.
  </Step>
</Steps>

### Testing

During development, you can test your webhook security implementation by:

1. Creating a test webhook with a known secret
2. Manually crafting webhook requests with correct signatures
3. Verifying that invalid signatures are properly rejected
4. Testing with expired timestamps

By implementing these checks, you ensure that only authentic, recent, and unmodified webhooks from Ultravox are processed by your system.
Remember to store your webhook secret securely and never expose it in client-side code or public repositories.


