# Storybook Documentation
# Source: https://storybook.js.org/docs/faq
# Page: /docs/faq

# Frequently Asked Questions

ReactVueAngularWeb ComponentsMore

Here are some answers to frequently asked questions. If you have a question, you can ask it in our [GitHub discussions](https://github.com/storybookjs/storybook/discussions/new?category=help).

## 

Error: No angular.json file found

Storybook can be set up for both single-project and multi-project Angular workspaces. To set up Storybook for a project, run [the install command](./get-started/install) at the root of the workspace where the `angular.json` file is located. During initialization, the `.storybook` folder will be created and the `angular.json` file will be edited to add the Storybook configuration for the selected project. It's important to run the command at the root level to ensure that Storybook detects all projects correctly.

## 

How can I opt-out of Angular Ivy?

In case you are having trouble with Angular Ivy you can deactivate it in your `main.js|ts`:

.storybook/main.js|ts
    
    
    export default {
      stories: [
        /* ... */
      ],
      addons: [
        /* ... */
      ],
      framework: {
        name: '@storybook/angular',
        options: {
          enableIvy: false,
        },
      },
    };

## 

How can I opt-out of Angular ngcc?

In case you postinstall ngcc, you can disable it:

.storybook/main.js|ts
    
    
    export default {
      stories: [
        /* ... */
      ],
      addons: [
        /* ... */
      ],
      framework: {
        name: '@storybook/angular',
        options: {
          enableNgcc: false,
        },
      },
    };

Please report any issues related to Ivy in our [GitHub Issue Tracker](https://github.com/storybookjs/storybook/labels/app%3A%20angular) as the support for View Engine will be dropped in a future release of Angular.

## 

How can I run coverage tests with Create React App and leave out stories?

Create React App does not allow providing options to Jest in your `package.json`, however you can run `jest` with commandline arguments:
    
    
    npm test -- --coverage --collectCoverageFrom='["src/**/*.{js,jsx}","!src/**/stories/*"]'

💡

If you're using [`Yarn`](https://yarnpkg.com/) as a package manager, you'll need to adjust the command accordingly.

## 

How do I setup Storybook to share Webpack configuration with Next.js?

You can generally reuse Webpack rules by placing them in a file that is imported from both your `next.config.js` and your `.storybook/main.js|ts` files. For example:

.storybook/main.js|ts
    
    
    export default {
      webpackFinal: async (baseConfig) => {
        const nextConfig = await import('/path/to/next.config.js');
     
        // merge whatever from nextConfig into the webpack config storybook will use
        return { ...baseConfig, ...nextConfig };
      },
    };

## 

How do I fix module resolution in special environments?

In case you are using [Yarn Plug-n-Play](https://yarnpkg.com/features/pnp) or your project is set up within a mono repository environment, you might run into issues with module resolution similar to this when running Storybook:
    
    
    WARN   Failed to load preset: "@storybook/react-webpack5/preset"
    Required package: @storybook/react-webpack5 (via "@storybook/react-webpack5/preset")

To fix this, you can wrap the package name inside your Storybook configuration file (i.e., `.storybook/main.js|ts`) as follows:

CSF 3CSF Next 🧪

.storybook/main.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
     
    import { dirname } from 'node:path';
    import { fileURLToPath } from 'node:url';
     
    const getAbsolutePath = (packageName: string) =>
      dirname(fileURLToPath(import.meta.resolve(`${packageName}/package.json`)));
     
    const config: StorybookConfig = {
      framework: {
        // Replace your-framework with the same one you've imported above.
        name: getAbsolutePath('@storybook/your-framework'),
        options: {},
      },
      stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
      addons: [
        //👇 Use getAbsolutePath when referencing Storybook's addons and frameworks
        getAbsolutePath('@storybook/addon-docs'),
      ],
    };
     
    export default config;

## 

How do I setup the new React Context Root API with Storybook?

If your installed React Version equals or is higher than 18.0.0, the new React Root API is automatically used and the newest React [concurrent features](https://reactjs.org/docs/concurrent-mode-intro.html) can be used.

You can opt-out from the new React Root API by setting the following property in your `.storybook/main.js|ts` file:

.storybook/main.js|ts
    
    
    export default {
      framework: {
        name: '@storybook/react-webpack5',
        options: {
          legacyRootApi: true,
        },
      },
    };

## 

Why is there no addons channel?

A common error is that an addon tries to access the "channel", but the channel is not set. It can happen in a few different cases:

  1. You're trying to access addon channel (e.g., by calling `setOptions`) in a non-browser environment like Jest. You may need to add a channel mock:
         
         import { addons, mockChannel } from 'storybook/preview-api';
          
         addons.setChannel(mockChannel());

  2. In React Native, it's a special case documented in [#1192](https://github.com/storybookjs/storybook/issues/1192)




## 

Why aren't the addons working in a composed Storybook?

Composition is a new feature that we released with version 6.0, and there are still some limitations to it.

For now, the addons you're using in a composed Storybook will not work.

We're working on overcoming this limitation, and soon you'll be able to use them as if you are working with a non-composed Storybook.

## 

Can I have a Storybook with no local stories?

Storybook does not work unless you have at least one local story (or docs page) defined in your project. In this context, local means a `.stories.*` or `.mdx` file that is referenced in your project's `.storybook/main.js` config.

If you're in a [Storybook composition](./sharing/storybook-composition) scenario, where you have multiple Storybooks, and want to have an extra Storybook with no stories of its own, that serves as a "glue" for all the other Storybooks in a project for demo/documentation purposes, you can do the following steps:

Introduce a single `.mdx` docs page (addon-docs required), that serves as an Introduction page, like so:

Introduction.mdx
    
    
    # Welcome
     
    Some description here

And then refer to it in your Storybook config file:

.storybook/main.js|ts
    
    
    const config = {
      // define at least one local story/page here
      stories: ['../Introduction.mdx'],
      // define composed Storybooks here
      refs: {
        firstProject: { title: 'First', url: 'some-url' },
        secondProject: { title: 'Second', url: 'other-url' },
      },
      // ...
    };
    export default config;

## 

Which community addons are compatible with the latest version of Storybook?

Starting with Storybook version 6.0, we've introduced some great features aimed at streamlining your development workflow.

With this, we would like to point out that if you plan on using addons created by our fantastic community, you need to consider that some of those addons might be working with an outdated version of Storybook.

We're actively working to provide a better way to address this situation, but in the meantime, we'd like to ask for a bit of caution on your end so that you don't run into unexpected problems. Let us know by leaving a comment in the following [GitHub issue](https://github.com/storybookjs/storybook/issues/26031) so that we can gather information and expand the current list of addons that need to be updated to work with the latest version of Storybook.

## 

Is it possible to browse the documentation for past versions of Storybook?

With the release of version 6.0, we updated our documentation as well. That doesn't mean that the old documentation was removed. We kept it to help you with your Storybook migration process. Use the content from the table below in conjunction with our [migration guide](https://github.com/storybookjs/storybook/blob/next/MIGRATION.md).

We're only covering versions 5.3 and 5.0 as they were important milestones for Storybook. If you want to go back in time a little more, you'll have to check the specific release in the monorepo.

Section| Page| Current Location| Version 5.3 location| Version 5.0 location  
---|---|---|---|---  
N/A| Why Storybook| [See current documentation](./get-started/why-storybook)| Non existing feature or undocumented| Non existing feature or undocumented  
Get started| Install| [See current documentation](./get-started/install)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/guides/quick-start-guide)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/guides/quick-start-guide)  
| What's a story| [See current documentation](./get-started/whats-a-story)| [See versioned documentation for your framework](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/guides)| [See versioned documentation for your framework](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/guides)  
| Browse Stories| [See current documentation](./get-started/browse-stories)| [See versioned documentation for your framework](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/guides)| [See versioned documentation for your framework](https://github.com/storybookjs/storybook/blob/release/5.0/docs/src/pages/guides)  
| Setup| [See current documentation](./get-started/setup)| [See versioned documentation for your framework](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/guides)| [See versioned documentation for your framework](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/guides)  
Write stories| Introduction| [See current documentation](./writing-stories)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/basics/writing-stories)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/basics/writing-stories)  
| Parameters| [See current documentation](./writing-stories/parameters)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/basics/writing-stories/index.md#parameters)| Non existing feature or undocumented  
| Decorators| [See current documentation](./writing-stories/decorators)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/basics/writing-stories/index.md#decorators)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/basics/writing-stories/index.md#using-decorators)  
| Naming components and hierarchy| [See current documentation](./writing-stories/naming-components-and-hierarchy)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/basics/writing-stories)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/basics/writing-stories)  
| Build pages and screens| [See current documentation](./writing-stories/build-pages-with-storybook)| Non existing feature or undocumented| Non existing feature or undocumented  
| Stories for multiple components| [See current documentation](./writing-stories/stories-for-multiple-components)| Non existing feature or undocumented| Non existing feature or undocumented  
Write docs| Autodocs| [See current documentation](./writing-docs/autodocs)| See versioned addon documentation| Non existing feature or undocumented  
| MDX| [See current documentation](./writing-docs/mdx)| See versioned addon documentation| Non existing feature or undocumented  
| Doc Blocks| [See current documentation](./writing-docs/doc-blocks)| Non existing feature or undocumented| Non existing feature or undocumented  
| Preview and build docs| [See current documentation](./writing-docs/build-documentation)| Non existing feature or undocumented| Non existing feature or undocumented  
Testing| Visual tests| [See current documentation](./writing-tests/visual-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/testing/automated-visual-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/testing/automated-visual-testing)  
| Accessibility tests| [See current documentation](./writing-tests/accessibility-testing)| Non existing feature or undocumented| Non existing feature or undocumented  
| Interaction tests| [See current documentation](./writing-tests/interaction-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/testing/interaction-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/testing/interaction-testing)  
| Snapshot tests| [See current documentation](./writing-tests/snapshot-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/testing/structural-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/testing/structural-testing)  
| Import stories in tests/Unit tests| [See current documentation](./writing-tests/integrations/stories-in-unit-tests)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/testing/react-ui-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/testing/react-ui-testing)  
| Import stories in tests/End-to-end testing| [See current documentation](./writing-tests/integrations/stories-in-end-to-end-tests)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/testing/react-ui-testing)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/testing/react-ui-testing)  
Sharing| Publish Storybook| [See current documentation](./sharing/publish-storybook)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/basics/exporting-storybook)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/basics/exporting-storybook)  
| Embed| [See current documentation](./sharing/embed)| Non existing feature or undocumented| Non existing feature or undocumented  
| Composition| [See current documentation](./sharing/storybook-composition)| Non existing feature or undocumented| Non existing feature or undocumented  
| Package Composition| [See current documentation](./sharing/package-composition)| Non existing feature or undocumented| Non existing feature or undocumented  
Essentials| Controls| [See current documentation](./essentials/controls)| Controls are specific to version 6.0 see [Knobs versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/addons/knobs)| Controls are specific to version 6.0 see [Knobs versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/addons/knobs)  
| Actions| [See current documentation](./essentials/actions)| [See addon versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/addons/actions)| [See addon versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/addons/actions)  
| Viewport| [See current documentation](./essentials/viewport)| [See addon versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/addons/viewport)| [See addon versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/addons/viewport)  
| Backgrounds| [See current documentation](./essentials/backgrounds)| [See addon versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/addons/backgrounds)| [See addon versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/addons/backgrounds)  
| Toolbars and globals| [See current documentation](./essentials/toolbars-and-globals)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/basics/toolbar-guide)| Non existing feature or undocumented  
Configure| Overview| [See current documentation](./configure)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/overview)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/basics/writing-stories)  
| Integration/Frameworks| [See current documentation](./configure/integration/frameworks)| Non existing feature or undocumented| Non existing feature or undocumented  
| Integration/Framework support for frameworks| [See current documentation](./configure/integration/frameworks-feature-support)| Non existing feature or undocumented| Non existing feature or undocumented  
| Integration/Compilers| [See current documentation](./configure/integration/compilers)| See versioned documentation [here](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/custom-babel-config)| See versioned documentation [here](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/custom-babel-config)  
| Integration/Typescript| [See current documentation](./configure/integration/typescript)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/typescript-config)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/typescript-config)  
| Integration/Styling and CSS| [See current documentation](./configure/styling-and-css)| See versioned documentation| See versioned documentation  
| Integration/Images and assets| [See current documentation](./configure/integration/images-and-assets)| See versioned documentation| See versioned documentation  
| Story rendering| [See current documentation](./configure/story-rendering)| See versioned documentation [here](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/add-custom-head-tags) and [here](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/add-custom-body)| See versioned documentation [here](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/add-custom-head-tags)  
| Story Layout| [See current documentation](./configure/story-layout)| Non existing feature or undocumented| Non existing feature or undocumented  
| User Interface/Features and behavior| [See current documentation](./configure/user-interface/features-and-behavior)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/options-parameter)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/options-parameter)  
| User Interface/Theming| [See current documentation](./configure/user-interface/theming)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/theming)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/theming)  
| User Interface/Sidebar & URLS| [See current documentation](./configure/user-interface/sidebar-and-urls)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/options-parameter)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/options-parameter)  
| Environment variables| [See current documentation](./configure/environment-variables)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/env-vars)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/env-vars)  
Builders| Introduction| [See current documentation](./builders)| Non existing feature or undocumented| Non existing feature or undocumented  
| Vite| [See current documentation](./builders/vite)| Non existing feature or undocumented| Non existing feature or undocumented  
| Webpack| [See current documentation](./builders/webpack)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/custom-webpack-config/index.md)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/custom-webpack-config/index.md)  
| Builder API| [See current documentation](./builders/builder-api)| Non existing feature or undocumented| Non existing feature or undocumented  
Addons| Introduction| [See current documentation](./addons)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/addons/writing-addons)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/addons/writing-addons)  
| Install addons| [See current documentation](./addons/install-addons)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/addons/using-addons/)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/addons/using-addons/)  
| Writing Addons| [See current documentation](./addons/writing-addons)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/addons/writing-addons)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/addons/writing-addons)  
| Writing Presets| [See current documentation](./addons/writing-presets)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/presets/writing-presets)| Non existing feature or undocumented  
| Addons Knowledge Base| [See current documentation](./addons/addon-knowledge-base)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/addons/writing-addons)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/addons/writing-addons)  
| Types of addons| [See current documentation](./addons/addon-types)| Non existing feature or undocumented| Non existing feature or undocumented  
| Addons API| [See current documentation](./addons/addons-api)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/addons/api)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/addons/api)  
API| @storybook/addon-docs/blocks/ArgTypes| [See current documentation](./api/doc-blocks/doc-block-argtypes)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Canvas| [See current documentation](./api/doc-blocks/doc-block-canvas)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/ColorPalette| [See current documentation](./api/doc-blocks/doc-block-colorpalette)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Controls| [See current documentation](./api/doc-blocks/doc-block-controls)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Description| [See current documentation](./api/doc-blocks/doc-block-description)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/IconGallery| [See current documentation](./api/doc-blocks/doc-block-icongallery)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Markdown| [See current documentation](./api/doc-blocks/doc-block-markdown)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Meta| [See current documentation](./api/doc-blocks/doc-block-meta)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Primary| [See current documentation](./api/doc-blocks/doc-block-primary)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Source| [See current documentation](./api/doc-blocks/doc-block-source)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Stories| [See current documentation](./api/doc-blocks/doc-block-stories)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Story| [See current documentation](./api/doc-blocks/doc-block-story)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Subtitle| [See current documentation](./api/doc-blocks/doc-block-subtitle)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Title| [See current documentation](./api/doc-blocks/doc-block-title)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Typeset| [See current documentation](./api/doc-blocks/doc-block-typeset)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/Unstyled| [See current documentation](./api/doc-blocks/doc-block-unstyled)| Non existing feature or undocumented| Non existing feature or undocumented  
| @storybook/addon-docs/blocks/useOf| [See current documentation](./api/doc-blocks/doc-block-useof)| Non existing feature or undocumented| Non existing feature or undocumented  
| Stories/Component Story Format (see note below)| [See current documentation](./api/csf)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/formats/component-story-format)| Non existing feature or undocumented  
| ArgTypes| [See current documentation](./api/arg-types)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/Overview| [See current documentation](./api/main-config/main-config)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/framework| [See current documentation](./api/main-config/main-config-framework)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/stories| [See current documentation](./api/main-config/main-config-stories)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/addons| [See current documentation](./api/main-config/main-config-addons)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/babel| [See current documentation](./api/main-config/main-config-babel)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/babelDefault| [See current documentation](./api/main-config/main-config-babel-default)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/build| [See current documentation](./api/main-config/main-config-build)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/core| [See current documentation](./api/main-config/main-config-core)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/docs| [See current documentation](./api/main-config/main-config-docs)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/env| [See current documentation](./api/main-config/main-config-env)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/features| [See current documentation](./api/main-config/main-config-features)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/indexers| [See current documentation](./api/main-config/main-config-indexers)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/logLevel| [See current documentation](./api/main-config/main-config-log-level)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/managerHead| [See current documentation](./api/main-config/main-config-manager-head)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/previewAnnotations| [See current documentation](./api/main-config/main-config-preview-annotations)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/previewBody| [See current documentation](./api/main-config/main-config-preview-body)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/previewHead| [See current documentation](./api/main-config/main-config-preview-head)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/refs| [See current documentation](./api/main-config/main-config-refs)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/staticDirs| [See current documentation](./api/main-config/main-config-static-dirs)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/swc| [See current documentation](./api/main-config/main-config-swc)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/typescript| [See current documentation](./api/main-config/main-config-typescript)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/viteFinal| [See current documentation](./api/main-config/main-config-vite-final)| Non existing feature or undocumented| Non existing feature or undocumented  
| `main.js` configuration/webpackFinal| [See current documentation](./api/main-config/main-config-webpack-final)| Non existing feature or undocumented| Non existing feature or undocumented  
| Frameworks| [See current documentation](./api/new-frameworks)| Non existing feature or undocumented| Non existing feature or undocumented  
| CLI options| [See current documentation](./api/cli-options)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.3/docs/src/pages/configurations/cli-options)| [See versioned documentation](https://github.com/storybookjs/storybook/tree/release/5.0/docs/src/pages/configurations/cli-options)  
  
ℹ️

If you have stories written with the older `storiesOf` format, it was removed in Storybook 8.0 and is no longer maintained. We recommend that you migrate your stories to CSF. See the [migration guide](./releases/migration-guide#major-breaking-changes) for more information. However, if you need, you can still access the old `storiesOf` [documentation](https://github.com/storybookjs/storybook/blob/release/5.3/docs/src/pages/formats/storiesof-api/index.md) for reference.

## 

What icons are available for my toolbar or my addon?

With the [`@storybook/icons`](https://www.npmjs.com/package/@storybook/icons) package, you get a set of icons that you can use to customize your UI. Go through the [documentation](https://main--64b56e737c0aeefed9d5e675.chromatic.com/?path=/docs/introduction--docs) to see how the icons look and use it as a reference when writing your addon or defining your Storybook global types.

## 

I see a "No Preview" error with a Storybook production build

If you're using the `serve` package to verify your production build of Storybook, you'll get that error. It relates to how `serve` handles rewrites. For instance, `/iframe.html` is rewritten into `/iframe`, and you'll get that error.

We recommend that you use [http-server](https://www.npmjs.com/package/http-server) instead and use the following command to preview Storybook:
    
    
    npx http-server storybook-static

ℹ️

Suppose you don't want to run the command above frequently. Add `http-server` as a development dependency and create a new script to preview your production build of Storybook.

## 

Can I use Storybook with Vue 2?

Vue 2 entered [End of Life](https://v2.vuejs.org/lts/) (EOL) on December 31, 2023, and is no longer supported by the Vue team. As a result, we've stopped supporting Vue 2 in Storybook 8 and above and will not be releasing any new versions that support it. We recommend upgrading your project to Vue 3, which Storybook fully supports. If that's not an option, you can still use Storybook with Vue 2 by installing the latest version of Storybook 7 with the following command:

npm
    
    
    npx storybook@^7 init

## 

Why aren't my code blocks highlighted with Storybook MDX?

Out of the box, Storybook provides syntax highlighting for a set of languages (e.g., Javascript, Markdown, CSS, HTML, Typescript, GraphQL) you can use with your code blocks. Currently, there's a known limitation when you try to register a custom language to get syntax highlighting. We're working on a fix for this and will update this section once it's available.

## 

Why aren't my MDX styles working in Storybook?

Writing documentation with MDX can be troublesome, especially regarding how your code is formatted when using line breaks with code blocks. For example, this will break:

Example.mdx
    
    
    <style>{`
      .class1 {
        ...
      }
     
      .class2 {
        ...
      }
    `}</style>

But this will work:

Example.mdx
    
    
    <style>
      {`
        .class1 {
          ...
        }
     
        .class2 {
          ...
        }
      `}
    </style>

See the following [issue](https://github.com/mdx-js/mdx/issues/1945) for more information.

## 

Why are my mocked GraphQL queries failing with Storybook's MSW addon?

If you're working with Vue 3, you'll need to install [`@vue/apollo-composable`](https://www.npmjs.com/package/@vue/apollo-composable). With Svelte, you'll need to install [`@rollup/plugin-replace`](https://www.npmjs.com/package/@rollup/plugin-replace) and update your `rollup.config` file to the following:

rollup.config.js
    
    
    // Boilerplate imports
     
    import replace from '@rollup/plugin-replace';
    const production = !process.env.ROLLUP_WATCH;
     
    // Remainder rollup.config implementation
     
    export default {
      input: 'src/main.js',
      output: {
        sourcemap: true,
        format: 'iife',
        name: 'app',
        file: 'public/build/bundle.js',
      },
      plugins: [
        // Other plugins
     
        // Configures the replace plugin to allow GraphQL Queries to work properly
        replace({
          'process.env.NODE_ENV': JSON.stringify('development'),
        }),
      ]
    };

With Angular, the most common issue is the placement of the `mockServiceWorker.js` file. Use this [example](https://github.com/mswjs/examples/tree/main/examples/with-angular) as a point of reference.

## 

Can I use other GraphQL providers with Storybook's MSW addon?

Yes, check the [addon's examples](https://github.com/mswjs/msw-storybook-addon/tree/main/packages/docs/src/demos) to learn how to integrate different providers.

## 

Can I mock GraphQL mutations with Storybook's MSW addon?

No, currently, the MSW addon only has support for GraphQL queries. If you're interested in including this feature, open an issue in the [MSW addon repository](https://github.com/mswjs/msw-storybook-addon) and follow up with the maintainer.

## 

Why are my stories not showing up correctly when using certain characters?

Storybook allows you to use most characters while naming your stories. Still, specific characters (e.g., `#`) can lead to issues when Storybook generates the internal identifier for the story, leading to collisions and incorrectly outputting the correct story. We recommend using such characters sparsely.

## 

Why is Storybook's source loader returning undefined with curried functions?

This is a known issue with Storybook. If you're interested in getting it fixed, open an issue with a [working reproduction](./contribute/how-to-reproduce) so that it can be triaged and fixed in future releases.

## 

Why are my args no longer displaying the default values?

Before version 6.3, unset args were set to the `argTypes.defaultValue` if specified or inferred from the component's properties (e.g., React's prop types, Angular inputs, Vue props). Starting with version 6.3, Storybook no longer infers default values but instead defines the arg's value as `undefined` when unset, allowing the framework to supply its default value.

If you are using `argTypes.defaultValue` to fix the above, you no longer need to, and you can safely remove it from your stories.

Additionally, suppose you were using `argTypes.defaultValue` or relying on inference to set a default value for an arg. In that case, you should define the arg's value at the component level instead:

MyComponent.stories.js
    
    
    export default {
      component: MyComponent,
      args: {
        //👇 Defining the arg's value at the component level.
        text: 'Something',
      },
    };

For Storybook's Docs, you can manually configure the displayed value by configuring the `table.defaultValue` setting:

MyComponent.stories.js
    
    
    export default {
      component: MyComponent,
      argTypes: {
        //👇 Defining the arg's display value in docs.
        text: {
          table: { defaultValue: { summary: 'SomeType<T>' } },
        },
      },
    };

## 

Why isn't Storybook's test runner working?

There's an issue with Storybook's test runner and the latest version of Jest (i.e., version 28), which prevents it from running effectively. As a workaround, you can downgrade Jest to the previous stable version (i.e., version 27), and you'll be able to run it. See the following [issue](https://github.com/storybookjs/test-runner/issues/99) for more information.

## 

How does Storybook handle environment variables?

Storybook has built-in support for [environment variables](./configure/environment-variables). By default, environment variables are only available in Node.js code and are not available in the browser as some variables should be kept secret (e.g., API keys) and **not** exposed to anyone visiting the published Storybook.

To expose a variable, you must preface its name with `STORYBOOK_`. So `STORYBOOK_API_URL` will be available in browser code but `API_KEY` will not. Additionally you can also customize which variables are exposed by setting the [`env`](./configure/environment-variables#using-storybook-configuration) field in the `.storybook/main.js` file.

Variables are set when JavaScript is compiled so when the development server is started or you build your Storybook. Environment variable files should not be committed to Git as they often contain secrets which are not safe to add to Git. Instead, add `.env.*` to your `.gitignore` file and set up the environment variables manually on your hosting provider (e.g., [GitHub](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository)).

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/faq.mdx)