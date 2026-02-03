# Source: https://docs.baseten.co/reference/cli/training/training-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Training CLI reference

> Deploy, manage, and monitor training jobs using the Truss CLI.

The `truss train` command provides subcommands for managing the full training job lifecycle.

```sh  theme={"system"}
truss train [COMMAND] [OPTIONS]
```

### Universal options

The following options are available for all `truss train` commands:

* `--help`: Show help message and exit.
* `--non-interactive`: Disable interactive prompts (for CI/automated environments).
* `--remote TEXT`: Name of the remote in `.trussrc`.

***

## init

Initialize a training project from templates or create an empty project.

```sh  theme={"system"}
truss train init [OPTIONS]
```

### Options

<ParamField body="--examples" type="string">
  Template name or comma-separated list of templates to initialize. See the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook) for available examples.
</ParamField>

<ParamField body="--target-directory" type="string">
  Directory to initialize the project in. Defaults to current directory.
</ParamField>

<ParamField body="--list-examples">
  List all available example templates.
</ParamField>

### Examples

Initialize a project from a template:

```sh  theme={"system"}
truss train init --examples llama-8b-lora-unsloth
```

Initialize multiple templates:

```sh  theme={"system"}
truss train init --examples llama-8b-lora-unsloth,qwen3-8b-lora-dpo-trl
```

List available templates:

```sh  theme={"system"}
truss train init --list-examples
```

Create an empty training project:

```sh  theme={"system"}
truss train init
```

***

## push

Submit and run a training job.

```sh  theme={"system"}
truss train push [OPTIONS] CONFIG
```

### Arguments

<ParamField body="CONFIG" type="string" required>
  Path to the training configuration file (e.g., `config.py`).
</ParamField>

### Options

<ParamField body="--tail">
  Stream status and logs after submitting the job.
</ParamField>

<ParamField body="--job-name" type="string">
  Name for the training job.
</ParamField>

<ParamField body="--team" type="string">
  Team name for the training project. If not specified, Truss infers the team or prompts for selection.
</ParamField>

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

### Examples

Submit a training job:

```sh  theme={"system"}
truss train push config.py
```

Submit and stream logs:

```sh  theme={"system"}
truss train push config.py --tail
```

Submit to a specific team:

```sh  theme={"system"}
truss train push config.py --team my-team-name
```

Submit with a custom job name:

```sh  theme={"system"}
truss train push config.py --job-name fine-tune-v1
```

***

## logs

Fetch and stream logs from a training job.

```sh  theme={"system"}
truss train logs [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string">
  Job ID to fetch logs from.
</ParamField>

<ParamField body="--project" type="string">
  Project name or project ID.
</ParamField>

<ParamField body="--project-id" type="string">
  Project ID.
</ParamField>

<ParamField body="--tail">
  Continuously stream new logs.
</ParamField>

### Examples

Stream logs for a specific job:

```sh  theme={"system"}
truss train logs --job-id abc123 --tail
```

View logs for a job without streaming:

```sh  theme={"system"}
truss train logs --job-id abc123
```

***

## metrics

View real-time metrics for a training job including CPU, GPU, and storage usage.

```sh  theme={"system"}
truss train metrics [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string">
  Job ID to fetch metrics from.
</ParamField>

<ParamField body="--project" type="string">
  Project name or project ID.
</ParamField>

<ParamField body="--project-id" type="string">
  Project ID.
</ParamField>

### Examples

View metrics for a specific job:

```sh  theme={"system"}
truss train metrics --job-id abc123
```

***

## view

List training projects and jobs, or view details for a specific job.

```sh  theme={"system"}
truss train view [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string">
  View details for a specific training job.
</ParamField>

<ParamField body="--project" type="string">
  View jobs for a specific project (name or ID).
</ParamField>

<ParamField body="--project-id" type="string">
  View jobs for a specific project ID.
</ParamField>

### Examples

List all training projects:

```sh  theme={"system"}
truss train view
```

View jobs in a specific project:

```sh  theme={"system"}
truss train view --project my-project
```

View details for a specific job:

```sh  theme={"system"}
truss train view --job-id abc123
```

***

## stop

Stop a running training job.

```sh  theme={"system"}
truss train stop [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string">
  Job ID to stop.
</ParamField>

<ParamField body="--project" type="string">
  Project name or project ID.
</ParamField>

<ParamField body="--project-id" type="string">
  Project ID.
</ParamField>

<ParamField body="--all">
  Stop all running jobs. Prompts for confirmation.
</ParamField>

### Examples

Stop a specific job:

```sh  theme={"system"}
truss train stop --job-id abc123
```

Stop all running jobs:

```sh  theme={"system"}
truss train stop --all
```

***

## recreate

Recreate an existing training job with the same configuration.

```sh  theme={"system"}
truss train recreate [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string">
  Job ID of the training job to recreate. If not provided, defaults to the last created job.
</ParamField>

<ParamField body="--tail">
  Stream status and logs after recreating the job.
</ParamField>

### Examples

Recreate a specific job:

```sh  theme={"system"}
truss train recreate --job-id abc123
```

Recreate and stream logs:

```sh  theme={"system"}
truss train recreate --job-id abc123 --tail
```

***

## download

Download training job artifacts to your local machine.

```sh  theme={"system"}
truss train download [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string" required>
  Job ID to download artifacts from.
</ParamField>

<ParamField body="--target-directory" type="path">
  Directory to download files to. Defaults to current directory.
</ParamField>

<ParamField body="--no-unzip">
  Keep the compressed archive without extracting.
</ParamField>

### Examples

Download artifacts to current directory:

```sh  theme={"system"}
truss train download --job-id abc123
```

Download to a specific directory:

```sh  theme={"system"}
truss train download --job-id abc123 --target-directory ./downloads
```

Download without extracting:

```sh  theme={"system"}
truss train download --job-id abc123 --no-unzip
```

***

## deploy\_checkpoints

Deploy a trained model checkpoint to Baseten's inference platform.

```sh  theme={"system"}
truss train deploy_checkpoints [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string">
  Job ID containing the checkpoints to deploy.
</ParamField>

<ParamField body="--project" type="string">
  Project name or project ID.
</ParamField>

<ParamField body="--project-id" type="string">
  Project ID.
</ParamField>

<ParamField body="--config" type="string">
  Path to a Python file defining a `DeployCheckpointsConfig`.
</ParamField>

<ParamField body="--dry-run">
  Generate a Truss config without deploying. Useful for previewing the deployment configuration.
</ParamField>

<ParamField body="--truss-config-output-dir" type="string">
  Path to output the generated Truss config. Defaults to `truss_configs/<model_version_name>_<model_version_id>`.
</ParamField>

### Examples

Deploy checkpoints interactively:

```sh  theme={"system"}
truss train deploy_checkpoints
```

Deploy checkpoints from a specific job:

```sh  theme={"system"}
truss train deploy_checkpoints --job-id abc123
```

Preview deployment without deploying:

```sh  theme={"system"}
truss train deploy_checkpoints --job-id abc123 --dry-run
```

***

## get\_checkpoint\_urls

Get presigned URLs for checkpoint artifacts.

```sh  theme={"system"}
truss train get_checkpoint_urls [OPTIONS]
```

### Options

<ParamField body="--job-id" type="string">
  Job ID containing the checkpoints.
</ParamField>

### Examples

Get checkpoint URLs for a job:

```sh  theme={"system"}
truss train get_checkpoint_urls --job-id abc123
```

***

## cache summarize

View a summary of the training cache for a project.

```sh  theme={"system"}
truss train cache summarize [OPTIONS] PROJECT
```

### Arguments

<ParamField body="PROJECT" type="string" required>
  Project name or project ID.
</ParamField>

### Options

<ParamField body="--sort" type="string">
  Sort files by column. Options: `filepath`, `size`, `modified`, `type`, `permissions`.
</ParamField>

<ParamField body="--order" type="string">
  Sort order: `asc` (ascending) or `desc` (descending).
</ParamField>

<ParamField body="--output-format, -o" type="string">
  Output format: `cli-table` (default), `csv`, or `json`.
</ParamField>

### Examples

View cache summary:

```sh  theme={"system"}
truss train cache summarize my-project
```

Sort by size descending:

```sh  theme={"system"}
truss train cache summarize my-project --sort size --order desc
```

Export as JSON:

```sh  theme={"system"}
truss train cache summarize my-project --output-format json
```

***

## Ignore files and folders

Create a `.truss_ignore` file in your project root to exclude files from upload. Uses `.gitignore` syntax.

```plaintext .truss_ignore theme={"system"}
# Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd

# Type checking
.mypy_cache/

# Testing
.pytest_cache/

# Large data files
data/
*.bin
```
