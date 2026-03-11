# Source: https://docs.flux.ai/reference/elementterminalnode.md

# ElementTerminalNode

The element terminal node represents a elements terminal.

## ElementTerminalNode operation properties

### type: "elementTerminal" [readonly]

The type of this node, represented by the string literal "route"

### parentUid: string [readonly]

The internal identifier of the parent node.

### name: string [readonly]

The name of the terminal that appears inline next to it in the diagram.

### voltage: number | undefined [readonly]

The current voltage at the terminal.

### current: number | undefined [readonly]

The current flowing through the terminal.

### voltageHistory: Array&lt;number&gt; [readonly]

The history of voltages at the terminal.

### currentHistory: Array&lt;number&gt; [readonly]

The history of currents flowing through the terminal.

### outputs: OutputNode

Gets/Sets the outputs for the terminal.

## Base node properties

### uid: string [readonly]

An internal identifier for a node.