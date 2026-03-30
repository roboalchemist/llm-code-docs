# Source: https://docs.infrahub.app/schema-library/reference/routing_bgp_rr.md

# Routing BGP RR

This schema extension extend the BGP extension to add BGP Route Reflector Clustering.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)
  * [extensions/routing\_bgp](/schema-library/reference/routing_bgp.md)

## Nodes[​](#nodes "Direct link to Nodes")

### BGPRRCluster[​](#bgprrcluster "Direct link to BGPRRCluster")

* **Label:** Route Reflector Cluster
* **Description:** A Route Reflector (RR) Cluster used for grouping internal peers
* **Namespace:** Routing
* **Icon:** mdi
  <!-- -->
  :router-network
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description                                         | kind | optional | default\_value | choices |
| ----------- | --------------------------------------------------- | ---- | -------- | -------------- | ------- |
| name        | Name of the Route Reflector Cluster                 | Text |          |                |         |
| description | Optional description of the Route Reflector Cluster | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name         | peer                | optional | cardinality | kind      |
| ------------ | ------------------- | -------- | ----------- | --------- |
| cluster\_id  | IpamIPAddress       | False    | one         | Attribute |
| peer\_groups | RoutingBGPPeerGroup | True     | many        | Generic   |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### RoutingBGPPeerGroup[​](#routingbgppeergroup "Direct link to RoutingBGPPeerGroup")

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name        | peer                | optional | cardinality | kind      |
| ----------- | ------------------- | -------- | ----------- | --------- |
| rr\_cluster | RoutingBGPRRCluster |          | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: BGPRRCluster
  namespace: Routing
  description: A Route Reflector (RR) Cluster used for grouping internal peers
  label: Route Reflector Cluster
  icon: mdi:router-network
  include_in_menu: false
  human_friendly_id:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    description: Name of the Route Reflector Cluster
    order_weight: 1000
    unique: true
  - name: description
    kind: Text
    description: Optional description of the Route Reflector Cluster
    optional: true
    order_weight: 1100
  relationships:
  - name: cluster_id
    label: Cluster ID
    peer: IpamIPAddress
    description: Cluster ID represented as a reference to an IP Address
    cardinality: one
    kind: Attribute
    optional: false
    order_weight: 1200
  - name: peer_groups
    label: BGP Peer Groups
    peer: RoutingBGPPeerGroup
    cardinality: many
    kind: Generic
    optional: true
extensions:
  nodes:
  - kind: RoutingBGPPeerGroup
    relationships:
    - name: rr_cluster
      label: RR Cluster
      peer: RoutingBGPRRCluster
      cardinality: one
      kind: Attribute
      order_weight: 1600
```
