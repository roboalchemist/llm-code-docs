# Source: https://docs.infrahub.app/guides/create-schema.md

# Creating a schema

This guide shows you how to create a new schema file for Infrahub. You'll learn to define data structures and relationships using a network device example with interfaces.

By following this guide, you'll build a complete schema that includes nodes, attributes, relationships, and generic abstractions. This example focuses on network devices to demonstrate key concepts, though real-world schemas involve additional complexity.

For conceptual background on schemas and design patterns, see [Schema](/topics/schema.md).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Infrahub running locally or in your environment
* [`infrahubctl`](/infrahubctl/infrahubctl.md) command-line tool installed
* Basic understanding of YAML syntax

Schema validation

Enable [schema validation](/reference/schema-validation.md) in your editor to catch errors while developing schema files.

## Alternative learning resources[​](#alternative-learning-resources "Direct link to Alternative learning resources")

### Hands-on lab[​](#hands-on-lab "Direct link to Hands-on lab")

Try the interactive [Infrahub Schema Introduction](https://opsmill.instruqt.com/pages/labs) lab for hands-on practice with schemas.

### Video tutorials[​](#video-tutorials "Direct link to Video tutorials")

Learn advanced schema concepts in this livestream recording:

## Step 1: Create basic nodes with attributes[​](#step-1-create-basic-nodes-with-attributes "Direct link to Step 1: Create basic nodes with attributes")

Create a file named `schema_guide.yml` in a location you can access easily, such as `/tmp/schema_guide.yml`.

Start by defining two basic nodes in the `Network` namespace:

* `Device`: Represents network devices with hostname and model attributes
* `Interface`: Represents network interfaces with name and description attributes

```
---
version: "1.0"
nodes:
  - name: Device
    namespace: Network
    human_friendly_id: ['hostname__value']
    attributes:
      - name: hostname
        kind: Text
        unique: true
      - name: model
        kind: Text
  - name: Interface
    namespace: Network
    attributes:
      - name: name
        kind: Text
      - name: description
        kind: Text
        optional: true
```

Human-friendly IDs

The `human_friendly_id` on the `hostname` attribute lets you use the hostname value instead of the system-generated ID in queries and mutations.

### Load the schema into Infrahub[​](#load-the-schema-into-infrahub "Direct link to Load the schema into Infrahub")

Create a new branch for your schema changes:

```
infrahubctl branch create network-device-schema
```

Load the schema into the branch:

```
infrahubctl schema load --branch network-device-schema /tmp/schema_guide.yml
```

View your schema in the [Web UI](http://localhost:8000/schema?branch=network-device-schema) under Object Management > Schemas.

![Schema page screenshot](/assets/images/create_schema_1-0c77748efef18604d3451c6b3609991d.png)

### Create test data[​](#create-test-data "Direct link to Create test data")

Test your schema by creating a device and interface:

* GraphQL
* Web interface
* cURL

Open the GraphQL sandbox (bottom left of the web interface) and execute:

```
mutation {
  NetworkDeviceCreate(data: {hostname: {value: "atl1-edge1"}, model: {value: "Cisco ASR1002-HX"}}) {
    ok
    object {
      id
    }
  }
  NetworkInterfaceCreate(data: {name: {value: "Ethernet1"}, description: {value: "WAN interface"}}) {
    ok
    object {
      id
    }
  }
}
```

1. Navigate to **Objects > Device** in the left menu
2. Click **Add Device**
3. Enter `atl1-edge1` as Hostname and `Cisco ASR1002-HX` as Model
4. Click **Save**
5. Navigate to **Objects > Interface**
6. Create an interface with `Ethernet1` as Name and `WAN interface` as Description

Replace the IP address and API key with your actual values:

```
curl -X POST http://localhost:8000/graphql/network-device-schema \
  -H "Content-Type: application/json" \
  -H "X-INFRAHUB-KEY: 1802eed5-eeb7-cc45-2e4d-c51de9d66cba" \
  -d '{"query": "mutation { NetworkDeviceCreate(data: {hostname: {value: \"atl1-edge1\"}, model: {value: \"Cisco ASR1002-HX\"}}) { ok object { id } } NetworkInterfaceCreate(data: {name: {value: \"Ethernet1\"}, description: {value: \"WAN interface\"}}) { ok object { id } } }"}'
```

Verify your objects were created by navigating to **Objects** and selecting **Device** or **Interface**.

## Step 2: Add relationships between nodes[​](#step-2-add-relationships-between-nodes "Direct link to Step 2: Add relationships between nodes")

Connect your device and interface nodes with relationships. This creates meaningful associations between your data.

Add these relationships to your schema:

1. **Device to interfaces**: One device can have many interfaces (component relationship)
2. **Interface to device**: Each interface belongs to one device (parent relationship)

Replace your `schema_guide.yml` content with:

```
---
version: "1.0"
nodes:
  - name: Device
    namespace: Network
    human_friendly_id: ['hostname__value']
    attributes:
      - name: hostname
        kind: Text
        unique: true
      - name: model
        kind: Text
    relationships:
      - name: interfaces
        cardinality: many
        peer: NetworkInterface
        kind: Component
  - name: Interface
    namespace: Network
    attributes:
      - name: name
        kind: Text
      - name: description
        kind: Text
        optional: true
    relationships:
      - name: device
        cardinality: one
        peer: NetworkDevice
        optional: false
        kind: Parent
```

### Load the updated schema[​](#load-the-updated-schema "Direct link to Load the updated schema")

Create a new branch for the relationship changes:

```
infrahubctl branch create network-device-relations
```

Load the updated schema:

```
infrahubctl schema load --branch network-device-relations /tmp/schema_guide.yml
```

### Test the relationships[​](#test-the-relationships "Direct link to Test the relationships")

Create connected objects using this GraphQL mutation:

```
mutation {
  NetworkDeviceCreate(data: {hostname: {value: "atl1-edge1"}, model: {value: "Cisco ASR1002-HX"}}) {
    ok
    object {
      id
    }
  }
  NetworkInterfaceCreate(data: {name: {value: "Ethernet1"}, description: {value: "WAN interface"}, device: {hfid: "atl1-edge1"}}) {
    ok
    object {
      id
    }
  }
}
```

In the Web UI, view the device details to see the relationship to the Ethernet1 interface.

![Schema page screenshot](/assets/images/create_schema_3-cc070529d09bc7eb1df4e51fe3a556eb.png)

## Step 3: Create generic nodes for abstraction[​](#step-3-create-generic-nodes-for-abstraction "Direct link to Step 3: Create generic nodes for abstraction")

Real network devices have different interface types with shared and unique characteristics. Use generic nodes to model this abstraction.

Physical interfaces (like Ethernet1) have properties like speed and cable connections. Logical interfaces (like Vlan1) don't have these physical properties but share common attributes like name and description.

### Create a generic interface[​](#create-a-generic-interface "Direct link to Create a generic interface")

Replace your schema with this structure using generics:

```
---
version: "1.0"
generics:
  - name: Interface
    namespace: Network
    attributes:
      - name: name
        kind: Text
      - name: description
        kind: Text
        optional: true
    relationships:
      - name: device
        cardinality: one
        peer: NetworkDevice
        kind: Parent
        optional: false
nodes:
  - name: Device
    namespace: Network
    human_friendly_id: ['hostname__value']
    attributes:
      - name: hostname
        kind: Text
        unique: true
      - name: model
        kind: Text
    relationships:
      - name: interfaces
        cardinality: many
        peer: NetworkInterface
        kind: Component
  - name: PhysicalInterface
    namespace: Network
    inherit_from:
      - NetworkInterface
    attributes:
      - name: speed
        kind: Number
  - name: LogicalInterface
    namespace: Network
    inherit_from:
      - NetworkInterface
```

### Load the generic schema[​](#load-the-generic-schema "Direct link to Load the generic schema")

Create a new branch for generic changes:

```
infrahubctl branch create network-device-generics
```

Load the schema:

```
infrahubctl schema load --branch network-device-generics /tmp/schema_guide.yml
```

### Test different interface types[​](#test-different-interface-types "Direct link to Test different interface types")

Create both physical and logical interfaces:

```
mutation {
  NetworkDeviceCreate(data: {hostname: {value: "atl1-edge1"}, model: {value: "Cisco ASR1002-HX"}}) {
    ok
    object {
      id
    }
  }
  NetworkPhysicalInterfaceCreate(data: {name: {value: "Ethernet1"}, description: {value: "WAN interface"}, speed: {value: 1000000000}, device: {hfid: "atl1-edge1"}}) {
    ok
    object {
      id
    }
  }
  NetworkLogicalInterfaceCreate(data: {name: {value: "Vlan1"}, description: {value: "SVI for VLAN 1"}, device: {hfid: "atl1-edge1"}}) {
    ok
    object {
      id
    }
  }
}
```

View the device in the Web UI to see both interface types connected to the same device.

![Schema page screenshot](/assets/images/create_schema_generics-eecd428f91e064e125bd10e3edfe2fcd.png)

## Step 4: Improve the schema with migrations[​](#step-4-improve-the-schema-with-migrations "Direct link to Step 4: Improve the schema with migrations")

Refine your schema using Infrahub's schema migration features. These changes demonstrate how to evolve schemas while preserving existing data.

Make these improvements:

1. Add `mtu` and `enabled` attributes to the generic `NetworkInterface`
2. Remove the `description` attribute from the generic `NetworkInterface`
3. Set a default value for the `speed` attribute of `NetworkPhysicalInterface`
4. Rename the `model` attribute to `device_type`
5. Add labels for better user experience
6. Define uniqueness constraints

### Get the attribute ID for migration[​](#get-the-attribute-id-for-migration "Direct link to Get the attribute ID for migration")

Attribute ID required

To rename an attribute, you need its current ID. Find the `model` attribute ID on the [NetworkDevice schema page](http://localhost:8000/schema?branch=network-device-generics\&kind=NetworkDevice) in the Web UI.

Replace your schema content (update the `id` value with the actual model attribute ID):

```
---
version: "1.0"
generics:
  - name: Interface
    namespace: Network
    attributes:
      - name: name
        kind: Text
        label: Name
      - name: description
        state: absent
        kind: Text
        optional: true
        label: Description
      - name: mtu
        kind: Number
        label: MTU
        optional: false
        default_value: 1500
      - name: enabled
        label: Enabled
        kind: Boolean
        optional: false
        default_value: false
    relationships:
      - name: device
        label: Device
        cardinality: one
        peer: NetworkDevice
        kind: Parent
        optional: false
nodes:
  - name: Device
    namespace: Network
    human_friendly_id: ['hostname__value']
    attributes:
      - name: hostname
        kind: Text
        label: Hostname
        unique: true
      - name: device_type
        label: Device Type
        kind: Text
        id: 17bcf8a7-9c03-4a6a-3295-c51345cb1c33
    relationships:
      - name: interfaces
        label: Interfaces
        cardinality: many
        peer: NetworkInterface
        kind: Component
  - name: PhysicalInterface
    namespace: Network
    uniqueness_constraints:
      - ["device", "name__value"]
    inherit_from:
      - NetworkInterface
    attributes:
      - name: speed
        label: Speed (bps)
        kind: Number
        default_value: 1000000000
  - name: LogicalInterface
    namespace: Network
    uniqueness_constraints:
      - ["device", "name__value"]
    inherit_from:
      - NetworkInterface
```

### Preview schema changes[​](#preview-schema-changes "Direct link to Preview schema changes")

Use the check command to see what changes will be applied:

```
infrahubctl schema check --branch network-device-generics /tmp/schema_guide.yml
```

This shows a diff of changes before applying them.

### Apply the migration[​](#apply-the-migration "Direct link to Apply the migration")

Load the improved schema:

```
infrahubctl schema load --branch network-device-generics /tmp/schema_guide.yml
```

Migration complete

Infrahub automatically migrates existing data to match the new schema structure. View the updated schema in the [Web UI](http://localhost:8000/schema?branch=network-device-generics).

## Relationship best practices[​](#relationship-best-practices "Direct link to Relationship best practices")

Follow these practices when creating relationships with generic nodes:

### Always set explicit identifiers[​](#always-set-explicit-identifiers "Direct link to Always set explicit identifiers")

```
# ❌ Avoid: Missing identifier with generics
generics:
  - name: Interface
    relationships:
      - name: device
        peer: TestDevice
        # Auto-generation may fail

# ✅ Prefer: Explicit identifier
generics:
  - name: Interface
    relationships:
      - name: device
        peer: TestDevice
        identifier: "device__interface"
```

### Use consistent naming patterns[​](#use-consistent-naming-patterns "Direct link to Use consistent naming patterns")

* Follow the pattern `<parent>__<child>` or `<node_a>__<node_b>`
* Verify that both sides of bidirectional relationships use matching identifiers
* Document cascade delete behavior when using `on_delete: cascade`

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you've created a basic schema:

* Learn about [schema validation](/reference/schema-validation.md) for development workflows
* Explore the complete [Schema topic](/topics/schema.md) for advanced concepts
* Try [importing existing schemas](/guides/import-schema.md) from other sources
* Set up [external repositories](/guides/repository.md) to manage schemas with Git

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Input should be a valid string (string\_type)[​](#input-should-be-a-valid-string-string_type "Direct link to Input should be a valid string (string_type)")

When loading a schema, you may encounter the error "Input should be a valid string (string\_type)". This typically occurs when YAML interprets certain unquoted values as booleans instead of strings.

YAML automatically converts unquoted `on`, `off`, `yes`, `no`, `true`, and `false` values to boolean types. When these values appear in fields expecting strings (like choice names), schema validation fails.

**Example of the problem:**

```
---
version: "1.0"
nodes:
  - name: Stuff
    namespace: Random
    attributes:
      - name: status
        kind: Dropdown
        choices:
          - name: on  # Interpreted as boolean true
            label: On
          - name: off  # Interpreted as boolean false
            label: Off
```

**Solution:**

Quote all boolean-like string values in your schema:

```
---
version: "1.0"
nodes:
  - name: Stuff
    namespace: Random
    attributes:
      - name: status
        kind: Dropdown
        choices:
          - name: "on"  # Properly interpreted as string
            label: "On"
          - name: "off"
            label: "Off"
```

This issue commonly appears in:

* Dropdown choice names
* Attribute names

## Related resources[​](#related-resources "Direct link to Related resources")

* [Schema topic](/topics/schema.md) - Complete schema documentation
* [Schema validation reference](/reference/schema-validation.md) - Validation tools and rules
* [GraphQL topic](/topics/graphql.md) - Query and mutation syntax
* [Import schema guide](/guides/import-schema.md) - Loading existing schemas
