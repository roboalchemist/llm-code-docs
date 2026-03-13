# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/ConstraintTypeColumn.md

# [ConstraintTypeColumn](https://bryntum.com/docs/gantt/api/Gantt/column/ConstraintTypeColumn)

[Constraint type](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-constraintType) column.

Default editor is a [ConstraintTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ConstraintTypePicker).

By default, the constraint type can be one of:

* As soon as possible
* As late as possible
* Must start on \[date\]
* Must finish on \[date\]
* Start no earlier than \[date\]
* Start no later than \[date\]
* Finish no earlier than \[date\]
* Finish no later than \[date\]

If you want to allow only certain constraint types to be selected, please refer to the docs for the [ConstraintTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ConstraintTypePicker).

The date of the constraint can be specified with the [ConstraintDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ConstraintDateColumn)

Defining valid constraint types
-------------------------------

You can easily filter out certain constraint types globally by configuring the `editor` or the `filterField` of this column with fewer options from the default set mentioned above:

```
   new Gantt({
       features : {
           filter : true
       },
       columns : [{
           type : 'constrainttype',

           // Editor for cell editing
           editor : {
               store : {
                   data : [
                       { id : 'none' },
                       { id : 'muststarton' },
                       { id : 'mustfinishon' }
                   ]
               }
           },

           // Override the input field for filtering by constraint type
           filterable : {
               filterField : {
                   store : {
                       data : [
                           { id : 'none' },
                           { id : 'muststarton' },
                           { id : 'mustfinishon' }
                       ]
                   }
               }
           }
       }]
   });
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isConstraintTypeColumn](https://bryntum.com/docs/gantt/api/Gantt/column/ConstraintTypeColumn#property-isConstraintTypeColumn)
Identifies an object as an instance of [ConstraintTypeColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ConstraintTypeColumn) class, or subclass thereof.

[isConstraintTypeColumn](https://bryntum.com/docs/gantt/api/Gantt/column/ConstraintTypeColumn#property-isConstraintTypeColumn-static)
Identifies an object as an instance of [ConstraintTypeColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ConstraintTypeColumn) class, or subclass thereof.
