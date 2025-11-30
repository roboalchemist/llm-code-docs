# Source: https://www.electronjs.org/docs/latest/api/structures/display

# Display Object

- `accelerometerSupport` string - Can be `available`, `unavailable`, `unknown`.
- `bounds` [Rectangle](/docs/latest/api/structures/rectangle) - the bounds of the display in DIP points.
- `colorDepth` number - The number of bits per pixel.
- `colorSpace` string - represent a color space (three-dimensional object which contains all realizable color combinations) for the purpose of color conversions.
- `depthPerComponent` number - The number of bits per color component.
- `detected` boolean - `true` if the display is detected by the system.
- `displayFrequency` number - The display refresh rate.
- `id` number - Unique identifier associated with the display. A value of of -1 means the display is invalid or the correct `id` is not yet known, and a value of -10 means the display is a virtual display assigned to a unified desktop.
- `internal` boolean - `true` for an internal display and `false` for an external display.
- `label` string - User-friendly label, determined by the platform.
- `maximumCursorSize` [Size](/docs/latest/api/structures/size) - Maximum cursor size in native pixels.
- `nativeOrigin` [Point](/docs/latest/api/structures/point) - Returns the display\'s origin in pixel coordinates. Only available on windowing systems like X11 that position displays in pixel coordinates.
- `rotation` number - Can be 0, 90, 180, 270, represents screen rotation in clock-wise degrees.
- `scaleFactor` number - Output device\'s pixel scale factor.
- `touchSupport` string - Can be `available`, `unavailable`, `unknown`.
- `monochrome` boolean - Whether or not the display is a monochrome display.
- `size` [Size](/docs/latest/api/structures/size)
- `workArea` [Rectangle](/docs/latest/api/structures/rectangle) - the work area of the display in DIP points.
- `workAreaSize` [Size](/docs/latest/api/structures/size) - The size of the work area.

The `Display` object represents a physical display connected to the system. A fake `Display` may exist on a headless system, or a `Display` may correspond to a remote, virtual display.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/display.md)