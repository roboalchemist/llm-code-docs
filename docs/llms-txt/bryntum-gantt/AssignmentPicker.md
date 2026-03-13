# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/widget/AssignmentPicker.md

# [AssignmentPicker](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentPicker)

Class for assignment field dropdown, wraps [AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid) within a frame and adds two buttons: Save and Cancel

Class for assignment field dropdown. It's a [tab panel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) having the following tabs:

Tab ref

Text

Weight

Class

Description

`workTab`

Work

10

[AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid)

Grid with work-resources

`materialTab`

Material

20

[AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid)

Grid with material-resources

`costTab`

Cost

30

[AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid)

Grid with cost-resources

Each tabs displays resources of corresponding type: _work_, _material_ and _cost_. The panel by default hides tabs for resource types not represented in the project. This is controlled by [autoHideResourceTypeTabs](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentPicker#config-autoHideResourceTypeTabs) config.

The panel bottom toolbar also has "Save" and "Cancel" buttons.

Widget ref

Text

Class

Description

`saveButton`

Save

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

Save changes button

`cancelButton`

Cancel

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

Cancel changes button

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showCostControls](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentPicker#config-showCostControls)
If set to `true` this will show rate table columns.

[autoHideResourceTypeTabs](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentPicker#config-autoHideResourceTypeTabs)
Set to `true` to automatically hide tabs representing resource types not used in the project.

[projectEvent](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentPicker#config-projectEvent)
The Event to load resource assignments for. Either an Event or [store](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentPicker#config-store) should be given.

[store](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentPicker#config-store)
Store for the picker. Either store or [projectEvent](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentPicker#config-projectEvent) should be given

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentPicker](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentPicker#property-isAssignmentPicker)
Identifies an object as an instance of [AssignmentPicker](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentPicker) class, or subclass thereof.

[isAssignmentPicker](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentPicker#property-isAssignmentPicker-static)
Identifies an object as an instance of [AssignmentPicker](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentPicker) class, or subclass thereof.
