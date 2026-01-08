# JSLint Documentation

Source: https://www.jslint.com/help.html

JSLint is the original opinionated JavaScript linter created by Douglas Crockford. It examines JavaScript programs to identify potential problems and enforces a professional subset of the language that is stricter than the ECMAScript standard.

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Configuration Directives](#configuration-directives)
4. [Configuration Options](#configuration-options)
5. [Language Rules](#language-rules)
6. [Whitespace Standards](#whitespace-standards)
7. [Analysis Report](#analysis-report)
8. [JavaScript API](#javascript-api)
9. [Philosophy](#philosophy)

## Overview

JSLint is a static code analysis tool that functions like the `lint` tool for C, but tailored specifically for JavaScript. It implements the "Principle of the Good Parts," which states: "If a feature is sometimes useful and sometimes dangerous and if there is a better option then always use the better option."

### Core Purpose

JavaScript began as a lightweight language for simple webpage tasks but has evolved into a platform for substantial projects. JSLint helps developers write higher-quality code by enforcing a professional subset of JavaScript—stricter than the ECMAScript standard.

**Key Principle:** JSLint rejects many programs that browsers accept. The tool prioritizes code quality over permissiveness, checking not only syntax errors but also style conventions and structural problems.

### Analysis Scope

- Identifies syntax errors
- Flags style violations
- Detects structural problems
- Scans both JavaScript and JSON source code
- Does not prove program correctness but provides additional review

## Key Features

### ECMAScript 6 Support

JSLint recognizes beneficial ES6 features including:

- Ellipsis operator (`...`) for variadic functions
- `let` and `const` statements with proper scoping
- Destructuring in parameter lists and variable declarations
- Enhanced object literals with shorthand syntax
- Fat arrow (`=>`) functions
- `import` and `export` statements
- Template literals (without nesting)
- Global constructors: `Map`, `Set`, `WeakMap`, `WeakSet`
- Binary (`0b`) and octal (`0o`) number formats
- Proper tail calls in ES6 for improved recursion efficiency

### JSON Support

JSLint can scan both JavaScript and JSON source code, detecting issues in both formats.

## Configuration Directives

Configuration can be controlled via comment directives placed before the first statement in your code.

### `/*global*/` Directive

Declares global variables available to a file. Commonly used before ES6 modules for linking source files.

**Example:**
```javascript
/*global
ADSAFE, report, jslint
*/
```

**Characteristics:**
- Listed names become read-only globals
- Names separated by commas
- Inhibits warnings but doesn't create runtime variables
- Only functional with the "Assume a browser" option
- Incompatible with `import`/`export`

### `/*jslint*/` Directive

Controls JSLint options via comment directives. Place this before the first statement.

**Example:**
```javascript
/*jslint
    bitwise, node
*/
```

### `/*property*/` Directive

Declares property identifiers used in the file. JSLint verifies all property names against this list to catch typing errors.

JSLint automatically generates a property list at the report's bottom, which you can copy into your source files:

```javascript
/*property
    length, map, slice
*/
```

## Configuration Options

| Option | Purpose |
|--------|---------|
| `beta` | Enables experimental warnings including variable redefinition and declaration ordering checks |
| `bitwise` | Allows bitwise operators (normally discouraged as `&` likely means `&&`) |
| `browser` | Predefined browser globals; rejects `import`/`export`; disallows file-level "use strict" |
| `convert` | Permits `!!`, unary `+`, and string concatenation for type conversion |
| `couch` | Enables CouchDB-specific globals |
| `devel` | Allows development tools like `console`, `alert`, `debugger`, and `TODO` comments |
| `eval` | Permits `eval` function usage |
| `fart` | Allows complex fat-arrow functions |
| `for` | Enables `for` loops (array methods preferred) |
| `getset` | Permits `get` and `set` accessor properties |
| `indent2` | Uses 2-space indentation (default is 4) |
| `long` | Permits lines exceeding 80 characters |
| `node` | Predefined Node.js environment globals |
| `nomen` | Allows unconventional property names (`$`, `_foo`, etc.) |
| `single` | Permits single-quote string literals |
| `subscript` | Allows subscript notation for properties (e.g., `foo["bar"]`) |
| `this` | Permits `this` keyword usage |
| `trace` | Includes JSLint stack traces for debugging |
| `unordered` | Allows non-alphabetical property/parameter declarations |
| `white` | Ignores whitespace rules |

### The `ignore` Identifier

The `ignore` identifier marks parameters that intentionally remain unused, suppressing unused variable warnings:

```javascript
function handler(ignore, value) {
    return doSomethingUseful(value);
}
```

## Language Rules

### Variable Declaration

Three statements declare variables, each with distinct characteristics:

- **`var`**: Exhibits hoisting behavior; outdated approach
- **`let`**: Respects block scope; modern alternative
- **`const`**: Like `let` but prevents reassignment; preferred choice

**JSLint Enforcement:**
- Single declaration per name in a function
- Declaration before usage
- Isolation to the declaring block
- No shadowing of outer scope variables
- Consistency—don't mix `var` and `let`
- One declaration per statement

### Comparison Operators

The language's equality operators present historical problems. **JSLint requires:**

- `==` is forbidden (promotes type-coercion errors)
- `===` required for comparisons
- Assignments prohibited in expression position
- Comparisons forbidden in statement position

This increases visual distance between assignment (`=`) and comparison (`===`).

### Semicolons

JSLint expects statement-terminating semicolons except after: `for`, `function`, `if`, `switch`, `try`, `while`.

**Important:** Automatic semicolon insertion is unreliable and should not be depended upon in production code.

### Function Syntax

Four syntactic forms create function objects:

**Function Statement:**
```javascript
function name(parameters) {
    statements;
}
```

**Function Expression:**
```javascript
const name = function(parameters) {
    statements;
};
```

**Enhanced Object Literal:**
```javascript
const obj = {
    name(parameters) {
        statements;
    }
};
```

**Fat Arrow:**
```javascript
const name = (parameters) => expression;
```

JSLint requires parentheses around arrow function parameters and forbids braces after `=>` to prevent ambiguity.

### Comma Usage

The comma operator is unnecessary and can obscure errors. JSLint permits commas only as separators, not operators. Array and object literal trailing commas are disallowed.

### Blocks

Blocks are required with: `function`, `if`, `switch`, `while`, `for`, `do`, `try`

Statements like `if` must use braces:

```javascript
if (condition) {
    statements;
}
```

Block form proves more resilient in collaborative codebases.

### Expression Statements

Valid expressions: assignments and function/method calls. All other standalone expressions trigger errors.

### Loop Constructs

#### `for` Loops

JSLint discourages traditional `for` loops, recommending array methods (`forEach`, `map`, etc.) instead. Use the `for` option to suppress some warnings.

**Discouraged:**
```javascript
for (let i = 0; i < array.length; i++) {
    process(array[i]);
}
```

**Preferred:**
```javascript
array.forEach(function(element) {
    process(element);
});
```

#### `for...in` Loops

Not recommended; prone to prototype chain pollution. If used, filter with `hasOwnProperty()`:

```javascript
for (name in object) {
    if (object.hasOwnProperty(name)) {
        // process
    }
}
```

**Better alternative:** Use `Object.keys()`:

```javascript
Object.keys(object).forEach(function(name) {
    // process
});
```

### Switch Statements

Each `case` must conclude with `break`, `return`, or `throw` to prevent unintended fall-through:

```javascript
switch (value) {
    case 1:
        doSomething();
        break;
    case 2:
        doSomethingElse();
        break;
    default:
        doDefault();
}
```

### `with` Statement

Never use. JSLint rejects this construct entirely.

### Labels

Permitted only on statements interacting with `break`: `switch`, `while`, `do`, `for`. Labels must not duplicate variable or parameter names.

### Unreachable Code

JSLint expects `return`, `break`, or `throw` statements to be followed by closing braces or `case`/`default` clauses.

```javascript
function example() {
    if (condition) {
        return value;
    }
    // Unreachable code here triggers warning
    console.log('never runs');
}
```

### Operator Cautions

- `+` must not be followed by `+` or `++`
- `-` must not be followed by `-` or `--`
- Use parentheses to clarify intent

**Good:**
```javascript
value = value + 1;
value = value + (+negative);
```

**Bad:**
```javascript
value = value ++ 1;  // Ambiguous
```

### Increment/Decrement Operators

`++` and `--` are discouraged despite being valid. They enable excessive complexity and create off-by-one errors. Use `+=` and `-=` instead:

**Discouraged:**
```javascript
count++;
value--;
```

**Preferred:**
```javascript
count += 1;
value -= 1;
```

### `void` Operator

Rejected as confusing and unnecessary. In JavaScript, `void` returns `undefined`.

### Regular Expressions

JSLint checks for portability issues and visual ambiguities. Regular expression literals must be preceded by: `(`, `=`, `:`, or `,`.

### `this` Keyword

Discouraged and disruptive to language comprehension. Suppress warnings via the `this` option if unavoidable.

### Constructors and `new`

Constructor functions must use PascalCase naming conventions. The `new` prefix is required when invoking constructors and forbidden otherwise.

**Avoid wrapper forms:**
```javascript
// Don't do this:
new Number(5);
new String("text");
new Boolean(true);
new Object();

// Instead:
Object.create(null);
```

## Whitespace Standards

### Indentation

Increases by 4 spaces (or 2 with `indent2` option) when the line ends with `{`, `[`, or `(`. Closing tokens restore previous indentation:

```javascript
const result = functionCall(
    argument1,
    argument2,
    argument3
);
```

### Ternary Operators

Question marks and colons always begin lines and indent 4 spaces:

```javascript
return (
    (condition)
    ? trueValue
    : falseValue
);
```

### Function Spacing

The word `function` always has one trailing space:

```javascript
function name() {}  // Correct
function() {}       // Correct
functionName() {}   // Not a function declaration
```

### Clause Indentation

`case`, `catch`, `default`, `else`, `finally` are not indented like statements:

```javascript
try {
    doSomething();
} catch (error) {
    handleError();
} finally {
    cleanup();
}
```

### Invocation Distinction

Spacing differentiates function calls from other constructs.

### Tabs vs. Spaces

Use spaces exclusively. Tabs lack universal width standards. While editors may use tabs internally, convert to spaces before committing.

## Analysis Report

### Function Report Contents

For each function, JSLint reports:

- **Line number:** Where the function begins
- **Function name:** Or guessed name for anonymous functions
- **Parameters:** Listed explicitly
- **Variables:** Declared within the function
- **Closure:** Variables/parameters accessed by nested functions
- **Exceptions:** Variables declared in `catch` clauses
- **Outer:** Variables declared in containing functions
- **Global:** Global variables used (minimize these)
- **Label:** Statement labels used

The report also includes all property names used via:
- Dot notation: `object.property`
- Subscript notation: `object["property"]`
- Object literals: `{ property: value }`

### Interpreting Warnings

JSLint output includes:
1. Line and character position of the issue
2. Description of the problem
3. Suggested fix or explanation
4. Function context (which function contains the issue)

## JavaScript API

### `jslint()` Function

Use JSLint programmatically in your JavaScript code.

**Signature:**
```javascript
jslint(source, option_object, global_array)
```

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | String or Array | Yes | Program text with `\n`, `\r`, or `\r\n` line breaks, or array of strings |
| `option_object` | Object | No | Options with boolean `true` or small number values |
| `global_array` | Array | No | Strings naming globals permitted in the program |

The function does not modify arguments.

**Example:**
```javascript
const result = jslint(
    "var x = 1;",
    {
        browser: true,
        devel: true
    },
    ["myGlobal"]
);
```

### Return Object Properties

The function returns an object with the following properties:

| Property | Type | Content |
|----------|------|---------|
| `directives` | Array | Comments containing directives |
| `edition` | String | JSLint version |
| `exports` | Object | Exported names and values |
| `froms` | Array | Strings from `import` statements |
| `functions` | Array | Function objects |
| `global` | Object | Global/outermost body |
| `id` | String | Always `"(JSLint)"` |
| `json` | Boolean | `true` if source is JSON |
| `lines` | Array | Source lines as strings |
| `module` | Boolean | `true` if contains `import`/`export` |
| `ok` | Boolean | `true` if no warnings found |
| `option` | Object | Passed-in or empty options |
| `property` | Object | Property names and occurrence counts |
| `stop` | Boolean | `true` if processing halted early |
| `tokens` | Array | Token objects in source order |
| `tree` | Array | Top-level statement tokens forming parse tree |
| `warnings` | Array | Warning objects |

### Token Objects

Source files comprise tokens: identifiers, operators, punctuators, literals, and comments (whitespace is not tokenized).

**Common Token Properties:**

| Property | Type | Description |
|----------|------|-------------|
| `arity` | String | `unary`, `binary`, `ternary`, `assignment`, `statement`, `variable`, `function`, `pre`, `post` |
| `block` | Token/Array | Block/compound statement contents |
| `body` | Boolean | `true` if block is function body |
| `catch` | Token | `catch` clause (on `try` tokens) |
| `closure` | Boolean | `true` if accessed by inner functions |
| `complex` | Boolean | `true` if using ES6 parameter syntax |
| `constant` | Boolean | `true` if compile-time constant |
| `context` | Object | Container for variables/parameters/labels/exceptions |
| `directive` | Boolean | Directive type: `jslint`, `global`, `property` |
| `disrupt` | Boolean | `true` if disruptive statement or block |
| `dot` | Boolean | `true` if previous token was dot |
| `ellipsis` | Boolean | `true` if preceded by `...` |
| `else` | Array | Alternate block (if/else, switch/default, try/finally) |
| `expression` | Token/Array | One or more expressions |
| `extra` | String | `get` or `set` for properties |
| `flag` | Object | Regexp flags: `g`, `i`, `m`, `u`, `y` |
| `from` | Number | Starting position within line (0 = left margin) |
| `id` | String | Token text; special: `"(comment)"`, `"(number)"`, `"(regexp)"`, `"(string)"`, `"(end)"`, `"(global)"` |
| `identifier` | Boolean | `true` if token is identifier |
| `import` | String | `import...from` literal string |
| `inc` | Token | Increment clause of `for` statement |
| `initial` | Token | Initialization clause of `for` statement |
| `label` | Token | Statement label or object property name |
| `level` | Number | Nesting level (0 = global, 1+ = functions) |
| `line` | Number | Line number (0-indexed; last line if multi-line) |
| `name` | Token/String | Function name |
| `names` | Token/Array | Parameters or `=` left-side names |
| `nr` | Number | Token sequence number |
| `parameters` | Array | Function parameter list |
| `parent` | Token | Containing function |
| `quote` | String | Quote character (string literals) |
| `role` | String | `exception`, `function`, `label`, `parameter`, `variable` |
| `shebang` | String | First line if starting with `#!` |
| `statement` | Boolean | `true` if token starts statement |
| `strict` | Token | `"use strict"` pragma |
| `thru` | Number | Ending position within line |
| `value` | String/Array | Token text; array for long comments/megastrings |
| `variable` | Token | Links variable to definition |
| `warning` | Object | Associated warning |
| `wrapped` | Boolean | `true` if expression wrapped in parens |
| `writable` | Boolean | `true` if variable assignable |

### Report Functions

The `report` object provides utility functions accepting `jslint()` results:

| Function | Output |
|----------|--------|
| `error` | HTML fragment detailing warnings |
| `function` | HTML detailing all function declarations |
| `property` | JSLint property directive for pasting into files |

## Delivery Files

| Filename | Purpose |
|----------|---------|
| `help.html` | Single-page JSLint application documentation |
| `index.html` | Single-page JSLint application interface |
| `jslint.mjs` | ES6 JSLint function (no dependencies) |

## Philosophy

JSLint intentionally rejects code some consider acceptable. The goal is producing error-free programs. While JSLint warns about things not necessarily wrong in isolation, such patterns have historically masked errors. The tool emphasizes visual distance between correct and incorrect code.

As stated by Saint-Exupéry: "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."

### Why JSLint is Strict

- **Prevention over Permissiveness:** Many warnings flag patterns that are occasionally incorrect in ways that are difficult to detect
- **Visual Clarity:** Correct code should look distinctly different from incorrect code
- **Professional Subset:** Enforces a professional subset of JavaScript that encourages best practices
- **Long-term Maintainability:** Strict standards make code easier to maintain across teams and time periods

## Installation and Usage

### Web Interface

Visit https://www.jslint.com to use the interactive web application:

1. Paste JavaScript code into the editor
2. Configure options as needed
3. Click the JSLint button
4. Review warnings and fixes

**Note:** Analysis runs entirely client-side without network transmission of your code.

### Command-Line Usage

JSLint can be used as a Node.js module:

```bash
npm install jslint
```

### As a Module

```javascript
import jslint from './jslint.mjs';

const source = `var x = 1;`;
const options = { node: true };
const result = jslint(source, options);

if (result.ok) {
    console.log('No issues found');
} else {
    result.warnings.forEach(warning => {
        console.log(`Line ${warning.line}: ${warning.message}`);
    });
}
```

## Further Resources

- **Official Website:** https://www.jslint.com
- **GitHub Repository:** https://github.com/jslint-org/jslint
- **Code Conventions:** https://www.crockford.com/javascript/code.html
- **JSON Standards:** https://www.json.org/

## Related Tools

While JSLint is the original JavaScript linter, other linters offer different philosophies:

- **ESLint:** More configurable with a large ecosystem of rules and plugins
- **JSHint:** A fork of JSLint with more flexible options
- **StandardJS:** Zero-config JavaScript linter based on a specific style guide

## Common Use Cases

### Enforcing Code Quality

Use JSLint directives to maintain consistent code quality across a project:

```javascript
/*jslint
    browser, devel, indent2
*/

function myFunction(parameter) {
    console.log(parameter);
}
```

### Catching Common Mistakes

JSLint catches patterns that frequently lead to bugs:

- Missing `const` or `let` declarations
- Loose equality comparisons (`==` instead of `===`)
- Undeclared globals
- Unreachable code
- Missing semicolons

### Integration with Development Workflow

Integrate JSLint into your build process:

```bash
node jslint.mjs myfile.js
```

Or use in pre-commit hooks to ensure code quality before commits.
