# Source: https://biomejs.dev/reference/reporters/

# Reporters 

Biome's CLI accepts a `--reporter` argument that allows to change how diagnostics and summary are printed to terminal.

## Summary

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Summary"]](#summary)

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --reporter=summary</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

<figure class="frame not-content">
<pre data-language="plaintext"><code>1reporter/parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━2  i The following files have parsing errors.3
4  - index.css5
6reporter/format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━7  i The following files needs to be formatted.8
9  - index.css10  - index.ts11  - main.ts12
13reporter/violations ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━14  i Some lint rules or assist actions reported some violations.15
16  Rule Name                                        Diagnostics17
18  lint/correctness/noUnknownFunction               14 (2 error(s), 12 warning(s), 0 info(s))19  lint/suspicious/noImplicitAnyLet                 16 (12 error(s), 4 warning(s), 0 info(s))20  lint/suspicious/noDoubleEquals                   8 (8 error(s), 0 warning(s), 0 info(s))21  assist/source/organizeImports                    2 (2 error(s), 0 warning(s), 0 info(s))22  lint/suspicious/noRedeclare                      12 (12 error(s), 0 warning(s), 0 info(s))23  lint/suspicious/noDebugger                       8 (8 error(s), 0 warning(s), 0 info(s))</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

## JSON

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "JSON"]](#json)

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTZDMTEuODAyMiAxNiAxMS42MDg5IDE2LjA1ODcgMTEuNDQ0NCAxNi4xNjg2QzExLjI4IDE2LjI3ODQgMTEuMTUxOCAxNi40MzQ2IDExLjA3NjEgMTYuNjE3M0MxMS4wMDA0IDE2LjgwMDEgMTAuOTgwNiAxNy4wMDExIDExLjAxOTIgMTcuMTk1MUMxMS4wNTc4IDE3LjM4OTEgMTEuMTUzIDE3LjU2NzMgMTEuMjkyOSAxNy43MDcxQzExLjQzMjcgMTcuODQ3IDExLjYxMDkgMTcuOTQyMiAxMS44MDQ5IDE3Ljk4MDhDMTEuOTk4OSAxOC4wMTk0IDEyLjIgMTcuOTk5NiAxMi4zODI3IDE3LjkyMzlDMTIuNTY1NCAxNy44NDgyIDEyLjcyMTYgMTcuNzIgMTIuODMxNSAxNy41NTU2QzEyLjk0MTMgMTcuMzkxMSAxMyAxNy4xOTc4IDEzIDE3QzEzIDE2LjczNDggMTIuODk0NiAxNi40ODA1IDEyLjcwNzEgMTYuMjkyOUMxMi41MTk2IDE2LjEwNTQgMTIuMjY1MiAxNiAxMiAxNlpNMjIuNjcgMTcuNDdMMTQuNjIgMy40NzAwM0MxNC4zNTk4IDMuMDAzNTQgMTMuOTc5OCAyLjYxNDk4IDEzLjUxOTIgMi4zNDQ1QzEzLjA1ODYgMi4wNzQwMSAxMi41MzQxIDEuOTMxNCAxMiAxLjkzMTRDMTEuNDY1OSAxLjkzMTQgMTAuOTQxNCAyLjA3NDAxIDEwLjQ4MDggMi4zNDQ1QzEwLjAyMDIgMi42MTQ5OCA5LjY0MDE5IDMuMDAzNTQgOS4zOCAzLjQ3MDAzTDEuMzggMTcuNDdDMS4xMTA3OSAxNy45MjQgMC45NjYxNDEgMTguNDQxIDAuOTYwNjQzIDE4Ljk2ODhDMC45NTUxNDQgMTkuNDk2NiAxLjA4OSAyMC4wMTY2IDEuMzQ4NjggMjAuNDc2MUMxLjYwODM3IDIwLjkzNTYgMS45ODQ3IDIxLjMxODUgMi40Mzk2OCAyMS41ODYxQzIuODk0NjYgMjEuODUzNiAzLjQxMjE4IDIxLjk5NjQgMy45NCAyMkgyMC4wNkMyMC41OTIxIDIyLjAwNTMgMjEuMTE1OSAyMS44Njg5IDIxLjU3NzkgMjEuNjA0OUMyMi4wMzk5IDIxLjM0MSAyMi40MjM0IDIwLjk1ODkgMjIuNjg5IDIwLjQ5NzhDMjIuOTU0NiAyMC4wMzY4IDIzLjA5MjggMTkuNTEzNCAyMy4wODk1IDE4Ljk4MTRDMjMuMDg2MiAxOC40NDkzIDIyLjk0MTQgMTcuOTI3NyAyMi42NyAxNy40N1pNMjAuOTQgMTkuNDdDMjAuODUyMyAxOS42MjYgMjAuNzI0NSAxOS43NTU2IDIwLjU2OTcgMTkuODQ1M0MyMC40MTQ5IDE5LjkzNSAyMC4yMzg5IDE5Ljk4MTUgMjAuMDYgMTkuOThIMy45NEMzLjc2MTExIDE5Ljk4MTUgMy41ODUxIDE5LjkzNSAzLjQzMDMyIDE5Ljg0NTNDMy4yNzU1MyAxOS43NTU2IDMuMTQ3NjUgMTkuNjI2IDMuMDYgMTkuNDdDMi45NzIyMyAxOS4zMTggMi45MjYwMiAxOS4xNDU2IDIuOTI2MDIgMTguOTdDMi45MjYwMiAxOC43OTQ1IDIuOTcyMjMgMTguNjIyIDMuMDYgMTguNDdMMTEuMDYgNC40NzAwM0MxMS4xNDM5IDQuMzA2MjMgMTEuMjcxNCA0LjE2ODc2IDExLjQyODQgNC4wNzI3N0MxMS41ODU1IDMuOTc2NzggMTEuNzY2IDMuOTI1OTkgMTEuOTUgMy45MjU5OUMxMi4xMzQgMy45MjU5OSAxMi4zMTQ1IDMuOTc2NzggMTIuNDcxNiA0LjA3Mjc3QzEyLjYyODYgNC4xNjg3NiAxMi43NTYxIDQuMzA2MjMgMTIuODQgNC40NzAwM0wyMC44OSAxOC40N0MyMC45ODkyIDE4LjYxOTkgMjEuMDQ2MiAxOC43OTM3IDIxLjA1NSAxOC45NzMyQzIxLjA2MzggMTkuMTUyNyAyMS4wMjQxIDE5LjMzMTIgMjAuOTQgMTkuNDlWMTkuNDdaTTEyIDguMDAwMDNDMTEuNzM0OCA4LjAwMDAzIDExLjQ4MDQgOC4xMDUzOCAxMS4yOTI5IDguMjkyOTJDMTEuMTA1NCA4LjQ4MDQ2IDExIDguNzM0ODEgMTEgOS4wMDAwM1YxM0MxMSAxMy4yNjUyIDExLjEwNTQgMTMuNTE5NiAxMS4yOTI5IDEzLjcwNzFDMTEuNDgwNCAxMy44OTQ3IDExLjczNDggMTQgMTIgMTRDMTIuMjY1MiAxNCAxMi41MTk2IDEzLjg5NDcgMTIuNzA3MSAxMy43MDcxQzEyLjg5NDYgMTMuNTE5NiAxMyAxMy4yNjUyIDEzIDEzVjkuMDAwMDNDMTMgOC43MzQ4MSAxMi44OTQ2IDguNDgwNDYgMTIuNzA3MSA4LjI5MjkyQzEyLjUxOTYgOC4xMDUzOCAxMi4yNjUyIDguMDAwMDMgMTIgOC4wMDAwM1oiPjwvcGF0aD48L3N2Zz4=)Caution

This reporter is experimental and subject to changes in patch releases.

It emits the summary and diagnostics in a JSON format.

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome ci --reporter=json</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

## JSON pretty

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "JSON pretty"]](#json-pretty)

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTZDMTEuODAyMiAxNiAxMS42MDg5IDE2LjA1ODcgMTEuNDQ0NCAxNi4xNjg2QzExLjI4IDE2LjI3ODQgMTEuMTUxOCAxNi40MzQ2IDExLjA3NjEgMTYuNjE3M0MxMS4wMDA0IDE2LjgwMDEgMTAuOTgwNiAxNy4wMDExIDExLjAxOTIgMTcuMTk1MUMxMS4wNTc4IDE3LjM4OTEgMTEuMTUzIDE3LjU2NzMgMTEuMjkyOSAxNy43MDcxQzExLjQzMjcgMTcuODQ3IDExLjYxMDkgMTcuOTQyMiAxMS44MDQ5IDE3Ljk4MDhDMTEuOTk4OSAxOC4wMTk0IDEyLjIgMTcuOTk5NiAxMi4zODI3IDE3LjkyMzlDMTIuNTY1NCAxNy44NDgyIDEyLjcyMTYgMTcuNzIgMTIuODMxNSAxNy41NTU2QzEyLjk0MTMgMTcuMzkxMSAxMyAxNy4xOTc4IDEzIDE3QzEzIDE2LjczNDggMTIuODk0NiAxNi40ODA1IDEyLjcwNzEgMTYuMjkyOUMxMi41MTk2IDE2LjEwNTQgMTIuMjY1MiAxNiAxMiAxNlpNMjIuNjcgMTcuNDdMMTQuNjIgMy40NzAwM0MxNC4zNTk4IDMuMDAzNTQgMTMuOTc5OCAyLjYxNDk4IDEzLjUxOTIgMi4zNDQ1QzEzLjA1ODYgMi4wNzQwMSAxMi41MzQxIDEuOTMxNCAxMiAxLjkzMTRDMTEuNDY1OSAxLjkzMTQgMTAuOTQxNCAyLjA3NDAxIDEwLjQ4MDggMi4zNDQ1QzEwLjAyMDIgMi42MTQ5OCA5LjY0MDE5IDMuMDAzNTQgOS4zOCAzLjQ3MDAzTDEuMzggMTcuNDdDMS4xMTA3OSAxNy45MjQgMC45NjYxNDEgMTguNDQxIDAuOTYwNjQzIDE4Ljk2ODhDMC45NTUxNDQgMTkuNDk2NiAxLjA4OSAyMC4wMTY2IDEuMzQ4NjggMjAuNDc2MUMxLjYwODM3IDIwLjkzNTYgMS45ODQ3IDIxLjMxODUgMi40Mzk2OCAyMS41ODYxQzIuODk0NjYgMjEuODUzNiAzLjQxMjE4IDIxLjk5NjQgMy45NCAyMkgyMC4wNkMyMC41OTIxIDIyLjAwNTMgMjEuMTE1OSAyMS44Njg5IDIxLjU3NzkgMjEuNjA0OUMyMi4wMzk5IDIxLjM0MSAyMi40MjM0IDIwLjk1ODkgMjIuNjg5IDIwLjQ5NzhDMjIuOTU0NiAyMC4wMzY4IDIzLjA5MjggMTkuNTEzNCAyMy4wODk1IDE4Ljk4MTRDMjMuMDg2MiAxOC40NDkzIDIyLjk0MTQgMTcuOTI3NyAyMi42NyAxNy40N1pNMjAuOTQgMTkuNDdDMjAuODUyMyAxOS42MjYgMjAuNzI0NSAxOS43NTU2IDIwLjU2OTcgMTkuODQ1M0MyMC40MTQ5IDE5LjkzNSAyMC4yMzg5IDE5Ljk4MTUgMjAuMDYgMTkuOThIMy45NEMzLjc2MTExIDE5Ljk4MTUgMy41ODUxIDE5LjkzNSAzLjQzMDMyIDE5Ljg0NTNDMy4yNzU1MyAxOS43NTU2IDMuMTQ3NjUgMTkuNjI2IDMuMDYgMTkuNDdDMi45NzIyMyAxOS4zMTggMi45MjYwMiAxOS4xNDU2IDIuOTI2MDIgMTguOTdDMi45MjYwMiAxOC43OTQ1IDIuOTcyMjMgMTguNjIyIDMuMDYgMTguNDdMMTEuMDYgNC40NzAwM0MxMS4xNDM5IDQuMzA2MjMgMTEuMjcxNCA0LjE2ODc2IDExLjQyODQgNC4wNzI3N0MxMS41ODU1IDMuOTc2NzggMTEuNzY2IDMuOTI1OTkgMTEuOTUgMy45MjU5OUMxMi4xMzQgMy45MjU5OSAxMi4zMTQ1IDMuOTc2NzggMTIuNDcxNiA0LjA3Mjc3QzEyLjYyODYgNC4xNjg3NiAxMi43NTYxIDQuMzA2MjMgMTIuODQgNC40NzAwM0wyMC44OSAxOC40N0MyMC45ODkyIDE4LjYxOTkgMjEuMDQ2MiAxOC43OTM3IDIxLjA1NSAxOC45NzMyQzIxLjA2MzggMTkuMTUyNyAyMS4wMjQxIDE5LjMzMTIgMjAuOTQgMTkuNDlWMTkuNDdaTTEyIDguMDAwMDNDMTEuNzM0OCA4LjAwMDAzIDExLjQ4MDQgOC4xMDUzOCAxMS4yOTI5IDguMjkyOTJDMTEuMTA1NCA4LjQ4MDQ2IDExIDguNzM0ODEgMTEgOS4wMDAwM1YxM0MxMSAxMy4yNjUyIDExLjEwNTQgMTMuNTE5NiAxMS4yOTI5IDEzLjcwNzFDMTEuNDgwNCAxMy44OTQ3IDExLjczNDggMTQgMTIgMTRDMTIuMjY1MiAxNCAxMi41MTk2IDEzLjg5NDcgMTIuNzA3MSAxMy43MDcxQzEyLjg5NDYgMTMuNTE5NiAxMyAxMy4yNjUyIDEzIDEzVjkuMDAwMDNDMTMgOC43MzQ4MSAxMi44OTQ2IDguNDgwNDYgMTIuNzA3MSA4LjI5MjkyQzEyLjUxOTYgOC4xMDUzOCAxMi4yNjUyIDguMDAwMDMgMTIgOC4wMDAwM1oiPjwvcGF0aD48L3N2Zz4=)Caution

This reporter is experimental and subject to changes in patch releases.

Same as `--reporter=json`, it emits the summary and diagnostics in a JSON format, and the output is formatted using the current JSON formatting options (configuration file or defaults).

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome ci --reporter=json-pretty</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

## GitHub

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "GitHub"]](#github)

Use this reporter in a GitHub workflow. When properly configured in a PR workflow, GitHub will print a message for each info/warning/error emitted.

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome ci --reporter=github</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

<figure class="frame not-content">
<pre data-language="plaintext"><code>1::error title=lint/suspicious/noDoubleEquals,file=main.ts,line=4,endLine=4,col=3,endColumn=5::Use === instead of ==2::error title=lint/suspicious/noDebugger,file=main.ts,line=6,endLine=6,col=1,endColumn=9::This is an unexpected use of the debugger statement.3::error title=lint/nursery/noEvolvingAny,file=main.ts,line=8,endLine=8,col=5,endColumn=6::This variable&#39;s type is not allowed to evolve implicitly, leading to potential any types.</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

## JUnit

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "JUnit"]](#junit)

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --reporter=junit</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

<figure class="frame not-content">
<pre data-language="xml"><code>1&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;2&lt;testsuites name=&quot;Biome&quot; tests=&quot;16&quot; failures=&quot;16&quot; errors=&quot;20&quot; time=&quot;&lt;TIME&gt;&quot;&gt;3  &lt;testsuite name=&quot;main.ts&quot; tests=&quot;1&quot; disabled=&quot;0&quot; errors=&quot;0&quot; failures=&quot;1&quot; package=&quot;org.biome&quot;&gt;4      &lt;testcase name=&quot;org.biome.lint.suspicious.noDoubleEquals&quot; line=&quot;4&quot; column=&quot;3&quot;&gt;5          &lt;failure message=&quot;Use === instead of ==. == is only allowed when comparing against `null`&quot;&gt;line 3, col 2, Use === instead of ==. == is only allowed when comparing against `null`&lt;/failure&gt;6      &lt;/testcase&gt;7  &lt;/testsuite&gt;8  &lt;testsuite name=&quot;main.ts&quot; tests=&quot;1&quot; disabled=&quot;0&quot; errors=&quot;0&quot; failures=&quot;1&quot; package=&quot;org.biome&quot;&gt;9      &lt;testcase name=&quot;org.biome.lint.suspicious.noDebugger&quot; line=&quot;6&quot; column=&quot;1&quot;&gt;10          &lt;failure message=&quot;This is an unexpected use of the debugger statement.&quot;&gt;line 5, col 0, This is an unexpected use of the debugger statement.&lt;/failure&gt;11      &lt;/testcase&gt;12  &lt;/testsuite&gt;13  &lt;testsuite name=&quot;main.ts&quot; tests=&quot;1&quot; disabled=&quot;0&quot; errors=&quot;0&quot; failures=&quot;1&quot; package=&quot;org.biome&quot;&gt;14      &lt;testcase name=&quot;org.biome.lint.nursery.noEvolvingAny&quot; line=&quot;8&quot; column=&quot;5&quot;&gt;15          &lt;failure message=&quot;This variable&#39;s type is not allowed to evolve implicitly, leading to potential any types.&quot;&gt;line 7, col 4, This variable&#39;s type is not allowed to evolve implicitly, leading to potential any types.&lt;/failure&gt;16      &lt;/testcase&gt;17  &lt;/testsuite&gt;18&lt;/testsuites&gt;</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

## GitLab

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "GitLab"]](#gitlab)

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --reporter=gitlab</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

<figure class="frame not-content">
<pre data-language="json"><code>1[2  12    }13  },14  24    }25  },26  36    }37  }38]</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

## Checkstyle

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Checkstyle"]](#checkstyle)

Use this reporter to emit diagnostics that follow tine [Checkstyle format](https://checkstyle.org/).

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --reporter=checkstyle</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

<figure class="frame not-content">
<pre data-language="xml"><code>1&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;2&lt;checkstyle version=&quot;4.3&quot;&gt;3  &lt;file name=&quot;index.ts&quot;&gt;4    &lt;error line=&quot;1&quot; column=&quot;8&quot; severity=&quot;warning&quot; message=&quot;This import is unused.&quot; source=&quot;lint/correctness/noUnusedImports&quot; /&gt;5    &lt;error line=&quot;2&quot; column=&quot;10&quot; severity=&quot;warning&quot; message=&quot;Several of these imports are unused.&quot; source=&quot;lint/correctness/noUnusedImports&quot; /&gt;6    &lt;error line=&quot;8&quot; column=&quot;5&quot; severity=&quot;warning&quot; message=&quot;This variable f is unused.&quot; source=&quot;lint/correctness/noUnusedVariables&quot; /&gt;7    &lt;error line=&quot;9&quot; column=&quot;7&quot; severity=&quot;warning&quot; message=&quot;This variable f is unused.&quot; source=&quot;lint/correctness/noUnusedVariables&quot; /&gt;8    &lt;error line=&quot;1&quot; column=&quot;1&quot; severity=&quot;error&quot; message=&quot;The imports and exports are not sorted.&quot; source=&quot;assist/source/organizeImports&quot; /&gt;9    &lt;error line=&quot;4&quot; column=&quot;3&quot; severity=&quot;error&quot; message=&quot;Using == may be unsafe if you are relying on type coercion.&quot; source=&quot;lint/suspicious/noDoubleEquals&quot; /&gt;10    &lt;error line=&quot;6&quot; column=&quot;1&quot; severity=&quot;error&quot; message=&quot;This is an unexpected use of the debugger statement.&quot; source=&quot;lint/suspicious/noDebugger&quot; /&gt;11    &lt;error line=&quot;8&quot; column=&quot;5&quot; severity=&quot;error&quot; message=&quot;This variable implicitly has the any type.&quot; source=&quot;lint/suspicious/noImplicitAnyLet&quot; /&gt;12    &lt;error line=&quot;9&quot; column=&quot;7&quot; severity=&quot;error&quot; message=&quot;This variable implicitly has the any type.&quot; source=&quot;lint/suspicious/noImplicitAnyLet&quot; /&gt;13    &lt;error line=&quot;2&quot; column=&quot;10&quot; severity=&quot;error&quot; message=&quot;Shouldn&amp;apos;t redeclare &amp;apos;z&amp;apos;. Consider to delete it or rename it.&quot; source=&quot;lint/suspicious/noRedeclare&quot; /&gt;14    &lt;error line=&quot;9&quot; column=&quot;7&quot; severity=&quot;error&quot; message=&quot;Shouldn&amp;apos;t redeclare &amp;apos;f&amp;apos;. Consider to delete it or rename it.&quot; source=&quot;lint/suspicious/noRedeclare&quot; /&gt;15    &lt;error line=&quot;0&quot; column=&quot;0&quot; severity=&quot;error&quot; message=&quot;Formatter would have printed the following content:&quot; source=&quot;format&quot; /&gt;16  &lt;/file&gt;17  &lt;file name=&quot;main.ts&quot;&gt;18    &lt;error line=&quot;1&quot; column=&quot;8&quot; severity=&quot;warning&quot; message=&quot;This import is unused.&quot; source=&quot;lint/correctness/noUnusedImports&quot; /&gt;19    &lt;error line=&quot;2&quot; column=&quot;10&quot; severity=&quot;warning&quot; message=&quot;Several of these imports are unused.&quot; source=&quot;lint/correctness/noUnusedImports&quot; /&gt;20    &lt;error line=&quot;8&quot; column=&quot;5&quot; severity=&quot;warning&quot; message=&quot;This variable f is unused.&quot; source=&quot;lint/correctness/noUnusedVariables&quot; /&gt;21    &lt;error line=&quot;9&quot; column=&quot;7&quot; severity=&quot;warning&quot; message=&quot;This variable f is unused.&quot; source=&quot;lint/correctness/noUnusedVariables&quot; /&gt;22    &lt;error line=&quot;1&quot; column=&quot;1&quot; severity=&quot;error&quot; message=&quot;The imports and exports are not sorted.&quot; source=&quot;assist/source/organizeImports&quot; /&gt;23    &lt;error line=&quot;4&quot; column=&quot;3&quot; severity=&quot;error&quot; message=&quot;Using == may be unsafe if you are relying on type coercion.&quot; source=&quot;lint/suspicious/noDoubleEquals&quot; /&gt;24    &lt;error line=&quot;6&quot; column=&quot;1&quot; severity=&quot;error&quot; message=&quot;This is an unexpected use of the debugger statement.&quot; source=&quot;lint/suspicious/noDebugger&quot; /&gt;25    &lt;error line=&quot;8&quot; column=&quot;5&quot; severity=&quot;error&quot; message=&quot;This variable implicitly has the any type.&quot; source=&quot;lint/suspicious/noImplicitAnyLet&quot; /&gt;26    &lt;error line=&quot;9&quot; column=&quot;7&quot; severity=&quot;error&quot; message=&quot;This variable implicitly has the any type.&quot; source=&quot;lint/suspicious/noImplicitAnyLet&quot; /&gt;27    &lt;error line=&quot;2&quot; column=&quot;10&quot; severity=&quot;error&quot; message=&quot;Shouldn&amp;apos;t redeclare &amp;apos;z&amp;apos;. Consider to delete it or rename it.&quot; source=&quot;lint/suspicious/noRedeclare&quot; /&gt;28    &lt;error line=&quot;9&quot; column=&quot;7&quot; severity=&quot;error&quot; message=&quot;Shouldn&amp;apos;t redeclare &amp;apos;f&amp;apos;. Consider to delete it or rename it.&quot; source=&quot;lint/suspicious/noRedeclare&quot; /&gt;29    &lt;error line=&quot;0&quot; column=&quot;0&quot; severity=&quot;error&quot; message=&quot;Formatter would have printed the following content:&quot; source=&quot;format&quot; /&gt;30  &lt;/file&gt;31&lt;/checkstyle&gt;</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

## RDJSON

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "RDJSON"]](#rdjson)

Use this reporter to emit diagnostics that follow the [RDJSON format](https://deepwiki.com/reviewdog/reviewdog/3.2-reviewdog-diagnostic-format).

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --reporter=rdjson</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

<figure class="frame not-content">
<pre data-language="json"><code>1,6  &quot;diagnostics&quot;: [7    ,12      &quot;location&quot;: ,19          &quot;start&quot;: 23        }24      },25      &quot;message&quot;: &quot;This import is unused.&quot;26    },27    ,32      &quot;location&quot;: ,39          &quot;start&quot;: 43        }44      },45      &quot;message&quot;: &quot;Several of these imports are unused.&quot;46    }47  ]48}</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/reference/reporters.mdx)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Environment variables] ]](/reference/environment-variables) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[Configuration] ]](/reference/configuration)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.