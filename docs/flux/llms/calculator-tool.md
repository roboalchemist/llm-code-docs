# Source: https://docs.flux.ai/reference/calculator-tool.md

# Flux Calculator Tool



Flux includes a powerful calculator tool that allows you to evaluate mathematical expressions and perform engineering calculations directly from the chat interface. This tool helps you quickly solve equations without having to switch to a separate calculator application.

## Overview

The calculator tool enables you to:

- Evaluate mathematical expressions of varying complexity
- Perform engineering calculations relevant to circuit design
- Work with arrays and matrices for more complex operations
- Get results in a clear, formatted output
- Extract and evaluate equations from datasheets

{% image url="https://uploads.developerhub.io/prod/86Yw/8egbatttvuz30sktni1d9oonrtgodjhdc5zrwrnnpt0syx5gll36z725ibi357ym.gif" mode="600" height="720" width="1280" %}
{% /image %}

## How to Use the Calculator Tool

To evaluate mathematical expressions using Flux, use the `@calculator` tool in your query:

```none
@calculator 2.2k * 0.01

@calculator 3.3V / 220ohm

@calculator sin(45 deg) * 5V
```




When you use the `@calculator` tool, Flux will:

1. Parse the mathematical expression
2. Check for any undefined variables or functions
3. Evaluate the expression using the mathjs library
4. Return the result in a formatted output

## Supported Operations

The calculator tool supports a wide range of mathematical operations:

### Basic Arithmetic

- Addition, subtraction, multiplication, division
- Exponentiation and square roots
- Modulo and integer division

### Trigonometric Functions

- Sine, cosine, tangent (and their inverses)
- Support for both radians and degrees (using `deg` suffix)

### Logarithmic and Exponential Functions

- Natural logarithm (ln) and base-10 logarithm (log10)
- Exponential function (exp)

### Engineering Functions

- Unit conversions (e.g., ohms to kilohms)
- Engineering notation (e.g., 1k = 1000)
- Complex number operations

### Matrix and Array Operations

- Matrix creation and manipulation
- Vector operations
- Array indexing and slicing

## Example Calculations

Here are some examples of how you can use the calculator tool:

### Circuit Calculations

```none
@calculator 5V / 1k  # Calculate current through a resistor

@calculator 0.5 * 3.3V  # Calculate voltage divider output

@calculator 1/(1/(10k) + 1/(22k))  # Calculate parallel resistance
```




### Power and Energy Calculations

```none
@calculator 12V * 0.5A  # Calculate power

@calculator 3.7V * 2000mAh / 1000  # Calculate energy in watt-hours

@calculator 5V^2 / 100ohm  # Calculate power using V²/R
```




### Timing and Frequency Calculations

```none
@calculator 1 / (2 * pi * 10k * 0.1uF)  # Calculate RC filter cutoff frequency

@calculator 1 / (2 * 10k * 1nF)  # Calculate time constant

@calculator 1 / 50MHz  # Calculate period from frequency
```




## Result Formatting

The calculator tool formats results based on the type of calculation:

### Scalar Values

Simple numerical results are displayed with appropriate precision and units when applicable.

### Arrays and Vectors

One-dimensional arrays are displayed in a tabular format with index and value columns.

### Matrices

Two-dimensional arrays (matrices) are displayed in a tabular format with row indices and values.

### Complex Numbers

Complex numbers are displayed in the form `a + bi` where `a` is the real part and `b` is the imaginary part.

## Tips for Effective Calculations

To get the most out of the calculator tool:

1. **Use engineering notation** - You can use suffixes like k, M, m, u, n, p (e.g., 10k for 10,000 or 1u for 0.000001).

2. **Include units for clarity** - While not required for calculation, adding units like V, A, or ohm helps with readability.

3. **Use parentheses for complex expressions** - Ensure correct order of operations by using parentheses in complex expressions.

4. **Break down complex calculations** - For very complex calculations, consider breaking them into smaller steps.

## Extracting Equations from Datasheets

A powerful feature of the calculator tool is its ability to extract and evaluate equations from datasheets:

1. Attach a datasheet to your chat
2. Use the `@calculator` tool to reference an equation in the datasheet
3. Provide the values for the variables in the equation

For example:

```none
@calculator From the attached datasheet, calculate the output voltage using the equation in Figure 3 with R1=10k and R2=5k
```




## Limitations

While the calculator tool is powerful, it has some limitations to be aware of:

- The tool cannot evaluate expressions with undefined variables
- Very complex mathematical operations might require breaking down into simpler steps
- The tool does not support solving equations (finding x where f(x) = 0)
- Some specialized engineering functions might not be available
- The tool does not maintain state between calculations

## Related Features

The calculator tool works well with other Flux capabilities:

- [Flux Help Tool](https://docs.flux.ai/flux/reference/help-tool) - Search Flux Editor documentation for guidance
- [Flux File Tool](https://docs.flux.ai/flux/reference/file-tool) - Extract information from datasheets
- [Flux Code Tool](https://docs.flux.ai/flux/reference/code-tool) - Generate Python scripts for more complex calculations
- [Flux Simulator Tool](https://docs.flux.ai/flux/reference/simulator-tool) - Run SPICE circuit simulations
- [Getting Started With Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Learn the basics of using Flux
