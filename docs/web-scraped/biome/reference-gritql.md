# Source: https://biomejs.dev/reference/gritql/

# GritQL 

GritQL is a query language for performing structural searches on source code. This means that trivia such as whitespace or even the type of quotes used in strings will be ignored in your search query. In addition, it offers many features that allow you to query syntax structure such as snippets, matching, nesting, and variables.

GritQL is [open-source](https://github.com/getgrit/gritql/) and created by [Grit.io](https://grit.io/).

Biome uses GritQL for two purposes:

-   The [Analyzer Plugins](/linter/plugins).
-   The [`biome search`](/reference/cli/#biome-search) command, which we hope to extend to our IDE extensions as well.

## Patterns

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Patterns"]](#patterns)

GritQL queries work through *patterns*. The most common pattern you will see is the code snippet, which looks like ordinary source code wrapped in backticks:

<figure class="frame not-content">
<pre data-language="grit"><code>1`console.log(&#39;Hello, world!&#39;)`</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

This pattern will match any call to `console.log()` that is passed the string `'Hello, world!'`. But because GritQL does *structural* matching, it doesn't care about formatting details. This also matches:

<figure class="frame not-content">
<pre data-language="js"><code>1console.log (2    &#39;Hello, world!&#39;3)</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

And so does this (note the change in quotes):

<figure class="frame not-content">
<pre data-language="js"><code>1console.log(&quot;Hello, world!&quot;)</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTFDMTEuNzM0OCAxMSAxMS40ODA0IDExLjEwNTQgMTEuMjkyOSAxMS4yOTI5QzExLjEwNTQgMTEuNDgwNCAxMSAxMS43MzQ4IDExIDEyVjE2QzExIDE2LjI2NTIgMTEuMTA1NCAxNi41MTk2IDExLjI5MjkgMTYuNzA3MUMxMS40ODA0IDE2Ljg5NDYgMTEuNzM0OCAxNyAxMiAxN0MxMi4yNjUyIDE3IDEyLjUxOTYgMTYuODk0NiAxMi43MDcxIDE2LjcwNzFDMTIuODk0NiAxNi41MTk2IDEzIDE2LjI2NTIgMTMgMTZWMTJDMTMgMTEuNzM0OCAxMi44OTQ2IDExLjQ4MDQgMTIuNzA3MSAxMS4yOTI5QzEyLjUxOTYgMTEuMTA1NCAxMi4yNjUyIDExIDEyIDExWk0xMi4zOCA3LjA4QzEyLjEzNjUgNi45Nzk5OCAxMS44NjM1IDYuOTc5OTggMTEuNjIgNy4wOEMxMS40OTczIDcuMTI3NTkgMTEuMzg1MSA3LjE5ODk2IDExLjI5IDcuMjlDMTEuMjAxNyA3LjM4NzIgMTEuMTMwNiA3LjQ5ODgyIDExLjA4IDcuNjJDMTEuMDI0IDcuNzM4NjggMTAuOTk2NiA3Ljg2ODgyIDExIDhDMTAuOTk5MiA4LjEzMTYxIDExLjAyNDUgOC4yNjIwNyAxMS4wNzQyIDguMzgzOTFDMTEuMTI0IDguNTA1NzQgMTEuMTk3MyA4LjYxNjU2IDExLjI5IDguNzFDMTEuMzg3MiA4Ljc5ODMzIDExLjQ5ODggOC44NjkzNiAxMS42MiA4LjkyQzExLjc3MTUgOC45ODIyNCAxMS45MzYgOS4wMDYzMiAxMi4wOTkgOC45OTAxMUMxMi4yNjE5IDguOTczOTEgMTIuNDE4NCA4LjkxNzkyIDEyLjU1NDcgOC44MjcwN0MxMi42OTEgOC43MzYyMiAxMi44MDI5IDguNjEzMjggMTIuODgwNSA4LjQ2OTA3QzEyLjk1ODIgOC4zMjQ4NiAxMi45OTkyIDguMTYzNzggMTMgOEMxMi45OTYzIDcuNzM1MjMgMTIuODkyNyA3LjQ4MTYzIDEyLjcxIDcuMjlDMTIuNjE0OSA3LjE5ODk2IDEyLjUwMjggNy4xMjc1OSAxMi4zOCA3LjA4Wk0xMiAyQzEwLjAyMjIgMiA4LjA4ODc5IDIuNTg2NDkgNi40NDQzIDMuNjg1M0M0Ljc5OTgxIDQuNzg0MTIgMy41MTgwOSA2LjM0NTkgMi43NjEyMSA4LjE3MzE3QzIuMDA0MzMgMTAuMDAwNCAxLjgwNjMgMTIuMDExMSAyLjE5MjE1IDEzLjk1MDlDMi41NzggMTUuODkwNyAzLjUzMDQxIDE3LjY3MjUgNC45Mjg5NCAxOS4wNzExQzYuMzI3NDYgMjAuNDY5NiA4LjEwOTI5IDIxLjQyMiAxMC4wNDkxIDIxLjgwNzlDMTEuOTg4OSAyMi4xOTM3IDEzLjk5OTYgMjEuOTk1NyAxNS44MjY4IDIxLjIzODhDMTcuNjU0MSAyMC40ODE5IDE5LjIxNTkgMTkuMjAwMiAyMC4zMTQ3IDE3LjU1NTdDMjEuNDEzNSAxNS45MTEyIDIyIDEzLjk3NzggMjIgMTJDMjIgMTAuNjg2OCAyMS43NDEzIDkuMzg2NDIgMjEuMjM4OCA4LjE3MzE3QzIwLjczNjMgNi45NTk5MSAxOS45OTk3IDUuODU3NTIgMTkuMDcxMSA0LjkyODkzQzE4LjE0MjUgNC4wMDAzNSAxNy4wNDAxIDMuMjYzNzUgMTUuODI2OCAyLjc2MTJDMTQuNjEzNiAyLjI1ODY2IDEzLjMxMzIgMiAxMiAyWk0xMiAyMEMxMC40MTc4IDIwIDguODcxMDQgMTkuNTMwOCA3LjU1NTQ0IDE4LjY1MThDNi4yMzk4NSAxNy43NzI3IDUuMjE0NDcgMTYuNTIzMyA0LjYwODk3IDE1LjA2MTVDNC4wMDM0NyAxMy41OTk3IDMuODQ1MDQgMTEuOTkxMSA0LjE1MzcyIDEwLjQzOTNDNC40NjI0IDguODg3NDMgNS4yMjQzMyA3LjQ2MTk3IDYuMzQzMTUgNi4zNDMxNUM3LjQ2MTk3IDUuMjI0MzMgOC44ODc0MyA0LjQ2MjQgMTAuNDM5MyA0LjE1MzcyQzExLjk5MTEgMy44NDUwNCAxMy41OTk3IDQuMDAzNDYgMTUuMDYxNSA0LjYwODk2QzE2LjUyMzMgNS4yMTQ0NyAxNy43NzI3IDYuMjM5ODQgMTguNjUxOCA3LjU1NTQ0QzE5LjUzMDggOC44NzEwMyAyMCAxMC40MTc3IDIwIDEyQzIwIDE0LjEyMTcgMTkuMTU3MiAxNi4xNTY2IDE3LjY1NjkgMTcuNjU2OUMxNi4xNTY2IDE5LjE1NzEgMTQuMTIxNyAyMCAxMiAyMFoiPjwvcGF0aD48L3N2Zz4=)Note

Most shells interpret backticks as command invocations, which conflicts with GritQL's code snippets. So when using the `biome search` command, it's best to put *single quotes* around your Grit queries:

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome search &#39;`console.log($message)`&#39; # find all `console.log` invocations</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

## Variables

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Variables"]](#variables)

GritQL queries can also have *variables*. The following will match any call to `console.log()` regardless of the message passed:

<figure class="frame not-content">
<pre data-language="grit"><code>1`console.log($message)`</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

This will match any of the methods on the `console` object too:

<figure class="frame not-content">
<pre data-language="grit"><code>1`console.$method($message)`</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

The same variable name can occur multiple times in a single snippet:

<figure class="frame not-content">
<pre data-language="grit"><code>1`$fn &amp;&amp; $fn()`</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

This will match `foo && foo()`, and even `foo.bar && foo.bar()`, but not `foo && bar()`.

## Conditions

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Conditions"]](#conditions)

You can add conditions to patterns by using the `where` operator. This is commonly used together with the *match operator*, `<:`:

<figure class="frame not-content">
<pre data-language="grit"><code>1`console.$method($message)` where </code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

This query is identical to the `console.log($message)` pattern we saw earlier, but it gets quickly more interesting when add other operators in the mix:

<figure class="frame not-content">
<pre data-language="grit"><code>1`console.$method($message)` where 3}</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

## Matching Biome Syntax Nodes

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Matching Biome Syntax Nodes"]](#matching-biome-syntax-nodes)

For more precise queries, you can match against Biome's internal syntax nodes directly. Each node is identified by a unique `PascalCase` name.

For example, to find all JavaScript `if` statements, you can match the `JsIfStatement` node:

<figure class="frame not-content">
<pre data-language="grit"><code>1engine biome(1.0)2language js(typescript,jsx)3
4JsIfStatement() as $stmt where </code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

You can discover node names for your code by exploring the syntax tree in the [Biome Playground](https://biomejs.dev/playground/). A complete list of all available nodes is also available in the `.ungram` files in the [`xtask/codegen`](https://github.com/biomejs/biome/tree/main/xtask/codegen) directory of the Biome repository.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTZDMTEuODAyMiAxNiAxMS42MDg5IDE2LjA1ODcgMTEuNDQ0NCAxNi4xNjg2QzExLjI4IDE2LjI3ODQgMTEuMTUxOCAxNi40MzQ2IDExLjA3NjEgMTYuNjE3M0MxMS4wMDA0IDE2LjgwMDEgMTAuOTgwNiAxNy4wMDExIDExLjAxOTIgMTcuMTk1MUMxMS4wNTc4IDE3LjM4OTEgMTEuMTUzIDE3LjU2NzMgMTEuMjkyOSAxNy43MDcxQzExLjQzMjcgMTcuODQ3IDExLjYxMDkgMTcuOTQyMiAxMS44MDQ5IDE3Ljk4MDhDMTEuOTk4OSAxOC4wMTk0IDEyLjIgMTcuOTk5NiAxMi4zODI3IDE3LjkyMzlDMTIuNTY1NCAxNy44NDgyIDEyLjcyMTYgMTcuNzIgMTIuODMxNSAxNy41NTU2QzEyLjk0MTMgMTcuMzkxMSAxMyAxNy4xOTc4IDEzIDE3QzEzIDE2LjczNDggMTIuODk0NiAxNi40ODA1IDEyLjcwNzEgMTYuMjkyOUMxMi41MTk2IDE2LjEwNTQgMTIuMjY1MiAxNiAxMiAxNlpNMjIuNjcgMTcuNDdMMTQuNjIgMy40NzAwM0MxNC4zNTk4IDMuMDAzNTQgMTMuOTc5OCAyLjYxNDk4IDEzLjUxOTIgMi4zNDQ1QzEzLjA1ODYgMi4wNzQwMSAxMi41MzQxIDEuOTMxNCAxMiAxLjkzMTRDMTEuNDY1OSAxLjkzMTQgMTAuOTQxNCAyLjA3NDAxIDEwLjQ4MDggMi4zNDQ1QzEwLjAyMDIgMi42MTQ5OCA5LjY0MDE5IDMuMDAzNTQgOS4zOCAzLjQ3MDAzTDEuMzggMTcuNDdDMS4xMTA3OSAxNy45MjQgMC45NjYxNDEgMTguNDQxIDAuOTYwNjQzIDE4Ljk2ODhDMC45NTUxNDQgMTkuNDk2NiAxLjA4OSAyMC4wMTY2IDEuMzQ4NjggMjAuNDc2MUMxLjYwODM3IDIwLjkzNTYgMS45ODQ3IDIxLjMxODUgMi40Mzk2OCAyMS41ODYxQzIuODk0NjYgMjEuODUzNiAzLjQxMjE4IDIxLjk5NjQgMy45NCAyMkgyMC4wNkMyMC41OTIxIDIyLjAwNTMgMjEuMTE1OSAyMS44Njg5IDIxLjU3NzkgMjEuNjA0OUMyMi4wMzk5IDIxLjM0MSAyMi40MjM0IDIwLjk1ODkgMjIuNjg5IDIwLjQ5NzhDMjIuOTU0NiAyMC4wMzY4IDIzLjA5MjggMTkuNTEzNCAyMy4wODk1IDE4Ljk4MTRDMjMuMDg2MiAxOC40NDkzIDIyLjk0MTQgMTcuOTI3NyAyMi42NyAxNy40N1pNMjAuOTQgMTkuNDdDMjAuODUyMyAxOS42MjYgMjAuNzI0NSAxOS43NTU2IDIwLjU2OTcgMTkuODQ1M0MyMC40MTQ5IDE5LjkzNSAyMC4yMzg5IDE5Ljk4MTUgMjAuMDYgMTkuOThIMy45NEMzLjc2MTExIDE5Ljk4MTUgMy41ODUxIDE5LjkzNSAzLjQzMDMyIDE5Ljg0NTNDMy4yNzU1MyAxOS43NTU2IDMuMTQ3NjUgMTkuNjI2IDMuMDYgMTkuNDdDMi45NzIyMyAxOS4zMTggMi45MjYwMiAxOS4xNDU2IDIuOTI2MDIgMTguOTdDMi45MjYwMiAxOC43OTQ1IDIuOTcyMjMgMTguNjIyIDMuMDYgMTguNDdMMTEuMDYgNC40NzAwM0MxMS4xNDM5IDQuMzA2MjMgMTEuMjcxNCA0LjE2ODc2IDExLjQyODQgNC4wNzI3N0MxMS41ODU1IDMuOTc2NzggMTEuNzY2IDMuOTI1OTkgMTEuOTUgMy45MjU5OUMxMi4xMzQgMy45MjU5OSAxMi4zMTQ1IDMuOTc2NzggMTIuNDcxNiA0LjA3Mjc3QzEyLjYyODYgNC4xNjg3NiAxMi43NTYxIDQuMzA2MjMgMTIuODQgNC40NzAwM0wyMC44OSAxOC40N0MyMC45ODkyIDE4LjYxOTkgMjEuMDQ2MiAxOC43OTM3IDIxLjA1NSAxOC45NzMyQzIxLjA2MzggMTkuMTUyNyAyMS4wMjQxIDE5LjMzMTIgMjAuOTQgMTkuNDlWMTkuNDdaTTEyIDguMDAwMDNDMTEuNzM0OCA4LjAwMDAzIDExLjQ4MDQgOC4xMDUzOCAxMS4yOTI5IDguMjkyOTJDMTEuMTA1NCA4LjQ4MDQ2IDExIDguNzM0ODEgMTEgOS4wMDAwM1YxM0MxMSAxMy4yNjUyIDExLjEwNTQgMTMuNTE5NiAxMS4yOTI5IDEzLjcwNzFDMTEuNDgwNCAxMy44OTQ3IDExLjczNDggMTQgMTIgMTRDMTIuMjY1MiAxNCAxMi41MTk2IDEzLjg5NDcgMTIuNzA3MSAxMy43MDcxQzEyLjg5NDYgMTMuNTE5NiAxMyAxMy4yNjUyIDEzIDEzVjkuMDAwMDNDMTMgOC43MzQ4MSAxMi44OTQ2IDguNDgwNDYgMTIuNzA3MSA4LjI5MjkyQzEyLjUxOTYgOC4xMDUzOCAxMi4yNjUyIDguMDAwMDMgMTIgOC4wMDAwM1oiPjwvcGF0aD48L3N2Zz4=)Caution

Biome's grammar can change between versions, especially for new languages. This may cause node names to change, which could break your patterns. Be prepared to update your queries when upgrading Biome.

## Language Documentation

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Language Documentation"]](#language-documentation)

For more information about GritQL and its syntax, see the official [GritQL Language Documentation](https://docs.grit.io/language/overview).

Please keep in mind that Biome doesn't support all of Grit's features (yet).

## Integration Status

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Integration Status"]](#integration-status)

GritQL support in Biome is actively being worked on. Many things already work, but bugs are still expected and some features are still outright missing.

For a detailed overview of which GritQL features are supported and which are still in-progress, please see the GitHub issue: <https://github.com/biomejs/biome/issues/2582>.

We also have a detailed RFC which guides the direction for our plugin efforts: <https://github.com/biomejs/biome/discussions/1762>

**tl;dr**: We are working on supporting plugins, which can be either pure GritQL plugins or JS/TS plugins that use GritQL to select the code they wish to operate on. Stay tuned!

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/reference/gritql.mdx)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Zed extension] ]](/reference/zed) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[Continuous Integration] ]](/recipes/continuous-integration)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.