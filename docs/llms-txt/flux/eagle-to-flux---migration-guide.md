# Source: https://docs.flux.ai/Introduction/eagle-to-flux---migration-guide.md

# Eagle to Flux



As Autodesk forces Eagle CAD users to transition towards Fusion360, this presents a valuable opportunity to explore other EDA tools. Flux offers built-in support for modern hardware design methodologies: reusability, collaboration, and AI-assisted design. All in your browser.





## Overview

In this guide, we will navigate the migration process from Eagle to Flux, explaining the key concepts and workflows for a smooth transition.

We'll start by addressing unique Flux functionalities. Then dive into Flux’s schematic and PCB editors, discussing design and library management, parts and footprints, high-speed routing, and PCB manufacturing.

This is the list of topics we'll be covering, with links to the specific sections if you want to learn more.

{% image url="https://uploads.developerhub.io/prod/86Yw/69p7rl1okt4i0ty5evjcezmruqoj4nq2u0wmdux1koegdpmeesy8fig686cq3av8.png" caption="" mode="600" height="1117" width="1728" %}
{% /image %}


### Why Flux?

Before we get started, this is why you should be considering Flux as Eagle gets sunsetted:

- **Fully-featured free tier**. There’s no board size or layer count limit. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#creating-an-account)
- **Frictionless collaboration**. Anyone with access to a browser can use Flux . [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#sharing-and-permissions)
- **Design faster with AI.** [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#ai-assisted-hardware-design)
- **Auto-save, auto-version control, auto-history**. Never mess with files or saving again. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#files-and-version-control)
- **Never start from scratch**. Use templates and example projects to get started quickly. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#starting-projects)

### Schematic Editor

Learn how schematic design works in Flux. How parts and libraries work, and how to add metadata to your parts.

- **SCH files and Flux's schematic editor**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#schematic-editor)
- **There isn’t a standalone symbol or footprint editor in Flux.** Parts, modules, and projects are all edited in the same way through the schematic diagram and PCB layout. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#components)
- **Simplified library management in Flux**. No more keeping track of library files. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#library-management)
- **Add manufacturer and distributor metadata to your parts.** [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#parts-fields-and-properties)
- **Live pricing and availability for your parts**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#pricing-and-availability)

### PCB Editor

Learn how to do PCB layout in Flux. Get familiar with layout rules, high-speed design and copper fills.

- **BRD files and Flux's PCB editor**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#pcb-editor)
- **Schematic and PCB data are automatically synchronized**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#netlist-and-eco)
- **PCBs object properties are called rules in Flux.** [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#eagle-properties-vs-flux-rules)
- **High-speed layout is as easy as routing any other trace**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#routing)
- **Quickly create copper fills connected to ground, power or any other net**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#copper-fills)
- **DRC checks ensure your designs are safe to be manufactured**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#drc-checks)
- **Export your designs for manufacturing**. [Learn more.](https://docs.flux.ai/flux/Introduction/eagle-to-flux---migration-guide#gerber-files-and-fabrication-export)

## Getting Started

### Creating an Account

We believe you should be able to fully test a tool before committing. Flux's free plan is fully-featured, only limited by the number of private projects you can have simultaneously.

{% image url="https://uploads.developerhub.io/prod/86Yw/ghepc79806v373ptwnxr16239vqlfilzjljq771647r2dl9fo3mlepfdk2mqrm2x.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


The first screen after logging in to Flux is your profile page. This is where you’ll find every project you have contributed to. It's similar to the Control Panel in Eagle, with the difference that your Flux profile is sharable. If you share your profile’s URL, other people can see your public projects, which means your profile can act as a portfolio.

### Sharing and Permissions

Projects are made private by default, meaning only you will be able to open and see those projects. If you want to give other users access to your projects or make them fully public, you’ll need to use the [share menu](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions).

Since Flux is browser-based, anyone with access to a project will be able to use every feature. There's no need to download a tool or be limited to viewing only.

{% image url="https://uploads.developerhub.io/prod/86Yw/lh1npn7dj17ahg7855eo9xyohh2exvahxko2493zpk2h5ukxfgvirpstniw4h76w.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


Projects are also sharable the same way your profile is, by simply copying and pasting the URL. Anyone with the right access level will be able to work on and collaborate on the same design. This is especially convenient for open-source projects, where engineers might be working remotely on the same project.

### AI-Assisted Hardware Design

Flux Editor has a built-in hardware design AI assistant. It's a Flux-trained large language model (LLM) that lives inside your project and can provide direct feedback to help you design faster, safer, and more complex PCBs. Learn more about Flux in [this tutorial](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design).

{% image url="https://uploads.developerhub.io/prod/86Yw/rn0v5puy0uiz2bnaoka7w39io73yhk17uf0rhh7grqry6k7cp0nq1t5k9pbp8apv.png" caption="" mode="responsive" height="1530" width="2410" %}
{% /image %}


### Files and Version Control

Just like in Fusion360, your project will be saved in our infrastructure. There's one key difference though, Flux automatically saves and version-controls your work. This guarantees that no single change is ever lost. To revert your document to a previous state, go to the “Change History” menu.

{% image url="https://uploads.developerhub.io/prod/86Yw/9kvo3a866cahf9b3d63c3a7u5h53w3aurqn8eqvztdvlelbfoynlogbeeha0pn40.png" caption="" mode="responsive" height="1281" width="1953" %}
{% /image %}


### Starting Projects

Click the "New project" button in the top right to start a new project. However, Flux hosts a ton of great templates and example projects you can use to get started faster. Remember that there are no files in Flux, so each project is accessed via it's URL instead of the .epf file

We encourage you to browse the publicly available projects in one of two ways:

- [Featured projects page](https://www.flux.ai/p/projects)
- Using the search bar in the top left.
-     - #project or #template plus a few keywords to filter for specific types of project

## The Schematic Editor

The schematic editor should feel familiar. Remember that there are no files in Flux, so no need to worry about synchronizing the .sch and .brd files. There are three main sections:

{% image url="https://uploads.developerhub.io/prod/86Yw/f2jmj0n5qnywj2ja9o1pmg8mu90j0olkqvnpqqwvh19lpd2dn6xvlij7g27ap05g.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


- [The library](https://docs.flux.ai/flux/reference/reference-library) on the left sidebar. This is where you'll find all the available parts and submodules.
- The canvas in the middle. This is where you'll create schematics.
- The properties menu on the right side. This one contains a few sub-menus:
-
    - [Properties](https://docs.flux.ai/flux/reference/reference-inspector-properties): equivalent to Eagle's part attributes. Contains metadata info for parts, including MPN, manufacturer info, etc.
    - Availability and pricing: Flux automatically displays pricing and availability information for parts with an MPN property.
    - [Assets](https://docs.flux.ai/flux/reference/reference-inspector-assets): here's where you add external assets (symbols, thumbnails, etc.) to your project or parts.

### Parts, Symbols, and Footprints

This section is key to understanding how Flux works and how to best use it. Flux is incredibly powerful but may take some getting used to.

{% image url="https://uploads.developerhub.io/prod/86Yw/alrm3hxxpywfs58hvfnuzyucmpr8lq49vs3cor1077vnmppwotyiyukohtz86bp8.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


### Components

There is a relative similarity between the concept of components in Flux and device in Eagle. In Flux, a component contains a footprint (package), a symbol, and a schematic. Components are what you will find in the library and drag into your schematic.

The main difference between a component in Flux and a device in Eagle is that to create a new component you first create a new project, add symbols and footprints, and then publish it to the library. Only when you publish it to the library the project becomes a component, and you can use it in other designs.

### Schematic and Symbol

The concept of schematic will be new for those of you coming from Eagle. Let’s open [this resistor as an example](https://www.flux.ai/jharwinbarrozo/r-0805-2012-metric). The first thing you’ll notice is that the schematic only consists of two terminals. So why isn’t there a symbol?

Components have two “views” in Flux:

- The internal view is what you see when you open a part. It’s as if you were looking at what it has inside. Resistors, ICs, connectors, and almost every discrete part will only contain terminals. This view will be important when we discuss submodules.

{% image url="https://uploads.developerhub.io/prod/86Yw/vzoauvb6vyl4abasery2d0c6r2arhf82ysuavvjkaw3qfa6buwo2olrnmafrkox4.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


- The external view is what you see when you place the part in a project. This is what we call the symbol. This view is what you’re used to when working with symbols in Eagle.

{% image url="https://uploads.developerhub.io/prod/86Yw/pvsglrn8pqv59zbrckanxhrkkag8ix9yskkmc5q5pts329q6esg1ldbs25ug8uhv.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


[This is](https://docs.flux.ai/flux/tutorials/tutorial-add-part-library) an excellent tutorial to learn more about parts, including creating custom symbols.

### Footprints

For the most part, footprints work like packages do in Eagle. Each terminal you place on the schematic generates a pad on the PCB editor. For example, if you'd like to create a new part with ten pins, insert ten terminals from the library in the schematic.

{% image url="https://uploads.developerhub.io/prod/86Yw/z9bm95grg7rf9yguyadobwa0x5i6o2vzx2d6b6hlisojs83zx5x6wf503i0j2ar8.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


If you’re wondering how we handle parts with multiple footprints, take a look at the [generic parts tutorial](https://docs.flux.ai/flux/tutorials/tutorial-generic-part).

### Submodules

Submodules are an extension of the concept of parts. They behave like parts in almost every way, but the key difference is that they contain multiple parts, traces, etc. They're essentially a project with their own layout that has been "converted" to a part to be reused in other projects.

Similar to parts, there will be one terminal (pin) in the submodule's symbol for each terminal in the submodule's schematic.

{% image url="https://uploads.developerhub.io/prod/86Yw/ojdnz6mucq8wlou3to93x42qmmh08vb4ucdz80ds7sv5upv60rzlu6cy9x4sv0v4.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


[Here's an example](https://www.flux.ai/jharwinbarrozo/usb-c-receptacle-with-built-in-esd-protection-and-3v3-ldo-smart-module) submodule to play around with. To create your own submodule out of a project, follow the same process as making a part out of a project:

- Go to the project you wish to convert to a submodule and click on the Flux menu in the top left corner.
- Click on "Publish to library".

### Library Management

Coming from Eagle, you’re probably used to managing the different kinds of libraries, local, cloud, global, project-specific, etc. In Flux, there’s only one library to care about, the Flux Library. Every part and submodule you have access to will be present in the library.

What's even better is that you might need to manage any library at all. Flux library is full of community-made parts that you can use right away in your design. You can also add your own parts if you need to.

{% image url="https://uploads.developerhub.io/prod/86Yw/uh26m773p8aoab7na22la1c0bo27znwc2da2upyi6ylh5c77ycd1x7ccby5e23ak.png" caption="" mode="responsive" height="1281" width="1953" %}
{% /image %}


Having access to a part or submodule can mean one of three things:

- The part is public, and anyone can access it. There are thousands of public parts in the library to choose from.
- Someone gave you access to that part. (Remember the share dialog?).
- It’s a part that you created or cloned yourself. [This is how](https://docs.flux.ai/flux/tutorials/tutorial-add-part-library) you can add parts to the library.

### Parts' Fields and Properties

In Flux, properties are equivalent to Eagle's part attributes. They allow you to add metadata (MPN, manufacturer, distributor, etc.) to your parts.

The benefit of being an online tool is that Flux can provide real-time pricing and availability for all your parts. Simply add an MPN property with a valid manufacturer part number from one of the leading distributors (DigiKey, Mouser, etc.)

{% image url="https://uploads.developerhub.io/prod/86Yw/a8sgflyllvqzz1al5a4y12jtrlcpbyibyjkhuq55sglx2m386fscy1zlue8f9u2m.png" caption="" mode="responsive" height="1281" width="1951" %}
{% /image %}


### Pricing and Availability

For parts that contain a Manufacturer Part Number property, Flux will automatically add live pricing and availability information from the main distributors.

{% image url="https://uploads.developerhub.io/prod/86Yw/zn4zdoyqone3x2rq5a2zvebomq2izfmrzq64kyo20cv4y6x4ukpi8j9bdt4qlmf1.png" caption="" mode="responsive" height="1168" width="1840" %}
{% /image %}


## The PCB Editor

The PCB editor is where you create layouts and footprints. The Flux PCB editor contains three main sections:

{% image url="https://uploads.developerhub.io/prod/86Yw/c8qvzquunc2jx18rtwfksrqxxyych9rbxrgpmw9zd6bwh3nsui9l1znv0pnknkmb.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


- The [layout object tree](https://docs.flux.ai/flux/reference/reference-object-tree-pcb) on the left side: shows a list of all the objects present in the PCB layout.
- The [Selector-Based Layout Rules](https://docs.flux.ai/flux/reference/pcb-layout-rule-selectors) menu on the left side: where you create selector-based rules.
- The [Object-Specific Layout Rules](https://docs.flux.ai/flux/reference/object-specific-pcb-rules) menu on the right side: where you create object-specific rules.
- Some menus are shared with the schematic editor, like the [The Library](https://docs.flux.ai/flux/reference/reference-library) and [Properties](https://docs.flux.ai/flux/reference/reference-inspector-properties) menus.

### Netlist and ECO

The relationship between schematics and layout in Flux is pretty straightforward. Any change in one editor will immediately be reflected in the other. There is no need to generate netlists or ECOs.

### Eagle Properties vs Flux Rules

Flux's Rules are the most important concept in the PCB editor. They are similar to Eagle's properties, but in Flux every object in the layout is modified through rules. For example, the board outline, trace width, or pad size are adjusted this way.

In Flux, rules are not only design guardrails, but they can directly modify a design as well. For example, if you add a "position" rule to an object, that object will immediately be moved to that position. In Flux, there are two main types of rules:

- Object-specific Layout Rules: rules set here only apply to the selected object. You will see these rules on the right-side menu as soon as you select an object.
- Selector-based Layout Rules: rules set here will apply to every object that matches the selector. You will see them when you go to the "Rules" menu on the left. An object-specific rule takes precedence over selector-based rules. This is similar to adding elements to a group and then modifying group properties.

{% image url="https://uploads.developerhub.io/prod/86Yw/5nh15bcxchnsox3um0skbuqtdmniynjkl6m7rsctge9jb4s1k3hdai2dvqgmhs38.gif" caption="" mode="responsive" height="500" width="800" %}
{% /image %}


### Routing

Routing in Flux is also straightforward. When a pad connects to another pad in the schematic (they share a net), a white dot will appear when you hover your mouse on top of the pad. Simply click on the white dot and route your trace. For multi-layer routing, right-click while laying out a trace and select the target layer. Flux will automatically place the necessary vias.

High-speed routing is as easy as low-speed routing. Flux seamlessly handles the complexities behind the scenes, with automatic integration of impedance and differential pair metadata baked into components. Initiating a route for one trace in a differential pair triggers automatic routing for its counterpart. Learn more in [this tutorial](https://docs.flux.ai/flux/tutorials/advanced-routing).

{% image url="https://uploads.developerhub.io/prod/86Yw/rsbjt5c80cfzggjp4b7y414f0ikymj5pbdvkfm2gnxpiv86zild10uadbnq0rdev.gif" caption="" mode="responsive" height="500" width="800" %}
{% /image %}


### Copper Fills

Flux doesn't currently support arbitrary-shaped polygons (ground or otherwise). Flux will create a full-board ground fill as soon as a ground symbol is placed into the schematic. These copper fills can also be re-assigned to other nets to create power planes.

To learn more about automatic ground-fills, copper fills in general, how to disable it or how to add via stitching, refer to the [copper fills documentation](https://docs.flux.ai/flux/tutorials/tutorial-ground-fills-deep-dive).

{% image url="https://uploads.developerhub.io/prod/86Yw/cubw6vprktgrl2zzk7gls6p6kfii9m4ctof4sp9ki7wmp7del9z1z4vh3vmpsvn8.png" caption="" mode="responsive" height="2464" width="3808" %}
{% /image %}


### DRC Checks

Flux’s layout rules do a great job of eliminating unnecessary mistakes, but certain types of violations require additional checking. Such violations include overlapping traces, unrouted nets, missing footprints, etc. [Learn more about DRC checks](https://docs.flux.ai/flux/reference/design-rule-check--drc-).

### Gerber Files and Fabrication Export

Flux allows you to export all the files you'll need for fabrication, including Gerbers, BoM, and pick and place files. [Learn more about manufacturing](https://docs.flux.ai/flux/reference/gerber-export).
