# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/javascript-npm.md

# Getting Started with Bryntum Gantt in JavaScript with npm package manager

## Try JavaScript demos

Bryntum Gantt is delivered with a variety of JavaScript demo applications showing its functionality.

<div class="b-card-group-2">
<a href="https://bryntum.com/products/gantt/examples/" class="b-card"><i class="fas fa-globe"></i>View online JS demos</a>
<a href="#Gantt/guides/download.md#javascript-demos" class="b-card"><i class="fab fa-js"></i>View local JS demos</a>
</div>

## Version requirements

Minimum supported:

* JavaScript: `` or higher
* TypeScript: `3.6.0` or higher (for TypeScript application)
* Vite `4.0.0` or higher (for application build with Vite)

Recommended:

* JavaScript: `` or higher
* TypeScript: `4.0.0` or higher (for TypeScript application)
* Vite `5.0.0` or higher (for application build with Vite)

## Create JavaScript application

In this guide we will explain how to get started using the npm CLI. If you prefer to not use
npm, please visit the dedicated [Quick Start here](#Gantt/guides/quick-start/javascript.md).

To get started, the broad steps are as follows:

1. [Access to npm registry](##access-to-npm-registry)
2. [Create Application](##create-application)
3. [Bryntum bundles](##bryntum-bundles)
4. [Install component](##install-component)
5. [Add component to Application](##add-component-to-application)
6. [Apply styles](##apply-styles)
7. [Run the application](##run-the-application)

The application we are about to build together is pretty simple, and will look
like the live demo below:
<div class="external-example" data-file="Gantt/guides/readme/basic.js"></div>

## Access to npm registry

You can try out Bryntum components for free using our public Bryntum trial packages.
If you have a Bryntum license, please refer to our [Npm Repository Guide](#Gantt/guides/npm/repository/private-repository-access.md) to access the private Bryntum repository.

## Create Application

To create an application, we will use [Vitejs](https://vitejs.dev/guide) and
choose vanilla JavaScript.

First, execute the vite command:

```shell
npm create vite@latest my-gantt-app -- --template vanilla
```

<div class="note">

For npm 7+, extra double-dash is needed.

</div>

It will generate a vanilla JavaScript boilerplate. Next, install dependencies:

```shell
cd my-gantt-app
npm install
```

Open the project folder and delete `counter.js`, we don't need it in our case.

## Install component

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

Once you have project set up, you can proceed with configuring your Gantt.

Delete the `counter.js` and replace your `main.js` with the following code:

```javascript
import { Gantt } from '@bryntum/gantt';
import './style.css';

const gantt = new Gantt({
    appendTo  : 'app',
    startDate : new Date(2022, 0, 1),
    endDate   : new Date(2022, 0, 10),
    columns   : [
        { type : 'name', width : 160 }
    ],
    project : {

        // Automatically introduces a `startnoearlier` constraint for tasks that (a) have no predecessors,
        // (b) do not use constraints and (c) aren't `manuallyScheduled`
        autoSetConstraints : true,
        tasks              : [
            {
                id       : 1,
                name     : 'Documentation Project',
                expanded : true,
                children : [
                    {
                        id       : 2,
                        name     : 'Preparation',
                        expanded : true,
                        children : [
                            { id : 6, name : 'Proof-read docs', startDate : '2026-01-02', endDate : '2026-01-09' },
                            { id : 3, name : 'Release docs', startDate : '2026-01-09', endDate : '2026-01-10' }
                        ]
                    },
                    {
                        id       : 4,
                        name     : 'Development',
                        expanded : true,
                        children : [
                            { id : 7, name : 'Write API docs', startDate : '2026-01-05', endDate : '2026-01-12' },
                            { id : 8, name : 'Write tutorials', startDate : '2026-01-10', endDate : '2026-01-16' },
                            { id : 9, name : 'Create examples', startDate : '2026-01-12', endDate : '2026-01-18' }
                        ]
                    },
                    {
                        id       : 5,
                        name     : 'Review & Release',
                        expanded : true,
                        children : [
                            { id : 10, name : 'Team review', startDate : '2026-01-18', endDate : '2026-01-20' },
                            { id : 11, name : 'Final approval', startDate : '2026-01-20', endDate : '2026-01-21' },
                            { id : 12, name : 'Public release', startDate : '2026-01-22', endDate : '2026-01-22' }
                        ]
                    }
                ]
            }
        ],
        dependencies : [
            { fromTask : 6, toTask : 3 },
            { fromTask : 7, toTask : 8 },
            { fromTask : 8, toTask : 9 },
            { fromTask : 9, toTask : 10 },
            { fromTask : 10, toTask : 11 },
            { fromTask : 11, toTask : 12 }
        ]
    }
});
```

Here we are providing inline data, you can learn more about how we manage
data using Store [in this guide](#Core/guides/data/storebasics.md).

The code above creates a simple project with a few tasks and dependencies between them.

Bryntum Gantt schedules project tasks taking dependencies, constraints, and calendars into account.
For an in-depth introduction to the Project, please refer to the [Data guide]("#Gantt/guides/data/project_data.md").

<div class="note">

Note that the <code>startDate</code> and <code>endDate</code> configs passed to the <code>Gantt</code> instance denote the currently accessible
timespan.

</div>

<div class="note">

By default, tasks will automatically be moved to the project's start date if there are
no constraints, dependencies, or manually scheduled tasks. To prevent this, set <code>autoSetConstraints</code> to <code>true</code> in the
ProjectModel configuration.

</div>

Learn more about how to use EcmaScript modules [here](#Gantt/guides/gettingstarted/es6bundle.md).

If you want to discover how flexible the Bryntum Gantt Component is, please explore
the [API documentation](#Gantt/view/Gantt).

## Apply styles

### Stylesheets

The following CSS files are provided with the Bryntum npm packages:

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
correctly, and if you are not replacing the icons used by the component, you will also need to include Font Awesome.

Remove the content of `style.css` and replace it with the following:

```css
/* FontAwesome is used for icons */
@import "@bryntum/gantt/fontawesome/css/fontawesome.css";
@import "@bryntum/gantt/fontawesome/css/solid.css";
/* Structural CSS */
@import "@bryntum/gantt/gantt.css";
/* Bryntum theme of your choice */
@import "@bryntum/gantt/svalbard-light.css";
```

<div class="note">

We have referenced the CSS file directly from the <code>node_modules</code> folder for simplicity in this code example.
Consider using your preferred build tool instead.

</div>

### Sizing the component

By Default, the Component is configured to take `100%` of the parent DOM element with a min-height of `10em`.

For your application to show the Component with the appropriate size, you can for example make parent components take
the full height of the screen.

```css
#app {
    margin         : 0;
    display        : flex;
    flex-direction : column;
    height         : 100vh;
    font-size      : 14px;
}
```

There are many other solutions depending on the situation. Feel free to adapt the code above regarding your
application layout. For more information on the topic, see this guide
[Sizing the component](https://bryntum.com/products/grid/docs/guide/Grid/basics/sizing).

## Run the application

Run the application by executing:

```shell
npm run dev
```

## What to do next?

### Tutorial

Now it is time to customize your application. To get familiar with the most common tasks developers perform, we have
designed an [engaging tutorial](#Gantt/guides/tutorial.md) that we are excited
to see you follow.

### Learn about Data

Bryntum components often use multiple collections and entities.

The [Data guide](#Gantt/guides/data/project_data.md) explains how they all fit together.

### Rendering and styling

In the [rendering and styling](#Gantt/guides/customization/styling.md) guide you will learn how to
customize the rendering of your Gantt.

### Enabling features

Please refer to the
[enabling extra features guide](#Gantt/guides/basics/features.md)
to learn how to enhance your Gantt chart with additional functionality (such as displaying labels for the tasks).

### Responsiveness

Gantt can be configured to work well on many different screen sizes. This is achieved by specifying different
responsive "levels" (breakpoints) on Gantt and then having per level configurations on the columns.

If this is a
concern now, visit the  [responsive guide](#Gantt/guides/customization/responsive.md)
 to learn how to configure responsiveness.

### Localization

Bryntum Gantt uses locales for translations of texts, date formats and such. This
[localization guide](#Gantt/guides/customization/localization.md)
shows you how to use one of the locales that Bryntum Gantt ships with and how to create your own.
