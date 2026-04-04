# Source: https://typescript-eslint.io/rules/no-misused-new

On this page# no-misused-new
Enforce valid definition of `new` and `constructor`.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
JavaScript classes may define a `constructor` method that runs when a class instance is newly created.
TypeScript allows interfaces that describe a static class object to define a `new()` method (though this is rarely used in real world code).
Developers new to JavaScript classes and/or TypeScript interfaces may sometimes confuse when to use `constructor` or `new`.
This rule reports when a class defines a method named `new` or an interface defines a method named `constructor`.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-misused-new": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-misused-new": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtLlZkiACa0miAO7ooiaNA7RI4MAF8QyoA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
declare class C {
new(): C;
}
interface I {
new (): I;
constructor(): void;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtLlZkiACa0miAO7ooiaNA7RI4MAF8QyoA&code=CYUwxgNghgTiAEkoGdnwMLwN4Ch7wDsQB3ACgEoAuDAbhwF8ccBLAgFxBgDMowEBJbHkIl4Favzr4wAewLI2MAK5g2MmOPgA3Gc2B16QA&fileType=.ts)```
declare class C {
constructor();
}
interface I {
new (): C;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtLlZkiACa0miAO7ooiaNA7RI4MAF8QyoA&code=CYUwxgNghgTiAEkoGdnwMLwN4Ch6IHsA7ZAFxgFcxSCYAKASgG4cBfHHASyNJBgDMoYBAElseeERAB3eIwBcGFqyA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you intentionally want a class with a `new` method, and you&#x27;re confident nobody working in your code will mistake it with a constructor, you might not want this rule.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-misused-new.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-misused-new.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-misused-new.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)