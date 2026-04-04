# Source: https://docs.wandb.ai/models/ref/query-panel/file.md

# Source: https://docs.wandb.ai/models/ref/python/public-api/file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# File

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/apis/public/files.py" />

## <kbd>class</kbd> `File`

File saved to W\&B.

Represents a single file stored in W\&B. Includes access to file metadata. Files are associated with a specific run and can include text files, model weights, datasets, visualizations, and other artifacts. You can download the file, delete the file, and access file properties.

Specify one or more attributes in a dictionary to fine a specific file logged to a specific run. You can search using the following keys:

* id (str): The ID of the run that contains the file
* name (str): Name of the file
* url (str): path to file
* direct\_url (str): path to file in the bucket
* sizeBytes (int): size of file in bytes
* md5 (str): md5 of file
* mimetype (str): mimetype of file
* updated\_at (str): timestamp of last update
* path\_uri (str): path to file in the bucket, currently only available for S3 objects and reference files

**Args:**

* `client`:  The run object that contains the file
* `attrs` (dict):  A dictionary of attributes that define the file
* `run`:  The run object that contains the file

### <kbd>property</kbd> File.path\_uri

Returns the URI path to the file in the storage bucket.

**Returns:**

* `str`:  The S3 URI (e.g., 's3://bucket/path/to/file') if the file is stored in S3,  the direct URL if it's a reference file, or an empty string if unavailable.

**Returns:**

* `str`: The path\_uri property value.

***

### <kbd>property</kbd> File.size

Returns the size of the file in bytes.

**Returns:**

* `int`: The size property value.

***

### <kbd>method</kbd> `File.delete`

```python  theme={null}
delete() → None
```

Delete the file from the W\&B server.

***

### <kbd>method</kbd> `File.download`

```python  theme={null}
download(
    root: 'str' = '.',
    replace: 'bool' = False,
    exist_ok: 'bool' = False,
    api: 'Api | None' = None
) → io.TextIOWrapper
```

Downloads a file previously saved by a run from the wandb server.

**Args:**

* `root`:  Local directory to save the file. Defaults to the  current working directory (".").
* `replace`:  If `True`, download will overwrite a local file  if it exists. Defaults to `False`.
* `exist_ok`:  If `True`, will not raise ValueError if file already  exists and will not re-download unless replace=True.  Defaults to `False`.
* `api`:  If specified, the `Api` instance used to download the file.

**Raises:**
`ValueError` if file already exists, `replace=False` and `exist_ok=False`.
