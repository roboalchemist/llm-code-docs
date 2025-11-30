# Source: https://www.electronjs.org/docs/latest/api/structures/thumbar-button

# ThumbarButton Object

- `icon` [NativeImage](/docs/latest/api/native-image) - The icon showing in thumbnail toolbar.
- `click` Function
- `tooltip` string (optional) - The text of the button\'s tooltip.
- `flags` string\[\] (optional) - Control specific states and behaviors of the button. By default, it is `['enabled']`.

The `flags` is an array that can include following `string`s:

- `enabled` - The button is active and available to the user.
- `disabled` - The button is disabled. It is present, but has a visual state indicating it will not respond to user action.
- `dismissonclick` - When the button is clicked, the thumbnail window closes immediately.
- `nobackground` - Do not draw a button border, use only the image.
- `hidden` - The button is not shown to the user.
- `noninteractive` - The button is enabled but not interactive; no pressed button state is drawn. This value is intended for instances where the button is used in a notification.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/thumbar-button.md)