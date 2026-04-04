# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/quick-start/nextjs.md

# Getting started with Bryntum Gantt in Next.js

This quick start guide will show you how to build a basic Bryntum Gantt in a Next.js TypeScript application using the
[Next.js getting started guide](https://nextjs.org/docs/getting-started/installation) as a starting point.

You can also take a shortcut and start with our
[Bryntum Gantt Next.js with TypeScript starter template](https://github.com/bryntum/bryntum-gantt-nextjs-quick-start)
that we will create in this guide.

## Requirements

Next.js version 15 requires [Node.js 18.18](https://nodejs.org/) or higher. Bryntum Gantt requires React `16.0.0`
or higher and TypeScript `3.6.0` or higher for applications written in TypeScript.

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

To get started, we'll follow these steps to create a basic Bryntum Gantt Next.js app:

1. Setup a Next.js application.
2. Install the Bryntum Gantt component.
3. Create a Bryntum Gantt component.
4. Run the application.

The basic Bryntum Gantt starter template that we'll build will look like this:

<img src="Gantt/getting-started-result.png" class="b-screenshot" alt="Getting Started on Bryntum Gantt with Next.js Result">

## Setup a Next.js application

We will use the [Next.js getting started guide](https://nextjs.org/docs/getting-started/installation) to create a
Next.js application. Next.js recommends using `create-next-app` to create a new Next.js app as it sets everything up
for you, automatically. Create a Next.js application by running the following command:

```shell
npx create-next-app@latest
```

You'll see multiple prompts. To follow along with this guide, choose the following options:

```shell
What is your project named? bryntum-gantt
Would you like to use TypeScript? No / Yes ✔️
Would you like to use ESLint? No / Yes ✔️
Would you like to use Tailwind CSS? No ✔️ / Yes
Would you like to use `src/` directory? No ✔️ / Yes 
Would you like to use App Router? (recommended) No / Yes ✔️
Would you like to use Turbopack for `next dev`? No ✔️ / Yes
Would you like to customize the default import alias (@/*)? No ✔️ / Yes
```

After you've selected your answers for the prompt questions, `create-next-app` will create a folder with your
project name and install the dependencies.

Change your current working directory to the new Next.js project directory:

```shell
cd bryntum-gantt
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

### Dependencies

The application configuration may add a caret `^` as a prefix of the dependencies version in your `package.json` file.
We recommend removing the caret character as a version prefix so that you have full control over package updates.

## Create a Bryntum Gantt component

Create a config file called `ganttConfig.ts` in the `app/` folder. Add the following lines of code to it:

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

<div class="note">

By default, tasks will automatically be moved to the project's start date if there are
no constraints, dependencies, or manually scheduled tasks. To prevent this, set <code>autoSetConstraints</code> to <code>true</code> in the
ProjectModel configuration.

</div>

Create a file called `Gantt.tsx` in the `app/components/` folder. Add the following lines of code to it:

```typescript
"use client";

import { BryntumGantt } from "@bryntum/gantt-react";
import { useEffect, useRef } from "react";

export default function Gantt({ ...props }) {
  const ganttRef = useRef<BryntumGantt>(null);

  useEffect(() => {
    // Bryntum Gantt instance
    const gantt = ganttRef?.current?.instance;
  }, []);

  return <BryntumGantt {...props} ref={ganttRef} />;
}
```

The Gantt component is a React
[client component](https://nextjs.org/docs/app/building-your-application/rendering/client-components) as it uses the
`"use client"` directive at the top of the file.

The code in the useEffect hook setup function shows you how to access the Bryntum Gantt instance.

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

We need to create a wrapper component for the Bryntum Gantt React component to render on the client only.
In the `components` folder, create a file called `GanttWrapper.tsx` and add the following lines of code to it:

```typescript
'use client';

import dynamic from "next/dynamic";
import { ganttProps } from "../ganttConfig";

const Gantt = dynamic(() => import("./Gantt"), {
  ssr: false,
  loading: () => {
    return (
      <div
        style={{
          display        : "flex",
          alignItems     : "center",
          justifyContent : "center",
          height         : "100vh",
        }}
      >
        <p>Loading...</p>
      </div>
    );
  },
});

const GanttWrapper = () => {
    return <Gantt {...ganttProps} />
};
export { GanttWrapper };
```

The Bryntum Gantt React component is
[dynamically imported](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading#nextdynamic)
with server-side rendering (`ssr`) set to `false`. This is done to prevent the Bryntum Gantt React client component
from being pre-rendered on the server as Bryntum components are client-side only.

<div class="note">

If the above throws an error, replace the <code>ssr: false,</code> with <code>ssr: !!false,</code>.

</div>

Next, replace the code in the `app/page.tsx` file with the following lines of code:

```typescript
import { GanttWrapper } from "@/app/components/GanttWrapper";
/* FontAwesome is used for icons */
import "@bryntum/gantt/fontawesome/css/fontawesome.css";
import "@bryntum/gantt/fontawesome/css/solid.css";
/* Importing Gantt's structural CSS and a theme */
import "@bryntum/gantt/gantt.css";
import "@bryntum/gantt/svalbard-light.css";
import styles from "./page.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <GanttWrapper />
    </main>
  );
}
```

We imported the CSS styles for the Bryntum Gantt Svalbard Light theme, which is one of five available themes.

## Styling

To style the Bryntum Gantt so that it takes up the whole page, replace the styles in the `app/globals.css`
file with the following styles:

```css
body,
html {
  margin: 0;
  display: flex;
  flex-direction: column;
  height: 100vh;
  font-family: Poppins, "Open Sans", Helvetica, Arial, sans-serif;
  font-size: 14px;
}
```

Create `src/app/page.module.css` file with the following style for the `<main>` HTML tag:

```css
.main {
  height: 100%;
}
```

If you want to customize the default theme, you can replace the `stockholm.css` with the sass version.
Visit [Creating a custom theme](#Gantt/guides/customization/styling.md#creating-a-custom-theme) section for more info.

You can learn more about styling your Bryntum Gantt in our [style guide](#Gantt/guides/customization/styling.md).

## Using ref outside Gantt Component

To access the Bryntum Gantt instance outside of `Gantt.tsx`, you can use React’s `useRef` hook. Typically,
you would use `forwardRef`; however, in this case, the Gantt component is lazy-loaded, so the ref needs to be
passed as a regular prop. To implement this, make the `GanttWrapper.tsx` a client component, create a ref in the
`GanttWrapper` function and pass it as a prop to the Gantt:

```typescript
"use client"; // make it a client component

import { useEffect, useRef } from "react";
import { BryntumGantt } from "@bryntum/gantt-react";

const GanttWrapper = () => {
  const ganttRef = useRef<BryntumGantt>(null);

  useEffect(() => {
    // For testing purposes, since Gantt is lazy loaded, ganttRef is null initially
    setTimeout(() => {
      console.log(ganttRef);
    }, 2000);
  });

  return <Gantt ganttRef={ganttRef} {...ganttProps} />;
};
```

In `Gantt.tsx`, define the `Props` type:

```typescript
type Props = {
  ganttRef: React.Ref<BryntumGantt>;
} & BryntumGanttProps;
```

Next, pass and apply the `ganttRef` within the `Gantt` function and remove any existing ref used for
`BryntumGantt`.

```typescript
export default function Gantt({ ganttRef, ...props }: Props) {
  return (
    <BryntumGantt
      {...props}
      ref={ganttRef}
      // additional config
    />
  );
}
```

Gantt can now be accessed from `Gantt`, letting you access Gantt's events and configs.

## Run the application

Run the local development server:

```shell
npm run dev
```

You'll see the Bryntum Gantt app at the URL [http://localhost:3000](http://localhost:3000/).
