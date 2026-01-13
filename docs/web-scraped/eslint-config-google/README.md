# eslint-config-google

> ESLint [shareable config](http://eslint.org/docs/developer-guide/shareable-configs.html) for the [Google JavaScript style guide (ES2015+ version)](https://google.github.io/styleguide/jsguide.html)

**Source:** https://github.com/google/eslint-config-google

## Installation

```
$ npm install --save-dev eslint eslint-config-google
```

## Usage

Once the `eslint-config-google` package is installed, you can use it by specifying `google` in the [`extends`](http://eslint.org/docs/user-guide/configuring#extending-configuration-files) section of your [ESLint configuration](http://eslint.org/docs/user-guide/configuring).

```js
{
  "extends": "google",
  "rules": {
    // Additional, per-project rules...
  }
}
```

### Using the `google` config with `eslint:recommended`

There are several rules in the [`eslint:recommended` ruleset](http://eslint.org/docs/rules/) that Google style is not opinionated about that you might want to enforce in your project.

To use Google style in conjunction with ESLint's recommended rule set, extend them both, making sure to list `google` last:

```js
{
  "extends": ["eslint:recommended", "google"],
  "rules": {
    // Additional, per-project rules...
  }
}
```

To see how the `google` config compares with `eslint:recommended`, refer to the [source code of `index.js`](https://github.com/google/eslint-config-google/blob/main/index.js), which lists every ESLint rule along with whether (and how) it is enforced by the `google` config.

## Configuration Rules

The configuration implements Google's JavaScript style guide for ES2015+ code. Key rules include:

### Code Quality Rules (Best Practices)
- `guard-for-in` - Enforce `for...in` loops to check hasOwnProperty
- `no-caller` - Disallow use of `arguments.caller` or `arguments.callee`
- `no-extend-native` - Disallow extending of native objects
- `no-extra-bind` - Disallow unnecessary function binding
- `no-invalid-this` - Disallow `this` keywords outside of classes or class-like objects
- `no-multi-spaces` - Disallow multiple spaces
- `no-multi-str` - Disallow multiline strings
- `no-new-wrappers` - Disallow new operators with the String, Number, and Boolean objects
- `no-throw-literal` - Disallow throwing literals as exceptions
- `no-with` - Disallow `with` statements
- `prefer-promise-reject-errors` - Require rejecting promise with error objects

### Stylistic Rules

#### Spacing and Indentation
- `array-bracket-spacing` - Never allow spaces inside brackets
- `block-spacing` - Never allow space inside blocks
- `comma-spacing` - Require space after commas
- `computed-property-spacing` - Require no space inside computed properties
- `func-call-spacing` - Require no space between function names and their invocations
- `indent` - 2 spaces, with specific rules for call expressions, function declarations, and objects
- `key-spacing` - Enforce spacing around keys in objects
- `keyword-spacing` - Enforce spacing around keywords
- `object-curly-spacing` - Enforce spacing inside curly braces
- `semi-spacing` - Enforce spacing around semicolons
- `space-before-blocks` - Enforce spacing before blocks
- `space-before-function-paren` - Enforce spacing before function parentheses
- `spaced-comment` - Require space after comment slashes

#### Code Format
- `brace-style` - Enforce stroustrup brace style
- `camelcase` - Enforce camelCase naming convention
- `comma-dangle` - Require trailing commas in multiline
- `comma-style` - Enforce comma-first style
- `curly` - Enforce braces for multiline statements
- `eol-last` - Require newline at end of file
- `linebreak-style` - Enforce Unix linebreak style
- `max-len` - Enforce 80 character line length (with exceptions for URLs and goog.module/require)
- `no-mixed-spaces-and-tabs` - Disallow mixed spaces and tabs
- `no-multiple-empty-lines` - Disallow multiple consecutive empty lines (max 2)
- `no-new-object` - Disallow Object constructor
- `no-tabs` - Disallow tabs
- `no-trailing-spaces` - Disallow trailing spaces
- `new-cap` - Require capitalization of constructor functions
- `no-array-constructor` - Disallow Array constructor
- `operator-linebreak` - Enforce operators at end of line
- `padded-blocks` - Disallow padding inside blocks
- `quote-props` - Enforce consistent quote properties
- `quotes` - Enforce single quotes (allow template literals)
- `semi` - Require semicolons
- `switch-colon-spacing` - Enforce spacing around switch colons
- `one-var` - Enforce one variable declaration per statement

#### Variables
- `no-unused-vars` - Disallow unused variables (except function parameters)

#### ES2015+
- `arrow-parens` - Always require parentheses around arrow function parameters
- `constructor-super` - Require super() calls in constructors
- `generator-star-spacing` - Enforce space after * in generators
- `no-new-symbol` - Disallow new with Symbol
- `no-this-before-super` - Disallow this before super
- `no-var` - Require `const` or `let` instead of `var`
- `prefer-const` - Require `const` for non-reassigned variables
- `prefer-rest-params` - Require rest parameters instead of `arguments`
- `prefer-spread` - Require spread operators instead of `.apply()`
- `rest-spread-spacing` - Enforce spacing with rest and spread operators
- `yield-star-spacing` - Enforce spacing around `*` in yield* expressions

## License

Apache License 2.0

See [License](https://github.com/google/eslint-config-google/blob/main/LICENSE)
