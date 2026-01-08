# Test rules

Source: https://semgrep.dev/docs/writing-rules/testing-rules

- [](/docs/)- [Write rules](/docs/writing-rules/overview)- Write rules for Semgrep Code- Test rules**On this page- [Rule writing](/docs/tags/rule-writing)Test rules
Semgrep provides a testing mechanism for your rules. You can write code and provide annotations to let Semgrep know where you are or aren&#x27;t expecting findings. Semgrep provides the following annotations:

- `ruleid: &lt;rule-id&gt;` for protecting against false negatives
- `ok: &lt;rule-id&gt;` for protecting against false positives
- `todoruleid: &lt;rule-id&gt;` for future &quot;positive&quot; rule improvements
- `todook: &lt;rule-id&gt;` for future &quot;negative&quot; rule improvements

When writing tests, remember that:

- The `--test` flag tells Semgrep to run tests in the specified directory.
- Annotations are specified as a comment immediately preceeding the offending line.
- Semgrep looks for tests based on the rule filename and the languages
specified in the rule. In other words, `path/to/rule.yaml` searches for
`path/to/rule.py`, `path/to/rule.js`, and similar, based on the languages specified in the rule.

infoThe `.test.yaml` file extension can also be used for test files. This is necessary when testing YAML language rules.

## Test rules with autofix[​](#test-rules-with-autofix)
Semgrep&#x27;s testing mechanism also provides a way to test the behavior of any `fix` values defined in the rules.

To define a test for autofix behavior:

- Create a new **autofix test file** with the `.fixed` suffix before the file type extension. For example, name the autofix test file of a rule with test code in `path/to/rule.py` as `path/to/rule.fixed.py`.
- Within the autofix test file, enter the expected result of applied autofix rule to the test code.
- Run `semgrep --test` to verify that your autofix test file is correctly detected.

When you use `semgrep --test`, Semgrep applies the autofix rule to the original test code (`path/to/rule.py`), then verifies whether this matches the expected outcome defined in the autofix test file (`path/to/rule.fixed.py)`. If there is a mismatch, the line diffs are printed.

info**Hint**: Creating an autofix test for a rule with autofix can take less than a minute with the following flow of commands:

`cp rule.py rule.fixed.pysemgrep --config rule.yaml rule.fixed.py --autofix`These commands apply the autofix of the rule to the test code. After Semgrep delivers a fix, inspect whether the outcome of this fix is as expected (for example, using `vimdiff rule.py rule.fixed.py`).

## Example[​](#example)
Consider the following rule:

`rules:- id: insecure-eval-use  patterns:  - pattern: eval($VAR)  - pattern-not: eval(&quot;...&quot;)  fix: secure_eval($VAR)  message: Calling &#x27;eval&#x27; with user input  languages: [python]  severity: MEDIUM`
If the filename with the preceeding rule is `rules/detect-eval.yaml`, you can create `rules/detect-eval.py`:

`from lib import get_user_input, safe_get_user_input, secure_evaluser_input = get_user_input()# ruleid: insecure-eval-useeval(user_input)# ok: insecure-eval-useeval(&#x27;print(&quot;Hardcoded eval&quot;)&#x27;)totally_safe_eval = eval# todoruleid: insecure-eval-usetotally_safe_eval(user_input)# todook: insecure-eval-useeval(safe_get_user_input())`
Run the tests with the following:

`semgrep --test rules/`
This produces the following output:

`1/1: ✓ All tests passedNo tests for fixes found.`
Semgrep tests automatically avoid failing on lines marked with `# todoruleid` or `# todook`.

## Store rules and test targets in different directories[​](#store-rules-and-test-targets-in-different-directories)
Creating different directories for rules and tests helps you manage a growing library of custom rules. To store rules and test targets in different directories, use the `--config` option.

For example, in the directory with the following structure:

`$ tree teststests├── rules│   └── python│       └── insecure-eval-use.yaml└── targets    └── python        └── insecure-eval-use.py4 directories, 2 files`
Use of the following command

`semgrep --test --config tests/rules/ tests/targets/`
Produces the same output as in the previous example.

The subdirectory structure of these two directories must be the same for Semgrep to correctly find the associated files.

To test the autofix behavior, add the autofix test file `rules/detect-eval.fixed.py` to represent the expected outcome of applying the fix to the test code:

`from lib import get_user_input, safe_get_user_input, secure_evaluser_input = get_user_input()# ruleid: insecure-eval-usesecure_eval(user_input)# ok: insecure-eval-useeval(&#x27;print(&quot;Hardcoded eval&quot;)&#x27;)totally_safe_eval = eval# todoruleid: insecure-eval-usetotally_safe_eval(user_input)# todook: insecure-eval-usesecure_eval(safe_get_user_input())`
So that the directory structure is printed as the following:

`$ tree teststests├── rules│   └── python│       └── insecure-eval-use.yaml└── targets    └── python        └── insecure-eval-use.py        └── insecure-eval-use.fixed.py4 directories, 2 files`
Use of the following command:

`semgrep --test --config tests/rules/ tests/targets/`
Results in the following outcome:

`1/1: ✓ All tests passed1/1: ✓ All fix tests passed`
If the fix does not behave as expected, the output prints a line diff.
For example, if you replace `secure_eval` with `safe_eval`, you can see that lines 5 and 15 do not render as expected.

`1/1: ✓ All tests passed0/1: 1 fix tests did not pass:--------------------------------------------------------------------------------	✖ targets/python/detect-eval.fixed.py &lt;&gt; autofix applied to targets/python/detect-eval.py	---	+++	@@ -5 +5 @@	-safe_eval(user_input)	+secure_eval(user_input)	@@ -15 +15 @@	-safe_eval(safe_get_user_input())	+secure_eval(safe_get_user_input())`
## Validating rules[​](#validating-rules)
You can run `semgrep --validate --config [filename]` to verify the rule&#x27;s configuration. This command runs a combination of Semgrep rules and OCaml checks against your rules to search for issues such as duplicate patterns and missing fields. All rules submitted to the Semgrep Registry are validated.

The semgrep rules are pulled from `p/semgrep-rule-lints`.

This feature is still experimental and under active development. Your feedback is welcomed!

## Enabling autofix in Semgrep Code[​](#enabling-autofix-in-semgrep-code)
To enable autofix for all projects in your Semgrep AppSec Platform organization, follow these steps:

- In Semgrep AppSec Platform, go to **[Settings &gt; General &gt; Code](https://semgrep.dev/orgs/-/settings/general/code)**.
- Click the **Autofix** ** toggle to enable this feature.
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Rule writing](/docs/tags/rule-writing)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/writing-rules/testing-rules.md)Last updated on **Oct 21, 2025**