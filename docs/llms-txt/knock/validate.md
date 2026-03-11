# Source: https://docs.knock.app/mapi-reference/translations/validate.md

# Source: https://docs.knock.app/mapi-reference/message_types/validate.md

# Source: https://docs.knock.app/mapi-reference/guides/validate.md

# Source: https://docs.knock.app/mapi-reference/partials/validate.md

# Source: https://docs.knock.app/mapi-reference/email_layouts/validate.md

# Source: https://docs.knock.app/mapi-reference/broadcasts/validate.md

# Source: https://docs.knock.app/mapi-reference/workflows/validate.md

# Source: https://docs.knock.app/cli/message-type/validate.md

# Source: https://docs.knock.app/cli/guide/validate.md

# Source: https://docs.knock.app/cli/partial/validate.md

# Source: https://docs.knock.app/cli/translation/validate.md

# Source: https://docs.knock.app/cli/email-layout/validate.md

# Source: https://docs.knock.app/cli/workflow/validate.md

# Validate workflow

You can validate a new or updated workflow directory with the `workflow validate` command. Knock will validate the given workflow payload in the same way as it would with the `workflow push` command, except without persisting those changes.

Note: Validating a workflow is only done against the `development` environment.

### Flags

- **--all** (boolean): Whether to validate all workflows from the target directory path set by `--workflows-dir`. Defaults to false.
- **--workflows-dir** (directory): Specifies the target directory path to find and validate all workflows from. Only available to be used with --all, and defaults to the current working directory.

```bash title="Basic usage"
knock workflow validate my-workflow
```
