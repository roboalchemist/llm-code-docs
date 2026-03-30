# Source: https://spectreconsole.net/cli/tutorials/quick-start-your-first-cli-app

Title: Quick Start: Your First CLI App

URL Source: https://spectreconsole.net/cli/tutorials/quick-start-your-first-cli-app

Markdown Content:
In this tutorial, we'll build a greeting command-line application together. By the end, we'll have a working CLI that accepts a name, repeats greetings on demand, and shows helpful usage information automatically.

1.   1
**Create the Project**

Let's start by creating a new console application and adding the Spectre.Console.Cli package:

```
dotnet new console -n GreetingApp
cd GreetingApp
dotnet add package Spectre.Console.Cli
``` 
The output confirms the package was installed. Now we're ready to write some code.

2.   2
**Create Your First Command**

Open `Program.cs` and replace its contents with our greeting command:

```
internal class GreetCommand : Command<GreetCommand.Settings>
{
    public class Settings : CommandSettings
    {
        [CommandArgument(0, "<name>")]
        [Description("The name to greet")]
        public string Name { get; init; } = string.Empty;
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        System.Console.WriteLine($"Hello, {settings.Name}!");
        return 0;
    }
}
``` 
Run the application:

```
dotnet run -- Alice
``` 
You should see `Hello, Alice!` printed to the console. Notice the `<name>` in angle brackets? That means it's required. Try running without a name to see the built-in error handling:

```
dotnet run
``` 
The CLI automatically tells you that the name argument is missing. No extra code needed.

3.   3
**Add an Option**

Arguments are great for required values, but sometimes you want optional behavior. Let's add a `--count` option to repeat the greeting:

```
internal class GreetCommand : Command<GreetCommand.Settings>
{
    public class Settings : CommandSettings
    {
        [CommandArgument(0, "<name>")]
        [Description("The name to greet")]
        public string Name { get; init; } = string.Empty;
  
        [CommandOption("-c|--count")]
        [Description("Number of times to greet")]
        [DefaultValue(1)]
        public int Count { get; init; } = 1;
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        for (var i = 0; i < settings.Count; i++)
        {
            System.Console.WriteLine($"Hello, {settings.Name}!");
        }
        return 0;
    }
}
``` 
Run the application with the new option:

```
dotnet run -- Alice --count 3
``` 
The greeting appears three times. The `-c` short form works too:

```
dotnet run -- Alice -c 2
``` 
Options default to the value you specify (here, `1`), so the original command still works:

```
dotnet run -- Alice
``` 
4.   4
**Explore Built-in Help**

Every Spectre.Console.Cli application gets automatic help. Run with `--help`:

```
dotnet run -- --help
``` 
The output shows your command's usage, the required `<name>` argument, and the optional `--count` flag with its description. All of this was generated from the attributes we added. The `[Description]` attributes appear right in the help text.

You didn't write any help-rendering code. It just works.

5.   5
**See Validation in Action**

Spectre.Console.Cli validates input automatically. Try passing an invalid count:

```
dotnet run -- Alice --count abc
``` 
The CLI shows an error explaining that `abc` isn't a valid integer. Try omitting the required name:

```
dotnet run
``` 
Again, a clear error message appears. This built-in validation saves you from writing repetitive error-handling code.

You've built a complete command-line application from scratch. Your CLI accepts arguments, supports options with defaults, displays auto-generated help, and validates user input - all with minimal code.

These same patterns scale to larger applications with multiple commands, complex arguments, and rich validation rules.

Looking to enhance your CLI app with rich console features? Check out these Spectre.Console tutorials:
