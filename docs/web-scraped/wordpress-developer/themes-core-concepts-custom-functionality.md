# Custom Functionality (functions.php)

**Source:** [https://developer.wordpress.org/themes/core-concepts/custom-functionality/](https://developer.wordpress.org/themes/core-concepts/custom-functionality/)



# Custom Functionality (functions.php)




## In this article


Table of Contents- What is functions.php?
- Common uses for functions.phpAdding actions or filters to hooksTheme setup functionLoading scripts and styles
- Including other PHP files
- Avoid closing ?> tags at the end of files



↑Back to top



This document will introduce you to thefunctions.phpfile. It is one of the optional standard files you first learned about inTheme Structure. Both block and classic themes can utilize it.


The following will introduce you to the core concepts around using PHP withinfunctions.php, but it will not teach you the PHP programming language itself. You can visit the officialPHP documentationfor more information on how to write your own PHP code.


Throughout the handbook, you will encounter more examples where you will add custom functionality, so getting the basics down is important. You can jump into more advanced PHP examples in theFeatures,Advanced Topics, andClassic Themeschapters.


## What is functions.php?


Thefunctions.phpessentially acts like a WordPress plugin, letting you add custom PHP functions, classes, interfaces, and more. It opens up the entirety of the PHP programming language to your theme.


WordPress automatically loads thefunctions.phpfile (if it exists) as soon as it loads the theme on all page views on both the admin and front-end of the website. So it provides you with a lot of power to build unique features around WordPress.


Just because youcanbuild plugin-like features in a theme doesn’t mean you always should, particularly if you are distributing your theme to others to use. If you are creating features that should be available regardless of the site’s design,it is best practice to put the code in a plugin. The rule of thumb is that themes should only deal with the site’s design.


While all themes can have a customfunctions.phpfile, WordPress will only load the currently active theme’s.


The only caveat to that rule is when a child theme is active. In that case, WordPress loads the child theme’sfunctions.phpjust before loading the parent theme’sfunctions.php. You can learn more aboutchild themesin the Advanced Topics chapter.


## Common uses for functions.php


Because thefunctions.phpfile lets you write any PHP, you will often see themes with wildly different code, organizational systems, naming conventions, and more. The deeper your understanding of PHP, the easier it will be to follow the code from other themes.


The following are some uses you will often find in a theme’sfunctions.phpfile.


### Adding actions or filters to hooks


Hooks are the entry point to extending WordPress’ functionality, providing you with a way to inject custom code or filter data. Think of them as a way for themes (and plugins) to communicate directly with WordPress.


WordPress’ hooks system offers two different methods for executing your code during the page loading process:


- Action hooksallow you to run a custom action callback and “act on” the information that it receives.
- Filter hookslet you filter data via a custom filter callback and manipulate it.


Technically, hooks are a part of the Plugin API, and you canread the documentationon them in the Plugin Handbook.


Despite being in the Plugin API, hooks are also extremely useful in the context of themes. Like plugins, you should always run your code on a hook so that it performs its functionality at the appropriate point in the load process.


Throughout this handbook, you will see examples of adding features or functionality fromfunctions.php, and these examples will always use a hook. Familiarizing yourself with their documentation will make it easier to understand PHP code in the handbook.


### Theme setup function


One common use case for many themes is adding a setup function, which is generally used to register theme-supported features with WordPress. This is almost always executed on theafter_setup_themeaction hook, which is the first hook available after a theme’sfunctions.phpfile has been loaded.


To test this, open your theme’sfunctions.phpfile (create one if it doesn’t exist), and add the following PHP code:


```
<?php
add_action( 'after_setup_theme', 'theme_slug_setup' );

function theme_slug_setup() {
	add_theme_support( 'wp-block-styles' );
}
```


This code adds support for WordPress’ more-opinionated block styles to your theme. You do not have to use this; it is merely serving as an example of what a setup function might look like.


Setup functions are more common in classic themes. When using a block theme, the theme is often automatically opted into the features needed. You can find a list of theme-supported features here:


- Function Reference:add_theme_support()
- Block Editor Handbook: Theme Support


### Loading scripts and styles


If you are familiar with HTML, you will likely have come across adding JavaScript via the<script>tag or stylesheets via the<link rel=”stylesheet”/>or<style>tags.


WordPress provides helper functions and specific action hooks for loading scripts and styles. This ensures that they are injected at the appropriate place in the document output. WordPress creates the appropriate HTML markup for you.


You can learn more about loading scripts and styles in theIncluding Assetsdocumentation.


It is not uncommon when building block themes to have no need of including additional scripts/styles. Some themes rely entirely onGlobal Settings and Stylesfor the front-end design.


## Including other PHP files


WordPress will automatically load your theme’sfunctions.phpfor you, but you are not limited to only adding custom PHP code in that file. You can load other files with PHP interfaces, classes, traits, and functions from elsewhere in your theme.


As you learned inTheme Structure, some themes include a custom folder named/inc(or any custom folder) to store custom PHP files. Let’s assume you had an/inc/helpers.phpfile for custom helper functions, you could load it viafunctions.phpusing theget_parent_theme_file_path()function:


```
include get_parent_theme_file_path( 'inc/helpers.php' );
```


Generally speaking, you should use this function to get the correct directory path to any PHP file you need to load.


Alternatively, if you wanted to allow a child theme to override the file with a fallback to the parent theme, you could useget_theme_file_path()instead:


```
include get_theme_file_path( 'inc/helpers.php' );
```


It’s not standard practice to let child theme’s override files with PHP functions or classes, but there are use cases where it’s needed.


## Avoid closing ?> tags at the end of files


This section could otherwise be titled “How to avoid the dreaded WordPresswhite screen of death.”


There are various reasons that you might see a broken site with nothing but a white screen. One of those reasons is when thefunctions.phpfile (or any PHP file) has whitespace following its closing?>tag like this:


```
<?php
// some code...
?>
 
```


Many editor configurations will automatically add an extra line at the end of files (a common development practice). When you add a closing?>tag at the end of the file, it can be easy to miss this extra whitespace, which may cause the “white screen of death” in some environments.


The easiest way to avoid this issue is to leave the closing?>tag out altogether, which is perfectly valid PHP and standard practice. The above code should be written as:


```
<?php
// some code...
 
```





First published


November 21, 2023


Last updated


December 16, 2023



[PreviousTemplatesPrevious: Templates](https://developer.wordpress.org/themes/core-concepts/templates/)
[NextIncluding AssetsNext: Including Assets](https://developer.wordpress.org/themes/core-concepts/including-assets/)


