# Source: https://docs.infrahub.app/schema-library/reference/vlan-translation.md

# VLAN Translation

This schema extension is based on Juniper VLAN MAP, and not yet test out for other vendors.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### MapInOut[​](#mapinout "Direct link to MapInOut")

* **Label:** VLAN Map In/Out
* **Description:** VLAN Mapping for In/Out operations
* **Namespace:** Network
* **Icon:** ph
  <!-- -->
  :swap
* **Uniqueness Constraints:**
  * interface, direction\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name                     | description                                             | kind     | optional | default\_value | choices                                                                  |
| ------------------------ | ------------------------------------------------------- | -------- | -------- | -------------- | ------------------------------------------------------------------------ |
| direction                | Direction of the mapping                                | Dropdown | True     |                | input, output                                                            |
| operation                | Operation type                                          | Dropdown | True     |                | pop, pop\_pop, pop\_swap, push, push\_push, swap, swap\_push, swap\_swap |
| vlan\_id\_swap           | VLAN ID to swap to during SWAP operations               | Number   | True     |                |                                                                          |
| inner\_vlan\_id          | Inner VLAN ID for operations involving double VLAN tags | Number   | True     |                |                                                                          |
| inner\_tag\_protocol\_id | Inner tag protocol ID (TPID)                            | Number   | True     |                |                                                                          |
| tag\_protocol\_id        | Tag protocol ID (TPID) for outer VLAN operations        | Number   | True     |                |                                                                          |

#### Relationships[​](#relationships "Direct link to Relationships")

| name      | peer          | optional | cardinality | kind   |
| --------- | ------------- | -------- | ----------- | ------ |
| interface | DcimInterface | False    | one         | Parent |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### DcimInterface[​](#dciminterface "Direct link to DcimInterface")

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name          | peer            | optional | cardinality | kind      |
| ------------- | --------------- | -------- | ----------- | --------- |
| network\_maps | NetworkMapInOut |          | many        | Component |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: MapInOut
  namespace: Network
  label: VLAN Map In/Out
  icon: ph:swap
  menu_placement: DcimInterface
  include_in_menu: true
  description: VLAN Mapping for In/Out operations
  order_by:
  - interface__name__value
  - direction__value
  - operation__value
  uniqueness_constraints:
  - - interface
    - direction__value
  attributes:
  - name: direction
    kind: Dropdown
    description: Direction of the mapping
    label: Map Direction
    order_weight: 1050
    choices:
    - name: input
      label: Input
      description: Input direction
      color: '#D2B4DE'
    - name: output
      label: Output
      description: Output direction
      color: '#A9CCE3'
    optional: true
  - name: operation
    kind: Dropdown
    description: Operation type
    label: Map Operation
    order_weight: 1100
    choices:
    - name: pop
      label: POP
      description: Single POP operation
      color: '#B2D4E6'
    - name: pop_pop
      label: POP-POP
      description: Double POP operation
      color: '#AED6F1'
    - name: pop_swap
      label: POP-SWAP
      description: POP then SWAP operation
      color: '#A9DFBF'
    - name: push
      label: PUSH
      description: Single PUSH operation
      color: '#CDEACC'
    - name: push_push
      label: PUSH-PUSH
      description: Double PUSH operation
      color: '#9FA8DA'
    - name: swap
      label: SWAP
      description: Single SWAP operation
      color: '#D2B4DE'
    - name: swap_push
      label: SWAP-PUSH
      description: SWAP then PUSH operation
      color: '#C4B7E6'
    - name: swap_swap
      label: SWAP-SWAP
      description: Double SWAP operation
      color: '#CBC3E3'
    optional: true
  - name: vlan_id_swap
    label: VLAN ID Swap
    kind: Number
    description: VLAN ID to swap to during SWAP operations
    optional: true
    order_weight: 1200
  - name: inner_vlan_id
    label: Inner VLAN ID
    kind: Number
    description: Inner VLAN ID for operations involving double VLAN tags
    optional: true
    order_weight: 1300
  - name: inner_tag_protocol_id
    label: Inner Tag Protocol ID
    kind: Number
    description: Inner tag protocol ID (TPID)
    optional: true
    order_weight: 1400
  - name: tag_protocol_id
    label: Tag Protocol ID
    kind: Number
    description: Tag protocol ID (TPID) for outer VLAN operations
    optional: true
    order_weight: 1500
  relationships:
  - name: interface
    kind: Parent
    peer: DcimInterface
    description: Interface to which the Input/Output VLAN mapping is applied
    cardinality: one
    optional: false
    label: Interface
    order_weight: 1000
extensions:
  nodes:
  - kind: DcimInterface
    relationships:
    - name: network_maps
      kind: Component
      peer: NetworkMapInOut
      description: Interface Input/Output VLAN mapping
      cardinality: many
      label: Input/Output MAP
      order_weight: 1600
```
