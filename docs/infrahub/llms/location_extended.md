# Source: https://docs.infrahub.app/schema-library/reference/location_extended.md

# Location Extended

This schema extension is the most detailed when it comes to location, you'll find all the layers you can think of.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Continent[​](#continent "Direct link to Continent")

* **Label:** Continent
* **Namespace:** Location
* **Icon:** jam
  <!-- -->
  :world
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

### Country[​](#country "Direct link to Country")

* **Label:** Country
* **Namespace:** Location
* **Icon:** gis
  <!-- -->
  :search-country
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

### Region[​](#region "Direct link to Region")

* **Label:** Region
* **Namespace:** Location
* **Icon:** carbon
  <!-- -->
  :cics-region-target
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

### Metro[​](#metro "Direct link to Metro")

* **Label:** Metro
* **Namespace:** Location
* **Icon:** healthicons
  <!-- -->
  :city
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

### Building[​](#building "Direct link to Building")

* **Label:** Building
* **Namespace:** Location
* **Icon:** ri
  <!-- -->
  :building-line
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

#### Attributes[​](#attributes "Direct link to Attributes")

| name              | description | kind | optional | default\_value | choices |
| ----------------- | ----------- | ---- | -------- | -------------- | ------- |
| facility\_id      |             | Text | True     |                |         |
| physical\_address |             | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name  | peer                | optional | cardinality | kind |
| ----- | ------------------- | -------- | ----------- | ---- |
| owner | OrganizationGeneric | True     | one         |      |

### Floor[​](#floor "Direct link to Floor")

* **Label:** Floor
* **Namespace:** Location
* **Icon:** mdi
  <!-- -->
  :home-floor-0
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

### Suite[​](#suite "Direct link to Suite")

* **Label:** Suite
* **Namespace:** Location
* **Icon:** game-icons
  <!-- -->
  :cage
* **Display Labels:** name\_\_value
* **Inherit From:** LocationGeneric

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name         | description | kind | optional | default\_value | choices |
| ------------ | ----------- | ---- | -------- | -------------- | ------- |
| facility\_id |             | Text | True     |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

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
* **Human Friendly ID:** shortname\_\_value
* **Inherit From:** LocationGeneric

#### Attributes[​](#attributes-2 "Direct link to Attributes")

| name         | description | kind | optional | default\_value | choices |
| ------------ | ----------- | ---- | -------- | -------------- | ------- |
| facility\_id |             | Text | True     |                |         |

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name  | peer                | optional | cardinality | kind |
| ----- | ------------------- | -------- | ----------- | ---- |
| owner | OrganizationGeneric | True     | one         |      |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### OrganizationProvider[​](#organizationprovider "Direct link to OrganizationProvider")

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name     | peer             | optional | cardinality | kind |
| -------- | ---------------- | -------- | ----------- | ---- |
| location | LocationBuilding | True     | many        |      |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: Continent
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Continent
  display_labels:
  - name__value
  parent: ''
  children: LocationCountry
  icon: jam:world
- name: Country
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Country
  display_labels:
  - name__value
  parent: LocationContinent
  children: LocationRegion
  icon: gis:search-country
- name: Region
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Region
  display_labels:
  - name__value
  parent: LocationCountry
  children: LocationMetro
  icon: carbon:cics-region-target
- name: Metro
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Metro
  display_labels:
  - name__value
  parent: LocationRegion
  children: LocationBuilding
  icon: healthicons:city
- name: Building
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Building
  display_labels:
  - name__value
  parent: LocationMetro
  children: LocationFloor
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
- name: Floor
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Floor
  display_labels:
  - name__value
  parent: LocationBuilding
  icon: mdi:home-floor-0
  children: LocationSuite
- name: Suite
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Suite
  display_labels:
  - name__value
  parent: LocationFloor
  children: LocationRack
  icon: game-icons:cage
  attributes:
  - name: facility_id
    kind: Text
    unique: false
    optional: true
    order_weight: 1100
  relationships:
  - name: owner
    peer: OrganizationGeneric
    optional: true
    cardinality: one
- name: Rack
  namespace: Location
  inherit_from:
  - LocationGeneric
  include_in_menu: true
  menu_placement: LocationGeneric
  label: Rack
  display_labels:
  - name__value
  human_friendly_id:
  - shortname__value
  parent: LocationSuite
  children: ''
  icon: clarity:rack-server-line
  attributes:
  - name: facility_id
    kind: Text
    unique: false
    optional: true
    order_weight: 1100
  relationships:
  - name: owner
    peer: OrganizationGeneric
    optional: true
    cardinality: one
extensions:
  nodes:
  - kind: OrganizationProvider
    relationships:
    - name: location
      peer: LocationBuilding
      cardinality: many
      optional: true
```
