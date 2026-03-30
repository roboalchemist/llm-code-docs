# Source: https://docs.infrahub.app/schema-library/reference/location.md

# Locations

Basic Location schema to capture locations, sites, and related information.

## Details[​](#details "Direct link to Details")

* **Dependencies:** No dependencies

## Generics[​](#generics "Direct link to Generics")

### Generic[​](#generic "Direct link to Generic")

* **Label:** Location
* **Description:** Generic Location, could be a country, city ...
* **Namespace:** Location
* **Icon:** mingcute
  <!-- -->
  :location-line
* **Display Labels:** name\_\_value
* **Human Friendly ID:** shortname\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text |          |                |         |
| shortname   |             | Text |          |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name | peer       | optional | cardinality | kind      |
| ---- | ---------- | -------- | ----------- | --------- |
| tags | BuiltinTag | True     | many        | Attribute |

### Hosting[​](#hosting "Direct link to Hosting")

* **Description:** Location directly hosting device and services.
* **Namespace:** Location

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name     | peer               | optional | cardinality | kind |
| -------- | ------------------ | -------- | ----------- | ---- |
| prefixes | IpamPrefix         | True     | many        |      |
| devices  | DcimPhysicalDevice | True     | many        |      |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: Generic
  namespace: Location
  description: Generic Location, could be a country, city ...
  label: Location
  icon: mingcute:location-line
  include_in_menu: true
  hierarchical: true
  human_friendly_id:
  - shortname__value
  order_by:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    order_weight: 1000
  - name: shortname
    kind: Text
    unique: true
    order_weight: 1100
  - name: description
    kind: Text
    optional: true
    order_weight: 1200
  relationships:
  - name: tags
    peer: BuiltinTag
    kind: Attribute
    optional: true
    cardinality: many
- name: Hosting
  namespace: Location
  description: Location directly hosting device and services.
  include_in_menu: false
  relationships:
  - name: prefixes
    label: Prefixes
    peer: IpamPrefix
    cardinality: many
    optional: true
  - name: devices
    label: Devices
    peer: DcimPhysicalDevice
    cardinality: many
    optional: true
```
