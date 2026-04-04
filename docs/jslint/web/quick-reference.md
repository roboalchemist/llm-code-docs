# JSLint Quick Reference

This is a quick reference guide for JSLint. For comprehensive documentation, see jslint-documentation.md.

## Quick Links

- **Website:** https://www.jslint.com
- **GitHub:** https://github.com/jslint-org/jslint
- **Online Tool:** https://www.jslint.com

## Configuration Template

```javascript
/*jslint
    browser,     // Enable browser globals
    devel,       // Allow console, alert, debugger
    indent2,     // Use 2-space indentation
    single,      // Allow single quotes
    node         // Enable Node.js globals
*/

/*global
    myGlobal,
    anotherGlobal
*/

/*property
    length,
    map,
    slice
*/
```

## Common Rules

| Rule | Example | Fix |
|------|---------|-----|
| Use `===` not `==` | `if (x == y)` | `if (x === y)` |
| Use `const`/`let` not `var` | `var x = 1;` | `const x = 1;` |
| Declare before use | Use `x` before declaring | Declare first |
| Use semicolons | `const x = 1` | `const x = 1;` |
| Use braces with `if` | `if (x) y();` | `if (x) { y(); }` |
| Array methods over `for` | `for (let i = 0; i < arr.length; i++)` | `arr.forEach()` |
| No `++`/`--` | `x++` | `x += 1` |
| `case` needs `break` | Missing `break` | Add `break;` |

## Options Quick Reference

### Environment Options
- `browser` - Browser globals (window, document, etc.)
- `node` - Node.js globals
- `couch` - CouchDB globals
- `devel` - Development tools (console, alert, debugger)

### Syntax Options
- `bitwise` - Allow bitwise operators
- `eval` - Allow eval()
- `for` - Allow for loops
- `getset` - Allow get/set properties
- `this` - Allow this keyword
- `convert` - Allow type conversion tricks (!!, +string)

### Style Options
- `indent2` - Use 2-space indentation (default: 4)
- `long` - Allow lines > 80 characters
- `single` - Allow single-quote strings
- `subscript` - Allow subscript notation (obj["prop"])
- `nomen` - Allow unconventional names ($, _var)
- `unordered` - Allow unordered properties

### Special Options
- `beta` - Enable experimental warnings
- `trace` - Include stack traces
- `white` - Ignore whitespace rules

## Common Warnings and Fixes

### "Unexpected var"
Appears when using `var` instead of `const`/`let`.
```javascript
// Bad
var x = 1;

// Good
const x = 1;
```

### "Expected '===' and instead saw '=='"
Use strict equality.
```javascript
// Bad
if (x == 5)

// Good
if (x === 5)
```

### "Unexpected '++'"
Use += instead.
```javascript
// Bad
x++;

// Good
x += 1;
```

### "Unexpected 'this'"
Enable the `this` option or refactor.
```javascript
// With option:
/*jslint this */

// Or refactor:
function method() {
    return this.value;  // Enable with /*jslint this */
}
```

### "Unexpected dangling '_'"
Leading underscore not allowed by default.
```javascript
// Enable nomen option:
/*jslint nomen */

const _private = 42;
```

### "Missing semicolon"
Add semicolons to statement endings.
```javascript
// Bad
const x = 1

// Good
const x = 1;
```

## Directives Summary

| Directive | Purpose | Example |
|-----------|---------|---------|
| `/*jslint ...*/` | Set options for file | `/*jslint node, indent2*/` |
| `/*global ...*/` | Declare globals | `/*global myVar, myFunc*/` |
| `/*property ...*/` | Declare properties | `/*property length, map*/` |
| `/*ignore*/` | Mark unused parameter | `function f(x, ignore) {}` |
| `//jslint ignore: line` | Ignore this line | `const unused = 1; //jslint ignore: line` |

## Code Style Guidelines

### Variable Declaration
```javascript
// Good: const first
const CONSTANT = 'value';
let variable = 0;

// Bad: mixing var with let
var old = 1;
let new = 2;
```

### Function Declaration
```javascript
// Good: named functions
function processData(input) {
    return input.map(item => item * 2);
}

// Good: arrow functions with parentheses
const calculate = (a, b) => a + b;

// Bad: arrow function without parens
const compute = a => a * 2;
```

### Conditional Statements
```javascript
// Good: always use braces
if (condition) {
    doSomething();
}

// Bad: no braces
if (condition) doSomething();
```

### Loops
```javascript
// Good: array methods
array.forEach(item => {
    process(item);
});

// Acceptable: for loop with /*jslint for*/
/*jslint for*/
for (let i = 0; i < array.length; i += 1) {
    process(array[i]);
}

// Bad: for...in without hasOwnProperty
for (const key in object) {
    process(object[key]);  // Missing hasOwnProperty check
}
```

### Comments
```javascript
// Good: clear comments
// This function calculates the sum
function sum(numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}

// Allow TODO comments with devel option
console.log('TODO: implement this'); // Requires /*jslint devel*/
```

## API Usage Example

```javascript
import jslint from './jslint.mjs';

// Simple analysis
const result = jslint("const x = 1;", {
    node: true,
    indent2: true
});

console.log(result.ok);          // true if no warnings
console.log(result.warnings);    // array of warning objects
console.log(result.edition);     // JSLint version

// With globals
const globalResult = jslint(
    "console.log(myGlobal);",
    { node: true },
    ["myGlobal"]
);

// Process warnings
if (!result.ok) {
    result.warnings.forEach(warning => {
        console.log(`Line ${warning.line}: ${warning.message}`);
    });
}
```

## Integration Examples

### Pre-commit Hook
```bash
#!/bin/bash
node jslint.mjs src/**/*.js || exit 1
```

### Build Script
```javascript
// build.js
import { lintFiles } from './jslint.mjs';

lintFiles(['src/**/*.js'], {
    node: true,
    indent2: true
}).then(result => {
    if (!result.ok) {
        console.error('Linting failed');
        process.exit(1);
    }
});
```

## Recommended Settings for Different Environments

### Browser Project
```javascript
/*jslint
    browser,
    devel,
    indent2,
    single
*/
```

### Node.js Project
```javascript
/*jslint
    node,
    devel,
    indent2
*/
```

### Strict Quality
```javascript
/*jslint
    browser,
    indent2
*/
```

### Relaxed (with justification)
```javascript
/*jslint
    browser,
    devel,
    indent2,
    single,
    this,
    for
*/
```

## See Also

- Full documentation: jslint-documentation.md
- Official help: https://www.jslint.com/help.html
- Code conventions: https://www.crockford.com/javascript/code.html
