# Source: https://docs.anyscale.com/reference/policy.md

# Policy API Reference

[View Markdown](/reference/policy.md)

# Policy API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Policy CLI[​](#policy-cli "Direct link to Policy CLI")

### `anyscale policy set` Beta[​](#anyscale-policy-set-beta "Direct link to anyscale-policy-set-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale policy set [OPTIONS]`

Set user group permission policy for a resource.

The config file should be in YAML format with bindings list.

For organization policies, --resource-id cannot be specified, the policy will be set for your current organization automatically.

Example policy.yaml:

 bindings:

* role\_name: collaborator principals:
  <!-- -->
  * ug\_abc123

* role\_name: readonly principals:

  <!-- -->

  * ug\_def456
  * ug\_ghi789

Valid role\_name values:

 Cloud: collaborator, readonly Project: owner, collaborator, readonly Organization: owner, collaborator

**Options**

* **`--resource-type`**: Resource type ('cloud', 'project', or 'organization').
* **`--resource-id`**: Resource ID (e.g., cld\_abc123, prj\_xyz789). Required for 'cloud' and 'project' types, not allowed for 'organization'.
* **`-f/--config-file`**: Path to a YAML config file with policy bindings.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
# Set policy for a cloud
$ anyscale policy set --resource-type cloud --resource-id cld_abc123 -f policy.yaml
(anyscale +0.5s) Setting policy for cloud cld_abc123...
(anyscale +1.2s) Policy for cloud cld_abc123 has been updated.

# Set policy for your organization (--resource-id is not allowed)
$ anyscale policy set --resource-type organization -f org_policy.yaml
(anyscale +0.5s) Setting policy for organization your organization...
(anyscale +1.2s) Policy for organization your organization has been updated.

$ cat policy.yaml
bindings:
  - role_name: collaborator
    principals:
      - ug_abc123
  - role_name: readonly
    principals:
      - ug_def456
      - ug_ghi789
```

### `anyscale policy get` Beta[​](#anyscale-policy-get-beta "Direct link to anyscale-policy-get-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale policy get [OPTIONS]`

Get user group permission policy for a resource.

For organization policies, --resource-id cannot be specified, the policy for your current organization will be returned automatically.

**Options**

* **`--resource-type`**: Resource type ('cloud', 'project', or 'organization').
* **`--resource-id`**: Resource ID (e.g., cld\_abc123, prj\_xyz789). Required for 'cloud' and 'project' types, not allowed for 'organization'.

#### Examples[​](#examples-1 "Direct link to Examples")

* CLI

```
# Get policy for a cloud
$ anyscale policy get --resource-type cloud --resource-id cld_abc123
(anyscale +0.5s) Policy for cloud cld_abc123:
Role      Principal (User Group ID)  Process Status
--------  -------------------------  --------------
collaborator  ug_abc123              success
readonly  ug_def456                  success
readonly  ug_ghi789                  success

# Get policy for your organization (--resource-id is not allowed)
$ anyscale policy get --resource-type organization
(anyscale +0.5s) Policy for organization your organization:
Role      Principal (User Group ID)  Process Status
--------  -------------------------  --------------
owner     ug_admins                  success
collaborator  ug_developers          success
```

### `anyscale policy list` Beta[​](#anyscale-policy-list-beta "Direct link to anyscale-policy-list-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale policy list [OPTIONS]`

List permission policies for all resources of a specific type.

Only shows resources that have bindings configured.

**Options**

* **`--resource-type`**: Resource type to list policies for ('cloud' or 'project').

#### Examples[​](#examples-2 "Direct link to Examples")

* CLI

```
$ anyscale policy list --resource-type cloud
(anyscale +0.6s) cloud: cld_abc123
Role      Principal (User Group ID)  Process Status
--------  -------------------------  --------------
collaborator  ug_abc123              success
readonly  ug_def456                  success

(anyscale +0.6s) cloud: cld_xyz789
Role      Principal (User Group ID)  Process Status
--------  -------------------------  --------------
collaborator  ug_ghi789              pending
```

## Policy SDK[​](#policy-sdk "Direct link to Policy SDK")

### `anyscale.policy.set`[​](#anyscalepolicyset "Direct link to anyscalepolicyset")

Set user group permission policy for a resource.

For organization policies, resource\_id cannot be specified, the policy will be set for your current organization automatically.

Valid role\_name values by resource type:

**Cloud**:

* `collaborator`: Read/write access (create, read, update, delete)
* `readonly`: Read-only access

**Project**:

* `collaborator`: Read/write access (create, read, update)
* `readonly`: Read-only access

**Organization**:

* `owner`: Full control (write + collaborator management)
* `collaborator`: Read/write access to organization resources

**Arguments**

* **`resource_type` (str)**: Resource type ('cloud', 'project', or 'organization').
* **`config` ([PolicyConfig](/reference/policy.md#policyconfig))**: Policy configuration with role bindings.
* **`resource_id` (str | None) = None**: Resource ID (e.g., cld\_abc123, prj\_xyz789). Required for 'cloud' and 'project' types, not allowed for 'organization'.

#### Examples[​](#examples-3 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.policy.models import PolicyConfig, PolicyBinding

# Set policy for a cloud
policy_config = PolicyConfig(
    bindings=[
        PolicyBinding(role_name="collaborator", principals=["ug_abc123"]),
        PolicyBinding(role_name="readonly", principals=["ug_def456", "ug_ghi789"]),
    ]
)
anyscale.policy.set(
    resource_type="cloud",
    resource_id="cld_abc123",
    config=policy_config,
)

# Set policy for your organization (no resource_id needed)
org_policy = PolicyConfig(
    bindings=[
        PolicyBinding(role_name="owner", principals=["ug_admins"]),
        PolicyBinding(role_name="collaborator", principals=["ug_developers"]),
    ]
)
anyscale.policy.set(
    resource_type="organization",
    config=org_policy,
)
```

### `anyscale.policy.get`[​](#anyscalepolicyget "Direct link to anyscalepolicyget")

Get user group permission policy for a resource.

For organization policies, resource\_id cannot be specified, the policy for your current organization will be returned automatically.

Returns a Policy object with role bindings.

**Arguments**

* **`resource_type` (str)**: Resource type ('cloud', 'project', or 'organization').
* **`resource_id` (str | None) = None**: Resource ID (e.g., cld\_abc123, prj\_xyz789). Required for 'cloud' and 'project' types, not allowed for 'organization'.

**Returns**: [Policy](/reference/policy.md#policy)

#### Examples[​](#examples-4 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.policy.models import Policy

# Get policy for a cloud
policy = anyscale.policy.get(resource_type="cloud", resource_id="cld_abc123")
for binding in policy.bindings:
    print(f"{binding.role_name}: {binding.principals}")

# Get policy for your organization (no resource_id needed)
org_policy = anyscale.policy.get(resource_type="organization")
for binding in org_policy.bindings:
    print(f"{binding.role_name}: {binding.principals}")
```

### `anyscale.policy.list`[​](#anyscalepolicylist "Direct link to anyscalepolicylist")

List permission policies for all resources of a specific type.

Returns a list of ResourcePolicy objects.

**Arguments**

* **`resource_type` (str)**: Resource type to list policies for ('cloud' or 'project').

**Returns**: List\[[ResourcePolicy](/reference/policy.md#resourcepolicy)]

#### Examples[​](#examples-5 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.policy.models import ResourcePolicy

policies = anyscale.policy.list(resource_type="cloud")
for policy in policies:
    print(f"{policy.resource_id}: {policy.bindings}")
```

## Policy Models[​](#policy-models "Direct link to Policy Models")

### `Policy`[​](#policy "Direct link to policy")

Policy model representing the policy for a single resource.

#### Fields[​](#fields "Direct link to Fields")

* **`bindings` (List\[[PolicyBinding](/reference/policy.md#policybinding)])**: List of role bindings for the policy.
* **`sync_status` ([PolicySyncStatus](/reference/policy.md#policysyncstatus))**: Sync status of the policy (pending, success, or failed).

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-6 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.policy.models import Policy

policy = anyscale.policy.get(resource_type="cloud", resource_id="cld_abc123")
print(f"Sync status: {policy.sync_status}")
for binding in policy.bindings:
    print(f"{binding.role_name}: {binding.principals}")
```

### `PolicyBinding`[​](#policybinding "Direct link to policybinding")

A binding of a role to a list of principals (user group IDs).

#### Fields[​](#fields-1 "Direct link to Fields")

* **`role_name` (str)**: The role name. For cloud/project policies use 'collaborator' or 'readonly'. For organization policies use 'owner' or 'collaborator'.
* **`principals` (List\[str])**: List of user group IDs that have this role.

#### Python Methods[​](#python-methods-1 "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-7 "Direct link to Examples")

* Python

```
from anyscale.policy.models import PolicyBinding

binding = PolicyBinding(role_name="collaborator", principals=["ug_abc123"])
```

### `PolicyConfig`[​](#policyconfig "Direct link to policyconfig")

Policy configuration with role bindings.

#### Fields[​](#fields-2 "Direct link to Fields")

* **`bindings` (List\[[PolicyBinding](/reference/policy.md#policybinding)])**: List of role bindings for the policy.

#### Python Methods[​](#python-methods-2 "Direct link to Python Methods")

```
def __init__(self, **fields) -> PolicyConfig
    """Construct a model with the provided field values set."""

def options(self, **fields) -> PolicyConfig
    """Return a copy of the model with the provided field values overwritten."""

def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-8 "Direct link to Examples")

* YAML
* Python

```
bindings:
  - role_name: collaborator
    principals:
      - ug_abc123
  - role_name: readonly
    principals:
      - ug_def456
      - ug_ghi789
```

```
from anyscale.policy.models import PolicyBinding, PolicyConfig

config = PolicyConfig(
    bindings=[
        PolicyBinding(role_name="collaborator", principals=["ug_abc123"]),
        PolicyBinding(role_name="readonly", principals=["ug_def456", "ug_ghi789"]),
    ]
)
```

### `PolicySyncStatus`[​](#policysyncstatus "Direct link to policysyncstatus")

Sync status for resource permission policies.

#### Values[​](#values "Direct link to Values")

* **`pending`**: Policy is pending synchronization.
* **`success`**: Policy has been successfully synchronized.
* **`failed`**: Policy synchronization has failed.

### `ResourcePolicy`[​](#resourcepolicy "Direct link to resourcepolicy")

Resource policy model representing permissions for a resource.

#### Fields[​](#fields-3 "Direct link to Fields")

* **`resource_id` (str)**: The ID of the resource.
* **`resource_type` (str)**: The type of the resource (e.g., 'cloud', 'project').
* **`bindings` (List\[[PolicyBinding](/reference/policy.md#policybinding)])**: List of role bindings for the policy.
* **`sync_status` ([PolicySyncStatus](/reference/policy.md#policysyncstatus))**: Sync status of the policy (pending, success, or failed).

#### Python Methods[​](#python-methods-3 "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-9 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.policy.models import ResourcePolicy

policies = anyscale.policy.list(resource_type="cloud")
for policy in policies:
    print(f"{policy.resource_id}: {policy.bindings} (sync_status: {policy.sync_status})")
```
