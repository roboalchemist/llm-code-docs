# Source: https://docs.infrahub.app/schema-library/reference/routing_policies_pim.md

# Routing Policies (PIM)

This schema inherits the `RoutingPolicy` schema and removes `import_policies` and `export_policies` attributes. However it adds a number of relationships to `RoutingPIM`.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)
  * [extensions/routing\_policies](/schema-library/reference/routing_policies.md)
  * [extensions/routing\_pim](/schema-library/reference/routing_pim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### PolicyPIM[​](#policypim "Direct link to PolicyPIM")

* **Label:** PIM Routing Policies
* **Description:** A routing policiers for PIM
* **Namespace:** Routing
* **Icon:** carbon
  <!-- -->
  :deployment-policy
* **Inherit From:** RoutingPolicy

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### RoutingPIM[​](#routingpim "Direct link to RoutingPIM")

#### Attributes[​](#attributes "Direct link to Attributes")

| name             | description | kind | optional | default\_value | choices |
| ---------------- | ----------- | ---- | -------- | -------------- | ------- |
| import\_policies |             | Text |          |                |         |
| export\_policies |             | Text |          |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name                      | peer             | optional | cardinality | kind    |
| ------------------------- | ---------------- | -------- | ----------- | ------- |
| import\_routing\_policies | RoutingPolicyPIM |          | many        | Generic |
| export\_routing\_policies | RoutingPolicyPIM |          | many        | Generic |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: PolicyPIM
  namespace: Routing
  description: A routing policiers for PIM
  label: PIM Routing Policies
  icon: carbon:deployment-policy
  include_in_menu: false
  inherit_from:
  - RoutingPolicy
extensions:
  nodes:
  - kind: RoutingPIM
    attributes:
    - name: import_policies
      kind: Text
      state: absent
    - name: export_policies
      kind: Text
      state: absent
    relationships:
    - name: import_routing_policies
      label: Import Routing Policies
      peer: RoutingPolicyPIM
      identifier: pim__import_policies
      description: The routing-policies used by this instance for import.
      kind: Generic
      cardinality: many
    - name: export_routing_policies
      label: Export Routing Policies
      peer: RoutingPolicyPIM
      identifier: pim__export_policies
      description: The routing-policies used by this instance for export.
      kind: Generic
      cardinality: many
```
