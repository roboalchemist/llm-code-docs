# Source: https://firebase.google.com/docs/reference/rules/rules.List.md.txt

# Interface: List

# [rules](https://firebase.google.com/docs/reference/rules/rules).List

interface static

List type. Items are not necessarily homogenous.

In addition to the methods listed below, lists have the following operators:

*** ** * ** ***

| Operator |                                  Usage                                  |
|----------|-------------------------------------------------------------------------|
| `x == y` | Compare lists x and y                                                   |
| `x[i]`   | Index operator, get value index i                                       |
| `x[i:j]` | Range operator, get sublist from index i to j                           |
| `v in x` | Check if value v exists in list x. ```text 'a' in ['a','b'] == true ``` |

## Methods

### concat

concat(list) returns [rules.List](https://firebase.google.com/docs/reference/rules/rules.List)

Create a new list by adding the elements of another list to the
end of this list.

|                                                        #### Parameter                                                        ||
|------|------------------------------------------------------------------------------------------------------------------------|
| list | [rules.List](https://firebase.google.com/docs/reference/rules/rules.List) list to concatenate. Value must not be null. |

Returns

:   `non-null `[rules.List](https://firebase.google.com/docs/reference/rules/rules.List) the list with all elements of the other list added.

### hasAll

hasAll(list) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Determine whether the list contains all elements in another list.

|                                                              #### Parameter                                                               ||
|------|-------------------------------------------------------------------------------------------------------------------------------------|
| list | [rules.List](https://firebase.google.com/docs/reference/rules/rules.List) The list of elements to look for. Value must not be null. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if this list contains all elements in the
    other.

### hasAny

hasAny(list) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Determine whether the list contains any element in another list.

|                                                              #### Parameter                                                               ||
|------|-------------------------------------------------------------------------------------------------------------------------------------|
| list | [rules.List](https://firebase.google.com/docs/reference/rules/rules.List) The list of elements to look for. Value must not be null. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if this list contains any element in the
    other.

### hasOnly

hasOnly(list) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Determine whether all elements in the list are present in another list.

|                                                              #### Parameter                                                               ||
|------|-------------------------------------------------------------------------------------------------------------------------------------|
| list | [rules.List](https://firebase.google.com/docs/reference/rules/rules.List) The list of elements to look for. Value must not be null. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if all elements in the list are present
    in another list, excluding repeated elements.

#### Example

    ['a', 'b'].hasOnly(['a', 'c']) == false
    ['a', 'b'].hasOnly(['a', 'b', 'c']) == true
    ['a', 'b'].hasOnly(['b', 'a']) == true
    ['a', 'a', 'b'].hasOnly(['a', 'b', 'b']) == true
    ['a', 'a', 'b'].hasOnly(['a', 'b', 'b', 'c']) == true

### join

join(separator) returns [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

Join the elements in the list into a string, with a separator.

|                                                                #### Parameter                                                                 ||
|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| separator | [rules.String](https://firebase.google.com/docs/reference/rules/rules.String) String to separate elements. Value must not be null. |

Returns

:   `non-null `[rules.String](https://firebase.google.com/docs/reference/rules/rules.String) the list joined as a string.

### removeAll

removeAll(list) returns [rules.List](https://firebase.google.com/docs/reference/rules/rules.List)

Create a new list by removing the elements of another list from this list.

|                                                            #### Parameter                                                            ||
|------|--------------------------------------------------------------------------------------------------------------------------------|
| list | [rules.List](https://firebase.google.com/docs/reference/rules/rules.List) list of elements to remove.. Value must not be null. |

Returns

:   `non-null `[rules.List](https://firebase.google.com/docs/reference/rules/rules.List) the list with all elements of the other list removed.

### size

size() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the number of values in the list.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the number of values in the list.

### toSet

toSet() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a set containing all unique elements in the list.

In case that two or more elements are equal but non-identical, the result set
will only contain the first element in the list. The remaining elements are
discarded.

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) set containing unique values in the given list.