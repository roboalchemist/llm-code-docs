# How-to Guides

**Source:** [https://developer.wordpress.org/block-editor/how-to-guides/](https://developer.wordpress.org/block-editor/how-to-guides/)

## In this article

Table of Contents- Creating blocks

- Extending blocks
- Extending the Editor UI
- Meta boxes
- Theme support
- Autocomplete
- Block parsing and serialization

↑Back to top

The new editor is highly flexible, like most of WordPress. You can build custom blocks, modify the editor’s appearance, add special plugins, and much more.

## Creating blocks

The editor is about blocks, and the main extensibility API is the Block API. It allows you to create your own static blocks,Dynamic Blocks( rendered on the server ) and also blocks capable of saving data to Post Meta for more structured content.

If you want to learn more about block creation, see theCreate a Block tutorialfor the best place to start.

## Extending blocks

It is also possible to modify the behavior of existing blocks or even remove them completely using filters.

Learn more in theBlock Filterssection.

Specifically forQuery Loopblock, besides the available filters, there are more ways to extend it and create bespoke versions of it. Learn more in theExtending the Query Loop blocksection.

## Extending the Editor UI

Extending the editor UI can be accomplished with theregisterPluginAPI, allowing you to define all your plugin’s UI elements in one place.

Refer to thePluginsandEdit Postsection for more information.

You can also filter certain aspects of the editor; this is documented on theEditor Filterspage.

## Meta boxes

Porting PHP meta boxes to blocks or sidebar plugins is highly encouraged, learn how in themeta boxandsidebar pluginguides.

## Theme support

By default, blocks provide their styles to enable basic support for blocks in themes without any change. Themes can add/override these styles, or rely on defaults.

There are some advanced block features which require opt-in support in the theme. Seetheme supportandhow to filter global styles.

## Autocomplete

Autocompleters within blocks may be extended and overridden. Learn more about theautocompletefilters.

## Block parsing and serialization

Posts in the editor move through a couple of different stages between being stored inpost_contentand appearing in the editor. Since the blocks themselves are data structures that live in memory it takes a parsing and serialization step to transform out from and into the stored format in the database.

Customizing the parser is an advanced topic that you can learn more about in theExtending the Parsersection.

First published

March 9, 2021

Last updated

January 16, 2024

Edit article

Improve it on GitHub: How-to Guides

[PreviousFrequently Asked QuestionsPrevious: Frequently Asked Questions](https://developer.wordpress.org/block-editor/getting-started/faq/)
[NextAccessibilityNext: Accessibility](https://developer.wordpress.org/block-editor/how-to-guides/accessibility/)
