# Source: https://ably.com/docs/ai-transport/messaging/human-in-the-loop.md

# Human in the loop

Human-in-the-loop (HITL) enables human oversight of AI agent actions. When an agent needs to perform sensitive operations, such as modifying data, performing sensitive actions, or accessing restricted resources, the action is paused and routed to an authorized human for approval before execution.

This pattern ensures humans remain in control of high-stakes AI operations, providing safety, compliance, and trust in agentic workflows.

## Why human-in-the-loop matters

AI agents are increasingly capable of taking autonomous actions, but certain operations require human judgement:

- Safety: Prevent unintended consequences from AI decisions.
- Compliance: Meet regulatory requirements for human oversight in sensitive domains.
- Trust: Build user confidence by keeping humans in control of critical actions.
- Accountability: Create clear audit trails of who approved what actions.
- Clarification: Allow the agent to request more information or guidance from users before proceeding.

HITL puts a human approval step in front of agent actions that carry risk or uncertainty.

## How it works

Human-in-the-loop authorization follows a request-approval pattern over Ably channels:

1. The AI agent determines a tool call requires human approval.
2. The agent publishes an authorization request to the channel.
3. An authorized user receives and reviews the request.
4. The human approves or rejects the request.
5. The agent receives the decision, verifies the responder's identity or role and proceeds accordingly.

## Request human approval

When an agent identifies an action requiring human oversight, it publishes a request to the channel. The request should include sufficient context for the approver to make an informed decision. The `toolCallId` in the message [extras](https://ably.com/docs/messages.md#properties) enables correlation between requests and responses when handling multiple concurrent approval flows.

The agent stores each pending request in some local state before publishing. When an approval response arrives, the agent uses the `toolCallId` to retrieve the original tool call details, verify the approver's permissions for that specific action, execute the tool if approved, and resolve the pending approval.

<Code>

### Javascript

```
const channel = realtime.channels.get('your-channel-name');
const pendingApprovals = new Map();

async function requestHumanApproval(toolCall) {
  pendingApprovals.set(toolCall.id, { toolCall });

  await channel.publish({
    name: 'approval-request',
    data: {
      tool: toolCall.name,
      arguments: toolCall.arguments
    },
    extras: {
      headers: {
        toolCallId: toolCall.id
      }
    }
  });
}
```

### Python

```
import uuid

channel = ably.channels.get('your-channel-name')

async def request_human_approval(tool_call):
    request_id = str(uuid.uuid4())

    await channel.publish('approval-request', {
        'requestId': request_id,
        'action': tool_call['name'],
        'parameters': tool_call['parameters']
    })

    return request_id
```

### Java

```
Channel channel = ably.channels.get("your-channel-name");

String requestHumanApproval(ToolCall toolCall) {
    String requestId = UUID.randomUUID().toString();

    JsonObject data = new JsonObject();
    data.addProperty("requestId", requestId);
    data.addProperty("action", toolCall.getName());
    data.add("parameters", toolCall.getParameters());

    channel.publish("approval-request", data);

    return requestId;
}
```

</Code>

<Aside data-type="note">
Set [`echoMessages`](https://ably.com/docs/api/realtime-sdk/types.md#client-options) to `false` on the agent's Ably client to prevent the agent from receiving its own approval requests, avoiding billing for [echoed messages](https://ably.com/docs/pub-sub/advanced.md#echo).
</Aside>

## Review and decide

Authorized humans subscribe to approval requests on the conversation channel and publish their decisions. The `toolCallId` correlates the response with the original request.

Use [identified clients](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-identity) or [user claims](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-claims) to establish a verified identity or role for the approver. For example, when a user [authenticates with Ably](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#authenticating), embed their identity and role in the JWT:

<Code>

### Javascript

```
const claims = {
  'x-ably-clientId': 'user-123',
  'ably.channel.*': 'user'
};
```

### Python

```
claims = {
    'x-ably-clientId': 'user-123',
    'ably.channel.*': 'user'
}
```

### Java

```
Map<String, String> claims = new HashMap<>();
claims.put("x-ably-clientId", "user-123");
claims.put("ably.channel.*", "user");
```

</Code>

The `clientId` and user claims are automatically attached to every message the user publishes and cannot be forged, so agents can trust this identity and role information.

<Aside data-type="further-reading">
For more information about establishing verified identities and roles, see [Identifying users and agents](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md).
</Aside>

<Code>

### Javascript

```
const channel = realtime.channels.get('your-channel-name');

await channel.subscribe('approval-request', (message) => {
  const request = message.data;
  const toolCallId = message.extras?.headers?.toolCallId;
  // Display request for human review
  displayApprovalUI(request, toolCallId);
});

async function approve(toolCallId) {
  await channel.publish({
    name: 'approval-response',
    data: {
      decision: 'approved'
    },
    extras: {
      headers: {
        toolCallId: toolCallId
      }
    }
  });
}

async function reject(toolCallId) {
  await channel.publish({
    name: 'approval-response',
    data: {
      decision: 'rejected'
    },
    extras: {
      headers: {
        toolCallId: toolCallId
      }
    }
  });
}
```

### Python

```
channel = ably.channels.get('your-channel-name')

def on_approval_request(message):
    request = message.data
    # Display request for human review
    display_approval_ui(request)

await channel.subscribe('approval-request', on_approval_request)

async def approve(request_id):
    await channel.publish('approval-response', {
        'requestId': request_id,
        'decision': 'approved'
    })

async def reject(request_id):
    await channel.publish('approval-response', {
        'requestId': request_id,
        'decision': 'rejected'
    })
```

### Java

```
Channel channel = ably.channels.get("your-channel-name");

channel.subscribe("approval-request", message -> {
    JsonObject request = (JsonObject) message.data;
    // Display request for human review
    displayApprovalUI(request);
});

void approve(String requestId) {
    JsonObject data = new JsonObject();
    data.addProperty("requestId", requestId);
    data.addProperty("decision", "approved");
    channel.publish("approval-response", data);
}

void reject(String requestId) {
    JsonObject data = new JsonObject();
    data.addProperty("requestId", requestId);
    data.addProperty("decision", "rejected");
    channel.publish("approval-response", data);
}
```

</Code>

<Aside data-type="note">
Set [`echoMessages`](https://ably.com/docs/api/realtime-sdk/types.md#client-options) to `false` in the client options to prevent approval responses from being echoed back to the approver. This avoids billing for the echoed message. When disabled, update your UI to reflect the approval decision immediately upon sending rather than waiting for the echoed message. See [echoing messages](https://ably.com/docs/pub-sub/advanced.md#echo) for more details.
</Aside>

## Process the decision

The agent listens for human decisions and acts accordingly. When a response arrives, the agent retrieves the pending request using the `toolCallId`, verifies that the user is permitted to approve that specific action, and either executes the action or handles the rejection.

<Aside data-type="note">
For audit trails, use [integration rules](https://ably.com/docs/platform/integrations.md) to stream approval messages to external systems.
</Aside>

### Verify by user identity

Use the `clientId` to identify the approver and look up their permissions in your database or access control system. This approach is useful when permissions are managed externally or change frequently.

<Aside data-type="note">
This approach requires the user to authenticate as an [identified client](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-identity) with a verified `clientId`.
</Aside>

<Code>

#### Javascript

```
const pendingApprovals = new Map();

await channel.subscribe('approval-response', async (message) => {
  const response = message.data;
  const toolCallId = message.extras?.headers?.toolCallId;
  const pending = pendingApprovals.get(toolCallId);

  if (!pending) return;

  // The clientId is the trusted approver identity
  const approverId = message.clientId;

  // Look up user-specific permissions from your database
  const userPermissions = await getUserPermissions(approverId);

  if (!userPermissions.canApprove(pending.toolCall.name)) {
    console.log(`User ${approverId} not authorized to approve ${pending.toolCall.name}`);
    return;
  }

  if (response.decision === 'approved') {
    const result = await executeToolCall(pending.toolCall);
    console.log(`Action approved by ${approverId}`);
  } else {
    console.log(`Action rejected by ${approverId}`);
  }

  pendingApprovals.delete(toolCallId);
});
```

#### Python

```
pending_approvals = {}

async def on_approval_response(message):
    response = message.data
    pending = pending_approvals.get(response['requestId'])

    if not pending:
        return

    # The clientId is verified by Ably - this is the trusted approver identity
    approver_id = message.client_id

    # Look up user-specific permissions from your database
    user_permissions = await get_user_permissions(approver_id)

    if not user_permissions.can_approve(pending['toolCall']['name']):
        print(f"User {approver_id} not authorized to approve {pending['toolCall']['name']}")
        return

    if response['decision'] == 'approved':
        result = await execute_tool_call(pending['toolCall'])
        print(f"Action approved by {approver_id}")
    else:
        print(f"Action rejected by {approver_id}")

    del pending_approvals[response['requestId']]

await channel.subscribe('approval-response', on_approval_response)
```

#### Java

```
Map<String, PendingApproval> pendingApprovals = new ConcurrentHashMap<>();

channel.subscribe("approval-response", message -> {
    JsonObject response = (JsonObject) message.data;
    PendingApproval pending = pendingApprovals.get(response.get("requestId").getAsString());

    if (pending == null) return;

    // The clientId is verified by Ably - this is the trusted approver identity
    String approverId = message.clientId;

    // Look up user-specific permissions from your database
    UserPermissions userPermissions = getUserPermissions(approverId);

    if (!userPermissions.canApprove(pending.getToolCall().getName())) {
        System.out.println("User " + approverId + " not authorized to approve " + pending.getToolCall().getName());
        return;
    }

    if (response.get("decision").getAsString().equals("approved")) {
        Object result = executeToolCall(pending.getToolCall());
        System.out.println("Action approved by " + approverId);
    } else {
        System.out.println("Action rejected by " + approverId);
    }

    pendingApprovals.remove(response.get("requestId").getAsString());
});
```

</Code>

### Verify by role

Use [user claims](https://ably.com/docs/auth/capabilities.md#custom-restrictions-on-channels-) to embed roles directly in the JWT for role-based access control (RBAC). This approach is useful when permissions are role-based rather than user-specific, allowing you to make authorization decisions based on the user's role without looking up individual user permissions.

<Aside data-type="note">
This approach uses [authenticated claims for users](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md#user-claims) to embed custom claims in JWTs that represent user roles or attributes.
</Aside>

Different actions may require different authorization levels. For example, an editor might be able to create drafts for review, but only a publisher or admin can approve publishing a blog post. Define approval policies that map tool names to minimum required roles, and when an approval arrives, compare the approver's role against the required role for that action type:

<Code>

#### Javascript

```
const roleHierarchy = ['editor', 'publisher', 'admin'];

const approvalPolicies = {
  publish_blog_post: 'publisher'
};

function canApprove(approverRole, requiredRole) {
  const approverLevel = roleHierarchy.indexOf(approverRole);
  const requiredLevel = roleHierarchy.indexOf(requiredRole);

  return approverLevel >= requiredLevel;
}

// When processing approval response
await channel.subscribe('approval-response', async (message) => {
  const response = message.data;
  const toolCallId = message.extras?.headers?.toolCallId;
  const pending = pendingApprovals.get(toolCallId);

  if (!pending) return;

  const policy = approvalPolicies[pending.toolCall.name];

  // Get the trusted role from the JWT claim
  const approverRole = message.extras?.userClaim;

  // Verify the approver's role meets the minimum required role for this action
  if (!canApprove(approverRole, policy)) {
    console.log(`Approver role '${approverRole}' insufficient: minimum required role is '${policy}'`);
    return;
  }

  if (response.decision === 'approved') {
    const result = await executeToolCall(pending.toolCall);
    console.log(`Action approved by role ${approverRole}`);
  } else {
    console.log(`Action rejected by role ${approverRole}`);
  }

  pendingApprovals.delete(toolCallId);
});
```

#### Python

```
role_hierarchy = ['user', 'manager', 'admin']

def can_approve(approver_role, required_role):
    approver_level = role_hierarchy.index(approver_role)
    required_level = role_hierarchy.index(required_role)

    return approver_level >= required_level

# When processing approval response
async def on_approval_response(message):
    response = message.data
    pending = pending_approvals.get(response['requestId'])
    policy = approval_policies[pending['toolCall']['name']]

    # Get the trusted role from the JWT claim
    approver_role = message.extras.get('userClaim')

    # Verify the approver's role meets the minimum required role for this action
    if not can_approve(approver_role, policy['minRole']):
        print(f"Approver role '{approver_role}' insufficient for required '{policy['minRole']}'")
        return

    if response['decision'] == 'approved':
        result = await execute_tool_call(pending['toolCall'])
        print(f"Action approved by role {approver_role}")
    else:
        print(f"Action rejected by role {approver_role}")

    del pending_approvals[response['requestId']]

await channel.subscribe('approval-response', on_approval_response)
```

#### Java

```
String[] roleHierarchy = {"user", "manager", "admin"};

boolean canApprove(String approverRole, String requiredRole) {
    int approverLevel = Arrays.asList(roleHierarchy).indexOf(approverRole);
    int requiredLevel = Arrays.asList(roleHierarchy).indexOf(requiredRole);

    return approverLevel >= requiredLevel;
}

// When processing approval response
channel.subscribe("approval-response", message -> {
    JsonObject response = (JsonObject) message.data;
    PendingApproval pending = pendingApprovals.get(response.get("requestId").getAsString());
    ApprovalPolicy policy = approvalPolicies.get(pending.getToolCall().getName());

    // Get the trusted role from the JWT claim
    String approverRole = message.extras.get("userClaim").getAsString();

    // Verify the approver's role meets the minimum required role for this action
    if (!canApprove(approverRole, policy.getMinRole())) {
        System.out.println("Approver role '" + approverRole + "' insufficient for required '" + policy.getMinRole() + "'");
        return;
    }

    if (response.get("decision").getAsString().equals("approved")) {
        Object result = executeToolCall(pending.getToolCall());
        System.out.println("Action approved by role " + approverRole);
    } else {
        System.out.println("Action rejected by role " + approverRole);
    }

    pendingApprovals.remove(response.get("requestId").getAsString());
});
```

</Code>

## Related Topics

- [Accepting user input](https://ably.com/docs/ai-transport/messaging/accepting-user-input.md): Enable users to send prompts to AI agents over Ably with verified identity and message correlation.
- [Tool calls](https://ably.com/docs/ai-transport/messaging/tool-calls.md): Stream tool call execution visibility to users, enabling transparent AI interactions and generative UI experiences.
- [Chain of thought](https://ably.com/docs/ai-transport/messaging/chain-of-thought.md): Stream chain-of-thought reasoning from thinking models in AI applications
- [Citations](https://ably.com/docs/ai-transport/messaging/citations.md): Attach source citations to AI responses using message annotations
- [Completion and cancellation](https://ably.com/docs/ai-transport/messaging/completion-and-cancellation.md): Signal when AI responses are complete and support user-initiated cancellation of in-progress responses.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
