# Including Assets

**Source:** [https://developer.wordpress.org/themes/core-concepts/including-assets/](https://developer.wordpress.org/themes/core-concepts/including-assets/)

## In this article

Table of Contents- URL and directory path functions

- Including CSSFront-end stylesheetsInline stylesEditor stylesheetsBlock stylesheets

- Including JavaScriptFront-end JavaScriptInline JavaScriptEditor JavaScriptDefault WordPress scripts

- Including images

- Including fonts

↑Back to top

Many block themes do not need to load any assets. For design aspects, specifically, much of this can be handled through theGlobal Settings and Stylessystem. But there are times when you might need to include a CSS stylesheet, custom JavaScript file, or even other types of media.

If you are familiar with HTML, you might be accustomed to including CSS stylesheets via the<link rel=”stylesheet”/>or<style>tags. The same might be true for including JavaScript via the<script>tag. But you should never manually hard code these HTML elements in your theme.

WordPress has specific hooks for determining when to load scripts/styles and functions for generating the markup. This ensures that WordPress, any active plugins, and your theme all play nicely together.

In this document, you will learn the necessary functions for generating the proper URL to point to asset files and how to include scripts, styles, and other assets in your theme.

This documentation is a leap forward in comparison to some of the previous pages in the Core Concepts chapter. You will need some baseline PHP and HTML knowledge to follow along. You must also understand how to use yourtheme’sfunctions.phpfile. This is necessary for loading CSS stylesheet and JavaScript files.

## URL and directory path functions

Before including assets, you should become familiar with some of the utility functions that WordPress provides for getting URLs and directory paths within a theme. You should always use these helper functions when including any type of asset to ensure the URL or path is correct.

Three of the primary URL helper functions are:

- get_stylesheet_uri(): Returns the active theme’sstyle.cssfile URL.

- get_theme_file_uri( $file ): Returns the active theme’s URL, with an optional$fileparameter. Falls back to the parent theme if a child theme is active and the file doesn’t exist.

- get_parent_theme_file_uri( $file ): Returns the parent theme’s URL, with an optional$filepath.

For directory paths, which are needed less often for assets, there are two primary functions:

- get_theme_file_path( $file ): Returns the active theme’s directory path, with an optional$fileparameter. Falls back to the parent theme if a child theme is active and the file doesn’t exist.

- get_parent_theme_file_path( $file ): Returns the parent theme’s directory path, with an optional$fileparameter.

## Including CSS

wp_enqueue_style()is the primary function for enqueueing a stylesheet, which tells WordPress that you want to put it in the queue to load. You would use this function within an action hook callback in yourfunctions.phpfile, which you learned about inCustom Functionality. You’ll learn which action hooks to use for specific scenarios in the next sections.

Take a look at the function signature:

```text
wp_enqueue_style(
    string $handle,
    string $src           = '',
    string[] $deps        = array(),
    string|bool|null $ver = false,
    string $media         = 'all'
);
```text
You can use these parameters:

- $handleis a unique name/ID for the stylesheet and should be prefixed with your theme slug.

- $srcis the file URL of your stylesheet. While it is technically an optional parameter, it is required to actually load a specific stylesheet.

- $depsis an optional array of other stylesheet handles that your stylesheet is dependent upon.

- $versets the version number of your stylesheet and is used for cache busting. Defaults to the current WordPress version.

- $mediais for specifying which type of media to load this stylesheet for, such asall(default),screen,print, orhandheld.

If you were enqueuing a stylesheet located at/assets/css/example.cssin your theme, your function call might look like this:

```text
wp_enqueue_style(
    'theme-slug-example',
    get_parent_theme_file_uri( 'assets/css/example.css' ),
    array(),
    wp_get_theme()->get( 'Version' ),
    'all'
);
```text
The above code useswp_get_theme()to grab the theme’s version number for cache busting, but you can leave it at the default or use something custom altogether.

### Front-end stylesheets

When loading stylesheets on the front end of a website, you will use thewp_enqueue_scriptshook for most scenarios.

Let’s assume that you wanted to load your theme’sstyle.cssfile using theget_stylesheet_uri()function. You would do this by adding the following code to yourfunctions.phpfile:

```text
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_styles' );

function theme_slug_enqueue_styles() {
    wp_enqueue_style(
        'theme-slug-style',
        get_stylesheet_uri()
    );
}
```text
Remember that you can also pass other parameters to thewp_enqueue_style()function if needed. The above code is the minimum needed to load the stylesheet.

Let’s further suppose that you wanted to load a second stylesheet located at/assets/css/primary.cssin your theme. For this, you would use theget_parent_theme_file_uri()function to get the correct URL.

Here is what your code would look like with both stylesheets enqueued:

```text
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_styles' );

function theme_slug_enqueue_styles() {
    wp_enqueue_style(
        'theme-slug-style',
        get_stylesheet_uri()
    );

    wp_enqueue_style(
        'theme-slug-primary',
        get_parent_theme_file_uri( 'assets/css/primary.css' )
    );
}
```text
### Inline styles

There are times when you might need to add some inline CSS to the<head>area on the front end. WordPress has thewp_add_inline_style()function for this specific scenario.

Here is a look at the function signature:

```text
wp_add_inline_style(
    string $handle,
    string $data
);
```text
In this case, you must pass in a$handleparameter that matches a handle of an existing stylesheet that is enqueued for the page. The$dataparameter is your custom CSS code.

Let’s extend the code from the previous section by adding a small bit of CSS that sets the body background color to a light gray:

```text
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_styles' );

function theme_slug_enqueue_styles() {
    wp_enqueue_style(
        'theme-slug-style',
        get_stylesheet_uri()
    );

    wp_enqueue_style(
        'theme-slug-primary',
        get_parent_theme_file_uri( 'assets/css/primary.css' )
    );

    wp_add_inline_style(
        'theme-slug-primary',
        'body { background: #eee; }'
    );
}
```text
In thewp_add_inline_style()function call, the code uses the existingtheme-slug-primaryhandle to attach an inline style.

### Editor stylesheets

When creating a theme with custom CSS on the front end, you will almost always want your custom styles to also appear in the editor. This will create a consistent user experience across the site. But WordPress does not automatically load your front-end stylesheets in the editor.

For that, you will need to use theadd_editor_style()function:

```text
add_editor_style( array|string $stylesheet = 'editor-style.css' );
```text
It accepts a single parameter of$stylesheet, which can be a single stylesheet filename or an array of filenames. These can be relative to the theme folder or a full URL.

Note that when using relative URLs, a file in the child theme with the same filename will take priority. That’s why it’s generally best practice to use the full stylesheet URL.

This code snippet shows how to add the active theme’s mainstyle.cssfile as an editor style:

```text
add_action( 'after_setup_theme', 'theme_slug_setup' );

function theme_slug_setup() {
    add_editor_style( get_stylesheet_uri() );
}
```text
If you wanted to add both thestyle.cssfile andprimary.cssfrom the earlier examples, you could pass them in as an array:

```text
add_action( 'after_setup_theme', 'theme_slug_setup' );

function theme_slug_setup() {
    add_editor_style( array(
        get_stylesheet_uri(),
        get_parent_theme_file_uri( 'assets/css/primary.css' )
    ) );
}
```text
### Block stylesheets

WordPress also includes awp_enqueue_block_style()function for loading per-block stylesheets in the editor and on the front end. This is covered in full detail in theBlock Stylesheetsdocumentation.

For an advanced exploration of block stylesheets, readLeveraging theme.json and per-block styles for more performant themeson the WordPress Developer Blog.

## Including JavaScript

Like stylesheets, WordPress has a primary function for enqueueing JavaScript files:wp_enqueue_script(). You would also use this function within an action hook callback in yourfunctions.phpfile, and you’ll learn which hooks to use in the following sections.

Take a look at the function signature:

```text
wp_enqueue_script(
    string $handle,
    string $src           = '',
    string[] $deps        = array(),
    string|bool|null $ver = false,
    array|bool $in_footer = false
);
```text
You can use these parameters:

- $handle:A unique name/ID for the script and should be prefixed with your theme slug.

- $src:The file URL of your script. While it is technically an optional parameter, it is required to actually load a specific script

- $deps:An optional array of other script handles that your script is dependent upon.

- $ver:Sets the version number of your script and is used for cache busting. Defaults to the current WordPress version.

- $in_footer:Determines whether to load the script in the header or footer. As of WordPress 6.3, this parameter accepts an array of values:strategy:Accepts either'defer'(default) or'async'to set the script-loading strategy.in_footer:A boolean value to determine whether to load the script in the header or footer.

If you were enqueuing a script located at/assets/js/example.jsin your theme, your function call might look like this:

```text
wp_enqueue_script(
    'theme-slug-example',
    get_parent_theme_file_uri( 'assets/js/example.js' ),
    array(),
    wp_get_theme()->get( 'Version' ),
    true
);
```text
### Front-end JavaScript

When loading stylesheets on the front end of a website, you will use thewp_enqueue_scriptshook for most scenarios.

Suppose you had a custom navigation script located atassets/js/navigations.jsin your theme. For this, you would use theget_parent_theme_file_uri()function to get the correct URL.

Here is what your function would look like when enqueueing the script:

```text
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_scripts' );

function theme_slug_enqueue_scripts() {
    wp_enqueue_script(
        'theme-slug-navigation',
        get_parent_theme_file_uri( 'assets/js/navigation.js' ),
        array(),
        wp_get_theme()->get( 'Version' ),
        true
    );
}
```text
### Inline JavaScript

Sometimes you might want to add some inline JavaScript to the<head>area on the front end. WordPress has thewp_add_inline_script()function for this purpose.

Take a look at the function signature:

```text
wp_add_inline_script(
    string $handle,
    string $data,
    string $position = 'after'
);
```text
Like its counterpart for styles, you must attach this to an enqueued script via the$handleparameter. The secondary parameter,$data, should be the JavaScript code itself. The difference here is the addition of a third parameter,$position, which lets you position the inline script before or after the script that it is attached to.

The following code builds on top of the navigation script from the previous section by adding an inline script to it:

```text
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_scripts' );

function theme_slug_enqueue_scripts() {
    wp_enqueue_script(
        'theme-slug-navigation',
        get_parent_theme_file_uri( 'assets/js/navigation.js' ),
        array(),
        wp_get_theme()->get( 'Version' ),
        true
    );

    wp_add_inline_script(
        'theme-slug-navigation',
        'console.log( "Testing" );'
    );
}
```text
In thewp_add_inline_script()function call, the code uses the existingtheme-slug-navigationhandle to attach the inline style.

### Editor JavaScript

When you need to load a JavaScript file for the block editor, you must use theenqueue_block_editor_assetshook. Note that this is for loading scripts on the admin page itself and not within the content iframe.

Suppose you had anassets/js/editor.jsfile that you needed to load for the editor. Your code should look like this:

```text
add_action( 'enqueue_block_editor_assets', 'theme_slug_enqueue_editor_scripts' );

function theme_slug_enqueue_editor_scripts() {
    wp_enqueue_script(
        'theme-slug-editor',
        get_parent_theme_file_uri( 'assets/js/editor.js' ),
        array(),
        wp_get_theme()->get( 'Version' ),
        true
    );
}
```text
Generally, themes wouldn’t need to load JavaScript for the editor itself. But for advanced use cases, it may be necessary. It is also recommended to integrate with the@wordpress/scriptspackage for easier management. For more information on how to do this, readBeyond block styles, part 1: using the WordPress scripts package with themes.

### Default WordPress scripts

WordPress bundles many custom and third-party scripts. You should always use these scripts if you need one of them instead of loading a custom version. This ensures that you avoid conflicts with plugins.

Some of the scripts are referenced in thewp_enqueue_script()documentation, but that list may not always be up to date. You can find the full list of included files inwp-includes/script-loader.php.

## Including images

Block themes will not often need to include images, except in patterns. You will learn more about these in theBlock Patternsdocumentation. But for a quick overview, let’s take a look at how to reference an image in your theme.

Assuming you had an image file located atassets/img/example.webp, you would use this code to reference the correct URL:

```text
<img src="<?php echo esc_url( get_parent_theme_file_uri( 'assets/img/example.webp' ) ); ?>" alt="" />
```text
Note that the above example usesget_parent_theme_file_uri(). In most cases, this will be the correct function.

But if you are building a child theme or a theme where you would like to allow other child theme authors to override the image, you can useget_theme_file_uri()instead:

```text
<img src="<?php echo esc_url( get_theme_file_uri( 'assets/img/example.webp' ) ); ?>" alt="" />
```text
## Including fonts

Typically, you would expect fonts to fall directly under the assets documentation. But WordPress has special methods for loading fonts via thetheme.jsonfile that integrates with the editor. This documentation is under theTypographypage of the Global Settings and Styles chapter.

First published

November 21, 2023

Last updated

December 14, 2023

[PreviousCustom Functionality (functions.php)Previous: Custom Functionality (functions.php)](https://developer.wordpress.org/themes/core-concepts/custom-functionality/)
[NextGlobal Settings and StylesNext: Global Settings and Styles](https://developer.wordpress.org/themes/core-concepts/global-settings-and-styles/)
