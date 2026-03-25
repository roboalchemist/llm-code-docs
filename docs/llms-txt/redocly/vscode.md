# Source: https://redocly.com/docs/vscode.md

# Redocly OpenAPI VS Code extension

Redocly OpenAPI is a [Visual Studio Code](https://code.visualstudio.com/) extension that helps you write, validate, and maintain your OpenAPI documents.
It warns about errors in OpenAPI definitions and lets you quickly access referenced schemas or open the files that contain them.
The extension works with OpenAPI 2.0 and 3.0 definitions, and has basic support for OpenAPI 3.1.

**Feature highlights:**

- Validate your OpenAPI definitions
- Quickly preview and access referenced schemas
- Work with multi-file definitions
- Preview API documentation side-by-side with your OpenAPI definition
- Access context-aware help about OpenAPI features
- Edit API definitions through interactive forms


![Peek and go-to-definition features](/assets/openapi-vscode-peek.a041df211e0525f867da75fe04aaaeb562b4b809e126d27b28d3309d2eeeaaf3.289fb047.gif)

## Requirements and limitations

- If you provide a `redocly.yaml` configuration file, it must be located in the root directory of your workspace.
If you don't have a custom configuration, the extension will automatically use the [recommended ruleset](https://redocly.com/docs/cli/rules/recommended).
For setup instructions, see the [Configuration section](/docs/vscode/configuration).
- Note that the extension only works with YAML files. Validation for JSON files is supported starting with version 0.2.0 of the extension.
- An API key from Redocly is required to use the live documentation preview feature in the extension.
- Functionality of the extension may be affected by some limitations of the VS Code editor. So far, we have identified these limitations:
  - Special characters `/`, `$` and `#` do not trigger VS Code suggestions
  - VS Code doesn't suggest values while inside a snippet


## Quickstart

To start using Redocly OpenAPI in your VS Code editor:

1. [Install the extension](/docs/vscode/installation).
2. Create a `redocly.yaml` [configuration file](/docs/vscode/configuration), or let the extension automatically generate one for you.
If you don't provide a custom configuration, the extension will use the default settings.
3. Open an existing OpenAPI document in VS Code, or [create a new one from the template](/docs/vscode/using-redocly-vscode).
4. Relax while the extension validates your OpenAPI documents automatically!


## Debug common problems

If you suspect the extension is not working properly, make sure the following conditions are true:

- the extension is enabled in the current VS Code workspace (or globally),
- the `redocly.yaml` configuration file is located in your workspace root and it is not empty,
- your API definition file is in the YAML format.


### Known issues

- Interactive forms are supported only for `info`, `server`, and `externalDocs` sections in the current version.
- Autocompletion support is limited in the current version.
- The `redocly.yaml` file must be saved to disk (Ctrl+S) for changes to apply.


### How to report issues

If you encounter issues with the extension that you're not able to resolve, report them in our [Redocly VS Code GitHub repository](https://github.com/Redocly/redocly-vs-code/issues/new/choose).

The [Contributing guide](https://github.com/Redocly/redocly-vs-code/blob/main/CONTRIBUTING.md) in the repository contains detailed guidelines for reporting issues.