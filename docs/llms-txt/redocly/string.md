# Source: https://redocly.com/learn/openapi/openapi-visual-reference/string.md

# `string`

> The string type is used for validating strings or text containing Unicode characters.


## Visuals

The following sample schema describes a string.


```yaml
type: string
description: A plain old string.
example: plain old string
```

The following image shows the string schema and corresponding example.

![string schema](/assets/schema-string.a6db30f4bd3401f8b6cc3b67d6cfb8417862a5ac09afadd968b1b6d88851fc08.6f948c6e.png)

### String data formats

#### `date-time`

The following example shows setting the format to `date-time`.


```yaml
type: string
format: date-time
description: A date time format.
```

The following image shows the string with a date-time format and the corresponding auto-generated example.

![string-date-time](/assets/schema-string-date-time.092b860672e1b79d48ffa798a2965dd385d164017d169cd17cbf2e96df261ca9.6f948c6e.png)

The following image shows an object composed of strings with different formats.

#### Common formats

The following example displays an object composed of strings with all of the common string formats.


```yaml
type: object
properties:
  date-time:
    type: string
    format: date-time
    description: With format date-time
  date:
    type: string
    format: date
    description: With format date
  email:
    type: string
    format: email
    description: With format email
  password:
    type: string
    format: password
    description: With format password
  uri:
    type: string
    format: uri
    description: With format uri
  ipv4:
    type: string
    format: ipv4
    description: With format ipv4
  ipv6:
    type: string
    format: ipv6
    description: With format ipv6
  uuid:
    type: string
    format: uuid
    description: With format uuid
```

The following image shows the corresponding schema and auto-generated examples.

![schema string formats](/assets/schema-string-formats.f584a18ee76c306fa110f09261f4280427ba940e950fb35e8f5d6ff2b61e7e68.6f948c6e.png)

## Types

- SchemaProperties



```ts
const SchemaProperties: NodeType = {
  properties: {},
  additionalProperties: 'Schema',
};
```