# Source: https://docs.infrahub.app/schema-library/reference/circuit.md

# Circuit

This schema extension contains Circuits and ways to connect them with your infrastructure! The circuit could be a fiber connecting two sites, you would then have two endpoints, one on each site.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/location\_minimal](/schema-library/reference/location_minimal.md)

## Nodes[​](#nodes "Direct link to Nodes")

### Circuit[​](#circuit "Direct link to Circuit")

* **Label:** Circuit
* **Description:** A Circuit represent service operated by a provider.
* **Namespace:** Dcim
* **Icon:** mdi
  <!-- -->
  :cable-data
* **Display Labels:** circuit\_id\_\_value
* **Human Friendly ID:** circuit\_id\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name          | description                    | kind     | optional | default\_value | choices                                    |
| ------------- | ------------------------------ | -------- | -------- | -------------- | ------------------------------------------ |
| circuit\_id   |                                | Text     |          |                |                                            |
| description   |                                | Text     | True     |                |                                            |
| circuit\_type | Specifies the type of circuit. | Dropdown |          |                | upstream, peering, dark\_fiber, mpls       |
| status        |                                | Dropdown |          |                | active, provisioning, maintenance, drained |

#### Relationships[​](#relationships "Direct link to Relationships")

| name     | peer                 | optional | cardinality | kind      |
| -------- | -------------------- | -------- | ----------- | --------- |
| provider | OrganizationProvider | False    | one         | Attribute |
| location | LocationHosting      | True     | one         | Attribute |
| enpoints | DcimCircuitEndpoint  | True     | many        | Component |

### CircuitEndpoint[​](#circuitendpoint "Direct link to CircuitEndpoint")

* **Label:** Circuit Endpoint
* **Description:** A circuit endpoint, could be a position in a MMR...
* **Namespace:** Dcim
* **Icon:** mdi
  <!-- -->
  :ethernet
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * circuit, name\_\_value
* **Human Friendly ID:** circuit\_\_circuit\_id\_\_value, name\_\_value
* **Inherit From:** DcimEndpoint

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name        | description                                                        | kind     | optional | default\_value | choices                                    |
| ----------- | ------------------------------------------------------------------ | -------- | -------- | -------------- | ------------------------------------------ |
| name        | Name of the circuit endoint, could be a MMR position for instance. | Text     |          |                |                                            |
| status      |                                                                    | Dropdown | True     |                | active, provisioning, maintenance, drained |
| description |                                                                    | Text     | True     |                |                                            |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name     | peer            | optional | cardinality | kind      |
| -------- | --------------- | -------- | ----------- | --------- |
| circuit  | DcimCircuit     | False    | one         | Parent    |
| location | LocationHosting | False    | one         | Attribute |

## Extensions[​](#extensions "Direct link to Extensions")

note

In this context "extensions" refer to modifications or additions to the existing schema, such as adding new attributes, relationships, or other schema elements.

### OrganizationProvider[​](#organizationprovider "Direct link to OrganizationProvider")

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name     | peer        | optional | cardinality | kind |
| -------- | ----------- | -------- | ----------- | ---- |
| circuits | DcimCircuit | True     | many        |      |

### LocationHosting[​](#locationhosting "Direct link to LocationHosting")

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name     | peer        | optional | cardinality | kind |
| -------- | ----------- | -------- | ----------- | ---- |
| circuits | DcimCircuit | True     | many        |      |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: Circuit
  namespace: Dcim
  description: A Circuit represent service operated by a provider.
  label: Circuit
  icon: mdi:cable-data
  human_friendly_id:
  - circuit_id__value
  order_by:
  - circuit_id__value
  display_labels:
  - circuit_id__value
  attributes:
  - name: circuit_id
    kind: Text
    unique: true
  - name: description
    kind: Text
    optional: true
  - name: circuit_type
    kind: Dropdown
    description: Specifies the type of circuit.
    choices:
    - name: upstream
      label: Upstream
      description: Connection to an upstream provider or Internet service provider
        (ISP)
      color: '#1e90ff'
    - name: peering
      label: Peering
      description: Connection to another network for exchange of traffic
      color: '#20b2aa'
    - name: dark_fiber
      label: Dark Fiber
      description: Leased, unlit fiber for customer management and operation
      color: '#333333'
    - name: mpls
      label: MPLS
      description: Multi-Protocol Label Switching circuit for QoS-based routing
      color: '#7f00ff'
  - name: status
    kind: Dropdown
    choices:
    - name: active
      label: Active
      description: Fully operational and currently in service.
      color: '#7fbf7f'
    - name: provisioning
      label: Provisioning
      description: In the process of being set up and configured.
      color: '#ffff7f'
    - name: maintenance
      label: Maintenance
      description: Undergoing routine maintenance or repairs.
      color: '#ffd27f'
    - name: drained
      label: Drained
      description: Temporarily taken out of service.
      color: '#bfbfbf'
  relationships:
  - name: provider
    peer: OrganizationProvider
    optional: false
    cardinality: one
    kind: Attribute
  - name: location
    label: Location
    peer: LocationHosting
    optional: true
    cardinality: one
    kind: Attribute
    order_weight: 1500
  - name: enpoints
    peer: DcimCircuitEndpoint
    optional: true
    cardinality: many
    kind: Component
- name: CircuitEndpoint
  namespace: Dcim
  description: A circuit endpoint, could be a position in a MMR...
  label: Circuit Endpoint
  inherit_from:
  - DcimEndpoint
  icon: mdi:ethernet
  menu_placement: DcimCircuit
  human_friendly_id:
  - circuit__circuit_id__value
  - name__value
  uniqueness_constraints:
  - - circuit
    - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
    description: Name of the circuit endoint, could be a MMR position for instance.
    order_weight: 1000
  - name: status
    kind: Dropdown
    optional: true
    choices:
    - name: active
      label: Active
      description: Fully operational and currently in service.
      color: '#7fbf7f'
    - name: provisioning
      label: Provisioning
      description: In the process of being set up and configured.
      color: '#ffff7f'
    - name: maintenance
      label: Maintenance
      description: Undergoing routine maintenance or repairs.
      color: '#ffd27f'
    - name: drained
      label: Drained
      description: Temporarily taken out of service.
      color: '#bfbfbf'
  - name: description
    kind: Text
    optional: true
  relationships:
  - name: circuit
    peer: DcimCircuit
    order_weight: 900
    optional: false
    cardinality: one
    kind: Parent
  - name: location
    label: Location
    peer: LocationHosting
    optional: false
    cardinality: one
    kind: Attribute
    order_weight: 1500
extensions:
  nodes:
  - kind: OrganizationProvider
    relationships:
    - name: circuits
      peer: DcimCircuit
      cardinality: many
      optional: true
  - kind: LocationHosting
    relationships:
    - name: circuits
      peer: DcimCircuit
      cardinality: many
      optional: true
```
