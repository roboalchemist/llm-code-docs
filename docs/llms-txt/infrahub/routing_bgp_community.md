# Source: https://docs.infrahub.app/schema-library/reference/routing_bgp_community.md

# Routing BGP Community

This schema extension adds the BGP Communities models.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)

## Nodes[​](#nodes "Direct link to Nodes")

### BGPCommunity[​](#bgpcommunity "Direct link to BGPCommunity")

* **Label:** BGP Community
* **Description:** Defines a BGP community.
* **Namespace:** Routing
* **Icon:** iconoir
  <!-- -->
  :community
* **Display Labels:** name\_\_value, community\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description                                                 | kind | optional | default\_value | choices |
| ----------- | ----------------------------------------------------------- | ---- | -------- | -------------- | ------- |
| name        | The name of the BGP community.                              | Text |          |                |         |
| description | An optional description of the BGP community.               | Text | True     |                |         |
| community   | The value of the BGP community (RFC1997, RFC4360, RFC8092). | Text |          |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name            | peer          | optional | cardinality | kind      |
| --------------- | ------------- | -------- | ----------- | --------- |
| routing\_policy | RoutingPolicy |          | many        | Generic   |
| tags            | BuiltinTag    | True     | many        | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: BGPCommunity
  namespace: Routing
  icon: iconoir:community
  label: BGP Community
  description: Defines a BGP community.
  human_friendly_id:
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  - community__value
  attributes:
  - name: name
    kind: Text
    description: The name of the BGP community.
    order_weight: 1000
    unique: true
  - name: description
    kind: Text
    description: An optional description of the BGP community.
    optional: true
    order_weight: 1100
  - name: community
    kind: Text
    description: The value of the BGP community (RFC1997, RFC4360, RFC8092).
    order_weight: 1200
    unique: true
  relationships:
  - name: routing_policy
    label: Routing Policies
    peer: RoutingPolicy
    description: The BGP Policies using this BGP Community.
    kind: Generic
    cardinality: many
  - name: tags
    peer: BuiltinTag
    kind: Attribute
    optional: true
    cardinality: many
    order_weight: 3000
```
