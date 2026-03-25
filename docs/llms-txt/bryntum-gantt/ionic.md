# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/ionic.md

# Getting Started with Bryntum Gantt in Ionic

## Try Ionic demos

Bryntum Gantt is delivered with a variety of Ionic demo applications showing its functionality.
All demo applications have been verified to be compatible with Node.js 20.

<div class="b-card-group-2">
<a href="https://bryntum.com/products/gantt/examples/#Integration" class="b-card"><i class="fas fa-globe"></i>View online Ionic demos</a>
<a href="#Gantt/guides/integration/ionic/guide.md#build-and-run-local-demos" class="b-card"><i class="b-logo b-ionic"></i>Build and run Ionic demos</a>
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

## Create Ionic application

To get started, the broad steps are as follows:

1. [Access to npm registry](##access-to-npm-registry)
2. [Create Application](##create-application)
3. [Install component](##install-component)
4. [Add component to Application](##add-component-to-application)
5. [Apply styles](##apply-styles)
6. [Run the application](##run-the-application)

The application we are about to build together is pretty simple, and will look like the illustration below:

<img src="Gantt/getting-started-result.png" class="b-screenshot" alt="Getting Started on Bryntum Gantt with Ionic Result">

## Access to npm registry

You can try out Bryntum components for free using our public Bryntum trial packages.
If you have a Bryntum license, please refer to our [Npm Repository Guide](#Gantt/guides/npm/repository/private-repository-access.md) to access the private Bryntum repository.

## Create Application

Similarly to all the examples shipped with the distribution, we will be using [Ionic CLI](https://cli.angular.io/) to
build Ionic applications.

Type the following command to install Ionic CLI:

```shell
npm install -g @ionic/cli
```

We will then create a basic application with Ionic CLI:

```shell
ionic start IonicApp blank --type=angular
```

Here we are using `blank`, the most simple starter template for the app.

Ionic can use Angular, React, or Vue. By `choosing --type=angular`, we tell Ionic CLI to generate an application using
Angular.

Feel free to select other defaults if needed following instruction provided in
the [Ionic Framework Documentation](https://ionicframework.com)

<div class="note">

Please feel free to change <code>IonicApp</code> to your preferred application name

</div>

You can then move to your application folder

```shell
cd IonicApp
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

Edit the **src/app/home/home.module.ts** file and add the following:

```typescript
import { BryntumGanttModule } from '@bryntum/gantt-angular';

@NgModule({
    imports : [
        BryntumGanttModule
    ]
})
```

Then, edit the `src/app/home/home.page.ts` file and replace the content with the following:

```typescript
import { Component, ViewChild} from '@angular/core';
import { BryntumGanttComponent, BryntumGanttProjectModelComponent } from '@bryntum/gantt-angular';
import { ganttProps, projectProps } from './home.config';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  standalone: false,
})
export class HomePage {

    ganttProps = ganttProps;
    projectProps = projectProps;

    @ViewChild('gantt') ganttComponent!: BryntumGanttComponent;
    @ViewChild('project') projectComponent!: BryntumGanttProjectModelComponent;

}
```

The code above creates a simple project with a few tasks and dependencies between them.

Bryntum Gantt schedules project tasks taking dependencies, constraints, and calendars into account.
For an in-depth introduction to the Project, please refer to the [Data guide]("#Gantt/guides/data/project_data.md").

### Add component data

Create a `assets/data/data.json` file for example data and add the following JSON data to it:

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

Create a `src/app/home/home.config.ts` file with the following content:

```typescript
import { BryntumGanttProps, BryntumGanttProjectModelProps } from '@bryntum/gantt-angular';

export const projectProps: BryntumGanttProjectModelProps = {
    // Automatically introduces a `startnoearlier` constraint for tasks that (a) have no predecessors,
    // (b) do not use constraints and (c) aren't `manuallyScheduled`
    autoSetConstraints : true,
    loadUrl            : 'assets/data/data.json',
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

Note that the <code>startDate</code> and <code>endDate</code> configs passed to <code>ganttConfig</code> denote the currently visible timespan.

</div>

<div class="note">

By default, tasks will automatically be moved to the project's start date if there are
no constraints, dependencies, or manually scheduled tasks. To prevent this, set <code>autoSetConstraints</code> to <code>true</code> in the
ProjectModel configuration.

</div>

And finally, edit the `src/app/home/home.page.html` file and replace the content with the following:

```html
<ion-content [fullscreen] = "true">
  <div id = "container">
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
  </div>
</ion-content>
```

## Apply styles

### Stylesheets

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
correctly,  and if you are not replacing the icons used by the component, you will also need to include Font Awesome.

Edit the `src/global.scss` and add the following:

```scss
// FontAwesome is used for icons
@import "~@bryntum/gantt/fontawesome/css/fontawesome.css";
@import "~@bryntum/gantt/fontawesome/css/solid.css";
// Structural CSS
@import "~@bryntum/gantt/gantt.css";
// Bryntum theme of your choice
@import "~@bryntum/gantt/svalbard-light.css";
```

### Sizing the component

By Default, the Component is configured to take `100%` of the parent DOM element with a min-height of `10em`.

For your application to show the Component with the appropriate size, you can for example make parent components take
the full height of the screen.

In your `src/app/home/home.page.scss` file, add the following:

```scss
#container {
    height : 100vh;
}
```

There are many other solutions depending on the situation. Feel free to adapt the code above regarding your application
layout. For more information on the topic, see this guide
[Sizing the component](https://bryntum.com/products/grid/docs/guide/Grid/basics/sizing).

## Run the application

From your terminal:

```shell
ionic serve
```

Your application is now available under [http://localhost:8100](http://localhost:8100), and your browser should
automatically open it for you.

## Troubleshooting

Please refer to this [Troubleshooting guide](#Gantt/guides/integration/ionic/troubleshooting.md).

## What to do next?

### Further on integration with Ionic

Do you want to know more about how Bryntum Gantt integrates with Ionic and starts to customize your application? We
provide you with a [complete Ionic guide here](#Gantt/guides/integration/ionic/guide.md).

### Learn about Data

Bryntum components often use multiple collections and entities.

The [Data guide](#Gantt/guides/data/project_data.md) explains how they all fit together.
