# Source: https://docs.infrahub.app/schema-library/reference/tenancy.md

# Tenancy

This schema extension introduces tenancy for some of the schema nodes (circuits...)

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/circuit](/schema-library/reference/circuit.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Tenant[​](#tenant "Direct link to Tenant")

* **Description:** A tenant is owning the corresponding entity
* **Namespace:** Tenancy
* **Icon:** mdi
  <!-- -->
  :domain
* **Inherit From:** OrganizationGeneric

#### Relationships[​](#relationships "Direct link to Relationships")

| name     | peer             | optional | cardinality | kind      |
| -------- | ---------------- | -------- | ----------- | --------- |
| tags     | BuiltinTag       | True     | many        | Attribute |
| location | LocationBuilding | True     | many        |           |
| circuit  | DcimCircuit      | True     | many        |           |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: Tenant
  namespace: Tenancy
  description: A tenant is owning the corresponding entity
  icon: mdi:domain
  include_in_menu: true
  inherit_from:
  - OrganizationGeneric
  relationships:
  - name: tags
    peer: BuiltinTag
    cardinality: many
    kind: Attribute
    optional: true
    order_weight: 3000
  - name: location
    peer: LocationBuilding
    cardinality: many
    optional: true
  - name: circuit
    peer: DcimCircuit
    cardinality: many
    optional: true
```
