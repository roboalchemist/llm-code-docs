# Source: https://docs.flux.ai/tutorials/advanced-routing.md

# High-speed routing

Learn how to design modern high-speed applications effortlessly with **automatic impedance control** and **differential pair routing.** 



## Overview

With the increasing complexity of PCB, high-speed routing capabilities have become vital. Impedance control and differential pair routing form the backbone of modern PCB design practices, enabling optimal power transfer and minimal signal distortion through impedance coherence.

Though high-speed design might seem challenging, Flux seamlessly handles the complexities behind the scenes. With automatic integration of impedance and differential pair metadata into components, routing becomes a breeze. Initiating a route for one trace in a differential pair triggers automatic routing for its counterpart.

## Automatic Impedance Control

Our library contains a wealth of components pre-configured with optimal impedance and differential pair parameters. This means that you don’t need to worry about any calculations. 

Initiate multi-routing by clicking on the routing touch point of either pad in a differential pair, and both traces will automatically route simultaneously. To enhance routing accuracy, Flux mirrors the shapes of the pairs as they depart from and arrive at pads

Routing an impedance-matched differential pair is pretty straightforward:

1. Drag one or more parts with an impedance-controlled interface (HDMI, USB, etc) from the library.
2. Wire the parts together.
3. Navigate to the PCB editor.
4. Make sure you configure your [stackup](https://docs.flux.ai/tutorials/routing-across-multiple-layers-on-a-pcb#configuring-board-stack-up).
5.     1. We have a few pre-configured stackups from JLCPCB that have been tested in manufacturing.
6. Click on any pad that belongs to a differential pair net.
7. 
    1. Tap the CMD key to route single-ended
    2. On the off-chance that the part hasn’t been configured, [here's how to configure it.](https://docs.flux.ai/flux/tutorials/advanced-routing#automatic-setup)

8. You can adjust the final position of any trace by clicking and dragging on a segment



### Verifying Impedance and Net Length

Both traces will be impedance-matched according to the interface being routed. You can check the parameters that were used to calculate the trace width and spacing by selecting the target net and viewing its properties. A net length property is also available for quick consistency checks. For verifying net length matching, all you need to do is click on the net. 

![](https://uploads.developerhub.io/prod/86Yw/c76121j3kznivw4erdgh45j1pn1flfe05ihsqqv5xm50nqe0dfv4gttby234fude.gif)

This covers the majority of what you'll need for advanced routing in most cases. If you wish to add impedance-control support for your own parts or learn about the inner workings of these features, keep on reading.

## Under the Hood

Here, we discuss the mechanics of impedance control and how to configure your parts.

### Defining Parameters

Pair-matching and impedance requirements are configured by specific properties. Let's explore an [example part](https://www.flux.ai/jharwinbarrozo/tpd12s520dbt?editor=schematic) to understand how it’s configured.

![](https://uploads.developerhub.io/prod/86Yw/ai8jss9kcebxfy72qeuf5la9gnlktykzmoyareb6x3hleqw4rshlqoonsyeropxe.png)

### Part Type Configuration

The first thing you’ll notice is that it has a “Part Type” property set to HDMI. Flux will automatically configure the right properties on each terminal when a part is assigned a "Part Type" property that contains an impedance-controlled interface, like HDMI. This automatic configuration requires some prerequisites discussed in the [Configuring Components section](https://docs.flux.ai/flux/tutorials/advanced-routing#configuring-components). In the next section, we’ll discuss a bit more about how each terminal is configured.

### Pin Configuration

The majority of the configuration for impedance control takes place at the terminal level. Each terminal needs to be configured with the right parameters. These properties can either be configured automatically by setting up the “Part Type” property, or manually.

Let's break down the required properties using an example: examining TMDS_D2+ and TMDS_D2- from an HDMI interface."

![](https://uploads.developerhub.io/prod/86Yw/ximlb1ejz2a5cdjyetku8oiot0bnc4lek74mpoqa6bkjza99d284wrsattuksgzc.png)

In the picture above, you can see that there are a number of properties that need to be configured. There are two main groups:

- **Interface parameters** (Controlled Impedance, Controlled Impedance Tolerance, Pair-Pair Skew Max, PN Skew Max and Pin Delay): these parameters depend on the target interface. HDMI, USB, and PCIe have different requirements.
- **Flux parameters** (Bus Type, Bus Group, Pair Role and Controlled Impedance Pair): these are internal Flux parameters that define how the different pairs and buses work.

We’ll discuss each parameter in detail in the [Manual setup](https://docs.flux.ai/flux/tutorials/advanced-routing#manual-setup) section.

### Layout Rules

Let’s now explore what happens when a properly configured part is used in a design. 

When transitioning to the PCB layout, the presence of the properties above triggers the automatic generation of certain [rules](https://docs.flux.ai/flux/tutorials/tutorial-layout-rules-deep-dive): Keep In, Keep Out, and Trace Width. As a result, differential pair traces are routed with the correct width and spacing, eliminating the need for any manual calculations. This behind-the-scenes intelligence ensures that your designs meet high-speed requirements effortlessly and accurately.

You can quickly check this by adding two of the [example parts](http://flux.ai/jharwinbarrozo/tpd12s520dbt?editor=schematic) in a new project and connecting them together. Then go to the PCB Editor and route a few differential pairs. If you select any of those nets, you’ll see a few Layout Rules like the ones below:

![](https://uploads.developerhub.io/prod/86Yw/3xup3mbbzdwklimrswza8ha7ukcribj05qsmu3xv7krefrqrwpgb9nkxda4bjdzx.png)

> Impedance calculation depends heavily on the [stackup](https://docs.flux.ai/flux/tutorials/routing-across-multiple-layers-on-a-pcb#configuring-board-stack-up) used, meaning these rules will change depending on the selected stackup.

## Configuring Components

Now that you have a general idea of how the pieces fit together, let’s discuss how to add impedance control and differential pair to a part. There are two ways of doing this:

- Automatic setup: this is the recommended process as it only requires part pins to be properly named.
- Manual setup: it’s also possible to manually add parameters directly to the pins.

### Automatic setup

Flux will automatically add the right parameters to every terminal in the part if the “Part Type” property is set to any of the supported interfaces listed below. This property can be set by the part creator before publishing the part to the library, or it can be [added to the part after](https://docs.flux.ai/flux/reference/reference-inspector-properties#high-speed-routing) it has been placed in a project.

Supported interfaces: USB A, USB B, USB C, HDMI, PCIe x1, PCIe x2, PCIe x4, PCIe x8, PCIe x16, Ethernet

Naming Requirements: In order for Flux to automatically match each terminal with the right role in the interface, those terminals need to follow a specific [naming convention](https://docs.flux.ai/flux/reference/impedance-control#automatic-setup).

### Manual setup

If you’re configuring impedance control for an interface that is not currently supported, you’ll need to add the parameters to every pin manually. This can only be done if you have edit access to the part you’re trying to add support to.

[Here's a guide](https://docs.flux.ai/flux/reference/impedance-control#manual--setup) of all the properties that need to be setup.

### Examples

Here you have a few parts that have already been configured to use as a reference:

[TPD12S520DBT](https://www.flux.ai/projects/c9961bf3-f371-4945-8fcb-100d2fe3dc14)

[1747981-1](https://www.flux.ai/projects/00cb976a-a144-4efa-a683-4a3a3d1ab845) 

[TUSB8041IRGCT](https://www.flux.ai/projects/c244a978-76c4-1679-36b7-3115814c5f66)

[USB type A](https://www.flux.ai/projects/2f8a8cb2-9925-dbce-f37e-e344ce7e908c)

[CYPD3177-24LQXQ](https://www.flux.ai/projects/4d0a62fe-e3f6-46b4-b6ff-27e6e0b9e8b1)

[USB Micro B](https://www.flux.ai/projects/9936dea9-c42b-2a06-373f-ad3ef75d1dc9)

[STM32F405RGT6](https://www.flux.ai/projects/a89f3340-7966-ee2e-2560-5fe1a385bd5a) 

[SS-52400-003](https://www.flux.ai/projects/646ad169-14fc-442e-20ce-4014717e7ff9)