# Storybook Documentation
# Source: https://storybook.js.org/docs/writing-stories
# Page: /docs/writing-stories

# How to write stories

ReactVueAngularWeb ComponentsMore

A story captures the rendered state of a UI component. It's an object with annotations that describe the component's behavior and appearance given a set of arguments.

Storybook uses the generic term arguments (args for short) when talking about React’s `props`, Vue’s `props`, Angular’s `@Input`, and other similar concepts.

## 

Where to put stories

A component’s stories are defined in a story file that lives alongside the component file. The story file is for development-only, and it won't be included in your production bundle. In your filesystem, it looks something like this:
    
    
    components/
    ├─ Button/
    │  ├─ Button.js | ts | jsx | tsx | vue | svelte
    │  ├─ Button.stories.js | ts | jsx | tsx | svelte
    

## 

Component Story Format

We define stories according to the [Component Story Format](./api/csf) (CSF), an ES6 module-based standard that is easy to write and portable between tools.

The key ingredients are the [default export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#Using_the_default_export) that describes the component, and [named exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#Using_named_exports) that describe the stories.

### 

Default export

The _default_ export metadata controls how Storybook lists your stories and provides information used by addons. For example, here’s the default export for a story file `Button.stories.js|ts`:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;

ℹ️

Starting with Storybook version 7.0, story titles are analyzed statically as part of the build process. The _default_ export must contain a `title` property that can be read statically or a `component` property from which an automatic title can be computed. Using the `id` property to customize your story URL must also be statically readable.

### 

Defining stories

Use the _named_ exports of a CSF file to define your component’s stories. We recommend you use UpperCamelCase for your story exports. Here’s how to render `Button` in the “primary” state and export a story called `Primary`.

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Primary: Story = {
      args: {
        primary: true,
        label: 'Button',
      },
    };

#### 

Custom rendering

By default, stories will render the component defined in the meta (default export), with the `args` passed to it. If you need to render something else, you can provide a function to the `render` property that returns the desired output.

For example, if you want to render a `Button` inside an `Alert`, you can define a custom render function like this:

CSF 3CSF Next 🧪

Button.stories.tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Alert } from './Alert';
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
    export default meta;
     
    type Story = StoryObj<typeof meta>;
     
    export const PrimaryInAlert: Story = {
      args: {
        primary: true,
        label: 'Button',
      },
      render: (args) => (
        <Alert>
          Alert text
          <Button {...args} />
        </Alert>
      ),
    };

ℹ️

Note how the `render` function spreads `args` onto the Button component. This ensures that features like [Controls](./essentials/controls) will work as expected, allowing you to dynamically change the Button's properties in the Storybook UI.

You can re-use the same render function across stories by applying it at the meta level:

CSF 3CSF Next 🧪

Button.stories.tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Alert } from './Alert';
    import { Button } from './Button';
     
    const meta = {
      component: Button,
      render: (args) => (
        <Alert>
          Alert text
          <Button {...args} />
        </Alert>
      ),
    } satisfies Meta<typeof Button>;
    export default meta;
     
    type Story = StoryObj<typeof meta>;
     
    export const DefaultInAlert: Story = {
      args: {
        label: 'Button',
      },
    };
     
    export const PrimaryInAlert: Story = {
      args: {
        primary: true,
        label: 'Button',
      },
    };

Whatever you define at the meta level can be overridden at the story level, so you can still customize the rendering of individual stories if needed.

Finally, `render` functions receive a second `context` argument, which contains all other details for the story, including [`parameters`](./writing-stories/parameters), [`globals`](./essentials/toolbars-and-globals), and more.

#### 

Working with React Hooks

[React Hooks](https://react.dev/reference/react) are convenient helper methods to create components using a more streamlined approach. You can use them while creating your component's stories if you need them, although you should treat them as an advanced use case. We **recommend** [args](./writing-stories/args) as much as possible when writing your own stories. As an example, here’s a story that uses React Hooks to change the button's state:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    import React, { useState } from 'react';
     
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    const ButtonWithHooks = () => {
      // Sets the hooks for both the label and primary props
      const [value, setValue] = useState('Secondary');
      const [isPrimary, setIsPrimary] = useState(false);
     
      // Sets a click handler to change the label's value
      const handleOnChange = () => {
        if (!isPrimary) {
          setIsPrimary(true);
          setValue('Primary');
        }
      };
      return <Button primary={isPrimary} onClick={handleOnChange} label={value} />;
    };
     
    export const Primary = {
      render: () => <ButtonWithHooks />,
    } satisfies Story;

### 

Rename stories

By default, Storybook uses the name of the story export as the basis for the story name. However, you can customize the name of your story by adding a `name` property to the story object. This is useful when you want to provide a more descriptive or user-friendly name for your story.

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Primary: Story = {
      // 👇 Rename this story
      name: 'I am the primary',
      args: {
        label: 'Button',
        primary: true,
      },
    };

Your story will now be shown in the sidebar with the given text.

## 

How to write stories

A story is an object that describes how to render a component. You can have multiple stories per component, and those stories can build upon one another. For example, we can add Secondary and Tertiary stories based on our Primary story from above.

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Primary: Story = {
      args: {
        backgroundColor: '#ff0',
        label: 'Button',
      },
    };
     
    export const Secondary: Story = {
      args: {
        ...Primary.args,
        label: '😄👍😍💯',
      },
    };
     
    export const Tertiary: Story = {
      args: {
        ...Primary.args,
        label: '📚📕📈🤓',
      },
    };

What’s more, you can import `args` to reuse when writing stories for other components, and it's helpful when you’re building composite components. For example, if we make a `ButtonGroup` story, we might remix two stories from its child component `Button`.

CSF 3CSF Next 🧪

ButtonGroup.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { ButtonGroup } from '../ButtonGroup';
     
    //👇 Imports the Button stories
    import * as ButtonStories from './Button.stories';
     
    const meta = {
      component: ButtonGroup,
    } satisfies Meta<typeof ButtonGroup>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Pair: Story = {
      args: {
        buttons: [{ ...ButtonStories.Primary.args }, { ...ButtonStories.Secondary.args }],
        orientation: 'horizontal',
      },
    };

When Button’s signature changes, you only need to change Button’s stories to reflect the new schema, and ButtonGroup’s stories will automatically be updated. This pattern allows you to reuse your data definitions across the component hierarchy, making your stories more maintainable.

That’s not all! Each of the args from the story function are live editable using Storybook’s [Controls](./essentials/controls) panel. It means your team can dynamically change components in Storybook to stress test and find edge cases.

You can also use the Controls panel to edit or save a new story after adjusting its control values.

Addons can enhance args. For instance, [Actions](./essentials/actions) auto-detects which args are callbacks and appends a logging function to them. That way, interactions (like clicks) get logged in the actions panel.

### 

Using the play function

Storybook's `play` function is a convenient helper methods to test component scenarios that otherwise require user intervention. They're small code snippets that execute once your story renders. For example, suppose you wanted to validate a form component, you could write the following story using the `play` function to check how the component responds when filling in the inputs with information:

CSF 3CSF Next 🧪

LoginForm.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { expect } from 'storybook/test';
     
    import { LoginForm } from './LoginForm';
     
    const meta = {
      component: LoginForm,
    } satisfies Meta<typeof LoginForm>;
    export default meta;
     
    type Story = StoryObj<typeof meta>;
     
    export const EmptyForm: Story = {};
     
    export const FilledForm: Story = {
      play: async ({ canvas, userEvent }) => {
        // 👇 Simulate interactions with the component
        await userEvent.type(canvas.getByTestId('email'), 'email@provider.com');
     
        await userEvent.type(canvas.getByTestId('password'), 'a-random-password');
     
        // See https://storybook.js.org/docs/essentials/actions#automatically-matching-args to learn how to setup logging in the Actions panel
        await userEvent.click(canvas.getByRole('button'));
     
        // 👇 Assert DOM structure
        await expect(
          canvas.getByText(
            'Everything is perfect. Your account is ready and we should probably get you started!',
          ),
        ).toBeInTheDocument();
      },
    };

You can interact with and debug your story's play function in the [interactions panel](./writing-tests/interaction-testing#debugging-interaction-tests).

### 

Using parameters

Parameters are Storybook’s method of defining static metadata for stories. A story’s parameters can be used to provide configuration to various addons at the level of a story or group of stories.

For instance, suppose you wanted to test your Button component against a different set of backgrounds than the other components in your app. You might add a component-level `backgrounds` parameter:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Meta } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
      //👇 Creates specific parameters at the component level
      parameters: {
        backgrounds: {
          options: {},
        },
      },
    } satisfies Meta<typeof Button>;
     
    export default meta;

![Parameters background color](/docs-assets/10.1/writing-stories/parameters-background-colors.png)

This parameter would instruct the backgrounds feature to reconfigure itself whenever a Button story is selected. Most features and addons are configured via a parameter-based API and can be influenced at a [global](./writing-stories/parameters#global-parameters), [component](./writing-stories/parameters#component-parameters), and [story](./writing-stories/parameters#story-parameters) level.

### 

Using decorators

Decorators are a mechanism to wrap a component in arbitrary markup when rendering a story. Components are often created with assumptions about ‘where’ they render. Your styles might expect a theme or layout wrapper, or your UI might expect specific context or data providers.

A simple example is adding padding to a component’s stories. Accomplish this using a decorator that wraps the stories in a `div` with padding, like so:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
      decorators: [
        (Story) => (
          <div style={{ margin: '3em' }}>
            {/* 👇 Decorators in Storybook also accept a function. Replace <Story/> with Story() to enable it  */}
            <Story />
          </div>
        ),
      ],
    } satisfies Meta<typeof Button>;
     
    export default meta;

Decorators [can be more complex](./writing-stories/decorators#context-for-mocking) and are often provided by [addons](./configure/user-interface/storybook-addons). You can also configure decorators at the [story](./writing-stories/decorators#story-decorators), [component](./writing-stories/decorators#component-decorators) and [global](./writing-stories/decorators#global-decorators) level.

## 

Stories for two or more components

Sometimes you may have two or more components created to work together. For instance, if you have a parent `List` component, it may require child `ListItem` components.

CSF 3CSF Next 🧪

List.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { List } from './List';
     
    const meta = {
      component: List,
    } satisfies Meta<typeof List>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    // Always an empty list, not super interesting
    export const Empty: Story = {};

In such cases, it makes sense to customize the rendering to output the `List` component with different numbers of `ListItem` children.

CSF 3CSF Next 🧪

List.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { List } from './List';
    import { ListItem } from './ListItem';
     
    const meta = {
      component: List,
    } satisfies Meta<typeof List>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Empty: Story = {};
     
    /*
     *👇 Render functions are a framework specific feature to allow you control on how the component renders.
     * See https://storybook.js.org/docs/api/csf
     * to learn how to use render functions.
     */
    export const OneItem: Story = {
      render: (args) => (
        <List {...args}>
          <ListItem />
        </List>
      ),
    };
     
    export const ManyItems: Story = {
      render: (args) => (
        <List {...args}>
          <ListItem />
          <ListItem />
          <ListItem />
        </List>
      ),
    };

You can also reuse _story data_ from the child `ListItem` in your `List` component. That’s easier to maintain because you don’t have to update it in multiple places.

CSF 3CSF Next 🧪

List.stories.ts|tsx

Typescript
    
    
    import * as React from 'react';
     
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { List } from './List';
    import { ListItem } from './ListItem';
     
    //👇 We're importing the necessary stories from ListItem
    import { Selected, Unselected } from './ListItem.stories';
     
    const meta = {
      component: List,
    } satisfies Meta<typeof List>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const ManyItems: Story = {
      render: (args) => (
        <List {...args}>
          <ListItem {...Selected.args} />
          <ListItem {...Unselected.args} />
          <ListItem {...Unselected.args} />
        </List>
      ),
    };

💡

Note that there are disadvantages in writing stories like this as you cannot take full advantage of the args mechanism and composing args as you build even more complex composite components. For more discussion, see the [multi component stories](./writing-stories/stories-for-multiple-components) workflow documentation.

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/writing-stories/index.mdx)