# Source: https://docs.knock.app/mapi-reference/workflows/run.md

# Source: https://docs.knock.app/cli/workflow/run.md

# Run workflow

You can run a workflow with the `workflow run` command. Knock will execute a run for the latest saved version of the workflow it finds with the given key and parameters you send it.

Note:

- Changes to the local version of the workflow in your file system will not be reflected in a workflow run; it will use the current version that is stored in Knock.

### Flags

- **--environment** (string): The slug of the environment in which to run this workflow. Defaults to development.
- **--recipients** (string[]): One or more recipient ids for this workflow run, maximum limit 5.
- **--data** (string): A JSON string of the data with which this workflow will run.
- **--actor** (string): An optional actor id for this workflow run.
- **--tenant** (string): An optional tenant id for this workflow run.

```bash title="Basic usage"
knock workflow run my-workflow \
  --environment=production \
  --recipients=ellie
```
