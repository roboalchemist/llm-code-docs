# Storybook Documentation
# Source: https://storybook.js.org/docs/api/parameters
# Page: /docs/api/parameters

# Parameters

ReactVueAngularWeb ComponentsMore

Parameters are static metadata used to configure your [stories](../get-started/whats-a-story) and [addons](../addons) in Storybook. They are specified at the story, meta (component), project (global) levels.

## 

Story parameters

Parameters specified at the story level apply to that story only. They are defined in the `parameters` property of the story (named export):

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
     
    export const Primary: Story = {
      // 👇 Story-level parameters
      parameters: {
        backgrounds: {
          options: {
            red: { name: 'Red', value: '#f00' },
            green: { name: 'Green', value: '#0f0' },
            blue: { name: 'Blue', value: '#00f' },
          },
        },
      },
    };

ℹ️

Parameters specified at the story level will override those specified at the project level and meta (component) level.

## 

Meta parameters

Parameter's specified in a [CSF](../writing-stories/index#component-story-format-csf) file's meta configuration apply to all stories in that file. They are defined in the `parameters` property of the `meta` (default export):

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

ℹ️

Parameters specified at the meta (component) level will override those specified at the project level.

## 

Project parameters

Parameters specified at the project (global) level apply to **all stories** in your Storybook. They are defined in the `parameters` property of the default export in your `.storybook/preview.js|ts` file:

CSF 3CSF Next 🧪

.storybook/preview.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Preview } from '@storybook/your-framework';
     
    const preview: Preview = {
      parameters: {
        backgrounds: {
          options: {
            light: { name: 'Light', value: '#fff' },
            dark: { name: 'Dark', value: '#333' },
          },
        },
      },
    };
     
    export default preview;

## 

Available parameters

Storybook only accepts a few parameters directly.

### 

`layout`

Type: `'centered' | 'fullscreen' | 'padded'`

Default: `'padded'`

Specifies how the canvas should [lay out the story](../configure/story-layout).

  * **centered** : Center the story within the canvas
  * **padded** : (default) Add padding to the story
  * **fullscreen** : Show the story as-is, without padding



### 

`options`

Type:
    
    
    {
      storySort?: StorySortConfig | StorySortFn;
    }

⚠️

The `options` parameter can _only_ be applied at the project level.

#### 

`options.storySort`

Type: `StorySortConfig | StorySortFn`
    
    
    type StorySortConfig = {
      includeNames?: boolean;
      locales?: string;
      method?: 'alphabetical' | 'alphabetical-by-kind' | 'custom';
      order?: string[];
    };
     
    type Story = {
      id: string;
      importPath: string;
      name: string;
      title: string;
    };
     
    type StorySortFn = (a: Story, b: Story) => number;

Specifies the order in which stories are displayed in the Storybook UI.

When specifying a configuration object, the following options are available:

  * **includeNames** : Whether to include the story name in the sorting algorithm. Defaults to `false`.
  * **locales** : The locale to use when sorting stories. Defaults to your system locale.
  * **method** : The sorting method to use. Defaults to `alphabetical`.
    * **alphabetical** : Sort stories alphabetically by name.
    * **alphabetical-by-kind** : Sort stories alphabetically by kind, then by name.
    * **custom** : Use a custom sorting function.
  * **order** : Stories in the specified order will be displayed first, in the order specified. All other stories will be displayed after, in alphabetical order. The order array can accept a nested array to sort 2nd-level story kinds, e.g. `['Intro', 'Pages', ['Home', 'Login', 'Admin'], 'Components']`.



When specifying a custom sorting function, the function behaves like a typical JavaScript sorting function. It accepts two stories to compare and returns a number. For example:
    
    
    (a, b) => (a.id === b.id ? 0 : a.id.localeCompare(b.id, undefined, { numeric: true }));

See [the guide](../writing-stories/naming-components-and-hierarchy#sorting-stories) for usage examples.

### 

`test`

Type:
    
    
    {
      clearMocks?: boolean;
      mockReset?: boolean;
      restoreMocks?: boolean;
      dangerouslyIgnoreUnhandledErrors?: boolean;
    }

#### 

`clearMocks`

Type: `boolean`

Default: `false`

[Similar to Vitest](https://vitest.dev/config/#clearmocks), it will call `.mockClear()` on all spies created with `fn()` from `storybook/test` when a story unmounts. This will clear mock history, but not reset its implementation to the default one.

#### 

`mockReset`

Type: `boolean`

Default: `false`

[Similar to Vitest](https://vitest.dev/config/#mockreset), it will call `.mockReset()` on all spies created with `fn()` from `storybook/test` when a story unmounts. This will clear mock history and reset its implementation to an empty function (will return `undefined`).

#### 

`restoreMocks`

Type: `boolean`

Default: `true`

[Similar to Vitest](https://vitest.dev/config/#restoremocks), it will call `.restoreMocks()` on all spies created with `fn()` from `storybook/test` when a story unmounts. This will clear mock history and reset its implementation to the original one.

#### 

`dangerouslyIgnoreUnhandledErrors`

Type: `boolean`

Default: `false`

Unhandled errors might cause false positive assertions. Setting this to `true` will prevent the [play function](../writing-stories/play-function) from failing and showing a warning when unhandled errors are thrown during execution.

* * *

### 

Essentials

All other parameters are contributed by features. The [essential feature's](../essentials) parameters are documented on their individual pages:

  * [Actions](../essentials/actions#parameters)
  * [Backgrounds](../essentials/backgrounds#parameters)
  * [Controls](../essentials/controls#parameters)
  * [Highlight](../essentials/highlight#parameters)
  * [Measure & Outline](../essentials/measure-and-outline#parameters)
  * [Viewport](../essentials/viewport#parameters)



## 

Parameter inheritance

No matter where they're specified, parameters are ultimately applied to a single story. Parameters specified at the project (global) level are applied to every story in that project. Those specified at the meta (component) level are applied to every story associated with that meta. And parameters specified for a story only apply to that story.

When specifying parameters, they are merged together in order of increasing specificity:

  1. Project (global) parameters
  2. Meta (component) parameters
  3. Story parameters



ℹ️

Parameters are **merged** , so objects are deep-merged, but arrays and other properties are overwritten.

In other words, the following specifications of parameters:

.storybook/preview.js|ts
    
    
    const preview = {
      // 👇 Project-level parameters
      parameters: {
        layout: 'centered',
        demo: {
          demoProperty: 'a',
          demoArray: [1, 2],
        },
      },
      // ...
    };
    export default preview;

Dialog.stories.js|ts
    
    
    const meta = {
      component: Dialog,
      // 👇 Meta-level parameters
      parameters: {
        layout: 'fullscreen',
        demo: {
          demoProperty: 'b',
          anotherDemoProperty: 'b',
        },
      },
    };
    export default meta;
     
    // (no additional parameters specified)
    export const Basic = {};
     
    export const LargeScreen = {
      // 👇 Story-level parameters
      parameters: {
        layout: 'padded',
        demo: {
          demoArray: [3, 4],
        },
      },
    };

Will result in the following parameter values applied to each story:
    
    
    // Applied story parameters
     
    // For the Basic story:
    {
      layout: 'fullscreen',
      demo: {
        demoProperty: 'b',
        anotherDemoProperty: 'b',
        demoArray: [1, 2],
      },
    }
     
    // For the LargeScreen story:
    {
      layout: 'padded',
      demo: {
        demoProperty: 'b',
        anotherDemoProperty: 'b',
        demoArray: [3, 4],
      },
    }

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/api/parameters.mdx)