# The block wrapper

**Source:** [https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-wrapper/](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-wrapper/)



# The block wrapper




## In this article


Table of Contents- Editor markup
- Save markup
- Dynamic render markup



↑Back to top


Every block in the Block Editor is contained within an HTML wrapper, which must have specific attributes to function correctly both in the Editor and on the front end. As developers, we can directly manipulate this markup, and WordPress offers tools likeuseBlockProps()to modify the attributes added to a block’s wrapper.


Ensuring proper attributes to the block wrapper is especially important when using custom styling or features likeblock supports.


A block in WordPress can be defined with three distinct types of markup, each serving a unique role:


- Editor Markup:This is the visual representation of the block within the Block Editor. It’s defined using anEditReact component when the block is registered on the client side viaregisterBlockType.
- Save Markup:This markup is what gets saved to the database when the block’s content is saved. It’s specified through asavefunction, also provided toregisterBlockTypeduring block registration. If the block doesn’t utilize dynamic rendering, this saved markup is what will be displayed on the front end.
- Dynamic Render Markup:When a block’s content needs to be generated dynamically, this markup comes into play. It’s defined server-side, either through arender_callbackfunction inregister_block_typeor arender.phpfile specified inblock.json. If present, this markup overrides any saved markup and is used for the block’s front-end display.


For both theEditcomponent and thesavefunction, it’s important to use a wrapper element that’s a standard DOM element (like a<div>) or a React component that passes all additional props to native DOM elements. Using React Fragments (<Fragment>) or the<ServerSideRender>component won’t work for these wrappers.


## Editor markup


TheuseBlockProps()hook, provided by the@wordpress/block-editorpackage, is used to define the outer markup of a block in theEditcomponent.


This hook simplifies several tasks, including:


- Assigning a uniqueidto the block’s HTML structure.
- Adding various accessibility anddata-attributes for enhanced functionality and information.
- Incorporating classes and inline styles that reflect the block’s custom settings. By default, this includes:Thewp-blockclass for general block styling.A block-specific class that combines the block’s namespace and name, ensuring unique and targeted styling capabilities.


In the following example, the Editor markup of the block is defined in theEditcomponent using theuseBlockProps()hook.


```
const Edit = () => <p { ...useBlockProps() }>Hello World - Block Editor</p>;

registerBlockType( ..., {
    edit: Edit
} );

```


See thefull block exampleof thecode above.


The markup of the block in the Block Editor could look like this, where the classes and attributes are applied automatically:


```
<p
    tabindex="0"
    id="block-4462939a-b918-44bb-9b7c-35a0db5ab8fe"
    role="document"
    aria-label="Block: Minimal Gutenberg Block ca6eda"
    data-block="4462939a-b918-44bb-9b7c-35a0db5ab8fe"
    data-type="block-development-examples/minimal-block-ca6eda"
    data-title="Minimal Gutenberg Block ca6eda"
    class="
        block-editor-block-list__block
        wp-block
        is-selected
        wp-block-block-development-examples-minimal-block-ca6eda
    "
>Hello World - Block Editor</p>

```


In a block’sEditcomponent, use theuseBlockProps()hook to include additional classes and attributes by passing them as arguments. (Seeexample)


When you enable features using thesupportsproperty, any corresponding classes or attributes are included in the object returned byuseBlockPropsautomatically.


## Save markup


When saving the markup in the database, it’s important to add the props returned byuseBlockProps.save()to the wrapper element of your block.useBlockProps.save()ensures that the block class name is rendered correctly in addition to any HTML attributes injected by the block supports API.


Consider the following code that registers a block in the client. Notice how it defines the markup that should be used when editing the block and when the block is saved in the database.


```
const Edit = () => <p { ...useBlockProps() }>Hello World - Block Editor</p>;
const save = () => <p { ...useBlockProps.save() }>Hello World - Frontend</p>;

registerBlockType( ..., {
    edit: Edit,
    save,
} );

```


See thefull block exampleof thecode above.


The markup of the block on the front end could look like this, where the class is applied automatically:


```
<p class="wp-block-block-development-examples-minimal-block-ca6eda">Hello World – Frontend</p>

```


If you want to add any additional classes or attributes to thesavefunction of the block, they should be passed as an argument ofuseBlockProps.save(). (Seeexample)


When you addsupportsfor any feature, the proper classes get added to the object returned by theuseBlockProps.save()hook. Text and background color classes have been added to the Paragraph block in the example below.


```
<p class="
    wp-block-block-development-examples-block-supports-6aa4dd
    has-accent-4-color
    has-contrast-background-color
    has-text-color
    has-background
">Hello World</p>

```


Theexample blockthat generated this HTML is available in theBlock Development Examplesrepository.


## Dynamic render markup


In dynamic blocks, where the front-end markup is rendered server-side, you can utilize theget_block_wrapper_attributes()function to output the necessary classes and attributes just like you would useuseBlockProps.save()in thesavefunction. (Seeexample)


```
<p <?php echo get_block_wrapper_attributes(); ?>>
    <?php esc_html_e( 'Block with Dynamic Rendering – hello!!!', 'block-development-examples' ); ?>
</p>

```





First published


November 29, 2023


Last updated


August 13, 2024


Edit article


Improve it on GitHub: The block wrapper





[PreviousRegistration of a blockPrevious: Registration of a block](https://developer.wordpress.org/block-editor/getting-started/fundamentals/registration-of-a-block/)
[NextThe block in the EditorNext: The block in the Editor](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-in-the-editor/)


