# Source: https://www.electronjs.org/docs/latest/api/structures/hid-device

# HIDDevice Object

- `deviceId` string - Unique identifier for the device.
- `name` string - Name of the device.
- `vendorId` Integer - The USB vendor ID.
- `productId` Integer - The USB product ID.
- `serialNumber` string (optional) - The USB device serial number.
- `guid` string (optional) - Unique identifier for the HID interface. A device may have multiple HID interfaces.
- `collections` Object\[\] - an array of report formats. See [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/HIDDevice/collections) for more.
  - `usage` Integer - An integer representing the usage ID component of the HID usage associated with this collection.
  - `usagePage` Integer - An integer representing the usage page component of the HID usage associated with this collection.
  - `type` Integer - An 8-bit value representing the collection type, which describes a different relationship between the grouped items.
  - `children` Object\[\] - An array of sub-collections which takes the same format as a top-level collection.
  - `inputReports` Object\[\] - An array of inputReport items which represent individual input reports described in this collection.
  - `outputReports` Object\[\] - An array of outputReport items which represent individual output reports described in this collection.
  - `featureReports` Object\[\] - An array of featureReport items which represent individual feature reports described in this collection.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/hid-device.md)