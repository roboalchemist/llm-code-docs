# Source: https://redocly.com/learn/openapi/openapi-visual-reference/array.md

# `array`

> Arrays are used for ordered elements. In JSON, each element in an array may be of a different type.


## Visuals

The following is an example of an array of vehicles.


```yaml
type: array
items:
  $ref: "#/components/schemas/vehicle"
```


```yaml
components:
  schemas:
    vehicles:
      type: array
      items:
        $ref: "#/components/schemas/vehicle"
    vehicle:
      type: object
      title: Vehicle
      properties:
        color:
          type: object
          title: Color
          properties:
            exterior:
              type: string
              description: The color of the vehicle exterior
              example: red
            trim:
              type: string
              description: The color of the vehicle trim
              example: chrome
            interior:
              type: string
              description: The color of the vehicle interior
              example: tan
        make:
          type: string
          description: The make of the vehicle
          example: Toyota
        model:
          type: string
          description: The model of the vehicle
          example: MR2
        year:
          type: integer
          description: The year of the vehicle
          example: 1995
```

The following image displays that array schema and example object.

![schema and example](/assets/schema-array.586d1f7db0ad137eae1a731a041e154f598c0c9cc1b3200c60e8692eb89a0de3.6f948c6e.png)

## Types

- SchemaProperties



```ts
const SchemaProperties: NodeType = {
  properties: {},
  additionalProperties: 'Schema',
};
```