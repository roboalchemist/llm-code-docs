# Source: https://docs.infrahub.app/schema-library/reference/vrf.md

# VRF

This schema extension contains models to support VRF in your network.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### VRF[​](#vrf "Direct link to VRF")

* **Label:** VRF
* **Description:** A VRF is isolated layer three domain
* **Namespace:** Ipam
* **Icon:** mdi
  <!-- -->
  :router
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text | False    |                |         |
| vrf\_rd     |             | Text | True     |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name       | peer               | optional | cardinality | kind      |
| ---------- | ------------------ | -------- | ----------- | --------- |
| namespace  | BuiltinIPNamespace | False    | one         | Attribute |
| import\_rt | IpamRouteTarget    | True     | one         | Attribute |
| export\_rt | IpamRouteTarget    | True     | one         | Attribute |

### RouteTarget[​](#routetarget "Direct link to RouteTarget")

* **Label:** Route Target
* **Description:** Route Target (RFC 4360)
* **Namespace:** Ipam
* **Icon:** mdi
  <!-- -->
  :target
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text |          |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name | peer    | optional | cardinality | kind |
| ---- | ------- | -------- | ----------- | ---- |
| vrf  | IpamVRF | True     | many        |      |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### IpamPrefix[​](#ipamprefix "Direct link to IpamPrefix")

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name | peer    | optional | cardinality | kind      |
| ---- | ------- | -------- | ----------- | --------- |
| vrf  | IpamVRF | True     | one         | Attribute |

### IpamIPAddress[​](#ipamipaddress "Direct link to IpamIPAddress")

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name | peer    | optional | cardinality | kind      |
| ---- | ------- | -------- | ----------- | --------- |
| vrf  | IpamVRF | True     | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: VRF
  namespace: Ipam
  description: A VRF is isolated layer three domain
  label: VRF
  icon: mdi:router
  human_friendly_id:
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    optional: false
    unique: true
  - name: vrf_rd
    label: Route Distinguisher
    kind: Text
    optional: true
  - name: description
    kind: Text
    optional: true
    order_weight: 1200
  relationships:
  - name: namespace
    peer: BuiltinIPNamespace
    optional: false
    cardinality: one
    kind: Attribute
  - name: import_rt
    identifier: vrf__import
    label: Import Targets
    peer: IpamRouteTarget
    optional: true
    cardinality: one
    kind: Attribute
  - name: export_rt
    identifier: vrf__export
    label: Export Targets
    peer: IpamRouteTarget
    optional: true
    cardinality: one
    kind: Attribute
- name: RouteTarget
  namespace: Ipam
  description: Route Target (RFC 4360)
  label: Route Target
  icon: mdi:target
  menu_placement: IpamVRF
  human_friendly_id:
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    unique: true
  - name: description
    kind: Text
    optional: true
  relationships:
  - name: vrf
    peer: IpamVRF
    optional: true
    cardinality: many
extensions:
  nodes:
  - kind: IpamPrefix
    relationships:
    - name: vrf
      label: VRF
      peer: IpamVRF
      optional: true
      cardinality: one
      kind: Attribute
      order_weight: 1150
  - kind: IpamIPAddress
    relationships:
    - name: vrf
      label: VRF
      peer: IpamVRF
      optional: true
      cardinality: one
      kind: Attribute
      order_weight: 1150
```
