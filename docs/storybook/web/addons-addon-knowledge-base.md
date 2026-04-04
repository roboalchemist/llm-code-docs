# Storybook Documentation
# Source: https://storybook.js.org/docs/addons/addon-knowledge-base
# Page: /docs/addons/addon-knowledge-base

# Addon knowledge base

ReactVueAngularWeb ComponentsMore

Once you understand the basics of writing addons, there are a variety of common enhancements to make your addon better. This page details additional information about addon creation. Use it as a quick reference guide when creating your own addons.

## 

Disable the addon panel

It’s possible to disable the addon panel for a particular story.

To make that possible, you need to pass the `paramKey` element when you register the panel:

/my-addon/manager.js
    
    
    addons.register(ADDON_ID, () => {
      addons.add(PANEL_ID, {
        type: types.PANEL,
        title: 'My Addon',
        render: () => <div>Addon tab content</div>,
        paramKey: 'myAddon', // this element
      });
    });

Then when adding a story, you can pass a disabled parameter.

CSF 3CSF Next 🧪

Button.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Meta } from '@storybook/your-framework';
     
    import { Button } from './Button';
     
    const meta = {
      /* 👇 The title prop is optional.
       * See https://storybook.js.org/docs/configure/#configure-story-loading
       * to learn how to generate automatic titles
       */
      title: 'Button',
      component: Button,
      parameters: {
        myAddon: { disable: true }, // Disables the addon
      },
    } satisfies Meta<typeof Button>;
     
    export default meta;

## 

Style your addon

Storybook uses [Emotion](https://emotion.sh/docs/introduction) for styling. Alongside with a theme that you can customize!

We recommend using Emotion to style your addon’s UI components. That allows you to use the active Storybook theme to deliver a seamless developer experience. If you don’t want to use Emotion, you can use inline styles or another css-in-js lib. You can receive the theme as a prop by using Emotion's `withTheme` HOC. [Read more about theming](../configure/user-interface/theming).

## 

Storybook components

Addon authors can develop their UIs using any React library. But we recommend using Storybook’s UI components in `storybook/internal/components` to build addons faster. When you use Storybook components, you get:

  * Battle-tested off-the-shelf components
  * Storybook native look and feel
  * Built-in support for Storybook theming



Use the components listed below with your next addon.

Component| Source| Story  
---|---|---  
Action Bar| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/ActionBar/ActionBar.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-actionbar--single-item)  
Addon Panel| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/addon-panel/addon-panel.tsx)| N/A  
Badge| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/Badge/Badge.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-badge--all-badges)  
Button| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/Button/Button.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-button--all-buttons)  
Form| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/form/index.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-form-button--sizes)  
Loader| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/Loader/Loader.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-loader--progress-bar)  
PlaceHolder| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/placeholder/placeholder.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-placeholder--single-child)  
Scroll Area| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/ScrollArea/ScrollArea.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-scrollarea--vertical)  
Space| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/spaced/Spaced.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-spaced--row)  
Syntax Highlighter| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/syntaxhighlighter/syntaxhighlighter.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-syntaxhighlighter--bash)  
Tabs| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/tabs/tabs.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-tabs--stateful-static)  
ToolBar| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/bar/bar.tsx)| N/A  
ToolTip| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/tooltip/Tooltip.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-tooltip-tooltip--basic-default)  
Zoom| [See component implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/Zoom/Zoom.tsx)| [See component story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-zoom--element-actual-size)  
  
Complementing the components, also included is a set of UI primitives. Use the content listed below as a reference for styling your addon.

Component| Source| Story  
---|---|---  
Color Palette (see note below)| [See implementation](https://github.com/storybookjs/storybook/blob/next/code/addons/docs/src/blocks/components/ColorPalette.tsx)| [See story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-colorpalette--page)  
Icon| [See implementation](https://github.com/storybookjs/storybook/blob/next/code/core/src/components/components/icon/icon.tsx)| [See story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-icon--labels)  
Typography| [See implementation](https://github.com/storybookjs/storybook/tree/next/code/core/src/components/components/typography)| [See story](https://main--5a375b97f4b14f0020b0cda3.chromatic.com/?path=/story/basics-typography--all)  
  
ℹ️

The color palette implemented by `@storybook/addon-docs/blocks` is a high-level abstraction of the [`storybook/theming`](https://github.com/storybookjs/storybook/tree/next/code/core/src/theming) module.

## 

Build system

When you're developing your addon as a package, you can’t use `npm link` to add it to your project. List your addon as a local dependency into your package.json:

package.json
    
    
    {
      "dependencies": {
        "@storybook/addon-controls": "file:///home/username/myrepo"
      }
    }

ℹ️

Run either `yarn` or `npm install` to install the addon.

## 

Hot module replacement

While developing your addon, you can configure HMR (hot module replacement) to reflect the changes made.

## 

Standalone Storybook addons

If you're developing a standalone addon, add a new script to `package.json` with the following:

package.json
    
    
    {
      "scripts": {
        "start": "npm run build -- --watch"
      }
    }

### 

Local Storybook addons

If you're developing a local Storybook addon built on top of an existing Storybook installation, HMR (hot module replacement) is available out of the box.

## 

Composing addons in presets

If you're working on a preset that loads third-party addons, which you don't have control over, and you need access to certain features (e.g., decorators) or provide additional configurations. In that case, you'll need to update your preset to the following to allow you to load and configure the other addons:

my-preset/index.js
    
    
    function managerEntries(entry = []) {
      return [...entry, import.meta.resolve('my-other-addon/manager')];
    }
     
    const previewAnnotations = (entry = [], options) => {
      return [...entry, import.meta.resolve('my-other-addon/preview')];
    };
     
    export default {
      managerEntries,
      previewAnnotations,
    };

If you have control over the addons you want to customize. In that case, you can update your preset and implement a custom function to load any additional presets and provide the necessary configuration.

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/addons/addon-knowledge-base.mdx)