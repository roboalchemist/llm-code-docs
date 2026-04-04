# JSLint Documentation

This directory contains comprehensive documentation for JSLint, the original opinionated JavaScript linter created by Douglas Crockford.

## Documentation Files

- **jslint-documentation.md** - Complete reference documentation covering all features, options, API, and language rules
- **README.md** - This file

## About JSLint

JSLint is a static code analysis tool for JavaScript that:

- Identifies syntax errors, style violations, and structural problems
- Enforces a professional subset of JavaScript stricter than ECMAScript standard
- Runs entirely in the browser (no code transmission to servers)
- Supports both JavaScript and JSON analysis
- Implements the "Principle of the Good Parts"

## Quick Start

### Web Interface

Visit https://www.jslint.com to use JSLint interactively:

1. Paste your JavaScript code into the editor
2. Configure options using checkboxes
3. Click "JSLint" to analyze
4. Review warnings and suggestions

### Installation

```bash
npm install jslint
```

### Basic Usage

```javascript
import jslint from './jslint.mjs';

const result = jslint("var x = 1;", { node: true });
if (!result.ok) {
    console.log(result.warnings);
}
```

## Key Configuration Options

| Option | Purpose |
|--------|---------|
| `browser` | Enable browser globals (window, document, etc.) |
| `node` | Enable Node.js globals |
| `devel` | Allow console, alert, debugger |
| `indent2` | Use 2-space indentation instead of 4 |
| `single` | Allow single quotes |
| `bitwise` | Allow bitwise operators |
| `for` | Allow for loops |
| `this` | Allow this keyword |

## Configuration Directives

Set options in your code:

```javascript
/*jslint
    browser, devel, indent2
*/

/*global myGlobal, anotherGlobal */

/*property
    length, map, slice
*/
```

## Links

- **Official Website:** https://www.jslint.com
- **GitHub Repository:** https://github.com/jslint-org/jslint
- **Code Conventions:** https://www.crockford.com/javascript/code.html

## Documentation Source

This documentation was extracted from:
- JSLint help documentation at https://www.jslint.com/help.html
- JSLint GitHub repository at https://github.com/jslint-org/jslint
- README and official resources

For the most up-to-date information, visit the official website or GitHub repository.
