# Source: https://mikefarah.gitbook.io/yq/v3.x/usage/value-parsing.md

# Value Parsing

`yq` attempts to parse values intelligently, e.g. when a number is passed it - it will assume it's a number as opposed to a string. `yq` will not alter the representation of what you give. So if you pass '03.0' in, it will assume it's a number and keep the value formatted as it was passed in, that is '03.0'.

The `--tag` flag can be used to override the tag type to force particular tags.

## Default behavior

### Integers

*Given*

```bash
yq new key 3
```

results in

```yaml
key: 3
```

*Given a formatted number*

```bash
yq new key 03
```

results in

```yaml
key: 03
```

`yq` keeps the number formatted as it was passed in.

### Float

*Given*

```bash
yq new key "3.1"
```

results in

```yaml
key: 3.1
```

Note that quoting the number does not make a difference.

*Given a formatted decimal number*

```bash
yq new key 03.0
```

results in

```yaml
key: 03.0
```

`yq` keeps the number formatted as it was passed in

### Booleans

Note that `yq` supports yaml spec 1.2  - which means the values yes/no are no longer parsed as booleans, but as strings see <https://yaml.org/spec/1.2/spec.html> and <https://github.com/go-yaml/yaml/tree/v3> for more information.

```bash
yq new key true
```

results in

```yaml
key: true
```

### Nulls

```bash
yq new key null
```

results in

```yaml
key: null
```

```bash
yq new key '~'
```

results in

```yaml
key: ~
```

```bash
yq new key ''
```

results in

```yaml
key:
```

### Strings

```bash
yq new key whatever
```

results in

```yaml
key: whatever
```

```bash
yq new key ' whatever '
```

results in

```yaml
key: ' whatever '
```

## Using the tag flag to cast

Previous versions of yq required double quoting to force values to be strings, this no longer works - instead use the --tag flag.

### Casting booleans

```bash
yq new --tag '!!str' key true
```

results in

```yaml
key: "true"
```

### Casting nulls

```bash
yq new --tag '!!str' key null
```

results in

```yaml
key: "null"
```

### Custom types

```bash
yq new --tag '!!farah' key gold
```

results in

```yaml
key: !!farah gold
```

## The style flag

The `--style` flag can be used to specify the quote or block style of the node value. Valid values are

* single
* double
* folded
* flow
* literal
* tagged

For example, given:

```bash
MULTILINE=$(cat <<END
    This is line one.
    This is line two.
END
)

SINGLE="only one line"
```

### Single

```yaml
yq n --style single things "$MULTILINE"
```

```yaml
things: 'This is line one.

  This is line two.'
```

### Double

```yaml
things: "This is line one.\nThis is line two."
```

### Folded:

```yaml
things: >-
  This is line one.

  This is line two.

```

#### Folded single line:

```yaml
things: >-
  only one line
```

### Flow:

```yaml
things: |-
  This is line one.
  This is line two.

```

#### Flow single line:

```yaml
things: only one line
```

### Literal

```yaml
things: |-
  This is line one.
  This is line two.

```

#### Literal single line

```yaml
things: |-
  only one line
```

### Tagged

Always show the tag, note - you must also pass in `--tag='!!str'`

```yaml
things: !!str |-
  This is line one.
  This is line two.

```

#### Tagged single line

```yaml
things: !!str only one line
```
