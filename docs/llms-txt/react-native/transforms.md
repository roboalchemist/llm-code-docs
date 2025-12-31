# Source: https://reactnative.dev/docs/transforms.md

# Transforms

Transforms are style properties that will help you modify the appearance and position of your components using 2D or 3D transformations. However, once you apply transforms, the layouts remain the same around the transformed component hence it might overlap with the nearby components. You can apply margin to the transformed component, the nearby components or padding to the container to prevent such overlaps.

## Example[​](#example "Direct link to Example")

***

# Reference

## Transform[​](#transform "Direct link to Transform")

`transform` accepts an array of transformation objects or space-separated string values. Each object specifies the property that will be transformed as the key, and the value to use in the transformation. Objects should not be combined. Use a single key/value pair per object.

The rotate transformations require a string so that the transform may be expressed in degrees (deg) or radians (rad). For example:

js

```
{
  transform: [{rotateX: '45deg'}, {rotateZ: '0.785398rad'}],
}
```

The same could also be achieved using a space-separated string:

js

```
{
  transform: 'rotateX(45deg) rotateZ(0.785398rad)',
}
```

The skew transformations require a string so that the transform may be expressed in degrees (deg). For example:

js

```
{
  transform: [{skewX: '45deg'}],
}
```

### Matrix Transform[​](#matrix-transform "Direct link to Matrix Transform")

The `matrix` transform accepts a 4x4 transformation matrix as an array of 16 numbers. This allows you to apply complex transformations that combine translation, rotation, scaling, and skewing in a single operation.

The matrix is specified in column-major order:

js

```
{
  transform: [
    {
      matrix: [
        scaleX,
        skewY,
        0,
        0,
        skewX,
        scaleY,
        0,
        0,
        0,
        0,
        1,
        0,
        translateX,
        translateY,
        0,
        1,
      ],
    },
  ];
}
```

For example, to apply a combination of scale and skew:

js

```
{
  transform: [
    {
      matrix: [
        1, 0.5, 0, 0, 0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
      ],
    },
  ];
}
```

note

Matrix transforms are useful when you need to apply pre-calculated transformation matrices, such as those from animation libraries or when building UI editor applications. For basic transformations, it's recommended to use the individual transform properties (scale, rotate, translate, etc.) as they are more readable.

| Type                                                                                                                                                                                                                                                                                                          | Required |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| array of objects: `{matrix: number[]}`, `{perspective: number}`, `{rotate: string}`, `{rotateX: string}`, `{rotateY: string}`, `{rotateZ: string}`, `{scale: number}`, `{scaleX: number}`, `{scaleY: number}`, `{translateX: number}`, `{translateY: number}`, `{skewX: string}`, `{skewY: string}` or string | No       |

***

### `decomposedMatrix`, `rotation`, `scaleX`, `scaleY`, `transformMatrix`, `translateX`, `translateY`[​](#decomposedmatrix-rotation-scalex-scaley-transformmatrix-translatex-translatey "Direct link to decomposedmatrix-rotation-scalex-scaley-transformmatrix-translatex-translatey")

Deprecated

Use the [`transform`](/docs/transforms.md#transform) prop instead.

## Transform Origin[​](#transform-origin "Direct link to Transform Origin")

The `transformOrigin` property sets the origin for a view's transformations. The transform origin is the point around which a transformation is applied. By default, the origin of a transform is `center`.

# Example

### Values[​](#values "Direct link to Values")

Transform origin supports `px`, `percentage` and keywords `top`, `left`, `right`, `bottom`, `center` values.

The `transformOrigin` property may be specified using one, two, or three values, where each value represents an offset.

#### One-value syntax:[​](#one-value-syntax "Direct link to One-value syntax:")

* The value must be a `px`, a `percentage`, or one of the keywords `left`, `center`, `right`, `top`, and `bottom`.

js

```
{
  transformOrigin: '20px',
  transformOrigin: 'bottom',
}
```

#### Two-value syntax:[​](#two-value-syntax "Direct link to Two-value syntax:")

* First value (x-offset) must be a `px`, a `percentage`, or one of the keywords `left`, `center`, and `right`.
* The second value (y-offset) must be a `px`, a `percentage`, or one of the keywords `top`, `center`, and `bottom`.

js

```
{
  transformOrigin: '10px 2px',
  transformOrigin: 'left top',
  transformOrigin: 'top right',
}
```

#### Three-value syntax:[​](#three-value-syntax "Direct link to Three-value syntax:")

* The first two values are the same as for the two-value syntax.
* The third value (z-offset) must be a `px`. It always represents the Z offset.

js

```
{
  transformOrigin: '2px 30% 10px',
  transformOrigin: 'right bottom 20px',
}
```

#### Array syntax[​](#array-syntax "Direct link to Array syntax")

`transformOrigin` also supports an array syntax. It makes it convenient to use it with Animated APIs. It also avoids string parsing, so should be more efficient.

js

```
{
  // Using numeric values
  transformOrigin: [10, 30, 40],
  // Mixing numeric and percentage values
  transformOrigin: [10, '20%', 0],
}
```

You may refer to MDN's guide on [Transform origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) for additional information.
