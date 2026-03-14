# Source: https://docs.flux.ai/Introduction/schematics--kicad-to-flux-.md

# Schematics (KiCAD to Flux)


This section dives into how to work with parts in schematics, wiring them together, and managing your Bill of Materials (BoM) in Flux.




## Overview

If you’re in a hurry, here’s what you need to know:

- Everything you’ll find on the properties panel in Kicad, **In Flux you can find in the inspector tab (right side of the screen) under properties**. From datasheet links, properties, to live pricing.
- KiCAD supports various type of labels to connect nets. **In Flux, labels are replaced by a part called “portal”**. You can find portals with different symbols in the library.

## Working with Parts on the Schematic

### In KiCAD

In KiCad, part properties like designators, datasheets, etc., are directly accessible via the symbol properties.

{% image url="https://uploads.developerhub.io/prod/86Yw/vi4f1jmuj03225hrcsxfk4vojlk9evd04343joxq9cudswyiwnenpc8j961nzpdu.png" mode="600" height="1307" width="2324" %}
{% /image %}

### In Flux




Component properties can be accessed through the inspector menu on the right side:

- Properties: equivalent to KiCAD’s symbol fields. Contains metadata info for parts, including MPN, manufacturer info, etc.
- Availability and pricing: Flux automatically displays pricing and availability information for parts with an MPN property.
- Assets: here’s where you add external assets (symbols, thumbnails, etc.) to your project or parts.
- Simulation: configure simulation parameters like speed, step, etc

> For parts that contain a Manufacturer Part Number property, Flux will automatically add live pricing and availability information from the main distributors (DigiKey, Mouser, etc.). [Learn more.](https://docs.flux.ai/flux/reference/reference-inspector-pricing-and-availability)


> Need help finding the right part or an alternative part? Use Flux to do part research. [Learn more.](https://docs.flux.ai/flux/tutorials/ai-component-research)


## Wiring Parts

### In KiCAD

In KiCad, you connect parts using wires, labels (global and hierarchical), and portals.

{% image url="https://uploads.developerhub.io/prod/86Yw/zajoxzwqjmp2yum9v9c5qxqdqztfz2dozxujdfzqazzr6qdmzc3a2qooqyswqjzu.png" mode="600" height="398" width="708" %}
{% /image %}

### In Flux




Flux simplifies connectivity with wires and net portals:

- Wires: hover over a part and click on the circle that appears at the end of the pin to create a wire.
- Net Portals: Use these for easy connections, including power and ground. Search “portal” in the library and drag it into your project.
- Use Power/GND portals for managing power distribution. The work exactly as net portals, but have a power/GND symbol for better legibility.

> Integrated version control lets you revert to previous states if you make a mistake while wiring. [Learn more.](https://docs.flux.ai/flux/tutorials/version-control---deep-dive)


## Managing the Bill of Materials (BoM)

### In KiCAD

You can generate your BoM using the “Generate BoM” menu. BoMs are generated based on customized scripts.

{% image url="https://uploads.developerhub.io/prod/86Yw/mz94vv19x7ny9a7fi6u693db7gv0qu4jylpxp5izret2iijd3ymuag8gyzi9t3xl.png" mode="600" height="996" width="1770" %}
{% /image %}

### In Flux

BoMs are automatically generated and exportable in various formats for the main manufacturers.

{% image url="https://uploads.developerhub.io/prod/86Yw/bgtte0qhsurwb7eahkailmlu9x6wyvbfxf9s6zqk5jz8tk58xau1m8md7a6pwayp.png" mode="600" height="1588" width="2823" %}
{% /image %}

---

Next in the KiCad to Flux tutorial -&gt; [Layout (KiCAD to Flux)](https://docs.flux.ai/flux/Introduction/layout--kicad-to-flux-)
