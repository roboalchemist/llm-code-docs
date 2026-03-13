# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/util/ProjectGenerator.md

# [ProjectGenerator](https://bryntum.com/docs/gantt/api/Gantt/util/ProjectGenerator)

A utility class which generates sample project data for Examples and Tests.

Example:

```
const result = await ProjectGenerator.generateAsync(1000, 50);
// result contains { startDate, endDate, tasks, dependencies }
```

## Functions

Functions are methods available for calling on the class

[generateAsync](https://bryntum.com/docs/gantt/api/Gantt/util/ProjectGenerator#function-generateAsync-static)
Generates project data asynchronously with the specified number of tasks.

[generateBlocks](https://bryntum.com/docs/gantt/api/Gantt/util/ProjectGenerator#function-generateBlocks-static)
Generator function that yields blocks of tasks and dependencies.

## Typedefs

Typedefs are type definitions for the class

[ProjectGeneratorResult](https://bryntum.com/docs/gantt/api/Gantt/util/ProjectGenerator#typedef-ProjectGeneratorResult)
Configuration object returned by ProjectGenerator.generateAsync
