<!-- Source: https://namespace.so/docs/reference/cli/token-create -->

# nsc token create

Create a revokable token with specific permissions and expiration.

`nsc token create` provides commands to manage revokable tokens that can be used for authentication in situations where federation is not available or practical. These tokens provide a flexible way to grant time-limited, scoped access to resources without using full workload federation.

Revokable tokens are useful for:

- CI/CD pipelines that don't support OIDC federation
- Local development and testing
- Automated scripts and tools
- Temporary access grants with expiration
- Situations requiring explicit permission scoping

`nsc token create` generates a new revokable token that can be used for authentication. Tokens can be scoped to specific resources and actions, and can be configured with custom expiration times (up to 90 days).

## Usage

```
nsc token create [flags]
```

### Examples

**Create a token with a name and description:**

```
$ nsc token create \
  --name "ci-pipeline-token" \
  --description "Token for GitHub Actions CI pipeline"
```

**Create a token with custom expiration:**

```
$ nsc token create \
  --name "short-lived-token" \
  --expires_in 1h
```

**Create a token with specific permissions:**

```
$ nsc token create \
  --name "builder-token" \
  --grant '{"resource_type":"builder","resource_id":"*","actions":["ensure","access"]}' \
  --grant '{"resource_type":"artifact","resource_id":"*","actions":["create","resolve","list"]}'
```

**Save token to file for automated usage:**

```
$ nsc token create \
  --name "automation-token" \
  --token_file token.json \
  --output token
```

**Display only the token value:**

```
$ nsc token create --name "quick-token" --output token
```

## Flags

### --name string

A unique name for the token within the tenant. This helps identify the token's purpose when listing or managing tokens.

### --grant stringArray (can be repeated)

Grant specific permissions to the token as a JSON object. This flag can be specified multiple times to grant multiple permissions.

**Format:**

```
{"resource_type":"...","resource_id":"...","actions":["..."]}
```

**Resource types and actions:**

| Resource Type | Actions | Description |
| --- | --- | --- |
| `instance` | `create`, `list`, `get`, `wait`, `destroy` | Ephemeral instances |
| `instance/o11y/*` | `get`, `list` | Instance observability (metrics, logs) |
| `containerregistry` | `pull`, `push` | Container registry access |
| `ingress` | `access` | Ingress endpoint access |
| `builder` | `ensure`, `access` | Remote builders |
| `artifact` | `create`, `resolve`, `expire`, `list` | Artifact storage |

**Example permissions:**

```
--grant '{"resource_type":"builder","resource_id":"*","actions":["ensure","access"]}'
--grant '{"resource_type":"artifact","resource_id":"*","actions":["create","resolve","list"]}'
```

### --description string (optional)

A human-readable description of the token's purpose. Use this to document why the token was created and what it's used for.

### --expires\_in duration (optional)

Duration until the token expires. The default is 24 hours. Maximum allowed duration is 90 days.

**Examples:**

- `1h` - 1 hour
- `24h` - 24 hours (default)
- `7d` - 7 days (note: use hours, e.g., `168h`)
- `2160h` - 90 days (maximum)

### --output string (optional)

Output format for the created token. Options: `table` (default), `json`, `token`.

- **table**: Display token information in a formatted table
- **json**: Output full token details as JSON
- **token**: Output only the token value (useful for scripts)

### --user (optional)

Scope the token to the current user's workspace membership. By default, creating tokens requires the user to be a workspace admin.
When `--user` is specified, the token is bound to the calling user's membership, allowing non-admin users to create tokens scoped to their own permissions.

### --token\_file string (optional)

Write the token to the specified file in JSON format. This is useful for automated workflows that need to store and reuse the token.

## Related Topics

- [nsc token list](/docs/reference/cli/token-list) - List existing tokens
- [nsc token revoke](/docs/reference/cli/token-revoke) - Revoke tokens
- [Workspace Access Controls](/docs/workspaces/access) - Permission management
- [Workload Federation](/docs/federation) - Federation with cloud providers
- [Security](/docs/workspaces/security) - Security best practices and audit logging

Last updated April 15, 2026
