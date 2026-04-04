# Source: https://docs.upsun.com/languages/php.md

# PHP

**Note**: 

You can now use the Upsun [composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) to install runtimes and tools in your application container.
To find out more about this feature, see the [dedicated documentation page](https://docs.upsun.com/create-apps/app-reference/composable-image.md). 
Also, see how you can [modify your PHP runtime when using the composable image](#modify-your-php-runtime-when-using-the-composable-image).

## Supported versions

You can select the major and minor version.

Patch versions are applied periodically for bug fixes and the like. When you deploy your app, you always get the latest available patches.

   - 8.5

   - 8.4

   - 8.3

   - 8.2

Note that from PHP versions 7.1 to 8.1, the images support the Zend Thread Safe (ZTS) version of PHP.

### Specify the language

To use PHP, specify `php` as your [app's `type`](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  <APP_NAME>:
    type: 'php:<VERSION_NUMBER>'
```

For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'
```

### Deprecated versions

The following versions are [deprecated](https://docs.upsun.com/glossary.md#deprecated-versions).
They're available, but they don't receive security updates from upstream and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported version](#supported-versions).

   - 8.1

   - 8.0

   - 7.4

   - 7.3

   - 7.2

   - 7.1

   - 7.0

   - 5.6

   - 5.5

   - 5.4

## Usage example

Configure your app to use PHP on Upsun.

### 1. Specify the version

Choose a [supported version](#supported-versions)
and add it to your [app configuration](https://docs.upsun.com../../create-apps/_index.md):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'
```
### 2. Serve your app

To serve your app, define what (and how) content should be served by setting the [`locations` parameter](https://docs.upsun.com/create-apps/image-properties/web.md#locations).

Usually, it contains the two following (optional) keys:

- `root` for the document root,
  the directory to which all requests for existing `.php` and static files (such as `.css`, `.jpg`) are sent.
- `passthru` to [define a front controller](https://docs.upsun.com../../create-apps/web/php-basic.md#set-different-rules-for-specific-locations) to handle nonexistent files.
  The value is a file path relative to the [app root](https://docs.upsun.com/create-apps/image-properties/source.md).

  **Note**: 

For enhanced security, when setting ``passthru`` to ``true``, you might also want to add the following configuration:

 - Set ``scripts`` to ``false``.
This prevents PHP scripts from being executed from the specified location.

 - Set ``allow`` to ``false``.
By default, when PHP scripts aren’t executed, their source code is delivered.
Setting ``allow`` to ``false`` allows you to keep the source code of your PHP scripts confidential.

Adjust the `locations` block to fit your needs.

In the following example, all requests made to your site's root (`/`) are sent to the `public` directory
and nonexistent files are handled by `app.php`:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'
    web:
      locations:
        '/':
          root: 'public'
          passthru: '/app.php'
```
See how to [create a basic PHP app with a front controller](https://docs.upsun.com../../create-apps/web/php-basic.md).
To have more control, you can define rules to specify which files you want to allow [from which location](https://docs.upsun.com../../create-apps/web/php-basic.md#set-different-rules-for-specific-locations).

### Complete example

A complete basic app configuration looks like the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'
    web:
      locations:
        '/':
          root: 'public'
          passthru: '/app.php'
```
## Dependencies

Up to PHP version 8.1, it's assumed that you're using [Composer](https://getcomposer.org/) 1.x to manage dependencies.
If you have a `composer.json` file in your code, the default [build flavor is run](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#build):

```bash
composer --no-ansi --no-interaction install --no-progress --prefer-dist --optimize-autoloader
```

To use Composer 2.x on your project, either use PHP 8.2+ or, in your app configuration, add the following [dependency](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#dependencies):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    dependencies:
      php:
        composer/composer: '^2'
```
Adding a dependency to the [dependencies block](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#dependencies) makes it available globally.
So you can then use included dependencies as commands within your app container.
You can add multiple global dependencies to the dependencies block, such as [Node.js](https://docs.upsun.com../nodejs.md#2-specify-any-global-dependencies).

If you want to have more control over Composer or if you don't want to use Composer at all, adapt the [build flavor](#change-the-build-flavor).
You can also use a [private, authenticated third-party Composer repository](https://docs.upsun.com/languages/php/composer-auth.md).

### Change the build flavor

If you need more control over the dependency management,
you can either use your custom build flavor
or interact with Composer itself through [its environment variables](https://getcomposer.org/doc/03-cli.md#environment-variables).

You can remove the default build flavor and run your own commands for complete control over your build.
Set the build flavor to `none` and add the commands you need to your `build` hook, as in the following example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    build:
      flavor: none

    hooks:
      build: |
        set -e
        composer install --no-interaction --no-dev
```
That installs production dependencies with Composer but not development dependencies.
The same can be achieved by using the default build flavor and [adding the `COMPOSER_NO_DEV` variable](https://docs.upsun.com../../development/variables/set-variables.md).

See more on [build flavors](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#build).

### Alternative repositories

In addition to the standard `dependencies` format,
you can specify alternative repositories for Composer to use as global dependencies.
So you can install a forked version of a global dependency from a custom repository.

To install from an alternative repository:

1. Set an explicit `require` block:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    dependencies:
      php:
        require:
          "platformsh/client": "2.x-dev"
```
   This is equivalent to `composer require platform/client 2.x-dev`.

2. Add the repository to use:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    dependencies:
      php:
        require:
          "platformsh/client": "2.x-dev"
        repositories:
          - type: vcs
            url: "git@github.com:platformsh/platformsh-client-php.git"
```
That installs `platformsh/client` from the specified repository URL as a global dependency.

For example, to install Composer 2 and the `platform/client 2.x-dev` library from a custom repository,
use the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'
    [...]
    dependencies:
      php:
        require:
          composer/composer: '^2'
          "platformsh/client": "2.x-dev"
        repositories:
          - type: vcs
            url: "git@github.com:platformsh/platformsh-client-php.git"
```
### Configure security blocking {#configure-security-blocking}

When building a PHP app, Upsun runs `composer install`, which runs the latest available Composer version.

By default, PHP builds fail if a dependency in a project has a known vulnerability. A PHP build might also fail if a dependency is abandoned. 

**The best practice is to upgrade the dependencies** to reduce security risks and to catch issues sooner. However, you can configure the level of security blocking by defining the following keys in the `.dependencies.php.config` section of your `.upsun/config.yaml` file. 

| Key                     | Description                                                      |
| ------------------------| ---------------------------------------------------------------- |
| `audit.block-insecure`  | Default is `true`. **Important: Upsun recommends keeping this default setting and upgrading affected dependencies to reduce security risks.**                                                 | 
| `audit.block-abandoned` | Default is `false`; set to `true` for even stricter security. Ignored if `audit.block-insecure` is `false`.                  |
| `audit.ignore`          | Array of specific advisories to ignore; see example below.        | 
| `audit.ignore-severity` | Ignore vulnerabilities based on their severity rating (`low`/`medium`/`high`). See the example below.<BR>For each rating, include an `apply` key with one of these values: - `all` to ignore everything for this rating -  `block` to ignore this severity level for blocking builds (but still flag findings in audit reports) - `audit` to ignore this severity level in audit reports (but still block builds) |

Examples: 
```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    dependencies:
      php:
        config:
          audit:
            ignore:  # ignore these security advisories
              - "PKSA-yhcn-xrg3-68b1"
              - "PKSA-2wrf-1mxk-1pky"
```

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    dependencies:
      php:
        config:
          audit:
            ignore-severity:
              low:
                apply: all   # ignore all low severity findings
```

Related information: 
- [Troubleshooting PHP builds that now fail](https://docs.upsun.com/languages/php/troubleshoot.md#build-failure-security-blocking)

### Additional Composer schema properties
In addition to [alternate repositories](#alternative-repositories), other
[Composer schema properties](https://getcomposer.org/doc/04-schema.md) can be added to the global dependencies. For
example, one of your dependencies may be a plugin where you need to explicitly whitelist it as an
[allowed-plugin](https://getcomposer.org/doc/06-config.md#allow-plugins).

To add additional composer schema properties:

1. Set an explicit `require` block:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    dependencies:
      php:
        require:
          "third-party/required-plugin"": "^3.0"
```

2. Add each additional property as a block at the same indentation as the `require` block:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'

    dependencies:
      php:
        require:
          symfony/runtime: '*'
        config:
          "allow-plugins":
            symfony/runtime: true
```

## Connect to services

You can access service credentials to connect to [managed services](https://docs.upsun.com/add-services/) from environment variables present in the application container.
Consult each of the individual service documentation to see how to retrieve and surface credentials into your application.

- [Chroma](https://docs.upsun.com/add-services/chroma.md#3-use-the-relationship-in-your-application)

- [ClickHouse](https://docs.upsun.com/add-services/clickhouse.md#usage-example)

- [Elasticsearch](https://docs.upsun.com/add-services/elasticsearch.md#use-in-app)

- [Edgee (Edge Analytics)](https://docs.upsun.com/add-services/edgee.md#setup-edgee)

- [Gotenberg](https://docs.upsun.com/add-services/gotenberg.md#usage-example)

- [Headless Chrome](https://docs.upsun.com/add-services/headless-chrome.md#use-in-app)

- [InfluxDB](https://docs.upsun.com/add-services/influxdb.md#use-in-app)

- [Kafka](https://docs.upsun.com/add-services/kafka.md#use-in-app)

- [MariaDB/MySQL](https://docs.upsun.com/add-services/mysql.md#use-in-app)

- [Memcached](https://docs.upsun.com/add-services/memcached.md#use-in-app)

- [Mercure](https://docs.upsun.com/add-services/mercure.md#use-in-app)

- [MongoDB](https://docs.upsun.com/add-services/mongodb.md#use-in-app)

- [Network Storage](https://docs.upsun.com/add-services/network-storage.md#usage-example)

- [OpenSearch](https://docs.upsun.com/add-services/opensearch.md#use-in-app)

- [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md#use-in-app)

- [Qdrant](https://docs.upsun.com/add-services/qdrant.md#4-use-the-relationship-in-your-application)

- [RabbitMQ](https://docs.upsun.com/add-services/rabbitmq.md#use-in-app)

- [Redis](https://docs.upsun.com/add-services/redis.md#use-in-app)

- [Solr](https://docs.upsun.com/add-services/solr.md#use-in-app)

- [Valkey](https://docs.upsun.com/add-services/valkey.md#use-in-app)

- [Varnish](https://docs.upsun.com/add-services/varnish.md#usage-example)

- [Vault KMS](https://docs.upsun.com/add-services/vault.md#use-vault-kms)

## PHP settings

You can configure your PHP-FPM runtime configuration by specifying the [runtime in your app configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#runtime).

In addition to changes in runtime, you can also change the PHP settings.
Some commonly used settings are:

| Name | Default | Description |
|------|---------|-------------|
| `max_execution_time` | `300` | The maximum execution time, in seconds, for your PHP scripts and apps. A value of `0` means there are no time limits. |
| `max_file_uploads` | `20` | The maximum number of files that can be uploaded in each request. |
| `max_input_time` | `60` | The maximum time in seconds that your script is allowed to receive input (such as for file uploads). A value of `-1` means there are no time limits. |
| `max_input_vars` | `1000` | The maximum number of input variables that are accepted in each request. |
| `memory_limit` | `128M` | The memory limit, in megabytes, for PHP. Ensure that the PHP memory limit is set to a lower value than your environment's memory. |
| `post_max_size` | `64M` | The maximum size, in megabytes, per uploaded file. To upload larger files, increase the value. |
| `zend.assertions` | `-1` | Assertions are optimized and have no impact at runtime. Set assertions to `1` for your local development system. [See more on assertions](https://www.php.net/manual/en/regexp.reference.assertions). |
| `opcache.memory_consumption` | `64` | The number of megabytes available for [the OPcache](https://docs.upsun.com/languages/php/tuning.md#opcache-preloading). For large apps with many files, increase this value. |
| `opcache.validate_timestamps` | `On` | If your app doesn't generate compiled PHP, you can [disable this setting](https://docs.upsun.com/languages/php/tuning.md#disable-opcache-timestamp-validation). |

### Retrieve the default values

To retrieve the default PHP values, run the following [CLI command](https://docs.upsun.com../../administration/cli/_index.md):

```bash
upsun ssh "php --info"
```

To get specific default values, use grep.
For example, to get the value for `opcache.memory_consumption`, run the following command:

```bash
upsun ssh "php --info" | grep opcache.memory_consumption
```

### Retrieve the settings

To see the settings used on your environment:

1.  Find the PHP configuration files with the following [CLI command](https://docs.upsun.com../../administration/cli/_index.md):

    ```bash
    upsun ssh "php --ini"
    ```

    The output is something like the following:

    ```bash
    Configuration File (php.ini) Path: /etc/php/8.0-zts/cli
    Loaded Configuration File:         /etc/php/8.0-zts/cli/php.ini
    Scan for additional .ini files in: /etc/php/8.0-zts/cli/conf.d
    Additional .ini files parsed:      (none)
    ```

2.  Display the configuration file by adapting the following command with the output from step 1:

    ```bash
    upsun ssh "cat <LOADED_CONFIGURATION_FILE_PATH>"
    ```

### Customize PHP settings

You can customize PHP values for your app in two ways.
The recommended method is to use variables.

For more information, see how to use [PHP-specific variables](https://docs.upsun.com/development/variables.md#php-specific-variables).
You can provide a custom ``php.ini`` file at the [app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory).
Using this method isn’t recommended since it offers less flexibility and is more error-prone.
Consider using variables instead.
For example, to change the PHP memory limit, use the following configuration:

    php.ini

```ini {}
memory_limit = 256M
```

If you're using [PHP-CLI](#execution-mode),
you need to take into account the default settings of PHP-CLI when you customize your PHP settings.
The default settings of PHP-CLI can't be overwritten and are the following:

```text
max_execution_time=0
max_input_time=-1
memory_limit=-1
```

### Disable functions for security

A common recommendation for securing PHP installations is disabling built-in functions frequently used in remote attacks.
By default, Upsun doesn't disable any functions.

If you're sure a function isn't needed in your app, you can disable it.

For example, to disable `pcntl_exec` and `pcntl_fork`, add the following to your [app configuration](https://docs.upsun.com../../create-apps/_index.md):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'php:8.5'
    variables:
      php:
        disable_functions: "pcntl_exec,pcntl_fork"
```
Common functions to disable include:

| Name | Description |
|------|-------------|
| `create_function` | This function has been replaced by anonymous functions and shouldn't be used anymore. |
| `exec`, `passthru`, `shell_exec`, `system`, `proc_open`, `popen` | These functions allow a PHP script to run a bash shell command. Rarely used by web apps except for build scripts that might need them. |
| `pcntl_*` | The `pcntl_*` functions are responsible for process management. Most of them cause a fatal error if used within a web request. Cron tasks or workers may need them. Most are usually safe to disable. |
| `curl_exec`, `curl_multi_exec` | These functions allow a PHP script to make arbitrary HTTP requests. If you're using HTTP libraries such as Guzzle, don't disable them. |
| `show_source` | This function shows a syntax highlighted version of a named PHP source file. Rarely useful outside of development. |

## Execution mode

PHP has two execution modes you can choose from:

- The command line interface mode (PHP-CLI) is the mode used for command line scripts and standalone apps.
  This is the mode used when you're logged into your container via SSH, for [crons](https://docs.upsun.com/create-apps/image-properties/crons.md),
  and usually also for [alternate start commands](#alternate-start-commands).
  To use PHP-CLI, run your script with `php <PATH_TO_SCRIPT>`,
  where <PATH_TO_SCRIPT> is a file path relative to the [app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory).
- The Common Gateway Interface mode (PHP-CGI) is the mode used for web apps and web requests.
  This is the default mode when the `start` command isn't explicitly set.
  To use PHP-CGI, run your script with a symlink: `/usr/bin/start-php-app <PATH_TO_SCRIPT>`,
  where <PATH_TO_SCRIPT> is a file path relative to the [app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory).
  With PHP-CGI, PHP is run using the FastCGI Process Manager (PHP-FPM).

## Alternate start commands

To specify an alternative process to run your code, set a `start` command.
For more information about the start command, see the [web commands reference](create-apps/image-properties/web.md#web-commands).

By default, start commands use PHP-CLI.
Find out how and when to use each [execution mode](#execution-mode).

Note that the `start` command must run in the foreground and is executed before the [deploy hook](https://docs.upsun.com../../create-apps/hooks/hooks-comparison.md).
That means that PHP-FPM can't run simultaneously with another persistent process
such as [ReactPHP](https://github.com/platformsh-examples/platformsh-example-reactphp)
or [Amp](https://github.com/platformsh-examples/platformsh-example-amphp).
If you need multiple processes, they have to run in separate containers.

See some generic examples on how to use alternate start commands:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    web:
      commands:
        start: /usr/bin/start-php-app
```

 - Add your web server’s code in a PHP file.

 - Specify an alternative ``start`` command by adapting the following:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    web:
      commands:
        start: /usr/bin/start-php-app
```

 - Configure the container to listen on a TCP socket:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    web:
      upstream:
        socket_family: tcp
        protocol: http
```

When you listen on a TCP socket, the ``$PORT`` environment variable is automatically set.
See more options on how to [configure where requests are sent](https://docs.upsun.com/create-apps/image-properties/web.md#upstream).
You might have to configure your app to connect via the ``$PORT`` TCP socket,
especially when using web servers such as [Swoole](https://docs.upsun.com/languages/php/swoole.md) or [Roadrunner](https://github.com/roadrunner-server/roadrunner).

 - Optional: Override redirects to let the custom web server handle them:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    locations:
      "/":
        passthru: true
        scripts: false
        allow: false
```

To execute runtime-specific tasks (such as clearing cache) before your app starts, follow these steps:

 - Create a separate shell script that includes all the commands to be run.

 - Specify an alternative ``start`` command by adapting the following:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    web:
      commands:
        start: bash <PATH_TO_SCRIPT> && /usr/bin/start-php-app
```

<PATH_TO_SCRIPT> is the bash script created in step 1.
<PATH_TO_SCRIPT> is a file path relative to the [app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory).

## Foreign function interfaces

PHP 7.4 introduced support for [foreign function interfaces (FFIs)](https://en.wikipedia.org/wiki/Foreign_function_interface).
FFIs allow your PHP program to call routines or use services written in C or Rust.

Note: FFIs are only intended for advanced use cases.
Use with caution.

If you are using C code, you need `.so` library files.
Either place these files directly in your repository or compile them in a makefile using `gcc` in your [build hook](https://docs.upsun.com../../create-apps/hooks/hooks-comparison.md#build-hook).
Note: The `.so` library files shouldn't be located in a publicly accessible directory.

If you are compiling Rust code, use the build hook to [install Rust](https://doc.rust-lang.org/stable/book/ch01-01-installation.md).

To leverage FFIs, follow these steps:

1.  [Enable and configure OPcache preloading](https://docs.upsun.com/languages/php/tuning.md#enable-opcache-preloading).

2.  Enable the FFI extension:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'php:8.5'
    runtime:
      extensions:
        - ffi
```

3.  Make sure that your [preload script](https://docs.upsun.com/languages/php/tuning.md#opcache-preloading) calls the `FFI::load()` function.
    Using this function in preload is considerably faster than loading the linked library on each request or script run.

4.  If you are running FFIs from the command line,
    enable the preloader by adding the following configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'php:8.5'
    variables:
      php:
        opcache.enable_cli: true
```

5.  Run your script with the following command:

    ```bash
    php <CLI_SCRIPT>
    ```

## Frameworks

All major PHP web frameworks can be deployed on Upsun.
See dedicated guides for deploying and working with them:

- [Laravel](https://docs.upsun.com/get-started/stacks/laravel.md)
- [Symfony](https://docs.upsun.com/get-started/stacks/symfony.md)

## Modify your PHP runtime when using the composable image

**Note**: 

This section is only relevant when using the Upsun [composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md).

The following table presents the possible modifications you can make to your PHP primary runtime using the `stack.runtimes` key in a composable image.

For example, `extensions` are enabled under `.applications.frontend.stack.runtimes[0]["php@8.5"].extensions` for PHP 8.5).
See the [example](#example-php-configuration) below for more details.

**Note**: 

The PHP-FPM service starts automatically only when PHP is the primary runtime.

| Name                        | Type                                                                                                                          | Description                                                                                             |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `extensions`                | List of `string`s OR [extensions definitions](https://docs.upsun.com/create-apps/app-reference/composable-image#php-extensions-and-python-packages) | [PHP extensions](https://docs.upsun.com/languages/php/extensions.md) to enable.                                               |
| `disabled_extensions`       | List of `string`s                                                                                                             | [PHP extensions](https://docs.upsun.com/languages/php/extensions.md) to disable.                                              |
| `request_terminate_timeout` | `integer`                                                                                                                     | The timeout (in seconds) for serving a single request after which the PHP-FPM worker process is killed. |
| `sizing_hints`              | A [sizing hints definition](#sizing-hints)                                      | The assumptions for setting the number of workers in your PHP-FPM runtime.                              |
| `xdebug`                    | An Xdebug definition                                                                                                          | The setting to turn on [Xdebug](https://docs.upsun.com/languages/php/xdebug.md).                                              |

### PHP-FPM service sizing hints {#sizing-hints}

The following table shows the properties that can be set in `sizing_hints`:

| Name              | Type      | Default | Minimum | Description                                    |
|-------------------|-----------|---------|---------|------------------------------------------------|
| `request_memory`  | `integer` | 45      | 10      | The average memory consumed per request in MB. |
| `reserved_memory` | `integer` | 70      | 70      | The amount of memory reserved in MB.           |

See more about [PHP-FPM workers and sizing](https://docs.upsun.com/languages/php/fpm.md).

### Example PHP configuration {#example-php-configuration}

Here is an example configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  frontend:
    type: "composable:25.11"
    stack:
      runtimes:
        - "php@8.4":
            extensions:
              - apcu # A PHP extension made available to the PHP runtime
              - sodium
              - xsl
              - pdo_sqlite

            xdebug:
              idekey: YOUR_KEY

            disabled_extensions:
              - gd

            request_terminate_timeout: 200

            sizing_hints:
              request_memory: 45
              reserved_memory: 70

        - "python@3.13"
      packages:
        - "php84Extensions.apcu" # A PHP extension made available to all runtimes.
        - "python313Packages.yq"
```

**Note**: 

You can also set your [app’s runtime timezone](https://docs.upsun.com/create-apps/timezone.md).


