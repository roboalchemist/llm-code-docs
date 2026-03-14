# Source: https://spectreconsole.net/cli

Title: Spectre.Console.Cli Documentation - Spectre.Console Documentation

URL Source: https://spectreconsole.net/cli

Markdown Content:
Build powerful command-line applications with Spectre.Console.Cli, a modern framework with a focus on type safety and developer experience.

Start Here
----------

Get Spectre.Console.Cli running in seconds:

```
dotnet add package Spectre.Console.Cli
```

Then try this quick example that creates a simple greeting command:

```
public class GreetSettings : CommandSettings
{
    [CommandArgument(0, "<name>")]
    [Description("The name to greet")]
    public required string Name { get; init; }
  
    [CommandOption("-c|--count")]
    [Description("Number of times to greet")]
    [DefaultValue(1)]
    public int Count { get; init; }
}
  
public class GreetCommand : Command<GreetSettings>
{
    protected override int Execute(CommandContext context, GreetSettings settings, CancellationToken cancellation)
    {
        for (var i = 0; i < settings.Count; i++)
        {
            AnsiConsole.MarkupLine($"Hello, [green]{settings.Name}[/]!");
        }
        return 0;
    }
}
```

In your Program.cs, wire it up:

```
var app = new CommandApp<GreetCommand>();
return app.Run(args);
```

Run it with `dotnet run -- World --count 3` to see typed argument parsing in action.

You should see something like this:

![Image 1: Screencast of Spectre.Console in action](https://spectreconsole.net/assets/cli-quickstart.svg)

* * *

Explore the Documentation
-------------------------

From simple single-command tools to complex CLI applications with nested commands and dependency injection, we've got you covered. The tutorials will walk you through the fundamentals, while the how-to guides tackle specific scenarios you'll encounter in real projects.

Tutorials
---------

*   [Quick Start: Your First CLI App](https://spectreconsole.net/cli/tutorials/quick-start-your-first-cli-app) - Build your first command-line application with Spectre.Console.Cli
*   [Building a Multi-Command CLI Tool](https://spectreconsole.net/cli/tutorials/building-a-multi-command-cli-tool) - Build a CLI application with multiple commands, subcommands, and shared settings
*   [Dependency Injection in CLI Apps](https://spectreconsole.net/cli/tutorials/dependency-injection-in-cli-apps) - Inject services into your CLI commands using Microsoft.Extensions.DependencyInjection
*   [Logging in CLI Apps](https://spectreconsole.net/cli/tutorials/logging-in-cli-apps) - Add structured logging to your CLI commands using Microsoft.Extensions.Logging

How-To Guides
-------------

*   [Defining Commands and Arguments](https://spectreconsole.net/cli/how-to/defining-commands-and-arguments) - How to declare command-line parameters (arguments and options) using Spectre.Console.Cli's attributes and settings classes
*   [Making Options Required](https://spectreconsole.net/cli/how-to/making-options-required) - How to make command-line options required instead of optional in Spectre.Console.Cli
*   [Handling Errors and Exit Codes](https://spectreconsole.net/cli/how-to/handling-errors-and-exit-codes) - How Spectre.Console.Cli deals with exceptions and how to customize error handling
*   [Async Commands and Cancellation](https://spectreconsole.net/cli/how-to/async-commands-and-cancellation) - How to create asynchronous commands and handle cancellation in Spectre.Console.Cli
*   [Configuring CommandApp and Commands](https://spectreconsole.net/cli/how-to/configuring-commandapp-and-commands) - How to register commands with the CommandApp and configure global settings
*   [Customizing Help Text and Usage](https://spectreconsole.net/cli/how-to/customizing-help-text-and-usage) - How to tailor the automatically generated help output of Spectre.Console.Cli
*   [Working with Multiple Command Hierarchies](https://spectreconsole.net/cli/how-to/working-with-multiple-command-hierarchies) - How to create hierarchical (nested) commands using branching
*   [Using Flag Arguments](https://spectreconsole.net/cli/how-to/using-flag-arguments) - How to use FlagValue for optional flag arguments that may or may not include a value
*   [Using Dictionary and Lookup Options](https://spectreconsole.net/cli/how-to/using-dictionary-and-lookup-options) - How to accept key-value pairs using IDictionary, ILookup, and IReadOnlyDictionary options
*   [Using Custom Type Converters](https://spectreconsole.net/cli/how-to/using-custom-type-converters) - How to create and apply custom type converters for complex command-line argument types
*   [Testing Command-Line Applications](https://spectreconsole.net/cli/how-to/testing-command-line-applications) - How to test CLI apps built with Spectre.Console.Cli to ensure they parse and execute correctly
*   [Hiding Commands and Options](https://spectreconsole.net/cli/how-to/hiding-commands-and-options) - How to hide commands and options from help output while keeping them functional
*   [Intercepting Command Execution](https://spectreconsole.net/cli/how-to/intercepting-command-execution) - How to use command interceptors to run logic before or after any command executes

Explanation
-----------

*   [Design Philosophy: Convention over Configuration](https://spectreconsole.net/cli/explanation/design-philosophy-convention-over-configuration) - An explanation of the guiding philosophy behind Spectre.Console.Cli
*   [Command Lifecycle and Execution Flow](https://spectreconsole.net/cli/explanation/command-lifecycle-and-execution-flow) - An explanatory deep-dive into what happens from the moment app.Run(args) is called to when a command finishes execution

Reference
---------

*   [Attribute and Parameter Reference](https://spectreconsole.net/cli/reference/attribute-and-parameter-reference) - A summary of all attributes and parameter-related features in Spectre.Console.Cli
*   [Type Converters](https://spectreconsole.net/cli/reference/type-converters) - Reference for type conversion in Spectre.Console.Cli command-line parsing
*   [CommandContext Reference](https://spectreconsole.net/cli/reference/command-context) - Reference documentation for the CommandContext class in Spectre.Console.Cli
*   [Built-in Command Behaviors](https://spectreconsole.net/cli/reference/built-in-command-behaviors) - A reference describing Spectre.Console.Cli's built-in behaviors and conventions for completeness
