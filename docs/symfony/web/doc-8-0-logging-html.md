# Source: https://symfony.com/doc/8.0/logging.html

Title: Logging (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/logging.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/logging.rst)

Symfony comes with two minimalist [PSR-3](https://www.php-fig.org/psr/psr-3/) loggers: [Logger](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Log/Logger.php "Symfony\Component\HttpKernel\Log\Logger") for the HTTP context and [ConsoleLogger](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Logger/ConsoleLogger.php "Symfony\Component\Console\Logger\ConsoleLogger") for the CLI context. In conformance with [the twelve-factor app methodology](https://12factor.net/logs), they send messages starting from the `WARNING` level to [stderr](https://en.wikipedia.org/wiki/Standard_streams#Standard_error_(stderr)).

The minimal log level can be changed by setting the `SHELL_VERBOSITY` environment variable:

| `SHELL_VERBOSITY` value | Minimum log level |
| --- | --- |
| `-1` | `ERROR` |
| `1` | `NOTICE` |
| `2` | `INFO` |
| `3` | `DEBUG` |

The minimum log level, the default output and the log format can also be changed by passing the appropriate arguments to the constructor of [Logger](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Log/Logger.php "Symfony\Component\HttpKernel\Log\Logger") and [ConsoleLogger](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Logger/ConsoleLogger.php "Symfony\Component\Console\Logger\ConsoleLogger").

The [Logger](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Log/Logger.php "Symfony\Component\HttpKernel\Log\Logger") class is available through the `logger` service. To pass your configuration, you can [override the "logger" service definition](https://symfony.com/doc/current/service_container.html#service-psr4-loader).

For more information about `ConsoleLogger`, see [Using the Logger](https://symfony.com/doc/current/components/console/logger.html).

[Logging a Message](https://symfony.com/doc/8.0/logging.html#logging-a-message "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

To log a message, inject the default logger in your controller or service:

Adding placeholders to log messages is recommended because:

* It's easier to check log messages because many logging tools group log messages that are the same except for some variable values inside them;
* It's much easier to translate those log messages;
* It's better for security, because escaping can then be done by the implementation in a context-aware fashion.

The `logger` service has different methods for different logging levels/priorities. See [LoggerInterface](https://github.com/php-fig/log/blob/master/src/LoggerInterface.php) for a list of all of the methods on the logger.

[Monolog](https://symfony.com/doc/8.0/logging.html#monolog "Permalink to this headline")
----------------------------------------------------------------------------------------

Symfony integrates seamlessly with [Monolog](https://github.com/Seldaek/monolog), the most popular PHP logging library, to create and store log messages in a variety of different places and trigger various actions.

For instance, using Monolog you can configure the logger to do different things based on the _level_ of a message (e.g. [send an email when an error occurs](https://symfony.com/doc/current/logging/monolog_email.html)).

Run this command to install the Monolog based logger before using it:

The following sections assume that Monolog is installed.

[Where Logs are Stored](https://symfony.com/doc/8.0/logging.html#where-logs-are-stored "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

By default, log entries are written to the `var/log/dev.log` file when you're in the `dev` environment.

In the `prod` environment, logs are written to [STDERR PHP stream](https://www.php.net/manual/en/features.commandline.io-streams.php), which works best in modern containerized applications deployed to servers without disk write permissions.

If you prefer to store production logs in a file, set the `path` of your log handler(s) to the path of the file to use (e.g. `var/log/prod.log`).

[Handlers: Writing Logs to different Locations](https://symfony.com/doc/8.0/logging.html#handlers-writing-logs-to-different-locations "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

The logger has a stack of _handlers_, and each can be used to write the log entries to different locations (e.g. files, database, Slack, etc).

Tip

You can _also_ configure logging "channels", which are like categories. Each channel can have its _own_ handlers, which means you can store different log messages in different places. See [How to Log Messages to different Files](https://symfony.com/doc/current/logging/channels_handlers.html).

Symfony pre-configures some basic handlers in the default `monolog.yaml` config files. Check these out for some real-world examples.

This example uses _two_ handlers: `stream` (to write to a file) and `syslog` to write logs using the [syslog](https://secure.php.net/manual/en/function.syslog.php "syslog") function:

This defines a stack of handlers. Each handler can define a `priority` (default `0`) to control its position in the stack. Handlers with a higher priority are called first, while those with the same priority keep the order in which they are defined:

Note

When adding handlers in other configuration files, it's recommended to set an explicit priority to ensure they are ordered as expected.

### [Handlers that Modify Log Entries](https://symfony.com/doc/8.0/logging.html#handlers-that-modify-log-entries "Permalink to this headline")

Instead of writing log files somewhere, _some_ handlers are used to filter or modify log entries before sending them to _other_ handlers. One powerful, built-in handler called `fingers_crossed` is used in the `prod` environment by default. It stores _all_ log messages during a request but _only_ passes them to a second handler if one of the messages reaches an `action_level`. Take this example:

Now, if even one log entry has an `LogLevel::ERROR` level or higher, then _all_ log entries for that request are saved to a file via the `file_log` handler. That means that your log file will contain _all_ the details about the problematic request - making debugging much easier!

Tip

The handler named "file_log" will not be included in the stack itself as it is used as a nested handler of the `fingers_crossed` handler.

[All Built-in Handlers](https://symfony.com/doc/8.0/logging.html#all-built-in-handlers "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

Monolog comes with _many_ built-in handlers for emailing logs, sending them to Loggly, or notifying you in Slack. These are documented inside of MonologBundle itself. For a full list, see [Monolog Configuration](https://github.com/symfony/monolog-bundle/blob/4.x/src/DependencyInjection/Configuration.php).

[How to Rotate your Log Files](https://symfony.com/doc/8.0/logging.html#how-to-rotate-your-log-files "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------

Over time, log files can grow to be _huge_, both while developing and on production. One best-practice solution is to use a tool like the [logrotate](https://github.com/logrotate/logrotate) Linux command to rotate log files before they become too large.

Another option is to have Monolog rotate the files for you by using the `rotating_file` handler. This handler creates a new log file every day and can also remove old files automatically. To use it, set the `type` option of your handler to `rotating_file`:

[Using a Logger inside a Service](https://symfony.com/doc/8.0/logging.html#using-a-logger-inside-a-service "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------

If your application uses [service autoconfiguration](https://symfony.com/doc/current/service_container.html#services-autoconfigure), any service whose class implements `Psr\Log\LoggerAwareInterface` will receive a call to its method `setLogger()` with the default logger service passed as a service.

If you want to use in your own services a pre-configured logger which uses a specific channel (`app` by default), you can either [autowire monolog channels](https://symfony.com/doc/current/logging/channels_handlers.html#monolog-autowire-channels) or use the `monolog.logger` tag with the `channel` property as explained in the [Dependency Injection reference](https://symfony.com/doc/current/reference/dic_tags.html#dic_tags-monolog).

[Handling Logs in Long Running Processes](https://symfony.com/doc/8.0/logging.html#handling-logs-in-long-running-processes "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------

During long running processes, logs can be accumulated into Monolog and cause some buffer overflow, memory increase or even non logical logs. Monolog in-memory data can be cleared using the `reset()` method on a `Monolog\Logger` instance. This should typically be called between every job or task that a long running process is working through.

[Learn more](https://symfony.com/doc/8.0/logging.html#learn-more "Permalink to this headline")
----------------------------------------------------------------------------------------------

* [How to Configure Monolog to Email Errors](https://symfony.com/doc/current/logging/monolog_email.html)
* [How to Log Messages to different Files](https://symfony.com/doc/current/logging/channels_handlers.html)
* [How to Define a Custom Logging Formatter](https://symfony.com/doc/current/logging/formatter.html)
* [How to Add extra Data to Log Messages via a Processor](https://symfony.com/doc/current/logging/processors.html)
* [Handlers](https://symfony.com/doc/current/logging/handlers.html)
* [How to Configure Monolog to Exclude Specific HTTP Codes from the Log](https://symfony.com/doc/current/logging/monolog_exclude_http_codes.html)
* [How to Configure Monolog to Display Console Messages](https://symfony.com/doc/current/logging/monolog_console.html)

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
