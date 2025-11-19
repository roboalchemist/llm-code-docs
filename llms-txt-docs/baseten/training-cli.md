# Source: https://docs.baseten.co/reference/cli/training/training-cli.md

# Training CLI reference

> Deploy, manage, and monitor training jobs using the Truss CLI.

# Initialize Training Jobs

## `init`

```sh  theme={"system"}
truss train init [OPTIONS]
```

Initializes files needed to launch a training job. If no options passed, initializes an empty training project.

**Options:**

* `--examples`: A single example or comma separated list of verified [examples](https://github.com/basetenlabs/ml-cookbook/tree/main/examples).
* `--target-directory`: Location to initialize the example/s or empty training project.

***

# Deploy Training Jobs

## `push`

```sh  theme={"system"}
truss train push [OPTIONS] CONFIG
```

Deploys and runs a training job.

* `CONFIG`: Path to a training configuration file.

**Options:**

* `--tail`: Tail status and logs after pushing the training job.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.

***

# Monitor Training Jobs

## `logs`

```sh  theme={"system"}
truss train logs [OPTIONS]
```

Fetch and display logs for a training job.

**Options:**

* `--job-id` (TEXT): Job ID to fetch logs from.
* `--tail`: Continuously stream new logs.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `metrics`

```sh  theme={"system"}
truss train metrics [OPTIONS]
```

Get metrics for a training job.

**Options:**

* `--job-id` (TEXT): Job ID to fetch metrics from.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `view`

```sh  theme={"system"}
truss train view [OPTIONS]
```

List and view training jobs.

**Options:**

* `--project` (TEXT): View training jobs for a specific project (ID or name).
* `--job-id` (TEXT): View details of a specific training job.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

***

# Manage Training Jobs

## `stop`

```sh  theme={"system"}
truss train stop [OPTIONS]
```

Stop a running training job.

**Options:**

* `--project` (TEXT): Specify the project (ID or name) to stop a training job from.
* `--job-id` (TEXT): ID of the job to stop.
* `--all`: Stop all running jobs.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

# Manage Training Cache

The training cache is scoped to a specific training project. The CLI allows you to see a summary of the contents in the cache to
help you manage your storage.

## `cache summarize`

```sh  theme={"system"}
truss train cache summarize <project_name or project_id> [OPTIONS]
```

View the contents of the training cache in a table. Optionally sort by different column names (e.g. modified, size, etc.)

**Options:**

* `--sort` (TEXT): column to sort by
* `--order` (TEXT): Ascending (asc) or descending (desc) order for sorting
* `--remote` (TEXT): Name of the remote in .trussrc.

# Manage Checkpoints

## `deploy_checkpoints`

```sh  theme={"system"}
truss train deploy_checkpoints [OPTIONS]
```

Deploy model checkpoints from a training job.

## `get_checkpoint_urls`

```sh  theme={"system"}
truss train get_checkpoint_urls [OPTIONS]
```

Get a list of URL's to checkpoint artifacts for a training job

**Options:**

* `--job-id` (TEXT): Job ID containing the checkpoints.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

**Options:**

* `--project` (TEXT): Project (ID or name) name containing the checkpoints.
* `--job-id` (TEXT): Job ID containing the checkpoints.
* `--config` (TEXT): Path to a Python file defining a DeployCheckpointsConfig.
* `--dry-run`: Generate a truss config without deploying.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `recreate`

```sh  theme={"system"}
truss train recreate [OPTIONS]
```

Recreate an existing training job from an existing job ID. If no job ID is provided, it will default to the last created active training job and ask for confirmation first.

**Options:**

* `--job-id` (TEXT): Existing Job ID of Training Job to recreate.
* `--tail`: Tail status and logs after recreation.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `download`

```sh  theme={"system"}
truss train download [OPTIONS]
```

Download training job artifacts.

**Options:**

* `--job-id` (TEXT): Job ID to download artifacts from. (Required)
* `--target-directory` (PATH): Directory where the file should be downloaded. Defaults to current directory.
* `--no-unzip`: Instructs truss to not unzip the compressed file upon download.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

# Ignoring files and folders

To ignore specific files or folders, place a `.truss_ignore` file in the root directory of your project. Define the files or folders you want `truss` to ignore.

These can be absolute paths or paths relative to the location of the `.truss_ignore`

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

# Some large files
data/
```
