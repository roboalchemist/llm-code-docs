# Source: https://docs.port.io/ai-interfaces/port-ai/api-interaction.md

# Port AI API Interaction

Port AI can be accessed programmatically through Port's API, enabling integration into custom applications and workflows. This provides the most flexible way to incorporate Port AI capabilities into your existing tools and processes.

## API Endpoints[â](#api-endpoints "Direct link to API Endpoints")

Port AI provides streaming API endpoints for real-time interaction:

* **Port AI Assistant**: `/v1/ai/invoke` - General-purpose AI interactions.
* **AI Agents**: `/v1/agent/<AGENT_IDENTIFIER>/invoke` - Domain-specific agent interactions.

All interactions use streaming responses as Server-Sent Events (SSE) to provide real-time updates during execution. The response will be in `text/event-stream` format.

### Interaction Process[â](#interaction-process "Direct link to Interaction Process")

1. Invoke Port AI
2. The API will start sending Server-Sent Events
3. Your client should process these events as they arrive, with each event providing information about the AI's progress or final response

### Basic API Examples[â](#basic-api-examples "Direct link to Basic API Examples")

**Port AI Assistant:**

```
curl 'https://api.port.io/v1/ai/invoke' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"prompt":"What services are failing health checks?"}'
```

**AI Agents:**

```
curl 'https://api.port.io/v1/agent/<AGENT_IDENTIFIER>/invoke' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"prompt":"Analyze the health of our production services"}'
```

**With metadata labels:**

```
curl 'https://api.port.io/v1/ai/invoke' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "prompt":"What services are failing health checks?",
    "tools": ["^(list|search|describe)_.*"],
    "labels": {
      "source": "monitoring_system",
      "environment": "production",
      "triggered_by": "automated_check"
    }
  }
```

## Streaming Response Format[â](#streaming-response-format "Direct link to Streaming Response Format")

The API responds with `Content-Type: text/event-stream; charset=utf-8`.

Each event in the stream has the following format:

```
event: <event_name>
data: <json_payload_or_string>
```

Note the blank line after `data: ...` which separates events.

### Example Event Sequence[â](#example-event-sequence "Direct link to Example Event Sequence")

```
event: tool_call
data: { "id": "call_0", "name": "list_entities", "arguments": "{\"blueprintIdentifier\":\"service\"}" }

event: tool_result
data: { "id": "call_0", "content": "Found 15 services in your catalog..." }

event: tool_call
data: { "id": "call_1", "name": "run_action", "arguments": "{\"actionIdentifier\":\"create_incident\"}" }

event: tool_result
data: { "id": "call_1", "content": "Action run created successfully with ID: run_12345" }

event: execution
data: I found 15 services in your catalog and created an incident report as requested.

event: done
data: {
  "rateLimitUsage": {
    "maxRequests": 200,
    "remainingRequests": 193,
    "maxTokens": 200000,
    "remainingTokens": 179910,
    "remainingTimeMs": 903
  },
  "monthlyQuotaUsage": {
    "monthlyLimit": 50,
    "remainingQuota": 49,
    "month": "2025-09",
    "remainingTimeMs": 1766899073
  }
}
```

## Event Types[â](#event-types "Direct link to Event Types")

**`tool_call` (Click to expand)**

Indicates that Port AI is about to execute a tool. This event provides details about the tool being called and its arguments. For large arguments, the data may be sent in multiple chunks.

```
{
  "id": "call_0",
  "name": "list_entities",
  "arguments": "{\"blueprintIdentifier\":\"service\",\"limit\":10}",
  "lastChunk": true
}
```

**Fields:**

* `id`: Unique identifier for this tool call.
* `name`: Name of the tool being executed (only included in the first chunk).
* `arguments`: JSON string containing the tool arguments (may be chunked for large payloads).
* `lastChunk`: Boolean indicating if this is the final chunk for this tool call (optional, only present on the last chunk).

**`tool_result` (Click to expand)**

Contains the result of a tool execution. For large results, the data may be sent in multiple chunks.

```
{
  "id": "call_0",
  "content": "Found 15 services in your catalog: api-gateway, user-service, payment-service...",
  "lastChunk": true
}
```

**Fields:**

* `id`: Unique identifier matching the corresponding tool call.
* `content`: The result content from the tool execution (may be chunked for large responses).
* `lastChunk`: Boolean indicating if this is the final chunk for this tool result (optional, only present on the last chunk).

**`execution` (Click to expand)**

The final textual answer or a chunk of the answer from Port AI. For longer responses, multiple `execution` events might be sent.

**`done` (Click to expand)**

Signals that Port AI has finished processing and the response stream is complete. This event also includes quota usage information for managing your API limits.

```
{
  "rateLimitUsage": {
    "maxRequests": 200,
    "remainingRequests": 193,
    "maxTokens": 200000,
    "remainingTokens": 179910,
    "remainingTimeMs": 903
  },
  "monthlyQuotaUsage": {
    "monthlyLimit": 50,
    "remainingQuota": 49,
    "month": "2025-09",
    "remainingTimeMs": 1766899073
  }
}
```

**Quota Usage Fields:**

* `maxRequests`: Maximum number of requests allowed in the current rolling window.
* `remainingRequests`: Number of requests remaining in the current window.
* `maxTokens`: Maximum number of tokens allowed in the current rolling window.
* `remainingTokens`: Number of tokens remaining in the current window.
* `remainingTimeMs`: Time in milliseconds until the rolling window resets.

## Processing Quota Information[â](#processing-quota-information "Direct link to Processing Quota Information")

Managing quota usage

Use the quota information in the `done` event to implement client-side rate limiting and avoid hitting API limits. When `remainingRequests` or `remainingTokens` are low, consider adding delays between requests or queuing them for later execution.

**JavaScript Example: Processing Quota Information (Click to expand)**

When processing the streaming response, you'll receive quota usage information in the final `done` event. Here's a JavaScript example of how to handle this:

```
const eventSource = new EventSource(apiUrl);

eventSource.addEventListener('done', (event) => {
  const data = JSON.parse(event.data);
  
  if (data.rateLimitUsage) {
    const { remainingRequests, remainingTokens, remainingTimeMs } = data.rateLimitUsage;
    
    // Check if quota is running low
    if (remainingRequests < 10 || remainingTokens < 10000) {
      console.warn('Quota running low, consider rate limiting');
      // Implement rate limiting logic
    }
    
    // Schedule next request after quota reset if needed
    if (remainingRequests === 0) {
      setTimeout(() => {
        // Safe to make next request
      }, remainingTimeMs);
    }
  }
  
  eventSource.close();
});
```

## Rate Limits and Quotas[â](#rate-limits-and-quotas "Direct link to Rate Limits and Quotas")

Port AI operates with specific limits to ensure optimal performance for all users:

LLM Provider Limits

These limits apply when using Port's managed AI infrastructure. When you [configure your own LLM provider](/ai-interfaces/port-ai/llm-providers-management/overview.md), these Port-specific limits no longer apply, and usage will be governed by your provider's own limits and pricing.

Port acts as a bridge to leading LLM providers and doesn't host LLM models internally.

### Rate Limits (Hourly)[â](#rate-limits-hourly "Direct link to Rate Limits (Hourly)")

* **Request limit**: 1,000 requests per hour.
* **Token usage limit**: 800,000 tokens per hour.
* These limits reset hourly.

### Monthly Quota[â](#monthly-quota "Direct link to Monthly Quota")

* **Default quota**: 500 AI invocations per month.
* Each interaction with Port AI counts as one request against your quota.
* Quota resets monthly.

Usage limits

Usage limits may change without prior notice. Once a limit is reached, you will need to wait until it resets.<br /><!-- -->If you attempt to interact with Port AI after reaching a limit, you will receive an error message indicating that the limit has been exceeded. The query limit is estimated and depends on the actual token usage.

### Monitor your usage[â](#monitor-your-usage "Direct link to Monitor your usage")

You can monitor your current usage in several ways:

#### Rate limits[â](#rate-limits "Direct link to Rate limits")

* Check the final `done` event in streaming responses for remaining requests, tokens, and reset time.

#### Monthly quota[â](#monthly-quota-1 "Direct link to Monthly quota")

You can monitor your current monthly quota usage using the [Get monthly AI invocations quota usage](/api-reference/get-monthly-ai-invocations-quota-usage.md) API endpoint

Proactive quota monitoring

Check your monthly quota before making multiple Port AI requests to avoid hitting limits. When `remainingQuota` is low, consider implementing rate limiting or queuing requests until the monthly quota resets. Note that you may also encounter hourly rate limits, which are separate from this monthly quota.

## Selecting Model[â](#selecting-model "Direct link to Selecting Model")

Port AI allows you to specify which LLM provider and model to use for specific API requests, giving you fine-grained control over AI processing on a per-request basis.

### How LLM Providers Work[â](#how-llm-providers-work "Direct link to How LLM Providers Work")

Port AI supports multiple LLM providers and models. You can either use Port's managed AI infrastructure (default) or configure your own LLM providers for additional control over data privacy, costs, and compliance.

Learn more about [LLM Provider Management](/ai-interfaces/port-ai/llm-providers-management/overview.md) and see the [supported models and providers](/ai-interfaces/port-ai/llm-providers-management/overview.md#supported-llms-and-providers).

### Specifying Provider and Model[â](#specifying-provider-and-model "Direct link to Specifying Provider and Model")

When making API requests, you can include `provider` and `model` parameters (if none specified, your organization's default will be used). See the [Invoke an agent](/api-reference/invoke-a-specific-agent.md) API reference for detailed example.

### Default Behavior[â](#default-behavior "Direct link to Default Behavior")

If no provider is specified in your API request, the system uses your organization's configured defaults, or falls back to Port's system defaults if none are configured.

## Tool Selection[â](#tool-selection "Direct link to Tool Selection")

Port AI allows you to control which specific tools from the [Port MCP server](/ai-interfaces/port-mcp-server/overview-and-installation.md) are available for each API interaction. This provides fine-grained control over what actions Port AI can perform, enabling you to create secure, purpose-specific AI interactions.

Permission-Based Tool Filtering

Selected tools will be available based on your regex patterns **but won't include tools that are not within your permission scope**. This means:

* If you request an action to **create a Jira ticket** but this action is not available to you as a user, it won't be available to Port AI.
* Members trying to use builder tools like `upsert_blueprint` will not have access to these tools through Port AI if they lack the necessary permissions.
* Tool availability is determined by the intersection of your regex selection AND your user permissions.

Port AI respects your individual user permissions and cannot access tools or perform actions that you don't have permission to use.

### How Tool Selection Works[â](#how-tool-selection-works "Direct link to How Tool Selection Works")

Include a `tools` parameter in your API request with an array of regex patterns. Port AI will only use tools whose names match at least one of these patterns.

**Basic format:**

```
{
  "prompt": "Your question or request",
  "tools": ["regex_pattern_1", "regex_pattern_2"]
}
```

### Common Tool Selection Patterns[â](#common-tool-selection-patterns "Direct link to Common Tool Selection Patterns")

**Read-only Operations (Click to expand)**

Perfect for monitoring dashboards and reporting systems where no modifications should be made.

```
["^(list|search|track|describe)_.*"]
```

**What this matches:**

* `list_entities`, `list_blueprints`, `list_scorecards`.
* `list_actions`, `list_integrations`.
* `describe_user_details`.
* `search_port_knowledge_sources`.

**Action Execution Only (Click to expand)**

Allows only action execution tools while blocking data query operations.

```
["^run_.*"]
```

**What this matches:**

* `run_create_service`, `run_deploy_to_production`.
* `run_github_create_issue`, `run_jira_create_ticket`.
* `run_slack_notify_team`.

**Specific Integration Actions (Click to expand)**

Target specific third-party service integrations.

```
["run_.*github.*", "run_.*jira.*", "run_.*zendesk.*"]
```

**What this matches:**

* `run_github_create_issue`, `run_github_merge_pr`.
* `run_jira_create_ticket`, `run_jira_update_status`.
* `run_zendesk_create_ticket`.

**Safe Entity Operations (Click to expand)**

Enables entity operations while preventing accidental deletions.

```
["(?!delete_)\\w+_entity$", "list_.*"]
```

**What this matches:**

* `list_entities`, `upsert_entity`.
* **Excludes:** `delete_entity`.

**Documentation and Help Tools (Click to expand)**

Focus on documentation search and help functionality.

```
[".*docs.*", "search_.*", "describe_.*"]
```

**What this matches:**

* `search_port_knowledge_sources`.
* `describe_user_details`.

**Blueprint and Scorecard Analysis (Click to expand)**

Focus on catalog structure and quality metrics without action execution.

```
[".*blueprint.*", ".*scorecard.*", "^list_.*"]
```

**What this matches:**

* `list_blueprints`, `upsert_blueprint`.
* `list_scorecards`, `upsert_scorecard`.
* All list operations.

### Interactive Tool Matcher[â](#interactive-tool-matcher "Direct link to Interactive Tool Matcher")

Test your regex patterns to see which MCP tools would be available to Port AI. Enter your patterns in JSON array format (e.g., `["^(list|get)_.*", "run_.*github.*"]`) and see the matching tools in real-time.

<!-- -->

Regex Patterns Array:\["(list|get|search)\_.\*"]

Enter an array of regex patterns in JSON format. Patterns automatically match from the beginning of tool names (^ is added automatically).

#### Tools (<!-- -->0<!-- --> of <!-- -->24<!-- --> matched)

`list_blueprints``upsert_blueprint``delete_blueprint``list_entities``upsert_entity``delete_entity``list_scorecards``upsert_scorecard``delete_scorecard``list_actions``upsert_action``delete_action``track_action_run``run_action``get_action_permissions``update_action_permissions``list_integrations``test_integration_mapping``get_integration_sync_metrics``get_integration_event_logs``get_integration_kinds_with_examples``search_port_knowledge_sources``describe_user_details``load_skill`

Action Tools Note

Action tools (starting with `run_*`) depend on your Port configuration. The examples shown represent common action patterns, but your actual available actions may differ based on the self-service actions configured in your Port instance.

### Best Practices[â](#best-practices "Direct link to Best Practices")

Security and Control

* **Principle of least privilege**: Only include tools necessary for the specific use case.
* **Test patterns**: Use the interactive matcher above to verify your regex patterns.
* **Automated systems**: Use highly restrictive patterns for automated workflows.
* **User-facing interfaces**: Consider broader patterns for interactive use cases.

## Integration Patterns[â](#integration-patterns "Direct link to Integration Patterns")

* API Integration
* Actions & Automations

**Direct API Calls**

Integrate Port AI directly into your applications using HTTP requests:

```
# Basic Port AI request
curl 'https://api.port.io/v1/ai/invoke' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "prompt": "What services are failing health checks?",
    "tools": ["^(list|search|describe)_.*"],
    "labels": {
      "source": "monitoring_system",
      "check_type": "health_analysis"
    }'

# AI Agent request
curl 'https://api.port.io/v1/agent/<AGENT_IDENTIFIER>/invoke' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "prompt": "Analyze the health of our production services",
    "labels": {
      "source": "monitoring_dashboard",
      "environment": "production"
    }'
```

**Application Integration Example**

```
// Example: Monitoring dashboard integration
async function checkServiceHealth(serviceName) {
  const response = await fetch('/api/port-ai/check-service', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      prompt: `Analyze the health of service ${serviceName}`,
      tools: ['^(list|search|describe)_.*'],
      labels: {
        source: 'monitoring_dashboard',
        service: serviceName,
        check_type: 'health_analysis'
      }
    })
  });
  
  // Process streaming response
  const reader = response.body.getReader();
  // Handle SSE parsing...
}
```

**Port Automations**

Automatically trigger Port AI based on catalog events using Port's automation system:

**Example: Infrastructure Healing Automation (Click to expand)**

Create in Port

```
{
  "identifier": "ai_infrastructure_healing",
  "title": "AI Infrastructure Healing",
  "description": "Automatically trigger AI analysis when infrastructure becomes unhealthy",
  "icon": "Cluster",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "ENTITY_UPDATED",
      "blueprintIdentifier": "k8s_workload"
    },
    "condition": {
      "type": "JQ",
      "expressions": [
        ".diff.before.properties.isHealthy == \"Healthy\"",
        ".diff.after.properties.isHealthy == \"Unhealthy\""
      ],
      "combinator": "and"
    }
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://api.port.io/v1/ai/invoke",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "prompt": "Infrastructure component {{ .event.diff.after.title }} is unhealthy. Analyze the issue and suggest remediation steps based on current state and recent changes.",
      "tools": ["^(list|search|describe)_.*", "run_.*incident.*", "run_.*notification.*"],
      "labels": {
        "source": "automation",
        "entity_type": "{{ .event.diff.after.blueprint }}",
        "entity_id": "{{ .event.diff.after.identifier }}",
        "trigger_type": "health_degradation"
      }
    }
  },
  "publish": true
}
```

**Self-Service Actions**

Create actions that invoke Port AI for on-demand analysis:

**Example: Service Health Analysis Action (Click to expand)**

Create in Port

```
{
  "identifier": "analyze_service_health",
  "title": "Analyze Service Health with AI",
  "description": "Get AI-powered analysis of service health and recommendations",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "blueprintIdentifier": "service"
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://api.port.io/v1/ai/invoke",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "prompt": "Analyze the health of service {{ .entity.title }}. Check metrics, recent deployments, incidents, and provide actionable recommendations.",
      "tools": ["^(list|search|describe)_.*", "run_.*incident.*"],
      "labels": {
        "source": "self_service",
        "service_name": "{{ .entity.identifier }}",
        "requested_by": "{{ .trigger.by.user.email }}"
      }
    }
  }
}
```

## Error Handling[â](#error-handling "Direct link to Error Handling")

Common error scenarios and handling strategies:

### Rate Limit Exceeded[â](#rate-limit-exceeded "Direct link to Rate Limit Exceeded")

```
{
  "error": "Rate limit exceeded",
  "type": "RATE_LIMIT_ERROR",
  "retryAfter": 3600
}
```

### Quota Exceeded[â](#quota-exceeded "Direct link to Quota Exceeded")

```
{
  "error": "Monthly quota exceeded",
  "type": "QUOTA_ERROR",
  "resetDate": "2025-10-01T00:00:00Z"
}
```

**Implementation Example: Error Handling (Click to expand)**

```
async function handlePortAIRequest(prompt) {
  try {
    const response = await invokePortAI(prompt);
    return response;
  } catch (error) {
    if (error.type === 'RATE_LIMIT_ERROR') {
      // Wait and retry
      await new Promise(resolve => setTimeout(resolve, error.retryAfter * 1000));
      return handlePortAIRequest(prompt);
    } else if (error.type === 'QUOTA_ERROR') {
      // Queue for next month or upgrade plan
      console.log('Monthly quota exceeded, queuing request');
      return null;
    }
    throw error;
  }
}
```

## Security Considerations[â](#security-considerations "Direct link to Security Considerations")

When integrating Port AI via API:

* **Authentication**: Always use secure API token storage and rotation.
* **Data privacy**: Port AI respects your organization's RBAC and data access policies.
* **Audit trail**: All API interactions are logged and trackable.
* **Rate limiting**: Implement client-side rate limiting to avoid hitting API limits.

For comprehensive security information, see [AI Security and Data Controls](/ai-interfaces/port-ai/security-and-data-controls.md).

**Detailed Security Information:**

* [Security and Permissions](/ai-interfaces/port-ai/security-and-data-controls.md#security-and-permissions) - How Port AI respects your security controls.
* [Compliance & Security Standards](/ai-interfaces/port-ai/security-and-data-controls.md#compliance--security-standards) - Integration with compliance requirements.
* [Data Access & Permissions](/ai-interfaces/port-ai/security-and-data-controls.md#data-access--permissions) - How AI respects your organization's access controls.
