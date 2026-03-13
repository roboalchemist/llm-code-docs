# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/CalendarEditor.md

# [CalendarEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor)

A widget allowing to edit the provided [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/CalendarModel).

The widget contains a [tab panel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) with three tabs "General", "Exceptions" and "Weeks" (the tab panel itself has `mainTabs` widget `ref`).

Tab ref

Type

Text

Weight

Description

`generalTab`

[Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container)

General

100

Calendar name, parent fields and a date picker displaying dates availability.

`exceptionTab`

[CalendarEditorExceptionTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/calendareditor/CalendarEditorExceptionTab)

Exceptions

200

Contains the calendar exception grid and editor.

`weekTab`

[CalendarEditorWeekTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/calendareditor/CalendarEditorWeekTab)

Weeks

300

Contains the calendar week grid and editor.

Besides that, there is a bottom toolbar with `Save`, `Delete` and `Cancel` buttons having (`ref` : `saveButton`, `weight` : `200`), (`ref` : `removeButton`, `weight` : `300`) and (`ref` : `cancelButton`, `weight` : `400`) respectively.

### General tab

"General" tab contains widgets for basic configurations and controls to oversee certain dates availability. The tab contains the following widgets:

* "Name" (`ref` : `nameField`, `type` : [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField), `weight` : `10`) A text field for editing the calendar name.
* "Parent" (`ref` : `parentField`, `type` : [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo), `weight` : `20`) A combobox field for editing the calendar parent.
* "Days are working by default" (`ref` : `unspecifiedTimeIsWorkingField`, `type` : [Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox), `weight` : `30`) A checkbox allowing to specify whether the calendar allows to work any time by default.
* (`ref` : `datePickerLegend`, `type` : [CalendarEditorLegend](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/calendareditor/CalendarEditorLegend), `weight` : `50`) A container displaying legend for the date picker (see next `datePicker` widget).
* (`ref` : `datePicker`, `type` : [CalendarEditorDatePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/calendareditor/CalendarEditorDatePicker), `weight` : `60`) A special date picker displaying the calendar effect on shown dates. The control basically highlights dates by adding color badges representing the calendar intervals. It does that for the dates affected by the corresponding intervals.
* (`ref` : `dateInfo`, `type` : [CalendarEditorDateInfo](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/calendareditor/CalendarEditorDateInfo), `weight` : `70`) A container that shows availability info for the date selected in the date picker. For the selected date the widget displays both availability and the interval providing it.

### Exceptions tab

The "Exceptions" tab allows to specify calendar exceptions - special availability overrides for particular date ranges (like holiday or vacations). The tab contains a grid listing registered exceptions on the left side and a panel allowing to edit the selected exception on the right side.

Widget ref

Type

Weight

Description

`grid`

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

10

Exception grid.

`panel`

[CalendarEditorExceptionPanel](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/calendareditor/CalendarEditorExceptionPanel)

20

Exception editor.

### Weeks tab

The "Weeks" tab allows to specify default weekly availability or weekly availability for specific date ranges. The tab contains a grid listing registered week availability intervals on the left side and a panel allowing to edit the selected interval on the right side.

Widget ref

Type

Weight

Description

`grid`

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

10

Week grid.

`panel`

[CalendarEditorWeekPanel](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/calendareditor/CalendarEditorWeekPanel)

20

Week editor.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[calendar](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#config-calendar)
A calendar to edit.

[activeDate](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#config-activeDate)
A date to display in the date picker.

[defaultWorkingDayAvailability](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#config-defaultWorkingDayAvailability)
Default availability ranges to be assigned to a day (or an exception) once it's made working. By default uses `08:00-12:00, 13:00-17:00` ranges.

[defaultWorkingDays](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#config-defaultWorkingDays)
Specifies days treated as working by default. The config is used when adding a new week. In this case the widget sets the week working days availability with [defaultWorkingDayAvailability](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CalendarEditor#config-defaultWorkingDayAvailability) value.

The value is an object with day indexes (0 - Sunday, 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday and 6 - Saturday) used as keys and boolean values (`true` if the corresponding day is working and `false` otherwise).

For example:

```
new CalendarEditor({
    // Sunday is the only non-working day by default
    defaultWorkingDays : {
        0 : false,
        1 : true,
        2 : true,
        3 : true,
        4 : true,
        5 : true,
        6 : true
    },
    ...
});
```

By default, the config sets 5 working days Monday - Friday with non-working Saturday and Sunday.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCalendarEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#property-isCalendarEditor)
Identifies an object as an instance of [CalendarEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CalendarEditor) class, or subclass thereof.

[isCalendarEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#property-isCalendarEditor-static)
Identifies an object as an instance of [CalendarEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CalendarEditor) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[save](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#function-save)
Saves changes to the calendar. The changes saving could be prevented by the widget if it finds some of the child controls are in invalid state. In that case the method displays [a message](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog) asking user to fix the data before saving.

## Typedefs

Typedefs are type definitions for the class

[WorkingDays](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/CalendarEditor#typedef-WorkingDays)
Type object containing working days settings.

Example: Set Sunday and Monday as non-working days:

```
const workingDays = {
    0 : false,
    1 : false,
    2 : true,
    3 : true,
    4 : true,
    5 : true,
    6 : true
}
```
