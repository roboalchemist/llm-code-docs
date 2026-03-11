# Source: https://docs.knock.app/cli/commit/promote.md

# Promote changes

You can promote one change to the subsequent environment, or all changes across all resources to the target environment from its directly preceding environment, using the `commit promote` command.

Note:

- For example, if you have three environments "development", "staging", and "production" (in that order), setting the `--to` flag to `production` will promote all new changes from the staging environment to the production environment.
- Promoting one single commit from staging using the `--only` flag, will result in that commit being promoted to production.
- The `--to` environment must be a non-development environment.
- The `--to` and `--only` flags can't be used together.

### Flags

- **--to** (string): The destination environment.
- **--only** (string): The target commit id to promote to the subsequent environment.
- **--force** (boolean): Removes the confirmation prompt. Defaults to false.

```bash title="Promotes all changes"
knock commit promote --to=production
```

```bash title="Promotes one change"
knock commit promote --only=69cdde18-830a-42e0-ad4b-a230943bdc90
```
