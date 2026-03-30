# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/widget/TreeCombo.md

# [TreeCombo](https://bryntum.com/docs/gantt/api/Grid/widget/TreeCombo)

A powerful [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo) box using a [TreeGrid](https://bryntum.com/docs/gantt/api/#Grid/view/TreeGrid) as its drop down widget. You can define your own set of columns to display and use all the regular features of the Grid.

```
new TreeCombo({
    label    : 'Pick task(s)',
    width    : '30em',
    appendTo : document.body,
    picker   : {
        // Define the columns to show in the grid
        columns : [
            { type : 'tree', text : 'Tasks', field : 'name', flex : 1 },
            { text : 'Priority', field : 'prio' }
        ]
    },
    chipView : {
        // Render the chips in the combo field
        itemTpl(record) {
            return StringHelper.xss`${record.name}`;
        }
    },
    store : {
        fields     : [
            'prio'
        ],
        data : [
            {
                name     : 'Development Tasks',
                expanded : true,
                children : [
                    { id : 1, name : 'Improve React docs', prio : 'High' },
                    { id : 2, name : 'Build Angular module', prio : 'Low' },
                    { id : 3, name : 'Creat Vue project', prio : 'Low' }
                ]
            },
            { name : 'Customer meeting', prio : 'Normal' },
            {
                name     : 'Customer Tasks',
                expanded : true,
                children : [
                    { id : 4, name : 'Intro meeting', prio : 'Normal' },
                    { id : 5, name : 'Build POC', prio : 'High' },
                    { id : 6, name : 'Documentation', prio : 'Low' }
                ]
            }
        ]
    }
});
```

Use as a cell editor
--------------------

You can use the TreeCombo as a cell editor in a Grid. In the following example, we use the TreeCombo as a cell editor for the Org unit column:

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTreeCombo](https://bryntum.com/docs/gantt/api/Grid/widget/TreeCombo#property-isTreeCombo)
Identifies an object as an instance of [TreeCombo](https://bryntum.com/docs/gantt/api/#Grid/widget/TreeCombo) class, or subclass thereof.

[isTreeCombo](https://bryntum.com/docs/gantt/api/Grid/widget/TreeCombo#property-isTreeCombo-static)
Identifies an object as an instance of [TreeCombo](https://bryntum.com/docs/gantt/api/#Grid/widget/TreeCombo) class, or subclass thereof.
