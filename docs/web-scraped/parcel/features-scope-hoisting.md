# Source: https://parceljs.org/features/scope-hoisting/

Title: Scope hoisting

URL Source: https://parceljs.org/features/scope-hoisting/

Markdown Content:
Historically, JavaScript bundlers have worked by wrapping each module in a function, which is called when the module is imported. This ensures that each module has a separate isolated scope and side effects run at the expected time, and enables development features like [hot module replacement](https://parceljs.org/features/development/#hot-reloading). However, all of these separate functions have a cost, both in terms of download size and [runtime performance](https://nolanlawson.com/2016/08/15/the-cost-of-small-modules/).

In production builds, Parcel concatenates modules into a single scope when possible, rather than wrapping each module in a separate function. This is called **“scope hoisting”.** This helps make minification more effective, and also improves runtime performance by making references between modules static rather than dynamic object lookups.

Parcel also statically analyzes the imports and exports of each module, and removes everything that isn't used. This is called **"tree shaking"** or **"dead code elimination".** Tree shaking is supported for both static and [dynamic import](https://parceljs.org/features/code-splitting/#tree-shaking), [CommonJS](https://parceljs.org/languages/javascript/#commonjs) and [ES modules](https://parceljs.org/languages/javascript/#es-modules), and even across languages with [CSS modules](https://parceljs.org/languages/css/#tree-shaking).

How scope hoisting works
------------------------

[#](https://parceljs.org/features/scope-hoisting/#how-scope-hoisting-works)
Parcel’s implementation of scope hoisting works by analyzing each module independently and in parallel, and at the end concatenating them together. In order to make concatenation into a single scope safe, the top-level variables of each module are renamed to ensure they are unique. In addition, imported variables are renamed to match the exported variable names from the resolved module. Finally, any unused exports are removed.

_index.js:_

`import {add} from './math';console.log(add(2, 3));`

_math.js:_

`export function add(a, b) {  return a + b;}export function square(a) {  return a * a;}`

Compiles to something like:

`function $fa6943ce8a6b29$add(a, b) {  return a + b;}console.log($fa6943ce8a6b29$add(2, 3));`
As you can see, the `add` function has been renamed, and the reference has been updated to match. The `square` function has been removed because it is unused.

This results in much smaller and faster output than if each module had been wrapped in a function. Not only are there no extra functions, but there are also no `exports` objects, and the reference to the `add` function is static rather than a property lookup.

Avoiding bail outs
------------------

[#](https://parceljs.org/features/scope-hoisting/#avoiding-bail-outs)
Parcel can statically analyze many patterns including ES module `import` and `export` statements, CommonJS `require()` and `exports` assignments, dynamic `import()` destructuring and property accesses, and more. However, when it comes across code that cannot be statically analyzed ahead of time, Parcel may have to "bail out" and wrap the module in a function in order to preserve side effects or allow exports to be resolved at runtime.

To determine why tree shaking is not occurring as expected, run Parcel with the `--log-level verbose` CLI option. This will print diagnostics for each bailout that occurs, including a code frame showing what caused it.

`parcel build src/app.html --log-level verbose`
### Dynamic member accesses

[#](https://parceljs.org/features/scope-hoisting/#dynamic-member-accesses)
Parcel can statically resolve member accesses that are known at build time, but when a dynamic property access is used, all exports of the module must be included in the build, and Parcel must create an exports object so that the value can be resolved at runtime.

`import * as math from './math';// ✅ Static property accessconsole.log(math.add(2, 3));// 🚫 Dynamic property accessconsole.log(math[op](2, 3));`
In addition, Parcel does not track re-assignments of a namespace object to another variable. Any usage of an import namespace other than a static property access will cause all exports to be included.

`import * as math from './math';// 🚫 Reassignment of import namespacelet utils = math;console.log(utils.add(2, 3));// 🚫 Unknown usage of import namespacedoSomething(math);`
### Dynamic imports

[#](https://parceljs.org/features/scope-hoisting/#dynamic-imports)
Parcel supports tree shaking dynamic imports with static property accesses or destructuring. This is supported with both `await` and Promise `then` syntax. However, if the Promise returned from `import()` is accessed in any other way, Parcel must preserve all exports of the resolved module.

**Note:** For the `await` cases, unused exports can unfortunately only be removed when `await` is not transpilied away (i.e. with a modern browserslist config).

`// ✅ Destructuring awaitlet {add} = await import('./math');// ✅ Static member access of awaitlet math = await import('./math');console.log(math.add(2, 3));// ✅ Destructuring Promise#thenimport('./math').then(({add}) => console.log(add(2, 3)));// ✅ Static member access of Promise#thenimport('./math').then(math => console.log(math.add(2, 3)));// 🚫 Dynamic property access of awaitlet math = await import('./math');console.log(math[op](2, 3));// 🚫 Dynamic property access of Promise#thenimport('./math').then(math => console.log(math[op](2, 3)));// 🚫 Unknown use of returned PromisedoSomething(import('./math'));// 🚫 Unknown argument passed to Promise#thenimport('./math').then(doSomething);`
### CommonJS

[#](https://parceljs.org/features/scope-hoisting/#commonjs)
In addition to ES modules, Parcel can also analyze many CommonJS modules. Parcel supports static assignments to `exports`, `module.exports`, and `this` within a CommonJS module. This means the property name must be known statically at build time (i.e. not a variable).

When a non-static pattern is seen, Parcel creates an `exports` object that all importing modules access at runtime. All exports must be included in the final build and no tree shaking can be performed.

`// ✅ Static exports assignmentsexports.foo = 2;module.exports.foo = 2;this.foo = 2;// ✅ module.exports assignmentmodule.exports = 2;// 🚫 Dynamic exports assignmentsexports[someVar] = 2;module.exports[someVar] = 2;this[someVar] = 2;// 🚫 Exports re-assignmentlet e = exports;e.foo = 2;// 🚫 Module re-assignmentlet m = module;m.exports.foo = 2;// 🚫 Unknown exports usagedoSomething(exports);doSomething(this);// 🚫 Unknown module usagedoSomething(module);`
On the importing side, Parcel supports static property accesses and destructuring of `require` calls. When a non-static access is seen, all exports of the resolved module must be included and no tree shaking can be performed.

`// ✅ Static property accessconst math = require('./math');console.log(math.add(2, 3));// ✅ Static destructuringconst {add} = require('./math');// ✅ Static property assignmentconst add = require('./math').add;// 🚫 Non-static property accessconst math = require('./math');console.log(math[op](2, 3));// 🚫 Inline requiredoSomething(require('./math'));console.log(require('./math').add(2, 3));`
### Avoid `eval`

[#](https://parceljs.org/features/scope-hoisting/#avoid-eval)
The `eval` function executes arbitrary JavaScript code in a string within the current scope. This means Parcel cannot rename any of the variables within the scope in case they are accessed by `eval`. In this case, Parcel must wrap the module in a function and avoid minifying the variable names.

`let x = 2;// 🚫 Eval causes wrapping and disables minificationeval('x = 4');`
If you need to run JavaScript code from a string, you may be able to use the [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function) constructor instead.

### Avoid top-level `return`

[#](https://parceljs.org/features/scope-hoisting/#avoid-top-level-return)
CommonJS allows `return` statements at the top-level of a module (i.e. outside a function). When this is seen, Parcel must wrap the module in a function so that execution stops only that module rather than the whole bundle. In addition, tree shaking is disabled because exports may not be known statically (e.g. if the return is conditional).

`exports.foo = 2;if (someCondition) {  // 🚫 Top-level return causes wrapping and disables tree shaking  return;}exports.bar = 3;`
### Avoid `module` and `exports` re-assignment

[#](https://parceljs.org/features/scope-hoisting/#avoid-module-and-exports-re-assignment)
When the CommonJS `module` or `exports` variables are re-assigned, Parcel cannot statically analyze the exports of the module. In this case, the module must be wrapped in a function and tree shaking is disabled.

`exports.foo = 2;// 🚫 Exports reassignment causes wrapping and disables tree shakingexports = {};exports.foo = 5;`
### Avoid conditional `require()`

[#](https://parceljs.org/features/scope-hoisting/#avoid-conditional-require())
Unlike ES module `import` statements which are only allowed at the top-level of a module, `require` is a function that may be called from anywhere. However, when `require` is called from within a conditional or another control flow statement, Parcel must wrap the resolved module in a function so that side effects are executed at the right time. This also applies recursively to any dependencies of the resolved module.

`// 🚫 Conditional requires cause recursive wrappingif (someCondition) {  require('./something');}`
Side effects
------------

[#](https://parceljs.org/features/scope-hoisting/#side-effects)
Many modules only contain declarations, like functions or classes, but some may also include **side effects**. For example, a module might insert something into the DOM, log something to the console, assign to a global variable (i.e. a polyfill), or initialize a singleton. These side effects must always be retained for the program to work correctly, even if the exports of the module are unused.

By default, Parcel includes all modules, which ensures side effects are always run. However, the `sideEffects` field in `package.json` can be used to give Parcel and other tools a hint about whether your files include side effects. This makes the most sense for libraries to include in their package.json files.

The `sideEffects` field supports the following values:

*   `false` – All files in this package have no side effects.
*   `string` – A glob matching files that includes side effects.
*   `Array<string>` – An array of globs matching files that include side effects.

When a file is marked as side effect free, Parcel is able to skip the entire file when concatenating the bundle if it does not have any used exports. This can reduce bundle sizes significantly, especially if the module calls helper functions during its initialization.

_app.js:_

`import {add} from 'math';console.log(add(2, 3));`

_node\_modules/math/package.json:_

`{  "name": "math"  "sideEffects": false}`

_node\_modules/math/index.js:_

`export {add} from './add.js';export {multiply} from './multiply.js';let loaded = Date.now();export function elapsed() {  return Date.now() - loaded;}`

In this case, only the `add` function from the `math` library is used. `multiply` and `elapsed` are unused. Normally, the `loaded` variable would still be needed because it includes a side effect that runs during the module's initialization. However, because the `package.json` includes the `sideEffects` field, the `index.js` module can be entirely skipped.

In addition to size benefits, using the `sideEffects` field also has build performance benefits. In the above example, because Parcel knows `multiply.js` has no side effects, and none of its exports are used, it is never even compiled at all. However, if `export *` had been used instead, this would not be true because Parcel would not know what exports are available.

Another benefit of `sideEffects` is that it also applies to bundling. If a module imports a CSS file or contains a dynamic `import()`, the bundle will not be created if the module is unused.

### PURE annotations

[#](https://parceljs.org/features/scope-hoisting/#pure-annotations)
You can also annotate individual function calls with a `/*#__PURE__*/` comment, which tells the minifier that it's safe to remove that function call when the result is unused.

`export const radius = 23;export const circumference = /*#__PURE__*/ calculateCircumference(radius);`
In this example, if the `circumference` export is unused, then the `calculateCircumference` function will also not be included. Without the PURE annotation, `calculateCircumference` would still be called in case it had side effects.
