# Source: https://ast-grep.github.io/catalog/typescript.md

---
url: /catalog/typescript.md
---
# TypeScript

This page curates a list of example ast-grep rules to check and to rewrite TypeScript applications.
Check out the [Repository of ESLint rules](https://github.com/ast-grep/eslint/) recreated with ast-grep.

:::danger TypeScript and TSX are different.
TypeScript is a typed JavaScript extension and TSX is a further extension that allows JSX elements.
They need different parsers because of [conflicting syntax](https://www.typescriptlang.org/docs/handbook/jsx.html#the-as-operator).

However, you can use the [`languageGlobs`](/reference/sgconfig.html#languageglobs) option to force ast-grep to use parse `.ts` files as TSX.
:::

## Find Import File without Extension

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6ImNvbnNvbGUubG9nKCRNQVRDSCkiLCJyZXdyaXRlIjoibG9nZ2VyLmxvZygkTUFUQ0gpIiwiY29uZmlnIjoibGFuZ3VhZ2U6IFwianNcIlxucnVsZTpcbiAgcmVnZXg6IFwiL1teLl0rW14vXSRcIiAgXG4gIGtpbmQ6IHN0cmluZ19mcmFnbWVudFxuICBhbnk6XG4gICAgLSBpbnNpZGU6XG4gICAgICAgIHN0b3BCeTogZW5kXG4gICAgICAgIGtpbmQ6IGltcG9ydF9zdGF0ZW1lbnRcbiAgICAtIGluc2lkZTpcbiAgICAgICAgc3RvcEJ5OiBlbmRcbiAgICAgICAga2luZDogY2FsbF9leHByZXNzaW9uXG4gICAgICAgIGhhczpcbiAgICAgICAgICBmaWVsZDogZnVuY3Rpb25cbiAgICAgICAgICByZWdleDogXCJeaW1wb3J0JFwiXG4iLCJzb3VyY2UiOiJpbXBvcnQgYSwge2IsIGMsIGR9IGZyb20gXCIuL2ZpbGVcIjtcbmltcG9ydCBlIGZyb20gXCIuL290aGVyX2ZpbGUuanNcIjtcbmltcG9ydCBcIi4vZm9sZGVyL1wiO1xuaW1wb3J0IHt4fSBmcm9tIFwicGFja2FnZVwiO1xuaW1wb3J0IHt5fSBmcm9tIFwicGFja2FnZS93aXRoL3BhdGhcIjtcblxuaW1wb3J0KFwiLi9keW5hbWljMVwiKTtcbmltcG9ydChcIi4vZHluYW1pYzIuanNcIik7XG5cbm15X2Z1bmMoXCIuL3VucmVsYXRlZF9wYXRoX3N0cmluZ1wiKVxuXG4ifQ==)

### Description

In ECMAScript modules (ESM), the module specifier must include the file extension, such as `.js` or `.mjs`, when importing local or absolute modules. This is because ESM does not perform any automatic file extension resolution, unlike CommonJS modules tools such as Webpack or Babel. This behavior matches how import behaves in browser environments, and is specified by the [ESM module spec](https://stackoverflow.com/questions/66375075/node-14-ecmascript-modules-import-modules-without-file-extensions).

The rule finds all imports (static and dynamic) for files without a file extension.

### YAML

```yaml
id: find-import-file
language: js
rule:
  regex: "/[^.]+[^/]$"
  kind: string_fragment
  any:
    - inside:
        stopBy: end
        kind: import_statement
    - inside:
        stopBy: end
        kind: call_expression
        has:
          field: function
          regex: "^import$"
```

### Example

```ts {1,5,7}
import a, {b, c, d} from "./file";
import e from "./other_file.js";
import "./folder/";
import {x} from "package";
import {y} from "package/with/path";

import("./dynamic1");
import("./dynamic2.js");

my_func("./unrelated_path_string")
```

### Contributed by

[DasSurma](https://twitter.com/DasSurma) in [this tweet](https://x.com/DasSurma/status/1706213303331029277).

## Migrate XState to v5 from v4&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6ImlmICgkQSkgeyAkJCRCIH0iLCJyZXdyaXRlIjoiaWYgKCEoJEEpKSB7XG4gICAgcmV0dXJuO1xufVxuJCQkQiIsImNvbmZpZyI6InV0aWxzOlxuICBGUk9NX1hTVEFURTogeyBraW5kOiBpbXBvcnRfc3RhdGVtZW50LCBoYXM6IHsga2luZDogc3RyaW5nLCByZWdleDogeHN0YXRlIH0gfVxuICBYU1RBVEVfRVhQT1JUOlxuICAgIGtpbmQ6IGlkZW50aWZpZXJcbiAgICBpbnNpZGU6IHsgaGFzOiB7IG1hdGNoZXM6IEZST01fWFNUQVRFIH0sIHN0b3BCeTogZW5kIH1cbnJ1bGU6IHsgcmVnZXg6IF5NYWNoaW5lfGludGVycHJldCQsIHBhdHRlcm46ICRJTVBPUlQsIG1hdGNoZXM6IFhTVEFURV9FWFBPUlQgfVxudHJhbnNmb3JtOlxuICBTVEVQMTogXG4gICAgcmVwbGFjZToge2J5OiBjcmVhdGUkMSwgcmVwbGFjZTogKE1hY2hpbmUpLCBzb3VyY2U6ICRJTVBPUlQgfVxuICBGSU5BTDpcbiAgICByZXBsYWNlOiB7IGJ5OiBjcmVhdGVBY3RvciwgcmVwbGFjZTogaW50ZXJwcmV0LCBzb3VyY2U6ICRTVEVQMSB9XG5maXg6ICRGSU5BTFxuLS0tIFxucnVsZTogeyBwYXR0ZXJuOiAkTUFDSElORS53aXRoQ29uZmlnIH1cbmZpeDogJE1BQ0hJTkUucHJvdmlkZVxuLS0tXG5ydWxlOlxuICBraW5kOiBwcm9wZXJ0eV9pZGVudGlmaWVyXG4gIHJlZ2V4OiBec2VydmljZXMkXG4gIGluc2lkZTogeyBwYXR0ZXJuOiAgJE0ud2l0aENvbmZpZygkJCRBUkdTKSwgc3RvcEJ5OiBlbmQgfVxuZml4OiBhY3RvcnMiLCJzb3VyY2UiOiJpbXBvcnQgeyBNYWNoaW5lLCBpbnRlcnByZXQgfSBmcm9tICd4c3RhdGUnO1xuXG5jb25zdCBtYWNoaW5lID0gTWFjaGluZSh7IC8qLi4uKi99KTtcblxuY29uc3Qgc3BlY2lmaWNNYWNoaW5lID0gbWFjaGluZS53aXRoQ29uZmlnKHtcbiAgYWN0aW9uczogeyAvKiAuLi4gKi8gfSxcbiAgZ3VhcmRzOiB7IC8qIC4uLiAqLyB9LFxuICBzZXJ2aWNlczogeyAvKiAuLi4gKi8gfSxcbn0pO1xuXG5jb25zdCBhY3RvciA9IGludGVycHJldChzcGVjaWZpY01hY2hpbmUsIHtcbi8qIGFjdG9yIG9wdGlvbnMgKi9cbn0pOyJ9)

### Description

[XState](https://xstate.js.org/) is a state management/orchestration library based on state machines, statecharts, and the actor model. It allows you to model complex logic in event-driven ways, and orchestrate the behavior of many actors communicating with each other.

XState's v5 version introduced some breaking changes and new features compared to v4.
While the migration should be a straightforward process, it is a tedious process and requires knowledge of the differences between v4 and v5.

ast-grep provides a way to automate the process and a way to encode valuable knowledge to executable rules.

The following example picks up some migration items and demonstrates the power of ast-grep's rule system.

### YAML

The rules below correspond to XState v5's [`createMachine`](https://stately.ai/docs/migration#use-createmachine-not-machine), [`createActor`](https://stately.ai/docs/migration#use-createactor-not-interpret), and [`machine.provide`](https://stately.ai/docs/migration#use-machineprovide-not-machinewithconfig).

The example shows how ast-grep can use various features like [utility rule](/guide/rule-config/utility-rule.html), [transformation](/reference/yaml/transformation.html) and [multiple rule in single file](/reference/playground.html#test-multiple-rules) to automate the migration. Each rule has a clear and descriptive `id` field that explains its purpose.

For more information, you can use [Codemod AI](https://app.codemod.com/studio?ai_thread_id=new) to provide more detailed explanation for each rule.

```yaml
id: migrate-import-name
utils:
  FROM_XS: {kind: import_statement, has: {kind: string, regex: xstate}}
  XS_EXPORT:
    kind: identifier
    inside: { has: { matches: FROM_XS }, stopBy: end }
rule: { regex: ^Machine|interpret$, pattern: $IMPT, matches: XS_EXPORT }
transform:
  STEP1:
    replace: {by: create$1, replace: (Machine), source: $IMPT }
  FINAL:
    replace: { by: createActor, replace: interpret, source: $STEP1 }
fix: $FINAL

---

id: migrate-to-provide
rule: { pattern: $MACHINE.withConfig }
fix: $MACHINE.provide

---

id: migrate-to-actors
rule:
  kind: property_identifier
  regex: ^services$
  inside: { pattern:  $M.withConfig($$$ARGS), stopBy: end }
fix: actors
```

### Example

```js {1,3,5,8,11}
import { Machine, interpret } from 'xstate';

const machine = Machine({ /*...*/});

const specificMachine = machine.withConfig({
  actions: { /* ... */ },
  guards: { /* ... */ },
  services: { /* ... */ },
});

const actor = interpret(specificMachine, {
  /* actor options */
});
```

### Diff

```js
import { Machine, interpret } from 'xstate'; // [!code --]
import { createMachine, createActor } from 'xstate'; // [!code ++]

const machine = Machine({ /*...*/}); // [!code --]
const machine = createMachine({ /*...*/}); // [!code ++]

const specificMachine = machine.withConfig({ // [!code --]
const specificMachine = machine.provide({ // [!code ++]
  actions: { /* ... */ },
  guards: { /* ... */ },
  services: { /* ... */ }, // [!code --]
  actors: { /* ... */ }, // [!code ++]
});

const actor = interpret(specificMachine, { // [!code --]
const actor = createActor(specificMachine, { // [!code ++]
  /* actor options */
});
```

### Contributed by

Inspired by [XState's blog](https://stately.ai/blog/2023-12-01-xstate-v5).

## No `await` in `Promise.all` array&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6ImNvbnNvbGUubG9nKCRNQVRDSCkiLCJyZXdyaXRlIjoibG9nZ2VyLmxvZygkTUFUQ0gpIiwiY29uZmlnIjoiaWQ6IG5vLWF3YWl0LWluLXByb21pc2UtYWxsXG5zZXZlcml0eTogZXJyb3Jcbmxhbmd1YWdlOiBKYXZhU2NyaXB0XG5tZXNzYWdlOiBObyBhd2FpdCBpbiBQcm9taXNlLmFsbFxucnVsZTpcbiAgcGF0dGVybjogYXdhaXQgJEFcbiAgaW5zaWRlOlxuICAgIHBhdHRlcm46IFByb21pc2UuYWxsKCRfKVxuICAgIHN0b3BCeTpcbiAgICAgIG5vdDogeyBhbnk6IFt7a2luZDogYXJyYXl9LCB7a2luZDogYXJndW1lbnRzfV0gfVxuZml4OiAkQSIsInNvdXJjZSI6ImNvbnN0IFtmb28sIGJhcl0gPSBhd2FpdCBQcm9taXNlLmFsbChbXG4gIGF3YWl0IGdldEZvbygpLFxuICBnZXRCYXIoKSxcbiAgKGFzeW5jICgpID0+IHsgYXdhaXQgZ2V0QmF6KCl9KSgpLFxuXSkifQ==)

### Description

Using `await` inside an inline `Promise.all` array is usually a mistake, as it defeats the purpose of running the promises in parallel. Instead, the promises should be created without `await` and passed to `Promise.all`, which can then be awaited.

### YAML

```yaml
id: no-await-in-promise-all
language: typescript
rule:
  pattern: await $A
  inside:
    pattern: Promise.all($_)
    stopBy:
      not: { any: [{kind: array}, {kind: arguments}] }
fix: $A
```

### Example

```ts {2}
const [foo, bar] = await Promise.all([
  await getFoo(),
  getBar(),
  (async () => { await getBaz()})(),
])
```

### Diff

```ts
const [foo, bar] = await Promise.all([
  await getFoo(), // [!code --]
  getFoo(), // [!code ++]
  getBar(),
  (async () => { await getBaz()})(),
])
```

### Contributed by

Inspired by [Alvar Lagerlöf](https://twitter.com/alvarlagerlof)

## No `console` except in `catch` block&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6ImlmICRBLmhhc19mZWF0dXJlP1xuICAgICQkJEJcbmVsc2UgXG4gICAgJCQkQyBcbmVuZCAiLCJyZXdyaXRlIjoiJCQkQiIsImNvbmZpZyI6InJ1bGU6XG4gIGFueTpcbiAgICAtIHBhdHRlcm46IGNvbnNvbGUuZXJyb3IoJCQkKVxuICAgICAgbm90OlxuICAgICAgICBpbnNpZGU6XG4gICAgICAgICAga2luZDogY2F0Y2hfY2xhdXNlXG4gICAgICAgICAgc3RvcEJ5OiBlbmRcbiAgICAtIHBhdHRlcm46IGNvbnNvbGUuJE1FVEhPRCgkJCQpXG5jb25zdHJhaW50czpcbiAgTUVUSE9EOlxuICAgIHJlZ2V4OiAnbG9nfGRlYnVnfHdhcm4nXG5maXg6ICcnIiwic291cmNlIjoiY29uc29sZS5kZWJ1ZygnJylcbnRyeSB7XG4gICAgY29uc29sZS5sb2coJ2hlbGxvJylcbn0gY2F0Y2ggKGUpIHtcbiAgICBjb25zb2xlLmVycm9yKGUpXG59In0=)

### Description

Using `console` methods is usually for debugging purposes and therefore not suitable to ship to the client.
`console` can expose sensitive information, clutter the output, or affect the performance.

The only exception is using `console.error` to log errors in the catch block, which can be useful for debugging production.

### YAML

```yaml
id: no-console-except-error
language: typescript
rule:
  any:
    - pattern: console.error($$$)
      not:
        inside:
          kind: catch_clause
          stopBy: end
    - pattern: console.$METHOD($$$)
constraints:
  METHOD:
    regex: 'log|debug|warn'
```

### Example

```ts {1,3}
console.debug('')
try {
    console.log('hello')
} catch (e) {
    console.error(e) // OK
}
```

### Diff

```ts
console.debug('') // [!code --]
try {
    console.log('hello') // [!code --]
} catch (e) {
    console.error(e) // OK
}
```

### Contributed by

Inspired by [Jerry Mouse](https://github.com/WWK563388548)

## Find Import Usage

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InR5cGVzY3JpcHQiLCJxdWVyeSI6IiIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoicmVsYXhlZCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoicnVsZTpcbiAgIyB0aGUgdXNhZ2VcbiAga2luZDogaWRlbnRpZmllclxuICBwYXR0ZXJuOiAkTU9EXG4gICMgaXRzIHJlbGF0aW9uc2hpcCB0byB0aGUgcm9vdFxuICBpbnNpZGU6XG4gICAgc3RvcEJ5OiBlbmRcbiAgICBraW5kOiBwcm9ncmFtXG4gICAgIyBhbmQgYmFjayBkb3duIHRvIHRoZSBpbXBvcnQgc3RhdGVtZW50XG4gICAgaGFzOlxuICAgICAga2luZDogaW1wb3J0X3N0YXRlbWVudFxuICAgICAgIyBhbmQgZGVlcGVyIGludG8gdGhlIGltcG9ydCBzdGF0ZW1lbnQgbG9va2luZyBmb3IgdGhlIG1hdGNoaW5nIGlkZW50aWZpZXJcbiAgICAgIGhhczpcbiAgICAgICAgc3RvcEJ5OiBlbmRcbiAgICAgICAga2luZDogaW1wb3J0X3NwZWNpZmllclxuICAgICAgICBwYXR0ZXJuOiAkTU9EICMgc2FtZSBwYXR0ZXJuIGFzIHRoZSB1c2FnZSBpcyBlbmZvcmNlZCBoZXJlIiwic291cmNlIjoiaW1wb3J0IHsgTW9uZ29DbGllbnQgfSBmcm9tICdtb25nb2RiJztcbmNvbnN0IHVybCA9ICdtb25nb2RiOi8vbG9jYWxob3N0OjI3MDE3JztcbmFzeW5jIGZ1bmN0aW9uIHJ1bigpIHtcbiAgY29uc3QgY2xpZW50ID0gbmV3IE1vbmdvQ2xpZW50KHVybCk7XG59XG4ifQ==)

### Description

It is common to find the usage of an imported module in a codebase. This rule helps you to find the usage of an imported module in your codebase.
The idea of this rule can be broken into several parts:

* Find the use of an identifier `$MOD`
* To find the import, we first need to find the root file of which `$MOD` is  `inside`
* The `program` file `has` an `import` statement
* The `import` statement `has` the identifier `$MOD`

### YAML

```yaml
id: find-import-usage
language: typescript
rule:
  kind: identifier # ast-grep requires a kind
  pattern: $MOD   # the identifier to find
  inside: # find the root
    stopBy: end
    kind: program
    has: # and has the import statement
      kind: import_statement
      has: # look for the matching identifier
        stopBy: end
        kind: import_specifier
        pattern: $MOD # same pattern as the usage is enforced here
```

### Example

```ts {4}
import { MongoClient } from 'mongodb';
const url = 'mongodb://localhost:27017';
async function run() {
  const client = new MongoClient(url);
}
```

### Contributed by

[Steven Love](https://github.com/StevenLove)

## Switch Chai from `should` style to `expect`&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InJ1c3QiLCJxdWVyeSI6IiIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoicmVsYXhlZCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoiaWQ6IHNob3VsZF90b19leHBlY3RfaW5zdGFuY2VvZlxubGFuZ3VhZ2U6IFR5cGVTY3JpcHRcbnJ1bGU6XG4gIGFueTpcbiAgLSBwYXR0ZXJuOiAkTkFNRS5zaG91bGQuYmUuYW4uaW5zdGFuY2VvZigkVFlQRSlcbiAgLSBwYXR0ZXJuOiAkTkFNRS5zaG91bGQuYmUuYW4uaW5zdGFuY2VPZigkVFlQRSlcbmZpeDogfC1cbiAgZXhwZWN0KCROQU1FKS5pbnN0YW5jZU9mKCRUWVBFKVxuLS0tXG5pZDogc2hvdWxkX3RvX2V4cGVjdF9nZW5lcmljU2hvdWxkQmVcbmxhbmd1YWdlOiBUeXBlU2NyaXB0XG5ydWxlOlxuICBwYXR0ZXJuOiAkTkFNRS5zaG91bGQuYmUuJFBST1BcbmZpeDogfC1cbiAgZXhwZWN0KCROQU1FKS50by5iZS4kUFJPUFxuIiwic291cmNlIjoiaXQoJ3Nob3VsZCBwcm9kdWNlIGFuIGluc3RhbmNlIG9mIGNob2tpZGFyLkZTV2F0Y2hlcicsICgpID0+IHtcbiAgd2F0Y2hlci5zaG91bGQuYmUuYW4uaW5zdGFuY2VvZihjaG9raWRhci5GU1dhdGNoZXIpO1xufSk7XG5pdCgnc2hvdWxkIGV4cG9zZSBwdWJsaWMgQVBJIG1ldGhvZHMnLCAoKSA9PiB7XG4gIHdhdGNoZXIub24uc2hvdWxkLmJlLmEoJ2Z1bmN0aW9uJyk7XG4gIHdhdGNoZXIuZW1pdC5zaG91bGQuYmUuYSgnZnVuY3Rpb24nKTtcbiAgd2F0Y2hlci5hZGQuc2hvdWxkLmJlLmEoJ2Z1bmN0aW9uJyk7XG4gIHdhdGNoZXIuY2xvc2Uuc2hvdWxkLmJlLmEoJ2Z1bmN0aW9uJyk7XG4gIHdhdGNoZXIuZ2V0V2F0Y2hlZC5zaG91bGQuYmUuYSgnZnVuY3Rpb24nKTtcbn0pOyJ9)

### Description

[Chai](https://www.chaijs.com) is a BDD / TDD assertion library for JavaScript. It comes with [two styles](https://www.chaijs.com/) of assertions: `should` and `expect`.

The `expect` interface provides a function as a starting point for chaining your language assertions and works with `undefined` and `null` values.
The `should` style allows for the same chainable assertions as the expect interface, however it extends each object with a should property to start your chain and [does not work](https://www.chaijs.com/guide/styles/#should-extras) with `undefined` and `null` values.

This rule migrates Chai `should` style assertions to `expect` style assertions. Note this is an example rule and a excerpt from [the original rules](https://github.com/43081j/codemods/blob/cddfe101e7f759e4da08b7e2f7bfe892c20f6f48/codemods/chai-should-to-expect.yml).

### YAML

```yaml
id: should_to_expect_instanceof
language: TypeScript
rule:
  any:
  - pattern: $NAME.should.be.an.instanceof($TYPE)
  - pattern: $NAME.should.be.an.instanceOf($TYPE)
fix: |-
  expect($NAME).instanceOf($TYPE)
---
id: should_to_expect_genericShouldBe
language: TypeScript
rule:
  pattern: $NAME.should.be.$PROP
fix: |-
  expect($NAME).to.be.$PROP
```

### Example

```js {2,5-9}
it('should produce an instance of chokidar.FSWatcher', () => {
  watcher.should.be.an.instanceof(chokidar.FSWatcher);
});
it('should expose public API methods', () => {
  watcher.on.should.be.a('function');
  watcher.emit.should.be.a('function');
  watcher.add.should.be.a('function');
  watcher.close.should.be.a('function');
  watcher.getWatched.should.be.a('function');
});
```

### Diff

```js
it('should produce an instance of chokidar.FSWatcher', () => {
  watcher.should.be.an.instanceof(chokidar.FSWatcher); // [!code --]
  expect(watcher).instanceOf(chokidar.FSWatcher); // [!code ++]
});
it('should expose public API methods', () => {
  watcher.on.should.be.a('function');   // [!code --]
  watcher.emit.should.be.a('function'); // [!code --]
  watcher.add.should.be.a('function');  // [!code --]
  watcher.close.should.be.a('function'); // [!code --]
  watcher.getWatched.should.be.a('function'); // [!code --]
  expect(watcher.on).to.be.a('function'); // [!code ++]
  expect(watcher.emit).to.be.a('function'); // [!code ++]
  expect(watcher.add).to.be.a('function'); // [!code ++]
  expect(watcher.close).to.be.a('function'); // [!code ++]
  expect(watcher.getWatched).to.be.a('function'); // [!code ++]
});
```

### Contributed by

[James](https://bsky.app/profile/43081j.com), by [this post](https://bsky.app/profile/43081j.com/post/3lgimzfxza22i)

### Exercise

Exercise left to the reader: can you write a rule to implement [this migration to `node:assert`](https://github.com/paulmillr/chokidar/pull/1409/files)?

## Speed up Barrel Import&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6IiIsInJld3JpdGUiOiIiLCJjb25maWciOiJydWxlOlxuICBwYXR0ZXJuOiBpbXBvcnQgeyQkJElERU5UU30gZnJvbSAnLi9iYXJyZWwnXG5yZXdyaXRlcnM6XG4tIGlkOiByZXdyaXRlLWlkZW50aWZlclxuICBydWxlOlxuICAgIHBhdHRlcm46ICRJREVOVFxuICAgIGtpbmQ6IGlkZW50aWZpZXJcbiAgZml4OiBpbXBvcnQgJElERU5UIGZyb20gJy4vYmFycmVsLyRJREVOVCdcbnRyYW5zZm9ybTpcbiAgSU1QT1JUUzpcbiAgICByZXdyaXRlOlxuICAgICAgcmV3cml0ZXJzOiBbcmV3cml0ZS1pZGVudGlmZXJdXG4gICAgICBzb3VyY2U6ICQkJElERU5UU1xuICAgICAgam9pbkJ5OiBcIlxcblwiXG5maXg6ICRJTVBPUlRTIiwic291cmNlIjoiaW1wb3J0IHsgYSwgYiwgYyB9IGZyb20gJy4vYmFycmVsJzsifQ==)

### Description

A [barrel import](https://adrianfaciu.dev/posts/barrel-files/) is a way to consolidate the exports of multiple modules into a single convenient module that can be imported using a single import statement. For instance, `import {a, b, c} from './barrel'`.

It has [some](https://vercel.com/blog/how-we-optimized-package-imports-in-next-js) [benefits](https://marvinh.dev/blog/speeding-up-javascript-ecosystem-part-7/) to import each module directly from its own file without going through the barrel file.
Such as reducing [bundle size](https://dev.to/tassiofront/barrel-files-and-why-you-should-stop-using-them-now-bc4), improving building time or avoiding [conflicting names](https://flaming.codes/posts/barrel-files-in-javascript/).

### YAML

```yaml
id: speed-up-barrel-import
language: typescript
# find the barrel import statement
rule:
  pattern: import {$$$IDENTS} from './barrel'
# rewrite imported identifiers to direct imports
rewriters:
- id: rewrite-identifer
  rule:
    pattern: $IDENT
    kind: identifier
  fix: import $IDENT from './barrel/$IDENT'
# apply the rewriter to the import statement
transform:
  IMPORTS:
    rewrite:
      rewriters: [rewrite-identifer]
      # $$$IDENTS contains imported identifiers
      source: $$$IDENTS
      # join the rewritten imports by newline
      joinBy: "\n"
fix: $IMPORTS
```

### Example

```ts {1}
import {a, b, c} from './barrel'
```

### Diff

```ts
import {a, b, c} from './barrel' // [!code --]
import a from './barrel/a' // [!code ++]
import b from './barrel/b' // [!code ++]
import c from './barrel/c' // [!code ++]
```

### Contributed by

[Herrington Darkholme](https://x.com/hd_nvim)

## Missing Component Decorator

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6ImltcG9ydCAkQSBmcm9tICdhbmltZWpzJyIsInJld3JpdGUiOiJpbXBvcnQgeyBhbmltZSBhcyAkQSB9IGZyb20gJ2FuaW1lJyIsInN0cmljdG5lc3MiOiJzbWFydCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoiaWQ6IG1pc3NpbmctY29tcG9uZW50LWRlY29yYXRvclxubWVzc2FnZTogWW91J3JlIHVzaW5nIGFuIEFuZ3VsYXIgbGlmZWN5Y2xlIG1ldGhvZCwgYnV0IG1pc3NpbmcgYW4gQW5ndWxhciBAQ29tcG9uZW50KCkgZGVjb3JhdG9yLlxubGFuZ3VhZ2U6IFR5cGVTY3JpcHRcbnNldmVyaXR5OiB3YXJuaW5nXG5ydWxlOlxuICBwYXR0ZXJuOlxuICAgIGNvbnRleHQ6ICdjbGFzcyBIaSB7ICRNRVRIT0QoKSB7ICQkJF99IH0nXG4gICAgc2VsZWN0b3I6IG1ldGhvZF9kZWZpbml0aW9uXG4gIGluc2lkZTpcbiAgICBwYXR0ZXJuOiAnY2xhc3MgJEtMQVNTICQkJF8geyAkJCRfIH0nXG4gICAgc3RvcEJ5OiBlbmRcbiAgICBub3Q6XG4gICAgICBoYXM6XG4gICAgICAgIHBhdHRlcm46ICdAQ29tcG9uZW50KCQkJF8pJ1xuY29uc3RyYWludHM6XG4gIE1FVEhPRDpcbiAgICByZWdleDogbmdPbkluaXR8bmdPbkRlc3Ryb3lcbmxhYmVsczpcbiAgS0xBU1M6XG4gICAgc3R5bGU6IHByaW1hcnlcbiAgICBtZXNzYWdlOiBcIlRoaXMgY2xhc3MgaXMgbWlzc2luZyB0aGUgZGVjb3JhdG9yLlwiXG4gIE1FVEhPRDpcbiAgICBzdHlsZTogc2Vjb25kYXJ5XG4gICAgbWVzc2FnZTogXCJUaGlzIGlzIGFuIEFuZ3VsYXIgbGlmZWN5Y2xlIG1ldGhvZC5cIlxubWV0YWRhdGE6XG4gIGNvbnRyaWJ1dGVkQnk6IHNhbXdpZ2h0dCIsInNvdXJjZSI6ImNsYXNzIE5vdENvbXBvbmVudCB7XG4gICAgbmdPbkluaXQoKSB7fVxufVxuXG5AQ29tcG9uZW50KClcbmNsYXNzIEtsYXNzIHtcbiAgICBuZ09uSW5pdCgpIHt9XG59In0=)

### Description

Angular lifecycle methods are a set of methods that allow you to hook into the lifecycle of an Angular component or directive.
They must be used within a class that is decorated with the `@Component()` decorator.

### YAML

This rule illustrates how to use custom labels to highlight specific parts of the code.

```yaml
id: missing-component-decorator
message: You're using an Angular lifecycle method, but missing an Angular @Component() decorator.
language: TypeScript
severity: warning
rule:
  pattern:
    context: 'class Hi { $METHOD() { $$$_} }'
    selector: method_definition
  inside:
    pattern: 'class $KLASS $$$_ { $$$_ }'
    stopBy: end
    not:
      has:
        pattern: '@Component($$$_)'
constraints:
  METHOD:
    regex: ngOnInit|ngOnDestroy
labels:
  KLASS:
    style: primary
    message: "This class is missing the decorator."
  METHOD:
    style: secondary
    message: "This is an Angular lifecycle method."
metadata:
  contributedBy: samwightt
```

### Example

```ts {2}
class NotComponent {
    ngOnInit() {}
}

@Component()
class Klass {
    ngOnInit() {}
}
```

### Contributed by

[Sam Wight](https://github.com/samwightt).

## Find Import Identifiers

* [Playground Link](https://ast-grep.github.io/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InR5cGVzY3JpcHQiLCJxdWVyeSI6ImNvbnNvbGUubG9nKCRNQVRDSCkiLCJyZXdyaXRlIjoibG9nZ2VyLmxvZygkTUFUQ0gpIiwic3RyaWN0bmVzcyI6InNtYXJ0Iiwic2VsZWN0b3IiOiIiLCJjb25maWciOiIjIGZpbmQtYWxsLWltcG9ydHMtYW5kLXJlcXVpcmVzLnlhbWxcbmlkOiBmaW5kLWFsbC1pbXBvcnRzLWFuZC1yZXF1aXJlc1xubGFuZ3VhZ2U6IFR5cGVTY3JpcHRcbm1lc3NhZ2U6IEZvdW5kIG1vZHVsZSBpbXBvcnQgb3IgcmVxdWlyZS5cbnNldmVyaXR5OiBpbmZvXG5ydWxlOlxuICBhbnk6XG4gICAgIyBBTElBUyBJTVBPUlRTXG4gICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAjIGltcG9ydCB7IE9SSUdJTkFMIGFzIEFMSUFTIH0gZnJvbSAnU09VUkNFJ1xuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgLSBhbGw6XG4gICAgICAgICMgMS4gVGFyZ2V0IHRoZSBzcGVjaWZpYyBub2RlIHR5cGUgZm9yIG5hbWVkIGltcG9ydHNcbiAgICAgICAgLSBraW5kOiBpbXBvcnRfc3BlY2lmaWVyXG4gICAgICAgICMgMi4gRW5zdXJlIGl0ICpoYXMqIGFuICdhbGlhcycgZmllbGQsIGNhcHR1cmluZyB0aGUgYWxpYXMgaWRlbnRpZmllclxuICAgICAgICAtIGhhczpcbiAgICAgICAgICAgIGZpZWxkOiBhbGlhc1xuICAgICAgICAgICAgcGF0dGVybjogJEFMSUFTXG4gICAgICAgICMgMy4gQ2FwdHVyZSB0aGUgb3JpZ2luYWwgaWRlbnRpZmllciAod2hpY2ggaGFzIHRoZSAnbmFtZScgZmllbGQpXG4gICAgICAgIC0gaGFzOlxuICAgICAgICAgICAgZmllbGQ6IG5hbWVcbiAgICAgICAgICAgIHBhdHRlcm46ICRPUklHSU5BTFxuICAgICAgICAjIDQuIEZpbmQgYW4gQU5DRVNUT1IgaW1wb3J0X3N0YXRlbWVudCBhbmQgY2FwdHVyZSBpdHMgc291cmNlIHBhdGhcbiAgICAgICAgLSBpbnNpZGU6XG4gICAgICAgICAgICBzdG9wQnk6IGVuZCAjIDw8PC0tLSBUaGlzIGlzIHRoZSBrZXkgZml4ISBTZWFyY2ggYW5jZXN0b3JzLlxuICAgICAgICAgICAga2luZDogaW1wb3J0X3N0YXRlbWVudFxuICAgICAgICAgICAgaGFzOiAjIEVuc3VyZSB0aGUgZm91bmQgaW1wb3J0X3N0YXRlbWVudCBoYXMgdGhlIHNvdXJjZSBmaWVsZFxuICAgICAgICAgICAgICBmaWVsZDogc291cmNlXG4gICAgICAgICAgICAgIHBhdHRlcm46ICRTT1VSQ0VcblxuICAgICMgREVGQVVMVCBJTVBPUlRTXG4gICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAjIGltcG9ydCB7IE9SSUdJTkFMIH0gZnJvbSAnU09VUkNFJ1xuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgLSBhbGw6XG4gICAgICAgIC0ga2luZDogaW1wb3J0X3N0YXRlbWVudFxuICAgICAgICAtIGhhczpcbiAgICAgICAgICAgICMgRW5zdXJlIGl0IGhhcyBhbiBpbXBvcnRfY2xhdXNlLi4uXG4gICAgICAgICAgICBraW5kOiBpbXBvcnRfY2xhdXNlXG4gICAgICAgICAgICBoYXM6XG4gICAgICAgICAgICAgICMgLi4udGhhdCBkaXJlY3RseSBjb250YWlucyBhbiBpZGVudGlmaWVyICh0aGUgZGVmYXVsdCBpbXBvcnQgbmFtZSlcbiAgICAgICAgICAgICAgIyBUaGlzIGlkZW50aWZpZXIgaXMgTk9UIHVuZGVyIGEgJ25hbWVkX2ltcG9ydHMnIG9yICduYW1lc3BhY2VfaW1wb3J0JyBub2RlXG4gICAgICAgICAgICAgIGtpbmQ6IGlkZW50aWZpZXJcbiAgICAgICAgICAgICAgcGF0dGVybjogJERFRkFVTFRfTkFNRVxuICAgICAgICAtIGhhczpcbiAgICAgICAgICAgIGZpZWxkOiBzb3VyY2VcbiAgICAgICAgICAgIHBhdHRlcm46ICRTT1VSQ0VcbiAgICBcbiAgICAjIFJFR1VMQVIgSU1QT1JUU1xuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgIyBpbXBvcnQgeyBPUklHSU5BTCB9IGZyb20gJ1NPVVJDRSdcbiAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgIC0gYWxsOlxuICAgICAgICAjIDEuIFRhcmdldCB0aGUgc3BlY2lmaWMgbm9kZSB0eXBlIGZvciBuYW1lZCBpbXBvcnRzXG4gICAgICAgIC0ga2luZDogaW1wb3J0X3NwZWNpZmllclxuICAgICAgICAjIDIuIEVuc3VyZSBpdCAqaGFzKiBhbiAnYWxpYXMnIGZpZWxkLCBjYXB0dXJpbmcgdGhlIGFsaWFzIGlkZW50aWZpZXJcbiAgICAgICAgLSBoYXM6XG4gICAgICAgICAgICBmaWVsZDogbmFtZVxuICAgICAgICAgICAgcGF0dGVybjogJE9SSUdJTkFMXG4gICAgICAgICMgNC4gRmluZCBhbiBBTkNFU1RPUiBpbXBvcnRfc3RhdGVtZW50IGFuZCBjYXB0dXJlIGl0cyBzb3VyY2UgcGF0aFxuICAgICAgICAtIGluc2lkZTpcbiAgICAgICAgICAgIHN0b3BCeTogZW5kICMgPDw8LS0tIFRoaXMgaXMgdGhlIGtleSBmaXghIFNlYXJjaCBhbmNlc3RvcnMuXG4gICAgICAgICAgICBraW5kOiBpbXBvcnRfc3RhdGVtZW50XG4gICAgICAgICAgICBoYXM6ICMgRW5zdXJlIHRoZSBmb3VuZCBpbXBvcnRfc3RhdGVtZW50IGhhcyB0aGUgc291cmNlIGZpZWxkXG4gICAgICAgICAgICAgIGZpZWxkOiBzb3VyY2VcbiAgICAgICAgICAgICAgcGF0dGVybjogJFNPVVJDRVxuXG4gICAgIyBEWU5BTUlDIElNUE9SVFMgKFNpbmdsZSBWYXJpYWJsZSBBc3NpZ25tZW50KSBcbiAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICMgZWc6IChjb25zdCBWQVJfTkFNRSA9IHJlcXVpcmUoJ1NPVVJDRScpKVxuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgLSBhbGw6XG4gICAgICAgIC0ga2luZDogdmFyaWFibGVfZGVjbGFyYXRvclxuICAgICAgICAtIGhhczpcbiAgICAgICAgICAgIGZpZWxkOiBuYW1lXG4gICAgICAgICAgICBraW5kOiBpZGVudGlmaWVyXG4gICAgICAgICAgICBwYXR0ZXJuOiAkVkFSX05BTUUgIyBDYXB0dXJlIHRoZSBzaW5nbGUgdmFyaWFibGUgbmFtZVxuICAgICAgICAtIGhhczpcbiAgICAgICAgICAgIGZpZWxkOiB2YWx1ZVxuICAgICAgICAgICAgYW55OlxuICAgICAgICAgICAgICAjIERpcmVjdCBjYWxsXG4gICAgICAgICAgICAgIC0gYWxsOiAjIFdyYXAgY29uZGl0aW9ucyBpbiBhbGxcbiAgICAgICAgICAgICAgICAgIC0ga2luZDogY2FsbF9leHByZXNzaW9uXG4gICAgICAgICAgICAgICAgICAtIGhhczogeyBmaWVsZDogZnVuY3Rpb24sIHJlZ2V4OiAnXihyZXF1aXJlfGltcG9ydCkkJyB9XG4gICAgICAgICAgICAgICAgICAtIGhhczogeyBmaWVsZDogYXJndW1lbnRzLCBoYXM6IHsga2luZDogc3RyaW5nLCBwYXR0ZXJuOiAkU09VUkNFIH0gfSAjIENhcHR1cmUgc291cmNlXG4gICAgICAgICAgICAgICMgQXdhaXRlZCBjYWxsXG4gICAgICAgICAgICAgIC0ga2luZDogYXdhaXRfZXhwcmVzc2lvblxuICAgICAgICAgICAgICAgIGhhczpcbiAgICAgICAgICAgICAgICAgIGFsbDogIyBXcmFwIGNvbmRpdGlvbnMgaW4gYWxsXG4gICAgICAgICAgICAgICAgICAgIC0ga2luZDogY2FsbF9leHByZXNzaW9uXG4gICAgICAgICAgICAgICAgICAgIC0gaGFzOiB7IGZpZWxkOiBmdW5jdGlvbiwgcmVnZXg6ICdeKHJlcXVpcmV8aW1wb3J0KSQnIH1cbiAgICAgICAgICAgICAgICAgICAgLSBoYXM6IHsgZmllbGQ6IGFyZ3VtZW50cywgaGFzOiB7IGtpbmQ6IHN0cmluZywgcGF0dGVybjogJFNPVVJDRSB9IH0gIyBDYXB0dXJlIHNvdXJjZVxuXG4gICAgIyBEWU5BTUlDIElNUE9SVFMgKERlc3RydWN0dXJlZCBTaG9ydGhhbmQgQXNzaWdubWVudCkgICAgIFxuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgIyBlZzogKGNvbnN0IHsgT1JJR0lOQUwgfSA9IHJlcXVpcmUoJ1NPVVJDRScpKVxuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgLSBhbGw6XG4gICAgICAgICMgMS4gVGFyZ2V0IHRoZSBzaG9ydGhhbmQgaWRlbnRpZmllciB3aXRoaW4gdGhlIHBhdHRlcm5cbiAgICAgICAgLSBraW5kOiBzaG9ydGhhbmRfcHJvcGVydHlfaWRlbnRpZmllcl9wYXR0ZXJuXG4gICAgICAgIC0gcGF0dGVybjogJE9SSUdJTkFMXG4gICAgICAgICMgMi4gRW5zdXJlIGl0J3MgaW5zaWRlIGFuIG9iamVjdF9wYXR0ZXJuIHRoYXQgaXMgdGhlIG5hbWUgb2YgYSB2YXJpYWJsZV9kZWNsYXJhdG9yXG4gICAgICAgIC0gaW5zaWRlOlxuICAgICAgICAgICAga2luZDogb2JqZWN0X3BhdHRlcm5cbiAgICAgICAgICAgIGluc2lkZTogIyBDaGVjayB0aGUgdmFyaWFibGVfZGVjbGFyYXRvciBpdCBiZWxvbmdzIHRvXG4gICAgICAgICAgICAgIGtpbmQ6IHZhcmlhYmxlX2RlY2xhcmF0b3JcbiAgICAgICAgICAgICAgIyAzLiBDaGVjayB0aGUgdmFsdWUgYXNzaWduZWQgYnkgdGhlIHZhcmlhYmxlX2RlY2xhcmF0b3JcbiAgICAgICAgICAgICAgaGFzOlxuICAgICAgICAgICAgICAgIGZpZWxkOiB2YWx1ZVxuICAgICAgICAgICAgICAgIGFueTpcbiAgICAgICAgICAgICAgICAgICMgRGlyZWN0IGNhbGxcbiAgICAgICAgICAgICAgICAgIC0gYWxsOlxuICAgICAgICAgICAgICAgICAgICAgIC0ga2luZDogY2FsbF9leHByZXNzaW9uXG4gICAgICAgICAgICAgICAgICAgICAgLSBoYXM6IHsgZmllbGQ6IGZ1bmN0aW9uLCByZWdleDogJ14ocmVxdWlyZXxpbXBvcnQpJCcgfVxuICAgICAgICAgICAgICAgICAgICAgIC0gaGFzOiB7IGZpZWxkOiBhcmd1bWVudHMsIGhhczogeyBraW5kOiBzdHJpbmcsIHBhdHRlcm46ICRTT1VSQ0UgfSB9ICMgQ2FwdHVyZSBzb3VyY2VcbiAgICAgICAgICAgICAgICAgICMgQXdhaXRlZCBjYWxsXG4gICAgICAgICAgICAgICAgICAtIGtpbmQ6IGF3YWl0X2V4cHJlc3Npb25cbiAgICAgICAgICAgICAgICAgICAgaGFzOlxuICAgICAgICAgICAgICAgICAgICAgIGFsbDpcbiAgICAgICAgICAgICAgICAgICAgICAgIC0ga2luZDogY2FsbF9leHByZXNzaW9uXG4gICAgICAgICAgICAgICAgICAgICAgICAtIGhhczogeyBmaWVsZDogZnVuY3Rpb24sIHJlZ2V4OiAnXihyZXF1aXJlfGltcG9ydCkkJyB9XG4gICAgICAgICAgICAgICAgICAgICAgICAtIGhhczogeyBmaWVsZDogYXJndW1lbnRzLCBoYXM6IHsga2luZDogc3RyaW5nLCBwYXR0ZXJuOiAkU09VUkNFIH0gfSAjIENhcHR1cmUgc291cmNlXG4gICAgICAgICAgICAgIHN0b3BCeTogZW5kICMgU2VhcmNoIGFuY2VzdG9ycyB0byBmaW5kIHRoZSBjb3JyZWN0IHZhcmlhYmxlX2RlY2xhcmF0b3JcblxuICAgICMgRFlOQU1JQyBJTVBPUlRTIChEZXN0cnVjdHVyZWQgQWxpYXMgQXNzaWdubWVudCkgXG4gICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAjIGVnOiAoY29uc3QgeyBPUklHSU5BTDogQUxJQVMgfSA9IHJlcXVpcmUoJ1NPVVJDRScpKVxuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgLSBhbGw6XG4gICAgICAgICMgMS4gVGFyZ2V0IHRoZSBwYWlyX3BhdHRlcm4gZm9yIGFsaWFzZWQgZGVzdHJ1Y3R1cmluZ1xuICAgICAgICAtIGtpbmQ6IHBhaXJfcGF0dGVyblxuICAgICAgICAjIDIuIENhcHR1cmUgdGhlIG9yaWdpbmFsIGlkZW50aWZpZXIgKGtleSlcbiAgICAgICAgLSBoYXM6XG4gICAgICAgICAgICBmaWVsZDoga2V5XG4gICAgICAgICAgICBraW5kOiBwcm9wZXJ0eV9pZGVudGlmaWVyICMgQ291bGQgYmUgc3RyaW5nL251bWJlciBsaXRlcmFsIHRvbywgYnV0IHByb3BlcnR5X2lkZW50aWZpZXIgaXMgY29tbW9uXG4gICAgICAgICAgICBwYXR0ZXJuOiAkT1JJR0lOQUxcbiAgICAgICAgIyAzLiBDYXB0dXJlIHRoZSBhbGlhcyBpZGVudGlmaWVyICh2YWx1ZSlcbiAgICAgICAgLSBoYXM6XG4gICAgICAgICAgICBmaWVsZDogdmFsdWVcbiAgICAgICAgICAgIGtpbmQ6IGlkZW50aWZpZXJcbiAgICAgICAgICAgIHBhdHRlcm46ICRBTElBU1xuICAgICAgICAjIDQuIEVuc3VyZSBpdCdzIGluc2lkZSBhbiBvYmplY3RfcGF0dGVybiB0aGF0IGlzIHRoZSBuYW1lIG9mIGEgdmFyaWFibGVfZGVjbGFyYXRvclxuICAgICAgICAtIGluc2lkZTpcbiAgICAgICAgICAgIGtpbmQ6IG9iamVjdF9wYXR0ZXJuXG4gICAgICAgICAgICBpbnNpZGU6ICMgQ2hlY2sgdGhlIHZhcmlhYmxlX2RlY2xhcmF0b3IgaXQgYmVsb25ncyB0b1xuICAgICAgICAgICAgICBraW5kOiB2YXJpYWJsZV9kZWNsYXJhdG9yXG4gICAgICAgICAgICAgICMgNS4gQ2hlY2sgdGhlIHZhbHVlIGFzc2lnbmVkIGJ5IHRoZSB2YXJpYWJsZV9kZWNsYXJhdG9yXG4gICAgICAgICAgICAgIGhhczpcbiAgICAgICAgICAgICAgICBmaWVsZDogdmFsdWVcbiAgICAgICAgICAgICAgICBhbnk6XG4gICAgICAgICAgICAgICAgICAjIERpcmVjdCBjYWxsXG4gICAgICAgICAgICAgICAgICAtIGFsbDpcbiAgICAgICAgICAgICAgICAgICAgICAtIGtpbmQ6IGNhbGxfZXhwcmVzc2lvblxuICAgICAgICAgICAgICAgICAgICAgIC0gaGFzOiB7IGZpZWxkOiBmdW5jdGlvbiwgcmVnZXg6ICdeKHJlcXVpcmV8aW1wb3J0KSQnIH1cbiAgICAgICAgICAgICAgICAgICAgICAtIGhhczogeyBmaWVsZDogYXJndW1lbnRzLCBoYXM6IHsga2luZDogc3RyaW5nLCBwYXR0ZXJuOiAkU09VUkNFIH0gfSAjIENhcHR1cmUgc291cmNlXG4gICAgICAgICAgICAgICAgICAjIEF3YWl0ZWQgY2FsbFxuICAgICAgICAgICAgICAgICAgLSBraW5kOiBhd2FpdF9leHByZXNzaW9uXG4gICAgICAgICAgICAgICAgICAgIGhhczpcbiAgICAgICAgICAgICAgICAgICAgICBhbGw6XG4gICAgICAgICAgICAgICAgICAgICAgICAtIGtpbmQ6IGNhbGxfZXhwcmVzc2lvblxuICAgICAgICAgICAgICAgICAgICAgICAgLSBoYXM6IHsgZmllbGQ6IGZ1bmN0aW9uLCByZWdleDogJ14ocmVxdWlyZXxpbXBvcnQpJCcgfVxuICAgICAgICAgICAgICAgICAgICAgICAgLSBoYXM6IHsgZmllbGQ6IGFyZ3VtZW50cywgaGFzOiB7IGtpbmQ6IHN0cmluZywgcGF0dGVybjogJFNPVVJDRSB9IH0gIyBDYXB0dXJlIHNvdXJjZVxuICAgICAgICAgICAgICBzdG9wQnk6IGVuZCAjIFNlYXJjaCBhbmNlc3RvcnMgdG8gZmluZCB0aGUgY29ycmVjdCB2YXJpYWJsZV9kZWNsYXJhdG9yXG4gICAgICAgICAgICBzdG9wQnk6IGVuZCAjIEVuc3VyZSB3ZSBjaGVjayBhbmNlc3RvcnMgZm9yIHRoZSB2YXJpYWJsZV9kZWNsYXJhdG9yXG5cbiAgICAjIERZTkFNSUMgSU1QT1JUUyAoU2lkZSBFZmZlY3QgLyBTb3VyY2UgT25seSkgXG4gICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAjIGVnOiAocmVxdWlyZSgnU09VUkNFJykpXG4gICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAtIGFsbDpcbiAgICAgICAgLSBraW5kOiBzdHJpbmcgIyBUYXJnZXQgdGhlIHNvdXJjZSBzdHJpbmcgbGl0ZXJhbCBkaXJlY3RseVxuICAgICAgICAtIHBhdHRlcm46ICRTT1VSQ0VcbiAgICAgICAgLSBpbnNpZGU6ICMgU3RyaW5nIG11c3QgYmUgdGhlIGFyZ3VtZW50IG9mIHJlcXVpcmUoKSBvciBpbXBvcnQoKVxuICAgICAgICAgICAga2luZDogYXJndW1lbnRzXG4gICAgICAgICAgICBwYXJlbnQ6XG4gICAgICAgICAgICAgIGtpbmQ6IGNhbGxfZXhwcmVzc2lvblxuICAgICAgICAgICAgICBoYXM6XG4gICAgICAgICAgICAgICAgZmllbGQ6IGZ1bmN0aW9uXG4gICAgICAgICAgICAgICAgIyBNYXRjaCAncmVxdWlyZScgaWRlbnRpZmllciBvciAnaW1wb3J0JyBrZXl3b3JkIHVzZWQgZHluYW1pY2FsbHlcbiAgICAgICAgICAgICAgICByZWdleDogJ14ocmVxdWlyZXxpbXBvcnQpJCdcbiAgICAgICAgICAgIHN0b3BCeTogZW5kICMgU2VhcmNoIGFuY2VzdG9ycyBpZiBuZWVkZWQgKGZvciB0aGUgYXJndW1lbnRzL2NhbGxfZXhwcmVzc2lvbilcbiAgICAgICAgLSBub3Q6XG4gICAgICAgICAgICBpbnNpZGU6XG4gICAgICAgICAgICAgIGtpbmQ6IGxleGljYWxfZGVjbGFyYXRpb25cbiAgICAgICAgICAgICAgc3RvcEJ5OiBlbmQgIyBTZWFyY2ggYWxsIGFuY2VzdG9ycyB1cCB0byB0aGUgcm9vdFxuXG4gICAgIyBOQU1FU1BBQ0UgSU1QT1JUUyBcbiAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICMgZWc6IChpbXBvcnQgKiBhcyBucyBmcm9tICdtb2QnKVxuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgLSBhbGw6XG4gICAgICAgIC0ga2luZDogaW1wb3J0X3N0YXRlbWVudFxuICAgICAgICAtIGhhczpcbiAgICAgICAgICAgIGtpbmQ6IGltcG9ydF9jbGF1c2VcbiAgICAgICAgICAgIGhhczpcbiAgICAgICAgICAgICAga2luZDogbmFtZXNwYWNlX2ltcG9ydFxuICAgICAgICAgICAgICBoYXM6XG4gICAgICAgICAgICAgICAgIyBuYW1lc3BhY2VfaW1wb3J0J3MgY2hpbGQgaWRlbnRpZmllciBpcyB0aGUgYWxpYXNcbiAgICAgICAgICAgICAgICBraW5kOiBpZGVudGlmaWVyXG4gICAgICAgICAgICAgICAgcGF0dGVybjogJE5BTUVTUEFDRV9BTElBU1xuICAgICAgICAtIGhhczpcbiAgICAgICAgICAgIGZpZWxkOiBzb3VyY2VcbiAgICAgICAgICAgIHBhdHRlcm46ICRTT1VSQ0VcblxuICAgICMgU0lERSBFRkZFQ1QgSU1QT1JUUyBcbiAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICMgZWc6IChpbXBvcnQgJ21vZCcpXG4gICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAtIGFsbDpcbiAgICAgICAgLSBraW5kOiBpbXBvcnRfc3RhdGVtZW50XG4gICAgICAgIC0gbm90OiAjIE11c3QgTk9UIGhhdmUgYW4gaW1wb3J0X2NsYXVzZVxuICAgICAgICAgICAgaGFzOiB7IGtpbmQ6IGltcG9ydF9jbGF1c2UgfVxuICAgICAgICAtIGhhczogIyBCdXQgbXVzdCBoYXZlIGEgc291cmNlXG4gICAgICAgICAgICBmaWVsZDogc291cmNlXG4gICAgICAgICAgICBwYXR0ZXJuOiAkU09VUkNFXG4iLCJzb3VyY2UiOiIvL0B0cy1ub2NoZWNrXG4vLyBOYW1lZCBpbXBvcnRcbmltcG9ydCB7IHRlc3RpbmcgfSBmcm9tICcuL3Rlc3RzJztcblxuLy8gQWxpYXNlZCBpbXBvcnRcbmltcG9ydCB7IHRlc3RpbmcgYXMgdGVzdCB9IGZyb20gJy4vdGVzdHMyJztcblxuLy8gRGVmYXVsdCBpbXBvcnRcbmltcG9ydCBoZWxsbyBmcm9tICdoZWxsb193b3JsZDEnO1xuXG4vLyBOYW1lc3BhY2UgaW1wb3J0XG5pbXBvcnQgKiBhcyBzb21ldGhpbmcgZnJvbSAnaGVsbG9fd29ybGQyJztcblxuLy8gU2lkZS1lZmZlY3QgaW1wb3J0XG5pbXBvcnQgJ0BmYXN0aWZ5L3N0YXRpYyc7XG5cbi8vIFR5cGUgaW1wb3J0XG5pbXBvcnQge3R5cGUgaGVsbG8xMjQzIGFzIHRlc3Rpbmd9IGZyb20gJ2hlbGxvJztcblxuLy8gUmVxdWlyZSBwYXR0ZXJuc1xuY29uc3QgbW9kID0gcmVxdWlyZSgnc29tZS1tb2R1bGUnKTtcbnJlcXVpcmUoJ3BvbHlmaWxsJyk7XG5cbi8vIERlc3RydWN0dXJlZCByZXF1aXJlXG5jb25zdCB7IHRlc3QxMjIsIHRlc3QyIH0gPSByZXF1aXJlKCcuL2Rlc3RydWN0dXJlZDEnKTtcbi8vIEFsaWFzZWQgcmVxdWlyZVxuY29uc3QgeyB0ZXN0MTIyOiB0ZXN0MTIzLCB0ZXN0MjogdGVzdDIzLCB0ZXN0MzogdGVzdDMzIH0gPSByZXF1aXJlKCcuL2Rlc3RydWN0dXJlZDInKTtcblxuLy8gTWl4ZWQgaW1wb3J0c1xuaW1wb3J0IGRlZmF1bHRFeHBvcnQsIHsgbmFtZWRFeHBvcnQgfSBmcm9tICcuL21peGVkJztcbmltcG9ydCBkZWZhdWx0RXhwb3J0MiwgKiBhcyBuYW1lc3BhY2UgZnJvbSAnLi9taXhlZDInO1xuXG5cbi8vIE11bHRpcGxlIGltcG9ydCBsaW5lcyBmcm9tIHRoZSBzYW1lIGZpbGVcbmltcG9ydCB7IG9uZSwgdHdvIGFzIGFsaWFzLCB0aHJlZSB9IGZyb20gJy4vbXVsdGlwbGUnO1xuaW1wb3J0IHsgbmV2ZXIsIGdvbm5hLCBnaXZlLCB5b3UsIHVwIH0gZnJvbSAnLi9tdWx0aXBsZSc7XG5cbi8vIFN0cmluZyBsaXRlcmFsIHZhcmlhdGlvbnNcbmltcG9ydCB7IHRlc3QxIH0gZnJvbSBcIi4vZG91YmxlLXF1b3RlZFwiO1xuaW1wb3J0IHsgdGVzdDIgfSBmcm9tICcuL3NpbmdsZS1xdW90ZWQnO1xuXG4vLyBNdWx0aWxpbmUgaW1wb3J0c1xuaW1wb3J0IHtcbiAgICBsb25nSW1wb3J0MSxcbiAgICBsb25nSW1wb3J0MiBhcyBhbGlhczIsXG4gICAgbG9uZ0ltcG9ydDNcbn0gZnJvbSAnLi9tdWx0aWxpbmUnO1xuXG4vLyBEeW5hbWljIGltcG9ydHNcbmNvbnN0IGR5bmFtaWNNb2R1bGUgPSBpbXBvcnQoJy4vZHluYW1pYzEnKTtcbmNvbnN0IHt0ZXN0aW5nLCB0ZXN0aW5nMTIzfSA9IGltcG9ydCgnLi9keW5hbWljMicpO1xuY29uc3QgYXN5bmNEeW5hbWljTW9kdWxlID0gYXdhaXQgaW1wb3J0KCcuL2FzeW5jX2R5bmFtaWMxJykudGhlbihtb2R1bGUgPT4gbW9kdWxlLmRlZmF1bHQpO1xuLy8gQWxpYXNlZCBkeW5hbWljIGltcG9ydFxuY29uc3QgeyBvcmlnaW5hbElkZW50aWZpZXI6IGFsaWFzZWREeW5hbWljSW1wb3J0fSA9IGF3YWl0IGltcG9ydCgnLi9hc3luY19keW5hbWljMicpO1xuXG4vLyBDb21tZW50cyBpbiBpbXBvcnRzXG5pbXBvcnQgLyogdGVzdCAqLyB7IFxuICAgIC8vIENvbW1lbnQgaW4gaW1wb3J0XG4gICAgY29tbWVudGVkSW1wb3J0IFxufSBmcm9tICcuL2NvbW1lbnRlZCc7IC8vIEVuZCBvZiBsaW5lIGNvbW1lbnQgXG5cblxuIn0=)

### Description

Finding import metadata can be useful. Below is a comprehensive snippet for extracting identifiers from various import statements:

* Alias Imports (`import { hello as world } from './file'`)
* Default & Regular Imports (`import test from './my-test`')
* Dynamic Imports (`require(...)`, and `import(...)`)
* Side Effect & Namespace Imports (`import * as myCode from './code`')

### YAML

```yaml
# find-all-imports-and-identifiers.yaml
id: find-all-imports-and-identifiers
language: TypeScript
rule:
  any:
    # ALIAS IMPORTS
    # ------------------------------------------------------------
    # import { ORIGINAL as ALIAS } from 'SOURCE'
    # ------------------------------------------------------------
    - all:
        # 1. Target the specific node type for named imports
        - kind: import_specifier
        # 2. Ensure it *has* an 'alias' field, capturing the alias identifier
        - has:
            field: alias
            pattern: $ALIAS
        # 3. Capture the original identifier (which has the 'name' field)
        - has:
            field: name
            pattern: $ORIGINAL
        # 4. Find an ANCESTOR import_statement and capture its source path
        - inside:
            stopBy: end # <<<--- Search ancestors.
            kind: import_statement
            has: # Ensure the found import_statement has the source field
              field: source
              pattern: $SOURCE

    # DEFAULT IMPORTS
    # ------------------------------------------------------------
    # import { ORIGINAL } from 'SOURCE'
    # ------------------------------------------------------------
    - all:
        - kind: import_statement
        - has:
            # Ensure it has an import_clause...
            kind: import_clause
            has:
              # ...that directly contains an identifier (the default import name)
              # This identifier is NOT under a 'named_imports' or 'namespace_import' node
              kind: identifier
              pattern: $DEFAULT_NAME
        - has:
            field: source
            pattern: $SOURCE

    # REGULAR IMPORTS
    # ------------------------------------------------------------
    # import { ORIGINAL } from 'SOURCE'
    # ------------------------------------------------------------
    - all:
        # 1. Target the specific node type for named imports
        - kind: import_specifier
        # 2. Ensure it *has* an 'alias' field, capturing the alias identifier
        - has:
            field: name
            pattern: $ORIGINAL
        # 4. Find an ANCESTOR import_statement and capture its source path
        - inside:
            stopBy: end # <<<--- This is the key fix! Search ancestors.
            kind: import_statement
            has: # Ensure the found import_statement has the source field
              field: source
              pattern: $SOURCE

    # DYNAMIC IMPORTS (Single Variable Assignment)
    # ------------------------------------------------------------
    # const VAR_NAME = require('SOURCE')
    # ------------------------------------------------------------
    - all:
        - kind: variable_declarator
        - has:
            field: name
            kind: identifier
            pattern: $VAR_NAME # Capture the single variable name
        - has:
            field: value
            any:
              # Direct call
              - all: # Wrap conditions in all
                  - kind: call_expression
                  - has: { field: function, regex: '^(require|import)$' }
                  - has: { field: arguments, has: { kind: string, pattern: $SOURCE } } # Capture source
              # Awaited call
              - kind: await_expression
                has:
                  all: # Wrap conditions in all
                    - kind: call_expression
                    - has: { field: function, regex: '^(require|import)$' }
                    - has: { field: arguments, has: { kind: string, pattern: $SOURCE } } # Capture source

    # DYNAMIC IMPORTS (Destructured Shorthand Assignment)
    # ------------------------------------------------------------
    # const { ORIGINAL } = require('SOURCE')
    # ------------------------------------------------------------
    - all:
        # 1. Target the shorthand identifier within the pattern
        - kind: shorthand_property_identifier_pattern
        - pattern: $ORIGINAL
        # 2. Ensure it's inside an object_pattern that is the name of a variable_declarator
        - inside:
            kind: object_pattern
            inside: # Check the variable_declarator it belongs to
              kind: variable_declarator
              # 3. Check the value assigned by the variable_declarator
              has:
                field: value
                any:
                  # Direct call
                  - all:
                      - kind: call_expression
                      - has: { field: function, regex: '^(require|import)$' }
                      - has: { field: arguments, has: { kind: string, pattern: $SOURCE } } # Capture source
                  # Awaited call
                  - kind: await_expression
                    has:
                      all:
                        - kind: call_expression
                        - has: { field: function, regex: '^(require|import)$' }
                        - has: { field: arguments, has: { kind: string, pattern: $SOURCE } } # Capture source
              stopBy: end # Search ancestors to find the correct variable_declarator

    # DYNAMIC IMPORTS (Destructured Alias Assignment)
    # ------------------------------------------------------------
    # const { ORIGINAL: ALIAS } = require('SOURCE')
    # ------------------------------------------------------------
    - all:
        # 1. Target the pair_pattern for aliased destructuring
        - kind: pair_pattern
        # 2. Capture the original identifier (key)
        - has:
            field: key
            kind: property_identifier # Could be string/number literal too, but property_identifier is common
            pattern: $ORIGINAL
        # 3. Capture the alias identifier (value)
        - has:
            field: value
            kind: identifier
            pattern: $ALIAS
        # 4. Ensure it's inside an object_pattern that is the name of a variable_declarator
        - inside:
            kind: object_pattern
            inside: # Check the variable_declarator it belongs to
              kind: variable_declarator
              # 5. Check the value assigned by the variable_declarator
              has:
                field: value
                any:
                  # Direct call
                  - all:
                      - kind: call_expression
                      - has: { field: function, regex: '^(require|import)$' }
                      - has: { field: arguments, has: { kind: string, pattern: $SOURCE } } # Capture source
                  # Awaited call
                  - kind: await_expression
                    has:
                      all:
                        - kind: call_expression
                        - has: { field: function, regex: '^(require|import)$' }
                        - has: { field: arguments, has: { kind: string, pattern: $SOURCE } } # Capture source
              stopBy: end # Search ancestors to find the correct variable_declarator
            stopBy: end # Ensure we check ancestors for the variable_declarator

    # DYNAMIC IMPORTS (Side Effect / Source Only)
    # ------------------------------------------------------------
    # require('SOURCE')
    # ------------------------------------------------------------
    - all:
        - kind: string # Target the source string literal directly
        - pattern: $SOURCE
        - inside: # String must be the argument of require() or import()
            kind: arguments
            parent:
              kind: call_expression
              has:
                field: function
                # Match 'require' identifier or 'import' keyword used dynamically
                regex: '^(require|import)$'
            stopBy: end # Search ancestors if needed (for the arguments/call_expression)
        - not:
            inside:
              kind: lexical_declaration
              stopBy: end # Search all ancestors up to the root

    # NAMESPACE IMPORTS
    # ------------------------------------------------------------
    # import * as ns from 'mod'
    # ------------------------------------------------------------
    - all:
        - kind: import_statement
        - has:
            kind: import_clause
            has:
              kind: namespace_import
              has:
                # namespace_import's child identifier is the alias
                kind: identifier
                pattern: $NAMESPACE_ALIAS
        - has:
            field: source
            pattern: $SOURCE

    # SIDE EFFECT IMPORTS
    # ------------------------------------------------------------
    # import 'mod'
    # ------------------------------------------------------------
    - all:
        - kind: import_statement
        - not: # Must NOT have an import_clause
            has: { kind: import_clause }
        - has: # But must have a source
            field: source
            pattern: $SOURCE
```

### Example

```ts {60}
//@ts-nocheck
// Named import
import { testing } from './tests';

// Aliased import
import { testing as test } from './tests2';

// Default import
import hello from 'hello_world1';

// Namespace import
import * as something from 'hello_world2';

// Side-effect import
import '@fastify/static';

// Type import
import {type hello1243 as testing} from 'hello';

// Require patterns
const mod = require('some-module');
require('polyfill');

// Destructured require
const { test122, test2 } = require('./destructured1');
// Aliased require
const { test122: test123, test2: test23, test3: test33 } = require('./destructured2');

// Mixed imports
import defaultExport, { namedExport } from './mixed';
import defaultExport2, * as namespace from './mixed2';


// Multiple import lines from the same file
import { one, two as alias, three } from './multiple';
import { never, gonna, give, you, up } from './multiple';

// String literal variations
import { test1 } from "./double-quoted";
import { test2 } from './single-quoted';

// Multiline imports
import {
    longImport1,
    longImport2 as alias2,
    longImport3
} from './multiline';

// Dynamic imports
const dynamicModule = import('./dynamic1');
const {testing, testing123} = import('./dynamic2');
const asyncDynamicModule = await import('./async_dynamic1').then(module => module.default);
// Aliased dynamic import
const { originalIdentifier: aliasedDynamicImport} = await import('./async_dynamic2');

// Comments in imports
import /* test */ {
    // Comment in import
    commentedImport
} from './commented'; // End of line comment
```

### Contributed by

[Michael Angelo Rivera](https://github.com/michaelangeloio)

## Use Logical Assignment Operators

* [Playground Link](/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoiamF2YXNjcmlwdCIsInF1ZXJ5IjoiJEEgPSAkQSB8fCAkQiIsInJld3JpdGUiOiIkQSB8fD0gJEIiLCJzdHJpY3RuZXNzIjoic21hcnQiLCJzZWxlY3RvciI6IiIsImNvbmZpZyI6IiMgWUFNTCBSdWxlIGlzIG1vcmUgcG93ZXJmdWwhXG4jIGh0dHBzOi8vYXN0LWdyZXAuZ2l0aHViLmlvL2d1aWRlL3J1bGUtY29uZmlnLmh0bWwjcnVsZVxucnVsZTpcbiAgYW55OlxuICAgIC0gcGF0dGVybjogY29uc29sZS5sb2coJEEpXG4gICAgLSBwYXR0ZXJuOiBjb25zb2xlLmRlYnVnKCRBKVxuZml4OlxuICBsb2dnZXIubG9nKCRBKSIsInNvdXJjZSI6ImNvbnN0IGEgPSB7IGR1cmF0aW9uOiA1MCwgdGl0bGU6ICcnIH07XG5cbmEuZHVyYXRpb24gPSBhLmR1cmF0aW9uIHx8IDEwO1xuY29uc29sZS5sb2coYS5kdXJhdGlvbik7XG5hLnRpdGxlID0gYS50aXRsZSB8fCAndGl0bGUgaXMgZW1wdHkuJztcbmNvbnNvbGUubG9nKGEudGl0bGUpO1xuIn0=)

### Description

A logical assignment operator in JavaScript combines a logical operation (like OR or nullish coalescing) with an assignment. It updates a variable or property only under specific conditions, making code more concise.

This is a relatively new feature in JavaScript (introduced in ES2021), so older codebases might not use it yet. This rule identifies instances where a variable is assigned a value using a logical OR (`||`) operation and suggests replacing it with the more concise logical assignment operator (`||=`).

### Pattern

```shell
ast-grep -p '$A = $A || $B' -r '$A ||= $B' -l ts
```

### Example

```ts {3,5}
const a = { duration: 50, title: '' };

a.duration = a.duration || 10;
console.log(a.duration);
a.title = a.title || 'title is empty.';
console.log(a.title);
```

### Diff

```ts
const a = { duration: 50, title: '' };

a.duration = a.duration || 10; // [!code --]
a.duration ||= 10; // [!code ++]
console.log(a.duration);
a.title = a.title || 'title is empty.'; // [!code --]
a.title ||= 'title is empty.'; // [!code ++]
console.log(a.title);
```

### Contributed by

Inspired by [this tweet](https://x.com/YTCodeAntonio/status/1973720331656605809).
