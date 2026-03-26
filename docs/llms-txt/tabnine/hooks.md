# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/hooks.md

# Hooks

Intercept and customize Tabnine CLI behavior at key lifecycle points.

### What are Hooks?

Hooks are scripts that run automatically at specific points during Tabnine CLI execution, allowing you to customize behavior, add logging, enforce policies, or integrate with external tools.

### Hook Types

Tabnine CLI supports hooks at various lifecycle events:

* **before-agent** - Before agent processing starts
* **after-agent** - After agent completes
* **before-model** - Before model request
* **after-model** - After model response
* **before-tool** - Before tool execution
* **after-tool** - After tool completes
* **on-error** - When errors occur

### Enabling Hooks

Hooks must be explicitly enabled in settings:

```json
{
  "hooks": {
    "enabled": true
  }
}
```

### Creating Hooks

Place executable scripts in `.tabnine/hooks/`:. For example, add the following file: `.tabnine/hooks/before-tool.sh`

{% code title=".tabnine/hooks/before-tool.sh" %}

```bash
#!/bin/bash

# Log all tool executions
echo "[$(date)] Tool: $TABNINE_TOOL_NAME" >> /tmp/tabnine-tools.log
```

{% endcode %}

In order to make it executable, run the `chmod` command:

```bash
chmod +x .tabnine/hooks/before-tool.sh
```

### Hook Context

Hooks receive context via environment variables:

* `TABNINE_CLI=1` - Running in Tabnine CLI
* `TABNINE_TOOL_NAME` - Tool being executed (for tool hooks)
* `TABNINE_MODEL` - Current model name
* Additional variables depending on hook type

### Use Cases

Logging

{% code title="log-hook.sh" %}

```bash
#!/bin/bash
echo "$(date): $TABNINE_TOOL_NAME" >> ~/tabnine-audit.log
```

{% endcode %}

Policy Enforcement

{% code title="block-shell-in-prod.sh" %}

```bash
#!/bin/bash
if [[ "$TABNINE_TOOL_NAME" == "run_shell_command" ]] && [[ "$ENV" == "prod" ]]; then
  echo "Shell commands blocked in production"
  exit 1
fi
```

{% endcode %}

External Integration

{% code title="notify-external.sh" %}

```bash
#!/bin/bash
curl -X POST https://api.example.com/notify \
  -d "{\"tool\": \"$TABNINE_TOOL_NAME\", \"time\": \"$(date)\"}"
```

{% endcode %}

{% hint style="info" %}
**Best Practices:**

1. **Keep hooks fast** – Hooks run synchronously and can slow down the CLI if they take too long.
2. **Handle errors gracefully** – A non-zero exit code from a hook will block the associated action. Make sure to handle failures and return appropriate exit codes.
3. **Log debugging info** – Hooks run silently unless they output; include useful logging to help debugging.
4. **test thoroughly** – Broken hooks can break Tabnine CLI. Test hooks in a safe environment before deploying to production.
   {% endhint %}

### Troubleshooting

There are some common problems that come up with hooks that have standard troubleshooting flows:

#### Hook not running

<details>

<summary>Check these items:</summary>

* Verify hooks are enabled: Use `/hooks list` to confirm that hooks are activated in the settings.
* Ensure the script is executable: `chmod +x .tabnine/hooks/hook-name.sh`
* Verify the script name matches the expected hook type:
* Ensure the file name corresponds to the hook lifecycle event you expect (for example, before-tool.sh).
* Check for syntax errors: Run the script manually to see any runtime or syntax errors.

</details>

#### Hook blocking execution

Cause: Hook returned non-zero exit code

Solution: Fix the hook script or temporarily disable hooks (for example via `/hooks disable`).

{% hint style="danger" %}
**Security Note:**

Hooks execute with your user permissions. Only use hooks from trusted sources.
{% endhint %}

### See Also

* [Commands: /hooks](https://docs.tabnine.com/main/getting-started/tabnine-cli/commands#hooks)
* [Settings](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/settings)
