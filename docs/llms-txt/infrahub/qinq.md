# Source: https://docs.infrahub.app/schema-library/reference/qinq.md

# QinQ

This schema extension brings extensions to VLAN model in order to support QinQ.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/vlan](/schema-library/reference/vlan.md)

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### IpamVLAN[​](#ipamvlan "Direct link to IpamVLAN")

#### Attributes[​](#attributes "Direct link to Attributes")

| name       | description | kind     | optional | default\_value | choices           |
| ---------- | ----------- | -------- | -------- | -------------- | ----------------- |
| qinq\_role |             | Dropdown | True     |                | suplier, customer |

#### Relationships[​](#relationships "Direct link to Relationships")

| name  | peer     | optional | cardinality | kind      |
| ----- | -------- | -------- | ----------- | --------- |
| svlan | IpamVLAN | True     | one         | Attribute |
| cvlan | IpamVLAN | True     | many        | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
extensions:
  nodes:
  - kind: IpamVLAN
    attributes:
    - name: qinq_role
      kind: Dropdown
      optional: true
      choices:
      - name: suplier
        label: Suplier
        description: A VLAN used to encapsulate multiple CVLANs.
      - name: customer
        label: Customer
        description: A VLAN assigned to customer traffic.
    relationships:
    - name: svlan
      label: Supplier vlan
      peer: IpamVLAN
      optional: true
      direction: inbound
      identifier: vlan__qinq
      cardinality: one
      kind: Attribute
    - name: cvlan
      label: Customer vlan(s)
      peer: IpamVLAN
      optional: true
      direction: outbound
      identifier: vlan__qinq
      cardinality: many
      kind: Attribute
```
