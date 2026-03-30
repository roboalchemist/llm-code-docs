# Source: https://ably.com/docs/ai-transport/messaging/accepting-user-input.md

# User input

User input enables users to send prompts and requests to AI agents over Ably channels. The agent subscribes to a channel to receive user messages, processes them, and sends responses back. This pattern uses [Ably Pub/Sub](https://ably.com/docs/basics.md) for realtime, bi-directional communication between users and agents.

User input works alongside [token streaming](https://ably.com/docs/ai-transport/token-streaming.md) patterns to create complete conversational AI experiences. While token streaming handles agent-to-user output, user input handles user-to-agent prompts.

## How it works

User input follows a channel-based pattern where both users and agents connect to a shared channel:

1. The agent subscribes to the channel to listen for user messages.
2. The user publishes a message containing their prompt.
3. The agent receives the message, processes it, and generates a response.
4. The agent publishes the response back to the channel, correlating it to the original input.

This decoupled approach means agents don't need to manage persistent connections to individual users. Instead, they subscribe to channels and respond to messages as they arrive.

<Aside data-type="further-reading">
Learn more about channel-based communication in [channel-oriented sessions](https://ably.com/docs/ai-transport/sessions-identity.md#connection-oriented-vs-channel-oriented-sessions).
</Aside>

## Identify the user

Agents need to verify that incoming messages are from legitimate users. Use [identified clients](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-identity) or [user claims](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-claims) to establish a verified identity or role for the user.

<Aside data-type="further-reading">
For more information about establishing verified identities and roles, see [Identifying users and agents](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md).
</Aside>

### Verify by user identity

Use the `clientId` to identify the user who sent a message. This enables personalized responses, per-user rate limiting, or looking up user-specific preferences from your database.

When a user [authenticates with Ably](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#authenticating), embed their identity in the JWT:

<Code>

#### Javascript

```
const claims = {
  'x-ably-clientId': 'user-123'
};
```

#### Python

```
claims = {
    'x-ably-clientId': 'user-123'
}
```

#### Java

```
Map<String, String> claims = new HashMap<>();
claims.put("x-ably-clientId", "user-123");
```

</Code>

The `clientId` is automatically attached to every message the user publishes, so agents can trust this identity.

<Code>

#### Javascript

```
await channel.subscribe('user-input', (message) => {
  const userId = message.clientId;
  // promptId is a user-generated UUID for correlating responses
  const { promptId, text } = message.data;

  console.log(`Received prompt from user ${userId}`);
  processAndRespond(channel, text, promptId, userId);
});
```

#### Python

```
def on_user_input(message):
    user_id = message.client_id
    # promptId is a user-generated UUID for correlating responses
    prompt_id = message.data['promptId']
    text = message.data['text']

    print(f'Received prompt from user {user_id}')
    process_and_respond(channel, text, prompt_id, user_id)

await channel.subscribe('user-input', on_user_input)
```

#### Java

```
channel.subscribe("user-input", message -> {
    String userId = message.clientId;
    // promptId is a user-generated UUID for correlating responses
    JsonObject data = (JsonObject) message.data;
    String promptId = data.get("promptId").getAsString();
    String text = data.get("text").getAsString();

    System.out.println("Received prompt from user " + userId);
    processAndRespond(channel, text, promptId, userId);
});
```

</Code>

### Verify by role

Use [user claims](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-claims) to verify that a message comes from a user rather than another agent sharing the channel. This is useful when the agent needs to distinguish message sources without needing the specific user identity.

When a user [authenticates with Ably](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#authenticating), embed their role in the JWT:

<Code>

#### Javascript

```
const claims = {
  'ably.channel.*': 'user'
};
```

#### Python

```
claims = {
    'ably.channel.*': 'user'
}
```

#### Java

```
Map<String, String> claims = new HashMap<>();
claims.put("ably.channel.*", "user");
```

</Code>

The user claim is automatically attached to every message the user publishes, so agents can trust this role information.

<Code>

#### Javascript

```
await channel.subscribe('user-input', (message) => {
  const role = message.extras?.userClaim;
  // promptId is a user-generated UUID for correlating responses
  const { promptId, text } = message.data;

  if (role !== 'user') {
    console.log('Ignoring message from non-user');
    return;
  }

  processAndRespond(channel, text, promptId);
});
```

#### Python

```
def on_user_input(message):
    role = message.extras.get('userClaim')
    # promptId is a user-generated UUID for correlating responses
    prompt_id = message.data['promptId']
    text = message.data['text']

    if role != 'user':
        print('Ignoring message from non-user')
        return

    process_and_respond(channel, text, prompt_id)

await channel.subscribe('user-input', on_user_input)
```

#### Java

```
channel.subscribe("user-input", message -> {
    String role = message.extras.get("userClaim").getAsString();
    // promptId is a user-generated UUID for correlating responses
    JsonObject data = (JsonObject) message.data;
    String promptId = data.get("promptId").getAsString();
    String text = data.get("text").getAsString();

    if (!role.equals("user")) {
        System.out.println("Ignoring message from non-user");
        return;
    }

    processAndRespond(channel, text, promptId);
});
```

</Code>

## Publish user input

Users publish messages to the channel to send prompts to the agent. Generate a unique `promptId` for each message to correlate agent responses back to the original prompt.

<Code>

### Javascript

```
const channel = ably.channels.get('your-channel-name');

const promptId = crypto.randomUUID();
await channel.publish('user-input', {
  promptId: promptId,
  text: 'What is the weather like today?'
});
```

### Python

```
import uuid

channel = ably.channels.get('your-channel-name')

prompt_id = str(uuid.uuid4())
message = Message(
    name='user-input',
    data={
        'promptId': prompt_id,
        'text': 'What is the weather like today?'
    }
)
await channel.publish(message)
```

### Java

```
Channel channel = ably.channels.get("your-channel-name");

String promptId = UUID.randomUUID().toString();
JsonObject data = new JsonObject();
data.addProperty("promptId", promptId);
data.addProperty("text", "What is the weather like today?");
channel.publish("user-input", data);
```

</Code>

<Aside data-type="note">
Set [`echoMessages`](https://ably.com/docs/api/realtime-sdk/types.md#client-options) to `false` to prevent the publishing client from receiving its own message, avoiding billing for [echoed messages](https://ably.com/docs/pub-sub/advanced.md#echo). When disabled, update your UI to reflect user input immediately upon sending rather than waiting for the echoed message.
</Aside>

## Subscribe to user input

The agent subscribes to a channel to receive messages from users. When a user publishes a message to the channel, the agent receives it through the subscription callback.

The following example demonstrates an agent subscribing to receive user input:

<Code>

### Javascript

```
const Ably = require('ably');

const ably = new Ably.Realtime({ key: 'your-api-key' });
const channel = ably.channels.get('your-channel-name');

await channel.subscribe('user-input', (message) => {
  const { promptId, text } = message.data;
  const userId = message.clientId;

  console.log(`Received prompt from ${userId}: ${text}`);

  // Process the prompt and generate a response
  processAndRespond(channel, text, promptId);
});
```

### Python

```
from ably import AblyRealtime

ably = AblyRealtime(key='your-api-key')
channel = ably.channels.get('your-channel-name')

def on_user_input(message):
    prompt_id = message.data['promptId']
    text = message.data['text']
    user_id = message.client_id

    print(f'Received prompt from {user_id}: {text}')

    # Process the prompt and generate a response
    process_and_respond(channel, text, prompt_id)

await channel.subscribe('user-input', on_user_input)
```

### Java

```
import io.ably.lib.realtime.AblyRealtime;
import io.ably.lib.realtime.Channel;

AblyRealtime ably = new AblyRealtime("your-api-key");
Channel channel = ably.channels.get("your-channel-name");

channel.subscribe("user-input", message -> {
    JsonObject data = (JsonObject) message.data;
    String promptId = data.get("promptId").getAsString();
    String text = data.get("text").getAsString();
    String userId = message.clientId;

    System.out.println("Received prompt from " + userId + ": " + text);

    // Process the prompt and generate a response
    processAndRespond(channel, text, promptId);
});
```

</Code>

<Aside data-type="note">
The agent can use `message.clientId` to identify which user sent the prompt. This is a verified identity when using [identified clients](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-identity).
</Aside>

## Publish agent responses

When the agent sends a response, it includes the `promptId` from the original input so users know which prompt the response relates to. This is especially important when users send multiple prompts in quick succession or when responses are streamed.

Use the `extras.headers` field to include the `promptId` in agent responses:

<Code>

### Javascript

```
async function processAndRespond(channel, prompt, promptId) {
  // Generate the response (e.g., call your AI model)
  const response = await generateAIResponse(prompt);

  // Publish the response with the promptId for correlation
  await channel.publish({
    name: 'agent-response',
    data: response,
    extras: {
      headers: {
        promptId: promptId
      }
    }
  });
}
```

### Python

```
async def process_and_respond(channel, prompt, prompt_id):
    # Generate the response (e.g., call your AI model)
    response = await generate_ai_response(prompt)

    message = Message(
        name='agent-response',
        data=response,
        extras={
            'headers': {
                'promptId': prompt_id
            }
        }
    )

    # Publish the response with the promptId for correlation
    await channel.publish(message)
```

### Java

```
void processAndRespond(Channel channel, String prompt, String promptId) {
    // Generate the response (e.g., call your AI model)
    String response = generateAIResponse(prompt);

    // Publish the response with the promptId for correlation
    JsonObject extras = new JsonObject();
    JsonObject headers = new JsonObject();
    headers.addProperty("promptId", promptId);
    extras.add("headers", headers);

    Message message = new Message("agent-response", response, new MessageExtras(extras));

    channel.publish(message);
}
```

</Code>

The user's client can then match responses to their original prompts:

<Code>

### Javascript

```
const pendingPrompts = new Map();

// Send a prompt and track it
async function sendPrompt(text) {
  const promptId = crypto.randomUUID();
  pendingPrompts.set(promptId, { text });
  await channel.publish('user-input', { promptId, text });
  return promptId;
}

// Handle responses
await channel.subscribe('agent-response', (message) => {
  const promptId = message.extras?.headers?.promptId;

  if (promptId && pendingPrompts.has(promptId)) {
    const originalPrompt = pendingPrompts.get(promptId);
    console.log(`Response for "${originalPrompt.text}": ${message.data}`);
    pendingPrompts.delete(promptId);
  }
});
```

### Python

```
import uuid

pending_prompts = {}

# Send a prompt and track it
async def send_prompt(text):
    prompt_id = str(uuid.uuid4())
    pending_prompts[prompt_id] = {'text': text}
    message = Message(name='user-input', data={'promptId': prompt_id, 'text': text})
    await channel.publish(message)
    return prompt_id

# Handle responses
def on_agent_response(message):
    prompt_id = message.extras.get('headers', {}).get('promptId')

    if prompt_id and prompt_id in pending_prompts:
        original_prompt = pending_prompts[prompt_id]
        print(f'Response for "{original_prompt["text"]}": {message.data}')
        del pending_prompts[prompt_id]

await channel.subscribe('agent-response', on_agent_response)
```

### Java

```
Map<String, Map<String, String>> pendingPrompts = new ConcurrentHashMap<>();

// Send a prompt and track it
String sendPrompt(String text) {
    String promptId = UUID.randomUUID().toString();
    Map<String, String> promptData = new HashMap<>();
    promptData.put("text", text);
    pendingPrompts.put(promptId, promptData);

    JsonObject data = new JsonObject();
    data.addProperty("promptId", promptId);
    data.addProperty("text", text);
    channel.publish("user-input", data);

    return promptId;
}

// Handle responses
channel.subscribe("agent-response", message -> {
    JsonObject headers = message.extras.asJsonObject().get("headers");
    String promptId = headers != null ? headers.get("promptId").getAsString() : null;

    if (promptId != null && pendingPrompts.containsKey(promptId)) {
        Map<String, String> originalPrompt = pendingPrompts.get(promptId);
        System.out.println("Response for \"" + originalPrompt.get("text") + "\": " + message.data);
        pendingPrompts.remove(promptId);
    }
});
```

</Code>

<Aside data-type="note">
Set [`echoMessages`](https://ably.com/docs/api/realtime-sdk/types.md#client-options) to `false` on the agent's Ably client to prevent the agent from receiving its own responses, avoiding billing for [echoed messages](https://ably.com/docs/pub-sub/advanced.md#echo).
</Aside>

## Stream responses

For longer AI responses, you'll typically want to stream tokens back to the user rather than waiting for the complete response. The `promptId` correlation allows users to associate streamed tokens with their original prompt.

When streaming tokens using [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) or [message-per-token](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md) patterns, include the `promptId` in the message extras:

<Code>

### Javascript

```
async function streamResponse(channel, prompt, promptId) {
  // Create initial message for message-per-response pattern
  const message = await channel.publish({
    name: 'agent-response',
    data: '',
    extras: {
      headers: {
        promptId: promptId
      }
    }
  });

  // Stream tokens by appending to the message
  for await (const token of generateTokens(prompt)) {
    await channel.appendMessage({
      serial: message.serial,
      data: token,
      extras: {
        headers: {
          promptId: promptId
        }
      }
    });
  }
}
```

### Python

```
async def stream_response(channel, prompt, prompt_id):
    # Create initial message for message-per-response pattern
    message = Message(
        name='agent-response',
        data='',
        extras={
            'headers': {
                'promptId': prompt_id
            }
        }
    )
    result = await channel.publish(message)
    message_serial = result.serials[0]

    # Stream tokens by appending to the message
    async for token in generate_tokens(prompt):
        await channel.append_message(Message(
            serial=message_serial,
            data=token,
            extras={
                'headers': {
                    'promptId': prompt_id
                }
            }
        ))
```

### Java

```
void streamResponse(Channel channel, String prompt, String promptId) throws Exception {
    // Create initial message for message-per-response pattern
    JsonObject extras = new JsonObject();
    JsonObject headers = new JsonObject();
    headers.addProperty("promptId", promptId);
    extras.add("headers", headers);

    CompletableFuture<PublishResult> publishFuture = new CompletableFuture<>();
    channel.publish("agent-response", "", extras, new Callback<PublishResult>() {
        @Override
        public void onSuccess(PublishResult result) {
            publishFuture.complete(result);
        }

        @Override
        public void onError(ErrorInfo reason) {
            publishFuture.completeExceptionally(AblyException.fromErrorInfo(reason));
        }
    });
    String messageSerial = publishFuture.get().serials[0];

    // Stream tokens by appending to the message
    for (String token : generateTokens(prompt)) {
        JsonObject appendExtras = new JsonObject();
        JsonObject appendHeaders = new JsonObject();
        appendHeaders.addProperty("promptId", promptId);
        appendExtras.add("headers", appendHeaders);

        channel.appendMessage(messageSerial, token, appendExtras);
    }
}
```

</Code>

<Aside data-type="note">
When appending tokens, include the `extras` with all headers to preserve them on the message. If you omit `extras` from an append operation, any existing headers will be removed. See token streaming with the [message per response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) pattern for more details.
</Aside>

## Handle multiple concurrent prompts

Users may send multiple prompts before receiving responses, especially during long-running AI operations. The correlation pattern ensures responses are matched to the correct prompts:

<Code>

### Javascript

```
// Agent handling multiple concurrent prompts
const activeRequests = new Map();

await channel.subscribe('user-input', async (message) => {
  const { promptId, text } = message.data;
  const userId = message.clientId;

  // Track active request
  activeRequests.set(promptId, {
    userId,
    text,
  });

  try {
    await streamResponse(channel, text, promptId);
  } finally {
    activeRequests.delete(promptId);
  }
});
```

### Python

```
# Agent handling multiple concurrent prompts
active_requests = {}

async def on_user_input(message):
    prompt_id = message.data['promptId']
    text = message.data['text']
    user_id = message.client_id

    # Track active request
    active_requests[prompt_id] = {
        'userId': user_id,
        'text': text,
    }

    try:
        await stream_response(channel, text, prompt_id)
    finally:
        del active_requests[prompt_id]

await channel.subscribe('user-input', on_user_input)
```

### Java

```
// Agent handling multiple concurrent prompts
Map<String, Map<String, String>> activeRequests = new ConcurrentHashMap<>();

channel.subscribe("user-input", message -> {
    JsonObject data = (JsonObject) message.data;
    String promptId = data.get("promptId").getAsString();
    String text = data.get("text").getAsString();
    String userId = message.clientId;

    // Track active request
    Map<String, String> requestData = new HashMap<>();
    requestData.put("userId", userId);
    requestData.put("text", text);
    activeRequests.put(promptId, requestData);

    try {
        streamResponse(channel, text, promptId);
    } finally {
        activeRequests.remove(promptId);
    }
});
```

</Code>

## Related Topics

- [Tool calls](https://ably.com/docs/ai-transport/messaging/tool-calls.md): Stream tool call execution visibility to users, enabling transparent AI interactions and generative UI experiences.
- [Human-in-the-loop](https://ably.com/docs/ai-transport/messaging/human-in-the-loop.md): Implement human-in-the-loop workflows for AI agents using Ably capabilities and claims to ensure authorized users approve sensitive tool calls.
- [Chain of thought](https://ably.com/docs/ai-transport/messaging/chain-of-thought.md): Stream chain-of-thought reasoning from thinking models in AI applications
- [Citations](https://ably.com/docs/ai-transport/messaging/citations.md): Attach source citations to AI responses using message annotations
- [Completion and cancellation](https://ably.com/docs/ai-transport/messaging/completion-and-cancellation.md): Signal when AI responses are complete and support user-initiated cancellation of in-progress responses.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
