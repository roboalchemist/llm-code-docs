# Source: https://docs.vale.sh/fixes/edit.md

# edit

Learn how to make in-place edits to your matches.

```go
func edit(match string) string
```

`edit` will perform an in-place edit on the match string according to the provided parameters.

## [https://vale.sh/docs/fixers/edit#regex](#regex)

Replace the provided regex pattern with the given string.

```yaml
extends: existence
message: Consider removing '%s'
level: warning
action:
  name: edit
  params:
    - regex
    - '([A-Z]\w+)([A-Z]\w+)' # pattern
    - '$1-$2' # repl
tokens:
  - '([A-Z]\w+)([A-Z]\w+)'
```

This is equivalent to the following Go code:

```go
match = pattern.ReplaceAllString(match, repl)
```

## [https://vale.sh/docs/fixers/edit#trim\_right](#trim_right)

Trim the first parameter from the end of the matched text.

```yaml
extends: existence
message: "Don't use exclamation points in text."
nonword: true
action:
  name: edit
  params:
    - trim_right
    - '!'
tokens:
  - '\w+!(?:\s|$)'
```

## [https://vale.sh/docs/fixers/edit#trim\_left](#trim_left)

Trim the first parameter from the start of the matched text.

```yaml
extends: existence
message: "'%s' too many spaces."
level: warning
nonword: true
action:
  name: edit
  params:
    - trim_left
    - ' '
tokens:
  - '(?<=[a-z][.!?] ) [A-Z]'
```

[remove](https://docs.vale.sh/fixes/remove) [Front Matter](https://docs.vale.sh/formats/front-matter)
