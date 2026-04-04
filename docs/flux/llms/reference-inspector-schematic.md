# Source: https://docs.flux.ai/reference/reference-inspector-schematic.md

# Schematic Inspector


Edit and view more information about objects on the schematic and your project.

## Overview

Use the inspector to view more information and change configurations for components, objects, and the project. It's located inside the Inspect tab in the right drawer, a unit on the right side of the editor. 

It's contextual to your selection. When an object is selected, you'll see info about that object. If no object is selected (like if you click on an empty section of the canvas), the inspector will show information about the project. It's also contextual to the mode you're in. When you're on the Schematic, you see different information than when you're on the PCB. And when you resize its width, it can show even more information.

![The inspector is located in the Inspect tab in the right drawer.](https://uploads.developerhub.io/prod/86Yw/ij6d14byae73d60r6ay42ax15ax35mzbow0i479ff4e687wsxshnj7mmchuhlo70.png)


## Inspector Panels

Sections found in the inspector are called panels. On Schematic, you'll see the following panels:

- **About** – The About panel allows you to view and edit high level information about the project, component, or net.
- **Controls** – The [Controls panel](https://docs.flux.ai/flux/reference/reference-inspector-controls) allows you to interact with components in ways which affects the behavior of the circuit and simulator.
- **Properties** – The [Properties panel](https://docs.flux.ai/flux/reference/reference-inspector-properties) allows you to define information in a structured way for the project, components, and nets. Some properties drive behavior elsewhere in Flux. Properties also get passed into Flux as context.
- **Availability & Pricing** – The [Availability & Pricing panel](/flux---documentation/flux/reference-inspector-pricing-and-availability) shows up-to-date availability and pricing information for the project and components.
- **Assets** – The [Assets panel](https://docs.flux.ai/flux/reference/reference-inspector-assets) is where external files live, such as SVGs to use as custom symbols, or 3D models.
- **Simulation** – The [Simulation panel](https://docs.flux.ai/flux/reference/reference-inspector-simulation) allows you to control the simulator engine and view its outputs.

## Contextual to What's Selected

The inspector shows different panels which have different functions depending on what's selected.

### Project Selected

- **About** – Information about the project.
- **Controls** – Controls defined for the project.
- **Properties** – Structured information describing the project.
- **Availability & Pricing** – Total cost of the project, taking into account components with MPNs or DPNs and the project's manufacturing quantity target.
- **Assets** – Files stored in the project.
- **Simulation** – Control the simulator engine in the project.

### Component Selected

- **About** – Information about the component.
- **Controls** – Controls defined for the component by the component creator.
- **Properties ** – Structured information describing the component.
- **Availability & Pricing** – Availability and pricing information for the component, assuming the component has an MPN or DPN.
- **Simulation** – Outputs for the component.

### Net Selected

- **About** – Information about the net.
- **Properties** – Structured information describing the net.

### Multiple Objects Selected

- **About** – Alter the designators of the multi-selection.
- **Properties** – Alter the properties of the multi-selection.

## Change the Width to See More

The inspector shows more information when it's wider. To change the width of the inspector, move your cursor to the left edge of the right drawer, then drag it left or right.
