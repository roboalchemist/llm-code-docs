# Storybook Documentation
# Source: https://storybook.js.org/docs/writing-docs/doc-blocks
# Page: /docs/writing-docs/doc-blocks

# Doc blocks

ReactVueAngularWeb ComponentsMore

Storybook offers several doc blocks to help document your components and other aspects of your project.

There are two common ways to use doc blocks in Storybook, within MDX and as part of the docs page template.

## 

Within MDX

The blocks are most commonly used within Storybook's [MDX documentation](./mdx):

![Screenshot of mdx content](/docs-assets/10.1/writing-docs/mdx-example.png)

ButtonDocs.mdx
    
    
    import { Meta, Primary, Controls, Story } from '@storybook/addon-docs/blocks';
     
    import * as ButtonStories from './Button.stories';
     
    <Meta of={ButtonStories} />
     
    # Button
     
    A button is ...
     
    <Primary />
     
    ## Props
     
    <Controls />
     
    ## Stories
     
    ### Primary
     
    A button can be of primary importance.
     
    <Story of={ButtonStories.Primary} />
     
    A button can be of secondary importance.
     
    <Story of={ButtonStories.Secondary} />
     
    {/* ... */}

## 

Customizing the automatic docs page

The blocks are also used to define the page template for [automatics docs](./autodocs). For example, here's the default template:

![Screenshot of automatic docs template](/docs-assets/10.1/writing-docs/autodocs-default-template.png)
    
    
    import { Title, Subtitle, Description, Primary, Controls, Stories } from '@storybook/addon-docs/blocks';
     
    export const autoDocsTemplate = () => (
      <>
        <Title />
        <Subtitle />
        <Description />
        <Primary />
        <Controls />
        <Stories />
      </>
    );

If you [override the default page template](./autodocs#write-a-custom-template), you can similarly use Doc Blocks to build the perfect documentation page for your project.

Note that some doc blocks render other blocks. For example, the `<Stories />` block expands to:
    
    
    ## Stories
     
    <Canvas>
      ### Story name
      <Description />
      <Story />
      <Source />
    </Canvas>
     
    {/* ... repeat <Canvas> for each story */}

As a result, for example, customizing the [`Source`](../api/doc-blocks/doc-block-source) block via parameters (see next section) will also affect the Source blocks rendered as part of [`Canvas`](../api/doc-blocks/doc-block-canvas) blocks.

## 

Customizing doc blocks

In both use cases (MDX and automatic docs), many of the doc blocks can be customized via [parameters](../writing-stories/parameters).

For example, you can filter out the `style` prop from all [`Controls`](../api/doc-blocks/doc-block-controls) tables through your Storybook:

CSF 3CSF Next 🧪

.storybook/preview.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Preview } from '@storybook/your-framework';
     
    const preview: Preview = {
      parameters: {
        docs: {
          controls: { exclude: ['style'] },
        },
      },
    };
     
    export default preview;

ℹ️

Parameters can also be defined at the [component](../writing-stories/parameters#component-parameters) (or meta) level or the [story](../writing-stories/parameters#story-parameters) level, allowing you to customize Doc Blocks exactly as you need, where you need.

The blocks that accept customization via parameters are marked in the list of available blocks below.

When using a doc block in MDX, it can also be customized with its props:
    
    
    <Controls exclude={['style']}>

## 

Available blocks

Each block has a dedicated API reference page detailing usage, available options, and technical details.

### 

[ArgTypes](../api/doc-blocks/doc-block-argtypes)

ℹ️

Accepts parameters in the namespace `parameters.docs.argTypes`.

The `ArgTypes` block can be used to show a static table of [arg types](../api/arg-types) for a given component as a way to document its interface.

![Screenshot of ArgTypes block](/docs-assets/10.1/api/doc-block-argtypes.png)

### 

[Canvas](../api/doc-blocks/doc-block-canvas)

ℹ️

Accepts parameters in the namespace `parameters.docs.canvas`.

The `Canvas` block is a wrapper around a [`Story`](../api/doc-blocks/doc-block-story), featuring a toolbar that allows you to interact with its content while automatically providing the required [`Source`](../api/doc-blocks/doc-block-source) snippets.

![Screenshot of Canvas block](/docs-assets/10.1/api/doc-block-canvas.png)

### 

[ColorPalette](../api/doc-blocks/doc-block-colorpalette)

The `ColorPalette` block allows you to document all color-related items (e.g., swatches) used throughout your project.

![Screenshot of ColorPalette and ColorItem blocks](/docs-assets/10.1/api/doc-block-colorpalette.png)

### 

[Controls](../api/doc-blocks/doc-block-controls)

ℹ️

Accepts parameters in the namespace `parameters.docs.controls`.

The `Controls` block can be used to show a dynamic table of args for a given story, as a way to document its interface, and to allow you to change the args for a (separately) rendered story (via the [`Story`](../api/doc-blocks/doc-block-story) or [`Canvas`](../api/doc-blocks/doc-block-canvas) blocks).

![Screenshot of Controls block](/docs-assets/10.1/api/doc-block-controls.png)

### 

[Description](../api/doc-blocks/doc-block-description)

The `Description` block displays the description for a component, story, or meta obtained from their respective JSDoc comments.

![Screenshot of Description block](/docs-assets/10.1/api/doc-block-title-subtitle-description.png)

### 

[IconGallery](../api/doc-blocks/doc-block-icongallery)

The `IconGallery` block lets you quickly document all icons associated with your project, displayed in a neat grid.

![Screenshot of IconGallery and IconItem blocks](/docs-assets/10.1/api/doc-block-icongallery.png)

### 

[Markdown](../api/doc-blocks/doc-block-markdown)

The `Markdown` block allows you to import and include plain markdown in your MDX files.

![Screenshot of Markdown block](/docs-assets/10.1/api/doc-block-markdown.png)

### 

[Meta](../api/doc-blocks/doc-block-meta)

The `Meta` block is used to attach a custom MDX docs page alongside a component’s list of stories. It doesn’t render any content but serves two purposes in an MDX file:

  * Attaches the MDX file to a component and its stories, or
  * Controls the location of the unattached docs entry in the sidebar.



### 

[Primary](../api/doc-blocks/doc-block-primary)

The `Primary` block displays the primary (first defined in the stories file) story in a [`Story`](../api/doc-blocks/doc-block-story) block. It is typically rendered immediately under the title in a docs entry.

![Screenshot of Primary block](/docs-assets/10.1/api/doc-block-primary.png)

### 

[Source](../api/doc-blocks/doc-block-source)

ℹ️

Accepts parameters in the namespace `parameters.docs.source`.

The `Source` block is used to render a snippet of source code directly.

![Screenshot of Source block](/docs-assets/10.1/api/doc-block-source.png)

### 

[Stories](../api/doc-blocks/doc-block-stories)

The `Stories` block renders the full collection of stories in a stories file.

![Screenshot of Stories block](/docs-assets/10.1/api/doc-block-stories.png)

### 

[Story](../api/doc-blocks/doc-block-story)

ℹ️

Accepts parameters in the namespace `parameters.docs.story`.

[Stories](../writing-stories) are Storybook's fundamental building blocks.

In Storybook Docs, you can render any of your stories from your CSF files in the context of an MDX file with all annotations (parameters, args, loaders, decorators, play function) applied using the `Story` block.

![Screenshot of Story block](/docs-assets/10.1/api/doc-block-story.png)

### 

[Subtitle](../api/doc-blocks/doc-block-subtitle)

The `Subtitle` block can serve as a secondary heading for your docs entry.

![Screenshot of Subtitle block](/docs-assets/10.1/api/doc-block-title-subtitle-description.png)

### 

[Title](../api/doc-blocks/doc-block-title)

The `Title` block serves as the primary heading for your docs entry. It is typically used to provide the component or page name.

![Screenshot of Title block](/docs-assets/10.1/api/doc-block-title-subtitle-description.png)

### 

[Typeset](../api/doc-blocks/doc-block-typeset)

The `Typeset` block helps document the fonts used throughout your project.

![Screenshot of Typeset block](/docs-assets/10.1/api/doc-block-typeset.png)

### 

[Unstyled](../api/doc-blocks/doc-block-unstyled)

The `Unstyled` block is a unique block that disables Storybook's default styling in MDX docs wherever it is added.

By default, most elements (like `h1`, `p`, etc.) in docs have a few default styles applied to ensure the docs look good. However, sometimes you might want some of your content not to have these styles applied. In those cases, wrap the content with the `Unstyled` block to remove the default styles.

![Screenshot of Unstyled block](/docs-assets/10.1/api/doc-block-unstyled.png)

## 

Make your own Doc Blocks

Storybook also provides a [`useOf` hook](../api/doc-blocks/doc-block-useof) to make it easier to create your own blocks that function like the built-in blocks.

## 

Troubleshooting

### 

Why can't I use the Doc Blocks inside my stories?

Storybook's Doc Blocks are highly customizable and helpful building blocks to assist you with building your custom documentation. Although most of them enable you to customize them with parameters or globally to create custom documentation templates, they are primarily designed for MDX files. For example, if you try to add the `ColorPalette` block to your stories as follows, you'll get an error message when the story loads in Storybook.

CSF 3CSF Next 🧪

MyComponent.stories.ts|tsx

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Meta } from '@storybook/your-framework';
     
    import { ColorItem, ColorPalette } from '@storybook/addon-docs/blocks';
     
    import { MyComponent } from './MyComponent';
     
    const meta = {
      component: MyComponent,
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    const theme = {
      colors: {
        primaryDark: {
          value: '#1C1C1C',
        },
        primaryRegular: {
          value: '#363636',
        },
        primaryLight1: {
          value: '#4D4D4D',
        },
        primaryLight2: {
          value: '#878787',
        },
        primaryLight3: {
          value: '#D1D1D1',
        },
        primaryLight4: {
          value: '#EDEDED',
        },
      },
    };
     
    // ❌ Don't use the Doc Blocks inside your stories. It will break Storybook with a cryptic error.
    export const Colors: Story = {
      render: () => (
        <ColorPalette>
          {Object.entries(theme.colors).map(([key, { value }]) => (
            <ColorItem
              colors={{
                [key]: value,
              }}
              key={key}
              subtitle={`theme.colors.${key}`}
              title={key}
            />
          ))}
        </ColorPalette>
      ),
    };

**Learn more about Storybook documentation**

  * [Autodocs](./autodocs) for creating documentation for your stories
  * [MDX](./mdx) for customizing your documentation
  * Doc Blocks for authoring your documentation
  * [Publishing docs](./build-documentation) to automate the process of publishing your documentation



Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/writing-docs/doc-blocks.mdx)