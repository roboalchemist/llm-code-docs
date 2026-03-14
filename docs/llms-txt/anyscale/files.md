# Source: https://docs.anyscale.com/platform/workspaces/files.md

# Files in Anyscale workspaces

[View Markdown](/platform/workspaces/files.md)

# Files in Anyscale workspaces

Anyscale workspaces persist files and folders within your project directory across restarts. When you restart an Anyscale workspace, Anyscale injects the files using the `working_dir` option and makes them visible to your Ray application using the path `/home/ray/default`. This capability maintains project state between workspace sessions.

Anyscale workspaces use containers to launch clusters, which isolates your files at the workspace level. See [Container-driven development on Anyscale](/development/containers.md).

When you launch a job or service from an Anyscale workspace, Anyscale injects your files into the Ray cluster. See [Local files, code, and directories in workspaces](/development/workspace-defaults.md#files).

note

You shouldn't store large amounts of data in workspace files. For data exceeding the 10 GB limit, Anyscale recommends using object storage in your cloud provider account, such as S3, Azure blob storage, or GCS. See [Storage on Anyscale](/storage.md).

## When does Anyscale snapshot file changes?[​](#snapshots "Direct link to When does Anyscale snapshot file changes?")

Whenever your Anyscale workspace restarts or terminates gracefully, Anyscale captures a snapshot of your current files during cluster termination. Workspaces that crash due to error might lose track of changes made since the last snapshot.

Snapshots only capture files under the path `/home/ray/default`, which is the default directory for your Anyscale workspace. If you install system packages or download files to locations higher in the directory structure for your workspace, Anyscale doesn't attempt to snapshot those files.

Anyscale attempts to take a periodic snapshot of your current files every five minutes. If the snapshot doesn't succeed after four minutes, Anyscale cancels the snapshot.

important

Anyscale limits snapshots to 10 GB per workspace. Periodic snapshots might begin to fail as you approach or exceed this threshold. Periodic snapshots that fail due to file size are likely to fail repeatedly, meaning that cluster termination can't persist changes to workspace files.

Anyscale sets a more forgiving timeout for workspace termination snapshots, but exceeding the size capacity for workspace files can also cause workspace termination snapshots to fail.

The following error message indicates you're experiencing size-based failures:

> The workspace has failed to snapshot your files. Terminating the workspace might lead to loss of edits to workspace files. If you are currently storing data files in workspace files, this might lead to data loss. Large files or exceeding the 10 GB limit for workspace files can lead to snapshot failure. Identify large files and move them to the shared storage or object storage, or ignore them by adding them to .anyscaleignore. For more information about workspace file management and limitations, see the workspace files documentation. If problems persist, contact <support@anyscale.com>.

## Exclude files from your working directory[​](#exclude-files "Direct link to Exclude files from your working directory")

Anyscale uses the `.gitignore` and `.anyscaleignore` files to exclude files from the working directory.

The following default behaviors occur for all files specified in the ignore files:

* Anyscale doesn't persist ignored files between workspace restarts.
* Anyscale doesn't include ignored files when submitting jobs and services from a workspace.
* Jobs and services also respect behaviors and settings for ignoring files when using the `working_dir` option for the CLI or SDK.

### Exclude files with `.gitignore`[​](#exclude-files-with-gitignore "Direct link to exclude-files-with-gitignore")

The `.gitignore` file excludes files from Git tracking. Anyscale also ignores these files between workspace sessions and when submitting directories of files using the `working_dir` option.

To override this behavior and include files excluded by `.gitignore` in your Anyscale clusters, set the environment variable `ANYSCALE_DISABLE_GITIGNORE_EXCLUSION=1`. This setting doesn't impact files ignored by the `.anyscaleignore` file.

note

An Anyscale workspace might include multiple Git repositories, each with their own `.gitignore` files. Anyscale applies override behavior across all directories in the workspace or `working_dir`.

### Exclude files with `.anyscaleignore`[​](#exclude-files-with-anyscaleignore "Direct link to exclude-files-with-anyscaleignore")

The `.anyscaleignore` file excludes files and folders from persistence between workspace sessions and inclusion when using the `working_dir` option. Anyscale looks for this file in the top level of your workspace directory or the directory specified in the `working_dir` path. This location maps to `/home/ray/default/.anyscaleignore` in your Ray cluster.

The `.anyscaleignore` file supports the following patterns to match files and folders:

```
# .anyscaleignore example
*.txt                  # Ignore files with a .txt extension at the same level as `.anyscaleignore`.
**/*.txt               # Ignore files with a .txt extension in ANY directory.
folder/                # Ignore all files under "folder/". The slash at the end is optional.
folder/*.txt           # Ignore files with a .txt extension under "folder/".
path/to/filename.py    # Ignore a specific file by providing its relative path.
file_[1,2].txt         # Ignore file_1.txt and file_2.txt.
```

warning

The `.anyscaleignore` file supports a subset of patterns from `.gitignore` syntax and has some behavior difference. For example:

* It doesn't support some patterns, such as negation and `\` escaping.
* Star matching (for example, `*.txt`) only matches files at the same level as `.anyscaleignore`. You must specify relative directories to exclude additional files.

See the [Git docs on gitignore](https://git-scm.com/docs/gitignore).
