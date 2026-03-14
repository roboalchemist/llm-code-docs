# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/angular.md

# Getting Started with Bryntum Gantt in Angular

## Try Angular demos

Bryntum Gantt is delivered with a variety of Angular demo applications showing its functionality.
All demo applications have been verified to be compatible with Node.js 20.

<div class="b-card-group-2">
<a href="https://bryntum.com/products/gantt/examples/?framework=angular" class="b-card"><i class="fas fa-globe"></i>View online Angular demos</a>
<a href="#Gantt/guides/integration/angular/guide.md#build-and-run-local-demos" class="b-card"><i class="fab fa-angular"></i>Build and run Angular demos</a>
</div>

## Version requirements

Minimum supported:

* Angular: `9.0.0` or higher
* TypeScript: `3.6.0` or higher (for TypeScript application)
* Vite `4.0.0` or higher (for application build with Vite)

Recommended:

* Angular: `12.0.0` or higher
* TypeScript: `4.0.0` or higher (for TypeScript application)
* Vite `5.0.0` or higher (for application build with Vite)

## Create Angular application

To get started, the broad steps are as follows:

1. [Access to npm registry](##access-to-npm-registry)
2. [Create Application](##create-application)
3. [Install component](##install-component)
4. [Add component to Application](##add-component-to-application)
5. [Apply styles](##apply-styles)
6. [Run the application](##run-the-application)

The application we are about to build together is pretty simple, and will look like the illustration below:

<img src="Gantt/getting-started-result.png" class="b-screenshot" alt="Getting Started on Bryntum Gantt with Angular Result">

## Access to npm registry

You can try out Bryntum components for free using our public Bryntum trial packages.
If you have a Bryntum license, please refer to our [Npm Repository Guide](#Gantt/guides/npm/repository/private-repository-access.md) to access the private Bryntum repository.

## Create Application

Similarly to all the examples shipped with the distribution, we will be using [Angular CLI](https://cli.angular.io/) to
build Angular applications.

Type the following command to install Angular CLI:

```shell
npm install -g @angular/cli
```

We will then create a basic application with Angular CLI using Typescript:

```shell
ng new gantt-app --no-standalone --no-routing --ssr=false
```

<div class="note">

The Bryntum components are designed to render on the client side. Therefore, we are using the option <code>--ssr=false</code> to
indicate that server-side rendering is not required.

</div>

When you run the command, you will be prompted to select a stylesheet format. We suggest choosing either **CSS** or
**SCSS**. This guide provides information on both options.

<div class="note">

Please feel free to change <code>gantt-app</code> to your preferred application name

</div>

You can then move to your application folder:

```shell
cd gantt-app
```

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

<div class="note">

Starting from Angular v20, file naming conventions have changed.
<ul>
<li><code>app.module.ts</code> → <code>app-module.ts</code></li>
<li><code>app.component.ts</code> → <code>app.ts</code></li>
<li><code>app.component.html</code> → <code>app.html</code></li>
<li><code>Class AppComponent</code> → <code>Class App</code></li>
</ul>
If you are on earlier version, please adjust the filenames and class names accordingly.

</div>

Edit the `src/app/app-module.ts` file and add the following import:

```typescript
import { BryntumGanttModule } from '@bryntum/gantt-angular';
```

Next, add `BryntumGanttModule` to `imports[]` :

```typescript
@NgModule({
    imports : [
        BryntumGanttModule
    ]
})
```

Then, edit the `src/app/app.ts` file and replace the content with the following:

```typescript
import { Component, ViewChild } from '@angular/core';
import { BryntumGanttComponent, BryntumGanttProjectModelComponent } from '@bryntum/gantt-angular';
import { ganttProps, projectProps } from './app.config';

@Component({
    selector    : 'app-root',
    standalone  : false,
    templateUrl : './app.html',
    styleUrl    : './app.css',
})
export class App {

    ganttProps = ganttProps;
    projectProps = projectProps;

    @ViewChild('gantt') ganttComponent!: BryntumGanttComponent;
    @ViewChild('project') projectComponent!: BryntumGanttProjectModelComponent;
}
```

If you prefer using SCSS styling then replace `'./app.css'` with `'./app.scss'`.

### Add component data

Create a `public/data/data.json` file for example data and add the following JSON data to it:

```javascript
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

The Bryntum Gantt uses multiple stores to manage its data, with each store dedicated to a specific type. For example,
the Resource Store holds resource data such as people or assets. This separation keeps the data organized, synchronized,
and easier to maintain.

To learn more, visit [Project Data](#Gantt/guides/data/project_data.md)

Create `src/app/app.config.ts` file with the following content:

```typescript
import { BryntumGanttProps, BryntumGanttProjectModelProps } from '@bryntum/gantt-angular';

export const projectProps: BryntumGanttProjectModelProps = {
    // Automatically introduces a `startnoearlier` constraint for tasks that (a) have no predecessors,
    // (b) do not use constraints and (c) aren't `manuallyScheduled`
    autoSetConstraints : true,
    loadUrl            : 'data/data.json',
    autoLoad           : true
};
export const ganttProps: BryntumGanttProps = {
    columns : [
        { type : 'name', width : 200 }
    ],
    startDate : new Date(2026, 0, 1),
    endDate   : new Date(2026, 2, 1)
};
```

<div class="note">

Note that the <code>startDate</code> and <code>endDate</code> configs passed to <code>ganttProps</code> denote the currently visible timespan.

</div>

<div class="note">

By default, tasks will automatically be moved to the project's start date if there are
no constraints, dependencies, or manually scheduled tasks. To prevent this, set <code>autoSetConstraints</code> to <code>true</code> in the
ProjectModel configuration.

</div>

And finally, edit the `src/app/app.html` file and replace the content with the following:

```html
<bryntum-gantt-project-model
    #project
    [loadUrl] = "projectProps.loadUrl!"
    [autoLoad] = "projectProps.autoLoad!"
    [autoSetConstraints] = "projectProps.autoSetConstraints!"
></bryntum-gantt-project-model>

<bryntum-gantt
    #gantt
    [startDate] = "ganttProps.startDate!"
    [columns] = "ganttProps.columns!"
    [endDate] = "ganttProps.endDate!"
    [project] = "project"
></bryntum-gantt>
```

## Apply styles

Including a theme + structural CSS is required to render the Bryntum Gantt correctly, and if you are not replacing
the icons used by the component, you will also need to include Font Awesome.

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

You'll need to reference the selected CSS file into your project.

<div class="docs-tabs" data-name="stylesheet">
<div>
    <a>build folder</a>
    <a>npm</a>
</div>
<div>

You'll need to copy the selected CSS file into your project, let's say in the <code>src/app</code> folder.

<div class="note">

We also recommend you to copy onto your application the <code>.css.map</code> file paired with the css file you selected.

</div>

Edit the <code>src/app/app.ts</code> file and add a reference the CSS file location as follows:

```typescript
styleUrls : [
    './app.css',
    './fontawesome/css/fontawesome.css',
    './fontawesome/css/solid.css',
    './gantt.css',
    './material3-light.css'
]
```

</div>
<div>

Edit the <code>src/styles.css</code> or <code>src/styles.scss</code> and add the following:

```scss
/* FontAwesome is used for icons */
@import '@bryntum/gantt/fontawesome/css/fontawesome.css';
@import '@bryntum/gantt/fontawesome/css/solid.css';
/* Structural CSS */
@import "@bryntum/gantt/gantt.css";
/* Bryntum theme of your choice */
@import "@bryntum/gantt/material3-light.css";
```

If you want to customize the default theme, simply override the relevant set of CSS variables after the import.
Visit <a href="#Gantt/guides/customization/styling.md#creating-a-custom-theme">Creating a custom theme</a> section for more info.
</div>
</div>

<div class="note">

The Bryntum components expect styling to be available globally, if you move the styling to <code>app.css</code>, it won't work, until you add the following lines of code to <code>app.ts</code>:

```typescript
import { ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  standalone: false,
  styleUrl: './app.scss',
  encapsulation: ViewEncapsulation.None
})
```

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

In your <code>src/styles.css</code> file, add the following:

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
app-root {
    flex : 1 1 100%;
}
```

</div>
<div>

In your <code>src/styles.scss</code> file, add the following:

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
app-root {
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
ng serve
```

Your application is now available under [http://localhost:4200](http://localhost:4200).

## Troubleshooting

Please refer to this [Troubleshooting guide](#Gantt/guides/integration/angular/troubleshooting.md).

## What to do next?

### Further on integration with Angular

Do you want to know more about how `Bryntum Gantt` integrates with Angular and starts to customize your application?
We provide you with a [complete Angular guide here](#Gantt/guides/integration/angular/guide.md).

### Learn about Data

Bryntum components often use multiple collections and entities.

The [Data guide](#Gantt/guides/data/project_data.md) explains how they all fit together.
