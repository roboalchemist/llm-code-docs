# Source: https://docs.infrahub.app/vscode/reference/commands-settings.md

# Extension Commands and Settings Reference

This reference document provides comprehensive information about all available commands, settings, keyboard shortcuts, and configuration options in the Infrahub VSCode extension.

## Commands[​](#commands "Direct link to Commands")

### Available Commands[​](#available-commands "Direct link to Available Commands")

The extension registers the following commands that can be executed via the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

| Command ID                     | Title                 | Description                                                            | Context                      |
| ------------------------------ | --------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| `infrahub.editInfrahubYaml`    | Edit file             | Opens the selected YAML file at a specific location                    | Tree view item               |
| `infrahub.editGqlQuery`        | Edit GraphQL Query    | Opens the GraphQL query file for editing                               | Query tree item              |
| `infrahub.executeGraphQLQuery` | Execute GraphQL Query | Runs a GraphQL query against selected server/branch                    | Query tree item              |
| `infrahub.runTransform`        | Run Transform         | Executes a Jinja2 or Python transform with automatic command selection | Transform/Artifact tree item |
| `infrahub.newBranch`           | New Branch            | Creates a new branch on the selected server                            | Server tree item             |
| `infrahub.deleteBranch`        | Delete Branch         | Deletes the selected branch                                            | Branch tree item             |
| `infrahub.visualizeSchema`     | Visualize Schema      | Opens an interactive graph visualization of the server's schema        | Server tree item (online)    |

### Command Execution[​](#command-execution "Direct link to Command Execution")

#### From Command Palette[​](#from-command-palette "Direct link to From Command Palette")

1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type "Infrahub" to filter commands
3. Select the desired command

#### From Context Menus[​](#from-context-menus "Direct link to From Context Menus")

Right-click on tree view items to access contextual commands:

* **Server Items**: New Branch, Visualize Schema
* **Branch Items**: Delete Branch
* **Query Items**: Execute Query, Edit Query
* **Transform/Artifact Items**: Run Transform (automatically detects Jinja2 vs Python)
* **YAML Items**: Edit File

#### Programmatic Execution[​](#programmatic-execution "Direct link to Programmatic Execution")

Commands can be executed programmatically:

```
// Execute a command from another extension
vscode.commands.executeCommand('infrahub.executeGraphQLQuery', queryItem);
```

## Extension Settings[​](#extension-settings "Direct link to Extension Settings")

### Configuration Properties[​](#configuration-properties "Direct link to Configuration Properties")

All settings are prefixed with `infrahub-vscode.`:

| Setting           | Type   | Default     | Description                               |
| ----------------- | ------ | ----------- | ----------------------------------------- |
| `servers`         | array  | `[]`        | List of Infrahub server configurations    |
| `schemaDirectory` | string | `"schemas"` | Path to directory containing schema files |

### Server Configuration Schema[​](#server-configuration-schema "Direct link to Server Configuration Schema")

Each server in the `servers` array follows this structure:

```
interface ServerConfig {
  name: string;           // Display name for the server
  address: string;        // Server URL (http/https)
  api_token?: string;     // Optional API token for authentication
  <!-- vale off -->tls_insecure<!-- vale on -->?: boolean; // Optional: Disable TLS certificate verification (default: false)
}
```

#### TLS configuration details[​](#tls-configuration-details "Direct link to TLS configuration details")

The `<!-- vale off -->tls_insecure<!-- vale on -->` property controls TLS certificate verification behavior:

* **Default value**: `false` (secure, certificates are verified)
* **When `true`**: Disables certificate verification for development environments
* **Scope**: Affects all HTTPS connections when any server has this enabled
* **Security impact**: Makes connections vulnerable to man-in-the-middle attacks

**Use cases for `<!-- vale off -->tls_insecure<!-- vale on -->: true`**:

* Development servers with self-signed certificates
* Internal testing environments with custom CA certificates
* Docker containers with self-signed certificates

**Never use in production** as it compromises security.

### Example Configuration[​](#example-configuration "Direct link to Example Configuration")

```
{
  "infrahub-vscode.servers": [
    {
      "name": "Local Development",
      "address": "http://localhost:8000"
    },
    {
      "name": "Production",
      "address": "https://infrahub.example.com",
      "api_token": "inf_1234567890abcdef"
    },
    {
      "name": "Development (Self-Signed)",
      "address": "https://dev.infrahub.local",
      "api_token": "inf_dev_token",
      "<!-- vale off -->tls_insecure<!-- vale on -->": true
    }
  ],
  "infrahub-vscode.schemaDirectory": "infrastructure/schemas"
}
```

warning

Setting `<!-- vale off -->tls_insecure<!-- vale on -->: true` disables certificate verification and is **not recommended for production environments**. Only use this option in development/testing environments with self-signed certificates.

### Environment Variable Substitution[​](#environment-variable-substitution "Direct link to Environment Variable Substitution")

Settings support environment variable substitution using `${env:VARIABLE_NAME}`:

```
{
  "infrahub-vscode.servers": [
    {
      "name": "Production",
      "address": "${env:INFRAHUB_SERVER_URL}",
      "api_token": "${env:INFRAHUB_API_TOKEN}"
    }
  ]
}
```

## Tree View Components[​](#tree-view-components "Direct link to Tree View Components")

### Infrahub Servers Tree View[​](#infrahub-servers-tree-view "Direct link to Infrahub Servers Tree View")

**View ID**: `InfrahubServerTreeView` **Location**: Activity Bar → Infrahub Container

#### Tree Structure[​](#tree-structure "Direct link to Tree Structure")

```
📁 Infrahub Servers
  └─ 🖥️ [Server Name]
      ├─ 🌿 main (default)
      ├─ 🌿 feature-branch-1
      └─ 🌿 feature-branch-2
```

#### Item Types[​](#item-types "Direct link to Item Types")

| Item Type        | View Item ID             | Available Actions            |
| ---------------- | ------------------------ | ---------------------------- |
| Server (online)  | `infrahubServer:online`  | New Branch, Visualize Schema |
| Server (offline) | `infrahubServer:offline` | New Branch                   |
| Branch (default) | `infrahubBranch-default` | Delete Branch                |
| Branch (regular) | `infrahubBranch`         | Delete Branch                |

### Infrahub YAML Tree View[​](#infrahub-yaml-tree-view "Direct link to Infrahub YAML Tree View")

**View ID**: `infrahubYamlTreeView` **Location**: Activity Bar → Infrahub Container

#### Tree Structure[​](#tree-structure-1 "Direct link to Tree Structure")

```
📁 Infrahub YAML
  └─ 📄 .infrahub.yml
      ├─ 📁 schemas
      │   ├─ 📄 network.yml
      │   └─ 📄 location.yml
      ├─ 📁 queries
      │   ├─ 📊 get_devices
      │   └─ 📊 topology_report
      └─ 📁 checks
          └─ 🔍 validate_hostnames
```

#### Item Types[​](#item-types-1 "Direct link to Item Types")

| Item Type | View Item ID Pattern | Available Actions         |
| --------- | -------------------- | ------------------------- |
| YAML File | `file`               | Edit File                 |
| Query     | `queries/*`          | Execute Query, Edit Query |
| Schema    | `schemas/*`          | Edit File                 |
| Check     | `checks/*`           | Edit File                 |

## Status Bar[​](#status-bar "Direct link to Status Bar")

### Status Bar Item[​](#status-bar-item "Direct link to Status Bar Item")

**Alignment**: Left **Priority**: 100

#### Status States[​](#status-states "Direct link to Status States")

| State       | Display Text                      | Background Color     |
| ----------- | --------------------------------- | -------------------- |
| Connected   | `Infrahub: v[version] ([server])` | Default              |
| No Server   | `Infrahub: No server set`         | No folder background |
| Unreachable | `Infrahub: Server unreachable`    | Error background     |

#### Update Interval[​](#update-interval "Direct link to Update Interval")

* Status updates every 10 seconds
* Displays first configured server's status

## Activation Events[​](#activation-events "Direct link to Activation Events")

The extension activates when:

```
"activationEvents": [
  "workspaceContains:.infrahub.yml",
  "workspaceContains:.infrahub.yaml"
]
```

## File Associations[​](#file-associations "Direct link to File Associations")

### YAML Validation[​](#yaml-validation "Direct link to YAML Validation")

Files matching these patterns receive schema validation:

```
"yamlValidation": [
  {
    "fileMatch": [
      "models/**/*.yml",
      "models/**/*.yaml",
      "schemas/**/*.yml",
      "schemas/**/*.yaml"
    ],
    "url": "https://schema.infrahub.app/infrahub/schema/latest.json"
  }
]
```

## Language Features[​](#language-features "Direct link to Language Features")

### Definition Provider[​](#definition-provider "Direct link to Definition Provider")

**Language**: YAML **Feature**: Go-to-definition (`F12` or `Ctrl+Click`)

Navigates to:

* Schema definitions
* Referenced nodes
* Relationship targets

### Document Symbol Provider[​](#document-symbol-provider "Direct link to Document Symbol Provider")

**Language**: YAML **Feature**: Document outline

Provides symbols for:

* Nodes
* Attributes
* Relationships
* Queries
* Checks

## Context Menu Integration[​](#context-menu-integration "Direct link to Context Menu Integration")

### View Item Context Menus[​](#view-item-context-menus "Direct link to View Item Context Menus")

Commands appear in context menus based on `when` clauses:

```
"menus": {
  "view/item/context": [
    {
      "command": "infrahub.newBranch",
      "when": "view == InfrahubServerTreeView && viewItem == infrahubServer"
    },
    {
      "command": "infrahub.deleteBranch",
      "when": "view == InfrahubServerTreeView && viewItem =~ /^infrahubBranch/"
    }
  ]
}
```

## Extension Dependencies[​](#extension-dependencies "Direct link to Extension Dependencies")

### Required Extensions[​](#required-extensions "Direct link to Required Extensions")

```
"extensionDependencies": [
  "redhat.vscode-yaml"  // YAML language support
]
```

The Red Hat YAML extension must be installed for schema validation to work.

## API Token Management[​](#api-token-management "Direct link to API Token Management")

### Token Format[​](#token-format "Direct link to Token Format")

Infrahub API tokens typically follow this format:

```
inf_[32-character-alphanumeric-string]
```

### Token Security Best Practices[​](#token-security-best-practices "Direct link to Token Security Best Practices")

1. **Never commit tokens**: Use environment variables
2. **Rotate regularly**: Change tokens periodically
3. **Minimal permissions**: Use read-only tokens when possible
4. **Separate environments**: Different tokens per environment

### Token Configuration Methods[​](#token-configuration-methods "Direct link to Token Configuration Methods")

#### Method 1: Direct in settings (not recommended)[​](#method-1-direct-in-settings-not-recommended "Direct link to Method 1: Direct in settings (not recommended)")

```
{
  "infrahub-vscode.servers": [
    {
      "api_token": "inf_direct_token_not_secure"
    }
  ]
}
```

#### Method 2: Environment variables (recommended)[​](#method-2-environment-variables-recommended "Direct link to Method 2: Environment variables (recommended)")

```
{
  "infrahub-vscode.servers": [
    {
      "api_token": "${env:INFRAHUB_TOKEN}"
    }
  ]
}
```

#### Method 3: VSCode secrets (future)[​](#method-3-vscode-secrets-future "Direct link to Method 3: VSCode secrets (future)")

Planned support for VSCode's secret storage API.

## Troubleshooting Reference[​](#troubleshooting-reference "Direct link to Troubleshooting Reference")

### Common Issues and Solutions[​](#common-issues-and-solutions "Direct link to Common Issues and Solutions")

| Issue                         | Possible Cause                      | Solution                                                                            |
| ----------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------- |
| Extension not activating      | No `.infrahub.yml` file             | Create `.infrahub.yml` in workspace root                                            |
| Server unreachable            | Invalid URL or network issue        | Check server URL and network connection                                             |
| Commands not appearing        | Wrong context                       | Ensure correct tree view item is selected                                           |
| Validation not working        | Missing YAML extension              | Install Red Hat YAML extension                                                      |
| Token not working             | Incorrect format or permissions     | Verify token format and permissions                                                 |
| TLS certificate errors        | Self-signed or invalid certificates | Add `"<!-- vale off -->tls_insecure<!-- vale on -->": true` for development servers |
| CERT\_HAS\_EXPIRED            | Expired SSL certificate             | Renew certificate or use `<!-- vale off -->tls_insecure<!-- vale on -->` for dev    |
| SELF\_SIGNED\_CERT\_IN\_CHAIN | Self-signed certificate             | Use `"<!-- vale off -->tls_insecure<!-- vale on -->": true` for development         |

### TLS error messages[​](#tls-error-messages "Direct link to TLS error messages")

The extension provides specific error messages for common TLS issues:

* **"TLS Certificate expired - check tls\_insecure setting"**: The server's certificate has expired
* **"Self-signed certificate - check tls\_insecure setting"**: The server uses a self-signed certificate
* **"TLS Verification failed - check tls\_insecure setting"**: General certificate verification failure These messages appear in the server tree view when connection attempts fail due to certificate issues.

### Debug Output[​](#debug-output "Direct link to Debug Output")

Enable debug logging:

1. Open VSCode Developer Tools: `Help → Toggle Developer Tools`
2. Check Console tab for extension logs
3. Look for messages starting with "Infrahub Extension"

## Keyboard Shortcuts[​](#keyboard-shortcuts "Direct link to Keyboard Shortcuts")

The extension doesn't define default keyboard shortcuts, but you can add custom ones:

### Adding Custom Shortcuts[​](#adding-custom-shortcuts "Direct link to Adding Custom Shortcuts")

1. Open Keyboard Shortcuts: `Ctrl+K Ctrl+S` (Windows/Linux) or `Cmd+K Cmd+S` (macOS)
2. Search for "Infrahub"
3. Click the `+` icon to add a keybinding

### Suggested Shortcuts[​](#suggested-shortcuts "Direct link to Suggested Shortcuts")

```
{
  "key": "ctrl+alt+q",
  "command": "infrahub.executeGraphQLQuery",
  "when": "view == infrahubYamlTreeView"
},
{
  "key": "ctrl+alt+b",
  "command": "infrahub.newBranch",
  "when": "view == InfrahubServerTreeView"
}
```

## Performance Settings[​](#performance-settings "Direct link to Performance Settings")

### Refresh Intervals[​](#refresh-intervals "Direct link to Refresh Intervals")

| Component        | Interval   | Configurable   |
| ---------------- | ---------- | -------------- |
| Server Tree View | 10 seconds | No (hardcoded) |
| Status Bar       | 10 seconds | No (hardcoded) |

### Resource Limits[​](#resource-limits "Direct link to Resource Limits")

* Maximum servers: No limit (performance may degrade with >10)
* Query result size: Limited by VSCode webview memory
* Tree view items: No hard limit

## Version Compatibility[​](#version-compatibility "Direct link to Version Compatibility")

### VSCode Version[​](#vscode-version "Direct link to VSCode Version")

* **Minimum**: 1.99.0
* **Recommended**: Latest stable version

### Infrahub Server Version[​](#infrahub-server-version "Direct link to Infrahub Server Version")

* **Minimum**: 0.14.0 (basic functionality)
* **Recommended**: 0.15.0+ (all features)

### Node.js Runtime[​](#nodejs-runtime "Direct link to Node.js Runtime")

* **Target**: ES2022
* **Module System**: Node16

## Extension Metadata[​](#extension-metadata "Direct link to Extension Metadata")

### Publisher Information[​](#publisher-information "Direct link to Publisher Information")

* **Publisher ID**: OpsMill
* **Publisher Name**: OpsMill
* **Homepage**: <https://github.com/opsmill/infrahub-vscode>

### Gallery Banner[​](#gallery-banner "Direct link to Gallery Banner")

```
"galleryBanner": {
  "color": "#2183F7",
  "theme": "dark"
}
```

## Further Information[​](#further-information "Direct link to Further Information")

* [Getting Started Tutorial](/vscode/tutorials/getting-started.md)
* [How to Visualize Your Schema](/vscode/guides/visualize-schema.md)
* [Understanding the Extension Architecture](/vscode/topics/extension-architecture.md)
* [Security Configuration and Best Practices](/vscode/topics/security-configuration.md)
* [GitHub Repository](https://github.com/opsmill/infrahub-vscode)
