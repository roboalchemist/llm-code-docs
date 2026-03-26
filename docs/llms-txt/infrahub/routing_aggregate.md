# Source: https://docs.infrahub.app/schema-library/reference/routing_aggregate.md

# Routing Aggregate

This schema extension contains all you need to model the Aggregate Routing Protocol.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)

## Nodes[​](#nodes "Direct link to Nodes")

### AggregateRoute[​](#aggregateroute "Direct link to AggregateRoute")

* **Label:** Aggregate Routes
* **Description:** Aggregate Protocol with action and BGP communities
* **Namespace:** Routing
* **Icon:** grommet-icons
  <!-- -->
  :aggregate
* **Inherit From:** RoutingProtocol

#### Attributes[​](#attributes "Direct link to Attributes")

| name             | description | kind    | optional | default\_value | choices |
| ---------------- | ----------- | ------- | -------- | -------------- | ------- |
| discard          |             | Boolean | True     | False          |         |
| import\_policies |             | Text    | True     |                |         |
| export\_policies |             | Text    | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name        | peer       | optional | cardinality | kind      |
| ----------- | ---------- | -------- | ----------- | --------- |
| destination | IpamPrefix |          |             | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: AggregateRoute
  namespace: Routing
  description: Aggregate Protocol with action and BGP communities
  label: Aggregate Routes
  include_in_menu: false
  icon: grommet-icons:aggregate
  inherit_from:
  - RoutingProtocol
  attributes:
  - name: discard
    label: Discard
    kind: Boolean
    optional: true
    default_value: false
    order_weight: 1275
  - name: import_policies
    kind: Text
    optional: true
    order_weight: 1300
  - name: export_policies
    kind: Text
    optional: true
    order_weight: 1350
  relationships:
  - name: destination
    kind: Attribute
    peer: IpamPrefix
    description: Destination network for the static route.
    order_weight: 1200
```
