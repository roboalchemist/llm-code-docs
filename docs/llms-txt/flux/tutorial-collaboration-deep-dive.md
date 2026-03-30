# Source: https://docs.flux.ai/tutorials/tutorial-collaboration-deep-dive.md

# Collaboration in Flux - Deep Dive


Collaborate effectively with other members from your team and external partners.




## Overview

Flux was built for collaboration and can support the kinds of workflows found in larger engineering organizations as well as small nimble teams. By facilitating real-time information flow, Flux enables engineering teams to work more efficiently.

## Getting Started

### Managing Access

With Flux, sharing a project with anyone on your team is extremely simple. As long as your project has permissions configured correctly, you can share your design by providing a URL to the project.

For detailed information about Flux's multi-layered permission system including organization and enterprise permissions, see [Permission Tiers and Access Control](https://docs.flux.ai/flux/reference/reference-permission-tiers).


#### For Individuals

Using the share menu in the top-right corner, you can control who has access to your project. Every project is private by default, meaning that only you have access to it.

Once permissions are set, simply copy the URL from your browser and paste it into an email, chat application, or even a text message!

{% image url="https://uploads.developerhub.io/prod/86Yw/fe1dj043byhk48ip898flpk4oyc7c4blcwwzx9rp9td6hvud3atu3q49pk70x0dc.png" mode="600" height="312" width="600" %}
{% /image %}


#### For Organizations

The steps for individuals apply to projects within organizations, with the addition of organization-wide access settings. Organizations can also set default permissions for all projects and manage user roles on a larger scale. For detailed instructions on setting up organizational permissions, please refer to the [organizations tutorial](https://docs.flux.ai/flux/Introduction/flux-for-organizations).

### Commenting

Flux's comments allow engineers and collaborators to interact directly where the design data lives, making the exchange of ideas and feedback more efficient and contextually relevant.

Comments are visually represented by pins on the design canvas and can be managed through options like adding, resolving, or deleting, as well as embedding external content such as videos or images to enrich discussions. They automatically adapt to different zoom levels, ensuring comments are accessible yet unobtrusive. You can learn more about how they work in the [comments tutorial](https://docs.flux.ai/flux/reference/reference-comments).

To add a new comment, you can right-click -&gt; "Insert Comment" or press the key `C`.

{% image url="https://uploads.developerhub.io/prod/86Yw/10244v5fdkkj2gn1vrm9wxie4f0sxrlunkkjwscazevw70g6k249bqd3p7exrp3n.png" mode="600" height="1306" width="600" %}
{% /image %}

### Shared Resources


#### The Library

The [community library](https://docs.flux.ai/flux/reference/reference-library) in Flux embodies Flux's commitment to collaboration. Designed for sharing [parts and projects](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts) so that they can be accessed and reused by other members of the Flux community, the library helps the community work faster and more efficiently.

{% image url="https://uploads.developerhub.io/prod/86Yw/tmezofypwua4vpsu3eyl09lir0yjjflxyyoce80dz8k7z1d4x73bcj2b0d8gfklr.gif" mode="600" height="356" width="600" %}
{% /image %}


#### Example Projects and Templates

We are big believers in not starting from scratch. At Flux, you can leverage a comprehensive repository of example projects and templates created by your team or the global hardware community.

Reusing existing resources accelerates your design process, allowing you to clone or fork as needed for customization. Explore these resources through our search bar, project launcher, or featured projects.

Refer to the [Reusing Projects tutorial](https://docs.flux.ai/flux/tutorials/reusing-community-projects) for a detailed guide on how to effectively use example projects and templates.

{% image url="https://uploads.developerhub.io/prod/86Yw/ea4xk3rhv6rikvnhnhu9bit6b7psbpb3j7h1u82xkj1by0oqgjudlok2tr7zxcjc.png" mode="responsive" height="1222" width="2172" %}
{% /image %}

## Team Collaboration

Once you've established your project in Flux, creating an intelligent workflow is essential.

In general, PCB design collaboration consists of one, or both, of the following:

- Mechanical engineer (ME) + electrical engineer (EE)
- Multiple electrical engineers (EE + EE)

### ME + EE Collaboration

Mechanical Engineers are responsible for many elements that determine the construction of an end product, and thus create constraints on what an EE can do in the PCB layout. EEs have to work within these constraints to make sure that the design fits into the enclosure, is within the required board size and shape, and that important components are fixed in their required locations.

Inside of Flux, MEs can define and lock component locations, set board size and keep-outs, and even create enclosures. MEs can also manage all the mechanical elements that PCB designers need to include in the PCB layout, including component models and design rules defining placement. Flux is also unique in that it allows for both groups to use the design rule system to create the final PCB layout.

{% image url="https://uploads.developerhub.io/prod/86Yw/l05bp8k0jpkc5c75c70iszwbc9fqnmlxolwhrghl2s3bs6wapzjvt62lvlrvwr91.png" mode="responsive" height="1079" width="1918" %}
{% /image %}

### EE + EE Collaboration

Electrical Engineers don't always work on the same project simultaneously, which can lead to repeated unnecessary work. Flux changes this narrative with the introduction of the parts and sub-layout functionality. With these features, Flux allows responsibilities to be very easily divided among multiple EEs without creating overlapping tasks. Now, EEs can divide up work within a project through some of the following methods:

- Parts creation
- Creating sub-layouts (both schematics and PCBs)
- Building simulations for modules
- Determining how to connect modules while sticking to constraints from the ME

Traditional ECAD applications do not implement the same kind of sub-layout system found in Flux, so it's difficult to divide responsibilities in this way. In Flux, an engineer can oversee a project and weave together each of these pieces into the final product.

## External Collaboration

Collaborating with external partners in PCB design and manufacturing is just as easy as working with your internal team when you use Flux. This platform streamlines interactions with PCB manufacturers and component suppliers, ensuring smooth and efficient processes from design to production.

**Engaging with Manufacturers:** Typically, manufacturers become involved only after your design is nearly finalized to help identify any design for manufacturability (DFM) issues. Flux facilitates this by allowing you to share your designs directly with manufacturers for a seamless review process, helping pinpoint and address potential DFM concerns right on the platform. [Read more](https://docs.flux.ai/flux/Introduction/getting-started-in-flux--export-and-manufacturing).

**Simplifying Procurement:** Encountering out-of-stock components no longer means a halt in progress. With Flux, you can easily find and substitute alternative parts within your design files. This functionality not only saves time but also enhances the adaptability of your production process. Team members can update component choices in real-time, ensuring the project moves forward without delays, regardless of supply chain fluctuations. [Read more](https://docs.flux.ai/flux/tutorials/components-procurement).

## What's Next

Now that you understand how collaboration works in Flux, you might want to explore:

- [Version Control Deep Dive](https://docs.flux.ai/flux/tutorials/version-control---deep-dive) - Learn how to manage changes to your projects
- [Parts and Sublayouts](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts) - Understand how to create reusable components
- [PCB Design Review](https://docs.flux.ai/flux/tutorials/pcb-design-review) - Learn how to effectively review designs with your team
- [Components Procurement](https://docs.flux.ai/flux/tutorials/components-procurement) - Explore how to manage component sourcing collaboratively
