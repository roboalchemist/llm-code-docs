# Source: https://clerc.so1ve.dev/guide/advanced.md

---

url: /guide/advanced.md
---

# Advanced Usage

## Passing Custom Arguments

Clerc allows you to pass a custom array of arguments instead of using the default `process.argv` / `Deno.args`. This is useful for testing or specific environments.

```ts twoslash
// @include: imports
Cli().parse(["node", "my-cli", "greet"]); // Pass a custom array of arguments
```

Alternatively, you can also pass an argument object:

```ts twoslash
// @include: imports
Cli().parse({
  argv: ["greet"],
});
```

## Parse Only Without Execution

Sometimes you may want to parse commands and flags without immediately executing the command handler. Clerc provides an option to achieve this:

```ts twoslash
// @include: imports
const result = Cli().parse({
  run: false, // Parse only, do not execute
});
```

When you need to run, you can call:

```ts twoslash
// @include: imports
result.run(); // Execute the parsed command
```
