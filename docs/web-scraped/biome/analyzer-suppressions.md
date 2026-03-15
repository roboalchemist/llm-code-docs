# Source: https://biomejs.dev/analyzer/suppressions/

# Suppressions 

The Biome analyzer is the foundation of the [linter](/linter) and [assist](/assist); in fact, both tools share a lot of similarities.

Among them, they share the same suppression engine, which means that you can suppress a lint rule the same way you would suppress an assist action.

With suppression, it's possible to turn off a lint rule (or action) for a specific line of code, a range, or the entire file.

Suppression is achievable with **suppression comments**.

## Suppression syntax

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Suppression syntax"]](#suppression-syntax)

Suppression comments have the following format:

<figure class="frame not-content">
<pre data-language="js"><code>1// biome-ignore lint: &lt;explanation&gt;2// biome-ignore assist: &lt;explanation&gt;3// biome-ignore syntax: &lt;explanation&gt;4// biome-ignore lint/suspicious: &lt;explanation&gt;5// biome-ignore lint/suspicious/noDebugger: &lt;explanation&gt;6// biome-ignore lint/suspicious/noDebugger(foo): &lt;explanation&gt;7// biome-ignore-all lint: &lt;explanation&gt;8// biome-ignore-start lint: &lt;explanation&gt;9// biome-ignore-end lint: &lt;explanation&gt;</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

Let's break it down:

-   `biome-ignore`, `biome-ignore-all`, `biome-ignore-start` and `biome-ignore-end` are the start of a suppression comment.
-   After the space follows the **category** of the suppression comment. It can be `lint`, `assist`, or `syntax`.
-   The category is followed by an optional group, or group and name, separated by slashes. For example, `/suspicious` or `/suspicious/noDebugger`. The more you specify, the more specific (i.e. targeted) your suppression is.
-   Some rules even allow you to specify values during suppression. These can be specified between parentheses, for example: `(foo)`. Refer to the rule documentation to see whether a rule supports suppression with values.
-   `<explanation>` explanation why the rule is disabled.

If you're unsure of the exact category of a rule/action, you can refer to their documentation page and use their *diagnostic category*.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTFDMTEuNzM0OCAxMSAxMS40ODA0IDExLjEwNTQgMTEuMjkyOSAxMS4yOTI5QzExLjEwNTQgMTEuNDgwNCAxMSAxMS43MzQ4IDExIDEyVjE2QzExIDE2LjI2NTIgMTEuMTA1NCAxNi41MTk2IDExLjI5MjkgMTYuNzA3MUMxMS40ODA0IDE2Ljg5NDYgMTEuNzM0OCAxNyAxMiAxN0MxMi4yNjUyIDE3IDEyLjUxOTYgMTYuODk0NiAxMi43MDcxIDE2LjcwNzFDMTIuODk0NiAxNi41MTk2IDEzIDE2LjI2NTIgMTMgMTZWMTJDMTMgMTEuNzM0OCAxMi44OTQ2IDExLjQ4MDQgMTIuNzA3MSAxMS4yOTI5QzEyLjUxOTYgMTEuMTA1NCAxMi4yNjUyIDExIDEyIDExWk0xMi4zOCA3LjA4QzEyLjEzNjUgNi45Nzk5OCAxMS44NjM1IDYuOTc5OTggMTEuNjIgNy4wOEMxMS40OTczIDcuMTI3NTkgMTEuMzg1MSA3LjE5ODk2IDExLjI5IDcuMjlDMTEuMjAxNyA3LjM4NzIgMTEuMTMwNiA3LjQ5ODgyIDExLjA4IDcuNjJDMTEuMDI0IDcuNzM4NjggMTAuOTk2NiA3Ljg2ODgyIDExIDhDMTAuOTk5MiA4LjEzMTYxIDExLjAyNDUgOC4yNjIwNyAxMS4wNzQyIDguMzgzOTFDMTEuMTI0IDguNTA1NzQgMTEuMTk3MyA4LjYxNjU2IDExLjI5IDguNzFDMTEuMzg3MiA4Ljc5ODMzIDExLjQ5ODggOC44NjkzNiAxMS42MiA4LjkyQzExLjc3MTUgOC45ODIyNCAxMS45MzYgOS4wMDYzMiAxMi4wOTkgOC45OTAxMUMxMi4yNjE5IDguOTczOTEgMTIuNDE4NCA4LjkxNzkyIDEyLjU1NDcgOC44MjcwN0MxMi42OTEgOC43MzYyMiAxMi44MDI5IDguNjEzMjggMTIuODgwNSA4LjQ2OTA3QzEyLjk1ODIgOC4zMjQ4NiAxMi45OTkyIDguMTYzNzggMTMgOEMxMi45OTYzIDcuNzM1MjMgMTIuODkyNyA3LjQ4MTYzIDEyLjcxIDcuMjlDMTIuNjE0OSA3LjE5ODk2IDEyLjUwMjggNy4xMjc1OSAxMi4zOCA3LjA4Wk0xMiAyQzEwLjAyMjIgMiA4LjA4ODc5IDIuNTg2NDkgNi40NDQzIDMuNjg1M0M0Ljc5OTgxIDQuNzg0MTIgMy41MTgwOSA2LjM0NTkgMi43NjEyMSA4LjE3MzE3QzIuMDA0MzMgMTAuMDAwNCAxLjgwNjMgMTIuMDExMSAyLjE5MjE1IDEzLjk1MDlDMi41NzggMTUuODkwNyAzLjUzMDQxIDE3LjY3MjUgNC45Mjg5NCAxOS4wNzExQzYuMzI3NDYgMjAuNDY5NiA4LjEwOTI5IDIxLjQyMiAxMC4wNDkxIDIxLjgwNzlDMTEuOTg4OSAyMi4xOTM3IDEzLjk5OTYgMjEuOTk1NyAxNS44MjY4IDIxLjIzODhDMTcuNjU0MSAyMC40ODE5IDE5LjIxNTkgMTkuMjAwMiAyMC4zMTQ3IDE3LjU1NTdDMjEuNDEzNSAxNS45MTEyIDIyIDEzLjk3NzggMjIgMTJDMjIgMTAuNjg2OCAyMS43NDEzIDkuMzg2NDIgMjEuMjM4OCA4LjE3MzE3QzIwLjczNjMgNi45NTk5MSAxOS45OTk3IDUuODU3NTIgMTkuMDcxMSA0LjkyODkzQzE4LjE0MjUgNC4wMDAzNSAxNy4wNDAxIDMuMjYzNzUgMTUuODI2OCAyLjc2MTJDMTQuNjEzNiAyLjI1ODY2IDEzLjMxMzIgMiAxMiAyWk0xMiAyMEMxMC40MTc4IDIwIDguODcxMDQgMTkuNTMwOCA3LjU1NTQ0IDE4LjY1MThDNi4yMzk4NSAxNy43NzI3IDUuMjE0NDcgMTYuNTIzMyA0LjYwODk3IDE1LjA2MTVDNC4wMDM0NyAxMy41OTk3IDMuODQ1MDQgMTEuOTkxMSA0LjE1MzcyIDEwLjQzOTNDNC40NjI0IDguODg3NDMgNS4yMjQzMyA3LjQ2MTk3IDYuMzQzMTUgNi4zNDMxNUM3LjQ2MTk3IDUuMjI0MzMgOC44ODc0MyA0LjQ2MjQgMTAuNDM5MyA0LjE1MzcyQzExLjk5MTEgMy44NDUwNCAxMy41OTk3IDQuMDAzNDYgMTUuMDYxNSA0LjYwODk2QzE2LjUyMzMgNS4yMTQ0NyAxNy43NzI3IDYuMjM5ODQgMTguNjUxOCA3LjU1NTQ0QzE5LjUzMDggOC44NzEwMyAyMCAxMC40MTc3IDIwIDEyQzIwIDE0LjEyMTcgMTkuMTU3MiAxNi4xNTY2IDE3LjY1NjkgMTcuNjU2OUMxNi4xNTY2IDE5LjE1NzEgMTQuMTIxNyAyMCAxMiAyMFoiPjwvcGF0aD48L3N2Zz4=)Note

From here onwards, JavaScript is used to explain suppression comments, and the `lint` category is used.

### Inline suppressions

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Inline suppressions"]](#inline-suppressions)

They disable a lint rule for the **next line** of code.

In the following example, the suppression comment `biome-ignore lint/suspicious/noDebugger: reason` will disable the `debugger;` statement at line 2, but the `debugger` at line 3 will still raise a diagnostic:

<figure class="frame has-title not-content">
<pre data-language="js"><code>1// biome-ignore lint/suspicious/noDebugger: reason2debugger;3debugger;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">file.js</span></figcaption>
</figure>

### Top-level suppressions

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Top-level suppressions"]](#top-level-suppressions)

They disable a lint rule for an entire file. They must be placed **at the top of the file**, and they must start with `biome-ignore-all`.

These suppression comments are very useful when you want to suppress some lint rule *for a particular file*, and you don't want to rely on a single configuration override to achieve that.

In the following example, the suppression comment `biome-ignore-all lint/suspicious/noDebugger: reason` will disable the lint rule for all lines in `generated.js`:

<figure class="frame has-title not-content">
<pre data-language="js"><code>1// biome-ignore-all lint/suspicious/noDebugger: reason2debugger;3debugger;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">generated.js</span></figcaption>
</figure>

When a top-level suppression comment isn't at the top of the file, it is considered *unused* and Biome will emit a diagnostic with category `suppression/unused`.

### Range suppressions

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Range suppressions"]](#range-suppressions)

They disable a lint rule from a particular *range* in the file, starting from the line with the start comment, until the line with the end comment.

To mark the beginning of a range suppression, the suppression comment must start with `// biome-ignore-start`. To mark the end of it, the suppression comment must start with `// biome-ignore-end`.

The following example will disable the rule `lint/suspicious/noDoubleEquals` for line 2 and 3, but line 5 will raise a diagnostic:

<figure class="frame not-content">
<pre data-language="js"><code>1// biome-ignore-start lint/suspicious/noDoubleEquals: reason2a == b;3c == d;4// biome-ignore-end lint/suspicious/noDoubleEquals: reason5f == g;</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTFDMTEuNzM0OCAxMSAxMS40ODA0IDExLjEwNTQgMTEuMjkyOSAxMS4yOTI5QzExLjEwNTQgMTEuNDgwNCAxMSAxMS43MzQ4IDExIDEyVjE2QzExIDE2LjI2NTIgMTEuMTA1NCAxNi41MTk2IDExLjI5MjkgMTYuNzA3MUMxMS40ODA0IDE2Ljg5NDYgMTEuNzM0OCAxNyAxMiAxN0MxMi4yNjUyIDE3IDEyLjUxOTYgMTYuODk0NiAxMi43MDcxIDE2LjcwNzFDMTIuODk0NiAxNi41MTk2IDEzIDE2LjI2NTIgMTMgMTZWMTJDMTMgMTEuNzM0OCAxMi44OTQ2IDExLjQ4MDQgMTIuNzA3MSAxMS4yOTI5QzEyLjUxOTYgMTEuMTA1NCAxMi4yNjUyIDExIDEyIDExWk0xMi4zOCA3LjA4QzEyLjEzNjUgNi45Nzk5OCAxMS44NjM1IDYuOTc5OTggMTEuNjIgNy4wOEMxMS40OTczIDcuMTI3NTkgMTEuMzg1MSA3LjE5ODk2IDExLjI5IDcuMjlDMTEuMjAxNyA3LjM4NzIgMTEuMTMwNiA3LjQ5ODgyIDExLjA4IDcuNjJDMTEuMDI0IDcuNzM4NjggMTAuOTk2NiA3Ljg2ODgyIDExIDhDMTAuOTk5MiA4LjEzMTYxIDExLjAyNDUgOC4yNjIwNyAxMS4wNzQyIDguMzgzOTFDMTEuMTI0IDguNTA1NzQgMTEuMTk3MyA4LjYxNjU2IDExLjI5IDguNzFDMTEuMzg3MiA4Ljc5ODMzIDExLjQ5ODggOC44NjkzNiAxMS42MiA4LjkyQzExLjc3MTUgOC45ODIyNCAxMS45MzYgOS4wMDYzMiAxMi4wOTkgOC45OTAxMUMxMi4yNjE5IDguOTczOTEgMTIuNDE4NCA4LjkxNzkyIDEyLjU1NDcgOC44MjcwN0MxMi42OTEgOC43MzYyMiAxMi44MDI5IDguNjEzMjggMTIuODgwNSA4LjQ2OTA3QzEyLjk1ODIgOC4zMjQ4NiAxMi45OTkyIDguMTYzNzggMTMgOEMxMi45OTYzIDcuNzM1MjMgMTIuODkyNyA3LjQ4MTYzIDEyLjcxIDcuMjlDMTIuNjE0OSA3LjE5ODk2IDEyLjUwMjggNy4xMjc1OSAxMi4zOCA3LjA4Wk0xMiAyQzEwLjAyMjIgMiA4LjA4ODc5IDIuNTg2NDkgNi40NDQzIDMuNjg1M0M0Ljc5OTgxIDQuNzg0MTIgMy41MTgwOSA2LjM0NTkgMi43NjEyMSA4LjE3MzE3QzIuMDA0MzMgMTAuMDAwNCAxLjgwNjMgMTIuMDExMSAyLjE5MjE1IDEzLjk1MDlDMi41NzggMTUuODkwNyAzLjUzMDQxIDE3LjY3MjUgNC45Mjg5NCAxOS4wNzExQzYuMzI3NDYgMjAuNDY5NiA4LjEwOTI5IDIxLjQyMiAxMC4wNDkxIDIxLjgwNzlDMTEuOTg4OSAyMi4xOTM3IDEzLjk5OTYgMjEuOTk1NyAxNS44MjY4IDIxLjIzODhDMTcuNjU0MSAyMC40ODE5IDE5LjIxNTkgMTkuMjAwMiAyMC4zMTQ3IDE3LjU1NTdDMjEuNDEzNSAxNS45MTEyIDIyIDEzLjk3NzggMjIgMTJDMjIgMTAuNjg2OCAyMS43NDEzIDkuMzg2NDIgMjEuMjM4OCA4LjE3MzE3QzIwLjczNjMgNi45NTk5MSAxOS45OTk3IDUuODU3NTIgMTkuMDcxMSA0LjkyODkzQzE4LjE0MjUgNC4wMDAzNSAxNy4wNDAxIDMuMjYzNzUgMTUuODI2OCAyLjc2MTJDMTQuNjEzNiAyLjI1ODY2IDEzLjMxMzIgMiAxMiAyWk0xMiAyMEMxMC40MTc4IDIwIDguODcxMDQgMTkuNTMwOCA3LjU1NTQ0IDE4LjY1MThDNi4yMzk4NSAxNy43NzI3IDUuMjE0NDcgMTYuNTIzMyA0LjYwODk3IDE1LjA2MTVDNC4wMDM0NyAxMy41OTk3IDMuODQ1MDQgMTEuOTkxMSA0LjE1MzcyIDEwLjQzOTNDNC40NjI0IDguODg3NDMgNS4yMjQzMyA3LjQ2MTk3IDYuMzQzMTUgNi4zNDMxNUM3LjQ2MTk3IDUuMjI0MzMgOC44ODc0MyA0LjQ2MjQgMTAuNDM5MyA0LjE1MzcyQzExLjk5MTEgMy44NDUwNCAxMy41OTk3IDQuMDAzNDYgMTUuMDYxNSA0LjYwODk2QzE2LjUyMzMgNS4yMTQ0NyAxNy43NzI3IDYuMjM5ODQgMTguNjUxOCA3LjU1NTQ0QzE5LjUzMDggOC44NzEwMyAyMCAxMC40MTc3IDIwIDEyQzIwIDE0LjEyMTcgMTkuMTU3MiAxNi4xNTY2IDE3LjY1NjkgMTcuNjU2OUMxNi4xNTY2IDE5LjE1NzEgMTQuMTIxNyAyMCAxMiAyMFoiPjwvcGF0aD48L3N2Zz4=)Note

Range suppressions must have a matching `biome-ignore-end` suppression.

Range suppressions can also overlap. Consider the following example:

<figure class="frame not-content">
<pre data-language="js"><code>1debugger;2// biome-ignore-start lint/suspicious/noDebugger: reason3debugger;4// biome-ignore-start lint/suspicious/noDoubleEquals: reason5a == b;6c == d;7// biome-ignore-end lint/suspicious/noDoubleEquals: reason8debugger;9f == g;10// biome-ignore-end lint/suspicious/noDebugger: reason</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

In the above code:

-   The `debugger` statement at line 1 will raise a diagnostic because there's no suppression comment that disables it.
-   The comment `// biome-ignore-start lint/suspicious/noDebugger: reason` at line 2 starts disabling `noDebugger` from line 3 onwards.
-   The comment `// biome-ignore-start lint/suspicious/noDoubleEquals: reason` at line 4 starts disabling `noDoubleEquals` from line 5 onwards.
-   The comment `// biome-ignore-end lint/suspicious/noDoubleEquals: reason` at line 7 terminates the suppression of `noDoubleEquals` that was started by the suppression comment at line 4.
-   The `debugger` statement at line 8 **doesn't** raise diagnostics due to the suppression comment at line 2.
-   The `f == g` statement raises a diagnostic because the rule `noDoubleEquals` isn't suppressed anymore.
-   The comment `// biome-ignore-end lint/suspicious/noDebugger: reason` at line 10 terminates the suppression of `noDebugger` that was started by the suppression comment at line 2.

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/analyzer/suppressions.mdx)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Formatter Option Philosophy] ]](/formatter/option-philosophy) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[Introduction] ]](/linter)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.