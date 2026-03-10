# Add back the modified/prettified files to staging
echo "$FILES" | xargs git add

exit 0
```

If git is reporting that your prettified files are still modified after committing, you may need to add a [post-commit script to update git’s index](https://github.com/prettier/prettier/issues/2978#issuecomment-334408427).

Add something like the following to `.git/hooks/post-commit`:

```sh
#!/bin/sh
git update-index -g
```


---


### Rationale

---
id: rationale
title: Rationale
---

Prettier is an opinionated code formatter. This document explains some of its choices.

## What Prettier is concerned about

### Correctness

The first requirement of Prettier is to output valid code that has the exact same behavior as before formatting. Please report any code where Prettier fails to follow these correctness rules — that’s a bug which needs to be fixed!

### Strings

Double or single quotes? Prettier chooses the one which results in the fewest number of escapes. `"It's gettin' better!"`, not `'It\'s gettin\' better!'`. In case of a tie or the string not containing any quotes, Prettier defaults to double quotes (but that can be changed via the [singleQuote](/docs/options#quotes) option).

JSX has its own option for quotes: [jsxSingleQuote](/docs/options#jsx-quotes).
JSX takes its roots from HTML, where the dominant use of quotes for attributes is double quotes. Browser developer tools also follow this convention by always displaying HTML with double quotes, even if the source code uses single quotes. A separate option allows using single quotes for JS and double quotes for "HTML" (JSX).

Prettier maintains the way your string is escaped. For example, `"🙂"` won’t be formatted into `"\uD83D\uDE42"` and vice versa.

### Empty lines

It turns out that empty lines are very hard to automatically generate. The approach that Prettier takes is to preserve empty lines the way they were in the original source code. There are two additional rules:

- Prettier collapses multiple blank lines into a single blank line.
- Empty lines at the start and end of blocks (and whole files) are removed. (Files always end with a single newline, though.)

### Multi-line objects

By default, Prettier’s printing algorithm prints expressions on a single line if they fit. Objects are used for a lot of different things in JavaScript, though, and sometimes it really helps readability if they stay multiline. See [object lists], [nested configs], [stylesheets] and [keyed methods], for example. We haven’t been able to find a good rule for all those cases, so by default Prettier keeps objects multi-line if there’s a newline between the `{` and the first key in the original source code. Consequently, long single-line objects are automatically expanded, but short multi-line objects are never collapsed.

You can disable this conditional behavior with the [`objectWrap`](options.md#object-wrap) option.

**Tip:** If you have a multi-line object that you’d like to join up into a single line:

```js
const user = {
  name: "John Doe",
  age: 30,
};
```

…all you need to do is remove the newline after `{`:

<!-- prettier-ignore -->
```js
const user = {  name: "John Doe",
  age: 30
};
```

…and then run Prettier:

```js
const user = { name: "John Doe", age: 30 };
```

And if you’d like to go multi-line again, add in a newline after `{`:

<!-- prettier-ignore -->
```js
const user = {
 name: "John Doe", age: 30 };
```

…and run Prettier:

```js
const user = {
  name: "John Doe",
  age: 30,
};
```

[object lists]: https://github.com/prettier/prettier/issues/74#issue-199965534
[nested configs]: https://github.com/prettier/prettier/issues/88#issuecomment-275448346
[stylesheets]: https://github.com/prettier/prettier/issues/74#issuecomment-275262094
[keyed methods]: https://github.com/prettier/prettier/pull/495#issuecomment-275745434

:::note[A note on formatting reversibility]

The semi-manual formatting for object literals is in fact a workaround, not a feature. It was implemented only because at the time a good heuristic wasn’t found and an urgent fix was needed. However, as a general strategy, Prettier avoids _non-reversible_ formatting like that, so the team is still looking for heuristics that would allow either to remove this behavior completely or at least to reduce the number of situations where it’s applied.

What does **reversible** mean? Once an object literal becomes multiline, Prettier won’t collapse it back. If in Prettier-formatted code, we add a property to an object literal, run Prettier, then change our mind, remove the added property, and then run Prettier again, we might end up with a formatting not identical to the initial one. This useless change might even get included in a commit, which is exactly the kind of situation Prettier was created to prevent.

:::

### Decorators

Just like with objects, decorators are used for a lot of different things. Sometimes it makes sense to write decorators _above_ the line they're decorating, sometimes it’s nicer if they're on the _same_ line. We haven’t been able to find a good rule for this, so Prettier keeps your decorator positioned like you wrote them (if they fit on the line). This isn’t ideal, but a pragmatic solution to a difficult problem.

```ts
@Component({
  selector: "hero-button",
  template: `<button>{{ label }}</button>`,
})
class HeroButtonComponent {
  // These decorators were written inline and fit on the line so they stay
  // inline.
  @Output() change = new EventEmitter();
  @Input() label: string;

  // These were written multiline, so they stay multiline.
  @readonly
  @nonenumerable
  NODE_TYPE: 2;
}
```

There’s one exception: classes. We don’t think it ever makes sense to inline the decorators for them, so they are always moved to their own line.

<!-- prettier-ignore -->
```ts
// Before running Prettier:
@observer class OrderLine {
  @observable price: number = 0;
}
```

```ts
// After running Prettier:
@observer
class OrderLine {
  @observable price: number = 0;
}
```

Note: Prettier 1.14.x and older tried to automatically move your decorators, so if you've run an older Prettier version on your code you might need to manually join up some decorators here and there to avoid inconsistencies:

```ts
@observer
class OrderLine {
  @observable price: number = 0;
  @observable
  amount: number = 0;
}
```

### Template literals

Template literals can contain interpolations. Deciding whether it's appropriate to insert a linebreak within an interpolation unfortunately depends on the semantic content of the template - for example, introducing a linebreak in the middle of a natural-language sentence is usually undesirable. Since Prettier doesn't have enough information to make this decision itself, it uses a heuristic similar to that used for objects: it will only split an interpolation expression across multiple lines if there was already a linebreak within that interpolation.

This means that a literal like the following will not be broken onto multiple lines, even if it exceeds the print width:

<!-- prettier-ignore -->
```js
`this is a long message which contains an interpolation: ${format(data)} <- like this`;
```

If you want Prettier to split up an interpolation, you'll need to ensure there's a linebreak somewhere within the `${...}`. Otherwise it will keep everything on a single line, no matter how long it is.

The team would prefer not to depend on the original formatting in this way, but it's the best heuristic we have at the moment.

### Semicolons

This is about using the [noSemi](options.md#semicolons) option.

Consider this piece of code:

<!-- prettier-ignore -->
```js
if (shouldAddLines) {
  [-1, 1].forEach(delta => addLine(delta * 20))
}
```

While the above code works just fine without semicolons, Prettier actually turns it into:

<!-- prettier-ignore -->
```js
if (shouldAddLines) {
  ;[-1, 1].forEach(delta => addLine(delta * 20))
}
```

This is to help you avoid mistakes. Imagine Prettier _not_ inserting that semicolon and adding this line:

```diff
 if (shouldAddLines) {
+  console.log('Do we even get here??')
   [-1, 1].forEach(delta => addLine(delta * 20))
 }
```

Oops! The above actually means:

<!-- prettier-ignore -->
```js
if (shouldAddLines) {
  console.log('Do we even get here??')[-1, 1].forEach(delta => addLine(delta * 20))
}
```

With a semicolon in front of that `[` such issues never happen. It makes the line independent of other lines so you can move and add lines without having to think about ASI rules.

This practice is also common in [standard] which uses a semicolon-free style.

Note that if your program currently has a semicolon-related bug in it, Prettier _will not_ auto-fix the bug for you. Remember, Prettier only reformats code, it does not change the behavior of the code. Take this buggy piece of code as an example, where the developer forgot to place a semicolon before the `(`:

<!-- prettier-ignore -->
```js
console.log('Running a background task')
(async () => {
  await doBackgroundWork()
})()
```

If you feed this into Prettier, it will not alter the behavior of this code, instead, it will reformat it in a way that shows how this code will actually behave when ran.

```js
console.log("Running a background task")(async () => {
  await doBackgroundWork();
})();
```

[standard]: https://standardjs.com/rules.html#semicolons

### Print width

The [printWidth](options.md#print-width) option is more of a guideline to Prettier than a hard rule. It is not the upper allowed line length limit. It is a way to say to Prettier roughly how long you’d like lines to be. Prettier will make both shorter and longer lines, but generally strive to meet the specified print width.

There are some edge cases, such as really long string literals, regexps, comments and variable names, which cannot be broken across lines (without using code transforms which [Prettier doesn’t do](#what-prettier-is-not-concerned-about)). Or if you nest your code 50 levels deep your lines are of course going to be mostly indentation :)

Apart from that, there are a few cases where Prettier intentionally exceeds the print width.

#### Imports

Prettier can break long `import` statements across several lines:

```js
import {
  CollectionDashboard,
  DashboardPlaceholder,
} from "../components/collections/collection-dashboard/main";
```

The following example doesn’t fit within the print width, but Prettier prints it in a single line anyway:

```js
import { CollectionDashboard } from "../components/collections/collection-dashboard/main";
```

This might be unexpected by some, but we do it this way since it was a common request to keep `import`s with single elements in a single line. The same applies for `require` calls.

#### Testing functions

Another common request was to keep lengthy test descriptions in one line, even if it gets too long. In such cases, wrapping the arguments to new lines doesn’t help much.

```js
describe("NodeRegistry", () => {
  it("makes no request if there are no nodes to prefetch, even if the cache is stale", async () => {
    // The above line exceeds the print width but stayed on one line anyway.
  });
});
```

Prettier has special cases for common testing framework functions such as `describe`, `it` and `test`.

### JSX

Prettier prints things a little differently compared to other JS when JSX is involved:

```jsx
function greet(user) {
  return user
    ? `Welcome back, ${user.name}!`
    : "Greetings, traveler! Sign up today!";
}

function Greet({ user }) {
  return (
    <div>
      {user ? (
        <p>Welcome back, {user.name}!</p>
      ) : (
        <p>Greetings, traveler! Sign up today!</p>
      )}
    </div>
  );
}
```

There are two reasons.

First off, lots of people already wrapped their JSX in parentheses, especially in `return` statements. Prettier follows this common style.

Secondly, [the alternate formatting makes it easier to edit the JSX](https://github.com/prettier/prettier/issues/2208). It is easy to leave a semicolon behind. As opposed to normal JS, a leftover semicolon in JSX can end up as plain text showing on your page.

```jsx
<div>
  <p>Greetings, traveler! Sign up today!</p>; {/* <-- Oops! */}
</div>
```

### Comments

When it comes to the _content_ of comments, Prettier can’t do much really. Comments can contain everything from prose to commented out code and ASCII diagrams. Since they can contain anything, Prettier can’t know how to format or wrap them. So they are left as-is. The only exception to this are JSDoc-style comments (block comments where every line starts with a `*`), which Prettier can fix the indentation of.

Then there’s the question of _where_ to put the comments. Turns out this is a really difficult problem. Prettier tries its best to keep your comments roughly where they were, but it’s no easy task because comments can be placed almost anywhere.

Generally, you get the best results when placing comments **on their own lines,** instead of at the end of lines. Prefer `// eslint-disable-next-line` over `// eslint-disable-line`.

Note that “magic comments” such as `eslint-disable-next-line` and `$FlowFixMe` might sometimes need to be manually moved due to Prettier breaking an expression into multiple lines.

Imagine this piece of code:

```js
// eslint-disable-next-line no-eval
const result = safeToEval ? eval(input) : fallback(input);
```

Then you need to add another condition:

<!-- prettier-ignore -->
```js
// eslint-disable-next-line no-eval
const result = safeToEval && settings.allowNativeEval ? eval(input) : fallback(input);
```

Prettier will turn the above into:

```js
// eslint-disable-next-line no-eval
const result =
  safeToEval && settings.allowNativeEval ? eval(input) : fallback(input);
```

Which means that the `eslint-disable-next-line` comment is no longer effective. In this case you need to move the comment:

```js
const result =
  // eslint-disable-next-line no-eval
  safeToEval && settings.allowNativeEval ? eval(input) : fallback(input);
```

If possible, prefer comments that operate on line ranges (e.g. `eslint-disable` and `eslint-enable`) or on the statement level (e.g. `/* istanbul ignore next */`), they are even safer. It’s possible to disallow using `eslint-disable-line` and `eslint-disable-next-line` comments using [`eslint-plugin-eslint-comments`](https://github.com/mysticatea/eslint-plugin-eslint-comments).

## Disclaimer about non-standard syntax

Prettier is often able to recognize and format non-standard syntax such as ECMAScript early-stage proposals and Markdown syntax extensions not defined by any specification. The support for such syntax is considered best-effort and experimental. Incompatibilities may be introduced in any release and should not be viewed as breaking changes.

## Disclaimer about machine-generated files

Some files, like `package.json` or `composer.lock`, are machine-generated and regularly updated by the package manager. If Prettier were to use the same JSON formatting rules as with other files, it would regularly conflict with these other tools. To avoid this inconvenience, Prettier will use a formatter based on `JSON.stringify` on such files instead. You may notice these differences, such as the removal of vertical whitespace, but this is an intended behavior.

## What Prettier is _not_ concerned about

Prettier only _prints_ code. It does not transform it. This is to limit the scope of Prettier. Let’s focus on the printing and do it really well!

Here are a few examples of things that are out of scope for Prettier:

- Turning single- or double-quoted strings into template literals or vice versa.
- Using `+` to break long string literals into parts that fit the print width.
- Adding/removing `{}` and `return` where they are optional.
- Turning `?:` into `if`-`else` statements.
- Sorting/moving imports, object keys, class members, JSX keys, CSS properties or anything else. Apart from being a _transform_ rather than just printing (as mentioned above), sorting is potentially unsafe because of side effects (for imports, as an example) and makes it difficult to verify the most important [correctness](#correctness) goal.


---


### Related Projects

---
id: related-projects
title: Related Projects
---

## ESLint Integrations

- [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) turns off all ESLint rules that are unnecessary or might conflict with Prettier
- [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier) runs Prettier as an ESLint rule and reports differences as individual ESLint issues
- [prettier-eslint](https://github.com/prettier/prettier-eslint) passes `prettier` output to `eslint --fix`
- [prettier-standard](https://github.com/sheerun/prettier-standard) uses `prettierx` and `prettier-eslint` to format code with `standard` rules

## stylelint Integrations

- [stylelint-config-prettier](https://github.com/prettier/stylelint-config-prettier) turns off all rules that are unnecessary or might conflict with Prettier.
- [stylelint-prettier](https://github.com/prettier/stylelint-prettier) runs Prettier as a stylelint rule and reports differences as individual stylelint issues
- [prettier-stylelint](https://github.com/hugomrdias/prettier-stylelint) passes `prettier` output to `stylelint --fix`

## Forks

- [prettierx](https://github.com/brodybits/prettierx) less opinionated fork of Prettier

## Misc

- [parallel-prettier](https://github.com/microsoft/parallel-prettier) is an alternative CLI that formats files in parallel to speed up large projects
- [prettier_d](https://github.com/josephfrazier/prettier_d.js) runs Prettier as a server to avoid Node.js startup delay
- [pretty-quick](https://github.com/azz/pretty-quick) formats changed files with Prettier
- [rollup-plugin-prettier](https://github.com/mjeanroy/rollup-plugin-prettier) allows you to use Prettier with Rollup
- [jest-runner-prettier](https://github.com/keplersj/jest-runner-prettier) is Prettier as a Jest runner
- [prettier-chrome](https://github.com/u3u/prettier-chrome) is an extension that runs Prettier in the browser
- [spotless](https://github.com/diffplug/spotless) lets you run prettier from [gradle](https://github.com/diffplug/spotless/tree/main/plugin-gradle#prettier) or [maven](https://github.com/diffplug/spotless/tree/main/plugin-maven#prettier).
- [csharpier](https://github.com/belav/csharpier) is a port of Prettier for C#
- [Prettier](https://github.com/jaywcjlove/Prettier) is a Swift version based on Prettier
- [reviewdog-action-prettier](https://github.com/EPMatt/reviewdog-action-prettier) runs Prettier in GitHub Actions CI/CD workflows
- [monaco-prettier](https://github.com/remcohaszing/monaco-prettier) integrates Prettier into [Monaco editor](https://microsoft.github.io/monaco-editor/)


---


### Sharing configurations

---
id: sharing-configurations
title: Sharing configurations
---

import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";

In case you have many different projects, it can be helpful to have a **shared configuration** which can be used in all of them, instead of copy-pasting the same config for every project.

This page explains how to create, publish and consume a shareable config.

## Creating a Shareable Config

Sharable configs are just [npm packages](https://docs.npmjs.com/about-packages-and-modules#about-packages) that export a single [prettier config file](./configuration.md).

Before we start, make sure you have:

- An account for [npmjs.com](https://www.npmjs.com/) to publish the package
- Basic understating about [how to create a Node.js module](https://docs.npmjs.com/creating-node-js-modules)

First, create a new package. We recommend creating a [scoped package](https://docs.npmjs.com/cli/v10/using-npm/scope) with the name `@username/prettier-config`.

A minimal package should have at least two files. A `package.json` for the package configuration and an `index.js` which holds the shared prettier configuration object:

```text
prettier-config/
├── index.js
└── package.json
```

Example `package.json`:

```json
{
  "name": "@username/prettier-config",
  "version": "1.0.0",
  "description": "My personal Prettier config",
  "type": "module",
  "exports": "./index.js",
  "license": "MIT",
  "publishConfig": {
    "access": "public"
  },
  "peerDependencies": {
    "prettier": ">=3.0.0"
  }
}
```

`index.js` is where you put the shared configuration. This file just exports a [regular prettier configuration](./configuration.md) with the same syntax and same options:

```js
const config = {
  trailingComma: "es5",
  tabWidth: 4,
  singleQuote: true,
};

export default config;
```

An example shared configuration repository is available [here](https://github.com/azz/prettier-config).

## Publishing a Shareable Config

Once you are ready, you can [publish your package to npm](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages#publishing-scoped-public-packages):

```bash
npm publish
```

## Using a Shareable Config

You first need to install your published configuration, for example:

<Tabs groupId="package-manager">
<TabItem value="npm">

```bash
npm install --save-dev @username/prettier-config
```

</TabItem>
<TabItem value="yarn">

```bash
yarn add --dev @username/prettier-config
```

</TabItem>
<TabItem value="pnpm">

```bash
pnpm add --save-dev @username/prettier-config
```

</TabItem>
<TabItem value="bun">

```bash
bun add --dev @username/prettier-config
```

</TabItem>
</Tabs>

Then, you can reference it in your `package.json`:

```json
{
  "name": "my-cool-library",
  "version": "1.0.0",
  "prettier": "@username/prettier-config"
}
```

If you don’t want to use `package.json`, you can use any of the supported extensions to export a string, e.g. `.prettierrc`:

```json
"@company/prettier-config"
```

### Extending a Sharable Config

To _extend_ the configuration to overwrite some properties from the shared configuration, import the file in a `.prettierrc.mjs` file and export the modifications, e.g:

```js
import usernamePrettierConfig from "@username/prettier-config";

/**
 * @see https://prettier.io/docs/configuration
 * @type {import("prettier").Config}
 */
const config = {
  ...usernamePrettierConfig,
  semi: false,
};

export default config;
```

## Other examples

### Using Type Annotation in the Shared Config

You can get type safety and autocomplete support in your shared configuration by using a `jsdoc` type annotation:

```js
/**
 * @type {import("prettier").Config}
 */
const config = {
  trailingComma: "es5",
  tabWidth: 4,
  semi: false,
  singleQuote: true,
};

export default config;
```

In order to make this work, you have to [install `prettier`](./install.md) for the project.

After that, your `package.json` file should look like this:

```diff
{
  "name": "@username/prettier-config",
  "version": "1.0.0",
  "description": "My personal Prettier config",
  "type": "module",
  "exports": "./index.js",
  "license": "MIT",
  "publishConfig": {
    "access": "public"
  },
  "peerDependencies": {
    "prettier": ">=3.0.0"
  },
+ "devDependencies": {
+   "prettier": "^3.3.3"
+ }
}
```

### Include Plugins in Shareable Configurations

In case you want to use [plugins](./plugins.md) in your shared configuration, you need to declare those plugins in the config file's `plugin` array and as `dependencies` in `package.json`:

```js
// index.js
const config = {
  singleQuote: true,
  plugins: ["prettier-plugin-xml"],
};

export default config;
```

```diff
// package.json
{
  "name": "@username/prettier-config",
  "version": "1.0.0",
  "description": "My personal Prettier config",
  "type": "module",
  "exports": "./index.js",
  "license": "MIT",
  "publishConfig": {
    "access": "public"
  },
+  "dependencies": {
+    "prettier-plugin-xml": "3.4.1"
+  },
  "peerDependencies": {
    "prettier": ">=3.0.0"
  }
}
```

An example repository can be found [here](https://github.com/kachkaev/routine-npm-packages/tree/bc3e658f88c0b41beb118c7a1b9b91ec647f8478/packages/prettier-config)

**Note:** You can use [`peerDependencies`](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#peerdependencies) instead of [`dependencies`](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#dependencies). To learn about their differences, you can read [this blog post from Domenic Denicola about peer dependencies](https://nodejs.org/en/blog/npm/peer-dependencies)


---


### Technical Details

---
id: technical-details
title: Technical Details
---

This printer is a fork of [recast](https://github.com/benjamn/recast)’s printer with its algorithm replaced by the one described by Wadler in "[A prettier printer](https://homepages.inf.ed.ac.uk/wadler/papers/prettier/prettier.pdf)". There still may be leftover code from recast that needs to be cleaned up.

The basic idea is that the printer takes an AST and returns an intermediate representation of the output, and the printer uses that to generate a string. The advantage is that the printer can "measure" the IR and see if the output is going to fit on a line, and break if not.

This means that most of the logic of printing an AST involves generating an abstract representation of the output involving certain commands. For example, `["(", line, arg, line, ")"]` would represent a concatenation of opening parens, an argument, and closing parens. But if that doesn’t fit on one line, the printer can break where `line` is specified.

The [Playground](https://prettier.io/playground) has a special mode for exploring how Prettier’s intermediate representation is printed. To get there, open the sidebar (the "Show options" button) and set the `parser` option to the special value `doc-explorer`.

More (rough) details can be found in [commands.md](https://github.com/prettier/prettier/blob/main/commands.md).


---


### Vim Setup

---
id: vim
title: Vim Setup
---

Vim users can install either [vim-prettier](https://github.com/prettier/vim-prettier), which is Prettier specific, or [Neoformat](https://github.com/sbdchd/neoformat) or [ALE](https://github.com/dense-analysis/ale) which are generalized lint/format engines with support for Prettier.

## [vim-prettier](https://github.com/prettier/vim-prettier)

See the [vim-prettier](https://github.com/prettier/vim-prettier) readme for installation and usage instructions.

## [Neoformat](https://github.com/sbdchd/neoformat)

The best way to install Neoformat is with your favorite plugin manager for Vim, such as [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'sbdchd/neoformat'
```

In order for Neoformat to use a project-local version of Prettier (i.e. to use `node_modules/.bin/prettier` instead of looking for `prettier` on `$PATH`), you must set the `neoformat_try_node_exe` option:

```vim
let g:neoformat_try_node_exe = 1
```

Run `:Neoformat` or `:Neoformat prettier` in a supported file to run Prettier.

To have Neoformat run Prettier on save:

```vim
autocmd BufWritePre *.js Neoformat
```

You can also make Vim format your code more frequently, by setting an `autocmd` for other events. Here are a couple of useful ones:

- `TextChanged`: after a change was made to the text in Normal mode
- `InsertLeave`: when leaving Insert mode

For example, you can format on both of the above events together with `BufWritePre` like this:

```vim
autocmd BufWritePre,TextChanged,InsertLeave *.js Neoformat
```

See `:help autocmd-events` in Vim for details.

It’s recommended to use a [config file](configuration.md), but you can also add options in your `.vimrc`:

```vim
autocmd FileType javascript setlocal formatprg=prettier\ --single-quote\ --trailing-comma\ es5
" Use formatprg when available
let g:neoformat_try_formatprg = 1
```

Each space in Prettier options should be escaped with `\`.

## [ALE](https://github.com/dense-analysis/ale)

ALE requires either Vim 8 or Neovim as ALE makes use of the asynchronous abilities that both Vim 8 and Neovim provide.

The best way to install ALE is with your favorite plugin manager for Vim, such as [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'dense-analysis/ale'
```

You can find further instructions on the [ALE repository](https://github.com/dense-analysis/ale#3-installation).

ALE will try to use Prettier installed locally before looking for a global installation.

Enable the Prettier fixer for the languages you use:

```vim
let g:ale_fixers = {
\   'javascript': ['prettier'],
\   'css': ['prettier'],
\}
```

ALE supports both _linters_ and _fixers_. If you don’t specify which _linters_ to run, **all available tools for all supported languages will be run,** and you might get a correctly formatted file with a bunch of lint errors. To disable this behavior you can tell ALE to run only linters you've explicitly configured (more info in the [FAQ](https://github.com/dense-analysis/ale/blob/ed8104b6ab10f63c78e49b60d2468ae2656250e9/README.md#faq-disable-linters)):

```vim
let g:ale_linters_explicit = 1
```

You can then run `:ALEFix` in a JavaScript or CSS file to run Prettier.

To have ALE run Prettier on save:

```vim
let g:ale_fix_on_save = 1
```

It’s recommended to use a [config file](configuration.md), but you can also add options in your `.vimrc`:

```vim
let g:ale_javascript_prettier_options = '--single-quote --trailing-comma all'
```

## [coc-prettier](https://github.com/neoclide/coc-prettier)

Prettier extension for [coc.nvim](https://github.com/neoclide/coc.nvim) which requires neovim or vim8.1.
Install coc.nvim with your favorite plugin manager, such as [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'neoclide/coc.nvim', {'branch': 'release'}
```

And install coc-prettier by command:

```vim
CocInstall coc-prettier
```

Setup `Prettier` command in your `init.vim` or `.vimrc`

```vim
command! -nargs=0 Prettier :call CocAction('runCommand', 'prettier.formatFile')
```

Update your `coc-settings.json` for languages that you want format on save.

```json
{
  "coc.preferences.formatOnSaveFiletypes": ["css", "markdown"]
}
```

[coc-prettier](https://github.com/neoclide/coc-prettier) have same configurations of [prettier-vscode](https://github.com/prettier/prettier-vscode), open `coc-settings.json` by `:CocConfig` to get autocompletion support.

## Running manually

If you want something really bare-bones, you can create a custom key binding. In this example, `gp` (mnemonic: "get pretty") is used to run prettier (with options) in the currently active buffer:

```vim
nnoremap gp :silent %!prettier --stdin-filepath %<CR>
```

Note that if there’s a syntax error in your code, the whole buffer will be replaced with an error message. You’ll need to press `u` to get your code back.

Another disadvantage of this approach is that the cursor position won’t be preserved.


---


### Watching For Changes

---
id: watching-files
title: Watching For Changes
---

You can have Prettier watch for changes from the command line by using [onchange](https://www.npmjs.com/package/onchange). For example:

```bash
npx onchange "**/*" -- npx prettier --write --ignore-unknown {{changed}}
```

Or add the following to your `package.json`:

```json
{
  "scripts": {
    "prettier-watch": "onchange \"**/*\" -- prettier --write --ignore-unknown {{changed}}"
  }
}
```


---


### WebStorm Setup

---
id: webstorm
title: WebStorm Setup
---

## JetBrains IDEs (WebStorm, IntelliJ IDEA, PyCharm, etc.)

WebStorm comes with built-in support for Prettier. If you’re using other JetBrains IDE like IntelliJ IDEA, PhpStorm, or PyCharm, make sure you have this [plugin](https://plugins.jetbrains.com/plugin/10456-prettier) installed and enabled in _Preferences / Settings | Plugins_.

First, you need to install and configure Prettier. You can find instructions on how to do it [here](https://www.jetbrains.com/help/webstorm/prettier.html#ws_prettier_install).

Once it’s done, you can do a few things in your IDE. You can use the **Reformat with Prettier** action (_Opt+Shift+Cmd+P_ on macOS or _Alt+Shift+Ctrl+P_ on Windows and Linux) to format the selected code, a file, or a whole directory.

You can also configure WebStorm to run Prettier on save (_Cmd+S/Ctrl+S_) or use it as the default formatter (_Opt+Cmd+L/Ctrl+Alt+L_). For this, open _Preferences / Settings | Languages & Frameworks | JavaScript | Prettier_ and tick the corresponding checkbox: **On save** and/or **On ‘Reformat Code’** action.

![Example](/images/webstorm/prettier-settings.png)

By default, WebStorm will apply formatting to all _.js, .ts, .jsx_, and _.tsx_ files that you’ve edited in your project. To apply the formatting to other file types, or to limit formatting to files located only in specific directories, you can customize the default configuration by using [glob patterns](https://github.com/isaacs/node-glob).

For more information, see [WebStorm online help](https://www.jetbrains.com/help/webstorm/prettier.html).


---


### Why Prettier?

---
id: why-prettier
title: Why Prettier?
---

## Building and enforcing a style guide

By far the biggest reason for adopting Prettier is to stop all the on-going debates over styles. [It is generally accepted that having a common style guide is valuable for a project and team](https://www.smashingmagazine.com/2012/10/why-coding-style-matters/) but getting there is a very painful and unrewarding process. People get very emotional around particular ways of writing code and nobody likes spending time writing and receiving nits.

So why choose the “Prettier style guide” over any other random style guide? Because Prettier is the only “style guide” that is fully automatic. Even if Prettier does not format all code 100% the way you’d like, it’s worth the “sacrifice” given the unique benefits of Prettier, don’t you think?

- “We want to free mental threads and end discussions around style. While sometimes fruitful, these discussions are for the most part wasteful.”
- “Literally had an engineer go through a huge effort of cleaning up all of our code because we were debating ternary style for the longest time and were inconsistent about it. It was dumb, but it was a weird on-going “great debate” that wasted lots of little back and forth bits. It’s far easier for us all to agree now: just run Prettier, and go with that style.”
- “Getting tired telling people how to style their product code.”
- “Our top reason was to stop wasting our time debating style nits.”
- “Having a githook set up has reduced the amount of style issues in PRs that result in broken builds due to ESLint rules or things I have to nit-pick or clean up later.”
- “I don’t want anybody to nitpick any other person ever again.”
- “It reminds me of how Steve Jobs used to wear the same clothes every day because he has a million decisions to make and he didn’t want to be bothered to make trivial ones like picking out clothes. I think Prettier is like that.”

## Helping Newcomers

Prettier is usually introduced by people with experience in the current codebase and JavaScript but the people that disproportionally benefit from it are newcomers to the codebase. One may think that it’s only useful for people with very limited programming experience, but we've seen it quicken the ramp up time from experienced engineers joining the company, as they likely used a different coding style before, and developers coming from a different programming language.

- “My motivations for using Prettier are: appearing that I know how to write JavaScript well.”
- “I always put spaces in the wrong place, now I don’t have to worry about it anymore.”
- “When you're a beginner you're making a lot of mistakes caused by the syntax. Thanks to Prettier, you can reduce these mistakes and save a lot of time to focus on what really matters.”
- “As a teacher, I will also tell to my students to install Prettier to help them to learn the JS syntax and have readable files.”

## Writing code

What usually happens once people are using Prettier is that they realize that they actually spend a lot of time and mental energy formatting their code. With Prettier editor integration, you can just press that magic key binding and poof, the code is formatted. This is an eye opening experience if anything else.

- “I want to write code. Not spend cycles on formatting.”
- “It removed 5% that sucks in our daily life - aka formatting”
- “We're in 2017 and it’s still painful to break a call into multiple lines when you happen to add an argument that makes it go over the 80 columns limit :(“

## Easy to adopt

We've worked very hard to use the least controversial coding styles, went through many rounds of fixing all the edge cases and polished the getting started experience. When you're ready to push Prettier into your codebase, not only should it be painless for you to do it technically but the newly formatted codebase should not generate major controversy and be accepted painlessly by your co-workers.

- “It’s low overhead. We were able to throw Prettier at very different kinds of repos without much work.”
- “It’s been mostly bug free. Had there been major styling issues during the course of implementation we would have been wary about throwing this at our JS codebase. I’m happy to say that’s not the case.”
- “Everyone runs it as part of their pre commit scripts, a couple of us use the editor on save extensions as well.”
- “It’s fast, against one of our larger JS codebases we were able to run Prettier in under 13 seconds.”
- “The biggest benefit for Prettier for us was being able to format the entire code base at once.”

## Clean up an existing codebase

Since coming up with a coding style and enforcing it is a big undertaking, it often slips through the cracks and you are left working on inconsistent codebases. Running Prettier in this case is a quick win, the codebase is now uniform and easier to read without spending hardly any time.

- “Take a look at the code :) I just need to restore sanity.”
- “We inherited a ~2000 module ES6 code base, developed by 20 different developers over 18 months, in a global team. Felt like such a win without much research.”

## Ride the hype train

Purely technical aspects of the projects aren’t the only thing people look into when choosing to adopt Prettier. Who built and uses it and how quickly it spreads through the community has a non-trivial impact.

- “The amazing thing, for me, is: 1) Announced 2 months ago. 2) Already adopted by, it seems, every major JS project. 3) 7000 stars, 100,000 npm downloads/mo”
- “Was built by the same people as React & React Native.”
- “I like to be part of the hot new things.”
- “Because soon enough people are gonna ask for it.”