# Source: https://docs.flux.ai/Introduction/kicad-to-flux.md

# KiCAD to Flux - Getting started

Are you a KiCad EDA user looking to take your first steps in Flux? In this tutorial, we’ll cover how the basic workflows translate between the tools and the terminology you need to understand to succeed in Flux. 



## Overview

If you’re in a hurry, here are the need-to-know basics for migrating from KiCad EDA to Flux:

- User Interface
    - **Flux is an all-in-one tool**. Meaning libraries, schematics and layout are created with the same interface.
    - **There are no files in Flux**, every project is easily accessible through its URL
    - **Files are automatically version controlled**. [Learn more.](https://docs.flux.ai/flux/tutorials/version-control---deep-dive)

- Parts and Libraries
    - In KiCAD, global and local libraries accessed differently in different projects. **In Flux, there is a unified library**, and whether you have access to a part or not is defined by the permissions that were set by the owner of the part.
    - In KiCAD, symbols and footprints exist as different files that need to be linked. **In Flux, parts are a single entity that contains symbol and footprint**. [Learn more.](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts)
    - Do you have your own KiCAD library? You can easily import it into Flux. [Learn more.](https://docs.flux.ai/flux/reference/reference-import-designs)

- Schematic Editor
    - Everything you’ll find on the properties panel in KiCAD, i**n Flux you can find in the inspector tab (right side of the screen) under properties**. From datasheet links, properties, to live pricing.
    - KiCAD supports various type of labels to connect nets. **In Flux, labels are replaced by a part called “portal”**. You can find portals with different symbols in the library.

- PCB Editor
    - Netlist and ECO do not exist in Flux. **Schematic and PCB data are automatically synchronized.** 
    - Everything you’ll find on the layout properties panel in Kicad, **in Flux you can find in the inspector tab (right side of the screen) under rule**s. [Learn more.](https://docs.flux.ai/flux/reference/reference-inspector-layout)
    - **Flux automatically creates ground fills (planes) connected to ground**. [Learn more.](https://docs.flux.ai/flux/tutorials/tutorial-ground-fills-deep-dive)

## Accessing Libraries, Schematics, and Layout

### In KiCad

KiCad uses multiple tools for each aspect of your design:

- Symbol Editor for creating/editing symbols
- Footprint Editor for footprints
- Schematic Editor and PCB Editor for circuit design and layout

![](https://uploads.developerhub.io/prod/86Yw/64yhkhkk9mpywtql54k36y5ypdk74nbcloe50r8aymmy7m17y5qfotqjc1u3wczx.png)

### In Flux

Flux integrates all these aspects into one single all-in-one tool:

- **Profile Page:** The first screen after logging in to Flux is your profile page. This is where you’ll find every project you have contributed to, starred, or cloned
    - Your Flux profile is sharable so other people can see your public projects. Essentially acting as a portfolio.

- **Project Page**: is where you access design elements like parts, schematics, and layouts.
- **Flux keeps everything linked in the cloud**, there’s no need to manage separate files.



> Flux handles file management for you, making it easy to share projects via URLs without worrying about version mismatches or missing files. [Learn more.](https://docs.flux.ai/flux/tutorials/version-control---deep-dive)

---

Next in the KiCad to Flux tutorial -&gt; [Parts and Libraries (KiCad to Flux)](https://docs.flux.ai/flux/Introduction/parts-and-libraries--kicad-to-flux-)