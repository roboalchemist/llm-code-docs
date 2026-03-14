# Source: https://docs.flux.ai/tutorials/working-with-symbols.md

# Working with Schematic Symbols in Flux: Creating Professional Component Representations

Easily create professional-looking symbols without drawing, or use the advanced tools to create custom-shaped symbols for your PCB designs.



## Overview

Flux works slightly differently than other PCB design tools you might be used to. In Flux, parts have two different views: the schematic and the symbol. The schematic view only contains the terminals, while **symbols are only visible when a part is placed into a project**.

To see a part's symbol at any point in the process, you need to:

1. Configure a parametric symbol, or create a custom one
2. [Publish to the library](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library)
3. Create a new project and add the part you just published
4. This process needs to be repeated every time a symbol is updated

Flux offers two main approaches to symbol creation:

### Parametric Symbols

Flux's **parametric symbols** allow you to better organize your schematic symbols by grouping pins based on functionality and logical connection, all without needing to physically draw the symbol. Instead, by attaching properties to terminals, symbols for parts and modules can organize themselves automatically.

![](https://uploads.developerhub.io/prod/86Yw/ydp5qfumw7bgn0q0y5k3xkoqzx0h0w643r9ahz6f7bipmopb6qfnjpo4xf3g14jr.gif)

### Custom Symbols

Flux's **custom symbols** provide more flexibility to create advanced or custom shapes for specialized components or to match industry standards.

## Parametric Symbols

Parametric symbols can be customized to create different sections within the symbol, group pins, or locate pins on a specific side of the symbol (left or right).

![](https://uploads.developerhub.io/prod/86Yw/5wufa0kx5zyt35orc4muhqyfvsjc3epe7vjuemq05ss2ux1xyy618c5p4ep3nbpw.png)

### Adding Terminals

The first step in the process is to add a terminal for every pin in your part:

1. Use the library menu on the right to find the element called "Terminal"
2. Click and drag as many terminals as you need onto the canvas
3. Select the newly added terminals and change their designator to match the target pin name

![](https://uploads.developerhub.io/prod/86Yw/7csnpcevhis1ucak4idvjjgkrpa9cy6e4oj4z7q876eldg9fctge4q48ycr5zffq.png)

### Changing Pin Numbers

To change a pin number:

1. Select the terminal(s) you want to edit
2. Locate the "Pin Number" property in the inspector menu
3. Enter the pin number according to the component datasheet

![](https://uploads.developerhub.io/prod/86Yw/0pkx53mu4b18vpjlrvzrmovc9kwqatyg3kqkafxhe1nh32p6q5qzc1hkesc4352n.png)

### Creating Sections

Sections allow you to create named areas within the symbol to locate related pins. For example, on a microcontroller, one section could be "Power" and another one "GPIO".

Terminals with no section property assigned will all be located in the same empty area.

To create a new section:

1. Select all the terminal(s) you want to be located in the same section
2. Locate the properties section on the right and click on the "Edit" button
3. Add a new property called "Section"
4. Type the section name in the textbox

![](https://uploads.developerhub.io/prod/86Yw/wdxnyprber4s5i17jvc31nndloypzvqj4xwxb7z8ds4z8ddnx4cogkpftdhxbz1a.png)

### Creating Pin Groups

Pin groups allow you to group together related pins and visibly separate them from other groups. Pins in the same group will be located closer together, and slightly further apart from pins in other groups. For example, within the GPIO section, you can group pins based on register or peripheral.

Terminals with no _pin group_ property assigned will be located further apart from each other and from other groups.

To create a new pin group:

1. Select all the terminal(s) you want to be located in the same group
2. Locate the properties section on the right and click on the "Edit" button
3. Add a new property called "Pin Group"
4. Type the group name in the textbox

![](https://uploads.developerhub.io/prod/86Yw/9uqg2zuf438noet6dlpc7fjip9w84t44kljzra1hty86jyttgek3b8e2a5uvdwef.png)

### Changing Pin Orientation

Pin orientation allows you to manually locate pins on the left or right side of the symbol.

To change a pin's location:

1. Select all the terminal(s) you want to change location for
2. Locate the properties section on the right and click on the "Edit" button
3. Add a new property called "Pin Orientation"
4. Type "Left" or "Right" in the textbox

![](https://uploads.developerhub.io/prod/86Yw/61xmn0l3tkvgu5ivahd5d9wi8lvatrmzk2owb71sayzy7jnweomurtqpvx84c0h5.png)

### Changing Pin Order

By default, pins will be sorted within their groups/sections in the order specified by the Pin Number. To configure pins in a different order:

1. Select the terminal(s) you want to edit
2. Locate the "Terminal Order" property in the inspector menu
3. Use numbers to set the order. Lower numbers will be placed first

![](https://uploads.developerhub.io/prod/86Yw/35dpf49x3aui80pzo5t6iia2wppxralgf1hnsuiqlpkhemcfoq13llbn426ivyat.png)

### Forcing Parametric Symbol View

Adding any of the properties described above will cause a symbol to be changed from regular to parametric. If you want to force a symbol to look like a parametric symbol without setting groups or sections:

1. Open the component and make sure nothing is selected
2. Find the inspector menu on the right and locate the Properties sub-menu
3. Click on the "Edit" button and add a property called "Symbol Style"
4. Set the "Symbol Style" property to "Parametric"

### Multi-Symbols

Parametric symbols also support splitting the symbol into multiple parts. This is especially useful to keep designs with high pin-count components clean and organized.

To split a symbol into multiple parts:

1. Select all the terminals that you want to put into a different part
2. Find the inspector menu on the right and locate the Properties sub-menu
3. Click on the "Edit" button and add a property called "Sub-symbol Designator Suffix"
4. Type the suffix. Each part of the symbol will be called "[designator]:[suffix]", for example "U1:power" or "U1:1"

![](https://uploads.developerhub.io/prod/86Yw/1ykvkouybjqt8dmmqiub3z5nzqxuwxzvbrf719szc0heefnt53kbhib2wxuwimvc.gif)

## Creating a Custom Symbol

If the default parametric symbol does not work for your use case, you can create a custom symbol. **We suggest only advanced users try this process as it requires external tools.**

Refer to the [Custom Pad Shapes](https://docs.flux.ai/flux/tutorials/custom-pad-shapes) tutorial to learn how to create a custom symbol shape. Once you have the asset created and added to Flux, proceed to matching pin locations.

### Matching Pin Locations

By default, all terminals will be located at the center of the symbol. To position the terminals to the desired location, there are a few more steps. We've covered this process both in video and written format.



1. [Publish the part](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library)
2. Create a [New Blank Project](https://docs.flux.ai/flux/reference/reference-blank-project) and drag the part you're importing.
3. You'll notice that both terminals are at the center of the symbol. Now go back to the imported part.
4. You'll need to do this process for every terminal in your part
    1. Select the terminal and find the "Properties" menu in the right-side panel.
    2. In the "Symbol Pin Position" field, type the desired x and y coordinates for the terminal to sit on the symbol.
    3. Publish the part and go back to the new project. You'll see a "Update available for your parts" legend in the bottom left. Click on "Review" and accept the changes.
    4. You'll notice that the terminals have moved. You might need to repeat this process a few times to nail the perfect position.

## Best Practices for Symbol Creation

1. **Follow industry standards**: Use standard symbol representations when possible
2. **Group related pins**: Organize pins by function (power, I/O, communication)
3. **Use consistent orientation**: Power pins typically go on top, ground on bottom
4. **Label clearly**: Use descriptive pin names that match the datasheet
5. **Split complex components**: Use multi-symbols for high pin-count devices
6. **Maintain proportions**: Keep symbol size proportional to pin count

## Troubleshooting Common Issues

### Symbol Not Appearing

- Verify that you've published the component to the library
- Check that you've created a new project and added the component
- Ensure that symbol properties are correctly applied

### Pin Organization Problems

- Verify that section and pin group properties are spelled consistently
- Check that pin orientation is set correctly (Left/Right)
- Ensure pin numbers match the datasheet

### Multi-Symbol Issues

- Verify that the Sub-symbol Designator Suffix is applied to the correct terminals
- Check that each sub-symbol has a unique suffix
- Ensure that related pins are grouped in the same sub-symbol