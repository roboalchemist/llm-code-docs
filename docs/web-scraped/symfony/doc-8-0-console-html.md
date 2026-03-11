# Source: https://symfony.com/doc/8.0/console.html

Title: Console Commands (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/console.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/console.rst)

The Symfony framework provides lots of commands through the `bin/console` script (e.g. the well-known `bin/console cache:clear` command). These commands are created with the [Console component](https://symfony.com/doc/current/components/console.html). You can also use it to create your own commands.

[Running Commands](https://symfony.com/doc/8.0/console.html#running-commands "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

Each Symfony application comes with a large set of commands. You can use the `list` command to view all available commands in the application:

Note

`list` is the default command, so running `php bin/console` is the same.

If you find the command you need, you can run it with the `--help` option to view the command's documentation:

Note

`--help` is one of the built-in global options from the Console component, which are available for all commands, including those you can create. To learn more about them, you can read [this section](https://symfony.com/doc/current/console/input.html#console-global-options).

### [APP_ENV & APP_DEBUG](https://symfony.com/doc/8.0/console.html#app-env-app-debug "Permalink to this headline")

Console commands run in the [environment](https://symfony.com/doc/current/configuration.html#config-dot-env) defined in the `APP_ENV` variable of the `.env` file, which is `dev` by default. It also reads the `APP_DEBUG` value to turn "debug" mode on or off (it defaults to `1`, which is on).

To run the command in another environment or debug mode, edit the value of `APP_ENV` and `APP_DEBUG`. You can also define this env vars when running the command, for instance:

### [Console Completion](https://symfony.com/doc/8.0/console.html#console-completion "Permalink to this headline")

If you are using the Bash, Zsh or Fish shell, you can install Symfony's completion script to get auto completion when typing commands in the terminal. All commands support name and option completion, and some can even complete values.

![Image 1: The terminal completes the command name "secrets:remove" and the argument "SOME_OTHER_SECRET".](https://symfony.com/doc/8.0/_images/completion.gif)

First, you have to install the completion script _once_. Run `bin/console completion --help` for the installation instructions for your shell.

Note

When using Bash, make sure you installed and setup the "bash completion" package for your OS (typically named `bash-completion`).

After installing and restarting your terminal, you're all set to use completion (by default, by pressing the Tab key).

Tip

Many PHP tools are built using the Symfony Console component (e.g. Composer, PHPstan and Behat). If they are using version 5.4 or higher, you can also install their completion script to enable console completion:

[Creating a Command](https://symfony.com/doc/8.0/console.html#creating-a-command "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

Commands are defined in classes and auto-registered using the `#[AsCommand]` attribute. For example, you may want a command to create a user:

If you can't use PHP attributes, register the command as a service and [tag it](https://symfony.com/doc/current/service_container/tags.html) with the `console.command` tag. If you're using the [default services.yaml configuration](https://symfony.com/doc/current/service_container.html#service-container-services-load-example), this is already done for you, thanks to [autoconfiguration](https://symfony.com/doc/current/service_container.html#services-autoconfigure).

You can also use `#[AsCommand]` to add a description, usage exampless, and longer help text for the command:

Additionally, you can extend the [Command](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Command/Command.php "Symfony\Component\Console\Command\Command") class to leverage advanced features like lifecycle hooks (e.g. [initialize()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Command/Command.php#:~:text=function%20initialize "Symfony\Component\Console\Command\Command::initialize()") and and [interact()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Command/Command.php#:~:text=function%20interact "Symfony\Component\Console\Command\Command::interact()")):

### [Running the Command](https://symfony.com/doc/8.0/console.html#running-the-command "Permalink to this headline")

After configuring and registering the command, you can run it in the terminal:

As you might expect, this command will do nothing as you didn't write any logic yet. Add your own logic inside the `__invoke()` method.

### [Command Aliases](https://symfony.com/doc/8.0/console.html#command-aliases "Permalink to this headline")

You can define alternative names (aliases) for a command directly in its name using a pipe (`|`) separator. The first name in the list becomes the actual command name; the others are aliases that can also be used to run the command:

[Console Output](https://symfony.com/doc/8.0/console.html#console-output "Permalink to this headline")
------------------------------------------------------------------------------------------------------

The `__invoke()` method has access to the output stream to write messages to the console:

Now, try executing the command:

### [Output Sections](https://symfony.com/doc/8.0/console.html#output-sections "Permalink to this headline")

The regular console output can be divided into multiple independent regions called "output sections". Create one or more of these sections when you need to clear and overwrite the output information.

Sections are created with the [ConsoleOutput::section()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Output/ConsoleOutput.php#:~:text=function%20section "Symfony\Component\Console\Output\ConsoleOutput::section()") method, which returns an instance of [ConsoleSectionOutput](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Output/ConsoleSectionOutput.php "Symfony\Component\Console\Output\ConsoleSectionOutput"):

Note

A new line is appended automatically when displaying information in a section.

Output sections let you manipulate the Console output in advanced ways, such as [displaying multiple progress bars](https://symfony.com/doc/current/components/console/helpers/progressbar.html#console-multiple-progress-bars) which are updated independently and [appending rows to tables](https://symfony.com/doc/current/components/console/helpers/table.html#console-modify-rendered-tables) that have already been rendered.

Warning

Terminals only allow overwriting the visible content, so you must take into account the console height when trying to write/overwrite section contents.

[Console Input](https://symfony.com/doc/8.0/console.html#console-input "Permalink to this headline")
----------------------------------------------------------------------------------------------------

Use input options or arguments to pass information to the command:

Now, you can pass the username to the command:

[Getting Services from the Service Container](https://symfony.com/doc/8.0/console.html#getting-services-from-the-service-container "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

To actually create a new user, the command has to access some [services](https://symfony.com/doc/current/service_container.html). Since your command is already registered as a service, you can use normal dependency injection. Imagine you have a `App\Service\UserManager` service that you want to access:

[Command Lifecycle](https://symfony.com/doc/8.0/console.html#command-lifecycle "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

Commands have three lifecycle methods that are invoked when running the command:

[initialize()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Command/Command.php#:~:text=function%20initialize "Symfony\Component\Console\Command\Command::initialize()")_(optional)_ This method is executed before the `interact()` and the `execute()` methods. Its main purpose is to initialize variables used in the rest of the command methods. [interact()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Command/Command.php#:~:text=function%20interact "Symfony\Component\Console\Command\Command::interact()")_(optional)_ This method is executed after `initialize()` and before `execute()`. Its purpose is to check if some of the options/arguments are missing and interactively ask the user for those values. This is the last place where you can ask for missing required options/arguments. This method is called before validating the input. Note that it will not be called when the command is run without interaction (e.g. when passing the `--no-interaction` global option flag). `__invoke()` (or [execute()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Command/Command.php#:~:text=function%20execute "Symfony\Component\Console\Command\Command::execute()")) _(required)_ This method is executed after `interact()` and `initialize()`. It contains the logic you want the command to execute and it must return an integer which will be used as the command [exit status](https://en.wikipedia.org/wiki/Exit_status).

[Testing Commands](https://symfony.com/doc/8.0/console.html#testing-commands "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

Symfony provides several tools to help you test your commands. The most useful one is the [CommandTester](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Tester/CommandTester.php "Symfony\Component\Console\Tester\CommandTester") class. It uses special input and output classes to ease testing without a real console:

If you are using a [single-command application](https://symfony.com/doc/current/components/console/single_command_tool.html), call `setAutoExit(false)` on it to get the command result in `CommandTester`.

Warning

When testing commands using the `CommandTester` class, console events are not dispatched. If you need to test those events, use the [ApplicationTester](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Tester/ApplicationTester.php "Symfony\Component\Console\Tester\ApplicationTester") instead.

Warning

When testing commands using the [ApplicationTester](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Tester/ApplicationTester.php "Symfony\Component\Console\Tester\ApplicationTester") class, don't forget to disable the auto exit flag:

Warning

When testing `InputOption::VALUE_NONE` command options, you must pass `true` to them:

Note

When using the Console component in a standalone project, use [Application](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Application.php "Symfony\Component\Console\Application") and extend the normal `\PHPUnit\Framework\TestCase`.

Note

The `CommandTester` class does not implement `ConsoleOutputInterface`, so methods like `section()` are not directly accessible. To test them, use the `capture_stderr_separately` option of the `execute()` method:

When testing your commands, it could be useful to understand how your command reacts on different settings like the width and the height of the terminal, or even the color mode being used. You have access to such information thanks to the [Terminal](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Terminal.php "Symfony\Component\Console\Terminal") class:

[Logging Command Errors](https://symfony.com/doc/8.0/console.html#logging-command-errors "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------

Whenever an exception is thrown while running commands, Symfony adds a log message for it including the entire failing command. In addition, Symfony registers an [event subscriber](https://symfony.com/doc/current/event_dispatcher.html) to listen to the [ConsoleEvents::TERMINATE event](https://symfony.com/doc/current/components/console/events.html#console-events-terminate) and adds a log message whenever a command doesn't finish with the `0`[exit status](https://en.wikipedia.org/wiki/Exit_status).

[Using Events And Handling Signals](https://symfony.com/doc/8.0/console.html#using-events-and-handling-signals "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------

When a command is running, many events are dispatched, one of them allows you to react to signals, read more in [this section](https://symfony.com/doc/current/components/console/events.html).

[Profiling Commands](https://symfony.com/doc/8.0/console.html#profiling-commands "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

Symfony allows you to profile the execution of any command, including yours. First, make sure that the [debug mode](https://symfony.com/doc/current/configuration/front_controllers_and_kernel.html#debug-mode) and the [profiler](https://symfony.com/doc/current/profiler.html) are enabled. Then, add the `--profile` option when running the command:

Symfony will now collect data about the command execution, which is helpful to debug errors or check other issues. When the command execution is over, the profile is accessible through the web page of the profiler.

Tip

If you run the command in verbose mode (adding the `-v` option), Symfony will display in the output a clickable link to the command profile (if your terminal supports links). If you run it in debug verbosity (`-vvv`) you'll also see the time and memory consumed by the command.

Warning

When profiling the `messenger:consume` command from the [Messenger](https://symfony.com/doc/current/messenger.html) component, add the `--no-reset` option to the command or you won't get any profile. Moreover, consider using the `--limit` option to only process a few messages to make the profile more readable in the profiler.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
