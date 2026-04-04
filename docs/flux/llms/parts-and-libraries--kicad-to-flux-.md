# Source: https://docs.flux.ai/Introduction/parts-and-libraries--kicad-to-flux-.md

# Parts and Libraries (KiCad to Flux)

Finding, adding, and managing parts within Flux compared to KiCAD.



## Overview

If you’re in a hurry, here’s what you need to know:

- In KiCAD, global and local libraries accessed differently in different projects. **In Flux, there is a unified library**, and whether you have access to a part or not is defined by the permissions that were set by the owner of the part.
- In KiCAD, symbols and footprints exist as different files that need to be linked. **In Flux, parts are a single entity that contains symbol and footprint.** [Learn more.](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts)
- Do you have your own KiCAD library? You can easily import it into Flux. [Learn more.](https://docs.flux.ai/flux/reference/reference-import-designs)

## Finding Parts in the Library

### In KiCad

KiCad separates parts into Global and Project-specific libraries. And access to each library is managed in a project-by-project basis. Meaning every project potentially has access to a different set of libraries. This is configured in the “Set up symbol libraries” menu.

![](https://uploads.developerhub.io/prod/86Yw/ytnjhi4x46l8txqn26g5cii8o6ph34z9jglr2zh7gl39b41a6qr5eq6p2k2hh5kp.png)

### In Flux



Flux’s approach is different. There’s a unified library where all parts are accessible. The library is accessed via the Library menu on the left side of a project view.

> The whole standard KiCad library is available in Flux. [Browse all the available parts](https://www.flux.ai/kicad-part-library).

#### Part's Access Management

Access to parts is determined by permissions set by the owner of said part. You can learn more about permissions [here](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions). The library will show:

- Parts owned by others that have been made public.
- Parts owned by others that have been shared with you.
- Parts you own.

#### Adding a part to a project

1. Open a project and locate the Library menu on the left.
    1. You can search and filter for parts using specific criteria, like "Contains Footprint" or MPN filters.
    2. For commonly used parts like capacitors and inductors, you can use generic parts that you can update later with the correct MPN.

2. Drag and drop the part onto your canvas.

> Instead of starting from scratch, you can leverage parts created by the community, saving you valuable time.

## Adding Parts to the Library (Creating a Part)

### In KiCad

Symbols and footprints are not necessarily related, other than when a footprint “is assigned to” a symbol. KiCad contains separate symbol and footprint libraries, which are created with different tools.

The process of creating a part looks something like: 

1. Open the Symbol Editor and create your symbol.
2. Use the Footprint Editor to design the footprint.
3. Link the symbol to the footprint in your project

![](https://uploads.developerhub.io/prod/86Yw/8hdnjil61nqvy8bzd1ibt0gjbda7byxw10b2gw3zdddt3m0wh3b2cbb6rshx22ds.png)

### In Flux



Symbols and footprints do not exist separately. There is no “assigning” a footprint to a symbol or part, every part contains a schematic, a symbol and a footprint.

Notice that we’ve said that each part contains a schematic and a symbol, this is a significant departure from KiCAD. Let’s see what that means with [an example](https://www.flux.ai/jharwinbarrozo/r-0805-2012-metric). When opening the link, the first thing you’ll notice is that the schematic only consists of two terminals. Terminals in Flux are equivalent to pins in KiCAD. So why isn’t there a symbol?

Parts have two “views” in Flux:

- **The internal view is what you see when you open a part**. It’s as if you were looking at what it has inside. Resistors, ICs, connectors, and almost every discrete part will only contain terminals.
- **The external view is what you see when you place the part in a project**. This is what we call the symbol. This view is what you’re used to when working with symbols in KiCAD. Learn more about how to create symbols

#### Importing KiCAD Libraries into Flux

You can import existing KiCAD parts directly into Flux:

1. Go to Import &gt; KiCad Part and follow the prompts.
2. Understand that in Flux, the schematic is distinct from the symbol, offering more customization options.

> Skip manual creation with our AI Importer that can quickly generate parts for you. [Learn more.](https://docs.flux.ai/flux/tutorials/ai-generated-component-libraries)

---

Next in the KiCad to Flux tutorial -&gt; [Schematics (KiCAD to Flux)](https://docs.flux.ai/flux/Introduction/schematics--kicad-to-flux-)