# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/javascript.md

# Getting Started with Bryntum Gantt in JavaScript

## Try JavaScript demos

Bryntum Gantt is delivered with a variety of JavaScript demo applications showing its functionality.

<div class="b-card-group-2">
<a href="https://bryntum.com/products/gantt/examples/" class="b-card"><i class="fas fa-globe"></i>View online JS demos</a>
<a href="#Gantt/guides/download.md#javascript-demos" class="b-card"><i class="fab fa-js"></i>View local JS demos</a>
</div>

## Create JavaScript application

In this guide we will explain how to get started if you are not using npm. If you prefer to use npm,
[please visit the dedicated Quick Start here](#Gantt/guides/quick-start/javascript-npm.md).

To get started, the broad steps are as follows:

1. [Download Bryntum Gantt](##download)
2. [Create Application](##create-application)
3. [Bryntum bundles](##bryntum-bundles)
4. [Add component to Application](##add-component-to-application)
5. [Apply styles](##apply-styles)
6. [Run the Application](##run-the-application)

The application we are about to build together is pretty simple, and will look like the live demo below:
<div class="external-example" data-file="Gantt/guides/readme/basic.js"></div>

## Download

Bryntum Gantt is a commercial product, but you can access our free trial archive with bundles and examples by
[downloading it here](https://bryntum.com/download/?product=gantt).

## Create Application

You can proceed as usual. The Bryntum Gantt Component is compliant with the most popular Javascript Standards.

To create an application, create a new folder and add the following to `index.html`:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bryntum Gantt App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/main.js"></script>
  </body>
</html>
```

## Bryntum bundles

The Bryntum Gantt distribution provides pre-build JavaScript bundles.
All bundles are transpiled with `chrome: 88` babel preset.

In distribution zip they are located under the `/build` folder.

| File                    | Contents                                                        |
|-------------------------|-----------------------------------------------------------------|
| `gantt.module.js`     | Modules format bundle without WebComponents                     |
| `gantt.lwc.module.js` | Modules format bundle with Lightning WebComponents (Salesforce) |
| `gantt.wc.module.js`  | Modules format bundle with WebComponents                        |
| `gantt.umd.js`        | UMD format bundle with WebComponents                            |

Bryntum Gantt also contains Non-UI bundles for usage with Node.JS.

| File                    | Contents                         |
|-------------------------|----------------------------------|
| `gantt.node.cjs`      | Non-UI bundle in CommonJS format |
| `gantt.node.mjs`      | Non-UI bundle in Modules format  |

Typings for TypeScripts can be found in files with a `.d.ts` file extension.

Minified bundles are available for Licensed product version and delivered with `.min.js` suffix.

### Using EcmaScript module bundles

If you choose this option, **copy** the selected module file onto your application, in the root folder, for instance.

Create a `main.js` file, you can import the gantt JavaScript.

```javascript
import { Gantt } from './gantt.module.js';

const gantt = new Gantt({/*...*/ });
```

<div class="note">

We have copied the module directly from the <code>build</code> folder for simplicity in this code example. Consider
using your preferred build tool instead.

</div>

Learn more about how to use EcmaScript modules [here](#Gantt/guides/gettingstarted/es6bundle.md).

### Using `<script>` tag and UMD files

Please consider this solution as legacy and use it only for compatibility. If you choose this option, **copy** the
selected UMD file onto your application, in the root folder, for instance.

To include Bryntum Gantt on your page using a plain old script tag, add a `<script>` tag pointing to the UMD bundle
file in the `<HEAD>` of your `index.html` page. Example:

```html
<script src="gantt.umd.js"></script>
```

In the `main.js`, you will be able to access Gantt classes in the global `bryntum` namespace as
follows:

```javascript
const gantt = new bryntum.gantt.Gantt({/*...*/ });
```

<div class="note">

We also recommend you to copy onto your application the <code>.js.map</code> file paired with the umd file you selected.

</div>

<div class="note">

We have copied the module directly from the <code>build</code> folder for simplicity in this code example. Consider
using your preferred build tool instead.

</div>

Read more on [script tag and UMD modules...](#Gantt/guides/gettingstarted/scripttag.md)

## Add component to Application

Assuming the use of an EcmaScript module bundle:

```javascript
import { Gantt } from './gantt.module.js';

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

If you want to discover how flexible the Bryntum Gantt Component is, please explore
the [API documentation](#Gantt/view/Gantt).

## Apply styles

### Stylesheets

You'll find a complete list of available CSS files in the `/build` folder of the distribution:

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

You'll need to copy and import the structural CSS and the preferred theme into your project for the Bryntum Gantt to
render correctly, and if you are not replacing the icons used by the component, you will also need to include Font
Awesome. Below we assume they are in the root folder.

<div class="note">

We also recommend you to copy onto your application the <code>.css.map</code> file paired with the css file you selected.

</div>

Add link tags for the structural CSS and a theme to your `index.html` in the `<head>...</head>` section:

```html
<!-- Structural CSS -->
<link rel="stylesheet" href="gantt.css">
<!-- Bryntum theme of your choice -->    
<link rel="stylesheet" href="svalbard-light.css" data-bryntum-theme>
```

Make sure to copy the `fonts/` folder located in the `/build` right next to the `.css` theme.

```bash
- my-gantt-app/
  - fonts/
  - gantt.css
  - svalbard-light.css
```

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

There are many other solutions depending on the situation. Feel free to adapt the code above regarding your application
layout. For more information on the topic, see this guide
[Sizing the component](https://bryntum.com/products/grid/docs/guide/Grid/basics/sizing).

## Run the application

To see the preview, start a live-server (if you are using one) or
open the `index.html` file in your browser from your local web server.

<div class="note">

A local web server is required, viewing the app page directly from the local file system won't work.

</div>

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
