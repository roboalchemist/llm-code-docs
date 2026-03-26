# Source: https://docs.infrahub.app/schema-library/reference/routing_policies_ospf.md

# Routing Policies OSPF

This extension is using the Routing Policies extensions and the Routing OSPF one together.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)
  * [extensions/routing\_policies](/schema-library/reference/routing_policies.md)
  * [extensions/routing\_ospf](/schema-library/reference/routing_ospf.md)

## Nodes[​](#nodes "Direct link to Nodes")

### PolicyOSPF[​](#policyospf "Direct link to PolicyOSPF")

* **Label:** OSPF Routing Policies
* **Description:** A routing policiers for OSPF
* **Namespace:** Routing
* **Icon:** carbon
  <!-- -->
  :deployment-policy
* **Inherit From:** RoutingPolicy

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### RoutingOSPF[​](#routingospf "Direct link to RoutingOSPF")

#### Attributes[​](#attributes "Direct link to Attributes")

| name             | description | kind | optional | default\_value | choices |
| ---------------- | ----------- | ---- | -------- | -------------- | ------- |
| import\_policies |             | Text |          |                |         |
| export\_policies |             | Text |          |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name                      | peer              | optional | cardinality | kind    |
| ------------------------- | ----------------- | -------- | ----------- | ------- |
| import\_routing\_policies | RoutingPolicyOSPF |          | many        | Generic |
| export\_routing\_policies | RoutingPolicyOSPF |          | many        | Generic |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: PolicyOSPF
  namespace: Routing
  description: A routing policiers for OSPF
  label: OSPF Routing Policies
  icon: carbon:deployment-policy
  include_in_menu: false
  inherit_from:
  - RoutingPolicy
extensions:
  nodes:
  - kind: RoutingOSPF
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
      peer: RoutingPolicyOSPF
      identifier: ospf__import_policies
      description: The routing-policies used by this instance for import.
      kind: Generic
      cardinality: many
    - name: export_routing_policies
      label: Export Routing Policies
      peer: RoutingPolicyOSPF
      identifier: ospf__export_policies
      description: The routing-policies used by this instance for export.
      kind: Generic
      cardinality: many
```
