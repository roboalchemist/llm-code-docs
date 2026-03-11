# GraphML Quick Reference

## Basic Document Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns
                             http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="attr1" for="node" attr.name="label" attr.type="string"/>
  <graph id="G" edgedefault="undirected">
    <node id="n1">
      <data key="attr1">Node 1</data>
    </node>
    <edge id="e1" source="n1" target="n2"/>
  </graph>
</graphml>
```

## Root Elements

### `<graphml>`

Root element containing the entire graph definition.

**Attributes:**

- `xmlns` - XML namespace (required): `http://graphml.graphdrawing.org/xmlns`
- `version` - GraphML version (typically "1.0")

**Child Elements:**

- `<key>` - Define custom data attributes (0 or more)
- `<graph>` - The actual graph definition (1 or more)

### `<graph>`

Container for nodes and edges.

**Attributes:**

- `id` - Unique identifier (required)
- `edgedefault` - Default edge direction: `directed` or `undirected` (required)
- `parse.nodeids` - Node ID validation: `free` or `canonical`
- `parse.edgeids` - Edge ID validation: `free` or `canonical`
- `parse.order` - Edge order tracking: `free` or `canonical`

**Child Elements:**

- `<desc>` - Optional description
- `<data>` - Custom graph attributes
- `<node>` - Node definitions (0 or more)
- `<edge>` - Edge definitions (0 or more)
- `<graph>` - Nested subgraphs (for hierarchical graphs)

### `<node>`

Represents a single node/vertex in the graph.

**Attributes:**

- `id` - Unique identifier within the graph (required)

**Child Elements:**

- `<desc>` - Optional description
- `<data>` - Custom node attributes

### `<edge>`

Represents a connection between two nodes.

**Attributes:**

- `id` - Unique identifier (optional but recommended)
- `source` - ID of source node (required)
- `target` - ID of target node (required)
- `directed` - Override default edge direction: `true` or `false`

**Child Elements:**

- `<desc>` - Optional description
- `<data>` - Custom edge attributes

### `<data>`

Associates custom data with an element.

**Attributes:**

- `key` - References a `<key>` element's id (required)

**Content:** The actual data value

### `<key>`

Defines custom attributes for nodes, edges, graphs, or ports.

**Attributes:**

- `id` - Unique identifier (required)
- `for` - Element type: `graph`, `node`, `edge`, `all` (required)
- `attr.name` - Attribute name (required for typed keys)
- `attr.type` - Data type: `boolean`, `int`, `long`, `float`, `double`, `string` (optional)
- `attr.default` - Default value if not specified (optional)

**Child Elements:**

- `<desc>` - Description
- `<default>` - Default value

## Common Data Types

| Type | Description | Example |
|------|-------------|---------|
| `string` | Text data | "Hello" |
| `int` | 32-bit integer | 42 |
| `long` | 64-bit integer | 9223372036854775807 |
| `float` | Single precision | 3.14 |
| `double` | Double precision | 3.141592653589793 |
| `boolean` | True/false | true |

## Practical Examples

### Simple Undirected Graph

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <graph id="simple" edgedefault="undirected">
    <node id="a"/>
    <node id="b"/>
    <node id="c"/>
    <edge source="a" target="b"/>
    <edge source="b" target="c"/>
    <edge source="c" target="a"/>
  </graph>
</graphml>
```

### Graph with Node Labels

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="label" for="node" attr.name="label" attr.type="string"/>
  <graph id="labeled" edgedefault="directed">
    <node id="n1">
      <data key="label">Node 1</data>
    </node>
    <node id="n2">
      <data key="label">Node 2</data>
    </node>
    <edge id="e1" source="n1" target="n2"/>
  </graph>
</graphml>
```

### Mixed Directed/Undirected Edges

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <graph id="mixed" edgedefault="undirected">
    <node id="a"/>
    <node id="b"/>
    <node id="c"/>
    <!-- Undirected (uses default) -->
    <edge source="a" target="b"/>
    <!-- Directed (overrides default) -->
    <edge source="b" target="c" directed="true"/>
  </graph>
</graphml>
```

### Graph with Multiple Custom Attributes

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="label" for="node" attr.name="label" attr.type="string"/>
  <key id="weight" for="node" attr.name="weight" attr.type="double" attr.default="1.0"/>
  <key id="color" for="node" attr.name="color" attr.type="string" attr.default="white"/>

  <graph id="weighted" edgedefault="directed">
    <node id="n1">
      <data key="label">Start</data>
      <data key="weight">10.5</data>
      <data key="color">red</data>
    </node>
    <node id="n2">
      <data key="label">End</data>
      <data key="weight">5.3</data>
    </node>
    <edge source="n1" target="n2"/>
  </graph>
</graphml>
```

### Hypergraph (Nested Nodes)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <graph id="hypergraph" edgedefault="directed">
    <node id="group1">
      <graph id="subgraph1" edgedefault="directed">
        <node id="n1"/>
        <node id="n2"/>
        <edge source="n1" target="n2"/>
      </graph>
    </node>
    <node id="group2">
      <graph id="subgraph2" edgedefault="directed">
        <node id="n3"/>
      </graph>
    </node>
    <edge source="group1" target="group2"/>
  </graph>
</graphml>
```

## Nested Graphs (Hierarchical Graphs)

Nodes can contain graphs, creating hierarchical structures:

```xml
<node id="compound">
  <graph id="inner" edgedefault="directed">
    <node id="inner_node1"/>
    <node id="inner_node2"/>
    <edge source="inner_node1" target="inner_node2"/>
  </graph>
</node>
```

This is useful for:

- Compound graphs (nodes containing subgraphs)
- Cluster visualization
- Hierarchical network representation

## Schema Validation

All GraphML documents should include:

```xml
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns
                    http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd"
```

This enables XML schema validation against the official XSD.

## Best Practices

1. **Always include namespace declaration** - Required for valid GraphML
2. **Use meaningful IDs** - Make node/edge IDs descriptive when possible
3. **Define keys before use** - All `<key>` elements should come before graphs
4. **Specify edge direction** - Explicitly set `edgedefault` for clarity
5. **Validate against XSD** - Use XML validators to catch errors early
6. **Use appropriate data types** - Choose the right type for each attribute
7. **Add descriptions** - Include `<desc>` elements for complex structures
8. **Default values** - Set sensible defaults in `<key>` definitions

## Limitations and Considerations

- GraphML doesn't enforce uniqueness across graphs (only within a graph)
- Edge IDs must be unique within a graph
- No built-in support for parallel edges (multiple edges between same nodes)
- Nested graphs may not be supported by all visualization tools
- Large graphs can create large XML files (consider compression)

## File Size Optimization

For large graphs:

- Use gzip compression (`.graphml.gz`)
- Consider specialized graph formats (GraphSON, edge list)
- Remove unnecessary attributes
- Omit edge IDs if not required

## Tools and Libraries

See the Ecosystem & Tools section for parsers, validators, and visualization software supporting GraphML.
