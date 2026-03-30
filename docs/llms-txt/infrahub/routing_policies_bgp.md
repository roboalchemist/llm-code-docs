# Source: https://docs.infrahub.app/schema-library/reference/routing_policies_bgp.md

# Routing Policies BGP

This extension is using the Routing Policies extensions and the Routing BGP one together.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/routing](/schema-library/reference/routing.md)
  * [extensions/routing\_policies](/schema-library/reference/routing_policies.md)
  * [extensions/routing\_bgp](/schema-library/reference/routing_bgp.md)

## Nodes[​](#nodes "Direct link to Nodes")

### PolicyBGP[​](#policybgp "Direct link to PolicyBGP")

* **Label:** BGP Routing Policies
* **Description:** A routing policiers for BGP
* **Namespace:** Routing
* **Icon:** carbon
  <!-- -->
  :deployment-policy
* **Inherit From:** RoutingPolicy

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### RoutingBGPPeerGroup[​](#routingbgppeergroup "Direct link to RoutingBGPPeerGroup")

#### Attributes[​](#attributes "Direct link to Attributes")

| name             | description | kind | optional | default\_value | choices |
| ---------------- | ----------- | ---- | -------- | -------------- | ------- |
| import\_policies |             | Text |          |                |         |
| export\_policies |             | Text |          |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name                      | peer             | optional | cardinality | kind    |
| ------------------------- | ---------------- | -------- | ----------- | ------- |
| import\_routing\_policies | RoutingPolicyBGP |          | many        | Generic |
| export\_routing\_policies | RoutingPolicyBGP |          | many        | Generic |

### RoutingBGPSession[​](#routingbgpsession "Direct link to RoutingBGPSession")

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name             | description | kind | optional | default\_value | choices |
| ---------------- | ----------- | ---- | -------- | -------------- | ------- |
| import\_policies |             | Text |          |                |         |
| export\_policies |             | Text |          |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name                      | peer          | optional | cardinality | kind    |
| ------------------------- | ------------- | -------- | ----------- | ------- |
| import\_routing\_policies | RoutingPolicy |          | many        | Generic |
| export\_routing\_policies | RoutingPolicy |          | many        | Generic |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: PolicyBGP
  namespace: Routing
  description: A routing policiers for BGP
  label: BGP Routing Policies
  icon: carbon:deployment-policy
  include_in_menu: false
  inherit_from:
  - RoutingPolicy
extensions:
  nodes:
  - kind: RoutingBGPPeerGroup
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
      peer: RoutingPolicyBGP
      identifier: bgp__import_policies
      description: The routing-policies used by this instance for import.
      kind: Generic
      cardinality: many
    - name: export_routing_policies
      label: Export Routing Policies
      peer: RoutingPolicyBGP
      identifier: bgp__export_policies
      description: The routing-policies used by this instance for export.
      kind: Generic
      cardinality: many
  - kind: RoutingBGPSession
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
      peer: RoutingPolicy
      identifier: bgp__import_policies
      description: The routing-policies used by this instance for import.
      kind: Generic
      cardinality: many
    - name: export_routing_policies
      label: Export Routing Policies
      peer: RoutingPolicy
      identifier: bgp__export_policies
      description: The routing-policies used by this instance for export.
      kind: Generic
      cardinality: many
```
