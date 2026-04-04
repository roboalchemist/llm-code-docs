# Source: https://uat.rive.app/docs/scripting/api-reference/path/path-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PathData

PathData is an indexed collection of [PathCommand](/scripting/api-reference/path/path-command) objects.
Both Path and PathData behave like arrays of commands and support iteration via ipairs.

## Methods

### `__len`

Each entry is a [PathCommand](/scripting/api-reference/path/path-command) describing one segment or action in the path.

```lua  theme={null}
for i, command in ipairs(pathData) do
  print(i, command.type)
end
```

Returns the number of commands in the path.

```lua  theme={null}
local count = #pathData
print(count)
```

### `contours`

Returns a [ContourMeasure](/scripting/api-reference/path/contour-measure) for the first contour in the path. A contour is a
sequence of path segments starting at a `moveTo` and ending before the next
`moveTo` (or end of path). Use the `next` property on the returned
[ContourMeasure](/scripting/api-reference/path/contour-measure) to iterate through subsequent contours. Returns `nil` if the
path has no contours.

```lua  theme={null}
local contour = pathData:contours()
while contour do
  print(contour.length)
  contour = contour.next
end
```

### `measure`

Returns a [PathMeasure](/scripting/api-reference/path/path-measure) that measures the entire path across all contours.
This provides the total length and allows operations on the path as a whole.

```lua  theme={null}
local measure = pathData:measure()
print(measure.length)
```
