# Source: https://docs.knock.app/cli/message-type/push.md

# Source: https://docs.knock.app/cli/guide/push.md

# Source: https://docs.knock.app/cli/partial/push.md

# Source: https://docs.knock.app/cli/translation/push.md

# Source: https://docs.knock.app/cli/email-layout/push.md

# Source: https://docs.knock.app/cli/workflow/push.md

# Source: https://docs.knock.app/cli/resources/push.md

# Push all resources

Pushes all local resource files (workflows, partials, email layouts, and translations) back to Knock and upserts them.

Resources will be pushed to the target directory path set either by your `knock.json` file or by the `--knock-dir` flag. See the [Directory structure](/cli/overview/directory-structure) section for details on the directory structure used by `push` and `pull` commands.

### Flags

- **--knock-dir** (directory): The target directory path to push all resources from.
- **--commit** (boolean): Push and commit at the same time. Defaults to false.
- **-m, --commit-message** (string): The commit message to pass when using the `--commit` flag.

```bash title="Push all resources"
knock push --knock-dir=./knock
```
