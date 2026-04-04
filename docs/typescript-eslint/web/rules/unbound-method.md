# Source: https://typescript-eslint.io/rules/unbound-method

On this page# unbound-method
Enforce unbound methods are called with their expected scope.
✅Extending [`"plugin:@typescript-eslint/recommended-type-checked"`](/users/configs#recommended-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
Class method functions don&#x27;t preserve the class scope when passed as standalone variables ("unbound").
If your function does not access `this`, [you can annotate it with `this: void`](https://www.typescriptlang.org/docs/handbook/2/functions.html#declaring-this-in-a-function), or consider using an arrow function instead.
Otherwise, passing class methods around as values can remove type safety by failing to capture `this`.
This rule reports when a class method is referenced in an unbound manner.
TipIf you&#x27;re working with `jest`, you can use [`eslint-plugin-jest`&#x27;s version of this rule](https://github.com/jest-community/eslint-plugin-jest/blob/main/docs/rules/unbound-method.md) to lint your test files, which knows when it&#x27;s ok to pass an unbound method to `expect` calls.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/unbound-method": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/unbound-method": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6WJgIwHsOATWgFtE%2BABbc%2B6KImjRu0SODABfEMqA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
class MyClass {
public log(): void {
console.log(this);
}
}
const instance = new MyClass();
// This logs the global scope (`window`/`global`), not the class instance
const myLog = instance.log;
myLog();
// This log might later be called with an incorrect scope
const { log } = instance;
// arith.double may refer to `this` internally
const arith = {
double(x: number): number {
return x * 2;
},
};
const { double } = arith;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6WJgIwHsOATWgFtE%2BABbc%2B6KImjRu0SODABfEMqA&code=MYGwhgzhAECyCeBhcVoG8BQ1oAcCuARiAJbDQgD2A5gBQCUAXNAG4XEAm6W20wFAdhAogApgDpKtAC4ALYhDoBubgF8MajH0FToxbWH7AR0ALzR%2BIgO5wkKCPWUYA9E%2BgAVOTEkxZxqpQIwEGgIPhxjGgADSz12CktIp0j-CkCQSLoAGnMKHV9eO119QxFNAQgdAFt4ABlqUyKKgyMJamVqutolDGdXD3lyesriKhkdcCkRACdoAmNgINFOGNloAyK%2BKamRYB1QinCy7XRBqmgVBr0mkscXNaniWTE4wlFoSrB4aG2AM2noKQUaCRWTySJFSZTfiLeBHCr3R4yBqYbAvIgiGgADyY-DwlTmU0Y5jxBK4PG%2BIikeCh0Ex0AAVNAAEzKbAqTLqZRaeFoaBot4XMxgB6yRRAA&fileType=.ts)```
class MyClass {
public logUnbound(): void {
console.log(this);
}
public logBound = () => console.log(this);
}
const instance = new MyClass();
// logBound will always be bound with the correct scope
const { logBound } = instance;
logBound();
// .bind and lambdas will also add a correct scope
const dotBindLog = instance.logUnbound.bind(instance);
const innerLog = () => instance.logUnbound();
// arith.double explicitly declares that it does not refer to `this` internally
const arith = {
double(this: void, x: number): number {
return x * 2;
},
};
const { double } = arith;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6WJgIwHsOATWgFtE%2BABbc%2B6KImjRu0SODABfEMqA&code=MYGwhgzhAECyCeBhcVoG8BQ1oAcCuARiAJbDQgD2A5gKoB2BFedAJgBQCUAXNAG4XEW6LNmjAKdCBRABTAHSUqbAC4ALYhA4BuEQF8MI-EVLlqAISatoAXmicbAPjESpshdRXrNO-RnGTlaGIAsDpgGRtoOhkAdzgkFAhOHQwAelTTKgtmIRjiEBBoMBAYsHgYAgjGHOg8tWg1CPEAJ2aZYECIcRwZPxdAtEzsq11I4IhlUPCdRWH2bQN06DkCYKFQoXAAWwIWSFr8wuKpIpZ151b2zu7e-wnoFgplMzWAGWoxkLD5RXpq1hWazY40m3wWd0CwWizXeVEi9msThBUx%2B1D%2BlnmKSWYGaxDUckehFk0BkAA8cCRgHiQPAHu1wG0YGowJDAo8ZDA6E9oG0AGYyZoNCjQAAGag0IqCdGUAroxRpfQCRVx9VsmGwhKIMk8Gh4-EEABpoKSeHQ8DsBdwoubKoL1aI2so8M06MboAAqaAAJh02F0Bowuh0EPQDyYWugo1sOLxqi0QA&fileType=.ts)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
{
/** Whether to skip checking whether `static` methods are correctly bound. */
ignoreStatic?: boolean;
},
];
const defaultOptions: Options = [{ ignoreStatic: false }];
```
### `ignoreStatic`[​](#ignorestatic)
Whether to skip checking whether `static` methods are correctly bound. Default: `false`.
Examples of **correct** code for this rule with `{ ignoreStatic: true }`:
```
class OtherClass {
static log() {
console.log(OtherClass);
}
}
// With `ignoreStatic`, statics are assumed to not rely on a particular scope
const { log } = OtherClass;
log();
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6WJgIwHsOATWgFtE%2BABbc%2B6MAG1w2HImjRu0SABo58rPOyRKAcyYrEAZXwBDfJTJT8cRJuwBfRwF05Lp0A&code=MYGwhgzhAEDyAuALApgJwMLitA3gKGmgnjHgEthoQB7AcwAoBKXAw6YagOwmpGQDoaDBCgxYIjANysAvnjl4A9IugB1MkmgADMrU7VUyAMolywLQBoipijDCHokCAFcAtsgAm0eNWj740IYgAJ7QXI7QAA72Zs7gqEQckch4HNwBOFR00DLQALxwSGiYTtJ4QkySQA&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If your project dynamically changes `this` scopes around in a way TypeScript has difficulties modeling, this rule may not be viable to use.
For example, some functions have an additional parameter for specifying the `this` context, such as `Reflect.apply`, and array methods like `Array.prototype.map`.
This semantic is not easily expressed by TypeScript.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
If you&#x27;re wanting to use `toBeCalled` and similar matches in `jest` tests, you can disable this rule for your test files in favor of [`eslint-plugin-jest`&#x27;s version of this rule](https://github.com/jest-community/eslint-plugin-jest/blob/main/docs/rules/unbound-method.md).
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/unbound-method.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/unbound-method.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/unbound-method.mdx)- [Examples](#examples)- [Options](#options)[`ignoreStatic`](#ignorestatic)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)