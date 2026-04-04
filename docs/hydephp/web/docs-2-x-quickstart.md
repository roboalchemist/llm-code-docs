# Source: https://hydephp.com/docs/2.x/quickstart

Title: HydePHP - Quickstart Guide

URL Source: https://hydephp.com/docs/2.x/quickstart

Markdown Content:
The recommended method of installing Hyde is using Composer, which installs the required dependencies on a per-project basis.

`composer create-project hyde/hyde`
### Requirements[#](https://hydephp.com/docs/2.x/quickstart#requirements "Permalink")

Hyde is based on [Laravel 11](https://laravel.com/docs/11.x/releases) which requires a minimum PHP version of 8.2. You should also have [Composer](https://getcomposer.org/) installed.

To use some features like [compiling your own assets](https://hydephp.com/docs/2.x/managing-assets) you also need NodeJS and NPM.

The main way to interact with Hyde is through the [HydeCLI](https://hydephp.com/docs/2.x/console-commands), a Laravel Artisan-based command-line interface. Learn more about the HydeCLI in the [console commands](https://hydephp.com/docs/2.x/console-commands) documentation.

To make previewing your site a breeze you can use the realtime compiler, which builds your pages on the fly.

`php hyde serve`
Simply run the serve command, and you will be able to preview your site at [http://localhost:8080](http://localhost:8080/).

Creating Content[#](https://hydephp.com/docs/2.x/quickstart#creating-content "Permalink")
-----------------------------------------------------------------------------------------

### Directory structure[#](https://hydephp.com/docs/2.x/quickstart#directory-structure "Permalink")

Creating content with Hyde is easy! Simply place source files in one of the source directories, and Hyde will automatically discover, parse, and compile them to static HTML. The directory and file extension of a source file will determine how HydePHP parses and compiles it. Please see the [directory structure](https://hydephp.com/docs/2.x/core-concepts#directory-structure) section for more information.

### Scaffolding files[#](https://hydephp.com/docs/2.x/quickstart#scaffolding-files "Permalink")

You can scaffold blog post files using the `php hyde make:post` command which automatically creates the front matter, based on your input selections. You can also scaffold pages with the `php hyde make:page` command.

`php hyde make:postphp hyde make:page`
### Compiling to static HTML[#](https://hydephp.com/docs/2.x/quickstart#compiling-to-static-html "Permalink")

Now that you have some amazing content, you'll want to compile your site into static HTML. Thankfully, this is as easy as executing the `build` command, after which your compiled site is stored in the `_site` directory.

`php hyde build`
When building the site, Hyde will scan your source directories for files and compile them into static HTML using the appropriate layout depending on what kind of page it is. You don't have to worry about routing as Hyde takes care of everything, including creating navigation menus!

### Managing assets[#](https://hydephp.com/docs/2.x/quickstart#managing-assets "Permalink")

Hyde comes bundled with a precompiled and minified `app.css` file, containing all the Tailwind you need for the default views meaning that you don't even need to use NPM. However, Hyde is already configured to use Vite to compile your assets if you feel like there's a need to build the assets yourself. See more on the [Managing Assets](https://hydephp.com/docs/2.x/managing-assets) page.

### Deploying your site[#](https://hydephp.com/docs/2.x/quickstart#deploying-your-site "Permalink")

You are now ready to show your site to the world! Simply copy the `_site` directory to your web server's document root, and you're ready to go.

You can even use GitHub Pages to host your site for free. That's what the Hyde website does, using an Actions CI workflow that automatically builds and deploys this site.

Here's some ideas of what to read next:

*   [Architecture Concepts & Directory Structure](https://hydephp.com/docs/2.x/core-concepts)
*   [Console Commands with the HydeCLI](https://hydephp.com/docs/2.x/console-commands)
*   [Creating Blog Posts](https://hydephp.com/docs/2.x/blog-posts)
