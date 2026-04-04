# Source: https://uat.rive.app/docs/editor/fundamentals/design-vs-animate-mode.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Design vs Animate Mode

> The Rive Editor has two distinct modes, Design and Animate. Switching between modes changes the interface to show the appropriate tools and options.

## Design Mode

Use Design Mode to prepare your graphics for animation. This is where you can design your own graphics with Rive's [tools](../interface-overview/toolbar), [import graphics from other software](./importing-assets), or rig your graphics with [bones](../manipulating-shapes/bones), [transform spaces](./transform-spaces), [layouts](https://rive.app/docs/editor/layouts/layouts-overview), [joysticks](https://rive.app/docs/editor/manipulating-shapes/joysticks), and [constraints](../constraints/).

<img src="https://mintcdn.com/rive/4qxx_h2cmmvnoly3/images/editor/fundamentals/Design_Mode.png?fit=max&auto=format&n=4qxx_h2cmmvnoly3&q=85&s=b7ecdb5433cbc45851d0385517d4f1dd" alt="Image" width="3456" height="2160" data-path="images/editor/fundamentals/Design_Mode.png" />

Design Mode is the default mode for any file that doesn't have any animations created. The mode exists because Rive allows you to attach multiple animations to a single artboard, so you need a place to set up and create those graphics.

## Animate Mode

Use [Animate Mode](../animate-mode/) to create all of the [States](https://rive.app/docs/editor/state-machine/states) and [State Machine](../state-machine/) for your artboard.

When you switch to Animate Mode, the UI updates to display a list of Timelines and State Machine associated with the [active artboard](./artboards#active-artboard). The [Inspector](https://rive.app/docs/editor/interface-overview/inspector) also updates to show key buttons next to any property that can be animated.

<img src="https://mintcdn.com/rive/4qxx_h2cmmvnoly3/images/editor/fundamentals/Animate_Mode.png?fit=max&auto=format&n=4qxx_h2cmmvnoly3&q=85&s=e9a63e327a4fb2c5df86ac3f86ebcd03" alt="Animate Mode Pn" width="3456" height="2160" data-path="images/editor/fundamentals/Animate_Mode.png" />

Selecting any Animation from the Animations list will bring up a timeline view, while selecting a state machine will replace the timeline with the graph view.

<img src="https://mintcdn.com/rive/4qxx_h2cmmvnoly3/images/editor/fundamentals/State_Machine.png?fit=max&auto=format&n=4qxx_h2cmmvnoly3&q=85&s=58361e841e1c0252b3286f507ec136f7" alt="State Machine Pn" width="3456" height="2160" data-path="images/editor/fundamentals/State_Machine.png" />

## Creating Assets in Animate Mode

While there are separate modes, graphics can be created and changed in both modes, but it's important to keep a few things in mind.

1. If a Timeline is selected, graphics, both procedural and custom paths, can be created. While graphics can be created, any changes to the path, shape, or its properties will automatically be keyed on the timeline. Because of this, we recommend not making any assets when a timeline is selected.
2. Animate Mode works like Design Mode if a State Machine is selected. Asset creation, rigging, and other design changes will not be automatically keyed. This lets you make any design changes you want without switching between the different modes, though you do lose some screen real estate due to the graph. We recommend making vast changes in Design mode while using Animate mode only to add quick adjustments like hitboxes or layouts.
