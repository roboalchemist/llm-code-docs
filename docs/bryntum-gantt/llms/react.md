# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/react.md

# Getting Started with Bryntum Gantt in React

## Try React demos

Bryntum Gantt is delivered with a variety of React demo applications showing its functionality.
All demo applications have been verified to be compatible with Node.js 20.

<div class="b-card-group-2">
<a href="https://bryntum.com/products/gantt/examples/?framework=react" class="b-card"><i class="fas fa-globe"></i>View online React demos</a>
<a href="#Gantt/guides/integration/react/guide.md#build-and-run-local-demos" class="b-card"><i class="fab fa-react">
</i>Build and run React demos</a>
</div>

## Version requirements

Minimum supported:

* React: `16.0.0` or higher
* TypeScript: `3.6.0` or higher (for TypeScript application)
* Vite `4.0.0` or higher (for application build with Vite)

Recommended:

* React: `18.0.0` or higher
* TypeScript: `4.0.0` or higher (for TypeScript application)
* Vite `5.0.0` or higher (for application build with Vite)

## Get Started

In this guide we will explain how to get started if you are using [vitejs.org guide](https://vitejs.dev/guide).

To get started, the broad steps are as follows:

1. [Access to npm registry](##access-to-npm-registry)
2. [Create Application](##create-application)
3. [Install components](##install-components)
4. [Add components to Application](##add-components-to-application)
5. [Apply styles](##apply-styles)
6. [Run the application](##run-the-application)

The application we are about to build together is pretty simple, and will look like the illustration below:

<img src="Gantt/getting-started-result.png" class="b-screenshot" alt="Getting Started on Bryntum Gantt with React Result">

## Access to npm registry

You can try out Bryntum components for free using our public Bryntum trial packages.
If you have a Bryntum license, please refer to our [Npm Repository Guide](#Gantt/guides/npm/repository/private-repository-access.md) to access the private Bryntum repository.

## Create Application

There are many possible ways of creating and building React applications. Let’s use
[React Vite guide](https://vitejs.dev/guide), which has proven to offer higher efficiency and better performance in
development.

If you are using **javascript only**, please type:

```shell
npm create vite@latest bryntum-gantt-app -- --template react
```

or if you prefer using **typescript**:

```shell
npm create vite@latest bryntum-gantt-app -- --template react-ts
```

Please feel free to change `bryntum-gantt-app` to your preferred application name.

Once the template is created, install the node modules:

```shell
cd bryntum-gantt-app
npm install && npm install sass
```

## Install components

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

### Dependencies

The application configuration may add a caret `^` as a prefix of dependencies version. We recommend not to use the caret
character as a version prefix to take upgrades fully under control. If necessary, please check the generated
**package.json** file and replace `dependencies` and `devDependencies` by the following:

<div class="docs-tabs" data-name="licensed">
<div>
    <a>Trial version</a>
    <a>Licensed version</a>
</div>
<div>

```json
"dependencies": {
  "@bryntum/gantt": "npm:@bryntum/gantt-trial@7.2.1",
  "@bryntum/gantt-react": "7.2.1",
  "react": "18.2.0",
  "react-dom": "18.2.0"
},
"devDependencies": {
  "@types/react": "~18.2.14",
  "@types/react-dom": "~18.2.6",
  "@vitejs/plugin-react": "~4.0.1",
  "postinstall": "~0.7.4",
  "sass": "~1.69.6",
  "typescript": "~5.1.6",
  "vite": "~4.4.5"
}
```

</div>
<div>

```json
"dependencies": {
  "@bryntum/gantt": "7.2.1",
  "@bryntum/gantt-react": "7.2.1",
  "react": "18.2.0",
  "react-dom": "18.2.0"
},
"devDependencies": {
  "@types/react": "~18.2.14",
  "@types/react-dom": "~18.2.6",
  "@vitejs/plugin-react": "~4.0.1",
  "postinstall": "~0.7.4",
  "sass": "~1.69.6",
  "typescript": "~5.1.6",
  "vite": "~4.4.5"
}
```

</div>
</div>

<div class="note">

Note: The version of React above is not mandatory and is used here only for the purpose of the example. Please
adjust the dependencies according to your development requirement.

</div>

### Vite Configuration

When using Vite to run a Bryntum application in development mode, in order to fix loading bundles multiple times, it is
recommended to include Bryntum packages in the [optimizeDeps](https://vitejs.dev/config/dep-optimization-options.html)
in **vite.config.js**.
Please follow [this guide](#Gantt/guides/integration/react/troubleshooting.md#vite-application) for more
configuration information.

## Add components to Application

Now that your project has been setup, let's start with creating a config file in the `src`, which will have Gantt
configuration.

<div class="docs-tabs" data-name="Gantt">
<div>
    <a>GanttConfig.js</a>
    <a>GanttConfig.ts</a>
</div>
<div>

```javascript
const ganttProps = {
    startDate  : new Date(2026, 0, 1),
    endDate    : new Date(2026, 2, 1),
    columns    : [{ type : 'name', field : 'name', width : 250 }],
    viewPreset : 'weekAndDayLetter',
    barMargin  : 10,

    project : {
        transport : {
            load : {
                url : 'data.json'
            }
        },
        autoLoad           : true,
        // Automatically introduces a `startnoearlier` constraint for tasks that (a) have no predecessors, (b) do not use
        // constraints and (c) aren't `manuallyScheduled`
        autoSetConstraints : true
    }
};

export { ganttProps };
```

</div>
<div>

```typescript
import { BryntumGanttProps } from "@bryntum/gantt-react";

const ganttProps : BryntumGanttProps = {
    startDate  : new Date(2026, 0, 1),
    endDate    : new Date(2026, 2, 1),
    columns    : [{ type : 'name', field : 'name', width : 250 }],
    viewPreset : 'weekAndDayLetter',
    barMargin  : 10,

    project : {
        transport : {
            load : {
                url : 'data.json'
            }
        },
        autoLoad           : true,
        // Automatically introduces a `startnoearlier` constraint for tasks that (a) have no predecessors, (b) do not use
        // constraints and (c) aren't `manuallyScheduled`
        autoSetConstraints : true
    }
};

export { ganttProps };
```

</div>
</div>

<div class="note">

By default, tasks will automatically be moved to the project's start date if there are
no constraints, dependencies, or manually scheduled tasks. To prevent this, set <code>autoSetConstraints</code> to <code>true</code> in the
ProjectModel configuration.

</div>

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

Next is to replace your `App.jsx` or `App.tsx` with the following code:

<div class="docs-tabs" data-name="App">
<div>
    <a>App.jsx</a>
    <a>App.tsx</a>
</div>
<div>

```javascript
import { BryntumGantt } from '@bryntum/gantt-react';
import { ganttProps } from './ganttConfig';
import './App.scss';

function App() {
  return <BryntumGantt {...ganttProps} />;
}

export default App;
```

</div>
<div>

```typescript
import { FunctionComponent, useRef } from 'react';
import { BryntumGantt } from '@bryntum/gantt-react';
import { ganttProps } from './ganttConfig';
import './App.scss';

const App: FunctionComponent = () => {
  const gantt = useRef<BryntumGantt>(null);

  return <BryntumGantt ref={gantt} {...ganttProps} />;
};

export default App;
```

</div>
</div>

This will setup your Gantt, but you need to apply some styling to it.

If you plan to use stateful React collections for data binding
please check [this guide](#Gantt/guides/integration/react/data-binding.md).

### Apply styles

Including a theme + structural CSS is required to render the Bryntum Gantt correctly, and if you are not replacing the
icons used by the component, you will also need to include Font Awesome.

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

To ensure there is no unexpected styling, delete the `index.css` file and also remove it from the `main.jsx` or `main.tsx`.

Next, rename the `App.css` file to `App.scss` and replace it with the following:

```scss
// FontAwesome is used for icons
@import "@bryntum/gantt/fontawesome/css/fontawesome.css";
@import "@bryntum/gantt/fontawesome/css/solid.css";
// Import gantt's structural CSS
@import "@bryntum/gantt/gantt.css";
// Import your preferred Bryntum theme
@import "@bryntum/gantt/svalbard-light.css";

// Giving our gantt some height
#root {
  height: 100vh;
}
```

Visit [Creating a custom theme](#Gantt/guides/customization/styling.md#creating-a-custom-theme) section for more info on how to create a custom theme.

You can learn more about styling your Bryntum Gantt in our [style guide](#Gantt/guides/customization/styling.md).

## Run the application

Run application development server:

```shell
npm run dev
```

Your application is now available under [http://localhost:5173](http://localhost:5173) in your browser.

Happy coding!

## Next.js guide

If you're looking for a guide on how to use Gantt with Next.js, we have a [blog post](https://bryntum.com/blog/creating-a-gantt-chart-with-react-using-next-js/) that covers the topic. You can also checkout [this boilerplate](https://github.com/bryntum/gantt-chart-nextjs-starter) used in the blog post.

## Troubleshooting

Please refer to this [Troubleshooting guide](#Gantt/guides/integration/react/troubleshooting.md).

## What to do next?

### Further on integration with React

Do you want to know more about how Bryntum Gantt integrates with react and start to customize your application? We
provide you with a [complete React guide here](#Gantt/guides/integration/react/guide.md).

### Learn about Data

[Data Binding Guide](#Gantt/guides/integration/react/data-binding.md) explains how data can be bound to the component.

Bryntum components often use multiple collections and entities.

The [Data guide](#Gantt/guides/data/project_data.md) explains how they all fit together.
