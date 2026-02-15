# The block in the Editor

**Source:** [https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-in-the-editor/](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-in-the-editor/)



# The block in the Editor




## In this article


Table of Contents- Built-in components
- Block Controls: Block Toolbar and Settings SidebarBlock ToolbarSettings Sidebar
- Additional resources



↑Back to top


The Block Editor is a React Single Page Application (SPA). Every block in the Editor is displayed through a React component defined in theeditproperty of the settings object used toregister the blockon the client.


Thepropsobject received by the block’sEditReact component includes:


- attributes:An object of all the block’s attributes.
- setAttributes:A method to update the attributes object.
- isSelected:A boolean value that communicates whether the block is currently selected


WordPress provides many built-in standard components that can be used to define the block interface in the Editor. These built-in components are available via packages such as@wordpress/componentsand@wordpress/block-editor.



    The WordPress Gutenberg project uses [Storybook](https://wordpress.github.io/gutenberg/?path=/docs/docs-introduction--page) to document the user interface components that are available in WordPress packages.

Custom settings controls for the block in the Block Toolbar or the Settings Sidebar can also be defined through thisEditReact component via built-in components such as:


- InspectorControls
- BlockControls


## Built-in components


The package@wordpress/componentsincludes a library of generic WordPress components to create common UI elements for the Block Editor and the WordPress dashboard. Some of the  most commonly used components from this package are:


- TextControl
- Panel
- ToggleControl
- ExternalLink


The package@wordpress/block-editorincludes a library of components and hooks for the Block Editor, including those to define custom settings controls for the block. Some of the components most commonly used from this package are:


- RichText
- BlockControls
- InspectorControls
- InnerBlocks



    The package [@wordpress/block-editor](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-block-editor/) also provides the tools to create and use standalone block editors.

A good workflow when using a component for the Block Editor is:


- Import the component from a WordPress package.
- Add the corresponding code for the component to your project in JSX format.
- Most built-in components will be used to setblock attributes, so define any necessary attributes inblock.jsonand create event handlers to update those attributes withsetAttributesin your component.
- Adapt the code to be serialized and stored in the database if needed.


## Block Controls: Block Toolbar and Settings Sidebar


To simplify block customization and ensure a consistent user experience, there are several built-in UI patterns to help generate the Editor preview of a block.


The image below details the Block Toolbar and the Settings Sidebar of a selected Paragraph block.



### Block Toolbar


When the user selects a block, a number of control buttons may be shown in a toolbar above the selected block. Some of these block-level controls may be included automatically, but you can also customize the toolbar to include controls specific to your block type. If the return value of your block type’sEditfunction includes aBlockControlselement, those controls will be shown in the selected block’s toolbar.


```
export default function Edit( { className, attributes: attr, setAttributes } ) {

    const onChangeContent = ( newContent ) => {
        setAttributes( { content: newContent } );
    };

    const onChangeAlignment = ( newAlignment ) => {
        setAttributes( {
            alignment: newAlignment === undefined ? 'none' : newAlignment,
        } );
    };

    return (
        <div { ...useBlockProps() }>
            <BlockControls>
                <ToolbarGroup>
                    <AlignmentToolbar
                        value={ attr.alignment }
                        onChange={ onChangeAlignment }
                    />
                </ToolbarGroup>
            </BlockControls>

            <RichText
                className={ className }
                style={ { textAlign: attr.alignment } }
                tagName="p"
                onChange={ onChangeContent }
                value={ attr.content }
            />
        </div>
    );
}

```


See thefull block exampleof thecode above.


Note thatBlockControlsis only visible when the block is currently selected and in visual editing mode.BlockControlsare not shown when editing a block in HTML editing mode.


### Settings Sidebar


The Settings Sidebar is used to display less-often-used settings or those that require more screen space. The Settings Sidebar should be used forblock-level settings onlyand is shown when a block is selected.


If a setting only affects selected content inside a block, such as “bolding” text,do not place the setting inside the Settings Sidebar. Use a toolbar instead. The Settings Sidebar is displayed even when editing a block in HTML mode, so it should only contain block-level settings.


Similar to rendering a toolbar, if you include anInspectorControlscomponent in thereturnvalue of your block type’sEditfunction, those controls will be shown in the Settings Sidebar region.


```
export default function Edit( { attributes, setAttributes } ) {
    const onChangeBGColor = ( hexColor ) => {
        setAttributes( { bg_color: hexColor } );
    };

    const onChangeTextColor = ( hexColor ) => {
        setAttributes( { text_color: hexColor } );
    };

    return (
        <div { ...useBlockProps() }>
            <InspectorControls key="setting">
                <div>
                    <fieldset>
                        <legend className="blocks-base-control__label">
                            { __( 'Background color', 'block-development-examples' ) }
                        </legend>
                        <ColorPalette // Element Tag for Gutenberg standard color selector
                            onChange={ onChangeBGColor } // onChange event callback
                        />
                    </fieldset>
                    <fieldset>
                        <legend className="blocks-base-control__label">
                            { __( 'Text color', 'block-development-examples' ) }
                        </legend>
                        <ColorPalette
                            onChange={ onChangeTextColor }
                        />
                    </fieldset>
                </div>
            </InspectorControls>
            <TextControl
                __next40pxDefaultSize
                value={ attributes.message }
                onChange={ ( val ) => setAttributes( { message: val } ) }
                style={ {
                    backgroundColor: attributes.bg_color,
                    color: attributes.text_color,
                } }
            />
        </div>
    );
}

```


See thefull block exampleof thecode above.


Block controls rendered in both the toolbar and sidebar will also be available when multiple blocks of the same type are selected.



    For common customization settings, including color, border, spacing, and more, you can rely on [block supports](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-json/#enable-ui-settings-panels-for-the-block-with-supports) instead of a custom solution. Block supports provide a consistent UI with the same functionality as other Core blocks.

## Additional resources


- Storybook for WordPress components
- @wordpress/block-editor
- @wordpress/components
- InspectorControls
- BlockControls





First published


December 18, 2023


Last updated


December 11, 2025


Edit article


Improve it on GitHub: The block in the Editor





[PreviousThe block wrapperPrevious: The block wrapper](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-wrapper/)
[NextMarkup representation of a blockNext: Markup representation of a block](https://developer.wordpress.org/block-editor/getting-started/fundamentals/markup-representation-block/)


