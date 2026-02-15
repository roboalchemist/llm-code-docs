# Package Reference

**Source:** [https://developer.wordpress.org/block-editor/reference-guides/packages/](https://developer.wordpress.org/block-editor/reference-guides/packages/)

## In this article

Table of Contents- Package Guidelines

- Using the packages via WordPress global
- Using the packages via npm
- Testing JavaScript code from a specific major WordPress version

↑Back to top

WordPress exposes a list of JavaScript packages and tools for WordPress development.

For information on creating and managing packages in Gutenberg, see thepackages README. For details on the build system and package configuration, see the@wordpress/build README.

## Package Guidelines

Packages are the first layer of architecture in Gutenberg. Each package should have a single, clear purpose, include a README, document prerequisites and public APIs, and avoid utility/kitchen-sink patterns. Default to bundled packages unless globals or modules are necessary.

For complete guidelines, see thepackage guidelinesin the packages README.

## Using the packages via WordPress global

JavaScript packages are available as a registered script in WordPress and can be accessed using thewpglobal variable.

If you wanted to use thePlainTextcomponent from the block editor module, first you would specifywp-block-editoras a dependency when you enqueue your script:

```php
wp_enqueue_script(
    'my-custom-block',
    plugins_url( $block_path, __FILE__ ),
    array( 'react', 'wp-blocks', 'wp-block-editor', 'wp-i18n' )
);

```

After the dependency is declared, you can access the module in your JavaScript code using the globalwplike so:

```javascript

const { PlainText } = wp.blockEditor;

```

## Using the packages via npm

All the packages are also available onnpmif you want to bundle them in your code.

Using the samePlainTextexample, you would install the block editor module with npm:

```bash

npm install @wordpress/block-editor --save

```

Once installed, you can access the component in your code using:

```python

import { PlainText } from '@wordpress/block-editor';

```python

## Testing JavaScript code from a specific major WordPress version

There is a way to quickly install a version of the individual WordPress package used with a given WordPress major version usingnpm distribution tags(example for WordPress5.8.x):

```bash

npm install @wordpress/block-editor@wp-5.8

```

It’s also possible to update all existing WordPress packages in the project with a single command:

```bash

npx @wordpress/scripts packages-update --dist-tag=wp-5.8

```

All major WordPress versions starting from5.7.xare supported (e.g.,wp-5.7orwp-6.0). Each individual dist-tag always points to the latest bug fix release for that major version line.

First published

March 9, 2021

Last updated

December 12, 2025

Edit article

Improve it on GitHub: Package Reference

[PreviousZStackPrevious: ZStack](https://developer.wordpress.org/block-editor/reference-guides/components/z-stack/)
[Next@wordpress/a11yNext: @wordpress/a11y](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-a11y/)
