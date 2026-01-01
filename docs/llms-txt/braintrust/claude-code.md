# Source: https://braintrust.dev/docs/integrations/sdk-integrations/claude-code.md

# Claude Code

[Claude Code](https://code.claude.com/docs/en/overview) is Anthropic's agentic coding tool that lives in your terminal. Braintrust provides two complementary plugins for Claude Code:

* **trace-claude-code**: Traces Claude Code's operations to show LLM calls, tool usage, and timing data. This can be useful for personal exploration or to monitor your team's activity.

* **braintrust**: Brings context (docs, logs, experiments) from Braintrust into your programming environment. For example, query logs, access Braintrust docs, or fetch experiment results when writing evaluations.

This guide covers both plugins and how to use them together.

## Setup

Install both plugins from the Braintrust plugin marketplace and run the setup script to configure your API key and project settings.

<Steps>
  <Step title="Prerequisites">
    Before installing the Braintrust plugins, ensure you have Claude Code and `jq` installed:

    Install Claude Code:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    Install the `jq` JSON processor, which the tracing hooks use to parse Claude Code's output:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    brew install jq
    ```
  </Step>

  <Step title="Install the plugins">
    Install the Braintrust plugin marketplace, the tracing plugin for automatic observability, and the operations plugin to enable Claude for querying logs and running evaluations:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    claude plugin marketplace add braintrustdata/braintrust-claude-plugin
    claude plugin install trace-claude-code@braintrust-claude-plugin
    claude plugin install braintrust@braintrust-claude-plugin
    ```
  </Step>

  <Step title="Run the setup script">
    The setup script will prompt you for your Braintrust API key and project name:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    ~/.claude/plugins/marketplaces/braintrust-claude-plugin/skills/trace-claude-code/setup.sh
    ```

    The script configures these environment variables in your Claude Code settings. You can customize them if needed:

    * `BRAINTRUST_CC_PROJECT` - Project name (default: "claude-code")
    * `BRAINTRUST_CC_DEBUG` - Set to "true" for verbose logging
    * `TRACE_TO_BRAINTRUST` - Set to "false" to temporarily disable tracing

    <Note>
      The plugin directory path may vary depending on your Claude Code configuration. If the path above doesn't exist, check your Claude Code settings for the plugins directory location.
    </Note>
  </Step>
</Steps>

## Trace Claude Code

The `trace-claude-code` plugin captures every operation Claude Code performs, helping you:

* Debug issues by seeing exactly what tools Claude ran
* Monitor team usage and patterns
* Understand LLM call costs and performance

Start a Claude Code session:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
claude
```

The plugin automatically traces each session as a hierarchy of spans:

* **Session root**: The overall Claude Code session from start to finish
* **Turns**: Individual conversation exchanges (your input → Claude's response)
* **Tool calls**: Operations like file reads, edits, terminal commands, and searches

Each trace includes rich metadata:

* Session ID and workspace location
* Turn numbers and conversation content
* Tool names with inputs and outputs
* Span attributes indicating type ("task", "llm", "tool")

To view your traces in real-time, go to your project in the [Braintrust UI](https://braintrust.dev) and select <Icon icon="activity" /> **Logs**.

## Use Braintrust with Claude Code

The `braintrust` plugin brings Braintrust data and context directly into Claude Code.

### Fetch experiment results

When writing evaluations, ask Claude to fetch experiment results so you can iterate on your evaluation logic:

```
Fetch the results from my latest "summarization-quality" experiment
```

```
Get the experiment data for "gpt-5-mini-baseline" and show me the failing cases
```

This is particularly useful when you're writing eval code and want to see real results without leaving your terminal.

### Query logs

Ask Claude to query your logs using natural language. Claude will use SQL to fetch the data:

```
Find all my Claude Code sessions from last week where I was working on authentication features
```

```
Query the logs for sessions where errors occurred in the last 3 days and summarize the common issues
```

Claude will share both the SQL query and the results.

### Log data

Ask Claude to log data to a Braintrust project:

```
Log this conversation to my project with metadata indicating it was a bug fix
```

## Update the integration

After initial setup, you can update the plugin configuration by editing the environment variables in your `.claude/settings.local.json` file. This file is located in your home directory at `~/.claude/settings.local.json`.

<Note>
  Configuration changes take effect the next time you start a Claude Code session. Exit any running sessions and start a new one to apply your changes.
</Note>

### Change your project

To change which Braintrust project your traces are sent to:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "env": {
    "BRAINTRUST_CC_PROJECT": "your-new-project-name"
  }
}
```

### Change your API key

To change your Braintrust API key:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "env": {
    "BRAINTRUST_API_KEY": "your-new-api-key"
  }
}
```

### Enable debug logging

To see detailed logging information for troubleshooting:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "env": {
    "BRAINTRUST_CC_DEBUG": "true"
  }
}
```

Debug logs are written to `~/.claude/state/braintrust_hook.log`.

### Disable the plugins

To temporarily stop sending traces to Braintrust without uninstalling the plugin, set the `TRACE_TO_BRAINTRUST` environment variable to `false` in your `.claude/settings.local.json`:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "env": {
    "TRACE_TO_BRAINTRUST": "false"
  }
}
```

This keeps the plugins installed but prevents them from capturing any data. To re-enable tracing, change the value back to `"true"`.

To completely remove the Braintrust plugins from Claude Code:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
claude plugin uninstall trace-claude-code@braintrust-claude-plugin
claude plugin uninstall braintrust@braintrust-claude-plugin
claude plugin marketplace remove braintrust-claude-plugin
```

After uninstalling, you may also want to clean up the state and log files:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
rm ~/.claude/state/braintrust_state.json
rm ~/.claude/state/braintrust_hook.log
```

## Troubleshooting

<Accordion title="No traces appearing">
  Check the hook logs for errors:

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  tail -f ~/.claude/state/braintrust_hook.log
  ```

  Verify your environment variables are set correctly in `.claude/settings.local.json`, and enable debug mode by setting `BRAINTRUST_CC_DEBUG=true`.
</Accordion>

<Accordion title="Permission errors">
  Make sure the hook scripts are executable:

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  chmod +x ~/.claude/plugins/marketplaces/braintrust-claude-plugin/skills/trace-claude-code/hooks/*.sh
  ```
</Accordion>

<Accordion title="State issues">
  If traces seem corrupted or incomplete, try resetting the state file:

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  rm ~/.claude/state/braintrust_state.json
  ```

  Then start a new Claude Code session.
</Accordion>

## Next steps

Now that you have both plugins set up:

* **Explore your traces**: Navigate to your project in Braintrust and explore the hierarchical trace structure.
* **Run evaluations**: Check out the [evaluation guide](/docs/guides/evals) to learn evaluation patterns.
* **Browse examples**: The [braintrust-claude-plugin repository](https://github.com/braintrustdata/braintrust-claude-plugin) includes evaluation suites that demonstrate the plugin's capabilities.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt