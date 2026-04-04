# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/checkpointing.md

# Checkpointing

Checkpointing automatically creates snapshots of your project before file-modifying tools execute, allowing you to undo changes.

### What is Checkpointing?

When checkpointing is enabled, Tabnine CLI creates a Git snapshot before any tool that modifies files (like `write_file`, `replace`) is executed. This allows you to restore your project to its previous state using the `/restore` command.

#### Requirements

* Git installed and available in your PATH
* A Git repository initialized in your project directory

#### Enable via Settings File

Edit `.tabnine/agent/settings.json` (global: `~/.tabnine/agent/settings.json` or project: `.tabnine/agent/settings.json`):

```json
{
  "general": {
    "checkpointing": {
      "enabled": true
    }
  }
}
```

{% hint style="info" %}
This setting is not available in the `/settings` dialog and must be set directly in the settings JSON file.
{% endhint %}

### How It Works

{% stepper %}
{% step %}
**Before file modification**

Tabnine CLI creates a Git commit snapshot.
{% endstep %}

{% step %}
**Tool executes**

File changes are made.
{% endstep %}

{% step %}
**Checkpoint saved**

Snapshot information is stored in `~/.tabnine/agent/tmp/<project_hash>/checkpoints/`.
{% endstep %}

{% step %}
**Restore available**

Use `/restore` to undo changes.
{% endstep %}
{% endstepper %}

### Using `/restore`

#### List Available Checkpoints

```
/restore
```

Shows a list of recent file modifications that can be undone.

#### Restore a Specific Checkpoint

```
/restore <tool_call_id>
```

Restores files to the state before that tool was executed.

**Example output:**

```
Available checkpoints:
- replace-2024-01-15-14-30-42 (Modified src/index.ts)
- write_file-2024-01-15-14-25-10 (Created config.json)
```

Then run:

```
/restore replace-2024-01-15-14-30-42
```

### Checkpoint Storage

Checkpoints are stored in:

* **Linux/macOS:** `~/.tabnine/agent/tmp/<project_hash>/checkpoints/`
* **Windows:** `C:\Users\<YourUsername>\.tabnine\agent\tmp\<project_hash>\checkpoints\`

{% hint style="info" %}
Checkpoints are project-specific based on your working directory.
{% endhint %}

### Checkpointing vs `/chat save`

| Feature          | Checkpointing                           | `/chat save`                |
| ---------------- | --------------------------------------- | --------------------------- |
| **Purpose**      | Undo file changes                       | Save conversation state     |
| **Automatic**    | Yes (before file mods)                  | No (manual)                 |
| **Restore with** | `/restore <id>`                         | `/chat resume <tag>`        |
| **What's saved** | Git snapshot                            | Conversation history        |
| **Location**     | `~/.tabnine/agent/tmp/.../checkpoints/` | `~/.tabnine/agent/tmp/.../` |

### Troubleshooting

<details>

<summary>"Checkpointing is enabled but Git service is not available"</summary>

Solution: Ensure Git is installed and your project is a Git repository:

```bash
git --version  # Check Git is installed
git status     # Check you're in a Git repo
git init       # Initialize repo if needed
```

</details>

<details>

<summary>"Cannot restore checkpoint: commit hash not found"</summary>

Cause: The Git commit was removed (e.g., repo re-cloned, history rewritten).

Solution: Checkpoints rely on Git history. If the repository was reset or re-cloned, old checkpoints cannot be restored.

</details>

<details>

<summary>Checkpoints not being created</summary>

Check:

* Git is installed: `git --version`
* You're in a Git repository: `git status`
* Checkpointing is enabled in `.tabnine/agent/settings.json`:

```json
{
  "general": {
    "checkpointing": {
      "enabled": true
    }
  }
}
```

</details>

{% hint style="success" %}

### Best Practices:

* Keep Git history: Avoid force-pushing or rewriting history if you need checkpoints
* Regular commits: Make manual commits for important milestones
* Cleanup: Old checkpoint files can be manually deleted from `~/.tabnine/agent/tmp/`
* Backup: Checkpoints are local; use Git remotes for actual backups
  {% endhint %}

### Disabling Checkpointing

Edit `.tabnine/agent/settings.json` and set to `false`:

```json
{
  "general": {
    "checkpointing": {
      "enabled": false
    }
  }
}
```

### See Also

* [Commands: /restore](https://docs.tabnine.com/main/getting-started/tabnine-cli/commands#restore)
* [Commands: /chat save](https://docs.tabnine.com/main/getting-started/tabnine-cli/commands#chat)
* [Settings](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/settings)
