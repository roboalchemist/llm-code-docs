# Source: https://docs.infrahub.app/schema-library/reference/interface_breakout.md

# Interface Breakout

This schema extension introduces relationships to support breakout interfaces, enabling you to document the breakout of a physical interface into smaller physical interfaces.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### InterfacePhysical[​](#interfacephysical "Direct link to InterfacePhysical")

#### Attributes[​](#attributes "Direct link to Attributes")

| name                 | description                                        | kind    | optional | default\_value | choices |
| -------------------- | -------------------------------------------------- | ------- | -------- | -------------- | ------- |
| breakout\_capability | Indicates if the port supports breakout capability | Boolean | False    | False          |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name                        | peer              | optional | cardinality | kind      |
| --------------------------- | ----------------- | -------- | ----------- | --------- |
| breakout\_child\_interfaces | InterfacePhysical | True     | many        | Attribute |
| breakout\_parent\_interface | InterfacePhysical | True     | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
extensions:
  nodes:
  - kind: InterfacePhysical
    attributes:
    - name: breakout_capability
      kind: Boolean
      optional: false
      default_value: false
      description: Indicates if the port supports breakout capability
    relationships:
    - name: breakout_child_interfaces
      peer: InterfacePhysical
      label: Breakout child interface(s)
      optional: true
      cardinality: many
      kind: Attribute
      identifier: physical__breakout
      direction: outbound
      description: Interfaces resulting from the breakout
      order_weight: 1650
    - name: breakout_parent_interface
      peer: InterfacePhysical
      label: Breakout parent interface
      optional: true
      cardinality: one
      kind: Attribute
      identifier: physical__breakout
      direction: inbound
      description: Interface from which breakout is created
      order_weight: 1700
```
