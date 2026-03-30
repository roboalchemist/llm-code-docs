# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/AddNewColumn.md

# [AddNewColumn](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn)

This column allows user to dynamically add columns to the Gantt chart by clicking the column header and picking columns from a combobox.

Customizing the combobox store data
-----------------------------------

In order to add, update or remove a column from the combobox one can use [processComboStoreConfig](https://bryntum.com/docs/gantt/api/#Gantt/column/AddNewColumn#config-processComboStoreConfig) config:

```
new Gantt{{
    columns : [
        {
            type : 'addnew',
            processComboStoreConfig({ config, column }) {
                // Add a new custom column to the combobox
                config.data.push({
                    text  : 'Custom date',
                    // column config
                    value : {
                        type  : 'date',
                        field : 'customDate',
                        text  : 'Custom date'
                    }
                });
            }
        }
    ]
}}
```

Adding a custom column class
----------------------------

In order to appear in the column combobox list a column class have to fulfill these conditions:

1. the class should have a static property `type` with unique string value that will identify the column.
2. the class should be registered with the call to [ColumnStore.registerColumnType](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore#function-registerColumnType-static).
3. the class should have a static property `isGanttColumn` with truthy value.
4. the class should have a static `text` property with column name.

For example:

```
import ColumnStore from 'gantt-distr/lib/Grid/data/ColumnStore.js';
import Column from 'gantt-distr/lib/Grid/column/Column.js';

// New column class to display task priority
export default class TaskPriorityColumn extends Column {
    // unique alias of the column
    static type = 'priority';

    // indicates that the column should be present in "Add New..." column
    static isGanttColumn = true;

    static defaults = {
        // the column is mapped to "priority" field of the Task model
        field : 'priority',
        // the column title
        text  : 'Priority'
    };
}

// register new column
ColumnStore.registerColumnType(TaskPriorityColumn);
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[allowMultipleColumnInstances](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#config-allowMultipleColumnInstances)
Specify `true` to allow adding more than one column of the same type to the Gantt.

[processComboStoreConfig](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#config-processComboStoreConfig)
A function to be called for processing the column combo store configuration object. Can be specified as a function, or name of a function in the ownership.

Can be used for editing the combo store data. For example:

```
new Gantt({
    columns : [
        {
            type : 'addnew',
            processComboStoreConfig({ config, column }) {
                // Adding a custom column
                config.data.push({
                    text  : 'Custom date',
                    // column config
                    value : {
                        type  : 'date',
                        field : 'customDate',
                        text  : 'Custom date'
                    }
                });
            }
        }
    ]
});
```

[combo](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#config-combo)
A configuration object to apply to the {Core.widget.Combo} rendered into the column header.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAddNewColumn](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#property-isAddNewColumn)
Identifies an object as an instance of [AddNewColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/AddNewColumn) class, or subclass thereof.

[isAddNewColumn](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#property-isAddNewColumn-static)
Identifies an object as an instance of [AddNewColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/AddNewColumn) class, or subclass thereof.

[allowMultipleColumnInstances](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#property-allowMultipleColumnInstances)
Specify `true` to allow adding more than one column of the same type to the Gantt.

[processComboStoreConfig](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#property-processComboStoreConfig)
A function to be called for processing the column combo store configuration object. Can be specified as a function, or name of a function in the ownership.

Can be used for editing the combo store data. For example:

```
new Gantt({
    columns : [
        {
            type : 'addnew',
            processComboStoreConfig({ config, column }) {
                // Adding a custom column
                config.data.push({
                    text  : 'Custom date',
                    // column config
                    value : {
                        type  : 'date',
                        field : 'customDate',
                        text  : 'Custom date'
                    }
                });
            }
        }
    ]
});
```

[combo](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#property-combo)
A configuration object to apply to the {Core.widget.Combo} rendered into the column header.

[combo](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#property-combo)
Returns the combo box field rendered into the header of this column

## Typedefs

Typedefs are type definitions for the class

[AddNewColumnComboModelConfig](https://bryntum.com/docs/gantt/api/Gantt/column/AddNewColumn#typedef-AddNewColumnComboModelConfig)
["Add New..." column](https://bryntum.com/docs/gantt/api/#Gantt/column/AddNewColumn) combobox item data.
