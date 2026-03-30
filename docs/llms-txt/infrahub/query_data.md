# Source: https://docs.infrahub.app/python-sdk/guides/query_data.md

# Querying data in Infrahub

We can query data in 3 ways using the SDK:

* querying a single node of a given kind, based on some filters, using the `get` method
* querying multiple nodes of a given kind, based on some filters, using the `filters` method
* querying all the nodes of a given kind, using the `all` method
* querying with a GraphQL query, using the `execute_graphql` method

## Query filters[​](#query-filters "Direct link to Query filters")

The `get` and `filters` query methods allow you to use filters. Filters specify on which attribute(s) or attributes of a relationship(s) the resulting node(s) should match. The available filters depend on the kind of Node you want to query and are dynamically generated from the schema.

### Discovering available filters[​](#discovering-available-filters "Direct link to Discovering available filters")

The easiest way to discover the available filters for a kind of node is by opening the GraphQLi Explorer in the GraphQL sandbox. Under each GraphQL query you will find the available filters.

### Attribute filters[​](#attribute-filters "Direct link to Attribute filters")

For every attribute the following filters will be generated (replace attribute with the name of the attribute):

* `attribute__value`: filter for a single attribute value
* `attribute__values`: (list) filter for multiple attribute values
* `attribute__is_visible`: (boolean) filter for the `is_visible` property of an attribute
* `attribute__is_protected`: (boolean) filter for the `is_protected` property of an attribute
* `attribute__source__id`: filter for the `source` property of an attribute
* `attribute__owner__id`: filter for the `owner` property of an attribute

### Relationship filters[​](#relationship-filters "Direct link to Relationship filters")

For every attribute of a relationship of the node, the same filters will be generated. The name of the filter will be prefixed with the relationship name followed by 2 underscores `relationship__attribute__value`.

### Using filters[​](#using-filters "Direct link to Using filters")

Filters can be passed as arguments to the `get` or `filters` method.

* Async
* Sync

```
tag = await client.get(kind="BuiltinTag", name__value="RED")
```

```
tag = client.get(kind="BuiltinTag", name__value="RED")
```

### Using multiple filters[​](#using-multiple-filters "Direct link to Using multiple filters")

When you pass multiple filters as argument to the `get` or `filters` method, they will combined in a logical AND operation. The resulting nodes of your query will match on all the filters in that case.

* Async
* Sync

```
tags = await client.filters(kind="BuiltinTag", name__values=["RED", "BLUE"], name__is_protected=True)
```

```
tags = client.filters(kind="BuiltinTag", name__values=["RED", "BLUE"], name__is_protected=True)
```

## Querying a single node[​](#querying-a-single-node "Direct link to Querying a single node")

You can query Infrahub for a single node of a particular kind, by using the `get` method and using 1 or more filters.

* Async
* Sync

```
tag = await client.get(kind="BuiltinTag", name__value="RED")
```

```
tag = client.get(kind="BuiltinTag", name__value="RED")
```

## Querying multiple nodes[​](#querying-multiple-nodes "Direct link to Querying multiple nodes")

You can query Infrahub for multiple nodes of a particular kind, by using the `filters` method and using 1 or more filters.

* Async
* Sync

```
tags = client.filters(kind="BuiltinTag", name__values=["RED", "BLUE"])
```

```
tags = client.filters(kind="BuiltinTag", name__values=["RED", "BLUE"])
```

## Querying all nodes[​](#querying-all-nodes "Direct link to Querying all nodes")

You can query Infrahub for all nodes of a particular kind, by using the `all` method.

* Async
* Sync

```
tags = await client.all(kind="BuiltinTag")
```

```
tags = client.all(kind="BuiltinTag")
```

## Querying with a GraphQL query[​](#querying-with-a-graphql-query "Direct link to Querying with a GraphQL query")

In some scenarios it might be more convenient to query Infrahub using a GraphQL query, rather than using the builtin mechanisms in the SDK.

An example might be finding all the devices connected to a given circuit. This would require us to execute multiple queries using the nodes provided by the SDK. However with a GraphQL query this can be achieved using only a single query.

The downside of using this method, is that it will not construct Python objects for the resulting data. Instead the SDK will return a Python dictionary containing the deserialized JSON data returned by the GraphQL API.

* Async
* Sync

```
query = """query {
  BuiltinTag(name__values: ["RED", "BLUE"]) {
    edges {
      node {
        name {
          value
        }
      }
    }
  }
}"""
data = await client.execute_graphql(query=query)
for tag in data["BuiltinTag"]["edges"]:
    print(tag["node"]["name"]["value"])
```

```
query = """query {
  BuiltinTag(name__values: ["RED", "BLUE"]) {
    edges {
      node {
        name {
          value
        }
      }
    }
  }
}"""
data = client.execute_graphql(query=query)
for tag in data["BuiltinTag"]["edges"]:
    print(tag["node"]["name"]["value"])
```

## Attributes and relationships[​](#attributes-and-relationships "Direct link to Attributes and relationships")

By default, the result of a query will include attributes, relationships of cardinality one and relationships of kind Attribute or Parent. Relationships that are included in a query will be automatically initialized which means the ID, type and display name of the peers will be included in the query. But the related node itself will not be included.

To explore this in a bit more details, we are going to assume the following schema has been loaded into Infrahub

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

### Attributes[​](#attributes "Direct link to Attributes")

Attributes are included by default.

* Async
* Sync

```
device = await client.get(kind="BuiltinTag", name__value="atl1-edge1")
print(device.name.value)
```

```
device = client.get(kind="BuiltinTag", name__value="atl1-edge1")
print(device.name.value)
```

### Relationships of cardinality one[​](#relationships-of-cardinality-one "Direct link to Relationships of cardinality one")

Relationships of cardinality one are included by default and will be initialized.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.site.initialized) # True
print(device.site.id, device.site.display_label, device.site.typename)
print(device.site.peer) # the related node is not included
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.site.initialized) # True
print(device.site.id, device.site.display_label, device.site.typename)
print(device.site.peer) # the related node is not included
```

Relationships of kind `Attribute`, `Parent` are included by default and will be initialized.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.tags.initialized) # True
print(device.tags.peers)

for tag in device.tags.peers:
    print(tag.id, tag.display_label, tag.typename)
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.tags.initialized) # True
print(device.tags.peers)

for tag in device.tags.peers:
    print(tag.id, tag.display_label, tag.typename)
```

### Relationships of cardinality many are not included by default[​](#relationships-of-cardinality-many-are-not-included-by-default "Direct link to Relationships of cardinality many are not included by default")

Relationships of cardinality many are not included by default.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.interfaces.initialized) # False
print(device.interfaces.peers) # empty list []
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.interfaces.initialized) # False
print(device.interfaces.peers) # empty list []
```

### Including attributes and relationships[​](#including-attributes-and-relationships "Direct link to Including attributes and relationships")

You can include attributes and relationships that are not retrieved as part of a query by default. The included relationships will be initialized and the related nodes (peers) will be initialized.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", include=["interfaces"])
print(device.interfaces.initialized) # True
print(device.interfaces.peers)

for interface in device.interfaces.peers:
    print(interface.id, interface.display_label, interface.typename)
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", include=["interfaces"])
print(device.interfaces.initialized) # True
print(device.interfaces.peers)

for interface in device.interfaces.peers:
    print(interface.id, interface.display_label, interface.typename)
```

### Excluding attribute and relationships[​](#excluding-attribute-and-relationships "Direct link to Excluding attribute and relationships")

You can exclude attributes and relationships that are retrieved with a query by default. This can be useful if you need to optimize or speed up a particular query.

* Async
* Sync

```
device = await client.get(kind="TestDevice", exclude=["site"])
print(device.site) # None
```

```
device = client.get(kind="TestDevice", exclude=["site"])
print(device.site) # None
```

### Fetching relationships manually[​](#fetching-relationships-manually "Direct link to Fetching relationships manually")

The `fetch` method can be used to retrieve relationships, initialize them; and retrieving the related nodes manually. The `fetch` method can also be used on relationship that were previously initialized.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.interfaces.initialized) # False

await device.interfaces.fetch()
print(device.interfaces.initialized) # True
for interface in device.interfaces.peers:
    print(interface.id, interface.display_label, interface.typename, interface.peer.name.value)
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1")
print(device.interfaces.initialized) # False

device.interfaces.fetch()
print(device.interfaces.initialized) # True
for interface in device.interfaces.peers:
    print(interface.id, interface.display_label, interface.typename, interface.peer.name.value)
```

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", include=["interfaces"])
print(device.interfaces.initialized) # True

await device.interfaces.fetch()
for interface in device.interfaces.peers:
    print(interface.id, interface.display_label, interface.typename, interface.peer.name.value)
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", include=["interfaces"])
print(device.interfaces.initialized) # True

device.interfaces.fetch()
for interface in device.interfaces.peers:
    print(interface.id, interface.display_label, interface.typename, interface.peer.name.value)
```

### Prefetch relationships[​](#prefetch-relationships "Direct link to Prefetch relationships")

Related nodes of a relationship can be retrieved, using the `prefetch_relationships` argument for the different `query` methods. But this requires the usage of the internal client store . More information can be found in the [Using the client store](/python-sdk/guides/store.md) guide.

## Query a node(s) in the past[​](#query-a-nodes-in-the-past "Direct link to Query a node(s) in the past")

To query the state of a Node in the past, you can pass the `at` argument to all the query methods. The at argument accepts a `str`, `DateTime` or `Timestamp` object as value. Values of type `str` will be parsed using the [Pendulum](https://pendulum.eustace.io/) library.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", at="10:10:10")
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", at="10:10:10")
```

### Properties of attributes and relationships[​](#properties-of-attributes-and-relationships "Direct link to Properties of attributes and relationships")

By default, the [meta data or properties](/topics/metadata.md) of attributes and relationships are not included. We can include these properties using the `property` argument of the SDK client's `all`, `filters` or `get` method.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", property=True)
print(device.name.is_protected)
print(device.name.source.display_label)
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", property=True)
print(device.name.protected)
print(device.name.source.display_label)
```

## Node metadata[​](#node-metadata "Direct link to Node metadata")

Node metadata provides information about when a node was created or last updated, and by whom. This includes timestamps and references to the accounts that made the changes.

### Including node metadata in queries[​](#including-node-metadata-in-queries "Direct link to Including node metadata in queries")

By default, node metadata is not included in query results. You can include it using the `include_metadata` argument of the SDK client's `all`, `filters`, or `get` method.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", include_metadata=True)
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", include_metadata=True)
```

### Accessing node metadata[​](#accessing-node-metadata "Direct link to Accessing node metadata")

Once metadata is included in the query, you can access it using the `get_node_metadata()` method. The metadata object contains the following fields:

* `created_at`: Timestamp when the node was created
* `created_by`: Reference to the account that created the node
* `updated_at`: Timestamp when the node was last updated
* `updated_by`: Reference to the account that last updated the node

- Async
- Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", include_metadata=True)

# Get the metadata object
metadata = device.get_node_metadata()

# Access creation metadata
print(metadata.created_at)  # e.g., "2024-01-15T10:30:00Z"
print(metadata.created_by.display_label)  # e.g., "admin"

# Access update metadata
print(metadata.updated_at)  # e.g., "2024-01-20T14:45:00Z"
print(metadata.updated_by.display_label)  # e.g., "admin"
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", include_metadata=True)

# Get the metadata object
metadata = device.get_node_metadata()

# Access creation metadata
print(metadata.created_at)  # e.g., "2024-01-15T10:30:00Z"
print(metadata.created_by.display_label)  # e.g., "admin"

# Access update metadata
print(metadata.updated_at)  # e.g., "2024-01-20T14:45:00Z"
print(metadata.updated_by.display_label)  # e.g., "admin"
```

The `created_by` and `updated_by` fields are `NodeProperty` objects that include:

* `id`: The unique identifier of the account
* `display_label`: A human-readable label for the account
* `typename`: The GraphQL type name of the account

## Relationship metadata[​](#relationship-metadata "Direct link to Relationship metadata")

When querying with `include_metadata=True`, you can also access metadata about relationship edges themselves. This tells you when a specific relationship (the connection between two nodes) was last modified and by whom.

### Accessing relationship metadata[​](#accessing-relationship-metadata "Direct link to Accessing relationship metadata")

Use the `get_relationship_metadata()` method on a related node to access the relationship edge metadata. This is different from node metadata - it describes when the relationship itself was created or modified, not the connected node.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", include_metadata=True)

# For a cardinality-one relationship
rel_metadata = device.site.get_relationship_metadata()
if rel_metadata:
    print(rel_metadata.updated_at)  # e.g., "2024-01-17T08:00:00Z"
    print(rel_metadata.updated_by.display_label)  # e.g., "admin"

# For a cardinality-many relationship
for tag in device.tags.peers:
    rel_metadata = tag.get_relationship_metadata()
    if rel_metadata:
        print(f"Tag relationship updated at: {rel_metadata.updated_at}")
        print(f"Updated by: {rel_metadata.updated_by.display_label}")
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", include_metadata=True)

# For a cardinality-one relationship
rel_metadata = device.site.get_relationship_metadata()
if rel_metadata:
    print(rel_metadata.updated_at)  # e.g., "2024-01-17T08:00:00Z"
    print(rel_metadata.updated_by.display_label)  # e.g., "admin"

# For a cardinality-many relationship
for tag in device.tags.peers:
    rel_metadata = tag.get_relationship_metadata()
    if rel_metadata:
        print(f"Tag relationship updated at: {rel_metadata.updated_at}")
        print(f"Updated by: {rel_metadata.updated_by.display_label}")
```

The `RelationshipMetadata` object contains:

* `updated_at`: Timestamp when the relationship was last updated
* `updated_by`: Reference to the account that last updated the relationship (a `NodeProperty` object with `id`, `display_label`, and `typename`)

note

Relationship metadata tracks changes to the relationship edge itself (for example, when the relationship was created or when its properties were modified), not changes to the connected nodes. For node-level metadata, use `get_node_metadata()` on the node itself.

## Ordering query results[​](#ordering-query-results "Direct link to Ordering query results")

You can control the order in which query results are returned using the `order` argument. This is particularly useful when you need results sorted by metadata fields like creation or update timestamps.

### Ordering by node metadata[​](#ordering-by-node-metadata "Direct link to Ordering by node metadata")

Use the `Order` and `NodeMetaOrder` classes along with `OrderDirection` to specify how results should be ordered.

* Async
* Sync

```
from infrahub_sdk.enums import OrderDirection
from infrahub_sdk.types import NodeMetaOrder, Order

# Get devices ordered by creation time (oldest first)
devices = await client.all(
    kind="TestDevice",
    order=Order(node_metadata=NodeMetaOrder(created_at=OrderDirection.ASC))
)

# Get devices ordered by last update time (most recent first)
devices = await client.all(
    kind="TestDevice",
    order=Order(node_metadata=NodeMetaOrder(updated_at=OrderDirection.DESC))
)
```

```
from infrahub_sdk.enums import OrderDirection
from infrahub_sdk.types import NodeMetaOrder, Order

# Get devices ordered by creation time (oldest first)
devices = client.all(
    kind="TestDevice",
    order=Order(node_metadata=NodeMetaOrder(created_at=OrderDirection.ASC))
)

# Get devices ordered by last update time (most recent first)
devices = client.all(
    kind="TestDevice",
    order=Order(node_metadata=NodeMetaOrder(updated_at=OrderDirection.DESC))
)
```

The available order directions are:

* `OrderDirection.ASC`: Ascending order (oldest/smallest first)
* `OrderDirection.DESC`: Descending order (newest/largest first)

note

You can only order by one metadata field at a time. Specifying both `created_at` and `updated_at` in the same `NodeMetaOrder` will raise a validation error, as they are mutually exclusive.

### Disabling default ordering[​](#disabling-default-ordering "Direct link to Disabling default ordering")

For performance optimization, you can disable the default ordering behavior entirely:

* Async
* Sync

```
from infrahub_sdk.types import Order

# Disable ordering to improve query performance
devices = await client.all(kind="TestDevice", order=Order(disable=True))
```

```
from infrahub_sdk.types import Order

# Disable ordering to improve query performance
devices = client.all(kind="TestDevice", order=Order(disable=True))
```

### Combining metadata and ordering[​](#combining-metadata-and-ordering "Direct link to Combining metadata and ordering")

You can include metadata and order results in the same query:

* Async
* Sync

```
from infrahub_sdk.enums import OrderDirection
from infrahub_sdk.types import NodeMetaOrder, Order

# Get the 10 most recently updated devices with their metadata
devices = await client.filters(
    kind="TestDevice",
    limit=10,
    include_metadata=True,
    order=Order(node_metadata=NodeMetaOrder(updated_at=OrderDirection.DESC))
)

for device in devices:
    metadata = device.get_node_metadata()
    print(f"{device.name.value} - Last updated: {metadata.updated_at}")
```

```
from infrahub_sdk.enums import OrderDirection
from infrahub_sdk.types import NodeMetaOrder, Order

# Get the 10 most recently updated devices with their metadata
devices = client.filters(
    kind="TestDevice",
    limit=10,
    include_metadata=True,
    order=Order(node_metadata=NodeMetaOrder(updated_at=OrderDirection.DESC))
)

for device in devices:
    metadata = device.get_node_metadata()
    print(f"{device.name.value} - Last updated: {metadata.updated_at}")
```

## Query a node(s) in a different branch[​](#query-a-nodes-in-a-different-branch "Direct link to Query a node(s) in a different branch")

If you want to query a node(s) in a different branch than the default branch with which the SDK client was initiated, then you can use the `branch` argument of the query methods.

* Async
* Sync

```
device = await client.get(kind="TestDevice", name__value="atl1-edge1", branch="refresh-site-atl1")
```

```
device = client.get(kind="TestDevice", name__value="atl1-edge1", branch="refresh-site-atl1")
```

## Query for a large amount of nodes[​](#query-for-a-large-amount-of-nodes "Direct link to Query for a large amount of nodes")

When you have a query that matches a large amount of nodes, it could have an implication on the performance of the query. The SDK tries to optimize this process by using pagination, which happens transparently. However, even when using pagination, such queries could take a long time to complete.

Using the `parallel` argument, we can enable concurrent retrieval of pages of data for large queries, which can significantly improve the resolution time of the query.

The `parallel` argument is available for the SDK client's `filters` and `all` method.

* Async
* Sync

```
device = await client.all(kind="TestDevice", parallel=True)
```

```
device = client.get(kind="TestDevice", parallel=True)
```
