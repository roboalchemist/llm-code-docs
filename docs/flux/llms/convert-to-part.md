# Source: https://docs.flux.ai/reference/convert-to-part.md

# Convert to component

Using Flux’s “Convert to Component” feature, you can quickly create a [module](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts) from a group of components.

![](https://uploads.developerhub.io/prod/86Yw/8y0z8x4yvugwm3j3z2j60vtt28er3cg48ebowiu4rlunh9m2snedopi53jwanb15.png)

## Overview

Modules are a great way to reuse portions of a circuit that stay consistent across multiple projects. If you find a group of components in one of your projects that could be reused in another design, you can use the "Convert to Component" function to quickly make it a module for future reuse.

## Convert to Component

To convert a group of components into a single component:

- Select all the components you want to convert.
- Right-click and select "Convert to Component"

### Adding Terminals

As mentioned, using the "Convert to Component" option turns a group of components into a [module](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts). As with any module, terminals are required to use it in a project.

**If the group of components you've selected doesn't contain any terminals, the resulting** module **won't have any connections.**

![](https://uploads.developerhub.io/prod/86Yw/zqqb5go51u4ox74q3mf2u3d20ht96mtusgc2zgubry48ssjm6qiw3bkfq3mc7h53.png)

There are two ways to add terminals:

- Add terminals to the group of components before using the "Convert to Component" option
- After using the "Convert to Component" option, right click on the generated module and select "Open".
    - Once inside the module drag the terminals to the desired position and then [publish the changes.](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library)