# Source: https://docs.flux.ai/tutorials/tutorial-utilizing-sublayouts.md

# Creating Modules

Create your own modules for circuit blocks to easily reuse in any project. 



## Overview

The process of creating a module is similar to the one used to create a regular PCB layout but with some additional differences. In this tutorial, we'll show you how to create a module and best practices to get the most out of your module.

## How To Create a Module

The main difference between a standard PCB layout and a module is the presence of terminals. **While terminals are optional for standard designs, they are required for a** **module** **to work.** This is because the terminals are used to connect the module to other components once the module is placed in a project. 

![](https://uploads.developerhub.io/prod/86Yw/0pyd86twc0w5529vdqko5f4dk9qkf7xt09k4counh9pad8p1ryo60l47yqr6uv8w.png)

The process to create a module is as follows:

1. Create the circuit you want to make a module out of
2. Add terminals to establish the connections
3. Connect the terminals' pads in the PCB editor
4. Add a designator prefix
5. Publish the module

### 1- Create a circuit

Create the circuit you want to convert into a module. Make sure you follow some of these [Module Design Best Practices](https://docs.flux.ai/flux/tutorials/tutorial-sublayouts-bestpractice) to get the most out of your design.

### 2- Add terminals

Simply drag the terminals from the library into the schematic editor. You can think of terminals as the inputs and outputs of your module. This means they should be connected to the nets or parts where you expect to connect other components when the module is used.

[In this example](https://www.flux.ai/nico/sublayout-docs), we created a module that converts any input voltage to 3.3V. As you see, the terminals are connected to the input and output of the regulator and to ground.

![](https://uploads.developerhub.io/prod/86Yw/f472brl9nl0rww4fbkow5isxde9n9pxcb6njep45v92udopdqwci3iukw47r4l1h.gif)

### 3- Connect the pads in the PCB layout

Once everything is placed and connected in the schematics, open the PCB Editor to begin placing and routing components. Once you open the PCB editor, you'll notice that each terminal has a corresponding pad. 

![](https://uploads.developerhub.io/prod/86Yw/5hmm3qecwjly3zp0nm2ij3k6ikqpr1d95z3mpl8k4099ycu4jduspkx0e3w95vut.png)

You will route your connections to these points when the module is used in another project. Points P1, P2, and P3 could be placed on pads, through-holes, or vias in the module. For example, we could place P2 directly on the left pad of R2. Once placed, you can add a Size rule to reduce the size of P2 so that it is not excessively large, as shown in the GIF below.

![](https://uploads.developerhub.io/prod/86Yw/27d49abioc7cuybz21fwkb1jdgfs8bcrnp2r2c7y0uhhu0fwzu7gfbfoznv9nqsk.gif)

For P1 in this example, it would be a good idea to place two vias connecting C2. This way, it will be easy to route a connection to P1 once the module is used in another project.

![](https://uploads.developerhub.io/prod/86Yw/6xpzqjcmldqnlop6rk1b954wdfiqsp67ksxkcwyxnumxbjumeiscigvuyifni3r1.gif)

Once P3 is placed and resized using the Size rule, the module is complete and ready to be published.The completed example is below.

![](https://uploads.developerhub.io/prod/86Yw/knkvc34ss95b89zb033g90p7dawjgws95q8hfyou1cpi1hj6nmy8te9xdrnb6gl3.png)

### 4- Add  a designator prefix

It is good practice to add the word “module” to the Designator Prefix Fields, located in the project properties area (right side of the screen). This will make it clear that your project is intended to be a module and make your schematics easy to read. To add a designator prefix:

- Make sure no object is selected by clicking on an empty portion of the canvas
- Find the "Properties" menu on the right side
- Edit the "Designator Prefix" property and add the word "module"
    - If there is no such property, you can add one by clicking the "Edit" button below.

![](https://uploads.developerhub.io/prod/86Yw/an46jqzr0md2rqc8e9fm29ql4zi3luow4ir2h7j2oozmfa5222bh8gu2zgo2hefu.png)

### 5- Publish the Module

The final step is to [publish](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library) the module to the library. Once the module is published, it can be searched and added to a project. When you drag the module into the schematic editor in a new project, you will see that it will include the module's designator prefix.