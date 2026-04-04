# Storybook Documentation
# Source: https://storybook.js.org/docs/api/csf
# Page: /docs/api/csf

# Component Story Format (CSF)

ReactVueAngularWeb ComponentsMore

CSF 3[CSF Next (Preview)](./csf/csf-next)

Component Story Format (CSF) is the recommended way to [write stories](./../writing-stories). It's an open standard based on ES6 modules that is portable beyond Storybook.

In CSF, stories and component metadata are defined as ES Modules. Every component story file consists of a required [default export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#Using_the_default_export) and one or more [named exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export).

## 

Default export

The default export defines metadata about your component, including the `component` itself, its `title` (where it will show up in the [navigation UI story hierarchy](./../writing-stories/naming-components-and-hierarchy#sorting-stories)), [decorators](./../writing-stories/decorators), and [parameters](./../writing-stories/parameters).

The `component` field is required and used by addons for automatic prop table generation and display of other component metadata. The `title` field is optional and should be unique (i.e., not re-used across files).

CSF 3CSF Next 🧪

MyComponent.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Meta } from '@storybook/your-framework';
     
    import { MyComponent } from './MyComponent';
     
    const meta = {
      /* 👇 The title prop is optional.
       * See https://storybook.js.org/docs/configure/#configure-story-loading
       * to learn how to generate automatic titles
       */
      title: 'Path/To/MyComponent',
      component: MyComponent,
      decorators: [
        /* ... */
      ],
      parameters: {
        /* ... */
      },
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;

For more examples, see [writing stories](./../writing-stories).

## 

Named story exports

With CSF, every named export in the file represents a story object by default.

CSF 3CSF Next 🧪

MyComponent.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { MyComponent } from './MyComponent';
     
    const meta = {
      component: MyComponent,
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Basic: Story = {};
     
    export const WithProp: Story = {
      render: () => <MyComponent prop="value" />,
    };

The exported identifiers will be converted to "start case" using Lodash's [startCase](https://lodash.com/docs/#startCase) function. For example:

Identifier| Transformation  
---|---  
name| Name  
someName| Some Name  
someNAME| Some NAME  
some_custom_NAME| Some Custom NAME  
someName1234| Some Name 1 2 3 4  
  
We recommend that all export names to start with a capital letter.

Story objects can be annotated with a few different fields to define story-level [decorators](./../writing-stories/decorators) and [parameters](./../writing-stories/parameters), and also to define the `name` of the story.

Storybook's `name` configuration element is helpful in specific circumstances. Common use cases are names with special characters or Javascript restricted words. If not specified, Storybook defaults to the named export.

CSF 3CSF Next 🧪

MyComponent.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { MyComponent } from './MyComponent';
     
    const meta = {
      component: MyComponent,
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Simple: Story = {
      name: 'So simple!',
      // ...
    };

## 

Args story inputs

Starting in SB 6.0, stories accept named inputs called Args. Args are dynamic data that are provided (and possibly updated by) Storybook and its addons.

Consider Storybook’s ["Button" example](./../writing-stories/index#defining-stories) of a text button that logs its click events:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { action } from 'storybook/actions';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Basic: Story = {
      render: () => <Button label="Hello" onClick={action('clicked')} />,
    };

Now consider the same example, re-written with args:

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { action } from 'storybook/actions';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Text = {
      args: {
        label: 'Hello',
        onClick: action('clicked'),
      },
      render: ({ label, onClick }) => <Button label={label} onClick={onClick} />,
    };

Or even more simply:

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
     
    export const Text: Story = {
      args: {},
    };

Not only are these versions shorter and more accessible to write than their no-args counterparts, but they are also more portable since the code doesn't depend on the actions feature specifically.

For more information on setting up [Docs](./../writing-docs) and [Actions](./../essentials/actions), see their respective documentation.

## 

Play function

Storybook's `play` functions are small snippets of code executed when the story renders in the UI. They are convenient helper methods to help you test use cases that otherwise weren't possible or required user intervention.

A good use case for the `play` function is a form component. With previous Storybook versions, you'd write your set of stories and had to interact with the component to validate it. With Storybook's play functions, you could write the following story:

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

When the story renders in the UI, Storybook executes each step defined in the `play` function and runs the assertions without the need for user interaction.

## 

Custom render functions

Starting in Storybook 6.4, you can write your stories as JavaScript objects, reducing the boilerplate code you need to generate to test your components, thus improving functionality and usability. `Render` functions are helpful methods to give you additional control over how the story renders. For example, if you were writing a story as an object and you wanted to specify how your component should render, you could write the following:

CSF 3CSF Next 🧪

MyComponent.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Layout } from './Layout';
    import { MyComponent } from './MyComponent';
     
    const meta = {
      component: MyComponent,
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    // This story uses a render function to fully control how the component renders.
    export const Example: Story = {
      render: () => (
        <Layout>
          <header>
            <h1>Example</h1>
          </header>
          <article>
            <MyComponent />
          </article>
        </Layout>
      ),
    };

When Storybook loads this story, it will detect the existence of a `render` function and adjust the component rendering accordingly based on what's defined.

## 

Storybook export vs. name handling

Storybook handles named exports and the `name` option slightly differently. When should you use one vs. the other?

Storybook will always use the named export to determine the story ID and URL.

If you specify the `name` option, it will be used as the story display name in the UI. Otherwise, it defaults to the named export, processed through Storybook's `storyNameFromExport` and `lodash.startCase` functions.

MyComponent-test.js
    
    
    it('should format CSF exports with sensible defaults', () => {
      const testCases = {
        name: 'Name',
        someName: 'Some Name',
        someNAME: 'Some NAME',
        some_custom_NAME: 'Some Custom NAME',
        someName1234: 'Some Name 1234',
        someName1_2_3_4: 'Some Name 1 2 3 4',
      };
      Object.entries(testCases).forEach(([key, val]) => {
        expect(storyNameFromExport(key)).toBe(val);
      });
    });

When you want to change the name of your story, rename the CSF export. It will change the name of the story and also change the story's ID and URL.

It would be best if you used the `name` configuration element in the following cases:

  1. You want the name to show up in the Storybook UI in a way that's not possible with a named export, e.g., reserved keywords like "default", special characters like emoji, spacing/capitalization other than what's provided by `storyNameFromExport`.
  2. You want to preserve the Story ID independently from changing how it's displayed. Having stable Story IDs is helpful for integration with third-party tools.



## 

Non-story exports

In some cases, you may want to export a mixture of stories and non-stories (e.g., mocked data).

You can use the optional configuration fields `includeStories` and `excludeStories` in the default export to make this possible. You can define them as an array of strings or regular expressions.

Consider the following story file:

CSF 3CSF Next 🧪

MyComponent.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { MyComponent } from './MyComponent';
     
    import someData from './data.json';
     
    const meta = {
      component: MyComponent,
      includeStories: ['SimpleStory', 'ComplexStory'], // 👈 Storybook loads these stories
      excludeStories: /.*Data$/, // 👈 Storybook ignores anything that contains Data
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const simpleData = { foo: 1, bar: 'baz' };
    export const complexData = { foo: 1, foobar: { bar: 'baz', baz: someData } };
     
    export const SimpleStory: Story = {
      args: {
        data: simpleData,
      },
    };
     
    export const ComplexStory: Story = {
      args: {
        data: complexData,
      },
    };

When this file renders in Storybook, it treats `ComplexStory` and `SimpleStory` as stories and ignores the `data` named exports.

For this particular example, you could achieve the same result in different ways, depending on what's convenient:

  * `includeStories: /^[A-Z]/`
  * `includeStories: /.*Story$/`
  * `includeStories: ['SimpleStory', 'ComplexStory']`
  * `excludeStories: /^[a-z]/`
  * `excludeStories: /.*Data$/`
  * `excludeStories: ['simpleData', 'complexData']`



The first option is the recommended solution if you follow the best practice of starting story exports with an uppercase letter (i.e., use UpperCamelCase).

## 

Upgrading from CSF 2 to CSF 3

ℹ️

Storybook provides a codemod to help you upgrade from CSF 2 to CSF 3. You can run it with the following command:

npm
    
    
    npx storybook migrate csf-2-to-3 --glob="**/*.stories.tsx" --parser=tsx

In CSF 2, the named exports are always functions that instantiate a component, and those functions can be annotated with configuration options. For example:

CSF 2 - Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { ComponentStory, ComponentMeta } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    export default {
      title: 'Button',
      component: Button,
    } as ComponentMeta<typeof Button>;
     
    export const Primary: ComponentStory<typeof Button> = (args) => <Button {...args} />;
    Primary.args = { primary: true };

This declares a Primary story for a Button that renders itself by spreading `{ primary: true }` into the component. The `default.title` metadata says where to place the story in a navigation hierarchy.

Here's the CSF 3 equivalent:

CSF 3 - Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      component: Button,
    } satisfies Meta<typeof Button>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const Primary: Story = { args: { primary: true } };

Let's go through the changes individually to understand what's going on.

### 

Spreadable story objects

In CSF 3, the named exports are **objects** , not functions. This allows us to reuse stories more efficiently with the JS spread operator.

Consider the following addition to the intro example, which creates a `PrimaryOnDark` story that renders against a dark background:

Here's the CSF 2 implementation:

CSF 2 - Button.stories.js|jsx|ts|tsx
    
    
    export const PrimaryOnDark = Primary.bind({});
    PrimaryOnDark.args = Primary.args;
    PrimaryOnDark.parameters = { background: { default: 'dark' } };

`Primary.bind({})` copies the story function, but it doesn't copy the annotations hanging off the function, so we must add `PrimaryOnDark.args = Primary.args` to inherit the args.

In CSF 3, we can spread the `Primary` object to carry over all its annotations:

CSF 3 - Button.stories.ts|tsx

Typescript
    
    
    export const PrimaryOnDark: Story = {
      ...Primary,
      parameters: { background: { default: 'dark' } },
    };

Learn more about named story exports.

### 

Default render functions

In CSF 3, you specify how a story renders through a `render` function. We can rewrite a CSF 2 example to CSF 3 through the following steps.

Let's start with a simple CSF 2 story function:

CSF 2 - Button.stories.ts|tsx

Typescript
    
    
    // Other imports and story implementation
    export const Default: ComponentStory<typeof Button> = (args) => <Button {...args} />;

Now, let's rewrite it as a story object in CSF 3 with an explicit `render` function that tells the story how to render itself. Like CSF 2, this gives us full control of how we render a component or even a collection of components.

CSF 3 - Button.stories.ts|tsx

Typescript
    
    
    // Other imports and story implementation
    export const Default: Story = {
      render: (args) => <Button {...args} />,
    };

Learn more about render functions.

But in CSF 2, a lot of story functions are identical: take the component specified in the default export and spread args into it. What's interesting about these stories is not the function, but the args passed into the function.

CSF 3 provides default render functions for each renderer. If all you're doing is spreading args into your component—which is the most common case—you don't need to specify any `render` function at all:

CSF 3 - Button.stories.js|jsx|ts|tsx
    
    
    export const Default = {};

For more information, see the section on custom render functions.

### 

Generate titles automatically

Finally, CSF 3 can automatically generate titles.

CSF 2 - Button.stories.js|jsx|ts|tsx
    
    
    export default {
      title: 'components/Button',
      component: Button,
    };

CSF 3 - Button.stories.js|jsx|ts|tsx
    
    
    export default { component: Button };

You can still specify a title like in CSF 2, but if you don't specify one, it can be inferred from the story's path on disk. For more information, see the section on [configuring story loading](./../configure/index#configure-story-loading).

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/api/csf/index.mdx)