# Source: https://docs.flux.ai/tutorials/toolbar.md

# Using the Toolbar in Flux PCB Editor

The toolbar is a context-aware interface that appears automatically when you select a node in the PCB editor. It provides a quick and intuitive way to modify layout properties of the selected node without having to navigate through menus or set up manual layout rules.

![](https://uploads.developerhub.io/prod/86Yw/8yy47zfzhs74kuahqmls23j295cjgh7rn2ambx988ixwwymj12kjwg1r9xq945wu.png)

## Accessing the Toolbar

To access the toolbar:

1. Open your PCB design in the PCB editor
2. Select any object in your PCB layout (such as the layout itself, a footprint, trace, via, etc.)
3. The toolbar will automatically appear near the selected object
4. The available options in the toolbar will change based on the type of object you've selected

## Available Properties

The toolbar dynamically adjusts the available options based on the type of node you've selected. Here are some of the properties you can modify using the toolbar:

### Layout Properties

- Size - change the layout dimensions
- Corner Radius - adjust the roundness of layout corners
- Board Shape - switch between rectangular and circular board shapes

### Component Properties

- Position - adjust X, Y coordinates
- Rotation - rotate components on the board
- Size - scale component dimensions

### Trace Properties

- Position - adjust trace location
- Trace Width - modify trace thickness
- Rotation - rotate trace segments

### Via Properties

- Position - adjust via location
- Hole Size - modify via hole diameter
- Via Options - configure via types and connections

### Text Properties

- Position - adjust text location
- Font Size - change text size
- Rotation - rotate text elements

## Advantages Over Manual Rule Setup

The toolbar offers several advantages over the traditional manual rule setup:

- **Immediate Access**: No need to navigate through menus or panels
- **Context-Aware**: Only shows relevant options for the selected object
- **Real-Time Updates**: See changes immediately as you adjust properties
- **Efficient Workflow**: Make multiple adjustments quickly without switching contexts

For more complex rule configurations or rules that need to apply to multiple objects simultaneously, you may still need to use the [selector-based layout rules](/reference/pcb-rules/pcb-layout-rule-selectors).