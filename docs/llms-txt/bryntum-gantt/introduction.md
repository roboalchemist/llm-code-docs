# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/understanding-data/introduction.md

# Introduction

Bryntum components are data-driven by design—data is not just an enhancement, it is a core requirement.
Whether you're rendering a Scheduler, Gantt chart, or Grid, each component depends on well-structured data to
function correctly.

This guide serves as an introduction to Bryntum’s data management concepts, helping you understand the underlying
data structures, loading mechanisms, and integration strategies needed to build functional and efficient applications.

Let's start by exploring the two main sources of data:

* Inline data
* Remote data

<img src="Gantt/data-sources.png" class="b-screenshot" alt="Sources of data">

## Inline data

The easiest way to feed data into your Bryntum Gantt is by using inline data. Just as HTML allows inline CSS,
you can include the data directly inside the `new Gantt({})` instance. Here's how to do it:

<div class="framework-tabs">
<div data-name="js">

```javascript
new Gantt({
    tasks : [
        {
            id       : 1,
            name     : 'Write docs',
            expanded : true,
            children : [
                { id : 2, name : 'Proof-read docs', startDate : '2020-01-02', endDate : '2020-01-05' },
                { id : 3, name : 'Release docs', startDate : '2020-01-09', endDate : '2020-01-10' }
            ]
        }
    ],

    dependencies : [
        { fromEvent : 2, toEvent : 3 }
    ]
})
```

</div>
<div data-name="react">

```javascript
const App = props => {
    const [tasks, setTasks] = useState([
        {
            id       : 1,
            name     : 'Write docs',
            expanded : true,
            children : [
                { id : 2, name : 'Proof-read docs', startDate : '2020-01-02', endDate : '2020-01-05' },
                { id : 3, name : 'Release docs', startDate : '2020-01-09', endDate : '2020-01-10' }
            ]
        }
    ]);
    const [dependencies, setDependencies] = useState([
        { fromEvent : 2, toEvent : 3 }
    ]);

    return <BryntumGantt tasks={tasks} dependencies={dependencies} />
}
```

</div>
<div data-name="vue">

```html
<bryntum-gantt :tasks="tasks" :dependencies="dependencies" />
```

```javascript
<script setup>
{/* other config */}

const
    tasks = reactive([
        {
            id       : 1,
            name     : 'Write docs',
            expanded : true,
            children : [
                { id : 2, name : 'Proof-read docs', startDate : '2020-01-02', endDate : '2020-01-05' },
                { id : 3, name : 'Release docs', startDate : '2020-01-09', endDate : '2020-01-10' }
            ]
        }
      ]),
    dependencies = reactive([
        { fromEvent : 2, toEvent : 3 }
    ])

</setup>
```

</div>
<div data-name="angular">

```html
<bryntum-gantt [tasks]="tasks" [dependencies]="dependencies"></bryntum-gantt>
```

```typescript
@Component()
export class AppComponent {
    tasks = [
        {
            id       : 1,
            name     : 'Write docs',
            expanded : true,
            children : [
                { id : 2, name : 'Proof-read docs', startDate : '2020-01-02', endDate : '2020-01-05' },
                { id : 3, name : 'Release docs', startDate : '2020-01-09', endDate : '2020-01-10' }
            ]
        }
    ]
    dependencies = [
        { fromEvent : 2, toEvent : 3 }
    ]
}
```

</div>
</div>

The above config results in the following Gantt:

<div class="external-example" data-file="Gantt/guides/readme/basic.js"></div>

## Remote data

Remote data can come from a static `.json` file hosted on a web server (e.g., in the `/public` folder of your project
or on a CDN), or it can be retrieved dynamically from a server through an API call (e.g., `data.php`).

If you have a `/data.php` endpoint, you can access the data as follows:

<div class="framework-tabs">
<div data-name="js">

```javascript
new Gantt({
    project : {
        loadUrl  : '/data.php',
        autoLoad : true // auto load on initialization
    }
})
```

</div>
<div data-name="react">

```javascript
// GanttConfig.tsx
import { BryntumGanttProps } from "@bryntum/gantt-react";

const ganttProps: BryntumGanttProps = {
    // other config
    project : {
        transport : {
            loadUrl : 'data.json' // can be replaced with an API endpoint (e.g. read.php)
        },
        autoLoad : true // auto load on initialization
    }

};

export { ganttProps };
```

```javascript
import { ganttProps } from "./ganttProps";
// App.tsx
const App = props => {
    return <BryntumGantt {...ganttProps} />
}
```

</div>
<div data-name="vue">

```html
<script setup lang="ts">
import { BryntumGantt } from '@bryntum/gantt-vue-3';
import { ganttConfig } from './AppConfig.ts';
</script>

<template>
  <bryntum-gantt v-bind="ganttConfig" />
</template>
```

```javascript
import { type BryntumGanttProps } from '@bryntum/gantt-vue-3';

export const ganttConfig : BryntumGanttProps = {
    // other config
    project : {
        transport : {
            loadUrl : 'data.json' // can be replaced with an API endpoint (e.g. read.php)
        },
        autoLoad : true // auto load on initialization
    }
};
```

</div>
<div data-name="angular">

```html
<bryntum-gantt-project-model
    #project
    [startDate]="projectModelProps.startDate!"
    [endDate]="projectModelProps.endDate!"
    [calendar]="projectModelProps.calendar!"
    [loadUrl]="projectModelProps.loadUrl!"
    [autoLoad]="projectModelProps.autoLoad!"
></bryntum-gantt-project-model>
<bryntum-gantt
    #gantt
    [project]="project"
></bryntum-gantt>
```

```typescript
// app.config.ts
import {  BryntumGanttProjectModelProps } from '@bryntum/gantt-angular';

export const projectModelProps : BryntumGanttProjectModelProps = {
    loadUrl            : 'data.json', // can be replaced with an API endpoint (e.g. read.php)
    autoLoad           : true,
    autoSetConstraints : true
};
```

```typescript
// app.component.ts
import { projectModelProps } from './app.config';

export class AppComponent implements AfterViewInit {
    public projectModelProps = projectModelProps;
}
```

</div>
</div>

The `project` approach populates all stores in one request, reducing the API calls when loading the data.
Take a look at the load [request](#Gantt/guides/data/crud_manager_project.md#load-request-structure) or
[response](#Gantt/guides/data/crud_manager_project.md#load-response-structure) structure to understand how to work with
the `project`.

<div class="external-example" data-file="Gantt/guides/readme/intro.js"></div>

You can also use `axios` or `fetch` API:

```javascript
async function loadData() {
    const response = await fetch('backend/load.php');
    return await response.json();
}

// Extract data from loadData() via `await` or `.then`
// Assuming it has been saved to `data`

const gantt = new Gantt({
    project : {
        inlineData : data
    }
})

// or

gantt.project.inlineData = data;
```

Working with remote data is more complex as it offers multiple ways of interaction. Let's move on to the next topic to
learn more about how stores work.

Continue reading: [Understanding the `Store`](#Gantt/guides/understanding-data/store.md)
