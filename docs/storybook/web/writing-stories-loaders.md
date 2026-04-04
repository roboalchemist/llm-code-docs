# Storybook Documentation
# Source: https://storybook.js.org/docs/writing-stories/loaders
# Page: /docs/writing-stories/loaders

# Loaders

ReactVueAngularWeb ComponentsMore

Loaders are asynchronous functions that load data for a story and its [decorators](./decorators). A story's loaders run before the story renders, and the loaded data injected into the story via its render context.

Loaders can be used to load any asset, lazy load components, or fetch data from a remote API. This feature was designed as a performance optimization to handle large story imports. However, [args](./args) is the recommended way to manage story data. We're building up an ecosystem of tools and techniques around Args that might not be compatible with loaded data.

They are an advanced feature (i.e., escape hatch), and we only recommend using them if you have a specific need that other means can't fulfill.

## 

Fetching API data

Stories are isolated component examples that render internal data defined as part of the story or alongside the story as [args](./args).

Loaders are helpful when you need to load story data externally (e.g., from a remote API). Consider the following example that fetches a todo item to display in a todo list:

CSF 3CSF Next 🧪

MyComponent.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { TodoItem } from './TodoItem';
     
    /*
     *👇 Render functions are a framework specific feature to allow you control on how the component renders.
     * See https://storybook.js.org/docs/api/csf
     * to learn how to use render functions.
     */
    const meta = {
      component: TodoItem,
      render: (args, { loaded: { todo } }) => <TodoItem {...args} {...todo} />,
    } satisfies Meta<typeof TodoItem>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Primary: Story = {
      loaders: [
        async () => ({
          todo: await (await fetch('https://jsonplaceholder.typicode.com/todos/1')).json(),
        }),
      ],
    };

The response obtained from the remote API call is combined into a `loaded` field on the story context, which is the second argument to a story function. For example, in React, the story's args were spread first to prioritize them over the static data provided by the loader. With other frameworks (e.g., Angular), you can write your stories as you'd usually do.

## 

Global loaders

We can also set a loader for **all stories** via the `loaders` export of your [`.storybook/preview.js`](../configure/index#configure-story-rendering) file (this is the file where you configure all stories):

CSF 3CSF Next 🧪

.storybook/preview.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Preview } from '@storybook/your-framework';
     
    const preview: Preview = {
      loaders: [
        async () => ({
          currentUser: await (await fetch('https://jsonplaceholder.typicode.com/users/1')).json(),
        }),
      ],
    };
     
    export default preview;

In this example, we load a "current user" available as `loaded.currentUser` for all stories.

## 

Loader inheritance

Like [parameters](./parameters), loaders can be defined globally, at the component level, and for a single story (as we’ve seen).

All loaders, defined at all levels that apply to a story, run before the story renders in Storybook's canvas.

  * All loaders run in parallel
  * All results are the `loaded` field in the story context
  * If there are keys that overlap, "later" loaders take precedence (from lowest to highest):
    * Global loaders, in the order they are defined
    * Component loaders, in the order they are defined
    * Story loaders, in the order they are defined



Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/writing-stories/loaders.mdx)