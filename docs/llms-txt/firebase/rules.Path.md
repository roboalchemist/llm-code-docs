# Source: https://firebase.google.com/docs/reference/rules/rules.Path.md.txt

# Interface: Path

# [rules](https://firebase.google.com/docs/reference/rules/rules).Path

interface static

Directory-like pattern for the location of a resource. Paths can be created
in two ways. The first is in the "raw" form beginning with a forward
slash `/`:  

```text
/path/to/resource
```

The second is by converting from a string using the `path()`
function:  

```text
path("path/to/resource")
```

In addition to the methods listed below, paths have the following operators:

*** ** * ** ***

| Operator |                       Usage                       |
|----------|---------------------------------------------------|
| `x == y` | Compare paths x and y                             |
| `x[f]`   | Index operator, get value at binding field name f |
| `x[i]`   | Index operator, get value at numeric index i      |
| `x.f`    | Value at binding field name f                     |

## Method

### bind

bind(map)

Bind key-value pairs in a map to a path.

|                                                  #### Parameter                                                   ||
|-----|--------------------------------------------------------------------------------------------------------------|
| map | [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map) Map to bind. Value must not be null. |

#### Example

    // Make the path '/path/something/another' by binding a map
    (/path/$(foo)/$(bar)).bind({"foo": "something", "bar": "another"})