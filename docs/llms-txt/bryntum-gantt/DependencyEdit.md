# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/DependencyEdit.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/DependencyEdit.md

# [DependencyEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit)

Feature that displays a popup containing fields for editing a dependency. Requires the [Dependencies](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Dependencies) feature to be enabled. Double-click a dependency line in the demo below to show the editor.

Customizing the built-in widgets
--------------------------------

```
 const scheduler = new Scheduler({
     columns : [
         { field : 'name', text : 'Name', width : 100 }
     ],
     features : {
         dependencies   : true,
         dependencyEdit : {
             editorConfig : {
                 items : {
                     // Custom label for the type field
                     typeField : {
                         label : 'Kind'
                     }
                 },

                 bbar : {
                     items : {
                         // Hiding save button
                         saveButton : {
                             hidden : true
                         }
                     }
                 }
             }
         }
     }
 });
```

Built-in widgets
----------------

Widget ref

Type

Weight

Description

`fromNameField`

[DisplayField](https://bryntum.com/docs/gantt/api/#Core/widget/DisplayField)

100

From task name (readonly)

`toNameField`

[DisplayField](https://bryntum.com/docs/gantt/api/#Core/widget/DisplayField)

200

To task name (readonly)

`typeField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

300

Edit type

`lagField`

[DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField)

400

Edit lag

The built-in buttons are:

Widget ref

Type

Weight

Description

`saveButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

100

Save button on the bbar

`deleteButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

200

Delete button on the bbar

`cancelButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

300

Cancel editing button on the bbar

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoClose](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#config-autoClose)
True to hide this editor if a click is detected outside it (defaults to true)

[saveAndCloseOnEnter](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#config-saveAndCloseOnEnter)
True to save and close this panel if ENTER is pressed in one of the input fields inside the panel.

[showDeleteButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#config-showDeleteButton)
True to show a delete button in the form.

[triggerEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#config-triggerEvent)
The event that shall trigger showing the editor. Defaults to `dependencydblclick`, set to empty string or `null` to disable editing of dependencies.

[showLagField](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#config-showLagField)
True to show the lag field for the dependency

[editorConfig](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#config-editorConfig)
Default editor configuration, used to configure the Popup.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-isDependencyEdit)
Identifies an object as an instance of [DependencyEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/DependencyEdit) class, or subclass thereof.

[isDependencyEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-isDependencyEdit-static)
Identifies an object as an instance of [DependencyEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/DependencyEdit) class, or subclass thereof.

[triggerEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-triggerEvent)
The event that shall trigger showing the editor. Defaults to `dependencydblclick`, set to empty string or `null` to disable editing of dependencies.

[fromNameField](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-fromNameField)
Reference to the source task name field

[toNameField](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-toNameField)
Reference to the target task name field

[typeField](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-typeField)
Reference to the dependency type field

[lagField](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-lagField)
Reference to the lag field

[saveButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-saveButton)
Reference to the save button, if used

[deleteButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-deleteButton)
Reference to the delete button, if used

[cancelButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#property-cancelButton)
Reference to the cancel button, if used

## Functions

Functions are methods available for calling on the class

[onBeforeSave](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-onBeforeSave)
Template method, intended to be overridden. Called before the dependency record has been updated.

[onAfterSave](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-onAfterSave)
Template method, intended to be overridden. Called after the dependency record has been updated.

[updateRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-updateRecord)
Updates record being edited with values from the editor

[editDependency](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-editDependency)
Opens a popup to edit the passed dependency.

[getEditor](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-getEditor)
Gets an editor instance. Creates on first call, reuses on consecutive

[loadRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-loadRecord)
Sets fields values from record being edited

[save](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-save)
Saves the changes (applies them to record if valid, if invalid editor stays open)

[deleteDependency](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#function-deleteDependency)
Delete dependency being edited

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeDependencyEditShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#event-beforeDependencyEditShow)
Fires on the owning Scheduler or Gantt widget when the editor for a dependency is available, but before it is shown. Allows manipulating fields before the widget is shown.

[beforeDependencyEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#event-beforeDependencyEdit)
Fires on the owning Scheduler or Gantt widget before an dependency is displayed in the editor. This may be listened for to allow an application to take over dependency editing duties. Return `false` to stop the default editing UI from being shown or a `Promise` yielding `true` or `false` for async vetoing.

[beforeDependencySave](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#event-beforeDependencySave)
Fires on the owning Scheduler or Gantt widget before a dependency is saved using the dependency edit popup

[beforeDependencyAdd](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#event-beforeDependencyAdd)
Fires on the owning Scheduler or Gantt widget before a dependency is added from the dependency edit popup

[afterDependencySave](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#event-afterDependencySave)
Fires on the owning Scheduler or Gantt widget after a dependency is successfully saved using the dependency edit popup

[beforeDependencyDelete](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyEdit#event-beforeDependencyDelete)
Fires on the owning Scheduler or Gantt widget before a dependency is deleted from the dependency edit popup, or when clicking the delete icon on a selected dependency line.
