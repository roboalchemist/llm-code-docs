# Storybook Documentation
# Source: https://storybook.js.org/docs/writing-docs/code-panel
# Page: /docs/writing-docs/code-panel

# Code panel

ReactVueAngularWeb ComponentsMore

ℹ️

Code Panel is a replacement for the [Storysource addon](https://storybook.js.org/addons/@storybook/addon-storysource), which was [discontinued in Storybook 9](https://github.com/storybookjs/storybook/blob/next/MIGRATION.md#storysource-addon-removed).

The Code panel renders a story’s source code when viewing that story in the canvas. Any [args](../writing-stories/args) defined in the story are replaced with their values in the output.

![Code panel showing story's source code](/docs-assets/10.1/writing-docs/code-panel.png)

## 

Usage

To enable the Code panel, set `parameters.docs.codePanel` to `true`. For most projects, this is best done in the `.storybook/preview.js|ts` file, to apply to all stories.

CSF 3CSF Next 🧪

.storybook/preview.ts

Typescript
    
    
    // Replace your-framework with the framework you are using (e.g., react-vite, vue3-vite, angular, etc.)
    import type { Preview } from '@storybook/your-framework';
     
    const preview: Preview = {
      parameters: {
        docs: {
          codePanel: true,
        },
      },
    };
     
    export default preview;

You can also enable it at the component or story level:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    import type { Meta, StoryObj } from '@storybook/react-vite';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
      parameters: {
        docs: {
          // 👇 Enable Code panel for all stories in this file
          codePanel: true,
        },
      },
    } satisfies Meta<typeof Button>;
    export default meta;
     
    type Story = StoryObj<typeof meta>;
     
    // 👇 This story will display the Code panel
    export const Primary: Story = {
      args: {
        children: 'Button',
      },
    };
     
    export const Secondary: Story = {
      args: {
        children: 'Button',
        variant: 'secondary',
      },
      parameters: {
        docs: {
          // 👇 Disable Code panel for this specific story
          codePanel: false,
        },
      },
    };

## 

Configuration

Code panel renders the same snippet as the [Source docs block](../api/doc-blocks/doc-block-source), which is also used in [Autodocs](./autodocs) pages. The snippet is customizable and reuses the [Source configuration parameters](../api/doc-blocks/doc-block-source#source).

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/writing-docs/code-panel.mdx)