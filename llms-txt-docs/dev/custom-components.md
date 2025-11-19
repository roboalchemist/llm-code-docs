# Source: https://dev.writer.com/framework/custom-components.md

# Custom components

It's possible to extend Framework with custom component templates.

They're developed using Vue 3 and TypeScript. Once transpiled, they can be used by copying them to the `extensions/` folder of any project.

<Note>
  Custom components behave exactly like built-in ones. They are just as
  performant, can contain other components, and offer the same the Builder
  experience. They only differ from built-in components in the way that they're
  bundled and imported.
</Note>

## Architecture

Framework front-end compiles to a collection of static assets that is distributed in the Python package. These static assets are then served via FastAPI.

During initialisation time, the server scans the `extensions/` folder in the project folder and looks for `.css` and `.js` files. This folder is also served, similarly to `static/`. If it finds any valid files in `extensions/`, it shares the list with clients and tells them to dynamically import these files during runtime.

Extensions and custom templates are currently synonyms, but this might change in order to accommodate other extension capabilities.

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.architecture.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=0bf436f6f05141b9c10203b73303db10" alt="Custom Components - Architecture" data-og-width="2291" width="2291" data-og-height="1190" height="1190" data-path="framework/images/custom-components.architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.architecture.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=6231fde8f3a44830f97815af792c03f2 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.architecture.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=7586d22976a23fcc6932b06c090ee88a 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.architecture.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=21b00a736247b9e3f87efd31744c3daa 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.architecture.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=3bea16b735b0df4a2e32df2a3654bdf3 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.architecture.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=8bb6dfb6e518051b28563c9818719924 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.architecture.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=8c3413b6e9f9cf60b52f4f573d4320f1 2500w" />

Dependencies are [provided](https://vuejs.org/api/composition-api-dependency-injection.html) using injection symbols and can be *injected* to be used by the component template. These include `evaluatedFields`, which contain the current values of the editable fields. Injected dependencies are fully typed, making development easier.

[Rollup's external feature](https://rollupjs.org/configuration-options/#external), invoked via Vite, allows for extensions to be compiled without dependencies and link those during runtime. Therefore, extensions aren't bundled to be standalone, but rather to work as a piece of a puzzle.

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.external.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=c79c2bffa0ff892d4b29585339ade35c" alt="Custom Components - External" data-og-width="2291" width="2291" data-og-height="530" height="530" data-path="framework/images/custom-components.external.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.external.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=654595fbeca47504003d6f5ffeb31f7d 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.external.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=e615a2a73dddb54ea6a0cea59b996c35 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.external.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=7273b136b62854eff8b16439ceb07a9c 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.external.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=6d30cabb1ef0149fdb0f2febd67da01d 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.external.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=a62b6fa618fbd333295f255fb9f51746 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.external.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=6f67fb90fdd4de8032177da97bc15c28 2500w" />

## Anatomy of a template

A template defines how a certain component is rendered. For example, `corebutton` defines how *Button* components are rendered.

Framework component templates are purely front-end. They are Vue 3 templates that extend the Vue specification via a [custom option](https://vuejs.org/api/utility-types.html#componentcustomoptions), `writer`. This custom option defines all the Framework-specific behaviour of the component. For example, its `fields` property establishes which fields will be editable via the Builder.

### Simple example

This example shows a template for *Bubble Message*, a simple demo component with one editable field, `text`.

```js  theme={null}
<template>
	<div class="BubbleMessage">
        <div class="triangle"></div>
        <div class="message">

            <!-- Shows the current value of the field "text" -->

            {{ fields.text.value }}
        </div>
	</div>
</template>

<script lang="ts">
export default {
    writer: {
		name: "Bubble Message",
		description: "Shows a message in the shape of a speech bubble.",
		category: "Content",

        // Fields will be editable via Framework Builder

        fields: {
			text: {
				name: "Text",
				type: FieldType.Text,
			},
		},

        // Preview field is used in the Component Tree

		previewField: "text",
	},
};
</script>
<script setup lang="ts">
import { FieldType } from "@/writerTypes";
import injectionKeys from "../injectionKeys";
import { inject } from "vue";

/*
The values for the fields defined earlier in the custom option
will be available using the evaluatedFields injection symbol.
*/

const fields = inject(injectionKeys.evaluatedFields);
</script>

<style scoped>
/* ... */
</style>
```

The code above will make Bubble Message available in the Builder.

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.bubble-message.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=5ea7079317c2b87385b7db8000124156" alt="Custom Components - Bubble Message" data-og-width="2291" width="2291" data-og-height="947" height="947" data-path="framework/images/custom-components.bubble-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.bubble-message.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=061f46e7a1e4fdd1a821f605eb1bf73c 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.bubble-message.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=97783c672e4c80a03d6e21256a76d472 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.bubble-message.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=ba2416f912700193fe2718fa18700d80 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.bubble-message.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=ef3c1991893f36e6ebbe1d2bc3c6889e 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.bubble-message.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=6081d89e40bea7f552f21a37b28431f9 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/custom-components.bubble-message.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=a3ff9667f44767741bc101623745174d 2500w" />

## Developing templates

### Run a local server

<Steps>
  <Step title="Clone the Framework Repository">
    To get started, clone the [Framework
    repository](https://github.com/writer/writer-framework) from GitHub.
  </Step>

  <Step title="Set Up the Development Environment">
    To develop custom templates in a developer-friendly way, ensure you have a
    front-end development server with instant reload capabilities. The front-end
    code for Framework is located in the `ui` folder. With Node and npm
    installed on your system, run `npm install` to install dependencies. Then,
    start the server with support for custom component templates using `npm run
        custom.dev`.

    ```sh cd ui npm install # "custom.dev" links templates in theme={null}
    "custom_components/" # "dev" runs the server without them npm run custom.dev
    ```
  </Step>

  <Step title="Start the Back-End Server">
    The command `npm run custom.dev` starts a front-end server, which requires a
    back-end to function fully. Start Framework via command line, specifying the
    option `--port 5000`, to provide a back-end on that port. It's recommended
    to create a new app for testing the template you're developing. `sh writer
        create customtester writer edit customtester --port 5000 `
  </Step>

  <Step title="Access Framework and Test Custom Component">
    You should now be able to access Framework via the URL provided by Vite,
    e.g. `http://localhost:5174`. In the Builder's *Toolkit*, you should see the
    sample component, *Balloon Message*. Add it to your tester application.
  </Step>
</Steps>

### Create a new component

<Tip>
  You can also have a look at the built-in component templates, since their
  syntax is equivalent. They can be found in the `ui/src/components/core` folder.
</Tip>

Go to `ui/src/components/custom` and open the Vue single-file components, i.e. the
`.vue` files. These files contain comments that will help you get started. Try editing
the provided templates, you should see changes reflected.

You can get started by duplicating one of these examples. Make sure you add the new template to the entrypoint, as discussed below.

### Define entrypoint

For custom component templates to be taken into account, they need to be accessible from the entrypoint. Edit `ui/src/components/custom/index.ts` to define which templates you wish to export and under which identifiers.

```ts  theme={null}
// Import the templates

import BubbleMessage from "./BubbleMessage.vue";
import BubbleMessageAdvanced from "./BubbleMessageAdvanced.vue";

// Export an object with the ids and the templates as default

export default {
  bubblemessage: BubbleMessage,
  bubblemessageadvanced: BubbleMessageAdvanced,
};
```

A single or multiple templates can be specified. Take into account that they will all be exported, and later imported, together.

## Bundling templates

Execute `npm run custom.build` into `src/ui`, this will generate the output `.js` and `.css` files into `./custom_components_dist`.

```sh  theme={null}
# "build" builds the entire front-end
# "custom.build" only builds the custom templates

npm run custom.check # Optional: checks certain issues on custom components
npm run custom.build
```

Collect the files from `./custom_components_dist` and pack them in a folder such as `my_custom_bubbles`. The folder containing the generated files, e.g. `my_custom_bubbles`, can now be placed in the `extensions/` folder of any Framework project. It'll be automatically detected during server startup.

<Tip>
  The `custom.check` command is optional, but it's recommended to run it before building the custom components. It checks for common issues in the custom components, such as invalid key declaration, ...
</Tip>
