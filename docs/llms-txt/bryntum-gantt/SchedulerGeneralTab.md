# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/taskeditor/SchedulerGeneralTab.md

# [SchedulerGeneralTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/SchedulerGeneralTab)

A tab inside the [scheduler task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) showing the general information for an event from a simplified scheduler project.

Contains the following fields by default:

Field ref

Type

Text

Weight

Description

`nameField`

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

Name

100

Task name

`resourcesField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

Resources

200

Shows a list of available resources for this task

`startDateField`

[DateTimeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateTimeField)

Start

300

Shows when the task begins

`endDateField`

[DateTimeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateTimeField)

Finish

400

Shows when the task ends

`durationField`

[DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField)

Duration

500

Shows how long the task is

`percentDoneField`

[NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)

% Complete

600

Shows what part of task is done already in percentage

`effort`

[EffortField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EffortField)

Effort

620

Shows how much working time is required to complete the whole event

`preambleField`

[DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField)

Preamble

650

Shows preamble time (task preparation time)

`postambleField`

[DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField)

Postamble

660

Shows postamble time (clean up after the task)

`colorField` ¹

[EventColorField](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField)

Color ¹

700

Choose background color for the task bar

**¹** Set the [showTaskColorPickers](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerProBase#config-showTaskColorPickers) config to `true` to enable this field

To customize the tab or its fields:

```
features : {
    taskEdit : {
        items : {
            generalTab : {
                // Custom title
                title: 'Common',
                // Customized items
                items : {
                    // Hide the duration field
                    durationField : null,
                    // Customize the name field
                    nameField : {
                        label : 'Title'
                    },
                    // Add a custom field
                    colorField : {
                        type   : 'text',
                        label  : 'Color',
                        // name maps to a field on the event record
                        name   : 'eventColor',
                        // place at top
                        weight : 0
                    }
                }
            }
        }
    }
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerGeneralTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/SchedulerGeneralTab#property-isSchedulerGeneralTab)
Identifies an object as an instance of [SchedulerGeneralTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SchedulerGeneralTab) class, or subclass thereof.

[isSchedulerGeneralTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/SchedulerGeneralTab#property-isSchedulerGeneralTab-static)
Identifies an object as an instance of [SchedulerGeneralTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SchedulerGeneralTab) class, or subclass thereof.
