# Source: https://cobra.dev/docs/tutorials/customizing-cli/

Title: Customizing Your CLI

URL Source: https://cobra.dev/docs/tutorials/customizing-cli/

Markdown Content:
In this tutorial, we’ll build upon the basic CLI from the [previous tutorial](https://cobra.dev/docs/tutorials/first-cli/) and add customization features like flags, custom descriptions, and configuration options.

Prerequisites
-------------

*   Completed the [My First CLI](https://cobra.dev/docs/tutorials/first-cli/) tutorial
*   Your `my-cli` project from the previous tutorial

Steps
-----

1.   **Customize the Root Command Description**

Let’s start by updating the main application description. Open the `cmd/root.go` file and see how we transform a basic command into a professional one:

2.   **Add Global Flags**

Let’s see how adding global flags transforms your CLI from basic to feature-rich. Here’s how the `init()` function evolves:

3.   **Enhance the Serve Command**

Watch how a simple serve command evolves into a fully-featured server command with flags and verbose output:

4.   **Test Your Enhanced CLI**

Build and test your updated CLI:

`go build -o my-cli``./my-cli --help``A powerful CLI tool built with Cobra``My CLI is a demonstration application built with Cobra.``This application shows how to create professional command-line``tools with proper flag handling, subcommands, and configuration.``Usage:``my-cli [command]``Available Commands:``completion  Generate the autocompletion script for the specified shell``help        Help about any command``serve       Start the application server``Flags:``-h, --help      help for my-cli``-t, --toggle    Help message for toggle``-v, --verbose   verbose output` 
5.   **Test the Serve Command with Flags**

Try out the serve command with different flag combinations:

`./my-cli serve --help``Start the application server on the specified host and port.``The serve command will start a web server that can handle requests``and provide API endpoints for your application.``Usage:``my-cli serve [flags]``Flags:``-h, --help          help for serve``-H, --host string   Host to bind the server to (default "localhost")``-p, --port int      Port to run the server on (default 8080)``Global Flags:``-v, --verbose   verbose output` 
Test with custom port and verbose mode:

`./my-cli serve --port 3000 --host 0.0.0.0 --verbose``Starting server on 0.0.0.0:3000``Verbose mode enabled` 
6.   **Add Input Validation**

See how adding validation transforms your command from basic functionality to production-ready code:

Summary
-------

In this tutorial, you’ve learned how to:

*   Customize command descriptions with the `Short` and `Long` fields
*   Add global flags that work across all commands using `PersistentFlags()`
*   Create command-specific flags with `Flags()`
*   Use different flag types (`bool`, `int`, `string`)
*   Implement flag shortcuts with single letters
*   Add basic input validation
*   Access global flags from subcommands

Your CLI now has proper help text, configurable options, and professional command-line behavior!

Next Steps
----------

*   Try adding more commands with `cobra-cli add [command-name]`
*   Explore configuration files with Viper integration
*   Add persistent configuration and environment variable support
