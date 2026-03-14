# Source: https://docs.flux.ai/Introduction/easyeda-to-flux.md

# EasyEDA to Flux


Experience the future of PCB design with Flux, a cutting-edge PCB design tool accessible via your web browser. Flux is an AI hardware design assistant capable of answering complex queries and creating schematic connections.




Overview

Embracing Flux for PCB design offers a modernized and streamlined approach featuring AI assistance, enhanced collaboration, efficient project development, and improved organization. In this tutorial, we will guide you through transitioning from EasyEDA to Flux. We will emphasize the key distinctions and provide valuable tips to ensure a seamless switch, enabling you to start designing circuit boards with ease.

{% image url="https://uploads.developerhub.io/prod/86Yw/5r4k35k8y3t16635dpu8tgcfa5n3woo29fn2r27ovf43jd1se0gfgfei9oitvhy9.png" mode="responsive" height="2382" width="3680" %}
{% /image %}

## Why Transition from EasyEDA to Flux?

Flux represents a contemporary tool with innovative workflows that enable streamlined processes, effortless collaboration, integration with AI, and rapid development.

Key Features:

- **Accelerated Design with AI**: Leverage AI capabilities to speed up the design process, enhancing efficiency.
- **Full-Featured Free Tier**: Flux offers a fully-featured free tier with no obligations, limiting only the number of concurrent private projects you can maintain.
- **Seamless Collaboration**: Multiple users can effortlessly collaborate on projects, simplifying project sharing and management.
- **Automated Features**: Enjoy the convenience of auto-save, auto-version control, and auto-history, eliminating the need to worry about file management and saving.
- **Effortless Project Sharing**: Share projects effortlessly by simply sharing a link, making collaboration straightforward.
- **Template and Example Projects**: Avoid starting from scratch by using Flux's templates and sample projects, enabling quick project initiation.
- **Community Integration**: Draw inspiration from the community's projects and quickly build upon them, fostering creativity and innovation.
- Simple Part Creation: Easily create new parts not already in your library, enhancing the versatility of your designs.
- **Project Accessibility**: Collaborate effectively by forking other projects, showcasing Flux's built-in accessibility and collaboration features.

{% image url="https://uploads.developerhub.io/prod/86Yw/z7p2gb1nipiz94ejmanq4gxbbucawqyxusfdg6gvt2i0i750403vgvixv38o13ih.png" mode="responsive" height="2464" width="3808" %}
{% /image %}

### Streamlined Collaboration

Flux's browser-based structure simplifies sharing and collaboration through the straightforward act of sharing links.

By default, projects remain private, ensuring that only you can access and view them. If you wish to grant other users access to your projects or make them entirely public, you can achieve this through the share menu.

Sharing projects is as easy as copying and pasting the URL. Individuals with the appropriate access level can seamlessly collaborate on the same design. This feature proves particularly convenient for open-source projects, facilitating collaboration among engineers working remotely on a shared endeavor.

{% image url="https://uploads.developerhub.io/prod/86Yw/aab4uhmqu1l7ky9znboelekmyuxzst4gly3cnbb2djlxhg3gf1pt68i8f0bb4g4f.png" mode="responsive" height="2024" width="3536" %}
{% /image %}

### Accelerated Development with AI

Flux Editor boasts a formidable AI assistant, which supports your project development in various ways.

With Flux integrated into your projects, you gain a robust AI design assistant that offers invaluable feedback, cost-saving insights, and error prevention. Flux comprehends the context of your project, encompassing components, connections, and datasheets, enabling tailored assistance in part selection, schematic design feedback, and comprehensive design analysis.

{% image url="https://uploads.developerhub.io/prod/86Yw/52isckhjdn7mmzt92ljvb1beq467vckybuqg2zeywwwo0fzyn3bk3bcw8lqhzvc6.png" mode="responsive" height="2040" width="3552" %}
{% /image %}

### Effortless Version Control

EasyEDA provides cloud-based storage for design files, making it easily accessible to work from anywhere with an internet connection —Flux, similarly uses cloud-based storage. Furthermore, Flux's user-friendly [version control](https://docs.flux.ai/flux/tutorials/version-control---deep-dive) simplifies the process of tracking changes in a collaborative environment and allows for easy rollback if issues arise. Flux's version control system resembles that of other web-based tools, such as Google Docs, where every modification you make is automatically saved and assigned a new version. This ensures that no individual change is ever lost, and you can easily revert your document to a previous state through the "Change History" menu.

{% image url="https://uploads.developerhub.io/prod/86Yw/nhljf9t0seybyjm8exiso0zdcvldtfukmo1hhfwuxb6iv6c8sx0lchjjeaj1rdy5.png" mode="responsive" height="2028" width="3540" %}
{% /image %}

### Organized Project Management

Being browser-based, every element within Flux possesses a readily shareable URL. Eliminating the concept of traditional files ensures that engineers always have convenient access to every aspect of a project. There's no need to fret about missing files when sharing a project.

### Modules

[Modules](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts) offer the capability to swiftly reuse circuit block modules, such as power converters or oscillators, that you've utilized in prior projects. These modules function as complete design blocks, complete with included parts, traces, vias, and more, facilitating their placement into existing projects for efficient reuse. Each terminal in the submodule's symbol corresponds to a terminal in the submodule's schematic, ensuring seamless integration and compatibility.

{% image url="https://uploads.developerhub.io/prod/86Yw/lx59fpwv4qod120m26pldov73vpzm2ror3xz8iy5m197sn5lhvdsbsqnvxmnkvyy.png" mode="responsive" height="1850" width="2912" %}
{% /image %}

### Flux’s Unified Library

Both Flux and EasyEDA have powerful libraries, but each works a little differently.

EasyEDA provides users with collection of three major component libraries: the common library, user-generated library, and a third library connected directly to a component parts vendor. EasyEDA also allows users to create custom components, enhancing the flexibility and versatility of their component choices within the platform.

Flux offers a unified library that is collectively curated by the community, housing all accessible components in one place. This unified approach streamlines the process of locating specific parts, making it both rapid and straightforward. Within this single library, you'll discover not only the components you or your team have generated, [regardless of their privacy settings](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions), but also components contributed by the broader community. This eliminates the need for users to sift through and manage multiple libraries individually, as they can effortlessly harness the extensive array of community-created parts by simply using the search feature.

{% image url="https://uploads.developerhub.io/prod/86Yw/8mlr7bhzld2wonp3mxcw3ls985fism96bmytr4pecoqj174qgkri2vwh1rewajg5.png" mode="responsive" height="2040" width="3552" %}
{% /image %}

> Can’t find the part you’re looking for? You can easily add parts to the library with specific permissions through this method.


### Part Creation

EasyEDA facilitates the creation of custom parts with a user-friendly approach. Users can easily design and define their unique electronic components, including symbols, footprints, and associated parameters, tailored to their specific project requirements.

To initiate the process of creating a new part in Flux, the first step involves the [creation of a new blank project](https://docs.flux.ai/flux/reference/reference-new-project-menu). Within this project, you have the flexibility to add an arbitrary number of terminals to the schematic, tailored to your specific requirements. Each terminal corresponds to a pad within the PCB editor, allowing you to customize and configure it to craft the precise footprint you desire. Once your project is complete, publishing it will automatically add it to the parts library. This unique approach signifies a departure from the conventional notion of "traditional parts," as in Flux, parts are constructed using the same methodology as projects, resulting in a more integrated and streamlined design process.

📖 Naming convention: pins (traditional) → terminals (Flux). Both have a similar function, but pins are called terminals in Flux.

In Flux, there is no “assigning” a footprint to a symbol or part. Every part, project, or module has a schematic and associated PCB layout, known as a footprint.

{% image url="https://uploads.developerhub.io/prod/86Yw/7740vseryo7cgksovbtbwwpo3tx4dnchzsczgd838pta7upca1q5suv1t3he3tre.png" mode="responsive" height="2020" width="3504" %}
{% /image %}

### Generic Parts

In Flux, users have the flexibility to choose from multiple footprints for a particular part. This capability is advantageous as it permits automation of package selection through code, enhancing efficiency in the design process. With specific footprints bundled with each part, there's no need to embark on a search across various libraries. All available footprints are readily accessible, enabling users to conveniently select the most suitable one as needed.

{% image url="https://uploads.developerhub.io/prod/86Yw/2svdmi51m2t62p1bednzgpmgyzc7mjt263e5vngxi8rsjjftzrmujjco3xp289ts.gif" mode="responsive" height="336" width="640" %}
{% /image %}

### Project Cloning and Forking

Flux simplifies project management with its easy-to-use project forking feature. This functionality not only preserves the entire history of changes but also facilitates the merging of the forked project back with the original, ensuring comprehensive version control and collaborative workflow. Additionally, users can opt to clone a project, generating a pristine copy devoid of any historical data, which can be valuable for starting new projects or making significant alterations without cluttering the project's history.

## From EasyEDA Schematic Editor to Flux Schematic

### Sheets

EasyEDA uses a series of different sheets in a hierarchal format for project file management. Flux, on the other hand, enables limitless nesting through the [modules feature](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts), meaning that when you drag a submodule into your schematic, you can simply double-click it to access and explore a more intricate, detailed view of its internal operations.

### Symbols

In both PCB design softwares, when placing a specific part or module into the schematic canvas, the symbol is what represents it on this level in the hierarchy.

EasyEDA designer uses a built-in editor for creating custom symbols that appear in the schematic. Flux provides [compatibility support for custom symbols](https://docs.flux.ai/flux/tutorials/tutorial-creating-a-part-from-scratch#2--creating-a-symbol) by allowing the importation of SVGs. Additionally, users have the capability to delve further into the hierarchy by double-clicking any part to gain insight into its internal components, or even observe the absence of such components.

### Wiring

In EasyEDA you may be used to pressing _W_ to place down wires or clicking the terminal of a part in the schematic editor. In Flux, it’s as simple as clicking on a pin and wiring away.

### Alignment

In EasyEDA, objects will automatically clip to the grid during the placement stage. In Flux, consider first aligning your symbols magnetically, as it can result in neater and more organized wiring in your schematic as you progress with your design.

### Flux Terminals & Net Portals act as EasyEDA’s Net Ports

In EasyEDA, net ports are utilized to establish connections between nodes across various sheets. Similarly, in Flux, terminals serve functions akin to ports, and net portals perform roles similar to labels.

### Bill of Materials (BoM), Pricing, and Availability

EasyEDA requires exporting its Bill of Materials (BoM) every time to view the latest part availability.

Flux, on the other hand, offers a LiveBoM feature which provides real-time updates on part sourcing from the top three distributors, using the manufacturer part number (MPN).

Generating a .CSV export is straightforward and includes all essential components along with their respective attributes.

{% image url="https://uploads.developerhub.io/prod/86Yw/10a9g3ck45n1a863k1bqpa7gj6y8xwi54wsppuguaqr8eo5gihlp99xvr64ekqe8.png" mode="responsive" height="827" width="280" %}
{% /image %}

### Notes & Comments

In Flux, users can directly create notes as objects on the schematic. Additionally, comments can be effortlessly made and positioned anywhere. This approach facilitates seamless collaboration among users working on a Flux PCB board.

## From EasyEDA’s PCB Editor to Flux’s PCB Editor

### EasyEDA’s Import Wizard is Automatically Handled In Flux.

EasyEDA requires you to go through an “import changes” wizard to facilitate any schematic changes being updated in the PCB.

Flux will automatically sync any changes made in the schematic, code, or PCB canvas to the cloud.. Although it doesn’t use a change buffer, Flux has Git-based version control that allows for restoring older versions if an undesired change is made.

{% image url="https://uploads.developerhub.io/prod/86Yw/6mffxd3x6bwmqbnzygiic5ta7bbu9kos0q8x01zlw5tz8v5ihg9pcz1yz40tq4lj.png" mode="responsive" height="627" width="353" %}
{% /image %}

### Flux’s Layout and Selector-Based Rules Mimic Easy EDA’s Design Rules Panel

When you start a new PCB project in EasyEDA, the design rules panel is crucial. It lets you configure various aspects such as clearance distances, shapes, and properties of elements like traces, silkscreens, and components. Once you've set these parameters, you can further fine-tune the properties of individual objects on the PCB canvas through the properties panel. The typical workflow in EasyEDA involves setting up board rules, placing parts and routing (while making adjustments via the properties panel), followed by a design rule check. If you violate any rules, errors will be flagged in the final stage.

Conversely, Flux adopts a real-time, rules-based workflow. Here, the properties of objects are governed by rules. Instead of waiting until all components and traces are placed, Flux provides continuous feedback and can even auto-adjust component properties to align with your established rules.

In Flux, specific layout rules are managed using the Inspector panel on the right. When you select an element, the layout rules menu appears, allowing you to add or modify rules and configure every detail, from parts and traces to the board itself.

{% image url="https://uploads.developerhub.io/prod/86Yw/96otytysv72826ao3cewbzqt0y7m7310n46op7uougsvdle235axg7epzxlla7qt.png" caption="Inspector panel on the right side with object-specific rules" mode="responsive" height="848" width="1131" %}
{% /image %}

Any attribute of any PCB element can be adjusted through rules in Flux, including position, rotation, size, and more. For further details, you can refer to the [layout rules page](https://docs.flux.ai/flux/reference/pcb-rules) rules. Your workflow in Flux involves constantly referencing these layout rules and components, as the rules dynamically update the circuit during your design process, unlike in EasyEDA.

Flux also offers  [selector-based layout rules](https://docs.flux.ai/flux/reference/pcb-layout-rule-selectors), which let you apply changes to multiple elements simultaneously. For instance, you could adjust the width of several traces in a single net with one rule.

Consider a scenario where you're an engineer reviewing a previously designed PCB and you come across a trace with an unusual width.

- In EasyEDA, the reason behind this specific width or the influencing factors might be unclear.
- However, in Flux, it's more transparent. Either a specific object rule or a selector-based rule has actively altered its width, and you can easily investigate which rule is influencing this particular trace.

### Trace Routing and Impedance Matching

Both EasyEDA and Flux allow for trace creation by simply click on the nodes of a pad object [and wire away](https://docs.flux.ai/flux/reference/reference-net-width)!

High-speed routing is just as straightforward as conventional routing. You can master all the nuances of high-speed routing, including impedance control and differential pairs, by [following this tutorial](https://docs.flux.ai/flux/tutorials/advanced-routing).

### Copy Pasting

Flux facilitates effortless duplication of any object on the canvas. You can design an object, assign your preferred rules to it, and then conveniently copy and paste it wherever needed.

### Polygon Pours

Currently, Flux doesn't support polygons of arbitrary shapes, whether for ground or other purposes. However, Flux automatically generates a full-board ground fill as soon as a ground symbol is added to the schematic. These copper fills can also be reassigned to different nets to create power planes. For more details about automatic ground-fills, general copper fills, how to disable them, or how to add via stitching, you can consult the [copper fills documentation](https://docs.flux.ai/flux/tutorials/tutorial-ground-fills-deep-dive). Additionally, Flux provides the option to "shelf" the GND fill by toggling its visibility button.

Instead of relying on arbitrarily shaped polygons, Flux's rule-based workflow dictates the form of copper fills. Specifically, rather than using a random shape for a copper fill, Flux automatically shapes it based on keep-out rules. This rule-driven approach to generating copper fills allows other engineers to inspect the board and more easily understand the rationale behind the copper fill's shape, as opposed to a pre-defined arbitrary form. However, it's worth noting that enhanced functionality for polygon pours is being planned for future updates!

### Stackup Manager

EasyEDA provides a layer manager for configuring the board stack-up. This includes setting up the number of copper layers, silkscreen, outlines, and more.

In contrast, Flux manages its stack-up configuration through constraints defined in the layout object. By default, new projects in Flux are set up with a 4-layer stack-up. If you need to configure a different stack-up in Flux, follow these steps:

1. Navigate to the "Objects" tab on the left panel of the PCB editor and locate the "layout" object.
2. Click on the "layout" object. In the right panel, you'll find the option to add an "Object Specific rule" named "Stackup.”
3. From there, you can select the appropriate stack-up from the provided list.

Flux offers multiple pre-made stackups tailored for commonly used manufacturers, [including AISLER](https://www.flux.ai/aisler), JLCPCB, and PCBWay

### Design Rules Check (DRC) and Constraints

EasyEDA employs a system of design rule checks (DRC) and various other constraints, which are defined within its design manager.

Conversely, in Flux, these tools and settings are managed using the layout tools. Flux simplifies the process by eliminating the need to scour manufacturers’ websites for constraints or navigate through multiple rule import wizards. Instead, you can conveniently [clone a template that already has all the necessary DRC presets](https://www.flux.ai/jharwinbarrozo/2-layer-jlcpcb-constraints?editor=pcb_2d).

Moreover, Flux is committed to regularly updating and adding new DRC rules. If you find that a specific rule you need is missing, you are encouraged to [submit a ticket](https://docs.flux.ai/flux/Introduction/getting-support) to request its inclusion.

### Board Outline

In Flux, the board outline is treated as a distinct object within the [object tree](https://docs.flux.ai/flux/reference/reference-object-tree-pcb) pcb. To edit its characteristics, just like you would with any other object, simply select the board outline. Then, you can modify its features using rules. You can find the "Layout" object in the object tree. For guidance on creating custom shapes, you can [refer to this specific tutorial](https://docs.flux.ai/tutorials/tutorial-board-outline-shape#advanced-custom-shapes).

### Navigation & Shortcuts

You can zoom in and out using the mouse wheel and pan the view by clicking the middle mouse button. Flux also natively supports trackpad gestures, making navigation as intuitive as browsing a website.

For a comprehensive list of Flux shortcuts, you can access them from the top left corner by selecting "Keyboard Shortcuts". Some handy shortcuts include:

- Zoom to Fit All or Selection 0
- Rotate Right ]
- Rotate Left [
- Flip wire elbow direction /
- Finish drawing a wire Double click the canvas or Click a terminal or Esc

### Flux Code and Simulator

In EasyEDA, users have the capability to simulate their circuits. This feature allows for the detection of errors and verification of functionality before moving forward with the PCB layout.

Flux, utilizing JavaScript, offers a public API that includes a . This enables you to run simulations on your circuit, ensuring that it functions as intended prior to proceeding with manufacturing.

### Wrap Up

| Feature | Flux | EasyEDA | 
| ---- | ---- | ---- | 
| Circuit Simulation | Yes | Yes | 
| Reusable Designs/Components/Modules | Yes | Yes | 
| Bill of Materials (BOM) Generation | Yes | Yes | 
| Design Rule Checking (DRC) | Yes | Yes | 
| Cloud-based Storage | Yes | Yes | 
| Collaborative Design | Yes | Yes | 
| Gerber File Generation | Yes | Yes | 
| 3D Viewer | Yes | Yes | 



That sums up the essential information for transitioning from EasyEDA to Flux. Overall, the switch should be relatively seamless, thanks to Flux’s intuitive user interface. Combined with its extensive community library, diverse collaboration features, and robust simulation capabilities, the transition to Flux should be swift, enabling you to design PCBs efficiently and effectively in no time.

### Getting Help

In case you need assistance, here are some additional resources:

- [Slack Community](https://www.flux.ai/p/slack-community): Engage directly with the Flux team and connect with other engineers, designers, and hardware enthusiasts. It's a great place to ask questions and share experiences.
- [Bug Reporting](https://fluxai.canny.io/): If you encounter bugs or unexpected behavior while using Flux, please report it through our issue-tracking tool. Your feedback is invaluable for improving the platform.
- [YouTube](https://www.youtube.com/channel/UC5CsglCHQBd4-WFrZmqzVyw): Dive into our extensive video tutorials, crash courses, and recorded events. You'll also find content from independent creators with insightful videos on how to utilize Flux effectively.
- [Live Support](https://www.flux.ai/p): For more direct assistance, visit our home page, scroll down to the bottom, and click "Contact us." We're here to help with any queries or issues you may have.
