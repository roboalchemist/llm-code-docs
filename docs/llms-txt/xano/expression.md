# Source: https://docs.xano.com/the-function-stack/data-types/expression.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Expression

Expressions are a flexible data type that Xano parses in real-time to support an inline syntax to expressing data with mathematical expressions. Anything you can do with Xano filters, can also be done inline within an expression.

When building expressions, make sure you have the 'expression' data type selected. You can also click Use Expression under any value box to quickly switch.

Expression building in Xano leverages auto-complete, which will auto-populate references to inputs and variables, filters, and other common notation.

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/xJweDspuVNo" title="Introducing the Expression Data Type" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

## Using the Expression Editor & Playground

When using the Expression data type, you will be presented with an Expression Editor & Playground to enable easier editing and testing of your expression.

<Tip>
  To get the most value out of the expression editor and playground, make sure to add any variable contents you'd like to use in the Context panel, and make sure to Run & Debug your function stack to enable auto-complete.
</Tip>

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Expression Editor**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7352adb9-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=0fe41b6f14faf9b1571c032c6353a347" width="900" height="1024" data-path="images/7352adb9-image.jpeg" /> | 1. Build and edit your expression here with easy auto-complete<br />2. Test your expression in the playground or apply the changes<br />3. Get quick context for variables accessible by your expression and their data types<br />4. Search the library of transformers (filters) available to use, and see examples of how they work<br />5. Take a quick Expressions tutorial<br />6. Enable new variables to be set to Expression type by default |
| **Playground**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e30198dc-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=089b39a20e4161eaf6385179e7f9743a" width="900" height="1027" data-path="images/e30198dc-image.jpeg" /> | 1) Edit your expression here<br />2) Run and test your expression<br />3) The result of the last executionThe playground also retains access to the transformers (filters) library and the tutorial. You'll need to edit your variable context here if testing with variable data. Just copy and paste the contents into the context panel.                                                                                                           |

## Mathematical Operators

| Operator | Function       | Example    | Result |
| -------- | -------------- | ---------- | ------ |
| +        | addition       | 100 + 101  | 201    |
| -        | subtraction    | 100 - 101  | -1     |
| \*       | multiplication | 100 \* 101 | 10101  |
| /        | division       | 100 / 10   | 10     |

### Operator Precedence

For the most part expressions are evaluated left to right. Using parentheses to illustrate a point, the following would be the same assuming all operators were being evaluated left to right.

```
1 + 2 + 3     == 6
1 + (2 + 3)   == 6
```

However, there are a few operators which get special priority and get evaluated first. These operators are the multiplication and divide operators.

```javascript  theme={null}
1 + 2 * 3    == 7          // if left to right, then 9 (which is incorrect)
1 + (2 * 3)  == 7

1 + 4 / 2    == 3          // if left to right, 2.5 (which is incorrect)
1 + (4 / 2)  == 3
```

## Text Operators

| Operator | Function      | Example | Result |
| -------- | ------------- | ------- | ------ |
| \~       | concatenation | a \~ b  | ab     |

<Info>
  To add separation when concatenating, add an empty string between the values: `a~" "~b`
</Info>

## Array Operators

| Operator | Function                     | Example                 | Result                  |
| -------- | ---------------------------- | ----------------------- | ----------------------- |
| ...      | spread items within an array | \[1,2,3, ...\[4,5,6],7] | \[1,2,3,4,5,6,7]        |
| ..       | range operator               | 1..10                   | \[1,2,3,4,5,6,7,8,9,10] |

## Array Indexes

Expressions have the ability to reference array elements using all integer values (0, positive numbers, and negative numbers). Using a negative number represents starting from the top of the list rather the beginning of the list.

| Expression        | Result |
| ----------------- | ------ |
| \[a,b,c,d,e]\[0]  | a      |
| \[a,b,c,d,e]\[1]  | b      |
| \[a,b,c,d,e]\[-1] | e      |
| \[a,b,c,d,e]\[-2] | d      |

## Object Operators

| Operator | Function                      | Example                      | Result             |
| -------- | ----------------------------- | ---------------------------- | ------------------ |
| ...      | spread items within an object | \{a:1, b:2, ...\{c:3}, d: 4} | \{a:1,b:2,c:3,d:4} |

## Comparison Operators

| Operator | Function                     | Example   | Result |
| -------- | ---------------------------- | --------- | ------ |
| ==       | equals (type conversion)     | 1 == "1"  | true   |
| ===      | strict equals                | 1 === "1" | false  |
| !=       | not equals (type conversion) | 1 != "1"  | false  |
| !==      | strict not equals            | 1 !== "1" | true   |
| >        | greater than                 | 1 > 2     | false  |
| >=       | greater than or equals       | 1 >= 2    | false  |
| \<       | less than                    | 1 \< 2    | true   |
| \<=      | less than or equals          | 1 \<= 2   | true   |

## Logical Operators

| Operator | Function | Example            | Result |
| -------- | -------- | ------------------ | ------ |
| !        | not      | !true              | false  |
| \|\|     | or       | 1 \< 2 \|\| 1 != 1 | true   |
| &&       | and      | 1 \< 2 && 1 != 1   | false  |

<Info>
  All of these operators evaluate their expressions as truthy statements. This means that a comparison operator is not required. For example: 0 || 1 would evaluate to true since 1 evaluates as true.
</Info>

## Conditional Operators

| Operator  | Function                      | Example        | Result |
| --------- | ----------------------------- | -------------- | ------ |
| a ? b : c | ternary (if/else)             | 1 \< 2 ? 3 : 4 | 3      |
| a ?: b    | shorthand ternary (this/that) | 1 ?: 2         | 1      |
| a ?? b    | null coalescing               | null ?? 10     | 10     |

<Info>
  The ternary operator has 2 forms - the traditional if/else based on expression and the shorthand (this/that). The shorthand version will use either the left (this) or the right (that) based on which one evaluates to a truthy statement first going from left to right.
</Info>

<Info>
  The null coalescing operator is very similar to the shorthand ternary, except that instead of relying on a truthy statement, it only checks for the null value.
</Info>

## Variable Syntax

Variables can be referenced using the same [syntax](/working-with-data/lambdas-javascript#special-variables) that is available within Lambdas.

### Variables

Variables within the function stack are accessible through `$var` root variable.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8da55200-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=ff3b61d87f9ba8ef2fc33f1488aad5dd" width="1825" height="712" data-path="images/8da55200-image.jpeg" />
</Frame>

### Inputs

Inputs are accessible through the `$input` root variable.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/59157645-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=30400a2eb46721b00d1b21c8f3e66635" width="1824" height="654" data-path="images/59157645-image.jpeg" />
</Frame>

### Authentication

Authentication values are accessible through the `$auth` root variable.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0242ed6a-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=7fb2322f5ea561640cb6e84303e1cc69" width="1822" height="750" data-path="images/0242ed6a-image.jpeg" />
</Frame>

### Environment Variables

Environment variables are accessible through the `$env` root variable. This includes both system variables (\$remote\_ip, \$datasource, etc.) as well as workspace environment variables.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d4d87cc0-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=fa8a1ca5c83adc406cf027214d272ca2" width="1865" height="734" data-path="images/d4d87cc0-image.jpeg" />
</Frame>

### Auto-Complete

When building expressions, you'll see autocomplete suggestions as you type. This works for variables, inputs, and environment variables, as well as filters.

For variables with nested data, such as objects, you'll also be presented with an auto-complete of the fields inside of that object. In this example, we're targeting a variable called `log`and are presented with the fields inside of that variable by the expression builder, as well as a description of each.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/745e6832-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=d9cdaf8171010d219a25ba7453678266" width="536" height="350" data-path="images/745e6832-image.jpeg" />
</Frame>

## Data Types

The Xano expression engine supports a more relaxed syntax for its data types to make it easier to reference text and variables without the strict requirements of using quotation marks.

| Expression         | Type                        | Result         |
| ------------------ | --------------------------- | -------------- |
| abc                | text                        | "abc"          |
| 123                | integer                     | 123            |
| \$var.score        | integer                     | 123            |
| "\$var.score"      | text                        | "\$var.score"  |
| "\\""              | text with escaped character | "              |
| true               | boolean                     | true           |
| false              | boolean                     | false          |
| "true"             | text                        | "true"         |
| null               | null                        | null           |
| "null"             | text                        | "null"         |
| "123"              | text                        | "123"          |
| \[1,2,3]           | array of integers           | \[1,2,3]       |
| \["1","2","3"]     | array of text               | \["1","2","3"] |
| \[a,b,c]           | array of text               | \["a","b","c"] |
| \["a","b","c"]     | array of text               | \["a","b","c"] |
| \{a:1}             | object                      | \{"a":1}       |
| \{"a":a}           | object                      | \{"a":"a"}     |
| \{"a":\$var.score} | object                      | \{"a":123}     |

## Dot Notation

The same relaxed syntax used for data types also applies to dot notation.

| Dot Notation            | JSON Equivalent         |
| ----------------------- | ----------------------- |
| \$var.items             | \$var.items             |
| \$var.items\[1]         | \$var.items\[1]         |
| \$var.items\["1"]       | \$var.items\["1"]       |
| \$var.items\[a]         | \$var.items\["a"]       |
| \$var.items\[a\~b\~c]   | \$var.items\["abc"]     |
| \$var.items\["a\~b\~c"] | \$var.items\["a\~b\~c"] |

## Filters

All of the Xano filters are available within the expression syntax. To use these, you need to follow the pipe expression syntax.

```
variable | pipe : arg1 : arg2 : argN
```

For example, to uppercase text using the upper filter, you would do the following.

```javascript  theme={null}
"xano"|upper

// result = XANO
```

Here is another example using a filter with an argument.

```csharp  theme={null}
1 + 2 + (3|add:1)

// result = 7
```

<Info>
  This particular example is using both a mathematical "+" and an add filter to illustrate how they can be mixed together.
</Info>

You can also chain filters together.

```csharp  theme={null}
1 + 2 + (3|add:1|mul:2)

// result = 11
```

## Importing Expressions

When importing cURL or pasting JSON into Xano, Xano can automatically detect the Expression data type, provided the expression begins with a \$ character.

As an example, the following JSON...

```php  theme={null}
{"id":"0a1612ca-37d3-4d45-85ad-841a7522e000","created_at":"$test.0.id"}
```

...will import as:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0840184a-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=5925808654e0663846c05406eaccd421" width="718" height="565" data-path="images/0840184a-image.jpeg" />
</Frame>

## Advanced Examples

As showcased above, the Xano expression engine is very powerful. Here we can look into some more advanced use cases that bring everything together.

### Conditional

#### Sample Data

```php  theme={null}
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [4,5,6]
}
```

Expression

```python  theme={null}
($input.scores|max) > ($var.numbers|min)

// result = false
```

### Null coalescing

#### Sample Data

```php  theme={null}
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [4,5,6]
}
```

#### Expression

```php  theme={null}
(($input.scores|merge:[100,101,102])|max)+($var.bad_syntax ?? 100)

// result = 202
```

### Ternary

#### Sample Data

```php  theme={null}
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [0,1,2,3,4,5,6]
}
```

#### Expression

```php  theme={null}
($input.scores[2] == 3 ? 10 : 100) + (($var.numbers|min) ?: $var.numbers|max))

// result = 16
```


Built with [Mintlify](https://mintlify.com).