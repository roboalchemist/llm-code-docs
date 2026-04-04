# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/react-remix.md

# Getting started with Bryntum Gantt in Remix

This quick start guide will show you how to build a basic Bryntum Gantt in a Remix TypeScript application.

## Version requirements

Bryntum Gantt requires React `16.0.0` or higher and TypeScript `3.6.0` or higher for applications written in
TypeScript and Remix version `2.15.0` requires [Node LTS version](https://nodejs.org/en).

## Version requirements

Minimum supported:

* React: `16.0.0` or higher
* TypeScript: `3.6.0` or higher (for TypeScript application)
* Vite `4.0.0` or higher (for application build with Vite)

Recommended:

* React: `18.0.0` or higher
* TypeScript: `4.0.0` or higher (for TypeScript application)
* Vite `5.0.0` or higher (for application build with Vite)

## Getting started

To get started, we will follow these steps to create a basic Bryntum Gantt Remix app:

1. [Setup a Remix application](##setup-a-remix-application)
2. [Install the Bryntum Gantt component](##install-the-bryntum-gantt-component)
3. [Create a Bryntum Gantt component](##create-a-bryntum-gantt-component)
4. [Run the application](##run-the-application)

The basic Bryntum Gantt starter template that we'll build will look like this:

<img src="Gantt/getting-started-result.png" class="b-screenshot" alt="Getting Started on
Bryntum Gantt with React Result">

## Setup a Remix application

We'll use the [Remix quick start guide](https://remix.run/docs/en/main/start/quickstart) to create a Remix application.
Create a Remix application by running the following command:

```shell
npx create-remix@latest
```

This command will prompt a few questions:

```bash
- Where should we create your new project?
 my-remix-gantt
- Initialize a new git repository?
 Yes
- Install dependencies with npm?
 Yes
```

After you've selected your answers for the prompt questions, `create-remix` will create a folder with your
project name and install the dependencies.

Change your current working directory to the new Remix project directory:

```shell
cd my-remix-gantt
```

## Install the Bryntum Gantt component

Installing the Bryntum Gantt component using npm is the quickest way to use our products. You can try out Bryntum components for free using our public Bryntum trial packages.
If you have a Bryntum license, please refer to our [Npm Repository Guide](#Gantt/guides/npm/repository/private-repository-access.md#repository-access) to access the private Bryntum repository.

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

You'll also need to install `remix-utils` to do client-side rendering.

```shell
npm install remix-utils
```

### Dependencies

The application configuration may add a caret `^` as a prefix of the dependencies version in your `package.json` file.
We recommend removing the caret character as a version prefix so that you have full control over package updates.

## Create a Bryntum Gantt component

Let's start by creating a config file called `app.config.tsx`.
Create a `components` folder in the `app` folder and add the following lines of code to it:

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

This object will be used for configuration of the Bryntum Gantt component.

Next, we'll create a Bryntum Gantt React component. Create a file called `bryntum.client.tsx` in the
`app/components/` folder. Add the following lines of code to it:

```typescript
import { BryntumGantt } from '@bryntum/gantt-react';
import { ganttProps } from './app.config';

const BryntumClient = () => {
    return (
        <BryntumGantt
            {...GanttProps}
        />
    );
};

export default BryntumClient;
```

The file extension is `.client.tsx` becase Bryntum components are rendered on **client-side** only and Remix uses
`.client.tsx` for client side files.

### Add component data

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

We need to create a wrapper component for the Bryntum Gantt React component to render on the client only.
Replace the `app/routes/_index.tsx` file with the following code:

```typescript
import { ClientOnly } from 'remix-utils/client-only';
import BryntumClient from '~/components/bryntum.client';

export default function Index() {
    return (
        <ClientOnly fallback={<h1>Loading Bryntum Gantt</h1>}>
            {() => <BryntumClient/>}
        </ClientOnly>
    );
}
```

Where the `ClientOnly` lets you render the components on the client-side only.

### Styling

To style the Bryntum Gantt, create a `app/styles/` folder and add `index.css` file:

```css
body,
html {
    margin         : 0;
    display        : flex;
    flex-direction : column;
    height         : 100vh;
    font-family    : Poppins, "Open Sans", Helvetica, Arial, sans-serif;
    font-size      : 14px;
}
```

Import the `index.css` file along with the structural CSS for Gantt and the Bryntum theme of your choice in
`Bryntum.client.tsx`:

```typescript
/* FontAwesome is used for icons */
import "@bryntum/gantt/fontawesome/css/fontawesome.css";
import "@bryntum/gantt/fontawesome/css/solid.css";
/* Import the structural CSS for gantt */
import "@bryntum/gantt/gantt.css";
/* Import a Bryntum theme */
import "@bryntum/gantt/svalbard-light.css";
import "../styles/index.css";
```

Visit [Creating a custom theme](#Gantt/guides/customization/styling.md#creating-a-custom-theme) section for more info on how to create a custom theme.

You can learn more about styling your Bryntum Gantt in our [style guide](#Gantt/guides/customization/styling.md).

## Run the application

Run the local development server:

```shell
npm run dev
```

You'll see the Bryntum Gantt app at the URL [http://localhost:5173/](http://localhost:5173/).

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
