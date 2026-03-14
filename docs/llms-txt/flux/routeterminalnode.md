# Source: https://docs.flux.ai/reference/routeterminalnode.md

# RouteTerminalNode

The route terminal node represents a routes terminal.

## RouteTerminalNode operation properties

### type: "routeTerminal" [readonly]

The type of this node, represented by the string literal "route"

### parentUid: string [readonly]

The internal identifier of the parent node.

### elementUid: string [readonly]

The element uid this route terminal is connected to.

### terminalUid: string [readonly]

The terminal uid this route terminal is connected to.

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