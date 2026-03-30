# Source: https://docs.flux.ai/reference/code-tool.md

# Flux Code Tool

Flux includes a powerful code tool that allows you to generate and execute Python scripts for data analysis, visualization, and complex calculations directly from the chat interface. This tool helps you perform advanced operations that go beyond simple calculations without having to set up a separate programming environment.

## Overview

The code tool enables you to:

- Generate and execute Python code based on natural language descriptions
- Create visualizations such as graphs, charts, and plots
- Perform complex data analysis and calculations
- Simulate circuit behavior and analyze results
- Generate reports with formatted output

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/xhq56dgleggpry6kwp0mrb8taegx3whhbkr16ajb7ix0ag6nptbmfokd30nuuny9.png)

## How to Use the Code Tool

To generate and execute Python code using Flux, use the `@code` tool in your query:

```none
@code Create a plot of a sine wave with frequency 1kHz sampled at 10kHz for 10ms

@code Calculate the frequency response of an RC low-pass filter with R=10k and C=0.1uF
```



When you use the `@code` tool, Flux will:

1. Generate Python code based on your description
2. Execute the code using a secure Python interpreter
3. Return the results, including any text output, tables, or visualizations
4. Provide the generated code for your reference

## Python Libraries

The code tool has access to many popular Python libraries for scientific computing and visualization:

### Data Analysis and Computation

- NumPy - For numerical computations and array operations
- SciPy - For scientific and technical computing
- Pandas - For data manipulation and analysis
- SymPy - For symbolic mathematics

### Visualization

- Matplotlib - For creating static, animated, and interactive visualizations
- Seaborn - For statistical data visualization
- Plotly - For interactive, publication-quality graphs

### Electronics and Signal Processing

- PySpice - For circuit simulation
- SciPy Signal - For signal processing functions

## Example Use Cases

Here are some examples of how you can use the code tool:

### Circuit Analysis and Simulation

```none
@code Simulate a voltage divider with R1=10k and R2=5k with an input of 5V

@code Plot the frequency response of a second-order Butterworth filter with a cutoff frequency of 1kHz

@code Calculate the step response of an RLC circuit with R=100 ohm, L=1mH, and C=10uF
```



### Data Visualization

```none
@code Create a bar chart comparing the power consumption of different microcontrollers

@code Generate a scatter plot of voltage vs. current measurements with a trend line

@code Create a heatmap showing the temperature distribution on a PCB
```



### Complex Calculations

```none
@code Calculate the optimal values for a PID controller given a step response

@code Perform Monte Carlo analysis on a circuit with component tolerances

@code Solve the differential equation for an RC charging circuit
```



## Working with Data

The code tool can work with data from various sources:

### Manual Input

You can provide data directly in your query:

```none
@code Plot the following voltage measurements: [3.3, 3.28, 3.31, 3.29, 3.32, 3.27]
```



### Attached Files

You can attach data files (CSV, TXT, etc.) to your chat and reference them:

```none
@code Analyze the temperature data in the attached CSV file and create a line chart with a 7-day moving average
```



### Generated Data

You can ask the code tool to generate synthetic data for analysis:

```none
@code Generate a noisy sine wave and apply a low-pass filter to clean it up
```



## Output Formats

The code tool can generate various types of output:

### Text Output

Simple text results for basic calculations and analysis.

### Tables

Structured data presented in tabular format for easy reading.

### Visualizations

Graphs, charts, and plots rendered as images in the chat.

### Interactive Elements

Some visualizations may include interactive elements for exploring data.

## Tips for Effective Code Generation

To get the most out of the code tool:

1. **Be specific about your requirements** - Clearly describe what you want the code to do, including any specific parameters or methods.
2. **Specify visualization details** - Mention axis labels, titles, and other formatting preferences for charts and graphs.
3. **Break complex tasks into steps** - For very complex analyses, consider breaking them into a sequence of simpler steps.
4. **Reference specific libraries if needed** - If you know you want to use a particular library or function, mention it in your query.

## Limitations

While the code tool is powerful, it has some limitations to be aware of:

- Execution time is limited, so very complex computations may time out
- Available memory is restricted, limiting the size of datasets that can be processed
- Not all Python libraries are available in the execution environment
- The tool cannot access external resources like websites or databases
- Generated code runs in a sandboxed environment for security reasons

## Related Features

The code tool works well with other Flux capabilities:

- [Help Tool](https://docs.flux.ai/flux/reference/help-tool) - Search Flux Editor documentation for guidance
- [File Tool](https://docs.flux.ai/flux/reference/file-tool) - Extract information from datasheets
- [Calculator Tool](https://docs.flux.ai/flux/reference/calculator-tool) - Perform simpler calculations
- [Simulator Tool](https://docs.flux.ai/flux/reference/simulator-tool) - Run SPICE circuit simulations
- [Getting Started With Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Learn the basics of using Flux