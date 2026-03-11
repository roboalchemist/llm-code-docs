# Source: https://docs.flux.ai/Introduction/getting-started-in-flux-manufacturing.md

# Getting Started in Flux: Export & Manufacturing

Order your Printed Circuit Board (PCB) from a manufacturer



## Summary

In this guide, we will walk you through the steps of ordering your PCB from a manufacturer after completing the design in Flux. You'll learn how to choose the right manufacturer, understand the difference between PCB and PCBA, and select the appropriate board parameters for your specific project.

### **PCB and PCBA**

A PCB is the bare board with no components attached. If you're also looking to have the components soldered onto the board, this is referred to as PCBA (Printed Circuit Board Assembly). Manufacturers often offer both services, but the assembly is an additional step and cost.

![](https://uploads.developerhub.io/prod/86Yw/fbr8cqtdvl0ugp3ppof9sxgwtdo5jf6xvsoqgijc58c2d6j1vmgok7l465ofl2gd.png)

## Getting Started

Make sure you have all the required Gerber files from the previous step. These files contain the information manufacturers need to produce your board. [Export](https://docs.flux.ai/flux/reference/gerber-export) them from Flux if you haven’t already.

### Choosing a Manufacturer

When choosing a manufacturer, there are a few key factors to consider:

- **Price vs. Speed:** Some manufacturers offer faster turnarounds but at a higher cost. Determine your timeline and budget before selecting.
- **Location:** Manufacturers located offshore may have lower costs, but longer shipping times and potential import taxes or fees. Local manufacturers may offer faster shipping, but at a higher price.
- **Reputation and Support:** If you're new to PCB ordering, you may prefer a manufacturer with strong customer support and an easy-to-use platform.

### How to Order a PCB

Most manufacturers have online quoting tools that allow you to easily upload your files and specify your order details. While the process is similar across different platforms, we'll walk you through it using Seeed Studio's platform as an example.

1- Upload Gerber Files

Upload the gerber files you exported from your Flux project to the manufacturer's website

![](https://uploads.developerhub.io/prod/86Yw/70xroi1f9yuqkrzj354qexe5bnim6l4mhyepz4lax6ixy86po62og5wefu9vj54q.gif)

### 2- Select Board Parameters

The second step is to define some additional parameters. Board parameters are the technical specifications you can customize for your PCB, such as the layer count, board thickness, material type, and more.

While most tools will automatically detect most parameters from the Gerber files, you may want to adjust them based on your specific needs. Some of these will increase the cost of your PCB, so make sure you only select the ones you need. Here's a breakdown of key parameters to consider:

| Parameter | Description | Tips for Selection | 
| ---- | ---- | ---- | 
| Plating Finish | The surface coating on the PCB that affects solderability and longevity. | - HASL is cost-effective, good for general use.\n- ENIG offers better reliability and is lead-free, suitable for high-density boards.\n- OSP provides a flat surface, ideal for fine pitch components but has a shorter shelf life. Choose based on your environmental requirements, soldering technology, and budget. | 
| Minimum Trace Width | The narrowest width of the conductive tracks on the PCB. | - Determine based on current carrying capacity and space constraints. Thinner traces save space but may not handle high currents well.\n- Use IPC-2221 guidelines to calculate the appropriate width for your application’s current requirements. | 
| Layer Count | The number of conductive layers in the PCB. | - More layers allow for more complex circuits in a smaller footprint but increase cost.\n- Assess the complexity of your circuit and space constraints to determine the necessary layer count. | 
| Board Thickness | The thickness of the PCB, typically ranging from 0.5mm to 3.2mm. | - Thicker boards are more robust and better for high-power applications.\n- Consider the end product's size constraints and mechanical requirements. | 
| Material Type | The substrate material used, affecting thermal and mechanical properties. | - FR-4 is standard, good for most applications.\n- Advanced materials like Rogers offer better performance at high frequencies.\n- Select based on thermal requirements, signal performance needs, and cost. | 
| Via Type | Conductive pathways (through-hole, blind, buried) connecting different layers. | - Through-hole vias are standard and cost-effective.\n- Blind and buried vias save space and are used in complex, high-density boards.\n- Choose based on circuit complexity and layer count. | 


These are some additional parameters you might want to consider:

- Choose a different PCB color (soldermask) if needed.
- Add a stencil to the order if you're planning to solder the components yourself.
- If you want the manufacturer to solder components for you, please refer to the PCBA section below.

![](https://uploads.developerhub.io/prod/86Yw/5u6ye98egp1nrgyf2qpk60pw59ifhhm1ru9ejm0vrep7b4nfxyyinjcnizvniax2.gif)

### 3- Ordering PCBA

If you'd like the manufacturer to assemble the components for you, you can opt for PCBA services. This step is optional—you can always choose to solder the components manually, which may give you more control but requires additional time and tools.

Reasons to choose PCBA:

- **Speed:** Manufacturers have the equipment to solder components quickly and accurately.
- **Precision:** Ideal for boards with many small or complex components.
- **Cost Efficiency:** For larger production runs, PCBA is often more cost-effective.

#### Uploading a BoM

To request PCBA, you'll need to upload a Bill of Materials (BoM). The BoM includes component part numbers, quantities, and placement details and typically comes in a spreadsheet format (CSV or XLS). Flux automatically generates BoM files that are compatible with several popular manufacturers, such as:

1. Seeed
2. Advanced Circuits
3. AllPCB
4. Seeed Studio Fusion
5. Eurocircuits
6. JLCPCB
7. PCBWay
8. Aisler
9. OSH Park
10. Lion Circuits

If your manufacturer isn’t listed, you can modify one of the generated BoM files or [request our team](https://feedback.flux.ai/featurerequests) to add support for your target manufacturer.

![](https://uploads.developerhub.io/prod/86Yw/cymiwcc40ifes4901he38q64v5w3h3nmnj5innajbtk6ig5smf933coe0zk98mdg.gif)