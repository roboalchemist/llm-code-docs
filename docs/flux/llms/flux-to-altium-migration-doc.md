# Source: https://docs.flux.ai/Introduction/flux-to-altium-migration-doc.md

# Altium to Flux


Step into the future of PCB design with a modern, browser-based eCAD tool powered by Flux, a generative AI hardware design assistant that answers complex questions and wires up schematics for you.

{% image url="https://uploads.developerhub.io/prod/86Yw/2i2l0lvk4vstwykkluy16ns1wjve5ifwwgkz8lx9md76g2janmk3ep7or3irb0gr.png" mode="responsive" height="1117" width="1728" %}
{% /image %}

## Overview

Switching to Flux allows for a more streamlined and modern approach to PCB design, with AI, collaboration, efficient development, project organization and more. In this Altium to Flux migration tutorial, we'll guide you through the process of switching from Altium Designer to Flux, highlighting the key differences and providing helpful tips for a smooth transition. We’ll do an overview of the differences and discuss helpful tips for making a quick and easy transition so you’ll be creating circuit boards in no time.

{% image url="https://uploads.developerhub.io/prod/86Yw/tkgnsoqvqz4jgzuv39z5crdqyb8xu4njyhml3bf82uhwakj1ktxyeurl04lq0w3g.png" mode="600" height="2382" width="3680" %}
{% /image %}

### Why Make the Jump from Altium Designer into Flux?

Flux is a modern tool with modern workflows —which allows it to be structured in a way that allows for streamlined workflows, easy collaboration, AI integration, and incredibly fast development.

- **Fully-featured free tier**. You can pick up Flux and create high-quality boards without any commitment. Flux's free tier is only limited by the by the number of private projects you can have simultaneously.
- **Browser-based workflow.** Flux works with any desktop device with a browser.
- **Frictionless collaboration**. Multiple users can easily collaborate and sharing projects is a breeze.
- **Design faster with AI.**
- **Auto-save, auto-version control, auto-history**. Never mess with files or saving again.
- **Simple project sharing and viewing.** As simple as sharing a link.
- **Never start from scratch**. Use templates and example projects to get started quickly.
- **Get inspired and build off the community's projects.**
- **Simple part creation process.** For any parts already not in your library.
- **Easily build off other projects by forking them.** Project acessibility and collaboration are built into flux.

{% image url="https://uploads.developerhub.io/prod/86Yw/ghepc79806v373ptwnxr16239vqlfilzjljq771647r2dl9fo3mlepfdk2mqrm2x.png" mode="responsive" height="2464" width="3808" %}
{% /image %}

### Browser-based Integrated Workflow

Flux is revolutionizing schematic and circuitboard design collaboration with its user-friendly browser-based workflow, breaking free from the limitations of operating systems and empowering engineers with modern tools. Experience seamless teamwork, easy sharing, and a streamlined design process that transcends traditional EDA boundaries with Flux.

Specifically, Flux is completely browser-based design tool, from the schematic design to PCB layout to export. This means you’ll constantly be using the most reliable and up-to-date version of Flux no matter where you are. This frees users from a lot of the hassles of traditional EDA software, such as file management systems, sharing files through email, or restriction to specific operating systems.

### Streamlined Collaboration

Flux’s browser-based structure allows for easy sharing and collaboration simply by sending links.

Projects are made private by default, meaning only you will be able to open and see those projects. If you want to give other users access to your projects or make them fully public, you’ll need to use the [share menu](https://docs.flux.ai/reference/reference-sharing-and-permissions#share-menu).

Projects are sharable by simply copying and pasting the URL. Anyone with the right access level will be able to work on and collaborate on the same design. This is especially convenient for open-source projects, where engineers might be working remotely on the same project.

{% image url="https://uploads.developerhub.io/prod/86Yw/458gmjkafsdfo88yxhsstgvsqnvo033zphijm4e4lrrq0istkg9b3qgim73f980e.png" mode="600" height="2024" width="3536" %}
{% /image %}

### Fast development with AI

Flux features a [powerful AI assistant](https://docs.flux.ai/tutorials/ai-for-hardware-design) that support you in your project development in a variety of ways.

With Flux, you gain a powerful AI design assistant that resides within your Flux projects, providing invaluable feedback, saving costs, and preventing errors. By understanding the context of your project, including components, connections, and datasheets, Flux offers tailored assistance in part selection, schematic design feedback, and comprehensive design analysis.

{% image url="https://uploads.developerhub.io/prod/86Yw/ntt5r1b57810daesqu6p295b3b0td24padpanzi7nev2gtjr7pnq8o95skpgj0q3.png" mode="600" height="2040" width="3552" %}
{% /image %}

### Version control

Flux’s simple to use [version control](https://docs.flux.ai/tutorials/version-control---deep-dive#overview) makes tracking changes in a collaborative setting simple, and allows for easy rollback if something goes wrong. Flux’s version control is similar to other web tools (such as Google Docs), where every change you make is automatically saved and assigned a new version. This guarantees that no single change is ever lost. To revert your document to a previous state, go to the “Change History” menu.

{% image url="https://uploads.developerhub.io/prod/86Yw/sn5rlfzpfhgb2q3wf1e9aqjvohl2glyhd5vubq0dqjegxqnqjipj9njl9qztiwbu.png" mode="600" height="2028" width="3540" %}
{% /image %}

### Project Organization

Being browser-based, every object in flux has an easily sharable URL. Getting rid of the concept of traditional files allows for engineers to always have every part of a project easily accessible and never worry about a missing file when sharing a project.

### Modules

[Modules](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts) allow you to quickly reuse circuit block modules (like power converters, oscillators, and anything else you come up with) that you’ve already used in other projects. They function as a complete design blocks with included parts, traces, vias, etc., that can be placed into existing projects to reuse previous designs with minimal effort.

Similar to parts, there will be one terminal (pin) in the submodule's symbol for each terminal in the submodule's schematic.

{% image url="https://uploads.developerhub.io/prod/86Yw/lhtk4d8v0ncill0vldkfgbftccoldmt8uyejyr47o64zqps9biaspfuuenyn6w07.png" mode="600" height="1850" width="2912" %}
{% /image %}

### Altium’s Multiple Libraries are Condensed into Flux’s Unified Library

Both Flux and Altium have powerful libraries, but each works a little differently.

Altium designer has a wide variety of different library options. From Altium 365, git-based libraries, database-based libraries, and more. Configuring libraries, and ensuring each part used is from the correct one can be quite tedious and at times frustrating.

Flux, on the other hand, has a single community-driven unified library with every part you have access to. This makes finding any part you want quick and simple. A single library includes all the parts you or your team has created, whether [they’re private or public](https://docs.flux.ai/reference/reference-sharing-and-permissions#access-levels), in addition to parts made by the community. Rather than needing to sort through and configure each library, users can easily leverage the large amount of community made parts through the search feature.

{% image url="https://uploads.developerhub.io/prod/86Yw/jay783dsbilb1urwkwny92igt8bpfgcov1ipkmjg9a1gnndjwpvm7kppn17lhwg1.png" mode="responsive" height="2040" width="3552" %}
{% /image %}

> Can’t find the part you’re looking for? You can easily add parts to the library with specific permissions through [this method](https://docs.flux.ai/flux/tutorials/tutorial-add-part-library).


### Part Creation

Altium allows for custom part creation, both in the schematic and footprints.  Flux also has a couple of methods to create or import previously-made parts.

In Flux, to create a new part, you must first [create a new project](https://docs.flux.ai/reference/reference-blank-project). Then, you can add as many terminals to the schematic as you need. Each terminal will generate a pad in the PCB editor that you can modify to create the desired footprint. Publishing this project then pushes it to the parts library. Through this method, the concept of “traditional parts” no longer exists. Rather, parts are created the same way projects are.

📖 Naming convention: pins (traditional) → terminals (Flux). Both have a similar function, but pins are called terminals in Flux.

In Flux, there is no “assigning” a footprint to a symbol or part. Every part, project, or module has a schematic and associated PCB layout, known as a footprint.

{% image url="https://uploads.developerhub.io/prod/86Yw/por7lhatn0swaijgla3tjizrxwiy8xpivyidogtsrlrvstby8ceqrwnct8ienpxy.png" mode="responsive" height="2020" width="3504" %}
{% /image %}

### Generic Parts

Just as Altium allows users to select multiple footprints for a given part, Flux supports the same functionality. Because parts (and modules) are exposed to the user, the package selection can be automated in code.

As there are specific footprint(s) that come with each part, you don’t need to go hunt for the footprint in different libraries. All footprints are easily accessible, and you can select the one that fits on the fly.

{% image url="https://uploads.developerhub.io/prod/86Yw/kgzetx2wqtooxj34vqxwurtnafl3vh12pbhgm2d65l8y75p69za3koufxan1ewy0.gif" mode="600" height="336" width="640" %}
{% /image %}

### Project Cloning and Forking

Flux allows for easy project forking, which preserves the history of changes and allows for merging back with the original project. Furthermore, you can also clone a project to create a clean copy without any history preservation.

## From Altium Schematic Editor to Flux Schematic

### Sheets

Altium uses a series of different sheets in a hierarchal format for project file management. Flux, instead allows for infinite nesting through [modules feature](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts). In other words, when dragging in a part of submodule onto your schematic, you’ll be able to double click it to enter and see a more detailed view of its inner functioning.

### Symbols

In both PCB design softwares, when dragging a specific part or module into the schematic canvas, the symbol is what represents it on this level in the hierarchy.

Altium  designer uses a built-in editor for creating custom symbols that appear in the schematic. Flux offers [compatibility support for custom symbols](https://docs.flux.ai/tutorials/tutorial-import-part#2--importing-a-symbol) by importing svgs. You’re able to go a step deeper in the hierarchy and double click any part to see it’s internal components (or lack there-of).

### Wiring

In Altium you may be used to ctrl+W to place down wires in the schematic editor. In Flux, it’s as simple as clicking on a pin and wiring away.

### Alignment

In Altium, objects will automatically clip to the grid during the placement stage. In Flux, trying aligning your symbols magnetically first, allowing for cleaner wires and schematic down the line.

### Flux Terminals & Net Portals act as Altium Ports & Net Labels

In Altium designer, the concept of ports allows for connecting nodes through different sheets. Net labels act similarly but are localized. In Flux, terminals mimic ports and net portals mimic labels.

### Bill of Materials (BoM), Pricing, and Availability

Altium’s BoM must be generated each time to see the most recent availability. Flux has a LiveBoM feature that supports live updates of part sourcing from the three largest distributors based on manufacturer part number (MPN).

Creating a .CSV export is easy, and contains all the necessary components with related attributes.

{% image url="https://uploads.developerhub.io/prod/86Yw/ph0k3sghlryz5vyf9rsth424yh05z3h00tw3m3ipe59puu4oo6j3locoorxytfsq.png" mode="responsive" height="827" width="280" %}
{% /image %}

### Notes & Comments

Flux also features notes as user created objects directly on the schematic. Comments are also easily created and can be placed anywhere. Through this method, different users can easily work together on a Flux PCB board, allowing for streamlined collaboration.

## From Altium PCB Editor to Flux’s PCB Editor

### Altium Engineering Change Orders (ECO) are Automatically Handled In Flux.

Altium features a Engineering Change Orders (ECO) panel that must be configured when moving from the schematic to the PCB.

Flux will automatically sync any changes made in the schematic, code, or PCB canvas to the cloud in an automatic bi-directional. Although it doesn’t use change buffer, Flux has Git-based version control that allows for restoring older versions if an undesired change is made.

{% image url="https://uploads.developerhub.io/prod/86Yw/pylt4ab6x40esjdzu958hrtvi62t12a7uzm1mxzkifm8xxy4ekvss4x21fdw2dtt.png" mode="responsive" height="627" width="353" %}
{% /image %}

### Flux’s Layout and Selector-Based Rules Mimic Altium’s Rules, Constraints Panel and Properties Panel

When creating a new PCB with Altium, one of the first panels users configure is the Rules and Constrains panels. This allows for configuring the clearance distances, shapes, and other properties of traces, silkscreens, components, and more. Then, any individual objects on the PCB canvas can have their properties edited through the properties panel. Altium’s workflow involves defining the board rules, part placement + routing (with editing through the properties panel), and then a design rule check. If any rules are violated, an error will be thrown in the final stage.

Flux, on the other hand has a real-time rules-based workflow. As objects’ properties are dictated by rules, rather than waiting until you’ve placed down all your components and traces, Flux provides constant feedback, even automatically modifying your components’ properties to fit your defined ruled.

For specific layout rules, Flux utilizes the Inspector panel on the right for rule configuration. The layout rules menu will pop-up on the right when an element is selected. Through this menu, it’s possible to add rules to modify, configure, and edit everything from parts, traces, to your board.

{% image url="https://uploads.developerhub.io/prod/86Yw/8ws1v4qupmup98dxfjn2jvx65olpsg16nhs0aiv9ydceim2dkgd34ureja5cozya.png" caption="Inspector panel on the right side with object-specific rules" mode="responsive" height="848" width="1131" %}
{% /image %}

Just about any characteristic of any PCB element on the board can be modified using rules. Including, position, rotation, size, and more. See the [layout rules page](https://docs.flux.ai/reference/pcb-rules) for more information. In Flux, your workflow will consist of going back and forth between these layout rules and components, as the rules will update the circuit as you design, unlike in Altium.

Flux also features selector-based rules. With [selector-based rules](https://docs.flux.ai/reference/pcb-layout-rule-selectors), you can generate rules that modify many elements at once - for example, changing the width of several traces in a single net

For example, consider the case where you are an engineer looking at a previously designed PCB, examining an individual trace.

- In Altium, if you see a specific trace with an arbitrarily-different trace width, you may not have any idea why it’s set to that value, or what factors may be contributing to its behavior.
- In Flux, it’s much clearer: either a specific object rule or a selector-based rule actively has changed its width. You can then click in to see what rule is affecting this individual trace.

### Trace Routing and Impedance Matching

Altium’s PCB editor allows for trace creation through Ctrl+W. In Flux, simply click on the nodes of a pad [object and wire away](https://docs.flux.ai/reference/reference-net-width)!

High-speed routing is as easy as traditional routing, you can learn everything about high-speed routing capabilities, including impedance control and differential pairs [in this tutorial](https://docs.flux.ai/tutorials/advanced-routing).

### Copy Pasting

Flux also allows for easy copy-pasting of any object in the canvas. This way you can create an object, apply your desired rules to it, and simply copy-paste it as needed.

### Polygon Pours

Flux doesn't currently support arbitrary-shaped polygons (ground or otherwise). Flux will create a full-board ground fill as soon as a ground symbol is placed into the schematic. These copper fills can also be re-assigned to other nets to create power planes. To learn more about automatic ground-fills, copper fills in general, how to disable it or how to add via stitching, refer to the [copper fills documentation.](https://docs.flux.ai/tutorials/tutorial-ground-fills-deep-dive) Flux also allows to shelf the GND fill by toggling the visibility button.

Rather than having arbitrarily shaped polygons, we believe Flux’s rule-based workflow should dictate the shape of copper fills. More specifically, rather than using an arbitrary shape for a copper fill, Flux will automatically generate a shape as dictated by keep out rules. Having the copper fills be generated explicitly through rules, allows other engineers to examine the board and more easily understand why the copper fill is the shape it is, rather than an arbitrary pre-defined shape. That being said, additional functionality for polygon pours is in the pipeline!

### Stackup Manager

Altium has a stack-up manager that allows for configuration of the board stack-up, including the number of layers, material, behavior and more.

Flux, on the other hand, utilizes constraints that are defined in the layout object. New projects are configured with a 4-layer stack-up by default. To further configure a different stack-up:

- Go to the "layout" object in the "Objects" tab on the left panel of the PCB editor.
- Select the "layout" object. In the right panel, you will be able to add an "Object Specific rule" called "Stackup". Select the appropriate stack-up from the list.

Flux also features multiple premade stackups for commonly used manufacturers, [such as AISLER](https://www.flux.ai/aisler), JLCPCB, and PCBWay.

### DRC and DFM Constraints

Altium uses a system of DRC and DFM constraints.

In Flux, these tools are set using the layout tools. Instead of searching through manufacturers’ websites for constrains or dealing with multiple rule import wizard, simply [clone a template with all the DRC already preset](https://www.flux.ai/jharwinbarrozo/2-layer-jlcpcb-constraints?editor=pcb_2d).

Furthermore, new DRC rules are continuously being added into Flux. If there’s one you’re missing, by all means [submit a ticket](https://docs.flux.ai/Introduction/getting-support).

### Board Outline

In Flux, the board outline is a separate object in the [object tree](https://docs.flux.ai/reference/reference-object-tree-pcb). Just like any other object, select the board outline to edit its characteristics via rules. Find the “Layout” object in the object tree. See this tutorial for [custom shapes](https://docs.flux.ai/tutorials/tutorial-board-outline-shape#advanced-custom-shapes).

### Navigation & Shortcuts

Flux mostly uses similar navigation and shortcuts to Altium. Use the mouse wheel to zoom and middle-click to pan. Flux also has trackpad support natively as well, making it as intuitive as navigating a website.

The full list of Flux shortcuts can be accessed in the top left corner under “Keyboard Shortcuts”. Some useful ones include”

- Zoom to Fit All or Selection 0
- Rotate Right ]
- Rotate Left [
- Flip wire elbow direction /
- Finish drawing a wire Double click the canvas or Click a terminal or Esc

### Gerber Export

Flux allows for Gerber exports through a single button click.

{% image url="https://uploads.developerhub.io/prod/86Yw/38razy5vzxpxi5tkock4hmy99yqk7r952tfj8omrdmsrfjm47m73gtetrregx4ha.png" mode="responsive" height="304" width="553" %}
{% /image %}

### Flux Code and Simulator

Altium contains a proprietary scripting language with documentation that isn’t especially widely available. Flux uses JavaScript and has a public API with a [built-in simulator](https://docs.flux.ai/faq/faq-s-about-the-simulator). You’re able to run simulations on your circuit to ensure functionality as intended before manufacturing.

## Wrap Up

That covers the need-to-know basics for transitioning from Altium designer to Flux. As a whole, the transition should be rather straightforward with Flux’s intuitive user interface. Coupled with an expansive community library, various collaboration methods, and simulation capabilities, the switch should be fast and having you designing PCBs in no time.

Getting Help

Before wrapping up, we would like to share some additional resources in case you need help:

- [Slack community](https://www.flux.ai/p/slack-community): Ask questions directly to the Flux team and meet other engineers, designers, and hardware enthusiasts using Flux.
- [Found a bug?](https://fluxai.canny.io/) If you find any unexpected behavior while using Flux, please report it in our issue-tracking tool.
- [YouTube](https://www.youtube.com/channel/UC5CsglCHQBd4-WFrZmqzVyw): Explore our library of video tutorials, crash courses, and recorded events. There are also some independent [content creators](https://www.youtube.com/@overshootchannel) with amazing videos on how to use Flux.
- [Live support](https://www.flux.ai/p): To contact us, go to our home page, scroll down to the bottom, and click on "Contact us".
