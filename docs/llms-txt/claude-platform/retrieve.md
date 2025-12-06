# Source: https://platform.claude.com/docs/en/api/typescript/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/ruby/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/python/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/kotlin/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/java/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/go/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/python/beta/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/java/beta/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/go/beta/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/messages/batches/retrieve.md

# Source: https://platform.claude.com/docs/en/api/admin/workspaces/members/retrieve.md

# Source: https://platform.claude.com/docs/en/api/admin/workspaces/retrieve.md

# Source: https://platform.claude.com/docs/en/api/admin/users/retrieve.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/skills/versions/retrieve.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/skills/versions/retrieve.md

# Source: https://platform.claude.com/docs/en/api/python/beta/skills/versions/retrieve.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/skills/versions/retrieve.md

# Source: https://platform.claude.com/docs/en/api/java/beta/skills/versions/retrieve.md

# Source: https://platform.claude.com/docs/en/api/go/beta/skills/versions/retrieve.md

# Source: https://platform.claude.com/docs/en/api/beta/skills/versions/retrieve.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/skills/retrieve.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/skills/retrieve.md

# Source: https://platform.claude.com/docs/en/api/python/beta/skills/retrieve.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/skills/retrieve.md

# Source: https://platform.claude.com/docs/en/api/java/beta/skills/retrieve.md

# Source: https://platform.claude.com/docs/en/api/go/beta/skills/retrieve.md

# Source: https://platform.claude.com/docs/en/api/beta/skills/retrieve.md

# Source: https://platform.claude.com/docs/en/api/admin/invites/retrieve.md

# Source: https://platform.claude.com/docs/en/api/admin/cost_report/retrieve.md

# Source: https://platform.claude.com/docs/en/api/admin/api_keys/retrieve.md

# Source: https://platform.claude.com/docs/en/api/typescript/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/ruby/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/python/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/kotlin/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/java/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/go/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/python/beta/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/java/beta/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/go/beta/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/beta/models/retrieve.md

# Source: https://platform.claude.com/docs/en/api/models/retrieve.md

## Retrieve

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Path Parameters

- `model_id: string`

  Model identifier or alias.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 16 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

### Returns

- `ModelInfo = object { id, created_at, display_name, type }`

  - `id: string`

    Unique model identifier.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: string`

    A human-readable name for the model.

  - `type: "model"`

    Object type.

    For Models, this is always `"model"`.

    - `"model"`

### Example

```http
curl https://api.anthropic.com/v1/models/$MODEL_ID \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
