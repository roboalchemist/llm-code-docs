# Source: https://docs.flux.ai/tutorials/start-to-finish-tutorial---schematics.md

# Buck Converter Tutorial: Creating the Schematic for Power Regulation


Design a reliable buck converter schematic based on the LM2596 IC, with guidance on component selection and circuit operation.

## Overview

To make our converter suitable for a variety of projects, we'll follow the **"typical application"** provided by Texas Instruments for the LM2596. This ensures that our design is versatile and reliable across different use cases.

{% image url="https://uploads.developerhub.io/prod/86Yw/oqlkgumnafks3ka9ywbguoncjvap3vjvjq12u04b1fw11vvtsl9kubqj430zmv0d.png" mode="responsive" height="1100" width="1956" %}
{% /image %}

## Getting Started

The typical application section of the [datasheet](https://www.ti.com/lit/ds/symlink/lm2596.pdf?ts=1729686808422&amp;ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FLM2596) requires a few parameters to be set, in our case:

- **Adjustable Version**: We're using an adjustable version of the LM2596, which requires a voltage divider at PIN 4 to set the output voltage.
- **ON/OFF Control**: The ON/OFF pin is left as an input, allowing external control to enable or disable the converter.

## Schematic Overview

Here, [we've put together the schematic in Flux](https://www.flux.ai/vasy_skral/lm2596-buck-converter-5v?editor=schematic) for our buck converter. Two points of note:

1. There is a voltage divider required at PIN4 because we are using an adjustable version of the LM2596, not a version with a fixed 5V output.
2. The ON/OFF pin is left as an input so the converter can be turned on/off with an external circuit. The ON/OFF pin, is actually a terminal which allows the module to be converted to a [module](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts). More about this in the sub-section below:

{% image url="https://uploads.developerhub.io/prod/86Yw/rr7tv3y5c3v22u3hymf5613gfi1m5yb8hah78bs92qj2fov3nz245m60qftpgzck.png" mode="600" height="830" width="600" %}
{% /image %}

### Working with Flux

Flux can assist in refining and understanding your schematic. Here are some examples of how Flux can help:

- **@Flux: Component Functions in the Schematic**
    - Ask Flux to explain each component's role, especially if you need clarification on a specific part.
    - `@Flux: Can you explain each component's function in the schematic?`

{% image url="https://uploads.developerhub.io/prod/86Yw/inatuxic1jk714vxawgrk8oiwao6466zfpin7w2uxd5qs46g1gxjnemaneb7r7yb.png" mode="responsive" height="660" width="500" %}
{% /image %}

- **@Flux: Buck Converter Explanation**
    - Flux can walk you through how the buck converter works in the context of your schematic, ensuring you're on track with your design.
    - `@Flux: Can you explain how this all works in the context of a buck converter?`

{% image url="https://uploads.developerhub.io/prod/86Yw/gq0zpa8u549g9t7ahkps7xv5955b2lpp3c512d035gt4jg98aio8ia2lgg78vrhc.png" mode="responsive" height="440" width="504" %}
{% /image %}

### Working with Flux's Modules

Modules allow you to **reuse layout sections and drop in fully functional blocks** into your design. A module is a block containing a complete design section, including parts, traces, vias, etc. These **blocks can then be placed into existing projects to reuse** previous designs with minimal effort. This idea of PCB layout reuse is a great way to help designers build things faster.

In our case, we can **convert this project into a module for easy reuse** in any of our future projects. All we have to do is find it in our parts library, and drag it into our project for future reuse.


#### Convert a Project to a Module

In a standard PCB layout, terminals are an optional feature, but in a module, they are mandatory for functionality. This is because the terminals are used to connect the module to other components once the module is placed in a project.

To delve into a more comprehensive explanation of creating modules, please refer to [detailed page on the subject](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts). The key aspects of this process have been concisely outlined below.

1. Create the circuit you want to make a module out of
2. Add terminals to establish the connections
3. Connect the terminals' pads in the PCB editor
4. Add a designator prefix
5. Publish the module

## Component Selection Guidelines

When implementing the LM2596 schematic, careful component selection is crucial:

### Input Capacitor (C1)

- Use a low ESR capacitor rated for at least 1.5x your input voltage
- Aluminum electrolytic capacitors work well for most applications
- Place as close as possible to the VIN pin

### Output Capacitor (C2)

- Low ESR is critical for stable operation
- Minimum capacitance of 220μF is recommended
- Higher capacitance improves transient response

### Catch Diode (D1)

- Use a Schottky diode with a current rating of at least 1.5x the maximum load current
- Voltage rating should exceed the maximum input voltage
- Fast recovery time is essential for efficient operation

### Inductor (L1)

- Select based on the current requirements and desired ripple current
- Higher inductance values reduce ripple but may limit maximum current
- Ensure the saturation current rating exceeds the peak current

### Feedback Resistors (R1, R2)

- Use 1% tolerance resistors for accurate output voltage
- Calculate values using the formula: Vout = 1.23V × (1 + R1/R2)
- Keep resistor values reasonably high to minimize power consumption

## Troubleshooting Common Issues

### Unstable Output Voltage

- Check feedback resistor values and connections
- Verify that the output capacitor meets minimum requirements
- Ensure proper grounding and short connections

### Excessive Noise or Ripple

- Add additional input/output filtering
- Check inductor selection and placement
- Verify that the catch diode has fast recovery characteristics

### Overheating Components

- Verify that components are properly rated for the application
- Check for proper thermal management in the PCB layout
- Ensure the IC is not operating beyond its recommended duty cycle

## What's Next

Now that you've completed the schematic design for your buck converter, you're ready to move on to:

- [PCB Layout](https://docs.flux.ai/flux/tutorials/start-to-finish-tutorial---pcb-layout) - Learn how to create an efficient PCB layout for your buck converter
- [Testing and Validation](/tutorials/testing-and-validation) - Discover techniques for testing your completed buck converter
- [Advanced Buck Converter Designs](/tutorials/advanced-buck-converter) - Explore more sophisticated power regulation circuits

By following this guide, you've created a solid foundation for your power regulation circuit that can be easily adapted for various projects.
