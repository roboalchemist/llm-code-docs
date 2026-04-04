# Source: https://symfony.com/doc/8.0/performance.html

Title: Performance (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/performance.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/performance.rst)

Symfony is fast. However, you can make it faster if you optimize your servers and your applications as explained in the following performance checklists.

[Performance Checklists](https://symfony.com/doc/8.0/performance.html#performance-checklists "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------

Use these checklists to verify that your application and server are configured for maximum performance:

* **Symfony Application Checklist**:

    1. [Restrict the number of locales enabled in the application](https://symfony.com/doc/current/performance.html#performance-enabled-locales)

* **Production Server Checklist**:

    1. [Dump the service container into a single file](https://symfony.com/doc/current/performance.html#performance-service-container-single-file)
    2. [Use the OPcache bytecode cache](https://symfony.com/doc/current/performance.html#performance-use-opcache)
    3. [Configure OPcache for maximum performance](https://symfony.com/doc/current/performance.html#performance-configure-opcache)
    4. [Don't check PHP files timestamps](https://symfony.com/doc/current/performance.html#performance-dont-check-timestamps)
    5. [Configure the PHP realpath Cache](https://symfony.com/doc/current/performance.html#performance-configure-realpath-cache)
    6. [Optimize Composer Autoloader](https://symfony.com/doc/current/performance.html#performance-optimize-composer-autoloader)

### [Dump the Service Container into a Single File](https://symfony.com/doc/8.0/performance.html#dump-the-service-container-into-a-single-file "Permalink to this headline")

Symfony compiles the [service container](https://symfony.com/doc/current/service_container.html) into multiple small files by default. Set this parameter to `true` to compile the entire container into a single file, which could improve performance when using PHP [class preloading](https://php.net/opcache.preloading.php):

Tip

The `.` prefix denotes a parameter that is only used during compilation of the container. See [Configuration Parameters](https://symfony.com/doc/current/configuration.html#configuration-parameters) for more details.

### [Use the OPcache Bytecode Cache](https://symfony.com/doc/8.0/performance.html#use-the-opcache-bytecode-cache "Permalink to this headline")

OPcache caches the compiled bytecode of PHP scripts to avoid recompiling them on each request. PHP ships with [OPcache](https://php.net/book.opcache.php), but depending on your setup, you may need to enable it explicitly.

### [Use the OPcache class preloading](https://symfony.com/doc/8.0/performance.html#use-the-opcache-class-preloading "Permalink to this headline")

OPcache can compile and load classes at start-up and make them available to all requests until the server is restarted, improving performance significantly.

During container compilation (e.g. when running the `cache:clear` command), Symfony generates a file with the list of classes to preload in the `var/cache/` directory. Rather than use this file directly, use the `config/preload.php` file that is created when [using Symfony Flex in your project](https://symfony.com/doc/current/setup/flex.html):

If this file is missing, run this command to update the Symfony Flex recipe: `composer recipes:update symfony/framework-bundle`.

Use the [container.preload](https://symfony.com/doc/current/reference/dic_tags.html#dic-tags-container-preload) and [container.no_preload](https://symfony.com/doc/current/reference/dic_tags.html#dic-tags-container-nopreload) service tags to define which classes should or should not be preloaded by PHP.

### [Configure OPcache for Maximum Performance](https://symfony.com/doc/8.0/performance.html#configure-opcache-for-maximum-performance "Permalink to this headline")

The default OPcache configuration is not suited for Symfony applications, so it's recommended to change these settings as follows:

### [Don't Check PHP Files Timestamps](https://symfony.com/doc/8.0/performance.html#don-t-check-php-files-timestamps "Permalink to this headline")

In production servers, PHP files should never change, unless a new application version is deployed. However, by default OPcache checks if cached files have changed their contents since they were cached. This check introduces some overhead that can be avoided as follows:

After each deployment, you must empty and regenerate the cache of OPcache. Otherwise you won't see the updates made in the application. Given that in PHP, the CLI and the web processes don't share the same OPcache, you cannot clear the web server OPcache by executing some command in your terminal. These are some of the possible solutions:

1. Restart the web server;
2. Call the `opcache_reset()` function via the web server (i.e. by having these in a script that you execute over the web);
3. Use the [cachetool](https://github.com/gordalina/cachetool) utility to control OPcache from the CLI.

### [Configure the PHP `realpath` Cache](https://symfony.com/doc/8.0/performance.html#configure-the-php-realpath-cache "Permalink to this headline")

When a relative path is transformed into its real and absolute path, PHP caches the result to improve performance. Applications that open many PHP files, such as Symfony projects, should use at least these values:

Note

PHP disables the `realpath` cache when the [open_basedir](https://www.php.net/manual/ini.core.php#ini.open-basedir) config option is enabled.

### [Optimize Composer Autoloader](https://symfony.com/doc/8.0/performance.html#optimize-composer-autoloader "Permalink to this headline")

The class loader used while developing the application is optimized to find new and changed classes. In production servers, PHP files should never change, unless a new application version is deployed. That's why you can optimize Composer's autoloader to scan the entire application once and build an optimized "class map", which is a big array of the locations of all the classes and it's stored in `vendor/composer/autoload_classmap.php`.

Execute this command to generate the new class map (and make it part of your deployment process too):

* `--no-dev` excludes the classes that are only needed in the development environment (i.e. `require-dev` dependencies and `autoload-dev` rules);
* `--classmap-authoritative` creates a class map for PSR-0 and PSR-4 compatible classes used in your application and prevents Composer from scanning the file system for classes that are not found in the class map. (see: [Composer's autoloader optimization](https://getcomposer.org/doc/articles/autoloader-optimization.md)).

### [Disable Dumping the Container as XML in Debug Mode](https://symfony.com/doc/8.0/performance.html#disable-dumping-the-container-as-xml-in-debug-mode "Permalink to this headline")

In [debug mode](https://symfony.com/doc/current/configuration/front_controllers_and_kernel.html#debug-mode), Symfony generates an XML file with all the [service container](https://symfony.com/doc/current/service_container.html) information (services, arguments, etc.) This XML file is used by various debugging commands such as `debug:container` and `debug:autowiring`.

When the container grows larger and larger, so does the size of the file and the time to generate it. If the benefit of this XML file does not outweigh the decrease in performance, you can stop generating the file as follows:

[Profiling Symfony Applications](https://symfony.com/doc/8.0/performance.html#profiling-symfony-applications "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

### [Profiling with Blackfire](https://symfony.com/doc/8.0/performance.html#profiling-with-blackfire "Permalink to this headline")

[Blackfire](https://blackfire.io/docs/introduction?utm_source=symfony&utm_medium=symfonycom_docs&utm_campaign=performance) is the best tool to profile and optimize performance of Symfony applications during development, test and production. It's a commercial service, but provides a [full-featured demo](https://demo.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_docs&utm_campaign=performance).

### [Profiling with Symfony Stopwatch](https://symfony.com/doc/8.0/performance.html#profiling-with-symfony-stopwatch "Permalink to this headline")

Symfony provides a basic performance profiler in the development [config environment](https://symfony.com/doc/current/configuration.html#configuration-environments). Click on the "time panel" of the [web debug toolbar](https://symfony.com/doc/current/page_creation.html#web-debug-toolbar) to see how much time Symfony spent on tasks such as making database queries and rendering templates.

You can measure the execution time and memory consumption of your own code and display the result in the Symfony profiler thanks to the [Stopwatch component](https://symfony.com/components/Stopwatch).

When using [autowiring](https://symfony.com/doc/current/service_container.html#services-autowire), type-hint any controller or service argument with the [Stopwatch](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Stopwatch/Stopwatch.php "Symfony\Component\Stopwatch\Stopwatch") class and Symfony will inject the `debug.stopwatch` service:

If the request calls this service during its execution, you'll see a new event called `export-data` in the Symfony profiler.

The `start()`, `stop()` and `getEvent()` methods return a [StopwatchEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Stopwatch/StopwatchEvent.php "Symfony\Component\Stopwatch\StopwatchEvent") object that provides information about the current event, even while it's still running. This object can be converted to a string for a quick summary:

You can also profile your template code with the [stopwatch Twig tag](https://symfony.com/doc/current/reference/twig_reference.html#reference-twig-tag-stopwatch):

#### [Profiling Categories](https://symfony.com/doc/8.0/performance.html#profiling-categories "Permalink to this headline")

Use the second optional argument of the `start()` method to define the category or tag of the event. This helps keep events organized by type:

#### [Profiling Periods](https://symfony.com/doc/8.0/performance.html#profiling-periods "Permalink to this headline")

A [real-world stopwatch](https://en.wikipedia.org/wiki/Stopwatch) not only includes the start/stop button but also a "lap button" to measure each partial lap. This is exactly what the `lap()` method does, which stops an event and then restarts it immediately:

#### [Profiling Sections](https://symfony.com/doc/8.0/performance.html#profiling-sections "Permalink to this headline")

Sections are a way to split the profile timeline into groups. Example:

All events that don't belong to any named section are added to the special section called `__root__`. This way you can get all stopwatch events, even if you don't know their names, as follows:

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
