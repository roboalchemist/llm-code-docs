# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/widget/AssignmentField.md

# [AssignmentField](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField)

A special field widget used to edit single event assignments.

This field is used as the default editor for the [ResourceAssignmentColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ResourceAssignmentColumn)

Customizing the drop-down grid
------------------------------

The field is a [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo) which has a [AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid) as its picker. Here's a snippet showing how to configure the grid:

```
const gantt = new Gantt({
    appendTo          : 'container',
    resourceImagePath : '../_shared/images/users/',
    columns           : [
        { type : 'name', field : 'name', text : 'Name', width : 250 },
        {
            type        : 'resourceassignment',
            width       : 250,
            showAvatars : true,
            editor      : {
                type   : 'assignmentfield',
                // The picker config is applied to the Grid
                picker : {
                    height : 350,
                    width  : 450,
                    items  : {
                        // configure Work-type resource grid
                        workTab : {
                            features : {
                                filterBar  : true,
                                group      : 'resource.city',
                                headerMenu : false,
                                cellMenu   : false
                            },
                            // The extra columns are concatenated onto the base column set.
                            columns : [{
                                text       : 'Calendar',
                                // Read a nested property (name) from the resource calendar
                                field      : 'resource.calendar.name',
                                filterable : false,
                                editor     : false,
                                width      : 85
                            }]
                        }
                    }
                }
            }
        }
    ],

    project
 });
```

Built-in widgets
----------------

The default toolbar buttons are:

Widget ref

Type

Weight

Description

`saveButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

100

Save event button on the bbar

`cancelButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

300

Cancel event editing button on the bbar

To customize the buttons:

```
const gantt = new Gantt({
    appendTo                : 'container',
    resourceImageFolderPath : '../_shared/images/users/',
    columns                 : [
        {
            type        : 'resourceassignment',
            width       : 250,
            showAvatars : true,
            editor      : {
                type   : 'assignmentfield',
                // The picker config is applied to the Grid
                picker : {
                    height   : 350,
                    width    : 450,
                    bbar : {
                       // Align the Save button to the left and the Cancel button to the right
                       saveButton : {
                           order : -1,
                           style : 'margin-inline-end: auto'
                       }
                    }
                }
            }
        }
    ],

    project
 });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[picker](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField#config-picker)
A config object used to configure the [assignment grid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid) used to select resources to assign.

Any `columns` provided are concatenated onto the default column set.

[pickerWidth](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField#config-pickerWidth)
Width of picker, defaults to this field's [pickerAlignElement](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField#config-pickerAlignElement) width

[projectEvent](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField#config-projectEvent)
Event to load resource assignments for. Either event or [store](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentField#config-store) should be given.

[store](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField#config-store)
Assignment manipulation store to use, or it's configuration object. Either store or [projectEvent](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentField#config-projectEvent) should be given

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField#config-tooltipTemplate)
A template function used to generate the tooltip contents when hovering this field. Defaults to showing "\[Name\] \[%\]"

```
const gantt = new Gantt({
  columns                 : [
        { type : 'name', field : 'name', text : 'Name', width : 250 },
        {
            type        : 'resourceassignment',
            editor      : {
                type   : 'assignmentfield',
                tooltipTemplate({ taskRecord, assignmentRecords }) {
                    return assignmentRecords.map(as => as.resource?.name).join(', ');
                }
            }
        }
    ]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentField](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField#property-isAssignmentField)
Identifies an object as an instance of [AssignmentField](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentField) class, or subclass thereof.

[isAssignmentField](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentField#property-isAssignmentField-static)
Identifies an object as an instance of [AssignmentField](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentField) class, or subclass thereof.
