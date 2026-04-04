# Source: https://docs.infrahub.app/python-sdk/guides/create_update_delete.md

# Create, update and deleting nodes

We will be using the following schema in this guide:

```
---
version: "1.0"
nodes:
  - name: Device
    namespace: Test
    attributes:
      - name: name
        kind: Text
        unique: true
        optional: false
    relationships:
      - name: tags
        cardinality: many
        kind: Attribute
        peer: BuiltinTag
        optional: true
      - name: site
        cardinality: one
        kind: Attribute
        peer: TestSite
        optional: false
      - name: interfaces
        cardinality: many
        kind: Component
        peer: TestInterface
        optional: false
  - name: Site
    namespace: Test
    attributes:
      - name: name
        kind: Text
        unique: true
        optional: false
    relationships:
      - name: device
        cardinality: many
        kind: Attribute
        peer: TestDevice
        optional: true
  - name: Interface
    namespace: Test
    attributes:
      - name: name
        kind: Text
        unique: true
        optional: false
    relationships:
      - name: device
        cardinality: one
        kind: Parent
        peer: TestDevice
        optional: true
```

## Creating a node[​](#creating-a-node "Direct link to Creating a node")

A node can be created using the `create` method. The `create` method will first construct a `InfrahubNode` object in memory. This `InfrahubNode` object will then need to be saved into Infrahub using the `save` method.

The attributes and relationships of the `InfrahubNode` you want to create can be passed as arguments to the `create` method, or you can pass them using a dictionary.

* Async
* Sync

```
device = await client.create(kind="TestDevice", name="atl1-edge1")
await device.save()
```

```
device = client.create(kind="TestDevice", name="atl1-edge1")
device.save()
```

* Async
* Sync

```
data = {"name": "atl1-edge1"}
device = await client.create(kind="TestDevice", data=data)
await device.save()
```

```
data = {"name": "atl1-edge1"}
device = client.create(kind="TestDevice", data=data)
device.save()
```

### Creating a node with a relation of cardinality one[​](#creating-a-node-with-a-relation-of-cardinality-one "Direct link to Creating a node with a relation of cardinality one")

* Async
* Sync

```
site = await client.get(kind="TestSite", name__value="atl1")
device = await client.create(kind="TestDevice", name="atl1-edge1", site=site)
await device.save()
```

```
site = client.get(kind="TestSite", name__value="atl1")
device = client.create(kind="TestDevice", name="atl1-edge1", site=site)
device.save()
```

### Creating a node with a relation of cardinality many[​](#creating-a-node-with-a-relation-of-cardinality-many "Direct link to Creating a node with a relation of cardinality many")

* Async
* Sync

```
interfaces = await client.filters(kind="TestInterface", name__values=["Ethernet1", "Ethernet2"])
device = await client.create(kind="TestDevice", name="atl1-edge1", interfaces=interfaces)
await device.save()
```

```
interfaces = client.filters(kind="TestInterface", name__values=["Ethernet1", "Ethernet2"])
device = client.create(kind="TestDevice", name="atl1-edge1", interfaces=interfaces)
device.save()
```

## Updating a node[​](#updating-a-node "Direct link to Updating a node")

To update a node from Infrahub using the SDK, we first have to retrieve the node using one of the query methods, then update the attributes and/or relations of the node and `save` the node.

* Async
* Sync

```
interface = await client.get(kind="TestInterface", name__value="Ethernet1")
interface.name.value = "Ethernet3"
await interface.save()
```

```
interface = client.get(kind="TestInterface", name__value="Ethernet1")
interface.name.value = "Ethernet3"
interface.save()
```

### Updating a relation of cardinality one on a node[​](#updating-a-relation-of-cardinality-one-on-a-node "Direct link to Updating a relation of cardinality one on a node")

* Async
* Sync

```
site = await client.get(kind="TestSite", name__value="atl2")
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
device.site = site
await device.save()
```

```
site = client.get(kind="TestSite", name__value="atl2")
device = client.get(kind="TestDevice", name__value="atl1-edge1")
device.site = site
device.save()
```

### Updating a relation of cardinality many on a node[​](#updating-a-relation-of-cardinality-many-on-a-node "Direct link to Updating a relation of cardinality many on a node")

Adding a single relation:

* Async
* Sync

```
interface = await client.get(kind="TestInterface", name__value="Ethernet1")
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
device.interfaces.add(interface)
await device.save()
```

```
interface = client.get(kind="TestInterface", name__value="Ethernet1")
device = client.get(kind="TestDevice", name__value="atl1-edge1")
device.interfaces.add(interface)
device.save()
```

Adding multiple relations:

* Async
* Sync

```
interfaces = await client.filters(kind="TestInterface", name__values=["Ethernet1", "Ethernet2"])
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
device.interfaces.extend(interfaces)
await device.save()
```

```
interfaces = client.filters(kind="TestInterface", name__values=["Ethernet1", "Ethernet2"])
device = client.get(kind="TestDevice", name__value="atl1-edge1")
device.interfaces.extend(interfaces)
device.save()
```

## Deleting a node[​](#deleting-a-node "Direct link to Deleting a node")

To delete a node from Infrahub using the SDK, we first have to retrieve the node using one of the query methods. The `delete` method can then be used on the retrieved `InfrahubNode` object.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
await device.delete()
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1")
device.delete()
```

## Upserting a node[​](#upserting-a-node "Direct link to Upserting a node")

The word upserting is formed out of the combination of updating and inserting. It refers to the action of creating a node if it does not yet exist, or to update the existing node if it already exists.

We first have to create the node in memory, then use the `save` method on the node with the `allow_upsert` argument set to `True`.

* Async
* Sync

```
site = await client.get(kind="TestSite", name="atl1")
device = await client.create(kind="TestDevice", name="atl1-edge1")
device.site = site
await device.save(allow_upsert=True)
```

```
site = client.get(kind="TestSite", name="atl1")
device = client.create(kind="TestDevice", name="atl1-edge1")
device.site = site
device.save(allow_upsert=True)
```
