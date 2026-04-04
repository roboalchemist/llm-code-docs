# Source: https://typescript-eslint.io/rules/no-unsafe-argument

On this page# no-unsafe-argument
Disallow calling a function with a value with type `any`.
✅Extending [`"plugin:@typescript-eslint/recommended-type-checked"`](/users/configs#recommended-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
The `any` type in TypeScript is a dangerous "escape hatch" from the type system.
Using `any` disables many type checking rules and is generally best used only as a last resort or when prototyping code.
Despite your best intentions, the `any` type can sometimes leak into your codebase.
Calling a function with an `any` typed argument creates a potential safety hole and source of bugs.
This rule disallows calling a function with `any` in its arguments.
That includes spreading arrays or tuples with `any` typed elements as function arguments.
This rule also compares generic type argument types to ensure you don&#x27;t pass an unsafe `any` in a generic position to a receiver that&#x27;s expecting a specific type.
For example, it will error if you pass `Set<any>` as an argument to a parameter declared as `Set<string>`.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unsafe-argument": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unsafe-argument": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZolp9oAc1gBbRC3RRE0aB2iRwYAL4h1QA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
declare function foo(arg1: string, arg2: number, arg3: string): void;
const anyTyped = 1 as any;
foo(...anyTyped);
foo(anyTyped, 1, &#x27;a&#x27;);
const anyArray: any[] = [];
foo(...anyArray);
const tuple1 = [&#x27;a&#x27;, anyTyped, &#x27;b&#x27;] as const;
foo(...tuple1);
const tuple2 = [1] as const;
foo(&#x27;a&#x27;, ...tuple2, anyTyped);
declare function bar(arg1: string, arg2: number, ...rest: string[]): void;
const x = [1, 2] as [number, ...number[]];
bar(&#x27;a&#x27;, ...x, anyTyped);
declare function baz(arg1: Set<string>, arg2: Map<string, string>): void;
baz(new Set<any>(), new Map<any, string>());
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZolp9oAc1gBbRC3RRE0aB2iRwYAL4h1QA&code=CYUwxgNghgTiAEAzArgOzAFwJYHtVJxwApYBzARgC54BnDGLVUgGnjICZrVkBbAIxAxWZAMzU6DJgEpqANxxZgAbgBQKsHjptUATwAqOgA4hg8ALzxybGtp2qViQkQB0rqLoPHgU1Y%2BLv9IxNWclYAcigwnzUNVC0AgEEYGCgdagCAbQBdc3hs3ydXZ0Tk1Oj1TQx4DGRDCBArCwyIsOEPIOBwvjCcqBtYugLiIpq6hvKBqtH69lyM8l7%2ByqGiFtYR2pm2wK9y0EhYBBR0bDx4PlgSGApxekYWNmvOeG5%2BQXXXODpbyVJsmXg8kUqkm8AAHnNQvB2Is8q8BEJ4EV4YJsllVBcYKtIh9nGDtp4THtwNA4Eg0JhcPgLgAvK43eAAZRAGAAPBJ7gA%2BYRPagAWSghnZdyYrA5TE5AKByhUtKIqBAAHcmSzWQFOUQpKwFcqBUKAmKRaQNVIfEA&fileType=.ts)```
declare function foo(arg1: string, arg2: number, arg3: string): void;
foo(&#x27;a&#x27;, 1, &#x27;b&#x27;);
const tuple1 = [&#x27;a&#x27;, 1, &#x27;b&#x27;] as const;
foo(...tuple1);
declare function bar(arg1: string, arg2: number, ...rest: string[]): void;
const array: string[] = [&#x27;a&#x27;];
bar(&#x27;a&#x27;, 1, ...array);
declare function baz(arg1: Set<string>, arg2: Map<string, string>): void;
baz(new Set<string>(), new Map<string, string>());
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZolp9oAc1gBbRC3RRE0aB2iRwYAL4h1QA&code=CYUwxgNghgTiAEAzArgOzAFwJYHtVJxwApYBzARgC54BnDGLVUgGnjICZrVkBbAIxAxWZAMzU6DJgEpqANxxZgAbgBQKxISIByKFtblWWvlqmqVYPHXgZkABwghy8ALzwA2jr3wD8I1oC6bDTwFqh0qhrEAHQxNvaOpmqgkLAIKOjYePB8sCQwFOL0jCxs%2BZzw3PyCrDFRcHSFkqRu-jLw8oqqoVawMFAAno3FLS7unv6qOTDauvo1Mb0DiSrJ0HBIaJi4%2BDkAXnkF8ADKIBgAPBLFAHzCZdQAslC2F0VMrJdMV20dyip7RKgQAB3Y6nF5NK5EKSsQEgx7PD4lRGQqSmIA&fileType=.ts)
There are cases where the rule allows passing an argument of `any` to `unknown`.
Example of `any` to `unknown` assignment that are allowed:
```
declare function foo(arg1: unknown, arg2: Set<unknown>, arg3: unknown[]): void;
foo(1 as any, new Set<any>(), [] as any[]);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZolp9oAc1gBbRC3RRE0aB2iRwYAL4h1QA&code=CYUwxgNghgTiAEAzArgOzAFwJYHtVJxwApYBzARgC540BrVHAd1QBp4yAmagZRAwB46DZgD42ZAMzUhTVAG0AugEpqANxxZgAbgBQiQkXLsAzu1QBPNqhCN4vAVAsiiStopNnzipVqA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your codebase has many existing `any`s or areas of unsafe code, it may be difficult to enable this rule.
It may be easier to skip the `no-unsafe-*` rules pending increasing type safety in unsafe areas of your project.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Related To[​](#related-to)
- [Avoiding `any`s with Linting and TypeScript](/blog/avoiding-anys)
- [`no-explicit-any`](/rules/no-explicit-any)
- [`no-unsafe-assignment`](/rules/no-unsafe-assignment)
- [`no-unsafe-call`](/rules/no-unsafe-call)
- [`no-unsafe-member-access`](/rules/no-unsafe-member-access)
- [`no-unsafe-return`](/rules/no-unsafe-return)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unsafe-argument.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unsafe-argument.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unsafe-argument.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)