# Source: https://docs.infrahub.app/schema-library/reference/organization.md

# Organization

Basic Organization schema to capture organizations, vendors, and related information.

## Details[​](#details "Direct link to Details")

* **Dependencies:** No dependencies

## Nodes[​](#nodes "Direct link to Nodes")

### Manufacturer[​](#manufacturer "Direct link to Manufacturer")

* **Description:** Device Manufacturer
* **Namespace:** Organization
* **Icon:** mdi
  <!-- -->
  :domain
* **Inherit From:** OrganizationGeneric

#### Relationships[​](#relationships "Direct link to Relationships")

| name         | peer           | optional | cardinality | kind |
| ------------ | -------------- | -------- | ----------- | ---- |
| device\_type | DcimDeviceType | True     | many        |      |
| platform     | DcimPlatform   | True     | many        |      |

### Provider[​](#provider "Direct link to Provider")

* **Description:** Circuit or Location Provider
* **Namespace:** Organization
* **Icon:** mdi
  <!-- -->
  :domain
* **Inherit From:** OrganizationGeneric

## Generics[​](#generics "Direct link to Generics")

### Generic[​](#generic "Direct link to Generic")

* **Label:** Organization
* **Description:** An organization represent a legal entity, a company.
* **Namespace:** Organization
* **Icon:** mdi
  <!-- -->
  :domain
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text |          |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name | peer       | optional | cardinality | kind      |
| ---- | ---------- | -------- | ----------- | --------- |
| tags | BuiltinTag | True     | many        | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: Generic
  namespace: Organization
  label: Organization
  description: An organization represent a legal entity, a company.
  human_friendly_id:
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  icon: mdi:domain
  include_in_menu: true
  attributes:
  - name: name
    kind: Text
    unique: true
    order_weight: 1000
  - name: description
    kind: Text
    optional: true
    order_weight: 1200
  relationships:
  - name: tags
    peer: BuiltinTag
    cardinality: many
    kind: Attribute
    optional: true
    order_weight: 3000
nodes:
- name: Manufacturer
  namespace: Organization
  description: Device Manufacturer
  icon: mdi:domain
  inherit_from:
  - OrganizationGeneric
  include_in_menu: true
  menu_placement: OrganizationGeneric
  relationships:
  - name: device_type
    peer: DcimDeviceType
    cardinality: many
    optional: true
  - name: platform
    peer: DcimPlatform
    cardinality: many
    optional: true
- name: Provider
  namespace: Organization
  description: Circuit or Location Provider
  icon: mdi:domain
  inherit_from:
  - OrganizationGeneric
  include_in_menu: true
  menu_placement: OrganizationGeneric
```
