# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/view/orientation/NewTaskRendering.md

# [NewTaskRendering](https://bryntum.com/docs/gantt/api/Gantt/view/orientation/NewTaskRendering)

Handles rendering of tasks, using the following strategy:

1. When a row is rendered, it collects a DOM config for its task bar and stores in a map (row -> config)
2. When a rendering pass is done, it syncs the DOM configs from the map to DOM

The need for caching with this approach is minimal, only the map needs to be kept up to date with available rows.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isNewTaskRendering](https://bryntum.com/docs/gantt/api/Gantt/view/orientation/NewTaskRendering#property-isNewTaskRendering)
Identifies an object as an instance of [NewTaskRendering](https://bryntum.com/docs/gantt/api/#Gantt/view/orientation/NewTaskRendering) class, or subclass thereof.

[isNewTaskRendering](https://bryntum.com/docs/gantt/api/Gantt/view/orientation/NewTaskRendering#property-isNewTaskRendering-static)
Identifies an object as an instance of [NewTaskRendering](https://bryntum.com/docs/gantt/api/#Gantt/view/orientation/NewTaskRendering) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getConnectorStartSide](https://bryntum.com/docs/gantt/api/Gantt/view/orientation/NewTaskRendering#function-getConnectorStartSide)
Gets displaying item start side

[getConnectorEndSide](https://bryntum.com/docs/gantt/api/Gantt/view/orientation/NewTaskRendering#function-getConnectorEndSide)
Gets displaying item end side
