# File structure of a block

**Source:** [https://developer.wordpress.org/block-editor/getting-started/fundamentals/file-structure-of-a-block/](https://developer.wordpress.org/block-editor/getting-started/fundamentals/file-structure-of-a-block/)

## In this article

Table of Contents- <plugin-file>.php

- package.json
- src folderblock.jsonindex.jsedit.jssave.jsstyle.(css|scss|sass)editor.(css|scss|sass)render.phpview.js
- build folder
- Additional resources

↑Back to top

When developing custom blocks for WordPress, it’s best practice to register them within plugins rather than themes. This strategy guarantees that your blocks stay accessible, even when users switch themes. While there might be situations where embedding blocks directly into a theme could be appropriate, this guide focuses on blocks housed within a plugin. Specifically, it details the file structure as produced by thecreate-blocktool.

Adhering to thecreate-blocktool’s structure is not mandatory, but it serves as a reliable reference. The files it generates encompass everything needed for a block’s definition and registration. Following this structure can help maintain consistency and ensure your blocks are well-organized and easy to maintain.

## <plugin-file>.php

When creating a block in a WordPress plugin, you usually register the block on the server in the main PHP file of the plugin. This is done using theregister_block_type()function.

```text
For more on creating a WordPress plugin, refer to the documentation on [Plugin Basics](https://developer.wordpress.org/plugins/plugin-basics/) and the [Header Requirements](https://developer.wordpress.org/plugins/plugin-basics/header-requirements/) for the main PHP file.

```python

## package.json

Thepackage.jsonfile is used to configure a Node.js project, which is technically what a block plugin is. In this file, you define thenpmdependencies of the block and the scripts used for local development.

## src folder

In a standard project, thesrc(source) folder contains the raw, uncompiled code, including JavaScript, CSS, and other assets necessary for developing the block. This is where you write and edit your block’s source code, utilizing modern JavaScript features and JSX for React components.

Thebuild processprovided bywp-scriptswill then take the files from this folder and generate the production-ready files in the project’sbuildfolder.

### block.json

Theblock.jsonfile contains theblock’s metadata, streamlining its definition and registration across client-side and server-side environments.

This file includes the block name, description,attributes,supports, and more, as well as the locations of essential files responsible for the block’s functionality, appearance, and styling.

When a build process is applied, theblock.jsonfile and the other generated files are moved to a designated folder, often thebuildfolder. Consequently, the file paths specified withinblock.jsonpoint to these processed, bundled versions of the files.

A few of the most important properties that can be defined in ablock.jsonare:

- editorScript:Usually set with the path of a bundledindex.jsfile that was built fromsrc/index.js.
- style:Usually set with the path of a bundledstyle-index.cssfile that was built fromsrc/style.(css|scss|sass).
- editorStyle:Usually set with the path of a bundledindex.cssthat was built fromsrc/editor.(css|scss|sass).
- render:Usually set with the path of a bundledrender.phpthat was copied fromsrc/render.php.
- viewScript:Usually set with the path of a bundledview.jsthat was built fromsrc/view.js.

### index.js

Theindex.jsfile (or any other file defined in theeditorScriptproperty ofblock.json) is the entry point file for JavaScript that should only get loaded in the Block Editor. It’s responsible for calling theregisterBlockTypefunction to register the block on the client and typically imports theedit.jsandsave.jsfiles to get the functions required for block registration.

### edit.js

Theedit.jsfile contains the React component responsible for rendering the block’s editing user interface, allowing users to interact with and customize the block’s content and settings in the Block Editor. This component gets passed to theeditproperty of theregisterBlockTypefunction in theindex.jsfile.

### save.js

Thesave.jsexports the function that returns the static HTML markup that gets saved to the WordPress database. This function gets passed to thesaveproperty of theregisterBlockTypefunction in theindex.jsfile.

### style.(css|scss|sass)

Astylefile with extensions.css,.scss, or.sasscontains the styles of the block that will be loaded in both the Block Editor and on the front end. In the build process, this file is converted intostyle-index.css, which is usually defined using thestyleproperty inblock.json

```text

The webpack configuration used internally by `wp-scripts` includes a [css-loader](https://webpack.js.org/loaders/css-loader/) chained with [postcss-loader](#) and [sass-loader](https://webpack.js.org/loaders/sass-loader/) that allows it to process CSS, SASS or SCSS files. Check [Default webpack config](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-scripts/#default-webpack-config) for more info

```python

### editor.(css|scss|sass)

Aneditorfile with extensions.css,.scss, or.sasscontains the additional styles applied to the block in the Block Editor. You will often use this file for styles specific to the block’s user interface. This file is converted toindex.cssduring the build process, usually defined using theeditorStyleproperty inblock.json.

### render.php

Therender.phpfile (or any other file defined in therenderproperty ofblock.json) defines the server-side process that returns the markup for the block when there is a request from the front end. If defined, this file will take precedence over other ways to render the block’s markup on the front end.

### view.js

Theview.jsfile (or any other file defined in theviewScriptproperty ofblock.json) will be loaded in the front end when the block is displayed.

## build folder

Thebuildfolder contains the compiled and optimized versions of the code from thesrcfolder. These files are generated from thebuild process, triggered by thebuildorstartcommands ofwp-scripts.

This transformation process includes minification, transpilation from modern JavaScript to a version compatible with a wider range of browsers, and bundling of assets for efficient loading. WordPress ultimately enqueues and uses thebuildfolder’s contents to render the block in the Block Editor and on the front end.

```text

You can use `webpack-src-dir` and `output-path` option of `wp-scripts` build commands to [customize the entry and output points](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-scripts/#automatic-block-json-detection-and-the-source-code-directory).

```

## Additional resources

- Diagram featuring the file structure of a block

First published

November 28, 2023

Last updated

May 23, 2024

Edit article

Improve it on GitHub: File structure of a block

[PreviousFundamentals of Block DevelopmentPrevious: Fundamentals of Block Development](https://developer.wordpress.org/block-editor/getting-started/fundamentals/)
[Nextblock.jsonNext: block.json](https://developer.wordpress.org/block-editor/getting-started/fundamentals/block-json/)
