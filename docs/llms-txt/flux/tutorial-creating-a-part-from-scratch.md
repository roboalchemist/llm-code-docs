# Source: https://docs.flux.ai/tutorials/tutorial-creating-a-part-from-scratch.md

# Creating Components from Scratch in Flux: A Comprehensive Guide

Learn how to create custom components from scratch in Flux, giving you complete control over your component library.



## Overview

In this tutorial, we'll cover the complete process of creating custom components in Flux. You'll learn how to create each element of a component, from terminals and symbols to footprints and simulation models, and finally how to publish your creation to the library for future use.

This guide covers the following topics:

- **Creating a part schematic with terminals**
- **Creating a custom symbol**
- **Creating a custom footprint**
- **Adding a 3D model**
- **Creating a simulation model**
- **Publishing to the library**

## Creating Parts

Parts in Flux are made of 5 main components. All these components are optional, but a part missing a component won't offer its full capabilities:

- **Schematic:** you might find this concept confusing at first. The schematic is the "inside" view of a part. In all cases (except for [modules](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts)), the schematic of a part will consist of terminals only.
- **Symbol:** what you'll see when you drag that part into another project. If you're coming from another tool, you'll find them familiar. 
- **Footprint:** represents how the physical part will sit on the board.
- **3D model:** shows the 3D shape and dimensions of the part.
- **Simulation model:** describes how the part should behave during simulation.

### 1- Creating a New Part Schematic

The very first step is to create a new blank project. You can do so in the main Flux menu in the top-left corner.

Terminals are the foundation of every part created in Flux. They allow the part to interact with the rest of the circuit. To add terminals to a new part:

1. Go to the library
2. Search for "Terminal"
3. Drag in as many terminals as you need for your component

Different components require different numbers of terminals:

- Resistors, capacitors, and inductors typically have two terminals
- Transistors and potentiometers usually have three terminals
- ICs and other complex components may have many more

![The terminals of a BJT transistor in a part schematic.](https://uploads.developerhub.io/prod/86Yw/bmxjkqh8uo9wl6k43sj8vln921imeq3j5wjc792mfv0l2zujfwmkyrvvpo5np8rx.png)

#### 1.1 Setting Part Properties

If your part isn't a [generic part](https://docs.flux.ai/tutorials/tutorial-generic-part), it's good practice to populate the properties section. This allows other users to more easily search for and utilize your created parts.

Properties such as `Manufacturer part number (MPN)` and `Manufacturer Name` help other users verify they've found the correct part after searching. When this part is brought into a project, these properties will be pre-loaded to save time and add additional detail.

Any property that isn't populated can be added later after the part is dropped into the canvas in another project.

After the part is created and dropped into the canvas, clicking on the eye icon next to each property will make it visible or hidden in the canvas.

### 2- Creating a Symbol

The symbol is the schematic representation of your component. For detailed instructions on creating custom symbols, please refer to our [working with symbols tutorial](https://docs.flux.ai/flux/tutorials/working-with-symbols).

Key aspects of symbol creation include:

- Designing a clear, recognizable shape
- Properly positioning pins
- Adding labels and designators
- Following industry standard conventions when possible

![](https://uploads.developerhub.io/prod/86Yw/rvlci04h66d3i9z0ddlkcj75zj1shg25qsp5pi0q51zjznnlx9izg2v95d74usbm.png)

### 3- Creating a Footprint

The footprint defines the physical layout of your component on the PCB. For detailed instructions on creating custom footprints, please refer to our [working with footprints tutorial](https://docs.flux.ai/flux/tutorials/working-with-footprints).

Important considerations for footprint creation:

- Accurate pad dimensions and spacing
- Proper silkscreen markings
- Courtyard definition
- Alignment with manufacturer specifications

![](https://uploads.developerhub.io/prod/86Yw/3oahsi1tew1z30wxedkukmnhy8idyeue2mvhw9z44a7e2vm53jhkl5wcrjrw88ms.png)

### 4- Adding a 3D Model

Flux currently supports importing 3D models rather than creating them from scratch. You can learn more about importing a 3D model in our [importing components tutorial](https://docs.flux.ai/flux/tutorials/tutorial-import-part#4--importing-a-3d-model).

3D models enhance your design by:

- Providing visual verification of component placement
- Enabling clearance checking in three dimensions
- Improving the presentation of your final design

![](https://uploads.developerhub.io/prod/86Yw/sl72dlokp8hiy6u5yf0u6plbu10o1nc6d8zv04ntmabwym2gc81n7zu79mk3jhk7.png)

### 5- Creating a Simulation Model

The simulator provides real-time information on circuit behavior. For a part to know how to behave, it must contain a simulation model to follow. Flux currently provides simulation models for most commonly used parts in a circuit.

To learn more about simulation models:

- Check our [simulator tutorial](https://docs.flux.ai/flux/tutorials/the-simulator) for a deep-dive on how the simulator works
- Review the [list of simulation models available](https://docs.flux.ai/flux/reference/resistor) for specific part types compatible with the simulator

![](https://uploads.developerhub.io/prod/86Yw/skklbozxdzegqrqcz5zmo4hg0xw0ur36isfsrchq57mmd6wmni5ra82fvnt3bsco.png)

### 6- Publishing to the Library

The final step is to publish your part to the library. Publishing is important because new projects in Flux don't show up in the library by default. You have to intentionally choose to share them there.

- Type `⌘P` on Mac or `Ctrl P` on Windows, or
- Click on the Flux Menu in the upper left corner of the screen
- Choose "Publish to Library..."
- Select "Publish"

![](https://uploads.developerhub.io/prod/86Yw/bvt8iarwexiwhasmstfseyx1juu4w10iwltb84po0ovim5xfrj5ij3otcafojsrx.png)

You can read more about the publishing process [here](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library).

## Best Practices for Component Creation

To ensure your components are useful and accurate:

1. **Follow industry standards**: Use standard symbols and footprints when possible
2. **Include comprehensive metadata**: Add manufacturer part numbers, descriptions, and tags
3. **Create accurate footprints**: Double-check dimensions against datasheets
4. **Add pin labels**: Clearly label all pins with their functions
5. **Test in a real design**: Verify the component works as expected in an actual project

## Troubleshooting Common Issues

### Symbol Creation Problems

If you're having trouble with symbol creation:

- Ensure all pins are properly matched to terminals
- Check that pin numbering matches the datasheet
- Verify the symbol follows standard conventions for clarity

### Footprint Issues

When creating footprints:

- Double-check all dimensions against the datasheet
- Ensure pad sizes are appropriate for manufacturing
- Verify that the footprint orientation matches the standard

### Simulation Model Challenges

If your simulation model isn't working correctly:

- Verify that you've selected the appropriate model type
- Check that all parameters are correctly entered
- Test with simple circuits first to isolate issues