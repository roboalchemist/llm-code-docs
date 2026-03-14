# Source: https://docs.flux.ai/reference/propertynode.md

# PropertyNode

The property node represents a document/element/route property which are used to specify components.

## PropertyNode operation properties

### type: "property" [readonly]

The type of this node, represented by the string literal "route".

### parentUid: string [readonly]

The internal identifier of the parent node.

### value: string | number | boolean | BigNumber | {} [readonly]

The value of the property. We support [BigNumber](https://mikemcl.github.io/bignumber.js/) here for higher resolution. For string values we run the same expression evaluation like we do in the UI...if you just want the raw value you can use .rawValue

### rawValue: string | number | boolean | BigNumber | {} [readonly]

The  raw value of the property. As opposed to . value we just provide the actual value of the property.

### unit: string | undefined [readonly]

The unit postfix thats set for the property.

## Base node properties

### uid: string [readonly]

An internal identifier for a node.