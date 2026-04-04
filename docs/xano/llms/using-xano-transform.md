# Source: https://docs.xano.com/xano-transform/using-xano-transform.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Xano Transform

<CardGroup col={3}>
  <Card title="❓ What?" href="/xano-transform/using-xano-transform#what-is-xano-transform">
    Get a quick overview of what Xano Transform can do
  </Card>

  <Card title="🤔 Why?" href="/xano-transform/using-xano-transform#why-xano-transform">
    Explaining the need for something like Xano Transform
  </Card>

  <Card title="🔍 How?" href="/xano-transform/using-xano-transform#how-do-i-use-xano-transform">
    The basics of how to utilize Xano Transform
  </Card>

  <Card title="♾️ Expression Data Type" href="/the-function-stack/data-types/expression">
    Use the Expression data type to quickly build complex expressions
  </Card>

  <Card title="📖 GET Filter" href="/xano-transform/using-xano-transform#retrieval-with-get">
    Xano Transform's GET Filter syntax and examples
  </Card>

  <Card title="🖌️ SET Filter" href="/xano-transform/using-xano-transform#transformation-with-set">
    Xano Transform's SET Filter syntax and examples
  </Card>

  <Card title="💡 Examples" href="/xano-transform/using-xano-transform#examples">
    Real-world examples of Xano Transform in action, with comparisons to other methods
  </Card>
</CardGroup>

## What is Xano Transform?

The Xano Transform Engine is a new technology built by Xano that takes the traditional dot notation syntax and upgrades it to support data manipulation. This syntax is friendly to objects and arrays and supports conditional filtering using the new [Expression data type](/the-function-stack/data-types/expression).

Xano Transform encompasses some updates to our GET and SET filters, allowing you to use a powerful and expansive new type of filtering syntax to parse, return, and transform your data in exactly the way you need. Consider it an alternative to chaining several filters and functions together to accomplish a specific result.

## Why Xano Transform?

Xano is, and will always remain, a No-Code first platform. That doesn't mean that we don't want to offer you more ways to accomplish your goals in the fastest way possible. While this may feel like a leap to "traditional development" methods, at its core, Xano Transform is here to provide both traditional developers a more familiar way to work with their data, and empower the no-code audience to work faster with a specific set of easy to learn syntax.

Xano Transform also offers you an easy way to share solutions with other Xano users by just copying and pasting an expression to them. This is an incredibly helpful tool while we work behind the scenes to offer other methods of function stack portability.

## How do I use Xano Transform?

Xano Transform has two different operating 'modes', as an extension of our GET filter, and a separate [*expression* data type](/the-function-stack/data-types/expression), which all work from utilizing a standardized syntax, outlined in this documentation.

Please note that you can use standard mathematical operators to compare values in areas where they would normally be accepted, such as >, \<, ==, !=, etc...

## The \$\$ special variable

Throughout this documentation, there will be repeated mentions of the `$$` special variable. This is our version of the standard `this` variable, which is commonly used in various programming languages and Lambda filters. This concept is used to represent the context that is being referenced within a function/filter.

<Info>
  In this example, \$\$ represents the expression`1+2+3`
</Info>

```txt  theme={null}
(1+2+3)|transform:$$+1                   // 7
```

One common problem with the `$$/this` variable concept, is what happens when you need to reference 2 or more different versions of it?

```txt  theme={null}
(1+2+3)|transform:$$+(1|transform:$$+1)
```

What if I wanted to reference the first `$$` in the second transform? There isn't a way to do this because the existence of the second transform has taken over the previous value of the \$\$ variable. The solution tends to involve manually creating new variables and assigning them to different copies of the \$\$ variable.

Xano gets around this by having `$$` represent more than just a value - it represents the top most value of anything binded to it.

All \$\$ variables are available via the following syntax. \$0, \$1, \$2 - or $\[0], $\[1], \$\[2], etc. This number keeps increasing as values are bounded to it. This means that the above example could also be written as the following:

```txt  theme={null}
(1+2+3)|transform:$0+(1|transform:$1+1)
```

Therefore, if we needed to access the first \$\$ within the 2nd transform, we could do so by referencing \$\[0].

```txt  theme={null}
(1+2+3)|transform:$$+(1|transform:$$+$0)
```

Sometimes, it is easier to reference items from the top instead of the bottom. Since Xano supports negative indexes, the second item from the top is represented as `-2`. Therefore, we could also use the following syntax using the array notation:

```txt  theme={null}
(1+2+3)|transform:$$+(1|transform:$$+$[-2])
```

## Retrieval with GET

<Frame>
  <iframe width="768" height="432" src="https://www.youtube.com/embed/O-eDey79cWo" title="Xano Transform: GET Filter" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

#### Example Data Payload

```json  theme={null}
{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
	 {"tag":"test","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
	{"tag":"def","weight":90}
      ]
    }
  ]
}
```

<table>
  <thead>
    <tr>
      <th>Syntax</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>v</td>
      <td>`10`</td>
    </tr>

    <tr>
      <td>items</td>

      <td>
        ```json  theme={null}
              [
            {
                "id": 1,
                "name": "s1",
                "score": 100,
                "tags": [
                    {"tag": "beta", "weight": 5},
                    {"tag": "test", "weight": 50}
                ]
            },
            {
                "id": 2,
                "name": "x9",
                "score": 87,
                "tags": [
                    {"tag": "abc", "weight": 10},
                    {"tag": "def", "weight": 90}
                ]
            }
        ]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[0]</td>

      <td>
        ```json  theme={null}
        {
            "id": 1,
            "name": "s1",
            "score": 100,
            "tags": [
                {"tag": "beta", "weight": 5},
                {"tag": "test", "weight": 50}
            ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>items\[0].id</td>
      <td>`1`</td>
    </tr>

    <tr>
      <td>items\[0].tags\[0]</td>
      <td>`{"tag": "beta", "weight": 5}`</td>
    </tr>

    <tr>
      <td>items\[0].tags\[0].tag</td>
      <td>`"beta"`</td>
    </tr>
  </tbody>
</table>

### Array Retrieval

<table>
  <thead>
    <tr>
      <th>Syntax</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>items.id</td>

      <td>
        ```
        [1,2]
        ```
      </td>
    </tr>

    <tr>
      <td>items.tags</td>

      <td>
        ```
        [
          {"tag":"beta","weight":5},
          {"tag":"test","weight":50},
          {"tag":"abc","weight":10},
          {"tag":"def","weight":90}
        ]
        ```
      </td>
    </tr>

    <tr>
      <td>items.tags.tag</td>

      <td>
        ```
        ["beta","test","abc","def"]
        ```
      </td>
    </tr>
  </tbody>
</table>

### Conditional Retrieval

Conditional retrieval is made possible by using the expression syntax within the array brackets of an item.

The `$$` special variable is used to represent the current context of the iterated item of the array.

As seen below, this syntax is supported across multiple levels for deeply nested arrays.

<table>
  <thead>
    <tr>
      <th>Syntax</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>items\[\$\$.id > 1]</td>

      <td>
        ```json  theme={null}
        [{
          "id": 2,
          "name": "x9",
          "score": 87,
          "tags": [
            {"tag":"abc","weight":10},
            {"tag":"def","weight":90}
          ]
        }]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[\$\$.id > 1].id</td>

      <td>
        ```csharp  theme={null}
        [2]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[\$\$.id > 1].tags.tag</td>

      <td>
        ```javascript  theme={null}
        ["abc","def"]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[$.id > 1].tags[$.weight>=90].tag</td>

      <td>
        ```javascript  theme={null}
        ["def"]
        ```
      </td>
    </tr>
  </tbody>
</table>

### Automatic Anchoring

Sometimes you may need to reference something outside of the `$$` special variable. For example, you may want to conditionally select something based on a value that is located in the original root of the object.

This type of reference is supported through automatic anchoring. Each item element of the breadcrumb hierarchy is numerically indexed through `$0`, `$1`, `$2`, `$N` variables.

#### Example: items \[\$\$.id > 1].tags\[\$\$.weight>=90].tag

<Info>
  \$2 and \$4 have multiple values since they represent an array iteration. The example below is just showing the snapshot of one iteration of their value.
</Info>

<table>
  <thead>
    <tr>
      <th>Special Variable</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>\$0</td>

      <td>
        ```json  theme={null}
        {
          "v": 10,
          "items": [
            {
              "id": 1,
              "name": "s1",
              "score": 100,
              "tags": [
                 {"tag":"beta","weight":5},
        	 {"tag":"test","weight":50}
              ]
            },
            {
              "id": 2,
              "name": "x9",
              "score": 87,
              "tags": [
                {"tag":"abc","weight":10},
        	{"tag":"def","weight":90}
              ]
            }
          ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>\$1</td>

      <td>
        ```json  theme={null}
        [
          {
            "id": 1,
            "name": "s1",
            "score": 100,
            "tags": [
              {"tag":"beta","weight":5},
              {"tag":"test","weight":50}
            ]
          },
          {
            "id": 2,
            "name": "x9",
            "score": 87,
            "tags": [
              {"tag":"abc","weight":10},
              {"tag":"def","weight":90}
            ]
          }
        ]
        ```
      </td>
    </tr>

    <tr>
      <td>\$2</td>

      <td>
        ```json  theme={null}
        {
          "id": 2,
          "name": "x9",
          "score": 87,
          "tags": [
            {"tag":"abc","weight":10},
            {"tag":"def","weight":90}
          ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>\$3</td>

      <td>
        ```json  theme={null}
        [
          {"tag":"abc","weight":10},
          {"tag":"def","weight":90}
        ]
        ```
      </td>
    </tr>

    <tr>
      <td>\$4</td>

      <td>
        ```json  theme={null}
        {"tag":"def","weight":90}
        ```
      </td>
    </tr>

    <tr>
      <td>\$5</td>

      <td>
        ```javascript  theme={null}
        "def"
        ```
      </td>
    </tr>
  </tbody>
</table>

<Info>
  The \$\$ special variable is available to be used as a convenience. It always represents the top most numerically indexed special variable that is available within its context.
</Info>

<table>
  <thead>
    <tr>
      <th>Syntax</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>items\[\$\$.id > 1].tags\[\$\$.weight>=90].tag</td>

      <td>
        ```javascript  theme={null}
        ["def"]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[\$2.id > 1].tags\[\$\$.weight>=90].tag</td>

      <td>
        ```javascript  theme={null}
        ["def"]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[\$\$.id > 1].tags\[\$4.weight>=90].tag</td>

      <td>
        ```javascript  theme={null}
        ["def"]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[\$2.id > 1].tags\[\$4.weight>=90].tag</td>

      <td>
        ```javascript  theme={null}
        ["def"]
        ```
      </td>
    </tr>
  </tbody>
</table>

#### Advanced Examples

<table>
  <thead>
    <tr>
      <th>Syntax</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>items\[\$\$.id > 1].tags\[\$\$.weight>=\$0.v].tag</td>

      <td>
        ```javascript  theme={null}
        ["abc","def"]
        ```
      </td>
    </tr>

    <tr>
      <td>items\[\$\$.id > (\[\$0.v,2,3]|max)].id</td>

      <td>
        ```
        []
        ```
      </td>
    </tr>

    <tr>
      <td>items\[\$\$.id > (\[\$0.v,2,3]|min) || \$\$.id == 1].id</td>

      <td>
        ```csharp  theme={null}
        [1,3]
        ```
      </td>
    </tr>
  </tbody>
</table>

## Transformation with SET

In addition to the syntax above for data retrieval, SET supports new syntax for data transformation.

The SET filter leverages the targeting mechanism of the GET filter and allows you to transform the data that is retrieved. It is important to note that after the transformation, the complete object (not just what got changed) is returned. By doing so, it allows for this process to be repeated as many times as you need to complete your transformations.

Below are some examples combining the above syntax with the SET filter.

<Frame>
  <iframe src="https://www.youtube.com/embed/PtxMkxmRNAk" title="Xano Transform: SET Filter" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Multiple SET filters may be required for each transformation.

<table>
  <thead>
    <tr>
      <th>Syntax</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Change the value of "v"<br /><br />**Path**: v <br />**Value**: 50</td>

      <td>
        ```javascript  theme={null}
        {"v": 50,...
        ```
      </td>
    </tr>

    <tr>
      <td>Change the value of all IDs in the items<br /><br />**Path**: items.id <br />**Value**: 99</td>

      <td>
        ```json  theme={null}
        {
          "v": 10,
          "items": [
            {
              "id": 99,
              "name": "s1",
              "score": 100,
              "tags": [
                 {"tag":"beta","weight":5},
        	 {"tag":"test","weight":50}
              ]
            },
            {
              "id": 99,
              "name": "x9",
              "score": 87,
              "tags": [
                {"tag":"abc","weight":10},
        	{"tag":"def","weight":90}
              ]
            }
          ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>Add 1 to all item IDs<br /><br />**Path**: items.id <br />**Value**: \$\$+1</td>

      <td>
        ```json  theme={null}
        {
          "v": 10,
          "items": [
            {
              "id": 2,
              "name": "s1",
              "score": 100,
              "tags": [
                 {"tag":"beta","weight":5},
        	 {"tag":"test","weight":50}
              ]
            },
            {
              "id": 3,
              "name": "x9",
              "score": 87,
              "tags": [
                {"tag":"abc","weight":10},
        	{"tag":"def","weight":90}
              ]
            }
          ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>Uppercase all item tags<br /><br />**Path**: items.tags.tag <br />**Value**: \$\$|to\_upper</td>

      <td>
        ```json  theme={null}
        {
          "v": 10,
          "items": [
            {
              "id": 1,
              "name": "S1",
              "score": 100,
              "tags": [
                 {"tag":"BETA","weight":5},
        	 {"tag":"TEST","weight":50}
              ]
            },
            {
              "id": 2,
              "name": "X9",
              "score": 87,
              "tags": [
                {"tag":"ABC","weight":10},
        	{"tag":"DEF","weight":90}
              ]
            }
          ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>Add the value of an input to each tag weight<br /><br />**Path**: items.tags.weight <br />**Value**: \$input.add+\$\$ <br />**Input**: 500</td>

      <td>
        ```json  theme={null}
        {
          "v": 10,
          "items": [
            {
              "id": 1,
              "name": "S1",
              "score": 100,
              "tags": [
                 {"tag":"BETA","weight":505},
        	 {"tag":"TEST","weight":550}
              ]
            },
            {
              "id": 2,
              "name": "X9",
              "score": 87,
              "tags": [
                {"tag":"ABC","weight":510},
        	{"tag":"DEF","weight":590}
              ]
            }
          ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>Add a new total\_weight key for each item that contains the sum of all tag weights<br /><br />**Path**: items.total\_weight <br />**Value**: \$1.tags.weight|sum</td>

      <td>
        ```json  theme={null}
        {
          "v": 10,
          "items": [
            {
              "id": 1,
              "name": "S1",
              "score": 100,
              "tags": [
                 {"tag":"BETA","weight":5},
        	 {"tag":"TEST","weight":50}
              ],
              "total_weight": 55
            },
            {
              "id": 2,
              "name": "X9",
              "score": 87,
              "tags": [
                {"tag":"ABC","weight":10},
        	{"tag":"DEF","weight":90}
              ],
              "total_weight": 100
            }
          ]
        }
        ```
      </td>
    </tr>
  </tbody>
</table>

## Expression Data Type

The expression data type can be applied to any value input and allows you to perform certain operations on your data when establishing new values. You can also reference other variables and inputs in your expressions which allows for faster data manipulation.

<Frame>
  <iframe src="https://www.youtube.com/embed/xJweDspuVNo" title="Introducing the Expression Data Type" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Please see our full, in-depth documentation on the Expression data type [here](/the-function-stack/data-types/expression).

## Expression Filters

The Xano Transform Engine provides several filters to assist in making transformation easier using the expression syntax. It also includes custom implementations of the [higher order filters](/xano-transform/using-xano-transform#higher-order-filters).

### as

The `as` filter provides a way to dynamically assign a variable to an expression while chaining together filters. This is useful for long or dynamic expressions that need to be referenced more than once.

Arguments

* name - the new variable name

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

#### Examples

```csharp  theme={null}
// initial data
$obj.really.long.ref.company             // foobar, inc https://foo.bar

// without as
$obj.really.long.ref.company|substr:0:($obj.really.long.ref.company|index:http)|trim
// foobar, inc

// with as
$obj.really.long.ref.company|as:C|substr:0:($C|index:http)|trim
// foobar, inc
```

### transform

<Info>
  This filter is similar to the map filter, except it can bind to all data - not just an array.
</Info>

The `transform` filter is universal way to transform data. It works with arrays, objects, and scalar values.

Arguments

* expression - the expression being used to transform `$$`.

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

#### Examples

```powershell  theme={null}
[1,2,3]|transform:($$|count)          // 3
[1,2,3]|transform:($$|count)+($$|sum) // 9

{first:Alpha,last:Beta}|transform:$$.first~" "~$$.last
// Alpha Beta
```

### to\_expr

<Info>
  It is very important to sanitize your data, if you are using this with user generated expressions. This filter provides a way to dynamically reference your variables and use the filters within Xano.
</Info>

The `to_expr` filter is introduces the possibility of dynamic programming. It converts text into an expression.

Arguments (none)

Context Variables (none)

#### Examples

```php  theme={null}
"1+2+3"|to_expr                      // 6

$input.score = 10
"1+2+3+$input.score"|to_expr         // 16
```

### get

<Info>
  See above for a detailed walkthrough of the improvements to the [get filter](/xano-transform/using-xano-transform#retrieval-with-get).
</Info>

### set

<Info>
  See above for a detailed walkthrough of the improvements to the [set filter](/xano-transform/using-xano-transform#transformation-with-set).
</Info>

## Higher Order Filters

These filters resemble their Lambda counterparts, but if used within an Expression, they have a simplified syntax along with their own high performance implementation. All of these have the requirement of binding to an array. There is also a subtle change where the Lambda `$this` variable is represented as the Expression `$$` variable.

### map

<Info>
  This filter binds to an array. If you need to transform an object or scalar value, try the transform filter.
</Info>

The `map` filter is used to do transformations on array elements.

Arguments

* expression - the expression being applied to each iteration of the array

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed

* **\$parent** - the context variable that represents the entire array with all of its elements.

#### Examples

```powershell  theme={null}
[1,2,3]|map:$$+1                      // [2,3,4]
[1,2,3]|map:$$+1+$index               // [2,4,6]
[1,2,3]|map:$$+1+($parent|count)      // [5,6,7]

[{name:foo},{name:bar}]|map:$$.name   // [foo,bar]
```

### some

The `some` filter (also called **has** or **has any element**) returns true, if the conditional expression matches any of the array elements - otherwise, false is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed.

* **\$parent** - the context variable that represents the entire array with all of its elements.

#### Examples

```csharp  theme={null}
[1,2,3]|some:$$==2                    // true
[1,2,3]|some:$$>10                    // false
```

### every

The `every` filter (also called **find every element**) returns true if the conditional expression matches all of the array elements - otherwise, false is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed.

* **\$parent** - the context variable that represents the entire array with all of its elements.

#### Examples

```powershell  theme={null}
[1,2,3]|every:$$>=1 && $$<=3          // true
[1,2,3]|every:$$>10                   // false
```

### find

The `find` filter (also called **find first element**) returns the array item, that first matches the conditional expression - otherwise, null is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed.

* **\$parent** - the context variable that represents the entire array with all of its elements.

Examples

```powershell  theme={null}
[1,2,3]|find:$$==2                    // 2
[1,2,3]|find:$$>1                     // 2

[{name:foo},{name:bar}]|find:($$.name|starts_with:b)
// {name:bar}
```

### findIndex

The `findIndex` filter (also called **find first element index**) returns the index of the array item, that first matches the conditional expression - otherwise, null is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed.

* **\$parent** - the context variable that represents the entire array with all of its elements.

Examples

```powershell  theme={null}
[1,2,3]|findIndex:$$==2               // 1
[1,2,3]|findIndex:$$>1                // 1

[{name:foo},{name:bar}]|findIndex:($$.name|starts_with:b)
// 1
```

### filter

The `filter` filter (also called **find all elements**) returns a new array of items that match the conditional expression.

Arguments

* expression - the expression being applied to each iteration of the array

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed.

* **\$parent** - the context variable that represents the entire array with all of its elements.

Examples

```powershell  theme={null}
[1,2,3]|filter:$$==2                  // [2]
[1,2,3]|filter:$$>1                   // [2,3]
```

### reduce

<Info>
  This also has an optional 2nd argument that represents the initial value. If not specified, it defaults to 0.
</Info>

The reduce filter is a bit more complicated than the other because it has state that changes through each iteration of the array elements. The purpose of this filter is to perform some calculation based on all of the array items. A common example would be summing a list of numbers together one after another.

Arguments

* expression - the expression being applied to each iteration of the array

* initialValue - (optional) the initial value for `$result`. This defaults to 0, if not specified.

Context Variables

* **\$\$** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed.

* **\$parent** - the context variable that represents the entire array with all of its elements.

* **\$result** - the context variable that is used to represent the result of the previous iteration or the initial value on the first iteration.

Examples

```powershell  theme={null}
[1,2,3]|reduce:$$+$result             // 6
[1,2,3]|reduce:$$+$result:10          // 16
```

## Use Cases & Examples

Xano Transform is almost limitless. Some of the most common use cases for Transform are as follows. Please note that this is not an extensive list, and we recommend reading on for more information and examples.

For the sake of these examples, assume we are working with the following data set. You can download the full list of products as CSV or JSON below as well if you want to try these yourself.

<Card href="https://3699875497-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tWsL4o1vHmDGb2UAUDD%2Fuploads%2FnLUFXuOhwfaKSRDCoXd4%2Fproducts-example-json.txt?alt=media&token=2eed77f8-4311-4354-b514-30a35bcf092d">
  products-example-json.txt
</Card>

<Card href="https://3699875497-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tWsL4o1vHmDGb2UAUDD%2Fuploads%2FXo6saDjAHPD6UEnExqUs%2Fproducts-example.csv?alt=media&token=efc341a0-0dc7-4214-a223-81a19dc08a2e">
  products-example.csv
</Card>

```json  theme={null}
{
    result:
            [
                {
                    id: 1,
                    created_at: 1702311936290,
                    title: iPhone 9,
                    description: An apple mobile which is nothing like apple,
                    price: 549,
                    discountPercentage: 12.96,
                    rating: 4.69,
                    stock: 94,
                    brand: Apple,
                    category: smartphones
                },
                {
                    id: 2,
                    created_at: 1702311936290,
                    title: iPhone X,
                    description: SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ...,
                    price: 899,
                    discountPercentage: 17.94,
                    rating: 4.44,
                    stock: 34,
                    brand: Apple,
                    category: smartphones
                },
            ...]
}
```

Using Xano Transform, we could use one or more of the following:

* Find me all of the products with a price greater than \$700

* Find me all of the smartphones that have a rating of at least 4.5 and are less than \$300

* Find me all of the iPhones that have a total price of their returned price + 7.5% to account for tax

These are just a few examples of what Xano Transform could accomplish.

#### Find all products with a price greater than \$700

<Tabs>
  <Tab title="Xano Transform (GET Filter)">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a4e3bd3c-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=ea4200b5fbe1104b582dfac40670c9ea" width="481" height="264" data-path="images/a4e3bd3c-image.jpeg" />
    </Frame>

    ```powershell  theme={null}
    result[$$.price>700]
    ```

    * \*\*result (\*\****Find all products)***

      * Selects something in the JSON, in this case the 'list' key

    * **\[]**

      * Indicates that we want to apply a condition to the selection

    * **\$\$.price** (with a price)

      * Use the value of 'price' as part of the expression

    * **>700** (greater than 700)

      * The expression used to define the data we want returned
  </Tab>

  <Tab title="No-Code">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7bb0f4b1-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=cb21d6585844b0768599a7df89c46edf" width="1244" height="458" data-path="images/7bb0f4b1-image.jpeg" />
    </Frame>

    * **Create Variable**

      * Create a variable to hold our list of qualifying results

    * **For Each Loop**

      * Use a For Each Loop to begin to iterate through the list of data we are working with

      * **Conditional**

        * Check to see if the item we are currently iterating through has a price greater than \$700

        * **Then**

          * If the item qualifies, add it to the variable created before the loop began

        * **Else**

          * Go to the next iteration of the loop
  </Tab>

  <Tab title="High Order Filters">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/17165d60-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=6c239082b85a63cc84361fee72a3a34f" width="1198" height="528" data-path="images/17165d60-image.jpeg" />
    </Frame>

    Using the higher order filter called 'filter', apply the following code:

    ```java  theme={null}
    return $this.price > 700;
    ```
  </Tab>

  <Tab title="Javascript">
    ```javascript  theme={null}
    return $var.products.filter(product => product.price > 700);
    ```
  </Tab>
</Tabs>

#### Find all products with a price greater than \$700 and a rating greater than 4.5

<Tabs>
  <Tab title="Xano Transform (GET Filter)">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f17bb362-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=96a40995a396b049ec3f1a0d75850c11" width="476" height="266" data-path="images/f17bb362-image.jpeg" />
    </Frame>

    ```powershell  theme={null}
    result[$$.price>700 && $$.rating>4.5]
    ```

    * \*\*result (\*\****Find all products)***

      * Selects something in the JSON, in this case the 'list' key

    * **\[]**

      * Indicates that we want to apply a condition to the selection

    * **\$\$.price** (with a price)

      * Use the value of 'price' as part of the expression

    * **>700** (greater than 700)

      * The first part of the expression used to define the data we want returned

    * **&&** (and)

      * Indicate that this expression contains multiple conditions

    * **\$\$.rating** (a rating)

      * Select the 'rating' value as a part of this condition

    * **>4.5** (greater than 4.5)

      * The second part of the expression used to define the data we want returned
  </Tab>

  <Tab title="No-Code">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/934e094b-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=5582281f8d0cf2f059fd85c5bba73d02" width="645" height="250" data-path="images/934e094b-image.jpeg" />
    </Frame>

    * **Create Variable**

      * Create a variable to hold our list of qualifying results

    * **For Each Loop**

      * Use a For Each Loop to begin to iterate through the list of data we are working with

      * **Conditional**

        * Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5

        * **Then**

          * If the item qualifies, add it to the variable created before the loop began

        * **Else**

          * Go to the next iteration of the loop
  </Tab>

  <Tab title="High Order Filters">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7640855d-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=8a6e33225648637509685e82f736d259" width="485" height="270" data-path="images/7640855d-image.jpeg" />
    </Frame>

    Using the higher order filter called 'filter', apply the following code:

    ```java  theme={null}
    return $this.price > 700 && $this.rating > 4.5;
    ```
  </Tab>

  <Tab title="Javascript">
    ```javascript  theme={null}
    return $var.products.filter(product => product.price > 700 && product.rating > 4.5);
    ```
  </Tab>
</Tabs>

#### Find all products with a price greater than \$700 and a rating greater than 4.5, that are in stock

<Tabs>
  <Tab title="Xano Transform (GET Filter)">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/48d2b8f4-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=27bb57c41e3dbc8099582069433c0565" width="481" height="264" data-path="images/48d2b8f4-image.jpeg" />
    </Frame>

    ```powershell  theme={null}
    result[$$.price>700 && $$.rating>4.5 && $$.stock>0]
    ```

    * \*\*result (\*\****Find all products)***

      * Selects something in the JSON, in this case the 'list' key

    * **\[]**

      * Indicates that we want to apply a condition to the selection

    * **\$\$.price** (with a price)

      * Use the value of 'price' as part of the expression

    * **>700** (greater than 700)

      * The first part of the expression used to define the data we want returned

    * **&&** (and)

      * Indicate that this expression contains multiple conditions

    * **\$\$.rating** (a rating)

      * Select the 'rating' value as a part of this condition

    * **>4.5** (greater than 4.5)

      * The second part of the expression used to define the data we want returned

    * \*\*&& \*\*(and)

      * Indicate that this expression contains multiple conditions

    * \*\*\$\$.stock>0 \*\*(that are currently in stock)

      * The third part of the expression used to define the data we want returned
  </Tab>

  <Tab title="No-Code">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/aeaaca8f-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=e1742d28d9a5f4443a14dd108196d5fe" width="761" height="249" data-path="images/aeaaca8f-image.jpeg" />
    </Frame>

    * **Create Variable**

      * Create a variable to hold our list of qualifying results

    * **For Each Loop**

      * Use a For Each Loop to begin to iterate through the list of data we are working with

      * **Conditional**

        * Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5, that also have a stock count greater than 0

        * **Then**

          * If the item qualifies, add it to the variable created before the loop began

        * **Else**

          * Go to the next iteration of the loop
  </Tab>

  <Tab title="High Order Filters">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/aaa96b8c-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=64507191bf286ac161102d71ecc2a7e1" width="480" height="292" data-path="images/aaa96b8c-image.jpeg" />
    </Frame>

    Using the higher order filter called 'filter', apply the following code:

    ```java  theme={null}
    return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
    ```
  </Tab>

  <Tab title="Javascript">
    ```javascript  theme={null}
    return $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);
    ```
  </Tab>
</Tabs>

#### Take the returned list of products and capitalize all product names

<Tabs>
  <Tab title="Xano Transform (SET Filter)">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/572d217d-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=7939a1516afeae327e6099eca2213afa" width="544" height="500" data-path="images/572d217d-image.jpeg" />
    </Frame>

    ```powershell  theme={null}
    Path: name
    Value: $$|to_upper
    ```

    * **Path: name**

      * Set the 'path' option to *name* to indicate this is the key to update

    * **Value: \$\$|to\_upper**

      * **\$\$**

        * Select the current name

      * **|to\_upper**

        * Apply the to\_upper filter
  </Tab>

  <Tab title="No-Code">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8e95f376-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=08a2d4250b27ce4eed263ce07cf24eb1" width="850" height="336" data-path="images/8e95f376-image.jpeg" />
    </Frame>

    * **Create Variable**

      * Create a variable to hold our list of qualifying results

    * **For Each Loop**

      * Use a For Each Loop to begin to iterate through the list of data we are working with

      * **Conditional**

        * Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5, that also have a stock count greater than 0

        * **Then**

          * Update the product's name by applying a to\_upper filter

          * If the item qualifies, add it to the variable created before the loop began

        * **Else**

          * Go to the next iteration of the loop
  </Tab>

  <Tab title="High Order Filters">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6ac6ffbd-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=d3231dc7442ab20b7dfe3d141228bf74" width="538" height="526" data-path="images/6ac6ffbd-image.jpeg" />
    </Frame>

    Using the filter **filter**, apply the following code:

    ```java  theme={null}
    return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
    ```

    Using the filter **map**, apply the following code:

    ```java  theme={null}
    return {
            ...$this,
            name: $this.name.toUpperCase()
        };
    ```
  </Tab>

  <Tab title="Javascript">
    ```javascript  theme={null}
    let filteredProducts = $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);
    let modifiedProducts = filteredProducts.map(product => {
        return {
            ...product,
            name: product.name.toUpperCase()
        };
    });
    return modifiedProducts;
    ```
  </Tab>
</Tabs>

#### Take the returned list of products, capitalize all product names, and conditionally update the price based on the stock value while applying proper price formatting

<Tabs>
  <Tab title="Xano Transform (SET Filter)">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/cc214f05-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=dc34ad5b9934218bc621157b7ff9fbc0" width="550" height="733" data-path="images/cc214f05-image.jpeg" />
    </Frame>

    *To complete this example, you'll want to apply the SET filter for name as described in the previous example.*

    ```powershell  theme={null}
    Path: price
    Value: $1.stock>50 ? ("$"~($$*0.9|number_format:2:.:,)) : ("$"~($$*1.3|number_format:2:.:,))
    ```

    * **Path: price**

      * Set the path option to 'price' to indicate this is the key to update

    * **Value: \$1.stock>50 ? ("\$"\~(\$$\*0.9|number\_format:2:.:,)) : ("\$"\~(\$\$\*1.3|number\_format:2:.:,))**

      * **\$1.stock>50**

        * Use anchored selection to get the stock count and check to see if it is greater than 50

      * **?**

        * Apply a condition based on what the previous portion of the expression returns

      * **If the stock > 50**

        * **("\$"\~**

          * Begin the value with a \$ character

        * **(\$\$\*0.9**

          * Multiply the price by 0.9

        * **|number\_format:2:.:,))**

          * Apply the number\_format filter to format the number as a standard price (2 decimal points, a . decimal separator, and a , thousands seperator)

      * **If the stock \< 50**

        * **("\$"\~**

          * Begin the value with a \$ character

        * **(\$\$\*1.3**

          * Multiply the price by 1.3

        * **|number\_format:2:.:,))**

          * Apply the number\_format filter to format the number as a standard price (2 decimal points, a . decimal separator, and a , thousands seperator)
  </Tab>

  <Tab title="No-Code">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c3be5fb8-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=2a0ca4dcc5faf11777c7d41272571d48" width="876" height="559" data-path="images/c3be5fb8-image.jpeg" />
    </Frame>

    * **Create Variable**

      * Create a variable to hold our list of qualifying results

    * **For Each Loop**

      * Use a For Each Loop to begin to iterate through the list of data we are working with

      * **Conditional**

        * Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5, that also have a stock count greater than 0

        * **Then**

          * Update the product's name by applying a to\_upper filter

          * **Conditional**

            * Check to see if the product stock is greater than 50

              * **Then**

                * Update the product price, multiplying it by 0.9

              * **Else**

                * Update the product price, multiplying it by 1.3

          * Update the product's price and apply the number\_format filter

        * **Else**

          * Go to the next iteration of the loop
  </Tab>

  <Tab title="High Order Filters">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f4997d67-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=60eec7d45daacc68fc1218bd8a265e42" width="543" height="614" data-path="images/f4997d67-image.jpeg" />
    </Frame>

    Using the filter **filter**, apply the following code:

    ```java  theme={null}
    return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
    ```

    Using the filter **map**, apply the following code:

    ```ruby  theme={null}
    return {
        ...$this,
        name: $this.name.toUpperCase(),
        price: $this.stock > 50 
               ? ($this.price * 0.9).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",") 
               : ($this.price * 1.3).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    };
    ```
  </Tab>

  <Tab title="Javascript">
    ```javascript  theme={null}
    let filteredProducts = $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);

    let modifiedProducts = filteredProducts.map(product => {
        let adjustedPrice = product.stock > 50 
                            ? product.price * 0.9 
                            : product.price * 1.3;
        
        return {
            ...product,
            name: product.name.toUpperCase(),
            price: adjustedPrice.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
        };
    });

    return modifiedProducts;
    ```
  </Tab>
</Tabs>

## Troubleshooting

### Text vs Expression

The get and set filters parse the path argument using the [Xano expression](/the-function-stack/data-types/expression) syntax. If you have a path that looks like an expression, but needs to be interpreted as text, then wrap it with brackets and quotes.

Some 3rd party APIs (like Stripe) rely on dot notation arguments being sent as text and then interpreted on their side. In this scenario, it is important to wrap them with the bracket syntax below using double quotation marks.

<Info>
  The [Import cURL](/the-function-stack/functions/apis-and-lambdas/external-api-request) feature has been updated to properly escape all arguments.
</Info>

| AS ARRAY              | AS TEXT                    |
| --------------------- | -------------------------- |
| expand\[0]            | \["expand\[0]"]            |
| line\_item\[0]\[data] | \["line\_item\[0]\[data]"] |


Built with [Mintlify](https://mintlify.com).