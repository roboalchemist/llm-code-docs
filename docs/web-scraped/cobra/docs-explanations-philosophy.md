# Source: https://cobra.dev/docs/explanations/philosophy/

Title: Philosophy of Cobra

URL Source: https://cobra.dev/docs/explanations/philosophy/

Markdown Content:
Cobra’s design is guided by three foundational principles that shape every aspect of the library. Understanding these principles will help you build better CLI applications and make decisions that align with Cobra’s philosophy.

CLI as a User Interface
-----------------------

The command-line interface is not just a technical necessity—it’s a user experience. Cobra treats the CLI as a first-class user interface, applying the same design principles you would use for any other interface.

### User-Centered Design

Just as graphical interfaces prioritize usability, your CLI should be intuitive, discoverable, and helpful. Users should be able to explore your application naturally through help commands, tab completion, and logical command hierarchies.

go

```
var rootCmd = &cobra.Command{
  Use:   "myapp",
  Short: "A brief description of your application",
  Long: `A longer description that spans multiple lines and provides
comprehensive information about what your application does, how to use it,
and any important details users should know.`,
}

var userCmd = &cobra.Command{
  Use:   "user",
  Short: "User management commands",
  Long:  `Commands for creating, updating, and managing user accounts.`,
}
```

### Discoverability and Help

Users should never feel lost. Cobra’s built-in help system, combined with thoughtful command organization, creates a self-documenting interface.

`myapp --help``A longer description that spans multiple lines and provides``comprehensive information about what your application does``Usage:``myapp [command]``Available Commands:``completion  Generate completion script``help        Help about any command``user        User management commands``Flags:``-h, --help     help for myapp``-v, --version  version for myapp`

### Consistency and Predictability

Users develop mental models of how your CLI works. Consistent patterns in command naming, flag usage, and output formatting reduce cognitive load and improve the overall experience.

Convention Over Configuration
-----------------------------

Cobra reduces decision fatigue by providing sensible defaults and established patterns. When you follow Cobra’s conventions, you get powerful functionality with minimal configuration.

### Sensible Defaults

Rather than forcing developers to configure every detail, Cobra provides defaults that work well in most scenarios. You can override these when needed, but the defaults let you focus on your application logic.

go

```
// Minimal command definition with powerful built-in features
var createCmd = &cobra.Command{
  Use:   "create [name]",
  Short: "Create a new resource",
  Args:  cobra.ExactArgs(1),
  Run: func(cmd *cobra.Command, args []string) {
    fmt.Printf("Creating %s\n", args[0])
  },
}
```

This simple command automatically gets:

*   Help generation
*   Argument validation
*   Error handling
*   Integration with the parent command structure

### Established Patterns

Following common CLI patterns makes your application familiar to users. Cobra encourages patterns like:

*   Hierarchical command structures (`git commit` vs `git commit --amend`)
*   Standard flag conventions (`--verbose`, `--help`, `--version`)
*   Consistent argument handling

go

```
// Following established patterns
var commitCmd = &cobra.Command{
  Use:   "commit",
  Short: "Record changes to the repository",
  Run: func(cmd *cobra.Command, args []string) {
    // Implementation
  },
}

func init() {
  commitCmd.Flags().BoolP("all", "a", false, "Stage all changes")
  commitCmd.Flags().StringP("message", "m", "", "Commit message")
  rootCmd.AddCommand(commitCmd)
}
```

### Configuration Hierarchy

When configuration is needed, Cobra supports a clear hierarchy: flags override environment variables, which override configuration files, which override defaults.

`myapp deploy --env production``MYAPP_ENV=production myapp deploy``myapp deploy  # Uses config file or default`

Batteries Included, But Swappable
---------------------------------

Cobra comes with everything you need to build a professional CLI, but every component can be customized or replaced when your needs go beyond the defaults.

### Rich Built-in Features

Out of the box, Cobra provides:

*   **Command parsing and routing**
*   **Flag handling with automatic help generation**
*   **Shell completion for bash, zsh, fish, and PowerShell**
*   **Man page generation**
*   **Markdown documentation generation**

go

```
// Rich functionality with minimal code
func Execute() {
  err := rootCmd.Execute()
  if err != nil {
    os.Exit(1)
  }
}

func init() {
  // Built-in shell completion
  rootCmd.CompletionOptions.DisableDefaultCmd = false
}
```

### Extensible Architecture

When the built-in features don’t meet your specific needs, Cobra’s architecture allows you to customize or replace components:

go

```
// Custom help command
cmd.SetHelpCommand(&cobra.Command{
  Use:   "help [command]",
  Short: "Help about any command",
  Run: func(c *cobra.Command, args []string) {
    // Custom help implementation
  },
})

// Custom usage template
cmd.SetUsageTemplate(`Custom Usage:
  {{.UseLine}}{{if .HasAvailableSubCommands}}

Available Commands:{{range .Commands}}{{if (or .IsAvailableCommand (eq .Name "help"))}}
  {{rpad .Name .NamePadding }} {{.Short}}{{end}}{{end}}{{end}}
`)
```

### Integration Points

Cobra provides clear integration points for common needs:

*   **Custom validators for arguments and flags**
*   **Hooks for pre and post command execution**
*   **Custom completion functions**
*   **Integration with configuration libraries like Viper**

go

```
var createCmd = &cobra.Command{
  Use:   "create [name]",
  Short: "Create a new resource",
  Args: func(cmd *cobra.Command, args []string) error {
    // Custom validation logic
    if len(args) != 1 {
      return fmt.Errorf("requires exactly one argument")
    }
    if !isValidName(args[0]) {
      return fmt.Errorf("invalid name format")
    }
    return nil
  },
  PreRun: func(cmd *cobra.Command, args []string) {
    // Pre-execution setup
    log.Printf("Starting creation of %s", args[0])
  },
  Run: func(cmd *cobra.Command, args []string) {
    // Main execution
  },
  PostRun: func(cmd *cobra.Command, args []string) {
    // Post-execution cleanup
    log.Printf("Completed creation of %s", args[0])
  },
}
```

Putting It All Together
-----------------------

These three principles work together to create a development experience that is both productive and flexible:

1.   **CLI as UI** ensures your applications are user-friendly and discoverable
2.   **Convention Over Configuration** lets you build powerful CLIs with minimal boilerplate
3.   **Batteries Included, But Swappable** provides immediate productivity with long-term flexibility

When you embrace these principles in your Cobra applications, you’ll find yourself building CLIs that users love to use and you enjoy maintaining.

go

```
// A command that embodies all three principles
var deployCmd = &cobra.Command{
  Use:   "deploy [environment]",
  Short: "Deploy your application to the specified environment",
  Long: `Deploy your application to one of the configured environments.
Supports staging, production, and custom environments.

This command will build your application, run tests, and deploy
to the target environment with zero-downtime deployment strategies.`,
  Args:              cobra.ExactArgs(1),
  ValidArgs:         []string{"staging", "production"},
  ValidArgsFunction: deploymentTargetCompletion,
  PreRun:            validateEnvironment,
  Run:               executeDeployment,
  PostRun:           notifyDeploymentComplete,
}

func init() {
  // Convention: common flags with sensible defaults
  deployCmd.Flags().Bool("dry-run", false, "Show what would be deployed without executing")
  deployCmd.Flags().String("config", "", "Path to deployment config (default: ./deploy.yaml)")
  deployCmd.Flags().Duration("timeout", 10*time.Minute, "Deployment timeout")
  
  rootCmd.AddCommand(deployCmd)
}
```

This command demonstrates all three principles working in harmony: it’s designed as a user interface with clear help and validation, follows conventions for flags and structure, and provides powerful functionality out of the box while remaining extensible.
