# Source: https://momentic.ai/docs/mobile-cli/commands/mcp.md

# Source: https://momentic.ai/docs/cli/commands/mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# mcp

Start the MCP (Model Context Protocol) server over stdio so coding assistants
can create, edit, and run Momentic tests. For full setup instructions see
[MCP](/model-context-protocol).

All options below can be passed as flags or, where noted, set via environment
variables. CLI flags override environment variables.

```bash  theme={null}
npx momentic mcp [options]
```

## Options

| Setting                         | Flag                                       | Environment variable                    | Description                                                                                                                          |
| ------------------------------- | ------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Momentic API key                | `--api-key <key>`                          | `MOMENTIC_API_KEY`                      | Authenticates the MCP server with Momentic APIs.                                                                                     |
| Config file path                | `-c`, `--config <path>`                    | —                                       | Points to the `momentic.config.yaml` file used to load project tests, modules, and environments.                                     |
| Headful browser (default: true) | `--headful-browser [true or false]`        | `MOMENTIC_HEADFUL_BROWSER`              | Sets whether browser sessions launch with a visible UI (`true`) or in headless mode (`false`).                                       |
| Device pixel ratio              | `--pixel-ratio <n>`                        | —                                       | Overrides viewport DPR used for browser rendering. Defaults to `2` on macOS Retina and `1` on other setups.                          |
| Session idle timeout            | `--session-idle-timeout-minutes <minutes>` | `MOMENTIC_SESSION_IDLE_TIMEOUT_MINUTES` | Idle timeout for MCP sessions in minutes. Sessions inactive for this duration are terminated automatically. Defaults to `5` minutes. |

### `--api-key <key>`

Momentic API key.

```bash  theme={null}
npx momentic mcp --api-key your-api-key
```

### `-c, --config <path>`

Path to the `momentic.config.yaml` file. Required when run from an MCP client;
use an absolute path so the server can resolve it correctly.

```bash  theme={null}
npx momentic mcp --config /absolute/path/to/momentic.config.yaml
```

### `--headful-browser [true|false]`

Whether to launch MCP session browsers with a visible UI (`true`) or in headless
mode (`false`). Defaults to `true`.

```bash  theme={null}
npx momentic mcp --headful-browser false
```

### `--pixel-ratio <n>`

Device pixel ratio for browser rendering. Defaults to `2` on macOS Retina and
`1` elsewhere.

```bash  theme={null}
npx momentic mcp --pixel-ratio 2
```

### `--session-idle-timeout-minutes <minutes>`

Session idle timeout in minutes. MCP sessions that remain idle for this duration
are automatically terminated. Defaults to `5` minutes. Can also be set via the
`MOMENTIC_SESSION_IDLE_TIMEOUT_MINUTES` environment variable.

```bash  theme={null}
npx momentic mcp --session-idle-timeout-minutes 5
```


Built with [Mintlify](https://mintlify.com).