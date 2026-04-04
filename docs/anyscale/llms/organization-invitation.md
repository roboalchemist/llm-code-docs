# Source: https://docs.anyscale.com/reference/organization-invitation.md

# Organization Invitation API Reference

[View Markdown](/reference/organization-invitation.md)

# Organization Invitation API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Organization Invitation CLI[​](#organization-invitation-cli "Direct link to Organization Invitation CLI")

### `anyscale organization-invitation create`[​](#anyscale-organization-invitation-create "Direct link to anyscale-organization-invitation-create")

**Usage**

`anyscale organization-invitation create [OPTIONS]`

Creates organization invitations for the provided emails.

**Options**

* **`--emails`**: The emails to send the organization invitations to. Delimited by commas.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
$ anyscale organization-invitation create --emails test1@anyscale.com,test2@anyscale.com
(anyscale +0.5s) Creating organization invitations...
(anyscale +1.7s) Organization invitations sent to: test1@anyscale.com, test2@anyscale.com
```

### `anyscale organization-invitation list`[​](#anyscale-organization-invitation-list "Direct link to anyscale-organization-invitation-list")

**Usage**

`anyscale organization-invitation list [OPTIONS]`

Lists organization invitations.

**Options**

#### Examples[​](#examples-1 "Direct link to Examples")

* CLI

```
$ anyscale organization-invitation list
ID             Email              Created At           Expires At
-------------  -----------------  -------------------  -------------------
orginv_abcedf  test@anyscale.com  11/25/2024 10:24 PM  12/02/2024 10:24 PM
```

### `anyscale organization-invitation delete`[​](#anyscale-organization-invitation-delete "Direct link to anyscale-organization-invitation-delete")

**Usage**

`anyscale organization-invitation delete [OPTIONS]`

Deletes an organization invitation.

**Options**

* **`--email`**: The email of the organization invitation to delete.

#### Examples[​](#examples-2 "Direct link to Examples")

* CLI

```
$ anyscale organization-invitation delete --email test@anyscale.com
(anyscale +0.6s) Organization invitation for test@anyscale.com deleted.
```

## Organization Invitation SDK[​](#organization-invitation-sdk "Direct link to Organization Invitation SDK")

### `anyscale.organization-invitation.create`[​](#anyscaleorganization-invitationcreate "Direct link to anyscaleorganization-invitationcreate")

Creates organization invitations for the provided emails.

Returns a tuple of successful emails and error messages.

**Arguments**

* **`emails` (List\[str])**: The emails to send the organization invitations to.

**Returns**: Tuple\[List\[str], List\[str]]

#### Examples[​](#examples-3 "Direct link to Examples")

* Python

```
import anyscale

anyscale.organization_invitation.create(emails=["test1@anyscale.com","test2@anyscale.com"])
```

### `anyscale.organization-invitation.list`[​](#anyscaleorganization-invitationlist "Direct link to anyscaleorganization-invitationlist")

Lists organization invitations.

Returns a list of organization invitations.

**Arguments**

**Returns**: List\[[OrganizationInvitation](/reference/organization-invitation.md#organizationinvitation)]

#### Examples[​](#examples-4 "Direct link to Examples")

* Python

```
import anyscale

anyscale.organization_invitation.list()
```

### `anyscale.organization-invitation.delete`[​](#anyscaleorganization-invitationdelete "Direct link to anyscaleorganization-invitationdelete")

Deletes an organization invitation.

Returns the email of the deleted organization invitation.

**Arguments**

* **`email` (str)**: The email of the organization invitation to delete.

**Returns**: str

#### Examples[​](#examples-5 "Direct link to Examples")

* Python

```
import anyscale

anyscale.organization_invitation.delete(email="test@anyscale.com")
```

## Organization Invitation Models[​](#organization-invitation-models "Direct link to Organization Invitation Models")

### `OrganizationInvitation`[​](#organizationinvitation "Direct link to organizationinvitation")

Organization invitation model.

#### Fields[​](#fields "Direct link to Fields")

* **`id` (str)**: ID of the organization invitation.
* **`email` (str)**: Email of the organization invitation.
* **`created_at` (datetime)**: Creation time of the organization invitation.
* **`expires_at` (datetime)**: Expiration time of the organization invitation.

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-6 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.organization_invitation.models import OrganizationInvitation

organization_invitations: List[OrganizationInvitation] = anyscale.organization_invitation.list()
```
