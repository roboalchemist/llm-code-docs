# Source: https://cobra.dev/docs/tutorials/getting-started/

Title: Getting Started with Cobra

URL Source: https://cobra.dev/docs/tutorials/getting-started/

Markdown Content:
Welcome to Cobra! This tutorial will guide you through the essentials of installing Cobra and creating your first command-line application. By the end of this tutorial, you’ll have a working CLI application with your own custom command.

Prerequisites
-------------

Before we begin, make sure you have:

*   Go 1.21 or later installed on your system
*   Basic familiarity with Go development
*   A terminal or command prompt

Step 1: Install Cobra and cobra-cli
-----------------------------------

First, let’s install the Cobra library and the cobra-cli tool that will help us generate our application structure:

`go get -u github.com/spf13/cobra@latest`

`go install github.com/spf13/cobra-cli@latest`

The first command adds Cobra as a dependency, while the second installs the cobra-cli generator tool that makes creating new applications and commands much easier.

Step 2: Create Your Application
-------------------------------

Now let’s create your first CLI application using the cobra-cli tool:

`cobra-cli init my-cli``Your Cobra application is ready at my-cli``Add commands to your application by using the `add` command`

This creates a new directory called `my-cli` with a complete Go module and basic Cobra application structure. Let’s explore what was created:

`cd my-cli``ls -la``total 16``drwxr-xr-x   6 user  staff   192 Aug 10 12:00 .``drwxr-xr-x   3 user  staff    96 Aug 10 12:00 ..``drwxr-xr-x   3 user  staff    96 Aug 10 12:00 cmd``-rw-r--r--   1 user  staff    87 Aug 10 12:00 go.mod``-rw-r--r--   1 user  staff   155 Aug 10 12:00 go.sum``-rw-r--r--   1 user  staff   615 Aug 10 12:00 main.go`

Step 3: Test Your Base Application
----------------------------------

Let’s test the basic application that was generated:

`go run main.go``A longer description that spans multiple lines and likely contains``examples and usage of using your application. For example:``Cobra is a CLI library for Go that empowers applications.``This application is a tool to generate the needed files``to quickly create a Cobra application.`

Great! Your base application is working. You can also test the built-in help:

`go run main.go --help``A longer description that spans multiple lines and likely contains``examples and usage of using your application. For example:``Cobra is a CLI library for Go that empowers applications.``This application is a tool to generate the needed files``to quickly create a Cobra application.``Usage:``my-cli [flags]``Flags:``-h, --help   help for my-cli`

Step 4: Add Your First Command
------------------------------

Now let’s add a custom command to make your CLI more interesting:

`cobra-cli add hello``hello created at cmd/hello.go`

This creates a new file `cmd/hello.go` with a `hello` command. Let’s test it:

`go run main.go hello``hello called`

Perfect! You now have a working command. Let’s see how it appears in the help:

`go run main.go --help``A longer description that spans multiple lines and likely contains``examples and usage of using your application. For example:``Cobra is a CLI library for Go that empowers applications.``This application is a tool to generate the needed files``to quickly create a Cobra application.``Usage:``my-cli [command]``Available Commands:``completion  Generate the autocompletion script for the specified shell``hello       A brief description of your command``help        Help about any command``Flags:``-h, --help   help for my-cli``Use "my-cli [command] --help" for more information about a command.`

Step 5: Customize Your Command
------------------------------

Let’s make the hello command more interesting by editing the generated file. Open `cmd/hello.go` and you’ll see the basic structure that cobra-cli created.

The key part is the `Run` function where you can add your custom logic:

`go run main.go hello``Hello from your new Cobra CLI application!`

You can also add flags to your command. Try the built-in help for your hello command:

`go run main.go hello --help``A brief description of your command``Usage:``my-cli hello [flags]``Flags:``-h, --help   help for hello`

Step 6: Build Your Application
------------------------------

Finally, let’s build your CLI application into an executable:

`go build -o my-cli``./my-cli hello``Hello from your new Cobra CLI application!`

Next Steps
----------

Now that you have a working Cobra application, you can:

*   Add more commands with `cobra-cli add [command-name]`
*   Learn about flags and arguments in the [My First CLI](https://cobra.dev/docs/tutorials/my-first-cli) tutorial
*   Explore command customization in the [Customizing Your CLI](https://cobra.dev/docs/tutorials/customizing-your-cli) tutorial
*   Read the [User Guide](https://cobra.dev/docs/user-guide/) for comprehensive documentation

Happy coding with Cobra!
