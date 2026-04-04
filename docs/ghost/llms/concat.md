# Source: https://docs.ghost.org/themes/helpers/utility/concat.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# concat

> Usage: `{{concat "a" "b" "c"}}`

***

The `{{concat}}` helper is designed to concatenate and link multiple things together.

The `{{concat}}` helper will take all of the items passed to it, treat them as strings, and concatenate them together without any spaces. There can be an unlimited amount of items passed to the helper.

Strings, variables and other helpers can be passed into the `{{concat}}` helper.

## Simple examples

```handlebars  theme={"dark"}
{{concat "hello world" "!" }}

Outputs:

hello world!
```

```handlebars  theme={"dark"}
{{concat "my-class" slug }}

Outputs:

my-classmy-post
```

`{{concat}}` is designed for strings. If an object is passed it will output `[object Object]` in true JavaScript™️ fashion. To make it error proof, if `{{concat}}` is passed an empty variable, the output will be an empty string.

## The separator attribute

By default, strings are concatenated together with nothing in between them. The `separator=""` attribute inserts the value provided between each string.

### Separator example

```handlebars  theme={"dark"}
{{concat "hello" "world" separator=" "}}

Outputs:

hello world
```


Built with [Mintlify](https://mintlify.com).