# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/CriticalPaths.md

# [CriticalPaths](https://bryntum.com/docs/gantt/api/Gantt/feature/CriticalPaths)

This feature highlights the project _critical paths_. Every task is important, but only some of them are critical. The critical path is a chain of linked tasks that directly affects the project finish date. If any task on the critical path is late, the whole project is late.

For more details on the _critical path method_ please check [this article](https://bryntum.com/docs/gantt/api/https://en.wikipedia.org/wiki/Critical_path_method).

This feature is loaded by default, but the visualization needs to be enabled:

```
// let's visualize the project critical paths
gantt.features.criticalPaths.disabled = false;
```

If you need to get information about critical paths, you can refer to [criticalPaths](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-criticalPaths) property of the project:

```
const paths = gantt.project.criticalPaths;
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[highlightCriticalRows](https://bryntum.com/docs/gantt/api/Gantt/feature/CriticalPaths#config-highlightCriticalRows)
Set this to `true` to add `b-critical` cls to grid rows to highlight critical tasks

To enable it:

```
new Gantt({
  features : {
    criticalPaths : {
        disabled              : false,
        highlightCriticalRows : true
    }
  }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCriticalPaths](https://bryntum.com/docs/gantt/api/Gantt/feature/CriticalPaths#property-isCriticalPaths)
Identifies an object as an instance of [CriticalPaths](https://bryntum.com/docs/gantt/api/#Gantt/feature/CriticalPaths) class, or subclass thereof.

[isCriticalPaths](https://bryntum.com/docs/gantt/api/Gantt/feature/CriticalPaths#property-isCriticalPaths-static)
Identifies an object as an instance of [CriticalPaths](https://bryntum.com/docs/gantt/api/#Gantt/feature/CriticalPaths) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[criticalPathsHighlighted](https://bryntum.com/docs/gantt/api/Gantt/feature/CriticalPaths#event-criticalPathsHighlighted)
Fired when critical paths get highlighted.

See also: [criticalPathsUnhighlighted](https://bryntum.com/docs/gantt/api/#Gantt/feature/CriticalPaths#event-criticalPathsUnhighlighted)

[criticalPathsUnhighlighted](https://bryntum.com/docs/gantt/api/Gantt/feature/CriticalPaths#event-criticalPathsUnhighlighted)
Fired when critical paths get hidden.

See also: [criticalPathsHighlighted](https://bryntum.com/docs/gantt/api/#Gantt/feature/CriticalPaths#event-criticalPathsHighlighted)
