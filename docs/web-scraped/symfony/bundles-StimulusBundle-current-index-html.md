# Source: https://symfony.com/bundles/StimulusBundle/current/index.html

Title: StimulusBundle Documentation

URL Source: https://symfony.com/bundles/StimulusBundle/current/index.html

Markdown Content:
StimulusBundle: Symfony integration with Stimulus
-------------------------------------------------

[Edit this page](https://github.com/symfony/stimulus-bundle/edit/2.x/doc/index.rst)

This bundle adds integration between Symfony, [Stimulus](https://stimulus.hotwired.dev/) and the Symfony UX packages:

* Twig `stimulus_` functions & filters to add Stimulus controllers, actions & targets in your templates;
* Integration to load [UX Packages](https://symfony.com/bundles/StimulusBundle/current/index.html#ux-packages) (extra Stimulus controllers)

[Installation](https://symfony.com/bundles/StimulusBundle/current/index.html#installation "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------

First, if you don't have one yet, choose and install an asset handling system; both work great with StimulusBundle:

* [AssetMapper](https://symfony.com/doc/current/frontend/asset_mapper.html): PHP-based system for handling assets

or

* [Webpack Encore](https://symfony.com/doc/current/frontend.html) Node-based packaging system

See [Encore vs AssetMapper](https://symfony.com/doc/current/frontend.html) to learn which is best for your project.

Next, install the bundle:

If you're using [Symfony Flex](https://symfony.com/doc/current/setup/flex.html), you're done! The recipe will update the necessary files. If not, or you're curious, see [Manual Setup](https://symfony.com/bundles/StimulusBundle/current/index.html#manual-installation).

Tip

If you're using Encore, be sure to install your assets (e.g. `npm install`) and restart Encore.

[Usage](https://symfony.com/bundles/StimulusBundle/current/index.html#usage "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

You can now create custom Stimulus controllers inside of the `assets/controllers` directory. In fact, you should have an example controller there already: `hello_controller.js`:

Then, activate the controller in your HTML:

Optionally, this bundle has a Twig function to render the attribute:

That's it! Whenever this element appears on the page, the `hello` controller will activate.

There's a _lot_ more to learn about Stimulus. See the [Stimulus Documentation](https://stimulus.hotwired.dev/) for all the goodies.

### [TypeScript Controllers](https://symfony.com/bundles/StimulusBundle/current/index.html#typescript-controllers "Permalink to this headline")

If you want to use [TypeScript](https://www.typescriptlang.org/) to define your controllers, you can! Install and set up the [sensiolabs/typescript-bundle](https://github.com/sensiolabs/AssetMapperTypeScriptBundle). Then be sure to add the `assets/controllers` path to the `sensiolabs_typescript.source_dir` configuration. Finally, create your controller in that directory and you're good to go.

### [The UX Packages](https://symfony.com/bundles/StimulusBundle/current/index.html#the-ux-packages "Permalink to this headline")

Symfony provides a set of UX packages that add extra Stimulus controllers to solve common problems. StimulusBundle activates any 3rd party Stimulus controllers that are mentioned in your `assets/controllers.json` file. This file is updated whenever you install a UX package.

Check out the [official UX packages](https://ux.symfony.com/packages).

### [Lazy Stimulus Controllers](https://symfony.com/bundles/StimulusBundle/current/index.html#lazy-stimulus-controllers "Permalink to this headline")

By default, all of your controllers (i.e. files in `assets/controllers/` + controllers in `assets/controllers.json`) will be downloaded and loaded on every page.

Sometimes you may have a controller that's only used on some pages. In that case, you can make the controller "lazy". In this case, will _not_ be downloaded on initial page load. Instead, as soon as an element appears on the page matching the controller (e.g. `<div data-controller="hello">`), the controller - and anything else it imports - will be lazily-loaded via Ajax.

To make one of your custom controllers lazy, add a special comment on top:

To make a third-party controller lazy, in `assets/controllers.json`, set `fetch` to `lazy`.

Note

If you write your controllers using TypeScript and you're using StimulusBundle 2.21.0 or earlier, make sure `removeComments` is not set to `true` in your TypeScript config.

[Stimulus Tools around the World](https://symfony.com/bundles/StimulusBundle/current/index.html#stimulus-tools-around-the-world "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Because Stimulus is used by developers outside of Symfony, many tools exist beyond the UX packages:

* [stimulus-use](https://stimulus-use.github.io/stimulus-use): Add composable behaviors to your Stimulus controllers, like debouncing, detecting outside clicks and many other things.
* [stimulus-components](https://www.stimulus-components.com/) A large number of pre-made Stimulus controllers, like for Copying to clipboard, Sortable, Popover (similar to tooltips) and much more.

[Stimulus Twig Helpers](https://symfony.com/bundles/StimulusBundle/current/index.html#stimulus-twig-helpers "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------

This bundle adds some Twig functions/filters to help add Stimulus controllers, actions and targets in your templates.

Note

Though this bundle provides these helpful Twig functions/filters, it's recommended to use raw data attributes instead, as they're straightforward.

Tip

If you use PhpStorm IDE - you may want to install [Stimulus plugin](https://plugins.jetbrains.com/plugin/24562-stimulus) to get nice auto-completion for the attributes.

### [stimulus_controller](https://symfony.com/bundles/StimulusBundle/current/index.html#stimulus-controller "Permalink to this headline")

This bundle ships with a special `stimulus_controller()` Twig function that can be used to render [Stimulus Controllers & Values](https://stimulus.hotwired.dev/reference/values) and [CSS Classes](https://stimulus.hotwired.dev/reference/css-classes). Stimulus Controllers can also reference other controllers by using [Outlets](https://stimulus.hotwired.dev/reference/outlets).

For example:

If you want to set CSS classes:

And with outlets:

Any non-scalar values (like `data: [1, 2, 3, 4]`) are JSON-encoded. And all values are properly escaped (the string `&#x5B;` is an escaped `[` character, so the attribute is really `[1,2,3,4]`).

If you have multiple controllers on the same element, you can chain them as there's also a `stimulus_controller` filter:

You can also retrieve the generated attributes as an array, which can be helpful e.g. for forms:

### [stimulus_action](https://symfony.com/bundles/StimulusBundle/current/index.html#stimulus-action "Permalink to this headline")

The `stimulus_action()` Twig function can be used to render [Stimulus Actions](https://stimulus.hotwired.dev/reference/actions).

For example:

If you have multiple actions and/or methods on the same element, you can chain them as there's also a `stimulus_action` filter:

You can also retrieve the generated attributes as an array, which can be helpful e.g. for forms:

You can also pass [parameters](https://stimulus.hotwired.dev/reference/actions#action-parameters) to actions:

### [stimulus_target](https://symfony.com/bundles/StimulusBundle/current/index.html#stimulus-target "Permalink to this headline")

The `stimulus_target()` Twig function can be used to render [Stimulus Targets](https://stimulus.hotwired.dev/reference/targets).

For example:

If you have multiple targets on the same element, you can chain them as there's also a `stimulus_target` filter:

You can also retrieve the generated attributes as an array, which can be helpful e.g. for forms:

[Configuration](https://symfony.com/bundles/StimulusBundle/current/index.html#configuration "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

If you're using [AssetMapper](https://symfony.com/doc/current/frontend/asset_mapper.html), you can configure the path to your controllers directory and the `controllers.json` file if you need to use different paths:

[Manual Installation Details](https://symfony.com/bundles/StimulusBundle/current/index.html#manual-installation-details "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------

When you install this bundle, its Flex recipe should handle updating all the files needed. If you're not using Flex or want to double-check the changes, check out the [StimulusBundle Flex recipe](https://github.com/symfony/recipes/tree/main/symfony/stimulus-bundle). Here's a summary of what's inside:

* `assets/bootstrap.js` starts the Stimulus application and loads your controllers. It's imported by `assets/app.js` and its exact content depends on whether you have Webpack Encore or AssetMapper installed (see below).
* `assets/app.js` is _updated_ to import `assets/bootstrap.js`
* `assets/controllers.json` This file starts (mostly) empty and is automatically updated as your install UX packages that provide Stimulus controllers.
* `assets/controllers/` This directory is where you should put your custom Stimulus controllers. It comes with one example `hello_controller.js` file.

A few other changes depend on which asset system you're using:

### [With AssetMapper](https://symfony.com/bundles/StimulusBundle/current/index.html#with-assetmapper "Permalink to this headline")

If you're using AssetMapper, two new entries will be added to your `importmap.php` file:

The recipe will update your `assets/bootstrap.js` file to look like this:

The `@symfony/stimulus-bundle` refers the one of the new entries in your `importmap.php` file. This file is dynamically built by the bundle and will import all your custom controllers as well as those from `controllers.json`. It will also dynamically enable "debug" mode in Stimulus when your application is running in debug mode.

Tip

For AssetMapper 6.3 only, you also need a `{{ ux_controller_link_tags() }}` in `base.html.twig`. This is not needed in AssetMapper 6.4+.

### [With WebpackEncoreBundle](https://symfony.com/bundles/StimulusBundle/current/index.html#with-webpackencorebundle "Permalink to this headline")

If you're using Webpack Encore, the recipe will also update your `webpack.config.js` file to include this line:

The `assets/bootstrap.js` file will be updated to look like this:

And 2 new packages - `@hotwired/stimulus` and `@symfony/stimulus-bridge` - will be added to your `package.json` file.

[How are the Stimulus Controllers Loaded?](https://symfony.com/bundles/StimulusBundle/current/index.html#how-are-the-stimulus-controllers-loaded "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you install a UX PHP package, Symfony Flex will automatically update your `package.json` file (not done or needed if using AssetMapper) to point to a "virtual package" that lives inside that PHP package. For example:

This gives you a _real_ Node package (e.g. `@symfony/ux-chartjs`) that, instead of being downloaded, points directly to files that already live in your `vendor/` directory.

The Flex recipe will usually also update your `assets/controllers.json` file to add a new Stimulus controller to your app. For example:

Finally, your `assets/bootstrap.js` file will automatically register:

* All files in `assets/controllers/` as Stimulus controllers;
* And all controllers described in `assets/controllers.json` as Stimulus controllers.

Note

If you're using WebpackEncore, the `bootstrap.js` file works in partnership with [@symfony/stimulus-bridge](https://github.com/symfony/stimulus-bridge). With AssetMapper, the `bootstrap.js` file works directly with this bundle: a `@symfony/stimulus-bundle` entry is added to your `importmap.php` file via Flex, which points to a file that is dynamically built to find and load your controllers (see [Configuration](https://symfony.com/bundles/StimulusBundle/current/index.html#configuration)).

The end result: you install a package, and you instantly have a Stimulus controller available! In this example, it's called `@symfony/ux-chartjs/chart`. Well, technically, it will be called `symfony--ux-chartjs--chart`. However, you can pass the original name into the `{{ stimulus_controller() }}` function from WebpackEncoreBundle, and it will normalize it:

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
