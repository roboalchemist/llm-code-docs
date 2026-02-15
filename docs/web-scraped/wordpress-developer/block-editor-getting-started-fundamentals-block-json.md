# block.json

**Source:** [https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-json/](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-json/)



# block.json




## In this article


Table of Contents- Basic metadata of a block
- Files for the block’s behavior, output, or style
- Using block attributes to store dataReading and updating attributes
- Using block supports to enable settings and styles
- Additional resources



↑Back to top


Theblock.jsonfile simplifies the process of defining and registering a block by using the same block’s definition in JSON format to register the block on both the server and the client (Block Editor).


The diagram below details the basic structure of theblock.jsonfile.




    To view a complete block example and its associated [block.json](https://github.com/WordPress/block-development-examples/blob/trunk/plugins/block-supports-6aa4dd/src/block.json) file, visit the [Block Development Examples](https://github.com/WordPress/block-development-examples/tree/trunk/plugins/block-supports-6aa4dd) GitHub repository.

Besides simplifying a block’s registration, using ablock.jsonhasseveral benefits, including improved performance.


TheMetadata in block.jsondocumentation has a comprehensive guide on all the properties you can use in ablock.jsonfile for a block. This article will cover the most common options, which allow you to specify:


- The block’s basic metadata.
- The files that dictate the block’s functionality, appearance, and output.
- How data is stored within the block.
- The block’s setting panels within the user interface.


## Basic metadata of a block


Usingblock.jsonproperties, you can define how the block will be uniquely identified and what information is displayed in the Block Editor. These properties include:


- apiVersion:Specifies theAPIversion the block uses. Use the latest version unless you have specific requirements.
- name:The unique name of the block, including namespace (e.g.,my-plugin/my-custom-block).
- title:The display title for the block, shown in the Inserter.
- category:The category under which the block appears in the Inserter. Common categories includetext,media,design,widgets, andtheme.
- icon:An icon representing the block in the Inserter. This can be aDashiconslug or a custom SVG icon.
- description:A short description of the block, providing more context than the title.
- keywords:An array of keywords to help users find the block when searching.
- textdomain:The text domain for the block, used for internationalization.


## Files for the block’s behavior, output, or style


Theblock.jsonfile also allows you to specify the essential files for a block’s functionality:


- editorScript:A JavaScript file or files for use only in the Block Editor.
- editorStyle:A CSS file or files for styling within the Block Editor.
- script:A JavaScript file or files loaded in both the Block Editor and the front end.
- style:A CSS file or files applied in both the Block Editor and the front end.
- viewScript:A JavaScript file or files intended solely for the front end.


For all these properties, you can provide afile path(starting withfile:), ahandlethat has been registered usingwp_register_scriptorwp_register_style, or an array combining both options.


Additionally, therenderproperty,introduced on WordPress 6.1, specifies the path to a PHP template file responsible for generating adynamically renderedblock’s front-end markup. This approach is used if a$render_callbackfunction is not provided to theregister_block_type()function.


## Using block attributes to store data


Blockattributesare settings or data assigned to blocks. They can determine various aspects of a block, such as its content, layout, style, and any other specific information you need to store along with your block’s structure. If the user changes a block, such as modifying the font size, you need a way to persist these changes. Attributes are the solution.


When registering a new block type, theattributesproperty ofblock.jsondescribes the custom data the block requires and how they’re stored in the database. This allows the Block Editor to parse these values correctly and pass theattributesto the block’sEditcomponent andsavefunction.


Here’s an example of three attributes defined inblock.json:


```
"attributes": {
    "fallbackCurrentYear": {
        "type": "string"
    },
    "showStartingYear": {
        "type": "boolean"
    },
    "startingYear": {
        "type": "string"
    }
},

```


Blocks are “delimited” using HTML-style comment tags that contain specific JSON-like attributes. These delimiters make it possible to recognize block boundaries and parse block attributes when rendering post content or editing a post in the Block Editor.


The code example below demonstrates the attributes defined in the block delimiter.


```
<!-- wp:block-development-examples/copyright-date-block-09aac3 {"fallbackCurrentYear":"2023","showStartingYear":true,"startingYear":"2020"} -->
<p class="wp-block-block-development-examples-copyright-date-block-09aac3">© 2020–2023</p>
<!-- /wp:block-development-examples/copyright-date-block-09aac3 -->

```


All attributes are serialized and stored in the block’s delimiter by default, but this can be configured to suit your needs. Check out theUnderstanding Block Attributesarticle to learn more.


### Reading and updating attributes


Theseattributesare passed to the block’sEditReact component for display in the Block Editor, to thesavefunction for generating the markup that gets stored in the database, and to any server-side rendering definition for the block.


TheEditcomponent uniquely possesses the ability to modify these attributes through thesetAttributesfunction.


The following diagram details how attributes are stored, read, and updated in a typical block.



See how the attributes are passed to theEditcomponent, thesavefunction, andrender.phpin thiscomplete block example.


For more information about attributes and how to use them in your custom blocks, visit theAttributes APIreference page.


## Using block supports to enable settings and styles


Many blocks, including Core blocks, offer similar customization options, such as background color, text color, and padding adjustments.


Thesupportsproperty inblock.jsonallows a block to declare support for a set of these common customization options. When enabled, users of the block can then adjust things like color or padding directly from the Settings Sidebar.


Leveraging these predefined block supports helps ensure your block behaves consistently with Core blocks, eliminating the need to recreate similar functionalities from scratch.


Here’s an example of color supports defined inblock.json:


```
"supports": {
    "color": {
        "text": true,
        "link": true,
        "background": true
    }
}

```


The use of block supports generates a set of properties that need to be manually added to thewrapping element of the block. This ensures they’re properly stored as part of the block data and taken into account when generating the markup of the block that will be delivered to the front end.


The following code demonstrates how the attributes and CSS classes generated by enabling block supports are stored in the markup representation of the block.


```
<!-- wp:block-development-examples/block-supports-6aa4dd {"backgroundColor":"contrast","textColor":"accent-4"} -->
<p class="wp-block-block-development-examples-block-supports-6aa4dd has-accent-4-color has-contrast-background-color has-text-color has-background">Hello World</p>
<!-- /wp:block-development-examples/block-supports-6aa4dd -->

```


See thecomplete block exampleof thecode above.


For more information about supports and how to use them in your custom blocks, visit theSupports APIreference page.


## Additional resources


- block.json diagram
- Attributes diagram





First published


November 29, 2023


Last updated


February 7, 2024


Edit article


Improve it on GitHub: block.json





[PreviousFile structure of a blockPrevious: File structure of a block](https://developer.wordpress.org/block-editor/getting-started/fundamentals/file-structure-of-a-block/)
[NextRegistration of a blockNext: Registration of a block](https://developer.wordpress.org/block-editor/getting-started/fundamentals/registration-of-a-block/)


