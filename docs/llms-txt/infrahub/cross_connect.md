# Source: https://docs.infrahub.app/schema-library/reference/cross_connect.md

# Cross Connect

This extension contains schema to capture Cross Connect. You can see it as "a cable operated by a provider". You will be able to attach it to a location and then connect endpoints to it (e.g. rear interface of a patch panel, circuit endpoint ...)

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### CrossConnect[​](#crossconnect "Direct link to CrossConnect")

* **Label:** Cross-Connect
* **Description:** Cross-connect between different endpoints within a datacenter.
* **Namespace:** Dcim
* **Icon:** streamline
  <!-- -->
  :arrow-crossover-right-solid
* **Display Labels:** identifier\_\_value
* **Uniqueness Constraints:**
  * identifier\_\_value, provider
* **Human Friendly ID:** provider\_\_name\_\_value, identifier\_\_value
* **Inherit From:** DcimConnector

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description | kind     | optional | default\_value | choices                      |
| ----------- | ----------- | -------- | -------- | -------------- | ---------------------------- |
| identifier  |             | Text     |          |                |                              |
| description |             | Text     | True     |                |                              |
| status      |             | Dropdown | True     |                | connected, planned, reserved |

#### Relationships[​](#relationships "Direct link to Relationships")

| name     | peer                 | optional | cardinality | kind      |
| -------- | -------------------- | -------- | ----------- | --------- |
| location | LocationHosting      | False    | one         | Attribute |
| provider | OrganizationProvider | False    | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: CrossConnect
  namespace: Dcim
  description: Cross-connect between different endpoints within a datacenter.
  label: Cross-Connect
  icon: streamline:arrow-crossover-right-solid
  inherit_from:
  - DcimConnector
  order_by:
  - provider__name__value
  display_labels:
  - identifier__value
  human_friendly_id:
  - provider__name__value
  - identifier__value
  uniqueness_constraints:
  - - identifier__value
    - provider
  attributes:
  - name: identifier
    kind: Text
    order_weight: 900
  - name: description
    kind: Text
    optional: true
    order_weight: 1300
  - name: status
    kind: Dropdown
    optional: true
    order_weight: 1200
    choices:
    - name: connected
      label: Connected
      description: Fully operational and currently in connected
      color: '#7fbf7f'
    - name: planned
      label: Planned
      description: In the process of being set up
      color: '#ffff7f'
    - name: reserved
      label: Reserved
      description: Fully connected and reserved for a future use
      color: '#9090de'
  relationships:
  - name: location
    label: Location
    peer: LocationHosting
    optional: false
    cardinality: one
    kind: Attribute
    order_weight: 1100
  - name: provider
    peer: OrganizationProvider
    optional: false
    cardinality: one
    kind: Attribute
    order_weight: 1000
```
