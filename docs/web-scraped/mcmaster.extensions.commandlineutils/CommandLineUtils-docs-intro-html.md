# Source: https://natemcmaster.github.io/CommandLineUtils/docs/intro.html

Title: Introduction

URL Source: https://natemcmaster.github.io/CommandLineUtils/docs/intro.html

Published Time: Thu, 05 Mar 2026 01:09:40 GMT

Markdown Content:
1.   [Documentation](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html)

**CommandLineUtils** is a library which helps developers implement command line applications. The primary goal of the library is to assist with parsing command line arguments and executing the correct commands related to those arguments. However, the library also provides various other utilities such as input helpers.

Installation[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html#installation)
--------------------------------------------------------------------------------------------

**CommandLineUtils** can be added to your project using NuGet. Follow instructions on [https://nuget.org/packages/McMaster.Extensions.CommandLineUtils](https://nuget.org/packages/McMaster.Extensions.CommandLineUtils) that match your project type or editor.

The two common ways to do this are:

1.   Using the [Package Manager Console](https://docs.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-in-visual-studio#package-manager-console):

```
Install-Package McMaster.Extensions.CommandLineUtils
```
[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html# "Copy")
2.   Using the [dotnet CLI](https://docs.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-using-the-dotnet-cli):

```
dotnet add package McMaster.Extensions.CommandLineUtils
```
[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html# "Copy")

Your first console application[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html#your-first-console-application)
--------------------------------------------------------------------------------------------------------------------------------

[Command Line Application](https://natemcmaster.github.io/CommandLineUtils/api/McMaster.Extensions.CommandLineUtils.CommandLineApplication.html) is the main entry point for most console apps parsing. There are two primary ways to use this API, using attributes or the builder pattern.

### Using Attributes[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html#using-attributes)

```
using System;
using McMaster.Extensions.CommandLineUtils;

public class Program
{
    public static int Main(string[] args)
        => CommandLineApplication.Execute<Program>(args);

    [Option(Description = "The subject")]
    public string Subject { get; }

    private void OnExecute()
    {
        var subject = Subject ?? "world";
        Console.WriteLine($"Hello {subject}!");
    }
}
```
[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html# "Copy")
### Using the Builder Pattern[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html#using-the-builder-pattern)

```
using System;
using McMaster.Extensions.CommandLineUtils;

public class Program
{
    public static int Main(string[] args)
    {
        var app = new CommandLineApplication();

        app.HelpOption();
        var subject = app.Option("-s|--subject <SUBJECT>", "The subject", CommandOptionType.SingleValue);
        subject.DefaultValue = "world";

        app.OnExecute(() =>
        {
            Console.WriteLine($"Hello {subject.Value()}!");
            return 0;
        });

        return app.Execute(args);
    }
}
```
[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html# "Copy")
Relationship to Microsoft.Extensions.Command Line Utils[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html#relationship-to-microsoftextensionscommandlineutils)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project is a fork of [Microsoft.Extensions.CommandLineUtils](https://github.com/aspnet/Common), which is no longer under [active development](https://github.com/aspnet/Common/issues/257). This project, on the other hand, will continue release updates and take contributions.

More information[](https://natemcmaster.github.io/CommandLineUtils/docs/intro.html#more-information)
----------------------------------------------------------------------------------------------------

For more information, you can refer to the sample applications.
