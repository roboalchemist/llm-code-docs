# Source: https://docs.anyscale.com/reference/service-account.md

# Service Account API Reference

[View Markdown](/reference/service-account.md)

# Service Account API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Service Account CLI[​](#service-account-cli "Direct link to Service Account CLI")

### `anyscale service-account create`[​](#anyscale-service-account-create "Direct link to anyscale-service-account-create")

**Usage**

`anyscale service-account create [OPTIONS]`

Create a service account.

**Options**

* **`--name/-n`**: Name for the service account.

### `anyscale service-account create-api-key`[​](#anyscale-service-account-create-api-key "Direct link to anyscale-service-account-create-api-key")

**Usage**

`anyscale service-account create-api-key [OPTIONS]`

Create a new API key for a service account.

**Options**

* **`--email`**: Email of the service account to create the new key for.
* **`--name`**: Name of the service account to create the new key for.

### `anyscale service-account list`[​](#anyscale-service-account-list "Direct link to anyscale-service-account-list")

**Usage**

`anyscale service-account list [OPTIONS]`

List service accounts.

**Options**

* **`--max-items`**: Max items to show in list.

### `anyscale service-account delete`[​](#anyscale-service-account-delete "Direct link to anyscale-service-account-delete")

**Usage**

`anyscale service-account delete [OPTIONS]`

Delete a service account.

**Options**

* **`--email`**: Email of the service account to delete.
* **`--name`**: Name of the service account to delete.

## Service Account SDK[​](#service-account-sdk "Direct link to Service Account SDK")

### `anyscale.service_account.create`[​](#anyscaleservice_accountcreate "Direct link to anyscaleservice_accountcreate")

Create a service account and return the API key.

**Arguments**

* **`name` (str)**: Name for the service account.

**Returns**: str

#### Examples[​](#examples "Direct link to Examples")

* Python

```
import anyscale

api_key = anyscale.service_account.create(
    name="my-service-account",
)
```

### `anyscale.service_account.create_api_key`[​](#anyscaleservice_accountcreate_api_key "Direct link to anyscaleservice_accountcreate_api_key")

Create an API key for the service account and return the API key.

**Arguments**

* **`email` (str | None) = None**: Email of the service account to create the new key for.
* **`name` (str | None) = None**: Name of the service account to create the new key for.

**Returns**: str

#### Examples[​](#examples-1 "Direct link to Examples")

* Python

```
import anyscale

api_key = anyscale.service_account.create_api_key(
    name="my-service-account",
)
```

### `anyscale.service_account.list`[​](#anyscaleservice_accountlist "Direct link to anyscaleservice_accountlist")

List service accounts.

**Arguments**

* **`max_items` (int) = 20**: Maximum number of items to return.

**Returns**: List\[[ServiceAccount](/reference/service-account.md#serviceaccount)]

#### Examples[​](#examples-2 "Direct link to Examples")

* Python

```
import anyscale

anyscale.service_account.list(
    max_items=20,
)
```

### `anyscale.service_account.delete`[​](#anyscaleservice_accountdelete "Direct link to anyscaleservice_accountdelete")

Delete a service account.

**Arguments**

* **`email` (str | None) = None**: Email of the service account to delete.
* **`name` (str | None) = None**: Name of the service account to delete.

#### Examples[​](#examples-3 "Direct link to Examples")

* Python

```
import anyscale

anyscale.service_account.delete(
    name="my-service-account",
)
```

## Service Account Models[​](#service-account-models "Direct link to Service Account Models")

### `ServiceAccount`[​](#serviceaccount "Direct link to serviceaccount")

Service account

#### Fields[​](#fields "Direct link to Fields")

* **`name` (str)**: Name of the service account.
* **`created_at` (datetime)**: The timestamp when this service account was created.
* **`permission_level` ([OrganizationPermissionLevel](/reference/service-account.md#organizationpermissionlevel))**: The organization permission level of the service account.
* **`email` (str)**: Email of the service account.

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-4 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.service_account.models import ServiceAccount

service_accounts: List[ServiceAccount] = anyscale.service_account.list()
```

### `OrganizationPermissionLevel`[​](#organizationpermissionlevel "Direct link to organizationpermissionlevel")

Permission levels for service accounts in an organization.

#### Values[​](#values "Direct link to Values")

* **`OWNER`**: Owner permission level for the organization
* **`COLLABORATOR`**: Collaborator permission level for the organization
