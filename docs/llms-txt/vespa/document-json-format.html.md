# Source: https://docs.vespa.ai/en/reference/schemas/document-json-format.html.md

# Document JSON format reference

 

This document describes the JSON format used for sending document operations to Vespa. Field types are defined in the[schema reference](schemas.html#field). This is a reference for:

- JSON representation of [document operations](#document-operations) (put, get, remove, update)
- JSON representation of [field types](#field-types) in Vespa documents
- JSON representation of addressing fields for update, and [update operations](#update-operations)

Also refer to [encoding troubleshooting](../../linguistics/troubleshooting-encoding.html).

```
[Document operations](#document-operations)[Put](#put)[Get](#get)[Remove](#remove)[Update](#update)[Test and set](#test-and-set)[Create](#create)[Field types](#field-types)[string](#string)[int](#int)[long](#long)[bool](#bool)[byte](#byte)[float](#float)[double](#double)[position](#position)[predicate](#predicate)[raw](#raw)[uri](#uri)[array](#array)[weightedset](#weightedset)[Tensors](#tensor)[Indexed tensors short form](#tensor-short-form-indexed)[Short form for tensors with a single mapped dimension](#tensor-short-form-mapped)[Mixed tensors short form](#tensor-short-form-mixed)[Cell values as binary data (hex dump format)](#tensor-hex-dump)[Tensor verbose form](#tensor-verbose-form)[struct](#struct)[map](#map)[reference](#reference)[Empty fields](#empty-fields)[Update operations](#update-operations)[assign](#assign)[Single value field](#single-value-field)[Assign tensor](#tensor-field)[Assign struct field](#<struct-field)[Replacing entire struct](#replacing-all-fields-in-a-struct)[Replace individual struct fields](#individual-struct-fields)[Assign map field](#assign-map-field)[Map to primitive value](#map-to-primitive-value)[Map to struct](#map-to-struct)[Arrays](#array-field)[Array of primitive values](#array-of-primitive-values)[Array of struct](#array-of-struct)[Weighted set field](#weighted-set-field)[Clearing a field](#clearing-a-field)[add](#add)[Add array elements](#add-array-elements)[Add to weighted set](#add-weighted-set)[Add to tensor](#tensor-add)[Remove elements in composites](#composite-remove)[Remove from weighted set field](#weighted-set-field-remove)[Remove from map field](#map-field-remove)[Remove from tensor](#tensor-remove)[Arithmetic](#arithmetic)[match](#match)[Tensor modify](#tensor-modify)[Fieldpath](#fieldpath)
```

## Field types

Unless otherwise noted, these formats are used both for returned values in read operations, and as input in write operations (put operations and field assign update operations).

| string | 

```
```
"name": "Polly"
```
```

Feeding in an empty string ("") for a field will have the same effect as not feeding a value for that field, and the field will not be rendered in the document API and in document summaries.

 |
| int | 

```
```
"age": 42
```
```
 |
| long | 

```
```
"current_time_ms": 1742837807000
```
```
 |
| bool | 

_true_ or _false_:

```
```
"alive": false
```
```
 |
| byte | 

```
```
"tinynumber": 128
```
```
 |
| float | 

```
```
"weight": 123.4567
```
```
 |
| double | 

```
```
"weight": 123.4567
```
```
 |
| position | 

A position is encoded as a lat/lng object:

```
```
"mypos": {
    "lat": 37.4181488,
    "lng": -122.0256157
}
```
```

See [Geo Search](../../querying/geo-search.html) for details.

 |
| predicate | 

A [predicate](../../schemas/predicate-fields.html) is represented with a string:

```
```
"predicate_field": "gender in [Female] and age in [20..30] and pos in [1..4]"
```
```
 |
| raw | 

The content of a [raw](schemas.html#raw) field is represented as a base64-encoded string:

```
```
"raw_field": "VW5rbm93biBhcnRpc3QgZnJvbSB0aGUgbW9vbg=="
```
```

When used as _summary_ field it will be rendered as a base64-encoded string.

 |
| uri | 

A URI is a string:

```
```
"url": "https://www.yahoo.com/"
```
```
 |
| array | 

Arrays are represented as JSON arrays.

```
```
"int_array_field": [
    123,
    456,
    789
]

"string_array_field": [
    "item 1",
    "item 2",
    "item 3"
]
```
```

An array of struct is represented as a JSON array of JSON objects matching the defined struct field:

```
```
"array_of_struct_field": [
   { "first_name": "Chris", "last_name": "Martin" },
   { "first_name": "James", "last_name": "Hetfield" },
   { "first_name": "Diana", "last_name": "Krall" }
]
```
```

Feeding in an empty array ([]) for a field will have the same effect as not feeding a value for that field, and the field will not be rendered in the document API and in document summaries.

 |
| weightedset | 

Weighted sets are represented as maps where the value is the weight. Note, even if the key is not a string as such, it will be represented as a string in the JSON format.

```
```
"int_weighted_set": {
    "123": 2,
    "456": 78
}

"string_weighted_set": {
    "item 1": 143,
    "item 2": 6
}
```
```

Feeding in an empty weightedset ({}) for a field will have the same effect as not feeding a value for that field, and the field will not be rendered in the document API and in document summaries.

 |
| tensor | 

**Indexed tensors short form:** An array where the values are ordered in the standard value order, where indexes of dimensions to the right are incremented before indexes to the left, where dimensions are ordered alphabetically (such that, e.g. with a tensor with dimensions x,y the "y" values for each value of "x" are adjacent):

```
```
"tensorfield": [2.0, 3.0, 5.0, 7.0]
```
```

The cells array can optionally be nested in an object under the key "values". This is how tensor values are returned [by default](../api/document-v1.html#format.tensors), along with another key "type" containing the tensor type.

**Short form for tensors with a single mapped dimension**: A map with the dimension key as key and the value as value.

```
```
"tensorfield": {
    "a": 2.0,
    "b": 3.0
}
```
```

The cells object can optionally be nested in an object under the key "cells". This is how tensor values are returned [by default](../api/document-v1.html#format.tensors), along with another key "type" containing the tensor type.

**Mixed tensors short form:** If the tensor has a single sparse dimension: A map where the key is the value of that dimension and the value is a nested array containing the values of the dense subspace within that key.  
 If the tensor has multiple sparse dimensions: An array nested in a "blocks" element where the elements consist of a map with the keys "address" and "values", where "address" is a map with the sparse dimensions and their values (as in cells), and "values" is a nested array containing the values of the dense subspace within that address.

Example - single sparse dimension:

```
```
"tensorfield": {
    "x1":[2.0,3.0],
    "x2":[4.0,5.0]
}
```
```

Example - multiple sparse dimensions:

```
```
"tensorfield": {
  "blocks": [
    {"address":{"x":"x1","y":"y2"},"values":[2.0,3.0]},
    {"address":{"x":"x2","y":"y2"},"values":[4.0,5.0]}
  ]
}
```
```

This is how tensor values are returned [by default](../api/document-v1.html#format.tensors), along with another key "type" containing the tensor type.

**Cell values as binary data** For dense and mixed tensors it's possible to fill the cell values directly from binary data sent in as a string of hexadecimal digits. The simplest possible case is if you have a vector with `int8` cell value type:

```
```
"tensorfield": {
    "values": "FF00118022FE"
}
```
```

This can be used to represent the value `tensor<int8>(x[6]):[-1,0,17,-128,34,-2]`.

For other cell types, it's possible to take the bits of the floating-point value, interpreted directly as an unsigned integer of appropriate width (16, 32, or 64 bits) and use the hex dump (respectively 4, 8, or 16 hex digits per cell) in a string. For "float" cells (32-bit IEE754 floating-point) a simple snippet for converting a cell could look like this:

```
```
import struct
def float_to_hex(f: float):
    return format(struct.unpack('=I', struct.pack('=f', f))[0], '08X')
```
```

As an advanced combination example, if you have a tensor with type `tensor<float>(tag{},x[3])` this input could be used, shown with corresponding output:

```
```
"mixedtensor": {
    "foo": "3DE38E393E638E393EAAAAAB",
    "bar": "3EE38E393F0E38E43F2AAAAB",
    "baz": "3F471C723F638E393F800000"
}
"mixedtensor":{
  "type":"tensor<float>(tag{},x[3])",
  "blocks":{
    "foo":[0.1111111119389534,0.2222222238779068,0.3333333432674408],
    "bar":[0.4444444477558136,0.5555555820465088,0.6666666865348816],
    "baz":[0.7777777910232544,0.8888888955116272,1.0]
  }
}
```
```

**Verbose:** [Tensor](../../ranking/tensor-user-guide.html) fields may be represented as an array of cells:

```
```
"tensorfield": [
    { "address": { "x": "a", "y": "0" }, "value": 2.0 },
    { "address": { "x": "a", "y": "1" }, "value": 3.0 },
    { "address": { "x": "b", "y": "0" }, "value": 4.0 },
    { "address": { "x": "b", "y": "1" }, "value": 5.0 }
]
```
```

This works for any tensor but is verbose, so shorter forms specific to various tensor types are also supported. Use the shortest form applicable to your tensor type for the best possible performance.

The cells array can optionally be nested in an object under the key "cells". This is how tensor values are returned [by default](../api/document-v1.html#format.tensors), along with another key "type" containing the tensor type.

 |
| struct | 

```
```
"mystruct": {
    "intfield": 123,
    "stringfield": "foo"
}
```
```
 |
| map | 

The JSON dictionary key must be a string, even if the map key type in the schema is not a string:

```
```
"int_to_string_map": {
    "123": "foo",
    "456": "bar",
    "789": "foobar"
}
```
```

Feeding in an empty map ({}) for a field will have the same effect as not feeding a value for that field, and the field will not be rendered in the document API and in document summaries.

 |
| reference | 

String with document ID referring to a [parent document](../../schemas/parent-child.html):

```
```
"artist_ref": "id:mynamespace:artists::artist-1"
```
```
 |
|
| |

## Empty fields

In general, fields that have not received a value during feeding will be ignored when rendering the document. They are considered as empty fields. However, certain field types have some values which causes them to be considered empty. For instance, the empty string ("") is considered empty, as well as the empty array ([]). See the above table for more information for each type.

## Document operations

Refer to [reads and writes](../../writing/reads-and-writes.html) for details - alternatives:

- Use the [Vespa CLI](../../clients/vespa-cli.html#documents).
- [/document/v1/](../api/document-v1.html): This API accepts one operation per request, with the document ID encoded in the URL. 
- [Vespa feed client](../../clients/vespa-feed-client.html): Java APIs / command line tool to feed document operations asynchronously to Vespa, over HTTP. 

### Put

The "put" payload has a "put" operation and ["fields"](#field-types) containing field values; ([/document/v1/ example](../../writing/document-v1-api-guide.html#post)):

```
```
{
    "put": "id:mynamespace:music::123",
    "fields": {
        "title": "Best of Bob Dylan"
    }
}
```
```

### Get

"get" does not have a payload - the response has the same "field" object as in "put", and also "id" and "pathId" fields ([/document/v1/ example](../../writing/document-v1-api-guide.html#get)):

```
```
{
    "pathId": "/document/v1/mynamespace/music/docid/123",
    "id": "id:mynamespace:music::123",
    "fields": {
        "title": "Best of Bob Dylan"
    }
}
```
```

### Remove

The "remove" payload only has a "remove" operation ([/document/v1/ example](../../writing/document-v1-api-guide.html#delete)):

```
```
{
    "remove": "id:mynamespace:music::123"
}
```
```

### Update

The "update" payload has an "update" operation and "fields". Note: Each field must contain an [update operation](#update-operations), not just the field value directly; ([/document/v1/ example](../../writing/document-v1-api-guide.html#put)):

```
```
{
    "update": "id:mynamespace:music::123",
    "fields": {
        "title": {
            "assign": "The best of Bob Dylan"
        }
    }
}
```
```

Flags can be added to add a [test and set](#test-and-set) condition, or allow the update to [create](#create) a new document (a so-called "upsert" operation).

#### Test and set

An optional _condition_ can be added to operations to specify a _test and set_ condition - see [conditional writes](../../writing/document-v1-api-guide.html#conditional-writes). The value of the _condition_ is a [document selection](../writing/document-selector-language.html), encoded as a string. Example: Increment the _sales_ field only if it is already equal to 999 ([/document/v1/ example](../../writing/document-v1-api-guide.html#conditional-writes)):

```
```
{
    "update": "id:mynamespace:music::bob/BestOf",
    "condition": "music.sales==999",
    "fields": {
        "sales": {
            "increment": 1
        }
    }
}
```
```

 **Note:** Use _documenttype.fieldname_ in the condition, not only _fieldname_.

If the condition is not met, a 412 response code is returned.

#### create (create if nonexistent)

**Updates** to nonexistent documents are supported using _create_; ([/document/v1/ example](../../writing/document-v1-api-guide.html#create-if-nonexistent)):

```
```
{
    "update": "id:mynamespace:music::bob/BestOf",
    "create": true,
    "fields": {
        "title": {
            "assign": "The best of Bob Dylan"
        }
    }
}
```
```

Since Vespa 8.178, _create_ can also be used together with conditional **Put** operations ([/document/v1/ example](../../writing/document-v1-api-guide.html#conditional-updates-and-puts-with-create) - review notes there before using):

```
```
{
    "put": "id:mynamespace:music::123",
    "condition": "music.sales==999",
    "create": true,
    "fields": {
        "title": "Best of Bob Dylan"
    }
}
```
```

## Update operations

The update operations are: [`assign`](#assign), [`add`](#add), [`remove`](#composite-remove), [arithmetics](#arithmetic) (`increment` `decrement` `multiply` `divide`), [`match`](#match), [`modify`](#tensor-modify)

## assign

`assign` is used to replace the value of a field (or an element of a collection) with a new value. When assigning, one can generally use the same syntax and structure as when feeding that field's value in a `put` operation.

### Single value field

```
field title type string {
    indexing: summary
}
```

```
```
{
    "update": "id:mynamespace:music::example",
    "fields": {
        "title": {
            "assign": "The best of Bob Dylan"
        }
    }
}
```
```

### Tensor field

```
field tensorfield type tensor(x{},y{}) {
    indexing: attribute | summary
}
```

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "assign": {
                "cells": [
                    { "address": { "x": "a", "y": "b" }, "value": 2.0 },
                    { "address": { "x": "c", "y": "d" }, "value": 3.0 }
                ]
            }
        }
    }
}
```
```

This will fully replace the entire tensor stored in this field.

### Struct field

#### Replacing all fields in a struct

A full struct is replaced by assigning an object of struct key/value pairs.

```
struct person {
    field first_name type string {}
    field last_name type string {}
}
field contact type person {
    indexing: summary
}
```

```
```
{
    "update": "id:mynamespace:workers::example",
    "fields": {
        "contact": {
            "assign": {
                "first_name": "Bob",
                "last_name": "The Plumber"
            }
        }
    }
}
```
```

#### Individual struct fields

Individual struct fields are updated using [field path](#fieldpath) syntax. Refer to the [reference](schemas.html#struct-name) for restrictions using structs.

```
```
{
    "update": "id:mynamespace:workers::example",
    "fields": {
        "contact.first_name": {
            "assign": "Bob"
        },
        "contact.last_name": {
            "assign": "The Plumber"
        }
    }
}
```
```

### Map field

Individual map entries can be updated using [field path](document-field-path.html) syntax. The following declaration defines a `map` where the `key` is an Integer and the value is a `person` struct.

```
struct person {
    field first_name type string {}
    field last_name type string {}
}
field contact type map<int, person> {
    indexing: summary
}
```

Example updating part of an entry in the `contact` map:

- `contact` is the name of the map field to be updated
- `{0}` is the key that is going to be updated
- `first_name` is the struct field to be updated inside the `person` struct

```
```
{
    "update": "id:mynamespace:workers::example",
    "fields": {
        "contact{0}.first_name": {
            "assign": "John"
        }
    }
}
```
```

Assigning an element to a key in a map will insert the key/value mapping if it does not already exist, or overwrite it with the new value if it does exist. Refer to the [reference](schemas.html#map) for restrictions using maps.

#### Map to primitive value

```
field my_food_scores type map<string, string> {
    indexing: summary
}
```

```
```
{
    "update": "id:mynamespace:food::example",
    "fields": {
        "my_food_scores{Strawberries}": {
            "assign": "Delicious!"
        }
    }
}
```
```

#### Map to struct

```
struct contact_info {
    field phone_number type string {}
    field email type string {}
}
field contacts type map<string, contact_info> {
    indexing: summary
}
```

```
```
{
    "update": "id:mynamespace:people::d_duck",
    "fields": {
        "contacts{\"Uncle Scrooge\"}": {
            "assign": {
                "phone_number": "555-123-4567",
                "email": "number_one_dime_luvr1877@example.com"
            }
        }
    }
}
```
```

### Array field

#### Array of primitive values

```
field ingredients type array<string> {
    indexing: summary
}
```

Assign full array:

```
```
{
    "update": "id:mynamespace:cakes:tasty_chocolate_cake",
    "fields": {
        "ingredients": {
            "assign": ["sugar", "butter", "vanilla", "flour"]
        }
    }
}
```
```

Assign existing elements in array:

```
```
{
    "update": "id:mynamespace:cakes:tasty_chocolate_cake",
    "fields": {
        "ingredients[3]": {
            "assign": "2 cups of flour (editor's update: NOT asbestos!)"
        }
    }
}
```
```

Note that the index element 3 needs to exist. Alternative using match:

```
```
{
    "update": "id:mynamespace:cakes:tasty_chocolate_cake",
    "fields": {
        "ingredients": {
            "match": {
                "element": 3,
                "assign": "2 cups of flour (editor's update: NOT asbestos!)"
            }
        }
    }
}
```
```

Individual array elements may be updated using [field path](document-field-path.html) or [match](#match) syntax.

#### Array of struct

Refer to the reference for restrictions using[array of structs](schemas.html#array).

```
struct person {
    field first_name type string {}
    field last_name type string {}
}
field people type array<person> {
    indexing: summary
}
```

```
```
{
    "update": "id:mynamespace:students:example",
    "fields": {
        "people[34]": {
            "assign": {
                "first_name": "Bobby",
                "last_name": "Tables"
            }
        }
    }
}
```
```

Note that the element index needs to exist. Use [add](#add-array-elements) to add a new element. Alternative syntax using match:

```
```
{
    "update": "id:mynamespace:students:example",
    "fields": {
        "people": {
            "match": {
                "element": 34,
                "assign": {
                     "first_name": "Bobby",
                     "last_name": "Tables"
                }
            }
        }
    }
}
```
```

### Weighted set field

Adding new elements to a weighted set can be done using [add](#add-weighted-set), or by assigning with `field{key}` syntax. Example of the latter:

```
field int_weighted_set type weightedset<int> {
    indexing: summary
}
field string_weighted_set type weightedset<string> {
    indexing: summary
}
```

```
```
{
    "update":"id:mynamespace:weightedsetdoctype::example1",
    "fields": {
        "int_weighted_set{123}": {
            "assign": 123
        },
        "int_weighted_set{456}": {
            "assign": 100
        },
        "string_weighted_set{\"item 1\"}": {
            "assign": 144
        },
        "string_weighted_set{\"item 2\"}": {
            "assign": 7
        }
    }
}
```
```

Note that using the `field{key}` syntax for weighted sets _may_ be less efficient than using [add](#add-weighted-set).

### Clearing a field

To clear a field, assign a `null` value to it.

```
```
{
    "update": "id:mynamespace:music::example",
    "fields": {
        "title": {
            "assign": null
        }
    }
}
```
```

## add

`add` is used to add entries to arrays, weighted sets or to the mapped dimensions of tensors.

### Adding array elements

The added entries are appended to the end of the array in the order specified.

```
field tracks type array<string> {
    indexing: summary
}
```

```
```
{
    "update": "id:mynamespace:music::https://music.yahoo.com/bobdylan/BestOf",
    "fields": {
       "tracks": {
            "add": [
                "Lay Lady Lay",
                "Every Grain of Sand"
            ]
        }
    }
}
```
```

### Add weighted set entries

Add weighted set elements by using a JSON key/value syntax, where the value is the weight of the element.

Adding a key/weight mapping that already exists will overwrite the existing weight with the new one.

```
field int_weighted_set type weightedset<int> {
    indexing: summary
}
field string_weighted_set type weightedset<string> {
    indexing: summary
}
```

```
```
{
    "update":"id:mynamespace:weightedsetdoctype::example1",
    "fields": {
        "int_weighted_set": {
            "add": {
                "123": 123,
                "456": 100
            }
        },
        "string_weighted_set": {
            "add": {
                "item 1": 144,
                "item 2": 7
            }
        }
    }
}
```
```

### Add tensor cells

Add cells to mapped or mixed tensors. Invalid for tensors with only indexed dimensions. Adding a cell that already exists will overwrite the cell value with the new value. The address must be fully specified, but cells with bound indexed dimensions not specified will receive the default value of `0.0`. See system test[tensor add update](https://github.com/vespa-engine/system-test/tree/master/tests/search/tensor_feed/tensor_add_remove_update)for more examples.

```
field tensorfield type tensor(x{},y[3]) {
    indexing: attribute | summary
}
```

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "add": {
                "cells": [
                    { "address": { "x": "b", "y": "0" }, "value": 2.0 },
                    { "address": { "x": "b", "y": "1" }, "value": 3.0 }
                ]
            }
        }
    }
}
```
```

In this example, cell `{"x":"b","y":"2"}` will implicitly be set to 0.0.

So if you started with the following tensor:

```
{
    {"x": "a", "y": "0"}: 0.2,
    {"x": "a", "y": "1"}: 0.3,
    {"x": "a", "y": "2"}: 0.5,
}
```

You now end up with this tensor after the above add operation was applied:

```
{
    {"x": "a", "y": "0"}: 0.2,
    {"x": "a", "y": "1"}: 0.3,
    {"x": "a", "y": "2"}: 0.5,
    {"x": "b", "y": "0"}: 2.0,
    {"x": "b", "y": "1"}: 3.0,
    {"x": "b", "y": "2"}: 0.0,
}
```

Prefer the _block short form_ for mixed tensors instead. This also avoids the problem where cells with indexed dimensions are not specified:

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "add": {
                "blocks": [
                    { "address": { "x": "b" }, "values": [2.0, 3.0, 5.0] }
                ]
            }
        }
    }
}
```
```

## remove

Remove elements from weighted sets, maps and tensors with `remove`.

### Weighted set field

```
field string_weighted_set type weightedset<string> {
    indexing: summary
}
```

```
```
{
    "update":"id:mynamespace:weightedsetdoctype::example1",
    "fields": {
        "string_weighted_set": {
            "remove": {
                "item 2": 0
            }
        }
    }
}
```
```

### Map field

```
field string_map type map<string, string> {
    indexing: summary
}
```

```
```
{
    "update":"id:mynamespace:mapdoctype::example1",
    "fields": {
        "string_map{item 2}": {
            "remove": 0
        }
    }
}
```
```

### Tensor field

Removes cells from mapped or mixed tensors. Invalid for tensors with only indexed dimensions. Only mapped dimensions should be specified for tensors with both mapped and indexed dimensions, as all indexed cells the mapped dimensions point to will be removed implicitly. See system test[tensor remove update](https://github.com/vespa-engine/system-test/tree/master/tests/search/tensor_feed/tensor_add_remove_update)for more examples.

```
field tensorfield type tensor(x{},y[2]) {
    indexing: attribute | summary
}
```

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "remove": {
                "addresses": [
                    {"x": "b"},
                    {"x": "c"}
                ]
            }
        }
    }
}
```
```

In this example, cells `{x:b,y:0},{x:b,y:1},{x:c,y:0},{x:c,y:1}` will be removed.

It is also supported to specify only a subset of the mapped dimensions in the addresses. In that case, all cells that match the label values of the specified dimensions are removed. In the given example, all cells having label `b` for dimension `x` are removed.

```
field tensorfield type tensor(x{},y{},z[2]) {
    indexing: attribute | summary
}
```

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "remove": {
                "addresses": [
                    {"x": "b"}
                ]
            }
        }
    }
}
```
```

## Arithmetic

The four arithmetic operators `increment`, `decrement`,`multiply` and `divide` are used to modify _single value_ numeric values without having to look up the current value before applying the update. Example:

```
field sales type int {
    indexing: summary | attribute
}
```

```
```
{
    "update": "id:mynamespace:music::https://music.yahoo.com/bobdylan/BestOf",
    "fields": {
        "sales": {
            "increment": 1
        }
    }
}
```
```

## match

If an arithmetic operation is to be done for a specific key in a _weighted set or array_, use the `match` operation:

```
field track_popularity type weightedset<string> {
    indexing: summary | attribute
}
```

```
```
{
    "update": "id:mynamespace:music::https://music.yahoo.com/bobdylan/BestOf",
    "fields": {
        "track_popularity": {
            "match": {
                "element": "Lay Lady Lay",
                "increment": 1
            }
        }
    }
}
```
```

In other words, for the weighted set "track\_popularity",`match` the element "Lay Lady Lay", then `increment` its weight by 1. See the [weightedset properties](schemas.html#weightedset-properties)reference for how to make incrementing a non-existing key trigger auto-create of the key.

If the updated field is an array, the `element` value would be a positive integer.

 **Note:** Only oneelement can be matched per operation.

## Modify tensors

Individual cells in tensors can be modified using the `modify` update. The cells are modified according to the given operation:

- `replace` - replaces a single cell value
- `add` - adds a value to the existing cell value
- `multiply` - multiples a value with the existing cell value

The addresses of cells must be fully specified. If the cell does not exist, the update for that cell will be ignored. Use `"create": true` (see example below) to create non-existing cells before the modify update is applied. See system test[tensor modify update](https://github.com/vespa-engine/system-test/tree/master/tests/search/tensor_feed/tensor_modify_update)for more examples.

```
field tensorfield type tensor(x[3]) {
    indexing: attribute | summary
}
```

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "modify": {
                "operation": "replace",
                "addresses": [
                    { "address": { "x": "1" }, "value": 7.0 },
                    { "address": { "x": "2" }, "value": 8.0 }
                ]
            }
        }
    }
}
```
```

In this example, cell `{"x":"1"}` is replaced with value 7.0 and `{"x":"2"}` with value 8.0. If operation `add` or `multiply` was used instead, 7.0 and 8.0 would be added or multiplied to the current values of cells `{"x":"1"}` and `{"x":"2"}`.

For tensors with a single mapped dimension the _cells short form_ can also be used:

```
field tensorfield type tensor(x{}) {
    indexing: attribute | summary
}
```

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "modify": {
                "operation": "add",
                "create": true,
                "cells": {
                    "b": 5.0,
                    "c": 6.0
                }
            }
        }
    }
}
```
```

In this example, 5.0 is added to cell `{"x":"b"}` and 6.0 is added to cell `{"x":"c"}`. With `"create": true` non-existing cells in the input tensor are created before applying the modify update. The default cell value is 0.0 for `replace` and `add`, and 1.0 for `multiply`. This means a non-existing cell ends up with the value specified in the operation.

For mixed tensors the _block short form_ can also be used to modify entire dense subspaces:

```
field tensorfield type tensor(x{},y[3]) {
    indexing: attribute | summary
}
```

```
```
{
    "update": "id:mynamespace:tensordoctype::example",
    "fields": {
        "tensorfield": {
            "modify": {
                "operation": "replace",
                "blocks": {
                    "a": [1,2,3],
                    "b": [4,5,6]
                }
            }
        }
    }
}
```
```

## Fieldpath

Fieldpath is for accessing fields within composite structures - for structures that are not part of index or attribute, it is possible to access elements directly using fieldpaths. This is done by adding more information to the field value. For map structures, specify the key (see [example](#assign)).

```
mymap{mykey}
```

and then do operation on the element which is keyed by "mykey". Arrays can be accessed as well (see [details](#assign)).

```
myarray[3]
```

And this is also true for structs (see [details](#assign)).**Note:** Struct updates do not work for[index](../applications/services/content.html#document) mode:

```
mystruct.value1
```

This also works for nested structures, e.g. a `map` of `map` to `array` of `struct`:

```
```
{
    "update": "id:mynamespace:complexdoctype::foo",
    "fields": {
        "nested_structure{firstMapKey}{secondMapKey}[4].title": {
            "assign": "Look at me, mom! I'm hiding deep in a nested type!"
        }
    }
}
```
```

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Field types](#field-types)
- [Empty fields](#empty-fields)
- [Document operations](#document-operations)
- [Put](#put)
- [Get](#get)
- [Remove](#remove)
- [Update](#update)
- [Update operations](#update-operations)
- [assign](#assign)
- [Single value field](#single-value-field)
- [Tensor field](#tensor-field)
- [Map field](#assign-map-field)
- [Array field](#array-field)
- [Weighted set field](#weighted-set-field)
- [Clearing a field](#clearing-a-field)
- [add](#add)
- [Adding array elements](#add-array-elements)
- [Add weighted set entries](#add-weighted-set)
- [Add tensor cells](#tensor-add)
- [remove](#composite-remove)
- [Weighted set field](#weighted-set-field-remove)
- [Map field](#map-field-remove)
- [Tensor field](#tensor-remove)
- [Arithmetic](#arithmetic)
- [match](#match)
- [Modify tensors](#tensor-modify)
- [Fieldpath](#fieldpath)

