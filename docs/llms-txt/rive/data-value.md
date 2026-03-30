# Source: https://uat.rive.app/docs/scripting/api-reference/data-value/data-value.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DataValue

Base type for values that can be stored in inputs. Provides
functions for checking the underlying value type.

## Static Functions

### `number`

Creates a [DataValueNumber](/scripting/api-reference/data-value/data-value-number) that stores a number.

```lua  theme={null}
local data = DataValue.number()
data.value = 42

print(data.value) -- 42
```

### `string`

Creates a [DataValueString](/scripting/api-reference/data-value/data-value-string) that stores a string.

```lua  theme={null}
local data = DataValue.string()
data.value = 'Rive for life!'

print(data.value) -- Rive for life!
```

### `boolean`

Creates a [DataValueBoolean](/scripting/api-reference/data-value/data-value-boolean) that stores a boolean.

```lua  theme={null}
local data = DataValue.boolean()
data.value = false

print(data.value) -- false
```

### `color`

Creates a [DataValueColor](/scripting/api-reference/data-value/data-value-color) that stores a [Color](/scripting/api-reference/color/color).

```lua  theme={null}
local data = DataValue.color()
data.value = Color.rgba(128, 55, 12, 128)

print(Color.red(data.value)) -- 255
```

## Methods

### `isNumber`

Returns true if the value is a number.

```lua  theme={null}
local dv: DataValueNumber = DataValue.number()
print(dv.isNumber) -- true
```

### `isString`

Returns true if the value is a string.

```lua  theme={null}
local dv: DataValueNumber = DataValue.number()
print(dv.isString) -- false
```

### `isBoolean`

Returns true if the value is a boolean.

```lua  theme={null}
local dv: DataValueNumber = DataValue.number()
print(dv.isBoolean) -- false
```

### `isColor`

Returns true if the value is a color.

```lua  theme={null}
local dv: DataValueNumber = DataValue.number()
print(dv.isColor) -- false
```
