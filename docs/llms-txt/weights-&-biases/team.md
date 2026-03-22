# Source: https://docs.wandb.ai/models/ref/python/public-api/team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Team

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/apis/public/teams.py" />

## <kbd>class</kbd> `Team`

A class that represents a W\&B team.

This class provides methods to manage W\&B teams, including creating teams, inviting members, and managing service accounts. It inherits from Attrs to handle team attributes.

### <kbd>method</kbd> `Team.__init__`

```python  theme={null}
__init__(
    client: 'RetryingClient',
    name: 'str',
    attrs: 'Mapping[str, Any] | None' = None
)
```

**Args:**

* `client` (`wandb.apis.public.Api`):  The api instance to use
* `name` (str):  The name of the team
* `attrs` (dict):  Optional dictionary of team attributes

**Note:**

> Team management requires appropriate permissions.

***

### <kbd>classmethod</kbd> `Team.create`

```python  theme={null}
create(api: 'Api', team: 'str', admin_username: 'str | None' = None) → Self
```

Create a new team.

**Args:**

* `api`:  (`Api`) The api instance to use
* `team`:  (str) The name of the team
* `admin_username`:  (str) optional username of the admin user of the team, defaults to the current user.

**Returns:**
A `Team` object

***

### <kbd>method</kbd> `Team.create_service_account`

```python  theme={null}
create_service_account(description: 'str') → Member | None
```

Create a service account for the team.

**Args:**

* `description`:  (str) A description for this service account

**Returns:**
The service account `Member` object, or None on failure

***

### <kbd>method</kbd> `Team.invite`

```python  theme={null}
invite(username_or_email: 'str', admin: 'bool' = False) → bool
```

Invite a user to a team.

**Args:**

* `username_or_email`:  (str) The username or email address of the user  you want to invite.
* `admin`:  (bool) Whether to make this user a team admin.  Defaults to `False`.

**Returns:**
`True` on success, `False` if user was already invited or didn't exist.

***
