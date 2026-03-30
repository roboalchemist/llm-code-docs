# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/vue-3.md

# Getting Started with Bryntum Gantt in Vue

## Try Vue demos

Bryntum Gantt is delivered with a variety of Vue demo applications showing its functionality.
All demo applications have been verified to be compatible with Node.js 20.

<div class="b-card-group-2">
<a href="https://bryntum.com/products/gantt/examples/?framework=vue" class="b-card"><i class="fas fa-globe"></i>View online Vue demos</a>
<a href="#Gantt/guides/integration/vue/guide.md#build-and-run-local-demos" class="b-card"><i class="fab fa-vuejs"></i>Build and run Vue demos</a>
</div>

## Version requirements

Minimum supported:

* Vue: `3.0.0` or higher
* TypeScript: `3.6.0` or higher (for TypeScript application)
* Vite `4.0.0` or higher (for application build with Vite)

Recommended:

* Vue: `3.0.0` or higher
* TypeScript: `4.0.0` or higher (for TypeScript application)
* Vite `5.0.0` or higher (for application build with Vite)

<div class="note">

Please note that this guide is designed for creating a Vue 3 application. Since Vue 2 has reached end of life, we no
longer maintain guides or components for Vue 2. We recommend upgrading to Vue 3 for continued support and compatibility.

</div>

## Create Vue 3 application

To get started, the broad steps are as follows:

1. [Access to npm registry](##access-to-npm-registry)
2. [Create Application](##create-application)
3. [Install component](##install-component)
4. [Add component to Application](##add-component-to-application)
5. [Apply styles](##apply-styles)
6. [Run the application](##run-the-application)

The application we will be building now should look like the illustration below:

<img src="Gantt/getting-started-result.png" class="b-screenshot" alt="Getting Started on Bryntum Gantt with Vue Result">

## Access to npm registry

You can try out Bryntum components for free using our public Bryntum trial packages.
If you have a Bryntum license, please refer to our [Npm Repository Guide](#Gantt/guides/npm/repository/private-repository-access.md) to access the private Bryntum repository.

## Create Application

Similarly to all the examples shipped with the distribution, we will be using [Vue CLI](https://cli.vuejs.org/) to build
Vue applications.

Type the following command to install Vue CLI:

```shell
npm create vue@latest
```

This command will install and execute create-vue, the official Vue project scaffolding tool.
You will be presented with prompts for several optional features such as TypeScript and testing support:

```shell
✔ Project name: … <your-project-name>
✔ Add TypeScript? … No / Yes✔️
✔ Add JSX Support? … No✔️ / Yes
✔ Add Vue Router for Single Page Application development? … No✔️ / Yes
✔ Add Pinia for state management? … No✔️ / Yes
✔ Add Vitest for Unit testing? … No✔️ / Yes
✔ Add an End-to-End Testing Solution? … No✔️ / Cypress / Nightwatch / Playwright
✔ Add ESLint for code quality? … No✔️ / Yes
✔ Add Prettier for code formatting? … No✔️ / Yes
✔ Add Vue DevTools 7 extension for debugging? (experimental) … No✔️ / Yes

Scaffolding project in ./<your-project-name>...
Done.
```

We are using the above config in this quick start guide but feel free to make any changes.

You can then move to your application folder:

```shell
cd <your-project-name>
```

<div class="note">

Please note some generated files will no longer be needed in your app, you can safely remove
<code>.src/components/HelloWorld.vue</code> and <code>src/assets/logo.png</code>. Also, remove the <code>assets</code> folder and any links to <code>.css</code>
files in the <code>main.ts</code> or <code>main.js</code>.

</div>

## Install Bryntum Gantt packages

From your terminal, update project dependencies using the following commands:

<div class="docs-tabs" data-name="licensed">
<div>
    <a>Trial version</a>
    <a>Licensed version</a>
</div>
<div>

```shell
npm install @bryntum/gantt@npm:@bryntum/gantt-trial@7.2.1 @bryntum/gantt-vue@7.2.1
```

</div>
<div>

```shell
npm install @bryntum/gantt@7.2.1 @bryntum/gantt-vue@7.2.1
```

</div>
</div>

<div class="note">

If you're using the licensed Bryntum version, ensure that you have configured your npm properly to get access to the Bryntum packages. If not, refer to <a href="#Gantt/guides/npm-repository.md">this guide</a>.

</div>

## Add component to Application

Edit the `src/App.vue` file and replace the content with the following:

<div class="docs-tabs" data-name="AppVue">
<div>
    <a>JavaScript</a>
    <a>TypeScript</a>
</div>
<div>

```javascript
<script setup>
import { BryntumGantt } from '@bryntum/gantt-vue-3';
import { ganttProps } from './AppConfig.js';
</script>

<template>
    <bryntum-gantt
        v-bind="ganttProps"
    />
</template>

<style lang="scss">
@import './App.scss';
</style>
```

</div>
<div>

```typescript
<script setup lang="ts">
import { BryntumGantt } from '@bryntum/gantt-vue-3';
import { ganttProps } from './AppConfig.ts';
</script>

<template>
    <bryntum-gantt
        v-bind="ganttProps"
    />
</template>

<style lang="scss">
@import './App.scss';
</style>
```

</div>
</div>

The code above creates a simple project with a few tasks and dependencies between them.

Bryntum Gantt schedules project tasks taking dependencies, constraints, and calendars into account.
For an in-depth introduction to the Project, please refer to the [Data guide]("#Gantt/guides/data/project_data.md").

<div class="note">

By default, tasks will automatically be moved to the project's start date if there are
no constraints, dependencies, or manually scheduled tasks. To prevent this, set <code>autoSetConstraints</code> to <code>true</code> in the
ProjectModel configuration.

</div>

Create a `AppConfig` file in the `src/` directory with the following content:

<div class="docs-tabs" data-name="AppConfig">
<div>
    <a>JavaScript</a>
    <a>TypeScript</a>
</div>
<div>

```javascript
'use strict';
Object.defineProperty(exports, '__esModule', { value : true });
exports.ganttConfig = void 0;
var gantt_1 = require('@bryntum/gantt');
exports.ganttConfig = {
    startDate : new Date(2026, 0, 1),
    endDate   : new Date(2026, 2, 1),

    dependencyIdField : 'sequenceNumber',
    rowHeight         : 45,
    tickSize          : 45,
    barMargin         : 8,
    project           : {
        autoSetConstraints : true,
        autoLoad           : true,
        loadUrl            : 'data/data.json'
    },
    columns      : [{ type : 'name', width : 250 }],
    // Custom task content, display task name on child tasks
    taskRenderer : function(_a) {
        var taskRecord = _a.taskRecord;
        if (taskRecord.isLeaf && !taskRecord.isMilestone) {
            return gantt_1.StringHelper.encodeHtml(taskRecord.name);
        }
        return '';
    }
};
```

</div>
<div>

```typescript
import type { TaskModel } from '@bryntum/gantt';
import { StringHelper } from '@bryntum/gantt';
import { type BryntumGanttProps } from '@bryntum/gantt-vue-3';

export const ganttConfig : BryntumGanttProps = {
    startDate : new Date(2026, 0, 1),
    endDate   : new Date(2026, 2, 1),

    dependencyIdField : 'sequenceNumber',
    rowHeight         : 45,
    tickSize          : 45,
    barMargin         : 8,
    project           : {
        autoSetConstraints : true, // automatically introduce `startnoearlier` constraint if tasks do not use constraints, dependencies, or manuallyScheduled
        autoLoad           : true,
        loadUrl : 'data/data.json'
    },

    columns : [{ type : 'name', width : 250 }],

    // Custom task content, display task name on child tasks
    taskRenderer({ taskRecord } : { taskRecord: TaskModel }) {
        if (taskRecord.isLeaf && !taskRecord.isMilestone) {
            return StringHelper.encodeHtml(taskRecord.name);
        }
        return '';
    }
};
```

</div>
</div>

<div class="note">

Note that the <code>startDate</code> and <code>endDate</code> configs passed to <code>ganttConfig</code> denote
the currently visible timespan.

</div>

## Add component data

Create a `public/data/data.json` file for example data and add the following JSON data to it:

```json
{
  "success": "true",
  "tasks": {
    "rows": [
      {
        "id": 1,
        "name": "Documentation Project",
        "expanded": true,
        "children": [
          {
            "id": 2,
            "name": "Preparation",
            "expanded": true,
            "children": [
              { "id": 6, "name": "Proof-read docs", "startDate": "2026-01-02", "endDate": "2026-01-09" },
              { "id": 3, "name": "Release docs",    "startDate": "2026-01-09", "endDate": "2026-01-10" }
            ]
          },
          {
            "id": 4,
            "name": "Development",
            "expanded": true,
            "children": [
              { "id": 7, "name": "Write API docs",  "startDate": "2026-01-05", "endDate": "2026-01-12" },
              { "id": 8, "name": "Write tutorials", "startDate": "2026-01-10", "endDate": "2026-01-16" },
              { "id": 9, "name": "Create examples", "startDate": "2026-01-12", "endDate": "2026-01-18" }
            ]
          },
          {
            "id": 5,
            "name": "Review & Release",
            "expanded": true,
            "children": [
              { "id": 10, "name": "Team review",     "startDate": "2026-01-18", "endDate": "2026-01-20" },
              { "id": 11, "name": "Final approval",  "startDate": "2026-01-20", "endDate": "2026-01-21" },
              { "id": 12, "name": "Public release",  "startDate": "2026-01-22", "endDate": "2026-01-22" }
            ]
          }
        ]
      }
    ]
  },
  "dependencies": {
    "rows": [
      { "fromTask": 6,  "toTask": 3  },
      { "fromTask": 7,  "toTask": 8  },
      { "fromTask": 8,  "toTask": 9  },
      { "fromTask": 9,  "toTask": 10 },
      { "fromTask": 10, "toTask": 11 },
      { "fromTask": 11, "toTask": 12 }
    ]
  }
}
```

This is the data the Bryntum Gantt will use.

## Apply styles

### Stylesheets

Remove both `src/assets/main.css` and `src/assets/base.css`, and delete the `main.css` import from `src/main.ts`.

The following CSS files are provided with the Bryntum npm packages or in the `/build` folder of the distribution:

| File                              | Contents                      |
|-----------------------------------|-------------------------------|
| `gantt.css`                     | Structural CSS                |
| `svalbard-light.css`              | Svalbard Light theme          |
| `svalbard-dark.css`               | Svalbard Dark theme           |
| `visby-light.css`                 | Visby Light theme             |
| `visby-dark.css`                  | Visby Dark theme              |
| `stockholm-light.css`             | Stockholm Light theme         |
| `stockholm-dark.css`              | Stockholm Dark theme          |
| `material3-light.css`             | Material3 Light theme         |
| `material3-dark.css`              | Material3 Dark theme          |
| `fluent2-light.css`               | Fluent2 Light theme           |
| `fluent2-dark.css`                | Fluent2 Dark theme            |
| `fontawesome/css/fontawesome.css` | Font Awesome Free base CSS    |
| `fontawesome/css/solid.css`       | Font Awesome Free solid icons |

You'll need to import the structural CSS and the preferred theme into your project for the Bryntum Gantt to render
correctly. And if you are not replacing the icons used by the component, you will also need to include Font Awesome.

<div class="docs-tabs" data-name="stylesheet">
<div>
    <a>CSS</a>
    <a>SCSS</a>
</div>
<div>

Create a <code>src/App.css</code> file and add the following:

```css
/* FontAwesome is used for icons */
@import "@bryntum/gantt/fontawesome/css/fontawesome.css";
@import "@bryntum/gantt/fontawesome/css/solid.css";
/* Structural CSS */
@import "@bryntum/gantt/gantt.css";
/* Bryntum theme of your choice */
@import "@bryntum/gantt/svalbard-light.css";
```

You need to change the <code>App.scss</code> to <code>App.css</code> in the <code>App.vue</code>.

</div>
<div>

Create a <code>src/App.scss</code> file and add the following:

```scss
// FontAwesome is used for icons
@import "@bryntum/gantt/fontawesome/css/fontawesome.css";
@import "@bryntum/gantt/fontawesome/css/solid.css";
// Structural CSS
@import "@bryntum/gantt/gantt.css";
// Bryntum theme
@import "@bryntum/gantt/svalbard-light.css";
```

For your application to support sass files, you'll need to add additional dependencies to your project.

From the terminal:

```shell
npm install sass@1.42.0 --save-dev --save-prefix=~
```

Visit <a href="#Gantt/guides/customization/styling.md#creating-a-custom-theme">Creating a custom theme</a> section for more info on how to create a custom theme.
</div>
</div>

### Sizing the component

By Default, the Component is configured to take `100%` of the parent DOM element with a min-height of `10em`.

For your application to show the Component with the appropriate size, you can for example make parent components take
the full height of the screen.

<div class="docs-tabs" data-name="stylesheet">
<div>
    <a>CSS</a>
    <a>SCSS</a>
</div>
<div>

In your <code>src/App.css</code> file, add the following:

```css
body,
html {
    margin         : 0;
    display        : flex;
    flex-direction : column;
    height         : 100vh;
    font-family    : sans-serif;
    font-size      : 14px;
}
```

```css
#app {
    flex : 1 1 100%;
}
```

</div>
<div>

In your <code>src/App.scss</code> file, add the following:

```css
body,
html {
    margin         : 0;
    display        : flex;
    flex-direction : column;
    height         : 100vh;
    font-family    : sans-serif;
    font-size      : 14px;
}
```

```css
#app {
    flex : 1 1 100%;
}
```

</div>
</div>

There are many other solutions depending on the situation. Feel free to adapt the code above regarding your application
layout. For more information on the topic, see this guide
[Sizing the component](https://bryntum.com/products/grid/docs/guide/Grid/basics/sizing).

## Run the application

From your terminal:

```shell
npm run dev
```

Your application is now available under [http://localhost:5173](http://localhost:5173).

## Further on integration with Vue

Do you want to know more about how Bryntum Gantt integrates with Vue and starts to customize your application? We
provide you with a [complete Vue guide here](#Gantt/guides/integration/vue/guide.md).

## Troubleshooting

Stuck somewhere? Please refer to this [Troubleshooting guide](#Gantt/guides/integration/vue/troubleshooting.md). If
you find errors in our docs and/or onboarding guides, please report them in [our forums](https://forum.bryntum.com).

### Learn about Data

Bryntum components often use multiple collections and entities.

The [Data guide](#Gantt/guides/data/project_data.md) explains how they all fit together.
