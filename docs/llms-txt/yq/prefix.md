# Source: https://mikefarah.gitbook.io/yq/v3.x/commands/prefix.md

# Prefix

```
yq p <yaml_file> <path>
```

See docs for [path expression](https://mikefarah.gitbook.io/yq/v3.x/usage/path-expressions) for more details.

## Prefix a document

Given a data1.yaml file of:

```yaml
a:
  b: [1, 2]
```

then

```bash
yq p data1.yaml c.d
```

will output:

```yaml
c:
  d:
    a:
      b: [1, 2]
```

## Updating files in-place

```bash
yq p -i data1.yaml c
```

will update the data1.yaml file so that the path 'c' prefixes the document.

## Multiple Documents

### Prefix a single document

Given a data1.yaml file of:

```yaml
something: else
---
a: simple
b: cat
```

then

```bash
yq p -d1 data1.yaml c
```

will output:

```yaml
something: else
---
c:
  a: simple
  b: cat
```

### Prefix all documents

Given a data1.yaml file of:

```yaml
something: else
---
a: simple
b: cat
```

then

```bash
yq p -d'*' data1.yaml c
```

will output:

```yaml
c:
  something: else
---
c:
  a: simple
  b: cat
```
