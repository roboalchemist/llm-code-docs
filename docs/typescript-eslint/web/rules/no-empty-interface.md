# Source: https://typescript-eslint.io/rules/no-empty-interface

On this page# no-empty-interface
Disallow the declaration of empty interfaces.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
DeprecatedThis rule has been deprecated in favour of the more comprehensive [`@typescript-eslint/no-empty-object-type`](/rules/no-empty-object-type) rule.
An empty interface in TypeScript does very little: any non-nullable value is assignable to `{}`.
Using an empty interface is often a sign of programmer error, such as misunderstanding the concept of `{}` or forgetting to fill in fields.
This rule aims to ensure that only meaningful interfaces are declared in the code.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-empty-interface": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-empty-interface": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge3oFsbDbm%2BRNABmAQzKJ0UYdA7RI4MAF8QyoA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
// an empty interface
interface Foo {}
// an interface with only one supertype (Bar === Foo)
interface Bar extends Foo {}
// an interface with an empty list of supertypes
interface Baz {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge3oFsbDbm%2BRNABmAQzKJ0UYdA7RI4MAF8QyoA&code=PTAEEMDtQUwWwA4BcCeoCWkkwE4DNwBjGAKE23yJlADEB7O0AbwF8SSQJpzcDjQA7uiQALUHUgAbNBOoBnAK4JcqZaAAUAIXA5QAXgO0GASjJZeVUNt0wAHtkgATOUcat2nKBnOV%2BQ0VywiKigkuhySOJ4oIrKOKowcmYUfNTaAF7MLEA&fileType=.ts)```
// an interface with any number of members
interface Foo {
name: string;
}
// same as above
interface Bar {
age: number;
}
// an interface with more than one supertype
// in this case the interface can be used as a replacement of an intersection type.
interface Baz extends Foo, Bar {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge3oFsbDbm%2BRNABmAQzKJ0UYdA7RI4MAF8QyoA&code=PTAEEMDtQS0gXApgJwGbgMaNAdxvACwkgE9RIBXAWwCMVQB7VUKxWlAZwCg4k1NsAMQYNQAby6hy4VgC5QHeMjgBzANxcAvly4gFM7OA4QaDAG6IeCFOiygAQuGTjJEFYnmV2yDdt1goWGt%2BOzxCFgZkbEJAhkhsDgoABxR4EhT-INBCGGMMI2iCbF4bAVB86DpQCg5EABMIY3BQKKSAGwFWBEZmQJLkWox4GDjs9MQAOis%2BW2xHAC9QRAAPJEg642EGABoHJ3FNIA&fileType=.ts)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
{
/** Whether to allow empty interfaces that extend a single other interface. */
allowSingleExtends?: boolean;
},
];
const defaultOptions: Options = [{ allowSingleExtends: false }];
```
### `allowSingleExtends`[​](#allowsingleextends)
Whether to allow empty interfaces that extend a single other interface. Default: `false`.
`allowSingleExtends: true` will silence warnings about extending a single interface without adding additional members.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t care about having empty/meaningless interfaces, then you will not need this rule.
## Related To[​](#related-to)
- [`no-empty-object-type`](/rules/no-empty-object-type)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-empty-interface.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-empty-interface.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-empty-interface.mdx)- [Examples](#examples)- [Options](#options)[`allowSingleExtends`](#allowsingleextends)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)