# Source: https://docs.vale.sh/topics/actions.md

# Actions

Create dynamic suggestions for your rules with Actions.

{% hint style="info" %}
Heads up!

See [`vale-ls`](https://docs.vale.sh/guides/lsp) for an easy way to integrate Actions into your favorite text editor.
{% endhint %}

Actions provide a way for users to define dynamic fixes for their custom rules that show up in the CLI and LSP-based integrations.

![Actions](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/TwYY3qcoRCdqRoNp4mPw/action.png)

In the Sublime Text example above, the “Quick Fix” menu is powered by the action defined in the rule definition:

{% code title="rule.yml" %}

```yaml
action:
  name: replace
```

{% endcode %}

See the documentation on each `action` type for more information:

| Name                                            | Description                                                                                  |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [`suggest`](https://docs.vale.sh/fixes/suggest) | An array of dynamically-computed suggestions.                                                |
| [`replace`](https://docs.vale.sh/fixes/replace) | An array of static suggestions. Supported by default in `substitution` and `capitalization`. |
| [`remove`](https://docs.vale.sh/fixes/remove)   | Remove the matched text.                                                                     |
| [`edit`](https://docs.vale.sh/fixes/edit)       | In-place edits of the matched text.                                                          |

## [CLI](#cli)

Most Vale rules are based on *static* suggestions—for example,

{% code title="rule.yml" %}

```yaml
extends: substitution
message: "Use '%s' instead of '%s'."
level: error
action:
  name: replace
swap:
  Javascript: JavaScript
```

{% endcode %}

Here, the `action` is a to *replace*`Javascript` with `JavaScript`. In such cases, we know what we want to suggest to the user ahead of time and Vale can easily generate the appropriate output message.

However, there are cases in which we *don’t* know the appropriate suggestion ahead of time. For example, consider the following rule:

{% code title="rule.yml" %}

```yaml
extends: existence
message: "'%s' should be '%s'."
level: error
action:
  name: edit
  params:
    - regex
    - '(\w+)_(\w+)'
    - '$1-$2'
tokens:
  - '\w+_\w+'
```

{% endcode %}

This rule is designed to catch instances of `snake_case` and suggest that the user convert to `kebab-case`. In this case, the exact suggestion is dependent on a string transformation that needs to be computed at runtime.

Using the `edit` action allows us to define a rule that can dynamically generate suggestions based on the matched text in CLI output:

![CLI](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/AlAJw1s9hA1dsGPiGzd1/snake.png)

As you can see, the CLI output is dynamically computing the suggestion based on the matched text.

## [LSP](#lsp)

In both static and dynamic cases, any application that uses the [Vale Language Server](https://docs.vale.sh/guides/lsp) will be able to provide the user with a list of “Quick Fixes” that can be applied to the document.

[Scopes](https://docs.vale.sh/topics/scopes) [Filters](https://docs.vale.sh/topics/filters)
