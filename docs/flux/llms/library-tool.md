# Source: https://docs.flux.ai/reference/library-tool.md

# Flux Library Tool

Flux includes a powerful library tool that allows you to search for electronic components and find the right parts for your designs directly from the chat interface. This tool helps you quickly locate components based on your requirements without having to manually browse through component catalogs.

## Overview

The library tool enables you to:

- Search the Flux component library using natural language queries
- Find components based on specific parameters or requirements
- Get detailed information about components including specifications and availability
- Compare similar components to make informed selection decisions
- Add components directly to your design from the search results

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/a3dq960hlox3u9umlri7fvn38jiw2h0bwrjgyn1o13s66w3runoejpg49h8wx2dx.png)

## How to Use the Library Tool

To search for components using Flux, use the `@library` tool in your query:

```none
@library Find a 10uF ceramic capacitor rated for 50V

@library I need a low-power microcontroller with I2C and SPI interfaces
```



When you use the `@library` tool, Flux will:

1. Process your query to understand your component requirements
2. Search the Flux component library for matching parts
3. Return a list of relevant components with key specifications
4. Provide links to add components directly to your design

## Search Capabilities

The library tool uses advanced natural language processing to understand your component requirements, even when they're expressed in conversational terms. You can search for components based on:

### Electrical Specifications

- Voltage ratings
- Current capabilities
- Power ratings
- Frequency ranges
- Resistance/capacitance values

### Physical Characteristics

- Package types
- Dimensions
- Mounting styles (SMD, through-hole)
- Temperature ranges

### Functional Requirements

- Communication interfaces (I2C, SPI, UART)
- Special features (low power, high speed)
- Application-specific needs

## Example Queries

Here are some examples of how you can use the library tool:

### Finding Passive Components

```none
@library Find a 0.1uF bypass capacitor in 0603 package

@library I need a 10k resistor with 1% tolerance that can handle at least 0.25W

@library Show me ferrite beads suitable for USB power filtering
```



### Searching for ICs

```none
@library Find a low-power microcontroller with Bluetooth capabilities

@library I need a voltage regulator that can output 3.3V at 1A

@library Show me op-amps with rail-to-rail output and low noise
```



### Finding Connectors and Mechanical Parts

```none
@library Find a 2x5 pin header with 2.54mm pitch

@library I need a USB Type-C connector for a PCB

@library Show me SMD tactile switches with a low profile
```



## Search Results Format

When Flux returns search results, they are presented in a structured format that includes:

- Component name and manufacturer
- Key specifications relevant to your query
- Package information
- Availability status
- Links to add the component to your design

If multiple relevant components are found, Flux will organize them by relevance and present them in a clear, readable format.

## Tips for Effective Library Searches

To get the most out of the library tool:

1. **Be specific about key parameters** - Include important specifications like voltage ratings, package sizes, or interface requirements.
2. **Mention application context** - Describing how you plan to use the component can help Flux find more suitable matches.
3. **Use technical terminology** - Using industry-standard terms will help Flux understand your requirements better.
4. **Refine your search if needed** - If the initial results don't meet your needs, try a more specific query with additional parameters.

## Adding Components to Your Design

When you find a suitable component in the search results, you can add it directly to your design by:

1. Clicking on the "Add to Design" link in the search results
2. Selecting the appropriate schematic symbol if multiple options are available
3. Placing the component in your schematic

## Related Features

The library tool works well with other Flux capabilities:

- [Flux Help Tool](https://docs.flux.ai/flux/reference/help-tool) - Search Flux Editor documentation for guidance
- [Flux File Tool](https://docs.flux.ai/flux/reference/file-tool) - Extract information from datasheets
- [Flux Calculator Tool](https://docs.flux.ai/flux/reference/calculator-tool) - Extract and evaluate equations
- [Getting Started With Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Learn the basics of using Flux