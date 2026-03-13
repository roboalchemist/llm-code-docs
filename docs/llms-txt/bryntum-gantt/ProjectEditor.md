# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/widget/ProjectEditor.md

# [ProjectEditor](https://bryntum.com/docs/gantt/api/Gantt/widget/ProjectEditor)

Provides a UI to edit the project settings in a dialog window. The widget is used internally by the [project edit feature](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit) and you don't normally need to deal with this class directly.

This demo shows how to use the ProjectEditor as a standalone widget:

Project editor customization
----------------------------

To append Widgets to any of the built-in tabs, use the `items` config. The Project editor contains tabs by default. Each tab contains built-in widgets: text fields, date fields, etc.

Tab ref

Text

Weight

Description

`generalTab`

[ProjectEditorGeneralTab](https://bryntum.com/docs/gantt/api/#Gantt/widget/projecteditor/ProjectEditorGeneralTab)

100

Basic configuration: name, start/end dates, schedule from

`descriptionTab`

[ProjectEditorDescriptionTab](https://bryntum.com/docs/gantt/api/#Gantt/widget/projecteditor/ProjectEditorDescriptionTab)

200

A text area to add a description to the selected project

`advancedTab`

[ProjectEditorAdvancedTab](https://bryntum.com/docs/gantt/api/#Gantt/widget/projecteditor/ProjectEditorAdvancedTab)

300

Advanced options: hours per day, days per week and days per month

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[project](https://bryntum.com/docs/gantt/api/Gantt/widget/ProjectEditor#config-project)
The project model that will be edited with the project editor.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectEditor](https://bryntum.com/docs/gantt/api/Gantt/widget/ProjectEditor#property-isProjectEditor)
Identifies an object as an instance of [ProjectEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor) class, or subclass thereof.

[isProjectEditor](https://bryntum.com/docs/gantt/api/Gantt/widget/ProjectEditor#property-isProjectEditor-static)
Identifies an object as an instance of [ProjectEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[loadProject](https://bryntum.com/docs/gantt/api/Gantt/widget/ProjectEditor#function-loadProject)
Loads a project model into the editor
