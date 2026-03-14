# Source: https://ably.com/docs/ai-transport/guides/anthropic/anthropic-human-in-the-loop.md

# Guide: Human-in-the-loop approval with Anthropic

This guide shows you how to implement a human-in-the-loop (HITL) approval workflow for AI agent tool calls using Anthropic and Ably. The agent requests human approval before executing sensitive operations, with role-based access control to verify approvers have sufficient permissions.

When the model calls a tool that requires human approval, the tool implementation itself handles the approval check before executing. Rather than executing immediately, the tool publishes an `approval-request` message to an Ably channel, waits for an `approval-response` from a human approver, verifies the approver has the required role using [claims embedded in their JWT token](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-claims), and only then executes the action. The model calls the tool as normal, and the approval logic lives inside the tool's implementation.

<Aside data-type="further-reading">
To learn more about human-in-the-loop patterns and verification strategies, see the [human-in-the-loop](https://ably.com/docs/ai-transport/messaging/human-in-the-loop.md) documentation.
</Aside>

## Prerequisites

To follow this guide, you need:

- Node.js 20 or higher
- An Anthropic API key
- An Ably API key

Useful links:

- [Anthropic tool use guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)
- [Ably JavaScript SDK getting started](https://ably.com/docs/getting-started/javascript.md)

Create a new Node project, which will contain the agent, client, and server code:

<Code>

### Shell

```
mkdir ably-anthropic-hitl-example && cd ably-anthropic-hitl-example
npm init -y
```

</Code>

Install the required packages using NPM:

<Code>

### Shell

```
npm install @anthropic-ai/sdk@^0.71 ably@^2 express jsonwebtoken
```

</Code>

<Aside data-type="note">
This guide uses version 0.71.x of the Anthropic SDK. Some details of interacting with the Anthropic SDK may differ from those given here if using a different major version.
</Aside>

Export your API keys to the environment:

<Code>

### Shell

```
export ANTHROPIC_API_KEY="your_anthropic_api_key_here"
export ABLY_API_KEY="your_ably_api_key_here"
```

</Code>

## Step 1: Initialize the agent

Set up the agent that will call Anthropic and request human approval for sensitive operations. This example uses a `publish_blog_post` tool that requires authorization before execution.

Initialize the Anthropic and Ably clients, and create a channel for communication between the agent and human approvers.

Add the following to a new file called `agent.mjs`:

<Code>

### Javascript

```
import Anthropic from '@anthropic-ai/sdk';
import Ably from 'ably';

const anthropic = new Anthropic();

// Initialize Ably Realtime client
const realtime = new Ably.Realtime({
  key: process.env.ABLY_API_KEY,
  echoMessages: false
});

// Wait for connection to be established
await realtime.connection.once('connected');

// Create a channel for HITL communication
const channel = realtime.channels.get('ai:your-channel-name');

// Track pending approval requests
const pendingApprovals = new Map();

// Function that executes the approved action
async function publishBlogPost(args) {
  const { title } = args;
  console.log(`Publishing blog post: ${title}`);
  // In production, this would call your CMS API
  return { published: true, title };
}
```

</Code>

<Aside data-type="note">
Set [`echoMessages`](https://ably.com/docs/api/realtime-sdk/types.md#client-options) to `false` on the agent's Ably client to prevent the agent from receiving its own messages, avoiding billing for [echoed messages](https://ably.com/docs/pub-sub/advanced.md#echo).
</Aside>

Tools that modify data, access sensitive resources, or perform actions with business impact are good candidates for HITL approval workflows.

## Step 2: Request human approval

When the model returns a tool use block, publish an approval request to the channel and wait for a human decision. The tool use ID is passed in the message headers to correlate requests with responses.

Add the approval request function to `agent.mjs`:

<Code>

### Javascript

```
async function requestHumanApproval(toolUse) {
  const approvalPromise = new Promise((resolve, reject) => {
    pendingApprovals.set(toolUse.id, { toolUse, resolve, reject });
  });

  await channel.publish({
    name: 'approval-request',
    data: {
      tool: toolUse.name,
      arguments: toolUse.input
    },
    extras: {
      headers: {
        toolCallId: toolUse.id
      }
    }
  });

  console.log(`Approval request sent for: ${toolUse.name}`);
  return approvalPromise;
}
```

</Code>

The `toolUse.id` provided by Anthropic correlates the approval request with the response, enabling the agent to handle multiple concurrent approval flows.

## Step 3: Subscribe to approval responses

Set up a subscription to receive approval decisions from human users. When a response arrives, verify the approver has sufficient permissions using role-based access control before resolving the pending promise.

Add the subscription handler to `agent.mjs`:

<Code>

### Javascript

```
async function subscribeApprovalResponses() {
  // Define role hierarchy from lowest to highest privilege
  const roleHierarchy = ['editor', 'publisher', 'admin'];

  // Define minimum role required for each tool
  const approvalPolicies = {
    publish_blog_post: { minRole: 'publisher' }
  };

  function canApprove(approverRole, requiredRole) {
    const approverLevel = roleHierarchy.indexOf(approverRole);
    const requiredLevel = roleHierarchy.indexOf(requiredRole);
    return approverLevel >= requiredLevel;
  }

  await channel.subscribe('approval-response', async (message) => {
    const { decision } = message.data;
    const toolCallId = message.extras?.headers?.toolCallId;
    const pending = pendingApprovals.get(toolCallId);

    if (!pending) {
      console.log(`No pending approval for tool call: ${toolCallId}`);
      return;
    }

    const policy = approvalPolicies[pending.toolUse.name];
    // Get the trusted role from the JWT user claim
    const approverRole = message.extras?.userClaim;

    // Verify the approver's role meets the minimum required
    if (!canApprove(approverRole, policy.minRole)) {
      console.log(`Insufficient role: ${approverRole} < ${policy.minRole}`);
      pending.reject(new Error(
        `Approver role '${approverRole}' insufficient for required '${policy.minRole}'`
      ));
      pendingApprovals.delete(toolCallId);
      return;
    }

    // Process the decision
    if (decision === 'approved') {
      console.log(`Approved by ${approverRole}`);
      pending.resolve({ approved: true, approverRole });
    } else {
      console.log(`Rejected by ${approverRole}`);
      pending.reject(new Error(`Action rejected by ${approverRole}`));
    }
    pendingApprovals.delete(toolCallId);
  });
}
```

</Code>

The `message.extras.userClaim` contains the role embedded in the approver's JWT token, providing a trusted source for authorization decisions. See [user claims](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-claims) for details on embedding claims in tokens. This ensures only users with sufficient privileges can approve sensitive operations.

## Step 4: Process tool calls

Create a function to process tool use blocks by requesting approval and executing the action if approved.

Add the tool processing function to `agent.mjs`:

<Code>

### Javascript

```
async function processToolUse(toolUse) {
  if (toolUse.name === 'publish_blog_post') {
    // requestHumanApproval returns a promise that resolves when the human
    // approves the tool use, or rejects if the human explicitly rejects
    // the tool call or the approver's role is insufficient.
    await requestHumanApproval(toolUse);
    return await publishBlogPost(toolUse.input);
  }
  throw new Error(`Unknown tool: ${toolUse.name}`);
}
```

</Code>

The function awaits approval before executing. If the approver rejects or has insufficient permissions, the promise rejects and the tool is not executed.

## Step 5: Run the agent

Create the main agent loop that sends prompts to the model and processes any tool use blocks that require approval.

Add the agent runner to `agent.mjs`:

<Code>

### Javascript

```
async function runAgent(prompt) {
  await subscribeApprovalResponses();

  console.log(`User: ${prompt}`);

  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    tools: [
      {
        name: 'publish_blog_post',
        description: 'Publish a blog post to the website. Requires human approval.',
        input_schema: {
          type: 'object',
          properties: {
            title: {
              type: 'string',
              description: 'Title of the blog post to publish'
            }
          },
          required: ['title']
        }
      }
    ],
    messages: [{ role: 'user', content: prompt }]
  });

  const toolUseBlocks = response.content.filter(block => block.type === 'tool_use');

  for (const toolUse of toolUseBlocks) {
    console.log(`Tool use: ${toolUse.name}`);
    try {
      const result = await processToolUse(toolUse);
      console.log('Result:', result);
    } catch (err) {
      console.error('Tool use failed:', err.message);
    }
  }
}

runAgent("Publish the blog post called 'Introducing our new API'");
```

</Code>

## Step 6: Create the authentication server

The authentication server issues JWT tokens with embedded role claims. The role claim is trusted by Ably and included in messages, enabling secure role-based authorization.

Add the following to a new file called `server.mjs`:

<Code>

### Javascript

```
import express from 'express';
import jwt from 'jsonwebtoken';

const app = express();

// Mock authentication - replace with your actual auth logic
function authenticateUser(req, res, next) {
  // In production, verify the user's session/credentials
  req.user = { id: 'user123', role: 'publisher' };
  next();
}

// Return claims to embed in the JWT
function getJWTClaims(user) {
  return {
    'ably.channel.*': user.role
  };
}

app.get('/api/auth/token', authenticateUser, (req, res) => {
  const [keyName, keySecret] = process.env.ABLY_API_KEY.split(':');

  const token = jwt.sign(getJWTClaims(req.user), keySecret, {
    algorithm: 'HS256',
    keyid: keyName,
    expiresIn: '1h'
  });

  res.type('application/jwt').send(token);
});

app.listen(3001, () => {
  console.log('Auth server running on http://localhost:3001');
});
```

</Code>

The `ably.channel.*` claim embeds the user's role in the JWT. When the user publishes messages, this claim is available as `message.extras.userClaim`, providing a trusted source for authorization.

Run the server:

<Code>

### Shell

```
node server.mjs
```

</Code>

## Step 7: Create the approval client

The approval client receives approval requests and allows humans to approve or reject them. It authenticates via the server to obtain a JWT with the user's role.

Add the following to a new file called `client.mjs`:

<Code>

### Javascript

```
import Ably from 'ably';
import readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const realtime = new Ably.Realtime({
  authCallback: async (tokenParams, callback) => {
    try {
      const response = await fetch('http://localhost:3001/api/auth/token');
      const token = await response.text();
      callback(null, token);
    } catch (error) {
      callback(error, null);
    }
  }
});

realtime.connection.on('connected', () => {
  console.log('Connected to Ably');
  console.log('Waiting for approval requests...\n');
});

const channel = realtime.channels.get('ai:your-channel-name');

await channel.subscribe('approval-request', (message) => {
  const request = message.data;

  console.log('\n========================================');
  console.log('APPROVAL REQUEST');
  console.log('========================================');
  console.log(`Tool: ${request.tool}`);
  console.log(`Arguments: ${JSON.stringify(request.arguments, null, 2)}`);
  console.log('========================================');

  rl.question('Approve this action? (y/n): ', async (answer) => {
    const decision = answer.toLowerCase() === 'y' ? 'approved' : 'rejected';

    await channel.publish({
      name: 'approval-response',
      data: { decision },
      extras: {
        headers: {
          toolCallId: message.extras?.headers?.toolCallId
        }
      }
    });

    console.log(`Decision sent: ${decision}\n`);
  });
});
```

</Code>

Run the client in a separate terminal:

<Code>

### Shell

```
node client.mjs
```

</Code>

With the server, client, and agent running, the workflow proceeds as follows:

1. The agent sends a prompt to the model that triggers a tool use
2. The agent publishes an approval request to the channel
3. The client displays the request and prompts the user
4. The user approves or rejects the request
5. The agent verifies the approver's role meets the minimum requirement
6. If approved and authorized, the agent executes the tool

## Next steps

- Learn more about [human-in-the-loop](https://ably.com/docs/ai-transport/messaging/human-in-the-loop.md) patterns and verification strategies
- Explore [identifying users and agents](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md) for secure identity verification
- Understand [sessions and identity](https://ably.com/docs/ai-transport/sessions-identity.md) in AI-enabled applications
- Learn about [tool calls](https://ably.com/docs/ai-transport/messaging/tool-calls.md) for agent-to-agent communication

## Related Topics

- [Message per response](https://ably.com/docs/ai-transport/guides/anthropic/anthropic-message-per-response.md): Stream tokens from the Anthropic Messages API over Ably in realtime using message appends.
- [Message per token](https://ably.com/docs/ai-transport/guides/anthropic/anthropic-message-per-token.md): Stream tokens from the Anthropic Messages API over Ably in realtime.
- [Citations](https://ably.com/docs/ai-transport/guides/anthropic/anthropic-citations.md): Attach source citations to AI responses from the Anthropic Messages API using Ably message annotations.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
