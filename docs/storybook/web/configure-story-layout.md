# Storybook Documentation
# Source: https://storybook.js.org/docs/configure/story-layout
# Page: /docs/configure/story-layout

# Story layout

ReactVueAngularWeb ComponentsMore

The `layout` [parameter](../writing-stories/parameters) allows you to configure how stories are positioned in Storybook's Canvas tab.

## 

Global layout

You can add the parameter to your [`./storybook/preview.js`](./index#configure-story-rendering), like so:

CSF 3CSF Next 🧪

.storybook/preview.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Preview } from '@storybook/your-framework';
     
    const preview: Preview = {
      parameters: {
        layout: 'centered',
      },
    };
     
    export default preview;

![Layout params centered story](/docs-assets/10.1/configure/layout-params-story-centered.png)

In the example above, Storybook will center all stories in the UI. `layout` accepts these options:

  * `centered`: center the component horizontally and vertically in the Canvas
  * `fullscreen`: allow the component to expand to the full width and height of the Canvas
  * `padded`: _(default)_ Add extra padding around the component



## 

Component layout

You can also set it at a component level like so:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Meta } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
      // Sets the layout parameter component wide.
      parameters: {
        layout: 'centered',
      },
    } satisfies Meta<typeof Button>;
     
    export default meta;

## 

Story layout

Or even apply it to specific stories like so:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const WithLayout: Story = {
      parameters: {
        layout: 'centered',
      },
    };

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/configure/story-layout.mdx)