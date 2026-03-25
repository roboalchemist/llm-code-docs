# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/migration/migrating_from_extjs.md

# Migrate from Gantt for Ext JS

In this guide we will walk you through in detail how to migrate from our <a href="https://bryntum.com/products/gantt-for-extjs">Ext JS based Gantt product</a>
to the modern Bryntum Gantt. We will focus our guide around the advanced example which has a fair amount of complexity,
and many features enabled (this example exists in both products). After completing this migration, you will end up with a simple JS application
which can be downloaded from [here](data/Gantt/guides/migration/ext-migration.zip).

## Introduction

In Ext Gantt, the advanced demo is built as a single page application. It has single entry point - `app.js` which is loaded by
the index page. The entry point creates an `Ext.Application`, a controller to listen to global events (like locale change), a state
tracking manager to enable undo/redo feature, and uses `Ext.Viewport` to render items of the main view to the page.

Bryntum Gantt however does not have an application concept, and it also does not assume to fully control the page content.
From the outside, it is a plain JS widget (though encapsulating enormous amounts of features) that you append to the page.
Compared to Ext JS Classic widgets, the modern Bryntum widgets can be sized with CSS (we prefer flexbox to do that)
rather than as part of a JS-based layout architecture. When porting the demo we will be using standard HTML/CSS to
compose the page and the contents of the `@bryntum/gantt` NPM package as ES6 imports (to avoid needing a build step).

## Bryntum widgets

While Bryntum is renowned for its powerful scheduling components, it offers much more than just scheduling capabilities.
In fact, it provides a comprehensive suite of widgets and UI components, reminiscent of Ext JS, that enable developers
to create versatile and feature-rich web applications in addition to scheduling.

These widgets include:

* [Toolbar](#Core/widget/Toolbar) that can be docked to all four sides
* [Button](#Core/widget/Button) with a variety of appearances and behaviors
* [Checkbox](#Core/widget/Checkbox) and [Radio](#Core/widget/Radio)
* [Menu](#Core/widget/Menu)
* [TextField](#Core/widget/TextField) and [NumberField](#Core/widget/NumberField)
* [DateField](#Core/widget/DateField) and [TimeField](#Core/widget/TimeField)
* [Combo](#Core/widget/Combo) with multi-select feature
* [Panel](#Core/widget/Panel) and [TabPanel](#Core/widget/TabPanel)
* and many, many more.

Therefore, most Ext applications can be ported without the need of any third party widget library.

## Migration considerations

A modern, enterprise-grade, big ExtJS application is usually developed and built with the help of
[Sencha Cmd](https://www.sencha.com/products/sencha-cmd/) which manages dependencies, related SASS files, packages and other
aspects of building, developing and deploying of the application. Although we do not have a similar comprehensive tool for
vanilla JavaScript/TypeScript applications we still need a tool that compiles and builds the application and prepares it
for deploying in a minified form.

We have chosen [Vite](https://vitejs.dev) to create, run and build the vanilla application. This tool is not necessary for a
successful migration or for running the new application, but it makes the development easier, it abstracts away many details,
provides an easy way to work with npm packages and can build the application for production eventually.

## Configuring Gantt

Let's go through the ExtJS configs and see what needs to be changed for the vanilla application. You can refer to this
section in the process of migration to make the resulting application as similar to the ExtJS one as possible.

```javascript
Ext.define('Gnt.examples.advanced.view.Gantt', {
    // This became a config of the TimeRanges feature.
    showTodayLine           : true,

    // This config accepts string to display during load and by default it
    // shows localized `Loading...` message.
    loadMask                : true,

    // This became a config of the PercentBar feature and is true by default.
    enableProgressBarResize : true,

    // This is the new 'Rollups' feature, disabled by default.
    showRollupTasks         : true,

    // Next two configs are identical compared to old version.
    rowHeight               : 30,
    viewPreset              : 'weekAndDayLetter',

    // Obsolete config. Project lines are managed by the ProjectLines feature
    // which doesn't allow configuring targets for lines.
    projectLinesConfig : {
        linesFor : 'start'
    },

    // Obsolete config. Gantt always allows to deselect rows when pressing
    // CTRL key. This cannot be turned off.
    allowDeselect : true,

    // Obsolete config. There is no spreadsheet selection model analog yet.
    selModel : {
        type : 'gantt_spreadsheet',
        rowNumbererHeaderWidth : 70
    },

    // This config has a slightly different syntax.
    lockedGridConfig : {
        width : 400
    },

    // This config doesn't exist anymore, to add class to the row you have to
    // use `record.cls` field or the column renderer.
    lockedViewConfig : {
        getRowClass : function (rec) {
            return rec.isRoot() ? 'root-row' : '';
        }
    },

    // Obsolete config. Task template is not configurable anymore, use
    // taskRenderer instead. This particular template behavior is the default.
    taskBodyTemplate : '...',

    // This should be configured on the Labels feature.
    leftLabelField : {
        dataIndex : 'Name',
        editor    : { xtype : 'textfield' }
    },

    // Ext JS has concept of plugins and features, in Bryntum Gantt there are
    // only features.
    plugins : [
        // This is replaced by the TaskMenu feature and enabled by default.
        'advanced_taskcontextmenu',
        // This is replaced by the Pan feature.
        'scheduler_pan',
        // Task editor exists, but this config is not applicable anymore.
        {
            ptype         : 'gantt_taskeditor',
            height        : 450,
            taskFormClass : 'Gnt.examples.advanced.view.TaskEditorGeneralForm'
        },
        // This plugin used to edit Project nodes and is obsolete now.
        'gantt_projecteditor',
        // This is replaced by the Filter feature - enabled by default.
        'gridfilters',
        // This is replaced by the ProgressLine feature.
        {
            ptype      : 'gantt_progressline',
            disabled   : true,
            statusDate : new Date(2017, 1, 6),
            id         : 'progressline'
        },
        // This is replaced by the DependencyEdit feature.
        {
            ptype : 'gantt_dependencyeditor',
            width : 320
        },
        // This is a demo-specific plugin which does not yet exist in Bryntum
        // Gantt.
        {
            pluginId : 'taskarea',
            ptype    : 'taskarea'
        },
        // This is replaced by the CellEdit feature and is enabled by default.
        {
            ptype        : 'scheduler_treecellediting',
            clicksToEdit : 2,
            pluginId     : 'editingInterface'
        },
        // This is not supported
        {
            ptype : 'gantt_clipboard',
            source : ['raw','text']
        },
        // This is a plugin related to spreadsheet selection model and is not
        // yet supported
        'gantt_selectionreplicator'
    ],

    columns : [
        // Does not exist anymore. This column purpose was to allow row
        // reordering with spreadsheet selection model. Since Bryntum Gantt
        // doesn't yet support spreadsheet selection, this column is not
        // available. There is a RowReorder feature, which is enabled for
        // Gantt by default.
        {   xtype     : 'dragdropcolumn' },
        {
            xtype     : 'namecolumn',
            width     : 200,
            cls       : 'namecolumn',
            // Similar behavior is achieved with the FilterBar feature.
            layout    : 'vbox',
            items     : {
                xtype : 'gantt-filter-field'
            }
        },
        // This is the default config for Date columns now.
        {
            xtype     : 'startdatecolumn',
            width     : 130,
            dataIndex : 'StartDate',
            filter    : {
                type : 'date'
            }
        },
        {
            xtype     : 'enddatecolumn',
            width     : 130,
            dataIndex : 'EndDate',
            filter    : {
                type : 'date'
            }
        },
        {
            xtype     : 'durationcolumn',
            width     : 100
        },
        {   xtype     : 'constrainttypecolumn' },
        {   xtype     : 'constraintdatecolumn' },
        {
            xtype     : 'percentdonecolumn',
            width     : 100,
            dataIndex : 'PercentDone',
            filter    : {
                type : 'number'
            }
        },
        {   xtype     : 'predecessorcolumn' },
        {   xtype     : 'addnewcolumn' }
    ],

    // Renderer is supported but has slightly different signature.
    eventRenderer : function (task, tplData) {
        var style,
            segments, i,
            result;

        if (task.get('Color')) {
            style = Ext.String.format(
                        'background-color: #{0};border-color:#{0}',
                        task.get('Color')
            );

            if (!tplData.segments) {
                result = {
                    style : style
                };
            }
            else {
                segments = tplData.segments;
                for (i = 0; i < segments.length; i++) {
                    segments[i].style = style;
                }
            }
        }

        return result;
    }
});
```

The config used to create a similar Gantt panel using Bryntum Gantt would look like this:

```javascript
{
    type : 'gantt',
    flex : 1,
    // We will define this variable below.
    project,
    rowHeight : 30,
    // Default bar margin differs very much from one in Ext Gantt.
    barMargin : 3,
    viewPreset : 'weekAndDayLetter',
    features : {
        timeRanges : {
            showCurrentTimeLine : true
        },
        rollups : true,
        labels : {
            left : {
                field  : 'name',
                editor : {
                    type : 'textfield'
                }
            }
        },
        pan : true,
        // Add feature and disable by default.
        progressLine : { disabled : true },
        dependencyEdit : true
    },
    },
    subGridConfigs : {
        locked : {
            width : 400
        }
    },
    columns : [
        { type : 'wbs' },
        { type : 'name', width : 250 },
        { type : 'startdate' },
        { type : 'enddate' },
        { type : 'duration' },
        { type : 'constrainttype' },
        { type : 'constraintdate' },
        { type : 'percentdone', width : 70 },
        {
            type  : 'predecessor',
            width : 112
        },
        { type : 'addnew' }
    ]
}
```

## Prerequisites

1. [Node JS](https://nodejs.org/en). In this migration guide we will use the LTS (Long Term Support) version of Node (20.11.1).
   If you have not installed it already, install this version for your platform from the Node.js site.
2. Login to private Bryntum NPM repo to fetch the `@bryntum/gantt` package (for more info please refer to the
   [NPM guide](#Gantt/guides/npm-repository.md)):

```shell
npm config set @bryntum:registry https://npm.bryntum.com
npm login --registry=https://npm.bryntum.com
```

## Step 1: Create an empty Vite application

In your development directory execute the following

```shell
npm create vite@latest ext-migration
```

In the menu that appears, select:

* Vanilla [enter]
* JavaScript [enter]

```shell
cd ext-migration
npm i
npm run dev
```

and navigate to [http://localhost:5173](http://localhost:5173). You should see the "Hello Vite!"
page without any errors.

## Step 2: Install Bryntum Gantt

In the `ext-migration` folder execute:

```shell
npm i @bryntum/gantt
```

<div class="note">
If you get any errors at this step, the error is most likely related to the
<a href="#Gantt/guides/npm-repository.md">Bryntum npm repository</a> setup.
</div>

Delete the following files:

* javascript.svg
* counter.js
* public/vite.svg

Replace content of the following files:

`main.js:`

```javascript
import { Gantt } from '@bryntum/gantt';
import './style.css'

const gantt = new Gantt({
    appendTo: 'app'
});
```

`style.css:`

```css
@import './node_modules/@bryntum/gantt/gantt.css';
@import './node_modules/@bryntum/gantt/svalbard-light.css';

body {
    padding: 0;
    margin: 0;
    font-family: sans-serif;
    font-size: 14px;
}

#app {
    height: 100vh;
}
```

Your browser should now show an empty Gantt chart similar to this screenshot:
<img src="data/Gantt/images/migration/empty-gantt.png" alt="Empty Gantt"/>

## Step 3: Connecting Data

It is very important now to recognize differences between Ext version of
[Gnt.model.Project](https://bryntum.com/products/gantt-for-extjs/docs/#!/api/Gnt.model.Project) and vanilla version
of [ProjectModel](https://bryntum.com/products/gantt/docs/api/Gantt/model/ProjectModel).

In `Ext Gantt`, any node can be specified as a `Gnt.model.Project` by specifying the `TaskType` data attribute
(See `load.json` in the advanced example). This approach cannot be directly ported to vanilla because vanilla
project is a wrapper class that encapsulates all Gantt stores, not just an extension of `TaskModel`.

Also, the vanilla project has built-in [CrudManager](https://bryntum.com/products/gantt/docs/api/Scheduler/crud/AbstractCrudManagerMixin). That
means that all configuration options of `CrudManager` are also applicable to `project`. Vanilla project is a mandatory
config option (an empty project is created if not set from application) and it is a "central hub" for configuring
data-related options.

### Task scheduling modes

The set of supported scheduling modes has been slightly changed in the new Gantt.
There are four supported modes `Normal`, `FixedDuration`, `FixedEffort` and `FixedUnits`.

Ext Gantt `EffortDriven` mode was renamed to `FixedEffort` in the new Gantt.
And a new special [effortDriven](#Gantt/model/TaskModel#field-effortDriven) boolean flag was added to configure tasks more flexibly.

The old `DynamicAssignment` mode was removed since in the new Gantt it's just a combination
of [schedulingMode](#Gantt/model/TaskModel#field-schedulingMode) set to `FixedDuration` with [effortDriven](#Gantt/model/TaskModel#field-effortDriven) flag set to `true`.

A new `FixedUnits` mode was added, in which the assignment units are a fixed (means user provided
and it will not be recalculated automatically) value.
In this mode, changing the [effort](#Gantt/model/TaskModel#field-effort) causes recalculation
of the task [duration](#Gantt/model/TaskModel#field-duration) and vice versa
[duration](#Gantt/model/TaskModel#field-duration) changes result recalculating
the task [effort](#Gantt/model/TaskModel#field-effort).

### Changes in the data package

There are a few key differences between the old and new CRUD protocols, which do not allow to simply load the same data.
Here is a list of differences:

* General changes:
  * Field names are camel cased, StartDate -> startDate.
  * Project meta information is defined in `project` section. It includes project calendar and project start date.
* Tasks:
  * Baselines should be an array.
  * `TaskType` field is no longer supported. It was mainly used to tell project node from task node, but is no longer
    required.
  * `leaf` field does not exist either. A node becomes a parent node only if it has at least one child node.
  * `schedulingMode` field set of supported modes has been changed. See details in
    [Task scheduling modes](##task-scheduling-modes) chapter.
* Calendars:
  * Calendar is described by 3 fields: `id`, `name` and `intervals`.
  * `Days` and `DefaultAvailability` fields were replaced by single `intervals` field, which uses different syntax
    to define working/non-working time.
  * `hoursPerDay/daysPerWeek/daysPerMonth` fields are moved from calendar to the project data (please see
    [Restoring calendar level duration converting](##restoring-calendar-level-duration-converting) chapter for details
    on how the old behavior can be achieved).
* Dependencies:
  * Fields are renamed: `From` -> `fromTask`, `To` -> `toTask`.
* Assignments:
  * Fields are renamed: `TaskId` -> `event`, `ResourceId` -> `resource`.

Some differences like field names could be fixed by using [field mapping](https://bryntum.com/products/gantt/docs/api/Core/data/Model#field-data-mapping) via
the [dataSource](https://bryntum.com/products/gantt/docs/api/Core/data/field/DataField#config-dataSource) model field
config option. Other differences, such as intervals, baselines, metadata require changes on the backend. When implementing backend
changes we recommend changing field names to camel case so that no name mapping is needed.

In this example, we change the original JSON file with data to demonstrate the changes that will need to be implemented
on the server.

### Project basics

In Bryntum Gantt, the CRUD Manager is a mixin consumed by a <code>ProjectModel</code>. The ProjectModel is a mega-store
which encapsulates all the Gantt-related data stores (tasks, calendars, resources etc) and manages all communication
with the backend (<code>load</code> & <code>sync</code>) but can also work without a backend using inline data.

The other main purpose of the ProjectModel is to schedule tasks according to the defined calendars and dependencies -
to calculate the project. In the Ext Gantt, these calculations where made by the <code>TaskStore</code>, but now it is
Project's responsibility. A typical workflow using a project can be described with this small code snippet:

```javascript
// create project which loads data from a URL
const project = new ProjectModel({
    autoLoad  : true,
    transport : {
        load : {
            url : 'load'
        },
        sync : {
            url : 'sync'
        }
    }
});

// Commit pending changes and wait for asynchronous project calculation
await project.commitAsync()

// Changing duration using accessor will schedule another commit after 100ms
project.taskStore.getById(1).duration = 2;

// But we want to force it...
await project.commitAsync();

// ...to store changes ASAP
return project.sync();
```

Now we add `project` configuration to Gantt in `main.js` so that it reads:

```javascript
import { Gantt } from '@bryntum/gantt';
import './style.css'

const gantt = new Gantt({
    appendTo: 'app',

    project: {
        transport: {
            load: {
                url: 'data/load.json',
                paramName: 'q'
            }
        },
        autoLoad: true,
    }
});
```

Then copy `load.json` data file from the
[Advanced Gantt Chart Demo for Ext] (https://bryntum.com/products/gantt-for-extjs/examples/advanced/#en)
to `public/data/` folder.

You can run the app now to verify that `load.json` is really loaded but UI will only show icons in the first column. We
need to change field names to display the data. For that, edit the file and change the field names:

| From                  | To                    |
|-----------------------|-----------------------|
| `"Id"`                | `"id"`                |
| `"Name"`              | `"name"`              |
| `"StartDate"`         | `"startDate"`         |
| `"EndDate"`           | `"endDate"`           |
| `"Description"`       | `"description"`       |
| `"PercentDone"`       | `"percentDone"`       |
| `"Duration"`          | `"duration"`          |
| `"Rollup"`            | `"rollup"`            |
| `"Cls"`               | `"cls"`               |
| `"Segments"`          | `"segments"`          |
| `"Resizable"`         | `"resizable"`         |
| `"AllowDependencies"` | `"allowDependencies"` |
| `"ShowInTimeline"`    | `"showInTimeline"`    |
| `"ConstraintType"`    | `"constraintType"`    |
| `"ConstraintDate"`    | `"constraintDate"`    |
| `"Draggable"`         | `"draggable"`         |
| `"Rate"`              | `"rate"`              |
| `"PerUseCost"`        | `"perUseCost"`        |
| `"TaskId"`            | `"taskId"`            |
| `"ResourceId"`        | `"resourceId"`        |
| `"Units"`             | `"units"`             |
| `"From"`              | `"fromTask"`          |
| `"To"`                | `"toTask"`            |

Now we widen the first column with `Name` by adding the following to the Gantt configuration:

```javascript
subGridConfigs : {
    locked : {
        flex : 1
    },
    normal : {
        flex : 3
    }
}
```

You should now see Gantt similar to this:

<img src="data/Gantt/images/migration/gantt-with-tasks.png" alt="Gantt with tasks"/>

## Step 4: Correct project and calendar

Values in the `project` property in the server response (JSON) are applied to the `ProjectModel` of the Gantt. Add the following to `load.json`:

```javascript
"project" : {
    "calendar"     : "general",
    "startDate"    : "2017-01-16",
    "hoursPerDay"  : 24,
    "daysPerWeek"  : 5,
    "daysPerMonth" : 20
},
```

Now we need to correct data for calendars. The original format of calendars is not valid anymore so we replace it with the
following data:

```json
"calendars" : {
    "rows"  : [
        {
            "id"        : "general",
            "name"      : "General",
            "intervals" : [
                {
                    "recurrentStartDate" : "on Sat",
                    "recurrentEndDate"   : "on Mon",
                    "isWorking"          : false
                },
                {
                    "name"      : "Some big holiday",
                    "startDate" : "2017-02-01",
                    "endDate"   : "2017-02-02",
                    "isWorking" : false,
                    "cls"       : "holiday"
                },
                {
                    "name"      : "Chinese New Year",
                    "startDate" : "2017-01-11",
                    "endDate"   : "2017-01-12",
                    "isWorking" : false,
                    "cls"       : "holiday"
                },
                {
                    "name"      : "Additional holiday",
                    "startDate" : "2017-02-15",
                    "endDate"   : "2017-02-18",
                    "isWorking" : false,
                    "cls"       : "holiday"
                }
            ]
        }
    ]
},
```

To make holidays visually different from weekends, add the following css class to `style.css`.

```css
.b-sch-time-range.holiday {
    background-color : rgba(255, 210, 210, 0.5);
}
```

We also want to use task labels similar to the original ExtJS demo so let's add the following to the the Gantt config:

```javascript
startDate : '2017-01-08',
features : {
    labels : {
        left : {
            field : 'name'
        }
    }
}
```

`startDate` defined on Gantt is where its time axis starts. `startDate` in the `project` defines where the
project starts.
The `labels` feature (disabled by default) displays labels besides (or above or below) tasks.
Here we link the label to task names, but it can be linked to any available field. Please consult the
[Labels Feature](#Gantt/feature/Labels) documentation for complete information on labels.

Please refer to the [Calendar Guide](#Gantt/guides/basics/calendars.md) to get complete information
about the calendar implementation.

The Gantt should now look similar to this screenshot:
<img src="data/Gantt/images/migration/gantt-with-calendars.png" alt="Gantt with calendars"/>

You can download the converted `load.json` file [here](data/Gantt/guides/migration/load.json).

## Step 5: Add Timeline widget

Timeline and Gantt will use same `project` so we refactor `main.js` slightly:

```javascript
import { Gantt, ProjectModel, Timeline } from '@bryntum/gantt';
import './style.css'

const project = new ProjectModel({
    transport: {
        load: {
            url: 'data/load.json',
            paramName: 'q'
        }
    },
    autoLoad: true,
});

const timeline = new Timeline({
    appendTo: 'app',
    project,
    height: '12em'
});

const gantt = new Gantt({
    appendTo: 'app',
    project,
    // etc
});
```

We have removed the `project` configuration from Gantt, we have created an instance of the `ProjectModel` and we used
this instance for both the timeline and the Gantt. We append both timeline and gantt to the same DOM element `'app'`.

We add the columns configuration so that it reads:

```javascript
features : {
    labels : {
        left : {
            field : 'name'
        }
    },
    filterBar : {
        keyStrokeFilterDelay : 100
    }
},
columns : [
    { type : 'wbs', filterable: false},
    { type : 'name', width: 250},
    { type : 'startdate' },
    { type : 'enddate' },
    { type : 'duration' },
    { type : 'constrainttype' },
    { type : 'constraintdate' },
    { type : 'percentdone', width : 70 },
    {
        type  : 'predecessor',
        width : 112
    },
    { type : 'addnew' }
],
subGridConfigs : {
    locked : {
        flex : 1.3
    },
    normal : {
        flex : 3
    }
},
```

Here we added `filterBar` to `features` to make the columns filterable, except WBS column.
We also made the left subgrid slightly wider. The browser should now show:

<img src="data/Gantt/images/migration/gantt-with-timeline.png" alt="Gantt with timeline"/>

## Step 6: Add toolbar

First of all we create folder `lib` and file `GanttToolbar.js` in this folder.

### Toolbar with Create and Remove buttons

We add the following code to the file:

```javascript
import { Toolbar } from '@bryntum/gantt';

export default class GanttToolbar extends Toolbar {

    static type = 'gantttoolbar';
    static $name = 'GanttToolbar';

    static configurable = {
        items : {
            addTaskButton : {
                color    : 'b-green',
                icon     : 'fa fa-plus',
                text     : 'Create',
                tooltip  : 'Create new task',
                onClick  : 'up.onAddTaskClick'
            },
            deleteTaskButton : {
                color    : 'b-red',
                icon     : 'fa fa-minus',
                tooltip  : 'Remove selected task',
                onClick  : 'up.onRemoveTaskClick',
                disabled : true
            }
        }
    }

    construct(...args) {
        super.construct(...args);

        // Save the gantt instance for use in handlers
        const gantt = this.gantt = this.parent;

        gantt.on({
            selectionChange: this.onSelectionChange
        });
    }

    onSelectionChange({ selected }){
        this.widgetMap.deleteTaskButton.disabled = !Boolean(selected.length);
    }

    onRemoveTaskClick() {
        const { gantt } = this;
        gantt.selectedRecords.forEach(task => {
            gantt.taskStore.remove(task);
        });
    }
}

// Register this widget
GanttToolbar.initClass();
```

This code defines a custom toolbar for a Gantt chart with two buttons: one for adding tasks and another for removing
selected tasks. The toolbar reacts to selection changes in the Gantt chart and enables/disables the "Remove" button
accordingly.

Now we use the toolbar in Gantt `main.js`:

```javascript
import GanttToolbar from './lib/GanttToolbar';

// etc.

const gantt = new Gantt({
    // etc.
    tbar : {
        type : 'gantttoolbar'
    }
    // etc.
});
```

Running the code at this point should show the toolbar at the top of the Gantt with "Create" and "Remove" buttons on
the left. The buttons work as expected.

If we look at the `onClick` configuration we see that they are not functions but strings. The strings have `up.`
prefix followed by the name of the function. This notation means that the function is implemented in a parent of the
button, which is the toolbar in this case.

This approach is a usual practice: instead of implementing item handlers inline, they are implemented on an upper
level component.

### Navigation buttons

Now we add more buttons to static `configurable.items` object in `GanttToolbar.js`:

```javascript
toggleButtons : {
    type  : 'buttonGroup',
    items : {
        expandAllButton : {
            icon     : 'fa fa-angle-double-down',
            tooltip  : 'Expand all',
            onClick  : 'up.onExpandAllClick'
        },
        collapseAllButton : {
            icon     : 'fa fa-angle-double-up',
            tooltip  : 'Collapse all',
            onClick  : 'up.onCollapseAllClick'
        }
    }
},
zoomButtons : {
    type  : 'buttonGroup',
    items : {
        zoomInButton : {
            icon     : 'fa fa-search-plus',
            tooltip  : 'Zoom in',
            onClick : 'up.onZoomInClick'
        },
        zoomOutButton : {
            icon     : 'fa fa-search-minus',
            tooltip  : 'Zoom out',
            onClick : 'up.onZoomOutClick'
        },
        zoomToFitButton : {
            icon     : 'fa fa-compress-arrows-alt',
            tooltip  : 'Zoom to fit',
            onClick : 'up.onZoomToFitClick'
        },
        previousButton : {
            icon     : 'fa fa-angle-left',
            tooltip  : 'Previous time span',
            onClick : 'up.onShiftPreviousClick'
        },
        nextButton : {
            icon     : 'fa fa-angle-right',
            tooltip  : 'Next time span',
            onClick : 'up.onShiftNextClick'
        }
    }
},
```

and their handlers too:

```javascript
onExpandAllClick() {
    this.gantt.expandAll();
}

onCollapseAllClick() {
    this.gantt.collapseAll();
}

onZoomInClick() {
    this.gantt.zoomIn();
}

onZoomOutClick() {
    this.gantt.zoomOut();
}

onZoomToFitClick() {
    this.gantt.zoomToFit({
        leftMargin  : 50,
        rightMargin : 50
    });
}

onShiftPreviousClick() {
    this.gantt.shiftPrevious();
}

onShiftNextClick() {
    this.gantt.shiftNext();
}
```

### Undo/Redo buttons

We add Undo/Redo buttons between remove button and navigation buttons:

```javascript
undoRedo : {
    type  : 'undoredo',
    items : {
        transactionsCombo : null
    }
},
```

We also need to enable STM (State Tracking Manager) in `main.js`. We add this configuration to the `project`:

```javascript
stm : {
    autoRecord : true
},
```

### Settings menu button

The settings button opens a menu of various options that can be changed to illustrate the possibilities
of configuration.

First add the following configuration to `items` object in `GanttToolbar.js`:

```javascript
featuresButton : {
    type    : 'button',
    icon    : 'fa fa-tasks',
    text    : 'Settings',
    tooltip : 'Toggle features',
    menu    : {
        onItem       : 'up.onFeaturesClick',
        onBeforeShow : 'up.onFeaturesShow',
        // "checked" is set to a boolean value to display a checkbox for menu items. No matter if it is true or false.
        // The real value is set dynamically depending on the "disabled" config of the feature it is bound to.
        items        : {
            settings : {
                text : 'UI settings',
                icon : 'fa-sliders-h',
                menu : {
                    cls         : 'settings-menu',
                    layoutStyle : {
                        flexDirection : 'column'
                    },
                    onBeforeShow : 'up.onSettingsShow',
                    defaults     : {
                        type      : 'slider',
                        showValue : true
                    },
                    items : [
                        {
                            ref     : 'rowHeight',
                            text    : 'Row height',
                            min     : 30,
                            max     : 70,
                            onInput : 'up.onRowHeightChange'
                        },
                        {
                            ref     : 'barMargin',
                            text    : 'Bar margin',
                            min     : 0,
                            max     : 10,
                            onInput : 'up.onBarMarginChange'
                        },
                        {
                            ref     : 'duration',
                            text    : 'Animation duration',
                            min     : 0,
                            max     : 2000,
                            step    : 100,
                            onInput : 'up.onAnimationDurationChange'
                        },
                        {
                            ref     : 'radius',
                            text    : 'Dependency radius',
                            min     : 0,
                            max     : 10,
                            onInput : 'up.onDependencyRadiusChange'
                        }
                    ]
                }
            }
        }
    }
}
```

That adds the "Settings" button with one menu item "UI Settings" which contains a submenu with sliders that
control various UI variables.

We need to add the following handlers to make them work:

```javascript
onFeaturesClick({ source : item }) {
    const { gantt } = this;

    if (item.feature) {
        const feature = gantt.features[item.feature];
        feature.disabled = !feature.disabled;
    }
    else if (item.subGrid) {
        const subGrid = gantt.subGrids[item.subGrid];
        subGrid.collapsed = !subGrid.collapsed;
    }
    else if (item.toggleConfig) {
        gantt[item.toggleConfig] = item.checked;
    }
}

onFeaturesShow({ source : menu }) {
    const { gantt } = this;

    menu.items.map(item => {
        const { feature } = item;

        if (feature) {
            // a feature might be not presented in the gantt
            // (the code is shared between "advanced" and "php" demos which use a bit different set of features)
            if (gantt.features[feature]) {
                item.checked = !gantt.features[feature].disabled;
            }
            // hide not existing features
            else {
                item.hide();
            }
        }
        else if (item.subGrid) {
            item.checked = gantt.subGrids[item.subGrid].collapsed;
        }
    });
}

onSettingsShow({ source : menu }) {
    const
        { gantt }                                  = this,
        { rowHeight, barMargin, duration, radius } = menu.widgetMap;

    rowHeight.value = gantt.rowHeight;
    barMargin.value = gantt.barMargin;
    barMargin.max = (gantt.rowHeight / 2) - 5;
    duration.value = gantt.transitionDuration;
    radius.value = gantt.features.dependencies.radius ?? 0;
}

onRowHeightChange({ value, source }) {
    this.gantt.rowHeight = value;
    source.owner.widgetMap.barMargin.max = (value / 2) - 5;
}

onBarMarginChange({ value }) {
    this.gantt.barMargin = value;
}

onAnimationDurationChange({ value }) {
    this.gantt.transitionDuration = value;
    this.styleNode.innerHTML = `.b-animating .b-gantt-task-wrap { transition-duration: ${value / 1000}s !important; }`;
}

onDependencyRadiusChange({ value }) {
    this.gantt.features.dependencies.radius = value;
}
```

We also need to add `styleNode` in `construct()` function:

```javascript
this.styleNode = document.createElement('style');
document.head.appendChild(this.styleNode);
```

Also, add the following to `style.css`:

```css
.settings-menu .b-menu-content{
    padding: 0.5em;
}
.settings-menu .b-slider{
    width: 12em;
    margin-bottom: 0.5em;
}
```

That makes the menu and sliders look better.

Now we add all other menu items with features. Paste them into the `featureButton` just after `settings`:

```javascript
drawDeps : {
    text    : 'Draw dependencies',
    feature : 'dependencies',
    checked : false
},
taskLabels : {
    text    : 'Task labels',
    feature : 'labels',
    checked : false
},
criticalPaths : {
    text    : 'Critical paths',
    feature : 'criticalPaths',
    tooltip : 'Highlight critical paths',
    checked : false
},
projectLines : {
    text    : 'Project lines',
    feature : 'projectLines',
    checked : false
},
nonWorkingTime : {
    text    : 'Highlight non-working time',
    feature : 'nonWorkingTime',
    checked : false
},
cellEdit : {
    text    : 'Enable cell editing',
    feature : 'cellEdit',
    checked : false
},
autoEdit : {
    text    : 'Auto edit',
    checked : false,
    onItem  : 'up.onAutoEditToggle'
},
columnLines : {
    text    : 'Show column lines',
    feature : 'columnLines',
    checked : true
},
baselines : {
    text    : 'Show baselines',
    feature : 'baselines',
    checked : false
},
rollups : {
    text    : 'Show rollups',
    feature : 'rollups',
    checked : false
},
progressLine : {
    text    : 'Show progress line',
    feature : 'progressLine',
    checked : false
},
parentArea : {
    text    : 'Show parent area',
    feature : 'parentArea',
    checked : false
},
fillTicks : {
    text         : 'Stretch tasks to fill ticks',
    toggleConfig : 'fillTicks',
    checked      : false
},
hideSchedule : {
    text    : 'Hide schedule',
    cls     : 'b-separator',
    subGrid : 'normal',
    checked : false
}
```

We already have the features handler so they already work. We only need to configure all available features. For that
add the following configs to the `features` object in Gantt configuration in `main.js`:

```javascript
baselines : {
    disabled : true
},
dependencies : {
    showLagInTooltip : true,
    // Soften up dependency line corners
    radius           : 3,
    // Make dependencies easier to reach using the mouse
    clickWidth       : 5
},
dependencyEdit : true,
parentArea : {
    disabled : true
},
progressLine : {
    disabled   : true,
    statusDate : new Date(2019, 0, 25)
},
rollups : {
    disabled : true
},
rowResize : {
    cellSelector : '.b-rownumber-cell'
},
rowReorder : {
    showGrip        : true,
    preserveSorters : true
},
timeRanges : {
    showCurrentTimeLine : true
},
fillHandle    : true,
cellCopyPaste : true,
taskCopyPaste : {
    useNativeClipboard : true
}
```

## Step 7: Baselines

Data structure for baselines are changed in the new version, so we need to edit our `load.json` which means that the server-side API
has to be updated too.

We need to change the tasks that have baselines defined to the new structure. The following example
illustrates the necessary changes:

### Old structure

```json
"id"                : 1,
"name"              : "Planning",
"BaselineStartDate" : "2017-01-13",
"BaselineEndDate"   : "2017-01-30"
```

### New structure

```json
"id"                : 1,
"name"              : "Planning",
"baselines"         : [
    {
        "startDate" : "2017-01-13",
        "endDate"   : "2017-01-30"
    }
]
```

With all the above changes done and after reloading the application and enabling baselines, you should get a result
similar to the following screenshot:

<img src="data/Gantt/images/migration/gantt-with-baselines.png" alt="Gantt with baselines"/>

## Step 8: Custom TaskModel and task editor

If we need custom fields in addition to the [default TaskModel fields](#Gantt/model/TaskModel#fields), we need to extend
`TaskModel` and add these fields in the extension. For that, create `lib/CustomTaskModel.js` file and populate it with
this content:

```javascript
import { TaskModel } from '@bryntum/gantt';

export default class CustomTaskModel extends TaskModel {
    static $name = 'CustomTaskModel';

    static fields = [{
        name: 'customField',
        type: 'string'
    }]
}
```

Then we import the class in `main.js` and use it as value of `taskModelClass` config option in `project`.

```javascript
import CustomTaskModel from './lib/CustomTaskModel';

const project = new ProjectModel({
    transport: {
        load: {
            url: 'data/load.json',
            paramName: 'q'
        }
    },
    taskModelClass: CustomTaskModel,
    stm : {
        autoRecord : true
    },
    autoLoad: true,
});
```

Now we add `customField` to task edit popup. We do it in Gantt `features` configuration:

```javascript
features : {
    taskEdit : {
        items : {
            generalTab : {
                items : {
                    customField : {
                        type   : 'textfield',
                        label  : 'Custom',
                        name   : 'customField',
                        weight : 150
                    }
                }
            }
        }
    },
// etc
```

This configuration adds a text field to the General Tab, link it to `customField` in model by `name` property and shows the field below the task name field. The customized task editor will look similar to this:

<img src="data/Gantt/images/migration/gantt-task-editor.png" alt="Gantt task editor"/>

There is a plethora of other ways to configure the task editor. Consult please the
[API Documentation](#Gantt/feature/TaskEdit) to learn about them.

## Step 9: Localization

Bryntum Gantt ships with 35 locales and it is not very difficult to add language changing support to the application.
We will implement English plus 2 additional languages with the language selector combo in this example.

### Import locales

Create folder `locales` and the following files in that folder:

* locales.js
* locale.En.js
* locale.Es.js
* locale.SvSE.js

and populate them with these contents:

`locales.js`:

```javascript
import './locale.En';
import './locale.Es';
import './locale.SvSE';
```

`locale.En.js`:

```javascript
import { LocaleHelper } from '@bryntum/gantt';
import '@bryntum/gantt/locales/gantt.locale.En';

const locale = {

    localeName : 'En',
    localeDesc : 'English (US)',
    localeCode : 'en-US',
};

export default LocaleHelper.publishLocale(locale);
```

`locale.Es.js`:

```javascript
import { LocaleHelper } from '@bryntum/gantt';
import '@bryntum/gantt/locales/gantt.locale.Es';

const locale = {

    localeName : 'Es',
    localeDesc : 'Español',
    localeCode : 'es',
};

export default LocaleHelper.publishLocale(locale);
```

`locale.SvSE.js`:

```javascript
import { LocaleHelper } from '@bryntum/gantt';
import '@bryntum/gantt/locales/gantt.locale.SvSE';

const locale = {

    localeName : 'SvSE',
    localeDesc : 'Svenska',
    localeCode : 'sv-SE',
};

export default LocaleHelper.publishLocale(locale);
```

The individual locales first import the corresponding Gantt locale and then publish it. It seems not necessary but we will add the application translations to these files that will add to the Gantt translations. For example, dates such as "Start date", "End date" are already translated in the default Gantt locale, however, we need to add the application specific translations.

`locales.js` works as a central hub of imports; we can add or remove the available languages here without changing the
remaining application code.

Now we import locales in `main.js`:

```javascript
import './locales/locales';
```

### Add the language combo

We will now work in `GanttToolbar.js`. The first step is to add the following combo code after `featuresButton`:

```javascript
localeCombo : {
    type         : 'combo',
    label        : 'L{Language}',
    width        : '25em',
    displayField : 'text',
    valueField   : 'value',
    editable     : false,
    onAction     : 'up.onLocaleChange'
}
```

Label of the combo is written in the special localizable format which instructs the translation software to replace
the string between curly braces with the translation. If the localization has not been activated or if the translation
is missing this special string is shown as the label.

Now populate combo with data of available locales and set the value to the default (English) locale.
For that, add the following code to `construct()` method:

```javascript
let locales = [];

Object.keys(me.localeManager.locales).map(key => {
    const locale = me.localeManager.locales[key];
    locales.push({
        value : key,
        text  : locale.localeDesc,
        data  : locale
    });
});

me.widgetMap.localeCombo.store.data = locales;
me.widgetMap.localeCombo.value = me.localeManager.locale.localeName;
```

<div class="note">
<code>widgetMap</code> is an object which contains a map of descendant widgets keyed by their <code>ref</code> or property name. See <a href="https://bryntum.com/products/gantt/docs/api/Core/widget/Container#property-widgetMap">the documentation</a> for more details.
</div>

We also need the handler; the following function added to `GanttToolbar` class:

```javascript
onLocaleChange({ value }) {
    const me = this;
    me.localeManager.applyLocale(value);

    Toast.show({
        html        : me.L('L{Locale changed}'),
        rootElement : document.body
    });
}
```

**_Note:_** We also need to `import { Toast } from '@bryntum/gantt';`.

### Add translations

The localization setup is completed at this point; now we need to work on the translations themselves. The first step
is to change all text in the application from `'Plain text'` to `'L{Plain text}'`. Then we need to add translations
to `locale` object in our locale files.

`locale.En.js`:

```javascript
Combo : {
    Language : 'Language',
},

GanttToolbar : {
    'Locale changed' : 'Locale changed',
},

Button : {
    Settings : 'Settings',
    Create : 'Create'
},

Tooltip : {
    'Toggle features' : 'Toggle features',
    'Create new task' : 'Create new task',
    'Remove selected task' : 'Remove selected task',
    'Expand all' : 'Expand all',
    'Collapse all' : 'Collapse all',
    'Zoom in' : 'Zoom in',
    'Zoom out' : 'Zoom out',
    'Zoom to fit' : 'Zoom to fit',
    'Previous time span' : 'Previous time span',
    'Next time span' : 'Next time span'
},

MenuItem : {
    'UI settings': 'UI settings',
    'Draw dependencies' : 'Draw dependencies',
    'Task labels' : 'Task labels',
    'Critical paths' : 'Critical paths',
    'Project lines' : 'Project lines',
    'Highlight non-working time' : 'Highlight non-working time',
    'Enable cell editing' : 'Enable cell editing',
    'Auto edit' : 'Auto edit',
    'Show column lines' : 'Show column lines',
    'Show baselines' : 'Show baselines',
    'Show rollups' : 'Show rollups',
    'Show progress line' : 'Show progress line',
    'Show parent area' : 'Show parent area',
    'Stretch tasks to fill ticks' : 'Stretch tasks to fill ticks',
    'Hide schedule' : 'Hide schedule'
},

Slider : {
    'Row height' : 'Row height',
    'Bar margin' : 'Bar margin',
    'Animation duration' : 'Animation duration',
    'Dependency radius' : 'Dependency radius'
}
```

`locale.Es.js`:

```javascript
Combo : {
    Language : 'Idioma',
},

GanttToolbar : {
    'Locale changed' : 'Idioma cambiado',
},

Button : {
    Settings : 'Ajustes',
    Create : 'Crear'
},

Tooltip : {
    'Toggle features' : 'Alternar funciones',
    'Create new task' : 'Crear nueva tarea',
    'Remove selected task' : 'Eliminar tarea seleccionada',
    'Expand all' : 'Expandir todo',
    'Collapse all' : 'Desplegar todo',
    'Zoom in' : 'Hacer zoom',
    'Zoom out' : 'Disminuir el zoom',
    'Zoom to fit' : 'Acercar para ajustar',
    'Previous time span' : 'Período de tiempo anterior',
    'Next time span' : 'Próximo intervalo de tiempo'
},

MenuItem : {
    'UI settings': 'Configuración de UI',
    'Draw dependencies' : 'Dibujar dependencias',
    'Task labels' : 'Etiquetas de tareas',
    'Critical paths' : 'Rutas críticas',
    'Project lines' : 'Líneas de proyecto',
    'Highlight non-working time' : 'Resaltar tiempo no laborable',
    'Enable cell editing' : 'Habilitar edición de celdas',
    'Auto edit' : 'Edición automática',
    'Show column lines' : 'Mostrar líneas de columnas',
    'Show baselines' : 'Mostrar líneas base',
    'Show rollups' : 'Mostrar resúmenes',
    'Show progress line' : 'Mostrar línea de progreso',
    'Show parent area' : 'Mostrar área principal',
    'Stretch tasks to fill ticks' : 'Estirar tareas para llenar ticks',
    'Hide schedule' : 'Ocultar horario'
},

Slider : {
    'Row height' : 'Alto de fila',
    'Bar margin' : 'Margen de barra',
    'Animation duration' : 'Duración de la animación',
    'Dependency radius' : 'Radio de dependencia'
}
```

`locale.SvSE.js`:

```javascript
Combo : {
    Language : 'Välj språk',
},

GanttToolbar : {
    'Locale changed' : 'Språk ändrat'
},

Button : {
    Settings : 'Inställningar',
    Create : 'Skapa'
},

Tooltip : {
    'Toggle features' : 'Växla funktioner',
    'Create new task' : 'Skapa ny uppgift',
    'Remove selected task' : 'Ta bort vald uppgift',
    'Expand all' : 'Utöka alla',
    'Collapse all' : 'Komprimera alla',
    'Zoom in' : 'Zooma in',
    'Zoom out' : 'Zooma ut',
    'Zoom to fit' : 'Zooma för att passa',
    'Previous time span' : 'Föregående tidsspann',
    'Next time span' : 'Nästa tidsspann'
},

MenuItem : {
    'UI settings': 'UI-inställningar',
    'Draw dependencies' : 'Rita beroenden',
    'Task labels' : 'Uppgiftsetiketter',
    'Critical paths' : 'Kritiska vägar',
    'Project lines' : 'Projektlinjer',
    'Highlight non-working time' : 'Markera icke-arbetstid',
    'Enable cell editing' : 'Aktivera cellredigering',
    'Auto edit' : 'Autoredigera',
    'Show column lines' : 'Visa kolumnrader',
    'Show baselines' : 'Visa baslinjer',
    'Show rollups' : 'Visa sammanställningar',
    'Show progress line' : 'Visa förloppsrad',
    'Show parent area' : 'Visa överordnat område',
    'Stretch tasks to fill ticks' : 'Stretchuppgifter för att fylla bockar',
    'Hide schedule' : 'Dölj schema'
},

Slider : {
    'Row height' : 'Radhöjd',
    'Bar margin' : 'Stapelmarginal',
    'Animation duration' : 'Animationens varaktighet',
    'Dependency radius' : 'Beroenderadie'
}
```

## Step 10 (optional): Theming and styling

### Using themes

In Step 2 we have imported the `gantt.css` & `svalbard-light.css` files, which gave our new Gantt application the
default look. Bryntum components ship with the following themes you can choose from:

1. Svalbard (`svalbard-light/dark.css`) - default
2. Visby (`visby-light/dark.css`)
3. Stockholm (`stockholm-light/dark.css`)
4. Material3 (`material2-light/dark.css`)
5. Fluent2 (`fluent2-light/dark.css`)

You can import any of these themes the same way we have done above:

```css
@import './node_modules/@bryntum/gantt/visby-dark.css';
```

The theme imported this way is processed by the application builder (Vite in our case) to produce the final css file(s)
of the application. The theme then cannot be changed dynamically at runtime.

The theme can also be linked in the application html file with:

```html
<html>
    <head>
        <link rel="stylesheet" href="./css/gantt.css">
        <link rel="stylesheet" href="./css/svalbard-light.css" data-bryntum-theme>
```

If the themes are loaded this way we must make them available by copying their files to `public/css` folder.
Implementation of theme switching would then be easy and it would involve implementation of  a combo with the
available theme names and a change handler that would call
[DomHelper.setTheme](#Core/helper/DomHelper#function-setTheme-static) with the theme name selected in
the combo. This approach is used in used in our [vanilla examples](https://bryntum.com/examples/gantt).

### Styling

Every Bryntum component and widget undergoes meticulous styling to ensure they are visually appealing. However,
you may want to adjust their appearance to match your liking or the design of your application. The styling has
been made very easy and is usually approached by defining a custom CSS class and then applying this class to the
selected places.

For example, for button, we can set:

```javascript
const button = new Button({
    appendTo  : document.body,
    rendition : 'elevated',
    cls       : 'custom-button',
});
```

Here we use predefined `elevated` rendition plus custom class `custom-button`.

Or we can style tasks by setting `cls` in the data file (`load.json`):

```json
  "tasks" : {
        "rows" : [
            {
                "id"          : 1,
                "name"        : "Planning",
                "cls"         : "planning-task",
                "percentDone" : 50,
                "startDate"   : "2017-01-16",
```

`planning-task` CSS class will be applied to the task.

There is a plethora of styling possibilities such as using [renderers](#Gantt/view/GanttBase#config-taskRenderer),
changing task [colors](#Gantt/model/TaskModel#field-eventColor) and many other.

The [Styling guide](#Gantt/guides/customization/styling.md) offers comprehensive information regarding styling
and adjusting appearance.

## Restoring calendar level duration converting

In the Gantt for Ext JS each calendar keeps own conversion rates. The approach was quite
controversial and caused a lot of questions. So it was decided to change that in the new Gantt and move
`hoursPerDay/daysPerWeek/daysPerMonth` fields to the project.

But if your application relies on that behavior it's possible to have this in the new Bryntum Gantt too.
It can be done with the following code:

```javascript
// Make calendars capable of converting durations.
// This will add "hoursPerDay", "daysPerWeek" and "daysPerMonth" fields to MyCalendarModel model
class MyCalendarModel extends DurationConverterMixin.derive(CalendarModel) {}

class MyDependencyModel extends DependencyModel {

    * convertLagGen(duration, fromUnit, toUnit) {
        // use the dependency calendar as lag converter
        const converter = yield this.$.calendar;

        return yield* converter.$convertDuration(duration, fromUnit, toUnit);
    }

}

class MyTaskModel extends TaskModel {

    * convertDurationGen(duration, fromUnit, toUnit) {
        // use the task calendar as duration converter
        const converter = yield this.$.effectiveCalendar;

        return yield* converter.$convertDuration(duration, fromUnit, toUnit);
    }

    // Override to check that the task calendar is ready for converting
    canConvertDuration(duration, fromUnit, toUnit) {
        // sanitize provided units ("d", "days" -> "day", "ms" -> "millisecond" etc)
        toUnit   = DateHelper.normalizeUnit(toUnit);
        fromUnit = DateHelper.normalizeUnit(fromUnit);

        const calendar = this.effectiveCalendar;

        // can convert duration if its numeric and
        return typeof duration === 'number' &&
            // the task calendar is resolved and has needed conversion rates
            calendar?.unitsInMs?.[ fromUnit ] && calendar.unitsInMs[ toUnit ];
    }
}

new Gantt({
    project : {
        // tell the project to use own customized models
        calendarModelClass   : MyCalendarModel,
        taskModelClass       : MyTaskModel,
        dependencyModelClass : MyDependencyModel,
        ...
    },
    ...
})
```

## Summing up

Bryntum Gantt has nearly full <a href="https://bryntum.com/products/gantt-for-extjs/compare/">feature parity</a>
with Ext Gantt. Some APIs have been changed but overall the approach is very similar:

1. Components can be configured using a class name or by a type name (`xtype` in Ext JS, `type` in Bryntum Gantt) passed
   to a factory (container, panel or even widget factory - `Widget.create()`).
2. Components are flexible and can be configured with an object.
3. Containers can contain components organized into component trees of any depth.
4. Components can be queried by reference, resolved from DOM elements etc.
5. Concepts such as column, editor, model, store are almost identical to how things work in Ext Gantt.
6. In Ext Gantt there are both plugins and features - in Bryntum Gantt everything is a feature. Features can
also enabled / disabled at runtime.
7. The event system is almost identical: events are triggered, and can be listened to with the `on` method which returns
   a detacher function.

You can download the migrated example app [here](data/Gantt/guides/migration/ext-migration.zip).

For more information please refer to our other guides and docs and if you find yourself stuck while migrating,
please ask for help in our <a href="https://forum.bryntum.com">forums</a> and we will do our best to assist you.
