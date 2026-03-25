# Source: https://docs.knock.app/cli/message-type/new.md

# Source: https://docs.knock.app/cli/guide/new.md

# Source: https://docs.knock.app/cli/partial/new.md

# Source: https://docs.knock.app/cli/email-layout/new.md

# Source: https://docs.knock.app/cli/workflow/new.md

# Create a new workflow

Create a new workflow with a minimal configuration. You can either select steps interactively or use a template to scaffold the workflow.

The command will create a new workflow directory in your local file system. By default, this will be in the workflows resource directory set by your `knock.json` file, or the current working directory if not configured.

### Flags

- **--key** (string): The key for the workflow. If not provided, will be prompted or inferred from the workflow directory name.
- **--name** (string): The name for the workflow. If not provided, will be generated from the key.
- **--environment** (string): The environment to use. Defaults to development.
- **--branch** (string): The branch to use. Defaults to the main branch.
- **--steps** (string): A comma-separated list of step types to include in the workflow (e.g., 'email,sms,in_app_feed'). If not provided, you will be prompted to select steps interactively.
- **--template** (string): A template to use for scaffolding the workflow. Accepts a template string that resolves to a GitHub repository URL. For example, `<your-org>/<your-repo>/workflows/digest-email`. Use `workflows/<workflow-key>` to reference [pre-built Knock templates](https://github.com/knocklabs/templates/tree/main/workflows).
- **--push** (boolean): Push the workflow to Knock after creating it locally. Defaults to false.
- **--force** (boolean): Overwrites an existing workflow directory without prompting for confirmation. Defaults to false.

```bash title="Create a workflow interactively"
knock workflow new
```

```bash title="Create a workflow with a specific key"
knock workflow new --key=my-workflow
```

```bash title="Create a workflow with specific steps"
knock workflow new --key=my-workflow --steps=email,sms,in_app_feed
```

```bash title="Create a workflow from a template"
knock workflow new --key=my-workflow --template=workflows/digest-email
```

```bash title="Create and push a workflow"
knock workflow new --key=my-workflow --steps=email --push
```
