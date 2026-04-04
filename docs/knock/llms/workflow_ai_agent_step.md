# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_ai_agent_step.md

### WorkflowAIAgentStep

An AI agent function step. Fetches data from an AI model and merges it into the workflow's `data` scope for use in later steps. Supports Liquid templating in the prompt. Read more in the [docs](https://docs.knock.app/designing-workflows/ai-agent-function).

#### Attributes

- **conditions** (object) - A conditions object that describes one or more conditions to be met in order for the step to be executed.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the AI agent step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "name": "AI agent step",
  "ref": "ai_agent_step",
  "settings": {
    "model": "anthropic:claude-haiku-4-5",
    "request_prompt": "You are a helpful assistant.",
    "response_type": "text"
  },
  "type": "ai_agent"
}
```

