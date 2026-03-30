# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/Dependencies.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/Dependencies.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/Dependencies.md

# [Dependencies](https://bryntum.com/docs/gantt/api/Gantt/feature/Dependencies)

This feature draws dependencies between tasks. Uses a dependency [store](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-dependencyStore) to determine which dependencies to draw.

To customize the dependency tooltip, you can provide the [tooltip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Dependencies#config-tooltip) config and specify a [getHtml](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-getHtml) function. For example:

```
const gantt = new Gantt({
    features : {
        dependencies : {
            tooltip : {
                getHtml({ activeTarget }) {
                    const dependencyModel = gantt.resolveDependencyRecord(activeTarget);

                    if (!dependencyModel) return null;

                    const { fromEvent, toEvent } = dependencyModel;

                    return `${fromEvent.name} (${fromEvent.id}) -> ${toEvent.name} (${toEvent.id})`;
                }
            }
        }
    }
}
```

Styling all dependency lines
----------------------------

You can easily customize the arrows drawn between events. To change all arrows, apply the following basic SVG CSS:

```
.b-sch-dependency {
   stroke-width: 2;
   stroke : red;
}

.b-sch-dependency-arrow {
    fill: red;
}
```

Styling individual dependency lines
-----------------------------------

To style an individual dependency line, you can provide a [cls](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyModel#field-cls) in your data:

```
{
    "id"   : 9,
    "from" : 7,
    "to"   : 8,
    "cls"  : "special-dependency"
}
```

```
// Make line dashed
.b-sch-dependency {
   stroke-dasharray: 5, 5;
}
```

By default predecessors and successors in columns and the task editor are displayed using task id and name. The id part is configurable, any task field may be used instead (for example wbsCode or sequence number) by [Gantt#dependencyIdField](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#config-dependencyIdField) property.

```
const gantt = new Gantt({
   dependencyIdField: 'wbsCode',

   project,
   columns : [
       { type : 'name', width : 250 }
   ],
});
```

Also see [DependencyColumn#dependencyIdField](https://bryntum.com/docs/gantt/api/#Gantt/column/DependencyColumn#config-dependencyIdField) to configure columns only if required.

This feature is **enabled** by default

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencies](https://bryntum.com/docs/gantt/api/Gantt/feature/Dependencies#property-isDependencies)
Identifies an object as an instance of [Dependencies](https://bryntum.com/docs/gantt/api/#Gantt/feature/Dependencies) class, or subclass thereof.

[isDependencies](https://bryntum.com/docs/gantt/api/Gantt/feature/Dependencies#property-isDependencies-static)
Identifies an object as an instance of [Dependencies](https://bryntum.com/docs/gantt/api/#Gantt/feature/Dependencies) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[resolveDependencyRecord](https://bryntum.com/docs/gantt/api/Gantt/feature/Dependencies#function-resolveDependencyRecord)
Returns the dependency record for a DOM element

[getHoverTipHtml](https://bryntum.com/docs/gantt/api/Gantt/feature/Dependencies#function-getHoverTipHtml)
Generates html for the tooltip shown when hovering a dependency

[createDependency](https://bryntum.com/docs/gantt/api/Gantt/feature/Dependencies#function-createDependency)
Create a new dependency from source terminal to target terminal
