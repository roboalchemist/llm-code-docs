# Source: https://symfony.com/doc/8.0/bundles.html

Title: The Bundle System (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/bundles.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/bundles.rst)

Warning

In Symfony versions prior to 4.0, it was recommended to organize your own application code using bundles. This is [no longer recommended](https://symfony.com/doc/current/best_practices.html#best-practice-no-application-bundles) and bundles should only be used to share code and features between multiple applications.

A bundle is similar to a plugin in other software, but even better. The core features of Symfony framework are implemented with bundles (FrameworkBundle, SecurityBundle, DebugBundle, etc.) Bundles are also used to add new features in your application via [third-party bundles](https://github.com/search?q=topic%3Asymfony-bundle&type=Repositories).

Bundles used in your applications must be enabled per [environment](https://symfony.com/doc/current/configuration.html#configuration-environments) in the `config/bundles.php` file:

Tip

In a default Symfony application that uses [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex), bundles are enabled/disabled automatically for you when installing/removing them, so you don't need to look at or edit this `bundles.php` file.

[Creating a Bundle](https://symfony.com/doc/8.0/bundles.html#creating-a-bundle "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

This section creates and enables a new bundle to show that only a few steps are required. The new bundle is called AcmeBlogBundle, where the `Acme` portion is an example name that should be replaced by some "vendor" name that represents you or your organization (e.g. AbcBlogBundle for some company named `Abc`).

Start by creating a new class called `AcmeBlogBundle`:

Warning

If your bundle must be compatible with previous Symfony versions you have to extend from the [Bundle](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Bundle/Bundle.php "Symfony\Component\HttpKernel\Bundle\Bundle") instead.

Tip

The name AcmeBlogBundle follows the standard [Bundle naming conventions](https://symfony.com/doc/current/bundles/best_practices.html#bundles-naming-conventions). You could also choose to shorten the name of the bundle to simply BlogBundle by naming this class BlogBundle (and naming the file `BlogBundle.php`).

This empty class is the only piece you need to create the new bundle. Though commonly empty, this class is powerful and can be used to customize the behavior of the bundle. Now that you've created the bundle, enable it:

And while it doesn't do anything yet, AcmeBlogBundle is now ready to be used.

[Bundle Directory Structure](https://symfony.com/doc/8.0/bundles.html#bundle-directory-structure "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------

The directory structure of a bundle is meant to help to keep code consistent between all Symfony bundles. It follows a set of conventions, but is flexible to be adjusted if needed:

`assets/` Contains the web asset sources like JavaScript and TypeScript files, CSS and Sass files, but also images and other assets related to the bundle that are not in `public/` (e.g. Stimulus controllers). `config/` Houses configuration, including routing configuration (e.g. `routes.php`). `public/` Contains web assets (images, compiled CSS and JavaScript files, etc.) and is copied or symbolically linked into the project `public/` directory via the `assets:install` console command. `src/` Contains all PHP classes related to the bundle logic (e.g. `Controller/CategoryController.php`). `templates/` Holds templates organized by controller name (e.g. `category/show.html.twig`). `tests/` Holds all tests for the bundle. `translations/` Holds translations organized by domain and locale (e.g. `AcmeBlogBundle.en.xlf`).

Tip

It's recommended to use the [PSR-4](https://www.php-fig.org/psr/psr-4/) autoload standard on your bundle's `composer.json` file. Use the namespace as key, and the location of the bundle's main class (relative to `composer.json`) as value. As the main class is located in the `src/` directory of the bundle:

[Developing a Reusable Bundle](https://symfony.com/doc/8.0/bundles.html#developing-a-reusable-bundle "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------

Bundles are meant to be reusable pieces of code that live independently from any particular Symfony application. However, a bundle cannot run on its own: it must be registered inside an application to execute its code.

This can be a bit challenging during development. When working on a bundle in its own repository, there's no Symfony application around it, so you need a way to test your changes inside a real application environment.

There are two common approaches to do this, depending on whether your bundle has already been published or is still under development.

### [Using a Local Path Repository](https://symfony.com/doc/8.0/bundles.html#using-a-local-path-repository "Permalink to this headline")

If your bundle hasn't been published yet (for example, it's not available on Packagist), you can point Composer to your local bundle directory from any Symfony application you use for testing.

Edit the `composer.json` file of your application and add this:

Then, in your application, install the bundle as usual:

Composer will create a symbolic link (symlink) to your local bundle directory, so any change you make in the `AcmeBlogBundle/` directory is immediately visible in the application. You can now enable the bundle in `config/bundles.php`:

This setup is ideal during early development because it allows quick iteration without publishing or rebuilding archives.

### [Linking an Already Published Bundle](https://symfony.com/doc/8.0/bundles.html#linking-an-already-published-bundle "Permalink to this headline")

If your bundle is already public (for example, it's published on Packagist), you can still develop it locally while testing it inside a Symfony application.

In your application, replace the installed bundle with a symlink to your local development copy. For example, if your bundle is installed under `vendor/acme/blog-bundle/` and your local copy is in `~/Projects/AcmeBlogBundle/`:

Symfony will now use your local bundle directly. You can edit its code, run tests, and see the changes immediately. When you're done, restore the vendor folder or reinstall the package with Composer to go back to the published version.

[Learn more](https://symfony.com/doc/8.0/bundles.html#learn-more "Permalink to this headline")
----------------------------------------------------------------------------------------------

* [How to Override any Part of a Bundle](https://symfony.com/doc/current/bundles/override.html)
* [Best Practices for Reusable Bundles](https://symfony.com/doc/current/bundles/best_practices.html)
* [How to Create Friendly Configuration for a Bundle](https://symfony.com/doc/current/bundles/configuration.html)
* [How to Load Service Configuration inside a Bundle](https://symfony.com/doc/current/bundles/extension.html)
* [How to Simplify Configuration of Multiple Bundles](https://symfony.com/doc/current/bundles/prepend_extension.html)

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
