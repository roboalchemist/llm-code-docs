# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/VersionGrid.md

# [VersionGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid)

Displays a list of versions and the transactions they contain. For use with the [Versions](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/Versions) feature.

Configure the VersionGrid with a [ProjectModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel) using the [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/VersionGrid#config-project) config.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#config-project)
The [ProjectModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel) whose versions and changes are being observed in this grid.

[showUnattachedTransactions](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#config-showUnattachedTransactions)
Whether to display transactions not yet associated with a version.

[showNamedVersionsOnly](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#config-showNamedVersionsOnly)
Whether to show only versions that have been assigned a specific name.

[showVersions](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#config-showVersions)
Whether to include version rows in the display.

[comparingVersionId](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#config-comparingVersionId)
The id of the version currently being compared, if any.

[dateFormat](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#config-dateFormat)
The date format used for displaying date values in change actions.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isVersionGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#property-isVersionGrid)
Identifies an object as an instance of [VersionGrid](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/VersionGrid) class, or subclass thereof.

[isVersionGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#property-isVersionGrid-static)
Identifies an object as an instance of [VersionGrid](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/VersionGrid) class, or subclass thereof.

[showUnattachedTransactions](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#property-showUnattachedTransactions)
Whether to display transactions not yet associated with a version.

[showNamedVersionsOnly](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#property-showNamedVersionsOnly)
Whether to show only versions that have been assigned a specific name.

[showVersions](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#property-showVersions)
Whether to include version rows in the display.

[comparingVersionId](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#property-comparingVersionId)
The id of the version currently being compared, if any.

## Functions

Functions are methods available for calling on the class

[processUpdates](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-processUpdates)
This is an optimization to more efficiently replace grid rows when the underlying stores change. We wait a tick, then replace the set of rows corresponding to the modified records with the new projected rowset.

The code below does not handle record remove, or updating transactions without their version in the same tick. (Versions can be updated without their transactions, as when renamed.)

[refreshGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-refreshGrid)
Does a full replace of all rows in the grid using all records currently in the two stores.

[getGridRows](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-getGridRows)
Transform a set of transactions (and optional parent version) into tree structure needed by grid

[renderPropertyValue](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-renderPropertyValue)
Return DomConfig for an individual data value.

[formatValueString](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-formatValueString)
Convert an individual data value to a string.

[formatPropertyName](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-formatPropertyName)
Format a property name in the change log to a displayable string. By default, converts e.g. "camelCase" to "Camel case".

[renderActionDescription](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-renderActionDescription)
Produces a text description to show in the description column for an 'action' row.

[sortActionRows](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-sortActionRows-static)
Sorts the actions within a transaction using precedence heuristic to show most "significant" actions first.

[renderHighlightedTextElements](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#function-renderHighlightedTextElements)
Produce a DomConfig for cell text where \*\*-delimited tokens are replaced by specified values. Used to allow CSS styling of replaced tokens (e.g. task names) in the changelog.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[restore](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#event-restore)
Fires when the user chooses to restore a selected version.

[compare](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#event-compare)
Fires when the user chooses to compare a selected version.

[stopCompare](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/VersionGrid#event-stopCompare)
Fires when the user chooses to stop comparing a currently compared version.
