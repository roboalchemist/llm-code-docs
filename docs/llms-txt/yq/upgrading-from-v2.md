# Source: https://mikefarah.gitbook.io/yq/v3.x/upgrading-from-v2.md

# Upgrading from V2

## New Features

* Keeps yaml comments and formatting, can specify yaml [tags](https://mikefarah.gitbook.io/yq/v3.x/usage/value-parsing#using-the-tag-field-to-override) when updating.
* Handles anchors!
* Can print out matching paths and values when splatting, more info [here](https://mikefarah.gitbook.io/yq/v3.x/commands/read#printing-matching-paths).
* JSON output works for all commands! Yaml files with multiple documents are printed out as one JSON document per line, more info [here](https://mikefarah.gitbook.io/yq/v3.x/usage/convert)
* Deep splat (`**`) to match arbitrary paths and match nodes by their children, more info [here](https://mikefarah.gitbook.io/yq/v3.x/usage/path-expressions)

## Breaking Changes

### Parsing values from the CLI

In V3 users are able to better control how values are treated when updating YAML by using a new `--tag` argument (see more info [here](https://mikefarah.gitbook.io/yq/v3.x/usage/value-parsing)). A result of this however, is that quoting values, e.g. "true" will no longer have an effect on how the value is interpreted like it did in V2.

For instance, to get the *string* "true" into a yaml file:

V2:

```
yq n a.path '"true"'
```

V3

```
yq n a.path --tag '!!str' true
```

### Reading paths that don't exist

In V2 this would return null, V3 does not return anything.

Similarly, reading null yaml values `null`, `~` and , V2 returns null whereas V3 returns the values as is.

This is a result of taking effort not to format values coming in and out of the original YAML.

### Update scripts file format has changed to be more powerful.

Comments can be added, and delete commands have been introduced.

V2

```
b.e[+].name: Mike Farah
```

V3

```yaml
- command: update 
  path: b.e[+].thing
  value:
    #great 
    things: frog # wow!
- command: delete
  path: b.d
```

### Reading and splatting, matching results are printed once per line.

e.g:

```yaml
parent:
  childA: 
    no: matches here
  childB:
    there: matches
    hi: no match
    there2: also matches
```

```
yq r sample.yaml 'parent.*.there*'
```

V2

```
- null
- - matches
  - also matches
```

V3

```
matches
also matches
```

### Converting JSON to YAML

As JSON is a subset of YAML, and `yq` now preserves the formatting of the passed in document, you will most likely need to use the `--prettyPrint` flag to format the JSON document as idiomatic YAML. See [Working with JSON](https://mikefarah.gitbook.io/yq/v3.x/usage/convert#json-to-yaml) for more info.
