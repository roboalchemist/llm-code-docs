# Source: https://docs.infrahub.app/schema-library/reference/routing_ospf.md

# Routing OSPF

This schema extension contains all you need to model the OSPF Routing Protocol.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)

## Nodes[​](#nodes "Direct link to Nodes")

### OSPF[​](#ospf "Direct link to OSPF")

* **Label:** OSPF
* **Description:** OSPF (Open Shortest Path First) instance on a Virtual Router.
* **Namespace:** Routing
* **Icon:** mdi
  <!-- -->
  :network-outline
* **Display Labels:** description\_\_value
* **Uniqueness Constraints:**
  * device, vrf, version\_\_value
* **Human Friendly ID:** device\_\_name\_\_value, vrf\_\_name\_\_value, version\_\_value
* **Inherit From:** RoutingProtocol

#### Attributes[​](#attributes "Direct link to Attributes")

| name                 | description                                      | kind     | optional | default\_value | choices      |
| -------------------- | ------------------------------------------------ | -------- | -------- | -------------- | ------------ |
| reference\_bandwidth | Reference bandwidth for OSPF instance (in Mbps). | Number   | True     | 1000           |              |
| version              | Version of the OSPF protocol.                    | Dropdown |          | ospf           | ospf, ospfv3 |
| import\_policies     |                                                  | Text     | True     |                |              |
| export\_policies     |                                                  | Text     | True     |                |              |

#### Relationships[​](#relationships "Direct link to Relationships")

| name             | peer                 | optional | cardinality | kind      |
| ---------------- | -------------------- | -------- | ----------- | --------- |
| router\_id       | IpamIPAddress        | True     | one         | Attribute |
| ospf\_interfaces | RoutingOSPFInterface | True     | many        | Component |

### OSPFInterface[​](#ospfinterface "Direct link to OSPFInterface")

* **Label:** OSPF Interface
* **Description:** Pivot table linking OSPF configuration to an interface.
* **Namespace:** Routing
* **Icon:** mdi
  <!-- -->
  :ethernet
* **Display Labels:** description\_\_value
* **Uniqueness Constraints:**
  * ospf, interface
* **Human Friendly ID:** description\_\_value

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name                 | description                                                                                 | kind     | optional | default\_value | choices                         |
| -------------------- | ------------------------------------------------------------------------------------------- | -------- | -------- | -------------- | ------------------------------- |
| description          | Description of the OSPF interface.                                                          | Text     | False    |                |                                 |
| metric               | OSPF metric for the interface.                                                              | Number   | True     |                |                                 |
| mode                 | Mode of the OSPF interface.                                                                 | Dropdown |          | normal         | normal, passive, peer\_to\_peer |
| authentication\_key  | Shared secret used to authenticate and secure routing messages between neighboring routers. | Password | True     |                |                                 |
| authentication\_mode |                                                                                             | Dropdown | True     |                | md5, sha1                       |
| area                 | OSPF area associated with the interface.                                                    | Text     |          |                |                                 |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name      | peer            | optional | cardinality | kind      |
| --------- | --------------- | -------- | ----------- | --------- |
| ospf      | RoutingOSPF     | False    | one         | Parent    |
| interface | InterfaceLayer3 | False    | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: OSPF
  namespace: Routing
  description: OSPF (Open Shortest Path First) instance on a Virtual Router.
  label: OSPF
  icon: mdi:network-outline
  include_in_menu: false
  order_by:
  - router_id__address__value
  - vrf__name__value
  - device__name__value
  uniqueness_constraints:
  - - device
    - vrf
    - version__value
  human_friendly_id:
  - device__name__value
  - vrf__name__value
  - version__value
  display_labels:
  - description__value
  inherit_from:
  - RoutingProtocol
  attributes:
  - name: reference_bandwidth
    kind: Number
    optional: true
    default_value: 1000
    description: Reference bandwidth for OSPF instance (in Mbps).
    order_weight: 1150
  - name: version
    kind: Dropdown
    choices:
    - name: ospf
      label: OSPFv2
      description: Open Shortest Path First version 2.
      color: '#E6E6FA'
    - name: ospfv3
      label: OSPFv3
      description: Open Shortest Path First version 3.
      color: '#E6E6FA'
    default_value: ospf
    description: Version of the OSPF protocol.
    order_weight: 1100
  - name: import_policies
    kind: Text
    optional: true
    order_weight: 1300
  - name: export_policies
    kind: Text
    optional: true
    order_weight: 1350
  relationships:
  - name: router_id
    peer: IpamIPAddress
    optional: true
    cardinality: one
    kind: Attribute
  - name: ospf_interfaces
    label: OSPF Interfaces
    peer: RoutingOSPFInterface
    identifier: ospf__ospfinterfaces
    optional: true
    cardinality: many
    kind: Component
- name: OSPFInterface
  namespace: Routing
  description: Pivot table linking OSPF configuration to an interface.
  label: OSPF Interface
  icon: mdi:ethernet
  include_in_menu: false
  order_by:
  - description__value
  display_labels:
  - description__value
  uniqueness_constraints:
  - - ospf
    - interface
  human_friendly_id:
  - description__value
  attributes:
  - name: description
    kind: Text
    optional: false
    unique: true
    description: Description of the OSPF interface.
    order_weight: 1500
  - name: metric
    kind: Number
    optional: true
    description: OSPF metric for the interface.
    order_weight: 1400
  - name: mode
    kind: Dropdown
    choices:
    - name: normal
      label: Normal
      description: Standard OSPF interface mode.
      color: '#E6E6FA'
    - name: passive
      label: Passive
      description: Interface will not send OSPF hello packets.
      color: '#E6E6FA'
    - name: peer_to_peer
      label: Peer-to-Peer
      description: OSPF peer-to-peer interface mode.
      color: '#E6E6FA'
    default_value: normal
    description: Mode of the OSPF interface.
    order_weight: 1300
  - name: authentication_key
    kind: Password
    description: Shared secret used to authenticate and secure routing messages between
      neighboring routers.
    optional: true
    order_weight: 1250
  - name: authentication_mode
    kind: Dropdown
    choices:
    - name: md5
      label: MD5
      color: '#E6E6FA'
    - name: sha1
      label: SHA1
      color: '#E6E6FA'
    optional: true
    order_weight: 1225
  - name: area
    kind: Text
    description: OSPF area associated with the interface.
    order_weight: 1200
  relationships:
  - name: ospf
    label: OSPF
    peer: RoutingOSPF
    identifier: ospf__ospfinterfaces
    optional: false
    cardinality: one
    kind: Parent
    order_weight: 1100
  - name: interface
    peer: InterfaceLayer3
    optional: false
    cardinality: one
    kind: Attribute
    order_weight: 1200
```
