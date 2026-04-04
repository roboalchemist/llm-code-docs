# Source: https://docs.flux.ai/tutorials/tutorials-sublayouts-best-practice.md

# Using Modules

Using a module is no different from using regular parts. They have a symbol with terminals to connect it to the schematic, and pads to connect it to the rest of the layout. This allows you to use an existing PCB layout in new projects.

### Adding a Module to a Project

You'll find publicly available modules in the library like you find other parts. **To differentiate a** **module** **from a part look for the** **module** **icon.**

**Pro tip:** you can enable the module [filter](https://docs.flux.ai/flux/reference/reference-library#filtering) to only get modules in the search result.

![](https://uploads.developerhub.io/prod/86Yw/ou16yhy2dqu083qvnnqz1djnxnbuc3ww0j8mgh398sbhxyuefsgqh2y6azdyga38.png)

Once you've found a module in the library, add it to your project by dragging it into the schematic. You can then connect the available pins on the module to other parts. The module then works like any other component!

![_Drag a_ module _into your schematic and connect it to other components._](https://uploads.developerhub.io/prod/86Yw/t9mfii3wkrx1h5n85rpd25a3o9g3kgyc2rtai16beux9yu7zrhnc40t95lb56x4j.gif)

### Routing a Module

When you open the PCB editor, you'll see that the module contains a fully routed circuit. You can then connect it to the rest of the layout with traces, just as with a part.

![_You don’t have to worry about re-routing the sub-layout when you use a traditional component within a sub-layout. The existing connections are preserved and you can place the other components as usual._](https://uploads.developerhub.io/prod/86Yw/yjhe4whljofzsu59yahejbtkmshlx6ybu86af6rvczssic4w29s52h840axxavnh.gif)