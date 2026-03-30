# Source: https://docs.infrahub.app/schema-library/reference/topology.md

# Topology

This schema extension introduces abstract network pods and services running in the pods, such as MPLS and EVPN.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Generics[​](#generics "Direct link to Generics")

### Generic[​](#generic "Direct link to Generic")

* **Label:** Topology
* **Description:** Generic model for topology.
* **Namespace:** Topology
* **Icon:** carbon
  <!-- -->
  :network-3

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name     | peer            | optional | cardinality | kind      |
| -------- | --------------- | -------- | ----------- | --------- |
| location | LocationGeneric | True     | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: Generic
  namespace: Topology
  description: Generic model for topology.
  label: Topology
  icon: carbon:network-3
  attributes:
  - name: description
    kind: Text
    order_weight: 1300
    optional: true
  relationships:
  - name: location
    peer: LocationGeneric
    optional: true
    cardinality: one
    kind: Attribute
```
