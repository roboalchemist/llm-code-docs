# Source: https://docs.infrahub.app/schema-library/reference/modules_routing_engine.md

# Modules Routing Engine

This schema extension allows you to capture Routing Engine related information like the version. You can insert the Routing Engine into a Dcim Physical Device and leverage the Routing Engine type model.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/modules](/schema-library/reference/modules.md)

## Nodes[​](#nodes "Direct link to Nodes")

### RoutingEngineType[​](#routingenginetype "Direct link to RoutingEngineType")

* **Label:** Routing Engine Type
* **Description:** Routing Engine Type information, detailing specifications such as part number and manufacturer.
* **Namespace:** Device
* **Inherit From:** DeviceGenericModuleType

#### Relationships[​](#relationships "Direct link to Relationships")

| name             | peer                | optional | cardinality | kind    |
| ---------------- | ------------------- | -------- | ----------- | ------- |
| routing\_engines | DeviceRoutingEngine |          | many        | Generic |

### RoutingEngine[​](#routingengine "Direct link to RoutingEngine")

* **Label:** Routing Engine
* **Description:** A Routing Engine (RE) installed in a device, responsible for routing functionalities.
* **Namespace:** Device
* **Icon:** mdi
  <!-- -->
  :cpu-64-bit
* **Display Labels:** serial\_number\_\_value
* **Uniqueness Constraints:**
  * serial\_number\_\_value
* **Human Friendly ID:** device\_\_name\_\_value, slot\_\_value
* **Inherit From:** DeviceGenericModule

#### Attributes[​](#attributes "Direct link to Attributes")

| name    | description                                                             | kind   | optional | default\_value | choices |
| ------- | ----------------------------------------------------------------------- | ------ | -------- | -------------- | ------- |
| slot    | The slot number where the Routing Engine is installed within the device | Number |          |                |         |
| version | Firmware version of the Routing Engine.                                 | Text   | True     |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name                  | peer                    | optional | cardinality | kind      |
| --------------------- | ----------------------- | -------- | ----------- | --------- |
| routing\_engine\_type | DeviceRoutingEngineType | False    | one         | Attribute |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: RoutingEngineType
  namespace: Device
  description: Routing Engine Type information, detailing specifications such as part
    number and manufacturer.
  label: Routing Engine Type
  inherit_from:
  - DeviceGenericModuleType
  relationships:
  - name: routing_engines
    peer: DeviceRoutingEngine
    cardinality: many
    kind: Generic
    description: Routing engines of this type.
- name: RoutingEngine
  namespace: Device
  description: A Routing Engine (RE) installed in a device, responsible for routing
    functionalities.
  label: Routing Engine
  icon: mdi:cpu-64-bit
  inherit_from:
  - DeviceGenericModule
  uniqueness_constraints:
  - - serial_number__value
  human_friendly_id:
  - device__name__value
  - slot__value
  order_by:
  - device__name__value
  - slot__value
  display_labels:
  - serial_number__value
  attributes:
  - name: slot
    kind: Number
    description: The slot number where the Routing Engine is installed within the
      device
    order_weight: 1100
  - name: version
    kind: Text
    label: Version
    description: Firmware version of the Routing Engine.
    optional: true
    order_weight: 1200
  relationships:
  - name: routing_engine_type
    label: RE Type
    peer: DeviceRoutingEngineType
    optional: false
    cardinality: one
    kind: Attribute
    order_weight: 1150
```
