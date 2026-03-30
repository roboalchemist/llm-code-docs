# Source: https://docs.flux.ai/reference/elementnode.md

# ElementNode

The element node is one of the most commonly used subjects in Flux. It represents parts of you diagram.

## ElementNode operation properties

### type: "element" [readonly]

The type of this node, represented by the string literal "element"

### label: string

The name of the element that appears inline next to it in the diagram.

### properties: PropertyNode [readonly]

The properties of the route that appear in the inspector.

### terminals: ElementTerminalNode [readonly]

The terminals nodes of the element that store to which route they are connected to.

## Base node properties

### uid: string [readonly]

An internal identifier for a node.