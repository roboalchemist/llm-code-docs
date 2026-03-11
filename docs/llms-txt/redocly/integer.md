# Source: https://redocly.com/learn/openapi/openapi-visual-reference/integer.md

# `integer`

> The `integer` type is used for integral numbers. JSON does not have distinct types for integers and floating-point values. Therefore, the presence or absence of a decimal point is not enough to distinguish between integers and non-integers. For example,`1` and `1.0` are two ways to represent the same value in JSON. JSON Schema considers that value an integer no matter which representation was used.


## Visuals

The following is an example of an integer type of property.


```yaml
age:
  type: integer
  description: Years since birth
  example: 16
```


```yaml
components:
  schemas:
    age:
      type: integer
      description: Years since birth
      example: 16
```

The following image displays that age schema.

![schema integer](/assets/schema-integer.d5492ad800867f408fc99c41669dbe9a99fe40d104a0faaed2a4ff66ee4d3136.6f948c6e.png)

Integers can be included inside of objects and arrays.
The following example shows an integer included in an object.


```yaml
type: object
properties:
  age:
    type: integer
    description: Years since birth
    example: 16
```

The following image displays that schema.

![schema integer in object](/assets/schema-integer-in-object.d68649e92ac4e0b0b016e47d92d3c7dba8fed4b36816981fbf0a342562cc04bf.6f948c6e.png)

### Integer data formats

There are two OAS-supported integer formats: `int32` (signed 32 bits), and `int64` (signed 64 bits).


```yaml
type: object
properties:
  age:
    type: integer
    title: age
    description: Years since birth
  population:
    type: integer
    description: The number of people in the world.
    format: int32
  particles:
    type: integer
    description: Number of particles in the universe.
    format: int64
```

![schema integer format](/assets/schema-integer-format.54fdcb1bab9fb6f9f993893fdcac463b14fb8318c85b1652b50e9d42d8fc4e4f.6f948c6e.png)

## Types

- SchemaProperties



```ts
const SchemaProperties: NodeType = {
  properties: {},
  additionalProperties: 'Schema',
};
```