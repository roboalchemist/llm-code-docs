# revive

Source: https://revive.run/docs/

This app works best with JavaScript enabled.HomeDocsRulesGuidesDevelop ruleDevelop formatterAPIrevive
Fast, configurable, extensible, flexible, and beautiful linter for Go. Drop-in replacement of golint.
Revive provides a framework for development of custom rules,
and lets you define a strict preset for enhancing your development & code review processes.
Logo by Georgi Serev
Here's how revive is different from golint:
Allows to enable or disable rules using a configuration file.
Allows to configure the linting rules with a TOML file.
2x faster running the same rules as golint.
Provides functionality for disabling a specific rule or the entire linter for a file or a range of lines.
golint allows this only for generated files.
Optional type checking. Most rules in golint do not require type checking.
If you disable them in the config file, revive will run over 6x faster than golint.
Provides multiple formatters which let us customize the output.
Allows to customize the return code for the entire linter or based on the failure of only some rules.
Everyone can extend it easily with custom rules or formatters.
Revive provides more rules compared to golint.
Installation
Homebrew
Install from Sources
Docker
Manual Binary Download
Usage
Bazel
Text Editors
GitHub Actions
Continuous Integration
Linter aggregators
golangci-lint
Command Line Flags
Sample Invocations
Comment Directives
Configuration
Custom Configuration
Recommended Configuration
Rule-level file excludes
Available Rules
Configurable rules
var-naming
Available Formatters
Friendly
Stylish
Default
Plain
Unix
JSON
NDJSON
Checkstyle
SARIF
Extensibility
Writing a Custom Rule
Using revive as a library
Custom Formatter
Speed Comparison
golint
revive's speed
Overriding colorization detection
Who uses Revive
Contributors
Maintainers
All
License
Installation
revive is available inside the majority of package managers.
Homebrew
Install revive using brew:
brew install revive
To upgrade to the latest version:
brew upgrade revive
Install from Sources
Install the latest stable release directly from source:
go install github.com/mgechev/revive@latest
To install the latest commit from the main branch:
go install github.com/mgechev/revive@HEAD
Docker
You can run revive using Docker to avoid installing it directly on your system:
docker run -v "$(pwd)":/var/YOUR_REPOSITORY ghcr.io/mgechev/revive:v1.10.0 -config /var/YOUR_REPOSITORY/revive.toml -formatter stylish ./var/YOUR_REPOSITORY/...
Note: Replace YOUR_REPOSITORY with the path to your repository.
A volume must be mounted to share the current repository with the container.
For more details, refer to the bind mounts Docker documentation.
-v: Mounts the current directory ($(pwd)) to /var/YOUR_REPOSITORY inside the container.
ghcr.io/mgechev/revive:v1.10.0: Specifies the Docker image and its version.
revive: The command to run inside the container.
Flags like -config and -formatter are the same as when using the binary directly.
Manual Binary Download
Download the precompiled binary from the Releases page:
Select the appropriate binary for your OS and architecture.
Extract the binary and move it to a directory in your PATH (e.g., /usr/local/bin).
Verify installation:
revive -version
Usage
Since the default behavior of revive is compatible with golint, without providing any additional flags,
the only difference you'd notice is faster execution.
revive supports a -config flag whose value should correspond to a TOML file describing which rules to use for revive's linting.
If not provided, revive will try to use a global config file (assumed to be located at $HOME/revive.toml).
Otherwise, if no configuration TOML file is found then revive uses a built-in set of default linting rules.
Bazel
If you want to use revive with Bazel, look at the rules that Atlassian maintains.
Text Editors
Support for VSCode via vscode-go by changing the go.lintTool setting to revive:
{
"go.lintTool": "revive",
}
Support for GoLand via File Watchers.
Support for vim via dense-analysis/ale.
let g:ale_linters = {
\
'go': ['revive'],
\}
Support for Neovim via null-ls.nvim.
require("null-ls").setup({
sources = {
require("null-ls").builtins.diagnostics.revive
},
})
GitHub Actions
Revive Action with annotation support
Continuous Integration
Codeac.io - Automated code review service integrates with GitHub,
Bitbucket and GitLab (even self-hosted) and helps you fight technical debt.
Check your pull-requests with
revive automatically.
(Free for open-source projects)
Linter aggregators
golangci-lint
To enable revive in golangci-lint you need to add revive to the list of enabled linters:
# golangci-lint configuration file
version: "2"
linters:
enable:
- revive
Then revive can be configured by adding an entry to the linters.settings section of the configuration, for example:
# golangci-lint configuration file
linters:
settings:
revive:
severity: warning
rules:
- name: atomic
- name: line-length-limit
severity: error
arguments: [80]
- name: unhandled-error
arguments: ["fmt.Printf", "myFunction"]
The above configuration enables three rules of revive: atomic, line-length-limit and unhandled-error and passes some arguments to the last two.
The Configuration section of this document provides details on how to configure revive.
Note that while revive configuration is in TOML, that of golangci-lint is in YAML or JSON.
See the golangci-lint website for more information about configuring revive.
Please notice that if no particular configuration is provided, revive will behave as golint does, i.e. all golint rules are enabled
(the Available Rules table details what are the golint rules).
When a configuration is provided, only rules in the configuration are enabled.
Command Line Flags
revive accepts the following command line parameters:
-config [PATH] - path to the config file in TOML format, defaults to $HOME/revive.toml if present.
-exclude [PATTERN] - pattern for files/directories/packages to be excluded for linting.
You can specify the files you want to exclude for linting either as package name (i.e. github.com/mgechev/revive),
list them as individual files (i.e. file.go), directories (i.e. ./foo/...), or any combination of the three.
If no exclusion patterns are specified, vendor/... will be excluded by default.
-formatter [NAME] - formatter to be used for the output. The currently available formatters are:
default - will output the failures the same way that golint does.
json - outputs the failures in JSON format.
ndjson - outputs the failures as a stream in newline delimited JSON (NDJSON) format.
friendly - outputs the failures when found. Shows the summary of all the failures.
stylish - formats the failures in a table. Keep in mind that it doesn't stream the output so it might be perceived as slower compared to others.
checkstyle - outputs the failures in XML format compatible with that of Java's Checkstyle.
-max_open_files -
maximum number of open files at the same time. Defaults to unlimited.
-set_exit_status - set exit status to 1 if any issues are found, overwrites errorCode and warningCode in config.
-version - get revive version.
Sample Invocations
revive -config revive.toml -exclude file1.go -exclude file2.go -formatter friendly github.com/mgechev/revive package/...
The command above will use the configuration from revive.toml
revive will ignore file1.go and file2.go
The output will be formatted with the friendly formatter
The linter will analyze github.com/mgechev/revive and the files in package
Comment Directives
Using comments, you can disable the linter for the entire file or only a range of lines:
//revive:disable
func Public() {}
//revive:enable
The snippet above, will disable revive between the revive:disable and revive:enable comments.
If you skip revive:enable, the linter will be disabled for the rest of the file.
With revive:disable-next-line and revive:disable-line you can disable revive on a particular code line.
You can do the same on a rule level. In case you want to disable only a particular rule, you can use:
//revive:disable:unexported-return
func Public() private {
return private
}
//revive:enable:unexported-return
This way, revive will not warn you that you're returning an object of an unexported type, from an exported function.
You can document why you disable the linter by adding a trailing text in the directive, for example
//revive:disable Until the code is stable
//revive:disable:cyclomatic High complexity score but easy to understand
You can also configure revive to enforce documenting linter disabling directives by adding
[directive.specify-disable-reason]
in the configuration. You can set the severity (defaults to warning) of the violation of this directive
[directive.specify-disable-reason]
severity = "error"
Configuration
revive can be configured with a TOML file. Here's a sample configuration with an explanation of the individual properties:
# When set to false, ignores files with "GENERATED" header, similar to golint
ignoreGeneratedHeader = true
# Sets the default severity to "warning"
severity = "warning"
# Sets the default failure confidence. This means that linting errors
# with less than 0.8 confidence will be ignored.
confidence = 0.8
# Sets the error code for failures with the "error" severity
errorCode = 0
# Sets the error code for failures with severity "warning"
warningCode = 0
# Configuration of the `cyclomatic` rule. Here we specify that
# the rule should fail if it detects code with higher complexity than 10.
[rule.cyclomatic]
arguments = [10]
# Sets the severity of the `package-comments` rule to "error".
[rule.package-comments]
severity = "error"
By default revive will enable only the linting rules that are named in the configuration file.
For example, the previous configuration file makes revive to enable only cyclomatic and package-comments linting rules.
To enable default rules you need to use:
enableDefaultRules = true
This will enable all rules available in golint and use their default configuration (i.e. the way they are hardcoded in golint).
The default configuration of revive can be found at defaults.toml.
To enable all available rules you need to add:
enableAllRules = true
This will enable all available rules no matter what rules are named in the configuration file.
To disable a rule, you simply mark it as disabled in the configuration.
For example:
[rule.line-length-limit]
Disabled = true
When enabling all rules you still need/can provide specific configurations for rules.
The following file is an example configuration where all rules are enabled, except for those that are explicitly disabled,
and some rules are configured with particular arguments:
severity = "warning"
confidence = 0.8
errorCode = 0
warningCode = 0
# Enable all available rules
enableAllRules = true
# Disabled rules
[rule.blank-imports]
Disabled = true
[rule.file-header]
Disabled = true
[rule.max-public-structs]
Disabled = true
[rule.line-length-limit]
Disabled = true
[rule.function-length]
Disabled = true
[rule.banned-characters]
Disabled = true
# Rule tuning
[rule.argument-limit]
Arguments = [5]
[rule.cyclomatic]
Arguments = [10]
[rule.cognitive-complexity]
Arguments = [7]
[rule.function-result-limit]
Arguments = [3]
[rule.error-strings]
Arguments = ["mypackage.Error"]
Custom Configuration
revive -config config.toml -formatter friendly github.com/mgechev/revive
This will use config.toml, the friendly formatter, and will run linting over the github.com/mgechev/revive package.
Recommended Configuration
The following snippet contains the recommended revive configuration that you can use in your project:
ignoreGeneratedHeader = false
severity = "warning"
confidence = 0.8
errorCode = 0
warningCode = 0
[rule.blank-imports]
[rule.context-as-argument]
[rule.context-keys-type]
[rule.dot-imports]
[rule.error-return]
[rule.error-strings]
[rule.error-naming]
[rule.exported]
[rule.increment-decrement]
[rule.var-naming]
[rule.var-declaration]
[rule.package-comments]
[rule.range]
[rule.receiver-naming]
[rule.time-naming]
[rule.unexported-return]
[rule.indent-error-flow]
[rule.errorf]
[rule.empty-block]
[rule.superfluous-else]
[rule.unused-parameter]
[rule.unreachable-code]
[rule.redefines-builtin-id]
Rule-level file excludes
You also can setup custom excludes for each rule.
It's an alternative for the global -exclude program arg.
ignoreGeneratedHeader = false
severity = "warning"
confidence = 0.8
errorCode = 0
warningCode = 0
[rule.blank-imports]
Exclude = ["**/*.pb.go"]
[rule.context-as-argument]
Exclude = ["src/somepkg/*.go", "TEST"]
You can use the following exclude patterns
full paths to files src/pkg/mypkg/some.go
globs src/**/*.pb.go
regexes (should have prefix ~) ~\.(pb|auto|generated)\.go$
well-known TEST (same as **/*_test.go)
special cases:
a. * and ~ patterns exclude all files (same effect as disabling the rule)
b. "" (empty) pattern excludes nothing
NOTE: do not mess with exclude that can
be used at the top level of TOML file, that means "exclude package patterns", not "exclude file patterns"
Available Rules
List of all available rules. The rules ported from golint are left unchanged and indicated in the golint column.
Name
Config
Description
golint
Typed
add-constant
map
Suggests using constant for magic numbers and string literals
no
no
argument-limit
int (defaults to 8)
Specifies the maximum number of arguments a function can receive
no
no
atomic
n/a
Check for common mistaken usages of the sync/atomic package
no
no
banned-characters
[]string (defaults to []string{})
Checks banned characters in identifiers
no
no
bare-return
n/a
Warns on bare returns
no
no
blank-imports
n/a
Disallows blank imports
yes
no
bool-literal-in-expr
n/a
Suggests removing Boolean literals from logic expressions
no
no
call-to-gc
n/a
Warns on explicit call to the garbage collector
no
no
cognitive-complexity
int (defaults to 7)
Sets restriction for maximum Cognitive complexity.
no
no
comment-spacings
[]string
Warns on malformed comments
no
no
comments-density
int (defaults to 0)
Enforces a minimum comment / code relation
no
no
confusing-naming
n/a
Warns on methods with names that differ only by capitalization
no
no
confusing-results
n/a
Suggests to name potentially confusing function results
no
no
constant-logical-expr
n/a
Warns on constant logical expressions
no
no
context-as-argument
n/a
context.Context should be the first argument of a function.
yes
no
context-keys-type
n/a
Disallows the usage of basic types in context.WithValue.
yes
yes
cyclomatic
int (defaults to 10)
Sets restriction for maximum Cyclomatic complexity.
no
no
datarace
n/a
Spots potential dataraces
no
no
deep-exit
n/a
Looks for program exits in funcs other than main() or init()
no
no
defer
map
Warns on some defer gotchas
no
no
dot-imports
n/a
Forbids . imports.
yes
no
duplicated-imports
n/a
Looks for packages that are imported two or more times
no
no
early-return
[]string
Spots if-then-else statements where the predicate may be inverted to reduce nesting
no
no
empty-block
n/a
Warns on empty code blocks
no
yes
empty-lines
n/a
Warns when there are heading or trailing newlines in a block
no
no
epoch-naming
n/a
Enforces naming conventions for epoch time variables
no
yes
enforce-map-style
string (defaults to "any")
Enforces consistent usage of make(map[type]type) or map[type]type{} for map initialization. Does not affect make(map[type]type, size) constructions.
no
no
enforce-repeated-arg-type-style
string (defaults to "any")
Enforces consistent style for repeated argument and/or return value types.
no
no
enforce-slice-style
string (defaults to "any")
Enforces consistent usage of make([]type, 0) or []type{} for slice initialization. Does not affect make(map[type]type, non_zero_len, or_non_zero_cap) constructions.
no
no
enforce-switch-style
[]string (defaults to enforce occurrence and position)
Enforces consistent usage of default on switch statements.
no
no
error-naming
n/a
Naming of error variables.
yes
no
error-return
n/a
The error return parameter should be last.
yes
no
error-strings
[]string
Conventions around error strings.
yes
no
errorf
n/a
Should replace errors.New(fmt.Sprintf()) with fmt.Errorf()
yes
yes
exported
[]string
Naming and commenting conventions on exported symbols.
yes
no
file-header
string (defaults to none)
Header which each file should have.
no
no
file-length-limit
map (optional)
Enforces a maximum number of lines per file
no
no
filename-format
regular expression (optional)
Enforces the formatting of filenames
no
no
flag-parameter
n/a
Warns on boolean parameters that create a control coupling
no
no
forbidden-call-in-wg-go
n/a
Warns on forbidden calls inside calls to wg.Go
no
no
function-length
int, int (defaults to 50 statements, 75 lines)
Warns on functions exceeding the statements or lines max
no
no
function-result-limit
int (defaults to 3)
Specifies the maximum number of results a function can return
no
no
get-return
n/a
Warns on getters that do not yield any result
no
no
identical-branches
n/a
Spots if-then-else statements with identical then and else branches
no
no
identical-ifelseif-branches
n/a
Spots if ... else if chains with identical branches.
no
no
identical-ifelseif-conditions
n/a
Spots identical conditions in
if ... else if chains.
no
no
identical-switch-branches
n/a
Spots switch with identical branches.
no
no
identical-switch-conditions
n/a
Spots identical conditions in case clauses of switch statements.
no
no
if-return
n/a
Redundant if when returning an error.
no
no
import-alias-naming
string or map[string]string (defaults to allow regex pattern ^[a-z][a-z0-9]{0,}$)
Conventions around the naming of import aliases.
no
no
import-shadowing
n/a
Spots identifiers that shadow an import
no
no
imports-blocklist
[]string
Disallows importing the specified packages
no
no
increment-decrement
n/a
Use i++ and i-- instead of i += 1 and i -= 1.
yes
no
indent-error-flow
[]string
Prevents redundant else statements.
yes
no
inefficient-map-lookup
n/a
Spots iterative searches for a key in a map
no
yes
line-length-limit
int (defaults to 80)
Specifies the maximum number of characters in a line
no
no
max-control-nesting
int (defaults to 5)
Sets restriction for maximum nesting of control structures.
no
no
max-public-structs
int (defaults to 5)
The maximum number of public structs in a file.
no
no
modifies-parameter
n/a
Warns on assignments to function parameters
no
no
modifies-value-receiver
n/a
Warns on assignments to value-passed method receivers
no
yes
nested-structs
n/a
Warns on structs within structs
no
no
optimize-operands-order
n/a
Checks inefficient conditional expressions
no
no
package-comments
n/a
Package commenting conventions.
yes
no
package-directory-mismatch
string
Checks that package name matches containing directory name
no
no
range-val-address
n/a
Warns if address of range value is used dangerously
no
yes
range-val-in-closure
n/a
Warns if range value is used in a closure dispatched as goroutine
no
no
range
n/a
Prevents redundant variables when iterating over a collection.
yes
no
receiver-naming
map (optional)
Conventions around the naming of receivers.
yes
no
redefines-builtin-id
n/a
Warns on redefinitions of builtin identifiers
no
no
redundant-build-tag
n/a
Warns about redundant // +build comment lines
no
no
redundant-import-alias
n/a
Warns on import aliases matching the imported package name
no
no
redundant-test-main-exit
n/a
Suggests removing Exit call in TestMain function for test files
no
no
string-format
map
Warns on specific string literals that fail one or more user-configured regular expressions
no
no
string-of-int
n/a
Warns on suspicious casts from int to string
no
yes
struct-tag
[]string
Checks common struct tags like json, xml, yaml
no
no
superfluous-else
[]string
Prevents redundant else statements (extends indent-error-flow)
no
no
time-date
n/a
Reports bad usage of time.Date.
no
yes
time-equal
n/a
Suggests to use time.Time.Equal instead of == and != for equality check time.
no
yes
time-naming
n/a
Conventions around the naming of time variables.
yes
yes
unchecked-type-assertions
n/a
Disallows type assertions without checking the result.
no
yes
unconditional-recursion
n/a
Warns on function calls that will lead to (direct) infinite recursion
no
no
unexported-naming
n/a
Warns on wrongly named un-exported symbols
no
no
unexported-return
n/a
Warns when a public return is from unexported type.
yes
yes
unhandled-error
[]string
Warns on unhandled errors returned by function calls
no
yes
unnecessary-if
n/a
Identifies if-else statements that can be replaced by simpler statements
no
no
unnecessary-format
n/a
Identifies calls to formatting functions where the format string does not contain any formatting verbs
no
no
unnecessary-stmt
n/a
Suggests removing or simplifying unnecessary statements
no
no
unreachable-code
n/a
Warns on unreachable code
no
no
unsecure-url-scheme
n/a
Checks for usage of potentially unsecure URL schemes.
no
no
unused-parameter
n/a
Suggests to rename or remove unused function parameters
no
no
unused-receiver
n/a
Suggests to rename or remove unused method receivers
no
no
use-any
n/a
Proposes to replace interface{} with its alias any
no
no
use-errors-new
n/a
Spots calls to fmt.Errorf that can be replaced by errors.New
no
no
use-fmt-print
n/a
Proposes to replace calls to built-in print and println with their equivalents from fmt.
no
no
use-waitgroup-go
n/a
Proposes to replace wg.Add ... go {... wg.Done ...} idiom with wg.Go
no
no
useless-break
n/a
Warns on useless break statements in case clauses
no
no
useless-fallthrough
n/a
Warns on useless fallthrough statements in case clauses
no
no
var-declaration
n/a
Reduces redundancies around variable declaration.
yes
yes
var-naming
allowlist & blocklist of initialisms
Naming rules.
yes
no
waitgroup-by-value
n/a
Warns on functions taking sync.WaitGroup as a by-value parameter
no
no
Configurable rules
Here you can find how you can configure some existing rules:
var-naming
This rule accepts two slices of strings, an allowlist and a blocklist of initialisms. By default, the rule behaves exactly as the alternative
in golint but optiongolint/lint/issues/89)
[rule.var-naming]
arguments = [["ID"], ["VM"]]
This way, revive will not warn for an identifier called customId but will warn that customVm should be called customVM.
Available Formatters
This section lists all the available formatters and provides a screenshot for each one.
Friendly
Stylish
Default
The default formatter produces the same output as golint.
Plain
The plain formatter produces the same output as the default formatter and appends the URL to the rule description.
Unix
The unix formatter produces the same output as the default formatter but surrounds the rules in [].
JSON
The json formatter produces output in JSON format.
NDJSON
The ndjson formatter produces output in Newline Delimited JSON format.
Checkstyle
The checkstyle formatter produces output in a Checkstyle-like format.
SARIF
The sarif
formatter produces output in SARIF, for Static Analysis Results Interchange Format,
a standard JSON-based format for the output of static analysis tools defined and promoted by OASIS.
Current supported version of the standard is SARIF-v2.1.0.
Extensibility
The tool can be extended with custom rules or formatters. This section contains additional information on how to implement such.
To extend the linter with a custom rule you can push it to this repository or use revive as a library (see below)
To add a custom formatter you'll have to push it to this repository or fork it.
This is due to the limited -buildmode=plugin support which works only on Linux (with known issues).
Writing a Custom Rule
See DEVELOPING.md for instructions on how to write a custom rule.
Using revive as a library
If a rule is specific to your use case
(i.e. it is not a good candidate to be added to revive's rule set) you can add it to your linter using revive as a linting engine.
The following code shows how to use revive in your application.
In the example only one rule is added (myRule), of course, you can add as many as you need to.
Your rules can be configured programmatically or with the standard revive configuration file.
The full rule set of revive is also actionable by your application.
package main
import (
"github.com/mgechev/revive/cli"
"github.com/mgechev/revive/lint"
"github.com/mgechev/revive/revivelib"
)
func main() {
cli.RunRevive(revivelib.NewExtraRule(&myRule{}, lint.RuleConfig{}))
}
type myRule struct{}
func (f myRule) Name() string {
return "myRule"
}
func (f myRule) Apply(*lint.File, lint.Arguments) []lint.Failure {
// ...
}
You can still go further and use revive without its CLI, as part of your library, or your CLI:
package mylib
import (
"github.com/mgechev/revive/config"
"github.com/mgechev/revive/lint"
"github.com/mgechev/revive/revivelib"
)
// Error checking removed for clarity
func LintMyFile(file string) {
conf, _ := config.GetConfig("../defaults.toml")
revive, _ := revivelib.New(
conf, // Configuration file
true, // Set exit status
2048, // Max open files
// Then add as many extra rules as you need
revivelib.NewExtraRule(&myRule{}, lint.RuleConfig{}),
)
failuresChan, err := revive.Lint(
revivelib.Include(file),
revivelib.Exclude("./fixtures"),
// You can use as many revivelib.Include or revivelib.Exclude as required
)
if err != nil {
panic("Shouldn't have failed: " + err.Error())
}
// Now let's return the formatted errors
failures, exitCode, _ := revive.Format("stylish", failuresChan)
// failures is the string with all formatted lint error messages
// exit code is 0 if no errors, 1 if errors (unless config options change it)
// ... do something with them
}
type myRule struct{}
func (f myRule) Name() string {
return "myRule"
}
func (f myRule) Apply(*lint.File, lint.Arguments) []lint.Failure {
// ...
}
Custom Formatter
Each formatter needs to implement the following interface:
type Formatter interface {
Format(<-chan Failure, Config) (string, error)
Name() string
}
The Format method accepts a channel of Failure instances and the configuration of the enabled rules.
The Name() method should return a string different from the names of the already existing rules.
This string is used when specifying the formatter when invoking the revive CLI tool.
For a sample formatter, take a look at this file.
Speed Comparison
Compared to golint, revive performs better because it lints the files for each individual rule into a separate goroutine.
Here's a basic performance benchmark on MacBook Pro Early 2013 run on Kubernetes:
golint
$ time golint kubernetes/... > /dev/null
real
0m54.837s
user
0m57.844s
sys
0m9.146s
revive's speed
# no type checking
$ time revive -config untyped.toml kubernetes/... > /dev/null
real
0m8.471s
user
0m40.721s
sys
0m3.262s
Keep in mind that if you use rules that require type checking, the performance may drop to 2x faster than golint:
# type checking enabled
$ time revive kubernetes/... > /dev/null
real
0m26.211s
user
2m6.708s
sys
0m17.192s
Currently, type-checking is enabled by default. If you want to run the linter without type-checking, remove all typed rules from the configuration file.
Overriding colorization detection
By default, revive determines whether or not to colorize its output based on whether it's connected to a TTY or not.
This works for most use cases, but may not behave as expected if you use revive in a pipeline of commands,
where STDOUT is being piped to another command.
To force colorization, add REVIVE_FORCE_COLOR=1 to the environment you're running in. For example:
REVIVE_FORCE_COLOR=1 revive -formatter friendly ./... | tee revive.log
Who uses Revive
tidb - TiDB is a distributed HTAP database compatible with the MySQL protocol
grafana - The tool for beautiful monitoring and metric analytics & dashboards for Graphite, InfluxDB & Prometheus & More
etcd - Distributed reliable key-value store for the most critical data of a distributed system
cadence - Cadence is a distributed, scalable, durable, and highly available orchestration engine by Uber to execute asynchronous long-running business logic in a scalable and resilient way
ferret - Declarative web scraping
gopass - The slightly more awesome standard unix password manager for teams
gitea - Git with a cup of tea, painless self-hosted git service
excelize - Go library for reading and writing Microsoft Excel™ (XLSX) files
aurora - aurora is a web-based Beanstalk queue server console written in Go
soar - SQL Optimizer And Rewriter
pyroscope - Continuous profiling platform
gorush - A push notification server written in Go (Golang).
dry - dry - A Docker manager for the terminal.
go-echarts - The adorable charts library for Golang
reviewdog - Automated code review tool integrated with any code analysis tools regardless of programming language
rudder-server - Privacy and Security focused Segment-alternative, in Golang and React.
sklearn - A partial port of scikit-learn written in Go.
protoc-gen-doc - Documentation generator plugin for Google Protocol Buffers.
llvm - Library for interacting with LLVM IR in pure Go.
jenkins-library - Jenkins shared library for Continuous Delivery pipelines by SAP.
pd - Placement driver for TiKV.
shellhub - ShellHub enables teams to easily access any Linux device behind firewall and NAT.
lorawan-stack - The Things Network Stack for LoRaWAN V3
gin-jwt - This is a JWT middleware for Gin framework.
gofight - Testing API Handler written in Golang.
Beaver - A Real Time Messaging Server.
ggz - An URL shortener service written in Golang
Codeac.io - Automated code review service integrates with GitHub, Bitbucket and GitLab (even self-hosted) and helps you fight technical debt.
DevLake - Apache DevLake is an open-source dev data platform to ingest, analyze, and visualize the fragmented data from DevOps tools，which can distill insights to improve engineering productivity.
checker - Checker helps validating user input through rules defined in struct tags or directly through functions.
milvus - A cloud-native vector database, storage for next generation AI applications.
indicator - Indicator provides various technical analysis indicators, strategies, and a backtesting framework.
Open a PR to add your project.
Contributors
Maintainers
mgechev
chavacava
denisvmedia
alexandear
All
This project exists thanks to all the people who contribute.
License
MIT
gechev/revive&max=500" />
License
MIT