# Source: https://biomejs.dev/internals/architecture/

# Architecture 

This document covers some of the internals of Biome, and how they are used inside the project.

## Scanner

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Scanner"]](#scanner)

Biome has a scanner that is responsible for crawling the file system to extract important metadata about projects. Specifically, there are three ways in which the scanner is used:

-   To discover nested `biome.json`/`biome.jsonc` files in monorepos.
-   To discover nested `.gitignore` files if the [`vcs.useIgnoreFile`](/reference/configuration/#vcsuseignorefile) setting is enabled.
-   To index `package.json` manifests as well as source files in a project if any rules from the [project domain](/linter/domains/#project) are enabled.

### Scanner targeting

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Scanner targeting"]](#scanner-targeting)

If project rules are not enabled, the scanner automatically targets only the folders that are relevant for a given session.

This means that if you have a large monorepo, and you run `biome check` from inside the `packages/foo/` folder, that folder will be "targeted". This means the following folders get scanned for nested configuration files and/or nested ignore files:

-   The root folder of the repository.
-   The `packages/` folder.
-   The `packages/foo/` folder.
-   Any folders that exist under `packages/foo/`, except `node_modules/` or those that are excluded by your configuration (see [below](#configuring-the-scanner)).

Other folders that may be adjacent to either `packages/` or `packages/foo/` will be automatically skipped.

Similarly, if you run `biome format packages/bar/src/index.ts` from the root of the repository, the scanner will target the `packages/bar/src/` folder.

If project rules are enabled, these optimisations don't apply.

### Configuring the scanner

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Configuring the scanner"]](#configuring-the-scanner)

The scanner can be configured through the [`files.includes`](/reference/configuration/#interactionwiththescanner) setting.

## Parser and CST

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Parser and CST"]](#parser-and-cst)

The architecture of the parser is bumped by an internal fork of [rowan](https://github.com/rust-analyzer/rowan), a library that implements the [Green and Red tree](https://learn.microsoft.com/en-us/archive/blogs/ericlippert/persistence-facades-and-roslyns-red-green-trees) pattern.

The CST (Concrete Syntax Tree) is a data structure very similar to an AST (Abstract Syntax Tree) that keeps track of all the information of a program, trivia included.

**Trivia** is represented by all that information that is important to a program to run:

-   spaces
-   tabs
-   comments

Trivia is attached to a node. A node can have leading trivia and trailing trivia. If you read code from left to right, leading trivia appears before a keyword, and trialing trivia appears after a keyword.

Leading trivia and trailing trivia are categorized as follows:

-   Every trivia up to the token/keyword (including line breaks) will be the **leading trivia**;
-   Everything until the next linebreak (but not including it) will be the **trailing trivia**;

Given the following JavaScript snippet, `// comment 1` is a trailing trivia of the token `;`, and `// comment 2` is a leading trivia to the keyword `const`. Below is a minimized version of the CST represented by Biome:

<figure class="frame not-content">
<pre data-language="js"><code>1const a = &quot;foo&quot;; // comment 12// comment 23const b = &quot;bar&quot;;</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

<figure class="frame not-content">
<pre data-language="plaintext"><code>10: JS_MODULE@0..552    ...3      1: SEMICOLON@15..27 &quot;;&quot; [] [Whitespace(&quot; &quot;), Comments(&quot;// comment 1&quot;)]4    1: JS_VARIABLE_STATEMENT@27..555        ...6        1: CONST_KW@27..45 &quot;const&quot; [Newline(&quot;\n&quot;), Comments(&quot;// comment 2&quot;), Newline(&quot;\n&quot;)] [Whitespace(&quot; &quot;)]7  3: EOF@55..55 &quot;&quot; [] []</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

The CST is never directly accessible by design; a developer can read its information using the Red tree, using a number of APIs that are autogenerated from the grammar of the language.

#### Resilient and recoverable parser

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Resilient and recoverable parser"]](#resilient-and-recoverable-parser)

In order to construct a CST, a parser needs to be error-resilient and recoverable:

-   resilient: a parser that is able to resume parsing after encountering syntax errors that belong to the language;
-   recoverable: a parser that is able to **understand** where an error occurred and being able to resume the parsing by creating **correct** information;

The recoverable part of the parser is not a science, and no rules are set in stone. This means that depending on what the parser was parsing and where an error occurred, the parser might be able to recover itself in an expected way.

The parser also uses' Bogus' nodes to protect the consumers from consuming incorrect syntax. These nodes are used to decorate the broken code caused by a syntax error.

In the following example, the parentheses in the `while` are missing, although the parser can recover itself in a good manner and can represent the code with a decent CST. The parenthesis and condition of the loop are marked as missing, and the code block is correctly parsed:

<figure class="frame not-content">
<pre data-language="js"><code>1while </code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

<figure class="frame not-content">
<pre data-language="plaintext"><code>1JsModule &quot; [] [],14      },15    },16  ],17  eof_token: EOF@8..8 &quot;&quot; [] [],18}</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

This is an error emitted during parsing:

<figure class="frame not-content">
<pre data-language="plaintext"><code>1main.tsx:1:7 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━2
3  ✖ expected `(` but instead found `6      │       ^7
8  ℹ Remove :

<figure class="frame not-content">
<pre data-language="js"><code>1function}</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

<figure class="frame not-content">
<pre data-language="plaintext"><code>1JsModule ,14    JsBogusStatement &quot; [] [],17      ],18    },19  ],20  eof_token: EOF@9..9 &quot;&quot; [] [],21}</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

This is the error we get from the parsing phase:

<figure class="frame not-content">
<pre data-language="plaintext"><code>1main.tsx:1:9 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━2
3  ✖ expected a name for the function in a function declaration, but found none4
5  &gt; 1 │ function}6      │         ^</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

## Formatter

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Formatter"]](#formatter)

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTFDMTEuNzM0OCAxMSAxMS40ODA0IDExLjEwNTQgMTEuMjkyOSAxMS4yOTI5QzExLjEwNTQgMTEuNDgwNCAxMSAxMS43MzQ4IDExIDEyVjE2QzExIDE2LjI2NTIgMTEuMTA1NCAxNi41MTk2IDExLjI5MjkgMTYuNzA3MUMxMS40ODA0IDE2Ljg5NDYgMTEuNzM0OCAxNyAxMiAxN0MxMi4yNjUyIDE3IDEyLjUxOTYgMTYuODk0NiAxMi43MDcxIDE2LjcwNzFDMTIuODk0NiAxNi41MTk2IDEzIDE2LjI2NTIgMTMgMTZWMTJDMTMgMTEuNzM0OCAxMi44OTQ2IDExLjQ4MDQgMTIuNzA3MSAxMS4yOTI5QzEyLjUxOTYgMTEuMTA1NCAxMi4yNjUyIDExIDEyIDExWk0xMi4zOCA3LjA4QzEyLjEzNjUgNi45Nzk5OCAxMS44NjM1IDYuOTc5OTggMTEuNjIgNy4wOEMxMS40OTczIDcuMTI3NTkgMTEuMzg1MSA3LjE5ODk2IDExLjI5IDcuMjlDMTEuMjAxNyA3LjM4NzIgMTEuMTMwNiA3LjQ5ODgyIDExLjA4IDcuNjJDMTEuMDI0IDcuNzM4NjggMTAuOTk2NiA3Ljg2ODgyIDExIDhDMTAuOTk5MiA4LjEzMTYxIDExLjAyNDUgOC4yNjIwNyAxMS4wNzQyIDguMzgzOTFDMTEuMTI0IDguNTA1NzQgMTEuMTk3MyA4LjYxNjU2IDExLjI5IDguNzFDMTEuMzg3MiA4Ljc5ODMzIDExLjQ5ODggOC44NjkzNiAxMS42MiA4LjkyQzExLjc3MTUgOC45ODIyNCAxMS45MzYgOS4wMDYzMiAxMi4wOTkgOC45OTAxMUMxMi4yNjE5IDguOTczOTEgMTIuNDE4NCA4LjkxNzkyIDEyLjU1NDcgOC44MjcwN0MxMi42OTEgOC43MzYyMiAxMi44MDI5IDguNjEzMjggMTIuODgwNSA4LjQ2OTA3QzEyLjk1ODIgOC4zMjQ4NiAxMi45OTkyIDguMTYzNzggMTMgOEMxMi45OTYzIDcuNzM1MjMgMTIuODkyNyA3LjQ4MTYzIDEyLjcxIDcuMjlDMTIuNjE0OSA3LjE5ODk2IDEyLjUwMjggNy4xMjc1OSAxMi4zOCA3LjA4Wk0xMiAyQzEwLjAyMjIgMiA4LjA4ODc5IDIuNTg2NDkgNi40NDQzIDMuNjg1M0M0Ljc5OTgxIDQuNzg0MTIgMy41MTgwOSA2LjM0NTkgMi43NjEyMSA4LjE3MzE3QzIuMDA0MzMgMTAuMDAwNCAxLjgwNjMgMTIuMDExMSAyLjE5MjE1IDEzLjk1MDlDMi41NzggMTUuODkwNyAzLjUzMDQxIDE3LjY3MjUgNC45Mjg5NCAxOS4wNzExQzYuMzI3NDYgMjAuNDY5NiA4LjEwOTI5IDIxLjQyMiAxMC4wNDkxIDIxLjgwNzlDMTEuOTg4OSAyMi4xOTM3IDEzLjk5OTYgMjEuOTk1NyAxNS44MjY4IDIxLjIzODhDMTcuNjU0MSAyMC40ODE5IDE5LjIxNTkgMTkuMjAwMiAyMC4zMTQ3IDE3LjU1NTdDMjEuNDEzNSAxNS45MTEyIDIyIDEzLjk3NzggMjIgMTJDMjIgMTAuNjg2OCAyMS43NDEzIDkuMzg2NDIgMjEuMjM4OCA4LjE3MzE3QzIwLjczNjMgNi45NTk5MSAxOS45OTk3IDUuODU3NTIgMTkuMDcxMSA0LjkyODkzQzE4LjE0MjUgNC4wMDAzNSAxNy4wNDAxIDMuMjYzNzUgMTUuODI2OCAyLjc2MTJDMTQuNjEzNiAyLjI1ODY2IDEzLjMxMzIgMiAxMiAyWk0xMiAyMEMxMC40MTc4IDIwIDguODcxMDQgMTkuNTMwOCA3LjU1NTQ0IDE4LjY1MThDNi4yMzk4NSAxNy43NzI3IDUuMjE0NDcgMTYuNTIzMyA0LjYwODk3IDE1LjA2MTVDNC4wMDM0NyAxMy41OTk3IDMuODQ1MDQgMTEuOTkxMSA0LjE1MzcyIDEwLjQzOTNDNC40NjI0IDguODg3NDMgNS4yMjQzMyA3LjQ2MTk3IDYuMzQzMTUgNi4zNDMxNUM3LjQ2MTk3IDUuMjI0MzMgOC44ODc0MyA0LjQ2MjQgMTAuNDM5MyA0LjE1MzcyQzExLjk5MTEgMy44NDUwNCAxMy41OTk3IDQuMDAzNDYgMTUuMDYxNSA0LjYwODk2QzE2LjUyMzMgNS4yMTQ0NyAxNy43NzI3IDYuMjM5ODQgMTguNjUxOCA3LjU1NTQ0QzE5LjUzMDggOC44NzEwMyAyMCAxMC40MTc3IDIwIDEyQzIwIDE0LjEyMTcgMTkuMTU3MiAxNi4xNTY2IDE3LjY1NjkgMTcuNjU2OUMxNi4xNTY2IDE5LjE1NzEgMTQuMTIxNyAyMCAxMiAyMFoiPjwvcGF0aD48L3N2Zz4=)Note

Work in progress

## Linter

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Linter"]](#linter)

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTFDMTEuNzM0OCAxMSAxMS40ODA0IDExLjEwNTQgMTEuMjkyOSAxMS4yOTI5QzExLjEwNTQgMTEuNDgwNCAxMSAxMS43MzQ4IDExIDEyVjE2QzExIDE2LjI2NTIgMTEuMTA1NCAxNi41MTk2IDExLjI5MjkgMTYuNzA3MUMxMS40ODA0IDE2Ljg5NDYgMTEuNzM0OCAxNyAxMiAxN0MxMi4yNjUyIDE3IDEyLjUxOTYgMTYuODk0NiAxMi43MDcxIDE2LjcwNzFDMTIuODk0NiAxNi41MTk2IDEzIDE2LjI2NTIgMTMgMTZWMTJDMTMgMTEuNzM0OCAxMi44OTQ2IDExLjQ4MDQgMTIuNzA3MSAxMS4yOTI5QzEyLjUxOTYgMTEuMTA1NCAxMi4yNjUyIDExIDEyIDExWk0xMi4zOCA3LjA4QzEyLjEzNjUgNi45Nzk5OCAxMS44NjM1IDYuOTc5OTggMTEuNjIgNy4wOEMxMS40OTczIDcuMTI3NTkgMTEuMzg1MSA3LjE5ODk2IDExLjI5IDcuMjlDMTEuMjAxNyA3LjM4NzIgMTEuMTMwNiA3LjQ5ODgyIDExLjA4IDcuNjJDMTEuMDI0IDcuNzM4NjggMTAuOTk2NiA3Ljg2ODgyIDExIDhDMTAuOTk5MiA4LjEzMTYxIDExLjAyNDUgOC4yNjIwNyAxMS4wNzQyIDguMzgzOTFDMTEuMTI0IDguNTA1NzQgMTEuMTk3MyA4LjYxNjU2IDExLjI5IDguNzFDMTEuMzg3MiA4Ljc5ODMzIDExLjQ5ODggOC44NjkzNiAxMS42MiA4LjkyQzExLjc3MTUgOC45ODIyNCAxMS45MzYgOS4wMDYzMiAxMi4wOTkgOC45OTAxMUMxMi4yNjE5IDguOTczOTEgMTIuNDE4NCA4LjkxNzkyIDEyLjU1NDcgOC44MjcwN0MxMi42OTEgOC43MzYyMiAxMi44MDI5IDguNjEzMjggMTIuODgwNSA4LjQ2OTA3QzEyLjk1ODIgOC4zMjQ4NiAxMi45OTkyIDguMTYzNzggMTMgOEMxMi45OTYzIDcuNzM1MjMgMTIuODkyNyA3LjQ4MTYzIDEyLjcxIDcuMjlDMTIuNjE0OSA3LjE5ODk2IDEyLjUwMjggNy4xMjc1OSAxMi4zOCA3LjA4Wk0xMiAyQzEwLjAyMjIgMiA4LjA4ODc5IDIuNTg2NDkgNi40NDQzIDMuNjg1M0M0Ljc5OTgxIDQuNzg0MTIgMy41MTgwOSA2LjM0NTkgMi43NjEyMSA4LjE3MzE3QzIuMDA0MzMgMTAuMDAwNCAxLjgwNjMgMTIuMDExMSAyLjE5MjE1IDEzLjk1MDlDMi41NzggMTUuODkwNyAzLjUzMDQxIDE3LjY3MjUgNC45Mjg5NCAxOS4wNzExQzYuMzI3NDYgMjAuNDY5NiA4LjEwOTI5IDIxLjQyMiAxMC4wNDkxIDIxLjgwNzlDMTEuOTg4OSAyMi4xOTM3IDEzLjk5OTYgMjEuOTk1NyAxNS44MjY4IDIxLjIzODhDMTcuNjU0MSAyMC40ODE5IDE5LjIxNTkgMTkuMjAwMiAyMC4zMTQ3IDE3LjU1NTdDMjEuNDEzNSAxNS45MTEyIDIyIDEzLjk3NzggMjIgMTJDMjIgMTAuNjg2OCAyMS43NDEzIDkuMzg2NDIgMjEuMjM4OCA4LjE3MzE3QzIwLjczNjMgNi45NTk5MSAxOS45OTk3IDUuODU3NTIgMTkuMDcxMSA0LjkyODkzQzE4LjE0MjUgNC4wMDAzNSAxNy4wNDAxIDMuMjYzNzUgMTUuODI2OCAyLjc2MTJDMTQuNjEzNiAyLjI1ODY2IDEzLjMxMzIgMiAxMiAyWk0xMiAyMEMxMC40MTc4IDIwIDguODcxMDQgMTkuNTMwOCA3LjU1NTQ0IDE4LjY1MThDNi4yMzk4NSAxNy43NzI3IDUuMjE0NDcgMTYuNTIzMyA0LjYwODk3IDE1LjA2MTVDNC4wMDM0NyAxMy41OTk3IDMuODQ1MDQgMTEuOTkxMSA0LjE1MzcyIDEwLjQzOTNDNC40NjI0IDguODg3NDMgNS4yMjQzMyA3LjQ2MTk3IDYuMzQzMTUgNi4zNDMxNUM3LjQ2MTk3IDUuMjI0MzMgOC44ODc0MyA0LjQ2MjQgMTAuNDM5MyA0LjE1MzcyQzExLjk5MTEgMy44NDUwNCAxMy41OTk3IDQuMDAzNDYgMTUuMDYxNSA0LjYwODk2QzE2LjUyMzMgNS4yMTQ0NyAxNy43NzI3IDYuMjM5ODQgMTguNjUxOCA3LjU1NTQ0QzE5LjUzMDggOC44NzEwMyAyMCAxMC40MTc3IDIwIDEyQzIwIDE0LjEyMTcgMTkuMTU3MiAxNi4xNTY2IDE3LjY1NjkgMTcuNjU2OUMxNi4xNTY2IDE5LjE1NzEgMTQuMTIxNyAyMCAxMiAyMFoiPjwvcGF0aD48L3N2Zz4=)Note

Work in progress

## Daemon

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Daemon"]](#daemon)

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTFDMTEuNzM0OCAxMSAxMS40ODA0IDExLjEwNTQgMTEuMjkyOSAxMS4yOTI5QzExLjEwNTQgMTEuNDgwNCAxMSAxMS43MzQ4IDExIDEyVjE2QzExIDE2LjI2NTIgMTEuMTA1NCAxNi41MTk2IDExLjI5MjkgMTYuNzA3MUMxMS40ODA0IDE2Ljg5NDYgMTEuNzM0OCAxNyAxMiAxN0MxMi4yNjUyIDE3IDEyLjUxOTYgMTYuODk0NiAxMi43MDcxIDE2LjcwNzFDMTIuODk0NiAxNi41MTk2IDEzIDE2LjI2NTIgMTMgMTZWMTJDMTMgMTEuNzM0OCAxMi44OTQ2IDExLjQ4MDQgMTIuNzA3MSAxMS4yOTI5QzEyLjUxOTYgMTEuMTA1NCAxMi4yNjUyIDExIDEyIDExWk0xMi4zOCA3LjA4QzEyLjEzNjUgNi45Nzk5OCAxMS44NjM1IDYuOTc5OTggMTEuNjIgNy4wOEMxMS40OTczIDcuMTI3NTkgMTEuMzg1MSA3LjE5ODk2IDExLjI5IDcuMjlDMTEuMjAxNyA3LjM4NzIgMTEuMTMwNiA3LjQ5ODgyIDExLjA4IDcuNjJDMTEuMDI0IDcuNzM4NjggMTAuOTk2NiA3Ljg2ODgyIDExIDhDMTAuOTk5MiA4LjEzMTYxIDExLjAyNDUgOC4yNjIwNyAxMS4wNzQyIDguMzgzOTFDMTEuMTI0IDguNTA1NzQgMTEuMTk3MyA4LjYxNjU2IDExLjI5IDguNzFDMTEuMzg3MiA4Ljc5ODMzIDExLjQ5ODggOC44NjkzNiAxMS42MiA4LjkyQzExLjc3MTUgOC45ODIyNCAxMS45MzYgOS4wMDYzMiAxMi4wOTkgOC45OTAxMUMxMi4yNjE5IDguOTczOTEgMTIuNDE4NCA4LjkxNzkyIDEyLjU1NDcgOC44MjcwN0MxMi42OTEgOC43MzYyMiAxMi44MDI5IDguNjEzMjggMTIuODgwNSA4LjQ2OTA3QzEyLjk1ODIgOC4zMjQ4NiAxMi45OTkyIDguMTYzNzggMTMgOEMxMi45OTYzIDcuNzM1MjMgMTIuODkyNyA3LjQ4MTYzIDEyLjcxIDcuMjlDMTIuNjE0OSA3LjE5ODk2IDEyLjUwMjggNy4xMjc1OSAxMi4zOCA3LjA4Wk0xMiAyQzEwLjAyMjIgMiA4LjA4ODc5IDIuNTg2NDkgNi40NDQzIDMuNjg1M0M0Ljc5OTgxIDQuNzg0MTIgMy41MTgwOSA2LjM0NTkgMi43NjEyMSA4LjE3MzE3QzIuMDA0MzMgMTAuMDAwNCAxLjgwNjMgMTIuMDExMSAyLjE5MjE1IDEzLjk1MDlDMi41NzggMTUuODkwNyAzLjUzMDQxIDE3LjY3MjUgNC45Mjg5NCAxOS4wNzExQzYuMzI3NDYgMjAuNDY5NiA4LjEwOTI5IDIxLjQyMiAxMC4wNDkxIDIxLjgwNzlDMTEuOTg4OSAyMi4xOTM3IDEzLjk5OTYgMjEuOTk1NyAxNS44MjY4IDIxLjIzODhDMTcuNjU0MSAyMC40ODE5IDE5LjIxNTkgMTkuMjAwMiAyMC4zMTQ3IDE3LjU1NTdDMjEuNDEzNSAxNS45MTEyIDIyIDEzLjk3NzggMjIgMTJDMjIgMTAuNjg2OCAyMS43NDEzIDkuMzg2NDIgMjEuMjM4OCA4LjE3MzE3QzIwLjczNjMgNi45NTk5MSAxOS45OTk3IDUuODU3NTIgMTkuMDcxMSA0LjkyODkzQzE4LjE0MjUgNC4wMDAzNSAxNy4wNDAxIDMuMjYzNzUgMTUuODI2OCAyLjc2MTJDMTQuNjEzNiAyLjI1ODY2IDEzLjMxMzIgMiAxMiAyWk0xMiAyMEMxMC40MTc4IDIwIDguODcxMDQgMTkuNTMwOCA3LjU1NTQ0IDE4LjY1MThDNi4yMzk4NSAxNy43NzI3IDUuMjE0NDcgMTYuNTIzMyA0LjYwODk3IDE1LjA2MTVDNC4wMDM0NyAxMy41OTk3IDMuODQ1MDQgMTEuOTkxMSA0LjE1MzcyIDEwLjQzOTNDNC40NjI0IDguODg3NDMgNS4yMjQzMyA3LjQ2MTk3IDYuMzQzMTUgNi4zNDMxNUM3LjQ2MTk3IDUuMjI0MzMgOC44ODc0MyA0LjQ2MjQgMTAuNDM5MyA0LjE1MzcyQzExLjk5MTEgMy44NDUwNCAxMy41OTk3IDQuMDAzNDYgMTUuMDYxNSA0LjYwODk2QzE2LjUyMzMgNS4yMTQ0NyAxNy43NzI3IDYuMjM5ODQgMTguNjUxOCA3LjU1NTQ0QzE5LjUzMDggOC44NzEwMyAyMCAxMC40MTc3IDIwIDEyQzIwIDE0LjEyMTcgMTkuMTU3MiAxNi4xNTY2IDE3LjY1NjkgMTcuNjU2OUMxNi4xNTY2IDE5LjE1NzEgMTQuMTIxNyAyMCAxMiAyMFoiPjwvcGF0aD48L3N2Zz4=)Note

Work in progress

Biome uses a server-client architecture to run its tasks.

A [daemon](https://en.wikipedia.org/wiki/Daemon_(computing)) is a long-running server that Biome spawns in the background and uses to process requests from the editor and CLI.

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/internals/architecture.mdx)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Language support] ]](/internals/language-support) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[People and Credits] ]](/internals/people-and-credits)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.