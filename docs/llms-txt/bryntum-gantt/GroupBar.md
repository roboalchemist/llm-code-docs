# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/widget/GroupBar.md

# [GroupBar](https://bryntum.com/docs/gantt/api/Grid/widget/GroupBar)

A widget used to manage grouping of a grid using [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) feature or a tree using the [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature. Column headers can be drag-dropped on this widget to regroup the data in the grid store. This widget only handles column-based grouping, and doesn't handle custom group functions.

```
const tree = new TreeGrid({
    appendTo : 'container',
    features : {
        treeGroup : {
            hideGroupedColumns : true,
            levels             : [
                'manager',
                'airline'
            ],
            parentRenderer : (field, data) => `${StringHelper.capitalize(field)}: ${data.name}`
        }
    },

    columns : [
        {
            text  : 'Name',
            field : 'name',
            flex  : 3,
            type  : 'tree'
        },
        {
            text   : 'Airline',
            field  : 'airline',
            align  : 'center',
            flex   : 2,
        },
        {
            type  : 'check',
            text  : 'Domestic',
            field : 'domestic',
            align : 'left',
            flex  : 1
        },
        {
            type  : 'number',
            text  : 'Capacity',
            field : 'capacity',
            flex  : 1
        },
        {
            type  : 'number',
            text  : 'Crew',
            field : 'crew',
            flex  : 1
        }
    ],

    tbar : [
        'Group by',
        {
            type : 'groupbar'
        }
    ]
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGroupBar](https://bryntum.com/docs/gantt/api/Grid/widget/GroupBar#property-isGroupBar)
Identifies an object as an instance of [GroupBar](https://bryntum.com/docs/gantt/api/#Grid/widget/GroupBar) class, or subclass thereof.

[isGroupBar](https://bryntum.com/docs/gantt/api/Grid/widget/GroupBar#property-isGroupBar-static)
Identifies an object as an instance of [GroupBar](https://bryntum.com/docs/gantt/api/#Grid/widget/GroupBar) class, or subclass thereof.
