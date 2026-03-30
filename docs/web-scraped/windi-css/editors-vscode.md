# Source: https://windicss.org/editors/vscode

Title: Windi CSS

URL Source: https://windicss.org/editors/vscode

Markdown Content:
Windi CSS Intellisense for VS Code
----------------------------------

[![Image 1](https://img.shields.io/badge/a-windicss--intellisense-gray?logo=github&label=)](https://github.com/windicss/windicss-intellisense)[![Image 2](https://img.shields.io/badge/a-%40voorjaar-48B0F1?label=)](https://github.com/voorjaar)

Windi CSS IntelliSense enhances the Windi development experience by providing Visual Studio Code users with advanced features such as autocomplete, syntax highlighting, code folding, and building.

Installation
------------

**[Install via the Visual Studio Code Marketplace →](https://marketplace.visualstudio.com/items?itemName=voorjaar.windicss-intellisense)**

**[Install via the Open VSX Registry →](https://open-vsx.org/extension/voorjaar/windicss-intellisense)**

This plugin packs a windicss compiler, so you can use it without installing windicss, and it also supports the configuration file `(tailwind|windi).config.(js|cjs|ts)`.

Features
--------

### Autocomplete

Intelligent suggestions for utilities and variants.

![Image 3: Auto Complete](https://raw.githubusercontent.com/windicss/windicss-intellisense/main/screenshots/completion.png)

### Hover Preview

See the complete CSS for a class name by hovering over it.

![Image 4: Hover Preview](https://raw.githubusercontent.com/windicss/windicss-intellisense/main/screenshots/hover.png)

### Syntax Highlighting

Highlight utilities, variants and importants.

![Image 5: Code Folding](https://raw.githubusercontent.com/windicss/windicss-intellisense/main/screenshots/highlight.png)

### Color Preview

Preview color and spectrum.

![Image 6: Color Preview](https://raw.githubusercontent.com/windicss/windicss-intellisense/main/screenshots/color.png)

### Code Folding

Fold overly long classes to increase readability.

![Image 7: Code Folding](https://raw.githubusercontent.com/windicss/windicss-intellisense/main/screenshots/highlight.png)

### Compile Commands

Built-in commands, one-key operation.

![Image 8: Compile Commands](https://raw.githubusercontent.com/windicss/windicss-intellisense/main/screenshots/commands.png)

Extension Settings
------------------

| Settings | type | default | description |
| --- | --- | --- | --- |
| `windicss.enableColorDecorators` | boolean | true | Enable Color Decorators. |
| `windicss.enableHoverPreview` | boolean | true | Enable hover className to show preview of CSS. |
| `windicss.enableCodeCompletion` | boolean | true | Enable/Disable all code completions. |
| `windicss.enableUtilityCompletion` | boolean | true | Enable Utility Completion. |
| `windicss.enableVariantCompletion` | boolean | true | Enable Variant Completion. |
| `windicss.enableDynamicCompletion` | boolean | true | Enable Dynamic Utilities Completion like p-${int}. |
| `windicss.enableRemToPxPreview` | boolean | true | Enable Rem to Px Preview. |
| `windicss.enableCodeFolding` | boolean | true | Enable ClassNames Code Folding. |
| `windicss.foldByLength` | boolean | false | Folding code by length. Default option is false, will fold by utility count. |
| `windicss.foldCount` | number | 3 | Used by foldByCount. |
| `windicss.foldLength` | number | 25 | Used by foldByLength |
| `windicss.hiddenText` | string | `...` | Placeholder used when folding code. |
| `windicss.hiddenTextColor` | string | #AED0A4 | Placeholder Color. |
| `windicss.sortOnSave` | boolean | false | Runs class sorting on file save. |

For more information
--------------------

*   [Windi CSS](https://github.com/windicss/windicss)
*   [Documentation](https://windicss.org/)
*   [Discussions](https://github.com/windicss/windicss/discussions)
*   [Issues](https://github.com/windicss/windicss-intellisense/issues)
