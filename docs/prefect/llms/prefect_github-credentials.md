# Source: https://docs.prefect.io/integrations/prefect-github/api-ref/prefect_github-credentials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# credentials

# `prefect_github.credentials`

Credential classes used to perform authenticated interactions with GitHub

## Classes

### `GitHubCredentials` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-github/prefect_github/credentials.py#L12" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Block used to manage GitHub authentication.

**Attributes:**

* `token`: the token to authenticate into GitHub.

**Examples:**

Load stored GitHub credentials:

```python  theme={null}
from prefect_github import GitHubCredentials
github_credentials_block = GitHubCredentials.load("BLOCK_NAME")
```

**Methods:**

#### `format_git_credentials` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-github/prefect_github/credentials.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
format_git_credentials(self, url: str) -> str
```

Format and return the full git URL with GitHub credentials embedded.

GitHub uses plain token format without any prefix.

**Args:**

* `url`: Repository URL (e.g., "[https://github.com/org/repo.git](https://github.com/org/repo.git)")

**Returns:**

* Complete URL with credentials embedded

**Raises:**

* `ValueError`: If token is not configured

#### `get_client` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-github/prefect_github/credentials.py#L58" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_client(self) -> HTTPEndpoint
```

Gets an authenticated GitHub GraphQL HTTPEndpoint client.

**Returns:**

* An authenticated GitHub GraphQL HTTPEndpoint client.


Built with [Mintlify](https://mintlify.com).