# Source: https://typescript-eslint.io/rules/prefer-return-this-type

On this page# prefer-return-this-type
Enforce that `this` is used when only `this` type is returned.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
[Method chaining](https://en.wikipedia.org/wiki/Method_chaining) is a common pattern in OOP languages and TypeScript provides a special [polymorphic `this` type](https://www.typescriptlang.org/docs/handbook/2/classes.html#this-types) to facilitate it.
Class methods that explicitly declare a return type of the class name instead of `this` make it harder for extending classes to call that method: the returned object will be typed as the base class, not the derived class.
This rule reports when a class method declares a return type of that class name instead of `this`.
```
class Animal {
eat(): Animal {
//   ~~~~~~
// Either removing this type annotation or replacing
// it with `this` would remove the type error below.
console.log("I&#x27;m moving!");
return this;
}
}
class Cat extends Animal {
meow(): Cat {
console.log(&#x27;Meow~&#x27;);
return this;
}
}
const cat = new Cat();
cat.eat().meow();
//        ~~~~
// Error: Property &#x27;meow&#x27; does not exist on type &#x27;Animal&#x27;.
// because `eat` returns `Animal` and not all animals meow.
```
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-return-this-type": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-return-this-type": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls-yxoTWvgAWlZKJKJ0UXtAD20SODABfEOqA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
class Foo {
f1(): Foo {
return this;
}
f2 = (): Foo => {
return this;
};
f3(): Foo | undefined {
return Math.random() > 0.5 ? this : undefined;
}
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls-yxoTWvgAWlZKJKJ0UXtAD20SODABfEOqA&code=MYGwhgzhAEBiD29oG8BQ1oDMCMAKAlAFxyIrobQBOApgC4CulAdtLQBYCWEA3OQL7lMAJmgBeaAWIIkogHxkKVOoxbsuvDHw1YAzJJJIAPtHpMAJtUwcm1Mwoo0GzaAFkw7AHSUw5%2BAFsCaHkABg8AVmgAflZOGGJTCysbM20BPiA&fileType=.ts)```
class Foo {
f1(): this {
return this;
}
f2() {
return this;
}
f3 = (): this => {
return this;
};
f4 = () => {
return this;
};
}
class Base {}
class Derived extends Base {
f(): Base {
return this;
}
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls-yxoTWvgAWlZKJKJ0UXtAD20SODABfEOqA&code=MYGwhgzhAEBiD29oG8BQ1oDMCMAKAlAFzQAuAFgJYxoYYBOApiQK50B2plEA3OtAL59MAJgIo%2B9Jqw7kqvDIIyYAzNAC80AsVkw1APnG1ojFu05y%2B-eVgAs6zfnUGatE9PM9LvQalCQYAEKQDCiCflDQACIMdBQAbgwAJtAMAB4kDGyJgcGGWFrQQRAhLpKmMlzWgvxAA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t use method chaining or explicit return values, you can safely turn this rule off.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-return-this-type.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-return-this-type.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-return-this-type.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)