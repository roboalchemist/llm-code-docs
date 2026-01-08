# Source: https://typescript-eslint.io/packages/utils

On this page# `@typescript-eslint/utils`
[](https://npmjs.com/@typescript-eslint/utils)
Utilities for working with TypeScript + ESLint together. ✨
This package contains public utilities for writing custom rules and plugins in TypeScript.
Rules declared in [`@typescript-eslint/eslint-plugin`](/packages/eslint-plugin) are created using these utility functions.
Any custom rules you write generally will be as well.
See [Custom Rules](/developers/custom-rules) for documentation on creating your own custom ESLint rules for TypeScript code.
## Exports[​](#exports)
NameDescription`AST_NODE_TYPES`An enum with the names of every single *node* found in `TSESTree`.`AST_TOKEN_TYPES`An enum with the names of every single *token* found in `TSESTree`.`ASTUtils`Tools for operating on the ESTree AST. Also includes the [`@eslint-community/eslint-utils`](https://www.npmjs.com/package/@eslint-community/eslint-utils) package, correctly typed to work with the types found in `TSESTree``ESLintUtils`Tools for creating ESLint rules with TypeScript.`JSONSchema`Strict types for the JSON Schema v4 spec - the version that ESLint uses to validate all rules with.`ParserServices`Typing for the parser services provided when parsing a file using `@typescript-eslint/typescript-estree`.`TSESLint`Types for ESLint, correctly typed to work with the types found in `TSESTree`.`TSESLintScope`The [`eslint-scope`](https://www.npmjs.com/package/eslint-scope) package, correctly typed to work with the types found in both `TSESTree` and `TSESLint``TSESTree`Types for the TypeScript flavor of ESTree created by `@typescript-eslint/typescript-estree`.[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/packages/Utils.mdx)- [Exports](#exports)