# Source: https://momentic.ai/docs/model-context-protocol.md

# Source: https://momentic.ai/docs/mobile-cli/model-context-protocol.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP

<Warning>Requires Momentic mobile CLI version 0.55.1 or greater.</Warning>

<Info>Currently only one emulator can run at a time.</Info>

Momentic's MCP server exposes tools so agents can:

* Browse tests, modules, and environments
* Edit tests and modules via tool calls (not direct YAML edits)
* Create tests from natural language
* Run sessions with a live emulator

## Prerequisites

* **Momentic-mobile CLI installed**: MCP is local only and requires the
  [Momentic-mobile CLI](/mobile-cli/setup) on your machine.
* **Project setup complete**: Finish CLI setup and ensure your project includes
  a valid `momentic.config.yaml`.

## Step 1: Set up your MCP client

<Tip>
  The MCP shell command must have access to `MOMENTIC_API_KEY`, `JAVA_HOME`, and
  `ANDROID_HOME` directly in the MCP command. You can provide it through the MCP
  server `env` block or pass the `--api-key`, `--java-home`, and `--android-home`
  flags directly to `momentic-mobile mcp`. Most MCP servers do *not* inherit your
  usual shell environment variables.
</Tip>

All configurations below use an absolute path to `momentic.config.yaml`. Replace
it with your project's actual path. For additional options, see the
[mcp command](/mobile-cli/commands/mcp).

<Tabs>
  <Tab title="Cursor">
    **Setup Steps**:

    1. Open Cursor's command palette (usually Cmd+Shift+P on Mac OS).
    2. Search for and select the "View: Open MCP Settings" command.
    3. Click "Add a new Custom MCP server".
    4. Add a block in the JSON file for "momentic-mobile" based on the code sample below. Replace the path with your true `momentic.config.yaml` location.
    5. Restart Cursor.

    ```json  theme={null}
    {
      "mcpServers": {
        "momentic-mobile": {
          "type": "stdio",
          "command": "npx",
          "args": [
            "momentic-mobile",
            "mcp",
            "--config",
            "/absolute/path/to/momentic.config.yaml",
            "--android-home",
            "/absolute/path/to/Android/sdk",
            "--java-home",
            "/absolute/path/to/java-home"
          ]
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json  theme={null}
      {
        "mcpServers": {
          "momentic-mobile": {
            "type": "stdio",
            "command": "npx",
            "args": [
              "momentic-mobile",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--android-home",
              "/absolute/path/to/Android/sdk",
              "--java-home",
              "/absolute/path/to/java-home",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "env": {
              "MOMENTIC_API_KEY": "your-api-key",
              "ANDROID_HOME": "/absolute/path/to/Android/sdk",
              "JAVA_HOME": "/absolute/path/to/java-home"
            }
          }
        }
      }
      ```
    </Accordion>
  </Tab>

  <Tab title="VS Code (GitHub Copilot)">
    **Setup Steps**:

    1. Open the Command Palette (Shift+Command+P on macOS, Shift+Ctrl+P on
       Windows/Linux).
    2. Type and select **MCP: Add Server**.
    3. Choose the **Command (stdio)** option.
    4. Add the **`momentic-mobile`** MCP server using the configuration below
       (replace the config path with your project's `momentic.config.yaml`):

    ```json  theme={null}
    {
      "mcpServers": {
        "momentic-mobile": {
          "type": "stdio",
          "command": "npx",
          "args": [
            "momentic-mobile",
            "mcp",
            "--config",
            "/absolute/path/to/momentic.config.yaml",
            "--android-home",
            "/absolute/path/to/Android/sdk",
            "--java-home",
            "/absolute/path/to/java-home"
          ]
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json  theme={null}
      {
        "mcpServers": {
          "momentic-mobile": {
            "type": "stdio",
            "command": "npx",
            "args": [
              "momentic-mobile",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--android-home",
              "/absolute/path/to/Android/sdk",
              "--java-home",
              "/absolute/path/to/java-home",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "env": {
              "MOMENTIC_API_KEY": "your-api-key"
            }
          }
        }
      }
      ```
    </Accordion>

    5. Name the server when prompted (e.g., "momentic-mobile").
    6. Open Extensions and confirm the MCP server connects and detects the tools.
    7. Allow all tools from Momentic.

    GitHub Copilot may require your organization to allow MCP server usage. VS Code may only allow MCP usage in agent mode.
  </Tab>

  <Tab title="Claude Code">
    **Setup Steps**:

    1. Open your terminal and navigate to your project directory.
    2. Run the command below. Replace the config path with your
       project's `momentic.config.yaml`. To add optional settings (API key,
       session idle timeout), see the [mcp command](/mobile-cli/commands/mcp).

    ```bash  theme={null}
    claude mcp add --transport stdio momentic-mobile -- npx momentic-mobile mcp --config /absolute/path/to/momentic.config.yaml
    ```

    3. Verify the server is configured: `claude mcp list`.
    4. Restart Claude Code if it was already running.

    **Note:** All options (e.g. `--transport stdio`, `--env`) must come before the
    server name. The `--` separates the server name from the command and its
    arguments.

    **Windows:** On native Windows (not WSL), wrap `npx` with `cmd /c`:
    `claude mcp add --transport stdio momentic-mobile -- cmd /c npx momentic-mobile mcp --config C:\path\to\momentic.config.yaml`

    Need help configuring advanced Claude flags (for example `--env`,
    `--scope`, or auth options)? See [Claude Code MCP server
    setup](https://code.claude.com/docs/en/mcp#option-3-add-a-local-stdio-server).
  </Tab>

  <Tab title="Codex">
    **Setup Steps**:

    1. Open your terminal in your project directory (or ensure the config path is
       absolute).
    2. Run the command below. Replace the config path with your
       project's `momentic.config.yaml`. To add optional settings (API key,
       session idle timeout), see the [mcp command](/mobile-cli/commands/mcp).
    3. Codex saves this configuration to `~/.codex/config.toml`. You can always edit your MCP configuration through this file.
    4. Restart Codex. Open a new chat and type `/mcp` to confirm that the Momentic mobile MCP server is active.

    ```bash  theme={null}
    codex mcp add momentic-mobile -- npx momentic-mobile mcp --config /absolute/path/to/momentic.config.yaml --api-key your-api-key --android-home /absolute/path/to/Android/sdk --java-home /absolute/path/to/java-home
    ```

    3. For advanced configuration, edit `~/.codex/config.toml` (or
       project-scoped `.codex/config.toml` in trusted projects).
    4. Verify MCP servers from Codex by running `/mcp` in the Codex TUI.
    5. If tools don’t appear, restart Codex.

    Refer to the [Codex docs](https://developers.openai.com/codex/mcp/) for help configuring advanced Codex MCP options such as environment variables and timeouts.
  </Tab>

  <Tab title="OpenCode">
    **Setup Steps**:

    1. Edit `opencode.json` or `opencode.jsonc` in your project root or global
       config (`~/.config/opencode/`). See [OpenCode MCP
       docs](https://opencode.ai/docs/mcp-servers/).
    2. Add the Momentic mobile MCP server under the `mcp` key. Replace the config path with your project's `momentic.config.yaml`.
    3. Start OpenCode.

    ```json  theme={null}
    {
      "mcp": {
        "momentic-mobile": {
          "type": "local",
          "command": [
            "npx",
            "momentic-mobile",
            "mcp",
            "--config",
            "/absolute/path/to/momentic.config.yaml",
            "--android-home",
            "/absolute/path/to/Android/sdk",
            "--java-home",
            "/absolute/path/to/java-home"
          ],
          "enabled": true
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json  theme={null}
      {
        "mcp": {
          "momentic-mobile": {
            "type": "local",
            "command": [
              "npx",
              "momentic-mobile",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--android-home",
              "/absolute/path/to/Android/sdk",
              "--java-home",
              "/absolute/path/to/java-home",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "enabled": true,
            "environment": {
              "MOMENTIC_API_KEY": "your-api-key"
            }
          }
        }
      }
      ```
    </Accordion>
  </Tab>
</Tabs>

## Step 2: Install the Momentic skill

The Momentic skill gives your assistant explicit operating guidance for Momentic
workflows: it teaches the model how to build reliable tests, construct test
steps correctly, reuse modules in your workspace, and more.

Without a skill, coding agents are far more likely to make malformed tool calls
and waste time on unnecessary actions.

<Card>
  <Tabs>
    <Tab title="Cursor">
      [Global skill directory](https://cursor.com/docs/context/skills):
      `~/.cursor/skills/momentic-test/SKILL.md`

      Cursor respected directories:

      * `~/.cursor/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.codex/skills/<name>/SKILL.md`

      ```bash  theme={null}
      npx momentic-mobile install-skills --cursor
      ```
    </Tab>

    <Tab title="Claude Code">
      [Global skill directory](https://code.claude.com/docs/en/skills):
      `~/.claude/skills/momentic-test/SKILL.md`

      Claude Code respected directories:

      * `~/.claude/skills/<name>/SKILL.md`

      ```bash  theme={null}
      npx momentic-mobile install-skills --claude-code
      ```
    </Tab>

    <Tab title="Codex">
      [Global skill directory](https://developers.openai.com/codex/skills):
      `~/.agents/skills/momentic-test/SKILL.md`

      Codex respected directories:

      * `~/.agents/skills/<name>/SKILL.md`

      ```bash  theme={null}
      npx momentic-mobile install-skills --codex
      ```
    </Tab>

    <Tab title="OpenCode">
      [Global skill directory](https://opencode.ai/docs/skills/):
      `~/.config/opencode/skills/momentic-test/SKILL.md`

      OpenCode respected directories:

      * `~/.config/opencode/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.agents/skills/<name>/SKILL.md`

      ```bash  theme={null}
      npx momentic-mobile install-skills --opencode
      ```
    </Tab>

    <Tab title="Copilot (VS Code)">
      [Global skill directory](https://code.visualstudio.com/docs/copilot/customization/agent-skills):
      `~/.copilot/skills/momentic-test/SKILL.md`

      Copilot respected directories:

      * `~/.copilot/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.agents/skills/<name>/SKILL.md`

      ```bash  theme={null}
      npx momentic-mobile install-skills --copilot
      ```
    </Tab>

    <Tab title="Custom path">
      ```bash  theme={null}
      npx momentic-mobile install-skills ~/my/custom/skills/momentic-test
      ```
    </Tab>
  </Tabs>
</Card>

## Step 3: Add an agent rule

Agent rules are stronger, global rulesets that agents are trained to strongly
respect. They are usually stored in an `AGENTS.md` file at the root of your
codebase. Some agents also support rules in their own custom directory (e.g.
`.cursor/rules`).

We recommend adding one of the following lines to your rules to prevent agents
from bypassing Momentic's MCP tools completely and directly editing your test or
module YAML files. Direct edits will likely lead to parsing and caching errors.

```bash  theme={null}
Never directly edit Momentic test (`*.test.yaml`) or module YAMLs (`*.module.yaml`). Only use the Momentic MCP tools to edit Momentic YAMLs. If they are unavailable tell the user you are unable to edit the YAML files.
```

## Step 4: Verify installation

The MCP server should now show up in a status page within your coding agent.
CLI-based tools usually provide a command like `/mcp` to view all installed MCP
servers.

Start a new chat and ask the agent what MCP servers and tools are available. It
should list tools whose names start with `momentic_`, such as
`momentic_get_artifacts`. If tools don’t appear, restart the IDE completely.

You're now ready to use Momentic's MCP! Select the Momentic skill and then
insert your desired goal.

## Usage

1. **Model selection**: Choose the latest frontier models for the best
   performance. As of version `0.55.1`, Momentic has benchmarked MCP performance
   on `GPT5.4`. If current agent performance is acceptable, `Medium` reasoning
   can improve speed by about 20%.
2. **Invoke Momentic's skill**: Explicitly invoke the skill in your assistant
   (e.g. in Codex, type `/momentic` and choose the autocompleted skill).
3. **Prompting**: Specific instructions generally lead to better outcomes. For
   exploratory testing, we recommend specifying a step limit so that the agent
   knows when to stop.
4. **Session management**: Allow sessions to clean up properly. You should
   notice the model calling the `momentic_session_terminate` tool, which will
   shut down the emulator session. Repeatedly stopping your coding agent may
   leak emulator resources and slow down your machine.

## Configurable settings

For all available flags and environment variables, see the
[mcp command reference](/mobile-cli/commands/mcp).


Built with [Mintlify](https://mintlify.com).