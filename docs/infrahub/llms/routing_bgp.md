# Source: https://docs.infrahub.app/schema-library/reference/routing_bgp.md

# Routing BGP

This schema extension contains all you need to model your BGP platform.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)

## Nodes[​](#nodes "Direct link to Nodes")

### AutonomousSystem[​](#autonomoussystem "Direct link to AutonomousSystem")

* **Label:** Autonomous System
* **Description:** An Autonomous System (AS) is a set of Internet routable IP prefixes belonging to a network
* **Namespace:** Routing
* **Icon:** mdi
  <!-- -->
  :bank-circle-outline
* **Display Labels:** asn\_\_value, name\_\_value
* **Human Friendly ID:** asn\_\_value, name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description                          | kind   | optional | default\_value | choices |
| ----------- | ------------------------------------ | ------ | -------- | -------------- | ------- |
| name        | Name of the Autonomous System        | Text   |          |                |         |
| asn         | Autonomous System Number             | Number |          |                |         |
| description | Description of the Autonomous System | Text   | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name         | peer                | optional | cardinality | kind      |
| ------------ | ------------------- | -------- | ----------- | --------- |
| organization | OrganizationGeneric | False    | one         | Attribute |
| location     | LocationGeneric     | True     | one         | Attribute |
| devices      | DcimDevice          | True     | many        | Attribute |

### BGPPeerGroup[​](#bgppeergroup "Direct link to BGPPeerGroup")

* **Label:** BGP Peer Group
* **Description:** A BGP Peer Group is used to regroup parameters that are shared across multiple peers
* **Namespace:** Routing
* **Icon:** mdi
  <!-- -->
  :view-grid-plus-outline
* **Display Labels:** name\_\_value, description\_\_value
* **Human Friendly ID:** name\_\_value, description\_\_value
* **Inherit From:** RoutingProtocol

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name             | description                                                                  | kind     | optional | default\_value | choices    |
| ---------------- | ---------------------------------------------------------------------------- | -------- | -------- | -------------- | ---------- |
| name             | Name of the BGP Group                                                        | Text     | False    |                |            |
| import\_policies |                                                                              | Text     | True     |                |            |
| export\_policies |                                                                              | Text     | True     |                |            |
| maximum\_routes  | Maximum routes for the BGP Group.                                            | Number   | True     |                |            |
| local\_pref      | Force Local Pref for this BGP Peer Group.                                    | Number   | True     |                |            |
| send\_community  | Whether to send community attributes.                                        | Checkbox | True     |                |            |
| address\_family  | The address family for the routing policy indicating the type of IP address. | Dropdown |          | ipv4           | ipv4, ipv6 |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name       | peer                    | optional | cardinality | kind      |
| ---------- | ----------------------- | -------- | ----------- | --------- |
| local\_as  | RoutingAutonomousSystem | True     | one         | Attribute |
| remote\_as | RoutingAutonomousSystem | True     | one         | Attribute |

### BGPSession[​](#bgpsession "Direct link to BGPSession")

* **Label:** BGP Session
* **Description:** A BGP Session represent a point to point connection between two routers
* **Namespace:** Routing
* **Icon:** mdi
  <!-- -->
  :router
* **Display Labels:** description\_\_value
* **Inherit From:** RoutingProtocol

#### Attributes[​](#attributes-2 "Direct link to Attributes")

| name             | description                                 | kind     | optional | default\_value | choices                     |
| ---------------- | ------------------------------------------- | -------- | -------- | -------------- | --------------------------- |
| import\_policies |                                             | Text     | True     |                |                             |
| export\_policies |                                             | Text     | True     |                |                             |
| session\_type    | Type of BGP Session                         | Text     |          |                |                             |
| role             | Role of the BGP Session                     | Dropdown |          |                | backbone, upstream, peering |
| local\_pref      | Force Local Pref for this BGP Peer Session. | Number   | True     |                |                             |

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name          | peer                    | optional | cardinality | kind      |
| ------------- | ----------------------- | -------- | ----------- | --------- |
| local\_as     | RoutingAutonomousSystem | True     | one         | Attribute |
| remote\_as    | RoutingAutonomousSystem | True     | one         | Attribute |
| local\_ip     | IpamIPAddress           | True     | one         | Attribute |
| remote\_ip    | IpamIPAddress           | True     | one         | Attribute |
| device        | DcimDevice              | True     | one         |           |
| peer\_group   | RoutingBGPPeerGroup     | True     | one         | Attribute |
| peer\_session | RoutingBGPSession       | True     | one         | Attribute |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### DcimGenericDevice[​](#dcimgenericdevice "Direct link to DcimGenericDevice")

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name | peer                    | optional | cardinality | kind      |
| ---- | ----------------------- | -------- | ----------- | --------- |
| asn  | RoutingAutonomousSystem | True     | one         | Attribute |

### OrganizationGeneric[​](#organizationgeneric "Direct link to OrganizationGeneric")

#### Relationships[​](#relationships-4 "Direct link to Relationships")

| name | peer                    | optional | cardinality | kind |
| ---- | ----------------------- | -------- | ----------- | ---- |
| asn  | RoutingAutonomousSystem | True     | many        |      |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: AutonomousSystem
  namespace: Routing
  description: An Autonomous System (AS) is a set of Internet routable IP prefixes
    belonging to a network
  label: Autonomous System
  icon: mdi:bank-circle-outline
  menu_placement: RoutingBGPSession
  human_friendly_id:
  - asn__value
  - name__value
  order_by:
  - asn__value
  - name__value
  display_labels:
  - asn__value
  - name__value
  attributes:
  - name: name
    kind: Text
    description: Name of the Autonomous System
    order_weight: 1000
    unique: true
  - name: asn
    kind: Number
    description: Autonomous System Number
    order_weight: 1050
    unique: true
  - name: description
    kind: Text
    optional: true
    description: Description of the Autonomous System
    order_weight: 1100
  relationships:
  - name: organization
    peer: OrganizationGeneric
    optional: false
    cardinality: one
    kind: Attribute
  - name: location
    peer: LocationGeneric
    optional: true
    cardinality: one
    kind: Attribute
  - name: devices
    peer: DcimDevice
    optional: true
    cardinality: many
    kind: Attribute
- name: BGPPeerGroup
  namespace: Routing
  description: A BGP Peer Group is used to regroup parameters that are shared across
    multiple peers
  label: BGP Peer Group
  icon: mdi:view-grid-plus-outline
  menu_placement: RoutingBGPSession
  inherit_from:
  - RoutingProtocol
  human_friendly_id:
  - name__value
  - description__value
  order_by:
  - name__value
  display_labels:
  - name__value
  - description__value
  attributes:
  - name: name
    kind: Text
    optional: false
    unique: true
    description: Name of the BGP Group
    order_weight: 1000
  - name: import_policies
    kind: Text
    optional: true
    order_weight: 1300
  - name: export_policies
    kind: Text
    optional: true
    order_weight: 1350
  - name: maximum_routes
    kind: Number
    optional: true
    description: Maximum routes for the BGP Group.
    order_weight: 1400
    regex: ^[0-9]+$
  - name: local_pref
    kind: Number
    optional: true
    description: Force Local Pref for this BGP Peer Group.
    order_weight: 1450
    regex: ^[0-9]+$
  - name: send_community
    kind: Checkbox
    optional: true
    description: Whether to send community attributes.
    order_weight: 1500
  - name: address_family
    description: The address family for the routing policy indicating the type of
      IP address.
    kind: Dropdown
    choices:
    - name: ipv4
      label: IPv4
      description: Policy applies to IPv4 addresses.
      color: '#E6E6FA'
    - name: ipv6
      label: IPv6
      description: Policy applies to IPv6 addresses.
      color: '#E6E6FA'
    default_value: ipv4
    order_weight: 1150
  relationships:
  - name: local_as
    identifier: bgppeergroup__local_as
    peer: RoutingAutonomousSystem
    optional: true
    cardinality: one
    kind: Attribute
  - name: remote_as
    identifier: bgppeergroup__remote_as
    peer: RoutingAutonomousSystem
    optional: true
    cardinality: one
    kind: Attribute
- name: BGPSession
  namespace: Routing
  description: A BGP Session represent a point to point connection between two routers
  label: BGP Session
  icon: mdi:router
  inherit_from:
  - RoutingProtocol
  order_by:
  - remote_as__asn__value
  display_labels:
  - description__value
  attributes:
  - name: import_policies
    kind: Text
    optional: true
  - name: export_policies
    kind: Text
    optional: true
  - name: session_type
    kind: Text
    enum:
    - EXTERNAL
    - INTERNAL
    description: Type of BGP Session
    order_weight: 1200
  - name: role
    kind: Dropdown
    choices:
    - name: backbone
      label: Backbone
      description: Provide main data routes.
      color: '#E6E6FA'
    - name: upstream
      label: Upstream
      description: Connect to Internet service provider.
      color: '#E6E6FA'
    - name: peering
      label: Peering
      description: Connect with other networks via IX.
      color: '#E6E6FA'
    description: Role of the BGP Session
    order_weight: 1600
  - name: local_pref
    kind: Number
    optional: true
    description: Force Local Pref for this BGP Peer Session.
    order_weight: 1450
    regex: ^[0-9]+$
  relationships:
  - name: local_as
    identifier: bgpsession__local_as
    peer: RoutingAutonomousSystem
    optional: true
    cardinality: one
    kind: Attribute
  - name: remote_as
    identifier: bgpsession__remote_as
    peer: RoutingAutonomousSystem
    optional: true
    cardinality: one
    kind: Attribute
  - name: local_ip
    identifier: bgpsession__local_ip
    peer: IpamIPAddress
    optional: true
    cardinality: one
    kind: Attribute
  - name: remote_ip
    identifier: bgpsession__remote_ip
    peer: IpamIPAddress
    optional: true
    cardinality: one
    kind: Attribute
  - name: device
    peer: DcimDevice
    optional: true
    cardinality: one
  - name: peer_group
    peer: RoutingBGPPeerGroup
    optional: true
    cardinality: one
    kind: Attribute
  - name: peer_session
    peer: RoutingBGPSession
    optional: true
    cardinality: one
    kind: Attribute
extensions:
  nodes:
  - kind: DcimGenericDevice
    relationships:
    - name: asn
      peer: RoutingAutonomousSystem
      optional: true
      cardinality: one
      kind: Attribute
      order_weight: 1600
  - kind: OrganizationGeneric
    relationships:
    - name: asn
      label: Autonomous System
      cardinality: many
      optional: true
      peer: RoutingAutonomousSystem
      order_weight: 2000
```
