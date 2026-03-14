# Source: https://docs.flux.ai/reference/flux.md

# Flux global object

These are methods and properties available on the `flux` global object.

## General

### apiVersion: string [readonly]

The version of the Flux API this plugin is running on.

### print(message: string): void

_Prints message to stdout_

### on(type: string, callback: (event: LifeCycleEventContext | InputControlEventContext) =&gt; void): void

Registers an callback that will be called when an event happens in the editor.

### once(type: string, callback: (event: LifeCycleEventContext | InputControlEventContext) =&gt; void): void

Same as flux.on, but the callback will only be called once, the first time the specified event happens.

### off(type: string, callback: (event: LifeCycleEventContext | InputControlEventContext) =&gt; void): void

Removes a callback added with flux.on or flux.once.

### notify(message: string, options?: NotificationOptions): NotificationHandler

Shows a notification at the center top of the screen.

### outputs(outputs: ReadonlyArray): ReadonlyArray

Sets/Gets the Documents public output metrics.

### createOutputNode(): Readonly

Creates a new output node.

### controls(controls: ReadonlyArray): ReadonlyArray

Sets/Gets the Documents public output metrics.

### createControlNode(): Readonly

Creates a new control node.

### properties(properties: ReadonlyArray): ReadonlyArray

Sets/Gets the Documents public properties.

### createPropertyNode(): Readonly

Creates a new property node.

### assets(properties: ReadonlyArray): ReadonlyArray

Sets/Gets the Documents assets.

### currentSymbol(symbol: string | undefined): string | undefined

Sets/Gets the Documents public symbol from one of the assets.

### nodes(nodes: ReadonlyArray): ReadonlyArray

Sets/Gets the Documents nodes.

### getNodeById(uid: string): DiagramNodeTypes | null

Finds a node by its uid in the current document. Every node has an uid property, which is unique. If the uid is invalid, or the node cannot be found (e.g. removed), returns null.

### simulationModel(modelConfig: SimulationModelConfigs): SimulationModelConfigs

Sets/Gets the atomic simulation model to be used.