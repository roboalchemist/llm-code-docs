# Source: https://docs.infrahub.app/schema-library/reference/circuit_service.md

# Circuit Service

This schema extension contains model coming on top of circuit to capture a single service shared across multiple circuits. For example you have a MPLS network supported by a provider connecting multiple locations:

* One single CircuitService would be needed to store MPLS related information (e.g. service id, provider ...)
* On each site we would create a circuit connecting on one side our device and the CircuitService on the other side

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [extensions/circuit](/schema-library/reference/circuit.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Service[​](#service "Direct link to Service")

* **Label:** Circuit Service
* **Description:** Represent the boundary of a provider network, the details of which are unknown or unimportant
* **Namespace:** Circuit
* **Icon:** mdi
  <!-- -->
  :cloud
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description | kind | optional | default\_value | choices |
| ----------- | ----------- | ---- | -------- | -------------- | ------- |
| name        |             | Text |          |                |         |
| service\_id |             | Text | True     |                |         |
| description |             | Text | True     |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name               | peer                 | optional | cardinality | kind      |
| ------------------ | -------------------- | -------- | ----------- | --------- |
| provider           | OrganizationProvider | False    | one         | Attribute |
| circuit\_endpoints | CircuitEndpoint      | True     | many        | Component |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### OrganizationProvider[​](#organizationprovider "Direct link to OrganizationProvider")

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name              | peer           | optional | cardinality | kind |
| ----------------- | -------------- | -------- | ----------- | ---- |
| circuit\_services | CircuitService | True     | many        |      |

### CircuitEndpoint[​](#circuitendpoint "Direct link to CircuitEndpoint")

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name             | peer           | optional | cardinality | kind |
| ---------------- | -------------- | -------- | ----------- | ---- |
| circuit\_service | CircuitService | True     | one         |      |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: Service
  namespace: Circuit
  description: Represent the boundary of a provider network, the details of which
    are unknown or unimportant
  label: Circuit Service
  icon: mdi:cloud
  menu_placement: DcimCircuit
  human_friendly_id:
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    unique: true
  - name: service_id
    kind: Text
    optional: true
  - name: description
    kind: Text
    optional: true
  relationships:
  - name: provider
    peer: OrganizationProvider
    optional: false
    cardinality: one
    kind: Attribute
  - name: circuit_endpoints
    peer: CircuitEndpoint
    optional: true
    cardinality: many
    kind: Component
extensions:
  nodes:
  - kind: OrganizationProvider
    relationships:
    - name: circuit_services
      peer: CircuitService
      cardinality: many
      optional: true
  - kind: CircuitEndpoint
    relationships:
    - name: circuit_service
      peer: CircuitService
      cardinality: one
      optional: true
```
