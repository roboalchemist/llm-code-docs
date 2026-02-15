# Registration of a block

**Source:** [https://developer.wordpress.org/block-editor/getting-started/fundamentals/registration-of-a-block/](https://developer.wordpress.org/block-editor/getting-started/fundamentals/registration-of-a-block/)



# Registration of a block




## In this article


Table of Contents- Registering a block with PHP (server-side)PHP-only blocks with auto-registration
- Registering a block with JavaScript (client-side)
- Additional resources



↑Back to top


Blocks in WordPress are typically bundled in a plugin and registered on both the server and client-side usingblock.jsonmetadata.


While it’s possible to register blocks solely on the client-side, best practices strongly advise registering them on both the server and client. This dual registration is crucial for enabling server-side features such as Dynamic Rendering, Block Supports, Block Hooks, and Style Variations. Without server-side registration, these functionalities will not operate correctly.


For instance, if you want a blockto be styled viatheme.json, it must be registered on the server. Otherwise, the block won’t recognize or apply any styles assigned to it intheme.json.


The following diagram details the registration process for a block.



## Registering a block with PHP (server-side)


Block registration on the server usually takes place in the main plugin PHP file with theregister_block_type()function called on theinithook. This function simplifies block type registration by reading metadata stored in ablock.jsonfile.


This function is designed to register block types and primarily uses two parameters in this context, although it can accommodate more variations:


- $block_type(string):This can either be the path to the directory containing theblock.jsonfile or the complete path to the metadata file if it has a different name. This parameter tells WordPress where to find the block’s configuration.
- $args(array):This is an optional parameter where you can specify additional arguments for the block type. By default, this is an empty array, but it can include various options, one of which is the$render_callback. This callback is used to render blocks on the front end and is an alternative to therenderproperty inblock.json.


During the development process, theblock.jsonfile is typically moved from thesrc(source) directory to thebuilddirectory as part of compiling your code. Therefore, when registering your block, ensure the$block_typepath points to theblock.jsonfile within thebuilddirectory.


Theregister_block_type()function returns the registered block type (WP_Block_Type) on success orfalseon failure. Here is a simple example using therender_callback.


```
register_block_type(
    __DIR__ . '/build',
    array(
        'render_callback' => 'render_block_core_notice',
    )
);

```


Here is a more complete example, including theinithook.


```
function minimal_block_ca6eda___register_block() {
    register_block_type( __DIR__ . '/build' );
}
add_action( 'init', 'minimal_block_ca6eda___register_block' );

```


See thefull block exampleof thecode above


### PHP-only blocks with auto-registration


For blocks that only need server-side rendering, you can register them exclusively in PHP using theauto_registerflag and arender_callback. These blocks automatically appear in the editor without requiring any JavaScript registration or client-side code and usedynamic rendering.


```
register_block_type( 'my-plugin/server-block', array(
    'render_callback' => function( $attributes ) {
        $wrapper_attributes = get_block_wrapper_attributes();

        return sprintf(
            '<div %1$s>Server content</div>',
            $wrapper_attributes
        );
    },
    'supports' => array(
        'auto_register' => true,
        'color' => array(
            'background' => true,
        ),
    ),
) );

```


## Registering a block with JavaScript (client-side)


When the block has already been registered on the server and unless usingPHP-only auto-registered blocks, you only need to register the client-side settings in JavaScript using theregisterBlockTypemethod from the@wordpress/blockspackage. You just need to make sure you use the same block name as defined in the block’sblock.jsonfile. Here’s an example:


```
import { registerBlockType } from '@wordpress/blocks';

registerBlockType( 'my-plugin/notice', {
    edit: Edit,
    // ...other client-side settings
} );

```


While it’s generally advised to register blocks on the server using PHP for the benefits outlined in the“Benefits using the metadata file”section, you can opt to register a block solely on the client-side. TheregisterBlockTypemethod allows you to register a block type using metadata.


The function accepts two parameters:


- blockNameOrMetadata(string|Object):This can either be the block type’s name as a string or an object containing the block’s metadata, which is typically loaded from theblock.jsonfile.
- settings(Object):This is an object containing the block’s client-side settings.



    You can import the contents of the `block.json` file (or any other `.json` file) directly into your JavaScript files if you’re using a build process, such as the one provided by [wp-scripts](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-scripts/#the-build-process-with-wp-scripts).

Thesettingsobject passed as the second parameter includes many properties, but these are the two most important ones:


- edit:The React component that gets used in the Editor for our block.
- save:The function that returns the static HTML markup that gets saved to the database.


TheregisterBlockType()function returns the registered block type (WPBlock) on success orundefinedon failure. Here’s an example:


```
import { registerBlockType } from '@wordpress/blocks';
import { useBlockProps } from '@wordpress/block-editor';
import metadata from './block.json';

const Edit = () => <p { ...useBlockProps() }>Hello World - Block Editor</p>;
const save = () => <p { ...useBlockProps.save() }>Hello World - Frontend</p>;

registerBlockType( metadata.name, {
    edit: Edit,
    save,
} );

```


See thefull block exampleof thecode above


## Additional resources


- register_block_typePHP function
- registerBlockTypeJS function
- Why a block needs to be registered in both the server and the client?| GitHub Discussion
- Block Registration diagram





First published


November 28, 2023


Last updated


October 14, 2025


Edit article


Improve it on GitHub: Registration of a block





[Previousblock.jsonPrevious: block.json](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-json/)
[NextThe block wrapperNext: The block wrapper](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-wrapper/)


