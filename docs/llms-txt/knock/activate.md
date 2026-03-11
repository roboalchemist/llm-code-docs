# Source: https://docs.knock.app/mapi-reference/guides/activate.md

# Source: https://docs.knock.app/mapi-reference/workflows/activate.md

# Source: https://docs.knock.app/cli/guide/activate.md

# Source: https://docs.knock.app/cli/workflow/activate.md

# Activate workflow

You can activate or deactivate a workflow in a given environment with the `workflow activate` command.

Note:

- This immediately enables or disables a workflow in a given environment without needing to go through environment promotion.
- By default, this command activates a given workflow. Pass in the `--status` flag with `false` in order to deactivate it.

### Flags

- **--environment** (string): The environment to activate the workflow in.
- **--force** (boolean): Removes the confirmation prompt. Defaults to false.
- **--status** (boolean): The status to set. Defaults to `true`.

```bash title="Basic usage"
knock workflow activate my-workflow \
  --environment=development
```

```bash title="Deactivating a workflow"
knock workflow activate my-workflow \
  --environment=development \
  --status=false
```
