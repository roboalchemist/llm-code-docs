# Source: https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html

Title: Getting Started | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html

Markdown Content:
Paste these commands into your favorite terminal on Windows, Mac, or Linux. This will install the [Terminal.Gui.Templates](https://github.com/gui-cs/Terminal.Gui.templates), create a new "Hello World" TUI app, and run it.

(Press `Esc` to exit the app)

```
dotnet new install Terminal.Gui.Templates@2.0.0-beta.*
dotnet new tui-simple -n myproj
cd myproj
dotnet run
```

[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html# "Copy")
Adding Terminal.Gui to a Project[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html#adding-terminalgui-to-a-project)
-----------------------------------------------------------------------------------------------------------------------------------

To install Terminal.Gui from [Nuget](https://www.nuget.org/packages/Terminal.Gui) into a .NET Core project, use the `dotnet` CLI tool with this command.

```
dotnet add package Terminal.Gui
```

[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html# "Copy")
Using the Templates[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html#using-the-templates)
----------------------------------------------------------------------------------------------------------

Use the [Terminal.Gui.Templates](https://github.com/gui-cs/Terminal.Gui.templates):

```
dotnet new install Terminal.Gui.Templates@2.0.0-beta.*
```

[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html# "Copy")
Sample Usage in C#[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html#sample-usage-in-c)
-------------------------------------------------------------------------------------------------------

The following example shows a basic Terminal.Gui application using the modern instance-based model (this is `./Example/Example.cs`):

```
// A simple Terminal.Gui example in C# - using C# 9.0 Top-level statements

// This is a simple example application.  For the full range of functionality
// see the UICatalog project

using Terminal.Gui.App;
using Terminal.Gui.Configuration;
using Terminal.Gui.ViewBase;
using Terminal.Gui.Views;
using Terminal.Gui.Input;

// Override the default configuration for the application to use the Amber Phosphor theme
ConfigurationManager.RuntimeConfig = """{ "Theme": "Amber Phosphor" }""";
ConfigurationManager.Enable (ConfigLocations.All);

IApplication app = Application.Create ().Init ();
var userName = app.Run<ExampleWindow> ().GetResult<string> ();
app.Dispose ();

// To see this output on the screen it must be done after Dispose,
// which restores the previous screen.
if (string.IsNullOrEmpty (userName))
{
    Console.WriteLine (@"Login cancelled");
}
else
{
    Console.WriteLine ($@"Username: {userName}");
}

// Defines a top-level window with border and title
public sealed class ExampleWindow : Runnable<string?>
{
    public ExampleWindow ()
    {
        Title = $"Example App ({Application.GetDefaultKey (Command.Quit)} to quit)";

        // Create input components and labels
        var usernameLabel = new Label { Text = "Username:" };

        var userNameText = new TextField
        {
            // Position text field adjacent to the label
            X = Pos.Right (usernameLabel) + 1,

            // Fill remaining horizontal space
            Width = Dim.Fill ()
        };

        var passwordLabel = new Label { Text = "Password:", X = Pos.Left (usernameLabel), Y = Pos.Bottom (usernameLabel) + 1 };

        var passwordText = new TextField
        {
            Secret = true,

            // align with the text box above
            X = Pos.Left (userNameText),
            Y = Pos.Top (passwordLabel),
            Width = Dim.Fill ()
        };

        // Create login button
        var btnLogin = new Button
        {
            Text = "Login",
            Y = Pos.Bottom (passwordLabel) + 1,

            // center the login button horizontally
            X = Pos.Center (),
            IsDefault = true
        };

        // When login button is clicked display a message popup
        btnLogin.Accepting += (s, e) =>
                              {
                                  if (userNameText.Text == "admin" && passwordText.Text == "password")
                                  {
                                      MessageBox.Query (App!, "Logging In", "Login Successful", "Ok");
                                      Result = userNameText.Text;
                                      App!.RequestStop ();
                                  }
                                  else
                                  {
                                      MessageBox.ErrorQuery ((s as View)?.App!, "Logging In", "Incorrect username or password", "Ok");
                                  }

                                  // When Accepting is handled, set e.Handled to true to prevent further processing.
                                  e.Handled = true;
                              };

        // Add the views to the Window
        Add (usernameLabel, userNameText, passwordLabel, passwordText, btnLogin);
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html# "Copy")

### Key aspects of the modern model:[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html#key-aspects-of-the-modern-model)

* Use [Application.Create()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.Create.html) to create an [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) instance
* The application initializes automatically when you call `Run<T>()`
* Use `app.Run<ExampleWindow>()` to run a window that implements [IRunnable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IRunnable.html)
* Call `app.Dispose()` to clean up resources and restore the terminal
* Event handling uses [Accepting](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Accepting.html) event instead of legacy `Accept` event
* Set `e.Handled = true` in event handlers to prevent further processing

When run the application looks as follows:

[![Image 1: Simple Usage app](https://gui-cs.github.io/Terminal.Gui/images/Example.png)](https://gui-cs.github.io/Terminal.Gui/images/Example.png)

Building the Library and Running the Examples[](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html#building-the-library-and-running-the-examples)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

* Windows, Mac, and Linux - Build and run using the .NET SDK command line tools (`dotnet build` in the root directory). Run `UICatalog` with `dotnet run --project UICatalog`.
* Windows - Open `Terminal.sln` with Visual Studio 202x.
