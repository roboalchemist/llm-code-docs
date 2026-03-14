# Source: https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data

Title: Extract Data | MuleSoft Documentation

URL Source: https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data

Published Time: Wed, 11 Mar 2026 09:30:46 GMT

Markdown Content:
![Image 1](https://docs.mulesoft.com/_/img/icons/dropdown-arrow.svg)

DataWeave can select data from DataWeave objects and arrays, variables that store that data, and the output of DataWeave functions when that output is an array or object.

More precisely, a DataWeave selector operates within a context, which can be a reference to the variable that stores the data, an object literal, an array literal, or the invocation of a DataWeave function. You can use selectors in Mule modules, connectors, and components that accept DataWeave expressions.

When DataWeave processes a selector, it sets a new context (or scope) for subsequent selectors, so you can navigate through the complex structures of arrays and objects using chains of selectors. The depth of the selection is limited only by the depth of the current context.

Supported variable references are [Mule Runtime variables](https://docs.mulesoft.com/dataweave/latest/dataweave-variables-context), such as `payload` and `attributes`, and [DataWeave variables](https://docs.mulesoft.com/dataweave/latest/dataweave-variables) that store arrays or objects. A simple example is `payload.myKey` where the payload is the object `{"myKey" : 1234 }`, so the result is `1234`.

A selector can act on the invocation of a function, such as the DataWeave `read` function. For example, `read('{"A":"B"}','application/json')."A"` returns `"B"`.

Use Selectors on DataWeave Arrays and Objects
---------------------------------------------

In DataWeave, selectors extract values from within a DataWeave object (such as `{ myKey : "myValue" }`) or array (such as `[1,2,3,4]` or `[ { "myKey" : "1234" }, { "name" : "somebody" } ]`).

The following DataWeave script uses the single-value selector (`.`) to retrieve values from the object and array defined by the variables `myObject` and `myArray`.

DataWeave Script:

```
%dw 2.0
var myObject = { "myKey" : "1234", "name" : "somebody" }
var myArray = [ { "myKey" : "1234" }, { "name" : "somebody" } ]
output application/json
---
{
    selectingValueUsingKeyInObject : myObject.name,
    selectingValueUsingKeyOfObjectInArray : myArray.name,
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex01)

Output JSON:

```
{
    "selectingValueUsingKeyInObject": "somebody",
    "selectingValueUsingKeyOfObjectInArray": [ "somebody" ]
 }
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex01)

As the Output shows:

*   `myObject.name` returns the value `"somebody"`

*   `myArray.name` returns the array `[ "somebody" ]`

Selector Quick Reference
------------------------

Single Value (`.`)
Acts on arrays and objects to return the value of a matching key. The syntax is `.myKey`. To retrieve values of duplicate keys in a DataWeave _object_, use `*`, instead. For examples, see [Single-Value Selector (.myKey)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#single_value).

Multiple Values (`*`)
Acts on arrays and objects to retrieve the values of all matching keys at a single level in the hierarchy of a data structure. The syntax is `*myKey`. For the values of all duplicate keys at lower levels in the hierarchy, use the descendants selector (`..`), instead. For examples, see [Multi-Value Selector (`.*`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#multi_value).

Key-Value Pair (`&`)
Acts on arrays and objects. Instead of returning the value of the DataWeave object, this selector returns the entire DataWeave object, both key and value. The syntax is `.&myKey`. For examples, see [Key-Value Pair Selector (`.&myKey`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#key_value).

Descendants (`..`)
Acts on arrays and objects to retrieve all matching keys from arrays and objects below the given key, regardless of their location in the hierarchy. The syntax is `..myKey` For examples, see [Descendants Selector (`..myKey`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#descendants).

Index (`[]`)
Returns the value at the specified index of an array. An example is the `[0]` at the end of `["a","b","c"][0]`, which returns `"a"`. For examples, see [Index Selector (`[anIndex]`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#index).

Range `[index1 to index2]`
Returns an array with values of the selected indices. An example is the `[2 to 3]` at the end of `["a","b","c","d"][2 to 3]`, which returns `["c","d"]`. For examples, see [Range selector (`anIndex to anotherIndex`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#range).

XML attribute (`.@myKey`)
Returns the value of a selected key for an XML attribute. For an example, see [XML Attribute Selector (`.@myKey`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#xml_attribute).

Namespace Selector (`myKey.#`)
Returns the `xmlns` namespace from the element that also contains the selected key. For an example, see [Namespace Selector (`#`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#namespace).

Selector Modifiers (`?` and `!`)
`?` and `!` check for the specified key. `?` returns `true` or `false`. `!` returns an error if the key is not present. For examples, see [Selector Modifiers (`!`, `?`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#selector_modifiers).

Filter Selectors (`myKey[?(booleanExpression)]`)
Returns the selected items if the Boolean expression returns `true` and the specified `key` is present. It returns `null` if the expression is false or the key is not present. For examples, see [Filter Selectors (`myKey[?($ == "aValue")]`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#filter_selectors).

[](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data) Metadata Selector `.^someMetadata`
Returns the value of specified metadata for a Mule payload, variable, or attribute. The selector can return the value of class (`.^class`), content length (`.^contentLength`), encoding (`.^encoding`), MIME type (`.^mimeType`), media type (`.^mediaType`), raw (`.^raw`), and custom (`.^myCustomMetadata`) metadata. For details, see [Metadata Selector (.^someMetadata)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#metadata_selector).

Key and Selector Syntax
-----------------------

In DataWeave, quotes around the name of an object’s key are required in some cases but optional in others. Though a key is not an identifier, if the key name meets the criteria of a [valid identifier name](https://docs.mulesoft.com/dataweave/latest/dataweave-language-introduction#valid-identifiers), quotes around the key are optional. If the key does not meet this criteria, you _must_ surround the key in quotes. For example, to correct the key syntax in `{ some-name : "somebody" }`, you can use `{ "some-name" : "somebody" }` or `{ 'some-name' : "somebody" }`. Without quotes, the key in `{ some-name : "somebody" }` produces the error `Invalid input '-', expected Namespace`.

If you are using a selector on a key that requires quotes, you must also surround the selector in quotes. For example, the selector `"some-name"` in `{ "some-name" : "somebody" }."some-name"` works, but the selector `some-name` in `{ "some-name" : "somebody" }.some-name` produces the error `Unable to resolve reference of: name` because the selector is not surrounded in quotes.

Quotes around a selector are optional if you are using a selector on a key that does not require the quotes. For example, all of these examples work:

*   `{"name" : "somebody"}.name`

*   `{"name" : "somebody"}."name"`

*   `{name : "somebody"}.name`

*   `{name : "somebody"}."name"`

Single-Value Selector (.myKey)
------------------------------

`.myKey` selectors work over an object or array to return the value of a matching key.

### Single-Value Selector Over an Object

For an object, the single-value selector returns the value of the matching key. For example, in the following script, `myObject.user` returns `"a"`.

DataWeave Script:

```
%dw 2.0
var myObject = { user : "a" }
output application/json
---
{ myObjectExample : myObject.user }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex02)

Output JSON:

```
{
  "myObjectExample": "a"
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex02)

When operating on a DataWeave _object_ (not an array), the `.` selector only returns the value of the _first_ matching key, even if the object contains multiple matching keys, for example:

DataWeave Script:

```
%dw 2.0
var myObject = { user : "a", "user" : "b" }
output application/json
---
{ myObjectExample : myObject.user }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex03)

Output JSON:

```
{
  "myObjectExample": "a"
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex03)

To return the values of multiple matching keys in cases like this, see [Multi-Value Selector (`.*`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#multi_value).

In the next example, `payload.people.person.address` returns the value of the `address` element. (It also uses the `output` directive to transform the JSON input to XML.)

DataWeave Script:

```
%dw 2.0
var myData = {
  "people": {
    "size" : 1,
    "person": {
      "name": "Nial",
      "address": {
        "street": {
          "name": "Italia",
          "number": 2164
        },
        "area": {
          "zone": "San Isidro",
          "name": "Martinez"
        }
      }
    }
  }
}
output application/xml
---
{ myaddresses: myData.people.person.address }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex04)

Expand content

Output XML:

```
<?xml version="1.0" encoding="UTF-8"?>
<myaddresses>
  <street>
    <name>Italia</name>
    <number>2164</number>
  </street>
  <area>
    <zone>San Isidro</zone>
    <name>Martinez</name>
  </area>
</myaddresses>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex04)

Single-Value Selector Over an Array
-----------------------------------

When acting on an array, the `.` selector returns an array, even if there is only one matching value. For example, `["a":"b"]."a"` returns `["b"]`.

Note that the `.` selector acts differently on arrays than it acts on objects. Like `.*`, the `.` selector returns an array with the values of _all matching keys_ at the specified level of the input array.

DataWeave Script:

```
%dw 2.0
var myArrayOfKeyValuePairs = [ "aString": "hello", "aNum": 2, "aString" : "world" ]
var myArrayOfObjects = [ { "aString": "hello" }, { "aNum": 2 }, { "aString" : "world" } ]
output application/json
---
{
    myKeyValueExample : myArrayOfKeyValuePairs.aString,
    myObjectExample :  myArrayOfObjects.aString
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex05)

Output JSON:

```
{
  "myKeyValueExample": [ "hello", "world" ],
  "myObjectExample": [ "hello", "world" ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex05)

In the following example, the value of the input variable, `myData`, is an array that contains two objects. The selector navigates both objects and returns the values of both `street` keys.

DataWeave Script:

```
%dw 2.0
var myData = {
  "people": [
    {
      "person": {
        "name": "Nial",
        "address": {
          "street": {
            "name": "Italia",
            "number": 2164
          },
          "area": {
            "zone": "San Isidro",
            "name": "Martinez"
          }
        }
      }
    },
    {
      "person": {
        "name": "Coty",
        "address": {
          "street": {
            "name": "Monroe",
            "number": 323
          },
          "area": {
            "zone": "BA",
            "name": "Belgrano"
          }
        }
      }
    }
  ]
}
output application/json
---
myData.people.person.address.street
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex06)

Expand content

Output JSON:

```
[
  {
    "name": "Italia",
    "number": 2164
  },
  {
    "name": "Monroe",
    "number": 323
  }
]
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex06)

Multi-Value Selector (`.*`)
---------------------------

`.*` traverses objects and arrays to select the values of all matching keys and returns matching results in an array.

### Multi-Value Selector Over an Object

`.*` returns an array with all the values whose key matches the expression.

The following example returns the values of all `user` elements from the input payload.

DataWeave Script:

```
%dw 2.0
output application/json
---
payload.users.*user
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex07)

Input XML Payload:

```
<users>
  <user>Mariano</user>
  <user>Martin</user>
  <user>Leandro</user>
</users>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex07)

Output JSON:

`[ "Mariano", "Martin", "Leandro" ]`
json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex07)

### Multi-Value Selector Over an Array

On arrays, `.*` works the same way as the single-value selector (`.`). For example, `payload.people.person.address.*street` and the example `payload.people.person.address.street` (from [Single-Value Selector Over an Array](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#single_value_array)) return the same results.

DataWeave Script:

```
%dw 2.0
var myArrayOfKeyValuePairs = [ "aString": "hello", "aNum": 2, "aString" : "world" ]
var myArrayOfObjects = [ { "aString": "hello" }, { "aNum": 2 }, { "aString" : "world" } ]
output application/json
---
{
    myKeyValueExample : myArrayOfKeyValuePairs.*aString,
    myObjectExample :  myArrayOfObjects.*aString
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex08)

Output JSON:

```
{
  "myKeyValueExample": [ "hello", "world" ],
  "myObjectExample": [ "hello", "world" ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex08)

Descendants Selector (`..myKey`)
--------------------------------

The `..` selector acts on arrays and objects.

This selector applies to the context using the form `..myKey`, and it retrieves the values of all matching key-value pairs in the sub-tree under the selected context. Regardless of the hierarchical structure of the fields, the output is returned at the same level.

In this example, all of the fields that match the key `name` are placed in a list called `names` regardless of their cardinality in the tree of the input data.

DataWeave Script:

```
%dw 2.0
output application/json
---
{ names: payload.people..name }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex09)

Input JSON Payload:

```
{
  "people": {
    "person": {
      "name": "Nial",
      "address": {
        "street": {
          "name": "Italia",
          "number": 2164
        },
        "area": {
          "zone": "San Isidro",
          "name": "Martinez"
        }
      }
    }
  }
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex09)

Output JSON:

```
{
  "names": [
    "Nial",
    "Italia",
    "Martinez"
  ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex09)

Key-Value Pair Selector (`.&myKey`)
-----------------------------------

The `&` selector acts on arrays and objects. `&` retrieves both the keys and values of all matching keys pairs in the current context. These are returned as an object, containing the retrieved keys and values.

DataWeave Script:

```
%dw 2.0
output application/xml
---
{
  users: payload.users.&user
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex10)

Input XML Payload:

```
<?xml version='1.0' encoding='US-ASCII'?>
<users>
  <user>Mariano</user>
  <user>Martin</user>
  <user>Leandro</user>
  <admin>Admin</admin>
  <admin>org_owner</admin>
</users>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex10)

Output XML:

```
<?xml version='1.0' encoding='US-ASCII'?>
<users>
  <user>Mariano</user>
  <user>Martin</user>
  <user>Leandro</user>
</users>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex10)

Note that unlike the multi-value selector, the output of this selector is an object, where the original keys for each value are also extracted.

### Select All the Descendant Key-Value Pairs

This example uses the `..` and `&` selectors in `myVar.people..&name` to select and return an array that contains all descendant objects from `myData` input that contain the key `name`. It also transforms the JSON input to XML output.

DataWeave Script:

```
%dw 2.0
var myData = {
  "people": {
    "person": {
      "name": "Nial",
      "address": {
        "street": {
          "name": "Italia",
          "number": 2164
        },
        "area": {
          "zone": "San Isidro",
          "name": "Martinez"
        }
      }
    }
  }
}
output application/xml
---
names: {(myData.people..&name)}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex11)

Expand content

Output XML:

```
<?xml version='1.0' encoding='UTF-8'?>
<names>
  <name>Nial</name>
  <name>Italia</name>
  <name>Martinez</name>
</names>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex11)

Index Selector (`[anIndex]`)
----------------------------

The index selector returns the element at the specified position. It can be applied over an array, object, or string.

### Index Selector Over an Array

This selector can be applied to String literals, Arrays and Objects. In the case of Objects, the value of the key-value pair found at the index is returned. In the case of Arrays, the value of the element is returned. The index is zero-based.

1.   If the index is bigger or equal to 0, it starts counting from the beginning.

2.   If the index is negative, it starts counting from the end where -1 is the last element.

DataWeave Script:

```
%dw 2.0
output application/json
---
payload.people[1]
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex12)

Input JSON Payload:

```
{
  "people": [
        {
          "nameFirst": "Nial",
          "nameLast": "Martinez"
        },
        {
          "nameFirst": "Coty",
          "nameLast": "Belgrano"
        }
    ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex12)

Output JSON:

```
{
  "nameFirst": "Coty",
  "nameLast": "Belgrano"
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex12)

### Index Selector Over an Object

The selector returns the value of the key-value pair at the specified position.

DataWeave Script:

```
%dw 2.0
output application/json
---
payload[1]
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex13)

Input JSON Payload:

```
{
  "nameFirst": "Mark",
  "nameLast": "Nguyen"
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex13)

Output JSON:

`"Nguyen"`
json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex13)

### Index Selector Over a String

When using the Index Selector with a string, the string is broken down into an array, where each character is an index.

DataWeave Script:

```
%dw 2.0
output application/json
---
{ name: "MuleSoft"[0] }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex14)

Output JSON:

`{ "name": "M" }`
json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex14)

The selector picks the character at a given position, treating the string as an array of characters.

1.   If the index is bigger or equal to 0, it starts counting from the beginning.

2.   If the index is negative, it starts counting from the end.

DataWeave Script:

```
%dw 2.0
output application/json
---
{ name: "Emiliano"[0] }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex15)

Output JSON:

`{ "name": "E" }`
json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex15)

Range selector (`anIndex to anotherIndex`)
------------------------------------------

The `to` selector returns values of matching indices in an array or string. You can also use it to reverse the order of the indices in the range. The selector treats characters in the string as indices.

*   Selecting an index from an array:

    *   `[1,2,3,4][0]` returns `1`

The index of the first element in an array is always `0`.

    *   `[1,2,3,4][3]` returns `4`

### Range Selector Over an Array

Range selectors limit the output to only the elements specified by the range on that specific order. This selector allows you to slice an array or even invert it.

DataWeave Script:

```
%dw 2.0
output application/json
---
{
  slice: [0,1,2][0 to 1],
  last: [0,1,2][-1 to 0]
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex16)

Output JSON:

```
{
  "slice": [
    0,
    1
  ],
  "last": [
    2,
    1,
    0
  ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex16)

### Range Selector Over a String

The Range selector limits the output to only the elements specified by the range on that specific order, treating the string as an array of characters. This selector enables you to slice a string or invert it.

DataWeave Script:

```
%dw 2.0
output application/json
---
{
  slice: "DataWeave"[0 to 1],
  middle : "superfragilisticexpialadocious"[10 to 13],
  last: "DataWeave"[-1 to 0]
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex17)

Output JSON:

```
{
  "slice": "Da",
  "middle": "list",
  "last": "evaeWataD"
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex17)

XML Attribute Selector (`.@myKey`)
----------------------------------

`.@myKey` selects an attribute in an XML element.

Using `.@` without the key name returns an object containing the attributes as key-value pairs.

This DataWeave example reads an XML sample into a variable and uses `@` to select attributes from the XML.

DataWeave Script:

```
%dw 2.0
var myVar = read('<product id="1" type="electronic">
  <brand>SomeBrand</brand>
</product>', 'application/xml')
output application/json
---
{
  item: [
  	{
      "type" : myVar.product.@."type",
      "name" : myVar.product.brand,
      "attributes": myVar.product.@
    }
  ]
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex18)

Output JSON:

```
{
  "item": [
    {
      "type": "electronic",
      "name": "SomeBrand",
      "attributes": {
        "id": "1",
        "type": "electronic"
      }
    }
  ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex18)

Namespace Selector (`#`)
------------------------

`#` returns the XML namespace of a selected key as plain text.

DataWeave Script:

```
%dw 2.0
output text/plain
---
payload.order.#
```

dataweave

Input XML Payload:

```
<?xml version="1.0" encoding="UTF-8"?>
<ns0:order xmlns:ns0="http://orders.company.com">
  <name>Mark</name>
  <items>42</items>
  <orderdate>2017-01-04</orderdate>
</ns0:order>
```

xml

Output Text:

`"http://orders.company.com"`
json

Selector Modifiers (`!`, `?`)
-----------------------------

You can check for the presence of a given key.

*   `!` evaluates the selection and fails with an exception message if the key is not present.

*   `?` returns `true` if the selected key is present, `false` if not. Note that `?` is also used in [Filter Selectors (`myKey[?($ == "aValue")]`)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#filter_selectors).

### Assert Present Validator

`!` returns an error if any of the specified key is missing.

*   `{ "name": "Annie" }.lastName!` returns an error with the message, `There is no key named 'lastName'`.

*   Without the `!`, `{ "name": "Annie" }.lastName` returns `null`.

*   When the key is present, `{ "name": "Annie" }.name!` the result is `"Annie"`.

### Key Present Validator

Returns `true` if the specified key is present in the object or as an attribute of an XML element.

This example returns `true` because the `name` key does exists.

DataWeave Script:

```
%dw 2.0
output application/xml
---
present: payload.name?
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex20)

Input JSON Payload:

`{ "name": "Annie" }`
json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex20)

Output XML:

```
<?xml version="1.0" encoding="UTF-8"?>
<present>true</present>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex20)

`?` also works with XML attributes:

DataWeave Script:

```
%dw 2.0
output application/json
---
{
  item: {
    typePresent : payload.product.@."type"?
  }
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex21)

Input XML Payload:

```
<product id="1" type="tv">
  <brand>Samsung</brand>
</product>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex21)

Output JSON:

```
{
  "item": { "typePresent": true }
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex21)

Filter Selectors (`myKey[?($ == "aValue")]`)
--------------------------------------------

`myKey[?($ == "aValue")]` returns only the values of matching keys within an array or object. Note that `?` is also used in [Key Present Validator](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#key_present). If no key-value pairs match, the result is `null`.

The following example inputs the array of `name` keys returned by `*.name`, then checks for `name` keys with the value `"Mariano"`. It filters out any values that do not match. Note that the `$` references the value of the selected key.

DataWeave Script:

```
%dw 2.0
output application/json
---
{ users: payload.users.*name[?($ == "Mariano")] }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex22)

Input XML Payload:

```
<users>
  <name>Mariano</name>
  <name>Luis</name>
  <name>Mariano</name>
</users>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex22)

Output JSON:

```
{
  "users": [
    "Mariano",
    "Mariano"
  ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex22)

The following example assumes the same [input](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#input_filter_selectors) and returns all the key-value pairs of the input because the expression `( 1 == 1 )` is true. Note that a false expression, such as `( 1 == 2 )`, returns `null`.

DataWeave Script:

```
%dw 2.0
output application/json
---
{ users: payload.users.*name[?( 1 == 1)] }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex23)

Input XML Payload:

```
<users>
  <name>Mariano</name>
  <name>Luis</name>
  <name>Mariano</name>
</users>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex23)

Output JSON:

```
{
  "users": [
    "Mariano",
    "Luis",
    "Mariano"
  ]
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex23)

The following example assumes the same [input](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#input_filter_selectors). It uses `mapObject` to iterate over the entire input object and return matching key-value pairs, filtering out any pairs that do not match.

DataWeave Script:

```
%dw 2.0
output application/json
---
payload mapObject { ($$) : $[?($=="Mariano")] }
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex24)

Input XML Payload:

```
<users>
  <name>Mariano</name>
  <name>Luis</name>
  <name>Mariano</name>
</users>
```

xml[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex24)

Output JSON:

```
{
  "users": {
    "name": "Mariano",
    "name": "Mariano"
  }
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex24)

Returns the value of specified metadata for a Mule payload, variable, or attribute. The selector can return the following metadata:

*   Content length metadata: `.^contentLength` returns the content length of the value, if the value is present. For an example, see [Content Length Metadata Selector (.^contentLength)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#caret_contentlength).

*   Class metadata: `.^class` returns the class of the Plain Old Java Object (POJO). For example, `{ "string" : payload.string.^class }` might return `{ "string": "java.lang.String" }` if the input payload defines a Java string, such as `simplePojo.string = "myString"`, in a simple POJO, and `{ "date" : payload.date.^class }` might return `{ "date": "java.util.Date" }`. For an example, see [Class Metadata Selector (.^class)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#caret_class).

*   Encoding metadata: `.^encoding` returns the encoding of a value. For example, `{ "myEncoding" : payload.^encoding }` might return `{"myEncoding": "UTF-8"}` for an input POJO. For an example, see [Encoding Metadata Selector (.^encoding)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#caret_encoding).

*   Media Type Selector: `.^mediaType` returns the MIME type of a value that includes parameters, for example, `application/json;charset=UTF-16`, and the expression in the value of `{ "myMediaType" : payload.^mediaType }` might return `"myMediaType": "/; charset=UTF-8"` for an input POJO. For an example, see [Media Type Metadata Selector (.^mediaType)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#caret_mediatype).

*   MIME Type metadata: `.^mimeType` returns the MIME type (without parameters) of a value, for example, `application/json`, and `{ "myMimeType" : payload.^mimeType }` might return `{ "myMediaType": "/" }` for an input POJO. For an example, see [MIME Type Metadata Selector (.^mimeType)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#caret_mimetype).

*   Raw metadata: `.^raw` returns the underlying data (typically, a binary value) of a plain old Java object (POJO). This selector is sometimes used when calculating an MD5 for hashes when checking for man-in-the-middle attacks. For examples, see [Raw Metadata Selector (.^raw)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#caret_raw).

*   Custom metadata: `.^myCustomMetadata` returns the value of custom metadata. For examples, see [Custom Metadata Selector (.^myCustomMetadata)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data#caret_custom_metadata).

### Content Length Metadata Selector (.^contentLength)

Returns the content length of the value, if the value is present.

In the following Mule app flow, the Logger uses `payload.^contentLength` to select the length of the string `my string`, set in the Set Payload (`set-payload`) component.

Mule App XML in Anypoint Studio:

```
<flow name="setpayloadobjectFlow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="15" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <!-- Set the payload to "my string". -->
  <set-payload value='"my string"' doc:name="Set Payload" />
  <!-- Select the class to which "my string" belongs. -->
  <logger level="INFO" doc:name="Logger" message="#[payload.^contentLength]"/>
</flow>
```

XML

The Studio console output shows that the length of the input string (`my string`) is eleven (`9`) characters long. The length includes the blank space in the string.

Console Output in Anypoint Studio:

```
INFO  2019-05-07 16:59:33,690 [[MuleRuntime].cpuLight.07:
 [carets].caretsFlow.CPU_LITE @39f1dbde]
 [event: 28ce97a0-7124-11e9-acfe-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 11
```

txt

### Class Metadata Selector (.^class)

Returns the class of the Plain Old Java Object (POJO). The value might result from calling a method in a Java class or have a data type (such as `String` or `DateTime`) that DataWeave treats as a Java value, for example:

*   `{ "string" : payload.mystring.^class }` might return `{ "mystring": "java.lang.String" }` if the input payload defines a Java string, such as `simplePojo.string = "myString"`, in a simple POJO.

*   `{ "mydate" : payload.mydate.^class }` might return `{ "mydate": "java.util.Date" }`.

In the following Mule app flow, the Logger uses `payload.^class` to select the Java class of `"my string"`, set in the Set Payload (`set-payload`) component.

Mule App XML in Anypoint Studio:

```
<flow name="setpayloadobjectFlow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="15" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <!-- Set the payload to "my string". -->
  <set-payload value='"my string"' doc:name="Set Payload" />
  <!-- Select the class to which "my string" belongs. -->
  <logger level="INFO" doc:name="Logger" message="#[payload.^class]"/>
</flow>
```

XML

The Studio console output shows that the payload string belongs to the class `java.lang.String`.

Console Output in Anypoint Studio:

```
INFO  2019-04-20 16:10:03,075 [[MuleRuntime].cpuLight.08:
 [setpayloadobject].setpayloadobjectFlow.CPU_LITE @6447187e]
 [event: 6da29400-63c1-11e9-98e0-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 java.lang.String
```

txt

### Encoding Metadata Selector (.^encoding)

Returns the encoding of a value. For example, `{ "myEncoding" : payload.^encoding }` might return `{"myEncoding": "UTF-8"}` for an input POJO.

In the following Mule app flow, the Logger uses `payload.^encoding` to select the encoding of `"my string"`set in the Set Payload (`set-payload`) component. The Scheduler (`scheduler`) component is simply an event source that regularly generates a new Mule event to hold the payload set in Set Payload.

Mule App XML in Anypoint Studio:

```
<flow name="setpayloadobjectFlow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="15" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <!-- Set the payload to "my string". -->
  <set-payload value='"my string"' doc:name="Set Payload" />
  <!-- Select the encoding of "my string". -->
  <logger level="INFO" doc:name="Logger" message="#[payload.^encoding]"/>
</flow>
```

XML

The Studio console output shows that the payload string has `UTF-8` encoding.

Console Output in Anypoint Studio:

```
INFO  2019-04-20 16:14:24,222 [[MuleRuntime].cpuLight.03:
 [setpayloadobject].setpayloadobjectFlow.CPU_LITE @62bea6a6]
 [event: 0938bf70-63c2-11e9-98e0-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 UTF-8
```

txt

### Media Type Metadata Selector (.^mediaType)

Returns the MIME type of a value that includes parameters (for example, `application/json;charset=UTF-16`). The expression in the value of `{ "myMediaType" : payload.^mediaType }` might return `"myMediaType": "/; charset=UTF-8"` for an input POJO.

In the following Mule app flow, the Logger uses `payload.^mediaType` to select the media type of `2014-10-12T11:11:19-00:03` set in the Set Payload (`set-payload`) component.

Mule App XML in Anypoint Studio:

```
<flow name="setpayloadobjectFlow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="15" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <set-payload value='#[|2014-10-12T11:11:19-00:03| as DateTime]' doc:name="Set Payload" />
  <logger level="INFO" doc:name="Logger" message="#[payload.^mediaType]"/>
</flow>
```

XML

The Studio console output shows that the `DateTime` payload has the `application/java; charset=UTF-8` media type.

Console Output in Anypoint Studio:

INFO  2019-04-20 16:41:01,276 [[MuleRuntime].cpuLight.04:
 [setpayloadobject].setpayloadobjectFlow.CPU_LITE @7e991c71]
 [event: c0e96860-63c5-11e9-bcff-8c8590a99d48]
 rg.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 application/java; charset=UTF-8

In the following Mule app flow, the Loggers use `payload.^mediaType` to select a string `"my string"`, then to select a string that is set within an **fx** expression (`#["my string as String type" as String]`) in the Set Payload (`set-payload`) component.

Mule App XML in Anypoint Studio:

```
<flow name="setpayloadobjectFlow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="15" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <!-- Set the payload to "my string". -->
  <set-payload value='"my string"' doc:name="Set Payload" />
  <!-- Select the media type of "my string". -->
  <logger level="INFO" doc:name="Logger" message='#[payload.^mediaType]'/>
  <!-- Set the payload using the fx expression "my string" as String. -->
  <set-payload value='#["my string as String type" as String]' doc:name="Set Payload" />
  <!-- Select the media type of a Java string. -->
  <logger level="INFO" doc:name="Logger" message='#[payload.^mediaType]'/>
</flow>
```

XML

The Studio console output shows that the simple string has the media type `/`, while the string that is set in the **fx** expression has the media type `application/java; charset=UTF-8`.

Console Output in Anypoint Studio:

```
INFO  2019-04-20 16:52:50,801 [[MuleRuntime].cpuLight.01:
 [setpayloadobject].setpayloadobjectFlow.CPU_LITE @5d914abe]
 [event: 68121cd0-63c7-11e9-bcff-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 */*

INFO  2019-04-20 16:52:51,085 [[MuleRuntime].cpuLight.01:
 [setpayloadobject].setpayloadobjectFlow.CPU_LITE @5d914abe]
 [event: 68121cd0-63c7-11e9-bcff-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 application/java; charset=UTF-8
```

txt

### MIME Type Metadata Selector (.^mimeType)

Returns the MIME type (without parameters) of a value, for example, `application/json`, and `{ "myMimeType" : payload.^mimeType }` might return `{ "myMediaType": "/" }` for an input POJO.

In the following Mule app flow, the Loggers use `payload.^mimeType` to select a string `"my string"`, then to select a string that is set within an **fx** expression (`#["my string as String type" as String]`) in the Set Payload (`set-payload`) component.

Mule App XML in Anypoint Studio:

```
<flow name="setpayloadobjectFlow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="15" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <!-- Set the payload to "my string". -->
  <set-payload value='"my string"' doc:name="Set Payload" />
  <!-- Select the MIME type of "my string". -->
  <logger level="INFO" doc:name="Logger" message='#[payload.^mimeType]'/>
  <!-- Set the payload using the fx expression "my string" as String. -->
  <set-payload value='#["my string as String type" as String]' doc:name="Set Payload" />
  <!-- Select the MIME type of a Java string. -->
  <logger level="INFO" doc:name="Logger" message='#[payload.^mimeType]'/>
</flow>
```

XML

The Studio console output shows that the simple string has the MIME type `/`, while the string that is set in the **fx** expression has the MIME type `application/java`.

Console Output in Anypoint Studio:

```
INFO  2019-04-20 17:02:07,762 [[MuleRuntime].cpuLight.06:
 [setpayloadobject].setpayloadobjectFlow.CPU_LITE @2d6f64b9]
 [event: b4097b00-63c8-11e9-bcff-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 */*

INFO  2019-04-20 17:02:08,029 [[MuleRuntime].cpuLight.06:
 [setpayloadobject].setpayloadobjectFlow.CPU_LITE @2d6f64b9]
 [event: b4097b00-63c8-11e9-bcff-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 application/java
```

txt

### Raw Metadata Selector (.^raw)

Returns the underlying binary value of a POJO. This selector is sometimes used when calculating an MD5 or some other cryptographic hash function to check for man-in-the-middle (MITM) attacks.

The following example uses the Set Payload component (`set-payload`) to produce a binary value, then uses the Transform Message component (`ee:transform`) component to return raw data for the MD5 (`MD5(payload.^raw)`) of the binary value. The Logger component (`logger`) is also set to write the raw data to the Studio console. For comparison, the second Logger returns the typical `payload` in a standard JSON format.

Mule App XML in Anypoint Studio:

```
<flow name="rawcaret2Flow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="30" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <set-payload value='#["1234-5678-9123" as Binary]' doc:name="Set Payload" />
  <ee:transform doc:name="Transform Message" >
    <ee:message >
      <ee:set-payload ><![CDATA[%dw 2.0
import * from dw::Crypto
output application/json
---
{ "myRawData" : MD5(payload.^raw) }]]></ee:set-payload>
    </ee:message>
  </ee:transform>
  <logger level="INFO" doc:name="Logger" message="#[payload.^raw]"/>
  <logger level="INFO" doc:name="Logger" message="#[payload]"/>
</flow>
```

XML

Notice that instead of producing standard JSON output, the raw output in the Logger message surrounds the entire payload in double-quotes and inserts new line characters (`\n`) for each new line.

Console Output in Anypoint Studio:

```
INFO  2019-04-22 14:10:14,537 [[MuleRuntime].cpuLight.08:
 [rawcaret2].rawcaret2Flow.CPU_LITE @764a5a61]
 [event: 058f6a90-6543-11e9-9d99-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 "{\n  "myRawData": "5403e5a202c594871d59898b13054be5"\n}"

INFO  2019-04-22 14:10:14,540 [[MuleRuntime].cpuLight.08:
 [rawcaret2].rawcaret2Flow.CPU_LITE @764a5a61]
 [event: 058f6a90-6543-11e9-9d99-8c8590a99d48]
 org.mule.runtime.core.internal.processor.LoggerMessageProcessor:
 { "myRawData": "5403e5a202c594871d59898b13054be5" }
```

txt

The following example uses the HTTP Listener source (`listener`) to get the XML payload received via a POST request, then uses the Transform Message component (`ee:transform`) to get the encoding value of the XML payload, by returning the raw data (`(payload.^raw as String) scan /encoding='([A-z0-9-]+)'/)`). The Logger component (`logger`) returns the `payload` in a JAVA format.

Mule App XML in Anypoint Studio:

```
<http:listener-config name="HTTP_Listener_config" >
    <http:listener-connection host="0.0.0.0" port="8081" />
</http:listener-config>
<flow name="test-flow">
	<http:listener path="/test" config-ref="HTTP_Listener_config"/>
	<ee:transform>
		<ee:message>
		<ee:set-payload ><![CDATA[%dw 2.0
output application/java
---
((payload.^raw as String) scan /encoding='([A-z0-9-]+)'/)[0][1]]]></ee:set-payload>
		</ee:message>
	</ee:transform>
	<logger level="INFO" message="#[payload]"/>
</flow>
```

XML

Using your preferred REST client or API testing tool, send a POST request with the XML body:

```
<?xml version='1.0' encoding='ISO-8859-1'?>
<test>
</test>
```

XML

The Logger message returns the extracted encoding value `ISO-8859-1`:

Console Output in Anypoint Studio:

`INFO  2021-05-12 12:25:41,618 [[MuleRuntime].uber.03: [xmlmodule].Flow.CPU_INTENSIVE @de48fc8] [processor: Flow/processors/2; event: 4fe7f6a0-b336-11eb-909c-f01898ad2638] org.mule.runtime.core.internal.processor.LoggerMessageProcessor: ISO-8859-1`
txt

### Custom Metadata Selector (.^myCustomMetadata)

Returns the value of custom metadata. Metadata can be associated with any value by using the `as` operator.

The following example uses `userName.^myCustomMetadata` to return the value of custom metadata that is defined as a variable (named `userName`) in the header of the script as a DataWeave script. For comparison, the example also returns the value of `userName`.

DataWeave Script:

```
%dw 2.0
output application/json
var userName = "DataWeave" as String {myCustomMetadata: "customMetadataValue"}
---

{
  "valueOfVariableMetaData" :  userName.^myCustomMetadata,
  "valueOfVariable" :  userName,
}
```

dataweave[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex25)

The output of the script is `"customMetadataValue"` for the value of the custom metadata and `"DataWeave"` for value of the `userName` variable.

Output JSON:

```
{
  "valueOfVariableMetaData": "customMetadataValue",
  "valueOfVariable": "DataWeave"
}
```

json[](https://dataweave.mulesoft.com/learn/playground?projectMethod=GHRepo&repo=mulesoft%2Fdocs-dataweave&path=modules%2FROOT%2Fpages%2F_partials%2Fcookbook-dw%2Fextract-data-ex25)
