# Storybook Documentation
# Source: https://storybook.js.org/docs/configure
# Page: /docs/configure

# Configure Storybook

ReactVueAngularWeb ComponentsMore

Storybook is configured via a folder called `.storybook`, which contains various configuration files.

ℹ️

Note that you can change the folder that Storybook uses by setting the `-c` flag to your `storybook dev` and `storybook build` [CLI commands](./api/cli-options).

## 

Configure your Storybook project

Storybook's main configuration (i.e., the `main.js|ts`) defines your Storybook project's behavior, including the location of your stories, the addons you use, feature flags and other project-specific settings. This file should be in the `.storybook` folder in your project's root directory. You can author this file in either JavaScript or [TypeScript](./configure/integration/typescript). Listed below are the available options and examples of how to use them.

CSF 3CSF Next 🧪

.storybook/main.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
     
    const config: StorybookConfig = {
      // Required
      framework: '@storybook/your-framework',
      stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
      // Optional
      addons: ['@storybook/addon-docs'],
      staticDirs: ['../public'],
    };
     
    export default config;

ℹ️

This configuration file is a [preset](./addons/addon-types) and, as such, has a powerful interface, which can be further customized. Read our documentation on writing [presets](./addons/writing-presets) to learn more.

Configuration element| Description  
---|---  
`stories`| The array of globs that indicates the location of your story files, relative to `main.js`  
`staticDirs`| Sets a list of directories of [static files](./configure/integration/images-and-assets#serving-static-files-via-storybook-configuration) to be loaded by Storybook   
`staticDirs: ['../public']`  
`addons`| Sets the list of [addons](https://storybook.js.org/integrations) loaded by Storybook   
`addons: ['@storybook/addon-docs']`  
`typescript`| Configures how Storybook handles [TypeScript files](./configure/integration/typescript)   
`typescript: { check: false, checkOptions: {} }`  
`framework`| Configures Storybook based on a set of [framework-specific](./configure/integration/frameworks) settings   
`framework: { name: '@storybook/svelte-vite', options:{} }`  
`core`| Configures Storybook's [internal features](./api/main-config/main-config-core)   
`core: { disableTelemetry: true, }`  
`docs`| Configures Storybook's [auto-generated documentation](./writing-docs/autodocs)  
`docs: { defaultName: 'Documentation' }`  
`features`| Enables Storybook's [additional features](./api/main-config/main-config-features)  
See table below for a list of available features  
`refs`| Configures [Storybook composition](./sharing/storybook-composition)   
`refs: { example: { title: 'ExampleStorybook', url:'https://your-url.com' } }`  
`logLevel`| Configures Storybook's logs in the browser terminal. Useful for debugging   
`logLevel: 'debug'`  
`webpackFinal`| Customize Storybook's [Webpack](./builders/webpack) setup   
`webpackFinal: async (config:any) => { return config; }`  
`viteFinal`| Customize Storybook's Vite setup when using the [vite builder](https://github.com/storybookjs/builder-vite)   
`viteFinal: async (config: Vite.InlineConfig, options: Options) => { return config; }`  
`env`| Defines custom Storybook [environment variables](./configure/environment-variables#using-storybook-configuration).   
`env: (config) => ({...config, EXAMPLE_VAR: 'Example var' }),`  
`build`| Optimizes Storybook's production [build](./api/main-config/main-config-build) for performance by excluding specific features from the bundle. Useful when decreased build times are a priority.   
`build: { test: {} }`  
  
## 

Configure story loading

By default, Storybook will load stories from your project based on a glob (pattern matching string) in `.storybook/main.js|ts` that matches all files in your project with extension `.stories.*`. The intention is for you to colocate a story file along with the component it documents.
    
    
    •
    └── components
        ├── Button.js
        └── Button.stories.js
    

If you want to use a different naming convention, you can alter the glob using the syntax supported by [picomatch](https://github.com/micromatch/picomatch#globbing-features).

For example, if you wanted to pull both `.md` and `.js` files from the `my-project/src/components` directory, you could write:

CSF 3CSF Next 🧪

.storybook/main.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
     
    const config: StorybookConfig = {
      framework: '@storybook/your-framework',
      stories: ['../my-project/src/components/*.@(js|md)'],
    };
     
    export default config;

### 

With a configuration object

Additionally, you can customize your Storybook configuration to load your stories based on a configuration object. For example, if you wanted to load your stories from a `packages/components` directory, you could adjust your `stories` configuration field into the following:

CSF 3CSF Next 🧪

.storybook/main.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
     
    const config: StorybookConfig = {
      framework: '@storybook/your-framework',
      stories: [
        {
          // 👇 Sets the directory containing your stories
          directory: '../packages/components',
          // 👇 Storybook will load all files that match this glob
          files: '*.stories.*',
          // 👇 Used when generating automatic titles for your stories
          titlePrefix: 'MyComponents',
        },
      ],
    };
     
    export default config;

When Storybook starts, it will look for any file containing the `stories` extension inside the `packages/components` directory and generate the titles for your stories.

### 

With a directory

You can also simplify your Storybook configuration and load the stories using a directory. For example, if you want to load all the stories inside a `packages/MyStories`, you can adjust the configuration as such:

CSF 3CSF Next 🧪

.storybook/main.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
     
    const config: StorybookConfig = {
      framework: '@storybook/your-framework',
      // 👇 Storybook will load all existing stories within the MyStories folder
      stories: ['../packages/MyStories'],
    };
     
    export default config;

### 

With a custom implementation

You can also adjust your Storybook configuration and implement custom logic to load your stories. For example, suppose you were working on a project that includes a particular pattern that the conventional ways of loading stories could not solve. In that case, you could adjust your configuration as follows:

CSF 3CSF Next 🧪

.storybook/main.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
    import type { StoriesEntry } from 'storybook/internal/types';
     
    async function findStories(): Promise<StoriesEntry[]> {
      // your custom logic returns a list of files
    }
     
    const config: StorybookConfig = {
      framework: '@storybook/your-framework',
      stories: async (list: StoriesEntry[]) => [
        ...list,
        // 👇 Add your found stories to the existing list of story files
        ...(await findStories()),
      ],
    };
     
    export default config;

#### 

Known limitations

Because of the way stories are currently indexed in Storybook, loading stories on demand has a couple of minor limitations at the moment:

  * [CSF formats](./api/csf) from version 1 to version 3 are supported.
  * Custom `storySort` functions are allowed based on a restricted API.



## 

Configure story rendering

To control the way stories are rendered and add global [decorators](./writing-stories/decorators#global-decorators) and [parameters](./writing-stories/parameters#global-parameters), create a `.storybook/preview.js` file. This is loaded in the Canvas UI, the “preview” iframe that renders your components in isolation. Use `preview.js` for global code (such as [CSS imports](./get-started/setup#render-component-styles) or JavaScript mocks) that applies to all stories.

The `preview.js` file can be an ES module and export the following keys:

  * `decorators` \- an array of global [decorators](./writing-stories/decorators#global-decorators)
  * `parameters` \- an object of global [parameters](./writing-stories/parameters#global-parameters)
  * `globalTypes` \- definition of [globalTypes](./essentials/toolbars-and-globals#global-types-and-the-toolbar-annotation)



If you’re looking to change how to order your stories, read about [sorting stories](./writing-stories/naming-components-and-hierarchy#sorting-stories).

## 

Configure Storybook’s UI

To control the behavior of Storybook’s UI (the **“manager”**), you can create a `.storybook/manager.js` file.

This file does not have a specific API but is the place to set [UI options](./configure/user-interface/features-and-behavior) and to configure Storybook’s [theme](./configure/user-interface/theming).

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/configure/index.mdx)