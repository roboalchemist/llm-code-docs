# Source: https://cobra.dev/docs/tutorials/12-factor-app/

Title: Building a 12-Factor App with Viper Integration

URL Source: https://cobra.dev/docs/tutorials/12-factor-app/

Markdown Content:
Have you ever hardcoded a port number, an API key, or a file path into a tool? It works fine on your machine, but then you need to share it. Suddenly, you’re editing code to change a setting for a colleague or recompiling to run in a different environment. This approach is brittle and doesn’t scale.

The **Twelve-Factor App** methodology offers a solution with its third factor: **Config**. It advises storing configuration in the environment, completely separate from your application code. For a command-line interface (CLI), this means creating a tool that is flexible and easy for both humans and automation to use.

A professional CLI should allow configuration to be specified from multiple sources with a clear order of precedence. A user might set a default in a config file, a CI/CD pipeline might override it with an environment variable, and a developer might override it again for a single run with a command-line flag.

In this tutorial, you’ll learn a powerful and reusable pattern to achieve this. We’ll use two of the most popular libraries in the Go ecosystem:

*   **Cobra** for building a powerful command structure and parsing flags.
*   **Viper** for handling configuration from multiple sources.

Together, they allow us to build CLIs that are a pleasure to use and maintain.

* * *

### The Goal: A Clear Precedence

We will build a simple server application that needs to know which port to run on. Our goal is to source this `port` configuration with the following priority, from highest to lowest:

1.   **Command-line flag** (e.g., `--port 3000`)
2.   **Environment variable** (e.g., `MYAPP_PORT=9000`)
3.   **Configuration file** (e.g., `port: 8081` in `config.yaml`)
4.   **A sensible default** (e.g., `8080`)

This hierarchy ensures that ephemeral, specific settings (like a flag) always win, while persistent, general settings (like a config file) provide a convenient baseline.

* * *

### Prerequisites

Before we start, you should have:

*   Go version 1.20 or newer installed.
*   Basic familiarity with Go and creating a simple application.
*   A shell environment (the examples use a Unix-like shell).

* * *

### Step 1: Laying the Foundation

First, let’s create a new Go project and initialize it as a Cobra application.

`# Create a directory for our project``mkdir myapp && cd myapp``# Initialize a Go module``go mod init [example.com/myapp](https://www.google.com/search?q=https://example.com/myapp)``# Install the Cobra generator``go install [github.com/spf13/cobra-cli@latest](https://www.google.com/search?q=https://github.com/spf13/cobra-cli%40latest)``# Create the basic application structure``cobra-cli init`

The `cobra-cli init` command scaffolds a simple application for us. Your project directory should now look like this:

```
.
├── cmd/
│   └── root.go
├── go.mod
└── main.go
```

Next, add Viper to our project. It will be the workhorse for managing our configuration values.

`go get [github.com/spf13/viper@latest](https://www.google.com/search?q=https://github.com/spf13/viper%40latest)`

* * *

### Step 2: Defining Commands and Flags

Our application will have a `serve` command that starts the server. We also want a global `--config` flag so users can specify a configuration file.

Let’s create the `serve` command first.

`cobra-cli add serve`

This creates a new file, `cmd/serve.go`. Now, let’s edit `cmd/root.go` and `cmd/serve.go` to define our flags. For now, we are just defining them; we will wire them up to Viper in the next step.

Here is the `cmd/serve.go` file. Notice we define the `--port` flag with its default value. The `RunE` function gets its configuration from Viper, not directly from the flag.

cmd/serve.go

go

```
package cmd

import (
"fmt"
"[github.com/spf13/cobra](https://github.com/spf13/cobra)"
"[github.com/spf13/viper](https://github.com/spf13/viper)"
)

var serveCmd = \&cobra.Command{
Use:   "serve",
Short: "Starts the server",
RunE: func(cmd \*cobra.Command, args []string) error {
// We get the configuration value from Viper, not from the flag directly.
port := viper.GetInt("port")
fmt.Printf("Starting server on port: %d\\n", port)
// In a real app, you would start a server here.
return nil
},
}

func init() {
rootCmd.AddCommand(serveCmd)

```
// Define a local flag for the 'serve' command.
serveCmd.Flags().Int("port", 8080, "Port to run the server on")
```

}
```

And here is the `cmd/root.go` file, where we’ll add the persistent `--config` flag.

cmd/root.go

go

```
package cmd

import (
"fmt"
"os"
"[github.com/spf13/cobra](https://github.com/spf13/cobra)"
)

var (
// Used for flags.
cfgFile string

```
rootCmd = &cobra.Command{
	Use:   "myapp",
	Short: "A demo application for Cobra and Viper",
}
```

)

func Execute() {
if err := rootCmd.Execute(); err \!= nil {
os.Exit(1)
}
}

func init() {
// Add the persistent --config flag to the root command.
rootCmd.PersistentFlags().StringVar(\&cfgFile, "config", "", "config file (default is $HOME/.myapp.yaml)")
}
```

* * *

### Step 3: The Heart of the Pattern: `PersistentPreRunE`

We need a single, central place to orchestrate our configuration logic. This logic must run after flags are parsed but _before_ our command’s `RunE` function executes. Cobra provides the perfect hook for this: `PersistentPreRunE`.

By adding this function to our `rootCmd`, we guarantee it runs for any subcommand the user executes. This is where we will tell Viper how to find and prioritize configuration. Let’s update `cmd/root.go` with our complete configuration logic.

cmd/root.go

go

```
package cmd

import (
"errors"
"fmt"
"os"
"strings"

```
"[github.com/spf13/cobra](https://github.com/spf13/cobra)"
"[github.com/spf13/viper](https://github.com/spf13/viper)"
```

)

var (
cfgFile string

```
rootCmd = &cobra.Command{
	Use:   "myapp",
	Short: "A demo application for Cobra and Viper",
	// PersistentPreRunE is called after flags are parsed but before the
	// command's RunE function is called.
	PersistentPreRunE: func(cmd *cobra.Command, args []string) error {
		return initializeConfig(cmd)
	},
}
```

)

func Execute() {
if err := rootCmd.Execute(); err \!= nil {
fmt.Fprintln(os.Stderr, err)
os.Exit(1)
}
}

func init() {
rootCmd.PersistentFlags().StringVar(\&cfgFile, "config", "", "config file (default locations: ., $HOME/.myapp/)")
}

func initializeConfig(cmd \*cobra.Command) error {
// 1. Set up Viper to use environment variables.
viper.SetEnvPrefix("MYAPP")
// Allow for nested keys in environment variables (e.g. `MYAPP_DATABASE_HOST`)
viper.SetEnvKeyReplacer(strings.NewReplacer(".", "*", "-", "*"))
viper.AutomaticEnv()

```
// 2. Handle the configuration file.
if cfgFile != "" {
	// Use config file from the flag.
	viper.SetConfigFile(cfgFile)
} else {
	// Search for a config file in default locations.
	home, err := os.UserHomeDir()
	// Only panic if we can't get the home directory.
	cobra.CheckErr(err)

	// Search for a config file with the name "config" (without extension).
	viper.AddConfigPath(".")
	viper.AddConfigPath(home + "/.myapp")
	viper.SetConfigName("config")
	viper.SetConfigType("yaml")
}

// 3. Read the configuration file.
// If a config file is found, read it in. We use a robust error check
// to ignore "file not found" errors, but panic on any other error.
if err := viper.ReadInConfig(); err != nil {
	// It's okay if the config file doesn't exist.
	var configFileNotFoundError viper.ConfigFileNotFoundError
	if !errors.As(err, &configFileNotFoundError) {
		return err
	}
}

// 4. Bind Cobra flags to Viper.
// This is the magic that makes the flag values available through Viper.
// It binds the full flag set of the command passed in.
err := viper.BindPFlags(cmd.Flags())
if err != nil {
	return err
}

// This is an optional but useful step to debug your config.
fmt.Println("Configuration initialized. Using config file:", viper.ConfigFileUsed())
return nil
```

}
```

#### **Why This Works**

*   **Centralized Logic:** All configuration is handled in one place, `initializeConfig`, making it easy to understand and modify. The logic is called from `PersistentPreRunE` so it always runs before any command logic.
*   **Environment Variables First:** By calling `viper.AutomaticEnv()` early, we set up the ability to read from the environment. The `SetEnvPrefix` and `SetEnvKeyReplacer` calls ensure variables like `MYAPP_PORT` correctly map to the `port` key.
*   **Flexible Config File:** The logic first checks for a user-provided `--config` file. If it’s missing, it gracefully searches in common locations (`.` and `$HOME/.myapp`). We explicitly ignore the “file not found” error, allowing the application to run without a config file.
*   **Connecting Flags to Viper:**`viper.BindPFlags(cmd.Flags())` is the crucial link. It tells Viper: “For any key you’re asked for, like `port`, first check if a Cobra flag named `port` was set. If so, use that value.” This is how flags get top priority.
*   **Clean Command Code:** Our command logic in `serve.go` remains pristine. It doesn’t need to know _where_ the `port` value came from. It just asks Viper: `viper.GetInt("port")`.

* * *

### Step 4: Seeing It All Work: Precedence in Action

Let’s test our new, robust configuration system. First, create a configuration file named `config.yaml` in the root of your project.

config.yaml

yaml

`port: 8081`

Now, build the binary:

`go build -o myapp`

Let’s walk through the different scenarios to demonstrate the precedence order.

#### **Case A: Using the Default Value**

We run the command with no flags, environment variables, or config file.

`# Run from a directory without config.yaml to test the default``(cd /tmp && /path/to/your/project/myapp serve)`

**Output:**

```
Configuration initialized. Using config file:
Starting server on port: 8080
```

**Result:** We get the default value (`8080`) defined in the flag in `serve.go`.

#### **Case B: Using the Config File**

Now, run from our project directory where `config.yaml` exists.

`./myapp serve`

**Output:**

```
Configuration initialized. Using config file: /path/to/your/project/config.yaml
Starting server on port: 8081
```

**Result:** The value from the file (`8081`) overrides the default (`8080`).

#### **Case C: Using an Environment Variable**

The environment variable takes precedence over the config file.

`MYAPP\_PORT=9000 ./myapp serve`

**Output:**

```
Configuration initialized. Using config file: /path/to/your/project/config.yaml
Starting server on port: 9000
```

**Result:** The environment variable (`9000`) overrides the file value (`8081`).

#### **Case D: Using a Command-Line Flag**

The flag is the ultimate override, winning against all other sources.

`./myapp serve --port=3000`

**Output:**

```
Configuration initialized. Using config file: /path/to/your/project/config.yaml
Starting server on port: 3000
```

**Result:** The flag’s value (`3000`) overrides all other sources.

* * *

### Conclusion: A Pattern for Growth

You’ve now implemented a professional configuration pattern that makes your Go CLIs robust, predictable, and easy to use. 🚀

By using Cobra’s `PersistentPreRunE` hook to orchestrate Viper, you have:

*   A **single source of truth** for configuration values in your application logic (e.g., `viper.Get...`).
*   A **clear and logical precedence**: Flags > Environment Variables > Config File > Defaults.
*   A **clean separation** between your application’s code and its configuration.

This pattern is the foundation for building much larger applications. You can add more commands, define more flags, and expand your `config.yaml` with nested keys (e.g., `database.host`). For even larger projects, consider moving the `initializeConfig` function and related logic into its own `config` package to further separate concerns. The core logic remains the same, providing a solid, testable, and maintainable base for your project’s future.
