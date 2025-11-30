# Source: https://www.electronjs.org/docs/latest/api/structures/notification-action

On this page

# NotificationAction Object

- `type` string - The type of action, can be `button`.
- `text` string (optional) - The label for the given action.

## Platform / Action Support[â€‹](#platform--action-support "Direct link to Platform / Action Support") 

Action Type

Platform Support

Usage of `text`

Default `text`

Limitations

`button`

macOS

Used as the label for the button

\"Show\" (or a localized string by system default if first of such `button`, otherwise empty)

Only the first one is used. If multiple are provided, those beyond the first will be listed as additional actions (displayed when mouse active over the action button). Any such action also is incompatible with `hasReply` and will be ignored if `hasReply` is `true`.

### Button support on macOS[â€‹](#button-support-on-macos "Direct link to Button support on macOS") 

In order for extra notification buttons to work on macOS your app must meet the following criteria.

- App is signed
- App has it\'s `NSUserNotificationAlertStyle` set to `alert` in the `Info.plist`.

If either of these requirements are not met the button won\'t appear.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/notification-action.md)