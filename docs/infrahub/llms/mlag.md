# Source: https://docs.infrahub.app/schema-library/reference/mlag.md

# MLAG

This schema extension contains the foundations to capture Multi-Chassis Link Aggregation Group (MLAG). It comes on top of the LAG extension.

In this implementation, a MLAG interface is essentially a LAG interface but linked to a MLAG domain (instead of a device). The MLAG domain regroup devices together (usually 2) and is built over LAG interfaces used as peer-link between the devices. MLAG interfaces defined at the MLAG domain level are then spread across all devices in the domain.

Note: This is a very minimalist implementation of MLAG, the goal is to make it easy to blend with existing models you might have. For example, if you are operating in a data center fabric environment you might already have a LeafGroup or similar concept. In that case you can have your LeafGroup inherit from GenericMlagDomain and add the necessary relationships/attributes.

Next steps:

* Add support for layer 3 overlay for MLAG interfaces (loopback, peer address ...)
* Create virtual relationship so MLAG interfaces can be seen on the devices in the domain

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/lag](/schema-library/reference/lag.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Interface[​](#interface "Direct link to Interface")

* **Label:** MLAG Interface
* **Description:** Multi-Chassis Link Aggregation Group Interface
* **Namespace:** Mlag
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * mlag\_domain, name\_\_value
* **Human Friendly ID:** mlag\_domain\_\_domain\_id\_\_value, name\_\_value
* **Inherit From:** InterfaceLayer2, GenericInterfaceBundle

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description                              | kind     | optional | default\_value | choices                                                            |
| ----------- | ---------------------------------------- | -------- | -------- | -------------- | ------------------------------------------------------------------ |
| name        | Name of the interface                    | Text     |          |                |                                                                    |
| mlag\_id    | Identifier for the MLAG interface        | Number   |          |                |                                                                    |
| description | A brief description of the interface     | Text     | True     |                |                                                                    |
| status      | The status of the interface              | Dropdown |          | active         | provisioning, free, active, maintenance, disabled, deleted, outage |
| role        | The role of the interface in the network | Dropdown | True     |                | server, router                                                     |

#### Relationships[​](#relationships "Direct link to Relationships")

| name         | peer              | optional | cardinality | kind   |
| ------------ | ----------------- | -------- | ----------- | ------ |
| mlag\_domain | GenericMlagDomain | False    | one         | Parent |

### Domain[​](#domain "Direct link to Domain")

* **Label:** MLAG Domain
* **Description:** MLAG (Multi-Chassis Link Aggregation Group) Domain
* **Namespace:** Mlag
* **Icon:** mingcute
  <!-- -->
  :cloud-line
* **Inherit From:** GenericMlagDomain

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name  | peer       | optional | cardinality | kind    |
| ----- | ---------- | -------- | ----------- | ------- |
| peers | DcimDevice | False    | many        | Generic |

## Generics[​](#generics "Direct link to Generics")

### MlagDomain[​](#mlagdomain "Direct link to MlagDomain")

* **Label:** MLAG Domain
* **Namespace:** Generic
* **Display Labels:** domain\_id\_\_value
* **Human Friendly ID:** domain\_id\_\_value

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name          | description                                                        | kind   | optional | default\_value | choices |
| ------------- | ------------------------------------------------------------------ | ------ | -------- | -------------- | ------- |
| domain\_id    | Identifier for the MLAG domain                                     | Text   |          |                |         |
| reload\_delay | Time in seconds to wait before bringing up the MLAG after a reload | Number |          | 300            |         |

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name             | peer          | optional | cardinality | kind      |
| ---------------- | ------------- | -------- | ----------- | --------- |
| peer\_links      | InterfaceLag  |          | many        | Attribute |
| mlag\_interfaces | MlagInterface |          | many        | Component |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### InterfaceLag[​](#interfacelag "Direct link to InterfaceLag")

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name             | peer       | optional | cardinality | kind      |
| ---------------- | ---------- | -------- | ----------- | --------- |
| mlag\_peer\_link | MlagDomain | True     | one         | Attribute |

### DcimDevice[​](#dcimdevice "Direct link to DcimDevice")

#### Relationships[​](#relationships-4 "Direct link to Relationships")

| name         | peer       | optional | cardinality | kind      |
| ------------ | ---------- | -------- | ----------- | --------- |
| mlag\_domain | MlagDomain | True     | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: MlagDomain
  namespace: Generic
  include_in_menu: false
  label: MLAG Domain
  display_labels:
  - domain_id__value
  human_friendly_id:
  - domain_id__value
  attributes:
  - name: domain_id
    label: MLAG Domain ID
    kind: Text
    unique: true
    description: Identifier for the MLAG domain
    order_weight: 900
  - name: reload_delay
    label: Reload Delay
    kind: Number
    description: Time in seconds to wait before bringing up the MLAG after a reload
    default_value: 300
    order_weight: 1650
  relationships:
  - name: peer_links
    label: Peer Links
    description: LAG interfaces used as peer-links between the MLAG peers
    peer: InterfaceLag
    cardinality: many
    kind: Attribute
    order_weight: 1500
  - name: mlag_interfaces
    label: MLAG Interface(s)
    peer: MlagInterface
    cardinality: many
    kind: Component
    description: Bundle interfaces that are spread across all devices in this MLAG
      domain.
    order_weight: 1500
nodes:
- name: Interface
  namespace: Mlag
  label: MLAG Interface
  description: Multi-Chassis Link Aggregation Group Interface
  inherit_from:
  - InterfaceLayer2
  - GenericInterfaceBundle
  include_in_menu: false
  uniqueness_constraints:
  - - mlag_domain
    - name__value
  human_friendly_id:
  - mlag_domain__domain_id__value
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    description: Name of the interface
    order_weight: 1000
  - name: mlag_id
    label: MLAG ID
    kind: Number
    description: Identifier for the MLAG interface
    order_weight: 1050
  - name: description
    kind: Text
    optional: true
    description: A brief description of the interface
    order_weight: 1100
  - name: status
    kind: Dropdown
    description: The status of the interface
    choices:
    - name: provisioning
      label: Provisioning
      description: Interface is being provisioned.
      color: '#A9DFBF'
    - name: free
      label: Free
      description: Interface is unused.
      color: '#CDEACC'
    - name: active
      label: Active
      description: Interface is active and operational.
      color: '#A9CCE3'
    - name: maintenance
      label: Maintenance
      description: Interface is under maintenance.
      color: '#FFF2CC'
    - name: disabled
      label: Disabled
      description: Interface has been disabled.
      color: '#D3D3D3'
    - name: deleted
      label: Deleted
      description: Interface has been deleted.
      color: '#FAD7A0'
    - name: outage
      label: Outage
      description: Interface is currently experiencing an outage.
      color: '#F4CCCC'
    default_value: active
    order_weight: 1200
  - name: role
    kind: Dropdown
    optional: true
    description: The role of the interface in the network
    choices:
    - name: server
      label: Server Interface
      description: Interface connecting servers
      color: '#A9DFBF'
    - name: router
      label: Router Interface
      description: Interface connecting routers
      color: '#B2D4E6'
    order_weight: 1250
  relationships:
  - name: mlag_domain
    label: MLAG Domain
    peer: GenericMlagDomain
    optional: false
    cardinality: one
    kind: Parent
    description: MLAG Domain this MLAG Interface belongs to
    order_weight: 1750
- name: Domain
  namespace: Mlag
  label: MLAG Domain
  description: MLAG (Multi-Chassis Link Aggregation Group) Domain
  icon: mingcute:cloud-line
  inherit_from:
  - GenericMlagDomain
  relationships:
  - name: peers
    peer: DcimDevice
    optional: false
    cardinality: many
    kind: Generic
    identifier: device__mlag_domain
    max_count: 2
    min_count: 2
    order_weight: 950
extensions:
  nodes:
  - kind: InterfaceLag
    relationships:
    - name: mlag_peer_link
      label: MLAG Peer Link
      peer: MlagDomain
      optional: true
      cardinality: one
      kind: Attribute
      description: MLAG Domain this LAG is used as peer link
      order_weight: 1800
  - kind: DcimDevice
    relationships:
    - name: mlag_domain
      label: MLAG Domain
      peer: MlagDomain
      optional: true
      cardinality: one
      kind: Attribute
      description: MLAG Domain this device belongs to
      order_weight: 1800
      identifier: device__mlag_domain
```
