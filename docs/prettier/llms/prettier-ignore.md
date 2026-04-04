# prettier-ignore
key  : value
hello: world
```

## GraphQL

```graphql
{
  # prettier-ignore
  addReaction(input:{superLongInputFieldName:"MDU6SXNzdWUyMzEzOTE1NTE=",content:HOORAY}) {
    reaction {content}
  }
}
```

## Handlebars

<!-- prettier-ignore -->
```hbs
{{! prettier-ignore }}
<div>
  "hello! my parent was ignored"
  {{#my-crazy-component     "shall"     be="preserved"}}
    <This
      is  =  "also preserved as is"
    />
  {{/my-crazy-component}}
</div>
```

## Command Line File Patterns

For one-off commands, when you want to exclude some files without adding them to `.prettierignore`, negative patterns can come in handy:

```bash
prettier . "!**/*.{js,jsx,vue}" --write
```

See [fast-glob](https://prettier.io/docs/cli#file-patterns) to learn more about advanced glob syntax.


---


### What is Prettier?

---
id: index
title: What is Prettier?
---

Prettier is an opinionated code formatter with support for:

- JavaScript (including experimental features)
- [JSX](https://facebook.github.io/jsx/)
- [Angular](https://angular.dev/)
- [Vue](https://vuejs.org/)
- [Flow](https://flow.org/)
- [TypeScript](https://www.typescriptlang.org/)
- CSS, [Less](https://lesscss.org/), and [SCSS](https://sass-lang.com)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [Ember/Handlebars](https://handlebarsjs.com/)
- [JSON](https://json.org/)
- [GraphQL](https://graphql.org/)
- [Markdown](https://commonmark.org/), including [GFM](https://github.github.com/gfm/) and [MDX v1](https://mdxjs.com/)
- [YAML](https://yaml.org/)

It removes all original styling[\*](#footnotes) and ensures that all outputted code conforms to a consistent style. (See this [blog post](https://jlongster.com/A-Prettier-Formatter))

Prettier takes your code and reprints it from scratch by taking the line length into account.

For example, take the following code:

```js
foo(arg1, arg2, arg3, arg4);
```

It fits in a single line so it’s going to stay as is. However, we've all run into this situation:

<!-- prettier-ignore -->
```js
foo(reallyLongArg(), omgSoManyParameters(), IShouldRefactorThis(), isThereSeriouslyAnotherOne());
```

Suddenly our previous format for calling function breaks down because this is too long. Prettier is going to do the painstaking work of reprinting it like that for you:

```js
foo(
  reallyLongArg(),
  omgSoManyParameters(),
  IShouldRefactorThis(),
  isThereSeriouslyAnotherOne(),
);
```

Prettier enforces a consistent code **style** (i.e. code formatting that won’t affect the AST) across your entire codebase because it disregards the original styling[\*](#footnotes) by parsing it away and re-printing the parsed AST with its own rules that take the maximum line length into account, wrapping code when necessary.

If you want to learn more, these two conference talks are great introductions:

[![A Prettier Printer by James Long on React Conf 2017](/images/youtube-cover/a-prettier-printer-by-james-long-on-react-conf-2017.png)](https://www.youtube.com/watch?v=hkfBvpEfWdA)

[![JavaScript Code Formatting by Christopher Chedeau on React London 2017](/images/youtube-cover/javascript-code-formatting-by-christopher-chedeau-on-react-london-2017.png)](https://www.youtube.com/watch?v=0Q4kUNx85_4)

#### Footnotes

\* _Well actually, some original styling is preserved when practical—see [empty lines](rationale.md#empty-lines) and [multi-line objects](rationale.md#multi-line-objects)._


---


### Install

---
id: install
title: Install
---

import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";

First, install Prettier locally:

<Tabs groupId="package-manager">
<TabItem value="npm">

```bash
npm install --save-dev --save-exact prettier
```

</TabItem>
<TabItem value="yarn">

```bash
yarn add --dev --exact prettier
```

</TabItem>
<TabItem value="pnpm">

```bash
pnpm add --save-dev --save-exact prettier
```

</TabItem>
<TabItem value="bun">

```bash
bun add --dev --exact prettier
```

</TabItem>
</Tabs>

Then, create an empty config file to let editors and other tools know you are using Prettier:

<!--
Note:
- `echo "{}" > .prettierrc` would result in `"{}"<SPACE>` on Windows.
- `echo {}> .prettierrc` would result the file in UTF-16LE encoding in PowerShell.
The below version works in cmd.exe, bash, zsh, fish, PowerShell.
-->

```bash
node --eval "fs.writeFileSync('.prettierrc','{}\n')"
```

Next, create a [.prettierignore](ignore.md) file to let the Prettier CLI and editors know which files to _not_ format. Here’s an example:

```bash
node --eval "fs.writeFileSync('.prettierignore','# Ignore artifacts:\nbuild\ncoverage\n')"
```

:::tip

Prettier will follow rules specified in .gitignore if it exists in the same directory from which it is run. You can also base your .prettierignore on .eslintignore (if you have one).

:::

:::tip[Another tip]

If your project isn’t ready to format, say, HTML files yet, add `*.html`.

:::

Now, format all files with Prettier:

<Tabs groupId="package-manager">
<TabItem value="npm">

```bash
npx prettier . --write
```

:::info

What is that `npx` thing? `npx` ships with `npm` and lets you run locally installed tools. We’ll leave off the `npx` part for brevity throughout the rest of this file!

:::

:::warning

If you forget to install Prettier first, `npx` will temporarily download the latest version. That’s not a good idea when using Prettier, because we change how code is formatted in each release! It’s important to have a locked down version of Prettier in your `package.json`. And it’s faster, too.

:::

</TabItem>
<TabItem value="yarn">

```bash
yarn exec prettier . --write
```

:::info

What is `yarn exec` doing at the start? `yarn exec prettier` runs the locally installed version of Prettier. We’ll leave off the `yarn exec` part for brevity throughout the rest of this file!

:::

</TabItem>
<TabItem value="pnpm">

```bash
pnpm exec prettier . --write
```

:::info

What is `pnpm exec` doing at the start? `pnpm exec prettier` runs the locally installed version of Prettier. We’ll leave off the `pnpm exec` part for brevity throughout the rest of this file!

:::

</TabItem>
<TabItem value="bun">

```bash
bunx prettier . --write
```

:::info

What is `bunx` doing at the start? `bunx prettier` runs the locally installed version of Prettier. We’ll leave off the `bunx` part for brevity throughout the rest of this file!

:::

:::warning

If you forget to install Prettier first, `bunx` will temporarily download the latest version. That’s not a good idea when using Prettier, because we change how code is formatted in each release! It’s important to have a locked down version of Prettier in your `package.json`. And it’s faster, too.

:::

</TabItem>
</Tabs>

`prettier --write .` is great for formatting everything, but for a big project it might take a little while. You may run `prettier --write app/` to format a certain directory, or `prettier --write app/components/Button.js` to format a certain file. Or use a _glob_ like `prettier --write "app/**/*.test.js"` to format all tests in a directory (see [fast-glob](https://github.com/mrmlnc/fast-glob#pattern-syntax) for supported glob syntax).

If you have a CI setup, run the following as part of it to make sure that everyone runs Prettier. This avoids merge conflicts and other collaboration issues!

```bash
npx prettier . --check
```

`--check` is like `--write`, but only checks that files are already formatted, rather than overwriting them. `prettier --write` and `prettier --check` are the most common ways to run Prettier.

## Set up your editor

Formatting from the command line is a good way to get started, but you get the most from Prettier by running it from your editor, either via a keyboard shortcut or automatically whenever you save a file. When a line has gotten so long while coding that it won’t fit your screen, just hit a key and watch it magically be wrapped into multiple lines! Or when you paste some code and the indentation gets all messed up, let Prettier fix it up for you without leaving your editor.

See [Editor Integration](editors.md) for how to set up your editor. If your editor does not support Prettier, you can instead [run Prettier with a file watcher](watching-files.md).

:::note

Don’t skip the regular local install! Editor plugins will pick up your local version of Prettier, making sure you use the correct version in every project. (You wouldn’t want your editor accidentally causing lots of changes because it’s using a newer version of Prettier than your project!)

And being able to run Prettier from the command line is still a good fallback, and needed for CI setups.

:::

## ESLint (and other linters)

If you use ESLint, install [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier#installation) to make ESLint and Prettier play nice with each other. It turns off all ESLint rules that are unnecessary or might conflict with Prettier. There’s a similar config for Stylelint: [stylelint-config-prettier](https://github.com/prettier/stylelint-config-prettier)

(See [Prettier vs. Linters](comparison.md) to learn more about formatting vs linting, [Integrating with Linters](integrating-with-linters.md) for more in-depth information on configuring your linters, and [Related projects](related-projects.md) for even more integration possibilities, if needed.)

## Git hooks

In addition to running Prettier from the command line (`prettier --write`), checking formatting in CI, and running Prettier from your editor, many people like to run Prettier as a pre-commit hook as well. This makes sure all your commits are formatted, without having to wait for your CI build to finish.

For example, you can do the following to have Prettier run before each commit:

1. Install [husky](https://github.com/typicode/husky) and [lint-staged](https://github.com/okonet/lint-staged):

<Tabs groupId="package-manager">
<TabItem value="npm">

```bash
npm install --save-dev husky lint-staged
npx husky init
node --eval "fs.writeFileSync('.husky/pre-commit','npx lint-staged\n')"
```

</TabItem>
<TabItem value="yarn">

```bash
yarn add --dev husky lint-staged
npx husky init
node --eval "fs.writeFileSync('.husky/pre-commit','yarn lint-staged\n')"
```

:::note

If you use Yarn 2, see https://typicode.github.io/husky/#/?id=yarn-2

:::

</TabItem>
<TabItem value="pnpm">

```bash
pnpm add --save-dev husky lint-staged
pnpm exec husky init
node --eval "fs.writeFileSync('.husky/pre-commit','pnpm exec lint-staged\n')"
```

</TabItem>
<TabItem value="bun">

```bash
bun add --dev husky lint-staged
bunx husky init
bun --eval "fs.writeFileSync('.husky/pre-commit','bunx lint-staged\n')"
```

</TabItem>
</Tabs>

2. Add the following to your `package.json`:

```json
{
  "lint-staged": {
    "**/*": "prettier --write --ignore-unknown"
  }
}
```

:::note

If you use ESLint, make sure lint-staged runs it before Prettier, not after.

:::

See [Pre-commit Hook](precommit.md) for more information.

## Summary

To summarize, we have learned to:

- Install an exact version of Prettier locally in your project. This makes sure that everyone in the project gets the exact same version of Prettier. Even a patch release of Prettier can result in slightly different formatting, so you wouldn’t want different team members using different versions and formatting each other’s changes back and forth.
- Add a `.prettierrc` to let your editor know that you are using Prettier.
- Add a `.prettierignore` to let your editor know which files _not_ to touch, as well as for being able to run `prettier --write .` to format the entire project (without mangling files you don’t want, or choking on generated files).
- Run `prettier --check .` in CI to make sure that your project stays formatted.
- Run Prettier from your editor for the best experience.
- Use [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) to make Prettier and ESLint play nice together.
- Set up a pre-commit hook to make sure that every commit is formatted.


---


### Integrating with Linters

---
id: integrating-with-linters
title: Integrating with Linters
---

Linters usually contain not only code quality rules, but also stylistic rules. Most stylistic rules are unnecessary when using Prettier, but worse – they might conflict with Prettier! Use Prettier for code formatting concerns, and linters for code-quality concerns, as outlined in [Prettier vs. Linters](comparison.md).

Luckily it’s easy to turn off rules that conflict or are unnecessary with Prettier, by using these pre-made configs:

- [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)

Check out the above links for instructions on how to install and set things up.

## Notes

When searching for both Prettier and your linter on the Internet you’ll probably find more related projects. These are **generally not recommended,** but can be useful in certain circumstances.

First, we have plugins that let you run Prettier as if it was a linter rule:

- [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier)
- [stylelint-prettier](https://github.com/prettier/stylelint-prettier)

These plugins were especially useful when Prettier was new. By running Prettier inside your linters, you didn’t have to set up any new infrastructure and you could re-use your editor integrations for the linters. But these days you can run `prettier --check .` and most editors have Prettier support.

The downsides of those plugins are:

- You end up with a lot of red squiggly lines in your editor, which gets annoying. Prettier is supposed to make you forget about formatting – and not be in your face about it!
- They are slower than running Prettier directly.
- They’re yet one layer of indirection where things may break.

Finally, we have tools that run `prettier` and then immediately lint files by running, for example, `eslint --fix` on them.

- [prettier-eslint](https://github.com/prettier/prettier-eslint)
- [prettier-stylelint](https://github.com/hugomrdias/prettier-stylelint)

Those are useful if some aspect of Prettier’s output makes Prettier completely unusable to you. Then you can have for example `eslint --fix` fix that up for you. The downside is that these tools are much slower than just running Prettier.


---


### Option Philosophy

---
id: option-philosophy
title: Option Philosophy
---

:::info

Prettier has a few options because of history. **But we won’t add more of them.**

Read on to learn more.

:::

Prettier is not a kitchen-sink code formatter that attempts to print your code in any way you wish. It is _opinionated._ Quoting the [Why Prettier?](why-prettier.md) page:

> By far the biggest reason for adopting Prettier is to stop all the ongoing debates over styles.

Yet the more options Prettier has, the further from the above goal it gets. **The debates over styles just turn into debates over which Prettier options to use.** Formatting wars break out with renewed vigour: “Which option values are better? Why? Did we make the right choices?”

And it’s not the only cost options have. To learn more about their downsides, see the [issue about resisting adding configuration](https://github.com/prettier/prettier/issues/40), which has more 👍s than any option request issue.

So why are there any options at all?

- A few were added during Prettier’s infancy to make it take off at all. 🚀
- A couple were added after “great demand.” 🤔
- Some were added for compatibility reasons. 👍

Options that are easier to motivate include:

- `--trailing-comma es5` lets you use trailing commas in most environments without having to transpile (trailing function commas were added in ES2017).
- `--prose-wrap` is important to support all quirky Markdown renderers in the wild.
- `--html-whitespace-sensitivity` is needed due to the unfortunate whitespace rules of HTML.
- `--end-of-line` makes it easier for teams to keep CRLFs out of their git repositories.
- `--quote-props` is important for advanced usage of the Google Closure Compiler.

But other options are harder to motivate in hindsight: `--arrow-parens`, `--jsx-single-quote`, `--bracket-same-line` and `--no-bracket-spacing` are not the type of options we’re happy to have. They cause a lot of [bike-shedding](https://en.wikipedia.org/wiki/Law_of_triviality) in teams, and we’re sorry for that. Difficult to remove now, these options exist as a historical artifact and should not motivate adding more options (“If _those_ options exist, why can’t this one?”).

For a long time, we left option requests open in order to let discussions play out and collect feedback. What we’ve learned during those years is that it’s really hard to measure demand. Prettier has grown a lot in usage. What was “great demand” back in the day is not as much today. GitHub reactions and Twitter polls became unrepresentative. What about all silent users? It looked easy to add “just one more” option. But where should we have stopped? When is one too many? Even after adding “that one final option”, there would always be a “top issue” in the issue tracker.

However, the time to stop has come. Now that Prettier is mature enough and we see it adopted by so many organizations and projects, the research phase is over. We have enough confidence to conclude that Prettier reached a point where the set of options should be “frozen”. **Option requests aren’t accepted anymore.** We’re thankful to everyone who participated in this difficult journey.

Please note that as option requests are out of scope for Prettier, they will be closed without discussion. The same applies to requests to preserve elements of input formatting (e.g. line breaks) since that’s nothing else but an option in disguise with all the downsides of “real” options. There may be situations where adding an option can’t be avoided because of technical necessity (e.g. compatibility), but for formatting-related options, this is final.


---


### Options

---
id: options
title: Options
---

Prettier ships with a handful of format options.

**To learn more about Prettier’s stance on options – see the [Option Philosophy](option-philosophy.md).**

If you change any options, it’s recommended to do it via a [configuration file](configuration.md). This way the Prettier CLI, [editor integrations](editors.md) and other tooling knows what options you use.

## Experimental Ternaries

Try prettier's [new ternary formatting](https://github.com/prettier/prettier/pull/13183) before it becomes the default behavior.

Valid options:

- `true` - Use curious ternaries, with the question mark after the condition.
- `false` - Retain the default behavior of ternaries; keep question marks on the same line as the consequent.

| Default | CLI Override               | API Override                    |
| ------- | -------------------------- | ------------------------------- |
| `false` | `--experimental-ternaries` | `experimentalTernaries: <bool>` |

## Experimental Operator Position

Valid options:

- `"start"` - When binary expressions wrap lines, print operators at the start of new lines.
- `"end"` - Default behavior; when binary expressions wrap lines, print operators at the end of previous lines.

| Default | CLI Override                                                    | API Override                                                   |
| ------- | --------------------------------------------------------------- | -------------------------------------------------------------- |
| `"end"` | <code>--experimental-operator-position \<start&#124;end></code> | <code>experimentalOperatorPosition: "\<start&#124;end>"</code> |

## Print Width

Specify the line length that the printer will wrap on.

:::warning

**For readability we recommend against using more than 80 characters:**

In code styleguides, maximum line length rules are often set to 100 or 120. However, when humans write code, they don’t strive to reach the maximum number of columns on every line. Developers often use whitespace to break up long lines for readability. In practice, the average line length often ends up well below the maximum.

Prettier’s printWidth option does not work the same way. It is not the hard upper allowed line length limit. It is a way to say to Prettier roughly how long you’d like lines to be. Prettier will make both shorter and longer lines, but generally strive to meet the specified printWidth.

Remember, computers are dumb. You need to explicitly tell them what to do, while humans can make their own (implicit) judgements, for example on when to break a line.

In other words, don’t try to use printWidth as if it was ESLint’s [max-len](https://eslint.org/docs/rules/max-len) – they’re not the same. max-len just says what the maximum allowed line length is, but not what the generally preferred length is – which is what printWidth specifies.

:::

| Default | CLI Override          | API Override        |
| ------- | --------------------- | ------------------- |
| `80`    | `--print-width <int>` | `printWidth: <int>` |

Setting `max_line_length` in an [`.editorconfig` file](https://editorconfig.org/) will configure Prettier’s print width, unless overridden.

(If you don’t want line wrapping when formatting Markdown, you can set the [Prose Wrap](#prose-wrap) option to disable it.)

## Tab Width

Specify the number of spaces per indentation-level.

| Default | CLI Override        | API Override      |
| ------- | ------------------- | ----------------- |
| `2`     | `--tab-width <int>` | `tabWidth: <int>` |

Setting `indent_size` or `tab_width` in an [`.editorconfig` file](https://editorconfig.org/) will configure Prettier’s tab width, unless overridden.

## Tabs

Indent lines with tabs instead of spaces.

| Default | CLI Override | API Override      |
| ------- | ------------ | ----------------- |
| `false` | `--use-tabs` | `useTabs: <bool>` |

Setting `indent_style` in an [`.editorconfig` file](https://editorconfig.org/) will configure Prettier’s tab usage, unless overridden.

(Tabs will be used for _indentation_ but Prettier uses spaces to _align_ things, such as in ternaries. This behavior is known as [SmartTabs](https://www.emacswiki.org/emacs/SmartTabs).)

## Semicolons

Print semicolons at the ends of statements.

Valid options:

- `true` - Add a semicolon at the end of every statement.
- `false` - Only add semicolons at the beginning of lines that [may introduce ASI failures](rationale.md#semicolons).

| Default | CLI Override | API Override   |
| ------- | ------------ | -------------- |
| `true`  | `--no-semi`  | `semi: <bool>` |

## Quotes

Use single quotes instead of double quotes.

Notes:

- JSX quotes ignore this option – see [jsx-single-quote](#jsx-quotes).
- If the number of quotes outweighs the other quote, the quote which is less used will be used to format the string - Example: `"I'm double quoted"` results in `"I'm double quoted"` and `"This \"example\" is single quoted"` results in `'This "example" is single quoted'`.

See the [strings rationale](rationale.md#strings) for more information.

| Default | CLI Override     | API Override          |
| ------- | ---------------- | --------------------- |
| `false` | `--single-quote` | `singleQuote: <bool>` |

## Quote Props

Change when properties in objects are quoted.

Valid options:

- `"as-needed"` - Only add quotes around object properties where required.
- `"consistent"` - If at least one property in an object requires quotes, quote all properties.
- `"preserve"` - Respect the input use of quotes in object properties.

| Default       | CLI Override                                                          | API Override                                                          |
| ------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `"as-needed"` | <code>--quote-props \<as-needed&#124;consistent&#124;preserve></code> | <code>quoteProps: "\<as-needed&#124;consistent&#124;preserve>"</code> |

Note that Prettier never unquotes numeric property names in Angular expressions, TypeScript, and Flow because the distinction between string and numeric keys is significant in these languages. See: [Angular][quote-props-angular], [TypeScript][quote-props-typescript], [Flow][quote-props-flow]. Also Prettier doesn’t unquote numeric properties for Vue (see the [issue][quote-props-vue] about that).

[quote-props-angular]: https://codesandbox.io/s/hungry-morse-foj87?file=/src/app/app.component.html
[quote-props-typescript]: https://www.typescriptlang.org/play?#code/DYUwLgBAhhC8EG8IEYBcKA0EBM7sQF8AoUSAIzkQgHJlr1ktrt6dCiiATEAY2CgBOICKWhR0AaxABPAPYAzCGGkAHEAugBuLr35CR4CGTKSZG5Wo1ltRKDHjHtQA
[quote-props-flow]: https://flow.org/try/#0PQKgBAAgZgNg9gdzCYAoVBjOA7AzgFzAA8wBeMAb1TDAAYAuMARlQF8g
[quote-props-vue]: https://github.com/prettier/prettier/issues/10127

## JSX Quotes

Use single quotes instead of double quotes in JSX.

| Default | CLI Override         | API Override             |
| ------- | -------------------- | ------------------------ |
| `false` | `--jsx-single-quote` | `jsxSingleQuote: <bool>` |

## Trailing Commas

_Default value changed from `es5` to `all` in v3.0.0_

Print trailing commas wherever possible in multi-line comma-separated syntactic structures. (A single-line array, for example, never gets trailing commas.)

Valid options:

- `"all"` - Trailing commas wherever possible (including [function parameters and calls](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#Trailing_commas_in_functions)). To run, JavaScript code formatted this way needs an engine that supports ES2017 (Node.js 8+ or a modern browser) or [downlevel compilation](https://babeljs.io/docs/index). This also enables trailing commas in type parameters in TypeScript (supported since TypeScript 2.7 released in January 2018).
- `"es5"` - Trailing commas where valid in ES5 (objects, arrays, etc.). Trailing commas in type parameters in TypeScript and Flow.
- `"none"` - No trailing commas.

| Default | CLI Override                                            | API Override                                            |
| ------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `"all"` | <code>--trailing-comma \<all&#124;es5&#124;none></code> | <code>trailingComma: "\<all&#124;es5&#124;none>"</code> |

## Bracket Spacing

Print spaces between brackets in object literals.

Valid options:

- `true` - Example: `{ foo: bar }`.
- `false` - Example: `{foo: bar}`.

| Default | CLI Override           | API Override             |
| ------- | ---------------------- | ------------------------ |
| `true`  | `--no-bracket-spacing` | `bracketSpacing: <bool>` |

## Object Wrap

_First available in v3.5.0_

Configure how Prettier wraps object literals when they could fit on one line or span multiple lines.

By default, Prettier formats objects as multi-line if there is a newline prior to the first property. Authors can use this heuristic to contextually improve readability, though it has some downsides. See [Multi-line objects](rationale.md#multi-line-objects).

Valid options:

- `"preserve"` - Keep as multi-line, if there is a newline between the opening brace and first property.
- `"collapse"` - Fit to a single line when possible.

| Default      | CLI Override                                         | API Override                                         |
| ------------ | ---------------------------------------------------- | ---------------------------------------------------- |
| `"preserve"` | <code>--object-wrap \<preserve&#124;collapse></code> | <code>objectWrap: "\<preserve&#124;collapse>"</code> |

## Bracket Line

Put the `>` of a multi-line HTML (HTML, JSX, Vue, Angular) element at the end of the last line instead of being alone on the next line (does not apply to self closing elements).

Valid options:

- `true` - Example:

<!-- prettier-ignore -->
```html
<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}>
  Click Here
</button>
```

- `false` - Example:

<!-- prettier-ignore -->
```html
<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}
>
  Click Here
</button>
```

| Default | CLI Override          | API Override              |
| ------- | --------------------- | ------------------------- |
| `false` | `--bracket-same-line` | `bracketSameLine: <bool>` |

## [Deprecated] JSX Brackets

:::danger

This option has been deprecated in v2.4.0, use --bracket-same-line instead.

:::

Put the `>` of a multi-line JSX element at the end of the last line instead of being alone on the next line (does not apply to self closing elements).

Valid options:

- `true` - Example:

<!-- prettier-ignore -->
```jsx
<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}>
  Click Here
</button>
```

- `false` - Example:

<!-- prettier-ignore -->
```jsx
<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}
>
  Click Here
</button>
```

| Default | CLI Override              | API Override                 |
| ------- | ------------------------- | ---------------------------- |
| `false` | `--jsx-bracket-same-line` | `jsxBracketSameLine: <bool>` |

## Arrow Function Parentheses

_First available in v1.9.0, default value changed from `avoid` to `always` in v2.0.0_

Include parentheses around a sole arrow function parameter.

Valid options:

- `"always"` - Always include parens. Example: `(x) => x`
- `"avoid"` - Omit parens when possible. Example: `x => x`

| Default    | CLI Override                                     | API Override                                     |
| ---------- | ------------------------------------------------ | ------------------------------------------------ |
| `"always"` | <code>--arrow-parens \<always&#124;avoid></code> | <code>arrowParens: "\<always&#124;avoid>"</code> |

At first glance, avoiding parentheses may look like a better choice because of less visual noise.
However, when Prettier removes parentheses, it becomes harder to add type annotations, extra arguments or default values as well as making other changes.
Consistent use of parentheses provides a better developer experience when editing real codebases, which justifies the default value for the option.

## Range

Format only a segment of a file.

These two options can be used to format code starting and ending at a given character offset (inclusive and exclusive, respectively). The range will extend:

- Backwards to the start of the first line containing the selected statement.
- Forwards to the end of the selected statement.

| Default    | CLI Override          | API Override        |
| ---------- | --------------------- | ------------------- |
| `0`        | `--range-start <int>` | `rangeStart: <int>` |
| `Infinity` | `--range-end <int>`   | `rangeEnd: <int>`   |

## Parser

Specify which parser to use.

Prettier automatically infers the parser from the input file path, so you shouldn’t have to change this setting.

Both the `babel` and `flow` parsers support the same set of JavaScript features (including Flow type annotations). They might differ in some edge cases, so if you run into one of those you can try `flow` instead of `babel`. Almost the same applies to `typescript` and `babel-ts`. `babel-ts` might support JavaScript features (proposals) not yet supported by TypeScript, but it’s less permissive when it comes to invalid code and less battle-tested than the `typescript` parser.

Valid options:

- `"babel"` (via [@babel/parser](https://github.com/babel/babel/tree/main/packages/babel-parser)) _Named `"babylon"` until v1.16.0_
- `"babel-flow"` (same as `"babel"` but enables Flow parsing explicitly to avoid ambiguity) _First available in v1.16.0_
- `"babel-ts"` (similar to `"typescript"` but uses Babel and its TypeScript plugin) _First available in v2.0.0_
- `"flow"` (via [flow-parser](https://github.com/facebook/flow/tree/master/src/parser))
- `"typescript"` (via [@typescript-eslint/typescript-estree](https://github.com/typescript-eslint/typescript-eslint)) _First available in v1.4.0_
- `"espree"` (via [espree](https://github.com/eslint/espree)) _First available in v2.2.0_
- `"meriyah"` (via [meriyah](https://github.com/meriyah/meriyah)) _First available in v2.2.0_
- `"acorn"` (via [acorn](https://github.com/acornjs/acorn)) _First available in v2.6.0_
- `"css"` (via [postcss](https://github.com/postcss/postcss)) _First available in v1.7.1_
- `"scss"` (via [postcss-scss](https://github.com/postcss/postcss-scss)) _First available in v1.7.1_
- `"less"` (via [postcss-less](https://github.com/shellscape/postcss-less)) _First available in v1.7.1_
- `"json"` (via [@babel/parser parseExpression](https://babeljs.io/docs/babel-parser#babelparserparseexpressioncode-options)) _First available in v1.5.0_
- `"json5"` (same parser as `"json"`, but outputs as [json5](https://json5.org/)) _First available in v1.13.0_
- `"jsonc"` (same parser as `"json"`, but outputs as "JSON with Comments") _First available in v3.2.0_
- `"json-stringify"` (same parser as `"json"`, but outputs like `JSON.stringify`) _First available in v1.13.0_
- `"graphql"` (via [graphql/language](https://github.com/graphql/graphql-js/tree/master/src/language)) _First available in v1.5.0_
- `"markdown"` (via [remark-parse](https://github.com/wooorm/remark/tree/main/packages/remark-parse)) _First available in v1.8.0_
- `"mdx"` (via [remark-parse](https://github.com/wooorm/remark/tree/main/packages/remark-parse) and [@mdx-js/mdx](https://github.com/mdx-js/mdx/tree/master/packages/mdx)) _First available in v1.15.0_
- `"html"` (via [angular-html-parser](https://github.com/ikatyang/angular-html-parser/tree/master/packages/angular-html-parser)) _First available in 1.15.0_
- `"vue"` (same parser as `"html"`, but also formats vue-specific syntax) _First available in 1.10.0_
- `"angular"` (same parser as `"html"`, but also formats angular-specific syntax via [angular-estree-parser](https://github.com/ikatyang/angular-estree-parser)) _First available in 1.15.0_
- `"lwc"` (same parser as `"html"`, but also formats LWC-specific syntax for unquoted template attributes) _First available in 1.17.0_
- `"mjml"` (same parser as `"html"`, but also formats MJML-specific syntax) _First available in 3.6.0_
- `"yaml"` (via [yaml](https://github.com/eemeli/yaml) and [yaml-unist-parser](https://github.com/ikatyang/yaml-unist-parser)) _First available in 1.14.0_

| Default | CLI Override        | API Override         |
| ------- | ------------------- | -------------------- |
| None    | `--parser <string>` | `parser: "<string>"` |

Note: the default value was `"babylon"` until v1.13.0.

Note: the Custom parser API has been removed in v3.0.0. Use [plugins](plugins.md) instead ([how to migrate](api.md#custom-parser-api-removed)).

<a name="filepath"></a>

## File Path

Specify the file name to use to infer which parser to use.

For example, the following will use the CSS parser:

```bash
cat foo | prettier --stdin-filepath foo.css
```

This option is only useful in the CLI and API. It doesn’t make sense to use it in a configuration file.

| Default | CLI Override                | API Override           |
| ------- | --------------------------- | ---------------------- |
| None    | `--stdin-filepath <string>` | `filepath: "<string>"` |

## Require Pragma

_First available in v1.7.0_

Prettier can restrict itself to only format files that contain a special comment, called a pragma, at the top of the file. This is very useful when gradually transitioning large, unformatted codebases to Prettier.

A file with the following as its first comment will be formatted when `--require-pragma` is supplied:

```js
/**
 * @prettier
 */
```

or

```js
/**
 * @format
 */
```

| Default | CLI Override       | API Override            |
| ------- | ------------------ | ----------------------- |
| `false` | `--require-pragma` | `requirePragma: <bool>` |

## Insert Pragma

_First available in v1.8.0_

Prettier can insert a special `@format` marker at the top of files specifying that the file has been formatted with Prettier. This works well when used in tandem with the `--require-pragma` option. If there is already a docblock at the top of the file then this option will add a newline to it with the `@format` marker.

Note that “in tandem” doesn’t mean “at the same time”. When the two options are used simultaneously, `--require-pragma` has priority, so `--insert-pragma` is ignored. The idea is that during an incremental adoption of Prettier in a big codebase, the developers participating in the transition process use `--insert-pragma` whereas `--require-pragma` is used by the rest of the team and automated tooling to process only files already transitioned. The feature has been inspired by Facebook’s [adoption strategy].

| Default | CLI Override      | API Override           |
| ------- | ----------------- | ---------------------- |
| `false` | `--insert-pragma` | `insertPragma: <bool>` |

[adoption strategy]: https://prettier.io/blog/2017/05/03/1.3.0.html#facebook-adoption-update

## Check Ignore Pragma

_First available in v3.6.0_

Prettier can allow individual files to opt out of formatting if they contain a special comment, called a pragma, at the top of the file.

Checking for these markers incurs a small upfront cost during formatting, so it's not enabled by default.

A file with the following as its first comment will **not** be formatted when `--check-ignore-pragma` is supplied:

```js
/**
 * @noprettier
 */
```

or

```js
/**
 * @noformat
 */
```

| Default | CLI Override            | API Override                |
| ------- | ----------------------- | --------------------------- |
| `false` | `--check-ignore-pragma` | `checkIgnorePragma: <bool>` |

## Prose Wrap

_First available in v1.8.2_

By default, Prettier will not change wrapping in markdown text since some services use a linebreak-sensitive renderer, e.g. GitHub comments and BitBucket. To have Prettier wrap prose to the print width, change this option to "always". If you want Prettier to force all prose blocks to be on a single line and rely on editor/viewer soft wrapping instead, you can use `"never"`.

Valid options:

- `"always"` - Wrap prose if it exceeds the print width.
- `"never"` - Un-wrap each block of prose into one line.
- `"preserve"` - Do nothing, leave prose as-is. _First available in v1.9.0_

| Default      | CLI Override                                                 | API Override                                                 |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `"preserve"` | <code>--prose-wrap \<always&#124;never&#124;preserve></code> | <code>proseWrap: "\<always&#124;never&#124;preserve>"</code> |

## HTML Whitespace Sensitivity

_First available in v1.15.0. First available for Handlebars in 2.3.0_

Specify the global whitespace sensitivity for HTML, Vue, Angular, and Handlebars. See [whitespace-sensitive formatting] for more info.

[whitespace-sensitive formatting]: https://prettier.io/blog/2018/11/07/1.15.0.html#whitespace-sensitive-formatting

Valid options:

- `"css"` - Respect the default value of CSS `display` property. For Handlebars treated same as `strict`.
- `"strict"` - Whitespace (or the lack of it) around all tags is considered significant.
- `"ignore"` - Whitespace (or the lack of it) around all tags is considered insignificant.

| Default | CLI Override                                                              | API Override                                                             |
| ------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `"css"` | <code>--html-whitespace-sensitivity \<css&#124;strict&#124;ignore></code> | <code>htmlWhitespaceSensitivity: "\<css&#124;strict&#124;ignore>"</code> |

## Vue files script and style tags indentation

_First available in v1.19.0_

Whether or not to indent the code inside `<script>` and `<style>` tags in Vue files.

Valid options:

- `false` - Do not indent script and style tags in Vue files.
- `true` - Indent script and style tags in Vue files.

| Default | CLI Override                    | API Override                      |
| ------- | ------------------------------- | --------------------------------- |
| `false` | `--vue-indent-script-and-style` | `vueIndentScriptAndStyle: <bool>` |

## End of Line

_First available in v1.15.0, default value changed from `auto` to `lf` in v2.0.0_

For historical reasons, there exist two common flavors of line endings in text files.
That is `\n` (or `LF` for _Line Feed_) and `\r\n` (or `CRLF` for _Carriage Return + Line Feed_).
The former is common on Linux and macOS, while the latter is prevalent on Windows.
Some details explaining why it is so [can be found on Wikipedia](https://en.wikipedia.org/wiki/Newline).

When people collaborate on a project from different operating systems, it becomes easy to end up with mixed line endings in a shared git repository.
It is also possible for Windows users to accidentally change line endings in a previously committed file from `LF` to `CRLF`.
Doing so produces a large `git diff` and thus makes the line-by-line history for a file (`git blame`) harder to explore.

If you want to make sure that your entire git repository only contains Linux-style line endings in files covered by Prettier:

1. Ensure Prettier’s `endOfLine` option is set to `lf` (this is a default value since v2.0.0)
1. Configure [a pre-commit hook](precommit.md) that will run Prettier
1. Configure Prettier to run in your CI pipeline using [`--check` flag](cli.md#--check). If you use Travis CI, set [the `autocrlf` option](https://docs.travis-ci.com/user/customizing-the-build#git-end-of-line-conversion-control) to `input` in `.travis.yml`.
1. Add `* text=auto eol=lf` to the repo’s `.gitattributes` file.
   You may need to ask Windows users to re-clone your repo after this change to ensure git has not converted `LF` to `CRLF` on checkout.

All modern text editors in all operating systems are able to correctly display line endings when `\n` (`LF`) is used.
However, old versions of Notepad for Windows will visually squash such lines into one as they can only deal with `\r\n` (`CRLF`).

Valid options:

- `"lf"` – Line Feed only (`\n`), common on Linux and macOS as well as inside git repos
- `"crlf"` - Carriage Return + Line Feed characters (`\r\n`), common on Windows
- `"cr"` - Carriage Return character only (`\r`), used very rarely
- `"auto"` - Maintain existing line endings
  (mixed values within one file are normalised by looking at what’s used after the first line)

| Default | CLI Override                                                 | API Override                                                |
| ------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| `"lf"`  | <code>--end-of-line \<lf&#124;crlf&#124;cr&#124;auto></code> | <code>endOfLine: "\<lf&#124;crlf&#124;cr&#124;auto>"</code> |

Setting `end_of_line` in an [`.editorconfig` file](https://editorconfig.org/) will configure Prettier’s end of line usage, unless overridden.

## Embedded Language Formatting

_First available in v2.1.0_

Control whether Prettier formats quoted code embedded in the file.

When Prettier identifies cases where it looks like you've placed some code it knows how to format within a string in another file, like in a tagged template in JavaScript with a tag named `html` or in code blocks in Markdown, it will by default try to format that code.

Sometimes this behavior is undesirable, particularly in cases where you might not have intended the string to be interpreted as code. This option allows you to switch between the default behavior (`auto`) and disabling this feature entirely (`off`).

Valid options:

- `"auto"` – Format embedded code if Prettier can automatically identify it.
- `"off"` - Never automatically format embedded code.

| Default  | CLI Override                                                 | API Override                                                |
| -------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| `"auto"` | <code>--embedded-language-formatting=\<off&#124;auto></code> | <code>embeddedLanguageFormatting: "\<off&#124;auto>"</code> |

## Single Attribute Per Line

_First available in v2.6.0_

Enforce single attribute per line in HTML, Vue, and JSX.

Valid options:

- `false` - Do not enforce single attribute per line.
- `true` - Enforce single attribute per line.

| Default | CLI Override                  | API Override                     |
| ------- | ----------------------------- | -------------------------------- |
| `false` | `--single-attribute-per-line` | `singleAttributePerLine: <bool>` |


---


### Plugins

---
id: plugins
title: Plugins
---

Plugins are ways of adding new languages or formatting rules to Prettier. Prettier’s own implementations of all languages are expressed using the plugin API. The core `prettier` package contains JavaScript and other web-focused languages built in. For additional languages you’ll need to install a plugin.

## Using Plugins

You can load plugins with:

- The [CLI](cli.md), via `--plugin`:

  ```bash
  prettier --write main.foo --plugin=prettier-plugin-foo
  ```

  :::tip

  You can set `--plugin` options multiple times.

  :::

- The [API](api.md), via the `plugins` options:

  ```js
  await prettier.format("code", {
    parser: "foo",
    plugins: ["prettier-plugin-foo"],
  });
  ```

- The [Configuration File](configuration.md):

  ```json
  {
    "plugins": ["prettier-plugin-foo"]
  }
  ```

Strings provided to `plugins` are ultimately passed to [`import()` expression](https://nodejs.org/api/esm.html#import-expressions), so you can provide a module/package name, a path, or anything else `import()` takes.

## Official Plugins

- [`@prettier/plugin-php`](https://github.com/prettier/plugin-php)
- [`@prettier/plugin-pug`](https://github.com/prettier/plugin-pug) by [**@Shinigami92**](https://github.com/Shinigami92)
- [`@prettier/plugin-ruby`](https://github.com/prettier/plugin-ruby)
- [`@prettier/plugin-xml`](https://github.com/prettier/plugin-xml)

## Community Plugins

- [`prettier-plugin-apex`](https://github.com/dangmai/prettier-plugin-apex) by [**@dangmai**](https://github.com/dangmai)
- [`prettier-plugin-astro`](https://github.com/withastro/prettier-plugin-astro) by [**@withastro contributors**](https://github.com/withastro/prettier-plugin-astro/graphs/contributors)
- [`prettier-plugin-bigcommerce-stencil`](https://github.com/phoenix128/prettier-plugin-bigcommerce-stencil) by [**@phoenix128**](https://github.com/phoenix128)
- [`prettier-plugin-elm`](https://github.com/gicentre/prettier-plugin-elm) by [**@giCentre**](https://github.com/gicentre)
- [`prettier-plugin-erb`](https://github.com/adamzapasnik/prettier-plugin-erb) by [**@adamzapasnik**](https://github.com/adamzapasnik)
- [`prettier-plugin-gherkin`](https://github.com/mapado/prettier-plugin-gherkin) by [**@mapado**](https://github.com/mapado)
- [`prettier-plugin-glsl`](https://github.com/NaridaL/glsl-language-toolkit/tree/main/packages/prettier-plugin-glsl) by [**@NaridaL**](https://github.com/NaridaL)
- [`prettier-plugin-go-template`](https://github.com/NiklasPor/prettier-plugin-go-template) by [**@NiklasPor**](https://github.com/NiklasPor)
- [`prettier-plugin-hugo-post`](https://github.com/metcalfc/prettier-plugin-hugo-post) by [**@metcalfc**](https://github.com/metcalfc)
- [`prettier-plugin-java`](https://github.com/jhipster/prettier-java) by [**@JHipster**](https://github.com/jhipster)
- [`prettier-plugin-jinja-template`](https://github.com/davidodenwald/prettier-plugin-jinja-template) by [**@davidodenwald**](https://github.com/davidodenwald)
- [`prettier-plugin-jsonata`](https://github.com/Stedi/prettier-plugin-jsonata) by [**@Stedi**](https://github.com/Stedi)
- [`prettier-plugin-kotlin`](https://github.com/Angry-Potato/prettier-plugin-kotlin) by [**@Angry-Potato**](https://github.com/Angry-Potato)
- [`prettier-plugin-marko`](https://github.com/marko-js/prettier) by [**@marko-js**](https://github.com/marko-js)
- [`prettier-plugin-motoko`](https://github.com/dfinity/prettier-plugin-motoko) by [**@dfinity**](https://github.com/dfinity)
- [`prettier-plugin-nginx`](https://github.com/joedeandev/prettier-plugin-nginx) by [**@joedeandev**](https://github.com/joedeandev)
- [`prettier-plugin-prisma`](https://github.com/umidbekk/prettier-plugin-prisma) by [**@umidbekk**](https://github.com/umidbekk)
- [`prettier-plugin-properties`](https://github.com/eemeli/prettier-plugin-properties) by [**@eemeli**](https://github.com/eemeli)
- [`prettier-plugin-rust`](https://github.com/jinxdash/prettier-plugin-rust) by [**@jinxdash**](https://github.com/jinxdash)
- [`prettier-plugin-sh`](https://github.com/un-ts/prettier/tree/master/packages/sh) by [**@JounQin**](https://github.com/JounQin)
- [`prettier-plugin-sql`](https://github.com/un-ts/prettier/tree/master/packages/sql) by [**@JounQin**](https://github.com/JounQin)
- [`prettier-plugin-sql-cst`](https://github.com/nene/prettier-plugin-sql-cst) by [**@nene**](https://github.com/nene)
- [`prettier-plugin-solidity`](https://github.com/prettier-solidity/prettier-plugin-solidity) by [**@mattiaerre**](https://github.com/mattiaerre)
- [`prettier-plugin-svelte`](https://github.com/sveltejs/prettier-plugin-svelte) by [**@sveltejs**](https://github.com/sveltejs)
- [`prettier-plugin-toml`](https://github.com/un-ts/prettier/tree/master/packages/toml) by [**@JounQin**](https://github.com/JounQin) and [**@so1ve**](https://github.com/so1ve)
- [`prettier-plugin-xquery`](https://github.com/drrataplan/prettier-plugin-xquery) by [**@DrRataplan**](https://github.com/drrataplan)

## Developing Plugins

Prettier plugins are regular JavaScript modules with the following five exports or default export with the following properties:

- `languages`
- `parsers`
- `printers`
- `options`
- `defaultOptions`

### `languages`

Languages is an array of language definitions that your plugin will contribute to Prettier. It can include all of the fields specified in [`prettier.getSupportInfo()`](api.md#prettiergetsupportinfo).

It **must** include `name` and `parsers`.

```js
export const languages = [
  {
    // The language name
    name: "InterpretedDanceScript",
    // Parsers that can parse this language.
    // This can be built-in parsers, or parsers you have contributed via this plugin.
    parsers: ["dance-parse"],
  },
];
```

### `parsers`

Parsers convert code as a string into an [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree).

The key must match the name in the `parsers` array from `languages`. The value contains a parse function, an AST format name, and two location extraction functions (`locStart` and `locEnd`).

```js
export const parsers = {
  "dance-parse": {
    parse,
    // The name of the AST that the parser produces.
    astFormat: "dance-ast",
    hasPragma,
    hasIgnorePragma,
    locStart,
    locEnd,
    preprocess,
  },
};
```

The signature of the `parse` function is:

```ts
function parse(text: string, options: object): Promise<AST> | AST;
```

The location extraction functions (`locStart` and `locEnd`) return the starting and ending locations of a given AST node:

```ts
function locStart(node: object): number;
```

_(Optional)_ The pragma detection function (`hasPragma`) should return if the text contains the pragma comment.

```ts
function hasPragma(text: string): boolean;
```

_(Optional)_ The "ignore pragma" detection function (`hasIgnorePragma`) should return if the text contains a pragma indicating the text should not be formatted.

```ts
function hasIgnorePragma(text: string): boolean;
```

_(Optional)_ The preprocess function can process the input text before passing into `parse` function.

```ts
function preprocess(text: string, options: object): string | Promise<string>;
```

_Support for async preprocess first added in v3.7.0_

### `printers`

Printers convert ASTs into a Prettier intermediate representation, also known as a Doc.

The key must match the `astFormat` that the parser produces. The value contains an object with a `print` function. All other properties (`embed`, `preprocess`, etc.) are optional.

```js
export const printers = {
  "dance-ast": {
    print,
    embed,
    preprocess,
    getVisitorKeys,
    insertPragma,
    canAttachComment,
    isBlockComment,
    printComment,
    getCommentChildNodes,
    hasPrettierIgnore,
    printPrettierIgnored,
    handleComments: {
      ownLine,
      endOfLine,
      remaining,
    },
  },
};
```

#### The printing process

Prettier uses an intermediate representation, called a Doc, which Prettier then turns into a string (based on options like `printWidth`). A _printer_'s job is to take the AST generated by `parsers[<parser name>].parse` and return a Doc. A Doc is constructed using [builder commands](https://github.com/prettier/prettier/blob/main/commands.md):

```js
import * as prettier from "prettier";

const { join, line, ifBreak, group } = prettier.doc.builders;
```

The printing process consists of the following steps:

1. **AST preprocessing** (optional). See [`preprocess`](#optional-preprocess).
2. **Comment attachment** (optional). See [Handling comments in a printer](#handling-comments-in-a-printer).
3. **Processing embedded languages** (optional). The [`embed`](#optional-embed) method, if defined, is called for each node, depth-first. While, for performance reasons, the recursion itself is synchronous, `embed` may return asynchronous functions that can call other parsers and printers to compose docs for embedded syntaxes like CSS-in-JS. These returned functions are queued up and sequentially executed before the next step.
4. **Recursive printing**. A doc is recursively constructed from the AST. Starting from the root node:
   - If, from the step 3, there is an embedded language doc associated with the current node, this doc is used.
   - Otherwise, the `print(path, options, print): Doc` method is called. It composes a doc for the current node, often by printing child nodes using the `print` callback.

#### `print`

Most of the work of a plugin's printer will take place in its `print` function, whose signature is:

```ts
function print(
  // Path to the AST node to print
  path: AstPath,
  options: object,
  // Recursively print a child node
  print: (selector?: string | number | Array<string | number> | AstPath) => Doc,
): Doc;
```

The `print` function is passed the following parameters:

- **`path`**: An object, which can be used to access nodes in the AST. It’s a stack-like data structure that maintains the current state of the recursion. It is called “path” because it represents the path to the current node from the root of the AST. The current node is returned by `path.node`.
- **`options`**: A persistent object, which contains global options and which a plugin may mutate to store contextual data.
- **`print`**: A callback for printing sub-nodes. This function contains the core printing logic that consists of steps whose implementation is provided by plugins. In particular, it calls the printer’s `print` function and passes itself to it. Thus, the two `print` functions – the one from the core and the one from the plugin – call each other while descending down the AST recursively.

Here’s a simplified example to give an idea of what a typical implementation of `print` looks like:

```js
import * as prettier from "prettier";

const { group, indent, join, line, softline } = prettier.doc.builders;

function print(path, options, print) {
  const node = path.node;

  switch (node.type) {
    case "list":
      return group([
        "(",
        indent([softline, join(line, path.map(print, "elements"))]),
        softline,
        ")",
      ]);

    case "pair":
      return group([
        "(",
        indent([softline, print("left"), line, ". ", print("right")]),
        softline,
        ")",
      ]);

    case "symbol":
      return node.name;
  }

  throw new Error(`Unknown node type: ${node.type}`);
}
```

Check out [prettier-python's printer](https://github.com/prettier/prettier-python/blob/034ba8a9551f3fa22cead41b323be0b28d06d13b/src/printer.js#L174) for some examples of what is possible.

#### (optional) `embed`

A printer can have the `embed` method to print one language inside another. Examples of this are printing CSS-in-JS or fenced code blocks in Markdown. The signature is:

```ts
function embed(
  // Path to the current AST node
  path: AstPath,
  // Current options
  options: Options,
):
  | ((
      // Parses and prints the passed text using a different parser.
      // You should set `options.parser` to specify which parser to use.
      textToDoc: (text: string, options: Options) => Promise<Doc>,
      // Prints the current node or its descendant node with the current printer
      print: (
        selector?: string | number | Array<string | number> | AstPath,
      ) => Doc,
      // The following two arguments are passed for convenience.
      // They're the same `path` and `options` that are passed to `embed`.
      path: AstPath,
      options: Options,
    ) => Promise<Doc | undefined> | Doc | undefined)
  | Doc
  | undefined;
```

The `embed` method is similar to the `print` method in that it maps AST nodes to docs, but unlike `print`, it has power to do async work by returning an async function. That function's first parameter, the `textToDoc` async function, can be used to render a doc using a different plugin.

If a function returned from `embed` returns a doc or a promise that resolves to a doc, that doc will be used in printing, and the `print` method won’t be called for this node. It's also possible and, in rare situations, might be convenient to return a doc synchronously directly from `embed`, however `textToDoc` and the `print` callback aren’t available at that case. Return a function to get them.

If `embed` returns `undefined`, or if a function it returned returns `undefined` or a promise that resolves to `undefined`, the node will be printed normally with the `print` method. Same will happen if a returned function throws an error or returns a promise that rejects (e.g., if a parsing error has happened). Set the `PRETTIER_DEBUG` environment variable to a non-empty value if you want Prettier to rethrow these errors.

For example, a plugin that has nodes with embedded JavaScript might have the following `embed` method:

```js
function embed(path, options) {
  const node = path.node;
  if (node.type === "javascript") {
    return async (textToDoc) => {
      return [
        "<script>",
        hardline,
        await textToDoc(node.javaScriptCode, { parser: "babel" }),
        hardline,
        "</script>",
      ];
    };
  }
}
```

If the [`--embedded-language-formatting`](options.md#embedded-language-formatting) option is set to `off`, the embedding step is entirely skipped, `embed` isn’t called, and all nodes are printed with the `print` method.

#### (optional) `preprocess`

The `preprocess` method can process the AST from the parser before passing it into the `print` method.

```ts
function preprocess(ast: AST, options: Options): AST | Promise<AST>;
```

#### (optional) `getVisitorKeys`

This property might come in handy if the plugin uses comment attachment or embedded languages. These features traverse the AST iterating through all the own enumerable properties of each node starting from the root. If the AST has [cycles](<https://en.wikipedia.org/wiki/Cycle_(graph_theory)>), such a traverse ends up in an infinite loop. Also, nodes might contain non-node objects (e.g., location data), iterating through which is a waste of resources. To solve these issues, the printer can define a function to return property names that should be traversed.

Its signature is:

```ts
function getVisitorKeys(node, nonTraversableKeys: Set<string>): string[];
```

The default `getVisitorKeys`:

```js
function getVisitorKeys(node, nonTraversableKeys) {
  return Object.keys(node).filter((key) => !nonTraversableKeys.has(key));
}
```

The second argument `nonTraversableKeys` is a set of common keys and keys that prettier used internal.

If you have full list of visitor keys

```js
const visitorKeys = {
  Program: ["body"],
  Identifier: [],
  // ...
};

function getVisitorKeys(node /* , nonTraversableKeys*/) {
  // Return `[]` for unknown node to prevent Prettier fallback to use `Object.keys()`
  return visitorKeys[node.type] ?? [];
}
```

If you only need exclude a small set of keys

```js
const ignoredKeys = new Set(["prev", "next", "range"]);

function getVisitorKeys(node, nonTraversableKeys) {
  return Object.keys(node).filter(
    (key) => !nonTraversableKeys.has(key) && !ignoredKeys.has(key),
  );
}
```

#### (optional) `insertPragma`

A plugin can implement how a pragma comment is inserted in the resulting code when the `--insert-pragma` option is used, in the `insertPragma` function. Its signature is:

```ts
function insertPragma(text: string): string;
```

#### Handling comments in a printer

Comments are often not part of a language's AST and present a challenge for pretty printers. A Prettier plugin can either print comments itself in its `print` function or rely on Prettier's comment algorithm.

By default, if the AST has a top-level `comments` property, Prettier assumes that `comments` stores an array of comment nodes. Prettier will then use the provided `parsers[<plugin>].locStart`/`locEnd` functions to search for the AST node that each comment "belongs" to. Comments are then attached to these nodes **mutating the AST in the process**, and the `comments` property is deleted from the AST root. The `*Comment` functions are used to adjust Prettier's algorithm. Once the comments are attached to the AST, Prettier will automatically call the `printComment(path, options): Doc` function and insert the returned doc into the (hopefully) correct place.

#### (optional) `getCommentChildNodes`

By default, Prettier searches all object properties (except for a few predefined ones) of each node recursively. This function can be provided to override that behavior. It has the signature:

```ts
function getCommentChildNodes(
  // The node whose children should be returned.
  node: AST,
  // Current options
  options: object,
): AST[] | undefined;
```

Return `[]` if the node has no children or `undefined` to fall back on the default behavior.

### (optional) `hasPrettierIgnore`

```ts
function hasPrettierIgnore(path: AstPath): boolean;
```

Returns whether or not the AST node is `prettier-ignore`d.

### (optional) `printPrettierIgnored`

If the AST node is `prettier-ignore`d, Prettier will slice for the text for parsing without calling `print` function by default, however plugin can also handle the `prettier-ignore`d node print by adding this property.

This property have the same signature as the `print` property.

_First available in v3.7.0_

#### (optional) `printComment`

Called whenever a comment node needs to be printed. It has the signature:

```ts
function printComment(
  // Path to the current comment node
  commentPath: AstPath,
  // Current options
  options: object,
): Doc;
```

#### (optional) `canAttachComment`

```ts
function canAttachComment(node: AST, ancestors: T[]): boolean;
```

This function is used for deciding whether a comment can be attached to a particular AST node. By default, _all_ AST properties are traversed searching for nodes that comments can be attached to. This function is used to prevent comments from being attached to a particular node. A typical implementation looks like

```js
function canAttachComment(node, [parent]) {
  return !(
    node.type === "comment" ||
    (parent?.type === "shorthand-property" &&
      parent.key === node &&
      parent.key !== parent.value)
  );
}
```

_The second parameter `ancestors` first added in v3.7.0._

#### (optional) `isBlockComment`

```ts
function isBlockComment(node: AST): boolean;
```

Returns whether or not the AST node is a block comment.

#### (optional) `handleComments`

The `handleComments` object contains three optional functions, each with signature

```ts
(
  // The AST node corresponding to the comment
  comment: AST,
  // The full source code text
  text: string,
  // The global options object
  options: object,
  // The AST
  ast: AST,
  // Whether this comment is the last comment
  isLastComment: boolean,
) => boolean;
```

These functions are used to override Prettier's default comment attachment algorithm. `ownLine`/`endOfLine`/`remaining` is expected to either manually attach a comment to a node and return `true`, or return `false` and let Prettier attach the comment.

Based on the text surrounding a comment node, Prettier dispatches:

- `ownLine` if a comment has only whitespace preceding it and a newline afterwards,
- `endOfLine` if a comment has a newline afterwards but some non-whitespace preceding it,
- `remaining` in all other cases.

At the time of dispatching, Prettier will have annotated each AST comment node (i.e., created new properties) with at least one of `enclosingNode`, `precedingNode`, or `followingNode`. These can be used to aid a plugin's decision process (of course the entire AST and original text is also passed in for making more complicated decisions).

#### Manually attaching a comment

The `prettier.util.addTrailingComment`/`addLeadingComment`/`addDanglingComment` functions can be used to manually attach a comment to an AST node. An example `ownLine` function that ensures a comment does not follow a "punctuation" node (made up for demonstration purposes) might look like:

```js
import * as prettier from "prettier";

function ownLine(comment, text, options, ast, isLastComment) {
  const { precedingNode } = comment;
  if (precedingNode && precedingNode.type === "punctuation") {
    prettier.util.addTrailingComment(precedingNode, comment);
    return true;
  }
  return false;
}
```

Nodes with comments are expected to have a `comments` property containing an array of comments. Each comment is expected to have the following properties: `leading`, `trailing`, `printed`.

<!-- TODO: add a note that this might change in the future -->

The example above uses `prettier.util.addTrailingComment`, which automatically sets `comment.leading`/`trailing`/`printed` to appropriate values and adds the comment to the AST node's `comments` array.

The `--debug-print-comments` CLI flag can help with debugging comment attachment issues. It prints a detailed list of comments, which includes information on how every comment was classified (`ownLine`/`endOfLine`/`remaining`, `leading`/`trailing`/`dangling`) and to which node it was attached. For Prettier’s built-in languages, this information is also available on the Playground (the 'show comments' checkbox in the Debug section).

### `options`

`options` is an object containing the custom options your plugin supports.

Example:

```js
export default {
  // ... plugin implementation
  options: {
    openingBraceNewLine: {
      type: "boolean",
      category: "Global",
      default: true,
      description: "Move open brace for code blocks onto new line.",
    },
  },
};
```

### `defaultOptions`

If your plugin requires different default values for some of Prettier’s core options, you can specify them in `defaultOptions`:

```js
export default {
  // ... plugin implementation
  defaultOptions: {
    tabWidth: 4,
  },
};
```

### Utility functions

`prettier.util` provides the following limited set of utility functions for plugins:

```ts
type Quote = '"' | "'";
type SkipOptions = { backwards?: boolean };

function getMaxContinuousCount(text: string, searchString: string): number;

function getStringWidth(text: string): number;

function getAlignmentSize(
  text: string,
  tabWidth: number,
  startIndex?: number,
): number;

function getIndentSize(value: string, tabWidth: number): number;

function skip(
  characters: string | RegExp,
): (
  text: string,
  startIndex: number | false,
  options?: SkipOptions,
) => number | false;

function skipWhitespace(
  text: string,
  startIndex: number | false,
  options?: SkipOptions,
): number | false;

function skipSpaces(
  text: string,
  startIndex: number | false,
  options?: SkipOptions,
): number | false;

function skipToLineEnd(
  text: string,
  startIndex: number | false,
  options?: SkipOptions,
): number | false;

function skipEverythingButNewLine(
  text: string,
  startIndex: number | false,
  options?: SkipOptions,
): number | false;

function skipInlineComment(
  text: string,
  startIndex: number | false,
): number | false;

function skipTrailingComment(
  text: string,
  startIndex: number | false,
): number | false;

function skipNewline(
  text: string,
  startIndex: number | false,
  options?: SkipOptions,
): number | false;

function hasNewline(
  text: string,
  startIndex: number,
  options?: SkipOptions,
): boolean;

function hasNewlineInRange(
  text: string,
  startIndex: number,
  startIndex: number,
): boolean;

function hasSpaces(
  text: string,
  startIndex: number,
  options?: SkipOptions,
): boolean;

function getPreferredQuote(
  text: string,
  preferredQuoteOrPreferSingleQuote: Quote | boolean,
): Quote;

function makeString(
  rawText: string,
  enclosingQuote: Quote,
  unescapeUnnecessaryEscapes?: boolean,
): string;

function getNextNonSpaceNonCommentCharacter(
  text: string,
  startIndex: number,
): string;

function getNextNonSpaceNonCommentCharacterIndex(
  text: string,
  startIndex: number,
): number | false;

function isNextLineEmpty(text: string, startIndex: number): boolean;

function isPreviousLineEmpty(text: string, startIndex: number): boolean;
```

### Tutorials

- [How to write a plugin for Prettier](https://medium.com/@fvictorio/how-to-write-a-plugin-for-prettier-a0d98c845e70): Teaches you how to write a very basic Prettier plugin for TOML.

## Testing Plugins

Since plugins can be resolved using relative paths, when working on one you can do:

```js
import * as prettier from "prettier";

const code = "(add 1 2)";
await prettier.format(code, {
  parser: "lisp",
  plugins: ["./index.js"],
});
```

This will resolve a plugin relative to the current working directory.


---


### Pre-commit Hook

---
id: precommit
title: Pre-commit Hook
---

import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";

You can use Prettier with a pre-commit tool. This can re-format your files that are marked as “staged” via `git add` before you commit.

## Option 1. [lint-staged](https://github.com/okonet/lint-staged)

**Use Case:** Useful for when you want to use other code quality tools along with Prettier (e.g. ESLint, Stylelint, etc.) or if you need support for partially staged files (`git add --patch`).

_Make sure Prettier is installed and is in your [`devDependencies`](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file) before you proceed._

```bash
npx mrm@2 lint-staged
```

This will install [husky](https://github.com/typicode/husky) and [lint-staged](https://github.com/okonet/lint-staged), then add a configuration to the project’s `package.json` that will automatically format supported files in a pre-commit hook.

Read more at the [lint-staged](https://github.com/okonet/lint-staged#configuration) repo.

## Option 2. [pretty-quick](https://github.com/prettier/pretty-quick)

**Use Case:** Great for when you want an entire file formatting on your changed/staged files.

Install it along with [simple-git-hooks](https://github.com/toplenboren/simple-git-hooks):

<Tabs groupId="package-manager">
<TabItem value="npm">

```bash
npm install --save-dev simple-git-hooks pretty-quick
echo '{\n  "pre-commit": "npx pretty-quick --staged"\n}\n' > .simple-git-hooks.json
npx simple-git-hooks
```

</TabItem>
<TabItem value="yarn">

```bash
yarn add --dev simple-git-hooks pretty-quick
echo '{\n  "pre-commit": "yarn pretty-quick --staged"\n}\n' > .simple-git-hooks.json
yarn simple-git-hooks
```

</TabItem>
<TabItem value="pnpm">

```bash
pnpm add --save-dev simple-git-hooks pretty-quick
echo '{\n  "pre-commit": "pnpm pretty-quick --staged"\n}\n' > .simple-git-hooks.json
pnpm simple-git-hooks
```

</TabItem>
<TabItem value="bun">

```bash
bun add --dev simple-git-hooks pretty-quick
echo '{\n  "pre-commit": "bun pretty-quick --staged"\n}\n' > .simple-git-hooks.json
bun simple-git-hooks
```

</TabItem>
</Tabs>

Read more at the [pretty-quick](https://github.com/prettier/pretty-quick) repo.

## Option 3. [Husky.Net](https://github.com/alirezanet/Husky.Net)

**Use Case:** A dotnet solution to use Prettier along with other code quality tools (e.g. dotnet-format, ESLint, Stylelint, etc.). It supports multiple file states (staged - last-commit, git-files etc.)

```bash
dotnet new tool-manifest
dotnet tool install husky
dotnet husky install
dotnet husky add pre-commit
```

after installation you can add prettier task to the `task-runner.json`.

```json
{
  "command": "npx",
  "args": ["prettier", "--ignore-unknown", "--write", "${staged}"],
  "pathMode": "absolute"
}
```

## Option 4. [git-format-staged](https://github.com/hallettj/git-format-staged)

**Use Case:** Great for when you want to format partially-staged files, and other options do not provide a good fit for your project.

Git-format-staged is used to run any formatter that can accept file content via stdin. It operates differently than other tools that format partially-staged files: it applies the formatter directly to objects in the git object database, and merges changes back to the working tree. This procedure provides several guarantees:

1. Changes in commits are always formatted.
2. Unstaged changes are never, under any circumstances staged during the formatting process.
3. If there are conflicts between formatted, staged changes and unstaged changes then your working tree files are left untouched - your work won’t be overwritten, and there are no stashes to clean up.
4. Unstaged changes are not formatted.

Git-format-staged requires Python v3 or v2.7. Python is usually pre-installed on Linux and macOS, but not on Windows. Use git-format-staged with [husky](https://github.com/typicode/husky):

<Tabs groupId="package-manager">
<TabItem value="npm">

```bash
npx husky init
npm install --save-dev git-format-staged
node --eval "fs.writeFileSync('.husky/pre-commit', 'git-format-staged -f \'prettier --ignore-unknown --stdin --stdin-filepath \"{}\"\' .\n')"
```

</TabItem>
<TabItem value="yarn">

```bash
yarn husky init
yarn add --dev git-format-staged
node --eval "fs.writeFileSync('.husky/pre-commit', 'git-format-staged -f \'prettier --ignore-unknown --stdin --stdin-filepath \"{}\"\' .\n')"
```

</TabItem>
<TabItem value="pnpm">

```bash
pnpm exec husky init
pnpm add --save-dev git-format-staged
node --eval "fs.writeFileSync('.husky/pre-commit', 'git-format-staged -f \'prettier --ignore-unknown --stdin --stdin-filepath \"{}\"\' .\n')"
```

</TabItem>
<TabItem value="bun">

```bash
bunx husky init
bun add --dev git-format-staged
bun --eval "fs.writeFileSync('.husky/pre-commit', 'git-format-staged -f \'prettier --ignore-unknown --stdin --stdin-filepath \"{}\"\' .\n')"
```

</TabItem>
</Tabs>

Add or remove file extensions to suit your project. Note that regardless of which extensions you list formatting will respect any `.prettierignore` files in your project.

To read about how git-format-staged works see [Automatic Code Formatting for Partially-Staged Files](https://www.olioapps.com/blog/automatic-code-formatting/).

## Option 5. Shell script

Alternately you can save this script as `.git/hooks/pre-commit` and give it execute permission:

```sh
#!/bin/sh
FILES=$(git diff --cached --name-only --diff-filter=ACMR | sed 's| |\\ |g')
[ -z "$FILES" ] && exit 0