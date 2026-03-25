# Source: https://redocly.com/docs/cli/rules/oas/tags-alphabetical.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/tags-alphabetical.md

# tags-alphabetical

Ensures that all tag `name` fields in the `tags` object are listed in alphabetical order.
Note that this rule does not automatically sort your tags if they are not in alphabetical order.
The rule only produces a warning or an error, and expects you to modify your API descriptions.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

Information architecture is important. Among other benefits, it improves the efficiency and speed with which people discover information in the resources you provide.
When deciding how to organize tags in your API descriptions and documentation, you can try different approaches through tree testing (we did some tree testing on Redocly documentation navigation).
However, sometimes it's easier to keep things simple, and go alphabetical. If you've already decided to alphabetize, this rule keeps it alphabetized.

We've been here and it's ugly:

> X: "Can't you see it's in alphabetical order?"
Y: "Can't you talk to me like an adult?"
X: "Don't adults know the alphabet?"


This rule is intended to prevent bikeshedding and diffuse tension between teammates (could be renamed to peacemaker).

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off` (in `recommended` configuration). |
| ignoreCase | boolean | Possible values: `true`, `false`. Default `false` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  tags-alphabetical: error
```

## Examples

Given this configuration:


```yaml
rules:
  tags-alphabetical: error
```

Example of **incorrect** tags:


```yaml
tags:
  - name: Partner APIs
  - name: External APIs
  - name: Testing APIs
  - name: Central Management APIs
```

Example of **correct** tags:


```yaml
tags:
  - name: Central Management APIs
  - name: External APIs
  - name: Partner APIs
  - name: Testing APIs
```

## Related rules

- [tag-description](/docs/cli/v1/rules/oas/tag-description)
- [operation-description](/docs/cli/v1/rules/oas/operation-description)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/tags-alphabetical.ts)
- [Tags docs](https://redocly.com/docs/openapi-visual-reference/tags/)