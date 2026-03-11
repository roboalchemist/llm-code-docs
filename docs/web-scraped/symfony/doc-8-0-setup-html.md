# Source: https://symfony.com/doc/8.0/setup.html

Title: Installing & Setting up the Symfony Framework (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/setup.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/setup.rst)

[Technical Requirements](https://symfony.com/doc/8.0/setup.html#technical-requirements "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

Before creating your first Symfony application you must:

* Install PHP 8.4 or higher and these PHP extensions (which are installed and enabled by default in most PHP 8 installations): [Ctype](https://www.php.net/book.ctype), [iconv](https://www.php.net/book.iconv), [PCRE](https://www.php.net/book.pcre), [Session](https://www.php.net/book.session), [SimpleXML](https://www.php.net/book.simplexml), and [Tokenizer](https://www.php.net/book.tokenizer);
* [Install Composer](https://getcomposer.org/download/), which is used to install PHP packages.

Also, [install the Symfony CLI](https://symfony.com/download). This is optional, but it gives you a helpful binary called `symfony` that provides all tools you need to develop and run your Symfony application locally.

The `symfony` binary also provides a tool to check if your computer meets all requirements. Open your console terminal and run this command:

[Creating Symfony Applications](https://symfony.com/doc/8.0/setup.html#creating-symfony-applications "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------

Open your console terminal and run any of these commands to create a new Symfony application:

The only difference between these two commands is the number of packages installed by default. The `--webapp` option installs extra packages to give you everything you need to build a web application.

If you're not using the Symfony binary, run these commands to create the new Symfony application using Composer:

No matter which command you run to create the Symfony application. All of them will create a new `my_project_directory/` directory, download some dependencies into it and even generate the basic directories and files you'll need to get started. In other words, your new application is ready!

Note

The project's cache and logs directory (by default, `<project>/var/cache/` and `<project>/var/log/`) must be writable by the web server. If you have any issue, read how to [set up permissions for Symfony applications](https://symfony.com/doc/current/setup/file_permissions.html).

[Setting up an Existing Symfony Project](https://symfony.com/doc/8.0/setup.html#setting-up-an-existing-symfony-project "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------

In addition to creating new Symfony projects, you will also work on projects already created by other developers. In that case, you only need to get the project code and install the dependencies with Composer. Assuming your team uses Git, setup your project with the following commands:

You'll probably also need to customize your [.env file](https://symfony.com/doc/current/configuration.html#config-dot-env) and do a few other project-specific tasks (e.g. creating a database). When working on an existing Symfony application for the first time, it may be useful to run this command which displays information about the project:

[Running Symfony Applications](https://symfony.com/doc/8.0/setup.html#running-symfony-applications "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

In production, you should install a web server like Nginx or Apache and [configure it to run Symfony](https://symfony.com/doc/current/setup/web_server_configuration.html). This method can also be used if you're not using the Symfony local web server for development.

However for local development, the most convenient way of running Symfony is by using the [local web server](https://symfony.com/doc/current/setup/symfony_cli.html#symfony-cli-server) provided by the Symfony CLI tool. This local server provides among other things support for HTTP/2, concurrent requests, TLS/SSL and automatic generation of security certificates.

Open your console terminal, move into your new project directory and start the local web server as follows:

Open your browser and navigate to `http://localhost:8000/`. If everything is working, you'll see a welcome page. Later, when you are finished working, stop the server by pressing `Ctrl+C` from your terminal.

Tip

The web server works with any PHP application, not only Symfony projects, so it's a very useful generic development tool.

[Installing Packages](https://symfony.com/doc/8.0/setup.html#installing-packages "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

A common practice when developing Symfony applications is to install packages (Symfony calls them [bundles](https://symfony.com/doc/current/bundles.html)) that provide ready-to-use features. Packages usually require some setup before using them (editing some file to enable the bundle, creating some file to add some initial config, etc.)

Most of the time this setup can be automated and that's why Symfony includes [Symfony Flex](https://github.com/symfony/flex), a tool to simplify the installation/removal of packages in Symfony applications. Technically speaking, Symfony Flex is a Composer plugin that is installed by default when creating a new Symfony application and which **automates the most common tasks of Symfony applications**.

Symfony Flex modifies the behavior of the `require`, `update`, and `remove` Composer commands to provide advanced features. Consider the following example:

If you run that command in a Symfony application which doesn't use Flex, you'll see a Composer error explaining that `logger` is not a valid package name. However, if the application has Symfony Flex installed, that command installs and enables all the packages needed to use the official Symfony logger.

This is possible because lots of Symfony packages/bundles define **"recipes"**, which are a set of automated instructions to install and enable packages into Symfony applications. Flex keeps track of the recipes it installed in a `symfony.lock` file, which must be committed to your code repository.

Symfony Flex recipes are contributed by the community and they are stored in two public repositories:

* [Main recipe repository](https://github.com/symfony/recipes), is a curated list of recipes for high quality and maintained packages. Symfony Flex only looks in this repository by default.
* [Contrib recipe repository](https://github.com/symfony/recipes-contrib), contains all the recipes created by the community. All of them are guaranteed to work, but their associated packages could be unmaintained. Symfony Flex will ask your permission before installing any of these recipes.

Read the [Symfony Recipes documentation](https://github.com/symfony/recipes/blob/master/README.rst) to learn everything about how to create recipes for your own packages.

### [Symfony Packs](https://symfony.com/doc/8.0/setup.html#symfony-packs "Permalink to this headline")

Sometimes a single feature requires installing several packages and bundles. Instead of installing them individually, Symfony provides **packs**, which are Composer metapackages that include several dependencies.

For example, to add debugging features in your application, you can run the `composer require --dev debug` command. This installs the `symfony/debug-pack`, which in turn installs several packages like `symfony/debug-bundle`, `symfony/monolog-bundle`, `symfony/var-dumper`, etc.

You won't see the `symfony/debug-pack` dependency in your `composer.json`, as Flex automatically unpacks the pack. This means that it only adds the real packages as dependencies (e.g. you will see a new `symfony/var-dumper` in `require-dev`).

[Checking Security Vulnerabilities](https://symfony.com/doc/8.0/setup.html#checking-security-vulnerabilities "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

The `symfony` binary created when you installed the [Symfony CLI](https://symfony.com/doc/current/setup.html#setup-symfony-cli) provides a command to check whether your project's dependencies contain any known security vulnerability:

A good security practice is to execute this command regularly to be able to update or replace compromised dependencies as soon as possible. The security check is done locally by fetching the public [PHP security advisories database](https://github.com/FriendsOfPHP/security-advisories), so your `composer.lock` file is not sent on the network.

The `check:security` command terminates with a non-zero exit code if any of your dependencies is affected by a known security vulnerability. This way you can add it to your project build process and your continuous integration workflows to make them fail when there are vulnerabilities.

Tip

In continuous integration services you can check security vulnerabilities by running the `composer audit` command. This uses the same data internally as `check:security` but does not require installing the entire Symfony CLI during CI or on CI workers.

[Symfony LTS Versions](https://symfony.com/doc/8.0/setup.html#symfony-lts-versions "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

According to the [Symfony release process](https://symfony.com/doc/current/contributing/community/releases.html), "long-term support" (or LTS for short) versions are published every two years. Check out the [Symfony releases](https://symfony.com/releases) to know which is the latest LTS version.

By default, the command that creates new Symfony applications uses the latest stable version. If you want to use an LTS version, add the `--version` option:

The `lts` and `next` shortcuts are only available when using Symfony to create new projects. If you use Composer, you need to tell the exact version:

[The Symfony Demo application](https://symfony.com/doc/8.0/setup.html#the-symfony-demo-application "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

[The Symfony Demo Application](https://github.com/symfony/demo) is a fully-functional application that shows the recommended way to develop Symfony applications. It's a great learning tool for Symfony newcomers and its code contains tons of comments and helpful notes.

Run this command to create a new project based on the Symfony Demo application:

[Learn More](https://symfony.com/doc/8.0/setup.html#learn-more "Permalink to this headline")
--------------------------------------------------------------------------------------------

* [Using Docker with Symfony](https://symfony.com/doc/current/setup/docker.html)
* [Using Symfony with Homestead/Vagrant](https://symfony.com/doc/current/setup/homestead.html)
* [Configuring a Web Server](https://symfony.com/doc/current/setup/web_server_configuration.html)
* [Upgrading a Third-Party Bundle for a Major Symfony Version](https://symfony.com/doc/current/setup/bundles.html)
* [Setting up or Fixing File Permissions](https://symfony.com/doc/current/setup/file_permissions.html)
* [Upgrading Existing Applications to Symfony Flex](https://symfony.com/doc/current/setup/flex.html)
* [How To Configure and Use Flex Private Recipe Repositories](https://symfony.com/doc/current/setup/flex_private_recipes.html)
* [Symfony CLI](https://symfony.com/doc/current/setup/symfony_cli.html)
* [How to Install or Upgrade to the Latest, Unreleased Symfony Version](https://symfony.com/doc/current/setup/unstable_versions.html)
* [Upgrading a Major Version (e.g. 6.4.0 to 7.0.0)](https://symfony.com/doc/current/setup/upgrade_major.html)
* [Upgrading a Minor Version (e.g. 6.3.0 to 6.4.0)](https://symfony.com/doc/current/setup/upgrade_minor.html)
* [Upgrading a Patch Version (e.g. 6.0.0 to 6.0.1)](https://symfony.com/doc/current/setup/upgrade_patch.html)

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
