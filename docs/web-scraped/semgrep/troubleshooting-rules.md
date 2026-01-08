# Troubleshooting rules

Source: https://semgrep.dev/docs/troubleshooting/rules

- [](/docs/)- [Write rules](/docs/writing-rules/overview)- Write rules for Semgrep Code- Troubleshooting rules**On this page- [Troubleshooting](/docs/tags/troubleshooting)- [Rule writing](/docs/tags/rule-writing)Troubleshooting rules
This page intends to help rule authors fix common mistakes when writing Semgrep rules. If you have a problem while running a rule you didn&#x27;t write yourself, please [open a GitHub issue in the Semgrep Registry](https://github.com/semgrep/semgrep-rules/issues/new/choose) repository.

## If your pattern can’t be parsed[​](#if-your-pattern-cant-be-parsed)
This error means your pattern does not look like complete source code in the selected language.

&quot;Complete source code&quot; means that the Semgrep pattern must look like a valid, complete expression or statement on its own.

To illustrate with an example, Python isn&#x27;t able to parse `if 4 &lt; 5` as a line of code, because it&#x27;s missing the code block on the right hand side.

`&gt;&gt;&gt; if 4 &lt; 5  File &quot;&lt;stdin&gt;&quot;, line 1    if 4 &lt; 5            ^SyntaxError: invalid syntax&gt;&gt;&gt;`
To get Python to parse this, you need to add a colon and a code block:

`&gt;&gt;&gt; if 4 &lt; 5: print(&quot;it works!&quot;)...it works!&gt;&gt;&gt;`
The same way Python&#x27;s parser cannot parse partial statements or expressions, Semgrep cannot either.

The Semgrep pattern `if $X &lt; 5` is invalid, and needs to be changed to a complete statement with a wildcard: `if $X &lt; 5: ...`

While this is the most common reason for pattern parse errors, other things to verify include:

- Making sure the correct language is indicated in the rule.
- Making sure that any metavariables you use are in all uppercase and does not start with a number. Valid metavariable names include `$X`, `$NAME`, and `$_VAR_2`. Invalid metavariable names include `$name`, `$1stvar` and `$VAR-WITH-DASHES`.

## If your rule doesn&#x27;t match where it should[​](#if-your-rule-doesnt-match-where-it-should)
In general, it helps to test the patterns within your rule in isolation. If you scan for the patterns individually and they each find what you expect, the issue is with the Boolean logic within your rule. Review the [rule syntax](/docs/writing-rules/rule-syntax) to make sure the operators are meant to behave like you expect. If you managed to find a pattern that behaves incorrectly, continue debugging with the section below.

## If your pattern doesn&#x27;t match where it should[​](#if-your-pattern-doesnt-match-where-it-should)
If you isolated the issue to one specific pattern, here are some common issues to look out for:

- When referencing something imported from a module, you need to fully qualify the import path. To match `import google.metrics; metrics.send(foo)` in Python, your pattern needs to be `google.metrics.send(...)` instead of `metrics.send(...)`.
- If your pattern uses a metavariable, make sure it&#x27;s all uppercase and does not start with a number. Valid metavariable names include `$X`, `$NAME`, and `$_VAR_2`. Invalid metavariable names include `$name`, `$1stvar` and `$VAR-WITH-DASHES`.

## If a regex pattern doesn&#x27;t match where it should[​](#if-a-regex-pattern-doesnt-match-where-it-should)

- When using `metavariable-regex`, the regex matches against all characters of the found metavariable. This means that if the metavariable matches a `&quot;foo&quot;` string in your code, the `metavariable-regex` pattern runs against a five character string with the quote characters at either end.
- Note that using the pipe (`|`) character appends a newline to your regex! If you are writing `pattern-regex: |` and then a newline with the regex, you almost certainly want the `|-` operator as in `pattern-regex: |-` to remove that trailing newline.
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Troubleshooting](/docs/tags/troubleshooting)- [Rule writing](/docs/tags/rule-writing)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/troubleshooting/rules.md)Last updated on **Oct 15, 2025**