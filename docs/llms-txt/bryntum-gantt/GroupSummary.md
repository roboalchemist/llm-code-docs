# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/GroupSummary.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/GroupSummary.md

# [GroupSummary](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary)

Displays a summary row as a group footer in a grouped grid. Uses the same configuration options on columns as [Summary](https://bryntum.com/docs/gantt/api/#Grid/feature/Summary).

This feature is **disabled** by default.

```
new Grid({
    features : {
        group        : 'city',
        groupSummary : true
    },
    columns : [
        { text : 'Score', data : 'score', width : 80, sum : 'sum' }
        { text : 'Rank', data : 'rank', width : 80, sum : 'average', summaryRenderer: ({ sum }) => return 'Average rank ' + sum }
    ]
})
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[collapseToHeader](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#config-collapseToHeader)
Configure as `true` to have group summaries rendered in the group header when a group is collapsed.

```
const grid = new Grid({
   features : {
       groupSummary : {
           collapseToHeader : true
       }
   }
});
```

Only applies when [target](https://bryntum.com/docs/gantt/api/#Grid/feature/GroupSummary#config-target) is `'footer'` (the default).

[target](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#config-target)
Where to render the group summaries to, either `header` to display them in the group header or `footer` to display them in the group footer (the default).

```
const grid = new Grid({
   features : {
       groupSummary : {
           target : 'header'
       }
   }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGroupSummary](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#property-isGroupSummary)
Identifies an object as an instance of [GroupSummary](https://bryntum.com/docs/gantt/api/#Grid/feature/GroupSummary) class, or subclass thereof.

[isGroupSummary](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#property-isGroupSummary-static)
Identifies an object as an instance of [GroupSummary](https://bryntum.com/docs/gantt/api/#Grid/feature/GroupSummary) class, or subclass thereof.

[collapseToHeader](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#property-collapseToHeader)
Set to `true` to have group summaries rendered in the group header when a group is collapsed.

Only applies when [target](https://bryntum.com/docs/gantt/api/#Grid/feature/GroupSummary#config-target) is `'footer'` (the default).

[target](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#property-target)
Where to render the group summaries to, either `header` to display them in the group header or `footer` to display them in the group footer (the default).

## Functions

Functions are methods available for calling on the class

[onBeforeRenderRow](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#function-onBeforeRenderRow)
Called before rendering row contents, used to reset rows no longer used as group summary rows

[renderCell](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#function-renderCell)
Called when a cell is rendered, styles the group rows first cell.

[onStoreUpdate](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#function-onStoreUpdate)
Updates summaries on store changes (except record update, handled below)

[refresh](https://bryntum.com/docs/gantt/api/Grid/feature/GroupSummary#function-refresh)
Refreshes the summaries
