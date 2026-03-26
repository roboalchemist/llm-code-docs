# Source: https://docs.infrahub.app/schema-library/reference/users.md

# Users

This schema extension contains models for account management.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Group[​](#group "Direct link to Group")

* **Label:** User Groups
* **Description:** User Group
* **Namespace:** User
* **Icon:** iconoir
  <!-- -->
  :group
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name          | description | kind     | optional | default\_value | choices                    |
| ------------- | ----------- | -------- | -------- | -------------- | -------------------------- |
| name          |             | Text     |          |                |                            |
| description   |             | Text     | True     |                |                            |
| idle\_timeout |             | Number   |          |                |                            |
| permissions   |             | Dropdown | False    |                | admin, operator, read-only |

### Account[​](#account "Direct link to Account")

* **Label:** User Account
* **Description:** User login and authentication
* **Namespace:** User
* **Icon:** mdi
  <!-- -->
  :account-key
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name         | description                                    | kind     | optional | default\_value | choices |
| ------------ | ---------------------------------------------- | -------- | -------- | -------------- | ------- |
| name         | The login username                             | Text     |          |                |         |
| full\_name   | Full name of the account                       | Text     | True     |                |         |
| ssh\_key     | SSH key for secure access                      | Password | True     |                |         |
| password     | Password for login (alternative to SSH key)    | Password | True     |                |         |
| mfa\_enabled | Whether multi-factor authentication is enabled | Boolean  |          | False          |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name         | peer                | optional | cardinality | kind      |
| ------------ | ------------------- | -------- | ----------- | --------- |
| user\_group  | UserGroup           | False    | one         | Attribute |
| organization | OrganizationGeneric | False    | one         | Parent    |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### OrganizationGeneric[​](#organizationgeneric "Direct link to OrganizationGeneric")

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name     | peer        | optional | cardinality | kind      |
| -------- | ----------- | -------- | ----------- | --------- |
| accounts | UserAccount |          | many        | Component |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: Group
  namespace: User
  description: User Group
  label: User Groups
  icon: iconoir:group
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  attributes:
  - name: name
    kind: Text
    order_weight: 1000
    unique: true
  - name: description
    kind: Text
    optional: true
    order_weight: 1100
  - name: idle_timeout
    label: Idle Timeout (s)
    kind: Number
    order_weight: 1300
  - name: permissions
    kind: Dropdown
    optional: false
    choices:
    - name: admin
      description: All rights on device.
      color: '#E6E6FA'
    - name: operator
      description: Operator right on configuration.
      color: '#E6E6FA'
    - name: read-only
      description: Read only right on configuration.
      color: '#E6E6FA'
    order_weight: 1200
- name: Account
  namespace: User
  description: User login and authentication
  label: User Account
  icon: mdi:account-key
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  attributes:
  - name: name
    label: Username
    kind: Text
    description: The login username
    order_weight: 1000
    unique: true
  - name: full_name
    kind: Text
    optional: true
    description: Full name of the account
    order_weight: 1100
  - name: ssh_key
    kind: Password
    optional: true
    description: SSH key for secure access
    order_weight: 1300
  - name: password
    kind: Password
    optional: true
    description: Password for login (alternative to SSH key)
    order_weight: 1400
  - name: mfa_enabled
    kind: Boolean
    default_value: false
    description: Whether multi-factor authentication is enabled
    order_weight: 1500
  relationships:
  - name: user_group
    peer: UserGroup
    cardinality: one
    optional: false
    kind: Attribute
    order_weight: 1200
  - name: organization
    peer: OrganizationGeneric
    optional: false
    cardinality: one
    kind: Parent
extensions:
  nodes:
  - kind: OrganizationGeneric
    relationships:
    - name: accounts
      kind: Component
      peer: UserAccount
      description: List of Accounts under this organization
      cardinality: many
```
