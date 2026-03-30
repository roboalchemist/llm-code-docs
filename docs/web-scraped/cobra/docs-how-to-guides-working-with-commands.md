# Source: https://cobra.dev/docs/how-to-guides/working-with-commands/

Title: Working with Commands

URL Source: https://cobra.dev/docs/how-to-guides/working-with-commands/

Markdown Content:
How can we make you feel genuinely important? By meeting you where you are: you know Go, you’re building a CLI, and you want clear, reliable patterns. What would happen if we became genuinely interested in your perspective? We’d explain what to do, why it matters, and when to reach for each tool—without drama.

This guide walks through the everyday moves you’ll make with Cobra:

*   Add a subcommand
*   Organize commands as your app grows
*   Give commands aliases that users will guess
*   Return errors cleanly with `RunE`
*   Group commands so help stays readable

Along the way, we favor the Kernighan/Pike virtues: simple words, small steps, and code you can trust.

Prerequisites:

*   Go 1.20+
*   A Cobra project (created with `cobra-cli init`)

If you don’t have one yet:

`mkdir myapp && cd myapp``go mod init example.com/myapp``go install github.com/spf13/cobra-cli@latest``cobra-cli init`

Your tree will look like:

*   main.go
*   cmd/ 
    *   root.go

How to Add a Subcommand
-----------------------

The standard recipe is: define a `*cobra.Command` and attach it to a parent with `AddCommand`—usually in the child’s `init()`.

Example: add a `greet` command.

cmd/greet.go

go

```
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var greetCmd = &cobra.Command{
	Use:   "greet [name]",
	Short: "Print a friendly greeting",
	Args:  cobra.MaximumNArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		name := "world"
		if len(args) == 1 { name = args[0] }
		fmt.Printf("Hello, %s!\n", name)
		return nil
	},
}

func init() {
	rootCmd.AddCommand(greetCmd)
}
```

Try it:

`go run . greet``Hello, world!``go run . greet Alice``Hello, Alice!`

Why this works: Cobra parses flags and args, then calls your `Run`/`RunE`. Attaching in `init()` ensures the command is registered before `Execute()` runs.

When to use: Always. Every subcommand follows this basic pattern.

How to Organize Commands in Packages
------------------------------------

Small apps are fine with all commands in one package (`cmd/`). Large apps benefit from modular packages where each feature exposes a constructor (e.g., `NewCommand()`). This keeps imports narrow, improves compile times, and lets subtrees evolve independently—an approach used by bigger projects like Hugo.

Two layouts you can choose from:

*   Simple (default Cobra): one `cmd` package, one file per command.
*   Modular (recommended at scale): each feature gets its own package that returns a `*cobra.Command`.

Example modular layout:

*   cmd/ 
    *   root.go

*   internal/cli/ 
    *   serve/command.go
    *   build/command.go

Serve command (feature package):

internal/cli/serve/command.go

go

```
package serve

import (
	"fmt"
	"github.com/spf13/cobra"
)

func NewCommand() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "serve",
		Short: "Run the HTTP server",
		RunE: func(cmd *cobra.Command, args []string) error {
			port, _ := cmd.Flags().GetInt("port")
			fmt.Printf("Serving on :%d\n", port)
			return nil
		},
	}
	cmd.Flags().Int("port", 8080, "port to listen on")
	return cmd
}
```

Wire it up from `root.go`:

cmd/root.go (excerpt)

go

```
package cmd

import (
	"os"
	"github.com/spf13/cobra"
	"example.com/myapp/internal/cli/serve"
	"example.com/myapp/internal/cli/build"
)

var rootCmd = &cobra.Command{Use: "myapp"}

func Execute() { if err := rootCmd.Execute(); err != nil { os.Exit(1) } }

func init() {
	rootCmd.AddCommand(serve.NewCommand())
	rootCmd.AddCommand(build.NewCommand())
}
```

Why: clear dependency boundaries; `serve` doesn’t pull in `build`’s imports.

When: switch to this once your `cmd/` grows beyond a handful of files or teams own different features.

How to Define Command Aliases
-----------------------------

Aliases let users type what they expect. In Cobra, `Aliases` is a slice of strings (`[]string`), not a single string.

Example: `install` with short forms.

cmd/install.go

go

```
package cmd

import "github.com/spf13/cobra"

var installCmd = &cobra.Command{
	Use:     "install",
	Short:   "Install dependencies",
	Aliases: []string{"i", "add"},
	RunE: func(cmd *cobra.Command, args []string) error {
		// ... do the work ...
		return nil
	},
}

func init() { rootCmd.AddCommand(installCmd) }
```

Try it:

`go run . install``go run . i``go run . add`

Why: fewer keystrokes; meets users where they are.

When: provide at most one or two obvious aliases; too many can cause ambiguity.

How to Handle Errors with RunE
------------------------------

Prefer `RunE` to `Run`. Returning an error keeps your command logic clean and lets Cobra handle the exit code. Two useful switches:

*   `cmd.SilenceUsage = true` avoids printing usage on runtime errors (it still prints usage for flag/arg errors).
*   `cmd.SilenceErrors = true` suppresses Cobra’s automatic error print if you want to print your own message.

Example:

cmd/open.go

go

```
package cmd

import (
	"fmt"
	"os"
	"github.com/spf13/cobra"
)

var openCmd = &cobra.Command{
	Use:   "open <file>",
	Short: "Open a file (demo of RunE)",
	Args:  cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		path := args[0]
		b, err := os.ReadFile(path)
		if err != nil {
			return fmt.Errorf("read %s: %w", path, err)
		}
		fmt.Printf("%d bytes\n", len(b))
		return nil
	},
}

func init() {
	openCmd.SilenceUsage = true // don’t spam usage for runtime errors
	rootCmd.AddCommand(openCmd)
}
```

Behavior:

*   If `RunE` returns `nil`, Cobra exits with code 0.
*   If `RunE` returns an error, Cobra prints it to stderr and exits with non‑zero.

Why: clear error paths, testable code, proper exit codes.

When: always use `RunE` unless your command can’t fail.

How to Group Commands in the Help Output
----------------------------------------

Busy CLIs deserve tidy help. Define groups on the root, then assign a `GroupID` to each command. Cobra will render sections in `--help`.

Root groups:

cmd/root.go (groups)

go

```
func init() {
	rootCmd.AddGroup(&cobra.Group{ID: "manage", Title: "Management Commands"})
	rootCmd.AddGroup(&cobra.Group{ID: "query",  Title: "Query Commands"})
	// Attach commands (somewhere in your init):
	// backupCmd.GroupID = "manage"
	// restoreCmd.GroupID = "manage"
	// searchCmd.GroupID = "query"
}
```

Assigning commands to a group:

cmd/backup.go

go

```
var backupCmd = &cobra.Command{Use: "backup", Short: "Create a backup"}

func init() {
	backupCmd.GroupID = "manage"
	rootCmd.AddCommand(backupCmd)
}
```

Now `myapp --help` will show logical sections, which dramatically improves discoverability once you have many subcommands.

Why: users scan, not read; groups reduce cognitive load.

When: introduce groups as soon as you pass ~8–10 subcommands or when you have natural categories.

Recap
-----

*   Add subcommands with `AddCommand`.
*   For larger apps, return commands from feature packages to keep boundaries clean.
*   Use `Aliases []string` for friendly shorthand.
*   Prefer `RunE` and set `SilenceUsage`/`SilenceErrors` intentionally.
*   Group commands to keep help readable as the CLI grows.

Keep it small, make it clear, and let the code do the talking.
