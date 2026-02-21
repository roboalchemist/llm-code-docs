# Source: https://cobra.dev/docs/how-to-guides/working-with-flags/

Title: Working with Flags

URL Source: https://cobra.dev/docs/how-to-guides/working-with-flags/

Markdown Content:
You’ve got commands; now make them configurable. Flags turn one-off demos into useful tools. This guide shows the everyday moves for flags in Cobra (pflag), with clear guidance on why and when to use each pattern.

We’ll cover:

*   Add local and persistent flags
*   Use shorthands and sensible defaults
*   Read values (bind to vars vs. read on demand)
*   Make flags required, validate, and cross‑check
*   Hide or deprecate flags without breaking users
*   Optional: wire flags to environment/config with Viper

Prerequisites:

*   Go 1.20+
*   A Cobra project (created with `cobra-cli init`)

If you need one:

`mkdir flagsapp && cd flagsapp``go mod init example.com/flagsapp``go install github.com/spf13/cobra-cli@latest``cobra-cli init`

Your tree will look like:

*   main.go
*   cmd/ 
    *   root.go

Add a Local Flag
----------------

Local flags live on a single command and do not inherit to children.

Example: add `--port` to `serve`.

cmd/serve.go

go

```
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var serveCmd = &cobra.Command{
	Use:   "serve",
	Short: "Run the HTTP server",
	RunE: func(cmd *cobra.Command, args []string) error {
		port, err := cmd.Flags().GetInt("port")
		if err != nil { return err }
		fmt.Printf("Serving on :%d\n", port)
		return nil
	},
}

func init() {
	// Local flag: only applies to `serve`.
	serveCmd.Flags().Int("port", 8080, "port to listen on")
	rootCmd.AddCommand(serveCmd)
}
```

Try it:

`go run . serve``Serving on :8080``go run . serve --port 9090``Serving on :9090`

Why: keep flags close to the command that owns the behavior.

When: most flags are local by default.

Add a Persistent Flag
---------------------

Persistent flags live on a parent and are available to all descendants (unless shadowed).

Example: a global `--verbose`.

cmd/root.go (excerpt)

go

```
package cmd

import (
	"os"
	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{Use: "flagsapp"}

func Execute() { if err := rootCmd.Execute(); err != nil { os.Exit(1) } }

func init() {
	// Persistent: visible on root and all subcommands.
	rootCmd.PersistentFlags().Bool("verbose", false, "enable verbose output")
}
```

Read it anywhere via `cmd.Flags().GetBool("verbose")` inside the command’s `RunE`.

Why: keep cross‑cutting settings (e.g., output, config path) in one place.

When: use persistent flags sparingly—only for truly global concerns.

Shorthand Flags (-p)
--------------------

Most flag helpers have a `P` variant to add a one‑letter shorthand.

cmd/serve.go (shorthand)

go

```
func init() {
	serveCmd.Flags().IntP("port", "p", 8080, "port to listen on")
	rootCmd.AddCommand(serveCmd)
}
```

Usage:

`go run . serve -p 9000`

Notes:

*   Avoid collisions across siblings; reserve `-h` for help.
*   For booleans, `-v` toggles true; use `-v=false` to turn off explicitly.

Bind to Variables vs. Read on Demand
------------------------------------

Two common styles:

*   Read on demand in `RunE` (simple, keeps scope tight).
*   Bind to a package variable (handy when multiple functions need the value).

Binding example:

cmd/serve.go (bind var)

go

```
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var (
	port    int
	verbose bool
)

var serveCmd = &cobra.Command{
	Use: "serve",
	RunE: func(cmd *cobra.Command, args []string) error {
		if verbose {
			// tweak logging
		}
		fmt.Printf("Serving on :%d\n", port)
		return nil
	},
}

func init() {
	serveCmd.Flags().IntVarP(&port, "port", "p", 8080, "port to listen on")
	// Inherit persistent verbose from root onto this var
	rootCmd.PersistentFlags().BoolVarP(&verbose, "verbose", "v", false, "enable verbose output")
	rootCmd.AddCommand(serveCmd)
}
```

Why: binding is convenient for shared access; reading is great for small, local commands.

Common Flag Types You’ll Use
----------------------------

*   String: `String`, `StringP`, `StringVar`
*   Int: `Int`, `IntP`, `IntVar`
*   Bool: `Bool`, `BoolP`, `BoolVar`
*   Duration: `Duration`, parses `300ms`, `5s`, `1m`
*   StringSlice / StringArray: multiple values (`--tag a --tag b`)

Example slices:

cmd/build.go

go

```
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var tags []string

var buildCmd = &cobra.Command{
	Use: "build",
	RunE: func(cmd *cobra.Command, args []string) error {
		fmt.Printf("Tags: %v\n", tags)
		return nil
	},
}

func init() {
	buildCmd.Flags().StringSliceVar(&tags, "tag", nil, "add build tag (repeatable)")
	rootCmd.AddCommand(buildCmd)
}
```

Usage:

`go run . build --tag ui --tag api``Tags: [ui api]`

Make a Flag Required
--------------------

Mark a flag required after it’s defined.

cmd/login.go

go

```
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var user, pass string

var loginCmd = &cobra.Command{
	Use:   "login",
	Short: "Authenticate to the service",
	RunE: func(cmd *cobra.Command, args []string) error {
		fmt.Println("Logged in as", user)
		return nil
	},
}

func init() {
	loginCmd.Flags().StringVar(&user, "username", "", "username")
	loginCmd.Flags().StringVar(&pass, "password", "", "password")
	if err := loginCmd.MarkFlagRequired("username"); err != nil { panic(err) }
	if err := loginCmd.MarkFlagRequired("password"); err != nil { panic(err) }
	rootCmd.AddCommand(loginCmd)
}
```

Behavior: Cobra prints a helpful error and usage when a required flag is missing.

When: use for credentials or parameters with no sensible default.

Use `PreRunE` to check relationships: mutual exclusion, required-together, or value constraints.

cmd/export.go

go

```
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var (
	outPath string
	stdout  bool
	format  string
)

var exportCmd = &cobra.Command{
	Use: "export",
	PreRunE: func(cmd *cobra.Command, args []string) error {
		// Mutually exclusive: either --stdout or --out
		if stdout && outPath != "" {
			return fmt.Errorf("--stdout and --out are mutually exclusive")
		}
		// Enum check
		switch format {
		case "json", "yaml":
		default:
			return fmt.Errorf("invalid --format: %s (want json|yaml)", format)
		}
		return nil
	},
	RunE: func(cmd *cobra.Command, args []string) error {
		// ... do the work ...
		return nil
	},
}

func init() {
	exportCmd.Flags().StringVar(&outPath, "out", "", "write to file path")
	exportCmd.Flags().BoolVar(&stdout, "stdout", false, "write to stdout")
	exportCmd.Flags().StringVar(&format, "format", "json", "output format (json|yaml)")
	rootCmd.AddCommand(exportCmd)
}
```

Why: keep parsing/validation separate from execution logic.

Hide or Deprecate Flags
-----------------------

Clean up without breaking scripts.

cmd/root.go (hide/deprecate)

go

```
func init() {
	rootCmd.PersistentFlags().String("config", "", "config file path")
	// Hide a flag from help (still works if used)
	_ = rootCmd.PersistentFlags().MarkHidden("config")

	rootCmd.PersistentFlags().String("colour", "auto", "use British spelling")
	// Deprecate with a hint
	_ = rootCmd.PersistentFlags().MarkDeprecated("colour", "use --color instead")
}
```

Tip: keep deprecated flags active for at least one minor release with clear messaging.

Optional: Wire Flags to Environment/Config (Viper)
--------------------------------------------------

If you use Viper, bind flags so users can set values via env vars or config files. Precedence (highest first) is: flag, env var, config file, default.

cmd/root.go (viper)

go

```
package cmd

import (
	"strings"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var rootCmd = &cobra.Command{Use: "flagsapp"}

func init() {
	rootCmd.PersistentFlags().Int("port", 8080, "port to listen on")
	// Bind flag to Viper key
	_ = viper.BindPFlag("port", rootCmd.PersistentFlags().Lookup("port"))

	// Env: FLAGSAPP_PORT=9090
	viper.SetEnvPrefix("flagsapp")
	viper.SetEnvKeyReplacer(strings.NewReplacer("-", "_"))
	viper.AutomaticEnv()
}
```

cmd/serve.go (viper use)

go

```
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var serveCmd = &cobra.Command{
	Use: "serve",
	RunE: func(cmd *cobra.Command, args []string) error {
		// flag > env > config > default
		port := viper.GetInt("port")
		fmt.Printf("Serving on :%d\n", port)
		return nil
	},
}

func init() { rootCmd.AddCommand(serveCmd) }
```

When: reach for Viper if you need env/config files and consistent precedence.

Tips and Gotchas
----------------

*   Flags() vs PersistentFlags(): use local by default; promote consciously.
*   Don’t reuse shorthands across sibling commands unless behavior is identical.
*   Name booleans positively (e.g., `--verbose`, not `--no-verbose`); allow `--verbose=false` when needed.
*   Mark required flags in `init()` right after defining them.
*   For complex parsing/validation, implement a custom `pflag.Value` type and use `Var`/`VarP`.

Recap
-----

*   Local flags configure a single command; persistent flags flow down the tree.
*   Use shorthands judiciously and provide good defaults.
*   Read flags in `RunE` or bind to vars—choose based on scope.
*   Mark required flags and validate relationships in `PreRunE`.
*   Hide/deprecate to evolve safely; bind to Viper when you need env/config support.

Keep options clear, error messages kind, and defaults sensible—your users will thank you.
