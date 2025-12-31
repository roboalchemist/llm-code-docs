# Source: https://firebase.google.com/docs/reference/rules/rules.Map.md.txt

# Interface: Map

# [rules](https://firebase.google.com/docs/reference/rules/rules).Map

interface static

Map type, used for simple key-value mappings.

Keys must be of type `rules.String`.

In addition to the methods listed below, maps have the following operators:

*** ** * ** ***

| Operator |                  Usage                  |
|----------|-----------------------------------------|
| `x == y` | Compare maps x and y                    |
| `x[k]`   | Index operator, get value at key name k |
| `x.k`    | Get value at key name k                 |
| `k in x` | Check if key k exists in map x          |

## Methods

### diff

diff(map_to_compare) returns [rules.MapDiff](https://firebase.google.com/docs/reference/rules/rules.MapDiff)

Return a [rules.MapDiff](https://firebase.google.com/docs/reference/rules/rules.MapDiff) representing the result of comparing the
current Map to a comparison Map.

|                                                                               #### Parameter                                                                               ||
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| map_to_compare | [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map) A Map to which the current (calling) Map will be compared. Value must not be null. |

Returns

:   `non-null `[rules.MapDiff](https://firebase.google.com/docs/reference/rules/rules.MapDiff) object representing the result of the comparison.

### get

get(key, default_value) returns value

Returns the value associated with a given search key string.

For nested Maps, involving keys and ***sub-keys***, returns the value
associated with a given sub-key string. The sub-key is identified using a
list, the first item of which is a top-level key and the last item the
sub-key whose value is to be looked up and returned. See the nested Map
example below.

The function requires a default value to return if no match to
the given search key is found.

|                                                                                                                                        #### Parameter                                                                                                                                        ||
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| key           | (non-null [rules.String](https://firebase.google.com/docs/reference/rules/rules.String) or non-null [rules.List](https://firebase.google.com/docs/reference/rules/rules.List)) Either a key specified as a string, or for nested Maps, a sub-key specified using list syntax. |
| default_value | default_value Value to return if the Map does not contain the given search key. Can be any Rules language type.                                                                                                                                                               |

Returns

:   `value` Value corresponding to the given `key`, or the
    default return value specified by `default_value` if no match to
    the given key is found. Since Map contents are user-defined, the data type of
    the returned `value` can be any Rules language type.

#### Example

    // "c" is not a key in the supplied Map, returns default value 7.
    {"a": 3,"b": 2}.get("c", 7) == 7

    // Default result can be any type, e.g. a list such as [1, 1].
    {"a": [2, 7], "b": [9, 12]}.get("c", [1, 1]) == [1, 1]

    // Return a list on a successful match.
    {"a": [2, 7],"b": [9, 12]}.get("b", [1, 1]) == [9, 12]

    // For nested Maps, use list ["a", "b"] to specify lookup on sub-key "b".
    {"a": {"b": 1},"c": 2}.get(["a", "b"], 7) == 1

### keys

keys() returns [rules.List](https://firebase.google.com/docs/reference/rules/rules.List)

Get the list of keys in the map.

Returns

:   `non-null `[rules.List](https://firebase.google.com/docs/reference/rules/rules.List) list of keys.

### size

size() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the number of entries in the map.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) number of entries.

### values

values() returns [rules.List](https://firebase.google.com/docs/reference/rules/rules.List)

Get the list of values in the map.

Returns

:   `non-null `[rules.List](https://firebase.google.com/docs/reference/rules/rules.List) list of values.