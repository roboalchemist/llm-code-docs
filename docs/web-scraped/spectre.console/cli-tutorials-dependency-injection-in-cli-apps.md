# Source: https://spectreconsole.net/cli/tutorials/dependency-injection-in-cli-apps

Title: Dependency Injection in CLI Apps

URL Source: https://spectreconsole.net/cli/tutorials/dependency-injection-in-cli-apps

Markdown Content:
In this tutorial, we'll add dependency injection to a CLI application. By the end, we'll have commands that receive services through their constructors - making them easier to test and more flexible.

The greeting logic lives in an injectable service, not hard-coded in the command.

1.   1
Starting Without DI
-------------------

Let's start by creating a project and building a simple greeting command:

```
dotnet new console -n GreetingApp
cd GreetingApp
dotnet add package Spectre.Console.Cli
``` 
Replace `Program.cs` with a greeting command that has the logic built right in:

```
public class GreetSettings : CommandSettings
{
    [CommandArgument(0, "<name>")]
    [Description("The name to greet")]
    public string Name { get; init; } = string.Empty;
  
    [CommandOption("-f|--formal")]
    [Description("Use formal greeting")]
    [DefaultValue(false)]
    public bool Formal { get; init; }
}
  
internal class GreetCommand : Command<GreetSettings>
{
    protected override int Execute(CommandContext context, GreetSettings settings, CancellationToken cancellation)
    {
        // Greeting logic is hard-coded here - not ideal for testing or flexibility
        if (settings.Formal)
        {
            AnsiConsole.WriteLine($"Good day, {settings.Name}.");
        }
        else
        {
            AnsiConsole.WriteLine($"Hello, {settings.Name}!");
        }
        return 0;
    }
}
``` 
Wire it up in your entry point:

```
using Spectre.Console.Cli;
  
var app = new CommandApp<GreetCommand>();
return app.Run(args);
``` 
Run the application:

```
dotnet run -- Alice
# Hello, Alice!
  
dotnet run -- Alice --formal
# Good day, Alice.
``` 
This works, but the greeting logic is embedded in the command. If we wanted to test this command, we'd have no way to substitute different greeting behavior. Let's fix that.

2.   2
Adding Dependency Injection
---------------------------

First, add the Microsoft DI package:

```
dotnet add package Microsoft.Extensions.DependencyInjection
``` 
Now we'll create a service interface, an implementation, and the bridge classes that connect Microsoft's DI container to Spectre.Console.Cli:

```
public interface IGreetingService
{
    string GetGreeting(string name, bool formal);
}
  
public class GreetingService : IGreetingService
{
    public string GetGreeting(string name, bool formal)
    {
        return formal
            ? $"Good day, {name}."
            : $"Hello, {name}!";
    }
}
  
public sealed class TypeRegistrar(IServiceCollection services) : ITypeRegistrar
{
    public ITypeResolver Build() => new TypeResolver(services.BuildServiceProvider());
  
    public void Register(Type service, Type implementation) => services.AddSingleton(service, implementation);
  
    public void RegisterInstance(Type service, object implementation) => services.AddSingleton(service, implementation);
  
    public void RegisterLazy(Type service, Func<object> factory) => services.AddSingleton(service, _ => factory());
}
  
public sealed class TypeResolver(IServiceProvider provider) : ITypeResolver
{
    public object? Resolve(Type? type) => type == null ? null : provider.GetService(type);
}
``` 
Update the command to accept the service through its constructor:

```
internal class GreetCommand : Command<GreetSettings>
{
    private readonly IGreetingService _greetingService;
    private readonly IAnsiConsole _console;
  
    public GreetCommand(IGreetingService greetingService, IAnsiConsole console)
    {
        _greetingService = greetingService;
        _console = console;
    }
  
    protected override int Execute(CommandContext context, GreetSettings settings, CancellationToken cancellation)
    {
        var greeting = _greetingService.GetGreeting(settings.Name, settings.Formal);
        _console.WriteLine(greeting);
        return 0;
    }
}
``` 
Finally, configure the DI container and pass the registrar to `CommandApp`:

```
using Microsoft.Extensions.DependencyInjection;
using Spectre.Console.Cli;
  
var services = new ServiceCollection();
services.AddSingleton<IGreetingService, GreetingService>();
  
var registrar = new TypeRegistrar(services);
var app = new CommandApp<GreetCommand>(registrar);
return app.Run(args);
``` 
Run it again:

```
dotnet run -- Alice
# Hello, Alice!
``` 
The output looks the same, but now the greeting logic is in a separate service. The framework automatically injects `IGreetingService` into the command's constructor.

`IAnsiConsole` is automatically registered and can be injected into your commands. Using it instead of the static `AnsiConsole` makes your commands testable. See [Test Console Output](https://spectreconsole.net/console/how-to/testing-console-output) to learn how to use `TestConsole` in unit tests.

3.   3
Keyed Services with Factory Pattern
-----------------------------------

Now let's take it further with [.NET 8+ keyed services](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection#keyed-services). Instead of one service handling all styles, we'll create separate implementations for each greeting style and use a factory to select the right one at runtime.

First, define the greeting style enum and a simplified service interface:

```
public enum GreetingStyle
{
    Casual,
    Formal,
    Enthusiastic
}
  
public interface IGreetingService
{
    string GetGreeting(string name);
}
``` 
Create three service implementations - one for each style:

```
public class CasualGreetingService : IGreetingService
{
    public string GetGreeting(string name) => $"Hello, {name}!";
}
  
public class FormalGreetingService : IGreetingService
{
    public string GetGreeting(string name) => $"Good day, {name}.";
}
  
public class EnthusiasticGreetingService : IGreetingService
{
    public string GetGreeting(string name) => $"Hey there, {name}! Great to see you!";
}
``` 
Now the key piece: a factory that receives the command's `Settings` through DI (Spectre.Console.Cli registers them automatically) and uses keyed services to resolve the correct implementation:

```
public interface IGreetingFactory
{
    IGreetingService Create();
}
  
public class GreetingFactory(IServiceProvider serviceProvider, GreetCommand.Settings settings)
    : IGreetingFactory
{
    public IGreetingService Create()
    {
        return serviceProvider.GetRequiredKeyedService<IGreetingService>(settings.Style);
    }
}
``` 
The command becomes very clean - it just asks the factory for a service:

```
public class GreetCommand : Command<GreetCommand.Settings>
{
    private readonly IGreetingFactory _greetingFactory;
    private readonly IAnsiConsole _console;
  
    public GreetCommand(IGreetingFactory greetingFactory, IAnsiConsole console)
    {
        _greetingFactory = greetingFactory;
        _console = console;
    }
  
    public class Settings : CommandSettings
    {
        [CommandArgument(0, "<name>")]
        [Description("The name to greet")]
        public string Name { get; init; } = string.Empty;
  
        [CommandOption("-s|--style")]
        [Description("The greeting style to use (Casual, Formal, or Enthusiastic)")]
        [DefaultValue(GreetingStyle.Casual)]
        public GreetingStyle Style { get; init; }
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        var service = _greetingFactory.Create();
        var greeting = service.GetGreeting(settings.Name);
        _console.WriteLine(greeting);
        return 0;
    }
}
``` 
Register everything with keyed services in your entry point:

```
using Microsoft.Extensions.DependencyInjection;
using Spectre.Console.Cli;
  
var services = new ServiceCollection();
  
// Register keyed greeting services - each style gets its own implementation
services.AddKeyedSingleton<IGreetingService, CasualGreetingService>(GreetingStyle.Casual);
services.AddKeyedSingleton<IGreetingService, FormalGreetingService>(GreetingStyle.Formal);
services.AddKeyedSingleton<IGreetingService, EnthusiasticGreetingService>(GreetingStyle.Enthusiastic);
  
// Register the factory that resolves the appropriate service based on settings
services.AddScoped<IGreetingFactory, GreetingFactory>();
  
var registrar = new TypeRegistrar(services);
var app = new CommandApp<GreetCommand>(registrar);
return app.Run(args);
``` 
The `TypeRegistrar` and `TypeResolver` stay the same - they're reusable infrastructure.

Try all the greeting styles using the `--style` option:

```
dotnet run -- Alice
# Hello, Alice!
  
dotnet run -- Alice --style Formal
# Good day, Alice.
  
dotnet run -- Alice --style Enthusiastic
# Hey there, Alice! Great to see you!
``` 
This pattern has several advantages:

    *   **Single responsibility**: Each service implementation does one thing well
    *   **Extensible**: Add new styles by creating a new service and registering it with a key
    *   **Testable**: Mock the factory or individual services easily
    *   **Settings injection**: The factory receives parsed command settings via DI, keeping the command code clean

This same pattern works for any service: loggers, database connections, HTTP clients, configuration providers, and more.
