# Source: https://docs.flux.ai/tutorials/high-density-designs--hdi-.md

# High Density Designs (HDI)


Learn how to design modern high-density interconnect (HDI) PCBs effortlessly.




## Overview

Key considerations for HDI boards include layer stack-up planning, via size and type, and manufacturability constraints. Proper design rules must be applied to ensure signal integrity and reliable manufacturing, and advanced techniques like laser drilling for microvias are often necessary.

While lower density boards can be completed with just through hole vias, Blind vias, micro vias, and buried vias are all necessary components in HDI PCB design.

- **Blind vias** connect an outer layer of the PCB to an inner layer but do not pass through the entire board.
- **Buried vias** link two internal layers without reaching the outer layer, and are therefore hidden within the board's structure.
- **Microvias** are very small vias typically used to connect adjacent layers.

{% image url="https://uploads.developerhub.io/prod/86Yw/bi6hssijippfsgcke6xsvwy0hsr87ztp0efuisl1f5m5a65v902orivcti28c8qe.png" mode="responsive" height="1284" width="2283" %}
{% /image %}

## Choosing the Right Via Configuration

Choosing the right via configuration depends on the board's design requirements. Blind vias are ideal for saving surface space, while buried vias are used to interconnect inner layers without disturbing the outer layers. Microvias enable higher density in compact designs. Designs often times have a combination of all the mentioned type of vias.

If you need help figuring out what type of vias are right for your design, you can try asking [Flux. ](https://docs.flux.ai/flux/reference/copilot)

```none
@flux I'm trying to design [add project description], can you tell me what kind of stackup would I need? Also estimate what kind of vias will be required.
```




### Configure your Vias

Once you've chosen the type of vias you want to use in your design, you'll need to get your stackup configured. **Flux's implementation of vias makes sure that, as soon as your stackup is setup, the right via type will be automatically selected during routing.** You can learn more about smart vias [here.](https://docs.flux.ai/flux/reference/vias#smart-vias)

We've created a few templates for some well-known manufacturers to help you get started. To use one of the templates below, open the desired template and [clone it](https://docs.flux.ai/flux/reference/reference-forking-cloning#cloning):

- PCBWay: [4-layer](https://www.flux.ai/jharwinbarrozo/pcbway-4-layer-hdi-stackup-template) and [6-layer](https://www.flux.ai/jharwinbarrozo/pcbway-6-layer-hdi-stackup-template) HDI stackup template
- VictoryPCB: [4-layer](https://www.flux.ai/jharwinbarrozo/victorpcb-4-layer-hdi-stackup-template) and [6-layer](https://www.flux.ai/jharwinbarrozo/victorypcb-6-layer-hdi-stackup-template) HDI stackup template
- Seeed Studio: [4-layer](https://www.flux.ai/seeedstudio/seeed-studio-4-layer-stackup) HDI stackup template


#### Manual Via Configuration

You can also create your own custom via configuration using our stackup editor. [Learn how to configure vias.](https://docs.flux.ai/flux/reference/vias#via-configuration)

{% image url="https://uploads.developerhub.io/prod/86Yw/bi6hssijippfsgcke6xsvwy0hsr87ztp0efuisl1f5m5a65v902orivcti28c8qe.png" mode="600" height="1284" width="2283" %}
{% /image %}

## How Vias Work in Flux

Traditionally, designers need to choose the appropriate via type on each connection. However, managing these connections, especially in multi-layered boards, can be cumbersome and error-prone. Flux alleviates this by dynamically computing the optimal via configurations and applying them as needed.

Consider the following scenario: You want to connect a trace from **mid-layer 2** to **top copper**. With Flux's Smart Vias, you don’t need to place and configure each via manually. Instead, you simply select the start and end layers, and Flux handles the rest, placing the necessary vias and adjusting the layout automatically. This feature significantly reduces manual effort and the risk of errors in complex multi-layer designs.

{% image url="https://uploads.developerhub.io/prod/86Yw/yowgvecjxg2xmcmytbensnp0q9745r09z20fc0ymknpqdwubqqpszjef242femh6.gif" mode="responsive" height="1080" width="1920" %}
{% /image %}

### Adding  Vias During Routing

In Flux, there are two main ways of placing a via while [routing, ](https://docs.flux.ai/flux/tutorials/routing-tutorial):

- **Place via menu:** right click and select the target layer from the menu.
- **Pressing  the `V` key:**  This action cycles through the different layers in your PCB stack-up. Each press of the key drops the trace to the next layer using the appropriate via type based on the current configuration.
    - For instance, pressing 'V' once might drop the trace from **top copper** to **mid-layer 1** using a microvia. Pressing 'V' again could drop it further to **mid-layer 2** using a buried via.

- **Note:** for these two menus to work you'll need to be laying out a trace.

{% image url="https://uploads.developerhub.io/prod/86Yw/dhssj30zejch1mjpuzgxjmuq98hqt8suhmvcg7ljou2oq7vqvazjw5zu431nstmc.gif" mode="600" height="480" width="832" %}
{% /image %}

### Changing the default Via Configuration

Flux also provides users with the flexibility to manually configure via options if needed. This can be done through the via configuration toolbar, where you can prioritize or remove specific via types based on your design requirements.

{% image url="https://uploads.developerhub.io/prod/86Yw/2769kgo3bz8gu12a9s4reb8fppxg52ub8wf9kqd8ucld9uzri49ge6bnycjn4s9k.png" mode="600" height="1496" width="2660" %}
{% /image %}

The via configuration toolbar in Flux is a powerful tool for managing your via settings. Here’s how you can use it:

1. **Access the Toolbar:** To access the via configuration toolbar, click an existing via.
2. **Prioritize or Deselect Vias:** In scenarios where multiple via types can achieve the same connection, you can prioritize one over the others. For example, you might choose to prioritize a stacked microvia over a blind via for a specific connection. If you remove certain via types from the options, Flux will automatically use the next available type based on your prioritization.
3. **Dynamic Updates:** When you make changes to the via configuration, such as removing a certain via type, the Smart Via children are updated in real time. This ensures that your design always reflects the most current configuration settings.

{% image url="https://uploads.developerhub.io/prod/86Yw/dzrczpup83z7lhf23fmf60a09c3li3yhxjg5ztm6fg5ysmpcnsjcxfj8bdn5ys51.gif" mode="responsive" height="1080" width="1920" %}
{% /image %}


#### Advanced Smart Via Configuration

Flux's new via capabilities also include advanced layout rules that offer more control over via placement and behavior. These rules include:

- **Keep-Out Rule:** This rule dictates the minimum hole-to-hole distance between vias. The default is set to 250 microns, but you can adjust this value to meet specific design needs. Increasing this distance can prevent overcrowding of vias, while reducing it allows for a more tightly packed layout.
- **Rotation Rule:** This rule controls the angle of staggered via configurations. By default, Smart Vias are automatically rotated to 90 degrees, but this can be changed to other angles, such as 180 degrees, depending on your design requirements.

You can find more information about advanced configurations on [this page.](https://docs.flux.ai/flux/reference/vias)
