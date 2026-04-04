# Source: https://typescript-eslint.io/rules/no-import-type-side-effects

On this page# no-import-type-side-effects
Enforce the use of top-level import type qualifier when an import only has specifiers with inline type qualifiers.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
The [`--verbatimModuleSyntax`](https://www.typescriptlang.org/tsconfig#verbatimModuleSyntax) compiler option causes TypeScript to do simple and predictable transpilation on import declarations.
Namely, it completely removes import declarations with a top-level `type` qualifier, and it removes any import specifiers with an inline `type` qualifier.
The latter behavior does have one potentially surprising effect in that in certain cases TS can leave behind a "side effect" import at runtime:
```
import { type A, type B } from &#x27;mod&#x27;;
// is transpiled to
import {} from &#x27;mod&#x27;;
// which is the same as
import &#x27;mod&#x27;;
```
For the rare case of needing to import for side effects, this may be desirable - but for most cases you will not want to leave behind an unnecessary side effect import.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-import-type-side-effects": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-import-type-side-effects": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1soFtiPodIqVrJKAE0T0AZtMRl8qDJETRoAyODABfENqA)
## Examples[​](#examples)
This rule enforces that you use a top-level `type` qualifier for imports when it only imports specifiers with an inline `type` qualifier
- ❌ Incorrect- ✅ Correct```
import { type A } from &#x27;mod&#x27;;
import { type A as AA } from &#x27;mod&#x27;;
import { type A, type B } from &#x27;mod&#x27;;
import { type A as AA, type B as BB } from &#x27;mod&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1soFtiPodIqVrJKAE0T0AZtMRl8qDJETRoAyODABfENqA&code=JYWwDg9gTgLgBAbzjAnmApnAgnAvnAMyghDgHIQIATMgbgChRJZFk1McBDAZ2x3yIlylGgybR4SVBmwAaNjIBCeQsVIVqdRuAmtpHODz7z9cZUcXKBa4ZtpA&fileType=.ts)```
import type { A } from &#x27;mod&#x27;;
import type { A as AA } from &#x27;mod&#x27;;
import type { A, B } from &#x27;mod&#x27;;
import type { A as AA, B as BB } from &#x27;mod&#x27;;
import T from &#x27;mod&#x27;;
import type T from &#x27;mod&#x27;;
import * as T from &#x27;mod&#x27;;
import type * as T from &#x27;mod&#x27;;
import { T } from &#x27;mod&#x27;;
import type { T } from &#x27;mod&#x27;;
import { T, U } from &#x27;mod&#x27;;
import type { T, U } from &#x27;mod&#x27;;
import { type T, U } from &#x27;mod&#x27;;
import { T, type U } from &#x27;mod&#x27;;
import type T, { U } from &#x27;mod&#x27;;
import T, { type U } from &#x27;mod&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1soFtiPodIqVrJKAE0T0AZtMRl8qDJETRoAyODABfENqA&code=JYWwDg9gTgLgBDAnmApnA3nAgnAvnAMyghDgHIQIATMgbgChRJYFk1McBDAZ2x3yIlylGgybR4SVBmwAaOACE8hYqQrU6jcBNbSOcHn3lLDCpQNXCNDLc3gAVFUPWjbOqWkeC1IzW5YAVAa8XpYumuIsHnBBhqHOvjaR8JiOFgnW-pJsMmlOPpnJufIAqsreVq5F0aml5WGJWTLR9nXpBVXaLLW6aGXtlX7VOa0y-fmDYl0O8pjR4xXhtEA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you&#x27;re not using TypeScript 5.0&#x27;s `verbatimModuleSyntax` option and your project is built with a bundler that manages import side effects for you, this rule may not be as useful for you.
## Related To[​](#related-to)
- [`consistent-type-imports`](/rules/consistent-type-imports)
- [`import/consistent-type-specifier-style`](https://github.com/import-js/eslint-plugin-import/blob/main/docs/rules/consistent-type-specifier-style.md)
- [`import/no-duplicates` with `{"prefer-inline": true}`](https://github.com/import-js/eslint-plugin-import/blob/main/docs/rules/no-duplicates.md#inline-type-imports)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-import-type-side-effects.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-import-type-side-effects.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-import-type-side-effects.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)