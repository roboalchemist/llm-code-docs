# Source: https://docs.flux.ai/reference/design-rule-check--drc-.md

# Design Rule Check (DRC)

Flux’s [layout rules](https://docs.flux.ai/flux/tutorials/tutorial-layout-rules-deep-dive) do a great job of eliminating unnecessary mistakes, but certain types of violations require additional checking. Such violations include overlapping traces, unrouted nets, missing footprints, etc.

In Flux, DRCs run in real-time, and their results can be accessed from the messages menu. 

![](https://uploads.developerhub.io/prod/86Yw/8prubj0bf0e1aurbyel5opm7gtms1jmxd6s72xzwzwlt6o28qqgryowqm7plsibn.gif)

## Overlapping Traces

Triggers a DRC violation when **two traces from different nets overlap each other.** 

![](https://uploads.developerhub.io/prod/86Yw/u4i80cei0wox6cmlxh73lixplopqikqo2d47hjrmn4bbh0zauz3uqvzabpa9l73b.gif)

## Missing Footprints

Triggers a DRC violation **when a component from the schematic does not have a footprint. This rule does not apply if the component has the property "Exclude from PCB".**

![](https://uploads.developerhub.io/prod/86Yw/l32tmn27jx1wmyzh8dexciykx7zpf21tguspjxr0fad3ftdzub1jnrevxjvp1f60.gif)

## Airwires

Triggers a DRC violation when there are existing airwires that remain on the board. Airwires show connections between nodes based on the schematic that are not yet connected on the board through copper. Signifies that terminals are not connected properly. To be properly connected, only connections to the center of pads are considered valid. Airwires are also refered to as ratsnest in other tools.

![](https://uploads.developerhub.io/prod/86Yw/tb7ormdf5z53wstfjfqk8fi78byuedb112pw31twu3c2t9xqouzzdnmbhocb5lbi.png)

## Invalid Layer

Triggers a DRC violation when nodes that are assigned to a layer do not exist in the layout stack up. This is common when adding a [module](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts) that contains more layers than the project in which it's placed. Ensure that each node is assigned to an existing layer.

## Component Overrides

This rule is triggered when a component has been modified using the “!important” flag.

## Board Layer with Multiple Copper Fills

This rule is triggered when there is a request for multiple copper fills of different nets in a single layer. Double check the _Connected Layers_ rule value for a Net object with fills is valid. In Flux, each copper fill is connected to a single layer, and thus two different fills may not occupy the same layer.

![](https://uploads.developerhub.io/prod/86Yw/693m2svs4jj8ek7bom6j80pint8jaqp5k9jt62p5bzquoubavphpmt5gdqvkvke4.gif)

## Floating Copper

Detects any via, trace or copper fill island that is not connected to any net.

More specifically, this rule is triggered when any area of copper that is not connected to a pad. This includes copper fill islands, floating vias, floating traces, and any floating connected components. This rule will also trigger if a copper fill island contains a stitching via but remain isolated from the larger ground plane. 

In order to clear this DRC rule ensure that your vias are connected and all traces and components are wired to their respective nets. For isolated copper fill islands: 

1. Ensure that there are appropriate stitching vias placed within the island if enough space is available
2. If there is not enough space, simply add an additional keep out rule spacing the copper out further from its surrounds components or other nets, such that the island does not form. 

> There is current no automated reliable method of removing copper fill islands. However, the triggering of this rule and subsequent manual handling of islands will ensure better board quality.