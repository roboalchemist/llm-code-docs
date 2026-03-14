# Source: https://docs.anyscale.com/reference/user-group.md

# User Group API Reference

[View Markdown](/reference/user-group.md)

# User Group API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## User Group CLI[​](#user-group-cli "Direct link to User Group CLI")

### `anyscale user-group list` Beta[​](#anyscale-user-group-list-beta "Direct link to anyscale-user-group-list-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale user-group list [OPTIONS]`

List user groups in the organization.

**Options**

* **`--max-items`**: Maximum number of user groups to return.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
$ anyscale user-group list --max-items 50
ID            Name
------------  ----------------
ug_abc123     Engineering
ug_def456     Data Science
ug_ghi789     Platform Team
```

### `anyscale user-group get` Beta[​](#anyscale-user-group-get-beta "Direct link to anyscale-user-group-get-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale user-group get [OPTIONS]`

Get a specific user group by ID.

**Options**

* **`--id`**: The ID of the user group to retrieve.

#### Examples[​](#examples-1 "Direct link to Examples")

* CLI

```
$ anyscale user-group get --id ug_abc123
ID               ug_abc123
Name             Engineering
Organization ID  org_abc123
Created At       2025-01-15 10:30:00 UTC
Updated At       2025-01-15 10:30:00 UTC
```

### `anyscale user-group list` Beta[​](#anyscale-user-group-list-beta-1 "Direct link to anyscale-user-group-list-beta-1")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale user-group list [OPTIONS]`

List all user groups with their members.

Shows each user group and which users are members of that group.

Output is JSON. Use --output to save to a file.

**Options**

* **`--output/-o`**: Write JSON output to a file instead of stdout.

#### Examples[​](#examples-2 "Direct link to Examples")

* CLI

```
$ anyscale user-group membership list
{
  "Engineering": [
    "alice@example.com",
    "charlie@example.com"
  ],
  "Data Science": [
    "bob@example.com"
  ]
}

# Save output to a file
$ anyscale user-group membership list --output memberships.json
```

## User Group SDK[​](#user-group-sdk "Direct link to User Group SDK")

### `anyscale.user_group.list`[​](#anyscaleuser_grouplist "Direct link to anyscaleuser_grouplist")

List user groups in the organization.

Returns a list of UserGroup objects.

**Arguments**

* **`max_items` (int) = 50**: Maximum number of user groups to return.

**Returns**: List\[[UserGroup](/reference/user-group.md#usergroup)]

#### Examples[​](#examples-3 "Direct link to Examples")

* Python

```
import anyscale

user_groups = anyscale.user_group.list(max_items=50)
for ug in user_groups:
    print(f"{ug.id}: {ug.name}")
```

### `anyscale.user_group.get`[​](#anyscaleuser_groupget "Direct link to anyscaleuser_groupget")

Get a specific user group by ID.

Returns a UserGroup object.

**Arguments**

* **`id` (str)**: The ID of the user group to retrieve.

**Returns**: [UserGroup](/reference/user-group.md#usergroup)

#### Examples[​](#examples-4 "Direct link to Examples")

* Python

```
import anyscale

user_group = anyscale.user_group.get(id="ug_abc123")
print(f"{user_group.id}: {user_group.name}")
```

## User Group Models[​](#user-group-models "Direct link to User Group Models")

### `UserGroup`[​](#usergroup "Direct link to usergroup")

A user group in the organization.

#### Fields[​](#fields "Direct link to Fields")

* **`id` (str)**: The unique identifier of the user group.
* **`name` (str)**: The name of the user group.
* **`org_id` (str)**: The organization ID.
* **`created_at` (datetime)**: When the user group was created.
* **`updated_at` (datetime)**: When the user group was last updated.

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-5 "Direct link to Examples")

* Python

```
import anyscale

user_group = anyscale.user_group.get(id="ug_abc123")
print(f"{user_group.id}: {user_group.name}")
```
