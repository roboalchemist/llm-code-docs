# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/functions/login.md

# Source: https://docs.wandb.ai/models/ref/python/functions/login.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# login()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/sdk/wandb_login.py" />

### <kbd>function</kbd> `login`

```python  theme={null}
login(
    key: 'str | None' = None,
    relogin: 'bool | None' = None,
    host: 'str | None' = None,
    force: 'bool | None' = None,
    timeout: 'int | None' = None,
    verify: 'bool' = False,
    referrer: 'str | None' = None,
    anonymous: 'DoNotSet' = <object object at 0x107d3d240>
) → bool
```

Log into W\&B.

You generally don't have to use this because most W\&B methods that need authentication can log in implicitly. This is the programmatic counterpart to the `wandb login` CLI.

This updates global credentials for the session (affecting all wandb usage in the current Python process after this call) and possibly the .netrc file.

If the identity\_token\_file setting is set, like through the WANDB\_IDENTITY\_TOKEN\_FILE environment variable, then this is a no-op.

Otherwise, if an explicit API key is provided, it is used and written to the system .netrc file. If no key is provided, but the session is already authenticated, then the session key is used for verification (if verify is True) and the .netrc file is not updated.

If none of the above is true, then this gets the API key from the first of:

* The WANDB\_API\_KEY environment variable
* The api\_key setting in a system or workspace settings file
* The .netrc file (either \~/.netrc, \~/\_netrc or the path specified by the  NETRC environment variable)
* An interactive prompt (if available)

**Args:**

* `key`:  The API key to use.
* `relogin`:  If true, get the API key from an interactive prompt, skipping  reading .netrc, environment variables, etc.
* `host`:  The W\&B server URL to connect to.
* `force`:  If true, disallows selecting offline mode in the interactive  prompt.
* `timeout`:  Number of seconds to wait for user input in the interactive  prompt. This can be used as a failsafe if an interactive prompt  is incorrectly shown in a non-interactive environment.
* `verify`:  Verify the credentials with the W\&B server and raise an  AuthenticationError on failure.
* `referrer`:  The referrer to use in the URL login request for analytics.

**Returns:**

* `bool`:  If `key` is configured.

**Raises:**

* `AuthenticationError`:  If `api_key` fails verification with the server.
* `UsageError`:  If `api_key` cannot be configured and no tty.
