# Source: https://firebase.google.com/docs/reference/rules/rules.Set.md.txt

# Interface: Set

# [rules](https://firebase.google.com/docs/reference/rules/rules).Set

interface static

Set type.

A set is an unordered collection. A set cannot contain duplicate items.

There is no set literal for use in creating sets. Instead, create sets from
lists using `List.toSet()`. See [rules.List](https://firebase.google.com/docs/reference/rules/rules.List).  

```scilab
// Create a set and check its size
['a','b'].toSet().size() == 2
```

In addition to the methods listed below, sets have the following operators:

*** ** * ** ***

| Operator |                                            Usage                                            |
|----------|---------------------------------------------------------------------------------------------|
| `x == y` | Compare sets x and y                                                                        |
| `v in x` | Check if value v exists in set x. For example: ```text 'a' in ['a','b'].toSet() == true ``` |

## Methods

### difference

difference() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a set that is the difference between the set calling
`difference()` and the set passed to `difference()`.
That is, returns a set containing the elements in the
comparison set that are not in the specified set.

If the sets are identical, returns an empty set (`size() == 0`).

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) difference set containing the elements found in the
    comparison set that are not gound in the calling set.

#### Example

    ['a','b'].toSet().difference(['a','c'].toSet()) == ['b'].toSet()

### hasAll

hasAll() returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Test whether the set calling `hasAll()` contains all of the items
in the comparison set passed to `hasAll()`.

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) whether the calling set contains all the items of
    the comparison set or list.

#### Example

    ['a','b'].toSet().hasAll(['a','c']) == false
    ['d','e','f'].toSet().hasAll(['d','e']) == true

### hasAny

hasAny() returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Test whether the set calling `hasAny()` contains any of the items
in the set or list passed to `hasAny()`.

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) whether the calling set contains any of the items
    of the comparison set or list.

#### Example

    ['a','b'].toSet().hasAny(['c','d'].toSet()) == false
    ['a','b'].toSet().hasAny(['a','c'].toSet()) == true

### hasOnly

hasOnly() returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Test whether the set calling `hasOnly()` contains only the items
in the comparison set or list passed to `hasOnly()`.

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) whether the calling set contains only the items of
    the comparison set or list.

#### Example

    ['a','b'].toSet().hasOnly(['a','c']) == false
    ['a','b'].toSet().hasOnly(['a','b']) == true

### intersection

intersection() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a set that is the intersection between the set calling
`intersection()` and the set passed to
`intersection()`. That is, returns a set containing the elements
the sets have in common.

If the sets have no elements in common, returns an empty set
(`size() == 0`).

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) intersection set containing the elements found in both
    the calling set and the comparison set.

#### Example

    ['a','b'].toSet().intersection(['a','c'].toSet()) == ['a'].toSet()

### size

size() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Returns the size of the set.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the number of values in the specified set.

### union

union() returns [rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set)

Returns a set that is the union of the set calling `union()` and
the set passed to `union()`. That is, returns a set that contains
all elements from both sets.

Returns

:   `non-null `[rules.Set](https://firebase.google.com/docs/reference/rules/rules.Set) union set containing all of the elements in both the
    calling set and comparison set.

#### Example

    ['a','b'].toSet().union(['a','c'].toSet()) == ['a', 'b', 'c'].toSet()