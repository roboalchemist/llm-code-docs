# Source: https://redocly.com/docs/cli/configuration.md

# Source: https://redocly.com/docs/cli/v1/configuration.md

# Source: https://redocly.com/docs/vscode/configuration.md

# Configuration

Create a configuration file called `redocly.yaml` in the root directory of your workspace.
The extension prompts you to create this file automatically if it doesn't exist.

Your directory structure should look similar to this:


```treeview
âââ workspace
â   âââ openapi-descriptions
â   â   âââ production.yaml
â   â   âââ test.yaml
â   âââ redocly.yaml
â   âââ some-file.txt
```

The `redocly.yaml` file defines the criteria for validating OpenAPI descriptions.

## Create a configuration file

Add the following example to your `redocly.yaml` file:


```yaml
extends:
  - recommended
rules:
  tag-description: off
  operation-summary: error
  no-unresolved-refs: error
  no-unused-components: error
  operation-2xx-response: error
  operation-operationId: error
  operation-singular-tag: error
  no-enum-type-mismatch: error
  no-identical-paths: error
  no-ambiguous-paths: error
```

## Update the configuration

Modify the `redocly.yaml` file at any time to control the extension's behavior.
Save the file to apply your changes.

For more information:

- Learn about built-in rules in the [Redocly CLI documentation](/docs/cli/rules)
- Find detailed options in the [configuration reference](/docs/cli/configuration)


## Working with multiple API files

Add multiple paths to OpenAPI files in the `apis` object.
The extension automatically validates listed APIs when you open them in VS Code.
Any changes to the `apis` section immediately appear in [the preview panel](/docs/vscode/live-preview).