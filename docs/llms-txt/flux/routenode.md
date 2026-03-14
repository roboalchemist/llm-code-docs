# Source: https://docs.flux.ai/reference/routenode.md

# RouteNode

The route node is one of the most commonly used subjects in Flux. It represents the wires that connect your part terminals with each other..

## RouteNode operation properties

### type: "route" [readonly]

The type of this node, represented by the string literal "route"

### label: string

The name of the route that appears inline next to it in the diagram.

### properties: PropertyNode [readonly]

The properties of the route that appear in the inspector.

### terminals: RouteTerminalNode [readonly]

The terminals of the route that store what part terminals the route is connected to.

## Base node properties

### uid: string [readonly]

An internal identifier for a node.