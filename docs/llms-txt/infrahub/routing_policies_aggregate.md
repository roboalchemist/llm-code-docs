# Source: https://docs.infrahub.app/schema-library/reference/routing_policies_aggregate.md

# Routing Policies Aggregate

This extension is using the Routing Policies extensions and the Routing Aggregate one together.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)
  * [extensions/routing\_policies](/schema-library/reference/routing_policies.md)
  * [extensions/routing\_aggregate](/schema-library/reference/routing_aggregate.md)

## Nodes[​](#nodes "Direct link to Nodes")

### PolicyAggregate[​](#policyaggregate "Direct link to PolicyAggregate")

* **Label:** Aggregate Routing Policies
* **Description:** A routing policiers for Aggregate
* **Namespace:** Routing
* **Icon:** carbon
  <!-- -->
  :deployment-policy
* **Inherit From:** RoutingPolicy

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: PolicyAggregate
  namespace: Routing
  description: A routing policiers for Aggregate
  label: Aggregate Routing Policies
  icon: carbon:deployment-policy
  include_in_menu: false
  inherit_from:
  - RoutingPolicy
```
