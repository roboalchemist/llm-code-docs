# Source: https://cobra.dev/docs/examples/01-text-formatter/

Title: Text Formatter CLI

URL Source: https://cobra.dev/docs/examples/01-text-formatter/

Markdown Content:
Build a simple yet powerful text formatting tool that demonstrates Cobra’s core concepts. This example is perfect for developers new to Cobra who want to understand command structure, flag handling, and input processing.

What You’ll Build
-----------------

A command-line tool called `textfmt` that can format text in various ways:

*   Convert text to uppercase, lowercase, or title case
*   Count words and characters
*   Apply multiple transformations at once
*   Accept input from arguments or stdin

Features Demonstrated
---------------------

*   **Root command** with basic structure
*   **String flags** with default values and validation
*   **Positional arguments** handling
*   **Help text** and usage messages
*   **Input flexibility** (arguments vs stdin)

Complete Source Code
--------------------

go

```
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/spf13/cobra"
)

var (
	uppercase   bool
	lowercase   bool
	titlecase   bool
	wordcount   bool
	charcount   bool
)

var rootCmd = &cobra.Command{
	Use:   "textfmt [text]",
	Short: "A simple text formatter",
	Long: `textfmt is a CLI tool for formatting and analyzing text.

You can provide text as arguments or pipe it in via stdin.
Multiple formatting options can be applied simultaneously.`,
	Args: cobra.ArbitraryArgs,
	Run:  runTextFormatter,
}

func init() {
	rootCmd.Flags().BoolVarP(&uppercase, "upper", "u", false, "Convert text to uppercase")
	rootCmd.Flags().BoolVarP(&lowercase, "lower", "l", false, "Convert text to lowercase")  
	rootCmd.Flags().BoolVarP(&titlecase, "title", "t", false, "Convert text to title case")
	rootCmd.Flags().BoolVar(&wordcount, "words", false, "Count words in text")
	rootCmd.Flags().BoolVar(&charcount, "chars", false, "Count characters in text")
}

func runTextFormatter(cmd *cobra.Command, args []string) {
	var text string

	// Get input text from args or stdin
	if len(args) > 0 {
		text = strings.Join(args, " ")
	} else {
		// Read from stdin
		scanner := bufio.NewScanner(os.Stdin)
		var lines []string
		for scanner.Scan() {
			lines = append(lines, scanner.Text())
		}
		text = strings.Join(lines, "\n")
	}

	if text == "" {
		fmt.Println("No input text provided")
		return
	}

	result := text

	// Apply formatting transformations
	if uppercase {
		result = strings.ToUpper(result)
	}
	if lowercase {
		result = strings.ToLower(result)
	}
	if titlecase {
		result = strings.Title(result)
	}

	// Output the formatted text
	fmt.Println(result)

	// Show analysis if requested
	if wordcount {
		words := len(strings.Fields(text))
		fmt.Printf("Words: %d\n", words)
	}
	if charcount {
		chars := len(text)
		fmt.Printf("Characters: %d\n", chars)
	}
}

func main() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
```

Build and Test Instructions
---------------------------

1.   **Create the project**:

`mkdir textfmt``cd textfmt``go mod init textfmt``go get github.com/spf13/cobra@latest` 
2.   **Save the code** above as `main.go`

3.   **Build the application**:

`go build -o textfmt` 
4.   **Test basic functionality**:

`./textfmt "hello world"``hello world``./textfmt --upper "hello world"``HELLO WORLD``./textfmt --title --words "hello world"``Hello World``Words: 2` 
5.   **Test stdin input**:

`echo "hello world" | ./textfmt --upper --chars``HELLO WORLD``Characters: 11` 
6.   **Check help output**:

`./textfmt --help``textfmt is a CLI tool for formatting and analyzing text.``You can provide text as arguments or pipe it in via stdin.``Multiple formatting options can be applied simultaneously.``Usage:``textfmt [text] [flags]``Flags:``--chars         Count characters in text``-h, --help          help for textfmt``-l, --lower         Convert text to lowercase``-t, --title         Convert text to title case``-u, --upper         Convert text to uppercase``--words         Count words in text` 

Key Learning Points
-------------------

### 1. Command Structure

The `cobra.Command` struct defines your CLI’s behavior:

*   `Use` sets the command name and argument pattern
*   `Short` provides a brief description
*   `Long` gives detailed help text
*   `Args` specifies argument validation
*   `Run` defines the main function to execute

### 2. Flag Definition

Flags are defined in the `init()` function:

*   `BoolVarP()` creates boolean flags with both long and short forms
*   `BoolVar()` creates boolean flags with only long form
*   Flags automatically appear in help output

### 3. Input Flexibility

The example shows two common input patterns:

*   **Arguments**: Direct command line arguments
*   **Stdin**: Piped input for shell integration

### 4. Error Handling

Cobra handles most errors automatically:

*   Invalid flags show usage and error messages
*   The `Execute()` method returns errors for custom handling

Extending the Example
---------------------

Try these modifications to deepen your understanding:

1.   **Add more transformations**: reverse text, remove spaces, etc.
2.   **Add validation**: prevent conflicting flags like `--upper` and `--lower`
3.   **Add file input**: read text from files specified as arguments
4.   **Add output options**: save formatted text to files

Next Steps
----------

*   **Learn about subcommands**: Check out the [Task Manager CLI](https://cobra.dev/docs/examples/02-task-manager/) example
*   **Explore flag types**: See the [Working with Flags](https://cobra.dev/docs/how-to-guides/working-with-flags/) guide
*   **Understand validation**: Read about [Working with Commands](https://cobra.dev/docs/how-to-guides/working-with-commands/)

This simple example demonstrates the power of Cobra for building intuitive CLI tools. Even with basic features, you can create professional, user-friendly applications!
