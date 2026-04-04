# Source: https://www.courier.com/docs/tools/cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier CLI

> Send messages, manage users, inspect delivery logs, and operate all 81 Courier API endpoints from the command line.

The Courier CLI is a native binary that covers the full Courier REST API. It works on macOS, Linux, and Windows with no runtime dependencies.

## Prerequisite: Create an API Key

You need a Courier API key to authenticate CLI commands. [Create one in your Courier Settings](https://app.courier.com/settings/api-keys), then set it in your shell:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

<Tip>
  If you pass `--api-key` on a command, it takes priority over the environment variable. This is useful for testing against a different workspace without changing your shell config. See [Global Flags](#global-flags) for all available flags.
</Tip>

## Installation

<Tabs>
  <Tab title="npm">
    ```bash  theme={null}
    npm install -g @trycourier/cli
    ```

    This downloads a platform-specific binary via a postinstall step. No Node.js runtime is needed after installation.
  </Tab>

  <Tab title="Homebrew">
    ```bash  theme={null}
    brew install trycourier/courier/courier
    ```

    <Note>
      On macOS, Gatekeeper may quarantine the binary on first run. If you see "Apple could not verify", run:

      ```bash  theme={null}
      xattr -d com.apple.quarantine "$(brew --prefix)/Caskroom/courier/$(brew list --versions courier | awk '{print $2}')/courier"
      ```
    </Note>
  </Tab>

  <Tab title="Direct download">
    Download the latest binary for your platform from [GitHub Releases](https://github.com/trycourier/courier-cli/releases). Extract it and add it to your `PATH`.
  </Tab>
</Tabs>

Verify the installation:

```bash  theme={null}
courier --version
```

## Command Structure

The CLI uses a resource-based pattern:

```bash  theme={null}
courier [resource] <command> [flags...]
```

Use `--help` on any command to see available flags:

```bash  theme={null}
courier send --help
courier messages list --help
```

## Common Commands

### Send a message

```bash  theme={null}
courier send message \
  --message.to.user_id "user-123" \
  --message.template "order-confirmation" \
  --message.data '{"orderId": "ORD-456"}'
```

### List recent messages

```bash  theme={null}
courier messages list
```

### Inspect a message

```bash  theme={null}
courier messages retrieve --message-id "1-abc123"
```

### View delivery history

```bash  theme={null}
courier messages history --message-id "1-abc123"
```

### Get a user profile

```bash  theme={null}
courier profiles retrieve --user-id "user-123"
```

### List notification templates

```bash  theme={null}
courier notifications list
```

## Output Formats

Every command supports structured output via the `--format` flag:

| Format   | Description                                           |
| -------- | ----------------------------------------------------- |
| `auto`   | Default; human-readable for terminals, JSON for pipes |
| `json`   | JSON output                                           |
| `yaml`   | YAML output                                           |
| `pretty` | Colorized, indented JSON                              |
| `raw`    | Raw response body                                     |
| `jsonl`  | Newline-delimited JSON (for streaming)                |

Filter output with [GJSON syntax](https://github.com/tidwall/gjson/blob/master/SYNTAX.md) using `--transform`:

```bash  theme={null}
courier messages list --format json --transform "results.#.id"
```

## Global Flags

| Flag              | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| `--api-key`       | Override `COURIER_API_KEY` for this command                      |
| `--base-url`      | Use a custom API URL                                             |
| `--format`        | Output format (`auto`, `json`, `yaml`, `pretty`, `raw`, `jsonl`) |
| `--transform`     | Filter output with GJSON syntax                                  |
| `--debug`         | Show HTTP request/response details                               |
| `--version`, `-v` | Print CLI version                                                |
| `--help`          | Show command usage                                               |

## CI/CD Integration

Use the CLI in automated pipelines to validate sends or run smoke tests during deployment.

```bash  theme={null}
export COURIER_API_KEY="$COURIER_TEST_KEY"

courier send message \
  --message.to.user_id "smoke-test-user" \
  --message.template "welcome"
```

<Tip>
  Store API keys as secrets in your CI provider (GitHub Actions secrets, GitLab CI variables, etc.) rather than hardcoding them.
</Tip>

## AI Agent Usage

The CLI works as a zero-config tool for AI agents in Cursor, Claude Code, Codex, and similar environments. Install once, set `COURIER_API_KEY`, and agents can run Courier operations directly via shell commands. Every command supports `--format json` for machine-readable output.

## What's Next

<CardGroup cols={2}>
  <Card title="MCP Server" icon="microchip-ai" href="/tools/mcp">
    Structured AI tool access for sending messages, managing users, and more.
  </Card>

  <Card title="API Reference" icon="code" href="/reference/get-started">
    Full REST API documentation for all 81 endpoints.
  </Card>
</CardGroup>

***

Source code: [trycourier/courier-cli](https://github.com/trycourier/courier-cli)
