# Source: https://docs.flux.ai/faq/frequently-asked-questions--faq-.md

# Schematic Editor FAQs

## Collaboration & Sharing

### How can I invite team members or share my project with others in Flux?

Click the **Share** button in your project to set global permissions (e.g., "Anyone can view" or "edit"). You can also invite team members by entering their email or username and then sharing the project link. More details are available in the [Sharing & Permissions guide](https://docs.flux.ai/reference/reference-sharing-and-permissions).

### Are my designs private by default? How can I make them public?

Yes, new projects are private by default. To make a design public, open the **Share** dialog and select an option like "Anyone can view" or "edit."

## Schematic Design

### How can I label nets or create named connections in the schematic?

Use **net portals** by placing a portal symbol on a wire and entering the desired net name. Any portal sharing that name will automatically connect the nets. Learn more in the [Schematic – Net Portals guide](https://docs.flux.ai/Introduction/getting-started-in-flux--schematic#net-portals).

### How do I create a circuit schematic and connect components in Flux?

- Drag components from the **Parts Library** onto the canvas.
- Connect them by clicking on a pin and dragging to another pin.
- Flux automatically assigns net names if you don’t label them.
More details in the [Getting Started – Schematic guide](https://docs.flux.ai/Introduction/getting-started-in-flux--schematic).

### How do I create a bus (multi-wire connection) for signals in my schematic?

Flux does not support a dedicated bus object. Instead, connect each signal individually and use net portals (e.g., `D0`, `D1`, `D2`...) to logically group them.

### Does Flux support multi-sheet schematics or reusable sub-circuits?

Flux uses a single-sheet schematic approach. However, you can section your schematic or create **[Modules](https://docs.flux.ai/tutorials/tutorial-parts-and-sublayouts)**—reusable sub-circuits that encapsulate part of your design.

### Can I export my schematic as a PDF?

No, you cannot export a PDF of your schematic from Flux right now.