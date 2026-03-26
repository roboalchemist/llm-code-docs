# Source: https://docs.infrahub.app/schema-library/reference/lag.md

# Lag

This schema extension includes models for Link Aggregation Groups (LAGs), enabling you to link physical interfaces as building blocs of your LAG interface. It can be used in standard networking environments as well as in compute scenarios, such as capturing bond interfaces.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Lag[​](#lag "Direct link to Lag")

* **Label:** LAG Interface
* **Description:** LAG interface
* **Namespace:** Interface
* **Inherit From:** DcimInterface, InterfaceLayer2, InterfaceLayer3, InterfaceHasSubInterface, GenericInterfaceBundle

#### Attributes[​](#attributes "Direct link to Attributes")

| name       | description                            | kind     | optional | default\_value | choices                   |
| ---------- | -------------------------------------- | -------- | -------- | -------------- | ------------------------- |
| lacp\_rate | LACP rate for the aggregated interface | Dropdown |          | fast           | slow, fast                |
| lacp\_mode | LACP mode for the aggregated interface | Dropdown |          | active         | active, passive, disabled |

#### Relationships[​](#relationships "Direct link to Relationships")

| name         | peer              | optional | cardinality | kind      |
| ------------ | ----------------- | -------- | ----------- | --------- |
| lag\_members | InterfacePhysical |          | many        | Attribute |

## Generics[​](#generics "Direct link to Generics")

### InterfaceBundle[​](#interfacebundle "Direct link to InterfaceBundle")

* **Label:** Generic Interface Bundle
* **Namespace:** Generic

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name | description           | kind | optional | default\_value | choices |
| ---- | --------------------- | ---- | -------- | -------------- | ------- |
| name | Name of the interface | Text |          |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name            | peer              | optional | cardinality | kind      |
| --------------- | ----------------- | -------- | ----------- | --------- |
| bundle\_members | InterfacePhysical |          | many        | Attribute |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### InterfacePhysical[​](#interfacephysical "Direct link to InterfacePhysical")

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name   | peer                   | optional | cardinality | kind      |
| ------ | ---------------------- | -------- | ----------- | --------- |
| bundle | GenericInterfaceBundle | True     | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: InterfaceBundle
  namespace: Generic
  label: Generic Interface Bundle
  include_in_menu: false
  attributes:
  - name: name
    kind: Text
    description: Name of the interface
    order_weight: 1000
  relationships:
  - name: bundle_members
    label: Bundle members
    peer: InterfacePhysical
    cardinality: many
    kind: Attribute
    description: Physical Interfaces that are members of this aggregate
    order_weight: 1800
nodes:
- name: Lag
  namespace: Interface
  label: LAG Interface
  description: LAG interface
  inherit_from:
  - DcimInterface
  - InterfaceLayer2
  - InterfaceLayer3
  - InterfaceHasSubInterface
  - GenericInterfaceBundle
  include_in_menu: false
  attributes:
  - name: lacp_rate
    label: LACP Rate
    kind: Dropdown
    choices:
    - name: slow
      label: Slow
      color: '#E6E6FA'
    - name: fast
      label: Fast
      color: '#E6E6FA'
    default_value: fast
    description: LACP rate for the aggregated interface
    order_weight: 1700
  - name: lacp_mode
    label: LACP Mode
    kind: Dropdown
    choices:
    - name: active
      label: Active
      color: '#E6E6FA'
    - name: passive
      label: Passive
      color: '#E6E6FA'
    - name: disabled
      label: Disabled
      color: '#E6E6FA'
    description: LACP mode for the aggregated interface
    default_value: active
    order_weight: 1750
  relationships:
  - name: lag_members
    common_parent: device
    label: Member(s)
    peer: InterfacePhysical
    cardinality: many
    kind: Attribute
    description: Physical Interfaces that are members of this aggregate
    order_weight: 1800
extensions:
  nodes:
  - kind: InterfacePhysical
    relationships:
    - name: bundle
      label: Interface Bundle
      peer: GenericInterfaceBundle
      optional: true
      cardinality: one
      kind: Attribute
      description: Interface Bundle using this Physical Interface
      order_weight: 1800
```
