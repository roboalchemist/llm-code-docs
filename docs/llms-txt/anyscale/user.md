# Source: https://docs.anyscale.com/reference/user.md

# User API Reference

[View Markdown](/reference/user.md)

# User API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## User CLI[​](#user-cli "Direct link to User CLI")

### `anyscale user batch-create`[​](#anyscale-user-batch-create "Direct link to anyscale-user-batch-create")

**Usage**

`anyscale user batch-create [OPTIONS]`

Batch create, as an admin, users without email verification.

**Options**

* **`--users-file/-f`**: Path to a YAML file that contains the information for user accounts to be created.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
$ anyscale user batch-create --users-file users.yaml
(anyscale +0.5s) Creating users...
(anyscale +0.8s) 2 users created.

$ cat users_file.yaml
create_users:
  - name: name1
    email: test1@anyscale.com
    password: ''
    is_sso_user: false
    lastname: lastname1
    title: title1
  - name: name2
    email: test2@anyscale.com
    password: ''
    is_sso_user: false
    lastname: lastname2
    title: title2
```

### `anyscale user list`[​](#anyscale-user-list "Direct link to anyscale-user-list")

**Usage**

`anyscale user list [OPTIONS]`

List users within your organization.

**Options**

* **`--email`**: Filter users by email.
* **`--name`**: Filter users by display name.
* **`--collaborator-type`**: Filter users by collaborator type.
* **`--service-account`**: Only show service accounts.
* **`--user-account`**: Only show user accounts (non-service accounts).
* **`--max-items`**: Maximum number of users to display when running non-interactively.
* **`--page-size`**: Items per page (max 50).
* **`--json/--no-json`**: Render output as JSON instead of a table.
* **`--interactive/--no-interactive`**: Enable or disable interactive pagination.

#### Examples[​](#examples-1 "Direct link to Examples")

* CLI

```
$ anyscale user list --page-size 5 --no-interactive
Output
USERS:
EMAIL                ID         NAME         ROLE         CREATED AT
owner@anyscale.com   usr_owner  Owner Name   owner        2024-01-01 12:00
service@anyscale.com           Service Bot  collaborator 2024-02-01 08:30
```

### `anyscale user get`[​](#anyscale-user-get "Direct link to anyscale-user-get")

**Usage**

`anyscale user get [OPTIONS]`

Get details for a single user in your organization.

**Options**

* **`--email`**: Email address of the user.
* **`--name`**: Display name of the user.
* **`--collaborator-type`**: Optional collaborator type constraint.
* **`--service-account`**: Restrict to service accounts.
* **`--user-account`**: Restrict to individual user accounts.
* **`--json/--no-json`**: Output JSON instead of YAML.

#### Examples[​](#examples-2 "Direct link to Examples")

* CLI

```
$ anyscale user get --email owner@anyscale.com --json
Output
{
  "name": "Owner Name",
  "email": "owner@anyscale.com",
  "created_at": "2024-01-01T12:00:00+00:00",
  "permission_level": "owner",
  "user_id": "usr_owner"
}
```

### `anyscale user list-permissions`[​](#anyscale-user-list-permissions "Direct link to anyscale-user-list-permissions")

**Usage**

`anyscale user list-permissions [OPTIONS]`

List users and their effective cloud/project permissions across the organization.

Shows each user's access to clouds and projects, combining both individually granted permissions and permissions inherited from user groups. Also lists the current organization owners.

Output is JSON. Use --output to save to a file.

**Options**

* **`--user-id`**: Filter to a specific user ID. If not provided, lists permissions for all users.
* **`--output/-o`**: Write JSON output to a file instead of stdout.

#### Examples[​](#examples-3 "Direct link to Examples")

* CLI

```
# List all users' effective cloud & project permissions
$ anyscale user list-permissions
(anyscale +0.6s) Listing users and their effective permissions...
{
  "organization_id": "org_p72",
  "org_owners": [
    {
      "user_email": "admin1@p72.com",
      "user_id": "usr_aaa"
    }
  ],
  "users": [
    {
      "clouds": [
        {
          "cloud_id": "cld_111",
          "cloud_name": "prod-cloud",
          "role": "collaborator",
          "projects": [
            {
              "project_id": "prj_111",
              "project_name": "prod-project",
              "role": "readonly"
            }
          ]
        }
      ],
      "user_email": "alice@p72.com",
      "user_id": "usr_abc"
    }
  ]
}

# List permissions for a specific user
$ anyscale user list-permissions --user-id usr_abc
(anyscale +0.4s) Listing users and their effective permissions...
{
  "organization_id": "org_p72",
  "org_owners": [
    {
      "user_email": "admin1@p72.com",
      "user_id": "usr_aaa"
    }
  ],
  "users": [
    {
      "clouds": [
        {
          "cloud_id": "cld_111",
          "cloud_name": "prod-cloud",
          "role": "collaborator"
        }
      ],
      "user_email": "alice@p72.com",
      "user_id": "usr_abc"
    }
  ]
}
```

## User SDK[​](#user-sdk "Direct link to User SDK")

### `anyscale.user.admin_batch_create`[​](#anyscaleuseradmin_batch_create "Direct link to anyscaleuseradmin_batch_create")

Batch create, as an admin, users without email verification.

**Arguments**

* **`admin_create_users` (List\[[AdminCreateUser](/reference/user.md#admincreateuser)])**: Users to be created by an admin.

**Returns**: List\[[AdminCreatedUser](/reference/user.md#admincreateduser)]

#### Examples[​](#examples-4 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.user.models import AdminCreateUser

anyscale.user.admin_batch_create(
    [AdminCreateUser(
        name="name",
        email="test@anyscale.com",
        password="",
        is_sso_user=False,
        lastname="lastname",
        title="title",
    ),],
)
```

### `anyscale.user.list`[​](#anyscaleuserlist "Direct link to anyscaleuserlist")

List collaborators within the organization.

**Arguments**

* **`email` (str | None) = None**: Filter collaborators by exact email address.
* **`name` (str | None) = None**: Filter collaborators by exact display name.
* **`collaborator_type` (str | None) = None**: Filter by collaborator type. Accepts values such as 'all\_accounts', 'only\_service\_accounts', or 'only\_user\_accounts'.
* **`is_service_account` (bool | None) = None**: If provided, filter collaborators by whether they are service accounts.
* **`max_items` (int | None) = None**: Maximum total number of users to yield (default: iterate all).
* **`page_size` (int | None) = None**: Number of users fetched per API request (default: API default).

**Returns**: ResultIterator\[[User](/reference/user.md#user)]

#### Examples[​](#examples-5 "Direct link to Examples")

* Python

```
import anyscale

for user in anyscale.user.list(max_items=10):
    print(user.email)
```

### `anyscale.user.get`[​](#anyscaleuserget "Direct link to anyscaleuserget")

Retrieve a single collaborator by email or name.

**Arguments**

* **`email` (str | None) = None**: Email address of the user to retrieve.
* **`name` (str | None) = None**: Display name of the user to retrieve.
* **`collaborator_type` (str | None) = None**: Optional collaborator type constraint when fetching the user.
* **`is_service_account` (bool | None) = None**: Filter by whether the user is a service account.

**Returns**: [User](/reference/user.md#user)

#### Examples[​](#examples-6 "Direct link to Examples")

* Python

```
import anyscale

user = anyscale.user.get(email="owner@anyscale.com")
print(user.permission_level)
```

## User Models[​](#user-models "Direct link to User Models")

### `AdminCreateUser`[​](#admincreateuser "Direct link to admincreateuser")

User to be created by an admin.

#### Fields[​](#fields "Direct link to Fields")

* **`name` (str)**: First name of the user to be created.
* **`email` (str)**: Email of the user to be created.
* **`password` (str | None)**: Password for the user account being created.
* **`is_sso_user` (bool)**: Whether the user is an SSO user. SSO users can log in using SSO.
* **`lastname` (str | None)**: Optional last name of the user to be created.
* **`title` (str | None)**: Optional title of the user to be created.

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-7 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.user.models import AdminCreateUser

admin_create_user = AdminCreateUser(
    # First name of the user to be created.
    name="name",
    # Email of the user to be created.
    email="test@anyscale.com",
    # Password for the user account being created.
    password="",
    # Whether the user is an SSO user. SSO users can log in using SSO.
    is_sso_user=False,
    # Optional last name of the user to be created.
    lastname="lastname",
    # Optional title of the user to be created.
    title="title",
)
```

### `AdminCreateUsers`[​](#admincreateusers "Direct link to admincreateusers")

Users to be created by an admin.

#### Fields[​](#fields-1 "Direct link to Fields")

* **`create_users` (List\[Dict\[str, Any]])**: Users to be created by an admin.

#### Python Methods[​](#python-methods-1 "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-8 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.user.models import AdminCreateUser

admin_create_user = AdminCreateUser(
    # First name of the user to be created.
    name="name",
    # Email of the user to be created.
    email="test@anyscale.com",
    # Password for the user account being created.
    password="",
    # Whether the user is an SSO user. SSO users can log in using SSO.
    is_sso_user=False,
    # Optional last name of the user to be created.
    lastname="lastname",
    # Optional title of the user to be created.
    title="title",
)
admin_create_users = AdminCreateUsers(
    # Users to be created by an admin.
    create_users=[admin_create_user]
)
```

### `AdminCreatedUser`[​](#admincreateduser "Direct link to admincreateduser")

User account created by an admin that has organization collaborator permissions.

#### Fields[​](#fields-2 "Direct link to Fields")

* **`user_id` (str)**: ID of the user that has been created.
* **`name` (str)**: First name of the user that has been created.
* **`email` (str)**: Email of the user that has been created.
* **`created_at` (datetime)**: The timestamp of when the user is created.
* **`is_sso_user` (bool)**: Whether the user is an SSO user. SSO users can log in using SSO.
* **`lastname` (str | None)**: Optional last name of the user that has been created.
* **`title` (str | None)**: Optional title of the user that has been created.

#### Python Methods[​](#python-methods-2 "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-9 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.user.models import AdminCreatedUser

admin_create_user = AdminCreateUser(
    # First name of the user to be created.
    name="name",
    # Email of the user to be created.
    email="test@anyscale.com",
    # Password for the user account being created.
    password="",
    # Whether the user is an SSO user. SSO users can log in using SSO.
    is_sso_user=False,
    # Optional last name of the user to be created.
    lastname="lastname",
    # Optional title of the user to be created.
    title="title",
)
admin_created_users: List[AdminCreatedUser] = anyscale.user.admin_batch_create([admin_create_user])
```

### `User`[​](#user "Direct link to user")

Collaborator returned by `anyscale.user` APIs.

#### Fields[​](#fields-3 "Direct link to Fields")

* **`email` (str)**: Email address associated with the collaborator.
* **`name` (str)**: Display name of the collaborator.
* **`created_at` (datetime)**: Timestamp for when the collaborator was created.
* **`permission_level` (str)**: Organization permission level for the collaborator.
* **`user_id` (str | None)**: Optional user ID backing the collaborator (may be absent for service accounts).

#### Python Methods[​](#python-methods-3 "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-10 "Direct link to Examples")

* Python

```
import anyscale

for user in anyscale.user.list(max_items=5):
    print(f"{user.email} ({user.permission_level})")
```
