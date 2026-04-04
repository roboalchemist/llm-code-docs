# Source: https://docs.flux.ai/reference/nets-and-traces.md

# Nets and Traces

When creating traces for a PCB, often times you will need to increase or decrease the size of the traces for a specific net. This can be done either through the specific net itself or, if you need to apply the size change to several nets, using rulesets.

![](https://uploads.developerhub.io/prod/86Yw/fzsuacb0mwd7iv8m5u5po6zspb3olhzxinl962i2e3ob19jyynjnhowaw2zoa14b.png)

## What Is a Net?

**Nets** are a collection of electrically connected nodes in PCB design software. They represent paths for electrical signals to travel between components on the board. Every terminal on a PCB design program is connected to a net, and (unless in the case of high frequency transmission lines) all points on a net should share the same voltage. Nets oftentimes are named for easy identification and organizational purposes. Nets are used to generate netlists, which is a list of all the electrical connections to each component in the design.

## What is a Trace?

Whereas a net represents the logical collection of nodes with a shared electrical connection, a **trace** is the physical conductive pathways that actually connects the individual components. A single net may represent the electrical connection of multiple components all sharing a single voltage value. This net, however, would be composed of multiple traces.

Traces are typically made of copper and can vary in widths depending on the desired current carrying capacity.

## Trace and Net Specific Rules

Flux contains other related rules that allow you to further customize the behavior of traces and nets, listed below. See the [complete list of rules](https://docs.flux.ai/reference/layout-rules-types) for further information and examples for using each.

- **Fill stitching density**: creates vias in a ground or power net fill, known as fill stitching.
- **Fill stitching offset**: allows for offsetting fill stitching.
- **Preferred trace width**: allows for presetting trace-widths for easy toggling during routing.
- **Trace shape**: defines the shape of a trace, either curved or arced.
- **Trace width**: sets the width of a trace (or collection of traces).

## Naming and Renaming Nets

To keep your design organized and make debugging easier, you can rename nets to something more descriptive than the default auto-generated names. In Flux, you can do this by selecting the net from the Object Tree, then updating the “Designator” field in the Inspector panel. Giving nets intuitive names (like `VCC`, `GND`, or `UART_TX`) makes it easier to apply rules, track signal paths, and communicate design intent with your team.

## Deleting Traces

Whether you're cleaning up a few connections or doing a full reroute, there are two ways to delete traces in Flux:

### Delete single traces

Click to select the trace, then press `Del`, or right-click and choose Delete.

### Delete multiple traces using the Objects panel

 Open the Objects panel on the right:

- **To remove all traces under a specific net**, expand the net in the list, select the traces, and press `Del`.
- **To wipe out** _**all**_ **traces**, type `"trace"` in the search bar, select the first result, hold `Shift`, scroll down, select the last one, and press `Del`.