# Source: https://docs.anyscale.com/reference/workspaces.md

# Source: https://docs.anyscale.com/platform/workspaces.md

# Source: https://docs.anyscale.com/archive/ref/workspaces.md

# Workspaces API Reference (Legacy)

[View Markdown](/archive/ref/workspaces.md)

# Workspaces API Reference (Legacy)

warning

These methods are deprecated and will be fully removed from the Anyscale platform on January 29, 2026. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier. Please use the [current APIs](/reference/workspaces.md) instead.

## Workspaces CLI[​](#workspaces-cli "Direct link to Workspaces CLI")

### `anyscale workspace create` Deprecated[​](#anyscale-workspace-create-deprecated "Direct link to anyscale-workspace-create-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use 'anyscale workspace\_v2 create' instead.

**Usage**

`anyscale workspace create [OPTIONS]`

\[DEPRECATED - use 'workspace\_v2 create' instead] Create a workspace on Anyscale.

**Options**

* **`--name/-n`**: Name of the workspace to create.
* **`--project-id`**: ID of the project to associate with the workspace.
* **`--cloud-id`**: ID of the cloud to use for the workspace.
* **`--cluster-env-build-id`**: ID of the cluster environment build to use for the workspace.
* **`--docker`**: Custom docker image URI.
* **`--python-version`**: Python version for the custom docker image.
* **`--ray-version`**: Ray version for the custom docker image.
* **`--compute-config-id`**: ID of the compute config to use for the workspace.

### `anyscale workspace run` Deprecated[​](#anyscale-workspace-run-deprecated "Direct link to anyscale-workspace-run-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use 'anyscale workspace\_v2 run\_command' instead.

**Usage**

`anyscale workspace run [OPTIONS] COMMAND`

\[DEPRECATED - use 'workspace\_v2 run\_command' instead] Run a command in a workspace, syncing files first if needed.

**Options**

* **`--web-terminal/-w`**: Run the command in the webterminal. Progress can be tracked from the UI.
* **`--as-job/-j`**: Run the command as a background job in a new cluster.
* **`--no-push/-s`**: Whether to skip pushing files prior to running the command.

### `anyscale workspace ssh` Deprecated[​](#anyscale-workspace-ssh-deprecated "Direct link to anyscale-workspace-ssh-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use 'anyscale workspace\_v2 ssh' instead.

**Usage**

`anyscale workspace ssh [OPTIONS] [ARGS]...`

\[DEPRECATED - use 'workspace\_v2 ssh' instead] ssh into a workspace, you can also pass args to the ssh command. E.g. 'anyscale workspace ssh -- -L 8888:localhost<!-- -->:8888

**Options**

### `anyscale workspace start` Deprecated[​](#anyscale-workspace-start-deprecated "Direct link to anyscale-workspace-start-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use 'anyscale workspace\_v2 start' instead.

**Usage**

`anyscale workspace start [OPTIONS]`

\[DEPRECATED - use 'workspace\_v2 start' instead] Start an existing workspace on Anyscale.

**Options**

* **`--name/-n`**: Name of existing workspace to start.

### `anyscale workspace terminate` Deprecated[​](#anyscale-workspace-terminate-deprecated "Direct link to anyscale-workspace-terminate-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use 'anyscale workspace\_v2 terminate' instead.

**Usage**

`anyscale workspace terminate [OPTIONS]`

\[DEPRECATED - use 'workspace\_v2 terminate' instead] Terminate a workspace on Anyscale.

**Options**

* **`--name/-n`**: Name of existing workspace to terminate.

### `anyscale workspace pull` Deprecated[​](#anyscale-workspace-pull-deprecated "Direct link to anyscale-workspace-pull-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use 'anyscale workspace\_v2 pull' instead.

**Usage**

`anyscale workspace pull [OPTIONS]`

\[DEPRECATED - use 'workspace\_v2 pull' instead] Pull files from a workspace on Anyscale.

**Options**

* **`--pull-git-state`**: Also pull git state. This will add additional overhead.

### `anyscale workspace push` Deprecated[​](#anyscale-workspace-push-deprecated "Direct link to anyscale-workspace-push-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use 'anyscale workspace\_v2 push' instead.

**Usage**

`anyscale workspace push [OPTIONS]`

\[DEPRECATED - use 'workspace\_v2 push' instead] Push files to a workspace on Anyscale.

**Options**

* **`--push-git-state`**: Also push git state. This is currently unoptimized and will be very slow.

### `anyscale workspace clone` Deprecated[​](#anyscale-workspace-clone-deprecated "Direct link to anyscale-workspace-clone-deprecated")

Deprecated

The workspace v1 CLI is being replaced. and will be removed on 2025-10-01. Please use workspace\_v2 clone functionality instead.

**Usage**

`anyscale workspace clone [OPTIONS]`

\[DEPRECATED - use workspace\_v2 clone functionality instead] Clone a workspace on Anyscale.

**Options**

* **`--name/-n`**: Name of existing workspace to clone.
* **`--verbose/-v`**: Verbose mode

### `anyscale workspace cp` Legacy[​](#anyscale-workspace-cp-legacy "Direct link to anyscale-workspace-cp-legacy")

Limited support

This command is not actively maintained. Use with caution.

**Usage**

`anyscale workspace cp [OPTIONS] REMOTE_PATH LOCAL_PATH`

Copy a file or a directory from workspace to local file system.

Examples

anyscale workspace cp /mnt/shared\_objects/foo.py /tmp/copy\_of\_foo.py

anyscale workspace cp "\~/default/README.md" \~/Downlaods

anyscale workspace cp "/tmp/" \~/Downlaods

**Options**
