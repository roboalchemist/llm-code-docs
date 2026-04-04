# Storybook Documentation
# Source: https://storybook.js.org/docs/essentials
# Page: /docs/essentials

# Essentials

Storybook essentials is a set of tools that help you build, test, and document your components within Storybook. It includes the following:

  * [Actions](./essentials/actions)
  * [Backgrounds](./essentials/backgrounds)
  * [Controls](./essentials/controls)
  * [Highlight](./essentials/highlight)
  * [Measure & outline](./essentials/measure-and-outline)
  * [Toolbars & globals](./essentials/toolbars-and-globals)
  * [Viewport](./essentials/viewport)



### 

Configuration

Essentials is "zero-config”. It comes with a recommended configuration out of the box.

Many of the features above can be configured via [parameters](./writing-stories/parameters). See each feature's documentation (linked above) for more details.

### 

Disabling features

If you need to disable any of the essential features, you can do it by changing your [`.storybook/main.js|ts`](./configure/index#configure-your-storybook-project) file.

For example, if you wanted to disable the [backgrounds feature](./essentials/backgrounds), you would apply the following change to your Storybook configuration:

CSF 3CSF Next 🧪

.storybook/main.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
     
    const config: StorybookConfig = {
      framework: '@storybook/your-framework',
      stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
      features: {
        backgrounds: false, // 👈 disable the backgrounds feature
      },
    };
     
    export default config;

💡

You can use the following keys for each individual feature: `actions`, `backgrounds`, `controls`, `highlight`, `measure`, `outline`, `toolbars`, and `viewport`.

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/essentials/index.mdx)