# Source: https://docs.wandb.ai/models/ref/python/functions/restore.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# restore()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/sdk/wandb_run.py" />

### <kbd>function</kbd> `restore`

```python  theme={null}
restore(
    name: 'str',
    run_path: 'str | None' = None,
    replace: 'bool' = False,
    root: 'str | None' = None
) → None | TextIO
```

Download the specified file from cloud storage.

File is placed into the current directory or run directory. By default, will only download the file if it doesn't already exist.

**Args:**

* `name`:  The name of the file.
* `run_path`:  Optional path to a run to pull files from, i.e. `username/project_name/run_id`  if wandb.init has not been called, this is required.
* `replace`:  Whether to download the file even if it already exists locally
* `root`:  The directory to download the file to.  Defaults to the current  directory or the run directory if wandb.init was called.

**Returns:**
None if it can't find the file, otherwise a file object open for reading.

**Raises:**

* `CommError`:  If W\&B can't connect to the W\&B backend.
* `ValueError`:  If the file is not found or can't find run\_path.
