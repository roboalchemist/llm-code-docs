# Source: https://juno.build/docs/guides/vue/build.md

# Source: https://juno.build/docs/guides/sveltekit/build.md

# Source: https://juno.build/docs/guides/react/build.md

# Source: https://juno.build/docs/guides/nextjs/build.md

# Source: https://juno.build/docs/guides/astro/build.md

# Source: https://juno.build/docs/guides/angular/build.md

# Build an Angular App

Ready to implement a feature-rich application with Juno? You can choose a step-by-step approach, building each component gradually, or dive into our quickstart template, which showcases Juno's core features.

Which path would you like to explore next?

([Step-by-step](#step-by-step))([Quickstart](#quickstart))

---

## Step-by-step

This guide provides quickstart instructions for integrating Juno in two scenarios: starting a new project and adding Juno to an existing Angular app.

### 1\. Choose Your Integration Path

You can either start a new project or add Juno to an existing app.

### Path A: Start a new project with a template

Create a new project using the Juno quickstart CLI:

*   npm
*   yarn
*   pnpm

```
npm create juno@latest -- --template angular-starter
```

```
yarn create juno -- --template angular-starter
```

```
pnpm create juno -- --template angular-starter
```

### Path B: Integrate Juno into an existing Angular app

Navigate to your existing app:

```
cd your-existing-app
```

and install Juno SDK:

*   npm
*   yarn
*   pnpm

```
npm i @junobuild/core
```

```
yarn add @junobuild/core @icp-sdk/core @icp-sdk/auth @dfinity/utils
```

```
pnpm add @junobuild/core @icp-sdk/core @icp-sdk/auth @dfinity/utils
```

### 2\. Start the Emulator

If the Juno admin CLI (required to run the emulator) is not installed yet, run:

```
npm i -g @junobuild/cli
```

Once installed, start the local emulator:

```
juno emulator start
```

Open the Console UI at [http://localhost:5866/](http://localhost:5866/).

**Note:**

When developing locally, you get an all-in-one emulator that closely mimics the production environment. This includes providing Juno and its Console UI locally.

Sign in, create a Satellite, navigate to the **Datastore** section, and create a collection named **demo**.

### 3\. Configure

To initialize your project with the Satellite ID you created, configure it in the `juno.config.mjs` file (or other extension), which should be available at the root.

Replace `<DEV_SATELLITE_ID>` with the ID.

```
import { defineConfig } from "@junobuild/config";/** @type {import('@junobuild/config').JunoConfig} */export default defineConfig({  satellite: {    ids: {      development: "<DEV_SATELLITE_ID>",      production: "<PROD_SATELLITE_ID>"    },    source: "out",    predeploy: ["npm run build"]  }});
```

In addition, add also the ID to your `environment.ts` file:

```
export const environment = {  satelliteId: "<DEV_SATELLITE_ID>"};
```

### 4\. Insert data from your app

In `app.component.ts`, initialize the Satellite.

Add an `insert` function to persist a document.

app.component.ts

```
import { Component } from "@angular/core";import { type Doc, initSatellite, setDoc } from "@junobuild/core";import { environment } from "../environments/environment";@Component({  selector: "app-root",  template: `    <button (click)="insert()">Insert a document</button>    <span *ngIf="doc !== undefined">Key: {{ doc.key }}</span>  `,  styleUrls: ["./app.component.css"]})export class AppComponent {  doc: Doc<{ hello: string }> | undefined = undefined;  async ngOnInit() {    await initSatellite({      satelliteId: environment.satelliteId    });  }  async insert() {    this.doc = await setDoc({      collection: "demo",      doc: {        key: window.crypto.randomUUID(),        data: {          hello: "world"        }      }    });  }}
```

### 5\. Start the app

Start the app, go to [http://localhost:4200](http://localhost:4200) in a browser, click "Insert a document," and you should see the data successfully persisted in your satellite.

**What's Next: Going Live:**

Once you're ready to deploy your app for others to access, continue to the [Deployment guide](/docs/guides/angular/deploy.md).

---

## Quickstart

This example demonstrates how to quickly deploy a basic note-taking app that integrates Juno's core features:

*   [Authentication](/docs/build/authentication.md): easy-to-use SDKs that support truly anonymous authentication.
*   [Datastore](/docs/build/datastore.md): a simple key-pair database for storing user data and other information.
*   [Storage](/docs/build/storage.md): a file storage system to store and serve user-generated content, such as photos.

Using the Juno CLI, you can easily scaffold this app.

*   npm
*   yarn
*   pnpm

```
npm create juno@latest -- --template angular-example
```

```
yarn create juno -- --template angular-example
```

```
pnpm create juno -- --template angular-example
```

  

Follow the CLI prompts to choose the note-taking app example and select local development. The CLI will manage all configurations and dependencies, allowing you to focus on exploring and customizing your app right away.