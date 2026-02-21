# Source: https://cobra.dev/docs/how-to-guides/clis-for-llms/

Title: Generate LLM‑Ready CLI Docs with Cobra

URL Source: https://cobra.dev/docs/how-to-guides/clis-for-llms/

Markdown Content:
Cobra already knows everything about your CLI—commands, flags, examples. You can turn that into clean, structured docs with the built‑in generators. This guide shows the pragmatic path to produce Markdown (and optionally Man/ReST) that’s easy for search, static sites, and LLMs to consume.

What you’ll do:

*   Export your root command for reuse
*   Add a tiny `docgen` tool
*   Generate Markdown for every command
*   Optionally add front matter for your docs site
*   Ship disciplined, LLM‑friendly reference pages

Prerequisites:

*   Go 1.20+
*   A Cobra project
*   Commands with useful `Short`, `Long`, and `Example` filled in (LLMs benefit a lot from good examples)

If you’re starting fresh, see Working with Commands.

1) Export the Root Command (one line)
-------------------------------------

Make the root command accessible so an external tool can traverse your tree.

cmd/root.go (exporter)

go

```
package cmd

import "github.com/spf13/cobra"

var rootCmd = &cobra.Command{Use: "myapp"}

// Root exposes the root command for tools like doc generators.
func Root() *cobra.Command { return rootCmd }
```

Tip: If you prefer not to export, you can place the `docgen` tool in the same package and call `rootCmd` directly.

2) Add a tiny doc generator
---------------------------

Create a small program that walks your command tree and writes docs. Markdown is the best default for search engines and LLMs; Man and ReST are available too.

internal/tools/docgen/main.go

go

```
package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/spf13/cobra/doc"
	"example.com/myapp/cmd" // update to your module path
)

func main() {
	out := flag.String("out", "./docs/cli", "output directory")
	format := flag.String("format", "markdown", "markdown|man|rest")
	front := flag.Bool("frontmatter", false, "prepend simple YAML front matter to markdown")
	flag.Parse()

	if err := os.MkdirAll(*out, 0o755); err != nil { log.Fatal(err) }

	root := cmd.Root()
	root.DisableAutoGenTag = true // stable, reproducible files (no timestamp footer)

	switch *format {
	case "markdown":
		if *front {
			prep := func(filename string) string {
				base := filepath.Base(filename)
				name := strings.TrimSuffix(base, filepath.Ext(base))
				title := strings.ReplaceAll(name, "_", " ")
				return fmt.Sprintf("---\ntitle: %q\nslug: %q\ndescription: \"CLI reference for %s\"\n---\n\n", title, name, title)
			}
			link := func(name string) string { return strings.ToLower(name) }
			if err := doc.GenMarkdownTreeCustom(root, *out, prep, link); err != nil { log.Fatal(err) }
		} else {
			if err := doc.GenMarkdownTree(root, *out); err != nil { log.Fatal(err) }
		}
	case "man":
		hdr := &doc.GenManHeader{Title: strings.ToUpper(root.Name()), Section: "1"}
		if err := doc.GenManTree(root, hdr, *out); err != nil { log.Fatal(err) }
	case "rest":
		if err := doc.GenReSTTree(root, *out); err != nil { log.Fatal(err) }
	default:
		log.Fatalf("unknown format: %s", *format)
	}
}
```

Run it:

`go run ./internal/tools/docgen -out ./docs/cli -format markdown``# optional: add front matter suitable for static sites (Hugo/Jekyll/etc.)``go run ./internal/tools/docgen -out ./content/reference -format markdown -frontmatter``# other formats``go run ./internal/tools/docgen -out ./man -format man``go run ./internal/tools/docgen -out ./docs/rest -format rest`

What you’ll see: one file per command path, e.g. `myapp.md`, `myapp_serve.md`, `myapp_serve_start.md`. Each file contains Usage, Synopsis, Examples, Options, and inherited options—great structure for chunking.

3) Make the output easy for LLMs to ingest
------------------------------------------

A few small choices make a big difference:

*   One command per file: Cobra’s generators already do this—keep it.
*   Stable slugs: use predictable filenames; the example above matches Cobra’s defaults.
*   Strong examples: populate `Example` on each command; LLMs rely on concrete I/O.
*   Clear long descriptions: add context in `Long` (what/why, not just what).
*   Reproducible files: set `DisableAutoGenTag` to avoid timestamp churn.
*   Logical groups: set `GroupID` on commands; the sections appear in help and often in docs.

Example of strengthening a command for better docs:

cmd/serve.go (excerpts)

go

```
var serveCmd = &cobra.Command{
	Use:   "serve",
	Short: "Run the HTTP server",
	Long:  "Start the HTTP server with sensible defaults. Useful in development and production.",
	Example: `  # serve on the default port
  myapp serve

  # serve on a custom port
  myapp serve --port 9090`,
}
```

4) Wire into CI or your release process
---------------------------------------

*   Add a task (Make/NPM/Go) to regenerate docs.
*   Publish the Markdown to your docs site or a `docs/` folder in the repo.
*   If using a vector index, chunk on H2/H3 headings (Synopsis, Options, Examples).

`go run ./internal/tools/docgen -out ./docs/cli -format markdown``git add docs/cli && git commit -m "docs(cli): refresh Cobra reference"`

FAQ
---

*   Where do the fields come from? From your Cobra command definitions: `Use`, `Short`, `Long`, `Example`, flags, and inherited flags.
*   Can I customize the Markdown? Yes—use `doc.GenMarkdownTreeCustom` with a prepender (front matter) and link handler.
*   Do I have to export `rootCmd`? No, place the generator in the same package or expose an accessor like `Root()` as shown.

Recap
-----

*   Use Cobra’s `doc` package to emit Markdown (or Man/ReST) for every command.
*   Keep files stable and simple; add good `Long` and `Example` strings.
*   Optional front matter makes it drop‑in for static sites; structure is ideal for LLMs.
