# Source: https://typescript-eslint.io/packages/scope-manager

On this page# `@typescript-eslint/scope-manager`
[](https://npmjs.com/@typescript-eslint/scope-manager)
A fork of [`eslint-scope`](https://github.com/eslint/eslint-scope), enhanced to support TypeScript functionality. ✨
A "scope analyser" traverses an AST and builds a model of how variables (and in our case, types) are defined and consumed by the source code.
This form of static analysis allows you to understand and trace variables throughout the program, allowing you to access powerful information about a program without needing to drop into the much, much heavier type information.
## API[​](#api)
### `analyze(tree, options)`[​](#analyzetree-options)
Analyses a given AST and returns the resulting `ScopeManager`.
```
interface AnalyzeOptions {
/**
* Known visitor keys.
*/
childVisitorKeys?: Record<string, string[]> | null;
/**
* Whether the whole script is executed under node.js environment.
* When enabled, the scope manager adds a function scope immediately following the global scope.
* Defaults to `false`.
*/
globalReturn?: boolean;
/**
* Implied strict mode.
* Defaults to `false`.
*/
impliedStrict?: boolean;
/**
* The identifier that&#x27;s used for JSX Element creation (after transpilation).
* This should not be a member expression - just the root identifier (i.e. use "React" instead of "React.createElement").
* Defaults to `"React"`.
*/
jsxPragma?: string;
/**
* The identifier that&#x27;s used for JSX fragment elements (after transpilation).
* If `null`, assumes transpilation will always use a member on `jsxFactory` (i.e. React.Fragment).
* This should not be a member expression - just the root identifier (i.e. use "h" instead of "h.Fragment").
* Defaults to `null`.
*/
jsxFragmentName?: string | null;
/**
* The lib used by the project.
* This automatically defines a type variable for any types provided by the configured TS libs.
* For more information, see https://www.typescriptlang.org/tsconfig#lib
*
* Defaults to [&#x27;esnext&#x27;].
*/
lib?: Lib[];
/**
* The source type of the script.
*/
sourceType?: &#x27;script&#x27; | &#x27;module&#x27;;
/**
* Emit design-type metadata for decorated declarations in source.
* Defaults to `false`.
*/
emitDecoratorMetadata?: boolean;
}
```
Example usage:
```
import { analyze } from &#x27;@typescript-eslint/scope-manager&#x27;;
import { parse } from &#x27;@typescript-eslint/typescript-estree&#x27;;
const code = `const hello: string = &#x27;world&#x27;;`;
const ast = parse(code, {
// note that scope-manager requires ranges on the AST
range: true,
});
const scope = analyze(ast, {
sourceType: &#x27;module&#x27;,
});
```
## References[​](#references)
- [You can view the original BSD 2 license for the code here](https://github.com/eslint/eslint-scope/blob/dbddf14d5771b21b5da704213e4508c660ca1c64/LICENSE)
- [https://eslint.org/docs/developer-guide/scope-manager-interface](https://eslint.org/docs/developer-guide/scope-manager-interface)
- [https://github.com/eslint/eslint-scope](https://github.com/eslint/eslint-scope)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/packages/Scope_Manager.mdx)- [API](#api)[`analyze(tree, options)`](#analyzetree-options)- [References](#references)