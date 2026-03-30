# Source: https://docs.vale.sh/topics/styles.md

# Styles

Learn about the primary component of Vale's configuration system.

Vale has a powerful extension system that doesn’t require knowledge of any programming language. Instead, it uses collections of individual [YAML](http://yaml.org/) files (or “rules”) to enforce particular writing constructs.

```yaml
# An example rule from the "Microsoft" style.
extends: existence
message: "Don't use end punctuation in headings."
link: https://docs.microsoft.com/en-us/style-guide/punctuation/periods
nonword: true
level: warning
scope: heading
action:
  name: edit
  params:
    - remove
    - '.?!'
tokens:
  - '[a-z0-9][.?!](?:\s|$)'
```

These collections are referred to as *styles* and are organized in a nested folder structure at a user-specified location. For example,

```
$ tree styles
styles/
├── base/
│   ├── ComplexWords.yml
│   ├── SentenceLength.yml
│   ...
├── blog/
│   ├── TechTerms.yml
│   ...
└── docs/
    ├── Branding.yml
```

where *base*, *blog*, and *docs* are your styles that each contain certain rules.

## [Rules](#rules)

{% hint style="warning" %}
Heads up!

Make sure your rule files end in extension `.yml`. Do not end them in `.yaml`, as Vale will not detect them.
{% endhint %}

The building blocks of styles are called *rules* (YAML files ending in `.yml`), which utilize *checks* to perform specific tasks.

The structure of a rule consists header followed by check-specific arguments. Every rule supports the following header fields:

| Name      | Required | Default      | Description                                                                                                                                                                                      |
| --------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `extends` | Yes      | `N/A`        | <p>The name of the check to extend in the particular rule. See <a href="../checks/existence">Rules</a> for more information.<br><code>\<br>extends: existence\<br></code></p>                    |
| `message` | Yes      | `N/A`        | <p>The message to display when the rule is triggered. Each extension point has different formatting options.<br><code>\<br>message: "Don't use '%s' headings."\<br></code></p>                   |
| `level`   | No       | `suggestion` | <p>The severity of the rule. The available options are <code>suggestion</code>, <code>warning</code>, and <code>error</code>.<br><code>\<br>level: warning\<br></code></p>                       |
| `scope`   | No       | `text`       | <p>The scope of the rule. See <a href="scopes">Scopes</a> for more information.<br><code>\<br>scope: heading\<br></code></p>                                                                     |
| `link`    | No       | `N/A`        | <p>A URL to associate with the rule. This is useful for providing more information about the rule.<br><code>\<br>link: [https://example.com\&#x3C;br>](https://example.com\&#x3C;br>)</code></p> |
| `limit`   | No       | `N/A`        | <p>The maximum number of times the rule can be triggered in a single file.<br><code>\<br>limit: 3\<br></code></p>                                                                                |
| `vocab`   | No       | `true`       | <p>If set to false, any active vocabularies will be disabled for the rule.<br><code>\<br>vocab: false\<br></code></p>                                                                            |

## [Checks](#checks)

Each rule *extends* a specific check, which is a built-in function that performs a particular task. For example, the `existence` check ensures that a given pattern is present in the content.

| Name                                                         | Description                                                                               |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| [existence](https://docs.vale.sh/checks/existence)           | Check for the presence of a specific regex pattern.                                       |
| [substitution](https://docs.vale.sh/checks/substitution)     | Replace a regex pattern with a specific string.                                           |
| [occurrence](https://docs.vale.sh/checks/occurrence)         | Ensure the presence of a regex pattern a specific number of times.                        |
| [repetition](https://docs.vale.sh/checks/repetition)         | Avoid repeating a regex pattern a specific number of times.                               |
| [consistency](https://docs.vale.sh/checks/consistency)       | Ensure that a regex pattern is used consistently.                                         |
| [conditional](https://docs.vale.sh/checks/conditional)       | Check for the presence of a regex pattern based on a condition.                           |
| [capitalization](https://docs.vale.sh/checks/capitalization) | Ensure that a regex pattern is capitalized in a specific way.                             |
| [metric](https://docs.vale.sh/checks/metric)                 | Check the readability (or other metrics) of your content using custom forumulas.          |
| [spelling](https://docs.vale.sh/checks/spelling)             | Spell check using Hunspell-compatible dictionaries.                                       |
| [sequence](https://docs.vale.sh/checks/sequence)             | Ensure that a regex pattern is used in a specific order. Supports part-of-speech tagging. |
| [script](https://docs.vale.sh/checks/script)                 | Run a custom Tengo script to check your content.                                          |

## [Regex](#regex)

Many rules will require the use of regular expressions to match specific patterns in your content. Vale uses [a superset](https://github.com/dlclark/regexp2?tab=readme-ov-file#compare-regexp-and-regexp2) of Go’s [regexp/syntax](https://pkg.go.dev/regexp/syntax) package to provide a powerful and flexible regex engine.

In addition to the standard Go regex syntax, Vale also supports positive lookahead (`(?=re)`), negative lookahead (`(?!re)`), positive lookbehind (`(?<=re)`), and negative lookbehind (`(?<!re)`).

See the [Regex](https://docs.vale.sh/guides/regex) guide for more information.

## [Vale](#vale)

Vale comes with a single built-in style named `Vale` that implements a few rules, as described in the table below.

| Name              | Description                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `Vale.Spelling`   | Checks for spelling errors in your content. Consumes any Hunspell-compatible dictionaries stored in `<StylesPath>/config/dictionaries`. |
| `Vale.Terms`      | Enforces the current project's accepted [Vocabulary](https://docs.vale.sh/keys/vocabularies) terms.                                     |
| `Vale.Avoid`      | Enforces the current project's rejected [Vocabulary](https://docs.vale.sh/keys/vocabularies) terms.                                     |
| `Vale.Repetition` | Flags repeated words such as "the the" or "and and".                                                                                    |
