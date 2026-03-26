# Source: https://momentic.ai/docs/mobile-cli/commands/install-skills.md

# Source: https://momentic.ai/docs/cli/commands/install-skills.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# install-skills

Install the Momentic skill so coding assistants get explicit instructions for
using momentic MCP. Without it, agents are more likely to make malformed tool
calls.

Run this after configuring the MCP server. For full setup, see
[MCP](/model-context-protocol).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills [options] [installPath]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills [options] [installPath]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills [options] [installPath]
  ```
</CodeGroup>

* **\[installPath]**: Optional target directory. **Mutually exclusive with all
  agent flags.** Either provide a path to install to a custom directory, or use
  one agent flag below, never both.

## Options

Use exactly one of these: either a custom `[installPath]` or one of the agent
flags below.

### `--cursor`

Install into Cursor's default skill directory:
`~/.cursor/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --cursor
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --cursor
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --cursor
  ```
</CodeGroup>

### `--claude-code`

Install into Claude Code's default skill directory:
`~/.claude/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --claude-code
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --claude-code
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --claude-code
  ```
</CodeGroup>

### `--codex`

Install into Codex's default skill directory:
`~/.agents/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --codex
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --codex
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --codex
  ```
</CodeGroup>

### `--opencode`

Install into OpenCode's default skill directory:
`~/.config/opencode/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --opencode
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --opencode
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --opencode
  ```
</CodeGroup>

### `--copilot`

Install into Copilot (VS Code)'s default skill directory:
`~/.copilot/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --copilot
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --copilot
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --copilot
  ```
</CodeGroup>

### Custom path

Install into a custom directory. The command creates `SKILL.md` in the given
path.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills ~/my/custom/skills/momentic-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills ~/my/custom/skills/momentic-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills ~/my/custom/skills/momentic-test
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).