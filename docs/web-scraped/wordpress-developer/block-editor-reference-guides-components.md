# Component Reference

**Source:** [https://developer.wordpress.org/block-editor/reference-guides/components/](https://developer.wordpress.org/block-editor/reference-guides/components/)



# Component Reference




## In this article


Table of Contents- Installation
- UsagePopoversTypeScript
- Docs & examples
- Contributing to this package



↑Back to top


This package includes a library of generic WordPress components to be used for creating common UI elements shared between screens and features of the WordPress dashboard.


## Installation


```
npm install @wordpress/components --save

```


This package assumes that your code will run in anES2015+environment. If you’re using an environment that has limited or no support for such language features and APIs, you should includethe polyfill shipped in@wordpress/babel-preset-defaultin your code.


## Usage


Within Gutenberg, these components can be accessed by importing from thecomponentsroot directory:


```
/**
 * WordPress dependencies
 */
import { Button } from '@wordpress/components';

export default function MyButton() {
    return <Button>Click Me!</Button>;
}

```


Many components include CSS to add styles, which you will need to load in order for them to appear correctly. Within WordPress, add thewp-componentsstylesheet as a dependency of your plugin’s stylesheet. Seewp_enqueue_style documentationfor how to specify dependencies.


In non-WordPress projects, link to thebuild-style/style.cssfile directly, it is located atnode_modules/@wordpress/components/build-style/style.css.


### Popovers


By default, thePopovercomponent will render within an extra element appended to the body of the document.


If you want to precisely control where the popovers render, you will need to use thePopover.Slotcomponent.


The following example illustrates how you can wrap a component using aPopoverand have those popovers render to a single location in the DOM.


```
/**
 * External dependencies
 */
import { Popover, SlotFillProvider } from '@wordpress/components';

/**
 * Internal dependencies
 */
import { MyComponentWithPopover } from './my-component';

const Example = () => {
    <SlotFillProvider>
        <MyComponentWithPopover />
        <Popover.Slot />
    </SlotFillProvider>;
};

```


### TypeScript


This package exposes its own types for the components it exports, however it doesn’t export its own types for component props. If you need to extract the props type, please useReact.ComponentPropsto get the types from the element.


```
import type { ComponentProps } from 'react';
import { Button } from '@wordpress/components';

export default function MyButton( props: ComponentProps< typeof Button > ) {
    return <Button { ...props }>Click Me!</Button>;
}

```


## Docs & examples


You can browse the components docs and examples athttps://wordpress.github.io/gutenberg/


## Contributing to this package


This is an individual package that’s part of the Gutenberg project. The project is organized as a monorepo. It’s made up of multiple self-contained software packages, each with a specific purpose. The packages in this monorepo are published tonpmand used byWordPressas well as other software projects.


To find out more about contributing to this package or Gutenberg as a whole, please read the project’s maincontributor guide.


This package also has its owncontributing informationwhere you can find additional details.





First published


March 9, 2021


Last updated


December 8, 2025


Edit article


Improve it on GitHub: Component Reference





[PreviousAvailable Styles OptionsPrevious: Available Styles Options](https://developer.wordpress.org/block-editor/reference-guides/theme-json-reference/styles-versions/)
[NextBaseFieldNext: BaseField](https://developer.wordpress.org/block-editor/reference-guides/components/base-field/)


