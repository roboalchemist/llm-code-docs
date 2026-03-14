# Source: https://docs.flux.ai/tutorials/tutorial-generic-part.md

# Using Generic Components in Flux

Generic components allow you to start designing now and make difficult decisions about parameters later.



## Overview

Generic components are used in an electrical design like a placeholder, without specific properties assigned upfront, like value, package/footprint, or manufacturer part number (MPN). 

In Flux, generics are intelligent and flexible: as you do add properties, the components update automatically. This means you can start designing quickly and push out difficult decisions until you're ready. It also means you're not locked into a decision early on.

For example, you can start using a generic capacitor without deciding which package you'll need, then later, you can choose a package and the footprint will update automatically.

## Adding a Generic Component

Generic components are available in the library and can be brought into schematics just like any other component. Flux currently has a [generic capacitor](https://www.flux.ai/jharwinbarrozo/generic-capacitor), a [generic resistor](https://www.flux.ai/jharwinbarrozo/generic-resistor), and a [generic inductor](https://www.flux.ai/jharwinbarrozo/generic-inductor).

To add a generic component to your design:

1. Open a project and locate the library search bar in the top left.
2. Type "generic" and the type of part you're looking for. For example, "generic capacitor" or "generic inductor".
3. The top result should be the one you're looking for.
4. Drag and place the generic component on your schematic as you would any other component.

![](https://uploads.developerhub.io/prod/86Yw/5mv10lh31gbzm64ytb4ri3tndk4yb236a654ccjm8a1il84cudthtc62kkfv96lw.gif)

**Pro tip:** You can quickly verify if a part is a generic by changing the "Package" property and see that the footprint gets automatically updated.

## Modifying Generic Component Properties

As with any other component in Flux, you can modify the properties of a generic component. However, there are 3 properties that have special features:

- **Package:** Choosing a package will automatically update the footprint on the PCB for that instance of the component. 
- **Resistance, Capacitance, or Inductance**: Choosing a value for the component, aka the Resistance, Capacitance, or Inductance, will impact calculations used for the simulator.
- **Manufacturer Part Number:** Choosing an MPN will cause up-to-date pricing and availability to show in the component's inspector. It'll also impact the total project price shown in project's inspector and the navigation bar at the top of the project.

### Changing the Footprint

With generic components, you can change footprints on the fly without having to replace your part for one with the right footprint. To change the footprint of a generic:

1. Click on the component you want to modify to select it.
    1. You can select it on the Schematic or PCB editors, but you'll only see the footprint change on the PCB editor.

2. Locate the Properties panel in the component's inspector on the right side.
3. Find the property called Package or Case Code.
4. Select the package you want from the drop-down menu.
    1. If you don't see the package you're looking for, you can create your own generic by following [this tutorial](https://docs.flux.ai/flux/tutorials/creating-a-generic-part).

![](https://uploads.developerhub.io/prod/86Yw/jyna2uaelbc534214mhf131axfgrluv4ma38mdv07g1wanvr0tor8m28ow79axnw.gif)

### Changing the Value

Modifying a generic component's value causes Flux's simulator to update its calculations considering the new value. To modify the value:

1. Click on the component you want to modify to select it.
2. Locate the Properties panel in the component's inspector on the right side.
3. Depending on the type of generic added, you'll see a property called Resistance, Capacitance or Inductance.
4. Type in the value you want.
    1. Flux accepts standard units in these fields. For example, you can type "12K" (as in kilo-Ohms), "12u" (as in micro-Farads) or "12n" (as in nano-Henry).

![](https://uploads.developerhub.io/prod/86Yw/mmezb1q2xn2iivwgkkrehojdg5vn1ydvb9d9yikibvplg3ghopv93p8x2t7f7gk2.gif)

### Changing the Manufacturer Part Number

The last step in fully defining a generic component is adding a manufacturer part number. To change the manufacturer part number:

1. Click on the component you want to modify to select it.
2. Locate the Properties panel in the component's inspector on the right side.
3. Find and edit the Manufacturer Part Number property.
4. Optionally, modify the Manufacturer Name property.
5. Right below the Properties panel you'll see the Pricing & Availability panel, which contains up-to-date info for the MPN you just added.

![](https://uploads.developerhub.io/prod/86Yw/3y07283101ii151z2qonsl0731nqg4eps8wgvr4ct0tdgfkyjiyp37mpid9232ve.gif)

##