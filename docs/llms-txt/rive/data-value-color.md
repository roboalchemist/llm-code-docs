# Source: https://uat.rive.app/docs/scripting/api-reference/data-value/data-value-color.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DataValueColor

[DataValue](/scripting/api-reference/data-value/data-value) that stores a color value encoded as a number, with
red, green, blue, and alpha components.

## Fields

### `value`

The full color value encoded as a number.

```lua  theme={null}
local dv: DataValueColor = DataValue.color()
dv.value = Color.rgba(255, 0, 0, 155)
```

### `red`

Color components in the range \[0, 255].

```lua highlight={4,5} theme={null}
local data = DataValue.color()
data.value = Color.rgba(128, 55, 12, 1)

print(data.red) -- 128
data.red = 233
```

### `green`

Color components in the range \[0, 255].

```lua highlight={4,5} theme={null}
local data = DataValue.color()
data.value = Color.rgba(128, 55, 12, 1)

print(data.green) -- 55
data.green = 233
```

### `blue`

Color components in the range \[0, 255].

```lua highlight={4,5} theme={null}
local data = DataValue.color()
data.value = Color.rgba(128, 55, 12, 1)

print(data.blue) -- 12
data.blue = 233
```

### `alpha`

Alpha component in the range \[0, 255].

```lua highlight={4,5} theme={null}
local data = DataValue.color()
data.value = Color.rgba(128, 55, 12, 1)

print(data.alpha) -- 1
data.alpha = 255
```
