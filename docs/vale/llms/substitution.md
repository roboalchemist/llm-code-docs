# Source: https://docs.vale.sh/checks/substitution.md

# substitution

Learn about the substitution extension point.

| Name         | Type    | Description                                                               |
| ------------ | ------- | ------------------------------------------------------------------------- |
| `append`     | `bool`  | Adds `raw` to the end of `tokens`, assuming both are defined.             |
| `ignorecase` | `bool`  | Makes all matches case-insensitive.                                       |
| `nonword`    | `bool`  | Removes the default word boundaries (`\b`).                               |
| `swap`       | `map`   | A sequence of `observed: expected` pairs.                                 |
| `exceptions` | `array` | An array of strings to be ignored.                                        |
| `vocab`      | `bool`  | If false, disables all active vocabularies for this rule (default: true). |
| `capitalize` | `bool`  | Matches the capitalization of the source token.                           |

`substitution` associates a string with a preferred form.

```
yaml
Copy

extends: substitution
message: Consider using '%s' instead of '%s'
level: warning
ignorecase: false
# swap maps tokens in form of bad: good
swap:
  abundance: plenty
  accelerate: speed up
```

If we want to suggest the use of “plenty” instead of “abundance,” for example, we’d write:

```
yaml
Copy

swap:
  abundance: plenty
```

## Regex keys

The keys may also be regular expressions:

```
yaml
Copy

swap:
  '(?:give|gave) rise to': lead to
```

You can also reference capture groups for more dynamic substitutions:

```
yaml
Copy

swap:
  'within the (.*)?directory': in the $1 directory
```

## Multiple suggestions

In some cases, you may want to suggest multiple alternatives for a single token. You can do this by separating them with a pipe ("|"):

```
yaml
Copy

extends: substitution
# NOTE: We don't quote the first '%s':
message: Consider using %s instead of '%s.'
level: warning
# NOTE: The action is required.
action:
  name: replace
swap:
  # You can suggest multiple alternatives for a single token
  # by separating them with a pipe ("|").
  masterful: skilled|authoritative|commanding
```

In the CLI, this will render as a sentence with multiple suggestions:

![Multiple suggestions](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/ndXPk2UKcmhPFauXBQlf/pipe.png)

In LSP-based editors, the suggestions will be presented as a list of ‘Quick Fixes’. See the [LSP guide](https://docs.vale.sh/guides/lsp) for more information.

## message

`substitution` can have one or two `%s` format specifiers in its message. This allows us to do either of the following:

```
yaml
Copy

message: "Consider using '%s' instead of '%s'."
# or
message: "Consider using '%s'."
```

[existence](https://docs.vale.sh/checks/existence) [occurrence](https://docs.vale.sh/checks/occurrence)
