# Source: https://docs.flux.ai/reference/outputnode.md

# OutputNode

The output node represents a documents simulation output to for example display a parts power consumption to the user.

## OutputNode operation properties

### type: "output" [readonly]

The type of this node, represented by the string literal "route"

### parentUid: string [readonly]

The internal identifier of the parent node.

## name: string

The user visible name of the Output Node.

## value: string | number

The value of the Output Node.

## unit: string

The unit of the Output Node.

## displayInline: boolean

Whether to show the output on canvas by default.

## Base node properties

### uid: string [readonly]

An internal identifier for a node.