# Source: https://docs.snowflake.com/en/user-guide/cortex-code/settings.md

# Cortex Code CLI Settings

Cortex Code CLI settings control tool permissions, connections, and session behavior. You can
configure settings using managed policy (if provided by your organization), configuration files,
environment variables, and command-line arguments.

## Configuration files

The following configuration files are used by Cortex Code CLI:

| File | Purpose |
| --- | --- |
| `<admin-managed path>/managed-settings.json` | Organization-managed policy file (optional). For OS-specific locations, see Managed settings (organization policy). |
| `~/.snowflake/cortex/settings.json` | Main Cortex Code CLI settings file. |
| `~/.snowflake/cortex/permissions.json` | Permission preferences. |
| `~/.snowflake/cortex/mcp.json` | MCP server configuration (see [Model Context Protocol (MCP)](extensibility.md)). |
| `~/.snowflake/config.toml` | Snowflake connections (see [Cortex Code CLI](cortex-code-cli.md)). Shared with Snowflake CLI. |

The full layout of the main configuration directory is:

```text
~/.snowflake/cortex/        # Main Cortex Code CLI config directory
├── settings.json          # Main settings
├── mcp.json               # MCP server configs
├── permissions.json       # Saved permissions
├── hooks.json             # Global hooks
├── history                # Command history
├── conversations/         # Session files
├── cache/                 # Temporary cache
│   ├── table_cache.json   # SQL result metadata
│   └── sql_result_cache/  # Parquet files
├── logs/                  # Log files
├── memory/                # Persistent memory
├── agents/                # Custom agents
├── skills/                # Global skills
├── commands/              # Custom commands
├── hooks/                 # Hook scripts
└── remote_cache/          # Cloned repos
```

### Settings precedence

Settings are applied in the following order of precedence (highest to lowest):

1. Managed settings (system-managed policy file, if present). See Managed settings (organization policy).
2. In-session commands (`/plan`, etc.)
3. Command-line arguments
4. Environment variables
5. Configuration files (`~/.snowflake/cortex/`)
6. Default values embedded in the Cortex Code CLI

### `settings.json`

`~/.snowflake/cortex/settings.json`
:   Main settings file for Cortex Code CLI.

Example content:

```json
{
   "compactMode": true,
   "autoUpdate": true,
   "theme": "dark"
}
```

The following settings are available:

* `compactMode`: Enables compact output formatting.
* `autoUpdate`: Enables automatic updates.
* `theme`: Sets the CLI theme (`light` or `dark`).

### `permissions.json`

`~/.snowflake/cortex/permissions.json`
:   Controls tool access permissions.

Example content:

```json
{
  "onlyAllow": ["read_file", "execute_sql"],
  "defaultMode": "ask",
  "dangerouslyAllowAll": false
}
```

The following settings are available:

* `onlyAllow`: List of allowed tool patterns.
* `defaultMode`: Default permission mode (`ask`, `allow`, `deny`).
* `dangerouslyAllowAll`: Allows all tools without prompts (unsafe).

### Managed settings (organization policy)

Managed settings allow IT administrators to enforce organization-wide policies for Cortex Code CLI. For example, administrators can restrict which tools or accounts can be used, enforce minimum CLI versions, and disable bypass capabilities.

These settings are typically deployed through enterprise configuration management tools (such as MDM or SCCM). Users generally cannot modify managed settings unless they have administrator/root privileges.

#### File locations

The managed settings file is stored at a system-level path:

| Platform | Path |
| --- | --- |
| macOS | `/Library/Application Support/Cortex/managed-settings.json` |
| Linux and WSL | `/etc/cortex/managed-settings.json` |

#### Configuration schema

The managed settings file uses JSON with the following structure:

```json
{
  "version": "1.0",
  "permissions": { },
  "settings": { },
  "required": { },
  "defaults": { },
  "ui": { }
}
```

#### Permissions

The `permissions` section can restrict what users can access. For example, you can allow or deny tool patterns and account patterns.

```json
{
  "permissions": {
    "onlyAllow": ["pattern1", "pattern2"],
    "deny": ["pattern3"],
    "defaultMode": "allow",
    "dangerouslyAllowAll": false
  }
}
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `onlyAllow` | `string[]` | — | Allowlist of patterns. If set, only matching items are allowed. |
| `deny` | `string[]` | — | Denylist of patterns. Deny takes precedence over allow. |
| `defaultMode` | `"allow"` or `"deny"` | `"deny"` | Behavior when no rule matches. |
| `dangerouslyAllowAll` | `boolean` | `false` | Controls whether bypass mode is allowed. |

#### Settings

The `settings` section enforces runtime behavior:

```json
{
  "settings": {
    "forceNoHistoryMode": true,
    "forceSandboxEnabled": true,
    "forceSandboxMode": "regular"
  }
}
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `forceNoHistoryMode` | `boolean` | `false` | Force no conversation history persistence. |
| `forceSandboxEnabled` | `boolean` | `false` | Force sandbox to always be enabled. |
| `forceSandboxMode` | `"regular"` or `"autoAllow"` | — | Force a specific sandbox mode. |

#### Required

The `required` section can enforce minimum versions:

```json
{
  "required": {
    "minimumVersion": "0.25.0"
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `minimumVersion` | `string` | Minimum CLI version. Older versions display an error and exit. |

#### Defaults

The `defaults` section provides default values. Users can override these defaults only if allowed by policy.

```json
{
  "defaults": {
    "connectionName": "prod",
    "profileName": "corporate",
    "theme": "dark"
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `connectionName` | `string` | Default Snowflake connection name. |
| `profileName` | `string` | Default profile to load. |
| `theme` | `string` | Default UI theme (for example, `dark` or `light`). |

#### UI

The `ui` section controls user interface presentation:

```json
{
  "ui": {
    "showManagedBanner": true,
    "bannerText": "[Secure] Managed by Corporate IT",
    "hideDangerousOptions": true
  }
}
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `showManagedBanner` | `boolean` | `false` | Display a banner indicating managed state. |
| `bannerText` | `string` | — | Custom text for the managed banner. |
| `hideDangerousOptions` | `boolean` | `false` | Hide dangerous options from help and UI. |

#### Examples

##### Basic corporate setup

Allow default functionality but disable bypass mode and show a managed banner.

```json
{
  "version": "1.0",
  "permissions": {
    "dangerouslyAllowAll": false,
    "defaultMode": "allow"
  },
  "settings": {},
  "required": {
    "minimumVersion": "0.25.0"
  },
  "ui": {
    "showManagedBanner": true,
    "bannerText": "Managed by IT"
  }
}
```

##### Restrict to specific Snowflake accounts

Only allow connections to production and staging accounts.

```json
{
  "version": "1.0",
  "permissions": {
    "dangerouslyAllowAll": false,
    "onlyAllow": [
      "account(mycompany-prod)",
      "account(mycompany-staging)"
    ],
    "defaultMode": "allow"
  }
}
```

## Environment variables

Cortex Code CLI recognizes the following configuration environment variables:

| Variable | Description |
| --- | --- |
| `SNOWFLAKE_HOME` | Overrides the default `~/.snowflake` directory. |
| `CORTEX_AGENT_MODEL` | Overrides model selection. |
| `CORTEX_ENABLE_MEMORY` | Enables the memory tool (set to `true` or `1`). |
| `COCO_DANGEROUS_MODE_REQUIRE_SQL_WRITE_PERMISSION` | Requires confirmation for SQL write operations in bypass mode. |

> **Note:**
>
> For additional permission-related environment variables, see [Security](security.md).

## Command-line overrides

Cortex Code CLI settings can be overridden via command-line arguments, which include the following:

| Example | Description |
| --- | --- |
| `cortex -c production` | Specifies the connection. |
| `cortex --workdir /path` | Sets the working directory. |
| `cortex --continue` | Continues the last session. |
| `cortex --resume <session_id>` | Resumes a specific session. |
| `cortex --plan` | Enables planning mode. |
| `cortex --dangerously-allow-all-tool-calls` | Disables permission prompts (unsafe). |

## Session storage

Conversations and settings are stored in:

| Location | Description |
| --- | --- |
| `~/.snowflake/cortex/conversations/` | Session files. |
| `~/.snowflake/cortex/permissions.json` | Permission preferences. |
| `~/.snowflake/cortex/mcp.json` | MCP configuration. |
