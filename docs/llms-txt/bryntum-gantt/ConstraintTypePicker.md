# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/ConstraintTypePicker.md

# [ConstraintTypePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ConstraintTypePicker)

Combo box preconfigured with possible constraint type values. This picker doesn't support [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect).

This field can be used as an editor for a [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the `ConstraintTypeColumn` in the Gantt chart.

The underlying store used by this class contains the following data by default:

```
store : {
    data : [
        { id : 'none' },
        { id : 'assoonaspossible' }, // Present only if `includeAsapAlapAsConstraints` is true
        { id : 'aslateaspossible' }, // Present only if `includeAsapAlapAsConstraints` is true
        { id : 'muststarton' },
        { id : 'mustfinishon' },
        { id : 'startnoearlierthan' },
        { id : 'startnolaterthan' },
        { id : 'finishnoearlierthan' },
        { id : 'finishnolaterthan' }
    ]
},
```

Defining valid constraint types
-------------------------------

You can easily filter out certain constraint types globally by configuring instances of this class with fewer options from the default set mentioned above:

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

[isConstraintTypePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ConstraintTypePicker#property-isConstraintTypePicker)
Identifies an object as an instance of [ConstraintTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ConstraintTypePicker) class, or subclass thereof.

[isConstraintTypePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ConstraintTypePicker#property-isConstraintTypePicker-static)
Identifies an object as an instance of [ConstraintTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ConstraintTypePicker) class, or subclass thereof.
