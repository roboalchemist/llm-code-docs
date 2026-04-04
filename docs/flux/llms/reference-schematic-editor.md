# Source: https://docs.flux.ai/reference/reference-schematic-editor.md

# Flux Schematic Editor


Flux's schematic editor provides a powerful environment for building and simulating electronic circuits in real-time. This reference guide explains the key components of the schematic editor interface and how to use them effectively.

The schematic editor is where you build and simulate circuit schematics. Unique to Flux, everything you do here is synced in real-time to the cloud, which brings a number of benefits.

![From left to right: **Chat**: use this interface to chat with Flux . - **Library**: list of all the parts you have access to **Inspector:** shows contextual information about the selected element (properties, pricing, etc)](https://uploads.developerhub.io/prod/86Yw/wd321j35o47sze69ycmvf56y55y585efsv85kiyjruvug3wteagtp8e33ntrm6bk.png)


## Key Components

### Flux Menu

The schematic editor integrates with [Flux](https://docs.flux.ai/flux/tutorials/copilot-use-cases) to provide AI-assisted design capabilities.

### Library

The [Library](https://docs.flux.ai/flux/reference/reference-library) is the main place where you'll find parts to drag into your schematic. It serves as a public library for community-created parts and your own personal library.

### Object Tree

The [Object Tree](https://docs.flux.ai/flux/reference/reference-object-tree-schematic) contains a hierarchical list of all the elements placed in your schematic, allowing you to easily navigate and select components.

### The Canvas

The [Canvas](https://docs.flux.ai/flux/reference/reference-positioning-wiring) is where you'll create your schematic diagram. This is the main workspace where you place components and create connections between them.

### The Inspector

The [Inspector](https://docs.flux.ai/flux/reference/reference-inspector-schematic) panel on the right side shows contextual information about the selected object. When nothing is selected, the inspector shows document-level information like the description, assets, and other properties. When a part is selected, it shows contextual information about it.

The Inspector includes several important sections:

- [Controls](https://docs.flux.ai/flux/reference/reference-inspector-controls): allows users to add controls to interact with simulator models
- [Properties](https://docs.flux.ai/flux/reference/reference-inspector-properties): carry additional part metadata like Manufacturer part number, value, etc.
- [Pricing and Availability](https://docs.flux.ai/flux/reference/reference-inspector-pricing-and-availability): Flux automatically searches for pricing and availability in parts with a MPN.
- [Assets](https://docs.flux.ai/flux/reference/reference-inspector-assets): Leverage existing files (STEP, SVG, etc.) to use as footprints, pad, silk, or board shapes inside Flux designs.
- [Simulation](https://docs.flux.ai/flux/reference/reference-inspector-simulation): controls simulation parameters for the global project or selected part.

### Schematic Grid

Flux’s schematic editor doesn’t use a traditional grid. Instead, components snap relative to each other for faster, cleaner placement. Just drag a component near another and alignment guides will appear—helping you line things up visually without worrying about grid spacing.

### The Share Menu

You can access the [Share Menu](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions) using the "share" button in the navigation bar. Every project is private by default, and can only be shared using this menu.
