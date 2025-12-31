# Source: https://firebase.google.com/docs/reference/rules/rules.MapDiff.md.txt

# Interface: MapDiff

# [rules](https://firebase.google.com/docs/reference/rules/rules).MapDiff

interface static

MapDiff type.

The MapDiff type represents the result of comparing two
[rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map) objects.

There is no MapDiff literal for use in creating diffs. MapDiff objects
are returned by calls to the [rules.Map#diff](https://firebase.google.com/docs/reference/rules/rules.Map#diff) function.

The MapDiff functions described below are called by chaining with
[rules.Map#diff](https://firebase.google.com/docs/reference/rules/rules.Map#diff). All MapDiff functions return [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)
objects listing keys compared between Map objects.  

```scilab
// Compare two Map objects and return whether the key "a" has been
// affected; that is, key "a" was added or removed, or its value was updated.
request.resource.data.diff(resource.data).affectedKeys().hasOnly(["a"]);
```

## Methods

### addedKeys

addedKeys() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set), which lists any keys that the Map calling
`diff()` contains that the Map passed to `diff()` does
not.

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) , a list of keys added to the [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map) passed to
    the `Map.diff()` function.

#### Example

    {"a":1}.diff({}).addedKeys() == ["a"].toSet()

### affectedKeys

affectedKeys() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set), which lists any keys that have been added to,
removed from or modified from the Map calling `diff()` compared to
the Map passed to `diff()`. This function returns the set
equivalent to the combined results of `MapDiff.addedKeys()`,
`MapDiff.removedKeys()` and `MapDiff.changedKeys()`.  

```text
({"a":0, "c":0, "u":0}).diff({"r":0, "c":1, "u": 0}).affectedKeys() ==
Â Â Â Â Â ["a", "r", "c"].toSet()
```

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) ,a list of keys added to, removed from or changed from
    the [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map) passed to the `Map.diff()` function.

### changedKeys

changedKeys() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set), which lists any keys that appear in both the Map
calling `diff()` and the Map passed to `diff()`, but
whose values are not equal.

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) , a list of keys that appear in both [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map)s
    but whose values are not equal.

#### Example

    {"a":0}.diff({"a":1, "b":4}).changedKeys() == ["a"].toSet()

### removedKeys

removedKeys() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set), which lists any keys that the Map calling
`diff()` does not contain compared to the Map passed to
`diff()`.

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) , a list of keys removed from the [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map)
    passed to the `Map.diff()` function.

#### Example

    {}.diff({"a":1}).removedKeys() == ["a"].toSet()

### unchangedKeys

unchangedKeys() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set), which lists any keys that appear in both the Map
calling `diff()` and the Map passed to `diff()`, and
whose values are equal.

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) , a list of keys that appear in both [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map)s
    but whose values are equal.

#### Example

    {"a": 0}.diff({"a":0}).unchangedKeys() == ["a"].toSet()