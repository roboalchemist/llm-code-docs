# ESLint Config Google - Complete Configuration Reference

**Source:** https://github.com/google/eslint-config-google

## Overview

This document provides the complete ESLint configuration rules implemented by `eslint-config-google`. The rules are organized by category as they appear in the official ESLint documentation.

## Possible Errors

Rules that detect problematic code patterns that might cause errors:

```javascript
'no-cond-assign': 'off',                    // Allow conditional assignment
'no-irregular-whitespace': 'error',         // Error on irregular whitespace
'no-unexpected-multiline': 'error',         // Error on unexpected multiline
```

## Best Practices

Rules that enforce coding conventions and best practices:

```javascript
'curly': ['error', 'multi-line'],           // Braces required for multiline statements
'guard-for-in': 'error',                    // Check hasOwnProperty in for...in loops
'no-caller': 'error',                       // No arguments.caller or arguments.callee
'no-extend-native': 'error',                // Don't extend native objects
'no-extra-bind': 'error',                   // No unnecessary bind
'no-invalid-this': 'error',                 // No invalid this usage
'no-multi-spaces': 'error',                 // No multiple spaces
'no-multi-str': 'error',                    // No multiline strings
'no-new-wrappers': 'error',                 // No String/Number/Boolean constructors
'no-throw-literal': 'error',                // Throw Error objects, not literals
'no-with': 'error',                         // No with statements
'prefer-promise-reject-errors': 'error',    // Reject promises with Error objects
```

## Variables

Rules for variable declarations and usage:

```javascript
'no-unused-vars': ['error', {args: 'none'}], // No unused variables
```

## Stylistic Issues

### Spacing and Layout

```javascript
'array-bracket-spacing': ['error', 'never'],        // [1, 2, 3] not [ 1, 2, 3 ]
'array-element-newline': 'off',                     // Don't enforce element newlines
'block-spacing': ['error', 'never'],                // {a: 1}b not { a: 1 } b
'computed-property-spacing': 'error',               // obj[key] not obj[ key ]
'func-call-spacing': 'error',                       // func() not func ()
'key-spacing': 'error',                             // {key: value} with proper spacing
'keyword-spacing': 'error',                         // Space around keywords
'no-mixed-spaces-and-tabs': 'error',                // No mixed spaces/tabs
'object-curly-spacing': 'error',                    // {a: 1} with proper spacing
'semi-spacing': 'error',                            // Spacing around semicolons
'space-before-blocks': 'error',                     // Space before blocks
'space-before-function-paren': [                    // Space before function parens
  'error',
  {
    asyncArrow: 'always',    // async () => {} with space
    anonymous: 'never',      // function() {} without space
    named: 'never',          // function foo() {} without space
  }
],
'spaced-comment': ['error', 'always'],              // // comment with space
'switch-colon-spacing': 'error',                    // Spacing around switch colons
```

### Indentation and Line Length

```javascript
'indent': [
  'error', 2, {
    'CallExpression': {
      'arguments': 2,                    // 2-space indent for call arguments
    },
    'FunctionDeclaration': {
      'body': 1,                         // 1 indent for function body
      'parameters': 2,                   // 2 indent for parameters
    },
    'FunctionExpression': {
      'body': 1,                         // 1 indent for function body
      'parameters': 2,                   // 2 indent for parameters
    },
    'MemberExpression': 2,               // 2-space indent for members
    'ObjectExpression': 1,               // 1 indent for object properties
    'SwitchCase': 1,                     // 1 indent for switch cases
    'ignoredNodes': [
      'ConditionalExpression',           // Ignore ternary expressions
    ],
  },
],
'linebreak-style': 'error',                         // Unix linebreaks (LF)
'max-len': [
  'error', {
    code: 80,                           // Maximum 80 characters per line
    tabWidth: 2,
    ignoreUrls: true,                   // Ignore URLs that exceed limit
    ignorePattern: 'goog\\.(module|require)',  // Ignore goog patterns
  }
],
'no-multiple-empty-lines': ['error', {max: 2}],    // Max 2 consecutive empty lines
```

### Naming and Quotes

```javascript
'camelcase': ['error', {properties: 'never'}],     // camelCase for identifiers
'new-cap': 'error',                                // Capitalize constructor functions
'no-array-constructor': 'error',                   // Use [] not new Array()
'no-new-object': 'error',                          // Use {} not new Object()
'quote-props': ['error', 'consistent'],            // Consistent property quotes
'quotes': ['error', 'single', {                    // Single quotes preferred
  allowTemplateLiterals: true,                    // Template literals allowed
}],
'semi': 'error',                                   // Semicolons required
```

### Code Structure

```javascript
'brace-style': 'error',                   // Stroustrup style: closing brace on own line
'comma-dangle': ['error', 'always-multiline'],  // Trailing comma in multiline
'comma-spacing': 'error',                 // Space after commas
'comma-style': 'error',                   // Comma-first style
'eol-last': 'error',                      // Newline at end of file
'no-tabs': 'error',                       // Use spaces, not tabs
'no-trailing-spaces': 'error',            // No trailing whitespace
'one-var': [                              // One declaration per statement
  'error',
  {
    var: 'never',
    let: 'never',
    const: 'never',
  }
],
'operator-linebreak': ['error', 'after'], // Operators at end of line
'padded-blocks': ['error', 'never'],      // No padding inside blocks
```

## ECMAScript 6

Rules for modern JavaScript features:

```javascript
'arrow-parens': ['error', 'always'],           // Always parentheses: (x) => x
'constructor-super': 'error',                  // Call super in constructor
'generator-star-spacing': ['error', 'after'],  // function* not function *
'no-new-symbol': 'error',                      // No new Symbol()
'no-this-before-super': 'error',               // No this before super
'no-var': 'error',                             // Use const/let, not var
'prefer-const': [                              // Use const for non-reassigned
  'error',
  {destructuring: 'all'}
],
'prefer-rest-params': 'error',                 // Use ...args not arguments
'prefer-spread': 'error',                      // Use spread not .apply()
'rest-spread-spacing': 'error',                // Proper spacing with ...
'yield-star-spacing': ['error', 'after'],      // yield* not yield *
```

## Quick Reference: Setup Examples

### Basic Setup

```json
{
  "extends": "google",
  "rules": {
    "max-len": ["error", {code: 100}]
  }
}
```

### With ESLint Recommended

```json
{
  "extends": ["eslint:recommended", "google"],
  "rules": {}
}
```

### With TypeScript (using eslint-config-google-typescript)

```json
{
  "extends": "google",
  "env": {
    "es2015": true,
    "node": true
  },
  "parserOptions": {
    "ecmaVersion": 2020,
    "sourceType": "module"
  }
}
```

## Key Principles

1. **Google Style Guide Compliance**: All rules implement the [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)

2. **Modern JavaScript**: Focus on ES2015+ with preference for `const`, `let`, and arrow functions

3. **Readability**: Emphasis on proper spacing, indentation, and line length to improve code readability

4. **Compatibility**: Works with both ESLint recommended rules (when extended) and standalone

5. **Minimal Overrides**: Focused ruleset that doesn't override unnecessary ESLint rules

## Related Resources

- [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
- [ESLint Documentation](https://eslint.org/docs/)
- [ESLint Rules Reference](https://eslint.org/docs/rules/)
- [Repository on GitHub](https://github.com/google/eslint-config-google)
