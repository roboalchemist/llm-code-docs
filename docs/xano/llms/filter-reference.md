# Source: https://docs.xano.com/xanoscript/filter-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XanoScript Filter Reference

> Reference of all the filters available in XanoScript

## Using Filters in XanoScript

Filters in XanoScript are applied right after the target value using a `|` pipe character.

As an example, we have a text string stored in a variable called `x1`. We want to apply a `capitalize` filter to it.

This is what defining the variable would look like in XanoScript.

```javascript  theme={null}
    var x1 {
      value = "hello"
    }
```

When we add the filter, it looks like this.

```javascript  theme={null}
    var x1 {
      value = "hello"|capitalize
    }
```

If a filter has parameters required to use it, we can use `:` characters to add and separate them.

As an example, we'll take our text string and use the `concat` filter to append additional text to it with a separator. `"hello"` will become `"hello, world"`. The `concat` filter asks for two parameters: a value and a separator. We'll use : to separate each parameter.

```javascript  theme={null}
    var x1 {
      value = "hello"|concat:"world":", "
    }
```

You can add multiple filters by separating each one with pipe characters.

```javascript  theme={null}
      value = "hello"|concat:"world":", "|capitalize
```

You can also nest filters. In this example, we're using the `capitalize` filter specifically on `"world"` inside of the `concat` filter.

```javascript  theme={null}
      value = "hello"|concat:"world"|capitalize:", "
```

## Filter Reference

<Card title="Manipulation" href="/xanoscript/filter-reference/manipulation">
   
</Card>

<Card title="Math" href="/xanoscript/filter-reference/math">
   
</Card>

<Card title="Timestamp" href="/xanoscript/filter-reference/timestamp">
   
</Card>

<Card title="Text" href="/xanoscript/filter-reference/text">
   
</Card>

<Card title="Array" href="/xanoscript/filter-reference/array">
   
</Card>

<Card title="Transform" href="/xanoscript/filter-reference/transform">
   
</Card>

<Card title="Comparison" href="/xanoscript/filter-reference/comparison">
   
</Card>

<Card title="Security" href="/xanoscript/filter-reference/security">
   
</Card>


Built with [Mintlify](https://mintlify.com).