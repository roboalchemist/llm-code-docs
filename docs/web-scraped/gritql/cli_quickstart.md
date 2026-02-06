# Source: https://docs.grit.io

# CLI Quickstart

The Grit CLI is a command-line interface for Grit. It allows you to apply GritQL patterns and run [custom workflows](/workflows/overview).
[
## Installation
](https://docs.grit.io/cli/quickstart#installation)You can install the Grit CLI from NPM:
bash npm install --location=global @getgrit/cliAlternatively, you can also install Grit with an installation script:
bash curl -fsSL https://docs.grit.io/install | bash*You can optionally run `grit init` to initialize a local [Grit configuration](/guides/config) and `grit install` to install additional binaries used for custom workflows.*
[
## Usage
](https://docs.grit.io/cli/quickstart#usage)[
### Overview
](https://docs.grit.io/cli/quickstart#overview)The primary purpose of the Grit CLI is to apply **automatic changes**. For example, you can automatically upgrade React Class Components to hooks with the following command from our [standard library](https://github.com/getgrit/stdlib/blob/main/.grit/patterns/js/react_to_hooks.md):
bash grit apply react_to_hooks[
### Applying patterns
](https://docs.grit.io/cli/quickstart#applying-patterns)Use `grit apply` to apply a pattern to the current directory including anything from our [standard library](https://github.com/getgrit/stdlib/tree/main/.grit/patterns) and custom patterns written in [GritQL](/language/overview).
Some examples include:
bash grit apply "const" # Simply shows all const declarations
grit apply no_console_log # Removes console.log statements from JavaScript
grit apply ternary_op # Converts if-else statements to ternary operators in Python
grit apply cypress_to_playwright # Converts Cypress tests to Playwright testsParameters can be passed to some patterns as well:
bash grit apply &#x27;remove_import(from=`"react"`)&#x27; # Removes all import statements from ReactTo view the full list of [available patterns](/patterns) in the standard library, run:
bash grit list[
## Telemetry
](https://docs.grit.io/cli/quickstart#telemetry)We collect usage data to help us improve the CLI. We **do not** collect any source code as part of this.
You can opt out of sending usage data by setting the `GRIT_TELEMETRY_DISABLED` environment variable to `true`.