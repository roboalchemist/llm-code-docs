# Source: https://docs.infrahub.app/schema-library/reference/location_minimal.md

# Location Minimal

This schema extension is minimal but will provide you with basic items to store location related data.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Country[​](#country "Direct link to Country")

* **Label:** Country
* **Namespace:** Location
* **Icon:** gis
  <!-- -->
  :search-country
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

#### Attributes[​](#attributes "Direct link to Attributes")

| name     | description | kind | optional | default\_value | choices |
| -------- | ----------- | ---- | -------- | -------------- | ------- |
| timezone |             | Text | True     |                |         |

### Metro[​](#metro "Direct link to Metro")

* **Label:** Metro
* **Namespace:** Location
* **Icon:** healthicons
  <!-- -->
  :city
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

### Site[​](#site "Direct link to Site")

* **Label:** Site
* **Namespace:** Location
* **Icon:** ri
  <!-- -->
  :building-line
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric, LocationHosting

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name              | description | kind | optional | default\_value | choices |
| ----------------- | ----------- | ---- | -------- | -------------- | ------- |
| facility\_id      |             | Text | True     |                |         |
| physical\_address |             | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name  | peer                | optional | cardinality | kind |
| ----- | ------------------- | -------- | ----------- | ---- |
| owner | OrganizationGeneric | True     | one         |      |

### Rack[​](#rack "Direct link to Rack")

* **Label:** Rack
* **Namespace:** Location
* **Icon:** clarity
  <!-- -->
  :rack-server-line
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric, LocationHosting

#### Attributes[​](#attributes-2 "Direct link to Attributes")

| name         | description | kind   | optional | default\_value | choices |
| ------------ | ----------- | ------ | -------- | -------------- | ------- |
| facility\_id |             | Text   | True     |                |         |
| height       |             | Number | False    | 42             |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name  | peer                | optional | cardinality | kind |
| ----- | ------------------- | -------- | ----------- | ---- |
| owner | OrganizationGeneric | True     | one         |      |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### OrganizationProvider[​](#organizationprovider "Direct link to OrganizationProvider")

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name  | peer         | optional | cardinality | kind |
| ----- | ------------ | -------- | ----------- | ---- |
| sites | LocationSite | True     | many        |      |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: Country
  namespace: Location
  label: Country
  inherit_from:
  - LocationGeneric
  menu_placement: LocationGeneric
  display_labels:
  - name__value
  parent: ''
  children: LocationMetro
  icon: gis:search-country
  attributes:
  - name: timezone
    kind: Text
    optional: true
    order_weight: 1300
- name: Metro
  namespace: Location
  label: Metro
  inherit_from:
  - LocationGeneric
  menu_placement: LocationGeneric
  display_labels:
  - name__value
  parent: LocationCountry
  children: LocationSite
  icon: healthicons:city
- name: Site
  namespace: Location
  label: Site
  inherit_from:
  - LocationGeneric
  - LocationHosting
  menu_placement: LocationGeneric
  display_labels:
  - name__value
  parent: LocationMetro
  children: LocationRack
  icon: ri:building-line
  attributes:
  - name: facility_id
    kind: Text
    unique: false
    optional: true
    order_weight: 1100
  - name: physical_address
    kind: Text
    unique: false
    optional: true
    order_weight: 1500
  relationships:
  - name: owner
    peer: OrganizationGeneric
    optional: true
    cardinality: one
- name: Rack
  namespace: Location
  label: Rack
  inherit_from:
  - LocationGeneric
  - LocationHosting
  include_in_menu: true
  display_labels:
  - name__value
  menu_placement: LocationGeneric
  parent: LocationSite
  icon: clarity:rack-server-line
  attributes:
  - name: facility_id
    kind: Text
    unique: false
    optional: true
    order_weight: 1100
  - name: height
    label: Height (U)
    optional: false
    default_value: 42
    kind: Number
    order_weight: 1300
  relationships:
  - name: owner
    peer: OrganizationGeneric
    optional: true
    cardinality: one
extensions:
  nodes:
  - kind: OrganizationProvider
    relationships:
    - name: sites
      peer: LocationSite
      cardinality: many
      optional: true
```
