# Source: https://docs.infrahub.app/schema-library/reference/security.md

# Security

This schema extension contains models for implementing detailed security.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Zone[​](#zone "Direct link to Zone")

* **Label:** Security zone
* **Description:** Security zones
* **Namespace:** Security
* **Icon:** game-icons
  <!-- -->
  :fire-zone
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name | description | kind | optional | default\_value | choices |
| ---- | ----------- | ---- | -------- | -------------- | ------- |
| name |             | Text | False    |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name       | peer                      | optional | cardinality | kind      |
| ---------- | ------------------------- | -------- | ----------- | --------- |
| interfaces | SecurityFirewallInterface | True     |             | Attribute |

### IPAMIPAddress[​](#ipamipaddress "Direct link to IPAMIPAddress")

* **Label:** IPAM IP Address
* **Description:** Infrahub IPv4/6 address
* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :ip-outline
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericAddress

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name        | peer           | optional | cardinality | kind      |
| ----------- | -------------- | -------- | ----------- | --------- |
| ip\_address | InfraIPAddress | False    | one         | Attribute |

### IPAMIPPrefix[​](#ipamipprefix "Direct link to IPAMIPPrefix")

* **Label:** IPAM IP Prefix
* **Description:** Infrahub IPv4/6 prefix
* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :ip-network-outline
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericAddress

#### Attributes[​](#attributes-2 "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name       | peer        | optional | cardinality | kind      |
| ---------- | ----------- | -------- | ----------- | --------- |
| ip\_prefix | InfraPrefix | False    | one         | Attribute |

### IPAddress[​](#ipaddress "Direct link to IPAddress")

* **Label:** IP Address
* **Description:** IPv4/6 address
* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :ip-outline
* **Display Labels:** name\_\_value, address\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericAddress

#### Attributes[​](#attributes-3 "Direct link to Attributes")

| name        | description | kind   | optional | default\_value | choices |
| ----------- | ----------- | ------ | -------- | -------------- | ------- |
| address     |             | IPHost |          |                |         |
| description |             | Text   | True     |                |         |

### Prefix[​](#prefix "Direct link to Prefix")

* **Label:** Prefix
* **Description:** IPv4/6 prefix
* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :ip-network-outline
* **Display Labels:** name\_\_value, prefix\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericAddress

#### Attributes[​](#attributes-4 "Direct link to Attributes")

| name        | description | kind      | optional | default\_value | choices |
| ----------- | ----------- | --------- | -------- | -------------- | ------- |
| prefix      |             | IPNetwork | False    |                |         |
| description |             | Text      | True     |                |         |

### IPRange[​](#iprange "Direct link to IPRange")

* **Label:** IP Range
* **Description:** IPv4/6 Range
* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :ip-outline
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericAddress

#### Attributes[​](#attributes-5 "Direct link to Attributes")

| name  | description | kind   | optional | default\_value | choices |
| ----- | ----------- | ------ | -------- | -------------- | ------- |
| start |             | IPHost | False    |                |         |
| end   |             | IPHost | False    |                |         |

### FQDN[​](#fqdn "Direct link to FQDN")

* **Label:** FQDN
* **Description:** Full Qualified Domain Name
* **Namespace:** Security
* **Icon:** eos-icons
  <!-- -->
  :dns
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericAddress

#### Attributes[​](#attributes-6 "Direct link to Attributes")

| name | description | kind | optional | default\_value | choices |
| ---- | ----------- | ---- | -------- | -------------- | ------- |
| fqdn |             | Text | False    |                |         |

### AddressGroup[​](#addressgroup "Direct link to AddressGroup")

* **Label:** Address Group
* **Description:** Group of addresses
* **Namespace:** Security
* **Icon:** material-symbols
  <!-- -->
  :menu-book-outline-rounded
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericAddressGroup

### IPProtocol[​](#ipprotocol "Direct link to IPProtocol")

* **Label:** IP Protocols
* **Description:** IP protocol
* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :protocol
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericService

#### Attributes[​](#attributes-7 "Direct link to Attributes")

| name     | description | kind   | optional | default\_value | choices |
| -------- | ----------- | ------ | -------- | -------------- | ------- |
| protocol |             | Number | True     |                |         |

### Service[​](#service "Direct link to Service")

* **Label:** Service
* **Description:** Service
* **Namespace:** Security
* **Icon:** eos-icons
  <!-- -->
  :application-outlined
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericService

#### Attributes[​](#attributes-8 "Direct link to Attributes")

| name | description | kind   | optional | default\_value | choices |
| ---- | ----------- | ------ | -------- | -------------- | ------- |
| port |             | Number |          |                |         |

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name         | peer               | optional | cardinality | kind      |
| ------------ | ------------------ | -------- | ----------- | --------- |
| ip\_protocol | SecurityIPProtocol | True     | one         | Attribute |

### ServiceRange[​](#servicerange "Direct link to ServiceRange")

* **Label:** Service range
* **Description:** Service range
* **Namespace:** Security
* **Icon:** eos-icons
  <!-- -->
  :application-outlined
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericService

#### Attributes[​](#attributes-9 "Direct link to Attributes")

| name  | description | kind   | optional | default\_value | choices |
| ----- | ----------- | ------ | -------- | -------------- | ------- |
| start |             | Number | False    |                |         |
| end   |             | Number | False    |                |         |

#### Relationships[​](#relationships-4 "Direct link to Relationships")

| name         | peer               | optional | cardinality | kind      |
| ------------ | ------------------ | -------- | ----------- | --------- |
| ip\_protocol | SecurityIPProtocol | False    | one         | Attribute |

### ServiceGroup[​](#servicegroup "Direct link to ServiceGroup")

* **Label:** Service group
* **Description:** Group of services
* **Namespace:** Security
* **Icon:** material-symbols
  <!-- -->
  :menu-book-outline-rounded
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** SecurityGenericServiceGroup

### Policy[​](#policy "Direct link to Policy")

* **Label:** Security Policy
* **Namespace:** Security
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-10 "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text | False    |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-5 "Direct link to Relationships")

| name             | peer               | optional | cardinality | kind      |
| ---------------- | ------------------ | -------- | ----------- | --------- |
| rules            | SecurityPolicyRule |          | many        | Component |
| location\_target | LocationGeneric    | True     | one         | Attribute |
| device\_target   | SecurityFirewall   | True     | one         | Attribute |

### PolicyRule[​](#policyrule "Direct link to PolicyRule")

* **Label:** Policy rule
* **Description:** Policy rule
* **Namespace:** Security
* **Icon:** material-symbols
  <!-- -->
  :policy
* **Uniqueness Constraints:**
  * index\_\_value, source\_zone, destination\_zone, policy

#### Attributes[​](#attributes-11 "Direct link to Attributes")

| name   | description | kind    | optional | default\_value | choices |
| ------ | ----------- | ------- | -------- | -------------- | ------- |
| index  |             | Number  | False    |                |         |
| name   |             | Text    | False    |                |         |
| action |             | Text    | False    | permit         |         |
| log    |             | Boolean | True     | False          |         |

#### Relationships[​](#relationships-6 "Direct link to Relationships")

| name                         | peer                        | optional | cardinality | kind      |
| ---------------------------- | --------------------------- | -------- | ----------- | --------- |
| policy                       | SecurityPolicy              | False    | one         | Attribute |
| source\_zone                 | SecurityZone                | False    | one         | Attribute |
| destination\_zone            | SecurityZone                | False    | one         | Attribute |
| source\_address              | SecurityGenericAddress      | True     | many        | Attribute |
| source\_groups               | SecurityGenericAddressGroup | True     | many        | Attribute |
| source\_services             | SecurityGenericService      | True     | many        | Attribute |
| source\_service\_groups      | SecurityGenericServiceGroup | True     | many        | Attribute |
| destination\_address         | SecurityGenericAddress      | True     | many        | Attribute |
| destination\_groups          | SecurityGenericAddressGroup | True     | many        | Attribute |
| destination\_services        | SecurityGenericService      | True     | many        | Attribute |
| destination\_service\_groups | SecurityGenericServiceGroup | True     | many        | Attribute |

### Firewall[​](#firewall "Direct link to Firewall")

* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :firewall
* **Human Friendly ID:** name\_\_value
* **Inherit From:** InfraGenericDevice, CoreArtifactTarget, SecurityPolicyAssignment

#### Attributes[​](#attributes-12 "Direct link to Attributes")

| name | description | kind     | optional | default\_value | choices        |
| ---- | ----------- | -------- | -------- | -------------- | -------------- |
| role |             | Dropdown | True     |                | edge\_firewall |

#### Relationships[​](#relationships-7 "Direct link to Relationships")

| name   | peer           | optional | cardinality | kind      |
| ------ | -------------- | -------- | ----------- | --------- |
| policy | SecurityPolicy |          | one         | Attribute |

### RenderedPolicyRule[​](#renderedpolicyrule "Direct link to RenderedPolicyRule")

* **Label:** Policy rule
* **Description:** Policy rule
* **Namespace:** Security

#### Attributes[​](#attributes-13 "Direct link to Attributes")

| name   | description | kind    | optional | default\_value | choices |
| ------ | ----------- | ------- | -------- | -------------- | ------- |
| index  |             | Number  | False    |                |         |
| name   |             | Text    | False    |                |         |
| action |             | Text    | False    | permit         |         |
| log    |             | Boolean | True     | False          |         |

#### Relationships[​](#relationships-8 "Direct link to Relationships")

| name                         | peer                        | optional | cardinality | kind      |
| ---------------------------- | --------------------------- | -------- | ----------- | --------- |
| source\_policy               | SecurityPolicy              | False    | one         | Attribute |
| source\_zone                 | SecurityZone                | False    | one         | Attribute |
| destination\_zone            | SecurityZone                | False    | one         | Attribute |
| source\_address              | SecurityGenericAddress      | True     | many        | Attribute |
| source\_groups               | SecurityGenericAddressGroup | True     | many        | Attribute |
| source\_services             | SecurityGenericService      | True     | many        | Attribute |
| source\_service\_groups      | SecurityGenericServiceGroup | True     | many        | Attribute |
| destination\_address         | SecurityGenericAddress      | True     | many        | Attribute |
| destination\_groups          | SecurityGenericAddressGroup | True     | many        | Attribute |
| destination\_services        | SecurityGenericService      | True     | many        | Attribute |
| destination\_service\_groups | SecurityGenericServiceGroup | True     | many        | Attribute |

### FirewallInterface[​](#firewallinterface "Direct link to FirewallInterface")

* **Label:** Firewall Interface
* **Namespace:** Security
* **Icon:** mdi
  <!-- -->
  :ethernet
* **Display Labels:** name\_\_value
* **Inherit From:** InfraInterface, InfraEndpoint

#### Relationships[​](#relationships-9 "Direct link to Relationships")

| name           | peer           | optional | cardinality | kind      |
| -------------- | -------------- | -------- | ----------- | --------- |
| ip\_addresses  | InfraIPAddress | True     | many        | Component |
| security\_zone | SecurityZone   | False    | one         | Attribute |

## Generics[​](#generics "Direct link to Generics")

### PolicyAssignment[​](#policyassignment "Direct link to PolicyAssignment")

* **Label:** Security Policy
* **Namespace:** Security

#### Relationships[​](#relationships-10 "Direct link to Relationships")

| name  | peer                       | optional | cardinality | kind      |
| ----- | -------------------------- | -------- | ----------- | --------- |
| rules | SecurityRenderedPolicyRule | True     | many        | Component |

### GenericAddressGroup[​](#genericaddressgroup "Direct link to GenericAddressGroup")

* **Namespace:** Security
* **Display Labels:** name\_\_value

#### Attributes[​](#attributes-14 "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text | False    |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-11 "Direct link to Relationships")

| name      | peer                   | optional | cardinality | kind      |
| --------- | ---------------------- | -------- | ----------- | --------- |
| addresses | SecurityGenericAddress | True     | many        | Component |

### GenericAddress[​](#genericaddress "Direct link to GenericAddress")

* **Namespace:** Security
* **Display Labels:** name\_\_value

#### Attributes[​](#attributes-15 "Direct link to Attributes")

| name | description | kind | optional | default\_value | choices |
| ---- | ----------- | ---- | -------- | -------------- | ------- |
| name |             | Text | False    |                |         |

#### Relationships[​](#relationships-12 "Direct link to Relationships")

| name            | peer                        | optional | cardinality | kind |
| --------------- | --------------------------- | -------- | ----------- | ---- |
| address\_groups | SecurityGenericAddressGroup | True     | many        |      |

### GenericServiceGroup[​](#genericservicegroup "Direct link to GenericServiceGroup")

* **Namespace:** Security
* **Display Labels:** name\_\_value

#### Attributes[​](#attributes-16 "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text | False    |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-13 "Direct link to Relationships")

| name     | peer                   | optional | cardinality | kind      |
| -------- | ---------------------- | -------- | ----------- | --------- |
| services | SecurityGenericService | True     | many        | Component |

### GenericService[​](#genericservice "Direct link to GenericService")

* **Namespace:** Security
* **Display Labels:** name\_\_value

#### Attributes[​](#attributes-17 "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text | False    |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-14 "Direct link to Relationships")

| name            | peer                        | optional | cardinality | kind |
| --------------- | --------------------------- | -------- | ----------- | ---- |
| service\_groups | SecurityGenericServiceGroup | True     | many        |      |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### LocationGeneric[​](#locationgeneric "Direct link to LocationGeneric")

#### Relationships[​](#relationships-15 "Direct link to Relationships")

| name   | peer           | optional | cardinality | kind      |
| ------ | -------------- | -------- | ----------- | --------- |
| policy | SecurityPolicy |          | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: PolicyAssignment
  namespace: Security
  label: Security Policy
  include_in_menu: false
  relationships:
  - name: rules
    label: Policy
    peer: SecurityRenderedPolicyRule
    kind: Component
    cardinality: many
    optional: true
- name: GenericAddressGroup
  namespace: Security
  include_in_menu: false
  display_labels:
  - name__value
  hierarchical: true
  attributes:
  - name: name
    kind: Text
    label: Name
    optional: false
    unique: true
  - name: description
    label: Description
    kind: Text
    optional: true
  relationships:
  - name: addresses
    peer: SecurityGenericAddress
    cardinality: many
    kind: Component
    optional: true
- name: GenericAddress
  namespace: Security
  display_labels:
  - name__value
  include_in_menu: false
  attributes:
  - name: name
    kind: Text
    optional: false
    unique: true
  relationships:
  - name: address_groups
    label: Address Groups
    peer: SecurityGenericAddressGroup
    cardinality: many
    optional: true
- name: GenericServiceGroup
  namespace: Security
  include_in_menu: false
  hierarchical: true
  display_labels:
  - name__value
  attributes:
  - name: name
    label: Name
    kind: Text
    optional: false
  - name: description
    label: Description
    kind: Text
    optional: true
  relationships:
  - name: services
    peer: SecurityGenericService
    label: Services
    cardinality: many
    kind: Component
    optional: true
- name: GenericService
  include_in_menu: false
  namespace: Security
  display_labels:
  - name__value
  attributes:
  - name: name
    label: Name
    kind: Text
    optional: false
  - name: description
    kind: Text
    label: Description
    optional: true
  relationships:
  - name: service_groups
    label: Service Groups
    peer: SecurityGenericServiceGroup
    cardinality: many
    optional: true
nodes:
- name: Zone
  namespace: Security
  menu_placement: SecurityPolicy
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  include_in_menu: true
  icon: game-icons:fire-zone
  description: Security zones
  label: Security zone
  attributes:
  - name: name
    kind: Text
    unique: true
    optional: false
  relationships:
  - name: interfaces
    label: Interfaces
    kind: Attribute
    optional: true
    peer: SecurityFirewallInterface
- name: IPAMIPAddress
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: mdi:ip-outline
  description: Infrahub IPv4/6 address
  label: IPAM IP Address
  human_friendly_id:
  - name__value
  inherit_from:
  - SecurityGenericAddress
  attributes:
  - name: description
    kind: Text
    optional: true
  relationships:
  - name: ip_address
    peer: InfraIPAddress
    cardinality: one
    kind: Attribute
    optional: false
- name: IPAMIPPrefix
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: mdi:ip-network-outline
  description: Infrahub IPv4/6 prefix
  label: IPAM IP Prefix
  human_friendly_id:
  - name__value
  inherit_from:
  - SecurityGenericAddress
  attributes:
  - name: description
    kind: Text
    optional: true
  relationships:
  - name: ip_prefix
    peer: InfraPrefix
    cardinality: one
    kind: Attribute
    optional: false
- name: IPAddress
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  description: IPv4/6 address
  human_friendly_id:
  - name__value
  label: IP Address
  icon: mdi:ip-outline
  inherit_from:
  - SecurityGenericAddress
  order_by:
  - address__value
  display_labels:
  - name__value
  - address__value
  attributes:
  - name: address
    kind: IPHost
  - name: description
    kind: Text
    optional: true
- name: Prefix
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: mdi:ip-network-outline
  description: IPv4/6 prefix
  label: Prefix
  human_friendly_id:
  - name__value
  inherit_from:
  - SecurityGenericAddress
  order_by:
  - name__value
  display_labels:
  - name__value
  - prefix__value
  attributes:
  - name: prefix
    kind: IPNetwork
    optional: false
    unique: true
  - name: description
    kind: Text
    optional: true
- name: IPRange
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: mdi:ip-outline
  description: IPv4/6 Range
  label: IP Range
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  inherit_from:
  - SecurityGenericAddress
  order_by:
  - name__value
  attributes:
  - name: start
    label: Start IP Address
    kind: IPHost
    optional: false
  - name: end
    label: End IP Address
    kind: IPHost
    optional: false
- name: FQDN
  namespace: Security
  description: Full Qualified Domain Name
  include_in_menu: true
  icon: eos-icons:dns
  menu_placement: SecurityPolicy
  label: FQDN
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  inherit_from:
  - SecurityGenericAddress
  order_by:
  - name__value
  - fqdn__value
  attributes:
  - name: fqdn
    label: FQDN
    kind: Text
    optional: false
    regex: (?=^.{1,253}$)(^(((?!-)[a-zA-Z0-9-]{1,63}(?<!-))|((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63})$)
- name: AddressGroup
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: material-symbols:menu-book-outline-rounded
  description: Group of addresses
  label: Address Group
  human_friendly_id:
  - name__value
  parent: SecurityAddressGroup
  display_labels:
  - name__value
  inherit_from:
  - SecurityGenericAddressGroup
- name: IPProtocol
  namespace: Security
  menu_placement: SecurityPolicy
  icon: mdi:protocol
  include_in_menu: true
  description: IP protocol
  label: IP Protocols
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  order_by:
  - name__value
  inherit_from:
  - SecurityGenericService
  attributes:
  - name: protocol
    kind: Number
    optional: true
- name: Service
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: eos-icons:application-outlined
  description: Service
  label: Service
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  order_by:
  - name__value
  inherit_from:
  - SecurityGenericService
  attributes:
  - name: port
    kind: Number
  relationships:
  - name: ip_protocol
    peer: SecurityIPProtocol
    optional: true
    cardinality: one
    kind: Attribute
- name: ServiceRange
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: eos-icons:application-outlined
  description: Service range
  label: Service range
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  order_by:
  - name__value
  inherit_from:
  - SecurityGenericService
  attributes:
  - name: start
    kind: Number
    optional: false
  - name: end
    kind: Number
    optional: false
  relationships:
  - name: ip_protocol
    peer: SecurityIPProtocol
    optional: false
    cardinality: one
    kind: Attribute
- name: ServiceGroup
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: material-symbols:menu-book-outline-rounded
  label: Service group
  description: Group of services
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  order_by:
  - name__value
  inherit_from:
  - SecurityGenericServiceGroup
- name: Policy
  namespace: Security
  label: Security Policy
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  order_by:
  - name__value
  attributes:
  - name: name
    label: Name
    kind: Text
    optional: false
  - name: description
    label: Description
    kind: Text
    optional: true
  relationships:
  - name: rules
    peer: SecurityPolicyRule
    cardinality: many
    kind: Component
  - name: location_target
    peer: LocationGeneric
    cardinality: one
    optional: true
    kind: Attribute
  - name: device_target
    peer: SecurityFirewall
    cardinality: one
    optional: true
    kind: Attribute
- name: PolicyRule
  namespace: Security
  menu_placement: SecurityPolicy
  include_in_menu: true
  icon: material-symbols:policy
  label: Policy rule
  description: Policy rule
  order_by:
  - source_zone__name__value
  - destination_zone__name__value
  - index__value
  uniqueness_constraints:
  - - index__value
    - source_zone
    - destination_zone
    - policy
  attributes:
  - name: index
    label: Index
    kind: Number
    optional: false
    order_weight: 99999
  - name: name
    label: Name
    kind: Text
    optional: false
  - name: action
    label: Action
    kind: Text
    enum:
    - permit
    - deny
    default_value: permit
    optional: false
  - name: log
    label: Log
    kind: Boolean
    default_value: false
    optional: true
    order_weight: 99998
  relationships:
  - name: policy
    peer: SecurityPolicy
    kind: Attribute
    cardinality: one
    optional: false
  - name: source_zone
    peer: SecurityZone
    kind: Attribute
    cardinality: one
    optional: false
    order_weight: 1
    identifier: policy_rule__source_zone
  - name: destination_zone
    peer: SecurityZone
    kind: Attribute
    cardinality: one
    optional: false
    order_weight: 2
    identifier: policy_rule__destination_zone
  - name: source_address
    peer: SecurityGenericAddress
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__source_address
  - name: source_groups
    peer: SecurityGenericAddressGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__source_address_group
  - name: source_services
    peer: SecurityGenericService
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__source_service
  - name: source_service_groups
    peer: SecurityGenericServiceGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__source_service_group
  - name: destination_address
    peer: SecurityGenericAddress
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__destination_address
  - name: destination_groups
    peer: SecurityGenericAddressGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__destination_address_group
  - name: destination_services
    peer: SecurityGenericService
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__destination_service
  - name: destination_service_groups
    peer: SecurityGenericServiceGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: policy_rule__destination_service_group
- name: Firewall
  namespace: Security
  inherit_from:
  - InfraGenericDevice
  - CoreArtifactTarget
  - SecurityPolicyAssignment
  icon: mdi:firewall
  include_in_menu: true
  human_friendly_id:
  - name__value
  menu_placement: InfraGenericDevice
  attributes:
  - name: role
    kind: Dropdown
    optional: true
    choices:
    - name: edge_firewall
      label: Edge firewall
      description: Security boundary with external network
      color: '#6a5acd'
  relationships:
  - name: policy
    peer: SecurityPolicy
    label: Security Policy
    cardinality: one
    kind: Attribute
- name: RenderedPolicyRule
  namespace: Security
  include_in_menu: false
  label: Policy rule
  description: Policy rule
  order_by:
  - source_zone__name__value
  - destination_zone__name__value
  - index__value
  attributes:
  - name: index
    label: Index
    kind: Number
    optional: false
    order_weight: 99999
  - name: name
    label: Name
    kind: Text
    optional: false
  - name: action
    label: Action
    kind: Text
    enum:
    - permit
    - deny
    default_value: permit
    optional: false
  - name: log
    label: Log
    kind: Boolean
    default_value: false
    optional: true
    order_weight: 99998
  relationships:
  - name: source_policy
    peer: SecurityPolicy
    kind: Attribute
    cardinality: one
    optional: false
  - name: source_zone
    peer: SecurityZone
    kind: Attribute
    cardinality: one
    optional: false
    identifier: rendered_policy_rule__source_zone
    order_weight: 1
  - name: destination_zone
    peer: SecurityZone
    kind: Attribute
    cardinality: one
    optional: false
    identifier: rendered_policy_rule__destination_zone
    order_weight: 2
  - name: source_address
    peer: SecurityGenericAddress
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__source_address
  - name: source_groups
    peer: SecurityGenericAddressGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__source_address_group
  - name: source_services
    peer: SecurityGenericService
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__source_service
  - name: source_service_groups
    peer: SecurityGenericServiceGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__source_service_group
  - name: destination_address
    peer: SecurityGenericAddress
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__destination_address
  - name: destination_groups
    peer: SecurityGenericAddressGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__destination_address_group
  - name: destination_services
    peer: SecurityGenericService
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__destination_service
  - name: destination_service_groups
    peer: SecurityGenericServiceGroup
    optional: true
    kind: Attribute
    cardinality: many
    identifier: rendered_policy_rule__destination_service_group
- name: FirewallInterface
  namespace: Security
  label: Firewall Interface
  menu_placement: InfraGenericDevice
  include_in_menu: false
  icon: mdi:ethernet
  display_labels:
  - name__value
  inherit_from:
  - InfraInterface
  - InfraEndpoint
  relationships:
  - name: ip_addresses
    peer: InfraIPAddress
    optional: true
    cardinality: many
    kind: Component
  - name: security_zone
    peer: SecurityZone
    optional: false
    cardinality: one
    kind: Attribute
extensions:
  nodes:
  - kind: LocationGeneric
    relationships:
    - name: policy
      peer: SecurityPolicy
      cardinality: one
      kind: Attribute
```
