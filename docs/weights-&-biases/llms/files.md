# Source: https://docs.wandb.ai/models/ref/python/public-api/files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Files

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/apis/public/files.py" />

## <kbd>class</kbd> `Files`

A lazy iterator over a collection of `File` objects.

Access and manage files uploaded to W\&B during a run. Handles pagination automatically when iterating through large collections of files.

**Example:**

```python  theme={null}
from wandb.apis.public.files import Files
from wandb.apis.public.api import Api

# Example run object
run = Api().run("entity/project/run-id")

# Create a Files object to iterate over files in the run
files = Files(api.client, run)

# Iterate over files
for file in files:
    print(file.name)
    print(file.url)
    print(file.size)

    # Download the file
    file.download(root="download_directory", replace=True)
```

### <kbd>method</kbd> `Files.__init__`

```python  theme={null}
__init__(
    client: 'RetryingClient',
    run: 'Run',
    names: 'list[str] | None' = None,
    per_page: 'int' = 50,
    upload: 'bool' = False,
    pattern: 'str | None' = None
)
```

Initialize a lazy iterator over a collection of `File` objects.

Files are retrieved in pages from the W\&B server as needed.

**Args:**

* `client`:  The run object that contains the files
* `run`:  The run object that contains the files
* `names` (list, optional):  A list of file names to filter the files
* `per_page` (int, optional):  The number of files to fetch per page
* `upload` (bool, optional):  If `True`, fetch the upload URL for each file
* `pattern` (str, optional):  Pattern to match when returning files from W\&B  This pattern uses mySQL's LIKE syntax,  so matching all files that end with .json would be "%.json".  If both names and pattern are provided, a ValueError will be raised.

***

### <kbd>property</kbd> Files.length

***
