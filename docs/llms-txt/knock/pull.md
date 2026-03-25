# Source: https://docs.knock.app/cli/message-type/pull.md

# Source: https://docs.knock.app/cli/guide/pull.md

# Source: https://docs.knock.app/cli/partial/pull.md

# Source: https://docs.knock.app/cli/translation/pull.md

# Source: https://docs.knock.app/cli/email-layout/pull.md

# Source: https://docs.knock.app/cli/workflow/pull.md

# Source: https://docs.knock.app/cli/resources/pull.md

# Pull all resources

Pulls the contents of all Knock resources (workflows, partials, email layouts, translations, guides, and message-types) from Knock into your local file system.

Resources will be grouped by resource type within subdirectories of the target directory path set either by your `knock.json` file or by the `--knock-dir` flag. See the [Directory structure](/cli/overview/directory-structure) section for details on the directory structure used by `push` and `pull` commands.

### Flags

- **--environment** (string): The environment to use. Defaults to development.
- **--branch** (string): The branch to use. Defaults to empty (the main branch).
- **--knock-dir** (directory): The target directory path to pull all resources into.
- **--hide-uncommitted-changes** (boolean): Should any uncommitted changes be hidden? Defaults to false.
- **--force** (boolean): Removes the confirmation prompt. Defaults to false.

```bash title="Pull all resources"
knock pull --knock-dir=./knock
```
