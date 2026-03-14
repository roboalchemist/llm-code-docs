# Source: https://uat.rive.app/docs/scripting/api-reference/path/path-command.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PathCommand

A PathCommand represents a single drawing instruction inside a Path.
Each command has a type, and a variable number of points depending on that type.

## Fields

### `type`

```lua highlight={5} theme={null}
local path = Path.new()
path:moveTo(Vector.xy(0, 0))
path:lineTo(Vector.xy(10, 0))

for i, command in ipairs(path) do
  print(i, command.type)
end
-- 1 moveTo
-- 2 lineTo
```

See [CommandType](/scripting/api-reference/path/command-type).

## Methods

### `__len`

The number of points varies depending on the command type:

* `moveTo`: 1 point
* `lineTo`: 1 point
* `quadTo`: 2 points
* `cubicTo`: 3 points
* `close`: 0 points

```lua highlight={11} theme={null}
local path = Path.new()
path:moveTo(Vector.xy(0, 0))
path:cubicTo(
  Vector.xy(25, -40),
  Vector.xy(75, 40),
  Vector.xy(100, 0)
)

local command = path[2]
print(command.type)      -- cubicTo
print(#command)          -- 3
```

Returns the number of points stored on this command.

```lua  theme={null}
local count = #command
```
