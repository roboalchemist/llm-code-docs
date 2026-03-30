# Source: https://docs.infrahub.app/schema-library/reference/cluster.md

# Cluster

This schema extension contains the foundations to capture clusters. With this one in place you can unlock various clusters flavors (hosting cluster able to host VMs, firewall clusters built with specific appliances ...)

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/compute](/schema-library/reference/compute.md)

## Generics[​](#generics "Direct link to Generics")

### Generic[​](#generic "Direct link to Generic")

* **Label:** Clusters
* **Description:** A cluster of machines hosting services or other machines.
* **Namespace:** Cluster
* **Icon:** mdi
  <!-- -->
  :dots-hexagon
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description          | kind | optional | default\_value | choices |
| ----------- | -------------------- | ---- | -------- | -------------- | ------- |
| name        | Name of the cluster. | Text |          |                |         |
| description |                      | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name     | peer            | optional | cardinality | kind      |
| -------- | --------------- | -------- | ----------- | --------- |
| location | LocationGeneric | False    | many        | Attribute |
| tags     | BuiltinTag      | True     | many        | Attribute |

### GenericComputeUnitNodes[​](#genericcomputeunitnodes "Direct link to GenericComputeUnitNodes")

* **Description:** A generic to apply on clusters that can be built out of generic compute units.
* **Namespace:** Cluster

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name  | peer               | optional | cardinality | kind      |
| ----- | ------------------ | -------- | ----------- | --------- |
| nodes | ComputeGenericUnit |          | many        | Component |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### ComputeGenericUnit[​](#computegenericunit "Direct link to ComputeGenericUnit")

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name                | peer                           | optional | cardinality | kind |
| ------------------- | ------------------------------ | -------- | ----------- | ---- |
| worker\_in\_cluster | ClusterGenericComputeUnitNodes | True     | one         |      |

### LocationGeneric[​](#locationgeneric "Direct link to LocationGeneric")

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name     | peer           | optional | cardinality | kind      |
| -------- | -------------- | -------- | ----------- | --------- |
| clusters | ClusterGeneric | True     | many        | Component |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: Generic
  namespace: Cluster
  description: A cluster of machines hosting services or other machines.
  label: Clusters
  icon: mdi:dots-hexagon
  human_friendly_id:
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    description: Name of the cluster.
    unique: true
    order_weight: 1000
  - name: description
    kind: Text
    optional: true
  relationships:
  - name: location
    label: Location
    peer: LocationGeneric
    optional: false
    cardinality: many
    kind: Attribute
    order_weight: 1400
  - name: tags
    peer: BuiltinTag
    optional: true
    cardinality: many
    kind: Attribute
    order_weight: 2000
- name: GenericComputeUnitNodes
  namespace: Cluster
  description: A generic to apply on clusters that can be built out of generic compute
    units.
  include_in_menu: false
  relationships:
  - name: nodes
    label: Nodes
    identifier: worker_in_cluster
    cardinality: many
    peer: ComputeGenericUnit
    kind: Component
extensions:
  nodes:
  - kind: ComputeGenericUnit
    relationships:
    - name: worker_in_cluster
      identifier: worker_in_cluster
      label: Worker in cluster
      peer: ClusterGenericComputeUnitNodes
      cardinality: one
      description: This device is a worker node of the specified cluster.
      optional: true
  - kind: LocationGeneric
    relationships:
    - name: clusters
      label: Clusters
      peer: ClusterGeneric
      cardinality: many
      kind: Component
      description: All clusters available on that location.
      optional: true
```
