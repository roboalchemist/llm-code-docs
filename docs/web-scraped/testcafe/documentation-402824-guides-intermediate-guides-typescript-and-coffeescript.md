# Source: https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript

Title: TypeScript and CoffeeScript | Intermediate Guides | Guides

URL Source: https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript

Markdown Content:
[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#typescript-support)TypeScript Support[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#typescript-support)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Important

TestCafe v2.0 and up includes a TypeScript 4 compiler. TestCafe v1.X includes a TypeScript 3 compiler.

TestCafe allows you to write tests with [TypeScript](https://www.typescriptlang.org/) - a typed superset of JavaScript. TypeScript comes with rich coding assistance, painless scalability, check-as-you-type code verification, and much more.

TestCafe bundles the TypeScript declaration file with the npm package, so you do not need to install it separately.

[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#automatic-compilation-and-manual-compilation)Automatic Compilation and Manual Compilation[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#automatic-compilation-and-manual-compilation)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe automatically compiles TypeScript tests on launch. TestCafe allows you to [customize compiler options](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#customize-compiler-options) and use a custom compiler binary.

If your use case requires total control over TypeScript compilation, you can manually compile your tests _before_ you launch them. View [this GitHub repository](https://github.com/DevExpress/testcafe-example-custom-typescript) for a ready-to-run example.

### [](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#write-tests-with-typescript)Write Tests with TypeScript[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#write-tests-with-typescript)

To start writing tests with TypeScript, install TestCafe into your project directory. For more information, see [Install TestCafe](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#local-installation).

If your text editor supports code completion (for example, VSCode, Sublime Text, WebStorm, etc.) but does not auto-complete TestCafe keywords, it needs to be made aware of the TypeScript declarations that ship with TestCafe. Include the following `import` statement in one of your test files:

```
import { Selector } from 'testcafe';
```

Note

If installed [globally](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#system-wide-installation), TestCafe will successfully compile and run your tests written in TypeScript. However, your IDE will not be able to locate the TestCafe declaration file and provide code completion.

![Image 1: Writing Tests with TypeScript](https://testcafe.io/images/typescript-support.png)

The syntax of TestCafe is identical for both JavaScript and TypeScript.

Whenever TestCafe encounters TypeScript compilation errors, it includes corresponding error messages in the test report.

#### [](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#type-cast-page-elements)Type Cast Page Elements[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#type-cast-page-elements)

TypeScript compilers cannot automatically identify TestCafe objects that refer to DOM elements. Perform manual [type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) in your [client-side code](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions) to ensure correct TypeScript compilation.

Specify the [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) data type to access the DOM element’s generic HTMLElement interface.

A [client function](https://testcafe.io/documentation/402671/reference/test-api/clientfunction) in the example below calls the [Element.scrollIntoView()](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView) method to scroll an element into view.

```
import { ClientFunction, Selector } from 'testcafe';
const scrollIntoView = ClientFunction( (selector: Selector) => {
    const element = selector() as unknown as HTMLElement;
    element.scrollIntoView();
});
fixture`HTMLElement`
    .page('https://example.com');
test('Scroll element into view', async t => {
    const bottomOfPage = Selector('#bottom-div');
    await scrollIntoView(bottomOfPage);
});
```

To avoid compilation errors, pick element-specific data types, such as [HTMLOListElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOListElement).

The example code below calls the [t.eval](https://testcafe.io/documentation/402703/reference/test-api/testcontroller/eval) method to determine if an ordered list is [reversed](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOListElement#instance_properties). The generic [HTMLElement Interface](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement#instance_properties) does not provide access to the element’s `reversed` property. To avoid compilation errors, convert the `list` object to the [HTMLOListElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOListElement#instance_properties) data type.

```
import { Selector } from 'testcafe';
fixture`HTMLOListElement`
    .page('https://example.com');
test('Check that the list is reversed', async t => {
    const olElement = Selector('#ordered-list');
    const isListReversed = await t.eval(() => {
        const list = olElement() as unknown as HTMLOListElement;
        return list.reversed;
    },
    {
        dependencies: { olElement }
    });
    await t
        .expect(isListReversed)
        .ok();
});
```

You can read more about client-side code in the [Obtain Client-Side Info](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions) topic.

### [](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#customize-compiler-options)Customize Compiler Options[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#customize-compiler-options)

TestCafe users can modify [the settings](https://www.typescriptlang.org/docs/handbook/compiler-options.html) of the TypeScript compiler in one of the following three ways:

*   the [--compiler-options](https://testcafe.io/documentation/402639/reference/command-line-interface#--compiler-options-options) command line parameter,

```
testcafe chrome my-tests --compiler-options typescript.options.lib=lib.es5.d.ts,lib.webworker.d.ts;typescript.typesRoot='this value contains spaces'
```
*   the [runner.compilerOptions](https://testcafe.io/documentation/402659/reference/testcafe-api/runner/compileroptions) API method,

```
runner.compilerOptions({
"typescript": {
    customCompilerModulePath: '../node_modules/typescript-v4',
    …
 }});
```
*   the [compilerOptions](https://testcafe.io/documentation/402638/reference/configuration-file#compileroptions) configuration file property.

```
{
"compilerOptions": {
    "typescript": {
       "configPath": "<path to tsconfig.json>",
       "customCompilerModulePath": "path to custom Typescript compiler module",
       "options": {"experimentalDecorators":  "true"}
       }
    }
}
```

See the full list of available options in the [TypeScript Compiler Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html) topic.

Note

You cannot override the following TypeScript options: `module`, `moduleResolution`, `target`.

Compile TypeScript tests [manually](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#automatic-compilation-and-manual-compilation) to control these options.

TestCafe passes the following options to the TypeScript compiler unless you override them:

| Option | Value | Possible to override |
| --- | --- | --- |
| `allowJs` | `true` | yes |
| `emitDecoratorMetadata` | `true` | yes |
| `experimentalDecorators` | `true` | yes |
| `inlineSourceMap` | `true` | yes |
| `jsx` | `2` (ts.JsxEmit.React) | yes |
| `noImplicitAny` | `false` | yes |
| `module` | `1` (ts.ModuleKind.CommonJS) | no |
| `moduleResolution` | `2` (ts.ModuleResolutionKind.Node) | no |
| `pretty` | `true` | yes |
| `suppressOutputPathCheck` | `true` | yes |
| `skipLibCheck` | `true` | yes |
| `target` | `3` (ts.ScriptTarget.ES2016) | no |

Note

TestCafe enables the `skipLibCheck` option for performance reasons. If you need to check types in your declaration files, set `skipLibCheck` to `false`.

[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#coffeescript-support)CoffeeScript Support[](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#coffeescript-support)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe allows you to write tests with [CoffeeScript](https://coffeescript.org/).

**Example**

*   [CoffeeScript](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#tabpanel_jvuTiGcKiO_tabid-coffee)

```
import { Selector } from 'testcafe'

fixture 'CoffeeScript Example'
    .page 'https://devexpress.github.io/testcafe/example/'

nameInput = Selector '#developer-name'

test 'Test', (t) =>
    await t
        .typeText(nameInput, 'Peter')
        .typeText(nameInput, 'Paker', { replace: true })
        .typeText(nameInput, 'r', { caretPos: 2 })
        .expect(nameInput.value).eql 'Parker';
```

You do not need to manually compile CoffeeScript tests. TestCafe does this automatically on launch.
