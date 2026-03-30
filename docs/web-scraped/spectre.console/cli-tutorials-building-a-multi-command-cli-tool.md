# Source: https://spectreconsole.net/cli/tutorials/building-a-multi-command-cli-tool

Title: Building a Multi-Command CLI Tool

URL Source: https://spectreconsole.net/cli/tutorials/building-a-multi-command-cli-tool

Markdown Content:
In this tutorial, we'll build a package manager CLI together. By the end, we'll have a tool with multiple commands organized into a hierarchy, sharing common options across all of them.

1.   1
**Adding Multiple Commands**

Let's start by creating a new project and adding the Spectre.Console.Cli package:

```
dotnet new console -n PackageManager
cd PackageManager
dotnet add package Spectre.Console.Cli
``` 
Now replace `Program.cs` with two commands - one to add packages and one to list them:

```
internal class AddCommand : Command<AddCommand.Settings>
{
    public class Settings : CommandSettings
    {
        [CommandArgument(0, "<name>")]
        [Description("The package name to add")]
        public string PackageName { get; init; } = string.Empty;
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        System.Console.WriteLine($"Added package {settings.PackageName}");
        return 0;
    }
}
  
internal class ListCommand : Command<ListCommand.Settings>
{
    public class Settings : CommandSettings
    {
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        System.Console.WriteLine("Packages:");
        System.Console.WriteLine("  (none yet)");
        return 0;
    }
}
``` 
Wire them up using `CommandApp` with `Configure()`:

```
using Spectre.Console.Cli;
  
var app = new CommandApp();
app.Configure(config =>
{
    config.AddCommand<AddCommand>("add");
    config.AddCommand<ListCommand>("list");
});
return app.Run(args);
``` 
Run the commands:

```
dotnet run -- add Newtonsoft.Json
# Added package Newtonsoft.Json
  
dotnet run -- list
# Packages:
#   (none yet)
``` 
Both commands work. Try running `dotnet run -- --help` to see the auto-generated help listing both commands. The CLI knows about `add` and `list` without any extra configuration.

2.   2
**Organizing Commands with Branches**

Our `add` command works, but real CLIs often have subcommands. Let's refactor so users can run `add package` and `add reference` separately.

Update `Program.cs` to use `AddBranch()`:

```
internal class AddPackageCommand : Command<AddPackageCommand.Settings>
{
    public class Settings : CommandSettings
    {
        [CommandArgument(0, "<name>")]
        [Description("The package name to add")]
        public string PackageName { get; init; } = string.Empty;
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        System.Console.WriteLine($"Added package {settings.PackageName}");
        return 0;
    }
}
  
internal class AddReferenceCommand : Command<AddReferenceCommand.Settings>
{
    public class Settings : CommandSettings
    {
        [CommandArgument(0, "<path>")]
        [Description("The project reference path to add")]
        public string ReferencePath { get; init; } = string.Empty;
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        System.Console.WriteLine($"Added reference to {settings.ReferencePath}");
        return 0;
    }
}
  
internal class ListCommand : Command<ListCommand.Settings>
{
    public class Settings : CommandSettings
    {
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        System.Console.WriteLine("Packages:");
        System.Console.WriteLine("  (none yet)");
        System.Console.WriteLine("References:");
        System.Console.WriteLine("  (none yet)");
        return 0;
    }
}
``` 
Configure the branch structure:

```
using Spectre.Console.Cli;
  
var app = new CommandApp();
app.Configure(config =>
{
    config.AddBranch("add", add =>
    {
        add.AddCommand<AddPackageCommand>("package");
        add.AddCommand<AddReferenceCommand>("reference");
    });
    config.AddCommand<ListCommand>("list");
});
return app.Run(args);
``` 
Now the commands are organized hierarchically:

```
dotnet run -- add package Newtonsoft.Json
# Added package Newtonsoft.Json
  
dotnet run -- add reference ../MyLib/MyLib.csproj
# Added reference to ../MyLib/MyLib.csproj
  
dotnet run -- add --help
# Shows 'package' and 'reference' as subcommands
``` 
The `add` branch groups related commands together. Users can run `add --help` to discover what's available.

3.   3
**Complete CLI with Shared Settings**

Most CLIs have options that apply everywhere - things like `--verbose` or `--quiet`. Let's add a shared `--verbose` flag to all our commands.

Create a base settings class that other settings inherit from:

```
internal class GlobalSettings : CommandSettings
{
    [CommandOption("-v|--verbose")]
    [Description("Enable verbose output")]
    [DefaultValue(false)]
    public bool Verbose { get; init; }
}
  
internal class AddPackageCommand : Command<AddPackageCommand.Settings>
{
    public class Settings : GlobalSettings
    {
        [CommandArgument(0, "<name>")]
        [Description("The package name to add")]
        public string PackageName { get; init; } = string.Empty;
  
        [CommandOption("--version")]
        [Description("The package version (default: latest)")]
        public string? Version { get; init; }
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        var version = settings.Version ?? "latest";
  
        if (settings.Verbose)
        {
            System.Console.WriteLine($"Searching for package {settings.PackageName}...");
            System.Console.WriteLine($"Resolving version {version}...");
            System.Console.WriteLine($"Installing to ./packages...");
        }
  
        System.Console.WriteLine($"Added package {settings.PackageName} v{version}");
        return 0;
    }
}
  
internal class AddReferenceCommand : Command<AddReferenceCommand.Settings>
{
    public class Settings : GlobalSettings
    {
        [CommandArgument(0, "<path>")]
        [Description("The project reference path to add")]
        public string ReferencePath { get; init; } = string.Empty;
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        if (settings.Verbose)
        {
            System.Console.WriteLine($"Validating project at {settings.ReferencePath}...");
            System.Console.WriteLine($"Adding reference to project file...");
        }
  
        System.Console.WriteLine($"Added reference to {settings.ReferencePath}");
        return 0;
    }
}
  
internal class ListCommand : Command<ListCommand.Settings>
{
    public class Settings : GlobalSettings
    {
    }
  
    protected override int Execute(CommandContext context, Settings settings, CancellationToken cancellation)
    {
        if (settings.Verbose)
        {
            System.Console.WriteLine("Reading project file...");
        }
  
        System.Console.WriteLine("Packages:");
        System.Console.WriteLine("  Newtonsoft.Json (13.0.1)");
        System.Console.WriteLine("References:");
        System.Console.WriteLine("  ../MyLib/MyLib.csproj");
        return 0;
    }
}
``` 
The configuration stays the same - each command's settings inherit from `GlobalSettings`:

```
using Spectre.Console.Cli;
  
var app = new CommandApp();
app.Configure(config =>
{
    config.AddBranch("add", add =>
    {
        add.AddCommand<AddPackageCommand>("package");
        add.AddCommand<AddReferenceCommand>("reference");
    });
    config.AddCommand<ListCommand>("list");
});
return app.Run(args);
``` 
The `--verbose` flag now works across all commands:

```
dotnet run -- add package Serilog --version 3.0.0 --verbose
# Searching for package Serilog...
# Resolving version 3.0.0...
# Installing to ./packages...
# Added package Serilog v3.0.0
  
dotnet run -- list --verbose
# Reading project file...
# Packages:
#   Newtonsoft.Json (13.0.1)
# References:
#   ../MyLib/MyLib.csproj
``` 
Settings inheritance keeps your code DRY. Define common options once, use them everywhere.

These same patterns scale to CLIs with dozens of commands and deep nesting.
