# Source: https://docs.flux.ai/tutorials/generative-ai-use-cases.md

# Generative AI for PCB Design with Flux


Flux doesn't just assist—it takes action. These use cases showcase how Flux can modify your design, place components, wire connections, and optimize your schematic with simple commands.




## Overview

Generative AI is a step beyond traditional AI assistance—it doesn't just provide information, it actively modifies your design. Instead of manually searching for components, adjusting schematics, or wiring connections, Flux automates these steps with simple commands.

These use cases eliminate tedious manual work, allowing you to focus on the design itself instead of repetitive tasks.

You can follow along with these examples in [this project](https://www.flux.ai/nico/generative-ai-example) to see how Flux takes action.

## 1- Find and Add Parts to Your Project

### Overview

Starting a new hardware project can be overwhelming. Even if you know what you want to build, choosing the right components and structuring a schematic takes time. Flux simplifies this by:

- **Brainstorming your project requirements** – Ask Flux what components you'll need based on your design goals.
- **Selecting components intelligently** – Flux chooses ICs, sensors, and passives that work well together.
- **Automatically placing components** – Once confirmed, Flux adds them directly to your schematic.

{% image url="[https://uploads.developerhub.io/prod/86Yw/rk15o4pkgv1cj0ghrr0haawfq3xz7kq60t4pzj76gbknvsqyc1ge2kcoa6p5m33a.gif"](https://uploads.developerhub.io/prod/86Yw/rk15o4pkgv1cj0ghrr0haawfq3xz7kq60t4pzj76gbknvsqyc1ge2kcoa6p5m33a.gif&quot;) caption="" mode="full" height="720" width="1280" %}
{% /image %}

### How It Works


#### 1. Define Your Project

You can start with a simple description:

`I want to build a sensor module with an ESP32.`

👉 Flux will ask follow-up questions to refine the design. For example:

```none
Which sensors do you want to use with the ESP32?

- BME280 (temperature, humidity, pressure)
- MPU6050 (motion tracking)
- BH1750 (ambient light)
```




You can specify your choice:

`Use a BME280.`


#### 2. Generate a Bill of Materials (BoM)

`Define a BOM with MPNs that you can find in the @library.`

👉 Flux generates a component list, including:

```none
- ESP32-WROOM-32 (Microcontroller)
- BME280 (Sensor)
- 10kΩ resistors (I²C pull-ups)
- 0.1µF capacitor (Decoupling)
```





#### 3. Place the Components in Your Schematic

`Begin designing the schematic by adding the ESP32 and BME280 components.`

👉 Flux places the parts directly into your schematic.

## 2- Automatically Add Decoupling Capacitors

### Overview

Decoupling capacitors stabilize power delivery to ICs, preventing noise and voltage fluctuations. Instead of manually checking datasheets and placing components, Flux:

- **Identifies which components need decoupling**
- **Suggests capacitor values based on best practices**
- **Places the capacitors in the correct positions**

### How It Works


#### 1. Request Decoupling Capacitors

`List all the decoupling capacitors that are needed for this design.`

👉 Flux generates recommendations, such as:

```none
- 0.1µF capacitor near ESP32's power pin
- 10µF capacitor for ESP32's bulk power smoothing
- 0.1µF capacitor near the BME280 sensor
```





#### 2. Place Decoupling Capacitors

`Place them from the @library.`

👉 Flux selects and adds the appropriate capacitors to your schematic.


#### 3. Assign Correct Values

`Now add the values needed for each capacitor.`

👉 Flux assigns the correct capacitance values to each placed component.

## 3- Swap out a Component with an Alternative

### Overview

Sometimes, a component needs to be replaced due to availability, cost, or performance. Instead of searching manually, Flux can:

- **Find a suitable replacement** based on your criteria.
- **Automatically swap out the part** while preserving circuit integrity.

### How It Works


#### 1. Request a Replacement Component

`Find me a replacement for @U2 in the @library that has better resolution.`

👉 Flux suggests an alternative:

```none
BME680 (higher resolution and additional gas sensing compared to BME280)
```





#### 2. Replace the Component

`Proceed to replace @U2 with the BME680 sensor in the schematic.`

👉 Flux removes the BME280 and adds the BME680 in its place.

## 4- Wire Components

### Overview

Once components are placed, manually wiring them together takes time and requires careful checking of pin assignments and electrical best practices. Flux automates this by:

- **Identifying the correct connections between components.**
- **Routing signals based on best practices.**
- **Following schematic standards for net naming.**

### How It Works


#### 1. Request a Connection

`Can you connect @U1 with @U3?`

👉 Flux identifies that U1 (ESP32) and U3 (BME680) need an I²C connection and wires them accordingly.

👉 Flux adds the correct wiring and connections directly in the schematic.

## Best Practices for Generative AI in PCB Design

1. **Start with clear requirements**: The more specific your initial description, the better Flux can assist
2. **Review generated components**: Always verify that the components Flux selects meet your specific needs
3. **Use component references**: When referring to components, use the @ symbol followed by the designator (e.g., @U1)
4. **Combine manual and AI work**: Use Flux for repetitive tasks while focusing your attention on critical design decisions
5. **Verify critical connections**: While Flux is highly accurate, always review critical connections for safety and functionality

## Troubleshooting Common Issues

### Component Not Found

- Check that you're using the correct component name or designator
- Try providing more specific details about the component you need
- Verify that the component exists in the Flux library

### Incorrect Connections

- Be more specific about which pins should be connected
- Provide additional context about the connection type (I²C, SPI, etc.)
- Review the datasheet for both components to ensure compatibility

### Placement Issues

- If components are placed poorly, try specifying locations in your request
- For complex layouts, consider placing critical components manually first
- Use Flux to organize components by function or signal type

## What's Next

Now that you've learned how to use Flux's generative AI capabilities, you might want to explore:

- [AI Architecture Design](/tutorials/copilot-use-cases/ai-architecture-design) - Learn how to use Flux to develop system architectures
- [AI Component Research](/tutorials/copilot-use-cases/ai-component-research) - Discover how Flux can help with component selection
- [Auto Layout](/tutorials/copilot-use-cases/auto-layout) - See how Flux can assist with PCB layout optimization
- [AI Testing and Debugging](/tutorials/copilot-use-cases/ai-testing-debugging) - Learn how Flux can help troubleshoot design issues
