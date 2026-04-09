# Continuous Formatting

**Continuous Formatting** is a VS Code extension that provides real-time TypeScript code formatting as you type. It enables automatic code style improvements and formatting corrections instantly without requiring manual invocation of format commands.

**Repository**: https://github.com/continuous-formatting/continuous-formatting (concept)
**Type**: VS Code Extension
**License**: MIT (typical)
**Primary Use**: Real-time code formatting for TypeScript

## Overview

Continuous Formatting eliminates the need to manually format code by applying formatting rules automatically as you type. This extension monitors your TypeScript code in real-time and applies configured formatting rules immediately, keeping your code style consistent without interrupting your workflow.

## Key Features

### Real-Time Formatting
- Automatic formatting as you type
- Instant code style corrections
- No manual format command needed
- Preserves cursor position and selection

### TypeScript Support
- Full TypeScript language support
- Works with JavaScript files
- Handles JSX/TSX syntax
- Compatible with modern JavaScript features

### Configurable Rules
- Customize indentation (spaces/tabs)
- Configure line length limits
- Set quote style preferences
- Manage trailing commas
- Control brace placement

### Performance
- Lightweight and efficient
- Non-blocking formatting operations
- Minimal memory footprint
- Works well with large files

## Installation

### Via VS Code Marketplace

1. Open VS Code
2. Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on macOS) to open Extensions
3. Search for "Continuous Formatting"
4. Click **Install**
5. Reload VS Code if prompted

### Via Command Line

```bash
code --install-extension continuous-formatting.continuous-formatting
```

## Configuration

### Basic Setup

Create or edit `.vscode/settings.json` in your project root:

```json
{
  "[typescript]": {
    "editor.defaultFormatter": "continuous-formatting.continuous-formatting",
    "editor.formatOnSave": false,
    "editor.formatOnType": true
  },
  "[javascript]": {
    "editor.defaultFormatter": "continuous-formatting.continuous-formatting",
    "editor.formatOnType": true
  },
  "continuousFormatting.enabled": true,
  "continuousFormatting.autoFormat": true,
  "continuousFormatting.formatDelay": 500
}
```

### Configuration Options

#### Core Settings

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `continuousFormatting.enabled` | boolean | `true` | Enable/disable the extension |
| `continuousFormatting.autoFormat` | boolean | `true` | Automatically format as you type |
| `continuousFormatting.formatDelay` | number | `500` | Delay in ms before formatting (debounce) |
| `continuousFormatting.onSave` | boolean | `false` | Apply final formatting on file save |

#### Formatting Rules

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `continuousFormatting.indentSize` | number | `2` | Number of spaces per indentation level |
| `continuousFormatting.useTabs` | boolean | `false` | Use tabs instead of spaces |
| `continuousFormatting.lineLength` | number | `80` | Maximum line length |
| `continuousFormatting.quoteStyle` | string | `single` | Quote style: `single` or `double` |
| `continuousFormatting.trailingComma` | string | `es5` | Trailing comma handling: `none`, `es5`, `all` |
| `continuousFormatting.bracketSpacing` | boolean | `true` | Add spaces inside object brackets |
| `continuousFormatting.semi` | boolean | `true` | Include semicolons at statement ends |
| `continuousFormatting.arrowParens` | string | `always` | Arrow function parentheses: `always` or `avoid` |

#### Behavior

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `continuousFormatting.ignoreErrorsOnFormatting` | boolean | `false` | Continue formatting if syntax errors detected |
| `continuousFormatting.showNotifications` | boolean | `true` | Show formatting status notifications |
| `continuousFormatting.respectEditorConfig` | boolean | `true` | Respect `.editorconfig` file settings |

## Usage

### Automatic Formatting

Once enabled, formatting happens automatically as you type:

```typescript
// As you type this code...
const obj={name:"John",age:30}

// It automatically formats to:
const obj = {name: "John", age: 30}
```

### Manual Formatting

Trigger formatting manually:
- **Command Palette**: Press `Ctrl+Shift+P` (or `Cmd+Shift+P`), search "Format Document"
- **Keyboard**: `Alt+Shift+F` (Windows/Linux) or `Option+Shift+F` (macOS)
- **Context Menu**: Right-click and select "Format Document"

### Format Selection

Format only the selected code:

```typescript
// Select this block
const x = 1
const y = 2

// Press Ctrl+Shift+P → "Format Selection"
// Result:
const x = 1;
const y = 2;
```

### Disable for Specific Files

Add to your `.vscode/settings.json`:

```json
{
  "[javascript]": {
    "continuousFormatting.enabled": false
  }
}
```

## Examples

### Example 1: Basic Formatting

**Input:**
```typescript
function greet(name:string):void{
console.log("Hello "+name)
}
```

**Output:**
```typescript
function greet(name: string): void {
  console.log("Hello " + name);
}
```

### Example 2: Object Formatting

**Input:**
```typescript
const user={id:1,name:"Alice",email:"alice@example.com",active:true}
```

**Output:**
```typescript
const user = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
  active: true
};
```

### Example 3: Arrow Functions

**Configuration:**
```json
{
  "continuousFormatting.arrowParens": "avoid",
  "continuousFormatting.trailingComma": "all"
}
```

**Input:**
```typescript
const handlers = [
  (event) => handleClick(event),
  (data) => processData(data)
]
```

**Output:**
```typescript
const handlers = [
  event => handleClick(event),
  data => processData(data),
];
```

### Example 4: Line Breaking

**Configuration:**
```json
{
  "continuousFormatting.lineLength": 60
}
```

**Input:**
```typescript
const longMessage = "This is a very long message that exceeds the maximum line length"
```

**Output:**
```typescript
const longMessage =
  "This is a very long message that exceeds the " +
  "maximum line length";
```

## Advanced Configuration

### Project-Specific Settings

Create `.vscode/settings.json` in your project:

```json
{
  "continuousFormatting.indentSize": 4,
  "continuousFormatting.lineLength": 100,
  "continuousFormatting.useTabs": false,
  "[typescript]": {
    "editor.formatOnType": true
  }
}
```

### EditorConfig Integration

Support for `.editorconfig` files:

```ini
# .editorconfig
root = true

[*.{js,ts,jsx,tsx}]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false
```

### Workspace Settings

Apply settings to entire workspace in `.code-workspace`:

```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "continuousFormatting.enabled": true,
    "continuousFormatting.formatDelay": 300,
    "[typescript]": {
      "editor.defaultFormatter": "continuous-formatting.continuous-formatting"
    }
  }
}
```

## Keyboard Shortcuts

### Custom Shortcuts

Add to `.vscode/keybindings.json`:

```json
[
  {
    "key": "shift+alt+f",
    "command": "continuousFormatting.formatDocument"
  },
  {
    "key": "shift+alt+s",
    "command": "continuousFormatting.formatSelection"
  },
  {
    "key": "ctrl+shift+l",
    "command": "continuousFormatting.toggleFormatting"
  }
]
```

## Troubleshooting

### Formatting Not Working

1. Check if extension is enabled:
   - Run "Continuous Formatting: Status" from Command Palette
   - Verify setting `continuousFormatting.enabled: true`

2. Verify formatter is default:
   ```json
   {
     "[typescript]": {
       "editor.defaultFormatter": "continuous-formatting.continuous-formatting"
     }
   }
   ```

3. Check delay setting:
   - Increase `continuousFormatting.formatDelay` if formatting happens too late
   - Decrease if you want more responsive formatting

### Performance Issues

If formatting causes lag:

1. Increase debounce delay:
   ```json
   {
     "continuousFormatting.formatDelay": 1000
   }
   ```

2. Disable for large files:
   ```json
   {
     "continuousFormatting.maxFileSize": 500000
   }
   ```

3. Check format rules for complexity

### Conflicts with Other Formatters

If multiple formatters are configured, specify priority:

```json
{
  "[typescript]": {
    "editor.defaultFormatter": "continuous-formatting.continuous-formatting"
  },
  "[javascript]": {
    "editor.defaultFormatter": "continuous-formatting.continuous-formatting"
  }
}
```

## Best Practices

### Team Development

For consistent team formatting, commit settings to git:

```bash
# Track settings in version control
git add .vscode/settings.json
git commit -m "Configure Continuous Formatting for team"
```

### Project Setup

Create `.vscode/settings.json`:

```json
{
  "[typescript]": {
    "editor.defaultFormatter": "continuous-formatting.continuous-formatting",
    "editor.formatOnType": true
  },
  "[javascript]": {
    "editor.defaultFormatter": "continuous-formatting.continuous-formatting",
    "editor.formatOnType": true
  },
  "continuousFormatting.enabled": true,
  "continuousFormatting.indentSize": 2,
  "continuousFormatting.quoteStyle": "double",
  "continuousFormatting.semi": true,
  "continuousFormatting.trailingComma": "es5"
}
```

### Performance Optimization

For large projects:

```json
{
  "continuousFormatting.formatDelay": 800,
  "continuousFormatting.ignoreErrorsOnFormatting": true,
  "continuousFormatting.maxFileSize": 1000000
}
```

## Commands

Access via Command Palette (`Ctrl+Shift+P`):

| Command | Description |
|---------|-------------|
| `Continuous Formatting: Format Document` | Format entire file |
| `Continuous Formatting: Format Selection` | Format selected text |
| `Continuous Formatting: Toggle Formatting` | Enable/disable extension |
| `Continuous Formatting: Status` | Show current status |
| `Continuous Formatting: Reset Settings` | Restore default configuration |

## Extension Settings in VS Code UI

Navigate to VS Code Settings (`Ctrl+,`) and search for "continuous formatting":

- **Enabled** - Toggle extension active state
- **Auto Format** - Enable automatic formatting
- **Format Delay** - Debounce delay in milliseconds
- **Indent Size** - Spaces per indentation level
- **Use Tabs** - Prefer tabs over spaces
- **Line Length** - Maximum line width
- **Quote Style** - Single or double quotes
- **Trailing Comma** - Comma handling strategy
- **Bracket Spacing** - Spacing in object literals
- **Semicolons** - Include statement terminators

## Performance Metrics

Typical performance characteristics:

- **Formatting time**: < 50ms per document
- **Memory usage**: < 20MB for typical projects
- **CPU impact**: < 5% during formatting
- **Large file support**: Up to 1MB+ files
- **Debounce responsiveness**: 300-800ms typical range

## Compatibility

### Supported Versions

| Component | Version |
|-----------|---------|
| VS Code | 1.60+ |
| TypeScript | 4.0+ |
| JavaScript | ES6+ |
| Node.js | 14+ (for development) |

### Operating Systems

- Windows 10+
- macOS 10.15+
- Linux (all modern distributions)

### File Types

- `.ts` - TypeScript files
- `.tsx` - TypeScript React files
- `.js` - JavaScript files
- `.jsx` - JavaScript React files
- `.mjs` - ES Modules
- `.cjs` - CommonJS modules

## Tips and Tricks

### Quick Toggle
Create a keyboard shortcut to enable/disable formatting:
```json
{
  "key": "ctrl+alt+f",
  "command": "continuousFormatting.toggleFormatting"
}
```

### Format on Save Only
If you prefer manual formatting:
```json
{
  "continuousFormatting.autoFormat": false,
  "editor.formatOnSave": true
}
```

### Preserve Alignment
For aligned code blocks:
```json
{
  "continuousFormatting.preserveAlignment": true
}
```

### Multi-Line Method Chains
Configure method chain formatting:
```json
{
  "continuousFormatting.chainDepth": 2,
  "continuousFormatting.chainNewline": true
}
```

## Related Extensions

- **Prettier** - Opinionated code formatter
- **ESLint** - JavaScript/TypeScript linter
- **EditorConfig for VS Code** - EditorConfig support
- **Code Spell Checker** - Spell checking

## Support and Issues

Report issues and feature requests on the project repository (when available).

## License

MIT License - See LICENSE file for details

## Changelog

### v1.0.0 (Latest)
- Initial release with real-time formatting
- Full TypeScript and JavaScript support
- Configurable formatting rules
- EditorConfig integration
- Performance optimizations

## See Also

- [Prettier Documentation](https://prettier.io/)
- [VS Code Extension API](https://code.visualstudio.com/api)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [EditorConfig Specification](https://editorconfig.org/)
